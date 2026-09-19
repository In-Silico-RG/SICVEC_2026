import sqlite3
from flask import current_app, g

SCHEMA = """
CREATE TABLE IF NOT EXISTS submissions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ref TEXT UNIQUE,
  created_at TEXT NOT NULL,
  email TEXT NOT NULL,
  title TEXT NOT NULL,
  language TEXT NOT NULL,
  modality TEXT NOT NULL,
  presentation TEXT NOT NULL,
  axis TEXT NOT NULL,
  abstract TEXT NOT NULL,
  keywords TEXT NOT NULL,
  word_count INTEGER NOT NULL,
  author_name TEXT NOT NULL,
  author_institution TEXT NOT NULL,
  author_program TEXT NOT NULL,
  author_country TEXT NOT NULL,
  other_authors TEXT NOT NULL DEFAULT '',
  consent INTEGER NOT NULL,
  status TEXT NOT NULL,              -- admisible | revision_manual | no_admisible
  flags TEXT NOT NULL DEFAULT '',
  decision TEXT,                     -- aceptado | aceptado_con_cambios | rechazado
  decision_note TEXT NOT NULL DEFAULT '',
  decided_at TEXT,
  notified_at TEXT,
  UNIQUE(email, title)
);
CREATE TABLE IF NOT EXISTS reviewers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  token TEXT NOT NULL UNIQUE,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS assignments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  submission_id INTEGER NOT NULL REFERENCES submissions(id),
  reviewer_id INTEGER NOT NULL REFERENCES reviewers(id),
  UNIQUE(submission_id, reviewer_id)
);
CREATE TABLE IF NOT EXISTS reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  assignment_id INTEGER NOT NULL UNIQUE REFERENCES assignments(id),
  s_relevance INTEGER NOT NULL, s_originality INTEGER NOT NULL, s_quality INTEGER NOT NULL,
  s_clarity INTEGER NOT NULL, s_impact INTEGER NOT NULL,
  weighted REAL NOT NULL,
  comments TEXT NOT NULL,
  recommendation TEXT NOT NULL,
  submitted_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS registrations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ref TEXT UNIQUE,
  created_at TEXT NOT NULL,
  name TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL,
  document TEXT NOT NULL, institution TEXT NOT NULL, country TEXT NOT NULL,
  category TEXT NOT NULL, attendance TEXT NOT NULL,
  presents INTEGER NOT NULL, submission_ref TEXT NOT NULL DEFAULT '',
  payment_ref TEXT NOT NULL DEFAULT '', receipt_file TEXT NOT NULL DEFAULT '',
  consent INTEGER NOT NULL,
  paid INTEGER NOT NULL DEFAULT 0,
  UNIQUE(email)
);
CREATE TABLE IF NOT EXISTS emails (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  to_addr TEXT NOT NULL, subject TEXT NOT NULL, body TEXT NOT NULL,
  status TEXT NOT NULL,              -- enviado | simulado (no SMTP) | error
  error TEXT NOT NULL DEFAULT ''
);
"""


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(app):
    import os
    os.makedirs(os.path.dirname(app.config["DATABASE"]) or ".", exist_ok=True)
    os.makedirs(app.config["UPLOAD_DIR"], exist_ok=True)
    con = sqlite3.connect(app.config["DATABASE"])
    con.executescript(SCHEMA)
    con.commit()
    con.close()
