# Skill review — build-pipeline (the INV-49 fan-out: co-location draws no lane edge)

`SKILL-REVIEW`

Skill: build-pipeline
Date: 2026-07-21
Reviewer: skill-creator (Anthropic) — review method applied against the diff from a fresh read

Verdict: passes — the two reworded lines sharpen the lane-graph edge rule to match the sharpened
INV-49, stay in register, cite anchors that resolve, and change no triggering surface (the
`description:` frontmatter is byte-for-byte identical). Body reviewed; description reviewed. One
non-blocking wording-consistency note recorded below.

## What changed

Two hunks in `skills/build-pipeline/SKILL.md`, both the INV-49 fan-out that loosens the lane-graph
edge from "any shared surface / spec section" to "true dependency or same-section/same-behaviour
collision", with mere co-location in a shared living doc explicitly not an edge.

- The **"Trains, one pen" (SPEC T-18, INV-39)** bullet: "pairwise independent: no shared surface, no
  shared spec section" becomes "pairwise independent: no true dependency between them and no
  same-section collision — mere co-location in a shared living doc is not an edge."
- The **"Lanes are picked by a graph" (SPEC INV-49)** paragraph: the edge rule "an edge wherever two
  rows share a surface, a spec section, a skill file, or a doc region" becomes "an edge only on a true
  dependency (one row needs another's landed output) or a same-section / same-behaviour collision (the
  two rewrite one clause or one behaviour's rule). Mere co-location in a shared living doc draws no
  edge: the shared living docs (PRODUCT_SPEC, ARCHITECTURE, TEST_MATRIX) are a convergence point
  reconciled at integration, never a serializing surface." The downstream sentence gains "co-location
  included" so a co-located pair is routed to isolated build stages with a declared landing order.

## How this review was run

A fresh read of the diff against the surrounding lane-and-pen section, the concurrent-edit fence it
elaborates, and INV-49 / INV-214 as the spec authority. The hunt was for an incoherent rule, a
dangling anchor, a moved trigger, and — the crux here — a change that would let two genuinely
dependent rows open in parallel.

## Findings

- **The sharpening is coherent and does not open a real dependency to parallelism (clean).** The new
  edge rule keeps both real serializers — a true output dependency and a same-section/same-behaviour
  rewrite — and only removes the over-broad "shared doc region" trigger. A row that needs another's
  landed output, or that rewrites the same clause, still draws an edge and still serializes. What is
  newly allowed to run in parallel is exactly the case the fence already covered another way: two rows
  that merely both land in the shared living docs, reconciled under the single pen at integration. The
  loosening is safe because the pen still serializes the shared-doc writes — the edge governs lane
  independence, the pen governs the merge, and the two are correctly kept distinct.

- **Anchors resolve (clean).** SPEC T-18, INV-39, INV-49, INV-214, INV-129 are all cited in the same
  section and unchanged; no anchor was added or dropped by the edit.

- **Trigger surface unchanged (clean).** The diff touches only body lines 467–482; the `description:`
  frontmatter and the `## When to use` framing are untouched, so no routing surface moved.

- **Minor wording-consistency note (accepted, non-blocking).** The "Trains, one pen" summary bullet
  writes "no same-section collision" while the authoritative graph rule below writes "same-section /
  same-behaviour collision" — the summary omits the "same-behaviour" half. The graph paragraph is the
  normative statement and carries both halves; the bullet is a one-line gloss. Not a regression, but a
  later editor could align the bullet to "same-section / same-behaviour" for exact parity. Left as an
  observation, not a blocker.

- **Consistency across the two co-changed skills (clean).** The same fan-out lands in
  live-spec-base's "lanes under one pen" bullet; the two now state one rule — the shared living doc is
  a convergence point the pen reconciles, never a lane edge — from their two altitudes, with no drift
  between them.
