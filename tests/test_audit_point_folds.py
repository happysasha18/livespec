"""Row 343 — the Fable audit's point fixes to the prover's own text (findings D4, D6-E, R1,
R3, R4, R5 of docs/audit/2026-07-16-prover-fable.md).

Six amendments, each a sentence or two in skills/product-prover/SKILL.md:
- D4: the surface-authority lens's fallback is a stated assumption, never silence.
- D6-E: 3d probes whether two clauses describing overlapping data state their agreement.
- R1: the KIND block names the blocking semantics of a paired-transition finding and of an
  open motion question at push time.
- R3: FEATURE-FIT's consistency exclusion scopes to PRE-EXISTING consistency; a delta clause
  contradicting an existing clause is the mode's first check.
- R4: FEATURE-FIT verdicts on a shipped system cite pinned clauses or go conditional.
- R5: the FULL pass's closing summary reports the accumulated [default] count.
"""
from conftest import read


def _skill():
    return read("skills/product-prover/SKILL.md")


def test_surface_authority_fallback_is_a_stated_assumption():
    s = _skill()
    assert "I found no authoritative surface for" in s
    assert "stay silent rather than produce a finding" not in s


def test_3d_probes_overlapping_data_agreement():
    s = _skill()
    assert "two clauses independently describe overlapping data" in s


def test_kind_block_names_motion_question_gate_semantics():
    s = _skill()
    assert "declared one-sided pair" in s
    assert "open motion question" in s


def test_feature_fit_consistency_scope_rewritten():
    s = _skill()
    assert "Pre-existing consistency between old clauses is out of scope" in s
    assert "Document-internal consistency is out of scope for this mode" not in s


def test_feature_fit_verdicts_cite_pinned_clauses_on_shipped_systems():
    s = _skill()
    assert "verdict cites a clause whose surface carries a current node pin" in s


def test_full_pass_reports_default_accretion():
    s = _skill()
    assert "[default]`-tagged sentences accumulated" in s
