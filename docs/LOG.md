# LOG — chronological lab notebook

*One dated entry per working session. Records what was decided, what was tried and
dropped, and the commits. Outcomes live in the numbered docs; this file keeps the order of
events and the dead ends. Every status change of a numbered doc gets a line here.*

Working mode: AC directs and decides; Claude executes and reports. Language: English.

Sessions before 2026-09-19 are **backfilled from the git log** (commit subjects, in
Spanish in the repo) and from the project memory. Decisions are attributed to AC only where
the commit or memory records them as his. Older narrative log: `../LOG_Actividades_SICVEC_2026.md`
(Spanish, kept as is).

---

## 2026-09-14 — Backfill: repo created, scope set

- Repo created and pushed (`f7c898f` 16:48): proposal, peer-review guides, COP budget draft, tasks.
- Decisions (AC, 2026-09-14): event dates 19-20 Oct 2026 (was 14-15 Nov); hybrid modality
  with online seats; audience widened to chemistry, physics, maths, biology, all engineering;
  Physics added as co-organizing department; 'Maestría en Biología' removed from cover.
  Registration fees: undergrad COP 20.000, postgrad 30.000, professionals 40.000.
- Commits: `32a7a15`, `46efdab` 17:36; `82b3936`, `b4a0637` 17:41.
- Dropped: `gh repo create --push` blocked by permissions; worked as create, then push over SSH.

## 2026-09-15 — Backfill: budget rewritten, letters

- Proposal finalized with 100 free online seats for external/international universities and
  open public streaming (`7b0cd31`, `bb01150` 09:29).
- Budget went USD draft → COP 6.000.000 without contingency (`4b13f56` 09:36) → **COP 2.000.000 final**
  (`5a64237` 09:39; propagated `4b841bf`, `8f5f953`, `4d133eb`). **Supersedes the USD 10.697 / COP 32,9 M
  figure in `~/.claude/CLAUDE.md` and the older memory.** `9ab4b4f` reverted a LaTeX budget change.
- Definitive schedule with specific dates (`d7452d8`, `fa1712d` 10:27); activity log added (`6bd056b`).
- Letters in LaTeX: department heads, scientific committee (`e28a752`), generic head letter
  (`1101664`), speaker invitation and international partner request (`a83d619`).
- Layout fixes to headers/budget in all PDFs (`6024f78`, `57ade4f`); contact email fixed (`97c3dee`).

## 2026-09-16 — Backfill: identity, schedule change, coordinators

- Selena Arias Avila added as Coordinadora Administrativa (`b187a89` 09:53). Not in CLAUDE.md.
- Programme trimmed: no practical workshops / day-1 panel, 15-min breaks, posters 17-18h (`04614f3`, `3866bcc`, `d128536`).
- Budget in proposal set to COP 2.500.000 (`38919a0` 10:29) after the 2.000.000 of 15 Sept, and a
  Budget section added to the proposal (`6ad4ed3`). **Check which figure is current** (see Open).
- Logos: IN SILICO, SICVEC on proposal, all letters, emails, flyer; A5 flyer created (`d7a2029`, `ba1c205`).
- Email templates for co-organizing departments (`e1e73bc`).
- Peer-review schedule changed (AC, 2026-09-16): call 22 Sep–4 Oct, close 4 Oct 23:59, evaluation 5-7 Oct,
  notification 8-9 Oct, payment deadline 15 Oct, final material 14 Oct. Propagated to schedule,
  proposal, manual (`c143555`, `a5dd894`, `6f3cb11`, `130ea23`). Supersedes the 28 Sep close.
- Log/memory update `00b6a0a` 16:51.

## 2026-09-17 — Backfill: letters, speakers

- Letters and communications updated to Sept-17 dates and the corrected timeline (`d3be383` 09:17).
- Department email drafts (`138c3b9`; tone changed to 'a su Departamento' `688a5c4`).
- Speaker invitations: Kafarov (UIS), Beatriz Escobar (CICY México) (`013766a`); four speakers
  finalized (`1618bf4` 15:50). Files also exist for Marianny Combariza and Wilson Castro.

## 2026-09-18 — Backfill: corporate sponsorship

- Corporate sponsorship proposal ('Muestra Empresarial') and speaker info sheet (`bc65ff5` 11:59);
  contact set to Selena Arias Avila (`0a8de89` 12:06).
- Planned in the older log: coordinators' meeting 18 Sep 4 PM. Outcome not recorded.

## 2026-09-19 — Session: resume in SICVEC mode

- AC: "seguimos en modo SICVEC". Read git log, TAREAS.md, memory. No `docs/LOG.md` existed:
  created this file, `docs/TEMPLATE.md`, `docs/reviews/`.
- State found: HEAD `0a8de89`, `main` in sync with origin. Uncommitted: removal of the
  'Recursos' item (technical/financial/in-kind support) from
  `Solicitud_Entidad_Asociada_Internacional.tex/.pdf`; five untracked logo files in `07_Comunicaciones/`.
- `TAREAS.md` still says "Actualizado 14 sept" in its header and lists work already done
  (flyer, email templates) as open.
- Open for AC: see below.

- Decisions (AC, 2026-09-19): budget is **COP 2.500.000** (1.000.000 materials + 1.500.000 image/audiovisual).
  Already correct in proposal `.tex`/PDF and `Presupuesto_SICVEC_2026_COP.md`; stale in `README.md:148`
  (USD 11,198) — fixed. `~/.claude/CLAUDE.md` synced (budget, Selena Arias Avila, 22 Sep–4 Oct schedule).
- AC confirmed "YES" to: public launch done, department emails sent, 18 Sep coordinators' meeting held.
  No details recorded (what was agreed at the meeting is unknown to the log).
- `TAREAS.md` header set to 19 Sep; flyer ticked, budget item ticked, email-template item annotated.
- Not touched: `LOG_Actividades_SICVEC_2026.md` and `.claude/worktrees/update-budget/` still carry old
  figures (USD 10.697 / COP 2.000.000); the former is a historical log, kept as is.

- Decision (AC, 2026-09-19): removal of the 'Recursos' item from the international partner letter is
  intended; commit and push everything.
- Commit `ab4ec2b` 12:00 — Remove 'Recursos' item from international partner letter; add logo files
- Commit `b953a9a` 12:00 — Sync budget (COP 2.500.000) in README and TAREAS; add docs/LOG.md with backfill

- SSH broke: `~/.ssh` was regenerated 2026-09-19 09:33 (known_hosts deleted, new `id_ed25519` not registered
  on GitHub; the registered one was 'Clave SSH para Aldo at Univac', 2026-07-04). Push of `93d5470` went once
  over HTTPS with the `gh` token. Fix (AC asked to redo the connection): new key registered with
  `gh ssh-key add` as 'Aldo new key 2026-09-19'; `known_hosts` rebuilt from the host keys returned by
  `gh api meta` (fingerprints checked against GitHub's published ones), not by trust-on-first-use.
  Verified: `ssh -T git@github.com` authenticates as In-Silico-RG; `git ls-remote origin` works.
  Note: the same `id_ed25519` is the IdentityFile for the GUANE HPC hosts in `~/.ssh/config`.

### Open for AC
1. What came out of the 18 Sep meeting (venue, online seats/platform, reviewers)?
