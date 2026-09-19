# 02 — Google Forms plan: abstract submission, registration and peer review

*Started 2026-09-19. Phase: peer-review and registration infrastructure, before the call opens on 2026-09-22 (Tuesday).*

**Objective.** Run abstract submission, registration and blind peer review with Google Forms and
Google Sheets, at no cost, and replace the `[URL - Completar]` placeholders in the author documents.
**Status.** superseded 2026-09-19 by `03_app_plan.md` (AC chose a custom app). Kept for the field lists. Field lists are written (`04_Inscripcion/Formularios/Especificacion_Formularios.md`);
the forms are not built yet, and the bank details, data-treatment text and chair account are missing.
Every change of this status line gets a dated line in `LOG.md`.

## 1. Design

Three forms, one master Sheet, one blind Sheet for reviewers.

| Piece | What it does |
|---|---|
| **Form A — Envío de resúmenes** | Authors send metadata and the abstract text. Open to anyone (no Google sign-in). |
| **Form B — Inscripción** | Category and fee, in-person or virtual, payment receipt upload for paying categories. |
| **Form C — Evaluación de revisores** | The five-criterion rubric (1-5), recommendation, confidentiality and conflict declarations. |
| **Master Sheet** | Responses of A and B. Owned by the chairs only. Adds the reference number `SICVEC-###` and the weighted score. |
| **Reviewer Sheet** | Separate file fed from the master with `IMPORTRANGE` and `QUERY`: reference number, title, axis, keywords and abstract only, **no author columns**. Reviewers get access to this file, never to the master. |

Key design choice: the abstract is pasted as **text** in the form, not uploaded as a PDF. A file upload
forces every respondent to sign in with a Google account (a barrier for international authors), and a
PDF may carry author names, which breaks blind review. Text in a field lets the reviewer Sheet omit the
authors by construction. This changes the current guide, which asks for a PDF (`Guia_Presentacion_Resumenes.tex`
step 3.3): see open question 1.

## 2. Workflow and dates

| Date | Step | Owner |
|---|---|---|
| 2026-09-20 | Create forms A, B, C and both Sheets under the institutional account; test with dummy data | AC |
| 2026-09-21 | Insert the real links into the guide, manual, template, flyer and emails; recompile | Claude |
| 2026-09-22 | Call opens | AC / MXD |
| 2026-10-04 23:59 | Form A closes (turn off "Accepting responses" by hand, or with a Form add-on / script) | AC |
| 2026-10-04/05 | Admissibility: word count, keywords, axis, anonymity of the text; assign 2 reviewers per abstract | MXD |
| 2026-10-05/07 | Reviewers fill Form C, one response per abstract | reviewers |
| 2026-10-08 | Decision from the weighted score and the recommendations; notification 8-9 Oct by email (mail merge from the Sheet) | MXD / AC |
| 2026-10-14 | Final material from accepted authors (email or a fourth form) | authors |
| 2026-10-15 | Payment deadline | participants |

## 3. What Google Forms cannot do, and the workaround

| Gap | Workaround |
|---|---|
| No reference number | Sheet column `="SICVEC-"&TEXT(ROW()-1,"000")` next to the response. |
| No automatic reviewer assignment | Manual table `Asignaciones` in the master Sheet: reference number, reviewer 1, reviewer 2. |
| No enforced word limit | Character cap in the form (oral 300 words, poster 250, workshop 500: cap at 3.600 characters) and a word-count check at admissibility. |
| Form does not close at a set time | Add a Google Apps Script trigger, or close it by hand on 4 Oct at 23:59. |
| No blind review out of the box | Reviewer Sheet described above. Reviewers must also not be shown authors inside the abstract text: the CFP tells authors to leave names out of the abstract field. |
| Notifications to authors | Mail merge from the Sheet (Apps Script or a merge add-on). |
| Weighted score | `=0,25*B2+0,25*C2+0,25*D2+0,15*E2+0,10*F2` on the Form C responses (Sheet locale with decimal comma; use `.` otherwise). |

## Decisions

- 2026-09-19, AC: use Google Forms for abstract submission and registration. EasyChair rejected: the Free
  plan is capped at 20 submissions and Professional costs £2.90 per submission, credit card only, with no
  software line in the COP 2.500.000 budget. Recorded in `LOG.md`.
- 2026-09-19, AC: the abstract is pasted as text in Form A, not uploaded as a PDF (no sign-in, blind by
  construction). Guide step 3.3 and the template checklist changed accordingly.
- 2026-09-19, AC: the forms and Sheets are owned by `insilico@unisucre.edu.co`.

## Open questions

1. **Data-treatment text (AC).** Colombian data-protection law (Ley 1581 de 2012) requires an authorization
   text. Use UNISUCRE's official policy text: `[PENDIENTE]`.
2. **Bank details for the fee (SV / AC).** Account, holder and reference to write on the transfer:
   `[PENDIENTE]`. Nothing in the repo lists them.
3. **Reviewers (MXD, before 2026-09-30).** 10-15 names and emails, needed before assignments on 4-5 Oct.
4. **Online seats (AC, today).** AC answered "300 seats open". Proposal, letters and flyer say 100 free online
   seats. Does 300 replace 100, and is it free? Until answered, no seat count is changed in the documents.
5. **Institutional mailbox (AC).** Confirm `insilico@unisucre.edu.co` is monitored; it will receive the form
   notifications and appear on the forms.

## References

- `03_Memorias_y_PeerReview/Rubricas_Evaluacion/Rubrica_PeerReview.tex` (criteria and weights).
- `03_Memorias_y_PeerReview/Guias_Autores/Guia_Presentacion_Resumenes.tex` (modalities, limits).
- `docs/01_easychair_plan.md` (superseded; keeps the EasyChair cost findings).
