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
        "FEES": {"pregrado": 20000, "posgrado": 30000, "profesional": 40000, "virtual": 0},
        "CONSENT_TEXT": os.environ.get(
            "CONSENT_TEXT",
            "[PENDIENTE: texto oficial de la política de tratamiento de datos de UNISUCRE]"),
        "SMTP_HOST": os.environ.get("SMTP_HOST", ""),
        "SMTP_PORT": int(os.environ.get("SMTP_PORT", "587")),
        "SMTP_USER": os.environ.get("SMTP_USER", ""),
        "SMTP_PASSWORD": os.environ.get("SMTP_PASSWORD", ""),
        "MAIL_FROM": os.environ.get("MAIL_FROM", "insilico@unisucre.edu.co"),
        "BASE_URL": os.environ.get("BASE_URL", "http://localhost:5000"),
        "SESSION_COOKIE_SECURE": os.environ.get("SESSION_COOKIE_SECURE", "") == "1",
        "SESSION_COOKIE_SAMESITE": "Lax",
    }
    if overrides:
        cfg.update(overrides)
    return cfg
