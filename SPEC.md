# live-spec — SPEC (v0.15.24, 2026-07-06)

> How to read: each section is a scenario — what you do and what you see. The short codes in brackets are
> quiet machine anchors (for the prover, the test matrix, and transcript greps); the Formal index at the end
> maps every anchor to its home section. Edit history lives in JOURNAL.md; this spec states today's truth.
> Restructured use-case-first 2026-07-04 (queue row 22) under an anchor-set guard: v0.4 carries exactly the
> anchor set of v0.3 — the shape changed, no rule was lost.

**Current vs target.** Shipped today: the six skills (the base rulebook and the five working ones), the
templates, the adoption procedure text, the inbox, the skill evals with their run records, this spec and
queue, and the first guardrails slice —
the pack repo's own pre-push gates and the opt-in commit fence, installed and tested. Target (each owned
by a ROADMAP row, not yet code): the guardrails' host-facing checks and surface registry [E-6, E-10], the
snapshot machinery [E-7] (the adoption baseline A-6 rides it), the CI mirror [M-5], the model router
[ACT-3], the optional design-sync machine [E-18]. This spec never claims shipped what isn't — clauses below marked [target] await their row, and
the tag binds at the granularity it is written: a surface is [target] only if its OWN clause carries the
tag, never merely a parent section or one leg of a split anchor. The promise is mechanized: the suite
holds the map from every [target]-marked index fact to its owning, still-open queue row — a target whose
row lands, vanishes, or was never named turns the suite red, and so does a node keeping the tag after
its pins became real. [S-0]

## What live-spec is

A package a software project attaches to — at the start or in the middle — to work by one discipline:
wishes are thrown in passing, each one enters a proven process, machines hold the bounds, the human is
interrupted only for decisions that are genuinely theirs. The package is a **base skill** — the pack's
shared rulebook and default settings [E-12] — plus five working skills (spec-author, product-prover,
build-pipeline, communicator, publish), document templates, an adoption procedure, and a set of
mechanical guardrails a project instantiates.

The project it attaches to is the **host**. The host owns its own spec, matrix, queue, journal, surface
registry, inbox, and a `.live-spec/` folder (profile, checkpoints, installed-skill versions). [E-1]

## Throwing a wish

You say, mid-anything: "and let the card also show…" — and go back to your thought. A **wish** is exactly
that: one request in plain words, any size, spoken at any moment. [E-2]

