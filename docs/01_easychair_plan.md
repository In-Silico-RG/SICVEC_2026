# 01 — EasyChair plan: abstract submission and peer review

*Started 2026-09-19. Phase: peer-review infrastructure, before the call opens on 2026-09-22.*

**Objective.** Set up EasyChair as the single system for abstract submission, blind peer
review, decisions and author notifications for SICVEC 2026, and replace the
`[URL - Completar]` placeholders in the author documents.
**Status.** superseded 2026-09-19 by `02_google_forms_plan.md`. AC chose Google Forms; EasyChair not used.
Every change of this status line gets a dated line in `LOG.md`.

## 1. Requirements taken from the project documents

| Requirement | Source | EasyChair mapping |
|---|---|---|
| Modalities: oral (max 300 words), poster (max 250), practical workshop (descriptive proposal, max 500) | `Guia_Presentacion_Resumenes.tex` | No modality field by default. Verify whether the license allows a custom question; fallback: separate tracks (multi-track needs Professional or higher) or a modality tag as the first word of the title. |
| "Solo asistencia" is a fourth option | same | Registration, not submission. Stays in the registration form, not in EasyChair. |
| Languages: Spanish or English | same | Nothing to configure; state it in the CFP text. |
| Max 5 authors, 3-5 keywords, one main thematic axis | same | Authors: EasyChair does not cap them; state the limit in the CFP. Keywords: built-in field. Axes: the six SICVEC axes as EasyChair *topics*. |
| Abstract as PDF | same | Upload field. |
| Word limits (300 / 250) | same | EasyChair does not enforce word counts; state them in the CFP and check at admissibility. |
| Blind review: reviewers must not know the authors | `Rubrica_PeerReview.tex` §6 | Anonymous submission option; authors must submit a PDF with no names or affiliations. |
| Five weighted criteria (1-5): Relevance 25 %, Originality 25 %, Scientific quality 25 %, Clarity 15 %, Impact 10 % | `Rubrica_PeerReview.tex` | Review form. Verify whether the license allows custom scored fields; otherwise use the overall score plus comments and compute the weighted mean from the exported scores. |
| Recommendation: Accepted / Accepted with changes / Rejected | same | Decision options (customizable in all licenses). |
| The rubric asks reviewers to email the form to `sicvec.academico@unisucre.edu.co` | `Rubrica_PeerReview.tex:326` | Obsolete once EasyChair is used; remove that line. |
| Virtual authors (international networks) | `TAREAS.md` | Not an EasyChair field on the free plan; handle in the registration form. |

## 2. Cost and limits (source: easychair.org license pages, read 2026-09-19)

| License | Limit | Price | Notes |
|---|---|---|---|
| Free | max **20** submissions; no advanced features, no support | 0 | Loses access to the conference if over 20 and unpaid. |
| Professional | up to **60** submissions | **£2.90 per submission**, minimum charge for 20 (£58) | Credit card only, pay as you go. Adds multi-track, imports, Excel/CSV export. |
| Executive | larger conferences, helpdesk | not read | Needed above 60. |

At £2.90 the range is £58 (20 submissions) to £174 (60 submissions), roughly COP 0.25-0.7 M at
about 4.000 COP/£ (rough conversion, check the rate). The approved budget is COP 2.500.000 with no
line for software, so this is a decision, not a detail. The two pages were read through a
summarizer and one pricing page returned an error; confirm price and limits on the license
selection screen before paying.

## 3. Setup steps (about 2 hours once the decisions in §5 are made)

1. **Chair account.** Create the EasyChair account with an institutional address. The reviewer form in the
   documents already uses `sicvec.academico@unisucre.edu.co`; use it if it exists and someone reads it.
2. **Create the conference.** Name "SICVEC 2026", full name "Simposio Internacional de Ciencia Verde y
   Economía Circular". Pick the license (§5.1).
3. **Time zone and deadlines.** Set Colombia time (UTC-5) first, then:
   submission close **2026-10-04 23:59**; reviews due **2026-10-07**; decisions **2026-10-08**;
   notifications **2026-10-08/09**; final material **2026-10-14** (verify the license has a final-version stage).
4. **Topics.** The six axes: Economía Circular; Química Verde y Procesos Sostenibles; Biotecnología
   Sostenible; Tecnologías Verdes y Energías Renovables; Sostenibilidad en Cadenas de Suministro;
   Política Pública y Gobernanza Ambiental.
5. **Submission settings.** Anonymous submissions on; PDF upload required; 3-5 keywords; abstract field.
6. **Review settings.** Blind. Review form with the five criteria and the three recommendations.
   Confidentiality text from the rubric §6.
7. **Program committee.** Add the 10-15 reviewers (`TAREAS.md`, still open) and the chairs
   (Aldo, María Ximena Díaz). Aldo and María Ximena should not review submissions from their own group;
   mark those conflicts in the system.
8. **Test.** Submit a dummy abstract with a second account, assign it, review it, decide it, delete it.
9. **Publish the link.** Put the URL in `Guia_Presentacion_Resumenes.tex:353`,
   `Manual_Memorias_PeerReview.tex:360`, `Template_Resumen_Cientifico.tex:207`, the flyer and the
   announcement emails. Recompile the PDFs (two passes, check with `pdftotext`).

## 4. Timeline

| Date | Task | Owner |
|---|---|---|
| 2026-09-19 (Sat) | Decisions in §5; propagate the 4 Oct close date (§5.4) | AC |
| 2026-09-20 (Sun) | Create conference, topics, deadlines, review form; dummy test | Claude prepares text, AC creates the account |
| 2026-09-21 (Mon eve) | Publish URL into documents; recompile PDFs | Claude |
| 2026-09-22 (Tue) | Call opens with the link live | AC / MXD |
| 2026-10-04 | Close 23:59 | system |
| 2026-10-04/05 | Admissibility check (word counts, anonymization); assign reviewers | MXD |
| 2026-10-05/07 | Reviews | reviewers |

Note: 2026-09-22 is a Tuesday (2026-09-19 is a Saturday). Earlier in this session Claude wrote
"Mon 22 Sep" in chat; that was wrong. It is not in the repo files.

## Decisions

- 2026-09-19, AC: use EasyChair for abstract submission and peer review.

## Open questions

1. **License (AC, today).** Free (max 20 submissions) or Professional (£2.90 per submission, credit card).
   How many abstracts do you expect? Above 20, Free stops working.
2. **Who pays (AC, today).** Professional is credit card only: an institutional card, a personal one to be reimbursed, or
   a card of the research group?
3. **Chair account (AC, today).** Which email owns the conference? Does `sicvec.academico@unisucre.edu.co` exist?
4. **Close date (AC, today).** Six files still show a 28 Sep close instead of 4 Oct (see the log entry of
   2026-09-19); propagate before the link is published.
5. **Reviewers (MXD, before 2026-09-30).** 10-15 names and emails are needed before assignments on 4-5 Oct;
   they must accept an EasyChair invitation.
6. **Modality and virtual option (AC).** How do we capture oral / poster / workshop and in-person / virtual?
   Decide once the license is known.

## References

- EasyChair, license pages: easychair.org/docs/license_free, /license_pro, /license_kinds (read 2026-09-19).
- `03_Memorias_y_PeerReview/Guias_Autores/Guia_Presentacion_Resumenes.tex`, `Manual_Memorias_PeerReview.tex`.
- `03_Memorias_y_PeerReview/Rubricas_Evaluacion/Rubrica_PeerReview.tex`.
