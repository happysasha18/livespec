# Cleanup movement re-check record — the pushed state for 1.4.0, 2026-07-14

**Milestone gate:** M-6 (the push re-check) folded into the M-1 milestone form, since the movement is a
MINOR bump. This is the re-check record the push gate requires for the pushed state — no such record
means the push should not have happened.

**Prover this pass ran under:** the deep whole-spec + architecture audit ran on **Fable** (the milestone's
own three-pass gate, INV-116 + INV-46 — the highest-value use of the Fable budget); the finding-kind
format and the per-finding outcome column are **product-prover v1.1.4**, the repo copy the movement ships.
The independent read was fresh-context, adversarial by nature [INV-46, INV-145] — a whole-read that set
out to break the delta and refute its claims.

**Documents proven:** `PRODUCT_SPEC.md` (header moved to v1.4.0, 2026-07-14; tree state = cleanup chunk 5,
`2bdf3f6`) — FULL mode, whole document; `ARCHITECTURE.md` — architecture lens, all checks. Special scope:
the whole delta `origin/main..HEAD` (five committed chunks) read against the whole existing method.

**Suite at record time:** 682 passed, 1 failed — the one red is Gate A's `test_real_repo_passes`, red
only because this record is not yet committed; it clears at the commit that lands it. No content red.

## The three-pass audit ran

Pass 1 — the product-prover FULL over the whole `PRODUCT_SPEC.md`. Pass 2 — the architecture lens over
`ARCHITECTURE.md` (all six checks). Pass 3 — the version / matrix / cross-cut sweep. The audit is
recorded in full at `docs/prover/../scratchpad/fable-minor-gate-audit.md` (the Fable working file); this
record is its landed re-check for the pushed state, listing every finding's outcome.

## Findings and their outcome

Six defects (block the bump) and five recommendations (a now/later grade). Every defect is folded; the
recommendations are folded where cheap and queued where they earn a row.

| id | finding | kind | outcome |
|---|---|---|---|
| D1 | the M-6 push-gate clause still folded on "Must-fix findings" — the retired severity vocabulary, the exact stale-neighbour class the movement swept | defect | **FOLDED** — "Must-fix findings are folded before pushing" → "Defect findings are folded before pushing" (PRODUCT_SPEC.md:777); a case-insensitive severity-token scan over the spec + README pins it |
| D2 | the public README described the prover in severity terms ("Must-fix findings fold into the spec") | defect | **FOLDED** — "Defect findings fold into the spec" (README.md:78), one word class, same sentence shape; covered by the same scan |
| D3 | "twenty-six rules" was a false pinned count in two shipped surfaces after chunk 4 added base rule 27 (INV-143) and chunk 5 added rule 28 (INV-145) | defect | **FOLDED** — "twenty-six" → "twenty-eight" in the base skill frontmatter description and README.md:133; the count is a spec-cited literal, pinned by the reconciliation test |
| D4 | the provenance-narrative lint cited "docs/spec-style.md R/HARD", a rule that did not exist; the doc's provenance sentence named only the JOURNAL as the home | defect | **FOLDED** — the provenance-narrative rule is now **R15** in docs/spec-style.md (the three story shapes, the ordinary-verb carve-out, the homes incl. docs/lenses.md); the script and test citations point at R15 |
| D5 | the suite was red at HEAD and the milestone's own records were not yet landed (prover record, first design-review record, the bump lockstep) | defect (gate duty) | **FOLDED by this landing** — this prover record + the first design-review record (`docs/design-review/2026-07-14.md`) + the bump in one commit (VERSION, plugin.json, spec header, the reconciliation test's `_1_4_0_line` re-pin) |
| D6 | the provenance law and the spec body disagreed: the "(Born of …)" shape was swept but the sibling shapes ("(Set by the owner …)", "(Sharpened …)", "(Raised by …)", …) survived | defect | **FOLDED** — chunk 5 finished the sweep (+13 more parentheticals to docs/lenses.md); a scan of the spec for the born-of family returns zero, the lint's provenance-narrative arm reports zero hits in scope |
| R1 | the ARCHITECTURE pin caches drifted after the rule-7 split (+13 lines) and the KIND-block collapse (−7 lines) | recommendation · now | **FOLDED** — the base-rulebook and product-prover row caches refreshed in the movement |
| R2 | the eval scorecard's stale sibling cell ("GREEN (F2, must-fix, …)") | recommendation · now | **FOLDED** — aligned to kind terms at the M-1 evals re-run |
| R3 | TEST_MATRIX.md carries 18 trailing "; born of …" cells — the PROV_CELL shape the lint flags — outside the gate test's practical scope (a test-ledger, not a normative body) | recommendation · later | **QUEUED — ROADMAP row 315** (sweep the cells to docs/lenses.md and widen the scope, or record the matrix as a stated boundary of R15) |
| R4 | sharpen INV-144's silent-completion arm (name whose word certifies "correct" where the definition is silent) and one citation (INV-12 → INV-4) | recommendation · later | **FOLDED** — the silent-completion arm rides the ordinary spec-delta road ([default]-tagged, told at landing) unless the human's word is genuinely needed; the citation corrected |
| R5 | 1.4.0's migration verdict owed explicitly (the KIND retirement changes what hosts read in prover output) | recommendation · now | **FOLDED** — verdict recorded: no host-side tree action (reinstall rides the existing adopt/refresh path); stated rather than left to silence |

