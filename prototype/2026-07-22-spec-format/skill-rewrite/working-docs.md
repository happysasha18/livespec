# Working-docs tier — register rewrite notes (2026-07-22)

Register-only rewrite of the working-docs tier. Meaning, rules, and facts preserved; only the
contrast-by-denial frame, drama, coined metaphor, and tangled sentences changed. Baseline was
`docs/audit/2026-07-22-register-census.md`.

## Key finding — the census's "Finding 1" is stale

The census recorded that `spec-style-lint.py`'s scissors rule never matches `rather than` / `instead
of`. That gap has since been closed: the lint now carries `_rather_instead_scissors`, which flags a
DEFINITIONAL `rather than`/`instead of` (a copula/naming verb leads, or a determiner sits on both
sides, or a non-directional preposition repeats) and passes a purely INSTRUCTIONAL substitution
directive (an imperative-led clause). This matches THE BAR's own line exactly. Consequence: the lint
was used as the authoritative definitional-vs-instructional judge for this pass, plus a hand sweep for
the residual cases the lint deliberately leaves uncaught (bare verb/participle contrasts, and genuine
contrasts that open with a directive verb).

## Per-file record (changed files)

Counts are of frames CONVERTED. "scissors" covers every contrast-by-denial variant (comma/dash
appositive, `rather than`/`instead of`, `X not Y`). No inflation or coined-metaphor findings were
present in this tier (the two census inflation hits were both in `docs/spec-format.md`, which is
excluded as already at the bar).

- **MIGRATION.md** — 8 scissors (routing paragraph ×1, `merges … rather than clobbering`, `once per
  machine, not once per host`, dash+`never` marker line, `inherits … not a breaking change`, `by a
  model, not a literal list`, `must run, not a walk`, `representative handful … rather than the
  exhaustive list`). 0 inflation, 0 metaphor. Pins "A wording never decides the routing" and "never
  nest the old directory inside the new one" kept verbatim. See pin record below for the `once per
  machine` phrase.
- **DECISIONS.md** — 1 scissors (the `## Open — recorded, not yet decided` section header →
  `## Open — carried, awaiting your word`). Three `rather than` inside RECORDED decisions skipped for
  meaning-risk (see skip list). Authority-anchor gate green before and after.
- **docs/restyle-repoint-log.md** — 9 scissors. This is a meta-log documenting the removal of scissors,
  so several flags were the old banned phrases QUOTED as evidence; those were wrapped in backticks
  (`scrub` strips inline code, so the phrase is preserved verbatim and the lint clears). Genuine prose
  scissors (`not shout` ×3, `map rather than a restatement`, `rather than lowercased`, `archived, not
  reworded`) rewritten positively.
- **docs/spec-style.md** — 6 scissors + 2 negation-opener. This is the register rulebook and its
  exemplar section claims "zero linter tells", so clearing it mattered. R13's own illustrative example
  `X does not become Y` was moved out of the block's opening 12 words and backticked; R14's title
  `a list instead of a paragraph` → `written as a list`.
- **docs/prior-art-frameworks.md** — 6 scissors + 1 negation-opener + 2 residual (`instead of drawing`,
  `batch-oriented rather than continuous-intake`). A comparison report; each verdict/lacks line that
  defined a framework by contrast was made positive with the real boundary as its own clause.
- **docs/prior-art-longtail.md** — 9 scissors (incl. the `NOT found anywhere` negation-opener) + 2
  residual (`checks … rather than consistency`, `governance framework rather than a SKILL`).
  `not just domain code` (×2) left as the lawful additive reading.
- **docs/lenses.md** — 3 scissors + 1 residual (`points at the record rather than duplicating`). The
  INV-110 rule-name heading `keys on a version delta, not a wording` → `keys on the version delta,
  never on the wording`. Lines 82 and 132 (`not only …`) left as the lawful additive reading. The
  line-45 `provenance-narrative` flag is NOT a bar item and is left as-is (see below).
- **docs/pipeline.md** — 1 scissors + 1 residual (`derived rather than filled in` → `derived, never
  hand-filled`).
- **docs/worker-liveness.md** — 1 scissors (`read a wrapper instead of the log`).
- **docs/spec-compaction-protocol.md** — 5 scissors + 1 negation-opener (`the redundancy is not
  symmetric` → `is asymmetric`).
- **docs/prose-quality-gate-design.md** — 1 scissors (`as dated debt instead of a silent park`).
- **docs/onboarding-and-settings.md** — 1 scissors (`instead of being continued by hand`).
- **docs/spec-format-by-project-type.md** — 1 scissors (`an extension, not new machinery`).
- **adopt/ADOPT.md** — 2 scissors (`code a host runs rather than prose`, `found now rather than on the
  next touch`). Line 77 `goes through the attic … instead of this sweep` left as a lawful routing
  directive (lint passes it).
