# GAPS — source holes found during the rewrite

These are places where the source section states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. Neither hole blocks the rewrite; each is a question the source owes.

## New holes

### G1 — the fix-sized / story-sized boundary names no measure
**Where:** Requirement 3, criterion 2. Source: the five routes, `PRODUCT_SPEC.md` line 969, `[T-20]`.
**Hole:** A fix-sized comment on shown work is fixed the same session, while a story-sized comment queues as a wish instead. The source splits the two by size but states no measure and names no judge for the boundary — how large a change, how many files, or whose call decides that a comment is fix-sized rather than story-sized. The route an item takes turns on this split.
**What it blocks:** A session cannot decide which comments to fix in place and which to queue without the boundary, so the routing either leans on an undeclared rule of thumb or asks the human every time. A test author cannot pin the case that separates the two routes.

### G2 — the reading of a strong reaction is deferred, with no measure
**Where:** Requirement 5, criterion 1. Source: the third arrow / feedback-collector, `PRODUCT_SPEC.md` lines 986, 990, `[E-30]`, `[INV-161]`.
**Hole:** The arm fires on a "genuinely strong reaction — a real delight, a real hurt, a comparably notable moment," and the source states outright that "the exact reading of 'strong' is a conservative floor here, its finer form a later design pass." So the measure that separates a strong reaction from a mild or routine one is named as deferred rather than given. The evaluative phrase "strong" carries no judge and no threshold.
**What it blocks:** The arm cannot decide when to offer the upstream note without the reading, so it either never fires or fires on an undeclared floor. A test author cannot pin the boundary case between a strong moment and a routine one.

## Note on scope

These are the two genuinely new holes this scenario section opens. Several other numbers and choices in the section are host-settable or human-owned *by design* and are not holes, because the source states both the rule and where the value lives: the feedback-collector's off-by-default flag (`feedback-upstream: off`, switched on only by a recorded profile line), the positive-consent gate (an explicit yes, asked every time), and the outbox's gitignored per-host home. Each names both a default and the human's power over it, a complete answer rather than a hole.

### G3 — the repeat-mention identity rule is unstated
**Where:** Requirement 1, criterion 5. Source: the feedback ledger's repeat-mention clause, `[INV-68]`.
**Hole:** A repeat mention appends its date to the existing line, and the source names no matching rule or judge for deciding that a new mention is the same item.
**What it blocks:** Two sessions can split or merge the same feedback differently; the criterion-6 promise that an item is never handed in twice cannot be tested at the boundary.
