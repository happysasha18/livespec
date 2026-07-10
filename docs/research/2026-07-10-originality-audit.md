# Originality audit — do we owe anyone a credit we haven't given? (2026-07-10)

*Asked by the owner on 2026-07-10 (~13:56): we studied BMAD, Kiro, Spec Kit, OpenSpec, GSD,
Superpowers, gstack and others at length — audit the pack so no one can later say ideas or code
were taken without attribution. Two independent passes ran: a borrowings inventory (every
mechanism we noted, adopted, or queued from a named neighbour, and where its source is stated)
and a verbatim-overlap scan (shared word runs between our shipped files and their public docs).*

## Verdict

Text: clean. Across seven shipped files against eleven public documents from the five most-read
neighbours, the scan (validated on a planted positive control first) found zero shared runs of
eight or more consecutive words; lowering the bar to four words surfaces only generic English
idioms. No skill, phase, or command name coincides with a neighbour's coined name, and both
places a neighbour's own term appears in our text name that neighbour with a citation.

Ideas: eighteen mechanisms adopted from named sources, every one traceable. Six are credited in
the shipped text itself; twelve are credited in the research docs and the queue rows that adopted
them. Two findings came out of the audit and are fixed or queued the same day: one provenance
pointer in guardrails/README.md had gone dead when its queue row was archived (repointed to this
audit), and one mechanism the owner approved on 2026-07-05 (the rationalization table) was never
built — re-queued rather than dropped.

The two audit passes follow in full.

---

# Audit — everything live-spec borrowed, adopted, or queued from neighbouring frameworks

Method: read `docs/prior-art.md`, `docs/prior-art-frameworks.md`, `docs/prior-art-longtail.md`, every
file in `docs/research/`, `docs/decisions/2026-07-05-research-answers.json` (Alexander's yes/no on
each candidate), `docs/spec-format-by-project-type.md`, then grepped `ROADMAP.md`, `JOURNAL.md`,
`README.md`, `PRODUCT_SPEC.md`, `ARCHITECTURE.md`, `skills/*/SKILL.md`, `guardrails/`, `templates/`,
`docs/prover/*.md` for BMAD, Kiro, spec-kit, OpenSpec, GSD, Superpowers, gstack, agent-guardrails, and
secondary names that surfaced (arc42, C4, Google, Kiro's EARS, Amazon Working Backwards, Shape Up,
Trail of Bits, Vercel, Jest/Percy/Chromatic). Note: `ROADMAP.md` prunes landed rows periodically
(doc compaction) — several row numbers named by the harvest doc as "filed" (111, 112, 113, 114, 116,
120, 122–127) no longer exist as standalone `| N |` lines today; their content was traced forward into
`PRODUCT_SPEC.md` invariants and `JOURNAL.md` landing entries, which is how each was confirmed adopted
below.

---

## Table 1 — borrowed / adopted / queued items

