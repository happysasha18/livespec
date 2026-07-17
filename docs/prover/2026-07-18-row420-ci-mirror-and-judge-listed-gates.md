# Prover record — 2026-07-18 — ROADMAP 420 candidates 1 & 2: the CI-mirror gate and the judge-listed gate

Short form (SPEC INV-61): a small, single-module infra delta — two new gate-chain-integrity
checks in the guardrails node, no new surface, no structure change.

## Previous records clean

The prior record `docs/prover/2026-07-18-...` (row 390/392 doc-rotation, INV-209) carries no
unfolded rows. Nothing outstanding is inherited.

## The delta in one line

Two gates that guard the gate chain's own integrity: gate u (`check-ci-mirror.sh`, INV-210) reds
when a local pre-push gate that should run in CI is absent from `gates.yml`; gate v
(`check-judge-listed.py`, INV-211) reds when a judge the pack runs is missing from the installed
`~/.claude/settings.json` hook arrays. Both turn a failure this movement hit into a machine, both
declare their "should be in CI / should be wired" set in one machine-readable place a human also
reads (`ci-mirror.json`, `judge-hooks.json`).

## Verdict

- **Every spec fact has an owning node.** INV-210 and INV-211 are both owned by the guardrails
  node in ARCHITECTURE.md, with pins for the four new files (`check-ci-mirror.sh`, `ci-mirror.json`,
  `check-judge-listed.py`, `judge-hooks.json`). No unowned fact.
- **No node stands without spec backing.** No new node; the two invariants land under the existing
  guardrails node.
- **Cross-section.** Gate v composes with gate A's carve-out list: gate v reads personal-layer
  settings.json absent in CI, so it is declared carve-out `v` in `ci-mirror.json` and is never a CI
  step. This composition is stated in both INV clauses and asserted by
  `test_judge_listed.test_gate_is_a_carveout_not_mirrored_in_ci`. Gate u itself is mirrored in CI
  (step `gate u`), so it never reds on its own absence — asserted by `test_gate_mirrored_in_ci`.
- **The should-be-in-CI set is clean, not drowning in exceptions.** Four carve-outs (c, k, m, v),
  each with a stated reason a human reads; the honesty arm reds a stale carve-out that names no
  local gate. The set did not drown, so candidate 1 built as designed.
- **Gate v reads settings.json safely.** It stands down by name (exit 0, printing the stand-down)
  where settings.json is absent or unreadable, and never falsely passes — the self-widening honesty
  arm over `hooks/` still runs in that case. Asserted by `test_absent_settings_stands_down`.
- **Red-first proven.** 27 of the 28 new tests failed against the pre-delta tree (scripts, JSON
  declarations, and the four doc surfaces all absent), then green after the delta. The two
  behavioural red-proofs each pass inside the green suite: a fixture `gates.yml` missing a
  should-be-present gate reds (`test_missing_gate_step_reds`), a fixture settings.json missing the
  Stop `register-judge-collect` arm reds (`test_missing_stop_arm_reds`).

## Open ⟨DECIDE⟩

None touched by these surfaces.

## Must-fix

0.
