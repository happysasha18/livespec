"""INV-169 — a feature delta that adds a second member of an existing kind draws the scoped
design review at intake.

The moment an undeclared same-kind grouping comes into existence is the intake of its SECOND
member — and that was exactly where the design review stood down (FEATURE-FIT drew none), so a
second sibling could enter, ship, and diverge, findable only at the next FULL pass after the
divergence was live. FEATURE-FIT now asks the second-sibling question by construction; a yes
draws the scoped design review over the delta.

These tests assert the spec states the law and both skills carry it, so the intake window is
closed in real text rather than a journal note.
"""
from conftest import read


def test_spec_states_the_second_sibling_law():
    spec = read("PRODUCT_SPEC.md")
    assert "second member of a kind an existing surface already has" in spec


def test_spec_scopes_the_stand_down():
    spec = read("PRODUCT_SPEC.md")
    assert "stands down at the push gate" in spec


def test_prover_skill_asks_the_question_at_intake():
    skill = read("skills/product-prover/SKILL.md")
    assert "second member of a kind an existing surface already has" in skill
    assert "INV-169" in skill


def test_design_reviewer_carries_the_exception():
    skill = read("skills/design-reviewer/SKILL.md")
    assert "second member" in skill
    assert "INV-169" in skill


def test_index_row_present():
    spec = read("PRODUCT_SPEC.md")
    assert "| INV-169 |" in spec
