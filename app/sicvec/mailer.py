import queue
import smtplib
import sqlite3
import threading
from datetime import datetime
from email.message import EmailMessage
from .config import CO

# SMTP delivery runs in one background thread per process, so a slow mail server never holds a request.
# A row is claimed ('pendiente' -> 'enviando') before sending, so two gunicorn workers never send the same email.
_queue = queue.Queue()
_worker_lock = threading.Lock()
_worker = None


def send_email(app, db, to_addr, subject, body):
    """Log every email. Queue it for SMTP when configured; otherwise mark it 'simulado' (nothing leaves the server)."""
    now = datetime.now(CO).isoformat(timespec="seconds")
    status, error = "simulado", ""
    if "\n" in to_addr or "\r" in to_addr or "\n" in subject or "\r" in subject:
        status, error = "error", "header injection blocked"
    elif app.config["SMTP_HOST"]:
        status = "pendiente"
    cur = db.execute("INSERT INTO emails(created_at,to_addr,subject,body,status,error) VALUES (?,?,?,?,?,?)",
                     (now, to_addr, subject, body, status, error))
    db.commit()
    if status == "pendiente":
        _start_worker(app)
        _queue.put(cur.lastrowid)
    return status


def requeue_pending(app):
    """At startup, queue emails left 'pendiente' by a previous process (the claim prevents double sends)."""
    if not app.config["SMTP_HOST"]:
        return
    con = _connect(app)
    try:
        ids = [r[0] for r in con.execute("SELECT id FROM emails WHERE status='pendiente' ORDER BY id")]
    finally:
        con.close()
    if ids:
        _start_worker(app)
        for i in ids:
            _queue.put(i)


def _connect(app):
    con = sqlite3.connect(app.config["DATABASE"], timeout=10)
    con.row_factory = sqlite3.Row
    return con


def _start_worker(app):
    global _worker
    with _worker_lock:
        if _worker is None or not _worker.is_alive():
            _worker = threading.Thread(target=_run, args=(app,), name="sicvec-mailer", daemon=True)
            _worker.start()


def _run(app):
    while True:
        email_id = _queue.get()
        try:
            _deliver(app, email_id)
        except Exception:  # never let one email kill the worker
            pass
        finally:
            _queue.task_done()


def _deliver(app, email_id):
    con = _connect(app)
    try:
        cur = con.execute("UPDATE emails SET status='enviando' WHERE id=? AND status='pendiente'", (email_id,))
        con.commit()
        if cur.rowcount != 1:
            return  # already claimed by another process
        row = con.execute("SELECT to_addr, subject, body FROM emails WHERE id=?", (email_id,)).fetchone()
        status, error = "enviado", ""
        try:
            msg = EmailMessage()
            msg["From"], msg["To"], msg["Subject"] = app.config["MAIL_FROM"], row["to_addr"], row["subject"]
            msg.set_content(row["body"])
            with smtplib.SMTP(app.config["SMTP_HOST"], app.config["SMTP_PORT"], timeout=15) as s:
                s.starttls()
                if app.config["SMTP_USER"]:
                    s.login(app.config["SMTP_USER"], app.config["SMTP_PASSWORD"])
                s.send_message(msg)
        except Exception as exc:
            status, error = "error", str(exc)[:300]
        con.execute("UPDATE emails SET status=?, error=? WHERE id=?", (status, error, email_id))
        con.commit()
    finally:
        con.close()
