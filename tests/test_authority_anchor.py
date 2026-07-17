"""A decision recorded as the person's names the exchange it came from; a claim the pack reasoned out
is written in the pack's own voice (SPEC INV-207, ROADMAP 415).

Every claim in this pack stands on an artifact a reader can go and check. A human's word is the one
input with no artifact behind it — the one claim no agent, prover, or gate questions — so a
challengeable judgment recorded AS the person's is a fabrication moved into the one slot nothing
reaches again. That is the defect born 2026-07-17, when a session recorded its own lane-ranking as the
person's decision and he recognised nothing on read-back.

Two machines hold the rule:
  * the read-back surface `DECISIONS.md` — the decision-set record, the read-back touchpoint the frame
    declares [INV-205], asynchronous and opened on request — shows the person the decisions the pack
    believes he made, so he strikes what he never said (a struck line retracted, kept with its note);
  * the gate `guardrails/check-authority-anchor.py` reads the decision set: in a declared
    `DECISION-RECORD` surface every live on-record entry carries its date, a struck entry skipped, so
    an unanchored one reds. Its standing scan is the decision-record surface (false-positive-free by
    construction); the spec, base rulebook, and roadmap take the one-time first sweep.

The fabricated lane-ranking is the corpus's first fixture.
"""
import os
import subprocess

from conftest import ROOT, read

GATE = os.path.join(ROOT, "guardrails", "check-authority-anchor.py")
CONFIG = os.path.join(ROOT, "guardrails", "authority-anchor.json")
FIXTURES = os.path.join(ROOT, "guardrails", "authority-anchor-fixtures")


def _gate(*args):
    return subprocess.run(["python3", GATE, *args], capture_output=True, text=True)


def _fix(name):
    return os.path.join(FIXTURES, name)


# --- the two machines ship ---

def test_gate_ships():
    assert os.path.isfile(GATE), "guardrails/check-authority-anchor.py missing"


def test_config_ships():
    assert os.path.isfile(CONFIG), "guardrails/authority-anchor.json missing"


def test_readback_surface_ships():
    assert os.path.isfile(os.path.join(ROOT, "DECISIONS.md")), "DECISIONS.md (the read-back) missing"


def test_readback_declares_its_touchpoint():
    text = read("DECISIONS.md")
    assert "TOUCHPOINT-KIND: decision-readback" in text, "DECISIONS.md does not declare its touchpoint"
    manifest = read("guardrails/touchpoints.json")
    assert "decision-readback" in manifest, "the manifest does not declare the decision-readback point"
    assert '"surface": "DECISIONS.md"' in manifest, "the manifest does not point at DECISIONS.md"


def test_readback_is_a_decision_record():
    assert "DECISION-RECORD" in read("DECISIONS.md"), "DECISIONS.md carries no DECISION-RECORD marker"


def test_template_ships():
    tmpl = os.path.join(ROOT, "templates", "DECISIONS.template.md")
    assert os.path.isfile(tmpl), "templates/DECISIONS.template.md missing"
    text = read("templates/DECISIONS.template.md")
    assert "DECISION-RECORD" in text and "TOUCHPOINT-KIND: decision-readback" in text


# --- the gate: the decision-record surface ---

def test_gate_reds_the_fabricated_ranking():
    """The corpus's first fixture: a lane-ranking recorded as his with no exchange named."""
    r = _gate(_fix("record-unanchored.md"))
    assert r.returncode == 1, r.stdout
    assert "his ranking" in r.stdout.lower() or "ranking" in r.stdout.lower()


def test_gate_passes_a_dated_record():
    assert _gate(_fix("record-anchored.md")).returncode == 0


def test_gate_passes_a_struck_record():
    """A struck line is retracted; the gate skips it, since the person has already struck it."""
    assert _gate(_fix("record-struck.md")).returncode == 0


# --- the gate: the first-sweep act over free prose ---

def test_gate_reds_unanchored_prose():
    assert _gate(_fix("prose-unanchored.txt")).returncode == 1


def test_gate_passes_dated_prose():
    assert _gate(_fix("prose-anchored.txt")).returncode == 0


def test_gate_passes_rule_language():
    """The pack's own rule language ('the human's word settles it') is an abstract role, not a
    recorded decision — the law's own challengeable side, needing no anchor."""
    assert _gate(_fix("prose-rule-language.txt")).returncode == 0


# --- the real surfaces and the standing scan ---

def test_gate_passes_the_readback_surface():
    """DECISIONS.md, the host's real decision record, is fully anchored."""
    assert _gate(os.path.join(ROOT, "DECISIONS.md")).returncode == 0


def test_gate_standing_scan_spares_the_archive():
    """Push mode scans only the DECISION-RECORD surfaces; the churny archive and diaries are spared,
    exactly as check-shipped-language and check-freeze spare them, so the standing gate is green."""
    r = _gate()  # no args → push mode
    assert r.returncode == 0, r.stdout
    src = read("guardrails/check-authority-anchor.py")
    for spared in ("JOURNAL.md", "NEXT_STEPS.md", "ROADMAP.md"):
        assert spared in src, "%s must be named in the spared set" % spared


def test_gate_names_no_person_in_code():
    """The person roster lives in the config DATA; the gate's own code names no person (the
    shipped-language allowlist's rule)."""
    import json
    src = read("guardrails/check-authority-anchor.py")
    roster = json.loads(read("guardrails/authority-anchor.json")).get("person_names", [])
    assert roster, "the config declares no person roster"
    for name in roster:
        assert name not in src, "the gate's code names %r — it must live only in the config data" % name


def test_gate_wired_into_pre_push():
    assert "check-authority-anchor.py" in read("guardrails/pre-push"), \
        "pre-push does not wire the authority-anchor gate"


# --- traceability across the four documents ---

def test_spec_states_the_law():
    spec = read("PRODUCT_SPEC.md")
    assert "[INV-207]" in spec
    assert "check-authority-anchor.py" in spec
    assert "DECISIONS.md" in spec


def test_formal_index_row():
    assert "| INV-207 |" in read("PRODUCT_SPEC.md")


def test_architecture_owns_the_invariant():
    arch = read("ARCHITECTURE.md")
    assert "INV-207" in arch
    assert "check-authority-anchor.py" in arch


def test_matrix_row_covers_the_law():
    matrix = read("TEST_MATRIX.md")
    assert "M-388" in matrix
    assert "INV-207" in matrix
