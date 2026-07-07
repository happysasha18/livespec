# SPEC humanize — the reconciled migration plan (2026-07-07, session 24, fresh /clear)

Reconciles three deferred items into ONE movement, on Alexander's word (2026-07-07 ~14:30):
his ask #1 (human-first SPEC re-layout) · row 148 Phase 3 (whole-doc genre rewrite) · the 0.9.0
milestone (doc compaction + 3-pass preventive audit). His two live decisions this session:
depth = **deep** (break long sentences · move anchors to line-ends · clean coined metaphors ·
compress repeats) · timing = **reconcile all three into one plan first, then execute** (no section
reworked twice). This document is that one plan. Supersedes nothing; extends
`2026-07-07-genre-migration-plan.md` (row 148), which stays the record of Phases 1–2.

**Proven by Fable (2026-07-07, record: `docs/prover/2026-07-07-spec-humanize-plan.md`).** Verdict
READY-WITH-FIXES: the spine is real and the push gate backs it, but Fable found 5 MUST-FIX escape paths
(whole-doc needle matching vs "compress repeats" · backwards grep + missing extractor script ·
anchor-set diff proves presence not meaning · SPEC↔skill echo pairs · D4 missing the consumer
inventory) + 3 SHOULD. ALL folded below, tagged `MUST-FIX n` / `NICE n` at the fold site. Awaits
Alexander's go before batch 1.

## The reconciliation (why these are one movement, not three)

- **Ask #1 = row 148 Phase 3.** His 12:20 word on the genre doc already fused them: the genre rewrite
  is "better but not yet fully human", and the human-polish is a fresh-context job run as a tight
  «давай по-человечески» loop, smallest-first, his taste the bar. The "readability re-layout" and the
  "genre rewrite" are the same section-by-section pass. NEXT_STEPS' "overlapping but not identical"
  is resolved: one movement.
- **0.9.0 is served by it.** 0.9.0 = doc compaction + a 3-pass preventive audit. The deep readability
  pass IS the compaction (short sentences, cut repeats, cleaned metaphors shrink the doc). The 3-pass
  audit is a separate QA gate that runs AT the 0.9.0 landing, over the already-rewritten doc — it does
  not rewrite, it verifies. So: rewrite first (this movement), audit at the gate (0.9.0 close).
- **This is a reusable sub-skill of project migration** (his framing, ~14:33). The method below — a
  prose-genre migration that a mechanical needle-registry + anchor-set diff hold safe — is not
  live-spec-only. It crystallizes as a capability the pack can re-run on any host doc. tlvphoto is the
  first external application, in a SEPARATE process on his command (NOT this session, NOT this window).
  Deliverable D4 below is what makes it reusable.

## The load-bearing shapes — what a rewrite MUST NOT break (from row 148 Phase 1, verified today)

The push gate + suite already hold these; listed so every batch checks them consciously.

1. **Formal index**: `## Formal index` header; pipe table; anchor code in first cell; ranges like
   `T-1..T-7` legal; >40 anchors, unique; anchor sets equal across SPEC ↔ ARCHITECTURE ↔ TEST_MATRIX.
2. `[target]` tags stay inside index fact cells where they stand.
3. `## Open decisions`: `- ` bullets, literal `⟨DECIDE⟩` marker, each entry citing its `D-n`;
   `Decided` never precedes a live marker.
4. Header line format: `# live-spec — SPEC (vX.Y.Z, YYYY-MM-DD)`.
5. Bracketed anchors stay present in prose (`[T-9]`, `[INV-22]`, `[T-14, INV-19]`) — codes trail at
   line ends, unchanged.
6. Pipeline station list appears verbatim once: `spec → prove → architecture → prove architecture →
   matrix → test → code → verify → commit & show` (+ "plus the terminal landed").
7. `rule 18` appears exactly twice.
8. No `appetite` anywhere (banned, negative-asserted).
9. Whitespace free (tests flatten it) — paragraph/list reflow safe.
10. Entities stay defined in **bold** where a scenario first meets them.

**The needle registry.** `tests/test_traceability.py` holds ~276 `assertIn` checks; a large subset
assert VERBATIM SPEC sentences, grouped by clause ("SPEC lost the fences clause", "…work-kind clause",
"…intake-trio clause", each a list of exact phrases). The tests ARE the registry — no copy is kept
here (a copy forks the truth).

