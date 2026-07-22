# GAPS — source holes found during the rewrite

This is the place where the source section states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. It became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. The hole does not block the rewrite; it is a question the source owes.

## New holes

### G1 — a bug's critical priority names no judge or measure
**Where:** Requirement 1, criterion 3. Source: when a bug cuts the line, `PRODUCT_SPEC.md` lines 1077–1078, `[T-9]`.
**Hole:** An arriving bug, "critical included," joins the waiting line, and "waiting bugs order critical-first; bugs of equal priority go by arrival." So a bug carries a priority with critical as a level, and the ordering of the waiting line turns on it. The source names no judge and no measure for that priority — who marks a bug critical, and by what test a bug is critical rather than ordinary, is unstated. The source T-9 index row repeats the preemption behaviour without defining the level either.
**What it blocks:** The waiting line cannot be ordered without knowing how a bug's priority is set, so the order either leans on an undeclared rule or asks the human each time. A test author cannot pin the case that separates a critical bug from an ordinary one, and cannot check that critical-first ordering fires correctly.

## Note on scope

This is the one genuinely new hole this scenario section opens. Several other numbers and choices in the section are counted, human-owned, or defined *by design* and are not holes, because the source states both the rule and where the value or verdict lives: the two-strikes ladder (a first sighting recorded, the second occurrence buying an owner, a third unowned recurrence escalated), the parked-feature bound (at most one per lane), the no-problem verdict (the human's alone, on the human's dated word), and the archival trigger (the milestone compaction). Each names a concrete threshold or a named owner, a complete answer rather than a hole.

### G2 — the second-occurrence branch has no stated measure
**Where:** Requirement 4, criterion 3. Source: the problem-ledger walk, `PRODUCT_SPEC.md` ~line 1111, `[INV-23]`.
**Hole:** At a signature's second occurrence the system opens a queue row for a problem that needs solving or writes a no-problem recommendation for noise; the source names the seat's own read as the chooser and the human as the settler, and gives no measure separating the two branches.
**What it blocks:** Two sessions can branch the same signature differently; a test author cannot pin the boundary case.
