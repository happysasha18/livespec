# A node's fitness is re-answered as it grows — the design consult

**Date:** 2026-07-17 · **Asked by:** the owner · **Answered by:** a Fable seat, on his word (the pack's
economy rung holds Fable for adversarial passes and for a pass he names; he named this one) ·
**Queue row:** ROADMAP 390 · **Status:** design accepted, implementation queued.

## The question as he asked it

He had been reading exhibition-engine and noticed himself that one of its files is enormous and wants
splitting. His words, compressed: the system should catch this itself — the prover should have caught
it, or the design reviewer, or something in the pipeline; when a component grows, it should at minimum
PROPOSE some modularization where that is possible. He asked for the root fix and ruled the particular
case out of scope: exhibition-engine's file is the evidence, and its split is that project's own work.

## The grounding fact, measured

`engine/assets/exhibition.js` is 4017 lines carrying roughly 45 comment-fenced sections, each anchored
to its own spec code (the quiz, the zoom, the sound, the translations, the series, the door, the
gallery). The decisive fact sits in exhibition-engine's own ARCHITECTURE.md at rows 36-40: the node
table already declares **five separate nodes** — door and gallery walk · zoom and its gracious
deterrent · story and series · quiz · chrome and compose — and every one of the five pins into that one
file.

The map was honest. It said five-nodes-one-file in plain sight, at the exact grain the reader needed.
No check's sentence ever turned that into a question.

A second fact from the same document: its budget table records the bundle-size budget as "none wired; a
budget with no watcher," which INV-41 already ranks a derivation defect. The existing net had a thread
on this file and the thread went unpulled.

## The hole: birth has a law, growth has none

The three-question fitness test [INV-122] governs a node at its **birth**: can it be tested alone · does
a real second place need it · can it and its neighbour be worked in parallel without queuing on shared
files. Three yes answers make the node right.

A node born correctly and then grown carries a standing yes that nobody re-reads. It passes every
existing check forever, because every existing check runs at birth or reads the map's internal
consistency. That asymmetry is the hole, and it is what let this file grow in the open.

## The law

**A node's fitness is re-answered as it grows, and node co-residence in one file is the counted signal.**
Each node re-answers the three questions on its pins as they stand today, at every architecture
re-prove. Two nodes whose pins share one file answer the parallel-work question no by construction:
their edits queue on the shared file, and neither one's tests bind its node's code at its own grain. So
co-residence is the mechanical face of a failed growth answer. A no found by the re-ask demands what the
birth gate demands — a named plan (a split row in the queue) or a decided sentence stating why the
co-residence stands [INV-59]. A split moves only through the architecture step and its re-prove
[INV-37, INV-113].

## The measured thing, and the proxies rejected

**Nodes-per-file, read from the architecture doc's own pin column.** It is definitional rather than
statistical: INV-122's third question fails for every node pair sharing a file, so the count states how
many fitness answers are currently no. It costs one grep over a structured markdown column. It stays
current on machinery that already runs — every landing refreshes pins, `check-pin-drift.sh` holds them
honest, and the every-fact-owned-once backstop forces new spec facts into the table. On the worked
instance the count reads five, which is exactly the split the owner wanted proposed.

Rejected, each with its reason:

