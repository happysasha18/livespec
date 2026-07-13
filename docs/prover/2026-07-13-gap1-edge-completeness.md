# Prover record — INV-138, "a gated behaviour names every side of its gate"

**Pass run by:** product-prover (live-spec pack, base `live-spec-base` v1.0.9), lens set current on
2026-07-13 — which already includes the edge-completeness lens under review here (the delta arms its own
family's lens; this pass reads it as a reviewer of the clause's fit, not as a user of the lens).

**Mode:** CROSS-LINK on a single method-delta (a new composition-lens-family invariant), fresh-context
reviewer, not the author. Adversarial opening hypothesis: *the new lens duplicates an existing one,
contradicts a sibling, or the goal was missed.*

**Primary sources read (no summary trusted):**
- `PRODUCT_SPEC.md:1691` (prose clause, under `### Composing across axes`, after the INV-127 clause) and
  `:1933` (Formal-index row, Section "Composing across axes").
- `skills/product-prover/SKILL.md:283` (new "Edge-condition completeness" lens) against `:263`
  ("Bounds and edges"), `:264` ("Dependency reality"), `:282` (INV-136 interactive-overlap).
- `skills/spec-author/SKILL.md:283–290` (new "Edge completeness" facet) against `:262` (the pre-existing
  "empty, error, and loading states" facet) and `:276–282` (paired-transition facet).
- `ARCHITECTURE.md:44` (spec-author node owned anchors).
- `TEST_MATRIX.md:170` (M-280) confirmed under `### [node: spec-author]` (same node as M-267/INV-126,
  M-268/INV-127).

## Verdict

**Sound to land.** Zero must-fix. The new lens is a genuine sharpening, not a duplication; the two faces
share one real root; traceability is single-owner and complete. Two should-clarify notes below, each with a
cheap recommended edit the orchestrator may fold; one worth-considering.

## Adversarial questions — settled

1. **Duplicate of "Bounds and edges" / "Dependency reality"?** No. The new prover lens self-declares as
   "the mechanical face of the bounds and dependency probes above, run as a completeness sweep rather than a
   spot-check," and it carries obligations neither generic probe does: (a) an *exhaustive* sweep of every
   threshold-gated transition rather than a sampled habit-of-attention, (b) a *both-ends* completeness demand,
   (c) a *visible-pending* requirement for a reserved async slot. Added obligation is real — not empty
   restatement.
2. **One invariant or two?** Genuinely one. The root is stated ("a condition whose out-of-range or in-between
   state is left unspecified renders as nothing"). The async face is itself a threshold on a running quantity
   (time-since-request, pending = the region below the lower bound), so the two faces are the same shape, not
   force-fused. Consistent with the family pattern where each of INV-125/126/136 is one lens.
3. **Traceable and complete?** Yes. Owned by exactly one node (spec-author, `ARCHITECTURE.md:44`); Formal-index
   row present (`:1933`); one matrix row (M-280) under `[node: spec-author]`, matching how INV-126 (M-267) and
   INV-127 (M-268) are owned — the applier's two-row draft was correctly consolidated to one. See F2 for the one
   residue of that consolidation.
4. **Contradiction/overlap with INV-72, 125/126/136, or the empty/error/loading facet?** No contradiction — it
   is declared a member of the composition-lens family and the INV-72 blank-answer class, consistent with the
   siblings. One real overlap with the pre-existing "empty, error, and loading states" facet (F1).
5. **Register?** Clean. No banned `X — not Y` scissors frame ("not only at the one point" is additive, not the
   exclusive frame). No coined mechanism name ("range-and-lifecycle member" is descriptive; "faces of the wait"
   is ordinary figurative English, matching sibling clauses' register). No non-native phrasing.

## Findings

| id | finding | severity | folded / rejected |
|---|---|---|---|
| F1 | The spec-author async face (pending/arrived/failed, `spec-author:287–288`) overlaps the pre-existing "empty, error, and loading states" facet (`spec-author:262`): loading≈pending, error≈failed. The prover-side lens cross-references its parent probes ("the mechanical face of the bounds and dependency probes above"); the spec-author-side facet does not point at the loading/error facet it sharpens, so an author reading the list sees two near-identical facets. | should-clarify · over-general (abstraction) | must-fold (orchestrator to apply) — one clause. Fix: in the `spec-author` Edge-completeness facet (`skills/spec-author/SKILL.md:287`), after "write the three faces of a wait — pending, arrived, failed" add a pointer, e.g. "— the reserved-slot, visible-pending sharpening of the empty/error/loading facet above, not a second copy of it." This states what the async face ADDS (a reserved slot that renders blank in flight; a *visible* pending) over the generic loading state. |
| F2 | The Formal-index homes list for INV-138 reads "+ the matrix rows" (plural), a residue of the applier's two-row draft; only M-280 exists. Siblings INV-126 (`:1931`) and INV-127 (`:1932`) list NO matrix row in their homes at all, so this line is both stale-plural and inconsistent with the family. | should-clarify · internal-conflict (consistency) | must-fold (orchestrator to apply) — one token. Fix: in `PRODUCT_SPEC.md:1933`, drop "+ the matrix rows" from the homes clause to match INV-126/127 (homes name spec/prover/author, not the matrix row). If a matrix reference is wanted, singularize to "+ the matrix row (M-280)" — but sibling-alignment favours dropping it. |
| F3 | The clause could state that the async face is a *special case* of the threshold face (time-since-request as the running quantity, pending = below the lower bound), which would further justify the single-invariant fusion the doc already makes. Currently the two faces are presented as coordinate members sharing a root; the tighter containment relation is left implicit. | worth-considering · over-general (abstraction) | rejected (non-blocking, taste) — the fusion is already sound and defensible as written; making the containment explicit is an optional strengthening, not a gap. Left for the author's discretion; recorded so it is not re-discovered. |

## What I assumed

- I read the delta as a method change to the pack (a new invariant + its lens/facet/matrix homes), reviewed in
  CROSS-LINK mode against the composition-lens family, not a FULL re-prove of PRODUCT_SPEC.md.
- I treated the born-of incident (tlvphotos's returning-visitor line and story slot) as illustrative
  provenance, not a claim requiring code-pin verification — it is a dated incident note, consistent with how
  INV-125/126/136 record theirs.
- I judged register against the profile's standing bans (the `X — not Y` scissors ban, no-coined-names) as I
  recall them; I did not re-read the profile this pass.

## Coverage note

CRUD / authorization / invariants-per-state tables are N/A: the artifact under review is a method-document
delta (a review lens and its spec/facet/matrix homes), not a stateful product surface. The relevant coverage
is traceability across the five homes, confirmed above: prose clause · Formal index · prover lens · spec-author
facet · matrix row, single-owner under spec-author.
