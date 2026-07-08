# 0.9.0 milestone — preventive audit (2026-07-08, autonomous loop)

Three read-only audit passes ran in parallel (skill craft lens · doc-compaction candidates · thin-loader +
open-gates + formal-index). Below: what each found, and the disposition. The full spec re-prove already ran
today (`docs/prover/2026-07-08-humanize-whole-doc.md`).

## Folded this session (safe, mechanical / factual)

1. **communicator SKILL.md — rule count fixed.** Intro said "Seventeen rules" while the section header and
   body carry twenty-two. Changed the intro to "Twenty-two rules". (The register's "Fourteen rules" count is
   correct, left as-is.)
2. **product-prover SKILL.md — formatting.** Collapsed a double blank line before "Write the way a senior
   reviewer talks."
3. **ARCHITECTURE.md — intro de-duplicated.** The standalone "When this doc changes" paragraph (introduced
   in today's DEC-2 rewrite) restated the "kept current by assignment" paragraph. Merged its one distinct
   clause (large/surface wish updates before the matrix) into the first paragraph and dropped the duplicate.
   No anchor moved.
4. **spec-author SKILL.md — description gained its "when NOT" boundary.** The triggering description had no
   negative clause (every sibling does), so it could over-trigger on review / retro-doc / prototype asks.
   Appended: NOT for reviewing (product-prover's half), retro-documenting built code, or an unfenced sketch.

Suite 176 green after the folds; three skills re-synced to the installed copies.

## Deferred to their own station (bigger mechanical compaction — next loop ticks)

5. **ROADMAP.md — archive ~65 terminally-landed rows.** The active table holds ~106 rows; ~65 carry a
   terminal `landed` status with no open leg and belong in `docs/queue-archive/` (INV-1: archive, never
   delete). Rows that STAY (open field/first-run leg, waiting, in-work, queued, deferred, [target]): 27, 33,
   42–44, 48, 49, 54, 55, 69, 93, 95, 96, 99, 100, 108, 117–119, 128–131, 133–136, 140, 141, 143, 144, 148,
   163, 165, 166, 168, 170, 171. This is the milestone's queue compaction; do it as a dedicated tick with a
   dated archive file so no row reference breaks.
6. **SPEC.md — collapse the four decided items in "Open decisions".** Only D-1 (attic layout) is genuinely
   open; D-2/D-3/D-4/D-5 open "Decided 2026-07-05/07…" and carry full dated rationale that belongs in
   JOURNAL. Collapse each to a one-line resolved pointer (KEEPING the anchor — D-2/D-3/D-4 are cited
   elsewhere), move rationale to JOURNAL. Touches SPEC, so it re-runs under the milestone re-prove.

## For Alexander's word (his personal config, not the pack repo)

7. **Thin loader (`~/.claude/CLAUDE.md`) — 21 lines, close to thin.** One real migration finding: bullet 1's
   named-window list ("live-spec, track-coach, tlvphoto") and the "live-spec runs on Fable only" note are
   personal/environment facts, not bootstrap preconditions — they belong in the personal profile, not the
   global loader. Bullet 3's trailing method detail ("a non-trivial change goes through build-pipeline; the
   shared rules live in live-spec-base") restates pack rules. NOT auto-edited: this file is his personal
   layer (git home = the playbook repo), and its migration is his call.

## Verified clean / confirmed

- **Inbox:** clean (only README.md).
- **Formal index ↔ prose:** no drift — every prose anchor resolves to an index row and back; every index
  Section value resolves to a real heading. (Cosmetic only: a few Section labels are written two ways —
  "Machines" vs "The machines that hold the bounds" — all resolving correctly; normalization not worth the
  risk this pass.)
- **Open human gates** (correctly NOT autonomous): rows 166 (board round 2), 148 (genre Phase 3), 170
  (pre-show lint priority), 171 (no-hooks/no-GitHub generalization). All need his word. (The gates pass
  mis-cited rows 121/122 here — both are cleanly landed since session 12, verified at compaction time.)
- **Skill drift (INV-13):** no clear re-legislation of a base rule; build-pipeline's tripwire re-listing is
  borderline but cites base rule 15 and is the door's operational skill — left.

## Optional, low-value — skipped this pass (noted)

- SPEC worker-tier meanings enumerated in both the roster (§Who decides) and INV-69 — the roster could
  point to INV-69 for meanings. Low value.
- SPEC INV-24 stacked catch-count tallies could move to JOURNAL, but several are tested phrase-needles;
  left to avoid churn.
