# Skill review — live-spec-base (base rule 34: re-derive a deferred item's state from code before resuming)

`SKILL-REVIEW`

Skill: live-spec-base
Date: 2026-07-21
Reviewer: skill-creator (Anthropic) — review method applied against the diff from a fresh read

Verdict: passes — the added rule states one law in the base-rulebook's own format, cites anchors that
resolve, stays in register, and its description-count change is synced with the body. Body reviewed;
description reviewed.

## What changed

Two hunks in `skills/live-spec-base/SKILL.md`:

- **Base rule 34 added** (SPEC INV-247): before a session resumes a deferred or queued item, the first act
  is a freshness check of the item's own subject against the shipped source — read the code the item
  touches, confirm the problem the row describes still holds, and re-derive the item's real current state
  before designing on it. It cites rule 13 (primary source), rule 8 (freshness at breakpoints), and INV-129
  (the queue-take trigger re-scan) as its neighbours, and draws the read-the-trigger / read-the-internals
  line that keeps it distinct from INV-129.
- **Description count 33 → 34** — the `description:` frontmatter's "thirty-three rules in the body" moved to
  "thirty-four rules in the body". This is a triggering surface, so it is called out here; the rule count on
  disk (34) now matches the description, the README, and the guard test `test_base_rule_33_states_it`.

## Judgment

- **Format.** Follows the `N. **Bold imperative title (SPEC INV-x).**` shape of every numbered rule, with
  the SPEC anchor trailing in the title parens. Placed after rule 33 and before the "When NOT to load this"
  heading — the correct insertion point.
- **Register.** No denied-neighbour contrast frame, no calque, no coined term without gloss. The role-plus-
  date attribution ("The owner asked the pack to hold it, 2026-07-20") matches rule 33's own precedent.
- **Consistency with the spec.** The rule is the base-rulebook face of INV-247; the two agree on WHEN (the
  first act of resuming the one item) after the prover's must-fix was folded into the spec clause.
- **Count synchronization.** stamp-versions.py stamped the base to v3.4.0; the description count, README, and
  the hardcoded guard-test literal all moved together, so no surface reports a stale count.

Non-blocking notes: none.
