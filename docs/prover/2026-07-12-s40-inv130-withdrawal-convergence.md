# Prover record — INV-130 (withdrawn-decision convergence) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, skill kind, no new surface, no structure change).

## The delta

One invariant, INV-130: a withdrawn decision converges — after two withdrawals the recommended option is
taken as a surfaced `[default]`. An answered question closes forever [INV-59], but a withdrawal re-asks in
plainer terms with no cap of its own [INV-9], so a genuine taste call could loop unbounded. The bound is
two; on the second withdrawal of the same decision the session takes the recommendation and surfaces it as
a `[default]` on the landing report, silence consent from there [INV-31], never re-asked. Homes: the
decision-page clause + Formal index, and communicator's rule 10. Owning node: communicator (owns-list +
M-271). Test: `tests/test_withdrawal_convergence.py` (4 assertions, red-proven then green).

## Previous record's unfolded rows

`2026-07-12-s40-inv129-deferred-revisit-cadence.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (communicator owns-list carries INV-130, beside INV-59 the ask-convergence law and
  E-22 the decision page it lives in); matrix row M-271 sits under the communicator block and cites
  INV-130; Formal-index row present. Index density, owning node, and matrix-row-under-owner all hold.
- Composition clean against every neighbour named. INV-59 (an answered question closes forever) is the twin
  the bound imports: the withdrawal path now gets the same convergence the answered path already had, so
  the two are consistent rather than in tension. INV-9 (a withdrawn pick re-asks in plainer terms, and mode
  and trust move only on the human's word) is bounded, not overridden — the human still owns the decision,
  and after two withdrawals the recommended option carries only as a `[default]` he can still tweak, which
  is exactly INV-31's silence-is-consent contract, not a decision made against him. INV-31 (a default is
  told, never asked; silence stays consent) is the mechanism the converged pick uses.
- No new surface and no new state beyond the withdrawal count, which is read from the decision archive's
  existing answered-then-withdrawn log — no new store. A later genuine change of mind is routed as a new
  wish, closing the loop without reopening the settled decision, consistent with the no-question-asked-twice
  law [INV-59].

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
