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

### G3 — the bounded glance carries no numeric size bound
**Where:** Requirement 13, criterion 2. Source: the reading discipline, `PRODUCT_SPEC.md` ~line 1766, `[INV-137]`.
**Hole:** The glance that stays with the orchestrator is bounded as "one small file, or a handful of targeted lines whose result is itself the deliverable"; the source gives the operative test (the result is the deliverable) and no number for "small" or "handful", while the neighbouring worker-brief bound is numeric (about 300 lines, at most about 8 files).
**What it blocks:** Two sessions can draw the keep-or-dispatch boundary differently on the same read; a test author cannot pin the boundary case.

### G4 — the bounded decide-read's "small edit" carries no size measure (Requirement 13)
**Where:** Requirement 13, criterion 4. Source: the reading discipline, `PRODUCT_SPEC.md` ~line 1766, `[INV-53, INV-137]`.
**Hole:** The brief-owed read of a change's files is dispatched to a reader worker "or" made "a bounded decide-read for a small edit." The source names the fork — dispatch versus a direct decide-read — but gives no size or line count for the small edit that earns the direct read, distinct from the neighbouring glance bound (G3), which at least states its operative test.
**What it blocks:** A test author cannot pin where a dispatched read is owed and where a direct decide-read is legal; two sessions can draw that line differently on the same edit.

### G5 — the bounded decide-read's "small edit" carries no size measure (Requirement 19)
**Where:** Requirement 19, criterion 3. Source: the brief-authoring discipline, `PRODUCT_SPEC.md` ~line 1795, `[INV-53, INV-137]`.
**Hole:** The same fork as G4 recurs where a brief's own files-to-touch read is dispatched or made "a bounded decide-read for a small edit"; the source gives no size or line count here either.
**What it blocks:** The same boundary case G4 leaves unpinned recurs at this second occurrence of the clause.

### G6 — the tight rung's "small deliveries" carry no size or count bound
**Where:** Requirement 22, criterion 5. Source: the economy ladder's tight rung, `PRODUCT_SPEC.md` line 1824, `[T-19, INV-39]`.
**Hole:** The tight rung lets "consecutive small landings share one full-suite run at the batch's end." The source names the mechanism — batching, a batch-end run, a bisect on red — but no size or row count for the "small" deliveries that qualify to batch.
**What it blocks:** A test author cannot pin which deliveries batch and which stay on their own full-suite run; two sessions under the tight rung can batch differently on the same queue.

### G7 — the reason-category set differs between prose and net
**Where:** Requirement 15, criteria 2 and 4. Source: the deferral clause, `PRODUCT_SPEC.md` ~line 1770, `[INV-152]`.
**Hole:** The prose names three human-only facts (a taste, a policy, an act irreversible outside git); the mechanical net's category list adds device-feel as a fourth. The source never states whether device-feel is a fourth member or a named subtype of taste.
**What it blocks:** A reader cannot state the closed set's size; a page naming device-feel passes the net while the prose's three-member list disowns it.
