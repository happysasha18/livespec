# Genre migration — validation inventory and the whole-doc rewrite plan (2026-07-07, session 23, row 148)

His round-4 verdict approved the use-case genre (user story · short narrative · plain-sentence
acceptance criteria · pre/postconditions where they exist) and demanded a serious validation before
any whole-doc rewrite. This document is that validation's record and the plan.

## Phase 1 — inventory (DONE, scout run ~09:38–09:42)

Every mechanical consumer of SPEC.md's shape was read: all tests, all guardrail scripts, the CI
workflow.

**Safe under a prose rewrite (keyed on anchors and structure only):** the Formal-index parser and its
anchor-set equality checks against the architecture and the matrix; the matrix block/coverage checks;
pin drift; prover-record freshness; the CI workflow itself.

**Break on rewording (keyed on verbatim prose):** ~60 tests in `tests/test_traceability.py` assert
exact SPEC sentences ("needles"). The tests themselves are the needle registry — before rewriting a
section, grep that file for fragments of the section's sentences; every needle whose sentence is
reworded is updated to the new sentence IN THE SAME COMMIT, meaning identical, delta named in the
landing. Copying the needle list here would fork the truth; the tests are the one home.

**Structural constraints the new genre must keep (the load-bearing shapes):**
1. The Formal index: `## Formal index` header; pipe table; anchor code in the first cell; ranges like
   `T-1..T-7` legal; >40 anchors, unique; anchor sets must stay equal across SPEC ↔ ARCHITECTURE ↔
   TEST_MATRIX.
2. `[target]` tags stay inside index fact cells where they stand.
3. `## Open decisions` section: `- ` bullets, the literal `⟨DECIDE⟩` marker, each entry citing its
   `D-n`; `Decided` never precedes a live marker.
4. The header line format: `# live-spec — SPEC (vX.Y.Z, YYYY-MM-DD)`.
5. Bracketed anchors stay present in prose (`[T-9]`, `[INV-22]`, `[T-14, INV-19]` forms) — the genre
   keeps codes trailing at line ends, unchanged.
6. The pipeline station list appears verbatim once: `spec → prove → architecture → prove architecture
   → matrix → test → code → verify → commit & show` (+ "plus the terminal landed").
7. The exact phrase `rule 18` appears exactly twice (the collision law's two citation sites).
8. No `appetite` anywhere (a banned word, negative-asserted).
9. Whitespace is free (tests flatten it) — paragraph and list reflow is safe.
10. Entities stay defined in **bold** where a scenario first meets them (the spine law, unchanged).

## Phase 2 — pilot (DONE, ~09:47)

"When a bug cuts the line" rewritten in the approved genre directly in SPEC.md: user story ·
narrative · precondition · five plain-sentence acceptance criteria (no caps) · postcondition. Anchor
set held identical (T-9, T-11, T-18). Full suite: 164 green. Pin drift: green. The section carried no
prose needles, so the pilot proves genre-vs-machinery; the needle-update discipline gets its proof on
the first needled section of Phase 3.

## Phase 3 — the whole-doc rewrite (AWAITS his word on this plan)

- Section by section, one batch = one scenario section; each batch: rewrite in genre → grep the test
  file for the section's needles → update needles with the rewrite, meaning intact → full suite green
  → commit. The suite gates every step; a red batch stops the walk.
- Anchor sets diffed before/after per batch (sorted list equality); any delta named in the landing.
- Pre/postconditions added where a feature genuinely has them; never invented for symmetry.
- The prover: CROSS-LINK per batch on the rewritten section; one FULL pass over the whole document at
  the end (the row's own done-when).
- EPIC GROUPING (his adjustment): propose grouping the scenario sections under the map's natural
  arcs — e.g. "The wish's road" (throwing · classifying · lanes · bugs · decline) · "The workshop"
  (ledger · skills discovery · economy) · "Setup" (bootstrap · adoption · onboarding) · "Showing and
  shipping" (reports · decision pages · publishing) · "Governance" (who decides · settings ladder) —
  as a table-of-contents layer above the sections, each epic naming its goal in one sentence.
  Sections stay the features; the epics are the reading map. Exact grouping goes to him with the
  first batch.
- The genre law lands in the spec-author skill with the first batch (write-new-specs-this-way), so
  every future spec is born in the genre, and the caps ban + plain-criteria voice ride the skill.

Scale estimate: 19 scenario sections; the needled ones cluster around the wish walk, the worker
contract, and the milestone laws. Several sessions, each batch independently green and pushed.
