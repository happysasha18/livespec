# Inbox sweep worker checkpoint — ROADMAP rows 257-260

Briefed: 2026-07-12, applier role, mechanical landing from .live-spec/checkpoints/pending-inbox-sweep.md.
Write-set fixed by the brief, plus one orchestrator-ordered addition (working-material clause in rows
259/260) and one deviation forced by live file state (see below).

## Write-set
- .live-spec/checkpoints/inbox-sweep-worker.md (this file)
- ROADMAP.md (insert rows 257-260 after row 256)
- inbox/2026-07-11-from-tlvphotos-architecture-rework-owes-document-rework.md -> docs/queue-archive/ (git mv + pointer line)
- inbox/2026-07-12-from-tlvphotos-restructure-merge-gate-needs-a-stated-law.md -> docs/queue-archive/ (git mv + pointer line)
- inbox/2026-07-12-from-alexander-design-principles-impact-analysis-and-compaction.md -> docs/queue-archive/ (plain mv + fresh add — see deviation)
- .live-spec/checkpoints/pending-inbox-sweep.md (append APPLIED + CLOSED line)

## Anchor confirmed present before editing (2026-07-12)
- ROADMAP.md line 154: `| 256 | **A repeatedly-broken behavioural rule earns a live channel**` ...
  ending `... suite 400) | Done when: ... suite green — MET (both homes red-proven; the audit item
  cites the law; suite 400) |` — matches the draft's cited anchor text verbatim. Confirmed the row
  233/239/240/242 status-cell changes made after the draft was written do NOT touch row 256 or
  anything after it — anchor unaffected.

## Rows inserted
Rows 257, 258, 259, 260 pasted verbatim from the draft's "Drafted rows" table, in order, immediately
after the row-256 line (now ROADMAP.md lines 155-158).

**Orchestrator addition applied:** in row 259's and row 260's trailing parenthetical (the door/kind/map/
kin/born-of block), inserted before the closing paren, right after the `born-of:` clause:
`; working material: .live-spec/checkpoints/pending-design-principles-architect-draft.md (P0-P12) + the
wish file's two addenda`. Verified present exactly once per row via grep before writing the file.

## Retirements
- Wish 1 and wish 2 were tracked files with git history (ac133e9, da6e9e2) — retired with `git mv` to
  `docs/queue-archive/`, pointer lines appended (`> Harvested into ROADMAP row 257 (2026-07-12).` and
  `> Harvested into ROADMAP row 258 (2026-07-12).` respectively).
- **Deviation from the draft's literal `git mv` instruction:** wish 3
  (`inbox/2026-07-12-from-alexander-design-principles-impact-analysis-and-compaction.md`) showed up as
  UNTRACKED in `git status` at the start of this task (no commit ever added it — confirmed via
  `git log --all -- <path>` returning nothing). `git mv` requires a tracked source, so it was moved with
  a plain `mv` and will be added fresh at the new path in this commit; there is no old tracked path to
  remove. Content moved whole, including both ADDENDUM blocks (his word 2026-07-12 ~02:06 and ~02:08),
  confirmed present by reading the file before the move. Pointer line appended:
  `> Harvested into ROADMAP rows 259-260 (2026-07-12).` This is a file-state deviation, not an
  interpretation of the draft's wording — the draft could not have anticipated the file was never
  committed. No content lost; net effect (file lands at the archive path, inbox/ no longer has it) is
  identical to what `git mv` would have produced.
- Confirmed `.live-spec/checkpoints/pending-design-principles-architect-draft.md` exists (30079 bytes,
  2026-07-12) — the working-material citation in rows 259/260 points at a real file.

## Suite
Full suite after all edits: `python3 -m pytest tests/` -> `411 passed in 38.80s`, 0 failed. No
row-format test failure; the expected 411 count matched exactly (400 baseline + 3 no-silent-drop tests
already landed by row 233 + 3 live-channel tests already landed by row 256 + 5 more from intervening
landings — read the tail as-is, no need to reconcile the arithmetic since the number matched the brief's
own expectation).

## Status
DONE, 2026-07-12. All four rows inserted, all three wish files retired, suite green (411 passed), no
version bump (per instruction — queue bookkeeping, precedent da6e9e2). Commit and push are the next
steps outside this checkpoint's own scope.
