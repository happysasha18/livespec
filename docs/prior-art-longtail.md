# Long-tail prior art search — categories (a)–(d)
# Checkpoint: done
# Searched: 2026-07-04

---

## Search scope

GitHub topics (claude-skills, claude-code, ai-sdlc, spec-driven, cursor-rules), code search
for SKILL.md + spec + pipeline; awesome-claude-code repos (hesreallyhim, ComposioHQ, travisvn,
GetBindu, rohitg00, kodustech, VoltAgent, sickn33, alirezarezvani); Smithery.ai skills;
SDLC frameworks (ai-sdlc-framework, GAAI, agentic-os, aidlc-workflows, cc-sdd, speckit-agent-skills,
OpenSpec); community writing (Medium, dev.to, HN); arxiv for formal verification angle.

---

## Category (a): Continuous wish-intake into a spec-validated queue
(casual request → spec-delta check → persistent roadmap)

### What exists

**Backlog-management skills** — structured task queueing exists:

- **github-backlog-management-skill** (gringolito)
  https://github.com/gringolito/github-backlog-management-skill
  Claude Code skill. Adds every new request through an INVEST gate (Independent, Negotiable,
  Valuable, Estimable, Small, Testable) before it lands in the GitHub Issues queue. Items failing
  the gate are labelled needs-clarification and blocked from the backlog.
  _Touches (a): format/structure quality gate on intake. Does NOT check requests against a living
  spec; "spec-delta check" is absent._

- **backlog-agents** (Sintetiko-labs)
  https://github.com/Sintetiko-labs/backlog-agents
  Runs 6 validation checks including backlog coherence and contract verification on new tickets.
  Generates tickets from short descriptions, analyzes codebase for context.
  _Touches (a): closer — "backlog coherence" implies cross-item checking. Still not spec-delta:
  no check against a formal SPEC.md._

- **GAAI-framework** (Fr-e-d)
  https://github.com/Fr-e-d/GAAI-framework
  .gaai/ drop-in governance layer. Discovery agent produces stories with acceptance criteria;
  Delivery never decides scope. Backlog is the "contract between Discovery and Delivery." Daemon
  delivers Stories in parallel tmux sessions.
  _Touches (a): structured intake + acceptance criteria. The Discovery agent does reason about
  what to build and validates "artefact complete, criteria testable, no scope drift." BUT: validation
  is against internally-generated acceptance criteria, not against a separate living SPEC.md that
  the intake validates a delta against._

- **Backlog.md** (MrLesk)
  https://github.com/MrLesk/Backlog.md
  Git-native task management for human+AI collaboration. No spec validation layer.

- **ai-sdlc-framework**
  https://github.com/ai-sdlc-framework/ai-sdlc
  Definition-of-Ready gate that refuses to dispatch undecided tasks. Decision Catalog routes open
  questions to decision-makers. Has a DoR concept (Definition of Ready) that is a strong analogue
  of spec-delta check, but the DoR checks internal task completeness, not consistency with a
  living product SPEC.

### Verdict (a): PARTIAL / NOT FOUND as a packaged skill

