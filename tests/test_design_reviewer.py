"""INV-141 / INV-142 — the design-review pass (similarity discovery + the echo channel).
Enshrines the pass across its homes: the design-reviewer skill, the two spec clauses and
their index rows, the ARCHITECTURE node and seams, and these matrix rows. Landed 2026-07-14.
String level against the SHIPPED files on disk (matrix M-283, M-284)."""
from conftest import read, read_flat

SKILL = "skills/design-reviewer/SKILL.md"


# --- the shipped skill (INV-141) ---

def test_skill_ships():
    head = "\n".join(read(SKILL).splitlines()[:10])
    assert "name: design-reviewer" in head, "frontmatter lost its name"
    assert "version:" in head, "frontmatter lost its version"
    flat = read_flat(SKILL)
    # the description carves the trigger from the prover's: design-rightness, not spec-verification
    assert "same-kind" in flat, "skill lost the same-kind grouping headline"
    assert "judge the design" in flat or "judges the design" in flat, \
        "skill lost the judge-the-design mandate"


def test_similarity_lens_ships():
    flat = read_flat(SKILL)
    for step in ("Enumerate", "Describe by role", "Propose", "parity", "the tight ask"):
        assert step in flat, "similarity lens lost the step: %s" % step
    # role sentence uses the person's action words, not the author's class names
    assert "action words" in flat, "lens lost the person's-action-words rule"


def test_inventory_never_a_rival_registry():
    flat = read_flat(SKILL)
    assert "transient" in flat, "skill lost the transient-inventory word"
    assert "never written into the surface registry" in flat, \
        "skill lost the never-a-rival-registry boundary [E-10, INV-97]"


def test_never_blocks():
    flat = read_flat(SKILL)
    assert "never hold a landing" in flat, "skill lost the never-holds-a-landing property"
    assert "no blocking defects" in flat or "produces no defects" in flat, \
        "skill lost the no-defects derivation [INV-140]"


def test_record_discipline():
    flat = read_flat(SKILL)
    assert "docs/design-review/" in flat, "skill lost the dated-record home"
    assert "per-finding outcome" in flat, "skill lost the per-finding outcome column"


# --- the confidence read and the echo channel (INV-142) ---

def test_confidence_read_two_values():
    flat = read_flat(SKILL)
    assert "confident" in flat and "likely" in flat, "skill lost the two confidence values"
    assert "spec text alone" in flat, "skill lost the confident definition (text alone)"
    assert "human's intent" in flat, "skill lost the likely definition (intent)"


def test_echo_bar_and_cap():
    flat = read_flat(SKILL).lower()
    for cond in ("one plain sentence", "whole behaviour", "no spec sentence already decides"):
        assert cond in flat, "strong-signal bar lost the condition: %s" % cond
    assert "at most three" in flat, "echo channel lost the cap of three"
    assert "strongest first" in flat, "echo channel lost the strongest-first ordering"
    assert "recommended default" in flat, "echo channel lost the recommended default"


def test_unanswered_held():
    flat = read_flat(SKILL)
    assert "unanswered" in flat, "skill lost the unanswered-ask path"
    assert "not raised again" in flat or "not re-raised" in flat, \
        "skill lost the do-not-re-fire rule [INV-130]"


# --- the spec clauses and index rows ---

def test_spec_clauses_stand():
    spec = read("PRODUCT_SPEC.md")
    assert "A design review reads a proven spec and judges the design behind it." in spec, \
        "SPEC lost the INV-141 clause headline"
    assert "Every design review finding carries a confidence read" in spec, \
        "SPEC lost the INV-142 clause headline"
    assert "[INV-141]" in spec and "[INV-142]" in spec, "SPEC lost the clause anchors"


def test_formal_index_rows():
    lines = read("PRODUCT_SPEC.md").splitlines()
    for anchor in ("INV-141", "INV-142"):
        row = next((l for l in lines if l.startswith("| %s |" % anchor)), None)
        assert row is not None, "no Formal-index row for %s" % anchor
        assert "design review" in row, "%s index row lost its subject" % anchor
        assert "homes —" in row, "%s index row lost its homes line" % anchor


# --- the architecture node and seams ---

def test_architecture_node_and_seams():
    arch = read("ARCHITECTURE.md")
    node = next((l for l in arch.splitlines() if l.startswith("| design-reviewer |")), None)
    assert node is not None, "ARCHITECTURE lost the design-reviewer node row"
    assert "INV-141" in node and "INV-142" in node, "design-reviewer node lost its owned anchors"
    flat = read_flat("ARCHITECTURE.md")
    for seam in ("spec → design review", "design review → record", "design-review ask → human"):
        assert seam in flat, "ARCHITECTURE lost the seam: %s" % seam


# --- the matrix rows sit under the node ---

def test_matrix_rows_cite_the_node():
    mat = read("TEST_MATRIX.md")
    assert "### [node: design-reviewer]" in mat, "TEST_MATRIX lost the design-reviewer block"
    rows = [l for l in mat.splitlines() if l.startswith("| M-283 |") or l.startswith("| M-284 |")]
    assert len(rows) == 2, "TEST_MATRIX lost a design-review row (want M-283, M-284)"
    assert any("INV-141" in r for r in rows) and any("INV-142" in r for r in rows), \
        "design-review matrix rows lost their anchors"
