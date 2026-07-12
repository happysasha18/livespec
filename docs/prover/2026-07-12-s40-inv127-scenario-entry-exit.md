# Prover record — INV-127 (scenario entry/exit contracts) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.7. Mode: CROSS-LINK short form (SPEC INV-61 — small
skill-kind delta, no new surface, no structure change).

## The delta

One invariant, INV-127 (row 192, a large theme Alexander deferred 2026-07-09, revived at today's
prover-method landings): each person-facing scenario states how it is ENTERED (from where, what must already
hold) and how it EXITS (to where, what it leaves true). The per-operation precondition/postcondition lenses
lifted to the SCENARIO level, kin of the entry-symmetry lens (INV-50) and the runtime view's flow walks
(INV-74). The prover carries the scenario-level lens; an unstated edge is a finding. Binds forward (INV-15).
Homes: the composition clause + Formal index, the entry/exit duty in spec-author's scenario-authoring
guidance, product-prover's scenario-level lens. Owning node: spec-author (owns-list + M-268; the prover
lens is wiring, as with INV-50). Test: `tests/test_scenario_entry_exit.py` (6 assertions, red-proven then
green).

## Validated on one real spec

The pack's own PRODUCT_SPEC.md already practices the convention where it matters: the bug scenario
("When a bug cuts the line", F-bug) states an explicit **Precondition** ("a feature is in work when the bug
report arrives") and **Postcondition** ("the bug's fix is landed; every parked feature is back in
work..."). Other scenarios state their edges implicitly or not at all — exactly the gaps the new
scenario-level lens flags. So the law is grounded in a real, working example, and its forward-binding
enforcement has real targets. Full retrofit of every scenario's edges is future work the lens drives, never
a blocking backlog (INV-15).

## Previous record's unfolded rows

`2026-07-12-s40-inv126-paired-transition.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (spec-author owns-list carries INV-127, beside INV-50 its closest kin); matrix row
  M-268 under the spec-author block; Formal-index row present.
- Composition clean: INV-127 lifts the operation-level precondition/postcondition lenses (already in the
  prover's phase-3 list) to the scenario level, and is kin of INV-50 (entry symmetry, a face's re-entry) and
  INV-74 (the runtime view's flow walks). No contradiction; the finding class is INV-72's blank-answer class.
- The forward-binding clause (INV-15) prevents the law from opening a blocking backlog of unstated edges on
  older scenarios — the prover flags, never blocks. This matches how INV-50 and INV-74 already bind.

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
