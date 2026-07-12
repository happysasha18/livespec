# Prover record — INV-135 (per-kind concrete-layers and proofs declaration) — 2026-07-12 s41

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — the
delta is skill+infra kind, no new user-facing surface; the law's homes are base rule 24, the spec founding
clause, the host-profile record, the ARCHITECTURE per-kind table, spec-author/test-author, and a founding
check).

## The delta

One invariant, INV-135 (P0k of the fourteen-principle architect draft): the entry impact read, the
footprint categories [INV-128], and the test ladder are kind-abstract stations. Each project kind fills
them with its own concrete layers and its own concrete proof kinds. `project.kind` [INV-36], recorded at
founding, gains two companion lines in the host profile — `project.layers` (the concrete footprint
categories) and `project.proofs` (the concrete test-ladder rungs). A founding check reds a kind recorded
with neither, flagged at adoption the way an unbacked surface is [A-10]. ARCHITECTURE.md carries the
per-kind footprint-and-proof table; spec-author and test-author read the declared layers and proofs rather
than assuming code. Owning node: base-rulebook (base rule 24 is the invariant's clearest home; owns-list +
M-276).

## Previous record's unfolded rows

`2026-07-12-s41-inv134-footprint-note-enforcement.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Index density, owning node, matrix-row-under-owner all hold: the Formal-index row INV-135 is present;
  the base-rulebook node's owns-list carries INV-135 beside INV-98/INV-108 (its sibling base rules 22/23);
  matrix row M-276 sits under the base-rulebook block (moved there after the first cut placed it under
  build-pipeline, which the matrix-row-under-owner check red-caught — the check has teeth).
- Composition against every neighbour named. INV-36 (project.kind at founding) is the law this extends —
  the same founding line gains two companions, the ask staying the human's, no personal-profile seeding.
  INV-128 (the footprint categories) is generalized cleanly: the three footprints already hold past code
  in INV-128's own prose; this names the concrete layers each kind fills them with. INV-134 (the footprint
  note check) reads the declared categories rather than a hardcoded list — a forward reference the ratchet
  clause states, not yet mechanized (left to R3/R5), so no over-claim. A-10 (the unbacked-surface verdict)
  is the model for the founding check's flag, cited not contradicted.
- One-home held. The rule's normative home is base rule 24 (the base rulebook). spec-author, test-author,
  ADOPT.md, ARCHITECTURE, and the host profile all reference-and-elaborate it in their own domains — the
  pack's by-design elaboration, each a pointer at the base rule, not a parallel full statement.
- The founding check reads the profile RAW (line-anchored `project.*:` records), not the flattened prose
  read_flat gives — an early cut read flat and passed the incomplete live profile falsely; caught and
  fixed, so the check has real teeth (the live host profile went red until its layers/proofs lines landed).
- Red-proof honest: the three passing fixtures are the three real hosts (track-coach code/music, tlvphotos
  photo, promotion prose), and the founding check reds against a kind-only fixture and a missing-only-proofs
  fixture — the Done-when's "red-proven against three fixtures" met with a real red demonstrated.
- Scope: this row lands the declaration and the founding check; the footprint check and the test-level
  check actually READING the declared categories mechanically (rather than a hardcoded code list) is named
  as the ratchet but left to the R3/R5 machinery — a stated non-goal, not a silent gap.

## Verdict

CROSS-LINK clean, 0 must-fix. The delta generalizes the code-shaped stations to a kind-abstract shape with
a per-kind founding fill, composes cleanly with INV-36/INV-128/INV-134/A-10, and keeps one home for the
rule. Suite green at 562.
