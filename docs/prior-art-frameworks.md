done / PART 1: 6 frameworks compared / PART 2: skill-creator location + install

Sources verified: github.com/bmad-code-org/BMAD-METHOD, kiro.dev, github.com/github/spec-kit,
github.com/Fission-AI/OpenSpec, github.com/buildermethods/agent-os,
github.com/eyaltoledano/claude-task-master, ruvnet/claude-flow (now Ruflo),
github.com/anthropics/skills, code.claude.com/docs/en/skills

---

# PART 1 — Prior art for a spec-driven continuous agentic SDLC

## Design being compared against

Our target pipeline:
1. Continuous casual wish intake anytime
2. Per-wish spec-delta validation (few clarifying questions, batched)
3. Persistent roadmap / ordered queue
4. Async execution by tiered models (cheap for bulk, expensive for judgment)
5. Mechanical pre-push guardrails: completeness check, test-per-change, behaviour-traces-to-spec,
   declared-scope diff against previous run's artifacts
6. Milestones with full re-validation + doc compaction/pruning

---

## 1. BMAD Method
**Repo:** github.com/bmad-code-org/BMAD-METHOD (MIT, active as of 2026)
**What it is:** Simulates a full agile team of AI personas — PM, Architect, Developer, UX, QA, etc.
("Party Mode" puts them all in one session). Structured workflows span ideation → PRD → architecture →
implementation. Documentation is the sole source of truth; code is downstream of docs. 34+ workflows,
expandable module ecosystem.

**Overlaps with our design:**
- Spec/doc as primary artifact (overlaps goals 1-3)
- Phased structured workflows with persona-gating (partial overlap with step 2)
- SPARC sub-methodology (Spec → Pseudocode → Architecture → Refinement → Completion) maps roughly
  to our spec-delta → roadmap → code order

**Lacks from our list:**
- No continuous wish intake — you start a project session, not a persistent feed
- No automated per-wish spec-delta validation or batching of questions
- No persistent cross-session roadmap/queue (session-scoped)
- No model tiering — uses whatever model you hand it
- No artifact snapshot diff vs previous run
- No process-self-validation (no formal invariant checking)
- No doc compaction/pruning at milestones

**Verdict:** Closest thing to a structured agentic SDLC today, but session-scoped and human-orchestrated.
The "agile simulation" is a metaphor, not a mechanical pipeline.

---

## 2. AWS Kiro
**URL:** kiro.dev (launched July 2025, succeeded Amazon Q Developer for new users May 2026)
**What it is:** Full agentic IDE (also CLI + web) built on Amazon Bedrock. Core innovation: requires three
sequential spec documents before any code — requirements.md, design.md, tasks.md. Agent hooks fire
on file-save events. Supports both spec-driven and vibe-coding modes. Routes between Claude Sonnet
(reasoning) and Amazon Nova (high-throughput generation).

**Overlaps with our design:**
- Strongest overlap on goal 5 (pre-code spec gate): the three-doc stack is a hard requirement
- Agent hooks = event-driven quality checkpoints (partial overlap with guardrails)
- Spec-code sync: can update specs from code or tasks from specs (bidirectional)
- Model tiering is baked in (Sonnet vs Nova routing)

**Lacks from our list:**
- No continuous wish intake — each project is a bounded session
- No per-wish batched question/clarification flow
- No persistent cross-session roadmap queue
- No artifact snapshot diff against previous run's rendered output
- No process-self-validation (spec is not formally proved)
- No doc compaction/pruning milestone mechanism

**Verdict:** The closest to our guardrail concept (spec required before code), and the only framework with
real model tiering. But still session-bounded; no continuous intake, no diff against prior artifacts,
no formal spec validation.

---

## 3. GitHub Spec-Kit
**Repo:** github.com/github/spec-kit (open source, works with Copilot, Claude Code, Gemini CLI, 30+ agents)
**What it is:** A toolkit and methodology for spec-driven development, packaged as Claude Code skills
(slash commands). Workflow: /speckit.specify → /speckit.plan → /speckit.tasks → /speckit.implement.
CLAUDE.md encodes vocabulary and definition-of-done for each session. Works across any AI coding agent.

**Overlaps with our design:**
- Spec-first ordering (goals 1-2 partially)
- Structured phases that keep tasks traceable to spec sentences
- Works with Claude Code's native skill system

**Lacks from our list:**
- No continuous wish intake — per-project, per-session invocation
- No automated spec-delta validation or batching of clarifying questions
- No persistent cross-session roadmap or queue
- No model tiering
- No artifact diff vs previous run
- No process-self-validation
- No doc compaction at milestones
- No async background execution

**Verdict:** Good UX layer for "spec before you code," but a workflow guide rather than an orchestration
system. Everything is human-invoked.

---

## 4. OpenSpec
**Repo:** github.com/Fission-AI/OpenSpec (openspec.dev, Node.js 20.19.0+, 25+ AI tool integrations)
**What it is:** Lightweight CLI framework that manages features as "changes" through a lifecycle:
Proposal → Specification → Design → Tasks. Every change lives in an openspec/ directory. Commands:
/opsx:propose, /opsx:explore, /opsx:apply, /opsx:archive. Supports "Stores" (beta) for cross-repo
feature planning.

