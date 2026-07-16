# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-16 ~15:20 — v2.1.1 landing in progress)
VERSION 2.1.1 (PATCH: bug fixes + changed vendored scripts). Rows 354/356/357/358 all LANDED in the
working tree; commits + prover re-check + push are the session's remaining steps. What landed:
row 354 — ARCHITECTURE register folded (3 errors → 0), LICENSE allowlisted, ARCHITECTURE.md joins the
convergence-lock floor; old-vs-new meaning-diff accepted the sweep. Row 356 — the five 2.1.0
leftovers: pins strict-clean (52), FEATURE-FIT record homed (INV-156), extensionless-shebang sweep
(muted-launch gate), `adopt/install-scaffold.sh` (one-command scaffold attach, merged manifest),
INV-180 installed-copy drift-net class (attach node, M-336). Row 357 — the stranger-echo decision
(Alexander 14:40): echo comment on the source Issue at harvest, Issue closed at terminal exit
(INV-147 + INV-27, M-337). Row 358 — track-coach's field bug: the ratchet installer now wires the
gate at a safe anchor with a stable marker, repairs a stranded block on re-run, merges the manifest,
and the watcher names the re-install road per kit (9 fixtures red on old code). Suite 934 green
pre-close-out. Records: the three 2026-07-16 gate files + JOURNAL's v2.1.1 chapter.

## ON RESUME — the queue
- **Row 359 — matrix-names-real-tests extractor:** truncates at the `.` in a `(tests/test_x.py)`
  parenthetical; teach it the file-path form, re-verify M-146.
- **Adoption follow-through (his windows):** tlvphotos — ratchet wired and live (checked 15:07).
  promoter — manifest present, `guardrails/pre-push` absent: the wiring step is unfinished there
  (its own window's work). track-coach — adopted with a local hand-fix that matches the pack's
  row-358 fix; after the 2.1.1 push its update watcher will propose the re-install roads.
- If this session died before push: run the pre-push gate, the prover re-check
  (record `docs/prover/2026-07-16-2p1p1-prepush.md` — if absent, the pass never ran; run it),
  re-bless the freeze baseline (`python3 scripts/spec-freeze.py --freeze PRODUCT_SPEC.md
  ARCHITECTURE.md TEST_MATRIX.md --compaction`), then commit (inbox deposit first, then the
  landing removing it) and push. Checkpoint: `.live-spec/checkpoints/2026-07-16-rows356-354.md`.

## Standing word / OWNER-HELD
- Do the whole movement solo, push on green; plain English in docs, plain Russian in chat. Gates
  mandatory everywhere.
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never `git add -A`;
  re-check HEAD before writing (fence). A co-located deposit is the FILE ALONE — no staging, no commit
  (INV-174); the commit-time fence also stops a staged file carrying unstaged edits (INV-175).
- Next free codes: INV-181, M-338, next ROADMAP row 360. Memory can be wiped once pushed — story in
  JOURNAL.md (v2.1.1 chapter) + the three 2026-07-16 gate records.
