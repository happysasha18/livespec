# Two more frameworks, read for spec coverage: Superpowers and gstack

*2026-07-10. Since the 2026-07-06 comparison against BMAD-METHOD and Kiro, two frameworks rose fast
in the same Claude Code ecosystem: obra/superpowers and garrytan/gstack, grouped with each other and
with GSD in third-party write-ups as the leading orchestration frameworks of the moment. This note
asks one question of each: does it cover the ground live-spec claims — a persistent living spec,
invariants, a formal spec review step, spec-to-test-to-code traceability — or solve an adjacent
problem.*

## Superpowers (obra/superpowers)

### What it is

A cross-agent skills framework by Jesse Vincent ("obra"): Markdown skill files with YAML frontmatter,
packaged as a plugin per host (Claude Code, Cursor, Codex CLI, Copilot CLI, OpenCode, and others;
Gemini CLI support was dropped in v6.1.0), installed via the official Claude Code plugin marketplace.
Fourteen skills cover brainstorming, plan-writing, plan-execution, subagent-driven development,
parallel-agent dispatch, code review (giving and receiving), git-worktree use, branch-finishing, TDD,
systematic debugging, verification-before-completion, and writing new skills. The official Anthropic
plugin listing states over 913,000 installs, from a single, uncorroborated source.
([repo](https://github.com/obra/superpowers))

### Method

A mandatory, sequential seven-phase workflow — brainstorm, isolate in a git worktree, write a plan,
implement via subagents, apply TDD, review, finish the branch. Brainstorming runs a nine-step gated
conversation; no code gets written until the user approves a presented design. Plan-writing breaks
work into two-to-five-minute tasks with exact file paths, code samples, test commands, and a per-task
commit instruction, and its header copies the design doc's "global constraints" into itself. TDD is
enforced as an unconditional rule: no production code before a failing test, and code written out of
order gets deleted and redone. Systematic debugging runs a four-phase root-cause investigation before
any fix. Subagent-driven development hands a fresh subagent only the plan and the tests, not the
reasoning behind them; a single reviewer skill (two roles merged into one in v6.0.0) grades the result
on spec compliance and code quality, with progress state kept in a git-ignored `.superpowers/sdd/`
directory ("SDD" here means Subagent-Driven Development, not spec-driven — a naming collision worth
flagging). Verification-before-completion blocks any "done" claim not backed by fresh evidence run in
that session. The bootstrap footprint is deliberately small: Simon Willison measured the core
skill-loading cost at under 2,000 tokens. ([Willison's write-up](https://simonwillison.net/2025/Oct/10/superpowers/), 2025-10-10)

### How it handles specs

Brainstorming produces one dated design document per feature, at
`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`, with a built-in self-review checklist; once
the user approves it, it is committed to git. The plan-writing skill copies the design's constraints
verbatim and cross-checks that every plan task maps back to a spec requirement. That is the extent of
it — nothing in the sources describes a design document being revisited or amended after its approval
gate, so it reads as a per-feature artifact, not a project-lifetime one. An independent comparison
against GitHub's Spec Kit names the difference plainly: Spec Kit is artifact-centric, with the spec as
a persisting contract that evolves over the project's life, while Superpowers is process-centric,
where the procedure persists and the design document is a one-time output of it — no constitution or
governance layer, and no requirement-to-code audit trail after the fact.
([dev.to/truongpx396](https://dev.to/truongpx396), Spec Kit vs. Superpowers)

Not found anywhere in the sources: invariants as a concept, a formal prover-style review of a spec, a
single spec that persists and gets updated across a project's life, or spec-to-test-to-code
traceability beyond the plan copying the design's constraints into its own header.

### Traction

Created 2025-10-09. As of the GitHub API in 2026-07: 251,354 stars, 22,435 forks, 309 open issues,
ranked #14 on star-history's global chart. Latest release v6.1.1 (2026-07-02), active cadence.
Covered by Simon Willison and by [Marc Nuri](https://blog.marcnuri.com/superpowers-claude-code-skills-framework),
and discussed in three Hacker News threads: [Oct 2025](https://news.ycombinator.com/item?id=45547344),
["A Rave Review of Superpowers"](https://news.ycombinator.com/item?id=47623101), and
["Superpowers 6"](https://news.ycombinator.com/item?id=48739459).

### Strengths and criticisms

Strengths cited across sources: the token-light bootstrap; a pattern where users who turn it off tend
to come back to it; it addresses a real failure mode of unguided agents skipping tests and burying
problems rather than surfacing them. Criticisms cited across sources: no empirical validation exists
(no A/B test, no benchmark), so effectiveness rests on user reports, and some commenters dismiss the
approach as unproven ritual; others report cognitive overhead and fatigue from the mandatory ceremony;
context bloat in heavy frameworks generally is a live 2026 criticism, and the test-first requirement
adds real token and time cost; the interactive brainstorming step can block the input stream when
combined with other frameworks; and the changelog records rough edges — SDD scratch files leaking
into `.git/` (fixed v6.0.3) and a broken evals submodule that took down installs (removed v6.0.2).

### Unverified

The 913,000-install figure rests on one source; exact star-growth checkpoints were not independently
confirmed; and whether any user has amended an approved design document is unknown — no source
describes it happening, but absence of a report is not proof it never occurs.

## gstack (garrytan/gstack)

### What it is

An MIT-licensed collection of role-based Claude Code skills built by Garry Tan (YC's CEO), giving
personas for CEO, staff engineer, designer, QA lead, security officer, and release engineer — about
23 primary skills and 35-plus total slash commands. Installed by cloning into
`~/.claude/skills/gstack` and running its setup script (requires Claude Code, Git, Bun); a templated
`SKILL.md.tmpl` supports other hosts. Created 2026-03-11, with a push as recent as 2026-07-10.
([repo](https://github.com/garrytan/gstack);
[Pulumi's framework roundup](https://pulumi.com/blog/claude-code-orchestration-frameworks/))

### Method

A sprint sequence — think, plan, build, review, test, ship, reflect — with role isolation and a
quality gate at each handoff. Entry point `/office-hours` interrogates product strategy through six
forcing questions; `/autoplan` chains CEO, design, engineering, and developer-experience reviews
before any code is written. `/review` runs a staff-engineer-style PR review. `/qa` drives a real
Playwright/Chromium browser, clicks through the actual flows, fixes what it finds, and generates
regression tests from the bugs it caught. `/codex` dispatches OpenAI's Codex as an independent second
reviewer, a genuine second model in the loop rather than one model reviewing itself. Shipping is
handled by `/ship` (tests, review, and PR together), `/land-and-deploy` (merge, CI, production health
check), and `/canary`. Opt-in advisory guardrails (`/careful`, `/freeze`, `/guard`) and a cross-session
memory index ("gbrain") round out the toolset. The design is framed around Andrej Karpathy's four
named failure modes of AI-assisted coding.

### How it handles specs

`/spec` turns a loose request into what its own documentation calls a precise, executable
specification, in five phases, triggered by phrases like "spec this out" or "file an issue." The
deliverable, however, is a GitHub issue, not a document that lives and gets versioned inside the
repository. The five phases: establish the why with five questions and a check against already-open
issues; scope the boundaries (what's out, the MVP cut, failure/rollback modes); interrogate the actual
codebase (the skill must grep and read real files, citing path:line evidence, before it may keep
asking questions); draft the spec together with the user; and file it via `gh issue create`, with a
local archive recording the issue number and a worktree path. An optional `--execute` flag spawns a
fresh implementer in its own worktree, pinned to a specific commit. A quality gate at phase 4.5, on by
default, has Codex score the draft 0–10 on how executable it would be for an unfamiliar implementer; a
score under 7 triggers a revision loop, capped at three iterations, after which the spec ships
regardless. A fail-closed scan for secrets and PII runs before anything is dispatched externally.

Traceability runs one direction and only conditionally: `/ship` appends "Closes #N" to a PR, but only
when that PR delivers the full spec, with no ongoing check for spec-to-code drift after the merge
lands. By default the filed spec is archived locally, not committed into the repository; syncing it
into the repo is opt-in (`--sync-archive`). The spec text includes a testing-pyramid table and
requires testable acceptance criteria, but nothing derives a test matrix from it, and there is no
red-test-first discipline built into `/spec` itself — that is credited to Superpowers in the
comparison pieces. Not found in any source: invariants, a prover-style review role for the spec
itself, spec versioning, or a document meant to live and change across the project's lifetime. One
third-party review states this outright — gstack lacks native specification-anchoring — and recommends
pairing it with GSD's own artifacts (PROJECT.md, DECISIONS.md, KNOWLEDGE.md) against context rot.
Pulumi's own comparison layers the three tools: gstack owns decisions/roles, GSD owns context/spec,
Superpowers owns execution — each solving a different part of the problem, none of them alone.

### Traction

Per the GitHub API on 2026-07-10: 120,909 stars, 18,062 forks, 806 open issues. Launched 2026-03-12
via a viral X and Product Hunt post; covered by TechCrunch on 2026-03-17, whose framing was that the
reaction split sharply between enthusiasm and pushback. A month-long critical review is at
[claude-codex.fr](https://claude-codex.fr/en/content/garry-tan-stack-claude-code/).

### Strengths and criticisms

Strengths cited across sources: role-based review genuinely produces different answers than a single
pass and surfaces edge cases a generalist prompt misses; `/qa`'s real-browser, screenshot-backed,
atomic-commit-fixing, regression-test-generating behavior is repeatedly singled out as the standout
feature; the Claude-plus-Codex multi-model review is a real second opinion, not a second prompt to the
same model; and the MIT license plus fork-and-trim design lowers the cost of adopting only part of it.
Criticisms cited across sources: some reviewers, including one named critic (Mo Bitar) and TechCrunch
itself, characterize it as a set of prompts in a text file with limited underlying novelty; its
visibility is tied to Tan's public position, independent of the tooling's merits; 35 commands create
real onboarding friction, and the vocabulary reads as specific to a certain startup culture; it
assumes full adoption of its own stack (gbrain, its own browser tooling), leaving dead weight for
partial adopters; a single execution-layer invocation can cost over 10,000 tokens; its TDD discipline
is rated weaker than Superpowers'; and specific productivity claims attributed to the project — output
on the order of twenty engineers from a small team, and a large multiple on logical lines of code per
day — were disputed publicly enough that the maintainers published a dedicated response document,
`docs/ON_THE_LOC_CONTROVERSY.md`. A separate controversy involved a viral tweet about an XSS
vulnerability discovered through the tooling.

### Unverified

Actual production adoption beyond the star count; contributor and commit counts; the Codex quality
gate's real-world pass rate; and what fraction of users invoke `/spec` at all, since it is opt-in.

## Reading against live-spec

Neither framework contradicts live-spec's central claims; neither makes the same claims either, so
this is a gap in coverage, not a clash. A persistent, project-lifetime living spec that gets amended
over time: not found in Superpowers (per-feature design docs, approved once, not revisited) or in
gstack (a filed GitHub issue, archived locally by default, not synced into the repo unless asked).
Invariants as a first-class concept: absent from both. A formal, prover-style review of the spec
itself, independent of the model that wrote it: absent from both — gstack's Codex gate reviews
executability for an implementer, a different question from whether the spec's claims are internally
consistent or complete. Spec-to-test-to-code traceability that holds after the fact: absent from
both — Superpowers' plans copy constraints into their header at write time but track nothing
afterward, and gstack's "Closes #N" link is one-directional and conditional. Two things are real and
worth learning from regardless: Superpowers' execution discipline (the iron-laws TDD rule, the
four-phase root-cause debugging, the verification-before-completion gate) is a genuinely different
concern from spec quality and could be checked against live-spec's own pipeline step for step;
gstack's `/qa` skill, driving a real browser through real flows and generating regression tests from
what it finds, plus its Codex second-opinion review, name a gap worth stating plainly — live-spec's
own judgment loop is still one model reviewing its own work, unlike gstack's.

## Sources

Superpowers: [repo](https://github.com/obra/superpowers) · [Simon Willison](https://simonwillison.net/2025/Oct/10/superpowers/) ·
[Marc Nuri](https://blog.marcnuri.com/superpowers-claude-code-skills-framework) ·
[dev.to/truongpx396](https://dev.to/truongpx396) (Spec Kit vs. Superpowers) · HN
[45547344](https://news.ycombinator.com/item?id=45547344), [47623101](https://news.ycombinator.com/item?id=47623101),
[48739459](https://news.ycombinator.com/item?id=48739459).

gstack: [repo](https://github.com/garrytan/gstack) ·
[Pulumi framework roundup](https://pulumi.com/blog/claude-code-orchestration-frameworks/) ·
[claude-codex.fr critical review](https://claude-codex.fr/en/content/garry-tan-stack-claude-code/) ·
a dev.to/imaginex comparison and a medium.com/@tentenco comparison (full URLs not captured).
