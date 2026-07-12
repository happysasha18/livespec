# Prover — composition-walk fold (2026-07-12, short form per INV-61)

Small delta (kind: spec clauses + two skill homes; four existing invariants amended, no new codes).

- **Previous records:** 2026-07-12-full-pass-pre-1.1.0 (0 must-fix, full pass); this delta is the
  composition-walk audit's own follow-up, drafted by the Opus auditor and landed mechanically per
  .live-spec/checkpoints/pending-draft-composition-fixes.md (commit 94f206b).
- **The delta in one line:** M-6 gains the inbox-only push-gate carve-out (clause + index + profile
  pointer, PRODUCT_SPEC.md + .live-spec/profile.md); INV-111 states the full-suite-green check and its
  routing relationship to INV-114 (clause + index); INV-114's token-identity gate scopes to
  content-preserving restructures, stated in all three homes (spec clause + product-prover/SKILL.md +
  build-pipeline/SKILL.md, plus the index row); INV-112 gains the live-session stand-down exemption
  sentence for its one-file additive deposit (clause + index). Three test extensions
  (test_restructure_merge_gate.py, test_docs_layout_vehicle.py, test_inbox_remote_arm.py) proved red
  against the pre-delta tree, then green after the prose landed. No new INV/M codes minted; no
  renumbering.
- **Composition read:** the four amendments target the seams the audit itself found between laws that
  landed within two days of each other (INV-111/INV-113/INV-114) and between the push gate and the new
  remote-inbox arm (M-6/INV-112) — each amendment is a single-clause scope statement closing exactly the
  gap the audit named, verified against the audit's own self-verify section (needle compatibility,
  byte-exact anchors, register). No clash found with any other law read during application.
- **Verdict:** ready to ship — 0 must-fix, 0 should-clarify. Full suite 422/422 green pre-commit.
