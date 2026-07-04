# Findings from the tlvphoto adopt run + a later re-read

Source: the tlvphoto host (first real adopt run, 2026-07-04) and a follow-up session that
re-read the package at SPEC v0.3 and cleaned up / set up the host remote. Read-only outsider —
these are wishes, not edits. Three package gaps surfaced, each with a primary source.

## 1. Adopt writes .gitignore but never actually sets up the remote INV-8 recommends
A-5 does git init + baseline commit + .gitignore, and INV-8 says a remote is "recommended"
before the first landing — but nothing in the sequence MAKES the remote happen, so the run
ended with the host local-only. Proof: after the adopt run tlvphoto's `git remote -v` was
empty; a later session (this one) had to create the GitHub remote by hand, on Alexander's ask.
Wish: make "remote exists (or explicitly declined)" a named adopt deliverable, or a first-landing
guardrail that flags a local-only host — so the backup INV-8 wants is not left to chance.

## 2. Adopt working artifacts have no specified home
The run produced `adopt_orient_digest.md`, `adopt_inventory.md`, `adopt_reconcile.md`. A-1..A-3
name these outputs but not WHERE they live, so they landed in the host's `data/` and are now
git-tracked product clutter. Proof: `git ls-files` in tlvphoto lists `data/adopt_*.md`.
Wish: SPEC should pin an adopt-artifact home next to the other package state — proposal
`.livespec/adopt/` (gitignored like checkpoints, or tracked if we want the audit trail), so the
host root/product tree stays clean.

## 3. Adopt writes .gitignore but does not sweep pre-existing ignored cruft off disk
A-5's .gitignore correctly excludes heavy/generated files, but the files already sitting on disk
stay. After adopt, tlvphoto still carried ~25 MB `review.zip`, ~700 KB of `*.log`, `.DS_Store`,
and `__pycache__` — junk the gitignore names but nobody removed until a later hand-cleanup.
Proof: `git status --ignored` listed them present post-adopt.
Wish: A-5 could add an optional sweep — surface the list ("N ignored files, M MB — remove?")
and, on the human's ok, delete the clearly-regenerable cruft. Never silent; never touching
anything not already ignored.
