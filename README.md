# live-spec

**Ten [Claude Code](https://claude.com/claude-code) skills that turn a wish spoken in passing into a specified, reviewed, tested, committed change — with scripts that block the push when the documents and the code disagree.**

---

You tell your agent *"the report page needs a date filter"* and four minutes later it is written, tested, and green. The tests pass because they came from the same spec, and the spec never said what happens when the date is invalid, so the agent picked something and shipped it. Nobody chose that behaviour and nobody reviewed it; the green suite never looked at it.

That is the gap. The spec became the thing your agent builds from, and nothing checks the spec itself.

live-spec closes it. You say the sentence in passing, with no ticket and no form. It gets classified, written into a living spec, reviewed by a formal-verification pass, covered by tests derived from that spec, coded until green, and committed with its documents in one change. A script on the pre-push hook compares the spec to the code that shipped and refuses the push when the two disagree. There is no CLI; you talk to it.

---

## Install

```
/plugin marketplace add happysasha18/live-spec
/plugin install live-spec@live-spec
```

Or clone and run `./install.sh`. Then attach it to a project: [`templates/`](templates/) for a new one, [`docs/adoption.md`](docs/adoption.md) for an existing codebase, where it writes the spec from what actually ships first. After that everything runs in plain words: *"attach live-spec to this project"*, any wish, *"status"*, *"publish"*.

---

## What's different

**The gates are scripts, not prompts.** Two checks decide whether a push is allowed: every fact in the spec has an owning test, and the documents match what shipped. Both are Python on the pre-push hook, mirrored in [CI](.github/workflows/gates.yml). A change that drifts from its specification is refused. The alternatives enforce their specs by instructing a model to check, and a model having a bad day says it checked.

**It refuses to ship theatre, and writes down why.** A queue row asked for a gate that would fail any session working serially instead of in parallel. The [prover's record](docs/prover/) for that landing says no, with reasons: independence is a judgment rather than a diff, the evidence a correct run would leave is destroyed by design, and the one mechanical signal available would fire on every lawful serial run. It shipped as a recorded discipline instead. The house phrase is **a law with no machine is a wish**, and its corollary is that a judgment call is never a gate. There are 292 of those records in [`docs/prover/`](docs/prover/), including the ones where the reviewer missed something and said so.

**The rules are built for a model's failure modes.** Every claim shown for review is tagged with its provenance — read from the artifact, your own recorded word, or the agent's inference, with inferences flagged loudest — because the line between what a document says and what a model filled in is invisible to a reader, and that is where the errors live. A background worker from a dead session is treated as a concurrent writer until three signals agree it stopped. A decision withdrawn twice takes its recommendation and is never raised again, because a tireless agent will not stop asking on its own.

---

## Three thousand lines of rules, and that is the point

They are not a configuration burden waiting for you. They are the part a software house would charge you for — thirty-three shared rules, stated once: how a spec gets written so it stays readable, when a question is worth your attention and when it isn't, what a green suite does and doesn't prove. You do not read them. They run.

The relationship is the one you have with a builder rather than with a framework: **you don't need to know how; you still decide what.** A good contractor doesn't ask the client to choose the rebar, and doesn't pick the kitchen either.

Which does mean it is opinionated, and the opinions are one engineer's rather than neutral practice. Adopting the pack adopts them.

---

## "So I'm not in control any more?"

You are, and in a strong sense. Access to the diff was never the problem; knowing where to look is.

- **Nothing is decided silently.** Every default is printed in the landing report, in the product's words, marked tweakable: *"on a phone this gallery stacks into one column."*
- **Told and asked are different.** Standard choices are told and the lane keeps moving; only what the documents genuinely leave open reaches you as a question.
- **Undo is one commit.** The change lands with its spec, matrix, and architecture together.
- **It can't run away.** The gates go red and stop the push.

Most tools give you control by asking fourteen questions. That is work wearing the costume of control.

---

## What it missed

Two projects run under this in production, and both caught the method out. A dead-end lens ran on the right surface and still missed a one-way door, because it checked states within a surface while nothing walked the round trip between two — the method's own fault, absorbed as a new invariant. A test guarded that near-silent audio stems are dropped from a view and stayed green for a month while the spec's actual requirement, that those stems stay *visible and named*, went unrendered. And a scroll that satisfies its motion contract exactly still feels cheap, which no rubric will ever catch honestly.

> **A spec owns what a project can write down and test. Feel belongs to the owner's eye.**

The full accounts, including the reviews that missed something and said so, live in the prover records: [`docs/prover/`](docs/prover/).

---

## The skills

`live-spec-base` the shared rulebook · `build-pipeline` sequences a change end to end · `spec-author` writes the living spec · [`product-prover`](https://github.com/happysasha18/product-prover) reviews it · `design-reviewer` asks whether the design itself is right once the spec holds together · `test-author` derives the matrix and the tests · `communicator` shows work and asks answerable questions · `feedback-intake` routes what you hand back · `feedback-collector` sends upstream notes with your consent · `publish` gates anything leaving the machine.

Map of everything: [`OVERVIEW.md`](OVERVIEW.md) · [pipeline](docs/pipeline.md) · [adoption](docs/adoption.md)

---

## Who it's for, and the limits

For people who can already build software, know what discipline costs, and now build with agents that are fast and untrustworthy. The pack is the wrong tool for a first project: it hands you a spec, an architecture document, a test matrix, and a pre-push hook, which is the right shape for the problem and too much for someone who has never shipped.

Two projects, one author, no outside adopters yet. The judgment loop is one model reviewing its own work; only the mechanical gates are genuinely independent, which is exactly why they are scripts. The version moves fast and the rules will sharpen under you, and the gates stabilize first, because those carry red-proofs.

Prior art is credited in full, including what was borrowed and from whom: [survey](docs/prior-art-frameworks.md) · [originality audit](docs/research/2026-07-10-originality-audit.md) · [comparative reviews](docs/research/2026-07-06-bmad-kiro-livespec-comparison.md), briefed to criticize all three subjects. [Superpowers](https://github.com/obra/superpowers) is ahead of anything here on execution discipline, and its stars are earned. If you know prior art we missed, open an issue.

**Known issues.** Internal vocabulary still leaks into human-facing text; a register lint blocks known leaks in shown artifacts, and chat stays the weakest surface. The spec's Formal index carries recorded style debt, counted and dated in the queue. The settings card is young and has run on one project. All three are tracked and reviewed at every push.

---

[MIT](LICENSE) © Alexander Abramovich, 2026 · [`VERSION`](VERSION) · [what lives where](OVERVIEW.md)
