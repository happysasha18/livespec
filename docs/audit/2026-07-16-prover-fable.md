# Adversarial audit of product-prover — 2026-07-16 (Fable pass)

Artifact under audit: `skills/product-prover/SKILL.md` v1.1.4 (441 lines), read in full, against
PRODUCT_SPEC.md INV-165 (motion-parity lens) and INV-167 (entry-state lens) and the lens provenance
in `docs/lenses.md`. Mandate: break the prover, not bless it. Findings are ranked; each carries a
concrete failure scenario and a recommended fold. Nothing in the skill or spec was edited.

## The missed-case class

INV-165 and INV-167 are not two unrelated patches. Read together with the earlier post-hoc lenses
(INV-125 pinch-zoom, INV-126 side-room hard cut, INV-136 player over overlay, INV-138 returning-visitor
greeting — every one born from a bug the owner found by hand), they name one structural hole:

**The prover verifies the state graph's topology, not its payloads.** Its core questions are
existence-shaped — does a transition exist (undefined-path), does a state have an exit (dead-end),
does a re-entry path exist (entry symmetry), is a direction stated (paired-transition). What it never
systematically asks is what each node and edge *carries*: the initialization vector a state opens
with, the motion an edge plays, the residual internal variables a surface keeps between visits. Both
new lenses are payload patches — INV-165 patched one edge payload (exit motion), INV-167 patched one
node payload (re-entry position and reset-or-resume). The rest of the payload family is still open.

The deeper mechanism: in every one of these bugs, **the platform's default silently became the
behavior**. The DOM keeps a lane's scroll; the browser plays no exit animation unless one is coded;
audio keeps playing under a veil; focus falls to the document body. The spec was silent not because
the author skipped a question but because no decision moment ever occurred — the machine answered for
free. The prover's lenses are all keyed on something WRITTEN ("when a clause states…", "when a
surface declares…", "when the document provides clear evidence…"); a behavior supplied entirely by an
unwritten default gives no trigger to fire on. The nominal catch-all, the unwritten-seams lens
[INV-72], walks SITUATIONS (view, mode, viewport, co-present surfaces), not the sub-surface internal
degrees of freedom (scroll offset, playhead, focus, half-typed input, timer phase).

Missing lenses of this class — each named, with the bug it would catch and the spec-shaped question:

1. **Focus and selection across lifecycle boundaries.** Bug: an overlay closes by Escape and keyboard
   focus lands on `<body>`; a keyboard user is dumped to the top of the page. Question: for every
   overlay or mode close, which element holds focus after, and is it the invoking control?
2. **Uncommitted input across interruption.** Bug: a visitor types into a field, an interrupting
   transition fires (navigation, timeout, an overlay), and the draft is silently lost — or ghost-
   restored later into a changed context. Question: for every surface accepting incremental input,
   what happens to uncommitted input on each stated exit — kept, discarded, or committed?
3. **Playing media across covering and re-entry.** Bug: room audio keeps playing under the side-room
   veil because start/stop were keyed to enter/leave and covering is neither. Question: for every
   surface that plays or animates, what does each exit AND each covering do to playback — pause,
   continue, resume-at-position, restart? (INV-136 took the click-collision half of the overlay
   problem; the media-state half was never minted.)
4. **Navigation-level restoration.** Sibling of INV-167 one level up: the browser back button,
   history restore, an anchor jump. Bug: back lands mid-wall with the entry ceremony re-running, or
   at the top losing the visitor's place — whichever the platform picked. Question: for each
   navigable surface, what does back restore — position, state, or a fresh entry?
5. **Time-driven behavior across suspend.** Bug: a countdown or autoplay carousel is backgrounded;
   on foreground it has either frozen or jumped, undecided. Question: for every timer-driven
   behavior, what holds across a tab background or device sleep?
6. **Derived-display refresh cadence.** Bug: a count, preview, or ordering shown on one surface goes
   stale when another surface mutates the source; on return the visitor sees the old value.
   Question: for every displayed derivation, which events re-sample it — and is a stated rule's
   input frozen at entry or live? (See constructed bug C below.)
7. **Global-setting re-sampling at entry.** INV-167 scopes to the surface's OWN internal state; it
   does not ask which cross-cutting settings (theme, language, mute) a re-entered surface re-reads.
   Bug: toggle dark theme in settings, re-enter a room, get a stale-theme flash. Question: on every
   entry, which global settings are re-sampled versus baked at first render?

