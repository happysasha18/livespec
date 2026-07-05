# Spec-driven AI development, compared: BMAD-METHOD · Kiro · live-spec

*2026-07-06. Method: three independently-briefed agents with clean context — two senior analysts
(each told to research BMAD and Kiro on the web, read the live-spec repo from the files, treat its
self-descriptions as claims to verify, and be explicitly critical of all three, live-spec included)
plus one landscape scout mapping comparable projects. This document merges their findings without
softening them. live-spec is our own project; both analysts were told that must not bias them, and
their criticism is kept intact below.*

## The shared bet

All three put a written specification between the human's wish and the agent's edits, betting that
this produces less AI slop than free-form "vibe coding". They differ in weight, packaging, what
actually enforces the spec once it exists, and what you get locked into.

## At a glance

| Dimension | BMAD-METHOD | Kiro | live-spec |
|---|---|---|---|
| Form | Prompt/persona framework (~12 role agents: Analyst, PM, Architect, Dev, QA) | Proprietary AWS IDE (VS Code fork); requirements → design → tasks flow | Claude Code skill pack; wish → spec → prove → architecture → matrix → red tests → code → verify |
| Cost | Free, MIT | $0–$200/mo credit tiers, metered | Free, MIT |
| Portability | High — any LLM/IDE | Low — locked to Kiro IDE + AWS | Low — Claude Code only (documents are portable markdown) |
| Anti-drift mechanism | Story-file context embedding — discipline, not enforced | Steering files — documented by users to drift | Executable pre-push gates + traceability tests — enforced, first slice live |
| Ceremony per feature | Very heavy (6–7 handoffs) | Heavy (3-doc cycle) | Heavy (9 steps; bug/skip shortcuts exist) |
| Maturity | Mature, churny (~43–50K stars, v6, breaking renames) | GA, backed by AWS; unstable pricing history | Days old, single author, one real adoption (a sibling project by the same author) |
| Independent judgment | None — all personas are one model | None — single agent | None — all skills are one Claude |

## What each is strong and weak at

**BMAD-METHOD** is the most battle-tested: a huge community, cross-IDE portability, and the
story-file pattern (self-contained context per unit of work) is genuinely good context engineering.
Its costs are equally documented: an independent head-to-head clocked BMAD Full at ~6 days and ~$200
in AI spend for a task competitors finished in 1–2 days; its own issue tracker holds "I just burned
100K tokens and accomplished nothing" (#1188) and 82–96K tokens per story-creation step (#1235); one
logged issue shows the review workflow forcing a minimum of three findings per review — manufactured
nitpicks. Artifact-to-code sync relies on agent discipline, which is exactly where agents drift. All
personas run on the same model, so an Analyst's error is inherited, not caught, by the Architect.

**Kiro** is the most turnkey: the spec flow is first-class IDE UI, steering files give durable
context, hooks automate on save/commit, hunk-level review gives granular control. The price is total
lock-in to a paid AWS IDE — and a real pricing-history liability: the August 2025 restructuring was
publicly branded "wallet-wrecking", AWS later admitted a billing bug was draining users' request
limits, and capacity caps plus waitlists appeared days after launch. Users report specs that "keep
drifting until you have duplication and contradictions", and the default autopilot edits code without
approval — slop with a spec-shaped alibi.

**live-spec** is the only one of the three whose enforcement is executable rather than documentary —
and the youngest by two orders of magnitude. Both analysts independently confirmed the same
distinction. What one analyst verified by running it: the pre-push gate demands a fresh committed
prover record newer than the last spec change; a pin-drift check re-verifies that architecture →
code line references still resolve; a prototype fence fails the build if production code wires to a
sketch; a traceability test goes red on a spec clause no test covers. What is honestly NOT built
yet: the surface registry, CI mirror, and snapshot machinery are `[target]` — spec'd, marked, not
shipped. And the weaknesses both analysts converged on, kept verbatim in spirit: the repo was days
old at review time with a bus factor of one; the "production-proven" evidence largely belongs to a
sibling project by the same author; the judgment loop (spec-author, prover, pipeline) is one model
grading its own homework — only the mechanical gates are independent; and the spec's dense,
anchor-laden prose is a steep read for a second engineer. One analyst's live anecdote cuts both
ways: at the moment of his inspection the suite was RED — a ledger edit mid-session had an illegal
status — which means the flagship was not green when a stranger looked, and also that the gate would
have blocked that state from ever being pushed. (It was fixed the same hour; the fence did its job.)

