# Skill review — build-pipeline (skill-creator review of the row-480 archive-move reteach)

`SKILL-REVIEW`

Skill: build-pipeline
Date: 2026-07-23
Reviewer: skill-creator review, applied over the delta at ROADMAP row 480 (the live-body law, SPEC
INV-276 — a closed queue row moves from the queue's body to the month's archive file in its own closing
commit).

Verdict: pass — both re-taught passages agree with the shipped SPEC law and the suite that reads it; no
contradiction with the rest of the skill, no stale "status cell" wording left anywhere in the skill
tree, and the frontmatter (description, triggers, metadata) is untouched so no re-trigger analysis is
owed.

## What changed

Two spots in `skills/build-pipeline/` re-teach the same law — a landed/declined/superseded row's
delivery report (including its delegation-saving line) now rides the row into the monthly archive file
at the same closing commit, rather than staying findable only via a "status cell" in the live queue body:

- `SKILL.md`, the trains/one-pen paragraph (SPEC T-18, INV-39): gains one clause — "that same closing
  commit moves the row from the queue's body to the month's archive file with its delivery report (the
  live-body law, SPEC INV-276)" — inserted between the pen-stage sentence and the re-fence sentence.
- `SKILL.md`, the junior-delegation paragraph (SPEC INV-69): "recorded in the landed row's status cell"
  becomes "in the row's delivery report, checked by suite and moved to the archive with the row by the
  closing commit (SPEC INV-103, INV-276)".
- `references/delegation-protocol.md`, the "every delegation reports its saving" passage: same swap,
  "the line lives in the landed row's status cell, and a suite check reads it" becomes "the line lives
  in the row's delivery report, which the closing commit moves to the archive with the row, and a suite
  check reads it from the archive" (SPEC INV-103, INV-276).

## Check walked

- **Frontmatter/triggers untouched** — `git diff HEAD~8` touches only body prose in the two files
  (7 insertions/2 deletions in SKILL.md, 5/2 in delegation-protocol.md); the `description:` block and
  `name:` are byte-identical to before. No re-trigger analysis owed.
- **Size** — 8 net lines added across two reference-sized files; not a materially different skill.
- **Agreement with SPEC** — PRODUCT_SPEC.md INV-276 (the queue rows, e.g. R5.1/R209.1/R287.1) states
  exactly this: a terminal-exit row moves verbatim, delivery report riding with it, to the archive in
  the same closing commit (line 6588), and the INV-103 requirement (line 4769) already reads the
  delegation line "from the archive" — the skill's reworded text is not a new claim, it is catching the
  skill body up to a law the spec already carries.
- **No orphaned wording** — grepped the whole `skills/build-pipeline/` tree for "status cell": zero
  hits after the edit (was the retiring phrase in both spots). "delivery report" now names the one home
  consistently across `SKILL.md` and `references/delegation-protocol.md`.
- **Suite agreement** — `tests/test_delegation_line.py` (`TestDelegationLineLaw.test_law_in_both_homes`)
  pins four literal needles against the whitespace-flattened `SKILL.md` (which `read_all_flat` folds
  together with its `references/` files): "the row's delivery report", "a suite check reads it from the
  archive", "a delivered row without the line goes red", "binds the orchestrator seat regardless of".
  Verified directly (`read_all_flat` call) — all four are present in the reworded text. Ran
  `pytest tests/test_delegation_line.py`: `test_law_in_both_homes` and `test_spec_anchor_and_index` both
  pass. The third test in the file, `test_every_forward_landed_row_carries_the_line`, fails — but on
  ROADMAP row 445's status cell missing the word "delegation" in the live queue body, a pre-existing
  data gap unrelated to either changed passage (confirmed by reverting `skills/build-pipeline/` alone to
  its HEAD~8 state and finding the failure is not caused by the two prose changes under review; the
  file's own `_queue_lines()` docstring already documents the archive-union read this delta describes).
  Out of scope for this record — it names a queue-row data fix, not a skill-body defect.
- **Coherence** — both passages read as one continuation of their surrounding sentence, not a bolted-on
  clause; the trains/one-pen insertion sits between the two sentences it bridges (pen-stage discipline →
  archive move → re-fence), and the delegation-protocol.md sentence keeps its original clause order
  ("the line lives in X, and a suite check reads it") with only X's referent updated.

none fix-worthy — no suggested edit for the orchestrator to apply. The row-445 status-cell gap is noted
above for the queue owner, not this skill review.
