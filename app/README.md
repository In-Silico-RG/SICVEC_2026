# SICVEC 2026 — management app

Flask + SQLite app that automates abstract submission, blind peer review, registration and
notifications. Written 2026-09-19; plan and decisions in `../docs/03_app_plan.md`.

## Public pages
`/` (about, objectives, six axes, SDGs, how to take part, fees, venue), `/programa` (preliminary two-day structure from the proposal),
`/conferencistas` (Escobar). Content lives in `sicvec/content.py`; fees, seats and deadlines come from the config.
Still `por anunciar/por confirmar` on the pages: streaming platform, room/address, keynote slot, second keynote.

## What runs by itself
- **Deadlines** are enforced by the clock (Colombia time, UTC-5): submission closes 2026-10-04 23:59,
  reviews 2026-10-07 23:59, payment noted 2026-10-15. No manual closing.
- **Validation at submit**: word limit per modality (oral 300, poster 250), 3-5 keywords,
  at most 5 authors, axis from the six axes, consent and originality boxes, duplicate guard.
- **Blind-review check**: abstracts that contain an email or an author's name go to `revision_manual`.
- **Reference numbers** `SICVEC-###` and `REG-###`, and a confirmation email for each.
- **Reviewer assignment**: one click assigns 2 reviewers per admissible abstract, balanced by load, skipping conflicts.
- **Blind review**: reviewers open a private link (no account). The reviewer view never reads author columns.
- **Score**: weighted mean with the rubric weights 25/25/25/15/10, plus a decision *suggestion*
  (thresholds approved by AC 2026-09-19, in `sicvec/logic.py`). The decision is always entered by a person.
- **Notifications**: one click emails every decided, not-yet-notified author with the anonymous comments.
- **Registration**: fee by category, online-seat cap (`ONLINE_SEATS`), receipt upload (PDF/PNG/JPG checked by content).
- **Exports**: CSV of abstracts, registrations, reviews (formula-injection neutralized). Every email is logged.

## Run locally
```bash
cd app
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
ADMIN_PASSWORD='choose-one' .venv/bin/python -m flask --app run run     # http://localhost:5000
.venv/bin/python -m pytest -q                                            # 24 tests
```
Admin panel: `/admin`, user `admin`, password from `ADMIN_PASSWORD` (no default; without it the panel is off).

## Configuration (environment variables)
| Variable | Meaning |
|---|---|
| `ADMIN_PASSWORD` | required for `/admin` |
| `SECRET_KEY` | session key; set a fixed random value in production |
| `BASE_URL` | public URL, used in reviewer invitation links |
| `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `MAIL_FROM` | real email. Without `SMTP_HOST` emails are logged as `simulado` and nothing is sent |
| `CONSENT_TEXT` | official UNISUCRE data-treatment text (still `[PENDIENTE]`) |
| `ONLINE_SEATS` | cap for virtual registrations, default 300 (AC, 2026-09-19); virtual attendance is free, in-person pays by category |
| `SUBMISSION_DEADLINE`, `REVIEW_DEADLINE`, `PAYMENT_DEADLINE` | ISO 8601 with offset, e.g. `2026-10-04T23:59:00-05:00` |
| `DATABASE`, `UPLOAD_DIR` | paths; default `instance/` |
| `SESSION_COOKIE_SECURE=1` | set behind HTTPS |

## Deploying (not done yet: needs a host)
1. Any Linux host with Python 3.10+ (a UNISUCRE server or a small VPS).
2. `pip install gunicorn`; run `gunicorn -w 2 -b 127.0.0.1:8000 run:app` under systemd.
3. Put nginx or Caddy in front with HTTPS (the admin uses HTTP Basic auth: **never expose it over plain HTTP**).
4. Set the variables above; back up `instance/` (database and receipts) daily.
5. Personal data (IDs, receipts): restrict server access, and set the real consent text before opening the call.

## Known limits
- HTTP Basic auth for a single admin; no per-user accounts or audit trail beyond the email log.
- No rate limiting on the public forms: put it in the reverse proxy if abuse appears.
- Emails are sent synchronously; fine for ~200 users, not for thousands.
- Not security-audited. Treat it as an MVP that handles personal data.
