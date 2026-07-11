# live-spec

live-spec is a pack of eight Claude Code skills for spec-driven development. A wish spoken in passing enters a fixed pipeline: it is classified, written into a living product spec, reviewed, covered by tests, coded to green, and committed with its documents in the same change. Eight executable checks wired into git gate this repository's own pipeline, blocking commits and pushes when the discipline slips, so it holds across session resets and memory wipes. A project that adopts the pack gets the same for its own side: four runnable checks under `scaffold/guardrails/` — completeness, tests-present, behaviour-traces-to-spec, and conflicts — each a standalone Python script driven by one config file the project fills in, attachable to its pre-push hook in about fifteen minutes. This repository is the first host to run them on its own pushes.

The current release number lives in [`VERSION`](VERSION). [`OVERVIEW.md`](OVERVIEW.md) is the one-page map of what lives where.

## Who it is for

Builders who develop with Claude Code and want every change to leave a specified, reviewed, tested trail. The pack fits continuous work: wishes arrive mid-conversation in one sentence, a persistent queue carries them across sessions, and a cold session resumes from files alone. The full pipeline is for changes that add a surface, a state, or a behaviour; a tiny reversible edit shortcuts straight to code plus a test.

## Install

Claude Code is required.

```bash
git clone https://github.com/happysasha18/live-spec.git
cd live-spec
./install.sh
```

The script copies every skill into `~/.claude/skills/`, where Claude Code loads them in every project on the machine. When a skill with the same name already exists there, the script first backs it up to `~/.claude/skills-attic/` with a timestamp, so re-running is safe.

Then attach the pack to a project:

- New project: copy the document templates from [`templates/`](templates/) into the project root.
- Existing codebase: follow [`docs/adoption.md`](docs/adoption.md) — inventory the code, write the spec from what actually ships, pin the architecture to the real files, derive the tests from there.

The pack has no CLI. Everything is driven in plain words inside a Claude Code session: "attach live-spec to this project", any wish in passing, "status", "publish". Conversation happens in whatever language you write — it follows you, with no setup. Written work — documents, code, commit messages — is always in good English.

## A worked example

A wish arrives mid-conversation: "the report page needs a date filter."

1. **Intake.** The wish is classified before any code (this one adds an interaction, so it is a feature) and gets a row in the project queue (`ROADMAP.md`). The `build-pipeline` skill drives every step from here.
2. **Spec.** `spec-author` writes the delta into `PRODUCT_SPEC.md`: the scenario the user walks, fences naming what must keep working on the touched page, a sweep of the standard facets (empty state, errors, phone, accessibility), non-goals, and a success measure.
3. **Prove.** `product-prover` reviews the delta with formal-verification thinking. Must-fix findings are folded into the spec; open decisions go back to the human as one batched set of questions.
4. **Architecture.** `ARCHITECTURE.md` gains the filter's owning node, pinned to its place in the code, and the prover checks the updated document.
5. **Tests.** `test-author` derives matrix rows for the new facts, pins each row to a test level on the ladder from plain string checks up to pixel comparison, and writes tests that assert the real rendered page. Each new test fails first, proving it can catch the missing behaviour.
6. **Code.** Implement until the suite is green: zero failures, and the skipped tests match the expected list exactly.
7. **Verify by deed.** The guardrail scripts run before anything moves outward: traceability (every spec fact has an owning test) and freshness (the documents match the shipped truth). These are executable checks that block a push.
8. **Commit and show.** The change lands in one commit together with its spec, matrix, and architecture updates, and accepted work reaches the project's remote by rule (see [`docs/push-law.md`](docs/push-law.md)). The report to the human is one plain line. A release the human reserved by name — a version milestone on their explicit word — waits for that word.

A bug takes a shortcut: matrix row, failing test, fix — the spec is touched only when the broken fact was never written down. The example compresses the pipeline; the full station-by-station walk is [`docs/pipeline.md`](docs/pipeline.md).

## The skills

