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
    assert b"REG-001" in r.data and b"20.000" in r.data


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


def test_default_online_seats_is_300(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "t.sqlite"), "UPLOAD_DIR": str(tmp_path / "u"), "SECRET_KEY": "k"})
    assert app.config["ONLINE_SEATS"] == 300


def test_public_info_pages(client):
    home = client.get("/").get_data(as_text=True)
    for needle in ("Ejes temáticos", "ODS 12", "Pregrado: COP 20.000", "300 cupos en línea", "Centro Comercial Guacarí"):
        assert needle in home
    prog = client.get("/programa").get_data(as_text=True)
    assert "Programa preliminar" in prog and "Lunes 19 de octubre" in prog and "Martes 20 de octubre" in prog
    conf = client.get("/conferencistas").get_data(as_text=True)
    assert "Beatriz Escobar Morales" in conf and "sargazo holopelágico" in conf
    assert client.get("/static/speaker_escobar.jpg").status_code == 200
