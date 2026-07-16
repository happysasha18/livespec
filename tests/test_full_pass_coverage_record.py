"""INV-171 — a full prover pass owes a coverage record: mandatory sweeps with verdicts.

The heaviest mode had the weakest accountability: FEATURE-FIT owed a verdict per lens while FULL
owed none, and on a frontend-kind spec the three coverage tables collapsed to one sanctioned N/A
line — a skipped lens was indistinguishable from a lens that found nothing (both shipped misses
were skim casualties inside a "not a checklist" stress wall). The stress lenses now split into
mandatory sweeps — each owing one verdict line, hit / clean / N/A-with-reason, rendered as a
surface × sweep table — and discretionary imaginative probes. The five lifecycle lenses gather
under the transition-payload parent (INV-168) so one lifecycle is walked once, not five times
from five colliding angles.
"""
from conftest import read


def _skill():
    return read("skills/product-prover/SKILL.md")


def test_spec_states_the_coverage_record_law():
    spec = read("PRODUCT_SPEC.md")
    assert "owes a coverage record" in spec
    assert "| INV-171 |" in spec


def test_skill_splits_sweeps_from_probes():
    s = _skill()
    assert "Mandatory sweeps" in s
    assert "Imaginative probes" in s


def test_each_sweep_owes_a_verdict_line():
    s = _skill()
    assert "hit / clean / N/A-with-reason" in s
    assert "A missing verdict line reads as a skipped sweep" in s


def test_surface_by_sweep_table_replaces_the_na_collapse():
    s = _skill()
    assert "surface × sweep" in s


def test_lifecycle_gathers_under_the_payload_parent():
    s = _skill()
    assert "**Lifecycle**" in s
    # the five gathered lenses keep their names and anchors
    for name in ("**Transition payload**", "**Entry symmetry**", "**Entry state**",
                 "**Paired-transition symmetry**", "**Persistence and versions**",
                 "**Scenario entry and exit**"):
        assert name in s, name
