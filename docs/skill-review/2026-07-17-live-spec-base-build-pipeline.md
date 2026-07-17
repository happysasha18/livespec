# Skill review — live-spec-base, build-pipeline (ROADMAP 415 read-back feed, INV-207)

SKILL-REVIEW

Skill: live-spec-base
Skill: build-pipeline

Date: 2026-07-17
Reviewer: skill-creator (emulated at the adversarial-review fix of ROADMAP 415)

Verdict: passes; both bodies reviewed, no description or triggering change. The human-authority writing
rule and the read-back feed are now carried in the base rulebook and the pipeline skill, closing the hole
an adversarial review found — sessions load skills, not PRODUCT_SPEC.md, so before this change no session
was instructed to anchor an attribution or feed DECISIONS.md.

## What changed

- **live-spec-base/SKILL.md** — rule 13 ("A claim needs its primary source") gains a paragraph stating
  the writing rule on human authority (SPEC INV-207): a sentence recorded AS the person's names the
  exchange it came from; a sentence the seat reasoned out is the pack's own voice; an autonomy grant
  authorizes deciding, never recording the decision as the human's; recording a decision as his adds an
  ANCHORED entry to DECISIONS.md, the read-back set shown on the asynchronous touchpoint cadence
  [INV-205, INV-206], the load-bearing defence a text gate cannot be. Extended rule 13 rather than adding
  a rule 32, so the rule count and every "thirty-one rules" reference stay correct.
- **build-pipeline/SKILL.md** — a paragraph in step 9 (Commit & show), where a landing report, a ROADMAP
  row, and a decision page record decisions: a `[default]` the seat picked is the seat's own judgment in
  the pack's voice, never dressed as the human's word; a genuine decision-as-his names its exchange and an
  anchored copy goes to DECISIONS.md; a grant authorizes deciding, never recording as the human's. This is
  the surface the founding fabrication was written into (a ROADMAP row), so the pipeline is its home.

## Why build-pipeline and not communicator

The communicator body is already at its ~500-line size ideal (the row-280 thinning ratchet), and the
surface where a decision-as-his first gets WRITTEN is the landing artifact build-pipeline authors — the
ROADMAP row the founding fabrication actually lived in. So the working-skill reference lands in
build-pipeline; communicator still shows the read-back as a person-opened touchpoint under the frame it
already carries [INV-205/206], needing no new line.

## Findings

- **Description accuracy (skill-creator's first check): PASS.** Neither description changed; both still
  describe their skill's scope. The base rulebook's "thirty-one rules in the body" stays accurate because
  the change extended an existing rule.
- **Placement / no duplication (base rule 13, SPEC INV-13): PASS.** The human-authority law is a special
  case of "a claim needs its primary source", so it belongs as rule 13's arm rather than a new rule; the
  normative statement lives once, in the base, and build-pipeline REFERENCES it ("base rule 13") and
  elaborates only its own domain (the landing surfaces where a decision is recorded).
- **Triggering: PASS.** No `description` or `name` edit, so triggering accuracy is unchanged.
- **Writing laws: PASS.** New prose is native plain English, states the rule in the pack's own abstract
  voice (no specific decision attributed to the person, so no anchor owed), carries no banned contrast
  frame and no significance-inflation.
- **Cross-references resolve: PASS.** INV-207, INV-205, INV-206, DECISIONS.md, and
  guardrails/check-authority-anchor.py all exist in the tree.
- **Size gates: PASS.** build-pipeline has no size-thinned gate; communicator's row-280 size ideal is left
  intact by keeping the reference out of it.

None rejected; none outstanding.
