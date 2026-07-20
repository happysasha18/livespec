# History-cleanup movement — scope inventory (2026-07-21)

The movement builds a PERMANENT pack gate: a project name or a provenance turn never sits in a core spec, held
forever and inherited by every host (Alexander's word 2026-07-20/21, ROADMAP row for the cleanup + the intake
classifier row 440). The one-time sweep clears the current debt so the gate goes green. This file is the
read-only scope inventory a worker produced, so the build does not re-scan.

## The load-bearing finding

No test asserts any of `track-coach` / `tlvphotos` / `promoter` appears INSIDE PRODUCT_SPEC.md, ARCHITECTURE.md,
or TEST_MATRIX.md. The fixture names live self-contained in the test files (`FIXTURE_CODE`/`FIXTURE_PHOTO`/
`FIXTURE_VISUAL` in tests/), and the traceability tests assert generic structural strings, never the project
names. So every spec mention is safe to reword or abstract.

## Counts (by occurrence)

| Class | PRODUCT_SPEC | ARCHITECTURE | TEST_MATRIX | Total |
|---|---|---|---|---|
| A — provenance/history (reword to the rule, history to JOURNAL) | 26 | 4 | 15 | 45 |
| B — fixture-binding label (safe to abstract) | 0 | 3 | 2 | 5 |
| C — false positive, preserve verbatim | 0 | 0 | 3 | 3 |

## Class A — provenance (45): reword each to state the RULE, drop the project name and the date

The history belongs in JOURNAL. Spec sentences state the rule with no project name and no dated incident.
PRODUCT_SPEC lines: 259, 339, 341, 731, 819, 1147(×2), 1346, 1544, 1567, 1910(×2), 1949, 1986(×2), 2058,
2325, 2326(×3), 2365, 2366, 2373(×2), 2385, 2428. ARCHITECTURE: 51(×2), 54(×2). TEST_MATRIX: 191, 192, 220,
221, 222, 223, 224, 230, 242, 301, 492(×2), 559(×2), 622.

## Class B — fixture labels (5): abstract in the upstream docs, keep the concrete trace in one home

- ARCHITECTURE 197-198 and 266: reword to the abstract kinds only ("a code/music kind, a photo/visual kind, a
  prose kind"). The pairing to real fixtures survives because the test files still name them
  (test_founding_layers_proofs.py FIXTURE_CODE/FIXTURE_PHOTO, test_composition_axes.py:59 FIXTURE_VISUAL,
  test_design_principles.py:60 FIXTURE_VISUAL_WITH).
- TEST_MATRIX 172: the one defensible home for the concrete fixture-name trace (TEST_MATRIX is the fixture
  ledger). Keep the names here, strip them from ARCHITECTURE.

## Class C — preserve verbatim (3): NOT the project

TEST_MATRIX 399, 400, 401: `test_promoter_harvest_trio` is the literal test-function name for INV-58/59/60
(promote/harvest of approved text), traceable to tests/test_traceability.py:1847. "promoter" is a substring of
a function name. The gate must not flag it.

## Gate-design implication

- PRODUCT_SPEC + ARCHITECTURE: strict — after the sweep, no project name and no dated-incident provenance turn.
- TEST_MATRIX: allow the fixture-ledger names (line 172) and test-function-name substrings
  (`test_promoter_harvest_trio`). The gate scopes its strictness to PRODUCT_SPEC + ARCHITECTURE, and on
  TEST_MATRIX it reds a provenance turn (a dated incident) while permitting a fixture label and a test name.
- Detection patterns: a bare project name in PRODUCT_SPEC/ARCHITECTURE; a project name adjacent to an ISO date
  (a dated incident) anywhere in the three. Born with a known-red proof (INV-212), rides the suite + pre-push.
