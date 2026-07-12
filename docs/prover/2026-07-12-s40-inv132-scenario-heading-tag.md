# Prover record — INV-132 (scenario-heading tag convention) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, skill/infra kind, no new surface, no structure change).

## The delta

One invariant, INV-132: the reverse direction of the feature-coverage check [INV-73] has teeth through a
heading convention. Every H3 heading in PRODUCT_SPEC.md carries either its `[feature: F-x]` tag (a
person-facing scenario, mapped by the coverage table [E-29]) or the explicit `[not a scenario]` marker (a
machinery, rules, or reference section, legitimately untagged); an H3 carrying neither is unambiguously red,
so a forgotten scenario tag can no longer ship uncovered. Homes: the feature-coverage clause + Formal index,
and spec-author. Owning node: guardrails (owns-list + M-273). Test:
`tests/test_scenario_heading_tag.py` (5 assertions incl. the seeded red-proof, red against the 10 unmarked
H3s then green).

## Previous record's unfolded rows

`2026-07-12-s40-inv131-redoor-independence-rebuild.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (guardrails owns-list carries INV-132, beside INV-73/E-29 the feature-coverage trace
  it gives teeth); matrix row M-273 sits under the guardrails block and cites INV-132; Formal-index row
  present. Index density, owning node, and matrix-row-under-owner all hold.
- Composition clean. INV-73 (the two-way feature-coverage check) is the invariant made enforceable, never
  contradicted: its reverse direction ("every scenario carries its tag") now has a mechanical floor instead
  of resting on a hand-walk. E-29 (the per-project-type primary unit tagged inline) is honoured — the
  `[feature: F-x]` tag stays exactly as it was, the marker only names the complement so the checker can tell
  the two apart. The 10 machinery/rules/reference headings now carry `[not a scenario]`; none is a
  person-facing scenario, so none should have a feature tag.
- No collision with the existing parsers. The `[not a scenario]` marker carries no PREFIX-NUMBER token, so
  the Formal-index symmetry and body-anchor scans ignore it; the `[feature: F-x]` regex and the "### Formal
  index" / "## Open decisions" split points still match as substrings, verified by the green traceability
  and formal-index suites.
- The check reads the shipped spec (not a fragment); the red-proof seeds an untagged H3 into a copy and
  asserts the pure checker catches it, and asserts a marked and a tagged heading are each spared — the never
  side stands permanent. The existing `test_every_scenario_carries_its_feature_tag` (the hardcoded-list
  forward direction) is untouched and still green, so both directions now hold.

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