The parent fold that closes the class rather than the next instance: **a transition-payload lens** —
for every stated transition and every re-enterable state, enumerate the user-perceivable parameters
(motion, duration, landing position, focus, playback, pending input, timers, sampled globals) and
demand each be either stated or explicitly delegated to a named default. A parameter answered only by
the platform is the finding. Without this, the pack will keep minting INV-16x lenses one shipped bug
at a time — the provenance file already shows six iterations of exactly that loop.

## Ranked findings

### D1 — The prover checks graph topology, not payloads (the class above) — defect

Scenario: any of the seven bugs listed above; each walks Phases 1–4 clean because every state,
transition, and direction is STATED — only its payload is defaulted. The class already shipped twice
(INV-165's hard-cut exit, INV-167's stale lane scroll) after full prover passes.
Fold: add the transition-payload lens to 3e as a mandatory sweep (see D5), and fold members 1–7 as
its named parameter families. The lens fires on stated transitions, so it has a written trigger —
unlike the misses, which had none.

### D2 — FEATURE-FIT switches off the only station that can see a newborn undeclared kind — defect

The moment an undeclared same-kind grouping comes into existence is the intake of its SECOND member —
a feature delta. At exactly that moment: the cross-surface uniformity lens [INV-125] cannot fire (no
class is declared yet, and no kind-general sentence exists to recognize); and the design review — the
one pass built to find undeclared groupings [INV-141] — is defined to stand down at FEATURE-FIT
("FEATURE-FIT intake and the M-6 push-gate re-check draw none"). So the second sibling enters, ships,
and diverges; the divergence is only findable at the next FULL, i.e. after the bug is live. This is
the INV-125/INV-165 discovery channel closed precisely at the moment those lenses' birth-bugs are
born. Scenario: the walk has a pinch-open frame; a feature adds a pinch-open polaroid with slightly
different close behavior; FEATURE-FIT walks its journey seams (all backed), no uniformity class
exists, no design review runs — ships non-uniform. That is the literal tlvphotos pinch-zoom bug
recurring through the mode built after it.
Fold: FEATURE-FIT gains one cheap question — "is anything in this delta a second member of a kind an
existing surface already has?" — and a yes triggers the scoped design review instead of standing it
down. One sentence in the mode table and in INV-141's keying.

### D3 — CROSS-LINK never re-checks old quantified claims against the grown surface set — defect

CROSS-LINK aims findings at "the NEW surface's seams against the existing surfaces it composes with"
and skips the whole-doc property sweep. But a surface add falsifies EXISTING document-level sentences
without touching them: a class clause's member enumeration ("pinch-zoom refused on: walk, door,
side-room") now silently excludes the newcomer; an "only"/"exactly one"/"every surface" sentence is
quantified over a set that just grew; a previously terminal scenario's decided "exits to nowhere" is
now false. None of these are seams the new surface composes ACROSS — they are distant clauses whose
truth quantifies over the surface set — so the mode's stated scope excludes them, and the skipped
property sweep is where they would have been re-verified. Scenario: a class clause enumerates its
members per INV-125's own required form; a fourth sibling lands under CROSS-LINK; every seam check
passes; the enumeration is now a lie and the mechanical guardrail keyed to the registry may or may
not pick the newcomer up depending on registration. The enumeration-style fix INV-125 demands is
itself the staleness vector.
Fold: CROSS-LINK adds one mandatory step — grep the whole doc for enumerations and universal
quantifiers ("every", "only", "all", "exactly", explicit member lists) and re-verify each against
the surface set including the newcomer. Cheap, mechanical, delta-shaped.

### D4 — The surface-authority lens's evidence gate excludes its own target case — defect

> "Fire this lens ONLY when the document itself provides clear evidence of a competing authoritative
> surface… When in doubt, stay silent rather than produce a finding." — Phase 3e, surface authority

