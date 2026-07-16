# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-16 ~16:38 — post-2.1.1 docs landing: the outside review folded)
An outside adversarial review of the prover (relayed by Alexander) landed docs-only: the
prover/design-reviewer boundary homed in "When NOT to use", the description trimmed to its trigger,
the paired-transition kind-split moved to its lens, README refreshed to 2.1.1 (two-tier stress
structure), FEEDBACK.md born, row 360 queued (mirror release history). Suite 934 green; skill-creator
review clean; record docs/prover/2026-07-16-prover-doc-restructure.md; mirror re-synced after push.
Prior state below stands.

## PRIOR STATE (2026-07-16 ~15:48 — v2.1.1 SHIPPED)
VERSION 2.1.1 pushed (`be70e35`): rows 354/356/357/358 — the story and per-row detail live in
JOURNAL.md's v2.1.1 chapter and the ROADMAP rows. Installed copies on this machine re-synced to
2.1.1, update watcher calm.

## ON RESUME — the queue
- **Row 359 — matrix-names-real-tests extractor:** truncates at the `.` in a `(tests/test_x.py)`
  parenthetical; teach it the file-path form, re-verify M-146.
- **Row 360 — public mirrors carry a readable release history:** sync-mirrors.sh stamps a short
  per-release story (or a generated CHANGELOG.md) into each mirror; the surface's form is the
  owner's taste call.
- **Adoption follow-through (his windows):** tlvphotos — ratchet wired and live (checked 15:07).
  promoter — manifest present, `guardrails/pre-push` absent: the wiring step is unfinished there
  (its own window's work). track-coach — adopted with a local hand-fix that matches the pack's
  row-358 fix; after the 2.1.1 push its update watcher will propose the re-install roads.
- After the 2.1.1 push, hosts that adopted at 2.1.0 see the update watcher name the stale
  vendored files and the per-kit re-install road; each window re-installs on its own word.

## Standing word / OWNER-HELD
- Do the whole movement solo, push on green; plain English in docs, plain Russian in chat. Gates
  mandatory everywhere.
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never `git add -A`;
  re-check HEAD before writing (fence). A co-located deposit is the FILE ALONE — no staging, no commit
  (INV-174); the commit-time fence also stops a staged file carrying unstaged edits (INV-175).
- Next free codes: INV-181, M-338, next ROADMAP row 361. Memory can be wiped once pushed — story in
  JOURNAL.md (v2.1.1 chapter + the 16:38 outside-review chapter) + the 2026-07-16 records.
