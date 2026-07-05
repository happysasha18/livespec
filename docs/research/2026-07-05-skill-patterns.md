# What the best shipped skills do — and what live-spec can borrow (2026-07-05)

Survey of skill-authoring practice across the strongest public sources, read at the primary
source (actual SKILL.md files and authoring docs, not blog summaries). Goal: find structure,
triggering, and quality patterns worth borrowing into the live-spec pack (live-spec-base +
spec-author, product-prover, build-pipeline, communicator).

Sources studied:

1. Anthropic official — [anthropics/skills](https://github.com/anthropics/skills) repo,
   [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
   [engineering post on Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills),
   the `skill-creator` and `docx` skills.
2. [obra/superpowers](https://github.com/obra/superpowers) — the most-cited community pack;
   read `writing-skills`, `test-driven-development`, `using-superpowers` SKILL.md files.
3. [trailofbits/skills](https://github.com/trailofbits/skills) — security firm's pack with the
   strictest published authoring guidelines (their AGENTS.md).
4. [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) —
   `react-best-practices`, the most prominent vendor-shipped reference skill.
5. Awesome lists for ecosystem context —
   [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (~20k stars, 1000+ skills),
   [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills),
   [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills).

Where we already do something well, it says so — this is a borrow list, not a rewrite order.

---

## 1. Anthropic official (repo + authoring docs)

The repo ([anthropics/skills](https://github.com/anthropics/skills)) is organized as
`skills/` (examples by category), `spec/` (the Agent Skills specification, also at
[agentskills.io](http://agentskills.io)), and `template/` (a starter skill). The document
skills (docx/pdf/pptx/xlsx) are the production skills behind Claude's file features.

### Structure

- **Progressive disclosure is the core design principle.** Three levels: metadata
  (name + description, always in context) → SKILL.md body (loaded when relevant) →
  bundled files (loaded only as needed). "Like a well-organized manual that starts with a
  table of contents, then specific chapters, and finally a detailed appendix."
- **Hard size guidance: SKILL.md body under 500 lines.** When approaching it, split into
  reference files. Frequently-loaded content should be much smaller.
- **References one level deep only.** Nested reference chains (SKILL.md → advanced.md →
  details.md) cause partial reads (`head -100` previews); every reference file should link
  directly from SKILL.md.
- **Reference files over 100 lines get a table of contents** so a partial read still shows
  the full scope.
- **Three degrees of freedom**, matched to task fragility: text heuristics (high freedom),
  parameterized pseudocode (medium), "run exactly this script, do not modify" (low). The
  narrow-bridge/open-field analogy is a genuinely useful authoring test.
- Directory pattern for bigger skills: `SKILL.md` + `references/` (or FORMS.md-style topical
  files) + `scripts/` (executed, not loaded). Make execution intent explicit: "Run X" vs
  "See X for the algorithm".

### Triggering

- Description must state **both what the skill does and when to use it**, third person only
  (first/second person injected into the system prompt hurts discovery), with concrete key
  terms and user-phrase triggers. Max 1024 chars.
- Name: max 64 chars, lowercase-hyphen; they recommend **gerund form** (`processing-pdfs`)
  or consistent noun phrases; ban vague names (`helper`, `utils`).
- The docs' example descriptions all follow the shape *"Does X, Y, Z. Use when \<contexts>
  or when the user mentions \<terms>."*

### Quality

- **"Build evaluations BEFORE writing extensive documentation."** Evaluation-driven skill
  development: document baseline failures without the skill, write three scenario evals,
  write the minimal skill that fixes them, iterate. Eval format: JSON with `query`, `files`,
  `expected_behavior` list (a rubric, graded by a model or human).
- **Claude-A/Claude-B loop**: one Claude instance helps author the skill, a fresh instance
  tests it; observe where B struggles and bring specifics back to A.
- **Workflow checklists**: for multi-step workflows, give a copyable checkbox checklist the
  agent pastes into its response and ticks off — "prevents Claude from skipping critical
  validation."
- **Feedback-loop pattern**: run validator → fix → repeat, stated explicitly in the skill
  ("Only proceed when validation passes").
- Anti-patterns named: time-sensitive content (use an "old patterns" collapsible instead),
  inconsistent terminology, too many alternative approaches (give one default + escape
  hatch), magic constants in scripts, punting error handling to the model.
- Ends with a **pre-share checklist** (description specific? body <500 lines? references one
  level deep? ≥3 evals? tested on Haiku/Sonnet/Opus?).

### Borrowable for us

The workflow-checklist pattern (build-pipeline stages as a tick-off list), the 500-line/
one-level-deep discipline as an explicit pack rule, the eval-first practice, the "old
patterns" section for deprecated behavior, and the pre-share checklist as a guardrail.

---

## 2. obra/superpowers (community, most-cited pack)

A methodology pack (TDD, systematic debugging, brainstorming, writing/executing plans,
subagent-driven development) plus meta-skills (`writing-skills`, `using-superpowers`).
Philosophy: "Mandatory workflows, not suggestions"; the agent checks for relevant skills
before any task. Ships to Claude Code, Cursor, Codex, Copilot CLI and more via plugin
mechanisms; has a separate eval harness repo (superpowers-evals, "drill" harness).

### The three ideas that make this pack stand out

1. **The Iron Law for skills themselves: "NO SKILL WITHOUT A FAILING TEST FIRST."**
   RED = run the scenario without the skill and document how the agent fails; GREEN = write
   the minimal skill that fixes those specific failures; REFACTOR = find the new
   rationalizations agents invent, add explicit counters, re-test. Applies to *edits* of
   skills, not just new ones. This is our red-first principle applied one level up — to the
   skill text itself.

2. **Description = when to use, NOT what the skill does.** Their sharpest, most contrarian
   rule: summarizing the workflow in the description creates a shortcut — the agent follows
   the one-line summary instead of reading the body. Bad: "Use when executing plans —
   dispatches subagent per task with code review." Good: "Use when executing implementation
   plans with independent tasks." (Anthropic says "what + when"; superpowers says the *what*
   belongs in the body. The synthesis: name the capability in a few words, never the
   process.) Their TDD skill's description is just: *"Use when implementing any feature or
   bugfix, before writing implementation code."*

3. **Bulletproofing discipline skills**: for rule-enforcing skills, close loopholes
   explicitly — state the rule, forbid the specific workarounds, address spirit-vs-letter
   arguments upfront, and include a **rationalization table** built from baseline testing
   plus a red-flags self-check list. Example counter from their TDD skill: "Delete code
   before test? Delete it. Start over. No exceptions — not as reference, not while adapting
   tests, not at all."

### Other patterns

- **Token targets by load frequency**: getting-started flows <150 words, frequently-loaded
  skills <200 words, others <500 words. Far stricter than Anthropic's 500 lines.
- **Cross-reference syntax**: `**REQUIRED BACKGROUND:** superpowers:skill-name` — reference
  by name, never @-links that force-load files. One canonical home per rule, pointers
  elsewhere (same instinct as our live-spec-base).
- **A gateway skill** (`using-superpowers`) that fires at conversation start and teaches the
  invocation discipline: announce "Using [skill] to [purpose]", process skills before
  implementation skills, user instructions > skills > defaults. It also pre-counters
  avoidance thoughts ("this is just a simple question" → check skills anyway).
- Standard SKILL.md skeleton: Overview → When to Use → Core Pattern (before/after) →
  Quick Reference (table) → Implementation → Common Mistakes → (optional) Real-World Impact.
- Flowcharts **only** for non-obvious decisions or A-vs-B forks, never for reference
  material or linear steps. One excellent complete example beats five mediocre ones.
- Skill-behavior tests live in `evals/` and run through a harness; plugin infrastructure has
  its own `tests/`. Deploying untested skills "violates quality standards."

### Borrowable for us

The rationalization table for build-pipeline (a discipline skill under constant "it's a
small edit" pressure), the description-workflow separation, pressure-scenario evals, the
REQUIRED BACKGROUND cross-ref syntax, and the red-flags self-check list.

---

## 3. Trail of Bits skills (the strictest published authoring bar)

Security-audit pack (CodeQL/Semgrep, variant analysis, Rust security review with SARIF
output, ~21 skills) plus a curated marketplace ([trailofbits/skills-curated](https://github.com/trailofbits/skills-curated)).
Their [AGENTS.md](https://github.com/trailofbits/skills/blob/main/AGENTS.md) authoring
guidelines are the most operational in the wild.

- **Mandatory sections in every SKILL.md: `## When to Use` AND `## When NOT to Use`.**
  Negative triggers are a required structural element, not a nicety. Security skills add
  `## Rationalizations to Reject` (same insight as superpowers, converged independently).
- **Loadability CI**: `check_claude_loadability.py` and `check_codex_loadability.py` run
  before any PR — mechanical checks that frontmatter parses, names fit limits, referenced
  files exist, no hardcoded paths. Skills are linted like code.
- Layout: `plugins/<name>/skills/<skill>/SKILL.md` + optional `references/`, `workflows/`,
  `scripts/`. Same one-level-deep rule: "SKILL.md links to files, files don't chain to more
  files."
- Quality bar in the PR checklist: examples show concrete input → output; content explains
  **"WHY, not just WHAT: include trade-offs, decision criteria, judgment calls"**; don't
  duplicate reference material, provide behavioral guidance.
- Governance: plugin README, entry in `marketplace.json`, CODEOWNERS line per plugin,
  **"version numbers incremented and synchronized across files for substantive changes."**
- They even ship a `skill-improver` plugin — a skill for improving their own skills.

### Borrowable for us

"When NOT to Use" as a mandatory section across all five skills; a loadability check in our
guardrails (we already run shell guardrails pre-push — this is a natural sibling); the
version-sync-across-files rule as a checkable invariant.

---

## 4. Vercel react-best-practices (the reference-skill archetype)

[SKILL.md](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md)
with 40–70 rules across 8 categories. This is how a large *reference* skill (as opposed to a
*discipline* skill) is best organized:

- **Priority-ranked categories with stable ID prefixes**: Eliminating Waterfalls (CRITICAL,
  `async-`), Bundle Size (CRITICAL, `bundle-`), Server-Side (HIGH, `server-`) … Advanced
  (LOW, `advanced-`). Every rule has a kebab-case ID (`async-parallel`), a rationale, and an
  incorrect/correct code pair.
- **One file per rule** under `rules/`, referenced from the SKILL.md index — progressive
  disclosure at rule granularity.
- **A compiled `AGENTS.md`** — the whole guide flattened into one file for agents that don't
  do file navigation. One source, two renderings.
- Frontmatter carries provenance: `license: MIT`, `metadata: {author: vercel,
  version: "1.0.0"}`.
- Description names the exact triggering activities: "…when writing, reviewing, or
  refactoring React/Next.js code… Triggers on tasks involving React components, Next.js
  pages, data fetching, bundle optimization, or performance improvements."

### Borrowable for us

Stable rule IDs with priority tiers is literally our trailing-anchors pattern — good
convergence, nothing to change. The genuinely new bit is the **compiled single-file
rendering** (skills → one AGENTS.md) for hosts that can't navigate a pack, and `license` +
`author` in frontmatter for a public pack.

---

## 5. Ecosystem context (awesome lists)

[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (~20k
stars) curates 1000+ skills with the filter "hand-picked, not AI-slop generated"; official
packs now come from Anthropic (17), Microsoft (133), Sentry (28), OpenAI (44), Hugging Face,
Cloudflare, Netlify, Stripe, Figma. Two signals matter for us:

- **Cross-agent portability is becoming table stakes** — the strong packs install into
  Claude Code, Codex, Cursor, Copilot CLI, OpenCode. The Agent Skills spec
  ([agentskills.io](http://agentskills.io)) is the common denominator. Our install.sh +
  plain SKILL.md folders are already spec-shaped; worth keeping it that way deliberately.
- **Curation is the differentiator** in a 1000-skill world — which means triggering
  precision (descriptions) and a visible quality bar (tests, versioning) are what make a
  pack citable. Our prover-over-the-pack story fits this current well.

---

## Where the live-spec pack already meets or beats this bar

Honest ledger before the borrow list:

- **One normative home per rule** (live-spec-base as the rulebook; working skills reference
  and elaborate) — superpowers and Trail of Bits both gesture at this; none states it as
  cleanly as our "one home per fact." Keep.
- **Version pins** — every skill carries `metadata.version`, pack-level VERSION file.
  Vercel-grade already; only the "sync on substantive change" check is missing.
- **Red-first tests over shipped text** — `tests/test_guardrails.py`,
  `tests/test_traceability.py` plus pre-push guardrails. Most packs test nothing; only
  superpowers and Trail of Bits test at all. What we lack is the *other* kind of test —
  behavioral evals of the skills themselves (does the skill fire when it should, does the
  agent obey it under pressure).
- **Size discipline** — all five SKILL.md files are 135–365 lines, under everyone's limits.
  product-prover (365) is the only one worth watching.
- **Trigger-rich descriptions** — ours already include quoted user phrases ("spec this
  out", "poke holes in this") and third person. build-pipeline is the only one with a
  negative trigger ("NOT for tiny reversible edits… or pure research"); the other four have
  none.
- **Rule IDs / anchors** — our trailing anchors and Formal index are the same move as
  Vercel's rule IDs. Converged; keep.

---

## Top 10 candidates for the live-spec pack (ranked)

1. **Add a "When NOT to Use" clause to every skill's description and body** — build-pipeline
   has one, the other four don't; in a many-skill session negative triggers are what stop
   wrong fires. *(Trail of Bits mandatory section; superpowers; Anthropic checklist.)*

2. **Skill-behavior evals: baseline-vs-with-skill scenarios, red first** — run the scenario
   without the skill, record the failure, keep it as the skill's test; our red-first
   principle applied to the skill text itself, which today only our guardrail texts get.
   *(Superpowers Iron Law "NO SKILL WITHOUT A FAILING TEST FIRST"; Anthropic
   "build evaluations before writing extensive documentation" + evals.json format.)*

3. **A rationalization table in build-pipeline** — list the exact excuses an agent uses to
   skip the pipeline ("it's a one-line change", "I'll spec after", "user is in a hurry") with
   explicit counters, built from observed failures. *(Superpowers bulletproofing;
   Trail of Bits "Rationalizations to Reject".)*

4. **Copyable progress checklist for the pipeline stages** — build-pipeline gives the agent
   a checkbox list (spec → prove → architecture → … → commit) to paste and tick off, so
   stages can't be silently skipped. *(Anthropic workflow-checklist pattern.)*

5. **Strip workflow summaries from descriptions; keep only capability + triggers** —
   build-pipeline's description currently narrates the whole stage sequence, which invites
   following the summary instead of reading the skill; move process into the body.
   *(Superpowers "description = when to use, NOT what the skill does".)*

6. **Formal cross-reference syntax between pack skills** — adopt one convention like
   `REQUIRED BACKGROUND: live-spec:live-spec-base` (reference by name, never force-load),
   stated once in live-spec-base; today our cross-references are prose. *(Superpowers.)*

7. **Loadability check in guardrails** — a small script asserting every SKILL.md: frontmatter
   parses, name ≤64 chars kebab-case, description ≤1024 chars and third person, every
   referenced file exists, references one level deep, version present. Runs pre-push next to
   the existing guardrails. *(Trail of Bits loadability CI; Anthropic frontmatter limits.)*

8. **Version-sync rule as a checkable invariant** — substantive skill change ⇒ its
   `metadata.version` and the pack VERSION move together; we pin versions but nothing
   enforces the bump. *(Trail of Bits PR checklist.)*

9. **Progressive disclosure inside the bigger skills** — product-prover (365 lines) splits
   its checklist catalogs into one-level-deep reference files with a table of contents,
   keeping the loaded body lean; adopt the 500-line/one-level/TOC trio as a pack rule in
   live-spec-base. *(Anthropic patterns; docx skill; Vercel rules/ layout.)*

10. **`license` and `author` in frontmatter + a compiled single-file rendering** — provenance
    fields for a public pack, and one generated flat file (AGENTS.md-style) so
    non-file-navigating agents can use the pack; one source, two renderings.
    *(Vercel react-best-practices; ecosystem portability trend.)*

Near-misses worth remembering: gerund naming (ours are role nouns — consistent, keep), the
"old patterns" collapsible for deprecated behavior (useful once we deprecate anything), the
Claude-A/Claude-B authoring loop (we effectively do this via prover), and a gateway skill à
la using-superpowers (our CLAUDE.md loader already plays that role).
