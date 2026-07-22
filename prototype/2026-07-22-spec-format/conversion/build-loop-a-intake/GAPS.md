# GAPS — source holes found during the rewrite

These are places where the source states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. Neither blocks the rewrite; each is a question the source owes.

## New holes

### G1 — the "quick win" priority mark names no measure
**Where:** Requirement 6, criterion 4. Source: the classification rule, `PRODUCT_SPEC.md` lines 96–98, `[INV-12]`.
**Hole:** Priority carries two marks. Critical is given three concrete conditions — an unusable surface, lost data, or a violated safety gate — each checkable. Quick win is given only two qualitative phrases, "low effort" and "immediate value" (plus "no design decision inside", which is checkable). The source names no measure or threshold that separates a quick win from a normal wish: what counts as low effort, and against what value it is weighed, are unstated. The nearest judge, the classifier asking the person at intake when it cannot call a priority `[INV-12]`, is named — but the person is handed no measure either.
**What it blocks:** A classifier cannot decide the mark on its own without a measure, so a quick win is settled only by a human judgment the source does not scope. A test author cannot pin the boundary case that separates a quick-win wish from a normal one.

### G2 — the large-wish trigger names no measure of a wish's "worth"
**Where:** Requirement 7, criterion 2. Source: the scope-negotiation rule, `PRODUCT_SPEC.md` line 102, `[T-15]`.
**Hole:** The scope negotiation opens "when a wish is larger than its worth". The comparison has two slots and the source fills neither: a wish's worth carries no measure, and the comparison names no judge. The sibling axis is concrete — the walk is explicit that time is never the input and scope is the only lever — but the trigger that starts the negotiation rests on an unquantified "worth".
**What it blocks:** The walk cannot mechanically decide when a wish crosses from proportionate to oversized, so the negotiation either never opens or opens on an unstated judgment. A test author cannot pin the point at which the cut-or-stage proposal must fire.

## Note on scope

These two are the genuinely new holes this unit opens. Several other numbers and judgments in the unit are complete answers rather than holes, because the source states both a default and, where relevant, the human's power to change it: the withdrawal-convergence bound (two withdrawals, then a surfaced `[default]`), the heartbeat's beatless bound (~10 minutes) and the detached-run cadence (~2 minutes), the long-work explanation threshold (an hour or more), and the four-word size vocabulary and the nine fixed pipeline steps, which are enumerated in full. Each of those names its measure, so none is recorded as a gap.