**Overlaps with our design:**
- Per-feature lifecycle with distinct phases (partial overlap with per-wish spec-delta, goal 2)
- Archive completed work (weak form of doc compaction)
- Organized change directory acts as a primitive queue (goal 3 partial)

**Lacks from our list:**
- No continuous wish intake — changes are manually created
- No automated spec validation or batching of clarifying questions
- No persistent prioritized roadmap with ordering logic
- No model tiering
- No artifact snapshot diff vs previous run
- No process-self-validation
- No milestone-triggered full re-validation

**Verdict:** Lightest-weight of the lot. Good for per-feature traceability, but entirely manual.
The "archive" is the closest thing to pruning; no automation around it.

---

## 5. Agent OS (Builder Methods / Brian Casel)
**Repo:** github.com/buildermethods/agent-os (v2, free open source, tool-agnostic)
**What it is:** A system for injecting codebase standards into AI agents. Extracts patterns from
existing code into documented standards, then injects relevant standards based on what's being built.
Modular architecture, multi-agent orchestration, works with Claude Code, Cursor, and others.
The core pitch: institutionalize team conventions so AI agents follow them consistently.

**Overlaps with our design:**
- Standards injection is a weak form of behaviour-traces-to-spec (goal 5 partial)
- Multi-agent orchestration (v2) overlaps with tiered execution conceptually

**Lacks from our list:**
- No continuous wish intake
- No spec-delta validation or batching
- No persistent roadmap/queue
- No model tiering
- No artifact snapshot diff
- No process-self-validation (the "standards" are conventions, not formal invariants)
- No doc compaction at milestones
- No test-per-change enforcement

**Verdict:** A codebase-context injection tool, not an SDLC orchestrator. Useful as a component
(could supply the "declared scope" context to our guardrail), but far from our design.

---

## 6. Claude-Flow / Ruflo (ruvnet)
**Repo:** ruvnet/claude-flow (mid-2025, renamed Ruflo in early 2026, rewritten in Rust/WASM)
**What it is:** Multi-agent swarm orchestrator for Claude. Key sub-methodology: SPARC
(Specification → Pseudocode → Architecture → Refinement → Completion) as a structured TDD approach
baked into the orchestrator. Coordinates parallel sub-agents on a shared filesystem.

**Overlaps with our design:**
- SPARC provides spec-first ordering before code (goals 1-2 partially)
- Parallel sub-agent execution = closest thing to async tiered execution (goal 4)
- Shared filesystem coordination

**Lacks from our list:**
- No continuous wish intake or persistent queue
- No per-wish batched clarifying questions
- No model tiering by task type (all agents same model tier)
- No artifact snapshot diff vs previous run
- No process-self-validation
- No doc compaction milestones
- No test-per-change enforcement gate

**Verdict:** Most technically ambitious orchestrator in the list. The Ruflo/WASM rewrite signals
production intent. Closest to our tiered async execution model, but lacks the spec-validation
loop, artifact diff, and the continuous intake feed.

---

## 7. Taskmaster AI (eyaltoledano/claude-task-master)
**Repo:** github.com/eyaltoledano/claude-task-master (active, MCP-based, works with Cursor / Lovable / Windsurf)
**What it is:** AI-powered task management system. Parses PRDs into dependency-ordered task graphs,
tracks progress, supports multi-model AI (Claude, OpenAI, Gemini, Perplexity, etc.), and exposes
everything via MCP so any editor can embed it. BMAD + Taskmaster is a common pairing.

**Overlaps with our design:**
- PRD → task graph is the closest existing thing to our wish → roadmap flow (goals 2-3)
- Multi-model support = weak form of model tiering (goal 4)
- Dependency ordering in the task queue

**Lacks from our list:**
- No continuous wish intake — PRD is a one-shot input, not a streaming feed
- No per-wish spec-delta validation or batching of questions
- No artifact snapshot diff vs previous run
- No process-self-validation
- No test-per-change gate
- No doc compaction at milestones

**Verdict:** Best pure task-queue manager in the field. If our design needs a persistent queue
component, Taskmaster or its conventions (PRD → task graph) are the closest prior art.
Still batch-oriented, not continuous-intake.

---

## 8. Notable gap: "continuous incremental spec validation" / artifact diff guardrails

No existing framework does this. The closest academic/research approach is the Spec Kit Agents
paper (arxiv.org/pdf/2604.05278), which describes a multi-agent SDD pipeline with context-grounding
via pre-phase discovery and post-phase validation hooks over SPEC/PLAN/TASKS artifacts. This is
the only published work with explicit "post-phase validation" hooks, but it doesn't diff against
a previous run's rendered artifacts — it validates within a single run.