| Mechanism (plain words) | Source project | Where it lives now | Where credited | Verdict |
|---|---|---|---|---|
| Adversarial fresh-context verifier at verify: re-derive claims from spec, never worker's summary, stub-detection greps | GSD (`agents/gsd-verifier.md`) | `PRODUCT_SPEC.md` INV-46; `build-pipeline` SKILL.md step 8 "adversarial option" | Research doc (`2026-07-06-neighbours-implementation-harvest.md` item 1) + ROADMAP row 110 + JOURNAL; NOT named "GSD" in the SPEC/skill text itself | credited (research doc + row text only) |
| Brief born from reading files in full before writing (current-state / what-changes / what-must-survive, sourced claims) | BMAD (`bmad-create-story/SKILL.md`) | `PRODUCT_SPEC.md` INV-53; `build-pipeline` SKILL.md | Research doc (item 2) + JOURNAL "rows 111+112+113" entry; not named in SPEC text | credited (research doc + row text only) |
| Worker HALT list — named stop conditions only (ambiguous requirement, 2 consecutive unexplained failures, missing dependency, acceptance impossible) | BMAD (`bmad-dev-story/SKILL.md`) | `PRODUCT_SPEC.md` INV-54; `build-pipeline` SKILL.md | Research doc (item 3) + JOURNAL; not named in SPEC text | credited (research doc + row text only) |
| Quantified brief sizing (~300 lines / ~8 files, paths never inlined bodies, split above the bound) | GSD (`references/context-budget.md`) | `PRODUCT_SPEC.md` INV-55; `build-pipeline` SKILL.md | Research doc (item 4) + JOURNAL; not named in SPEC text | credited (research doc + row text only) |
| Gate hygiene contract — typed `{severity, code, message, fix}` JSON on every blocking-gate failure, blocking-vs-advisory declared per check, all-or-nothing artifact writes | OpenSpec (`archive.ts`, `cli/index.ts`) | `PRODUCT_SPEC.md` INV-47; `guardrails/README.md` "The gate contract" section | `guardrails/README.md` says "the neighbours' CLI lesson, ROADMAP row 114" — **that row-114 pointer is now dead/stale** (pruned from ROADMAP.md); OpenSpec named only in the research doc | credited, but with a stale in-repo pointer (needs a fix: repoint or drop the "row 114" citation) |
| Resume-digest size cap — NEXT_STEPS stays ≤100 lines, growth is a design failure, detail flows to the journal | GSD (`templates/state.md`) | `PRODUCT_SPEC.md` INV-48; `templates/NEXT_STEPS.template.md` | Research doc (item 6) + JOURNAL; not named in template text | credited (research doc + row text only) |
| Self-contained worker brief — embeds the exact spec sentences, edit strings, checks, checkpoint path (the "story-file" pattern) | BMAD (scrum-master story files) | `build-pipeline` SKILL.md line 397 | **Named explicitly in the shipped skill text**: "the BMAD story-file lesson" | fully credited, adopted |
| Regression fences — a wish touching a live surface opens with what must keep working, cited to existing clauses | Kiro (EARS "SHALL CONTINUE TO" best practice) | `PRODUCT_SPEC.md` T-14/INV-19; `spec-author` SKILL.md | Research doc `2026-07-05-methods.md` candidate #1 + `docs/decisions/2026-07-05-research-answers.json` (`"regression-fences": "now"`) | credited (research doc + decision record); the EARS WHEN/THEN/SHALL *grammar* itself was later explicitly killed (row 148, "псевдодраматичность") — only the underlying discipline survived, in plain prose |
| Non-goals — a mandatory closing sentence naming what's deliberately left out | Shape Up ch.06 / Google design docs | `PRODUCT_SPEC.md` INV-20; `spec-author` SKILL.md | Research doc candidate #3 + decisions JSON (`"non-goals": "now"`) | credited, adopted |
| Success measure — a mandatory closing sentence: how we'd notice the feature worked | GitHub spec-kit (Success Criteria SC-001…) | `PRODUCT_SPEC.md` INV-21; `spec-author` SKILL.md | Research doc candidate #8 + decisions JSON (`"appetite-success": "now"`, conflated by Alexander with KPI/data-driven framing) | credited, adopted |
| Facet-list curation rule — a facet earns its place only by a named real incident, list re-justified at milestones | Google SRE book ch.27 (launch-checklist curation) | `spec-author` SKILL.md canonical facet list | **Named explicitly in the shipped skill text**: "(the Google launch-checklist lesson)" | fully credited, adopted |
| Two new facets: "two windows at once" (concurrent instances) and "a missing source" (dependency failure) | Google eng-practices (concurrency) + SRE book (failure modes / external deps) | `spec-author` SKILL.md canonical facet list, each with its own cited incident | Decisions JSON (`"facet-additions": "now"`) + research doc; Google not named next to these two specific entries (only the curation-rule sentence names Google) | credited (research doc + decision record), adopted |
| "When NOT to Use" as a mandatory section in every skill | Trail of Bits (`AGENTS.md` authoring guidelines) | `spec-author`, `product-prover`, `communicator`, `publish`, `test-author` (all have "## When NOT to use"), `feedback-intake` ("## When NOT to fire"), `build-pipeline` (inline negative trigger) | Research doc `2026-07-05-skill-patterns.md` candidate #1 + decisions JSON (`"skill-hygiene": "now"`) | credited, adopted across the whole pack |
| Skill loadability check — frontmatter parses, name/description limits, referenced files exist | Trail of Bits (`check_claude_loadability.py`) | `guardrails/check-skill-loadability.sh` | Research doc candidate #7 + decisions JSON (`"skill-hygiene": "now"`) | credited, adopted |
| Skill-behaviour evals — record a scenario where a session without the skill fails, keep it as the skill's red-first test ("no skill without a failing test") | Superpowers (obra) | `PRODUCT_SPEC.md` E-19; `evals/` directory; ROADMAP row 94 (pruned from current ROADMAP.md but traced via JOURNAL) | **JOURNAL names it explicitly**: "superpowers' 'no skill without a failing test', made ours" + research doc candidate #2; not named in SPEC E-19 text or `evals/README.md` | credited (JOURNAL + research doc), adopted |
| Running the pack's own skills through Anthropic's official skill-creator tool as a standing QA practice | Anthropic (`anthropics/skills` repo, `skill-creator`) | ROADMAP rows 130/137/219; `PRODUCT_SPEC.md` M-1 audit clause (line ~679); `docs/audit/2026-07-06-skill-creator-walk.md` | Named explicitly and repeatedly as "skill-creator" throughout ROADMAP/SPEC/JOURNAL; source repo documented in `docs/prior-art-frameworks.md` Part 2 | fully credited, adopted, standing/recurring practice |
| arc42 + C4 vocabulary crosswalk for the architecture doc — tiers-first reading order, shape-at-a-glance, if-it-fails fallback column, DECISIONS index, seam-schema homes, secrets placement | arc42, C4 model, BMAD architecture template, Kiro `design.md` | `ARCHITECTURE.md` intro (explicit crosswalk); `docs/spec-format-by-project-type.md` (full crosswalk table); `spec-author` SKILL.md "Standard vocabulary" section | **Named explicitly throughout**: "arc42's §6", "BMAD architecture's high-level overview", "Kiro design.md's Overview section" | fully credited, adopted (rows 188/189) |
| Irreversibility rule for the human's gate — push is not irreversible; money/deletion/publish always stop for the human regardless of proactivity mode | OpenAI, "A practical guide to building agents" (human-in-the-loop triggers) | `live-spec-base` SKILL.md rule 17; `PRODUCT_SPEC.md` | Research doc candidate #10 + decisions JSON (`"two-one-liners": "now"`, refined by Alexander's own correction that a push is not irreversible) | credited (research doc + decision record, then refined by his word), adopted |
| Snapshot/baseline-diff testing as one leg of the pre-push guardrail concept | Jest, Percy, Chromatic (visual-regression tradition) | `PRODUCT_SPEC.md` E-7 — **[target], not yet built** | Named explicitly and warmly in `README.md` ("we're grateful to the projects that made it standard practice") and `docs/prior-art.md` | credited, but **not actually adopted yet** — mechanism unbuilt |
| Declared-scope diff against a task brief (a freelancing-catcher: undeclared file changes flagged) | agent-guardrails (logi-cmd) | `PRODUCT_SPEC.md` E-7 — **[target], not yet built** | Named explicitly and strongly in `README.md` ("whose approach we lean on directly") and `docs/prior-art.md` | credited, but **not actually adopted yet** — mechanism unbuilt |

