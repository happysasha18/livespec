# Skill review — live-spec-base (the INV-49 fan-out in "lanes under one pen")

`SKILL-REVIEW`

Skill: live-spec-base
Date: 2026-07-21
Reviewer: skill-creator (Anthropic) — review method applied against the diff from a fresh read

Verdict: passes — one bullet gains a trailing clause that draws the write-vs-lane distinction
INV-49 now requires; the pre-existing rule (shared-doc writes serialize under the single pen) is
preserved verbatim and the clause only adds that this pen-serialization is not itself a lane edge.
No triggering surface moved. Body reviewed; description reviewed.

## What changed

One bullet in `skills/live-spec-base/SKILL.md`, "Lanes under one pen, up to the profile cap." The
existing sentence — "every write to a document the lanes share serializes under the single PEN, one
lane at a time" — is unchanged; it gains the trailing clause "— the shared living doc is a
convergence point the pen reconciles at integration, never an edge that serializes the lanes
themselves, so co-location alone never pulls two rows into one lane (SPEC INV-49)."

## How this review was run

A fresh read of the diff against the concurrent-edit fence section this bullet sits under, its four
sibling lane rules, and INV-49. The specific risk checked: whether the addition contradicts the pen
rule it extends, or blurs the two mechanisms (the pen that serializes shared writes vs. the graph
edge that decides lane membership).

## Findings

- **The write-vs-lane distinction is drawn correctly (clean).** The bullet keeps two separate facts
  that were previously fused into one: (1) writes to a shared document serialize under the single pen,
  one lane at a time — the merge discipline, unchanged; (2) that shared-doc convergence is not a lane
  edge, so two rows that only co-locate in the shared living docs stay independent lanes. Before the
  edit a reader could take "every write to a shared document serializes" as also meaning "so the lanes
  are dependent"; the added clause closes exactly that misread and aligns the base rule with INV-49.
  The pen still serializes; the lanes stay independent; the two are no longer conflated.

- **One home per fact — this is the base statement, elaborated in build-pipeline (clean).** The base
  skill carries the normative one-liner and the anchor (SPEC INV-49); build-pipeline elaborates the
  same rule into the queue-take graph mechanics. The base does not duplicate the graph procedure — it
  points at the invariant — so the "one home per fact" discipline holds across the two.

- **Anchor resolves (clean).** SPEC INV-49 is a live spec invariant; the citation is new to this
  bullet and correct. SPEC T-18 and E-13, already on the line, are unchanged.

- **Trigger surface unchanged (clean).** Only the one body bullet changed; the `description:`
  frontmatter is byte-for-byte identical, so live-spec-base's load-triggering surface did not move.