**Two escape paths the Fable pass found here, and the fix (MUST-FIX 1, 2, 4):**
- Needles assert presence in the FLATTENED WHOLE doc, not a section — some phrases occur many times
  (e.g. "one-way" appears 7×). So "compress a repeat out of section A" passes the grep because a copy
  survives in section B, then a later batch reweords B and the fact is silently gone. The check must be
  **section-scoped**: every needle that matched the OLD section text must still match the NEW section
  text; a deliberate relocation is named in the landing.
- The needles are short FRAGMENTS ("bind forward", "one-way"), not the section's sentences — you cannot
  find them by grepping FROM the prose. A **needle-extractor script** (built before batch 1) pulls all
  asserted literals from `test_traceability.py`, whitespace-normalizes both sides as the tests do, and
  matches them against the OLD section text. That list — not a by-eye grep — is the mechanical gate.
- Some clauses are **echoed verbatim in a skill doc too** (e.g. "An unresolved kind scales nothing
  down" lives in SPEC AND build-pipeline, each separately needled). Coupled skill prose is IN SCOPE:
  per shared clause, reword the skill copy + its needle in the same commit, or name the divergence.

## The sections (19 scenario sections + index; the batch list)

Epic grouping (his idea, row 148) — a plain table-of-contents LIST at the top of the doc, each epic
naming its goal in one sentence; sections stay the features. Mechanical form (MUST-FIX 6): epics are a
TOC list, NOT `##` headers — every section keeps its exact `## ` header string, so the parser's
`## Open decisions` / `## Formal index` splits and the shape rules never break. Proposed arcs (exact
grouping goes to him with batch 1):

- **The wish's road** — What live-spec is · Throwing a wish · Asking what the product does · When a
  bug cuts the line · A prototype is not the product
- **The workshop** — Sending feedback in · When the workshop itself misbehaves (problem ledger) ·
  One rulebook behind the skills · When money or time run short (economy ladder)
- **Setup** — Starting a new project (bootstrap) · Attaching to a live project (adoption)
- **Showing & shipping** — From the spec to the tests · The rhythm (breakpoints, milestones, pushes)
  · Publishing · Composing across axes
- **Governance** — Who decides what · The machines that hold the bounds · The package repo (two
  sessions at once)
- **Formal close** — Open decisions · Formal index (machinery — reflow only, never reworded)

Already rewritten (row 148 Phase 2 pilot): "When a bug cuts the line". Needled clusters (heavier
care): the wish walk, the worker contract, the milestone laws.

## The per-batch procedure (the safety spine — every step gated)

One batch = one scenario section. Never two sections in one commit.

1. **Read** the section + run the needle-extractor over the OLD section text → the section's exact
   needle list (from `test_traceability.py`, and any skill-doc echo of the same clause).
2. **Rewrite** in the approved genre at DEEP depth: user story · short narrative · plain-sentence
   acceptance (no caps) · pre/postconditions only where they genuinely exist. Break long sentences;
   move anchors to line ends; clean coined metaphors (ground or drop; keep only where it earns its
   keep); compress repeats. Entities bold at first meeting. Anchors and index untouched.
3. **Anchor→sentence diff** (not just set): the section's anchor→trailing-sentence PAIRS before vs
   after. Set-equality is necessary but NOT sufficient (an anchor can migrate to a weaker sentence with
   the set unchanged); every changed pairing is named and the prover signs it.
4. **Section-scoped needle re-match**: every needle that matched the OLD section must match the NEW
   section (not merely the doc). Update every reworded needle → its new sentence in the SAME commit,
   meaning intact; a coupled skill-doc echo is reworded + reneedled in the same commit or its
   divergence named. A relocated (not dropped) needle is named in the landing.
5. **Full suite green** (175+) — a red batch STOPS the walk; fix before moving.
6. **Prover CROSS-LINK** on the rewritten section: an OLD-vs-NEW fact table built from `git diff` of
   the section (never from the new prose alone) — does the new prose still carry every fact,
   precondition, invariant the old prose claimed? Record under `docs/prover/`.
7. **Show Alexander** the before→after for taste (the «по-человечески» loop) — smallest-first, his
   taste the bar; adjust to his nudges before the next batch inherits the register.
8. **Commit**, landing line names: section, anchor-set delta (or "identical"), needle count updated.

At the END of the whole movement: the final register-sweep pass + one FULL prover pass over the
document (row 148 done-when) + a grep for stale verbatim SPEC quotes in the UNTESTED prose class
(README.md, OVERVIEW.md, MIGRATION.md, docs/ — nothing gates them, so desync is silent; NICE 11) +
the 0.9.0 3-pass preventive audit gate + VERSION bump + gated push.

## Order — smallest-first, register set early

- **Warm-up / register-setter (batch 1):** "What live-spec is" — short, the most-read opening, no
  heavy needle cluster; nailing its register sets the bar every later batch inherits. Show it, tune it
  with him, freeze the register.
- Then the tiny ones ("Composing across axes", "Asking what the product does") to build momentum.
- Then the needled heavies (the wish walk — "Throwing a wish", the worker contract, the milestone
  laws) with the register already his-approved, so care goes to needles not style.
- Governance / machines / package-repo sections last.
- "Formal index" is machinery: reflow only, never reworded.
- **The register EVOLVES, so it is not frozen at batch 1 (MUST-FIX 7).** Batch 1 sets a working
  register, but his taste sharpens over the first 2–3 batches (his history: 5 rejected voice rounds,
  the 12:20 "better but not fully human"). A named **final register-sweep** pass closes the movement:
  wording-only, needles and anchors held stable, the suite gates it — so the most-read opening can be
  re-touched to the settled register without violating "one section, never reworked twice".
- `templates/SPEC.template.md` is one small batch in the movement (MUST-FIX 8): it is itself needled
  and stays old-register otherwise, which would break D1's "every future spec born in the genre".

Scale: ~18 sections left (pilot done) + template + final register sweep; several sessions, each batch
independently green and pushable.

## Deliverables that make it a reusable sub-skill (D4 — his framing)

- **D1** genre law → `spec-author` skill (write-new-specs-this-way): every future spec born in the
  genre; caps ban + plain-criteria voice ride the skill. Lands with batch 1 (per row 148).
- **D2** deep-polish register named in `spec-author` / the craft ladder: short sentences · anchors
  trail · coined-metaphor restraint · compress-repeats — the taste bar, written down, not memory-only.
- **D3** the pre-show plain-language lint (row 170) folded into `communicator`: scissors ban first,
  coined-metaphor titles as a sibling pattern — the mechanical guard so a humanized page STAYS human
  and no coined metaphor leaks onto a shown surface. Closes the row-56 durable-gap (ask #3).
- **D4** the migration METHOD itself, generalized into a reusable sub-skill of project migration.
  The Fable pass caught that the five-gate loop PRESUMES a needle registry — which a new host
  (tlvphoto) does not have. So D4 exports the loop WITH its precondition (MUST-FIX 5), in order:
  (1) **inventory** every mechanical consumer of the doc (tests, guardrails, CI, skill echoes,
  cross-doc quotes) — this is row 148 Phase 1; (2) **derive** the load-bearing shapes; (3) **build /
  verify** the needle registry + the extractor script; (4) THEN the five-gate batch loop (section-scoped
  needle re-match · anchor→sentence diff · full suite · prover cross-link on the git-diff fact table ·
  taste loop). Steps 1–3 are what make it safe on a first external run; a sub-skill that ships only the
  loop is unsafe. tlvphoto is its first external application — a SEPARATE process, another window, on
  Alexander's command (never this session).
- **D3 sequencing (NICE 10):** the pre-show lint is a different skill + gate family — it rides its own
  row (170) so a lint debate never stalls a rewrite batch; it lands the durable-gap fix in parallel,
  not inside the critical path of the rewrite.

## What this movement does NOT do

- Does not touch anchor IDs, the Formal index rows, or any keyed section header.
- Does not invent pre/postconditions for symmetry — only where a feature genuinely has them.
- Does not batch silently — every section shown; the register is his call, not inferred.
- Does not run in / against tlvphoto — that is his separate process, another window.
- Does not push without the full gate + his word (track-coach-style push discipline does not apply
  here — live-spec pushes on a green gate; but a MINOR milestone push still gets his word).