## What breaks first under pressure

- **BMAD:** token economics and version churn — six-figure token counts on large PRDs; breaking
  renames between releases break your setup.
- **Kiro:** the wallet and the queue — metered credits punish iteration; capacity caps mid-task.
- **live-spec:** the human bottleneck and the bus factor — one author, one adopter, conventions that
  are load-bearing and (for now) explained only by the repo itself.

## Recommendation matrix (merged from both analysts)

| | Solo developer | Small team (3–10) | Enterprise |
|---|---|---|---|
| BMAD-METHOD | No — ceremony dwarfs payoff | Greenfield/design-critical only | Viable for regulated work; budget for tokens |
| Kiro | Greenfield, if metering is tolerable | Maybe, if AWS-aligned | Viable if AWS-committed |
| live-spec | **Best fit** — if you live in Claude Code and want enforced discipline without a bill | Not yet — unproven multi-author | No — too young, no track record |

Both analysts' bottom line on live-spec, unsoftened: the *idea* worth adopting today is enforced
traceability, freshness-gated review, and pin-drift checks; the *project* should earn a second user
before a team bets on it.

## The wider landscape (scout's pass, mid-2026, by traction)

- **GitHub Spec Kit** — 118K stars; the de-facto reference implementation of spec-driven development:
  Constitution → Specify → Clarify → Plan → Tasks → Implement, consumed by 30+ agents. The
  "constitution" step (durable principles gating every phase) is its distinguishing idea.
- **MetaGPT** — ~68K stars; the original "AI software company" (role agents auto-generate PRD →
  design → code with no per-artifact human sign-off). Adjacent category: autonomous generation, not
  spec-as-contract.
- **GSD / Open GSD** — ~65K stars pre-migration; meta-prompting against "context rot" — every task
  gets a clean context via spawned researcher/planner/executor/verifier sub-agents.
- **OpenSpec** — 58.8K stars; brownfield change management: "change folders" (proposal, spec delta,
  design, tasks) against a spec baseline. Scored highest in an independent February 2026 four-tool
  evaluation for teams valuing an audit trail.
- **Taskmaster AI** — ~21–27K stars; one layer only: PRD → dependency-aware task graph, mostly for
  Cursor.
- **Agent OS (Builder Methods)** — 5K stars; extracts your codebase's existing conventions into
  "standards" injected per-spec. Boutique scale.
- **Tessl** — $125M raised; pivoted January 2026 from "spec as source" to an agent-skill package
  manager — partial overlap now.
- Embedded, non-portable spec modes: Cursor plan/agents mode, Claude Code spec tasks, Windsurf (now
  Devin Desktop) — product features, not portable methodologies.

Ideas from neighbours worth studying at the implementation level (queued as its own piece of work):
Spec Kit's constitution gate and cross-artifact consistency checks; OpenSpec's change-folder audit
trail; GSD's clean-context sub-agent split; BMAD's story-file embedding (already absorbed into
live-spec's worker briefs).

## Sources

BMAD: [repo](https://github.com/bmad-code-org/BMAD-METHOD) · [critical analysis](https://adsantos.medium.com/you-should-bmad-part-2-a007d28a084b) · issues #1188, #1235, #1332.
Kiro: [specs docs](https://kiro.dev/docs/specs/) · [The Register on pricing](https://www.theregister.com/software/2025/08/18/aws-pricing-for-kiro-dev-tool-a-wallet-wrecking-tragedy/) · [InfoWorld on the billing bug](https://www.infoworld.com/article/4042912/aws-blames-bug-for-kiro-pricing-glitch-that-drained-developer-limits.html).
live-spec: the repo itself, read and executed by both analysts (README, OVERVIEW, SPEC, ARCHITECTURE,
TEST_MATRIX, skills/, guardrails/ — suite and guardrail scripts actually run).
Landscape: [Spec Kit](https://github.com/github/spec-kit) · [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ·
[Open GSD](https://opengsd.net/) · [OpenSpec](https://github.com/Fission-AI/OpenSpec) ·
[Taskmaster](https://github.com/eyaltoledano/claude-task-master) · [Agent OS](https://github.com/buildermethods/agent-os) ·
[Tessl](https://tessl.io/).
