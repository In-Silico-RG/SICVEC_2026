import re
from datetime import datetime, timedelta

import pytest

from sicvec import create_app
from sicvec.config import CO

ADMIN = ("admin", "pw-test")


@pytest.fixture
def app(tmp_path):
    return create_app({"TESTING": True, "DATABASE": str(tmp_path / "t.sqlite"), "UPLOAD_DIR": str(tmp_path / "up"),
                       "ADMIN_PASSWORD": "pw-test", "SECRET_KEY": "k"})


@pytest.fixture
def client(app):
    return app.test_client()


def token(client, path="/enviar"):
    html = client.get(path).get_data(as_text=True)
    return re.search(r'name="_csrf" value="([^"]+)"', html).group(1)


def auth():
    import base64
    return {"Authorization": "Basic " + base64.b64encode(b"admin:pw-test").decode()}


def submission_data(client, **over):
    d = dict(_csrf=token(client), email="ana@uni.co", title="Pirólisis de lignina", language="es",
             modality="oral", presentation="presencial", axis="Química Verde y Procesos Sostenibles",
             abstract="Se estudió la conversión térmica de lignina técnica en bio-aceite.",
             keywords="lignina, pirólisis, bio-aceite", author_name="Ana Pérez", author_institution="UNISUCRE",
             author_program="Química", author_country="Colombia", other_authors="", consent="1", originality="1")
    d.update(over)
    return d


def test_submit_ok_sends_confirmation(client, app):
    r = client.post("/enviar", data=submission_data(client))
    assert r.status_code == 200 and b"SICVEC-001" in r.data
    with app.app_context():
        from sicvec.db import get_db
        m = get_db().execute("SELECT * FROM emails").fetchone()
        assert m["to_addr"] == "ana@uni.co" and m["status"] == "simulado"


def test_submit_rejects_over_word_limit(client):
    r = client.post("/enviar", data=submission_data(client, modality="poster", abstract="palabra " * 251))
    assert b"251 palabras" in r.data and b"SICVEC-001" not in r.data


def test_submit_requires_csrf(client):
    d = submission_data(client)
    d["_csrf"] = "bad"
    assert client.post("/enviar", data=d).status_code == 400


def test_submit_closed_after_deadline(tmp_path):
    past = datetime.now(CO) - timedelta(minutes=1)
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "t.sqlite"), "UPLOAD_DIR": str(tmp_path / "u"),
                      "SUBMISSION_DEADLINE": past, "SECRET_KEY": "k"})
    assert app.test_client().get("/enviar").status_code == 403


def test_duplicate_submission_rejected(client):
    client.post("/enviar", data=submission_data(client))
    r = client.post("/enviar", data=submission_data(client))
    assert b"Ya existe" in r.data


def test_blind_flag_sends_to_manual_review(client, app):
    client.post("/enviar", data=submission_data(client, abstract="Trabajo de Ana Pérez sobre lignina."))
    with app.app_context():
        from sicvec.db import get_db
        assert get_db().execute("SELECT status FROM submissions").fetchone()[0] == "revision_manual"


def test_admin_requires_password(client, app):
    assert client.get("/admin").status_code == 401
    assert client.get("/admin", headers=auth()).status_code == 200
    app.config["ADMIN_PASSWORD"] = ""
    assert client.get("/admin", headers=auth()).status_code == 503


def add_reviewers(client, n=2):
    for i in range(n):
        client.post("/admin/revisores", headers=auth(),
                    data={"_csrf": token(client, "/enviar"), "name": f"Revisor {i}", "email": f"r{i}@x.co"})


def test_full_flow_blind_review_and_decision(client, app):
    client.post("/enviar", data=submission_data(client))
    add_reviewers(client, 2)
    r = client.post("/admin/asignar", headers=auth(), data={"_csrf": token(client)})
    assert r.status_code == 302
    with app.app_context():
        from sicvec.db import get_db
        db = get_db()
        assert db.execute("SELECT COUNT(*) FROM assignments").fetchone()[0] == 2
        toks = [x["token"] for x in db.execute("SELECT token FROM reviewers ORDER BY id")]
        aids = [x["id"] for x in db.execute("SELECT id FROM assignments ORDER BY id")]
    page = client.get(f"/revisor/{toks[0]}/{aids[0]}").get_data(as_text=True)
    assert "Pirólisis de lignina" in page and "conversión térmica" in page
    for leak in ("Ana Pérez", "ana@uni.co", "UNISUCRE"):
        assert leak not in page, f"blind review leaked {leak}"
    for t, a in zip(toks, aids):
        form = {"_csrf": token(client), "comments": "Buen trabajo", "recommendation": "aceptado",
                "c_conf": "1", "c_coi": "1", "c_obj": "1",
                **{f"s_{k}": "4" for k in ("relevance", "originality", "quality", "clarity", "impact")}}
        assert client.post(f"/revisor/{t}/{a}", data=form).status_code == 302
    detail = client.get("/admin/resumenes/1", headers=auth()).get_data(as_text=True)
    assert "Aceptado" in detail and "4.0" in detail
    client.post("/admin/resumenes/1/decision", headers=auth(),
                data={"_csrf": token(client), "decision": "aceptado", "note": ""})
    client.post("/admin/notificar", headers=auth(), data={"_csrf": token(client)})
    with app.app_context():
        from sicvec.db import get_db
        db = get_db()
        assert db.execute("SELECT notified_at FROM submissions").fetchone()[0] is not None
        body = db.execute("SELECT body FROM emails WHERE subject LIKE '%resultado%'").fetchone()[0]
        assert "Buen trabajo" in body and "Aceptado" in body


