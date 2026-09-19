import smtplib
from datetime import datetime
from email.message import EmailMessage
from .config import CO


def send_email(app, db, to_addr, subject, body):
    """Log every email. Send through SMTP when configured; otherwise mark it 'simulado' (nothing leaves the server)."""
    now = datetime.now(CO).isoformat(timespec="seconds")
    status, error = "simulado", ""
    if "\n" in to_addr or "\r" in to_addr or "\n" in subject or "\r" in subject:
        status, error = "error", "header injection blocked"
    elif app.config["SMTP_HOST"]:
        try:
            msg = EmailMessage()
            msg["From"], msg["To"], msg["Subject"] = app.config["MAIL_FROM"], to_addr, subject
            msg.set_content(body)
            with smtplib.SMTP(app.config["SMTP_HOST"], app.config["SMTP_PORT"], timeout=15) as s:
                s.starttls()
                if app.config["SMTP_USER"]:
                    s.login(app.config["SMTP_USER"], app.config["SMTP_PASSWORD"])
                s.send_message(msg)
            status = "enviado"
        except Exception as exc:  # a mail failure must never break the request
            status, error = "error", str(exc)[:300]
    db.execute("INSERT INTO emails(created_at,to_addr,subject,body,status,error) VALUES (?,?,?,?,?,?)",
               (now, to_addr, subject, body, status, error))
    db.commit()
    return status
