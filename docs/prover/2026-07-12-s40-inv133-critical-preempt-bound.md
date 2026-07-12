# Prover record — INV-133 (critical-priority preemption bound) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, skill kind, no new surface, no structure change).

## The delta

One invariant, INV-133: a critical non-bug heads the queue but never preempts a rolling lane, and the bound
is echoed back at intake. "Critical" is defined in bug terms but liftable onto any door [T-11], so a critical
non-bug could head the queue and then wait for the current lane while a human who said "critical" for a live
break expected bug-like preemption. Preemption belongs to the bug door alone [T-9], so a critical non-bug
lands at the current lane's checkpoint ahead of everything else waiting, but never stops the rolling lane; a
genuine live break is a bug. The capture echo [INV-27] says the bound back when a wish is marked critical on
a non-bug door, so the human can re-door it a bug if that is what he meant. Homes: the priority clause +
Formal index, and communicator's rule 12. Owning node: build-pipeline (owns-list + M-274). Test:
`tests/test_critical_preempt_bound.py` (4 assertions, red-proven then green).

## Previous record's unfolded rows

`2026-07-12-s40-inv132-scenario-heading-tag.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (build-pipeline owns-list carries INV-133, beside T-9/T-11 the queue-cutting and
  priority-ordering laws and INV-12 the classify step it sharpens); matrix row M-274 sits under the
  build-pipeline block and cites INV-133; Formal-index row present. Index density, owning node, and
  matrix-row-under-owner all hold.
- Composition clean against every neighbour named. T-9 (queue-cutting belongs to the bug door alone) is the
  law the bound rests on, restated not contradicted — the new clause simply makes explicit that critical on
  a non-bug does NOT borrow the bug door's preemption. T-11 (priority moves the lane; critical heads the
  queue whatever its door) is preserved: the queue-head promise stands, only the misread that it also
  preempts is closed. INV-27 (every intake echoed back) is the carrier for the new echo line, its existing
  one-sentence echo gaining one bounded case. INV-9 (the human owns priority) is honoured — the clause
  states what critical buys per door and never refuses the mark, and the human can re-door to a bug for real
  preemption. INV-2 (the bug lane preempts) is the door that DOES preempt, named as the honest alternative.
- The chosen arm of the finding's fork is the no-preempt-plus-echo one, not the restrict-critical-to-bug-door
  arm: restricting the mark would have needed a second urgency word for a non-bug break and re-touched every
  intake surface, where stating the bound and echoing it keeps one urgency vocabulary and closes the gap at
  the exact moment the human could be misled — intake. Recorded as the taste call.
- No new surface and no new state: the echo rides the existing capture echo, the bound is a reading of the
  already-stated queue/preemption rules.

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