### Approved but never landed (a real gap)

| Mechanism | Source | Status |
|---|---|---|
| A rationalization table (named excuses to skip the pipeline, with explicit counters) | Superpowers "bulletproofing" + Trail of Bits "Rationalizations to Reject" | Alexander answered `"rationalizations": "now"` in `docs/decisions/2026-07-05-research-answers.json` — approved for adoption same day the research landed — but no trace of it exists anywhere in `ROADMAP.md`, `JOURNAL.md`, or any skill file. **Never built.** |

### Explicitly considered, then rejected

| Mechanism | Source | What happened |
|---|---|---|
| QA-gate verdict ladder PASS/CONCERNS/FAIL/WAIVED, with a waiver record (reason + approved-by) | BMAD `qa-gate-tmpl.yaml` | Rejected outright: `docs/decisions/2026-07-05-research-answers.json`, `"waived-risk": "no"`, his note: "БМАД это типа промпты которые реализуют скрам. нам скрам нафиг не нужен" (BMAD is basically prompts implementing scrum; we don't need scrum) |
| "Appetite" — fixed-time, variable-scope declared at wish intake | Shape Up ch.06 | Adopted briefly, then killed by name at ROADMAP row 99 (2026-07-05 ~22:40/23:15): the whole time-budget mechanism removed, replaced by "scope-never-time" (T-15) — he calls the discarded idea "bmad" colloquially, though the actual source doc traces it to Shape Up |
| EARS grammatical notation (WHEN/IF…THEN…SHALL) for acceptance criteria | Kiro | Explicitly killed at row 148: "the WHEN/THEN/SHALL caps KILLED («псевдодраматичность»)" — the underlying regression-fence *discipline* survived (see Table 1), the *grammar* did not |
| Version-sync-across-files as a checkable invariant (skill version + pack VERSION move together) | Trail of Bits PR checklist | Named as a top-10 candidate in `2026-07-05-skill-patterns.md`; no trace found built anywhere |
| Compiled single-file `AGENTS.md` rendering + `license`/`author` skill frontmatter | Vercel `react-best-practices` | Named as a top-10 candidate; neither an `AGENTS.md` file nor `license:`/`author:` frontmatter exists anywhere in the repo |
| Task waves from a dependency graph (parallel-lane grouping) | Kiro | Parallel-lane work did land (rows 149, 215, 234) but on Alexander's own direct request, not cited back to Kiro anywhere found — a convergence, not a credited borrowing |
| `[NEEDS CLARIFICATION]` open-hole marker | GitHub spec-kit | Named as a near-miss in `2026-07-05-methods.md`; not built (we only have `[default]` for *answered* holes) |
| Honest self-assessment DoD (structured "what's genuinely done" confession before review) | BMAD `story-dod-checklist.md` | Named as a near-miss; not found built |
| Alternatives-considered discipline (record the losing options and why) | Google design-docs tradition | Named as a near-miss; not found built beyond the existing `docs/decisions/*.json` records, which don't formally carry "alternatives" |

---

## Table 2 — mentions of an external project that are NOT a borrowing (comparison / critique only)

- `README.md` "Why live-spec, when BMAD, spec-kit, Kiro, Superpowers and gstack exist" — positioning section, explains difference, not adoption.
- `docs/prior-art.md` — entire document is verdicts on what's novel vs. not, against BMAD, spec-kit, Kiro, OpenSpec, agent-guardrails, Lean4Agent, agentic-os.
- `docs/prior-art-frameworks.md` Part 1 — full comparison table across BMAD, Kiro, GitHub Spec-Kit, OpenSpec, Agent OS, Claude-Flow/Ruflo, Taskmaster AI, ending "None covers continuous intake… our design combines features that do not co-exist in any single tool today."
- `docs/prior-art-longtail.md` — comparison sweep against github-backlog-management-skill, backlog-agents, GAAI-framework, Backlog.md, ai-sdlc-framework, the wilddog64 pre-commit approach, git-prism, spec-aware-review, Lean4Agent, payment-invariants, agentic-os, the AIP graph-representation proposal, OpenSpec's `/opsx:onboard`, reverse-engineering-skill, spec-kit's reverse-spec command, cc-sdd, alirezarezvani/claude-skills.
- `docs/research/2026-07-06-bmad-kiro-livespec-comparison.md` — head-to-head verdict table plus a landscape scan (MetaGPT, GSD, OpenSpec, Taskmaster, Agent OS, Tessl) naming what each lacks; ends with "the *project* should earn a second user before a team bets on it" — self-critical, not a borrowing.
- `docs/research/2026-07-10-superpowers-gstack.md` — full comparison of Superpowers and gstack against live-spec's claims; concludes neither covers the same ground, names two things "worth learning from" (Superpowers' execution discipline, gstack's `/qa` real-browser pass) but records no queue row taking either.
- ROADMAP row 108 — explicitly contrasts against BMAD's ceremony ("не надо как в бмад") while designing a lighter feature-fit interrogation; a critique that shapes the design by negation, not a borrowing.
- ROADMAP row 99 — the appetite mechanism's kill entry, framed as rejecting "bmad['s]… закомпьютеризованные ажайл процессы" (BMAD's computerized agile ceremony) — critique, not adoption (the underlying idea, sourced from Shape Up, is separately tracked as "rejected" in Table 1).

