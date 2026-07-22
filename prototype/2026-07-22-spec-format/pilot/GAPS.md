# GAPS — source holes found during the rewrite

These are places where the source section states a behaviour but leaves a judge, a measure, or a scope unanswered. Each became a `[GAP]` line under its criterion in `section.md`. Inventing the missing answer is forbidden; the gap line is the correct output. None of these blocks the rewrite; each is a question the source owes.

## New holes

### G1 — the scaffold's "live-state block" has no defined content
**Where:** Requirement 2, criterion 6. Source: the bootstrap scaffold, `PRODUCT_SPEC.md` ~line 1175–1181.
**Hole:** The scaffold's green requires "one live-state block", but the source does not state what that block must contain for the suite to count it present. The other three scaffold checks are concrete (document set exists, headers filled, coverage checklist present); this one names a thing without defining it.
**What it blocks:** A test author cannot write the presence check without knowing what a live-state block is. Related: the "coverage checklist" is named as a required artifact but its required contents are also unstated, so the same ambiguity touches criterion 4.

### G2 — no judge or measure for "content and mechanism can no longer share one file"
**Where:** Requirement 5, criterion 7. Source: the engine/instance split, `PRODUCT_SPEC.md` ~line 1211, `[INV-85]`.
**Hole:** After a declined split, the offer returns only when the product "outgrows one home", one trigger being that "the content and the mechanism start fighting for the same file". The source names no judge for this condition and no measure of when two have started fighting for one file. The sibling trigger — "a second instance appears" — is observable; this one is not.
**What it blocks:** The system cannot know when to re-raise the split offer on this arm, so the re-offer either never fires on it or fires on a subjective read.

### G3 — a bootstrap founding that omits layers or proofs is not said to be flagged
**Where:** Requirement 7, criterion 3. Source: concrete layers and proof kinds, `PRODUCT_SPEC.md` ~line 1229, `[INV-135, A-10]`.
**Hole:** A `project.kind` recorded with no declared layers and no declared proofs is "incomplete, flagged at adoption the way an unbacked surface is". The source names only adoption as the flagging moment. It does not say whether a fresh bootstrap founding that records a kind but omits its layers and proofs is flagged at founding, or whether such a host can pass founding incomplete and only be caught if it is later re-adopted or caught up.
**What it blocks:** The founding check's reach is undefined — a founded-but-incomplete host may sit unflagged until an unrelated adoption or catch-up run reads its profile.

## Pre-existing open decision encountered (not new)

### D-1 — the adoption attic's layout
**Where:** Requirement 12, criterion 5. Source: `[D-1]`, `PRODUCT_SPEC.md` ~line 1287.
This is already a recorded open decision in the source (flat folder with a manifest and a source-directory prefix on collision, against dated subfolders), left open until a real adoption run forces the choice. It is listed here for completeness because it surfaced during conversion, but it is a known open decision, not a hole the rewrite discovered.
