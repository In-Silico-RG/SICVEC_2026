import csv
import hmac
import io
import os
import secrets
from datetime import datetime
from functools import wraps

from flask import (Flask, Response, abort, flash, g, redirect, render_template, request,
                   send_from_directory, session, url_for)

from . import content, i18n, logic
from .config import CO, load_config
from .db import close_db, get_db, init_db
from .mailer import requeue_pending, send_email


def now():
    return datetime.now(CO)


def create_app(overrides=None):
    app = Flask(__name__)
    app.config.update(load_config(overrides))
    if not app.config["SECRET_KEY"]:
        app.config["SECRET_KEY"] = secrets.token_hex(32)  # sessions reset on restart; set SECRET_KEY in production
    init_db(app)
    requeue_pending(app)
    app.teardown_appcontext(close_db)

    # ---------- security helpers ----------
    def csrf_token():
        if "_csrf" not in session:
            session["_csrf"] = secrets.token_hex(16)
        return session["_csrf"]

    @app.before_request
    def check_csrf():
        if request.method == "POST":
            sent = request.form.get("_csrf", "")
            if not sent or not hmac.compare_digest(sent, session.get("_csrf", "")):
                abort(400, "Formulario caducado o inválido. Recargue la página.")

    # ---------- interface language (es/en/pt): ?lang= sets a cookie; otherwise cookie, then browser, then Spanish ----------
    @app.before_request
    def pick_lang():
        asked = request.args.get("lang")
        if asked in i18n.LANGS:
            g.lang, g.set_lang = asked, True
        else:
            cookie = request.cookies.get("lang")
            g.lang = cookie if cookie in i18n.LANGS else (request.accept_languages.best_match(i18n.LANGS) or "es")
            g.set_lang = False

    @app.after_request
    def remember_lang(resp):
        if getattr(g, "set_lang", False):
            resp.set_cookie("lang", g.lang, max_age=180 * 86400, samesite="Lax",
                            secure=app.config.get("SESSION_COOKIE_SECURE", False))
        return resp

    # Stylesheet version = its modification time, so browsers fetch the new CSS after each redeploy (AC, 2026-09-30:
    # the footer showed the UNISUCRE logo at full size because a cached old style.css had no rule for it).
    css_version = int(os.path.getmtime(os.path.join(app.static_folder, "style.css")))

    @app.context_processor
    def lang_context():
        lang = getattr(g, "lang", "es")
        return dict(lang=lang, LANGS=i18n.LANGS, LANG_NAMES=i18n.LANG_NAMES, C=content.for_lang(lang), CSS_V=css_version,
                    t=lambda key, **kw: i18n.html(key, lang, **kw),
                    axis_label=lambda a: i18n.axis_label(a, lang),
                    modality_label=lambda k: i18n.modality_label(k, lang),
                    category_label=lambda k: i18n.category_label(k, lang))

    def tr(key, **kw):
        return i18n.plain(key, getattr(g, "lang", "es"), **kw)

    @app.after_request
    def headers(resp):
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("X-Frame-Options", "DENY")
        resp.headers.setdefault("Referrer-Policy", "same-origin")
        resp.headers.setdefault("Content-Security-Policy", "default-src 'self'; style-src 'self'")
        return resp

    def admin_required(view):
        @wraps(view)
        def wrapped(*a, **kw):
            pw = app.config["ADMIN_PASSWORD"]
            if not pw:
                abort(503, "Panel deshabilitado: falta ADMIN_PASSWORD.")
            auth = request.authorization
            if not auth or auth.username != "admin" or not hmac.compare_digest(auth.password or "", pw):
                return Response("Acceso restringido", 401, {"WWW-Authenticate": 'Basic realm="SICVEC admin"'})
            return view(*a, **kw)
        return wrapped

    app.jinja_env.globals.update(csrf_token=csrf_token, AXES=logic.AXES, MODALITIES=logic.MODALITIES,
                                 CATEGORIES=logic.CATEGORIES, CRITERIA=logic.CRITERIA,
                                 RECOMMENDATIONS=logic.RECOMMENDATIONS, WORD_LIMITS=logic.WORD_LIMITS,
                                 fee_for=lambda c, a: logic.fee_for(app.config["FEES"], c, a),
                                 config=app.config, now=now, content=content)

    @app.template_filter("fecha")
    def fecha(dt):
        return dt.strftime("%d/%m/%Y %H:%M") if hasattr(dt, "strftime") else dt

    @app.template_filter("cop")
    def cop(n):
        return f"{n:,}".replace(",", ".")

    def ref_for(prefix, n):
        return f"{prefix}-{n:03d}"

    # ---------- public ----------
    @app.get("/")
    def index():
        return render_template("index.html", ejes=list(zip(logic.AXES, content.for_lang(g.lang).EJES_TOPICOS)))

    @app.get("/programa")
    def programa():
        return render_template("programa.html")

    @app.get("/conferencistas")
    def conferencistas():
        return render_template("conferencistas.html")

    @app.route("/enviar", methods=["GET", "POST"])
    def submit():
        cfg = app.config
        if now() > cfg["SUBMISSION_DEADLINE"]:
            return render_template("closed.html", when=cfg["SUBMISSION_DEADLINE"]), 403
        errors, f = [], request.form
        if request.method == "POST":
            get = lambda k: f.get(k, "").strip()
            email, title, abstract = get("email"), get("title"), get("abstract")
            modality, language = get("modality"), get("language")
            presentation, axis = get("presentation"), get("axis")
            keywords = [k.strip() for k in get("keywords").split(",") if k.strip()]
            if not logic.valid_email(email):
                errors.append(tr("e_email"))
            if not title or len(title) > 200:
                errors.append(tr("e_title"))
            if language not in ("es", "en", "pt"):
                errors.append(tr("e_lang"))
            if modality not in logic.MODALITIES:
                errors.append(tr("e_modality"))
            if presentation not in ("presencial", "virtual"):
                errors.append(tr("e_presentation"))
            if axis not in logic.AXES:
                errors.append(tr("e_axis"))
            if not 3 <= len(keywords) <= 5:
                errors.append(tr("e_keywords"))
            wc = logic.word_count(abstract)
            limit = logic.WORD_LIMITS.get(modality)
            if not abstract:
                errors.append(tr("e_abstract"))
            elif limit and wc > limit:
                errors.append(tr("e_words", wc=wc, limit=limit))
            for field, label in (("author_name", "n_name"), ("author_institution", "n_institution"),
                                 ("author_program", "n_program"), ("author_country", "n_country")):
                if not get(field):
                    errors.append(tr("e_presenter", label=tr(label)))
            other = get("other_authors")
            if len([l for l in other.splitlines() if l.strip()]) > 4:
                errors.append(tr("e_authors"))
            if not f.get("consent"):
                errors.append(tr("e_consent"))
            if not f.get("originality"):
                errors.append(tr("e_orig"))
            if not errors:
                names = logic.author_names_from(get("author_name"), other)
                flags = logic.blind_flags(abstract, names, email)
                shown_flags = logic.blind_flags(abstract, names, email, msg=lambda k, **kw: tr(k, **kw))
                status = "revision_manual" if flags else "admisible"
                db = get_db()
                try:
                    cur = db.execute(
                        """INSERT INTO submissions(created_at,email,title,language,modality,presentation,axis,
                           abstract,keywords,word_count,author_name,author_institution,author_program,
                           author_country,other_authors,consent,status,flags,ui_lang)
                           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (now().isoformat(timespec="seconds"), email, title, language, modality, presentation,
                         axis, abstract, ", ".join(keywords), wc, get("author_name"),
                         get("author_institution"), get("author_program"), get("author_country"),
                         other, 1, status, " | ".join(flags), g.lang))
                except Exception:
                    db.rollback()
                    errors.append(tr("e_dup_sub"))
                else:
                    ref = ref_for("SICVEC", cur.lastrowid)
                    db.execute("UPDATE submissions SET ref=? WHERE id=?", (ref, cur.lastrowid))
                    db.commit()
                    send_email(app, db, email, tr("m_sub_subject", ref=ref),
                               tr("m_sub_body", title=title, ref=ref,
                                  close=f"{cfg['SUBMISSION_DEADLINE']:%d/%m/%Y %H:%M}"))
                    return render_template("submit_ok.html", ref=ref, flags=shown_flags)
        return render_template("submit.html", errors=errors, f=f)

    def save_receipt(file):
        if not file or not file.filename:
            return ""
        ext = os.path.splitext(file.filename)[1].lower()
        head = file.stream.read(8)
        file.stream.seek(0)
        ok = {".pdf": head.startswith(b"%PDF"), ".png": head.startswith(b"\x89PNG"),
              ".jpg": head[:3] == b"\xff\xd8\xff", ".jpeg": head[:3] == b"\xff\xd8\xff"}
        if not ok.get(ext):
            raise ValueError(tr("e_receipt"))
        name = secrets.token_hex(16) + ext
        file.save(os.path.join(app.config["UPLOAD_DIR"], name))
        return name

    @app.route("/inscripcion", methods=["GET", "POST"])
    def register():
        cfg, errors, f = app.config, [], request.form
        if request.method == "POST":
            get = lambda k: f.get(k, "").strip()
            cat, att, email = get("category"), get("attendance"), get("email")
            for field, label in (("name", "n_name"), ("phone", "n_phone"), ("document", "n_document"),
                                 ("institution", "n_institution"), ("country", "n_country")):
                if not get(field):
                    errors.append(tr("e_missing", label=tr(label)))
            if not logic.valid_email(email):
                errors.append(tr("e_email2"))
            if cat not in logic.CATEGORIES:
                errors.append(tr("e_category"))
            if att not in ("presencial", "virtual"):
                errors.append(tr("e_presentation"))
            if cat == "virtual" and att != "virtual":
                errors.append(tr("e_catvirtual"))
            if not f.get("consent"):
                errors.append(tr("e_consent"))
            db = get_db()
            if att == "virtual" and cfg["ONLINE_SEATS"] is not None:
                used = db.execute("SELECT COUNT(*) FROM registrations WHERE attendance='virtual'").fetchone()[0]
                if used >= cfg["ONLINE_SEATS"]:
                    errors.append(tr("e_seats"))
            receipt = ""
            if not errors:
                try:
                    receipt = save_receipt(request.files.get("receipt"))
                except ValueError as exc:
                    errors.append(str(exc))
            if not errors:
                try:
                    cur = db.execute(
                        """INSERT INTO registrations(created_at,name,email,phone,document,institution,country,
                           category,attendance,presents,submission_ref,payment_ref,receipt_file,consent,ui_lang)
                           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (now().isoformat(timespec="seconds"), get("name"), email, get("phone"), get("document"),
                         get("institution"), get("country"), cat, att, 1 if f.get("presents") else 0,
                         get("submission_ref"), get("payment_ref"), receipt, 1, g.lang))
                except Exception:
                    db.rollback()
                    errors.append(tr("e_dup_reg"))
                else:
                    ref = ref_for("REG", cur.lastrowid)
                    db.execute("UPDATE registrations SET ref=? WHERE id=?", (ref, cur.lastrowid))
                    db.commit()
                    fee = logic.fee_for(cfg["FEES"], cat, att)
                    send_email(app, db, email, tr("m_reg_subject", ref=ref),
                               tr("m_reg_body", ref=ref, fee=f"{fee:,}".replace(",", "."),
                                  date=f"{cfg['PAYMENT_DEADLINE']:%d/%m/%Y}"))
                    return render_template("register_ok.html", ref=ref, fee=fee)
        return render_template("register.html", errors=errors, f=f)

    # ---------- reviewers (private link, no account) ----------
    def reviewer_or_404(token):
        r = get_db().execute("SELECT * FROM reviewers WHERE token=?", (token,)).fetchone()
        if not r:
            abort(404)
        return r

    @app.get("/revisor/<token>")
    def reviewer_home(token):
        r = reviewer_or_404(token)
        rows = get_db().execute(
            """SELECT a.id AS aid, s.ref, s.title, rv.id AS done
               FROM assignments a JOIN submissions s ON s.id=a.submission_id
               LEFT JOIN reviews rv ON rv.assignment_id=a.id
               WHERE a.reviewer_id=? ORDER BY s.id""", (r["id"],)).fetchall()
        return render_template("reviewer_home.html", r=r, rows=rows)

    @app.route("/revisor/<token>/<int:aid>", methods=["GET", "POST"])
    def review(token, aid):
        r = reviewer_or_404(token)
        db = get_db()
        # Blind review: only these columns are ever read here. No author fields.
        a = db.execute(
            """SELECT a.id AS aid, s.ref, s.title, s.axis, s.modality, s.keywords, s.abstract, s.language
               FROM assignments a JOIN submissions s ON s.id=a.submission_id
               WHERE a.id=? AND a.reviewer_id=?""", (aid, r["id"])).fetchone()
        if not a:
            abort(404)
        mine = db.execute("SELECT * FROM reviews WHERE assignment_id=?", (aid,)).fetchone()
        closed = now() > app.config["REVIEW_DEADLINE"]
        errors = []
        if request.method == "POST":
            if closed:
                abort(403, "El plazo de evaluación terminó.")
            try:
                scores = {k: int(request.form.get("s_" + k, "0")) for k, _l, _w in logic.CRITERIA}
                weighted = logic.weighted_score(scores)
            except ValueError:
                errors.append("Califique los cinco criterios de 1 a 5.")
            rec = request.form.get("recommendation", "")
            comments = request.form.get("comments", "").strip()
            if rec not in logic.RECOMMENDATIONS:
                errors.append("Elija una recomendación.")
            if not comments:
                errors.append("Escriba comentarios para los autores.")
            if not all(request.form.get(c) for c in ("c_conf", "c_coi", "c_obj")):
                errors.append("Debe aceptar las tres declaraciones de confidencialidad y conflicto de interés.")
            if not errors:
                db.execute(
                    """INSERT INTO reviews(assignment_id,s_relevance,s_originality,s_quality,s_clarity,s_impact,
                       weighted,comments,recommendation,submitted_at) VALUES (?,?,?,?,?,?,?,?,?,?)
                       ON CONFLICT(assignment_id) DO UPDATE SET s_relevance=excluded.s_relevance,
                       s_originality=excluded.s_originality, s_quality=excluded.s_quality,
                       s_clarity=excluded.s_clarity, s_impact=excluded.s_impact, weighted=excluded.weighted,
                       comments=excluded.comments, recommendation=excluded.recommendation,
                       submitted_at=excluded.submitted_at""",
                    (aid, scores["relevance"], scores["originality"], scores["quality"], scores["clarity"],
                     scores["impact"], weighted, comments, rec, now().isoformat(timespec="seconds")))
                db.commit()
                flash("Evaluación registrada. Gracias.")
                return redirect(url_for("reviewer_home", token=token))
        return render_template("review.html", r=r, a=a, mine=mine, closed=closed, errors=errors)

    # ---------- admin ----------
    @app.get("/admin")
    @admin_required
    def admin_home():
        db = get_db()
        c = lambda q: db.execute(q).fetchone()[0]
        stats = {
            "resúmenes": c("SELECT COUNT(*) FROM submissions"),
            "para revisión manual": c("SELECT COUNT(*) FROM submissions WHERE status='revision_manual'"),
            "revisores": c("SELECT COUNT(*) FROM reviewers"),
            "asignaciones": c("SELECT COUNT(*) FROM assignments"),
            "evaluaciones recibidas": c("SELECT COUNT(*) FROM reviews"),
            "con decisión": c("SELECT COUNT(*) FROM submissions WHERE decision IS NOT NULL"),
            "decisiones sin notificar": c("SELECT COUNT(*) FROM submissions WHERE decision IS NOT NULL AND notified_at IS NULL"),
            "inscripciones": c("SELECT COUNT(*) FROM registrations"),
            "inscripciones pagadas": c("SELECT COUNT(*) FROM registrations WHERE paid=1"),
        }
        return render_template("admin_home.html", stats=stats, smtp=bool(app.config["SMTP_HOST"]),
                               consent_pending="PENDIENTE" in app.config["CONSENT_TEXT"] + app.config["INSTITUTION_DATA"])

    @app.get("/admin/resumenes")
    @admin_required
    def admin_submissions():
        rows = get_db().execute(
            """SELECT s.*, (SELECT COUNT(*) FROM assignments a WHERE a.submission_id=s.id) AS n_assign,
               (SELECT COUNT(*) FROM assignments a JOIN reviews r ON r.assignment_id=a.id
                WHERE a.submission_id=s.id) AS n_reviews FROM submissions s ORDER BY s.id""").fetchall()
        return render_template("admin_submissions.html", rows=rows)

    @app.get("/admin/resumenes/<int:sid>")
    @admin_required
    def admin_submission(sid):
        db = get_db()
        s = db.execute("SELECT * FROM submissions WHERE id=?", (sid,)).fetchone()
        if not s:
            abort(404)
        revs = db.execute(
            """SELECT rv.*, r.name AS reviewer FROM assignments a JOIN reviewers r ON r.id=a.reviewer_id
               LEFT JOIN reviews rv ON rv.assignment_id=a.id WHERE a.submission_id=?""", (sid,)).fetchall()
        done = [dict(weighted=x["weighted"], recommendation=x["recommendation"]) for x in revs if x["weighted"] is not None]
        suggestion, note = logic.suggest_decision(done)
        return render_template("admin_submission.html", s=s, revs=revs, suggestion=suggestion, note=note)

    @app.post("/admin/resumenes/<int:sid>/estado")
    @admin_required
    def admin_status(sid):
        status = request.form.get("status")
        if status not in ("admisible", "no_admisible", "revision_manual"):
            abort(400)
        db = get_db()
        db.execute("UPDATE submissions SET status=? WHERE id=?", (status, sid))
        db.commit()
        return redirect(url_for("admin_submission", sid=sid))

    @app.post("/admin/resumenes/<int:sid>/decision")
    @admin_required
    def admin_decision(sid):
        dec = request.form.get("decision")
        if dec not in logic.RECOMMENDATIONS:
            abort(400)
        db = get_db()
        db.execute("UPDATE submissions SET decision=?, decision_note=?, decided_at=?, notified_at=NULL WHERE id=?",
                   (dec, request.form.get("note", "").strip(), now().isoformat(timespec="seconds"), sid))
        db.commit()
        return redirect(url_for("admin_submission", sid=sid))

    @app.route("/admin/revisores", methods=["GET", "POST"])
    @admin_required
    def admin_reviewers():
        db = get_db()
        if request.method == "POST":
            name, email = request.form.get("name", "").strip(), request.form.get("email", "").strip()
            if name and logic.valid_email(email):
                try:
                    db.execute("INSERT INTO reviewers(name,email,token,created_at) VALUES (?,?,?,?)",
                               (name, email, secrets.token_urlsafe(24), now().isoformat(timespec="seconds")))
                    db.commit()
                except Exception:
                    db.rollback()
                    flash("Ese correo ya está registrado como revisor.")
            else:
                flash("Nombre y correo válido son obligatorios.")
            return redirect(url_for("admin_reviewers"))
        rows = db.execute("SELECT r.*, (SELECT COUNT(*) FROM assignments a WHERE a.reviewer_id=r.id) AS n "
                          "FROM reviewers r ORDER BY r.id").fetchall()
        return render_template("admin_reviewers.html", rows=rows)

    @app.post("/admin/revisores/<int:rid>/invitar")
    @admin_required
    def admin_invite(rid):
        db = get_db()
        r = db.execute("SELECT * FROM reviewers WHERE id=?", (rid,)).fetchone()
        if not r:
            abort(404)
        link = f"{app.config['BASE_URL']}/revisor/{r['token']}"
        send_email(app, db, r["email"], "SICVEC 2026 — invitación como revisor/a",
                   f"Estimado/a {r['name']}:\n\nSu enlace personal para evaluar los resúmenes asignados "
                   f"(no lo comparta):\n{link}\n\nPlazo: {app.config['REVIEW_DEADLINE']:%d/%m/%Y} (hora Colombia).")
        flash("Invitación registrada en el buzón de correos.")
        return redirect(url_for("admin_reviewers"))

    @app.post("/admin/asignar")
    @admin_required
    def admin_assign():
        db = get_db()
        subs = [dict(id=s["id"], email=s["email"],
                     authors_text=s["author_name"] + "\n" + s["other_authors"])
                for s in db.execute("SELECT * FROM submissions WHERE status='admisible'")]
        revs = [dict(r) for r in db.execute("SELECT id,name,email FROM reviewers")]
        existing = {(a["submission_id"], a["reviewer_id"]) for a in db.execute("SELECT * FROM assignments")}
        new, short = logic.plan_assignments(subs, revs, existing)
        db.executemany("INSERT INTO assignments(submission_id,reviewer_id) VALUES (?,?)", new)
        db.commit()
        flash(f"{len(new)} asignaciones nuevas." + (f" Sin revisores suficientes: resúmenes {short}." if short else ""))
        return redirect(url_for("admin_home"))

    @app.post("/admin/notificar")
    @admin_required
    def admin_notify():
        db = get_db()
        rows = db.execute("SELECT * FROM submissions WHERE decision IS NOT NULL AND notified_at IS NULL").fetchall()
        for s in rows:
            comments = [c["comments"] for c in db.execute(
                """SELECT rv.comments FROM assignments a JOIN reviews rv ON rv.assignment_id=a.id
                   WHERE a.submission_id=?""", (s["id"],))]
            L = s["ui_lang"] if s["ui_lang"] in i18n.LANGS else "es"   # the language the author used on the site
            body = i18n.plain("m_dec_result", L, title=s["title"], ref=s["ref"],
                              decision=i18n.decision_label(s["decision"], L)) + "\n\n"
            if s["decision_note"]:
                body += i18n.plain("m_dec_note", L, note=s["decision_note"]) + "\n\n"
            if comments:
                body += i18n.plain("m_dec_comments", L) + "\n" + "\n".join(f"- {c}" for c in comments) + "\n\n"
            body += i18n.plain("m_dec_final", L)
            send_email(app, db, s["email"], i18n.plain("m_dec_subject", L, ref=s["ref"]), body)
            db.execute("UPDATE submissions SET notified_at=? WHERE id=?", (now().isoformat(timespec="seconds"), s["id"]))
        db.commit()
        flash(f"{len(rows)} notificaciones procesadas.")
        return redirect(url_for("admin_home"))

    @app.get("/admin/inscripciones")
    @admin_required
    def admin_registrations():
        rows = get_db().execute("SELECT * FROM registrations ORDER BY id").fetchall()
        return render_template("admin_registrations.html", rows=rows, fees=app.config["FEES"])

    @app.post("/admin/inscripciones/<int:rid>/pago")
    @admin_required
    def admin_paid(rid):
        db = get_db()
        db.execute("UPDATE registrations SET paid = 1 - paid WHERE id=?", (rid,))
        db.commit()
        return redirect(url_for("admin_registrations"))

    @app.get("/admin/recibo/<int:rid>")
    @admin_required
    def admin_receipt(rid):
        r = get_db().execute("SELECT receipt_file FROM registrations WHERE id=?", (rid,)).fetchone()
        if not r or not r["receipt_file"]:
            abort(404)
        return send_from_directory(os.path.abspath(app.config["UPLOAD_DIR"]), r["receipt_file"])

    @app.get("/admin/correos")
    @admin_required
    def admin_emails():
        rows = get_db().execute("SELECT * FROM emails ORDER BY id DESC LIMIT 200").fetchall()
        return render_template("admin_emails.html", rows=rows)

    @app.get("/admin/exportar/<name>.csv")
    @admin_required
    def admin_export(name):
        queries = {
            "resumenes": "SELECT ref,created_at,email,title,language,modality,presentation,axis,keywords,word_count,"
                         "author_name,author_institution,author_program,author_country,other_authors,status,flags,"
                         "decision,decision_note,notified_at FROM submissions ORDER BY id",
            "inscripciones": "SELECT ref,created_at,name,email,phone,document,institution,country,category,attendance,"
                             "presents,submission_ref,payment_ref,paid FROM registrations ORDER BY id",
            "evaluaciones": "SELECT s.ref,r.name AS reviewer,rv.s_relevance,rv.s_originality,rv.s_quality,rv.s_clarity,"
                            "rv.s_impact,rv.weighted,rv.recommendation,rv.comments,rv.submitted_at FROM reviews rv "
                            "JOIN assignments a ON a.id=rv.assignment_id JOIN submissions s ON s.id=a.submission_id "
                            "JOIN reviewers r ON r.id=a.reviewer_id ORDER BY s.id",
        }
        if name not in queries:
            abort(404)
        cur = get_db().execute(queries[name])
        out = io.StringIO()
        w = csv.writer(out)
        w.writerow([d[0] for d in cur.description])
        for row in cur:
            w.writerow([logic.csv_safe(v) for v in row])
        return Response("﻿" + out.getvalue(), mimetype="text/csv",
                        headers={"Content-Disposition": f"attachment; filename=sicvec_{name}.csv"})

    @app.get("/admin/basededatos")
    @admin_required
    def admin_database():
        db_path = os.path.abspath(app.config["DATABASE"])
        get_db().execute("PRAGMA wal_checkpoint(TRUNCATE)")  # flush WAL so the file on disk is complete
        stamp = now().strftime("%Y%m%d_%H%M")
        return send_from_directory(os.path.dirname(db_path), os.path.basename(db_path),
                                    as_attachment=True, download_name=f"sicvec_{stamp}.sqlite")

    return app