The lens exists for the operation that forgets to register with the authoritative surface. The
highest-value instance is the doc whose author forgot the registry ENTIRELY — which therefore
provides no "clear evidence," so the lens self-disarms exactly there. "When in doubt, stay silent"
also inverts the skill's own posture everywhere else ("state what you assumed," "never silently fill
gaps"). Scenario: a spec adds a print-export operation; the product has a downloads registry the doc
never mentions; the lens reads the doc, finds no competing surface named, stays silent; exports ship
unregistered. Fold: keep the anti-speculation core but change the fallback from silence to a stated
assumption — "I found no authoritative surface for <category> named in this doc; if one exists in
the product, this operation does not register with it" — which is an assumption line, not a finding,
and costs nothing when wrong. In pack use, the three-source lens should also be cited here: the
architecture doc is in view and DOES provide the evidence the document under review omits.

### D5 — FULL mode has no coverage record, and its only mechanical artifacts collapse to N/A on frontend specs — defect

Phase 3 opens "for every entity, transition, and operation" — but nothing in the output proves the
walk happened. The 3e section calls itself "habits of attention… not a checklist," yet it now
contains ~19 lenses, several of which are worded as mandatory whole-doc sweeps ("run as a
completeness sweep rather than a spot-check"; the declared-laws station "demands, per declared law…").
Meanwhile FEATURE-FIT — the LIGHTEST mode — requires a verdict per lens, and FULL requires none: the
heavier mode has the weaker accountability. The three coverage tables (CRUD, invariants-per-state,
authorization) are keyed to a backend world; for the frontend surface specs this pack mostly reviews,
the skill itself sanctions replacing them with one N/A line — so a FULL pass on tlvphotos-class specs
produces zero mechanical coverage artifact, and a skipped lens is indistinguishable from a lens that
found nothing. Both shipped misses (165's exit cut, 167's stale lane) were skim casualties inside a
"not a checklist" 3e on frontend specs. Scenario: any FULL pass; the reviewer honestly runs 12 of 19
lenses; the record shows findings but not the skip; the record's version line says the pass ran under
the current lens set, which is now a false assurance.
Fold: split 3e into (a) mandatory sweeps (declared laws, edge-condition completeness, uniformity,
entry state, unwritten seams, transition payloads) each owing one verdict line in the persisted
record — hit / clean / N/A-with-reason — and (b) imaginative probes, which stay discretionary. Add a
surface × sweep verdict table as the frontend-kind replacement for the CRUD table, instead of the
sanctioned N/A line.

### D6 — Constructed spec fragments the current phases pass (instances, each verified against the lens walk)

**Bug A — focus after overlay close.** "Tapping a photo opens the lightbox over the wall with a
300 ms fade; the same fade reversed closes it via the X or Escape. While it stands, the wall's
controls are unpressable." Paired-transition: both directions stated, mirrored — pass. Reversibility
of means: tap has no continuous inverse — no fire. Overlap [INV-136]: controls retracted — pass.
Entry symmetry and entry state: re-entry path and opening photo stated — pass. Hole: focus after
Escape lands on the body; a keyboard user is lost. No lens asks. (Class member 1.)

**Bug B — audio under the veil.** "Ambient audio starts on room enter and stops on room leave.
Opening the side-room covers the room with a veil." All transitions stated; INV-136 binds only
clickable controls and explicitly frees passive elements; covering is neither enter nor leave, so
the audio's fate is the platform's (keeps playing). INV-72 could in principle reach it, but its walk
is per-surface-situation, and "the audio" is a property, not a surface — no handle. (Class member 3.)

**Bug C — live re-sort under the finger.** "The catalog sorts prints by popularity; ties break by
newest first." Ambiguity-and-ties: resolution is deterministic — pass, and the lens is thereby
SATISFIED by the very sentence that hides the hole. Hole: popularity changes while the visitor
scrolls; nothing states whether the order is frozen at entry or live-reordering mid-scroll, so a row
can jump under the finger. No lens asks when a stated rule's input is sampled. (Class member 6.)

**Bug D — stale global on re-entry.** "The visitor toggles light/dark theme in Settings; each room
renders in the current theme." Entry state [INV-167]: the room's own internal state (position,
reset-or-resume) can be fully pinned — pass. Declared laws: fires only if the author declared theme
a cross-cutting law; an author who wrote it as a Settings feature did not. Hole: a re-entered
pre-rendered room flashes the old theme; whether entry re-samples globals is nobody's lens. (Class
member 7.)