"Artifact snapshot diff against previous run" (our mechanical guardrail #5) has no prior art in
any of the surveyed frameworks. It is a genuinely novel requirement.

---

## Verdict table

| Feature                                      | BMAD | Kiro    | Spec-Kit | OpenSpec | Agent OS | Claude-Flow | Taskmaster |
|----------------------------------------------|------|---------|----------|----------|----------|-------------|------------|
| Spec-first ordering (before code)            | YES  | YES     | YES      | YES      | partial  | YES (SPARC) | partial    |
| Continuous casual wish intake                | NO   | NO      | NO       | NO       | NO       | NO          | NO         |
| Per-wish spec-delta + batched clarifications | NO   | NO      | NO       | NO       | NO       | NO          | NO         |
| Persistent cross-session roadmap/queue       | NO   | NO      | NO       | partial  | NO       | NO          | YES        |
| Async tiered-model execution                 | NO   | YES     | NO       | NO       | NO       | partial     | partial    |
| Behaviour traces to spec (pre-push)          | NO   | partial | NO       | NO       | partial  | NO          | NO         |
| Test-per-change gate                         | NO   | NO      | NO       | NO       | NO       | partial     | NO         |
| Artifact snapshot diff vs previous run       | NO   | NO      | NO       | NO       | NO       | NO          | NO         |
| Process-self-validated (formal invariants)   | NO   | NO      | NO       | NO       | NO       | NO          | NO         |
| Doc compaction/pruning at milestones         | NO   | NO      | NO       | partial  | NO       | NO          | NO         |
| Full re-validation at milestones             | NO   | NO      | NO       | NO       | NO       | NO          | NO         |

Legend: YES = documented and shipped / partial = conceptually overlaps or partially implemented / NO = absent

**Summary reading:** Every framework covers spec-before-code in some form. None covers continuous
intake, artifact diff vs prior run, or process-self-validation. Kiro is the only one with real model
tiering. Taskmaster is the only one with a genuine cross-session persistent queue. Our design
combines features that do not co-exist in any single tool today — particularly the continuous intake
feed + per-wish batched clarification loop + artifact snapshot diff — and adds novel elements
(process-self-proven, compaction milestones) that have no direct prior art.

---

# PART 2 — Anthropic's official skill-creator skill

## Location

**Repo:** github.com/anthropics/skills (public, Apache 2.0)
**Exact path:** skills/skill-creator/
**SKILL.md:** github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
**Directory listing:** agents/, assets/, eval-viewer/, references/, scripts/, LICENSE.txt, SKILL.md

## What it does

skill-creator is a Claude Code skill for creating, improving, and evaluating other skills.
Workflow it automates:
1. Draft a new skill or modify an existing one with Claude
2. Run test prompts — it spawns parallel runs with and without the skill
3. Benchmark: grades outputs against assertions, generates timing/token metrics, produces an HTML
   report via the eval-viewer
4. Iterate: splits eval set 60/40 (train/held-out), evaluates the current description, proposes
   improvements on failures, iterates up to 5 times, selects best_description by test score
5. Package: `python -m scripts.package_skill <path/to/skill-folder>` generates a .skill file

Invoked by conversation with Claude (no slash commands listed in SKILL.md). It guides you through
the process interactively.

## How to install it into ~/.claude/skills/

The official filesystem install method (from code.claude.com/docs/en/skills, verified):

```bash
# Option A: manual clone + copy
git clone https://github.com/anthropics/skills.git /tmp/anthropics-skills
cp -r /tmp/anthropics-skills/skills/skill-creator ~/.claude/skills/skill-creator
```

```bash
# Option B: sparse checkout (pulls only the skill-creator subfolder)
mkdir -p ~/.claude/skills/skill-creator
cd /tmp && git clone --filter=blob:none --sparse https://github.com/anthropics/skills.git
cd anthropics-skills && git sparse-checkout set skills/skill-creator
cp -r skills/skill-creator/* ~/.claude/skills/skill-creator/
```

After copying, Claude Code detects the change live (no restart needed if ~/.claude/skills/ already
existed). Confirm with /skills in a Claude Code session.

The official plugin install route (if preferred over filesystem):
```
/plugin install anthropic-agent-skills
```
Then browse to select skill-creator from the marketplace. This is Claude Code's managed path but
requires the plugin marketplace — filesystem copy is simpler for a single skill.

Note from docs: "Copy to a writeable location before editing. The installed skill path may be
read-only." — relevant if installed via plugin, not manual copy.

## Maintenance / currency

- Repo has 158k stars, 281 issues, 722 pull requests as of research date (July 2026)
- Anthropic added workspace-wide skill deployment (December 18, 2025) and Claude.ai upload support
  (January 2026), indicating active development on the platform around this skill system
- The skill-creator itself (last commit date not directly verified, but the repo shows recent activity)
- An improved community fork exists: github.com/observerw/skill-creator-skill
- Smithery.ai also hosts the skill: smithery.ai/skills/lofcz/skill-creator (community distribution)

**Status:** Current and maintained as of July 2026. The official repo is the right source.

---

END OF REPORT
