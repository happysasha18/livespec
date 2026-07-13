# Wish: three method gaps a real-visitor session exposed — edge-condition completeness, a legibility floor, severity-labelled findings

**From:** the tlvphotos window, 2026-07-13, carrying what Alexander saw when a first real Hebrew-speaking
visitor walked the live exhibition on a phone. His explicit ask this time: the timing-window one the
prover should have caught — send it to live-spec, and the siblings of its family with it.

Three method gaps sit here. A fourth thing he named turned out to be a fresh instance of an
already-filed wish, so it is recorded below as confirmation, not as a new wish.

---

## Gap 1 — the prover must demand both ends of an edge condition before a spec passes

Two live examples, one root.

**A time-triggered line with no window.** The door carries a returning-visitor line and a farewell line
(EX-RETURN / INV-78, `renderDoor()` at `exhibition.js:963–979`). The spec said, in effect, "on a return
show the welcome-back line; on leaving show the farewell." It stopped there. The code does exactly that
and nothing more: the welcome-back fires on *any* cold arrival once the been-here flag is set, with no
upper bound — a visitor who last came months ago is greeted as if they just stepped out; the farewell
fires on *every* exit, with no lower bound — the very first exit and a two-second reload both trigger it.
Alexander's own reading names the missing window from both ends: too soon should stay silent (a quick
reload is not a return), and too late should reset to a first-time welcome (a long-gone visitor is new
again). The spec sentence "show welcome-back on return" is incomplete until it bounds "return" at both
ends. A retention-timing proposal that adds the lower bound already sits mocked in the project
(`gallery/retention-timing-mock.html`); the upper bound is the piece even that mock missed, which is the
tell — the omission is systemic, not a one-off oversight.

**The general shape.** Whenever a spec introduces a transition gated on a quantity that runs on a line —
elapsed time, a count, a distance, a size — the prover should refuse it until both ends of the live range
are named: what happens below the low end and above the high end. "On return", "after a while", "once
there are several", "when it gets large" each hide an unbounded interval. This is a completeness check the
prover can run mechanically: find every threshold-gated transition, assert each names its behaviour on
both sides.

**A second live instance of the same gap — asynchronous generation with no stated in-between.** Each
work's told narrative is fetched after the picture is already on the wall (EX-STORY-LINE:
`askPortion()` posts `/api/story` at `exhibition.js:1335–1356`; `tellStory()` fires it at the hang,
`:2070`, un-awaited). `fillTold()` at `:1312` paints an empty, silent slot when the line has not arrived
yet. Pictures carry a loading placeholder (the plate/skeleton ladder, EX-LOAD, `:996`, `:1996`); the
story line carries none. A visitor who reads faster than the round-trip — exactly what Alexander did —
meets a blank where a sentence belongs. The architecture either never stated that the narrative loads
asynchronously, or stated it without naming what the surface shows in the interval before it lands. Same
root as the timing window: a condition (generation in flight) whose in-between state was left unspecified,
so it rendered as nothing. The prover check that covers it: for every asynchronously produced piece of
content, require the spec to name the three states — pending, arrived, failed — and require a visible
pending state wherever the content has a reserved place on screen.

---

## Gap 2 — a legibility floor in the design review and in the pre-show gate

The Hebrew door text read faint and small on Alexander's screen, hard to make out. The measurements bear
it out: the ask line under the door is `--faint` (`#6b665f`) at 11px (`exhibition.css:78–79`), which is
about 3.3:1 against the near-black ground (`#0c0b0a`) — under the 4.5:1 that normal text needs to stay
legible. The credit link is 9px (`:400`); several chrome labels sit at 9–11px in `--faint`/`--muted-2`.
The same softness shows up in the HTML files this window hands Alexander for review: pretty, and a shade
too low in contrast and too small to read comfortably.

The register lint already guards the *words* a surface shows (`scripts/preshow-register-lint.py`). Nothing
guards whether those words can be *read*. The wish: the design-review pass, and the pre-show gate for
anything put in front of a human, should carry a legibility floor — a minimum contrast ratio for text
against its background and a minimum size for body and caption text — and flag any shown text that falls
under it. For product surfaces this reads the computed colours and sizes; for a review artifact it reads
the same from the file about to be opened. It belongs next to the register check because it guards the
same moment: the instant text meets a human's eye.

---

## Gap 3 — the prover should label a finding as a defect or a recommendation

Alexander asked this one straight: when the prover reports, can it say which findings are defects and
which are recommendations? The copy-protection unevenness below is a good test — is a missing guard on the
door a bug, or a suggestion toward uniformity? Today a prover walk returns findings in one undifferentiated
list, which leaves the human to sort severity by hand. The wish: each finding carries a kind — a defect
(a stated invariant is violated, a claim the spec makes is false) as against a recommendation (nothing
stated is broken, and a consistency or quality improvement is on offer). The kind changes what the human
does with it: a defect blocks, a recommendation queues for a taste call. A prover that already reasons in
invariants has the material to tell the two apart — a finding tied to a broken invariant is a defect; a
finding with no invariant behind it, only a "these siblings should match" or "this could read better", is
a recommendation.

---

## Recorded as confirmation, not a new wish — cross-surface policy uniformity strikes again

The room's hung works refuse right-click, drag, and long-press save (EX-PROTECT / INV-49): `onGrab`
matches `.exh-frame img.work` and is bound to the stage (`exhibition.js:1659–1674`), and the works carry
the guarding CSS (`exhibition.css:175–177`). The door's face images carry none of it. The door is built
onto `document.body`, not inside `#ex-stage` (`:899, :909`), so the stage-scoped listeners never fire for
it; the door image selector `.exd-window img` (`exhibition.css:105–110`) has no `user-select`, no
`-webkit-user-drag`, no `-webkit-touch-callout`. The entry face can be saved freely; the gallery behind it
cannot. This is precisely the **cross-surface policy uniformity** gap already filed from this project (a
policy true on one surface must hold on its siblings) — a second live instance, which is worth recording
because a recurring class earns its place in the method. No new wish for it; the product-side fix is being
built in tlvphotos and the uniformity lens, once in the prover, would have asked about the door before a
visitor found it open.

---

## Why these belong in the method, not only in this project

Every project the pack touches will grow time-gated behaviour, asynchronously produced content, text a
human must read, and prover reports a human must triage. An unbounded threshold, a blank where late
content belongs, faint small text, and an unsorted findings list are structural and recurring, and each
slipped past a green suite and a surface-by-surface prover walk. They ask for capabilities the prover and
the review method do not yet have: to demand both ends of every live range, to demand a pending state for
every async slot, to read legibility at the moment text is shown, and to label each finding by whether it
breaks something stated.

## Provenance
The tlvphotos window, 2026-07-13, from Alexander's first-real-Hebrew-visitor session on a phone. Filed as
wishes, not applied to the pack — this window does not write the pack tree. The product-side fixes (the
timing window, a pending state for the story line, Hebrew string coverage and a mirrored layout, the
door's copy guard, the contrast lift) are being built in tlvphotos and reported there.
