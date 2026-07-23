"""INV-144 — when the product and the spec diverge, the spec is the definition of correct,
and changing it is a decision. Enshrines the reconciliation triage + the ratification bar +
the forbidden move across its homes so none can silently drift out. Landed 2026-07-14."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def test_spec_states_the_definition_of_correct():
    spec = _read("PRODUCT_SPEC.md")
    assert "the spec is the definition of correct" in spec
    # the triage default: a divergence is presumed a product error, checked against the spec
    assert "defaults to a possible error in the product" in spec
    # the silent-spec path is completed and pinned
    assert "complete the spec to state the guarantee" in spec
    # the forbidden move
    assert "never silently rewritten to match the product" in spec
    assert "INV-144" in spec
    # Formal-index row
    assert "| INV-144 |" in spec


def test_prover_carries_the_divergence_pointer():
    prover = _read("skills/product-prover/SKILL.md")
    assert "INV-144" in prover


def test_architecture_owns_144():
    arch = _read("ARCHITECTURE.md")
    assert "INV-144" in arch


def test_matrix_row_for_144():
    matrix = _read("TEST_MATRIX.md")
    assert "INV-144" in matrix
