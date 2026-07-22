# GAPS — source holes found during the rewrite

These are places where the source (lines 277–620) states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. Neither hole blocks the rewrite; each is a question the source owes.

## New holes

### G1 — the promotable "small wish" has no size boundary
**Where:** Requirement 3, criterion 1. Source: the quick-win promotion paragraph, `PRODUCT_SPEC.md` line 283.
**Hole:** "When the lane frees, the agent may take [a quick win] ahead of larger queued wishes, marking the promotion in its row." The source lets the agent promote a small wish ahead of larger queued wishes but never states the size boundary that makes a wish a promotable quick win, nor the measure separating a promotable wish from a "larger" one. Size is an intake axis, but its buckets and the promotable threshold are not stated in these lines. The judge (the agent) is named; the measure is not.
**What it blocks:** The agent cannot tell mechanically which queued wish is small enough to promote, so the promotion either never fires or fires on an undeclared judgment. A test author cannot pin the boundary between a promotable wish and a wish too large to jump the line.

### G2 — the "tiny" row that rides serial has no measure
**Where:** Requirement 46, criterion 4. Source: the lanes-picked-by-a-graph paragraph, `PRODUCT_SPEC.md` line 571, `[INV-49]`.
**Hole:** "Parallel pays only when build stages dominate the pen work, so tiny rows ride serial." The source rides tiny rows serial when build stages do not dominate the pen work but states no measure of when a row is "tiny" or when build stages "dominate". The seat judges independence and says so aloud, and the false-serialization lens is named the seat's own read rather than a gate — so the judge is named — but no threshold, ratio, or measured quantity separates a row that pays to parallelize from one that does not.
**What it blocks:** A session cannot decide mechanically whether a given runnable row is tiny enough to keep serial, and a test author cannot pin the boundary where parallelizing stops paying. The rule stays the seat's own read with no measured floor, which the source states is deliberate for the enforcement (a judgment is never a gate) but leaves unanswered for the read itself.

## Known hole this unit also records

### G3 — a wish's worth-versus-effort judge and measure are unstated
**Where:** Requirement 4, criterion 1. Source: the intake-line paragraph, `PRODUCT_SPEC.md` line 289, and the scope-negotiation paragraph, line 102, `[T-15]`.
**Hole:** "A wish too big for its worth is negotiated in scope, never in time." The source states that a too-big wish is renegotiated in scope rather than time, and names the two moves scope negotiation may take, but never states who judges a wish too big for its worth nor what measure separates a wish whose worth justifies its size from one that does not. Size and priority are stated intake axes with their own rules; worth-versus-effort carries neither a named judge nor a named measure in these lines. Unlike G1 and G2, this hole is not newly found here: an open queue row already tracks the scope-negotiation clause's missing judge, and this unit's own `[GAP]` line is that same known hole surfacing where the rewrite meets it.
**What it blocks:** A session cannot tell mechanically when a wish has crossed into too-big-for-its-worth territory, so the renegotiation trigger rests on an undeclared judgment. A test author cannot pin the boundary a fixture would need to prove the renegotiation fires at the right size.

## Note on scope

G1 and G2 are the two genuinely new holes this unit opens; G3 is a known hole an open queue row already tracks, surfaced here as its own `[GAP]` line rather than newly discovered. Several other numbers and judgments in the source are answered by design and are not holes:

- The lane cap (package default of three, a settings-ladder value the profile may move) names both a default and the human's power to change it — a complete answer.
- The design-review loop cap (three progressing rounds by default, host-settable) and the at-most-three-questions-per-pass bound each name a default and its owner.
- The tunable-knob default (Requirement 36) is left to the agent by design — the source names the judge (the walk) and its inputs (cheaper or faster wherever quality allows), so the per-knob value is a stated agent judgment, not a hole.
- The footprint, work-kind, and door sets are closed and enumerated, each member defined; the "presentation-only" / "single-module" / "cross-cutting" and "product / infra / skill / prose" definitions are stated in the source.
- The listener-tripwire's firing condition (a non-empty socket field) is a stated mechanical definition, not a hole.

Judgments the source deliberately leaves to a named human or seat — motion feel, whether two elements are one kind, the minor-versus-major call — are not holes either: each names its judge, which is the answer the format's law 4 asks for.
