"""INV-138 — a gated behaviour names every side of its gate.
Both ends of a threshold-gated transition + the three states of an async slot.
Enshrines the law across its six homes. Landed 2026-07-13."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _flat(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def test_spec_clause_stands():
    spec = _flat("PRODUCT_SPEC.md")
    assert "A gated behaviour names every side of its gate" in spec
    assert "[INV-138]" in spec


def test_spec_names_both_faces():
    spec = _flat("PRODUCT_SPEC.md")
    assert "below the low end" in spec
    assert "above the high end" in spec
    assert "pending, arrived, and failed" in spec
    assert "visible pending" in spec


def test_formal_index_row():
    for line in _flat("PRODUCT_SPEC.md").splitlines():
        if line.startswith("| INV-138 |"):
            assert "gate" in line
            return
    raise AssertionError("no Formal-index row for INV-138")


def test_spec_author_carries_the_facet():
    sa = _flat("skills/spec-author/SKILL.md")
    assert "Edge completeness" in sa
    assert "the three faces of a wait" in sa


def test_prover_carries_the_edge_completeness_lens():
    pp = _flat("skills/product-prover/SKILL.md")
    assert "Edge-condition completeness" in pp
    assert "both ends of the range" in pp
    assert "[INV-138]" in pp


def test_matrix_row_covers_edge_completeness():
    for line in _flat("TEST_MATRIX.md").splitlines():
        if line.startswith("| M-") and "INV-138" in line:
            return
    raise AssertionError("no matrix row cites INV-138")