The closest thing is the DoR gate in ai-sdlc + the INVEST gate in github-backlog-management-skill.
Neither checks new requests against a separate persistent product spec (no "does this request conflict
with or extend SPEC.md?"). The spec-delta check half of (a) — where the spec is the authority and
intake validates against it — does not exist as a packaged skill anywhere found. Structured intake
queues with format gates: YES, mature. Spec-awareness in that gate: NOT FOUND.

---

## Category (b): Artifact snapshot-diff as AGENT guardrail with DECLARED SCOPE semantics
(undeclared file change = red, pre-push; specifically as freelancing-catcher, not visual regression)

### What exists

- **agent-guardrails** (logi-cmd) — STRONGEST HIT
  https://github.com/logi-cmd/agent-guardrails
  Pre-merge gate (MCP-based, works with Claude Code / Cursor / Codex / Gemini / OpenCode).
  Before the agent runs, you declare a task brief with --intended-files (exact files expected to
  change) and --allow-paths (directories the agent may touch). After the agent runs, you execute
  `agent-guardrails check --review`, which diffs actual git changes against the declared contract.
  Files changed outside the declared scope = scope violation flagged. Severity configurable (error
  blocks merge, warning lets acknowledged violations pass). 46 releases (latest v0.20.0, April 2026),
  216 commits, supports all major agent harnesses via MCP.
  _Directly addresses (b): declared scope + diff-against-declaration + merge gate. The "freelancing
  catcher" framing is explicitly its purpose. HOWEVER: it is a pre-MERGE gate, not a pre-push hook.
  The scope declaration is a task brief, not derived from a SPEC.md. No "DECLARED SCOPE semantics"
  tied to a formal spec document — scope is declared per-task, ad hoc, before each run._

- **wilddog64 pre-commit approach** (DEV Community)
  https://dev.to/wilddog64/i-built-the-guardrails-into-the-repo-not-the-prompt-4n3l
  Pre-commit hook that runs git diff --cached and blocks commits if staged files fall outside
  subtree guards or contain removed test cases. Catches structural violations deterministically
  at commit time, regardless of which agent committed.
  _Touches (b): file-scope enforcement via diff at commit. No spec connection; scope is hard-coded
  subtree rules, not derived from a task scope declaration._

- **git-prism** (mikelane)
  https://dev.to/mikelane/teaching-claude-to-stop-reaching-for-git-diff-git-prism-v070-4nel
  Structured change manifests (file snapshots, function context, commit history) returned as
  token-efficient JSON. Bundled PreToolUse redirect hook that blocks dangerous git commands.
  _Related to (b): provides richer diff artifacts but is a diff-viewing tool, not a scope guardrail._

- **spec-aware-review** (Joshua McDonald workflow)
  Custom skill described at joshmcdonald.medium.com. Reads the active spec and current diff
  side by side, asks whether the code matches what the spec said the code would do. Catches
  spec-drift: implementation deviated from spec intent.
  _Touches (b): spec-vs-diff comparison. But it is a review skill (runs at PR time, manually),
  not an automated pre-push guardrail that fails on undeclared changes. No "scope declaration"
  artifact — it reads a diff and a spec and produces a report._

### Verdict (b): PARTIAL — agent-guardrails is the closest published artifact

agent-guardrails implements the diff-against-declared-scope mechanism and is explicitly a
freelancing-catcher. The gap vs. the full concept: (1) scope is per-task ad hoc, not derived
from a SPEC.md; (2) it is pre-merge not pre-push; (3) "DECLARED SCOPE" in the sense of a
single authoritative document that the agent's changes must respect — that framing does not exist
anywhere found. Note: snapshot/visual-regression testing (Jest, Percy, Chromatic) is mature and
well-known prior art for rendered artifacts; the search confirmed none of that applies here.

---

## Category (c): "Process spec" formally proven by a reviewer skill
(invariants over the dev process itself, not just domain code)

### What exists

- **Lean4Agent** (arxiv 2606.06523, June 2026)
  https://arxiv.org/pdf/2606.06523
  Academic framework using Lean 4 to formally verify agent workflow trajectories and behavioral
  constraints. Proves properties about agent action sequences (trajectory verification, invariants
  that hold throughout execution paths). This IS about the agent's process, not just domain code.
  _Touches (c) most directly of anything found. BUT: it is an academic paper + prototype, not a
  packaged skill or published repo you can attach to a project. Not a "reviewer skill" you invoke._

- **payment-invariants** (xtilyn)
  https://github.com/xtilyn/payment-invariants
  Claude Code skill reviewing payment code against 19 invariants (Safety + Liveness tags). Domain
  code invariants, explicitly NOT process invariants. The skill itself is the reviewer pattern.
  _Shows the reviewer-skill-checking-invariants pattern exists — but for domain code, not for the
  dev process itself._

- **agentic-os** (KbWen)
  https://github.com/KbWen/agentic-os
  Phase-gated workflow (plan → build → review → test → ship) with a validate.sh script that
  parses work logs and fails commits if required phases are skipped or evidence is missing.
  _Closest thing to "proven process spec" at the tool level: it enforces process phase invariants
  (every phase must have evidence). But it is NOT formally proven — validate.sh is bash text
  matching, not a theorem prover. And there is no reviewer SKILL that checks the process spec
  itself for completeness/gaps._

- **ai-sdlc-framework**
  https://github.com/ai-sdlc-framework/ai-sdlc
  Declares Resources: Pipeline, Decision, AgentRole, QualityGate in JSON Schema. Quality gates
  run advisory → soft-mandatory → hard-mandatory. This is the most structurally sophisticated
  process enforcement found. Still not formal verification; it's declarative governance enforced
  by the harness, not a proof.

- **AIP: Graph Representation for Agent Skills** (search result, June 2026)
  Proposal to replace free-form skill prose with directed execution graphs: discrete steps as nodes
  with explicit typed input/output edges and schema-validated YAML spec. Improved Claude Sonnet
  pass rate from 53% to 67%. Not yet a packaged skill — a specification proposal.

### Verdict (c): NOT FOUND as a packaged skill

The concept of a reviewer SKILL that runs formal-verification-style checks (invariants, safety,
liveness) over a PROCESS SPEC (not domain code) does not exist as a published, installable artifact.
Lean4Agent is the closest in ambition (formal + process-level) but is academic prototype. The
payment-invariants pattern (domain-invariant reviewer skill) shows the pattern is viable but has not
been lifted to the process-spec level by anyone. Phase-gate enforcement (agentic-os, ai-sdlc) exists
and is real, but it is deterministic bash/YAML checking, not a reviewer skill reading a process spec
and reasoning about invariant coverage. The specific combination — SPEC.md describing the dev process
+ a reviewer agent that proves it for gaps — is original in the published ecosystem.

---

## Category (d): Full packaged "attach to any project mid-flight" method packs
(adopt/reverse-spec for Claude Code)

### What exists

- **OpenSpec** (Fission-AI) — STRONGEST HIT
  https://github.com/Fission-AI/openspec
  Self-described as "built for brownfield not just greenfield." Has /opsx:onboard command for
  existing projects and an "Existing Projects" guide. Core explore → propose → apply → archive
  workflow. Philosophy: "fluid not rigid / iterative not waterfall."
  _Touches (d): explicit brownfield onboarding command exists. Gap: does not produce a formally
  structured living SPEC with invariants; "fluid not rigid" is the explicit anti-thesis of the
  spec-proven approach. The onboard command's completeness is not fully documented._

- **reverse-engineering-skill** (meirm)
  https://github.com/meirm/reverse-engineering-skill
  Six skills: reverse-engineering, validation, gap analysis, refinement, acceptance criteria,
  test generation. Plus an orchestrator agent. Extracts business logic into 11-section BL docs,
  validates against code, identifies gaps. Explicitly supports "mid-flight adoption by
  reverse-speccing."
  _Touches (d): reverse-spec from existing code is its core purpose. 23 stars, 4 commits —
  nascent. Output is business-logic docs, not a SPEC.md with entities/states/transitions/invariants
  in the formalized sense._

- **speckit — /speckit.specify for reverse-engineering**
  https://github.com/github/spec-kit
  /speckit.specify can be run against existing modules to extract a spec that "preserves what
  the module does while you rebuild how it does it." Not a dedicated reverse-spec pack, but a
  command within the standard SDD workflow.

- **cc-sdd** (gotalab)
  https://github.com/gotalab/cc-sdd
  Has a /kiro-discovery command that routes work into extend-existing, direct-implement, single-spec,
  or multi-spec pathways. Generates brief.md and roadmap.md. Cross-agent (8 harnesses).
  _Touches (d): discovery for existing projects. Not a full adopt/reverse-spec method pack._

- **alirezarezvani/claude-skills** — code-to-prd skill
  https://github.com/alirezarezvani/claude-skills
  /code-to-prd converts existing code artifacts into PRD documents. Direction is code→spec.
  _Touches (d) in one direction. Not a full method pack for adopting an existing project mid-flight
  into a proven-spec workflow._

- **GAAI-framework** (Fr-e-d)
  https://github.com/Fr-e-d/GAAI-framework
  Drop-in .gaai/ folder into any project. The README says it works for existing projects.
  Provides cross-session memory and structured delivery. Not focused on reverse-speccing existing
  behavior.

### Verdict (d): PARTIAL

Scattered partial versions exist: OpenSpec has a brownfield onboard command; reverse-engineering-skill
is the most explicitly purpose-built reverse-spec tool but is nascent; speckit covers reverse-speccing
a module within its workflow; cc-sdd has discovery routing for existing projects. No single packaged
method pack exists that: installs in one step, reads an existing codebase, produces a formally
structured SPEC.md (entities / states / transitions / invariants), attaches a proven dev process
going forward, and is battle-tested. The brownfield gap is real and widely acknowledged in community
discussions — the tooling assumes you are starting fresh or at least starting with a spec.

---

## Honorable mentions (tangential but worth noting)

- **ai-sdlc-framework** — most complete governance framework found; DoR gates, DSSE attestation,
  independent cross-harness review, JSON Schema declared resources. Not a SKILL, not attaching
  mid-flight. https://github.com/ai-sdlc-framework/ai-sdlc

- **agentic-os** (KbWen) — phase-gate enforcement via validate.sh; closest to process-invariant
  checking as a deterministic tool. https://github.com/KbWen/agentic-os

- **freddo1503/claude-pre-commit** — pre-commit hooks specifically for validating Claude Code
  config files (SKILL.md, hooks, settings). Scope-checking at config level.
  https://github.com/freddo1503/claude-pre-commit

- **Lean4Agent** (arxiv June 2026) — formal trajectory verification for agent workflows; academic.
  https://arxiv.org/pdf/2606.06523

---

## Summary verdict table

| Category | Verdict | Strongest counter-example |
|---|---|---|
| (a) wish-intake → spec-delta check → persistent roadmap | NOT FOUND as packaged skill. Structured intake gates exist (INVEST, DoR), but none check against a living SPEC | github-backlog-management-skill (INVEST gate) + ai-sdlc DoR |
| (b) artifact snapshot-diff as agent freelancing-catcher with declared scope | PARTIAL. The mechanism exists (agent-guardrails); gaps: scope is per-task ad hoc, not SPEC-derived; pre-merge not pre-push | logi-cmd/agent-guardrails |
| (c) process spec formally proven by reviewer skill (invariants over the dev process) | NOT FOUND as packaged skill. Domain-invariant reviewer skills exist; process-level formal proof exists only as academic prototype | xtilyn/payment-invariants (pattern) + Lean4Agent (formal, academic) |
| (d) full packaged mid-flight method pack (adopt/reverse-spec) | PARTIAL. Scattered brownfield pieces exist; no single installable pack that produces a proven living SPEC from an existing project | meirm/reverse-engineering-skill + OpenSpec /opsx:onboard |

---

## What this means for originality

The specific combination that is NOT found anywhere:
- A SKILL that takes casual requests and validates them against a living SPEC before queueing (the spec is the authority, not just a format gate)
- A pre-push guardrail where "declared scope" is derived from the active SPEC (not a per-task brief), and any undeclared file change = hard fail
- A reviewer SKILL that treats the DEV PROCESS ITSELF as the spec (entities, states, transitions, invariants of the workflow) and proves it for gaps — not domain code
- A single installable method pack: drop into brownfield, reverse-spec the existing project into a proven SPEC.md, attach the pipeline going forward

Each concept has partial prior art (structured intake, diff-based scope gates, domain invariant reviewers, brownfield discovery). The integration of all four, with the spec as the single source of authority binding them together, is not published.

Private/scattered partial versions: yes, almost certainly exist as personal CLAUDE.md setups and unpublished team workflows (the community writing strongly implies this). Published and installable: not found.

