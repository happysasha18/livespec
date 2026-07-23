# Register census — 2026-07-22

Purpose: a per-file baseline of register violations (banned contrast-by-denial frames and
inflation words) across the repo's prose, plus lint findings, before a rewrite. This is the "was"
snapshot the future ratchet only tightens against — no file's numbers should rise from here.

## Method

Every markdown file in scope was measured for:
- **bytes** — plain file size (matters most for Tier A: those tokens are paid every session).
- **scissors-hits** — reported as `raw (est. real)`. `raw` is a broad regex over five banned-frame
  shapes: em-dash + not, comma + not (the appositive "X, not Y"), the Russian «, а не», `rather
  than`, and `instead of`. `est. real` is this repo's own lint (`scripts/spec-style-lint.py`,
  rule `scissors`) run in-process on the same text — it already excludes the lawful additive
  reading ("not only/just/merely/simply") and is line-scoped, so it is the trustworthy number for
  the comma/dash/Russian shapes. It does **not** cover `rather than` / `instead of` at all — see
  finding 1 below. The gap between `raw` and `real` in a given row is mostly that omission plus
  the "not only" exemption, not noise; a manual sample of ~25 `rather than`/`instead of` hits in
  ARCHITECTURE.md and `skills/live-spec-base/SKILL.md` found the false-positive rate for that
  pair to be near zero — almost every hit is a genuine contrast-by-denial ("the suite enforces the
  tag rather than trusting it"). The comma-form's main false-positive source is the "not only"
  additive reading, already subtracted in `real`.
- **inflation-hits** — a fixed word list (powerful, seamless, robust, game-changing, crucial,
  critically, dramatically, "in essence", revolutionary, cutting-edge, state-of-the-art,
  unprecedented, groundbreaking, transformative, world-class, best-in-class, effortless(ly),
  supercharge, unleash, elevate, empower(ing), magic(al)) counted verbatim, case-insensitive.
- **lint findings** — this repo's own gates, run on every file: `scripts/spec-style-lint.py`
  (default tier: scissors + negation-opener + machine-jargon as errors; caps-shout + second-person
  as warnings) and `scripts/preshow-register-lint.py` (coined-metaphor / calque / transliterated
  pack-term detector). The column sums scissors + negation-opener + machine-jargon +
  provenance-narrative (errors) plus the register-lint's own hit count; caps-shout and
  second-person are reported separately in the totals since they are advisory, not errors, in
  default mode. `scripts/check-weak-words.py` was **not** run — it is gated to spec-format
  documents with parsed criteria/`[GAP]` lines (INV-256) and errors on unstructured prose; it
  does not apply to this corpus. No other `register`/`style`/`prose`/`shipped-language`-named
  script in `scripts/` or `guardrails/` runs on free-form markdown without that same spec-format
  precondition, except `check-shipped-language.py`, which is a Cyrillic/name/project-name
  detector (a different concern) and was left out of the tally by design — see finding 2.

**Finding 1 — a lint gap.** `spec-style-lint.py`'s own `scissors` rule never matches `rather
than` or `instead of`. Those two account for the majority of this corpus's contrast-by-denial
volume (943 of Tier D's 2,227 raw hits; 83 of Tier A's 134) and read as genuine violations on
spot-check. If the rewrite's ratchet is meant to hold this class shut, the lint needs those two
forms folded in — today a file can carry dozens of them and still pass clean.

**Finding 2 — `check-shipped-language.py` not run.** It checks a different thing (Cyrillic
leakage, personal names, foreign project names) and is scoped to the SHIPPED set (spares
JOURNAL/ROADMAP/docs/tests/prototype by design) — orthogonal to this census, not run here.

## Corpus and tiers

- **Tier A** (loaded every session): `skills/**/*.md` — 29 files.
- **Tier B** (public reader): `README.md`, `OVERVIEW.md`, `adopt/*.md`, `templates/*.md` — 15
  files. (`install.sh` comments excluded per scope.)
- **Tier C** (working docs): `docs/*.md` at the top level only (not subdirectories), plus
  `MIGRATION.md`, `SURFACES.md`, `DECISIONS.md` — 21 files.
- **Tier D** (archive, measure only): `JOURNAL.md`, `ROADMAP.md`, `docs/attic/`, `docs/prover/`,
  `docs/queue-archive/`, `docs/reports/` (as named), plus every other dated/audit-trail
  subdirectory of `docs/` not claimed by Tier C — `docs/audit/`, `docs/briefs/`, `docs/decisions/`,
  `docs/design/`, `docs/design-review/`, `docs/evals/`, `docs/gate-audit/`,
  `docs/migration-sample/`, `docs/norms/`, `docs/research/`, `docs/skill-review/`, `docs/wishes/`
  — 477 files. **Judgment call**: the task named only four Tier-D directories explicitly; the rest
  of `docs/`'s subdirectories are dated one-off audit/decision/review/eval records with the same
  "measure only, no rewrite planned" shape, so they're grouped here rather than left unclassified.
  Flag if a different split was intended.
- **Excluded**: `prototype/`, `*.html`, `LICENSE`, `tests/`, `evals/` (top-level fixtures dir,
  distinct from `docs/evals/`), and `.claude/`, `.live-spec/`, `.spec-freeze/`, `.2.0-work/`,
  `.github/`, `hooks/`, `guardrails/`, `scripts/`, `inbox/` (non-prose or machinery, out of the
  corpus's scope).
- `ARCHITECTURE.md`, `PRODUCT_SPEC.md`, `TEST_MATRIX.md`, `NEXT_STEPS.md`, `FEEDBACK.md`,
  `WAITING.md`, `VERSION` at the repo root were left out of all four tiers — none of the task's
  tier definitions named them, and they are spec-format documents with their own gate
  (`spec-style-lint.py --gate`), not free prose. Flag if these should be folded into Tier C or a
  fifth tier.

## Tier A — loaded every session (skills/)

| file | bytes | scissors raw (real) | inflation | lint findings |
|---|---|---|---|---|
| skills/live-spec-base/SKILL.md | 55,884 | 22 (2) | 0 | 3 |
| skills/product-prover/SKILL.md | 59,792 | 16 (3) | 0 | 5 |
| skills/build-pipeline/SKILL.md | 53,389 | 18 (5) | 0 | 5 |
| skills/spec-author/SKILL.md | 50,901 | 18 (0) | 0 | 0 |
| skills/communicator/SKILL.md | 45,037 | 8 (5) | 0 | 15 |
| skills/design-reviewer/SKILL.md | 23,197 | 8 (6) | 0 | 8 |
| skills/test-author/SKILL.md | 18,244 | 5 (0) | 0 | 0 |
| skills/publish/SKILL.md | 12,890 | 6 (1) | 0 | 1 |
| skills/product-prover/README.md | 11,173 | 12 (5) | 0 | 6 |
| skills/communicator/references/writing-register.md | 9,062 | 0 (0) | 0 | 0 |
| skills/feedback-collector/SKILL.md | 8,072 | 4 (4) | 0 | 6 |
| skills/feedback-intake/SKILL.md | 7,469 | 1 (0) | 0 | 2 |
| skills/design-reviewer/README.md | 6,603 | 1 (0) | 0 | 0 |
| skills/test-author/README.md | 6,396 | 0 (0) | 0 | 0 |
| skills/build-pipeline/references/delegation-protocol.md | 6,232 | 1 (1) | 0 | 1 |
| skills/communicator/references/field-examples.md | 6,922 | 4 (1) | 0 | 2 |
| skills/feedback-intake/README.md | 5,649 | 0 (0) | 0 | 0 |
| skills/spec-author/README.md | 4,988 | 1 (1) | 0 | 1 |
| skills/build-pipeline/README.md | 4,923 | 4 (3) | 0 | 3 |
| skills/build-pipeline/references/work-kind-table.md | 3,103 | 0 (0) | 0 | 0 |
| skills/feedback-collector/README.md | 2,896 | 0 (0) | 0 | 1 |
| skills/communicator/README.md | 2,182 | 0 (0) | 0 | 1 |
| skills/build-pipeline/references/request-kind-table.md | 2,101 | 0 (0) | 0 | 1 |
| skills/build-pipeline/references/guardrails-catalog.md | 1,965 | 3 (0) | 0 | 0 |
| skills/build-pipeline/references/minor-bump-gate.md | 1,765 | 2 (0) | 0 | 0 |
| skills/build-pipeline/references/excuses-table.md | 1,298 | 0 (0) | 0 | 0 |
| skills/build-pipeline/references/drafter-applier-example.md | 1,166 | 0 (0) | 0 | 1 |
| skills/live-spec-base/README.md | 279 | 0 (0) | 0 | 0 |
| skills/publish/README.md | 1,041 | 0 (0) | 0 | 0 |

**Tier A total**: 29 files, 414,619 bytes (~405 KB paid every session). Scissors: 134 raw / 37
lint-real (83 of the 134 are `rather than`/`instead of`, uncaught by the lint). Inflation: 0.
Lint findings: 62 (includes 16 register-lint calque/coinage hits, concentrated in
`communicator/SKILL.md` (9) and `product-prover/SKILL.md` (2)). Advisory-only: 546 caps-shout
warnings, 149 second-person warnings (not counted in "lint findings" above — see Method).

## Tier B — public reader

| file | bytes | scissors raw (real) | inflation | lint findings |
|---|---|---|---|---|
| adopt/ADOPT.md | 21,366 | 3 (0) | 0 | 0 |
| templates/ARCHITECTURE.template.md | 10,991 | 0 (0) | 0 | 2 |
| README.md | 9,739 | 0 (0) | 0 | 0 |
| OVERVIEW.md | 6,830 | 0 (0) | 0 | 0 |
| templates/PRODUCT_SPEC.template.md | 4,373 | 0 (0) | 0 | 0 |
| templates/agent.template.md | 3,628 | 1 (0) | 0 | 0 |
| templates/TEST_MATRIX.template.md | 3,393 | 1 (1) | 0 | 1 |
| templates/ROADMAP.template.md | 2,886 | 0 (0) | 0 | 0 |
| templates/profile.template.md | 1,622 | 0 (0) | 0 | 0 |
| templates/DECISIONS.template.md | 1,493 | 0 (0) | 0 | 0 |
| templates/PROBLEMS.template.md | 1,267 | 0 (0) | 0 | 0 |
| templates/NEXT_STEPS.template.md | 1,099 | 0 (0) | 0 | 0 |
| templates/JOURNAL.template.md | 1,011 | 0 (0) | 0 | 0 |
| templates/KILL_LIST.template.md | 674 | 0 (0) | 0 | 0 |
| templates/skill-review.template.md | 489 | 0 (0) | 0 | 0 |

**Tier B total**: 15 files, 70,861 bytes. Scissors: 5 raw / 1 lint-real. Inflation: 0. Lint
findings: 3. README.md and OVERVIEW.md are clean (0/0/0) — README.md confirms the recent rewrite
holds at near-zero, as expected.

## Tier C — working docs

| file | bytes | scissors raw (real) | inflation | lint findings |
|---|---|---|---|---|
| docs/prior-art-longtail.md | 16,913 | 15 (0) | 0 | 1 |
| MIGRATION.md | 23,844 | 7 (6) | 0 | 6 |
| docs/prior-art-frameworks.md | 15,971 | 8 (0) | 0 | 1 |
| docs/spec-style.md | 14,428 | 6 (0) | 0 | 2 |
| docs/restyle-repoint-log.md | 14,488 | 10 (7) | 0 | 7 |
| docs/lenses.md | 19,277 | 5 (3) | 0 | 4 |
| docs/architecture-method.md | 8,856 | 0 (0) | 0 | 0 |
| docs/pipeline.md | 8,738 | 2 (0) | 0 | 0 |
| docs/test-method.md | 7,940 | 0 (0) | 0 | 0 |
| docs/worker-liveness.md | 7,703 | 1 (0) | 0 | 0 |
| docs/spec-compaction-protocol.md | 7,670 | 6 (4) | 0 | 5 |
| docs/pair-adoption.md | 7,425 | 0 (0) | 0 | 0 |
| docs/adoption.md | 7,111 | 0 (0) | 0 | 0 |
| docs/prose-quality-gate-design.md | 6,571 | 2 (0) | 0 | 0 |
| docs/onboarding-and-settings.md | 6,193 | 1 (0) | 0 | 0 |
| docs/spec-format-by-project-type.md | 5,513 | 1 (1) | 0 | 1 |
| docs/push-law.md | 4,951 | 0 (0) | 0 | 0 |
| docs/spec-format.md | 4,370 | 1 (1) | 2 | 1 |
| DECISIONS.md | 2,923 | 3 (0) | 0 | 0 |
| docs/prior-art.md | 1,249 | 0 (0) | 0 | 0 |
| SURFACES.md | 779 | 0 (0) | 0 | 0 |

**Tier C total**: 21 files, 192,913 bytes. Scissors: 68 raw / 22 lint-real. Inflation: 2 (both in
`docs/spec-format.md`). Lint findings: 28.

## Tier D — archive, measure only (477 files, aggregated by directory)

Per-file rows for 477 files would swamp this document; aggregated by directory, sorted by bytes.
`docs/prover/` alone (306 files) is 30% of the entire repo's markdown by byte count.

| directory | files | bytes | scissors raw (real) | inflation | lint findings |
|---|---|---|---|---|---|
| docs/prover/ | 306 | 1,640,287 | 768 (499) | 1 | 554 |
| docs/attic/ | 3 | 1,270,831 | 343 (6) | 0 | 30 |
| ROADMAP.md | 1 | 665,094 | 157 (45) | 0 | 71 |
| JOURNAL.md | 1 | 597,595 | 220 (137) | 3 | 168 |
| docs/audit/ | 27 | 315,822 | 146 (116) | 0 | 128 |
| docs/evals/ | 51 | 257,427 | 259 (135) | 0 | 153 |
| docs/queue-archive/ | 23 | 181,289 | 53 (33) | 0 | 42 |
| docs/research/ | 11 | 142,397 | 85 (62) | 1 | 71 |
| docs/design-review/ | 15 | 137,087 | 76 (49) | 0 | 54 |
| docs/design/ | 8 | 80,761 | 44 (12) | 0 | 18 |
| docs/skill-review/ | 18 | 64,031 | 43 (24) | 0 | 27 |
| docs/wishes/ | 6 | 24,653 | 13 (7) | 0 | 15 |
| docs/gate-audit/ | 1 | 16,355 | 5 (1) | 0 | 2 |
| docs/decisions/ | 2 | 11,531 | 3 (4) | 0 | 4 |
| docs/reports/ | 1 | 8,668 | 0 (0) | 0 | 0 |
| docs/briefs/ | 1 | 8,336 | 3 (1) | 0 | 1 |
| docs/migration-sample/ | 1 | 8,025 | 9 (2) | 0 | 2 |
| docs/norms/ | 1 | 654 | 0 (0) | 0 | 0 |

**Tier D total**: 477 files, 5,430,843 bytes (~5.3 MB). Scissors: 2,227 raw / 1,133 lint-real.
Inflation: 5. Lint findings: 1,356 (includes 91 register-lint calque/coinage hits — mostly in
`docs/prover/`, the largest and oldest folder).

## Worst ten files (repo-wide, by raw scissors + inflation + lint findings)

| rank | file | tier | bytes | raw scissors | lint findings | score |
|---|---|---|---|---|---|---|
| 1 | JOURNAL.md | D | 597,595 | 220 | 168 | 391 |
| 2 | docs/attic/2026-07-22-pre-format/PRODUCT_SPEC.md | D | 783,678 | 259 | 8 | 267 |
| 3 | ROADMAP.md | D | 665,094 | 157 | 71 | 228 |
| 4 | docs/attic/2026-07-22-pre-format/TEST_MATRIX.md | D | 385,079 | 66 | 25 | 91 |
| 5 | docs/prover/2026-07-19.md | D | 43,001 | 32 | 24 | 56 |
| 6 | docs/research/2026-07-05-methods.md | D | 24,895 | 24 | 14 | 38 |
| 7 | docs/audit/2026-07-05/pass1-prover-opus.md | D | 34,168 | 17 | 19 | 36 |
| 8 | docs/prover/2026-07-17-2.5.0-minor-gate.md | D | 27,126 | 19 | 11 | 30 |
| 9 | docs/design/2026-07-20-conduct-audit-stories-2-3-spec-delta.md | D | 22,635 | 23 | 7 | 30 |
| 10 | docs/evals/2026-07-10-rerun/scores.md | D | 20,349 | 18 | 12 | 30 |

All ten are Tier D (archive, no rewrite planned) — expected, since Tier D holds the oldest,
largest, most log-like prose (the pre-format attic dump alone is 783 KB with 259 raw scissors
hits but only 8 catch on today's lint, almost entirely the uncaught `rather than`/`instead of`
form). The worst Tier A file (the tier that actually matters for a rewrite) is
`skills/live-spec-base/SKILL.md` (22 raw / 2 lint-real scissors, 3 lint findings, far below any
Tier D file); the worst Tier C file is `docs/restyle-repoint-log.md` (10 raw / 7 lint-real, 7
lint findings).

## Tools run

- `scripts/spec-style-lint.py` (default tier) — imported and run in-process on every file's raw
  text; supplies the `scissors`/`negation-opener`/`machine-jargon`/`provenance-narrative` error
  counts and the `caps-shout`/`second-person` advisory counts, for all 542 files across all four
  tiers.
- `scripts/preshow-register-lint.py` — same, for calque/coinage/transliterated-pack-term hits.
- `scripts/check-weak-words.py` — checked but **not run**: it is gated to spec-format documents
  (INV-256) and does not apply to free-form prose; would error on every file in this corpus.
- No other `register`/`style`/`prose`/`shipped-language`-named script in `scripts/` or
  `guardrails/` applies to unstructured markdown outside the spec-format gate.
