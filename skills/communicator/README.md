# communicator

A small skill for one thing: **showing work to a human and asking for decisions they can actually make.**

Not about code. It's about the exchange. The same failure keeps happening in agent work — describing in words
what should be shown with the eyes, and asking a person to decide in units they don't think in (pixels, dB,
model weights, internal ids). `communicator` is the antidote, distilled into seven cheap-to-follow rules.

It's the presentation member of a four-skill pack:

| skill | job |
|---|---|
| [spec-author](https://github.com/happysasha18/spec-author) | write the spec |
| [product-prover](https://github.com/happysasha18/product-prover) | review the spec |
| build-pipeline | ship the change by the method |
| **communicator** | **make the human-facing exchange land** |

## When it fires

Every time you (a) need the human to **decide** something — especially anything visual or textual, (b) report a
**result or progress**, or (c) **name a problem**. Rule of thumb: if your next sentence is a question the person
can't answer without seeing something, stop and show it.

## The seven rules (short)

1. **Show, don't describe** — and when unsure, ask by showing (a mockup), never in raw units or a bare term.
2. Name a problem → make it **actionable in the same breath, with your recommended pick**.
3. **Show proactively, for approval** — the moment there's a real was → became, don't wait to be asked.
4. Don't fragment attention — **batch, show once, in one window** (was → became → why → before/after).
5. Put the artifact **where they'll actually see it** (browser or inline) — real data, never a path.
6. **Plain language, in the product's own words** — use-cases over mechanism, one name per thing, the spec's vocabulary.
7. **Honest about the result** — small is not a win; and don't escalate what you can decide yourself.

Full text, the fork-presentation template, anti-patterns, and worked examples are in [`SKILL.md`](./SKILL.md).

## Install

Drop the folder into your skills directory (e.g. `~/.claude/skills/communicator/`). The skill is a single
`SKILL.md`; there is no code to build.

## License

MIT.
