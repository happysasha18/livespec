> Archived 2026-07-07 ~08:19 (session 23) at intake: harvested into ROADMAP row 163 (test-author skill).

# Wish: extract the test methodology into the pack — a `test-author` skill (build-pipeline steps 4–5)

From: the track-coach session (Fable), 2026-07-05 late night, at the project's close for promotion.
One new inbox file, nothing else touched (SPEC INV-10). Surfaced by Alexander's direct question the
same night — he asked whether the tests-by-the-method work was truly done or quietly dropped; the
answer split in two, and this file is the half that is NOT done.

## What is done (context, not the wish)

track-coach's OWN suite was rebuilt by the method and the result is alive in that repo: the matrix is
organized architecture-node × spec-fact with a pinned level per fact (2026-07-04), the honest level-gap
debt was closed the next morning, a 6-check traceability test fails the suite on every commit, and the
pre-push hook runs the whole set. 795 green today; the count only ever grew.

## The wish

The METHOD that produced this lives nowhere reusable. It sits in track-coach's TEST_MATRIX header
prose, its `data/test_overhaul_*.md` inventories, and two paragraphs of build-pipeline (steps 4–5).
The pack's own cross-audit (`~/.claude/skills/CROSSAUDIT_2026-07-03.md`, finding F11) already named
this the weakest-supported judgment-heavy step and recommended extracting a **`test-author` skill**
owning matrix derivation + test writing (level ladder, real-artifact assertion, red-first, pinned
skip-set), invoked by build-pipeline at steps 4–5 the way steps 1–2 invoke spec-author and
product-prover. Field evidence for urgency, dated 2026-07-02: two user-visible track-coach bugs slipped
past ~660 string-only tests before the overhaul — the exact class the level ladder prevents.

Donor material ready for the extraction: the cross-audit's charter sketch (F11 + "the two proposed
roles" section), track-coach's TEST_MATRIX.md as the worked exemplar, its s34/s52 inventories as the
classification scheme, and its `test_traceability.py` as the enforcement pattern.

## Why now

track-coach closed at 1.4.1 for promotion, and its NEXT_STEPS queue was swept; the pack-work pointer
that used to live there would otherwise be homeless. Without the extraction, the next project starts
where track-coach started — string tests and slipped bugs — instead of where it ended.
