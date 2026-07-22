# Field report: the growable-doc bound is a catastrophe backstop, and nothing in the pack watches creep

**From:** the tlvphotos window, 2026-07-21 afternoon, after a reachability-parity movement.
**Kind:** defect in the method's compaction story, with the evidence from one host.

## The finding in one line

The document-bound gate (INV-234, gate z) is seeded so far above a document's real size that it cannot
fire for months, and no other gate measures growth at all — so the compaction station the pack calls a
per-push duty (INV-164) runs on attention alone, which the pack's own rule 30 names as a defect of the
method.

## The number that shows it

This host's `guardrails/doc-bounds.json` was seeded today, 2026-07-21. Its own recorded reason for the
spec's ceiling reads: **"378808 bytes today"**, and it sets `max_bytes` to 620000.

Measured a few hours later, the same day, the same file: **433855 bytes**. The document gained roughly
55 KB — about fifteen percent — between the ceiling being written and this report, and the gate reported
`OK` throughout, because 433855 sits at seventy percent of a ceiling seeded above a projected future size.

Line counts over the four days before that, one row per commit that touched the spec:

```
2026-07-17  3194 → 3431      2026-07-19  3469 → 3473
2026-07-18  3456              2026-07-20  3476 → 3489
2026-07-21  3611 → 3687
```

Every commit grows it. Across twenty commits touching the file, **not one shrinks it.** That is the shape
a per-push compaction station is supposed to prevent, and it is invisible to every gate in the chain.

## Why the gate cannot catch this, structurally

The seeding instruction in the vendored skeleton is explicit and is the cause:

> "Seed each ceiling ABOVE the doc's current size with rotation headroom so the gate never reds a tree
> that is already large."

That instruction is right for its own purpose — a gate that reds on adoption is a gate a host disables.
It makes the bound a backstop against catastrophe. It also means the bound can never speak to the thing
a reader actually feels, which is a document growing steadily past the size anyone will read.

## Two more holes beside it

1. **Warnings are ungated and therefore unread.** The style lint reports errors and warnings; only errors
   ride the debt cap. This host carries **991 warnings** on the spec and **425** on the architecture. A
   channel nobody counts is a channel that stops meaning anything, and it is where the readability
   signals live — the shouting caps, the second person, the register drift.

2. **The debt cap ratchets down only when a human chooses to ratchet it.** It forbids debt from growing
   and never asks for any reduction, so a host's debt freezes at whatever it was seeded at. This host sat
   at a seeded 89 style errors and 29 redundancy pairs since adoption; today's movement measured the real
   figures at exactly 89 and 29, so nothing had moved in either direction. A ratchet with no downward
   pressure is a freezer.

## What the pack might do with it

Offered as material for your own judgment rather than a prescription, since the fix is the pack's call:

- A **rate** reading beside the absolute bound. Bytes added per landing, or per week, against a declared
  budget. Creep is a first derivative and the current gate reads only the value.
- A **warning cap** in the same ratchet as the error cap, seeded at today's count so it never reds on
  adoption and can only fall.
- Give the compaction station a **number to hold**, whatever that number turns out to be. It is currently
  the only station in the pipeline whose output no gate can read, which is precisely the condition rule 30
  was written to forbid.
- Possibly: a bound that **tightens automatically after a rotation**, so rotating earns headroom once
  rather than permanently.

## The honest part of this report

The host noticed this size figure twice today and wrote it into a report both times as an observation,
and opened no row and sent no message either time. It took the owner asking "is this a live-spec bug, and
would you have sent it yourself?" for the finding to acquire an owner. The answer he got was no.

That is worth more to the pack than the size finding itself. A per-push station with no number does not
merely fail to run — it trains the seat to narrate the problem instead of routing it, because narrating
a number feels like having handled it. The routing law (INV-153, everything routes to the home whose
declared sentence governs it) held for every incoming request in that session and did not fire once for
an observation the seat produced itself. There may be a gap there: an outgoing finding has no intake.
