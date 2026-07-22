# GAPS — source holes found during the rewrite

These are places where the source section states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. Neither of these blocks the rewrite; each is a question the source owes.

## New holes

### G1 — the delegation accounting's "saving" has no unit or baseline
**Where:** Requirement 12, criterion 1. Source: the delegated-work accounting, `PRODUCT_SPEC.md` line 1764, `[INV-103]`.
**Hole:** Every delivered row records how its work was delegated — "the unit that went to a worker with a rough saving." The source names a saving figure but never states what the saving is measured in or against: tokens, wall-time, or money, and relative to what baseline (the senior doing the work itself, or the next tier up). The sibling half of the line — why the senior kept a stood-down unit — is a plain reason; this saving is the unfilled slot.
**What it blocks:** A reader cannot tell what a correct saving figure looks like, and a test author cannot pin the accounting line's value or assert a boundary case, so the check can only confirm the line exists rather than that its number is honest.

### G2 — the expensive-decision read's model tier is unstated
**Where:** Requirement 17, criterion 3. Source: the expensive-decision adversarial read, `PRODUCT_SPEC.md` line 1785, `[INV-235]`.
**Hole:** The read "run at the best tier the pack's quality habit sets." The source names a determiner — the pack's quality habit — but neither defines that quality habit in the spec nor states which tier it yields for this read, so the read's model tier out of the box is unstated. It parallels the verify audit, whose own tier the source likewise leaves to the same habit.
**What it blocks:** A host running an expensive-decision read before the quality habit is pinned cannot know which tier the read runs at, and a test author cannot pin the tier the read is expected to use; the "best tier" reads as an intent rather than a checkable value.

## Note on scope

These two are the genuinely new holes this section opens. Several other numbers in the section are host-settable or defaulted *by design* and are not holes, because the source states their default: the worker heartbeat interval (near 60 seconds), the liveness and stall bounds (near 30 seconds and near 2 minutes), the brief size bound (about 300 lines and about 8 files), and the economy pressure default (full). Each of those names both a default and the human's power to change it, which is a complete answer rather than a hole. The router's "airtight brief" condition is likewise not a hole: the source defines it as a brief that "leaves the worker nothing to decide."
