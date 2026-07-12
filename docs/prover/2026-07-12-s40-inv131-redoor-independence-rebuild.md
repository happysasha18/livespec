# Prover record — INV-131 (mid-work re-door rebuilds the independence graph) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, skill kind, no new surface, no structure change).

## The delta

One invariant, INV-131: a mid-work re-door [INV-16] rebuilds the parallel-lanes independence graph. When the
re-door creates a surface or state that did not exist when the lanes opened, the same re-check re-runs the
independence edges [INV-49] against every rolling lane; a new edge pulls the re-doored lane back to serial
with a board line, so the departures board never asserts a stale independence. Homes: the mid-work re-door
clause + Formal index, and build-pipeline's door re-fire. Owning node: build-pipeline (owns-list + M-272).
Test: `tests/test_redoor_independence_rebuild.py` (4 assertions, red-proven then green).

## Previous record's unfolded rows

`2026-07-12-s40-inv130-withdrawal-convergence.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (build-pipeline owns-list carries INV-131, beside INV-16 the door law and INV-49 the
  independence graph it joins); matrix row M-272 sits under the build-pipeline block and cites INV-131;
  Formal-index row present. Index density, owning node, and matrix-row-under-owner all hold.
- Composition clean against every neighbour named. INV-16 (the mid-work re-door) gains one more thing the
  re-check does, at the same stop it already makes; no new stop, no reordering. INV-49 (lanes picked by a
  graph at queue-take) is re-run rather than redefined — the same edge rule (shared surface / spec section
  / skill file / doc region) applied again at a new moment. INV-39 (the integration re-fence catches a
  collision at landing) is explicitly preserved and named as the still-standing safety net, so the new
  clause is honest that it closes an OBSERVABILITY gap (the board asserting stale independence between the
  re-door and the landing) rather than a correctness hole — matching the finding's own reading.
- No new automatic checker is claimed: the spec's existing "the senior judges independence and says so
  aloud" line [INV-49 territory] is preserved verbatim in meaning — the re-door is named only as the moment
  that judgement is owed again, so the human-judgement contract is not quietly replaced by a machine.
- The board line is the departures-board vocabulary [INV-27/T-18] already in use (a lane names whom it waits
  behind); no new board surface, the serial-by-the-graph line reused.

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
