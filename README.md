# live-spec

**A software house under your fingertips. Eight [Claude Code](https://claude.com/claude-code) skills that take a wish spoken in passing and return a specified, reviewed, tested, committed change.**

You say *"the report page needs a date filter"* in the middle of something else. No ticket, no planning session, no form. It gets classified, written into the living spec, reviewed by a formal-verification pass, covered by tests derived from that spec, coded until green, and committed together with its documents in the same change.

There is no CLI. You talk to it. There are no commands to memorize: a wish arrives in one sentence mid-conversation and the pipeline runs underneath, so a newcomer has no command list to hunt for.

---

## Install

Claude Code required. As a plugin:

```
/plugin marketplace add happysasha18/live-spec
/plugin install live-spec@live-spec
```

Or from source, if you'd rather see what you're installing first:

```bash
git clone https://github.com/happysasha18/live-spec.git
cd live-spec && ./install.sh
```

The script copies every skill into `~/.claude/skills/`, backing up any same-named skill to `~/.claude/skills-attic/` with a timestamp — re-running is safe.

Then attach the pack to a project:

- **New project** — copy the templates from [`templates/`](templates/) into the project root.
- **Existing codebase** — follow [`docs/adoption.md`](docs/adoption.md): inventory the code, write the spec from what actually ships, pin the architecture to the real files, derive the tests from there.

Everything after that runs in plain words: *"attach live-spec to this project"*, any wish, *"status"*, *"publish"*. It follows whatever language you speak; what it writes — documents, code, commits — is always in English.

---

## Why it doesn't interrogate you

Most spec tooling dies on the question load. Fourteen fields before anything moves. *What about the empty state? What about permissions? What if two users do this at once?* Every question is reasonable, and collectively they are why the tool sits unused after week two: the cost of being asked exceeds the cost of the bug the question would have prevented, so people route around it.

live-spec answers most of them itself. The rule is **ask, never guess — and never ask what you can decide or verify yourself.** Before a fork is put to you, the pack checks whether a proven artifact already settles it. If the architecture, the spec, or an invariant determines the answer, the requirement is *derived* and said back with the section cited as its ground, and no fork reaches you at all. What does reach you is what the documents genuinely leave open: a taste call, or a real trade-off with no artifact-grounded winner.

A pending question rides in its row while the lane keeps moving on the recommendation. You are not stopped at the door to confirm that yes, errors should be handled. Every default the pipeline picked is stated plainly in the landing report and marked tweakable, so you can overrule any of them in a sentence.

---

## The one claim: the gates are executable

Everything else in this pack is borrowed and credited. The part worth defending is that **the enforcement is mechanical, not rhetorical.**

- **Traceability** — every fact in the spec has an owning test.
- **Freshness** — the documents match what actually shipped.

A change that drifts from its specification is *blocked*. Not reminded. Not tut-tutted at by a prompt. The surveyed alternatives enforce their specs by instructing a model to check — and a model having a bad day says it checked.

The checks run twice from one source: the local pre-push hook, and [a CI mirror](.github/workflows/gates.yml) running *the same scripts* — a fresh prover record, the full suite, matrix coverage, skill loadability, pin drift. The local hook is a latency optimization. CI is the net that always runs the full set.

A project adopting the pack gets four checks of its own under [`scaffold/guardrails/`](scaffold/guardrails/) — completeness, tests-present, behaviour-traces-to-spec, conflicts. Python 3.9 stdlib, nothing to install, one config file parametrizes everything, and you never edit check code. About fifteen minutes to attach.

They are honest by construction, which is the part worth reading twice:

- A **missing config is red**, with a line telling you to attach it — never a silent pass.
- A config pointing at a path that doesn't exist is red.
- A precondition you genuinely lack is declared as a **waiver in the config**, where a reader sees it — `WAIVED (<check>): <reason>` — visible, exit 0, never silent.
- On red, each check prints the human sentence *and* one machine line: `GUARDRAIL-FAIL {...}`, valid JSON.

Everything binds to one living spec: intake validates each wish against it, tests derive from it, the prover reviews it, adoption reverse-generates it from an existing codebase — and the pipeline itself is specced and proven the same way. This repo carries its own `PRODUCT_SPEC.md`, queue, tests, and prover records in [`docs/prover/`](docs/prover/).

---

## A wish, end to end

*"The report page needs a date filter."*

1. **Intake** — classified before any code (this one adds an interaction, so: feature), lands as a row in [`ROADMAP.md`](ROADMAP.md).
2. **Spec** — `spec-author` writes the delta into `PRODUCT_SPEC.md`: the scenario a user walks, fences naming what must keep working on the touched page, a sweep of the standard facets (empty state, errors, phone, accessibility), non-goals, a success measure.
3. **Prove** — `product-prover` reviews the delta with formal-verification thinking. Defect findings fold into the spec; open decisions come back as one batched set, not a drip.
4. **Architecture** — `ARCHITECTURE.md` gains the filter's owning node, pinned to its place in the code. The prover checks that too.
5. **Tests** — `test-author` derives matrix rows for the new facts, pins each to a level on the ladder from string checks up to pixel comparison, and writes tests against the real rendered page. Each new test **fails first**, proving it can catch the missing behaviour.
6. **Code** — implement until green: zero failures, skipped tests matching the expected list exactly.
7. **Verify** — the guardrail scripts run before anything moves outward.
8. **Commit** — the change lands in one commit with its spec, matrix, and architecture updates. The report back to you is one plain line.

A bug takes the short road: matrix row, failing test, fix. The spec is touched only if the broken fact was never written down.

Full walk: [`docs/pipeline.md`](docs/pipeline.md).

---

## The rules underneath

One rulebook, stated once, that every skill works by — [`live-spec-base`](skills/live-spec-base/SKILL.md). Restating a shared rule inside a working skill counts as drift and gets folded at the next milestone. Some of what's in there:

**Work is routed per unit, to the cheapest tier that passes its brief.** A one-shot with no decision in it goes to a small model; multi-step mechanical work to a mid model; anything carrying judgment or design to the senior — and a judgment step is never routed down. Size is a weak hint, never the decider. Every override and every failed acceptance is logged: proposed tier → chosen tier → why.

**A worker's green is a lead, not a fact.** The worker pastes raw output — command, exit code, failing lines — as it goes. Raw output is evidence; the worker's prose is only a lead. The lead accepts a green by re-checking it, never on trust, and a large landing earns an independent fresh-context checker on top.

**Long work survives being cut off.** Every delegated or long-running lane keeps a checkpoint file on disk — done, in progress, next — updated *as* it runs, so an interrupted session resumes from disk instead of restarting. Red at a pause is never committed: the failing test name plus a hypothesis becomes the top item in `NEXT_STEPS.md`.

**A background worker from a previous context is a concurrent writer.** It survives a memory wipe, and neither the OS process list nor the harness task list is proof of death. A resuming session treats it as a foreign writer until three checks agree: the write-set's file times over a short window, the worker's heartbeat on its own checkpoint file, and one message to its recorded id.

**Every write re-checks the fence.** `git status` and HEAD against what was last read; if HEAD moved or the tree holds changes you didn't make — stop, re-read, then proceed surgically or back off. Up to three build lanes may roll in one session: every write to a shared document serializes under a single pen, and a later lane's code lives in an isolated worktree until it's integrated.

**Plain words carry the meaning; codes trail quietly.** No human-facing sentence leans on an internal handle. In chat the anchor trails in parentheses — *"no remote copy exists (INV-8)"*; in documents it sits at the line end in brackets. Never open a line with a code, and never loan-translate a coined term into the language you're speaking.

---

## What it taught us it cannot do

The sharpest critique of this pack came from using it.

The first real project built under it — a photo-portfolio site — shipped with every written promise intact. Nothing regressed. Traceability passed, freshness passed, the suite was green. And the site read as eighty percent finished, everywhere.

Everything that felt unfinished was living where the method wasn't looking. It specced *surfaces*; the visitor moves *between* them, and that path was unspecified. Verification confirmed "works" and stayed silent on "feels". Taste defaults accumulated, each individually reasonable, until the whole thing felt provisional.

This taught the method a boundary, which it now states as its own position:

> **A spec owns what a project can write down and test. Feel belongs to the owner's eye.**

"Everything looks eighty percent finished" formalizes badly. You can force it — invent a rubric, a taste linter, a scoring pass — and what you get is a test that goes green on a product that still feels dead. That is worse than no test, because now green means less everywhere. The method never dresses a taste call up as a test.

It routes instead. Three mechanisms carry the work, and they are shipped: a **visitor walk** at verify, traversing the product the way a person actually moves through it; a **feel pass**, scaled to the medium (a site walks its motion, a book walks its reading path); and **landing reports that state every taste default plainly and mark it tweakable**, so the calls the pipeline made silently arrive at your eye while changing them is still cheap.

The method's job is to bring the right call to a human at the right moment. Not to make the call.

---

## The skills

| Skill | When to use it |
|---|---|
| `live-spec-base` | The rulebook above: twenty-eight shared rules and the settings ladder. Loaded whenever another pack skill runs; when two skills seem to disagree, this one wins. |
| `build-pipeline` | Start here for any non-trivial change: *"build X properly"*, *"spec and ship Y"*. It sequences the whole arc from wish to committed change. |
| `spec-author` | Writes and grows the living spec: a new feature, a new stateful surface. Scenarios lead; formal codes trail as anchors. |
| `product-prover` | Reviews a spec or design document: *"poke holes in this"*. Reads documents; code review and tests stay elsewhere. Also published [standalone](https://github.com/happysasha18/product-prover). |
| `design-reviewer` | Reviews the design itself once the spec is proven: proposes the same-kind groupings the text never declared, checks each kind behaves alike, and brings you the strongest likely difference with both objects in hand. Recommends and questions; leaves the landing free. |
| `test-author` | Derives `TEST_MATRIX.md` from the proven spec and writes the tests. Call it directly for *"why did green tests miss this bug?"*. |
| `communicator` | Shows work and asks for decisions you can actually make: milestone reports, decision pages, evidence walks. |
| `feedback-intake` | Receives whatever you hand back — a remark, an answer, a screenshot, a dropped file — and routes each item to the file that owns it. |
| `publish` | The quality gate before work leaves the machine: a repo going public, a release, a directory submission, a README update. |

Docs: [pipeline](docs/pipeline.md) · [architecture method](docs/architecture-method.md) · [test method](docs/test-method.md) · [settings & onboarding](docs/onboarding-and-settings.md) · [commit & push gates](docs/push-law.md) · [background workers](docs/worker-liveness.md) · [adoption](docs/adoption.md) · [pair adoption](docs/pair-adoption.md) · [what lives where](OVERVIEW.md)

---

## Who it's for

Builders working with Claude Code who want every change to leave a specified, reviewed, tested trail — and who work *continuously* rather than in planning cycles. Wishes arrive mid-conversation in one sentence, a persistent queue carries them across sessions, and a cold session resumes from files alone. The full pipeline is for changes that add a surface, a state, or a behaviour; a tiny reversible edit shortcuts straight to code plus a test.

---

## Prior art, honestly

[BMAD](https://github.com/bmad-code-org/BMAD-METHOD), [Spec Kit](https://github.com/github/spec-kit), [Kiro](https://kiro.dev), [Superpowers](https://github.com/obra/superpowers) and [gstack](https://github.com/garrytan/gstack) all got there first on something, and they share the right instinct: spec before code. Use them if their shape fits your work — Superpowers in particular is better than anything here on execution discipline, and its quarter-million stars are earned.

What the July-2026 survey did not find anywhere is the integration this pack claims: one persistent living spec as the single authority that validates every wish at intake, derives the tests, passes a formal review, and stays the source of truth for the life of the project. Superpowers is process-centric — the procedure persists, and the artifact is whatever the procedure produced. gstack's traceability runs one direction and stops at merge. Snapshot testing comes from Jest, Percy and Chromatic; scope-declaration checking from [agent-guardrails](https://github.com/logi-cmd/agent-guardrails). Six mechanisms the neighbours do better went into the queue.

The full record, including the parts that don't flatter this repo:

- [`docs/prior-art.md`](docs/prior-art.md), [`docs/prior-art-frameworks.md`](docs/prior-art-frameworks.md) — the survey
- [`docs/research/2026-07-10-originality-audit.md`](docs/research/2026-07-10-originality-audit.md) — every borrowed mechanism with its source; a scan against their public docs found no shared runs of eight or more consecutive words
- [`docs/research/2026-07-06-bmad-kiro-livespec-comparison.md`](docs/research/2026-07-06-bmad-kiro-livespec-comparison.md) — clean-context model reviews, briefed to verify claims against the actual files and to criticize all three subjects, published in full

Read those for the criticism: this project is young and single-author, its strongest production evidence belongs to a sibling project ([track-coach](https://github.com/happysasha18/track-coach) — 700+ tests, a 30-widget library), and its judgment loop is one model reviewing its own work. Only the mechanical gates are genuinely independent — which is exactly why it matters that they are scripts and not prompts.

If you know prior art we missed, open an issue. We'd like to read it.

---

## Known issues

Reviewed at every push; an issue leaves the list the moment its fix ships.

- **Internal vocabulary leaks into human-facing text.** The pack's working terms, and loan-translations from other languages, sometimes surface in text meant for people. A register lint blocks any shown artifact carrying a known leaked term, and its pattern list grows with every catch. Chat messages have a reminder hook and remain the weakest surface.
- **The spec's Formal index carries style debt.** 62 recorded style-lint findings and 11 redundancy candidates, counted and dated, standing until that section's restyle lands.
- **The settings card is young.** Setup ends with a rendered settings card (`scripts/onboarding-card.py`) — one page showing what is set up and what is yours to change. It has run on one real project; expect rough edges on unusual profile shapes, and report them.

---

## License

[MIT](LICENSE) © Alexander Abramovich, 2026. Current release: [`VERSION`](VERSION).