- **templates/ARCHITECTURE.template.md** — 2 negation-opener (`is not templating`, `are not
  exclusive` → `can coexist`).
- **templates/TEST_MATRIX.template.md** — 1 scissors (`the declared interface, not its internals`).

## Files verified clean and untouched

Reported clean by both lints (no scissors / negation-opener / machine-jargon / provenance / preshow),
so left exactly as written:

- docs/adoption.md, docs/architecture-method.md, docs/test-method.md, docs/push-law.md,
  docs/prior-art.md, docs/pair-adoption.md
- SURFACES.md, WAITING.md, OVERVIEW.md
- templates/agent.template.md (its line-27 `rather than building its own copy` is a lawful
  instructional directive; the lint passes it), templates/DECISIONS.template.md,
  templates/JOURNAL.template.md, templates/KILL_LIST.template.md, templates/NEXT_STEPS.template.md,
  templates/PROBLEMS.template.md, templates/PRODUCT_SPEC.template.md, templates/ROADMAP.template.md,
  templates/profile.template.md, templates/skill-review.template.md

## Pins recorded

Before any change, distinctive fragments were grepped across `tests/` and `guardrails/`. One pinned
phrase was touched and RESTORED verbatim (the pinning file was not edited):

- **`once per machine`** — pinned by `tests/test_catchup_walk.py::TestCatchupWalk::
  test_catchup_pair_and_machine_level` (`self.assertIn("once per machine", mig)`).
  - OLD: `… and run once per machine, not once per host. Each such step states its already-done check:`
  - FIRST REWRITE (dropped the phrase, broke the test): `They run once for the whole machine, and every
    host on it shares the result.`
  - FINAL (phrase restored, still positive, test green): `They run once per machine, and every host on
    it shares the result.`

All other changed sentences pin-checked to no test/guardrail fragment. The two MIGRATION pins "A
wording never decides the routing" and "never nest the old directory inside the new one" were kept
word-for-word (only surrounding punctuation/dash near the latter changed).

## Skipped for meaning-risk (DECISIONS.md — a decision record)

Per the special-care rule, recorded past decisions keep their content where a rewrite could change what
was decided. These three `rather than` phrases sit inside recorded decisions and were left as written
(the preshow gate — the required one — is clean on the file, and the authority-anchor gate is green):

- Line 26 (decision 2026-07-17 ~15:26): `discovery is a bounded live scan for cards rather than a
  ratified list` — the contrast IS the decided substance (live scan vs. pre-ratified roster).
- Line 33 (decision 2026-07-20 ~14:34): `a representative handful of its members rather than the
  exhaustive list` — the accepted description form.
- Line 34 (same decision): `keep the class-member lists representative rather than complete` — a
  near-verbatim report of the owner's own asked words.

`spec-style-lint.py` still flags line 26 as a definitional scissors; it is left deliberately.

## Out-of-bar flag left in place

- **docs/lenses.md:45** — `provenance-narrative` on a `Born of …` birth-story. `docs/lenses.md` is the
  provenance HOME (per spec-style R15, birth-stories live here, keyed by code), so this is the doc's
  intended content, not a bar item (the bar covers scissors, inflation, metaphor, tangled sentences).
  Preshow is clean. Left as written.

## Verification

- `scripts/preshow-register-lint.py`: CLEAN on every changed file.
- `scripts/spec-style-lint.py` (scissors / negation-opener / machine-jargon / provenance): CLEAN on
  every changed file except the two deliberate residuals above (DECISIONS.md:26 decision-record skip,
  lenses.md:45 provenance home).
- `guardrails/check-authority-anchor.py DECISIONS.md`: GREEN (before and after);
  `tests/test_authority_anchor.py` 30 passed.
- Spot-run of the doc-reading test files: `test_catchup_walk`, `test_catchup_discriminator`,
  `test_founding_set_version`, `test_style_lint_tiers`, `test_prose_gate`, `test_guardrails`,
  `test_traceability`, `test_design_principles`, `test_scenario_entry_exit`,
  `test_preshow_register_lint`, `test_authority_anchor`. The one failure my edits caused
  (`test_catchup_pair_and_machine_level`, the `once per machine` pin) was fixed and re-run green.
  Three failures remain that are PRE-EXISTING and outside this write set: `test_skill_evals_present`
  (reads `evals/*.md` fixtures), `test_real_repo_lists_complete` (pack-list parity over
  README/OVERVIEW/PRODUCT_SPEC — none edited here), and `test_craft_ladder` (asserts a phrase in
  `skills/build-pipeline/SKILL.md`, which is excluded from this pass and whose live text differs from
  the test's expected string).

## Cold read

One fresh zero-context reader over the three most-changed files (MIGRATION.md, docs/spec-style.md,
docs/prior-art-longtail.md) with a strict blocking bar (unparseable / self-contradictory / garbled
sentences only). Verdict: all three clean, no blocking issues, no fixes required. That read stands as
the confirming read.
