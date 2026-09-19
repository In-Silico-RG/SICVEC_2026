"""Pure rules of the peer-review process: no Flask, no I/O, so they are easy to test."""
import re

AXES = [
    "Economía Circular",
    "Química Verde y Procesos Sostenibles",
    "Biotecnología Sostenible",
    "Tecnologías Verdes y Energías Renovables",
    "Sostenibilidad en Cadenas de Suministro",
    "Política Pública y Gobernanza Ambiental",
]
MODALITIES = {"oral": "Ponencia oral (20 min)", "poster": "Póster científico (90 × 120 cm)",
              "taller": "Taller práctico"}
WORD_LIMITS = {"oral": 300, "poster": 250, "taller": 500}   # Guia_Presentacion_Resumenes.tex
CATEGORIES = {"pregrado": "Pregrado", "posgrado": "Posgrado", "profesional": "Profesional",
              "virtual": "Asistencia virtual (cupos en línea)"}
# Rubrica_PeerReview.tex: weights 25/25/25/15/10, scale 1-5.
CRITERIA = [("relevance", "Relevancia al evento", 0.25), ("originality", "Originalidad e innovación", 0.25),
            ("quality", "Calidad científica", 0.25), ("clarity", "Claridad y redacción", 0.15),
            ("impact", "Impacto potencial", 0.10)]
RECOMMENDATIONS = {"aceptado": "Aceptado", "aceptado_con_cambios": "Aceptado con cambios",
                   "rechazado": "Rechazado"}
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Thresholds approved by AC on 2026-09-19. They only produce a suggestion; the decision is always made by a person.
ACCEPT_MIN = 3.5
REJECT_BELOW = 2.5
MAX_SPREAD = 2.0


def fee_for(fees, category, attendance):
    """AC, 2026-09-19: in-person attendance pays by category; virtual attendance (300 seats) is free."""
    return 0 if attendance == "virtual" else fees[category]


def word_count(text):
    return len(text.split())


def valid_email(value):
    return bool(EMAIL_RE.match(value)) and len(value) <= 254


def weighted_score(scores):
    """scores: dict criterion -> 1..5. Returns the weighted mean rounded to 2 decimals."""
    total = 0.0
    for key, _label, weight in CRITERIA:
        v = int(scores[key])
        if not 1 <= v <= 5:
            raise ValueError(f"{key} out of range")
        total += v * weight
    return round(total, 2)


def suggest_decision(reviews):
    """reviews: list of dicts with 'weighted' and 'recommendation'. Returns (suggestion|None, note)."""
    if len(reviews) < 2:
        return None, "Faltan evaluaciones (se necesitan 2)."
    scores = [r["weighted"] for r in reviews]
    mean = round(sum(scores) / len(scores), 2)
    if max(scores) - min(scores) >= MAX_SPREAD:
        return None, f"Discrepancia entre revisores (media {mean}): considerar un tercer revisor."
    recs = {r["recommendation"] for r in reviews}
    if mean >= ACCEPT_MIN and "rechazado" not in recs:
        return "aceptado", f"Media ponderada {mean}."
    if mean < REJECT_BELOW:
        return "rechazado", f"Media ponderada {mean}."
    return "aceptado_con_cambios", f"Media ponderada {mean}."


def blind_flags(abstract, author_names, contact_email):
    """Ways the abstract text may reveal its authors."""
    flags = []
    low = abstract.lower()
    if re.search(r"[^@\s]+@[^@\s]+", abstract) or contact_email.lower() in low:
        flags.append("El texto contiene una dirección de correo.")
    for name in author_names:
        parts = [p for p in re.split(r"\s+", name.strip().lower()) if len(p) >= 3]
        if len(parts) >= 2 and all(p in low for p in parts[:2]):
            flags.append(f"El texto parece mencionar a un autor ({name.strip()}).")
    return flags


def author_names_from(author_name, other_authors):
    names = [author_name]
    for line in other_authors.splitlines():
        first = line.split(",")[0].strip()
        if first:
            names.append(first)
    return names


def is_conflict(reviewer_name, reviewer_email, submission_email, authors_text):
    if reviewer_email.strip().lower() == submission_email.strip().lower():
        return True
    return bool(reviewer_name.strip()) and reviewer_name.strip().lower() in authors_text.lower()


def plan_assignments(submissions, reviewers, existing, per_submission=2):
    """Balanced automatic assignment.

    submissions: list of dicts (id, email, authors_text)
    reviewers:   list of dicts (id, name, email)
    existing:    set of (submission_id, reviewer_id)
    Returns (new_pairs, short) where short = ids of submissions that could not get enough reviewers.
    """
    load = {r["id"]: 0 for r in reviewers}
    for _s, rid in existing:
        if rid in load:
            load[rid] += 1
    have = {}
    for sid, _rid in existing:
        have[sid] = have.get(sid, 0) + 1
    new, short = [], []
    for s in sorted(submissions, key=lambda x: x["id"]):
        need = per_submission - have.get(s["id"], 0)
        if need <= 0:
            continue
        cands = [r for r in reviewers
                 if (s["id"], r["id"]) not in existing
                 and not is_conflict(r["name"], r["email"], s["email"], s["authors_text"])]
        cands.sort(key=lambda r: (load[r["id"]], r["id"]))
        for r in cands[:need]:
            new.append((s["id"], r["id"]))
            load[r["id"]] += 1
        if len(cands) < need:
            short.append(s["id"])
    return new, short


def csv_safe(value):
    """Neutralize spreadsheet formula injection in exported cells."""
    s = "" if value is None else str(value)
    return "'" + s if s[:1] in ("=", "+", "-", "@", "\t", "\r") else s