That same minute the wish becomes a row in the **queue (ROADMAP.md)** — the persistent, ordered home of
every wish: your words · class (size, plus priority when it isn't normal) · status · acceptance criterion,
one row each. [E-3] Spoken means the row
exists before anything else happens; it survives even if the session dies a second later, and rows are
never deleted — only closed with a named exit; at a milestone, rows closed with a TERMINAL exit (landed ·
declined · superseded) MOVE to a dated queue archive — the attic principle applied to the queue: archived,
never edited, never lost. A **deferred** row is not terminal: it stays in the active queue carrying its
revisit trigger until the trigger fires or it re-resolves to a terminal exit — the archive never swallows
a wish that is still due back. No wish is ever lost. [INV-1]

From the row the wish walks one path: classified by size, priority, door, and work-kind — stated back to
you in one INTAKE line (the paragraphs below) → a
spec-delta is drafted → validated against the WHOLE spec — here only genuinely-human questions go out to you, batched;
everything else proceeds on the recommended option, marked in the row → queued → in-work → landed (green
suite + guardrails + committed + the row closed with its acceptance met) → reported to you in one
plain-language LANDING line: position on the map · what landed · what remains. [T-1..T-7]

**How batched questions reach you.** Several open picks never become a serialized chat questionnaire:
they render as ONE interactive decision page — one card per question, the recommendation named, room for
a free-form answer on every card — opened in its own window while the lane keeps moving [INV-4]. The
answered file is read back, archived in the project's `docs/decisions/`, and every answer is harvested
into its queue row the same session — an answer left un-harvested is a decision lost. And an answer is
his WORD, not merely his click: a pick the human then disavows in plain speech ("я не понял, что
подтверждал") is WITHDRAWN — recorded as answered-then-withdrawn, the pick re-opens with a plainer
explanation owed before it is asked again; an uninformed pick never settles a verdict that needs his
word [INV-9] (born 2026-07-05 night: the shell-separator verdict, picked at 23:49, disavowed minutes
later). The page's
mechanics (filename law, ordinals, the JSON round-trip) live once, in the communicator skill's rule 10
[INV-13]. [E-22]

**A decision card asks in consequences, not mechanisms.** The shell-separator card explained HOW the
failure worked, and the reader still could not tell what he was deciding («я не понял проблему, не
понял последствия, не понял что решать» — 2026-07-06, the same incident that already birthed the
withdrawn-answer law above). So every card on a decision page OPENS with what the choice CHANGES for
the person — what he will see, get, or stop suffering under each option, in the product's words; the
mechanism follows only if it helps; and each option is labelled by its consequence, never by its
implementation. A card whose question cannot be answered without understanding the mechanism is a
defect of the card [INV-28 kin]. [INV-32]

**How a wish is classified.** Size is one four-word vocabulary everywhere — **bug / small / surface /
large** — and the queue's class column speaks the same four words, never a second SIZE scale (the door
below is a different axis — where the wish ENTERS the pipeline, not how big it is). Priority is
**normal** unless the row says otherwise; two marks exist: **critical** — the shipped product is broken for
its user (an unusable surface, data being lost, a safety gate violated) — and **quick win** — low effort,
immediate value, no design decision inside. When the classifier can't call a size, a priority, or a work-kind
[T-16], it asks you at intake and never guesses; until you answer, the wish carries normal (a kind: the
host's recorded default, else none — and a kind not yet named scales nothing down [INV-22]) and the open
question rides in the row — the lane keeps moving [INV-4]. [INV-12]

**A big wish negotiates scope, never time.** Nobody here asks "how long will it take", and an answer in
hours or days is not an input the walk accepts — a time estimate out of a builder is a guess dressed as
a number (Alexander 2026-07-05: "можно играться со скоупом, а не с таймлайнами"). When a wish looks
bigger than it is worth, the walk answers in scope terms and PROPOSES: **cut the scope** — fewer
surfaces in, plainer defaults on what stays — or **split into stages**, each stage one landing through
the full pipeline (the "large" size already decomposes this way [INV-12]). The proposal proceeds on the
recommended option — the lane never parks on it [INV-4] — and every cut rides the same batched report
as every taken default [INV-18], never silent [INV-5]: your re-widen is simply a new wish. A scope cut
bends scope only, never order — it is not a quick-win mark, and only priority moves the lane [T-11].
And what no cut may ever touch: the delta's MANDATORY sentences — the fences [T-14], a kept surface's
facets [INV-18], the non-goals and the success measure [INV-20, INV-21]. Scope dials richness; it never
touches the safety net. [T-15]

**One wish = one user story; a row closes only whole.** The failure this law is built on: a project
fused two stories — a door and a gallery — into one queue row; the door half shipped, the row was
declared COMPLETE, and the gallery stayed a rejected wall for four rebuilds, each drop caught by the
human's eyes, never by the pipeline. So, at intake: a wish carrying several USER STORIES — several
distinct things a person will DO and SEE — is SPLIT, each story its own row through the full pipeline.
Kin to a stage split, but a different knife: stages slice ONE story's depth [T-15]; separate stories
are never fused into one row to begin with. Sub-behaviours of one story — its hover face, its phone
face, a backpointer — are that story's ACCEPTANCE, not new stories; unclear whether it is one story or
two is asked at intake, never guessed [INV-12]; and a split loses nothing — every row born of it cites
the one spoken wish it came from [INV-1]. [T-17] Where a row nonetheless carries several legs (a
legacy fusion, a harvested batch), its Done-when enumerates per-leg acceptance and the row CANNOT close
with an unmet leg — half-done is a status, never a landing; and the resume file's LIVE-STATE
supersession never compresses an unfinished leg out of existence: a leg still open at compaction is
restated, not summarized away [M-2]. [INV-26]

**A wish hears itself land, and progress reads like a departures board.** You toss a wish in passing —
before sleep, mid-thought — and without an echo you cannot know it survived. So the intake line is not
only WRITTEN into the queue, it is SPOKEN back: one plain sentence — what was heard, the door called,
the name the work will answer to, its row number ("caught: …, it's a feature, we'll call it X, row N").
A wish that arrives silently (an inbox file, a harvest) gets its echo in the next report, never as an
interruption. And whenever status is reported, every in-flight feature is named by that name with its
pipeline STATION — spec → prove → architecture → prove architecture → matrix → test → code → verify →
commit & show, plus the terminal landed — so progress reads like a departures board at a glance, never
prose archaeology; the station vocabulary is the pipeline's own step names, one station per step, all
nine — a feature paused at proving the architecture or at commit & show reads under that station's own
name, never an improvised one; landed is a state, not a step: it says the row closed whole. (His word 2026-07-05, before sleep: "captured this that
request, it's a feature, we'll call it this and that — а потом рапортовать как каждая фича идет по
пайплайну".) [INV-27]

**The outcome does the talking: names are chosen plain, and every handle trails.** The first real
departures board passed its eval and failed its READER — lines led with coined metaphor-names
(«Прогулка по уликам», «Часы получают зубы») and row numbers he never opens, and squeezed facts into
riddles only their writer could parse ("seven times — twice the fence"; 2026-07-06 morning, the jargon
family's third strike in two days). Two arms, one law. NAMING: a feature's echo-name is a short
DESCRIPTIVE phrase in the product's own words — what the thing does, parseable cold by a reader who
missed its birth — never a private metaphor; a name that needs its story told first is a handle, not a
name. LINES: a human-facing report or board line (chat reports, report pages, decision pages, the
capture echo — method-internal docs keep their anchors) OPENS with what changed for the reader — what
they can now do, see, or stop fearing; every internal handle — spec codes, row and session numbers, and
any coined name the reader never chose to learn — may only TRAIL in parentheses; and one fact = one
standalone sentence — a compression whose parsing needs the writer's context is a defect of the line,
not a flourish. Bookkeeping numbers are handles too, and they kept walking into the message anyway —
two consecutive eval runs put "all 64 checks green, v0.9.16" into the human's message body (2026-07-06)
— so the law carries an explicit NEVER-list: a test count, a suite size, a version string, a check
tally is never message CONTENT; the message says what the number means for the reader ("tested clean",
"saved", "the method held"), and the number may only trail as a quiet anchor or stay in the records.
One carve-out, by law: where the number IS the asked substance — a direct question about it, or the
done-claim evidence walk, whose claim lines pin artifact and method version [INV-25] — it speaks as
the answer, not as bookkeeping. [INV-28]

**The report law is walked, not remembered.** The law above passed its evals and still failed on the
senior's own chat: the session-13 closing report led with pack-internal names and loan-translated doc
metaphors and was bounced by its reader («это ты на каком языке разговариваешь???» — 2026-07-06, the
jargon family's fourth strike in two days and the first AFTER the law landed). Chat has no suite, so
the enforcement is a STEP, not another sentence: before any movement-end or milestone report goes to
the human, the communicator rules are RE-READ, and the draft is passed phrase by phrase through one
question — does this sentence stand for a reader who does not live inside the pack; a pack surface it
names is explained in the reader's own words or dropped (quiet trailing anchors stay legal — the walk
governs what does the talking, never the handles that trail). The walk's one home is the communicator
skill; its acceptance belongs to the reader — a movement-end report that draws "а это что?" is the walk
not walked. [INV-34]

**Priority bends the lane order, visibly.** A critical bug lands before everything — it heads even the
waiting-bug line (next section). Critical priority heads the QUEUE whatever its door — a critical-priority
feature goes to the queue head too; but only the bug DOOR preempts the in-work lane [T-9]. A quick win may bubble up: when the lane frees, it may be taken ahead of
larger queued wishes, the jump marked in its row, never silent; after one bubbled landing the queue head
goes next, so a stream of quick wins cannot starve a big wish forever. An inbox wish's arrival IS its
harvest moment — that is when it first becomes a row the ordering rules can see; a file's own date never
competes with spoken timestamps. Arrival ties resolve by queue row order, top to bottom; within one sweep
an inbox batch harvests in filename-sorted order. [T-11]

**The door is named before any code.** Classification is an explicit step, not a feeling. A row carries
three axes, stated together in ONE intake line — size · priority · door · the work-kind (what the wish
builds — next paragraphs [T-16]); a wish too big for its worth is negotiated in scope, never in time [T-15]. Size (with priority) says how big
and how urgent; the **door** says where the wish enters the pipeline: **feature · bug · refactor ·
docs-only · skip**. The size and door axes share one word deliberately — a wish sized "bug" IS the bug door, one
call stated once; the door axis only adds the other four entries. [T-12]

The door is decided by an ordered procedure, tripwires first — never judgment. (1) It IS a **feature** —
however casually asked — when ANY of these holds: a new user-visible surface appears · new persistent
state appears · a new interaction lands on an existing surface · the touched surface is marked [target]
in the spec (the canonical, machine-checkable form of "not yet specified / later surface"; the
plain-prose cousins bind too, but the author writes the tag) · the change adds behaviour no spec clause
backs. (2) No tripwire fired, but shipped behaviour is wrong against what the spec or product already
promises → **bug**. (3) Behaviour stays identical, structure moves → **refactor**. (4) Only prose OUTSIDE the
normative spec changes (README, comments, guides) → **docs-only** — rewording a spec rule is NOT
docs-only: it changes what behaviour the spec backs and routes as feature or bug. (5) The narrow all-hold boundary (single file · no new state, element, or visible
behaviour · an existing test level already covers the touched fact) → **skip**. The tripwire verdict
outranks a casual label: a wish called a "bugfix" that fires a feature tripwire is re-doored to feature
and the intake line says so [INV-5]; queue-cutting [T-9] belongs ONLY to the bug door, so a re-doored
wish takes no preemption — your word can still raise its priority (priority is yours), but no word makes
a feature skip the spec step. The door is also re-checked mid-work: the moment running work is about to
create a user-visible surface or persistent state its current door doesn't grant, work STOPS and the
door step fires again — "it sounded like loading until the surface existed" is exactly the failure this
catches; the re-doored wish KEEPS the lane token and re-enters the walk in place (no re-queue, no park —
parking stays a bug-preemption move [T-9]). One request lives outside the lane entirely: asking to merely
SEE or TRY something, with no commitment to keep it, may be built as a labelled sketch (see "A prototype
is not the product" — the ask-when-unclear rule lives there). Casual
loading stays the contract — a wish is routed through its door, never refused for being casual, and
never hand-built past the pipeline because it sounded small. [INV-16]

**The intake line also names WHAT is being built.** Size says how big, the door says where the wish
enters — the **work-kind** says what kind of thing the work produces, and with it which pipeline
machinery earns its keep. Four kinds today: **product** — something the host's own user faces;
**infra** — tooling that serves the project itself (scripts, hooks, CI, pipelines); **skill** — a
behaviour document an agent works by (a SKILL.md, a prompt pack); **prose** — a document written for a
human to read (an overview, an article, a spec's own text). The kind is called from what the wish
PRODUCES, one kind per wish — a wish genuinely producing two kinds is two wishes, split at intake; a
kind the classifier can't call is asked like an uncallable size [INV-12]. A host with ONE usual kind may
record it as a host-profile default the intake line starts from [E-8, E-13] (track-coach's would be
product); a host whose wishes genuinely span kinds — live-spec itself ships skills, prose, and infra —
records none and calls each wish on its own. The vocabulary is CURATED like the facet list [T-13]: each kind above is earned by real
work the pack has already routed (track-coach's widget — product; render-doc.py — infra; the pack's five
skills — skill; OVERVIEW.md — prose), and a fifth joins only with a named wish the four mis-served,
re-justified at milestones. The law binds forward: a row queued before it carries no kind and owes no
retro-fill — it names its kind the moment it next moves (its in-work claim is its intake for this axis). [T-16]

**A kind scales the steps — it never skips one silently.** The door picks WHICH steps run [T-12]; the
kind picks the FORM each running step takes, never whether the walk happens: the per-kind meaning of every step (what "architecture" means for
a one-file script, what "verify by deed" means for a document a human reads) has its normative home in
the build-pipeline skill — one table for every project, the skill's own domain [E-12]. This spec binds
the contract around it: at landing, every pipeline step has either APPLIED in the form the table states
for the wish's kind, or STOOD DOWN by name in the landing's report ("design-sync — text product, stands
down"), so a skipped step is always a written fact, never an omission. An unresolved kind scales nothing
down — while the kind question rides the row [INV-12], every step applies in full, because standing a
step down requires a NAMED kind to answer for it. What no kind may ever touch: the
door law and its tripwires [T-12, INV-16], the delta's mandatory sentences — fences, facets, non-goals,
success measure [T-14, INV-18, INV-20, INV-21] — and ask-at-intake [INV-12]; the kind dials the
machinery, never the safety net — the same law a scope cut obeys [T-15]. [INV-22]

**Each step is worked in its craft's mindset.** A pipeline walked by one generalist head produces
generalist artifacts — a spec that reads like a coder's notes, a matrix that checks what was convenient
to check. So every step names the profession whose head you wear while walking it: the spec is written
as a strong product manager, the architecture as a software architect, the matrix and the tests as a QA
automation engineer, the code as a senior developer; the two prove steps are the prover's own
formal-reviewer head, commit & show is a careful release hand whose reader is the human — and the
verify walk is done with the visitor's own eyes, not the builder's [INV-30 kin]. The full step→craft
ladder has ONE home, build-pipeline's step list [E-12]; each artifact is judged by its craft's
standards, and the landing report's step accounting speaks in them. And the craft, like the step's
form, wears the KIND's face [INV-22, INV-30 kin]: on a prose product the code step is worked as a
strong writer, on infra as a toolsmith — the ladder names the archetypes, the wish's kind says what
their standards look like in its medium. (His word 2026-07-06: «когда ты
делаешь продукт-спеку — ты крутой продакт, когда архитектуру — крутой архитект, когда матрицу тестов —
крутой QA-автоматчик».) [INV-33]

**A feature is specified past what you know to ask.** You say "add a room where photos hang" — you don't
say "and decide what happens on a phone", because you can't know that's a question. So when a wish's door
says feature, drafting its spec-delta walks a fixed sweep of the **standard facets** — the dimensions
every visible feature has whether or not anyone names them: layout on a phone or narrow window · touch
where the design assumed a mouse (anything hover-only needs a touch answer) · the empty, error, and
loading states of each new surface · accessibility (reachable by keyboard, readable contrast) · the
performance envelope (at what input size it must stay usable) · visual hierarchy (the gap between
separate things larger than the gap within one thing; a heading never dimmer or smaller than its body)
· two windows at once (the same stored state open twice) · a missing source (an input file renamed or
gone). The facet list's normative home is the
spec-author skill, one list for every project, and the list is CURATED: a facet joins only with a named
real incident it would have caught, and the list is re-justified at milestones — a checklist that grows
by taste rots into a forty-row form. This spec binds THAT the sweep runs and what counts as
done. The sweep scopes to the feature's VISIBLE surfaces: a feature with none — new persistent state
only, say a cache — satisfies it with one explicit sentence, "no visible surface — facets N/A", never a
silent skip. A wish re-doored to feature mid-work [INV-16] walks the sweep before work resumes — the
late-recognized surface is exactly the one whose facets nobody looked at. A fenced prototype is NOT swept
— a sketch has no facets to promise [E-17]; the sweep fires when promotion makes it a feature. [T-13]

**Every facet ends as a spec sentence — silence is not an option.** Two ways a sentence gets there:
**decided** — you (or the walk's batched questions) called it — or **defaulted** — the recommended option
is taken so the lane keeps moving, written into the spec carrying the literal tag `[default]` at its line
end (so a later prover tells a taken default from a hole, and the matrix derives the facet's test row
either way [E-15]), and the choice is TOLD on the landing report's defaults list as a plain-words
tradeoff in your product's terms ("on a phone this gallery stacks into one column — tweakable"), never
one ping per facet and never a confirmation request — silence is consent [INV-31]; your veto simply
becomes a new wish. A facet with no sentence —
neither decided nor defaulted — is a spec defect the prover flags, the exact hole the Room shipped
through (hover-only openings, no phone layout). On an adopted or promoted surface that already lives
[A-10], a default is read from the shipped truth and reconciled like any re-engineered claim [A-3], never
invented greenfield against live behaviour. The sweep and the axis rule [C-1] split one dimension by
time: the sweep AUTHORS the facet sentences when the feature is first specified; the axes COMPOSE and
test them across views once the surface exists. [INV-18]

**A feature is interrogated for how it fits the product — a small prover on the wish itself.** The
device facets above ask what every visible feature owes; nobody yet asked how THIS feature sits in
the person's PATH — and path holes (enter → browse → re-enter → stuck at the tenth picture with no
way on) ship green because no clause ever promised the way out. So a feature-doored wish's spec-delta
also walks the FIT WALK, kind-scaled: a product/UX wish walks the visitor's journey — how the person
ARRIVES at the new thing, what they do there, where they go NEXT from every state it can be in, what
a RETURN visit or entry through another door changes, what neighbouring behaviour it IMPLIES
(no-repeat needs remembered state), what the FEEL owes against the approved prototype's bar [E-17],
and what next feature it invites; an infra wish walks its flows — inputs → outputs, data lifecycle,
failure paths; a skill wish walks trigger → correction → when NOT to fire. The walk interrogates the
FEATURE, never the person: derive each answer from the existing spec and the shipped truth first;
a hole that is trivially closable is CLOSED by the walker and the closing is WRITTEN down (his word
2026-07-06: закрыть и написать как закрыл); the rest are written decided or `[default]`-tagged, and
only the genuine taste calls go out, batched [INV-4, INV-18] — «не надо мучать пользователя вопросами
как на пытках» (Alexander 2026-07-06, with tlvphoto's shipped evidence in hand). The prover gains the
matching focused mode — FEATURE-FIT: given one feature's delta, walk its journey seams against the
whole spec the way CROSS-LINK walks a new surface's seams — the prover already thinks in flows,
states, and transitions; this pulls that thinking forward to intake. Lens lists live once, in
spec-author's sweep section, curated like the facet list [T-13]; the law binds forward — a landed
feature owes its walk at the first landing that touches it, never retroactively en masse [INV-21
kin]. [INV-29]

**Verify-by-deed walks the visit and watches the feel.** "Eyes on the artifact" has meant "it renders
and clicks" — and cheap-feeling motion or an ugly affordance shipped green through the whole pipeline
(tlvphoto's transitions and its open-work button, 2026-07-06). So for the product kind the verify
step includes a named VISITOR WALK — the whole journey as the person will live it: first visit,
return visit, entry through another door, "where am I and how do I move on" from any point, the
exits — and a FEEL pass: motion quality (easing, duration, choreography) and each affordance's craft,
judged against the approved prototype as the bar [E-17]. Findings become rows or red — never vibes,
never a mental note. The walk's checklist lives in the build-pipeline step-8 product cell [E-12,
INV-22]; this clause binds THAT it runs for anything a person visits — and in the FORM the medium actually
has: a browser product walks motion and affordance craft, a book walks its reading path and chapter
flow, a CLI its command round-trip; the feel lens is a partial skill applied by the product's
context, never a frontend checklist forced on prose (Alexander 2026-07-06). [INV-30]

**A taste choice made without asking is TOLD, never confirmed.** Building a feature, the walk makes
small taste calls itself so the lane keeps moving — an animation's speed, a button's shape, a
caption's wording — each written into the spec with its `[default]` tag [INV-18]. What went wrong the
first time was silence: a product accumulated eight untold choices and read unfinished everywhere
(tlvphoto, 2026-07-06). The law: the landing report NAMES each choice made without asking, in plain
words with an example, marked as tweakable — and that is ALL. No confirmation is requested; silence
is consent; nothing is re-asked later — the person asks when they want something changed, and the
`[default]` tags keep every such choice findable in the spec forever (Alexander 2026-07-06: «если
мне всё ок — не надо подтверждать… дальше уже, если надо, пользователь спросит»). [INV-31]

**What already works is promised before you touch it.** When a feature-doored wish touches a surface
that already lives, its spec-delta opens — before the facet sweep authors anything new [T-13] — with
**regression fences**: one sentence per neighbouring promise that must stay true through the change
("the catalog still opens on click", "the player keeps playing across a view switch"), each citing the
existing spec clause it guards. A fence is not new law and earns NO new matrix row: the cited clause's
own row already carries its never-side [INV-6], and the landing's full-suite run is what proves the
fence held — so "fixed one thing, quietly broke the neighbour" turns red before it ships. The delta
thereby splits everything it touches in two: promises that STAY — fenced, cited, untouched — and
behaviour being CHANGED — never fenced, re-authored as new law through the normal walk. A fence that
finds no clause behind it has discovered an unwritten promise: that promise is reconciled from the
shipped truth like an adopted claim [A-3], written as its own spec fact with its own row, and surfaced,
never silently assumed [INV-5]; likewise, touching a neighbour whose claim is adoption-born and still
unverified triggers that claim's reconciliation before it can be fenced. The wish's queue row names its
fences by the anchors they cite ("fences: …") — "untouched and still true" becomes a greppable claim —
while the LANDING line stays its one-line self [T-7]. Fence-AUTHORING belongs to the feature door; the
bug and refactor doors inherit only the catching (their full-suite runs exercise every never-side), and
a prototype fences nothing because it promises nothing [E-17]. [T-14, INV-19]

**A feature also says what it is NOT doing — and how we'd know it worked.** Every feature's spec-delta
closes with two short sentences, and both are ALWAYS written — like the facets, silence is not a legal
state. **Non-goals**: what is deliberately left out ("version comparison — not this time"); "nothing
deliberately left out this time" is itself a valid sentence — only a MISSING sentence is a hole. A
non-goal that narrows what the wish asked for is a scope decision, so it rides the same batched report
as every taken default [INV-4, INV-18], never a silent narrowing [INV-5]. [INV-20]
**A success measure**: how we'd notice the feature worked for its person, a number where one exists
("the producer opens the evidence panel at least once per session"), decided or `[default]`-tagged like
any facet — the tag marking provenance only: no matrix row derives from a success measure while the
machinery that READS them (KPI dashboards, A/B runs, segmentation) stays [target] under its own queue
rows; until then a measure is a written promise the human checks by eye, honestly labelled so. The
quantification questions — is there an analytics tag? how will we measure? is an A/B worth it? — ride
the facet sweep's batched report [T-13, INV-18]. Both sentences bind forward from features specified
after this rule lands; an adopted feature owes its pair at the first landing that touches it [A-3],
never retroactively en masse. A prototype writes neither — it promises nothing [E-17]. [INV-21]

While it walks, four things are always true:
- Intake is parallel, execution is serial — **one landing at a time, per repo**: the single in-work row IS
  the lane token, and CLAIMING it is an atomic committed act — the session commits the row→in-work flip
  first, then re-checks the token under the fence [INV-11] immediately before drafting the spec-delta; if
  the re-check reveals another committed in-work row, the later claimant backs off and re-queues. So any
  assigned session (a second parallel one included) takes a wish only after seeing — in committed history,
  never a bare read — no other row in-work. Bounded delegated execution (workers) may overlap under the senior — only on disjoint
  files, with the edit fence armed [INV-11] — but the lane itself (spec-delta, validation, integration,
  closing the row) still lands one at a time. A new wish waits its turn unless it is a bug preempting
  (next section). [INV-2]
- **A pending question for you never stops the work** — the lane proceeds on the recommended option; the
  question stays open in the row, revisitable any time. [INV-4]
- **No silent micro-decisions** — every choice not in your wish is either asked, or recorded in the spec
  AND surfaced in the same report. The batched report carries this as its own postcondition: EVERY taken
  default, trim, and deliberate narrowing of the walk appears in it — a decision absent from the report
  is silent by definition, whatever the spec recorded. Nothing decided-and-buried. [INV-5]
- **Every landing cites its wish row** — the commit message or journal entry names it, so "why does this
  exist" is always answerable. [INV-3]

A wish can also end without landing; its row stays in the table: **declined** (you said no) · **deferred**
(parked with a named revisit trigger) · **superseded** (absorbed by another wish; the row points to the
absorbing one). And declining is not a black hole for what the declined wish had absorbed: a wish other
rows were superseded INTO lists them at its decline, and each listed row is either declined BY NAME in
the same breath (your no covered it too) or RETURNED to the queue as its own row again (your no was
about the absorber's shape, not the need) — a superseded wish never dies by pointer [INV-1]. [T-8]

What the wishes grow is the **spec (SPEC.md)** — the living statement of what the product is, one surface
= one name, everywhere. [E-4]

## When a bug cuts the line

A bug may interrupt the wish in-work. The interrupted wish moves to **parked**: a checkpoint is written
(failing test names if red, hypothesis, touched files — nothing red is ever committed), the bug takes the
lane, and the parked wish resumes as the immediate next landing — ahead of ANY queued wish, a quick win
included: a bubble [T-11] jumps only fresh queued wishes, never a resume. Should more bugs arrive while one holds
the lane, **critical** bugs head the waiting line (among themselves by arrival), the rest follow by
arrival; the parked wish resumes only once no bug waits. A bug already in the lane is never itself
interrupted — an arriving bug, critical included, joins the line, so at most one wish is ever parked. [T-9]

## When the workshop itself misbehaves (the problem ledger)

Some noise is not a product bug: the test harness flakes, a dependency is missing, the shell eats a
command, a tool times out. The temptation is to retry and move on — and the same noise then eats the
same minutes in session after session. **The problem ledger** is the host's dynamic list of exactly this
operational noise: one git-tracked file, `.live-spec/PROBLEMS.md` (template in the pack;
of `.live-spec/` still only the checkpoints stay ignored [E-8]), born on its first entry. An entry is a
**signature** — a short, greppable plain phrase ("element not clickable: #ex-skip", "zsh eats a bare
===") — with its dated occurrences and a status: **WATCHED** (seen once) · **OWNED** (a named queue row
will solve it) · **AGREED NON-PROBLEM** (dated, the human's word) · **SOLVED** (its row landed, date
kept). [E-24]

**The walk, the moment noise fires mid-work: grep the ledger for the signature.** Not listed → write one
WATCHED line (signature, date, one line of context) and keep working — the write replaces the silent
retry, and it never takes the lane: a defect of the PRODUCT is a bug and goes to the bug lane instead
[T-9]. **Listed → this is the second occurrence, and it gets an owner THAT MOMENT:** either a queue row
(the problem will be solved) or the human's dated agreed non-problem — that verdict is the human's word
alone, never the agent's [INV-9]; the agent recommends, writes the recommended owner now, and the ask
rides the batched report [INV-4, E-22] — the lane never stalls on it. **A third recurrence arriving with
no owner is a defect of the METHOD, not of the day:** it leaves the host as a wish to the pack's own
queue (from a host window: one inbox file [E-11, INV-10]), citing the signature and its dates. [INV-23]

After the owner is written, the entry only collects dates: a recurrence on an OWNED or AGREED entry
appends its date and changes nothing else — re-raising an agreed non-problem is the human's move, the
growing date list is what he re-raises FROM. The landing that closes an OWNED entry's queue row flips it
to SOLVED in the same session — the entry never waits for an audit to learn its row landed.

The seams, stated: sessions write the ledger — a worker reports noise in its checkpoint and the session
carries it over, unless its brief names the ledger among its files (the brief stays the write-ownership
law [ACT-3]); two sessions on one host share the file under the concurrent-edit fence like any doc
[INV-11]; "same problem?" is decided by grep and eyes — signatures stay short so the grep is honest, and
one problem found under two wordings merges into one entry at the milestone compaction. SOLVED and
agreed entries move to a dated ARCHIVED tail of the same file at that compaction [M-1] — one file stays
the one home, and the ledger, too, never grows unboundedly. This is the workshop's law; the product
keeps its own (a recurring product bug re-doors to feature — the pipeline's rule, distinct by what
broke). No visible surface — facets N/A. Non-goals this landing: no mechanical guardrail yet — the named
candidate (a pre-push check that no entry crosses a milestone unowned) earns its row after real usage;
no automated signature matching; the first foreign-host ledgers (tlvphoto, track-coach) open from their
own windows — this landing opens the pack's own, with tonight's live entries. Success measure: the next
operational hiccup in a live-spec session lands as a ledger line instead of a silent retry, checked at
the milestone audit [default].

## A prototype is not the product

Exploring is legal — sometimes you sketch a room before building the house. A **prototype** is such a
sketch: it lives fenced in its own clearly-named home (a `prototype/` folder or branch), and every
artifact it produces carries the PROTOTYPE label in the form its kind can show — a rendered page: an
on-screen banner · an API or data payload: a `_prototype: true` field or header · a script/CLI: a
first-line PROTOTYPE banner · a bare file: the marker in its name or header line. [E-17] The boundary
with the door step: a wish to HAVE something in the product is a feature [INV-16]; a request to merely
SEE or TRY — no commitment — may live as a sketch here, in the fence, no lane, no spec; unclear which
was meant ⇒ one plain question, never a guess. Opening a prototype home is a repo write like any other —
governed by the write-ownership law [INV-10], a judgment act of the assigned senior [ACT-2]: an outside
session files an inbox wish instead, and a worker never opens one on its own brief. The fence is
one-way: a prototype is never wired into, linked from, or styled as a prod surface, and it is shown to
the human only under its label — nothing reaches you AS the product unless its surface walked the
pipeline. Promotion is not a merge: when a sketch earns its place, its feature enters at the spec step
like any wish [T-12, INV-16] — the prototype is evidence for that spec, its code holds no rights. The
machine side: the prototype fence is a guardrails check — a prod file referencing anything inside a
prototype home is RED [E-6], live for the pack repo today; the other two legs — the surface registry's
completeness scan [E-10] and behaviour-traces-to-spec — are still [target, E-6]. When all three land,
the header's honesty rule holds in BOTH directions — the spec never claims what isn't built [S-0], and
the build never contains what the spec doesn't name; today the fence leg is enforced, the rest is
promised, marked, and owned by its rows. [INV-17]

## Starting a new project (bootstrap)

**The version-control gate runs FIRST** — the same order adoption keeps [A-0]: git exists (init if
not), a remote settled or explicitly declined, before anything else is created — a gate cannot protect
files older than itself. Then copy the templates (SPEC, ARCHITECTURE, TEST_MATRIX, ROADMAP, JOURNAL,
NEXT_STEPS) **plus the suite scaffold** (`test_scaffold.py` into `tests/`) — the minimal runnable suite
that DEFINES what "green" means for landing #1: the document set present, every header really filled
(a leftover placeholder is red), the coverage checklist in place, one live-state block. That green is a
floor, not a ceiling — landing #1 ships its own first real test beside the scaffold, and the
traceability checks grow from there. Hooks are OFFERED at bootstrap exactly as at adoption [E-6] —
never imposed, plain words first. Then the first wish enters the queue → the pipeline runs from
intake. [B-1] The gate itself is an always-rule: **no
landing into an unversioned host** — version control exists, and a remote either exists or is explicitly
declined (recorded, not merely recommended), before the first landing. [INV-8]

**The founding questions are asked, never inferred.** Before the first wish walks, the questions that
shape everything downstream get explicit answers in the new spec's opening — first among them:
**personal tool, or reusable product?** A founding answer resolves like any setting [E-13]: the human's
profile answers when a line covers it — a personal-scope standing preference seeding this project's
default, and the seeding is SAID, not silent — asked otherwise; never derived from examples ("he named
three of his own artifacts" does not mean the product IS those artifacts; they may just be its first
users). This is deliberately STRONGER than the walk's proceed-on-default habit [INV-4, INV-12]: an
ordinary open question rides the row while the lane moves, but a founding answer blocks the FIRST wish
until asked or profile-read — every later sentence leans on it, which makes an inferred one the silent
micro-decision [INV-5] at its most expensive. Adoption owes the same questions at orient — A-1 carries
the pointer. (Born 2026-07-05: a fresh project was founded as "a personal agent for three artifacts" —
the reusable-product question was never asked, and the human's standing answer was reusable.) [B-2]

## Attaching to a live project (adoption)

Adoption is a sequence; each phase completes before the next. In practice the version-control gate [A-5]
is performed FIRST — before anything is touched or moved — so the whole run is reversible; the codes below
name meanings, not a frozen order (proven on the first real run, tlvphoto 2026-07-04). A phase marked
[target] is recorded-and-skipped until its machine lands — the run's journal names the deferral (the
pilot's baseline snapshot is the precedent). [A-0]

1. **Orient — read everything first.** Every existing document is read BEFORE anything is touched: README,
   any roadmap, any spec, any test suite, journals, TODO files, wikis in the repo. Adoption never assumes
   a blank slate — and it owes the project the founding questions (personal-vs-reusable first; the rule
   lives at the bootstrap [B-2]) about what it finds. [A-1]
2. **Inventory** — code, user-facing surfaces (seeding the host's surface registry [E-10]), and the
   document set from the orient pass, listed with owners (file:line for surfaces). [A-2] Adoption's
   working artifacts — the orient digest, this inventory, reconcile notes — live in the host's
   `.live-spec/adopt/`, tracked in git as the run's audit trail, never scattered into the host's own
   folders (the pilot polluted the host's `data/`). [A-8]
3. **Re-engineer the existing documents into live-spec shapes** — an existing spec becomes SPEC.md sections
   (original claims kept, marked unverified); the inventory's `file:line` pins seed ARCHITECTURE.md [E-14]
   (the nodes come from the real code structure, so the layer arrives at adoption, not as an afterthought);
   existing tests become matrix rows citing them at their real level, organized under those nodes [E-15];
   an existing roadmap/TODO becomes queue rows. Nothing existing is ignored, and nothing is trusted
   unreconciled. An unverified claim is reconciled (pinned to file:line, or removed) at the FIRST landing
   that touches its surface — and all remaining ones at the first milestone, whichever comes first. [A-3]
   One verdict is mandatory per unbacked LIVE surface: anything inventoried that reaches the user but has
   no spec backing — a de-facto prototype, the adopted host's most common residue — is flagged at orient,
   and the human decides per surface: **promote** (it enters at the spec step as a feature [INV-16]) ·
   **quarantine** (moved into a prototype home and labelled [E-17] — itself a production change: the human
   is choosing that users lose the surface or see it relabelled; the move leaves a dated one-line
   provenance record at the prototype home — what, why, date — the attic manifest's mirror) · **attic**
   [A-4]. [A-10]
4. **Attic, not deletion.** Any file superseded during adoption or rework moves to the **attic (attic/)**
   — the host's archive folder: append-only, one manifest line per file (what it was, why moved, date); on
   a basename collision the source dir prefixes the name, and a name STILL taken appends a numeric
   ordinal `-2`, `-3` — the pack's one collision law, stated once in the base skill (rule 18) [E-9].
   Flat-with-manifest vs dated subfolders is
   an open decision [D-1]. [A-4] The rule behind it never bends for anything authored: **no adopt or
   rework run deletes a host file** — superseded files move to attic/ with a manifest line. [INV-7]
   One exception, and only through a gate: adoption may OFFER a cruft sweep — clearly-regenerable junk
   (caches, build leftovers, already gitignored) listed with file counts and sizes, deleted only on the
   human's explicit OK, never silently; authored content never qualifies and always goes through the
   attic. [A-9]
5. **Version-control gate (done FIRST — see the note above).** If the host has no git: init it, write a
   `.gitignore` that excludes heavy generated/media artifacts, make a pristine baseline commit (this
   doubles as the diff baseline), and settle the remote as a NAMED deliverable: by the first landing a
   remote (GitHub) either exists or the human has explicitly declined one, and the outcome is recorded in
   the run's journal entry — a recommendation alone doesn't close the gate (the pilot ended local-only on
   a mere recommendation) [INV-8]. [A-5]
6. **Baseline snapshot [target]** — render/produce the current artifacts as they are and save them; this
   is the diff baseline the snapshot machinery [E-7] will guard. [A-6]
7. **Incremental thereafter** — the host now works by the same wish lifecycle as a bootstrapped project;
   installed skill versions are recorded in `.live-spec/` at attach time. **On any version change (live-spec
   or any installed skill), the agent RE-READS the changed SKILL.md before continuing** — never coasts on
   the stale in-memory version — and writes a one-line journal note naming old → new. The check is not
   event-only: at every safe breakpoint [M-2] the agent re-stats the installed skills and the package on
   disk (version / file mtime) and re-reads what changed — a parallel session may have shipped an update
   mid-flight. [A-7]

**How the skills arrive on a machine.** The pack ships one installer, `install.sh`: it copies every pack
skill into the agent's skills home (`~/.claude/skills/`), and it is idempotent — an existing copy is
backed up with a timestamp before being overwritten, never deleted — and the backup lands in an attic
folder BESIDE the skills home, never inside it, so the agent never scans a stale copy as a live skill
(the attic principle applied at install time). What the installer just wrote is exactly what A-7's record clause writes down in
`.live-spec/` — installing and recording are two halves of one seam. [E-21]

## One rulebook behind the skills

Open any skill of the pack and the same working rules greet you: ask, never guess; plain words with the
code trailing quietly; one surface = one name; one canonical home per fact; work a junior can resume from
a checkpoint after a cut-off. Until now each skill carried its own near-copy of those rules — and copies
drift (the pack's own sweep caught the anchor convention told two ways, and the concurrent-edit fence
stated only in the adoption text while every skill that writes shared files needs it).

**So the shared rules live ONCE, in the base skill** — the pack's shared rulebook beside the working skills (folder:
`live-spec-base`; pack structure decided: package-is-source, standalone repos read-only mirrors [D-4]). Every rule that belongs to every skill is stated there normatively, next to the
package's default settings [E-13]; each working skill opens with one line naming the base skill and the
base version it was written against — a pin the landing that bumps the base sweeps in the same session,
never leaves stale — and REFERENCES the shared rules instead of restating them. A working
skill elaborates only its own domain — communicator may teach HOW to speak plainly; THAT we speak plainly
is the base's sentence. A skill used standalone, outside the pack, still stands: the pointer reads as
plain advice and nothing in the skill's own domain depends on the base being installed. [E-12]

While the pack evolves, one thing is always true: **a shared rule has exactly one normative home — the
base skill; a second full statement inside a working skill is drift, a defect to fold, not a
convenience.** Restatements older than the base skill are pruned at milestones through the compaction pass
[M-1], skill by skill, never in one risky rewrite. [INV-13]

## Who decides what

**You (the human)** own taste, design, irreversible calls, publish/push gates, domain wording — and your
own working contract [INV-9]. [ACT-1] That contract is what the settings ladder RESOLVES to (next
paragraph): the lines about you — proactivity mode (ask-at-max | max-proactive), trust level, language,
domain vocabulary — live in your personal profile and follow you everywhere; the **host profile** at
`.live-spec/profile.md` narrows them for one project when you say so — created at attach, and git-tracked
in the host repo like the adopt artifacts [A-8]; of `.live-spec/` only the checkpoints stay ignored
[ACT-3] [E-8]. Communicator reads the resolved
contract, not any single file, before every human-facing exchange [E-13]. **Mode and trust are written
ONLY on your word — the agent may propose, never set; it never raises its own trust or proactivity
level.** [INV-9]

**"Did you actually do X?" is answered by walking the evidence — and the answer wears its method
version.** You ask whether something was done, adopted, true — "did that project run the tests by the
method?" — and a fluent story comes back; the story may even be right, but you cannot tell VERIFIED from
NARRATIVE, and that difference is the whole point of the method. So a done-claim is never answered from
memory: each claim in the answer is pinned to a checkable artifact — an adoption record, a prover
record, a suite run with its count, a git commit, a matrix row — walked NOW, not recalled (the
claims-need-primary-source rule applied to the answering exchange itself); what the walk verified is
said apart from what is merely asserted, in plain words; and because "done by live-spec" means nothing
without a version, the answer names the METHOD VERSION the work was done by — the pack and skill
versions read from that host's installed set (the version homes, [M-7]). One claim line reads
claim → artifact → version: "suite green — 795 tests, tonight's run, commit `193d39d` — done by
live-spec 0.8.x, prover 0.1.8". And where the host HAS no installed set — never adopted, or the work
predates adoption — the answer says exactly that in plain words: an absent version is itself an honest
answer, never an invented one. Born 2026-07-05: the track-coach answer was right, and he still could
not tell which half of it was checked. [INV-25]

**Settings climb a ladder of four NESTED scopes — the narrowest word wins.** Every way the pack behaves
for you is a named setting with a home in exactly one scope, and the scope is chosen by what the setting
DESCRIBES: about the pack itself → the **package defaults**, each value stated in the base skill beside
the rule it tunes [E-12]; about YOU, following you across every project (language: docs and commits vs
conversation · proactivity mode · trust · your domain vocabulary) → your **personal profile**, one file
per human at `~/.claude/live-spec/profile.md`; about THIS project → the **host profile** [E-8]; about
RIGHT NOW → the **session scope**: your live word in one conversation. The scopes nest — the package
holds every human, a personal profile holds every project that human touches, a host holds every session
run inside it — and a setting set at a broad scope is INHERITED down through the narrower ones until a
narrower one overrides it on your word (an all-English project overriding your Russian-chat line; a
"today answer me in English" overriding both for one sitting). Resolution therefore reads from the
narrowest scope out: session beats host beats personal beats package default. Profiles are re-read at
the same freshness points as skills [A-7]; a profile line the current pack does not recognize (written
under an older vocabulary) is ignored ALOUD — a dated note in the host's journal plus a line in the
session's next report (the journal half is durable, so a session dying before its report still leaves
the trace), never a silent drop and never an error. [E-13]

**No override is ever silent.** An override exists only as a written line in its profile file, and
setting one leaves a dated journal note in the home it governs — the host's journal for a host line, the
package's for a default change. This is the no-silent-micro-decisions rule [INV-5] applied to settings;
live-spec's own push gate [M-6] is the worked example: the package default says a full prover pass before
a MINOR bump, and live-spec's own host contract tightens it to "before every push" — recorded, visible,
never assumed. The session scope is the one that is never a file: a session override lives only in your
spoken word and dies with the conversation — the agent never writes it anywhere on its own; if it should
outlive the session, that is a PROMOTION into the profile it describes (personal or host), made on your
word and journaled like any other override. An announced self-compaction [M-2] carries the live session
lines forward in its summary; a full wipe ends the sitting — session lines die with it by design, and
that loss is your own move, never the agent's. [INV-14]

**Your profile is the ONE home of the personal layer; the global instruction file is a thin loader.**
Everything personal — who you are, how you like to be spoken to, your standing working rules — lives in
the personal profile, never scattered across always-on instruction files. The machine-global instruction
file (on this stack, `~/.claude/CLAUDE.md`) shrinks to a thin loader: the pointer that loads the profile,
plus ONLY the bootstrap lines that must hold before any pack file is read — the which-project
disambiguation rule is the type specimen: the rule that stops a session writing into a foreign repo
cannot itself wait for that repo's files to load. The loader is those bootstrap lines' ONE home; the
profile never restates them [INV-13]. Migrating an existing rule file into this shape is a
fork by scope — each rule moves to the scope it describes: a method rule the pack already states stays
the pack's (a second copy is drift [INV-13]); a personal line → the profile; a project line → that
project's host profile — proven lossless by a rule-by-rule mapping, with the old file kept in the attic
[INV-7] so one move rolls the whole change back. And the fork only WRITES what the running session owns:
pack rules land in the pack, the personal profile lives on the human's machine outside any host or pack
repo (a PRIVATE repo the human owns may serve as its git home; sitting outside any repo fence [INV-11],
a promotion RE-READS the file immediately before appending, and that git home is its recovery net);
a project line becomes a written migration note that the project's OWN session lands at its next update —
nothing in this migration writes a foreign repo [INV-10]. [E-16]

**The senior agent** owns judgment: spec deltas, matrix levels, findings triage, this document. [ACT-2]

**Workers (tiered) [router: target]** own mechanical execution, with persistent checkpoint files in the
host's `.live-spec/checkpoints/` (gitignored; never /tmp — a reboot must not erase a resume point); the
cheapest sufficient tier does the job (haiku one-shot / sonnet multi-step / senior judgment), budget-aware.
Whether the queue's size class fixes the tier mechanically or the senior may override is an open decision
[D-2]. **The worker contract** binds every delegation: a worker inherits its session's write-ownership
[INV-10] NARROWED to the files its brief names — outside them it reads but never writes; files a
same-session SIBLING worker just wrote are fence-benign — the concurrent-edit fence [INV-11] alarms on
foreign sessions, not on your own briefed hands, and the senior who briefed both owns their seams; the
session's live setting lines [E-13] ride INTO the brief verbatim (a worker never resolves the ladder
itself — it cannot hear the human's spoken word); the brief ARMS the worker for the workshop — it
carries the host's problem-ledger path with the WATCHED-line duty (noise the worker hits goes into its
checkpoint as a ledger line — signature, date, one line of context — never a silent retry; the senior
carries the lines into the ledger at verify unless the brief names the ledger among the worker's files
[INV-23]), and it carries the CLOCK — the date and time read at briefing — so a worker's stamps come
off the brief's clock, never invented [INV-24] (the day the briefs carried no clock, both eval arms led
their reports with a wrong hour, 2026-07-06); and a result that fails its brief's acceptance escalates
ONE tier with a logged line (haiku → sonnet → senior), never a silent retry on the same tier, never a
skipped rung. [ACT-3]

## From the spec to the tests: two layers that must not be skipped

The spec says WHAT the product is; tests prove facts about the shipped artifact. Between them live two
documents that were once implicit — and an implicit layer is a lost layer (Alexander caught the gap
2026-07-05: the pack taught a matrix template but not the layers that produce it).

**The architecture doc (ARCHITECTURE.md)** — how the product is BUILT: a short list of named nodes
(pipeline stages, modules, the owners of surfaces), one responsibility each, one name each — the
one-surface-one-name rule applied to structure. Every spec fact is OWNED by exactly one node; in a live
codebase every node pins to its owning place — the NORMATIVE pin is the named thing (a function, a
marker comment, a selector, a section heading), the `:line` beside it is a convenience cache that may
lag; a reader resolves the name, and a drift check re-greps it (pins rot silently otherwise — a real
host drifted 7 of 17 pins in ONE working session, and a wrong-with-confidence pin is worse than none).
Drafting the architecture IS where spec claims
get reconciled against shipped reality (each pin comes from a command actually run, never from the doc's
own prose). It is written from the proven spec (template: `ARCHITECTURE.template.md`) and — like the spec
— it is PROVEN before anything derives from it: a product-prover pass with the architecture lens (every
spec fact has an owning node · no node stands without spec backing · the seams between nodes are named).
A large or surface-class wish updates the doc before the matrix is touched; a bug or small wish cites the
existing node it lands in — or, when its fact has no owner yet, ASSIGNS it to the fitting existing node
(recorded in the doc; an assignment alone triggers no re-prove) — so no fix is ever the thing the rules
forbid to land. The doc is re-proven when its structure CHANGES, not on every landing. And it is
ITERATIVE, like the spec it serves: it maps the product as it stands plus the landing in flight — a node
exists for what ships today, or for what the spec already promises under an owned queue row (marked
[target] with an empty pin); it is never designed several milestones ahead. A future feature earns its
node when its landing arrives — speculative nodes are unbacked structure, the architecture's version of
a silent micro-decision. [E-14]

**The test spec — the matrix is DERIVED, never just filled.** The matrix [E-5] is not a bucket of rows.
Derivation is a method with a checkable output: rows are organized **architecture node × spec fact**,
every fact gets at least one row, every row pins a test level — and the derivation closes with the
**coverage validation** — the checklist whose normative home is the matrix template, actually walked:
every spec anchor appears in ≥1 row · every artifact-inventory entry owns ≥1 rendered-level row · every
visibility/layout/colour/interaction fact sits at level ≥ browser-computed · every node carries its
negative-side rows [INV-6] · no row cites an anchor or node that no longer exists (stale rows retire,
never vanish). A fact with no row, or a row at a too-weak level, is a derivation defect — caught at
derivation time, not by the user. [E-15]

While both layers live, one thing holds: **no wish lands whose facts lack an owning architecture node and
a matrix row at the right level** — the bridge from spec to tests is walked layer by layer, never jumped.
A project that predates these layers — this pack itself included — brings them up as an OWNED landing:
the invariant binds from the landing that creates its ARCHITECTURE.md and matrix, never retroactively
(the pack's own bring-up is queue row 50). [INV-15]

## The machines that hold the bounds

What keeps "it works" honest, each one a named machine:

- **The matrix (TEST_MATRIX.md)** — at least one row per fact, each row pinned to a test level; organized
  architecture node × spec fact, produced by the derivation method above [E-14, E-15]. [E-5] Every row states the
  positive AND the negative side — what the fact does and what it must never do; the negative side is the
  regression fence. [INV-6]
- **The guardrails** — the mechanical checks wired to the pre-push hook. Live for the pack repo itself:
  a today-dated prover record exists · the suite is green · every anchor owned by exactly one node · no
  unchecked matrix-coverage box · the prototype fence (no prod file references into a prototype home
  [E-17, INV-17]), plus the opt-in concurrent-edit fence on commit. Still [target]: the
  host-facing set — completeness (against the surface registry) · tests-present · behaviour-traces-to-spec
  · declared-scope diff vs snapshot. On a host, hooks are OFFERED, never imposed: only where the host uses
  git at all, and installed only after asking the human — with a plain-words explanation of what the hook
  will check and block, because the human may not know what a git hook is (Alexander 2026-07-05). [E-6]
- **The snapshot [target]** — the saved artifact of the last accepted run (HTML, JSON, files, numbers —
  any product), the baseline the next run is diffed against. The baseline advances only at *landed*, and
  only for the surfaces the change DECLARED; undeclared surfaces keep the old baseline — that asymmetry is
  what catches the unasked change. Retention (last-only vs last-N) is an open decision [D-3]. [E-7]
- **Design-sync [target: the machine; the wiring is live]** — an OPTIONAL machine for hosts with
  visual components: it syncs the components a landing DECLARED (the same declared-scope notion the
  snapshot diffs by [E-7]) to the team's design project (claude.ai/design), where the human reviews
  rendered cards. It SUPPLEMENTS the in-session render — the real render stays the authority for the
  landing gate; the design project is the team-review channel. WIRED today (row 93's pack-side half):
  the switch lives off-by-default in the base skill's defaults table [E-13] under the name
  `design-sync` — a host turning it on writes a recorded profile line [INV-14] — and the channel lines
  stand in communicator (where the cards go, after the gate) and in the pipeline's commit-and-show step
  (when a sync fires). STILL [target]: the machine itself — the first real sync on a visual host, shown
  working through the human's gate, closes row 93. Every sync is gated by the human because a sync
  PUBLISHES outside the machine [ACT-1]. The pack itself, a text product, never syncs — and the
  work-kind axis is what says so mechanically [T-16]: the machine applies to product-kind work on a
  visual host; every other kind stands it down by name [INV-22]. [E-18]
- **The skill evals** — the pack's own skills are tested like any shipped artifact, at the level that
  matters for a skill: BEHAVIOUR. Each working skill owns at least one recorded eval — a scenario where
  a bare session (the skill not loaded) demonstrably errs and the skill's text corrects it: the skill's
  own red-first test, proven red at authoring with a dated run record, never asserted from belief. The
  eval home is `evals/` in the pack repo — one file per skill stating the scenario prompt, the recorded
  bare failure (date + run record), what a with-skill run must show, and the checks a re-run walks.
  Evals re-run at milestones (the M-1 list carries the item) and at any landing that changes a skill's
  own BEHAVIOUR — a bump that only sweeps a pin or version line owes no re-run. The law binds from this
  landing: a working skill without its eval is a defect the milestone audit flags. [E-19]
- **The surface registry [target]** — one named list per host of every user-facing surface, and the
  PREFERRED form is executable: the list lives as a declared map inside a completeness-gate test, so a
  mismatch IS a failing test in both directions (rendered-but-unregistered · registered-but-empty); the
  `.md` file stays the honest fallback for a host with no test harness (a real host arrived with the
  executable form already working — adoption recognises it as satisfying this machine, never asks it to
  step backwards into a document). The completeness check
  scans the real rendered artifact against it; a surface that renders but isn't registered is RED, so the
  registry is self-closing, never a trusted hand-list. [E-10]

## The package repo: who may write, and two sessions at once

live-spec eats its own cooking — this spec, this queue, these rules govern live-spec's own development,
and the pack repo's own push gates run mechanically on the installed hooks (a fresh prover record, a
green suite, anchor ownership, matrix coverage — `guardrails/`); the host-facing checks stay [target]
with E-6. [M-4] That makes its repo a shared surface, and one evening
of two parallel sessions taught us the rules:

**The developer's own machine keeps its skills fresh by name, not by habit.** The repo is the source
[D-4]; the installed copies under the agent's skills home are mirrors — and a session that edits a
skill syncs the installed copy the SAME session, through the named tool: `scripts/sync-skills.sh`,
which copies each repo skill over its installed twin and reports every version change old → new — the
exact line A-7's re-read rule fires on. A hand-copy is the anti-pattern the tool retires: it syncs
silently, so nothing tells the next breakpoint what changed. [E-23]

**Only a session you assigned to live-spec itself writes this repo** (spec, queue, journal, skills,
templates, adopt procedure). Every other session — a host adopt run, a skill install, anything that merely
reads the package — is read-only here, with exactly one exception: creating a new wish file in the inbox.
The test is crisp: if the session cannot say "the human asked ME, in this conversation — or via a standing
routine the human created FOR live-spec — to change live-spec", it does not write. A host run's story lives
in the HOST's journal, never here. [INV-10]

**The inbox (inbox/)** is the parallel-safe intake door for wishes born outside a live-spec session: one
NEW file per wish (`YYYY-MM-DD-<source>-<slug>.md`; name taken → append `-2`, `-3`, … — the same one
collision law, base rule 18; two sessions racing one slug add a short session token to the source mark),
a few plain lines,
never an edit to an existing file — creating a fresh file cannot collide, shared files can. The outsider
COMMITS its one new file (a commit touching inbox/ only, message naming the source) — that commit is
inside the read-only exception. The door is host-general: every host carries its own inbox/ under the
same law, swept first by that host's own sessions — that is what keeps "no wish is ever lost" [INV-1]
true when two contributors' sessions share one host. [E-11] A live-spec session sweeps the inbox as its FIRST act and harvests
each file into a queue row — a wish must not wait durably-recorded but operationally invisible; the
harvest commit removes the file (git history keeps it — this internal removal is not an attic case, which
protects HOST files). Each harvest is ONE commit that both adds the row and removes its file — the row
names the source file, so an interrupted harvest (nothing committed) leaves the file untouched for the
next sweep, which harvests it exactly once — a committed harvest leaves no file behind to re-harvest. So
"spoken means it exists" holds without the outside session touching the queue. [T-10]

**Before writing to a repo — and again before every commit** — the agent re-checks `git status` + HEAD
against what it last read. If HEAD moved or the tree holds changes it did not make: STOP, re-read the
changed files, and only then proceed surgically — or back off to the inbox. New files under inbox/ are the
expected benign case, not a fence trip. Never push while another session is known to be live in the repo —
push coordination belongs to the human. Applies to live-spec AND to any host repo two sessions might share
(the concurrency axis of the composition rule, made mechanical). [INV-11]

## The rhythm: breakpoints, milestones, pushes

- **Safe breakpoint (end of every movement):** NEXT_STEPS live-state replaced (never stacked) + dated
  JOURNAL entry + committed ⇒ the session memory can be wiped with zero loss (NEXT_STEPS may be
  gitignored — the journal entry is the durable safety net). A long session SHOULD take
  that offer: at a breakpoint the agent compacts its own context to keep working — and SAYS so, never
  silently; a full wipe/clear of the conversation is the human's move, not the agent's. On the way back
  in, re-check skill freshness [A-7]. [M-2]
- **Milestone (MINOR gate):** full spec re-prove + matrix audit (the coverage validation [E-15] re-walked
  against the CURRENT spec + architecture) + surface-composition check + the skill evals re-run [E-19] + doc
  COMPACTION (pruning: redundancy removed from spec/matrix/queue/skills/ledger [E-24], and the TEST SUITE swept the
  same way — a duplicate or superseded test is deleted only when the matrix audit shows its rows still
  covered by a live test; nothing grows unboundedly, docs or suite;
  queue compaction ARCHIVES closed rows, never deletes [INV-1]) + a
  re-listing of every open human gate AND every unharvested inbox/ file, one line each, so a waiting wish
  is never forgotten + the formal index re-checked against the prose (the index is a derived map and must
  never drift into a second truth) + the derived docs' headers re-pinned to the spec version then proven
  + **the thin loader stays thin** [E-16]: the personal layer's global instruction file is re-read line
  by line, every line must pass the "must this hold BEFORE any pack file loads?" test, and the audit
  report states the line count — a rule that survives there without passing the test migrates to its
  real home (profile or pack), never lingers. [M-1]
- **Documents are versioned** like code: the queue and this spec carry dated versions, so "decided under
  which roadmap" is answerable. [M-3]
- **Time is read off the clock, never invented.** Every date a session writes — a file name, a journal
  or queue stamp, a ledger occurrence — comes from the machine's clock at write time; in doubt, git is
  the arbiter. The fence is mechanical, in the suite (and so in the pre-push walk): no repo file NAME,
  no journal entry heading, and no ledger date may sit LATER than the current clock — a future-dated
  stamp is red, not a style nit; prose QUOTING a past incident's wrong date stays legal. And the fence
  has a second arm for the family's TIME variant (the date fence cannot see same-day times, and the
  hand guessed them ahead three sessions running): at COMMIT, an ADDED line that pairs today's date
  with a clock time LATER than the commit moment is red — "pairs" means the ADJACENT stamp shape
  (`date [~]time`), so a line legally quoting other moments' times beside today's date stays green
  (the fence's own first live run proved the broader reading wrong — it flagged the ledger's history
  lines); the commit clock is the reference, so the check is not racy; the known cost, taken
  deliberately: a future plan is spelled without writing it as a date-time stamp. And the family has a
  CHAT face no mechanical fence can reach: a human-facing timestamp — the [HH:MM] a reply leads with,
  any moment spoken to the human — is read off the clock AT WRITE TIME, never continued or extrapolated
  from an earlier stamp (mid-session leads ran up to seven minutes fast, twice in two days, 2026-07-05/06);
  where no fence exists the rule is stated as law where the human-facing exchange shapes live — the
  communicator skill — and quoting a past moment's recorded time stays legal on this face too. (The
  invented-time family: six catches in two days, hand-swept twice before the fences.) [INV-24]
- **Versions have named homes.** The package: a `VERSION` file at the repo root. Each skill: a version
  line in its SKILL.md frontmatter, under `metadata:` — where the skill-format validator reads it. A host: the installed set recorded in `.live-spec/` at attach and on
  every update. So the freshness check [A-7] compares version against version, not just file times, and
  its "old → new" journal note is finally writable. [M-7]
- **CI mirror [target]** — the guardrails' native home is the local pre-push hook; a host may additionally
  mirror the same checks in its CI (Jenkins, GitHub Actions) as a second net. Same checks, one source of
  truth — CI runs them, never redefines them. (ROADMAP row 14.) [M-5]
- **Push gate for live-spec itself** — this repo is public and is the method's own flagship, so EVERY push
  is preceded, in the same session, by (a) the concurrent-edit fence [INV-11] and (b) a fresh whole-spec
  re-check: a product-prover pass over SPEC.md as it stands, its record landing in docs/prover/ before the
  push (record name `YYYY-MM-DD[-suffix].md`; suffix mandatory when the date's file exists). Findings that
  are must-fix fold before pushing; folds produced by the gate's own pass do NOT re-trigger the gate — they
  ship with the same record; the rest become queue rows. No re-check record for the pushed state ⇒ the
  push should not have happened. The record ENUMERATES the folds applied from its own pass, and a fold
  stays LOCAL to the sections its finding named — a fold reaching wider re-triggers the gate. [M-6]

## Publishing — the deposit owes what its kind owes

Sooner or later a piece of work leaves the machine: a repo goes public, a skill enters a plugin
directory, a release is cut, rendered cards go to a design project. **Publication is a surface of its
own, and it owes the reader what the artifact's KIND owes** — the same work-kind axis [T-16], read at
the door instead of the intake: a **skill** shows how to install it, the commands to run, when to use
it (and when not); a **tool** shows real runs with real output; a visual **product** shows FRESH
screenshots — a stale screenshot is a false claim in picture form; **prose** shows its reading path. A
comparison or a diagram joins when it carries the argument, never as decoration. The per-kind publish
checklist has ONE normative home — the publish skill, the pack's fifth working skill [E-12]; this spec
binds the contract: nothing is deposited outward past the checklist, and the walk's result rides the
landing report like any step [INV-22]. **Each publish TARGET is a plugin that embeds its own steps
into the walk** (Alexander 2026-07-05: a GitHub plugin brings its stages): GitHub brings
README-at-the-door + release notes; a plugin directory brings its manifest and forms; the design
project brings its cards [E-18] — the target adds steps, it never removes the kind's owed minimum. And
publishing never bypasses the gates that already stand: the human's publish gate for anything
irreversible or outward (base rule 17 [ACT-1]), the host's own push gates [M-6] — the checklist runs
BEFORE the gate, so what the human approves is already worth approving. [E-20]

## Composing across axes

Every stateful surface of a host is composed across the canonical axes (view · mode · tier · viewport ·
persistence/reopen · concurrency where real) — and adoption adds one axis of its own: **document
provenance** (native-live-spec × re-engineered-from-existing), because a re-engineered claim behaves
differently (unverified until reconciled per the adoption rules [A-3]) from a native one. [C-1]

## Open decisions

- ⟨DECIDE⟩ attic/ layout: flat with a manifest and source-dir prefix on collision (current pick) vs dated
  subfolders — revisit at the next real adopt run. [D-1]
- ⟨DECIDE⟩ whether the queue's size classification also fixes the model tier mechanically, or the senior
  may override per wish (current pick: router proposes, senior may override, override is logged). [D-2]
- ⟨DECIDE⟩ snapshot retention: last-only (current pick) vs last-N — revisit when a diff dispute needs
  history. [D-3]
- Decided 2026-07-05 (page 2): pack ↔ standalone-skill-repos structure is **package-is-source** — the
  pack repo is the single truth, standalone repos become read-only mirrors (Alexander's note: reusable
  parts must stay findable alone — exactly what mirrors give). The folder-NAME half had closed earlier
  the same day (`live-spec-base`). Execution: queue row 51 (mirrors + one sync command). [D-4]
- Decided 2026-07-05 (page 2): the personal-settings split is **all-into-profile** — everything personal
  moves into live-spec settings with servlet-style scopes (nested, inherited), CLAUDE.md shrinks to a
  thin loader, and setup gains an "understand who you're working with" onboarding step. The scope model
  and the thin-loader shape are spec'd (the ladder and profile paragraphs above, 2026-07-05, rows 52–53);
  the onboarding step remains row 54's landing. [D-5]

## Formal index

Machine handles → home section. For the prover, the matrix, and transcript greps; the prose above is the
meaning, this table is only the map.

| Anchor | One line | Section |
|---|---|---|
| S-0 | shipped vs target marked honestly | header |
| E-1 | host project + its `.live-spec/` | What live-spec is |
| E-2 | wish: plain words, any moment | Throwing a wish |
| E-3 | queue ROADMAP.md, one row per wish | Throwing a wish |
| E-4 | spec: living truth, one surface = one name | Throwing a wish |
| E-5 | matrix: fact × test level | Machines |
| E-6 | guardrails on the pre-push hook [target] | Machines |
| E-7 | snapshot baseline, declared-scope diff [target] | Machines |
| E-8 | host profile at `.live-spec/profile.md` | Who decides what |
| E-9 | attic: archive, never delete | Adoption step 4 |
| E-10 | surface registry, self-closing [target] | Machines |
| E-11 | inbox: one new committed file per outside wish | Package repo |
| E-12 | base skill: shared rules + defaults, stated once | One rulebook |
| E-13 | settings ladder: four nested scopes, session > host > personal > package default | Who decides what |
| E-14 | architecture doc: named nodes own spec facts, pinned to file:line, proven | From spec to tests |
| E-15 | test spec: matrix derived node × fact, coverage validated per level | From spec to tests |
| E-16 | personal layer lives in the profile; global instruction file = thin loader | Who decides what |
| E-17 | prototype: fenced home, visible label | A prototype is not the product |
| E-18 | design-sync: machine [target], wiring live — off-by-default switch in base defaults, channel lines in communicator/pipeline, human-gated (publishes) | Machines |
| E-19 | skill evals: per working skill one scenario, red proven bare, corrected by the skill; re-run at milestones and behaviour changes | Machines |
| E-20 | publishing owes the artifact's kind its checklist (one home: the publish skill); targets are plugins embedding their steps; gates untouched | Publishing |
| E-21 | installer: install.sh copies skills to the skills home; timestamped backup, never deletes | Adoption step 7 |
| E-22 | batched questions arrive as ONE decision page; answers archived and harvested same session | Throwing a wish |
| E-23 | dev-machine skill sync: named script, version changes reported old → new for the A-7 re-read | Package repo |
| E-24 | problem ledger: per-host `.live-spec/PROBLEMS.md`, signature + dated occurrences + status (WATCHED/OWNED/AGREED NON-PROBLEM/SOLVED) | Workshop misbehaves |
| T-1..T-7 | arrived → … → landed → reported | Throwing a wish |
| T-8 | exits: declined / deferred / superseded | Throwing a wish |
| T-9 | bug preempts, wish parks with checkpoint | Bug cuts the line |
| T-10 | outside wish arrives via inbox, swept first | Package repo |
| T-11 | priority bends the lane order, visibly; one bubble then the queue head | Throwing a wish |
| T-12 | the door is named before any code | Throwing a wish |
| T-13 | feature spec step sweeps the standard facets (phone/touch/empty-error-loading/a11y/perf) | Throwing a wish |
| T-14 | touching a live surface: spec-delta opens with regression fences citing existing clauses | Throwing a wish |
| T-15 | scope, never time: a too-big wish is cut or staged (a time budget/estimate is never an input); proposals proceed on the recommended option, surfaced; the safety net uncuttable | Throwing a wish |
| T-16 | work-kind named at intake: product / infra / skill / prose; one kind per wish; curated vocabulary; host default in its profile | Throwing a wish |
| T-17 | one wish = one user story: multi-story wishes split at intake, each story its own row; sub-behaviours are acceptance, not stories; unclear count asked | Throwing a wish |
| INV-1 | no wish is ever lost | Throwing a wish |
| INV-2 | one landing at a time | Throwing a wish |
| INV-3 | every landing cites its row | Throwing a wish |
| INV-4 | a pending question never blocks the lane | Throwing a wish |
| INV-5 | no silent micro-decisions | Throwing a wish |
| INV-6 | matrix rows state DO and NEVER sides | Machines |
| INV-7 | authored host files: attic, never deletion | Adoption step 4 |
| INV-8 | no landing into an unversioned host | Bootstrap |
| INV-9 | trust set only by the human | Who decides what |
| INV-10 | write-ownership of the package repo | Package repo |
| INV-11 | concurrent-edit fence before write/commit | Package repo |
| INV-12 | ambiguous size/priority/work-kind is asked at intake, never guessed | Throwing a wish |
| INV-13 | one normative home per shared rule: the base skill | One rulebook |
| INV-14 | no silent override; every profile line recorded + journaled | Who decides what |
| INV-15 | no landing without an owning node + a right-level matrix row | From spec to tests |
| INV-16 | feature tripwires are hard, not judged; casual asks still route | Throwing a wish |
| INV-17 | prototype fence one-way; build⊆spec honesty (fence live, other legs [target]) | A prototype is not the product |
| INV-18 | every facet ends as a spec sentence — decided, or `[default]`-tagged + reported | Throwing a wish |
| INV-19 | a fence cites its clause and discharges through that clause's existing never-side; fences named by anchor in the wish's row | Throwing a wish |
| INV-20 | the non-goals sentence is always written ("nothing left out" is valid); scope-narrowing non-goals ride the batched report | Throwing a wish |
| INV-21 | every feature states one success measure, decided or `[default]`-tagged (provenance only, no row yet); reading machinery [target]; binds forward | Throwing a wish |
| INV-22 | kind scales each step's FORM; a step applies or stands down BY NAME in the landing report — never a silent skip; the safety net is kind-proof | Throwing a wish |
| INV-23 | workshop noise: first sight = WATCHED line (never a silent retry); second occurrence gets an owner that moment (row, or the human's agreed non-problem); a third unowned recurrence is a METHOD defect → the pack's queue | Workshop misbehaves |
| INV-24 | time read off the clock, never invented: no future-dated file name, journal heading, or ledger date (suite fence) AND no added line pairing today's date with a time past the commit clock (pre-commit fence) AND the chat face: a human-facing timestamp read at write time, never extrapolated (law in communicator, no mechanical fence); quoting a past wrong date or time stays legal | Rhythm |
| INV-25 | a done-claim is an evidence walk: claim → artifact → method version, walked now; verified vs asserted said apart | Who decides what |
| INV-26 | a row closes only whole: per-leg Done-when, no close with an unmet leg; LIVE-STATE supersession never compresses an open leg away | Throwing a wish |
| INV-27 | every intake is echoed back in one sentence (heard · door · name · row; silent arrivals echo in the next report); every status report names each in-flight feature's pipeline station | Throwing a wish |
| INV-28 | echo-names are plain descriptive phrases; a report line opens with the reader's outcome; every handle (codes, numbers, coined names) only trails; one fact = one standalone sentence; NEVER-list: bookkeeping numbers (test counts, suite sizes, version strings) never as message content — translated, trailing, or in the records; the done-claim walk [INV-25] keeps them as the answer | Throwing a wish |
| INV-29 | a feature-doored wish walks the kind-scaled FIT WALK at intake (journey / flows / trigger lenses); trivially-closable holes closed and written how; only genuine taste calls go out, batched; prover mode FEATURE-FIT | Throwing a wish |
| INV-30 | product-kind verify includes the visitor walk + feel pass against the prototype bar, in the medium's own form (motion for a browser, reading path for a book); findings become rows or red | Throwing a wish |
| INV-31 | a taste choice made without asking is told in the landing report — plain words, an example, a tweakable mark; no confirmation, silence is consent, never re-asked; the [default] tag keeps it findable | Throwing a wish |
| INV-32 | a decision card opens with what the choice changes for the person; options labelled by consequence, mechanism only if it helps | Throwing a wish |
| INV-33 | every pipeline step is worked wearing its craft's head (product manager at spec · architect at architecture · QA automation at matrix and tests · senior developer at code · the visitor's own eyes at verify); the step→craft ladder's one home: build-pipeline | Throwing a wish |
| INV-34 | the pre-report walk: before any movement-end/milestone report, the communicator rules are re-read and the draft passes phrase by phrase through the outside-reader question; trailing anchors stay legal; acceptance = the reader's own read; the walk's one home: communicator | Throwing a wish |
| B-1 | bootstrap: templates → gate → first wish | Bootstrap |
| B-2 | founding questions asked, never inferred — personal-vs-reusable first; profile answers when it can | Bootstrap |
| A-0 | codes name meanings, VCS-gate runs first | Adoption |
| A-1 | orient: read everything first; owes the founding questions [B-2] | Adoption step 1 |
| A-2 | inventory code + surfaces + docs | Adoption step 2 |
| A-3 | re-engineer docs, unverified until reconciled | Adoption step 3 |
| A-4 | superseded files move to attic | Adoption step 4 |
| A-5 | version-control gate | Adoption step 5 |
| A-6 | baseline snapshot [target] | Adoption step 6 |
| A-7 | re-read changed skills; re-stat at breakpoints | Adoption step 7 |
| A-8 | adopt artifacts live in `.live-spec/adopt/`, tracked | Adoption step 2 |
| A-9 | cruft sweep: gated, listed, regenerable-only | Adoption step 4 |
| A-10 | unbacked live surface at adoption: promote / quarantine / attic | Adoption step 3 |
| ACT-1 | the human: taste, gates, wording | Who decides what |
| ACT-2 | senior agent: judgment | Who decides what |
| ACT-3 | tiered workers, checkpoints; every brief carries the ledger walk + the clock [router target] | Who decides what |
| M-1 | milestone: re-prove + audit + compaction + gate list | Rhythm |
| M-2 | safe breakpoint; announced self-compaction | Rhythm |
| M-3 | documents versioned like code | Rhythm |
| M-4 | live-spec is its own host | Package repo |
| M-5 | CI mirror of the same checks [target] | Rhythm |
| M-6 | push gate: prover re-check before every push | Rhythm |
| M-7 | version homes: VERSION file · SKILL.md frontmatter · host record | Rhythm |
| C-1 | canonical axes + provenance axis | Composing across axes |
| D-1 | attic layout | Open decisions |
| D-2 | tier routing override | Open decisions |
| D-3 | snapshot retention | Open decisions |
| D-4 | pack structure: package-is-source decided; mirrors = row 51 | Open decisions |
| D-5 | all-into-profile decided; rows 52–54 execute | Open decisions |
