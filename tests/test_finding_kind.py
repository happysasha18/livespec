"""INV-140 — the prover labels each finding a defect or a recommendation.
Enshrines the finding-kind reporting rule across its homes. Landed 2026-07-13."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _flat(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def test_prover_tag_carries_kind():
    pp = _flat("skills/product-prover/SKILL.md")
    assert "kind · plain-label (formal-term)" in pp
    assert "defect · boundary-issue (composition)" in pp


def test_severity_axis_retired_from_prover():
    """kind is the sole verdict axis: the old three-level severity vocabulary
    is gone from the prover's tag and rule surface (INV-140 collapse)."""
    pp = _flat("skills/product-prover/SKILL.md")
    for token in ("must-fix", "should-clarify", "worth-considering"):
        assert token not in pp, f"retired severity token {token!r} still in prover SKILL"


def test_severity_axis_retired_from_spec_and_readme_case_insensitive():
    """The retired three-level severity vocabulary is gone from the two most
    visible normative surfaces — case-insensitively, so a capital 'Must-fix'
    cannot survive again (D1/D2 defect class, INV-140 single-axis collapse)."""
    import re
    tokens = ("must-fix", "should-clarify", "should-fix", "nice-to-have", "worth-considering")
    pat = re.compile("|".join(re.escape(t) for t in tokens), re.IGNORECASE)
    for rel in ("PRODUCT_SPEC.md", "README.md"):
        hits = [m.group(0) for m in pat.finditer(_flat(rel))]
        assert hits == [], f"retired severity token(s) still in {rel}: {hits}"


def test_push_gate_folds_on_kind():
    """M-6 folds on kind, not on a separate severity level."""
    spec = _flat("PRODUCT_SPEC.md")
    assert "folds every defect and queues every recommendation" in spec
    pp = _flat("skills/product-prover/SKILL.md")
    assert "folds at the push gate" in pp


def test_prover_defines_defect_and_recommendation():
    pp = _flat("skills/product-prover/SKILL.md")
    assert "a stated invariant is violated" in pp
    assert "queues for a taste call" in pp
    assert "`defect`" in pp and "`recommendation`" in pp


def test_spec_clause_stands():
    spec = _flat("PRODUCT_SPEC.md")
    assert "The prover labels each finding a defect or a recommendation" in spec
    assert "[INV-140]" in spec


def test_formal_index_row():
    for line in _flat("PRODUCT_SPEC.md").splitlines():
        if line.startswith("| INV-140 |"):
            assert "defect" in line
            return
    raise AssertionError("no Formal-index row for INV-140")


def test_matrix_row_covers_finding_kind():
    for line in _flat("TEST_MATRIX.md").splitlines():
        if line.startswith("| M-") and "INV-140" in line:
            return
    raise AssertionError("no matrix row cites INV-140")


def test_architecture_owns_140():
    assert "INV-140" in _flat("ARCHITECTURE.md")