**Bug E — two homes for one derivable fact, no tie.** "The wall shows 12 prints per room. The map
shows every room with its print count." No contradiction (3d needs clauses that CONFLICT; these
merely never meet); three-source lens compares spec against architecture and code, not spec against
spec; class lens fires only after a defect is found. Hole: nothing states the map's counts equal the
walls' contents, so they drift independently. Missing probe: when two clauses independently describe
overlapping data, is their agreement stated as an invariant? One sentence in 3d closes it.

### R1 — Blocking-kind ambiguity on the paired-transition family — recommendation

The prover's paired-transition lens [INV-126] says a silent exit direction "is a finding," and under
the KIND rule a missing required answer is a defect, which BLOCKS at the push gate. The design
review's motion-parity lens [INV-165] over the same physical gap is "a recommendation or a question,
never a blocker." The same clause also says the undecidable pair "is surfaced to him rather than
judged from the text" — a question, not a defect — yet whether the push gate blocks on an unanswered
motion question is stated nowhere. Two stations, one gap, opposite blocking semantics, and the
boundary (declared-one-sided → prover-defect vs never-declared-grouping → review-recommendation) is
real but unstated. Fold: one sentence in the KIND block naming which kind an INV-126 finding takes
and what the gate does with a surfaced-to-the-human motion question that is still open at push time.

### R2 — Lens overlap without cross-reference: the lifecycle cluster — recommendation

Entry symmetry (re-entry path), entry state (re-entry payload), paired-transition symmetry (motion
both ways), persistence-and-versions ("reopened the widget and it looked broken"), and scenario
entry/exit all probe one lifecycle from five vocabulary-colliding angles; each needed a paragraph
disambiguating itself from its siblings, and the reopen case is claimed by two of them. A reviewer
who ran persistence can honestly believe reopen is covered and skip entry state. Fold: merge into
one lifecycle lens with named sub-questions (path in, state in, motion both ways, stored shape
across versions), or add one cross-reference table; this also shrinks the 3e wall that D5 shows
nobody fully walks.

### R3 — FEATURE-FIT's consistency exclusion is readable two ways — recommendation

"Document-internal consistency is out of scope for this mode" is presumably meant as PRE-EXISTING
internal consistency between old clauses. As written it also excludes delta-vs-existing
contradiction — the core of fit. A reviewer taking the broad reading passes a delta that directly
contradicts an old clause it never cites. Fold: rewrite as "pre-existing consistency between old
clauses is out of scope; a delta clause contradicting any existing clause is in scope and is the
mode's first check."

### R4 — FEATURE-FIT verdicts trust a spec whose currency it never checks — recommendation

Phase 0's node-pin currency check runs at triage of a shipped-system DOC; FEATURE-FIT's procedure
never invokes it, yet its per-lens verdict "backed by a clause" treats every existing clause as
live. A clause describing excised behavior backs the verdict with dead prose — the exact failure
Phase 0 exists to prevent, bypassed by the mode that runs most often. Fold: FEATURE-FIT verdicts on
a shipped system cite pinned clauses only, or mark the verdict conditional the same way Phase 0 does.

### R5 — Nothing bounds `[default]` accretion — recommendation

FEATURE-FIT lets every lens close `[default]`-tagged; INV-72 findings land `[default]`-tagged; no
station ever sweeps accumulated defaults for ratification. A product can converge to a spec that is
majority unratified defaults while every prover pass stays green. Fold: the FULL pass reports the
default count and lists the oldest N for a taste call — one line in Phase 5.

## Priorities

Defects (the method as written ships a bug): D1 (the payload class — highest; six shipped bugs
already trace to it), D2 (the second-sibling blind window at intake), D3 (CROSS-LINK's stale
quantifiers), D5 (no coverage record; N/A tables on frontend kinds), D4 (self-disarming
surface-authority gate), D6 (instances A–E; A–D fold into D1, E is its own one-sentence 3d probe).

Recommendations (quality/consistency, human weighs): R1 (blocking-kind of motion findings), R2
(lifecycle lens merge), R3 (FEATURE-FIT consistency wording), R4 (FEATURE-FIT currency), R5
(default-accretion sweep).

One-line verdict: the prover is strong on written topology and structurally blind to defaulted
payloads; it has been patching that blindness one shipped bug at a time (six lenses in five days by
the provenance file), and D1's parent lens plus D5's verdict record are the two folds that end the
loop instead of extending it.
