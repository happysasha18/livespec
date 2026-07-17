# Wish: who owns a cross-cutting concern, and when a new agent is warranted (owner's word 2026-07-17 ~13:27)

From: the promoter product-dev window (`~/promoter`), relaying the owner's word, dropped per the
one-wish-file inbox law. This is a separate item from the consumer-side note dropped earlier today.

## The architectural problem

As the project family grows (the site, the promoter, track-coach, the packs), concerns keep arising that
no single existing agent clearly owns; they cut across agents and projects. Two hit today:

- **Inter-agent communication** (the promoter needs the site's data to build campaigns): resolved this
  morning by handing it to live-spec as infrastructure.
- **Cross-project analytics** (a measurement tag across the GitHub projects, one place to see it all):
  the same shape — no obvious owner, and the owner named it explicitly as outside the website engine.

Each time, this is resolved ad-hoc, one conversation at a time. The owner asks live-spec to own the
meta-question so it stops being re-suffered per case.

## What the owner expects from live-spec

- **Decide when a new agent is warranted, and on what grounds.** Give a stated way to tell whether a new
  concern earns its own agent, folds into an existing one, or is a skill. Whether a cross-cutting concern
  becomes a new agent, or someone or something else, is live-spec's call to make.
- **Map responsibility by auditing what exists.** Live-spec may audit the current agents and skills and
  their transcripts to understand who is responsible for what, and build the ownership map from that
  evidence.
- **Overlapping responsibility is acceptable.** Two agents' scopes may overlap, and that is fine; no
  forced disjointness is needed.
- **The default router.** An agent that does not know who to turn to goes to live-spec. Live-spec is the
  fallback owner for any concern that arrives unrouted.

## The hard constraint (the owner's, stated plainly)

Work must keep moving while ownership is being re-architected. Refactoring the ownership map is always
available after the fact, so an agent that meets an unowned concern does the reasonable thing now in
whatever tree can hold it, marks it provisional, and live-spec re-homes it later. The re-home is cheap and
retroactive; a stall while everything is redone in live-spec is the single outcome to avoid.

## Relation to what is already in this inbox

This lifts the multi-agent-communication wish (`2026-07-17-from-owner-multi-agent-communication.md`) one
level up: that wish answers how two known agents talk; this one answers who owns a concern and when a new
agent is born. The cross-project analytics question is a fresh worked instance of the same gap.

## Who threw it

The promoter product-dev window, relaying the owner's word (2026-07-17 ~13:27), on his instruction to
describe the architectural problem and hand the ownership and agent-creation question to live-spec.
