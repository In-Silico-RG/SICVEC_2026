# SICVEC 2026 — WSGI entry for PythonAnywhere. Paste into the web app's WSGI file
# (Web tab -> "WSGI configuration file"), replacing its contents.
# Settings live in ~/sicvec.env (KEY=value per line, never committed); see app/README.md.
import os
import sys

HOME = os.path.expanduser("~")
APP_DIR = os.path.join(HOME, "SICVEC_2026", "app")

with open(os.path.join(HOME, "sicvec.env")) as fh:
    for line in fh:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()

os.environ.setdefault("MAIL_BACKGROUND", "0")  # PythonAnywhere does not support threads in web apps
os.chdir(APP_DIR)
sys.path.insert(0, APP_DIR)

from run import app as application  # noqa: E402
