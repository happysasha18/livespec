"""MINOR-gate 1.2.0 reconciliations (row 306) — enshrine the five folds the Fable
whole-spec audit forced, so none can silently drift back out. Landed 2026-07-13."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def test_base_rule_26_homes_design_principles():
    # D3: base-rulebook carries a real text home for INV-136/139 ownership
    base = _read("skills/live-spec-base/SKILL.md")
    assert "26. **A project kind also declares design principles the verify pass runs" in base
    assert "twenty-eight rules in the body" in base
    assert "INV-136, INV-139" in base
    # the periodic-full-audit rule is the final base rule (INV-145, Part C)
    assert "28. **A periodic full audit" in base
    # README's mirrored rule count is fresh
    assert "twenty-eight shared rules" in _read("README.md")


def test_d1_reading_discipline_composes_with_brief_read():
    # D1: rule 25 / INV-137 compose with INV-53 rather than contradicting it
    base = _read("skills/live-spec-base/SKILL.md")
    assert "lead never reads a file merely to hand a worker its anchors" in base
    spec = _read("PRODUCT_SPEC.md")
    assert "This read composes with the lead's reading discipline [INV-137]" in spec
    assert "dispatched to the reader whose distillation returns the brief's per-file lines" in spec


def test_d2_finding_kind_names_delta_scoped_exception():
    # D2: INV-140's "every defect blocks" carves out the delta-scoped gate (INV-114)
    spec = _read("PRODUCT_SPEC.md")
    prover = _read("skills/product-prover/SKILL.md")
    needle = "at a delta-scoped gate [INV-114] a pre-existing defect outside the delta queues"
    assert needle in spec
    assert needle in prover


def test_d5_chat_law_hook_carries_reading_discipline():
    # D5: the hook's routing echo now carries base rule 25 / INV-137
    hook = _read("scripts/chat-law-hook.sh")
    assert "base rule 25 (the reading discipline, SPEC INV-137)" in hook
    assert "dispatched to a reader worker" in hook


def test_minor_versions_on_the_1_4_0_line():
    # the milestone version numbers are current (1.4.0 at the cleanup movement,
    # 2026-07-14; PATCH 1.4.1 the stranger-door landing the same day — rows 261/315;
    # product-prover carries the finding-kind format at 1.1.4)
    assert _read("VERSION").strip() == "1.4.1"
    assert '"version": "1.4.1"' in _read(".claude-plugin/plugin.json")
    assert "version: 1.1.4" in _read("skills/product-prover/SKILL.md")
    assert "v1.4.1, 2026-07-14" in _read("PRODUCT_SPEC.md")
