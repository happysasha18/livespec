# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 ~23:29 — the 2.0 readability + compaction movement, IN PROGRESS on a clean green base)
The 2.0 release rewrites the living docs to read plainly and stay compact, with a machine that proves no
rule's meaning breaks, and turns the cleanup into a push-gate so no project re-bloats again. Version is
still 1.10.1; 2.0.0 is cut at the very end. Suite 809 green; spec-freeze green; style errors 154 → 119.

**Committed on main (5 checkpoints):**
1. INV-163 minted — the ship-the-shape / host-owns-the-instance split as one rule every site cites
   (ROADMAP 332); full adversarial audit ran (docs/prover/2026-07-15-332-inv163-audit.md).
2. Inbox harvested (3 wishes); INV-162 sharpened for cross-session browser kills (ROADMAP 335).
3. The safety machine: `scripts/spec-freeze.py` (freezes/verifies anchor counts, marker lines, numbers,
   paths; use `--compaction` for index/row work) + `docs/spec-compaction-protocol.md` (the Fable-hardened
   meaning-preservation protocol). style-lint gained the acronyms DOM/PID/OS/CDN/CDP.
4–5. All 68 duplicate Formal-index mega-rows compacted to one-liners (batch 1 by hand, batch 2 by Fable).
   Each rule's full law is unchanged in its prose clause; 8 traceability needles re-pointed
   (docs/restyle-repoint-log.md).

## REMAINING (ordered) — the movement is NOT done. Work solo with Fable per docs/spec-compaction-protocol.md.
Gate EVERY batch: `spec-freeze --compaction` + the full suite + style/redundancy not worse. Commit green
batches. Keep docs/prover/2026-07-15-2.0-movement.md fresh so Gate A passes (same commit as the spec change).

1. **Prose readability of PRODUCT_SPEC** — rewrite the ornate prose clauses to short plain sentences (clears
   the ~59 remaining prose style errors + general readability). Fable clean-writer per section; preserve
   every check-phrase (`.2.0-work/check_phrases_spec_only.txt`, 849 of them), every anchor, and every rule's
   meaning. Target: `scripts/spec-style-lint.py --gate PRODUCT_SPEC.md` = 0 errors.
2. **Redundancy → 0** — `scripts/spec-redundancy-precheck.py` (21 candidates) + `scripts/spec-judge.py`;
   dedup or dated waiver. Target: `scripts/spec-done-gate.py PRODUCT_SPEC.md` GREEN.
3. **The other living docs** — same safe pass on ARCHITECTURE.md, TEST_MATRIX.md, ROADMAP.md (archive landed
   rows to docs/queue-archive/), and the skill docs. NOT JOURNAL.md (dated history, stays). English only, no
   Cyrillic, no verbatim quotes (paraphrase + date) — scrub the Russian quotes in ROADMAP landed rows.
4. **The gates (the recurrence-stop — what the owner cares most about)** — wire into the push gate:
   spec-freeze verify, the style floor + redundancy floor with the monotonic ratchet
   (`scripts/spec-debt-cap.json`), and a new Cyrillic / no-quotes check for the shipped docs. So a doc can
   only get cleaner, never worse, in every project that adopts the pack.
5. **The method (task 6)** — bake into build-pipeline + a new spec invariant: compaction is a station run
   EVERY pass (not milestone-only), and the principle "anything a machine can verify is a gate, not a habit"
   (a quality left to attention is a defect of the method). It reaches all projects through the pack.
6. **Capstone before 2.0** — (a) the mechanical done-gate green (style 0, redundancy 0, anchor set identical,
   suite green, freeze green); (b) a fresh adversarial Fable read of the WHOLE old spec vs the new, both
   directions (no rule weakened or dropped, no invented law); (c) cross-doc consistency: the traceability
   suite + an architecture-lens prover pass; (d) spec↔code reconciliation (the suite asserts real artifacts;
   re-verify the architecture pins). This answers the owner's question "how do we know nothing broke".
7. **Cut 2.0.0** — VERSION + plugin json + spec header; MIGRATION.md 2.0.0 chapter (host action: none — a
   readability + compaction pass, no runtime change); close ROADMAP 332 + add the movement's landed row;
   diary JOURNAL.md; compact MEMORY.md index (hook flags it > 19 KB); push on green.

## Resume procedure (cold session)
- Read this file + `docs/spec-compaction-protocol.md` first.
- The safety inventory survived /clear in `.2.0-work/` (check_phrases_spec_only.txt, redundancy_map.md,
  section_map.md, anchors.txt, compacted_rows.json, compact_constraints.json). Regenerate the freeze
  baseline from the pre-compaction commit: `git show <pre-movement commit>:PRODUCT_SPEC.md` → freeze it as
  the baseline (see the batch-2 note in the rolling record for how it was done).
- Owner's standing word (2026-07-15): do the WHOLE movement solo with Fable, don't ask, don't show chunks;
  plain English in docs, plain Russian in chat (NO internal jargon — he could not follow it); version bumps
  are not owner-reserved; push on green. He lost two manual days last week to spec bloat — the machine and
  the gate exist so it never recurs.

## Standing habits / OWNER-HELD
- Memory can be wiped — the story is in JOURNAL.md + docs/prover/ + docs/spec-compaction-protocol.md + here.
- Next free codes: INV-164, M-313, E-31, T-22 (INV-163 + M-312 used; ROADMAP rows 332 open, 335 landed).
