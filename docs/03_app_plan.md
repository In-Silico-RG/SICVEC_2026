# 03 — SICVEC management app

*Started 2026-09-19. Replaces the Google Forms / EasyChair routes for submission, review and registration.*

**Objective.** Automate abstract submission, blind peer review, registration and notifications with a
small web app, with no per-submission cost and no third-party permission grants.
**Status.** in progress. MVP written and tested locally (22 tests pass; server smoke-tested). Not
deployed: needs a host, SMTP credentials, the consent text and the bank details.
Every change of this status line gets a dated line in `LOG.md`.

## 1. Choice of approach

| Option | Outcome |
|---|---|
| Google Forms built by hand | rejected by AC 2026-09-19 ("no vamos a hacer eso a mano") |
| Apps Script creating the forms | not run: needs an OAuth grant; AC "nope" |
| EasyChair | rejected: Free is capped at 20 submissions; Professional £2.90 per submission, credit card |
| Indico / Pretalx+Pretix (deploy, no code) | offered, not chosen |
| **Custom app (Flask + SQLite)** | chosen by AC 2026-09-19: "crea una app para ello" |

## 2. What was built (`app/`)
See `app/README.md`. Rules come from `Guia_Presentacion_Resumenes.tex` (modalities, word limits, 5 authors,
3-5 keywords) and `Rubrica_PeerReview.tex` (five criteria, weights 25/25/25/15/10, three recommendations).

## Decisions
- 2026-09-19, AC: build a code app to automate the process.
- 2026-09-19, Claude (default, reversible): Flask + SQLite, Spanish interface, private-link reviewers
  (no accounts), receipts uploaded to the server, decision suggestion only (a person decides).

## Open questions
1. **Host (AC).** Where does it run: UNISUCRE server or a VPS? Nothing goes live without this.
2. **SMTP (AC).** Which mailbox sends the emails (`insilico@unisucre.edu.co`?) and can it send by SMTP?
3. **Consent text (AC).** UNISUCRE's official data-treatment text.
4. **Bank details (SV / AC).** For the registration page.
5. **Decision thresholds (AC).** Suggested accept at mean >= 3.5 with no 'rechazado', reject below 2.5,
   third reviewer if the two scores differ by 2 or more. Proposal only.
6. **Online seats (AC).** 100 (documents) or 300 (AC's answer 2026-09-19); free?
7. **Guide and flyer.** They still need the app's URL once it exists.

## References
- `app/README.md`, `docs/02_google_forms_plan.md` (superseded), `docs/01_easychair_plan.md` (superseded).