- **Raw line or byte count.** A 4000-line file owning one responsibility is healthy; a 400-line file
  owning five nodes is the defect. For modularity this is the vanity metric INV-41 warns against.
  (Bundle bytes remains a real product performance budget with its own watcher — a separate law, and
  that host's budget table currently states it with no watcher at all.)
- **Responsibilities counted fresh.** The node table already declares them, so judging them again
  outside the table measures the reviewer.
- **Git churn by concern.** A real signal the pack already owns as the footprint read [INV-128] and
  `crosscut_counter.py`; it answers a different question — a boundary in the wrong place — and needs
  history plus window tuning.
- **Fan-in/fan-out and cohesion metrics.** Language-specific tooling outside the stdlib gate shape, and
  the numbers are gameable.
- **Anchors-per-node.** It carries no honest universal number: the pack's own spec-author node healthily
  owns twenty-plus anchors. Per INV-41's prior it is said by name instead — the prover's re-ask reads
  the node's one-line responsibility sentence, and a node whose sentence can only be written as an
  and-chain is the finding, with no number attached.

## The nets [INV-150] and their homes

Three existing homes grow. No new home is born, and no new skill: a dedicated skill fails INV-122's
second question, since no second place needs it beyond the lens set that already reviews architecture.

- **The mechanical gate** — a counter in `guardrails/`, sibling of `crosscut_counter.py`, on the
  guardrails node. It reads the architecture's node table, groups the pin column by file, and counts
  nodes per file. The count is a ratcheted budget [INV-98, INV-172]: seeded at the tree's current count
  so the gate lands green, red on any push that grows it, the standing debt flagged to the MINOR audit
  as split candidates. It differs from the crosscut counter deliberately: that count is advisory because
  its input is prose-parsed and a boundary move needs judgment; this count is exact, and the ratchet
  reds only an increase, which is deterministic and safe to block. It fires **on every push** — the
  INV-164 lesson transfers whole, since this is a quality a machine can verify by reading one table, and
  holding it at milestone cadence is how the spec once bloated.
- **The prover's judgment station** — the architecture lens grows a check: every node re-answers the
  three questions on current pins at every architecture re-prove. The one-no case takes the same
  flag-for-an-answer path the speculative-node flag already takes.
- **The design review's recommendation** — when the counter flags, or the re-ask finds a no whose split
  lines are open taste, the design review carries the proposal in its two-objects shape [INV-142]. This
  answers his "at minimum propose": the proposal has an obliged reader, since the MINOR audit reads the
  flags and the ratchet mechanically stops the hole deepening while the proposal waits.

## The numbers

The pack proposes a flag at **two nodes per code file**, with the ratchet seeded at the host's current
count [INV-172], shrinking only. The host's word sets the threshold and the debt-burn pace at the first
budget landing [INV-41]. INV-135's declared layers say what counts as a code file, so a prose project
needs no kind exception: its nodes each own their own file and the counter flags nothing.

## What a finding looks like

> **Finding (recommendation, confident).** `engine/assets/exhibition.js` (4017 lines) hosts the pins of
> five declared nodes (ARCHITECTURE.md rows 36-40). Two objects: node "The quiz" (its row's sentence:
> the public four-option chip, the card flow, the funnel stage; pins `:64`, `:2497`) and node "The zoom
> / gracious deterrent" (its row's sentence: pinch-to-inspect and the gift ceremony; pins `:1910`,
> `:2273`). The architecture already declares these two as separate responsibilities with disjoint
> spec-fact sets; their edits queue on one file, and neither one's tests can bind its node's code alone,
> so the parallel-work question [INV-122 q3] answers no for the pair, and for every other pair among the
> five. Recommended default: five files matching the five declared rows, the split routed through the
> architecture step and re-proven [INV-37, INV-113]; the bake-to-client seam (`exhibition_data.json` +
> `config.json`) is untouched by any split line. The one taste fork the human owns: the doc records "no
> build/minify step — source bytes are served bytes" as resolved-as-shipped, so a split either ships
> five script tags or introduces a concat step; the recommendation is the concat step, and the choice is
> his.

Both objects are the node table's own rows plus the shared file. The evidence is already in the tree,
at zero fresh instrumentation.

## What this design does not do

- No raw line-count gate. For modularity it reds honest files and greens the defect, and a spurious red
  trains bypass.
- The gate never demands a split inline. A boundary moves only through the architecture step and its
  re-prove, so the gate blocks the debt from growing and the split lands as its own row.
- No new skill, for the reason stated above.
- No cohesion-metric tooling: it breaks the stdlib gate shape and its numbers are gameable.
- The bundle-byte budget stays out of this law. It is a real performance budget with its own missing
  watcher, and it is that host's own one-line fix.

## The strongest objection, and its answer

**The counter trusts the map.** An architecture that lazily declares one coarse node ("the client") for
the whole file scores clean, so the gate is evadable by under-declaring, and the measure inherits the
map's honesty.

The answer has three parts. The observed failure was the opposite case: the map was honest and precise,
five nodes declared, and the question was never asked — so the cheap counter closes exactly the miss
that happened. The coarse map is already watched by standing law: every spec fact must be owned by
exactly one node, read at every re-prove, so new facts keep landing in the table, and the growth re-ask
reads the coarse node's one-line responsibility sentence, where an and-chained sentence is a finding
pinned to a stated sentence. And evading this gate requires writing a false shape into a document the
prover walks on every re-prove and the crosscut counter reads on every footprint, which converts a
silent drift into an actively maintained lie — the defect class the method's other nets exist to catch.

## Implementation surface

All in existing homes: one spec law (a sibling paragraph beside INV-122, its three nets named per
INV-150), one guardrail script beside `crosscut_counter.py` wired into `pre-push` with cap seeding per
INV-172, one added check in the prover's architecture lens, one paragraph in the design reviewer's lens
list for the split-proposal shape, and the pack's own node table gains the anchor.
