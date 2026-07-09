# Prover record — feature-coverage trace (E-29, INV-73)

Date: 2026-07-09 (session 29, the 1.0 RUN item 2). Mode: CROSS-LINK (small skill/infra delta — one
new machine bullet + its guardrail; no new user-facing surface). Prior records clean: the last full
re-prove is `2026-07-09-full-reprove-session29-body.md`; its unfolded rows are the queued design
findings (ROADMAP 173-179), untouched here.

## The delta in one line
A feature layer above the anchor matrix: live-spec's primary unit is its person-facing scenario, each
tagged `[feature: F-x]`, mapped in ARCHITECTURE.md's Feature coverage table to implementer node(s) + a
real test, with a two-way guardrail (`TestFeatureCoverage`).

## Cross-link checks

| Seam checked | Verdict |
|---|---|
| E-29 owned by exactly one node | PASS — guardrails node owns E-29/INV-73 (`test_architecture_owns_every_anchor_once` green) |
| INV-73 has ≥1 matrix row | PASS — M-180 (E-29) + M-181 (INV-73), both sides stated, BUILT, real tests |
| new seam named both sides | PASS — "unit → coverage" seam names what crosses + the two format owners (guardrails / spec-author) |
| no contradiction with the anchor matrix (INV-6) | PASS — the feature layer sits ABOVE the anchor matrix and reuses its ownership machinery; no second source of truth |
| no contradiction with pack-list parity (INV-66) | PASS — coverage rows name nodes, not skills lists; parity untouched |
| format's authoring home single | PASS — the format lives once in spec-author's "primary unit by project type" section; SPEC + ARCHITECTURE reference it |
| INV-72 unwritten-seam (co-present surfaces) | N/A — the trace is a doc-level infra machine, not a stateful user surface; no view/mode/co-present axis applies |

## Should-clarify (folded as a boundary, not a blocker)
The reverse guard (`test_every_scenario_carries_its_feature_tag`) is anchored to the KNOWN nine
person-facing scenarios: it catches a dropped tag on any of them and all tag↔table drift (both
directions, real-node, real-test). It does NOT auto-detect a brand-new scenario authored later without a
tag, because distinguishing a scenario H3 from a rule/reference H3 mechanically is itself ambiguous. The
mitigation is the spec-author format section, which instructs tagging each new scenario as it is written.
For live-spec's own dogfood this boundary is accepted; a fully-general "every scenario must be tagged"
checker is a candidate wish if a host needs it.

## Red-first proof
`TestFeatureCoverage` was written and run against HEAD first: RED (no tags, no E-29/INV-73, no coverage
table). Artifacts then added; suite GREEN at 213 (was 209). The never side (`test_stripped_coverage_goes_red`)
runs the pure checker on a deliberately broken table and asserts it catches a tagged-but-unmapped unit,
an orphan row, a fake node, and a fake test.

Verdict: FOLD — no must-fix. One should-clarify recorded above as an accepted boundary.