def test_reviewer_cannot_open_other_assignment(client, app):
    client.post("/enviar", data=submission_data(client))
    add_reviewers(client, 2)
    client.post("/admin/asignar", headers=auth(), data={"_csrf": token(client)})
    assert client.get("/revisor/token-inexistente").status_code == 404
    with app.app_context():
        from sicvec.db import get_db
        t = get_db().execute("SELECT token FROM reviewers WHERE id=1").fetchone()[0]
    assert client.get(f"/revisor/{t}/999").status_code == 404


def test_registration_and_receipt_validation(client):
    base = dict(_csrf=token(client, "/inscripcion"), name="Luis", email="l@x.co", phone="300", document="CC 1",
                institution="UNISUCRE", country="Colombia", category="pregrado", attendance="presencial", consent="1")
    from io import BytesIO
    bad = dict(base, receipt=(BytesIO(b"MZ not a pdf"), "x.pdf"))
    assert b"PDF, PNG o JPG" in client.post("/inscripcion", data=bad, content_type="multipart/form-data").data
    good = dict(base, receipt=(BytesIO(b"%PDF-1.4 ok"), "x.pdf"))
    r = client.post("/inscripcion", data=good, content_type="multipart/form-data")
    assert b"REG-001" in r.data and b"15.000" in r.data


def test_online_seat_cap(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "t.sqlite"), "UPLOAD_DIR": str(tmp_path / "u"),
                      "ONLINE_SEATS": 1, "SECRET_KEY": "k"})
    c = app.test_client()
    def go(email):
        d = dict(_csrf=token(c, "/inscripcion"), name="N", email=email, phone="1", document="1",
                 institution="I", country="C", category="virtual", attendance="virtual", consent="1")
        return c.post("/inscripcion", data=d)
    assert b"REG-001" in go("a@x.co").data
    assert "agotados".encode() in go("b@x.co").data


def test_export_csv_neutralizes_formulas(client):
    client.post("/enviar", data=submission_data(client, title="=HYPERLINK(1)"))
    csv_text = client.get("/admin/exportar/resumenes.csv", headers=auth()).get_data(as_text=True)
    assert "'=HYPERLINK(1)" in csv_text


def test_virtual_attendance_is_free_and_in_person_pays(client):
    def reg(email, cat, att):
        d = dict(_csrf=token(client, "/inscripcion"), name="N", email=email, phone="1", document="1",
                 institution="I", country="C", category=cat, attendance=att, consent="1")
        return client.post("/inscripcion", data=d).get_data(as_text=True)
    assert "COP 0" in reg("a@x.co", "posgrado", "virtual")
    assert "30.000" in reg("b@x.co", "posgrado", "presencial")


def test_no_online_seat_cap_by_default(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "t.sqlite"), "UPLOAD_DIR": str(tmp_path / "u"), "SECRET_KEY": "k"})
    assert app.config["ONLINE_SEATS"] is None


def test_public_info_pages(client):
    home = client.get("/").get_data(as_text=True)
    for needle in ("Ejes temáticos", "ODS 12", "Pregrado: COP 15.000", "Participación en línea gratuita", "Centro Comercial Guacarí", "Calle 28 No. 25B-97", "google.com/maps"):
        assert needle in home
    prog = client.get("/programa").get_data(as_text=True)
    assert "Programa preliminar" in prog and "Lunes 19 de octubre" in prog and "Martes 20 de octubre" in prog
    conf = client.get("/conferencistas").get_data(as_text=True)
    assert "Beatriz Escobar Morales" in conf and "sargazo holopelágico" in conf
    assert client.get("/static/speaker_escobar.jpg").status_code == 200
    assert "Wilson Manuel Castro Silupu" in conf and "Medicinal plant discrimination" in conf
    assert client.get("/static/speaker_castro.jpg").status_code == 200
    assert "Marianny Y. Combariza" in conf and "Título de la conferencia: por confirmar" in conf