## What held (verified sound across the five chunks)

- **Chunk 1 + 5 (provenance sweep + lint).** No mechanism sentence was lost with a biography — base rule
  7's split preserves the old wording to the token, the entry-symmetry lens keeps its states-vs-faces
  distinction, INV-126's twin sentence keeps its one full home. The lint's provenance-narrative arm reds
  every story shape on fixtures, passes the two ordinary-verb "born of" uses and the one-token pointers,
  and reports **zero** hits across PRODUCT_SPEC.md and every SKILL.md body. docs/lenses.md reads complete
  for the 88 swept biographies (75 in chunk 1 + 13 in chunk 5).
- **Chunk 2 (KIND single-axis).** defect/recommendation is the sole verdict everywhere it was pointed —
  the tag line, the KIND block, the prover README, docs/pipeline.md, OVERVIEW, build-pipeline, the evals
  bar, the F-wish flow row. The delta-scoped carve (INV-114) reads as the one exception and coheres with
  M-6. The severity axis is retired; the "defect never carries a grade" refinement lives in the skill.
- **Chunk 3 (design review into M-1 + compaction).** The design review is reachable on a milestone walk:
  the M-1 enumerated list names it with [INV-141] and its dated record, the M-1 index row carries it,
  ARCHITECTURE lands the record beside the prover's. The kind-scaling stand-down is stated by name.
  Compaction: interactive-overlap has one full home, INV-109 keeps its two declared homes, the decision
  archive is one name, INV-133's reworded bound tightens rather than loosens. The narrated lens-family
  cross-references were cut, the bare trailing anchors kept.
- **Chunk 4 (INV-143 / INV-144).** Both rules born clean — spec clause + Formal-index row + ARCHITECTURE
  ownership + matrix row, both with never-sides, both red-proven. INV-144 forms a coherent triangle with
  INV-121/INV-4/INV-143: the spec settles forks, derivable work is decided and reported, a change to the
  definition of correct is exactly what INV-143 surfaces and INV-144 gates on the human's word.
- **Chunk 5 (periodic audit).** INV-145 born clean — the two-layer rhythm (continuous lints on every push
  for KNOWN drift; a full audit every ten landings for UNKNOWN drift, host-settable [INV-70], resetting on
  a milestone) homed in base rule 28 + the rhythm clause + a Formal-index row + a test. "An audit is
  adversarial by nature" folded into INV-46 as a definition, the qualifier dropped elsewhere.
- **Versions.** Coherent at the 1.4.0 line after the bump: VERSION = plugin.json = spec header = 1.4.0;
  product-prover 1.1.4, base 1.0.16, build-pipeline 1.0.28; the reconciliation test re-pinned to the
  1.4.0 line and green.

## Verdict

**CLEAR to 1.4.0.** The movement's content is sound — the sweep preserved mechanism to the token, the
single-axis KIND holds everywhere it was pointed, the design review is reachable at M-1, and the three
new rules (INV-143, INV-144, INV-145) are clean with accurate anchors. The six defects the audit found
were each a one-sentence or one-commit fold, all folded; the recommendations are folded or queued (row
315). Migration verdict: no host-side tree action. The pack bumps from 1.3.0 to **1.4.0** (a MINOR — new
rules + a new lint + the KIND restructure), gated by the Fable three-pass audit.
