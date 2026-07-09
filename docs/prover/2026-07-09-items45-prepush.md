# Pre-push re-check — RUN items 4-5, SHORT-FORM (M-6, INV-61)

Date: 2026-07-09 (session 29). Form: SHORT-FORM — both deltas are skill/prose/infra kind, no new
user-facing surface, no new SPEC anchor, PRODUCT_SPEC.md untouched. Covers the two commits pushed on his
"after 3 and 5" gate: `3a47aed` (item 4) and `17a347c` (item 5).

## Previous records clean
Items 2-3 (`docs/prover/2026-07-09-feature-coverage-trace.md`, `-small-holes.md`) folded, pushed at
`1eb7530`. No unfolded prover row outstanding.

## The delta, one line each
- **Item 4** — retired the coined "needle" for "traceability check-phrase" across the live surfaces (the
  extract tool, spec-author, the prose-gate design doc); added a standard-vocabulary crosswalk (ISO 29148 /
  arc42 / C4 / ISO 25010) to spec-author + a lineage pointer to ARCHITECTURE. Behaviour-neutral rename
  (tool re-run by deed, output unchanged) + new prose with a string test.
- **Item 5** — node structure PROPOSED by `project.kind` (INV-36): a per-kind scaffold in the ARCHITECTURE
  template + build-pipeline step 3 pointer; validated read-only on tlvphoto (nothing touched there), which
  found and folded two scaffold gaps (a derive-pipeline tier, the static-first + edge-backend blend).

## Checks
No new anchor; the owns-every-anchor-once, matrix-coverage, and feature-coverage checks stay green. New
tests `TestAuthoringTerminology`, `TestArchitectureTiers`. No live surface still speaks the retired
metaphor. Suite 220 → 225 green. Full pre-push gate green (a-g).

Verdict: FOLD — clean, push authorized on his standing gate for items 3 and 5.
