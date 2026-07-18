# Skill review — spec-author, product-prover (ROADMAP 379 enumeration-reads-as-list, INV-215)

SKILL-REVIEW

Skill: spec-author
Skill: product-prover

Date: 2026-07-18
Reviewer: skill-creator (emulated at the build-pipeline landing of ROADMAP 379)

Verdict: passes; both bodies reviewed, no description or triggering change. The structure rule spec-author
already carried ("Use lists inside a scenario to break up a wall of prose") gains the explicit
three-or-more enumeration threshold and its INV-215 anchor, and the prover's cognitive-load lens gains the
reading-load reading of the same rule as a recommendation. Both are additive elaborations inside existing
sections; neither skill's when-to-use, description, or trigger set moved.

## What changed

- **spec-author/SKILL.md** — a new bullet after the "Use lists inside a scenario" rule states the
  enumeration threshold (SPEC INV-215): a prose paragraph packing an enumeration of three or more distinct,
  parallel facts earns bullet or numbered structure, prose staying for the laws, their reasoning, and their
  boundaries. The bullet also carries the honest verdict — the rule earns no mechanical lint of its own,
  because a regex flagging every three-comma sentence would trip on rhetorical triads, and the genuine
  vs. rhetorical call is a meaning judgment the register judge and the prover make.
- **product-prover/SKILL.md** — the cognitive-load lens row in the plain-label lens table gains the
  reading-load reading: a prose paragraph packing an enumeration past the threshold is a reading-load
  recommendation (never a block), the fix being spec-author's structure rule (SPEC INV-215).

## Findings

None. The edits add no new trigger surface and no new gate; the description and body register are
unchanged in kind. The rule is a doc-style recommendation, not a mechanical check, so no skill gained a
gate-wiring responsibility.