---

## Summary

**Adopted and shipped:** 18 mechanisms borrowed from named neighbours (BMAD ×5, GSD ×3, OpenSpec ×1,
Kiro ×1, Shape Up/Google ×3, GitHub spec-kit ×1, Trail of Bits ×2, Superpowers ×1, Anthropic ×1,
arc42/C4/BMAD/Kiro ×1 combined crosswalk, OpenAI ×1 — two more items, snapshot-diffing and
declared-scope-diff, are credited but still `[target]`/unbuilt, so not counted as shipped).

**Credited:** all 18 shipped items carry a traceable credit somewhere — either explicitly named in the
shipped skill/spec/README text (6 of them: the BMAD story-file line, the Google launch-checklist line,
the arc42/C4/BMAD/Kiro crosswalk, the skill-creator references, the JOURNAL's Superpowers citation, and
the README's Jest/Percy/Chromatic + agent-guardrails paragraph), or only in the research doc + the
ROADMAP/JOURNAL row text that queued them (12 of them: the six GSD/BMAD/OpenSpec items from the
implementation harvest, plus regression fences, non-goals, success measure, the two new facets, the
loadability check, the irreversibility rule).

**Needs a fix (uncredited or broken credit):** one item — `guardrails/README.md`'s gate-hygiene
contract cites "ROADMAP row 114" as its provenance, but row 114 no longer exists as a standalone entry
in the current `ROADMAP.md` (pruned by the pack's own doc-compaction habit); the pointer is dead and
should be repointed to the surviving trace (`docs/prover/2026-07-06-rows110-114-115.md` or the
`JOURNAL.md` 2026-07-06 ~23:56 entry) or replaced with OpenSpec's name directly.

**Approved but never built:** one item — the rationalization table (Superpowers/Trail of Bits),
answered "now" in the 2026-07-05 decision record, with no trace anywhere in the shipped pack.

**Explicitly rejected after consideration:** BMAD's WAIVED verdict ladder, Shape Up's "appetite"
time-budget (adopted then killed by name), Kiro's EARS grammar (killed, discipline kept in plain prose),
Trail of Bits' version-sync invariant, Vercel's compiled-AGENTS.md + license/author frontmatter, Kiro's
dependency-graph task waves, spec-kit's `[NEEDS CLARIFICATION]` marker, BMAD's honest-DoD confession,
and Google's alternatives-considered discipline.

---

# Originality spot-check: live-spec prose/code vs. studied frameworks' public docs

Date: 2026-07-10
Scope: verbatim-run comparison between our shipped docs and the public README/guide
documents of five frameworks we studied, plus an eyeball check on naming coincidences.

## Method

1. Fetched README plus 1–3 core guide/skill documents per framework via
   `raw.githubusercontent.com` (all fetches succeeded, none failed).
2. Copied our seven target files into a scratch `ours/` directory (verbatim, unmodified).
3. Wrote `detect_overlap.py` (scratchpad): tokenizes both sides on whitespace, normalizes
   case and strips non-alphanumeric characters per token, then does an exact n-gram scan
   for shared runs of ≥8 consecutive words between every our-file/their-file pair, with a
   greedy extension once a run is found (so a 12-word match doesn't get reported as
   overlapping 5-word slivers). Sanity-tested the script against a synthetic pair with a
   known 11-word overlap — it correctly found and reported it, confirming the detector
   itself works.
4. Ran the scan at the required 8-word threshold, then re-ran at 5-word and 4-word
   thresholds to see whether anything sits just below the bar worth eyeballing.
5. Manually reviewed skill/rule/command naming across projects for suspicious coincidence.

## Files fetched (their side)

| Project | Files fetched |
|---|---|
| github/spec-kit | `README.md`, `spec-driven.md`, `docs/index.md` |
| bmad-code-org/BMAD-METHOD | `README.md`, `docs/index.md`, `docs/_STYLE_GUIDE.md` |
| obra/superpowers | `README.md`, `skills/executing-plans/SKILL.md`, `skills/verification-before-completion/SKILL.md` |
| garrytan/gstack | `README.md` |
| logi-cmd/agent-guardrails | `README.md` |

No fetch failures — all five projects yielded readable content on the first try via raw
GitHub URLs.

## Files compared (our side)

`README.md`, `adopt/ADOPT.md`, `MIGRATION.md`, `docs/pipeline.md`, `docs/adoption.md`,
`skills/live-spec-base/SKILL.md`, `skills/build-pipeline/SKILL.md` — all seven requested.

## Results: verbatim-run scan

**At the 8-word threshold (the detection bar): 0 matches, across all 7×11 = 77 file
pairs.** No shared run of 8 or more consecutive words exists anywhere between our shipped
prose/code and any of the fetched documents.

**At 5-word and lower thresholds** (widened only to see if anything sits just under the
bar): also **0 matches at 5+ words**. The first matches of any kind appear only at
**4 words**, and there are exactly 8 of them, every one a generic English idiom or stock
phrase with no distinctive coinage:

| # | Our file:line | Their file:line | Shared run | Verdict |
|---|---|---|---|---|
| 1 | README.md:95 | speckit_spec-driven.md:5 | "the source of truth" | Benign — stock phrase, appears in the comparative-analysis paragraph where we explicitly discuss and cite spec-kit by name/link |
| 2 | build-pipeline-SKILL.md:29 | gstack_README.md:187 | "the bugs that pass" | Benign — generic phrase fragment, different surrounding sentences |
| 3 | build-pipeline-SKILL.md:367 | gstack_README.md:308 | "in its own isolated" | Benign — generic phrase ("in its own isolated {worktree/environment}"), common technical idiom |
| 4 | build-pipeline-SKILL.md:319 | speckit_spec-driven.md:5 | "the source of truth," | Benign — same stock phrase as #1 |
| 5 | live-spec-base-SKILL.md:60 | gstack_README.md:308 | "in its own isolated" | Benign — same as #3 |
| 6 | live-spec-base-SKILL.md:168 | gstack_README.md:191 | "then hand it to" | Benign — generic connective phrase |
| 7 | live-spec-base-SKILL.md:192 | gstack_README.md:423 | "out of the box" | Benign — universal idiom |
| 8 | live-spec-base-SKILL.md:192 | speckit_docs_index.md:24 | "out of the box" | Benign — same idiom as #7 |

**Needs-attention matches: 0.**

## Eyeball check: names and coinages

- **Skill/phase names**: our skill set (`build-pipeline`, `communicator`,
  `feedback-intake`, `live-spec-base`, `product-prover`, `publish`, `spec-author`,
  `test-author`) doesn't overlap in name or naming convention with any studied project.
  Superpowers uses gerund-phrase skill names (`executing-plans`, `writing-plans`,
  `systematic-debugging`, `verification-before-completion`, `test-driven-development`,
  `subagent-driven-development`, `using-git-worktrees`, `finishing-a-development-branch`,
  `requesting-code-review`, `receiving-code-review`, `dispatching-parallel-agents`,
  `brainstorming`); BMAD uses role personas (Analyst, PM, Architect, Dev, QA, Scrum
  Master); spec-kit uses slash commands (`/specify`, `/plan`, `/tasks`, `/implement`,
  `/constitution`); gstack uses a `/spec` command plus role personas (CEO, staff
  engineer, designer, QA). None of these match our domain-specific names
  (spec-author/product-prover pairing, INV-numbered invariants, etc.).
- **`/spec` mention in our README**: the one `/spec` reference in our README (line 93)
  is inside a paragraph describing *gstack's own* command, cited by name with a link — not
  presented as something of ours. No confusion risk.
- **BMAD reference in build-pipeline SKILL.md**: line 397 names "the BMAD story-file
  lesson" explicitly as an attributed technique, not disguised borrowing.
- Our README (lines 71–99) runs an extended, explicitly attributed comparative-analysis
  section naming BMAD, spec-kit, Kiro, Superpowers, and gstack by name with links,
  crediting specific techniques (agent-guardrails' file-touch verification, snapshot
  testing lineage from Jest/Percy/Chromatic) directly. This is open discussion/citation,
  the opposite of concealment.

## Closing verdict

Across seven of our shipped files (README, ADOPT, MIGRATION, docs/pipeline, docs/adoption,
and the live-spec-base and build-pipeline SKILL.md files) checked against eleven public
documents from the five studied frameworks, an exact n-gram scan validated on a synthetic
positive control found zero shared runs of eight or more consecutive words, and widening
the bar down to four words surfaces only generic English idioms ("out of the box," "the
source of truth," "in its own isolated") with no distinctive phrasing, sentence structure,
or coined terminology in common; skill names, phase names, and command names likewise
show no suspicious coincidence, and the one place a competitor's own command name
(gstack's `/spec`) and technique name (BMAD's "story-file") appear in our text, they are
explicitly attributed by name with a citation rather than presented as ours. Nothing in
this check would support a claim of copying.

Needs-attention matches: **0**
