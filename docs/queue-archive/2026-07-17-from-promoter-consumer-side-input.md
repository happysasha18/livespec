# Wish: consumer-side input to multi-agent communication (from the promoter engine window)

From: the promoter product-dev window (`~/promoter`), 2026-07-17, dropped per the one-wish-file inbox law.
This complements the owner wish `2026-07-17-from-owner-multi-agent-communication.md` — it answers that
wish's recon questions from the consumer side and hands up a proven adversarial pass.

## Why this exists

The owner reframed promoter queue item 7 (an inter-agent comms protocol) as live-spec infrastructure
(his word, 2026-07-17: live-spec thinks it through, agent-to-agent communication is infrastructure, send
it all to the inbox, it is not the promoter's to bake). Before that reframe this window had authored and
adversarially proven a promoter-side draft of the same protocol. The design belongs to live-spec now; its
findings come up here so they are not re-derived.

## Answers to the owner wish's recon questions (authoritative from this window)

**R2 — where the promoter (consumer) repo stands.** The promoter repo carries the vendored pack gates as
of pack 2.4.0 (`scripts/ratchet-manifest.json` pinned to 2.4.0; the register / redundancy / freeze gates
plus a ratchet-lock test are installed and green; suite 26/26 via pytest). Structurally the consumer side
lacks nothing for pinning a data contract — the gates are in and green, so it can pin a contract version
and grow a freshness and compatibility test on top of what it already has. The unfinished pre-push wiring
the older adoption notes mention is the public-flip gate (promoter queue item 1), a separate concern from
consumer-contract readiness.

**R3 — who owns the feed generator.** The promoter is the consumer, and it holds no claim on the
generator seam. On the producer side the general-case answer is right — the engine owns the generator so
every instance inherits it. The promoter only pins a contract version and reads the feed read-only.

## A proven adversarial pass, handed up (sharpens the owner wish's four stories)

This window ran the pack's spec-author and product-prover on a promoter-side draft (a fresh opus
adversary, ten findings). The draft as a whole is superseded by the owner wish's stronger feed-contract
model; four of its findings map onto that wish's stories and may sharpen them:

- **The credential boundary dissolves under the feed model — worth stating that it is meant to.** The
  owner wish has the producer publish a versioned feed the consumer reads read-only, so no credential
  crosses the boundary. The promoter draft reached the same safety the harder way (a D-2-style per-source
  read-only key grant with a home and a revocation act at the key-holder). If the feed is the whole data
  path, that key machinery is unnecessary; the contract can say outright that raw credentials never cross
  and the published feed is the only data path.
- **Owner-versus-agent provenance (sharpens story 3, the experiment lifecycle).** The prover flagged that
  a peer agent is not the owner, so an agent-initiated proposal (A/B, coupon, funnel change) must stay a
  proposal until the owner ratifies it, and it must never land in a home that records owner word. The
  owner wish already keeps his gates intact; naming the provenance split — only owner-initiated messages
  carry owner authority — closes the hole at the protocol level.
- **A request needs a terminal outcome or it stalls (sharpens stories 3–4).** A materials or experiment
  ask needs a terminal state — delivered, declined, or escalated past a stated need-by — or the consumer
  waits forever on a dormant producer window. The owner wish's freshness watcher already covers the
  data-feed side; the same "reaches a terminal state or escalates to the owner" property is worth binding
  to the experiment lifecycle's request side, so a proposal that the producer never acts on surfaces to
  the owner rather than expiring in silence.
- **Message identity on the wish door.** Two same-day same-slug wishes collide on one filename; the
  pack's `-2` / `-3` collision law (base rule 18) already handles the name. Worth confirming it covers
  agent-to-agent wishes, and that a message carries a stable identifier its reply can name after the
  original file is swept out of the inbox.

## Who threw it

The promoter product-dev window (`~/promoter`), on the owner's word to hand all of this to live-spec. The
full promoter-side draft and its prover record stay in the promoter's history (superseded, not carried
across); this note is the distilled consumer-side residue.
