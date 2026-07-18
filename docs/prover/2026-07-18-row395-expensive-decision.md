# Prover record — 2026-07-18 — row 395 (an expensive decision earns an adversarial read before it lands)

Mode: CROSS-LINK. One new law on the build-pipeline node (INV-235), seaming to the verify-audit law
it sits beside and to the five decision-point clauses it names. The whole spec was proven FULL at the
2026-07-17 MINOR gate and re-checked on the 2026-07-18 batches, with no structural change since; this
pass proves the new law against the named existing surfaces it seams to. Single senior seat, no worker
dispatch [INV-103]. Previous prover records' unfolded rows: none open.

## The reference check (ROADMAP row 395's own caution)

The row cites a "Karpathy advocate/prosecutor" idea, flagged unverified by the owner. Web check
(WebSearch + WebFetch of github.com/karpathy/llm-council): Andrej Karpathy's real published artifact is
the **LLM Council** — a three-stage process (first opinions from every model → anonymized peer review
and ranking → a designated Chairman synthesizes the final answer). Its documentation names no
"advocate", "prosecutor", "skeptic", or "judge" role; the only named role is the Chairman. The specific
"an advocate and a prosecutor arguing before a decider" shape is community elaboration of role-assigned
councils rather than Karpathy's own stated words. So the reference is NOT cited, and INV-235's road is stated
from the pack's own pieces only, as the row's caution directs.

## Surface under change

- **INV-235** (ROADMAP 395) — an expensive decision (one whose reversal costs more than making it did)
  earns an adversarial read before it lands. The class is a closed, enumerable set named in full on the
  enumerate-versus-ride keying [INV-226]: a new agent's birth [T-22], a node carve or merge
  [INV-113, INV-122], a contract's shape once a consumer pinned it [INV-187], a project's kind [INV-36],
  a repository going public [INV-44]. The read is assembled from owned pieces — a fresh-context
  best-tier audit [INV-46, INV-145] and, where a kind is in question, the design review's two-objects
  read [INV-141, INV-142] — closing by bringing the decision to the human with findings and a
  recommendation, the taste call staying his [INV-152]. Agent birth carries it: T-22's ratification now
  names the read the owner ratifies on. Owning node: build-pipeline. Spec + test, no new gate.

## Cross-link seams checked