def test_footer_has_coordinators_email(client):
    home = client.get("/").get_data(as_text=True)
    assert home.count("mailto:insilico@unisucre.edu.co") >= 2   # coordination column + contact column
    assert "María Ximena Díaz" in home and "Selena Arias Avila" in home


def test_home_names_the_venue_room(client):
    assert "sala de conferencias del Centro Comercial Guacarí" in client.get("/").get_data(as_text=True)


def test_smtp_sent_in_background(tmp_path, monkeypatch):
    import sqlite3
    import time
    from sicvec import mailer
    sent = []

    class FakeSMTP:
        def __init__(self, *a, **k): pass
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def starttls(self): pass
        def login(self, *a): pass
        def send_message(self, msg): sent.append(msg["To"])

    monkeypatch.setattr(mailer.smtplib, "SMTP", FakeSMTP)
    db_path = str(tmp_path / "s.sqlite")
    app = create_app({"TESTING": True, "DATABASE": db_path, "UPLOAD_DIR": str(tmp_path / "up"),
                      "ADMIN_PASSWORD": "pw-test", "SECRET_KEY": "k", "SMTP_HOST": "smtp.test", "MAIL_FROM": "x@y.co"})
    c = app.test_client()
    assert c.post("/enviar", data=submission_data(c)).status_code == 200
    mailer._queue.join()
    con = sqlite3.connect(db_path)
    assert con.execute("PRAGMA journal_mode").fetchone()[0] == "wal"
    assert con.execute("SELECT status FROM emails").fetchone()[0] == "enviado"
    assert sent == ["ana@uni.co"]


def test_smtp_sent_inline_when_background_off(tmp_path, monkeypatch):
    from sicvec import mailer
    sent = []

    class FakeSMTP:
        def __init__(self, *a, **k): pass
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def starttls(self): pass
        def login(self, *a): pass
        def send_message(self, msg): sent.append(msg["To"])

    monkeypatch.setattr(mailer.smtplib, "SMTP", FakeSMTP)
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "s.sqlite"), "UPLOAD_DIR": str(tmp_path / "up"),
                      "ADMIN_PASSWORD": "pw-test", "SECRET_KEY": "k", "SMTP_HOST": "smtp.test",
                      "MAIL_FROM": "x@y.co", "MAIL_BACKGROUND": False})
    c = app.test_client()
    assert c.post("/enviar", data=submission_data(c)).status_code == 200
    with app.app_context():
        from sicvec.db import get_db
        assert get_db().execute("SELECT status FROM emails").fetchone()[0] == "enviado"
    assert sent == ["ana@uni.co"]


def test_submit_portuguese_accepted(client):
    r = client.post("/enviar", data=submission_data(client, language="pt"))
    assert r.status_code == 200 and b"SICVEC-001" in r.data


def test_three_languages_switch_and_persist(client):
    assert b"Idiomas oficiales" in client.get("/").data
    en = client.get("/?lang=en").get_data(as_text=True)
    assert "Official languages" in en and "Undergraduate students: COP 15.000" in en and 'lang="en"' in en
    # the choice is remembered by cookie
    assert b"Abstract submission" in client.get("/enviar").data
    pt = client.get("/programa?lang=pt").get_data(as_text=True)
    assert "Programação" in pt and "Terça-feira, 20 de outubro" in pt
    assert "Palestrantes" in client.get("/conferencistas").get_data(as_text=True)


def test_browser_language_used_when_no_choice(app):
    c = app.test_client()
    assert b"Inscri\xc3\xa7\xc3\xa3o" in c.get("/inscripcion", headers={"Accept-Language": "pt-BR,pt;q=0.9"}).data


def test_portuguese_author_gets_portuguese_emails(client, app):
    client.get("/enviar?lang=pt")
    r = client.post("/enviar", data=submission_data(client, language="pt", keywords="a, b"))
    assert "Indique de 3 a 5 palavras-chave" in r.get_data(as_text=True)
    r = client.post("/enviar", data=submission_data(client, language="pt"))
    assert "Sua referência é" in r.get_data(as_text=True)
    with app.app_context():
        from sicvec.db import get_db
        db = get_db()
        m = db.execute("SELECT subject, body FROM emails").fetchone()
        assert m["subject"].startswith("SICVEC 2026 — resumo recebido") and "Recebemos seu resumo" in m["body"]
        assert db.execute("SELECT ui_lang FROM submissions").fetchone()[0] == "pt"
        db.execute("UPDATE submissions SET decision='aceptado'")
        db.commit()
    client.post("/admin/notificar", data={"_csrf": token(client, "/enviar")}, headers=auth())
    with app.app_context():
        from sicvec.db import get_db
        body = get_db().execute("SELECT body FROM emails WHERE subject LIKE '%resultado do seu%'").fetchone()[0]
        assert "Aceito" in body and "Material final" in body


