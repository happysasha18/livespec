# Lens & rule origins

The provenance home for the pack's rules and prover lenses: the date and the motivating case that
gave each rule its shape. The spec and the skill bodies state the mechanism in plain present tense;
the birth-story lives here, keyed by the rule's code, so it stays retrievable (and reusable for a
README or an article) without weighing down the normative body. This is the lens/rule analogue of
`docs/norms/`, which homes the provenance of an approved visual artifact the same way.

Where a fuller account already lives in a dated prover record under `docs/prover/`, the entry carries
the short story and points at the record rather than duplicating it. The running chronological
narrative stays in `JOURNAL.md`; this file is the code-keyed lookup.

Format: `### CODE — short name    (date)` then the story.

---

### INV-28 — internal handles trail, never lead    (2026-07-08)
A report to the owner opened with "rows 166 and 148" — bookkeeping numbers as the first thing he read,
where the reader's outcome should lead and every handle only trail. The pre-show lint grew to flag a
human-facing line that opens with an internal handle.

### INV-41 — a performance budget is a measurable sentence    (2026-07-06)
A gallery whose first picture loaded long with nothing measuring it — "fast enough" as the only
standard. The facet now ends as a measurable budget ("the first image appears within 2 s on a cold
visit") paired with an instrumentation home and an acceptance assertion.

### INV-50 — a conditionally-entered face owes a re-entry path    (from a real door)
On a real door, six seams were found and the one-way face was missed: a face entered only under a
condition (first visit, empty state, a one-time banner) with no deliberate path back. The dead-end
lens tests states for exits; this lens tests faces for re-entry over the visit's lifetime.

### INV-56 — a known, owned problem is serviced in batch, never per-instance    (2026-07-07)
A clock drift was hand-ceremonied ten times in one night while its owner row sat open — ten
interruptions for one known, owned problem. A defect with a named mechanical owner is now fixed
silently in batch where the fence catches it, with one ledger append at the session's end.

### INV-76 — a background worker outlives a memory wipe; the resume protocol proves it dead or alive    (2026-07-09 · 2026-07-12)
Born of a real two-writer race (2026-07-09), and of the prover finding that a compute-bound worker —
writing no file for minutes and slow to service the probe — read dead on both original checks though
it was live (2026-07-12). The third check (a heartbeat on the checkpoint file) was added so a
mid-computation worker is not declared dead.

### INV-102 — a test's expected value derives independently of the code    (2026-07-10)
Row 220's audit: green suites missed real walk bugs because the tests recomputed the code's own
formula and asserted the result as the expected value — a mirror that only ever proves the code
equals itself.

### INV-104 — a fix touching a spec-backed literal owes its docs and test the same session    (2026-07-10)
The row 220 audit: one-line fixes touching spec-backed literals (a version string, a pinned count, a
named vocabulary, a promised wording) shipped without same-session doc sync. The size of the diff had
been treated as an exemption; it grants none.

### INV-105 — one canonical state directory named `.live-spec`    (2026-07-10)
The audit's ghost `.livespec` directory, found standing beside the real `.live-spec` with a different
profile — two directories each claiming to be the host's records.

### INV-106 — the push walk reads the remote gate's verdict    (2026-07-10 ~11:00)
The owner's word: why does a GitHub email tell him a deploy failed that the session should have caught
and fixed itself? A red remote-gate verdict is now the pushing session's own immediate bug, fixed and
re-pushed the same session, so he never meets the red first in his mailbox.

### INV-107 — a landing closes the checkpoints it shipped    (2026-07-10)
The audit: two engine checkpoints still read "not started" after everything in them had shipped, so a
resuming session would have redone finished work.

### INV-109 — a rewrite that removes substance accounts for it in the landing report    (2026-07-10)
The night docs pass compressed the README's account of why live-spec stands beside BMAD, Kiro, and
spec-kit down to a single pointer line; the section was restored the same session on the owner's word.
A rewrite that drops a section, an argument, a rationale, or a worked example now lists every removal.

### INV-110 — the catch-up routing keys on a version delta, not a wording    (2026-07-10)
The track-coach audit: the catch-up walk fires only when the host's recorded package version is behind
the current VERSION; a docs restructure carrying no version delta is the host's own queue row,
whatever wording the ask used.

### INV-111 — a same-version docs-layout pass rides one sanctioned vehicle    (2026-07-10)
The track-coach s63 audited pass: a host restructuring its own documents with no package-version delta
now runs one named shape — decisions locked in a checkpoint first, a clean pushed base, content proven
by a word-token AND a punctuation multiset check, the full suite green, one journal chapter.

### INV-112 — the inbox has a remote arm    (2026-07-10)
The owner thinking the cloud seat through mid-session: the day's inbox law assumed a shared
filesystem, and a live routine alert was the first seat to hit the gap. A remote seat reaches a repo
only through git, depositing one new file in `inbox/` under a per-repo grant.

### INV-113 — a deliberate redesign re-shapes the document, not only its pins    (2026-07-11)
The tlvphotos second-finger redesign: a UI-layer rethink was ordered and the pack forced only a pins
update, not a re-shaping — so the old document shape lied while fresh pins sat on it.

### INV-114 — a restructure or migration merge gate judges the delta    (2026-07-12)
A strictly-improving restructure merge was parked on the old side's pre-existing clarity debts because
a spoken «prover finds nothing both sides» had been over-sharpened into «any finding parks the merge».
Corrected live: the gate blocks only on the delta, and pre-existing findings equal on both sides route
to queue rows.

### INV-115 — the full pass compacts every living document, meaning preserved    (2026-07-12)
The owner's compaction definition: compact means no redundant information — a fact lives once, in one
home, with a pointer from everywhere else — never the cutting of anything whose removal would change
meaning or a reader's understanding.

### INV-116 — the full pass proves the architecture beside the spec    (2026-07-12)
The owner's word and this session's for-fun prover run against the spec: every milestone and push gate
now runs the prover over `ARCHITECTURE.md` as well, so the design-level seams meet the same review.

### INV-117 — every session carries a stable identity minted at its start    (2026-07-12)
The for-fun prover run's finding F1: the parallel-lanes pen tie-break needed a stable per-session
identity to order a genuine concurrent claim with no git ancestry, so exactly one session backs off.

### INV-118 — shipped product docs state each requirement impersonally    (2026-07-12)
Track-coach's shipped-artifact audit found a shipped spec carrying many owner attributions accumulated
over months. The load-bearing reason stays and the personal attribution drops; candid attribution
lives only in the local-only diaries. The pack retired its own former self-exemption in the same pass.

### INV-119 — the engine's spec crosses the boundary clean    (2026-07-12)
The exhibition-engine public-publish pass: the spec carried a "Deltas from the <instance> reference
implementation" heading citing private-instance commit hashes, and named a generic mechanism by the
instance's own locale UI label across eight clauses. The engine now records its own public commits and
carries neutral internal names.

### INV-120 — a shipped artifact carries no Cyrillic outside a deliberate user-language string, and no owner name in a requirement    (2026-07-12)
Track-coach's audit: the publish gate grew a machine (`guardrails/check-shipped-language.sh`) reporting
each offence as file:line, with candid process-notes and attribution kept to the local-only diaries.

### INV-121 — a proven artifact settles a fork before the human hears it    (2026-07-12)
A track-coach session offered the owner two options while its `ARCHITECTURE.md` layer split already
determined the answer. His word: read the architecture, derive the requirement, stop handing forks.

### INV-122 — every new or carved node passes a three-question fitness test at its birth    (2026-07-12)
The six-principle design wish, principle 7: can it be tested alone, does a real second place need it,
can it and its neighbour be worked in parallel without queuing on shared files — three yes make the
node right.

### INV-123 — compaction is a scheduled station for code as well as docs    (2026-07-12)
The six-principle design wish, principles 4–6: beyond the doc-compaction pass the station widens to
code — duplicate logic merges, dead weight leaves with its listing, a ripened abstraction is extracted
only through the three-question fitness gate.

### INV-124 — a confirmed bug drives a class hunt before it closes    (2026-07-12)
The exhibition's pinch-zoom bug: naming the class abstractly — a browser zoom desyncing the scroll
animator, guarded on only some gestures — turned one report into five live siblings, all real and all
fixed together, with the spec updated to match. The owner's standing word made the class hunt the bug
door's close condition.

### INV-125 — a cross-surface policy is stated at the surface-class level    (2026-07-12)
Tlvphotos's pinch-zoom policy was shipped for the walk alone while the door, the series side-room, and
the polaroid table kept the browser default. Every test was green because the suite asserted only the
one surface the clause named; the gap was found only when the owner pinched each surface by hand on a
real phone. See also `docs/prover/2026-07-13-prover-overlap-lens.md` (the sibling family).

### INV-126 — both directions of a paired state change get the same craft    (2026-07-12)
Tlvphotos's polaroid side-room was revealed under a soft black veil in one breath and closed on a hard
cut with no transition at all — an asymmetry nobody decided on purpose, found only by the owner feeling
it on a real phone.

### INV-136 — interactive controls from different layers do not share one screen region    (2026-07-13)
A floating player was left pressable over a zoom overlay's close, found by hand on a real phone — two
interactive controls from different layers sharing one region. Full record:
`docs/prover/2026-07-13-prover-overlap-lens.md`.

### INV-137 — the orchestrator reads to decide, not to discover    (2026-07-13)
Two windows independently filled their own context with reads a worker should have done; the rule was
stated then only as a buried clause no seat enforced. The landing report's delegation accounting now
names the reads dispatched. Full record: `docs/prover/2026-07-13-gap0-read-discipline.md`.

### INV-138 — a gated behaviour names every side of its gate    (2026-07-13)
Tlvphotos's returning-visitor line greeted a months-gone visitor as if they had just stepped out (no
upper bound) and fired its farewell on every reload (no lower bound); its story line painted an empty
silent slot while the narrative was still in flight. All found when a real visitor read faster than the
round-trip on a phone. Full record: `docs/prover/2026-07-13-gap1-edge-completeness.md`.

