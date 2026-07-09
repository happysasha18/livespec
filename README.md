# live-spec

live-spec is a pack of eight Claude Code skills for spec-driven development. A wish spoken in passing enters a fixed pipeline: it is classified, written into a living product spec, reviewed, covered by tests, coded to green, and committed with its documents in the same change. Executable scripts gate the pipeline, so the discipline holds across session resets and memory wipes.

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

The pack has no CLI. Everything is driven in plain words inside a Claude Code session: "attach live-spec to this project", any wish in passing, "status", "publish".

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

This repo runs on its own method: it carries its own `PRODUCT_SPEC.md`, queue, tests, and prover records (`docs/prover/`). The method has run in production on the sibling project [track-coach](https://github.com/happysasha18/track-coach) (700+ tests, 30-widget library). For an honest outside look, two independent source-level comparisons with the neighbouring frameworks (`BMAD`, [Kiro](https://kiro.dev), [Spec Kit](https://github.com/github/spec-kit)) are published unsoftened in [`docs/research/`](docs/research/).

## Known issues

We keep this list honest and current, and we review it at every push.

- **Internal vocabulary can leak into human-facing text.** The pack's working terms, and loan-translations from other languages, sometimes appear in text meant for people. A register lint blocks any shown artifact that carries a known leaked term, and its pattern list grows with every catch. Chat messages have a reminder hook and stay the weakest surface.
- **The spec's Formal index has open style debt.** The product spec's closing Formal index section carries an unfinished style cleanup. It holds 63 recorded style-lint findings and 10 redundancy candidates. These stand as counted, dated debt until that section's restyle lands.
- **First-run onboarding is a mockup only.** Onboarding exists as an approved-pending mockup and does not run yet. Today a new project is set up by hand, following the settings documentation.
- **Guardrail checks ship as descriptions.** The scaffold describes four guardrail checks, and each project wires its own instance. Generic runnable check code has not shipped yet.

## License

`MIT` (see the `LICENSE` file). Copyright Alexander Abramovich 2026.