def test_fees_shown(client):
    html = client.get("/?lang=es").get_data(as_text=True)
    assert "Pregrado: COP 15.000" in html and "Posgrado: COP 30.000" in html and "Profesional: COP 50.000" in html


def test_speakers_include_renon_eller(client):
    html = client.get("/conferencistas?lang=es").get_data(as_text=True)
    for name in ("Beatriz Escobar Morales", "Wilson Manuel Castro Silupu", "Marianny Y. Combariza", "Monique Renon Eller"):
        assert name in html
    assert "Universidade Federal de Viçosa" in html


def test_speakers_include_valli(client):
    body = client.get("/conferencistas?lang=en").get_data(as_text=True)
    assert "Enrico Valli" in body
    assert "Valorization of by-products from olive oil production" in body
    assert client.get("/static/speaker_valli.jpg").status_code == 200


def test_home_figures_exist_in_every_language(client):
    for lang in ("es", "en", "pt"):
        body = client.get(f"/?lang={lang}").get_data(as_text=True)
        srcs = re.findall(r'src="(/static/fig_[^"]+)"', body)
        assert srcs == [f"/static/fig_ejes_{lang}.jpg", f"/static/fig_ods_{lang}.jpg"]
        for s in srcs:
            assert client.get(s).status_code == 200


def test_valli_first_on_speakers_page(client):
    for lang in ("es", "en", "pt"):
        body = client.get(f"/conferencistas?lang={lang}").get_data(as_text=True)
        assert body.index("Enrico Valli") < body.index("Beatriz Escobar Morales")


def test_keynote_slots_shown(client):
    # AC, 2026-09-30: programme sheet gives every keynote its slot; no "to be confirmed" line left.
    body = client.get("/conferencistas?lang=en").get_data(as_text=True)
    valli = body[body.index("Enrico Valli"):body.index("Beatriz Escobar Morales")]
    assert "Tuesday 20 October, 9:00–10:00" in valli
    for slot in ("Monday 19 October, 8:30–9:30", "Monday 19 October, 14:00–15:00", "Tuesday 20 October, 11:20–12:20",
                 "Tuesday 20 October, 15:35–16:35"):
        assert slot in body
    assert "to be confirmed (19 or 20 October)" not in body
    assert "Martes 20 de octubre, 9:00–10:00" in client.get("/conferencistas?lang=es").get_data(as_text=True)
    assert "Terça-feira, 20 de outubro, 9:00–10:00" in client.get("/conferencistas?lang=pt").get_data(as_text=True)


def test_combariza_photo(client):
    body = client.get("/conferencistas").get_data(as_text=True)
    assert "/static/speaker_combariza.jpg" in body
    assert client.get("/static/speaker_combariza.jpg").status_code == 200


def test_renon_photo_and_bio(client):
    body = client.get("/conferencistas").get_data(as_text=True)
    assert "/static/speaker_renon.jpg" in body
    assert "bioeconomía circular" in body
    assert client.get("/static/speaker_renon.jpg").status_code == 200


def test_calendar_2026_10_07(app):
    # AC, 2026-10-07: closing 12 Oct, review until 15 Oct, decision 15 Oct, payment 18 Oct; no separate
    # admisibilidad step. Supersedes test_calendar_2026_09_30 (10/14/15/17/18 Oct).
    cfg = app.config
    assert f"{cfg['SUBMISSION_DEADLINE']:%Y-%m-%d %H:%M}" == "2026-10-12 23:59"
    assert f"{cfg['REVIEW_DEADLINE']:%Y-%m-%d %H:%M}" == "2026-10-15 23:59"
    assert f"{cfg['PAYMENT_DEADLINE']:%Y-%m-%d %H:%M}" == "2026-10-18 23:59"


def test_footer_physics_logo(client):
    body = client.get("/").get_data(as_text=True)
    assert "/static/logo_fisica.jpg" in body and "pie-texto-logo" not in body
    assert client.get("/static/logo_fisica.jpg").status_code == 200



def test_programme_from_sheet(client):
    es = client.get("/programa?lang=es").get_data(as_text=True)
    assert "07:45–08:15" in es and "Conferencia magistral 5" in es and "Esp. Carlos Meza Bertel" in es
    assert "16:35–17:00" in es and "Eje 1" not in es
    en = client.get("/programa?lang=en").get_data(as_text=True)
    assert "Keynote lecture 4 · Dra. Monique Renon Eller" in en and "Talk 12 (to be assigned)" in en


def test_venue_logo(client):
    body = client.get("/").get_data(as_text=True)
    assert "/static/logo_guacari.png" in body
    assert client.get("/static/logo_guacari.png").status_code == 200


def test_stylesheet_versioned(client):
    body = client.get("/").get_data(as_text=True)
    assert "/static/style.css?v=" in body