| Seam | Both sides present + named the same? | Verdict |
|---|---|---|
| INV-235 ↔ INV-46 (the verify audit) | yes — INV-235 leans on INV-46's fresh-context adversarial checker for the read | clean: INV-46 states the checker is a differently-contexted head briefed from primary sources on the goal-missed hypothesis, set on breaking the work; INV-235 reuses that exact stance for a decision rather than a landing, and INV-46's clause stands whole |
| INV-235 ↔ INV-145 (the periodic audit) | yes — INV-235 names the adversarial stance the periodic audit takes as well | clean: INV-145 says an audit is adversarial by nature, a whole-read that sets out to break the work; the citation names the shared stance, no wording of INV-145 changed |
| INV-235 ↔ INV-141, INV-142 (the design review) | yes — the two-objects read applies where the decision turns on whether several things are one kind | clean: INV-142 owns the design review's two-objects-in-hand finding shape; INV-235 invokes it only for the grouping sub-case, consistent with the design review's own scope (a same-kind grouping in question) |
| INV-235 ↔ INV-152 (the human-only taste call) | yes — the taste call on the specific decision stays his | clean: INV-152 governs what pins to a fact only the human holds; an expensive decision's own resolution is such a fact (its cost only he carries), so INV-235 defers the call and states only the road that informs it — no conflict with INV-152's derive-before-defer posture, since the road is derived and only the final taste is deferred |
| INV-235 ↔ INV-226 (the enumerate-versus-ride keying) | yes — the members are a closed, enumerable set, so the clause names every member | clean: INV-226 keys enumeration on a closed set; INV-235's members are finite and nameable (they grow a member at a time by incident), so the enumerate side is the correct choice, and the clause states it explicitly |
| INV-235 ↔ T-22 (agent birth, the first member) | yes — T-22's proposal now carries the read and the owner ratifies on it | clean: T-22 already called agent birth expensive and the owner's call; INV-235 names WHAT he ratifies on (the adversarial read), extending the two existing sentences without contradicting the two-acts-on-two-objects structure — the read informs the founding act, the declaration act is untouched |
| INV-235 ↔ INV-113, INV-122 (node carve/merge) | yes — a node carve or merge is a named member | clean: INV-113 (deliberate redesign re-shapes and re-proves) and INV-122 (the three-question fitness test at a node's birth) are the carve/merge decision points; INV-235 names the carve/merge as expensive, adding the adversarial-read duty on top of the existing fitness gate, no overlap |
| INV-235 ↔ INV-187 (a pinned contract's shape) | yes — the shape of a contract once a consumer pinned it is a named member | clean: INV-187 gives the consumer a pinned version it reads until it chooses to move; re-shaping a pinned contract is expensive because every consumer's pin is at stake — INV-235 names the shape-change decision, INV-187's pin mechanism unchanged |
| INV-235 ↔ INV-36 / INV-44 (project kind / going public) | yes — both are named members | clean: INV-36's project-kind call and a repository going public are decisions costly to unwind (a kind reshapes the whole method's form; a public repo cannot be un-published); INV-235 names them as members and leaves each clause's own machinery whole |

## The footprint / gate-chain question

The row reads cross-cutting (a new method invariant that names five decision-point clauses), but its
concrete write-set is small: the INV-235 clause, its Formal-index row, two T-22 sentence extensions, one
ARCHITECTURE owns-list entry, one matrix row, one test file. No mechanical gate is added, and this is the
deliberate design: an expensive decision cannot be told from an ordinary one by a machine — no gate reads
a reversal cost — so the duty is a STATED DUTY at the enumerated decision points, held by the traceability
test `tests/test_expensive_decision_read.py` riding the suite, the far-tier [INV-222] and node-growth
[INV-233] checks the precedent for a check that rides the suite and mints no push-gate letter.
`.github/workflows/gates.yml` and `guardrails/gate-red-proofs.json` are UNTOUCHED; the gate-machinery
reach meta-tests correctly skip (the diff touches no gate file), and the gate-marker set is unchanged.

## Red-first proof

`tests/test_expensive_decision_read.py` was written against HEAD 35069ba and run before any
implementation: 9 failed, 1 passed. The one pass is `test_duty_rides_the_suite_not_the_push_chain`, the
honesty check that asserts INV-235 is ABSENT from the gate red-proofs — correctly green before and after,
since no gate was wired. After the delta: 10 passed on the file, 181 passed with the traceability suite,
1560 passed on the full suite, 2 skipped (the two gate-machinery reach meta-tests, the expected pinned
set). Red output saved to `docs/prover/red-proof-2026-07-18-row395.txt`.

## Fresh-eyes audit (SPEC INV-46) and its fold

This row edits the method (a new invariant), so a fresh-context checker read the shipped files on the
"tasks completed, goal missed" hypothesis, briefed from the spec sentences and the artifact paths only.
It confirmed the class definition, the T-22 carry, the honesty of the no-detector framing, the writing
laws, and the absence of any Karpathy/advocate/prosecutor citation. It raised four findings, all folded
before this commit:

| # | Finding | Fold |
|---|---|---|
| 1 (most severe) | The clause read "the duty is stated at each of these decision points and a traceability test holds that the points name the read" — true for agent birth alone; the other four members' own clauses do not name the read, and the test checks only T-22 at its locus. | Reworded: the clause states the duty for the whole class, each member carries it at its own point as the pack wires it member by member, agent birth the first wired; the traceability test holds that the class clause names the read and that agent birth carries it. The overclaim is gone, the honest scope matches what M-416 and ARCHITECTURE already said. |
| 2 | INV-152 alone cited for "the taste call stays his"; INV-152 is the deferral-derivability law, so a reader following it lands on a mechanism rather than the taste statement. | INV-143 (the orchestrator surfaces a decision only where it genuinely needs the human — a taste call) added as the direct home, INV-152 kept for the fact-only-he-holds half: "surfaced as a call only he can make [INV-143] because it needs a fact only he holds [INV-152]". |
| 3 | "at the best tier" attributed to INV-46/INV-145, neither of which names a tier — "best tier" is the quality-over-budget habit and appears in neither invariant. | Re-attributed: "run at the best tier the pack's quality habit sets", the [INV-46]/[INV-145] citations now carrying only the fresh-context and adversarial-stance claims they actually own. |
| 4 (candidate gap) | Sweeping for missed members, the engine/instance split [INV-85] meets the class definition (a founding-shape call the human decides, costly to unwind: merging back or splitting a monolith later restructures repos and a published engine contract), and it is distinct from a project's kind [INV-36] (kind is the book/backend/fullstack/CLI/skill-pack axis, orthogonal to the split). | Admitted as the sixth member across the clause, the Formal-index row, ARCHITECTURE, M-416, and the test's `test_members_swept_enumerated`. The audit's other candidates were dismissed on its own read: a MINOR bump and local→remote are reversible or covered by "a repo going public", and the skill-vs-agent grain [INV-182] folds into agent birth [T-22]. |

After the fold: the test file's `test_members_swept_enumerated` and `test_road_states_owned_pieces` were
widened to hold INV-85 and INV-143, the spec re-frozen, and the full suite re-run green.
