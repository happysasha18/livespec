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
    assert "thirty rules in the body" in base
    assert "INV-136, INV-139" in base
    # the periodic-full-audit rule is base rule 28 (INV-145, Part C); rule 29 is the deferral test
    assert "28. **A periodic full audit" in base
    assert "29. **A deferral must justify itself" in base
    # README's mirrored rule count is fresh
    assert "thirty shared rules" in _read("README.md")


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
    hook = _read("hooks/chat-law-hook.sh")
    assert "base rule 25 (the reading discipline, SPEC INV-137)" in hook
    assert "dispatched to a reader worker" in hook


def test_version_homes_agree():
    # The pack version has one source of truth, the VERSION file, and every other home
    # must AGREE with it — so a bump that misses a home reds here. This is derived from
    # VERSION rather than pinned to a literal, so it stays current across releases on its
    # own; it replaced a per-release 1.x.y snapshot that had to be hand-edited every bump
    # (the maintenance trap that reds a green release, fixed at root 2026-07-15).
    version = _read("VERSION").strip()
    assert f'"version": "{version}"' in _read(".claude-plugin/plugin.json")
    assert f"v{version}, " in _read("PRODUCT_SPEC.md")
