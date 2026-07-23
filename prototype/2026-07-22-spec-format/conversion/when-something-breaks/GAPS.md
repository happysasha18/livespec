# GAPS — source holes found during the rewrite

This is the place where the source section states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. It became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. The hole does not block the rewrite; it is a question the source owes.

## New holes

### G1 — RETIRED as false (row-445 audit, F1): a bug's critical priority is decided by the intake classification
**Where it stood:** Requirement 1, criterion 3. Source: when a bug cuts the line, `PRODUCT_SPEC.md` lines 1077–1078, `[T-9]`.
**Why retired:** The hole read the bug section alone. The intake classification (assembled R9.4, [INV-12]) states the measure in full — a wish is critical *when* the shipped product is broken for its user: an unusable surface, lost data, or a violated safety gate — and the audit's F1 named this the one false GAP of 42. The GAP line is deleted and R1.3 sharpened to cite INV-12's three conditions directly, so the waiting line's order reads its measure from the classification's one home.

## Note on scope

This is the one genuinely new hole this scenario section opens. Several other numbers and choices in the section are counted, human-owned, or defined *by design* and are not holes, because the source states both the rule and where the value or verdict lives: the two-strikes ladder (a first sighting recorded, the second occurrence buying an owner, a third unowned recurrence escalated), the parked-feature bound (at most one per lane), the no-problem verdict (the human's alone, on the human's dated word), and the archival trigger (the milestone compaction). Each names a concrete threshold or a named owner, a complete answer rather than a hole.

### G2 — the second-occurrence branch has no stated measure
**Where:** Requirement 4, criterion 3. Source: the problem-ledger walk, `PRODUCT_SPEC.md` ~line 1111, `[INV-23]`.
**Hole:** At a signature's second occurrence the system opens a queue row for a problem that needs solving or writes a no-problem recommendation for noise; the source names the seat's own read as the chooser and the human as the settler, and gives no measure separating the two branches.
**What it blocks:** Two sessions can branch the same signature differently; a test author cannot pin the boundary case.
