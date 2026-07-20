# Skill review — product-prover (new lens: false-serialization / over-broad independence edge)

`SKILL-REVIEW`

Skill: product-prover
Date: 2026-07-21
Reviewer: skill-creator (Anthropic) — review method applied against the diff from a fresh read

Verdict: passes — a single additive lens bullet joins the stress-test list, becoming the review
arm of the sharpened INV-49. It is symmetric (finds both a false serialization and a false
independence), correctly scoped to a senior read rather than a gate, cites anchors that resolve, and
disturbs no neighbouring lens. No triggering surface moved. Body reviewed; description reviewed.

## What changed

One added bullet in `skills/product-prover/SKILL.md`, in the per-operation stress-test list:
"**False-serialization / over-broad independence edge**" — a lens that reads a concurrency plan (a
departures board, a lane set, a queue-take dependency graph) and flags both sides of INV-49's edge
rule: a plan that serializes two movements on mere shared-doc co-location, and an edge drawn without a
true dependency or same-section/same-behaviour collision; with the safety twin — two truly colliding
rows marked independent and opened in parallel — called out as a finding of equal weight. It carries
the `[INV-49]` anchor and cites SPEC INV-49, INV-214.

## How this review was run

A fresh read of the added bullet against its neighbours in the stress-test list (each a
one-invariant lens ending in a bracket anchor), against the sharpened INV-49 it enforces, and against
build-pipeline's graph rule and live-spec-base's base statement — the two skills this lens now
polices. The hunt was for a one-sided lens (catching only false serialization, missing false
independence), an over-claim that a gate could do this work, and a dangling anchor.

## Findings

- **The lens is symmetric — it guards both failure directions (clean).** A weaker version would only
  catch the newly-legalised case: two co-located rows serialized needlessly. This bullet explicitly
  names the safety twin — "two rows that truly collide ... marked independent and opened in parallel"
  — as a finding of equal weight. So loosening the edge rule did not create a blind spot for the
  dangerous direction; the prover is told to hunt both a false edge and a false independence.

- **Correctly kept a senior read, not a gate (clean, and consistent with INV-214).** The bullet states
  that a gate keyed on this "would red every lawful landing, since every movement lands in the shared
  docs" — so judging a false edge stays a senior judgement, not a diff a guardrail can decide. This
  matches INV-214 (independence is a senior read no gate can settle) and correctly explains why this
  lens lives in the prover rather than in `guardrails/`.

- **Claims match the spec it enforces (accurate).** "The shared living docs are a convergence point
  reconciled at integration, never a serializing surface" and the edge definition ("a true dependency
  — one movement needs another's landed output — or a same-section / same-behaviour collision") are
  the same wording as the sharpened INV-49 in build-pipeline and live-spec-base. The lens is a
  faithful review-side restatement of the authoring-side rule, not a new or divergent claim.

- **Anchors resolve (clean).** SPEC INV-49 and INV-214 are live invariants; the trailing `[INV-49]`
  bracket matches the list's convention (each sibling lens ends in its anchor, e.g. `[INV-128]`).

- **Additive only — no neighbour disturbed (clean).** The hunk is a pure single-line insertion after
  the INV-128 lens; no adjacent lens was reworded, so no existing review instruction changed under
  cover of the addition.

- **Trigger surface unchanged (clean).** The `description:` frontmatter is byte-for-byte identical;
  the new lens is body content that applies once the prover is already reviewing a document, so the
  routing surface did not move.
