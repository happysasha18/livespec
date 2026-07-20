# Prover record — INV-245 project-name arm, detection soundness (2026-07-21)

Adversarial fresh-context review of the project-name arm added to `scripts/check-shipped-language.py`.
Verdict: **sound for the stated scope** (root PRODUCT_SPEC/ARCHITECTURE/TEST_MATRIX, ISO-dated incidents).
No active false positive. Real gaps are all false-negatives, and both notable ones are by design.

## Confirmed sound
- All three core specs pass today (rc=0). Line 172 (M-276) keeps `track-coach`/`tlvphotos` as fixture-ledger
  kind names; the only ISO date on that 1852-char line sits ~1000 chars away — far past the 40-char window,
  correctly permitted.
- `test_promoter_harvest_trio` does NOT match: `_` is a word char, so `\bpromoter\b` has no boundary inside it.
  `promotion`/`promote`/`promoted`/`promoters` also do not match.
- Engine source carries no literal project name (grep empty; `test_detector_source_names_no_project` asserts it).
  Engine + allowlist are in EXCLUDE_FILES (is_excluded True for both).
- `_near_iso_date` AND-logic is correct in both directions (date before / after the name); numerically the
  window is symmetric: gap ≤40 → near, 41 → not-near.

## Worth-considering (false-negatives, mostly by design)
1. **Non-ISO dated incidents slip through on TEST_MATRIX.** `ISO_DATE` only matches `YYYY-MM-DD`.
   `July 16 2026`, `16/07/2026`, `2026-7-6` (unpadded), `Jul-16` all evade. TEST_MATRIX distinguishes a
   dated incident from a permitted fixture label ONLY by date-proximity, so a non-ISO-dated incident reads as
   a fixture label and passes. (Inert for PRODUCT_SPEC/ARCHITECTURE — strict on bare name regardless.)
2. **The promotion-campaign project's spec-facing name is uncovered.** Patterns cover `track-coach`,
   `tlvphotos?`, `promoter` (the agent name). The specs refer to the third project as "the promotion campaign",
   and `promotion` is deliberately excluded as common English. So a bare mention or dated incident phrased
   "the promotion campaign 2026-07-16" evades in all three specs. Deliberate tradeoff; a real 2-of-3 coverage gap.
3. **`promoter` is a common English noun** (event/gene/sales promoter) — latent false positive. Not present as
   English in the core specs today, but any future legit `promoter` in PRODUCT_SPEC/ARCHITECTURE would red.
   Asymmetric with the deliberately-excluded `promotion`.

## Nit
4. Explicit-file invocation bypasses is_excluded (main() filters only on the no-arg shipped_set path). A
   run with an explicit path to an excluded core-spec fixture bearing a project name would scan it. Not the
   CI/pre-push path (both full-scan via the wrapper), and the current fixture has no project names — inert today.
5. Per-line scan: a name split across a markdown wrap (`track-\ncoach`), or a name/date split across two
   physical lines, evades. Near-zero practical impact (matrix rows are single lines; strict files red bare names).
6. Variant spellings (`trackcoach`, `track coach`, plural `promoters`) don't match. Allowlist is data, extensible.
7. Basename-global strictness: any non-excluded `PRODUCT_SPEC.md`/`ARCHITECTURE.md`/`TEST_MATRIX.md` in a subdir
   inherits strict treatment. None exist outside root today (fixtures are excluded). Defensible but surprising.