### INV-139 — the frontend kind carries a legibility floor    (2026-07-13)
A first real visitor met faint 11-pixel Hebrew text at about 3.3 to 1 on a phone, under the 4.5 to 1 a
reader needs. Full record: `docs/prover/2026-07-13-gap2-legibility-floor.md`.

### INV-140 — the prover labels each finding a defect or a recommendation    (2026-07-13)
A real prover walk returned its findings in one undifferentiated list, leaving the human to sort defect
from recommendation by hand. Full record: `docs/prover/2026-07-13-gap3-finding-kind.md`.

---

## Test-craft lens origins (test-author)

Each is a testing trap a real bug taught, kept here so the trap stays vivid while the skill body states
only the rule.

### Conformance-row trap — a render inventing its own structure ships green    (2026-07-10)
The onboarding card's bounce: the first render invented its own row format, dropped three norm sections,
and shipped green. Matrix row M-211 is the first live instance of the conformance row this rule now
demands.

### Real-device-walk trap — the suite cannot see the phone    (a real week)
A momentum swipe flew through several works on a phone, and a backgrounded tab turned a 2.5 s failsafe
into a black screen — both past every green desktop run. Behaviour like this owes a real-device walk
row the suite can never turn green.

### Relative-geometry trap — an absolute-pixel assertion passes while drift grows    (a real bug)
Centering was computed by an absolute shift that differed from the screen size — every next image
landed further off-center, and every one-step test stayed green. A positioning fact now asserts
relative geometry at two or more viewport sizes and after N steps.

### Engine assumption-contract trap — a donor constant leaks into the generic engine    (a real bug)
The donor's digits-only id pattern stayed in the engine's validator and rejected the engine's own slug
ids — every story call failed while the donor-shaped suite stayed green. Every donor constant the
extraction finds now owes a works-without-it test against the content contract. (Also the origin of
spec-author's assumption-contract rule.)

---

## Communicator lens origins

### INV-94 — self-certification is never content    (2026-07-10)
The pack's own README certified itself twice in one day — a line praising its own honesty says nothing
the reader can use.

### INV-16 / INV-17 — exchanges converge; an answered question closes forever    (promoter case)
One escalating hour: a pile of similar questions had already been answered, yet the dialogue re-opened
them. An answered question now closes forever and is harvested into its row the same session.

---

## Guardrail origins

### Kill-list scanner — a killed phrase reappearing turns the suite red    (promoter, 2026-07-07)
A banned pattern returned into a campaign's most visible line after the ban had been "written on the
forehead"; only the executable scanner ended it. The list is the declared truth, the test re-walks it
every run.