| Skill | When to use it |
|---|---|
| `live-spec-base` | The shared rulebook and default settings, stated once. Loaded whenever any other pack skill is in use; when two skills seem to disagree, this file wins. |
| `build-pipeline` | Start here for any non-trivial change: "build X properly", "spec and ship Y". It sequences the whole arc from wish to committed change. |
| `spec-author` | Writes and grows the living spec: "spec this out", a new feature, a new stateful surface. Scenarios lead; formal codes trail as anchors. |
| `product-prover` | Reviews a spec or design document: "poke holes in this", "is this spec ready?". It reads documents; code review and tests stay elsewhere. Also published as a [standalone repo](https://github.com/happysasha18/product-prover). |
| `test-author` | Derives `TEST_MATRIX.md` from the proven spec and writes the tests. `build-pipeline` invokes it at the matrix and test steps; call it directly for "derive the test matrix" or "why did green tests miss this bug?". |
| `communicator` | Shows work and asks for decisions the human can actually make: milestone reports, decision pages, evidence walks. |
| `feedback-intake` | Receives whatever the human hands back (a remark, an answer, a screenshot, a dropped file) and routes each item to the file that owns it. |
| `publish` | The quality gate before work leaves the machine: a repo going public, a release, a directory submission, a README update. |

## Docs map

- [`docs/pipeline.md`](docs/pipeline.md) — the pipeline walk, wish to shipped change
- [`docs/architecture-method.md`](docs/architecture-method.md) — the architecture method: tiers, runtime and placement views, budgets
- [`docs/test-method.md`](docs/test-method.md) — the test level ladder and the five field lessons
- [`docs/onboarding-and-settings.md`](docs/onboarding-and-settings.md) — settings ladder and per-person profiles
- [`docs/push-law.md`](docs/push-law.md) — commit and push gates
- [`docs/worker-liveness.md`](docs/worker-liveness.md) — background workers: spawning, liveness, resume
- [`docs/adoption.md`](docs/adoption.md) — adopting the pack in an existing project
- [`docs/pair-adoption.md`](docs/pair-adoption.md) — adopting as a pair: an engine and its instance

This repo runs on its own method: it carries its own `PRODUCT_SPEC.md`, queue, tests, and prover records (`docs/prover/`). The method has run in production on the sibling project [track-coach](https://github.com/happysasha18/track-coach) (700+ tests, 30-widget library).

## Why live-spec, when [BMAD](https://github.com/bmad-code-org/BMAD-METHOD), [spec-kit](https://github.com/github/spec-kit), [Kiro](https://kiro.dev), [Superpowers](https://github.com/obra/superpowers) and [gstack](https://github.com/garrytan/gstack) exist

They are good, and they share the right instinct: spec before code. Use them if their shape fits your work.

live-spec is built for **continuous** work: you throw wishes in passing, mid-anything, and each one enters the process in a sentence. No planning session is required, the queue is persistent across sessions, and execution runs asynchronously while you keep talking.

Snapshot testing, familiar from tools like Jest, Percy, and Chromatic, works by comparing a result against a saved reference and flagging any difference; that idea does a lot of the heavy lifting here, and we're grateful to the projects that made it standard practice. Verifying that an AI coding agent touched only the files declared for its task comes from [agent-guardrails](https://github.com/logi-cmd/agent-guardrails), whose approach we lean on directly. Our own contribution is the integration: binding both checks to a single living specification document. Thanks to all of this prior work for the foundation.

live-spec's one claim is the **integration**: the spec is the single authority binding the whole loop —

- intake validates every wish against it,
- scope declarations derive from it,
- a prover skill formally reviews it,
- adoption reverse-generates it from an existing codebase, and
- the development process itself is specced and proven the same way (this repo's own `PRODUCT_SPEC.md` went through product-prover before its first publish — findings in `docs/prover/`).

Our July-2026 survey — 7 frameworks plus a long-tail skill-ecosystem search — found that integration nowhere; the raw notes are in [`docs/prior-art.md`](docs/prior-art.md) and [`docs/prior-art-frameworks.md`](docs/prior-art-frameworks.md). If you know prior art we missed, open an issue — we would genuinely like to read it.

Two more frameworks rose to prominence while this pack was being built; read as of July 2026, full notes in [`docs/research/2026-07-10-superpowers-gstack.md`](docs/research/2026-07-10-superpowers-gstack.md).

[Superpowers](https://github.com/obra/superpowers) (Jesse Vincent) is the strongest of the field on process discipline, and it earns its roughly quarter-million GitHub stars. Its seven-phase workflow is mandatory and sequential — brainstorming through worktree isolation, planning, subagent implementation, test-driven development, code review, and branch finishing — and it holds the line where raw agents cut corners: tests come before production code by an explicit rule, and completion may be claimed only with fresh verification evidence. The difference from live-spec is structural. Its design document is a per-feature file dated in its own path and committed at approval, and no source describes it being revisited afterward; it is a one-time gate per feature. An [independent comparison](https://dev.to/truongpx396/spec-kit-vs-superpowers-a-comprehensive-comparison-practical-guide-to-combining-both-52jj) puts it plainly: Superpowers is process-centric, where a spec tool is artifact-centric — the procedure persists, and the artifact is whatever the procedure produces. Invariants as a first-class idea, a single spec living across the project's life, and a requirement-to-code audit trail are all absent by design.

[gstack](https://github.com/garrytan/gstack) (Garry Tan) took a different bet and has drawn about 120,000 stars since its March 2026 launch. Its strength is role-based review: separate personas for CEO, staff engineer, designer, and QA produce genuinely different answers and surface edge cases a single pass would miss. It reaches for a second model, dispatching OpenAI's Codex as an independent reviewer, and its QA command drives a real Chromium browser — clicking through flows, fixing what breaks, and writing regression tests. On the spec itself its design draws a firm boundary: the `/spec` command turns intent into a single GitHub issue through a one-shot quality gate that scores the draft before filing; the archive stays local by default, and traceability runs one direction and stops at merge, where the pull request carries a `Closes #N` line when it delivers the whole spec. Third-party writeups reach the same reading — the [Pulumi comparison](https://www.pulumi.com/blog/claude-code-orchestration-frameworks/) and a [combination guide](https://dev.to/imaginex/a-claude-code-skills-stack-how-to-combine-superpowers-gstack-and-gsd-without-the-chaos-44b3) both note that gstack lacks native specification-anchoring and recommend pairing it with a separate context layer to supply what it leaves out.

Both frameworks confirm the ground this section claims. The integration of one persistent living spec — the single authority that validates every wish at intake, derives the tests, passes a formal review, and stays the source of truth for the whole life of the project — is exactly the space these tools leave open. Their execution discipline is real, and we take it as the bar to meet on that layer.

A borrowing audit closes the loop (July 2026): it lists every mechanism this pack adopted from these neighbours together with its source, and a scan of our shipped files against their public docs found no shared runs of eight or more consecutive words. The full record: [`docs/research/2026-07-10-originality-audit.md`](docs/research/2026-07-10-originality-audit.md).

An independent look, July 2026: two clean-context analysts — briefed to verify this repo's claims against its actual files and to criticize all three subjects — compared live-spec with BMAD and Kiro, and three more read Spec Kit, OpenSpec, GSD and BMAD at source level. Their verdicts are published in full, including the uncomfortable parts: this project is young and single-author, its "production-proven" evidence largely belongs to a sibling project, and its judgment loop is one model reviewing itself — only the mechanical gates are independent. Full texts: [the comparison](docs/research/2026-07-06-bmad-kiro-livespec-comparison.md) and [the implementation-level harvest](docs/research/2026-07-06-neighbours-implementation-harvest.md).

One distinction both analysts confirmed by running things: live-spec's traceability and freshness gates are executable scripts that block a push, while the surveyed alternatives enforce their specs by prompt text (Spec Kit's consistency checks, analyze and converge included, are LLM instructions — the only mechanical checks in its repo are file-existence tests). Six mechanisms the neighbours genuinely do better were taken into our queue.

The sharpest critique arrived the same week from use. The first real project built under the pack — a photo-portfolio site — reported that while no written promise ever regressed, everything that felt unfinished lived where the method wasn't looking: it specced surfaces, the visitor's path went unspecified, verify-by-deed confirmed "works" and stayed silent on "feels", and taste defaults accumulated until the product read eighty-percent-finished everywhere. This converges with the analysts' structural critique, so we treat it as the strongest entry in this section. The answer is shipped work: a product-fit interrogation on every incoming feature, a visitor-walk and feel pass at verify (scaled to the medium: a site walks motion, a book walks its reading path), and landing reports that state every taste choice plainly, marked tweakable. These lenses have since run on the pack's own features and on real incoming wishes.

That critique taught the method a boundary that it now states as its own position. A spec owns what a project can write down and test. Feel belongs to the owner's eye. A judgment like "everything looks eighty percent finished" formalizes badly as a test. The method answers taste by routing: it brings the right call to the owner's eye at the right moment, and it never dresses a taste call up as a test. Three routes carry this work: the feel pass at verify, the visitor walk, and the list of taste defaults that each landing report states plainly and marks tweakable. The photo-portfolio project stays cited here as the case that taught the boundary.

## Known issues

This list is reviewed at every push; a resolved issue leaves it the moment its fix ships.

- **Internal vocabulary can leak into human-facing text.** The pack's working terms, and loan-translations from other languages, sometimes appear in text meant for people. A register lint blocks any shown artifact that carries a known leaked term, and its pattern list grows with every catch. Chat messages have a reminder hook and stay the weakest surface.
- **The spec's Formal index has open style debt.** The product spec's closing Formal index section carries an unfinished style cleanup. It holds 62 recorded style-lint findings and 11 redundancy candidates. These stand as counted, dated debt until that section's restyle lands.
- **The settings card is young.** Project setup now ends with a rendered settings card (`scripts/onboarding-card.py`) — one page showing what is set up and what is yours to change. It shipped today and has run on one real project; expect rough edges on unusual profile shapes, and report them.

## License

`MIT` (see the `LICENSE` file). Copyright Alexander Abramovich 2026.
