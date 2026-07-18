# Skill review — product-prover, design-reviewer (the node-growth re-ask and split proposal)

SKILL-REVIEW

Skill: product-prover
Skill: design-reviewer

Date: 2026-07-18
Reviewer: skill-creator (Anthropic)

Verdict: passes; both edits reviewed and sound. product-prover gains a seventh architecture-lens
check (the node-growth re-ask) that states cleanly and consistently with the other six; design-reviewer
gains a split-proposal finding that keeps the skill's two-objects shape, its strong-signal-only gate, and
its never-blocks stance. No must-fix. No description frontmatter changed on either skill, so no triggering
surface moved.

## What changed

The residual legs of ROADMAP rows 390/392 (commit 37365b8) added the node-growth law (INV-233) as a
review duty on both review skills:

- **product-prover** (Phase 0 Triage, the ARCHITECTURE.md bullet): the architecture lens goes from six
  checks to seven. The seventh is the node-growth re-ask — each node re-answers the three fitness
  questions on its pins as they stand now, since a node born right and later grown carries a standing yes
  no check re-reads (SPEC INV-122). Co-residence in one file, read as nodes-per-file from the doc's own
  pin column, is the mechanical face of a failed growth answer; the ratcheted counter
  `guardrails/node_growth_counter.py` reds any increase and rides the suite, and a split moves only
  through the architecture step and its re-prove (SPEC INV-233, INV-37). The "six checks" count and the
  lens-growth history sentence were updated to seven, dated 2026-07-18 to ROADMAP 390.
- **design-reviewer** (new section "The node-growth split proposal", SPEC INV-233): where an architecture
  is in view, an over-grown file earns the tight ask. The pass names the file and the two responsibilities
  co-residing in it, each with its node and the spec facts that node owns, asks whether the two should
  share one file, and offers a recommended default. The counter's red is a mechanical signal; the split
  is a design call the pass proposes, moving only through the architecture step and its re-prove.

## Findings

- **Seventh prover check states clearly and consistently (sound).** The added check follows the exact
  dotted-clause form of the other six, phrased as a duty with its SPEC citations, and names its watcher
  the same way check four (the budget check, INV-41) names its own. It explains its why — a grown node's
  standing yes goes unread — matching the skill's habit of grounding each check in a reason.

- **Count and history stay internally consistent (sound).** "six checks" became "seven checks", and the
  lens-growth narrative ("grew from three checks to six ... grew to seven on 2026-07-18") tracks the new
  total. This is the count-drift a review of this edit most needs to catch, and it holds.

- **The re-ask does not collide with the birth-time fitness check (sound).** Both the second check and the
  seventh cite INV-122, but they are distinct duties on one invariant: the second flags a one-caller node
  as speculative at birth; the seventh re-applies the three-question test to a grown node's current pins.
  The seventh states its distinctness plainly ("as they stand now"), so the two read as birth-time versus
  growth-time, not as a redundancy.

- **Split-proposal shape matches the existing finding shapes (sound).** design-reviewer's core finding
  (step 5) names two concrete objects, the shared role, the divergence, a question, and a recommended
  default. The split proposal instantiates the same shape (the file plus its two co-resident
  responsibilities, a question, a default) and states so explicitly (SPEC INV-142). It keeps the skill's
  strong-signal-only gate (an over-grown file at its ratchet), its silence discipline (silent where the
  nodes still earn co-residence), and its never-blocks stance ("a recommendation or a question, never a
  block"), all consistent with the skill's description and its boundary-with-the-prover section.

- **The two edits compose without contradiction (sound).** Both cite INV-233 and describe one mechanism —
  node co-residence, the ratcheted counter, the split through the architecture step — each at the altitude
  its skill owns: the prover as a review lens (does the architecture re-answer node fitness), the design
  reviewer as a finding shape (propose the split with two objects). The counter reds, the prover asks, the
  reviewer proposes, and the split lands only through the architecture step. One home per fact holds; the
  counter mechanism is described for each skill's own duty and owned by neither.

- **Description / triggering (none).** The diff touches only body prose in both files; neither
  `description` frontmatter changed. The trigger surfaces are untouched and no eval drift is expected.

- **No coined names (sound).** "The node-growth split proposal" and "the node-growth re-ask" name their
  mechanisms in plain words; no metaphor or invented term entered.

- **Minor coverage observation (folded, no change needed).** design-reviewer's frontmatter frames the
  skill around undeclared same-kind groups and their behaviour parity; the split proposal is a different
  flavour of finding (a co-residence split, not a same-kind divergence). It still sits under the
  description's umbrella — a tight ask with two objects that never blocks a landing — and no description
  edit shipped this landing, so the trigger surface stays as reviewed. Worth a note if a future landing
  broadens the frontmatter, but nothing to fix here.

- **Version stamp:** no skill-version bump this landing (the pack stays 2.6.3); the changes are body law
  under the pack's existing version, and this record ships in the same commit as the reviewed edits.
