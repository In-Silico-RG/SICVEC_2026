import pytest
from sicvec import logic


def test_weighted_score_matches_rubric_weights():
    assert logic.weighted_score(dict(relevance=5, originality=5, quality=5, clarity=5, impact=5)) == 5.0
    # 4*.25 + 3*.25 + 5*.25 + 2*.15 + 1*.10 = 3.4
    assert logic.weighted_score(dict(relevance=4, originality=3, quality=5, clarity=2, impact=1)) == 3.4


def test_weighted_score_rejects_out_of_range():
    with pytest.raises(ValueError):
        logic.weighted_score(dict(relevance=6, originality=3, quality=3, clarity=3, impact=3))


def test_word_count():
    assert logic.word_count("uno dos  tres\ncuatro") == 4


def test_suggest_needs_two_reviews():
    assert logic.suggest_decision([{"weighted": 4, "recommendation": "aceptado"}])[0] is None


def test_suggest_accept_reject_and_changes():
    a = {"weighted": 4.2, "recommendation": "aceptado"}
    assert logic.suggest_decision([a, a])[0] == "aceptado"
    assert logic.suggest_decision([dict(weighted=2.0, recommendation="rechazado")] * 2)[0] == "rechazado"
    assert logic.suggest_decision([dict(weighted=3.0, recommendation="aceptado_con_cambios")] * 2)[0] == "aceptado_con_cambios"
    # a rejection recommendation blocks a plain accept even with a high mean
    assert logic.suggest_decision([a, dict(weighted=3.6, recommendation="rechazado")])[0] == "aceptado_con_cambios"


def test_suggest_flags_disagreement():
    s, note = logic.suggest_decision([dict(weighted=1.5, recommendation="rechazado"),
                                      dict(weighted=4.5, recommendation="aceptado")])
    assert s is None and "tercer revisor" in note


def test_blind_flags():
    assert logic.blind_flags("Contacto ana@x.org", ["Ana Pérez"], "z@z.co")
    assert logic.blind_flags("Trabajo de Ana Pérez en la UNISUCRE", ["Ana Pérez"], "z@z.co")
    assert not logic.blind_flags("Se estudió la pirólisis de lignina.", ["Ana Pérez"], "z@z.co")


def test_plan_assignments_balances_and_avoids_conflicts():
    subs = [dict(id=i, email=f"a{i}@x.co", authors_text="Autor Uno") for i in (1, 2, 3)]
    revs = [dict(id=1, name="R Uno", email="r1@x.co"), dict(id=2, name="R Dos", email="r2@x.co"),
            dict(id=3, name="R Tres", email="r3@x.co")]
    new, short = logic.plan_assignments(subs, revs, set())
    assert not short and len(new) == 6
    loads = {}
    for _s, r in new:
        loads[r] = loads.get(r, 0) + 1
    assert max(loads.values()) - min(loads.values()) <= 1
    # conflict: reviewer 1 is the author of submission 1
    subs[0]["email"] = "r1@x.co"
    new, _ = logic.plan_assignments(subs[:1], revs, set())
    assert all(r != 1 for _s, r in new)


def test_plan_assignments_reports_shortage():
    subs = [dict(id=1, email="a@x.co", authors_text="A")]
    new, short = logic.plan_assignments(subs, [dict(id=1, name="R", email="r@x.co")], set())
    assert short == [1]


def test_csv_safe_blocks_formulas():
    assert logic.csv_safe("=1+1") == "'=1+1"
    assert logic.csv_safe("texto") == "texto"
