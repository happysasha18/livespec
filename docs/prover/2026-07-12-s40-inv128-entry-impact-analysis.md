# Prover record — INV-128 (entry impact-analysis station) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.8. Mode: CROSS-LINK (the new station's seams against
the named existing intake laws) plus a faithfulness read against the architect draft's P1-P6. An independent
FABLE adversarial audit runs beside this pass on the owner's word (row 259: build, then Fable + prover, then
his review); its findings fold before the landing.

## The delta

INV-128, the entry impact-analysis station — the entry station (P1-P6) of the fourteen-principle architect
draft (`.live-spec/checkpoints/pending-design-principles-architect-draft.md`; Alexander live 2026-07-12):
every request is read at intake against three sources (spec · architecture · code) producing one named
footprint (presentation-only · single-module · cross-cutting), spoken in the capture echo and written in the
row's `footprint:` note; the footprint decides the route (light road · the matrix step against the module's
interface · the full pipeline); a source disagreement is a finding routed to its owner (INV-37); the read is
the verdict derive-before-fork (INV-121) rests on; the footprint re-classifies mid-work; and the station
carries the boundary-health law (a right boundary keeps a typical request in one module, repeated cross-cuts
signalling a move through the architecture step's re-prove). Homes: the intake clause + Formal index,
build-pipeline step zero, ARCHITECTURE's boundary-health law, product-prover's three-source lens,
communicator's capture echo. Owning node: build-pipeline (owns-list + M-269). Test:
`tests/test_impact_analysis_entry.py` (10 assertions, red-proven then green).

## Validated on one real request of each footprint class (row 259 Done-when)

- **cross-cutting** — INV-128's own landing touches the spec, build-pipeline, ARCHITECTURE, product-prover,
  and communicator: five homes across the method, so it took the full pipeline from the spec step. A textbook
  cross-cutting footprint.
- **single-module** — today's INV-126 (paired-transition symmetry) added one facet living only in
  spec-author's canonical list plus its prover lens: one owned layer, so a single-module footprint entering
  at the matrix step against the spec-author block.
- **presentation-only** — a README hero-line reword touches what the audience meets and nothing behind it:
  the light road (the docs-only door widened to presentation).

The three roads map onto existing pipeline entries (the skip/docs-only boundary, the matrix-step entry, the
full pipeline), so the footprint keys the EXISTING roads rather than inventing a parallel routing system.

## Findings (product-prover pass)

**0 must-fix from this pass.** Cross-link checks walked:

- Owning node present (build-pipeline owns-list carries INV-128); matrix row M-269 under the build-pipeline
  block; Formal-index row present.
- INV-121 citation stands (row 259's hard Done-when leg): the clause states the three-source read is the
  verdict derive-before-fork rests on — the read is what tells whether a proven artifact already settles a
  question, closing row 270's leg 3 (which wired the citation into row 259's Done-when).
- No contradiction with the door (INV-16) or the skip/docs-only entries: the footprint is a THIRD intake
  dimension beside the door and work-kind, keying the existing roads; the mid-work re-classify is the
  explicit sibling of the door's mid-work re-fire, not a rival.
- Honest deferral: the mechanical enforcement (the `footprint:`-note suite check, the per-kind
  concrete-layers declaration, the cross-cut counter) is stated as riding follow-on rows, never claimed as
  live. The single-module road's interface-tests machinery (draft R5) is likewise future; the clause names
  "the module's interface and its own tests" as the road's shape without claiming the interface-test
  guardrail already exists.

The Fable adversarial audit's findings are folded in a section appended below before the landing commits.

## Fable adversarial audit — findings folded before landing (2026-07-12)

An independent Fable pass read all primary sources (the architect draft P0-P12, the landed homes, the door
law T-12/INV-16, INV-121/45/61/49, the test, the git diff), ran the suite (525 green), and reported. Its
verdict: substantively faithful to P1-P6 with honest deferrals, but not yet coherent with the door law. Two
must-fix, folded here:

- **F1 (must-fix) — the single-module road let a feature skip the spec step, contradicting INV-16.** The
  clause read "a single-module change enters at the matrix step", but the door law forbids a feature
  skipping the spec step, and any unbacked behaviour is a feature by tripwire 1. FOLDED: the routing
  paragraph now states the footprint COMPOSES with the door and never overrides it — the door decides which
  steps run, the footprint decides how far each step reaches; a feature never skips the spec step whatever
  its footprint; a single-module bug/refactor takes the existing matrix-step entry, a single-module feature
  keeps its spec step with the rest scoped to the one module. Homed identically in the spec clause and
  build-pipeline step zero.
- **F2 (must-fix) — "docs-only door widened to presentation" was asserted only inside INV-128, diverging
  from T-12's own home.** FOLDED: the light-road sentence is scoped to what the door already grants — the
  skip boundary or the docs-only door where the door routes it there, and the matrix-step minimum for a
  visible feature. INV-128 no longer silently re-defines the docs-only or skip doors; T-12 stays the one
  home for the door routes.
- **F3 (should-clarify) — the interface-test machinery was the one deferred piece the deferral note
  omitted.** FOLDED: the deferral parenthesis now names "the declared-module-interface and interface-level
  test machinery" among the follow-on pieces.
- **F6 (should-clarify) — the capture echo lacked the work-kind field P2 specified.** FOLDED: rule 12's echo
  now carries the work-kind (product · infra · skill · prose) beside the door and footprint.
- **F4 (should-clarify) — the route validation was retro-classification, restated honestly.** See the
  corrected validation note below: with F1 folded, the single-module witness (INV-126, a single-module
  feature) correctly KEEPS its spec step scoped to spec-author's block, so it now agrees with the law's
  letter rather than contradicting it. The presentation-only witness is labelled a classification of past
  work, not a walked route; walking one real request of each class under the live law is left to the law's
  first real uses (it binds forward).
- **F5 (worth-considering) — dogfood bookkeeping.** The closing landing carries row 259's own
  `footprint: cross-cutting` note and its "footprint held" line, so the law's first act obeys the law.

Corrected validation: a single-module FEATURE keeps its spec step (INV-126 walked the spec step and scoped
its work to spec-author's block — this is the law as folded, not a contradiction). A single-module bug or
refactor takes the matrix-step entry. A cross-cutting change (INV-128's own landing, five homes) takes the
full pipeline. A presentation-only reword takes the lightest road its door grants.

Verdict after fold: coherent with the door law; INV-16's spec-step guarantee is explicitly preserved. 0
open must-fix.
