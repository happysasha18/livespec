# Prover record — INV-129 (deferred-row revisit at every queue-take) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, skill kind, no new surface, no structure change).

## The delta

One invariant, INV-129: deferred rows are revisited at every queue-take, not only at milestones. A deferred
row carries a revisit trigger [T-8]; a time-bound one can come true and lapse between two milestone gates, so
the milestone re-scan [M-1] read the triggers too rarely. At every queue-take the session also re-scans each
deferred row's trigger against the current moment, a fired trigger returning its row to the runnable head
[INV-49] right then. Homes: the queue-take clause + Formal index, and build-pipeline's queue-take walk.
Owning node: build-pipeline (owns-list + M-270). Test: `tests/test_deferred_revisit_cadence.py` (4
assertions, red-proven then green).

## Previous record's unfolded rows

`2026-07-12-s40-inv46-audit-trigger-broadened.md` — 1 must-fix + 2 should-clarify, all folded that landing.
No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (build-pipeline owns-list carries INV-129, beside INV-49 the queue-take graph and
  INV-1 the no-wish-lost law it extends); matrix row M-270 sits under the build-pipeline block and cites
  INV-129; Formal-index row present. The suite's cross-reference laws (index density, owning node,
  matrix-row-under-owner) are satisfied.
- Composition clean against every neighbour the clause names. INV-1 (a deferred wish never waits on a
  trigger nobody reads) is strengthened, never contradicted: the promise now holds at two cadences instead
  of one. M-1 (the milestone gate's re-scan) stays exactly as written — the new cadence is additive, the
  milestone remains a reader. INV-49 (lanes picked by a graph at queue-take) gains one more thing the
  queue-take moment does, on the same runnable-head it already reads; no new state, no reordering of the
  graph walk. T-8 (the deferred end-state and its revisit trigger) is unchanged; the trigger vocabulary
  stays free-form, which the clause states plainly.
- No new asking machinery and no new surface: the re-scan is a read the session already had the data for,
  now run at a second, more frequent breakpoint. Non-goals stated (the vocabulary-restriction fork
  declined); success measure stated ([default]).

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
