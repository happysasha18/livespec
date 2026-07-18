# Skill review — live-spec-base, build-pipeline (ROADMAP 407, INV-217)

SKILL-REVIEW

Skill: live-spec-base
Skill: build-pipeline

Date: 2026-07-18
Reviewer: skill-creator (emulated at the build-pipeline commit step for ROADMAP 407)

Verdict: passes; both bodies reviewed, no description scope change and no triggering change. The
release-tier rule (when a release is a patch, a minor, or a major, read off what taking it costs a host)
now lives as base rulebook rule 32 — the law a host reads — with build-pipeline's commit-and-show step
carrying a pointer to it at the exact spot a release bumps its version.

## What changed

- **live-spec-base/SKILL.md** — a new numbered rule 32 (SPEC INV-217) stating the release-tier rule: a
  release's number reports what a host that vendored the previous version must do to take this one — a
  patch (host does nothing), a minor (host re-runs its catch-up walk with nothing rewritten), a major (a
  host cannot take it without changing what it already carries, and it ships its dated MIGRATION.md
  chapter). The rule states honestly that the minor-versus-major call is a judgment held by no machine,
  the same standing as a design-review finding that never blocks a lane [INV-141]. The frontmatter
  description's rule count follows the body: "thirty-one rules" → "thirty-two rules" (and README's
  mirrored count with it), keeping test_base_description_counts_the_rule and
  test_base_rule_26_homes_design_principles green.
- **build-pipeline/SKILL.md** — the step-9 "Bump the version (PATCH by default)" sentence gains a pointer:
  the number reports what taking the release costs a host, the tier read off that cost (base rule 32 /
  SPEC INV-217), and the minor-versus-major call is a stated judgment held by no gate. This routes a
  releasing session to the rule at the moment it picks the number. It is a pointer, not a second home.

## Why base rulebook is the home (and build-pipeline only points)

Base rule 4 gives every fact one home. The release-tier rule is a host-facing law, so its operative home
is the base rulebook a host reads (the INV-65 → base-rulebook precedent: a host-facing law lives as a base
rule, and the working skills reference it). The SPEC clause INV-217 is the formal invariant; build-pipeline
references it. No duplication of the normative statement.

## Findings

- **Description accuracy (skill-creator's first check): PASS.** Neither skill's description scope changed.
  The base rulebook's description still lists its themes; only the rule count moved, and it moved to match
  the body (thirty-two), so the count-derivation tests stay green.
- **Placement / no duplication (base rule 4, SPEC INV-13): PASS.** The normative rule lives once, as base
  rule 32; the SPEC carries the formal invariant clause; build-pipeline carries a pointer. Ownership pins
  to one node (base-rulebook) in ARCHITECTURE.md.
- **Triggering: PASS.** No `description` or `name` edit that changes what either skill triggers on.
- **Writing laws: PASS.** New prose is native plain English. No banned contrast frame ("X — not Y"). No
  significance-inflation. The sentence carrying the owner's authority names the exchange impersonally —
  "the owner asked for this guidance on 2026-07-17 ~15:45, saying it would be useful" [INV-120].
- **Cross-references resolve: PASS.** INV-91, INV-141, INV-178, INV-217, MIGRATION.md, and base rule 32
  all exist in the tree.
- **Honesty (rule, not gate): PASS.** Both homes state plainly that the minor-versus-major call is a
  judgment held by no machine, so no reader mistakes the guidance for a blocking check. The 2.0.0
  boundary case (its migration chapter records "Host action: none", so by the rule it reads as a minor)
  is named and left cited rather than restamped.
- **Size gates: PASS.** Neither skill carries a size-thinned ideal this edit breaks; build-pipeline's body
  gains one sentence, live-spec-base one rule.

None rejected; none outstanding.
