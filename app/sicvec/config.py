"""Configuration. Everything sensitive comes from environment variables; nothing has a default password."""
import os
from datetime import datetime, timedelta, timezone

CO = timezone(timedelta(hours=-5))  # Colombia, no daylight saving


def _dt(name, default):
    return datetime.fromisoformat(os.environ.get(name, default))


def load_config(overrides=None):
    cfg = {
        "SECRET_KEY": os.environ.get("SECRET_KEY", ""),
        "ADMIN_PASSWORD": os.environ.get("ADMIN_PASSWORD", ""),
        "DATABASE": os.environ.get("DATABASE", os.path.join("instance", "sicvec.sqlite")),
        "UPLOAD_DIR": os.environ.get("UPLOAD_DIR", os.path.join("instance", "uploads")),
        "MAX_CONTENT_LENGTH": 6 * 1024 * 1024,
        # Dates come from docs/LOG.md (AC, 2026-09-16 schedule change).
        "SUBMISSION_DEADLINE": _dt("SUBMISSION_DEADLINE", "2026-10-04T23:59:00-05:00"),
        "REVIEW_DEADLINE": _dt("REVIEW_DEADLINE", "2026-10-07T23:59:00-05:00"),
        "PAYMENT_DEADLINE": _dt("PAYMENT_DEADLINE", "2026-10-15T23:59:00-05:00"),
        # AC, 2026-09-19: 300 online seats, free for external and international participants.
        "ONLINE_SEATS": int(os.environ.get("ONLINE_SEATS", "300")),
        "FEES": {"pregrado": 15000, "posgrado": 30000, "profesional": 40000, "virtual": 0},
        "CONSENT_TEXT": os.environ.get(
            "CONSENT_TEXT",
            # Draft from Resolución 1129 de 2021 (UNISUCRE data policy), art. 6 purposes a, b, d; pending AC approval.
            "Autorizo de manera libre, previa, expresa e informada a la Universidad de Sucre para tratar mis datos "
            "personales con el fin de gestionar mi participación en SICVEC 2026 (envío y evaluación de resúmenes, "
            "inscripción, pagos, certificados, memorias del evento y comunicaciones relacionadas), conforme a la Ley 1581 "
            "de 2012 y a la Política de Tratamiento de Datos Personales de la Universidad de Sucre (Resolución 1129 de "
            "2021). Conozco mis derechos a conocer, actualizar, rectificar y suprimir mis datos y a revocar esta "
            "autorización."),
        "INSTITUTION_DATA": os.environ.get(
            "INSTITUTION_DATA",
            # From Resolución 1129 de 2021; atencionalciudadano@ from unisucre.edu.co (egresados/normatividad page).
            "Responsable del tratamiento: Universidad de Sucre, NIT 892.200.323-9, Cra. 28 # 5-267, Barrio Puerta Roja, "
            "Sincelejo (Sucre), Colombia. Política: Resolución 1129 de 2021, disponible en unisucre.edu.co. Consultas y "
            "reclamos: atencionalciudadano@unisucre.edu.co o comunicación escrita a la dirección indicada (respuesta en "
            "máximo 15 días hábiles). Dudas sobre el evento: insilico@unisucre.edu.co."),
        "SMTP_HOST": os.environ.get("SMTP_HOST", ""),
        "SMTP_PORT": int(os.environ.get("SMTP_PORT", "587")),
        "SMTP_USER": os.environ.get("SMTP_USER", ""),
        "SMTP_PASSWORD": os.environ.get("SMTP_PASSWORD", ""),
        "MAIL_FROM": os.environ.get("MAIL_FROM", "insilico@unisucre.edu.co"),
        # 1: send from a background thread (VPS). 0: send inside the request (PythonAnywhere: no threads in web apps).
        "MAIL_BACKGROUND": os.environ.get("MAIL_BACKGROUND", "1") == "1",
        "BASE_URL": os.environ.get("BASE_URL", "http://localhost:5000"),
        "SESSION_COOKIE_SECURE": os.environ.get("SESSION_COOKIE_SECURE", "") == "1",
        "SESSION_COOKIE_SAMESITE": "Lax",
    }
    if overrides:
        cfg.update(overrides)
    return cfg
