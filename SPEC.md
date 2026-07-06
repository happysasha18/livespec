# live-spec — SPEC (v0.15.48, 2026-07-07)

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
snapshot machinery [E-7] (the adoption baseline A-6 rides it), the model router
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
пайплайну".) The echo carries one more part — the wish's place on the product's map; its law lives in
the next paragraph [INV-37]. [INV-27]

**Every wish is also PLACED on the product's map — "this changes feature X", "this is a new feature",
or "the shape no longer fits" — and the placement is spoken, out of the box.** The echo above says what
the work IS (heard · door · name · row); the same breath says WHERE it lands. The map is not a new
document: the spec's scenario sections and the architecture's nodes ARE the product's feature map
[E-14] — this law only makes the until-now implicit mapping SPOKEN. Three verdicts exist: **changes an
existing feature** (the delta grows that scenario, names it) · **a new feature** (a new scenario
section, and at the architecture step its own node) · **restructure** (the wish fits no existing
carving cleanly, or fitting it in shows the modules have outgrown their shape — his words: the moment
of «формирование продуктовой модульной архитектуры»). A restructure verdict never re-carves in
passing: it queues its OWN row (refactor door when only structure moves; feature door when behaviour
moves with it), and the re-carve walks the architecture step with its re-prove [E-14] — the placement
may SAY the shape no longer fits, only a landing may change the shape. A bug's placement is the
feature it repairs; a wish whose feature the classifier can't call is asked like any uncallable axis
[INV-12]. And the verdict is WRITTEN as well as spoken: the wish's queue row carries a `map:` note —
changes X · new · restructure — so placement stays greppable after the echo fades, the way the fences
stay greppable in their rows [T-14 kin]. (His word 2026-07-06: «когда приходит новый запрос, ты должен понять, к какой фиче
относится — меняем ли фичу, пишем ли новую, нужна ли структуризация… я ожидал бы, чтобы это было
понятно из коробки».) [INV-37]

**The outcome does the talking: names are chosen plain, and every handle trails.** The first real
departures board passed its eval and failed its READER — lines led with coined metaphor-names
(«Прогулка по уликам», «Часы получают зубы») and row numbers he never opens, and squeezed facts into
riddles only their writer could parse ("seven times — twice the fence"; 2026-07-06 morning, the jargon
family's third strike in two days). Two arms, one law. NAMING: a feature's echo-name is a short
DESCRIPTIVE phrase in the product's own words — what the thing does, parseable cold by a reader who
missed its birth — never a private metaphor; a name that needs its story told first is a handle, not a
name. LINES: a human-facing report or board line (chat reports, narration lines [INV-35], report pages,
decision pages, the capture echo — method-internal docs keep their anchors) OPENS with what changed for the reader — what
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
the answer, not as bookkeeping. And because this law and the narration law live in skills a window
may never load (the day the field showed it: three windows leaked raw codes to their reader in one
day, 2026-07-06), they have a mechanical VOICE on the working machine: a prompt hook
(`scripts/chat-law-hook.sh`, installed beside the clock's hand by the human's own command) injects a
one-line reminder of both laws into every prompt — the skills remain the laws' homes, the hook only
reminds and never legislates, and a window that ignores the line is breaking the same law, not a
different one. [INV-28]

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

**Work is narrated while it runs — the third voice between the echo and the report.** The intake has
its echo [INV-27] and the landing has its report [INV-28], but between them a working session used to
go quiet, and the human — who leads several windows at once — was left reading silence. His word came
twice in one day (2026-07-06): the morning ask wrote a personal-profile line, and by afternoon the ask
returned ("не забывай отчитываться и по ходу действия… это должно быть и в проекте коммуникации
зафиксировано") — a habit held only in a personal profile did not carry across sessions, so it is pack
law. While work runs, each beat worth a sentence — a pipeline station just passed, a load-bearing
find, a change of direction — is SAID as it happens: one or two plain sentences in the roadmap's terms
(which wish is in hand, what it gives, what just moved), the same voice as the reports. The mechanical
grind stays quiet — narration marks beats, never a per-command commentary. His third word in the
family (2026-07-06 evening — the landing reports had become good and the mid-work trail was still
thin: «заход куда-то на полчаса-час, и непонятно, на что реально ушло время») gave the law three
teeth. IDENTITY: every narration beat names the work it belongs to — which wish is in hand and which
pipeline station it stands at (outside the pipeline — research, a harvest, a docs sweep — the work's
own name serves), and whether it mends something broken or builds something new — so a
reader dropping into the chat mid-session can tell what is being worked without scrolling back.
DIGEST: a station's completion is itself a beat by law, and its line carries a short digest of what
the station PRODUCED, in the work's own words — the spec station says what the delta promises, the
architecture station says the shape (what parts, what changed structurally), the test station says
what is now covered, the code station says what now works — two or three plain sentences, never the
artifact pasted into chat; a station a delegated worker closed becomes the senior's beat the moment
its result lands. HEARTBEAT: when a stretch runs long with no beat — a big suite, a worker
batch, a long render — narration says what is grinding and roughly why it takes long; a beatless
stretch past ~10 minutes owes its heartbeat [default]. The heartbeat has a second, forward-looking
face — the OFFLINE WINDOW (his word 2026-07-06: «надо иногда писать, когда можно оффлайн — например,
если тесты локально бегут»; the same evening's ask again — pulled back every half hour by a question):
when the coming stretch needs NOTHING from the human — a local suite run, a delegated worker batch, a
long render, a pipeline stretch with no gate or taste call ahead — narration says so BEFORE it starts:
that he may step away, an honest range for how long (read from the work's known shape or observed
runs; an unknown duration is said as unknown — never a guess dressed as a promise), and what he will
be needed for when it ends; and when he IS needed again, that too is a beat — said plainly, naming the
gate or decision that waits. The window is a read on the work, never a dismissal: beats keep landing
during it so the returning reader finds the trail whole; questions born inside the window batch to its
end [INV-4]; a window that ends off its spoken range says so — overrun, done sooner, or blocked on his
word alone — the heartbeat's own duty; the needed-again beat is a chat line awaiting his return, never
a summons (the machinery of reaching an absent human stays outside this law); and no offline sentence
fires when the very next beat needs the human. Together the trail is the session's time accounting: read top to
bottom it answers "where did the time go" in work terms — token and test counts stay bookkeeping
[INV-28]. A narration line is chat,
not a report: it walks no pre-report walk (the walk scopes to movement-end and milestone reports — a
deliberate line [INV-34]), it asks nothing [INV-31], and every law of human-facing lines still binds —
the outcome talks, handles trail, bookkeeping stays out of the content [INV-28]. Working notes marked
as the writer's own remain a separate, skippable register; narration is FOR the reader, and it
replaces no report — milestones still get the full one. The law's one home is the communicator (its
narration rule); the personal profile holds only the person's own tuning of it. [INV-35]

**Anything handed to the human opens with its passport.** A page opened in his browser at midnight
either says WHICH project it is and WHETHER it wants him — or it is noise (his 2026-07-06 word, twice
in one minute: the project's name in the visible content, never only the URL; and "needs your word:
what, by when" or "just an update, no action"). Every artifact handed or opened — a report page, a
decision page, a rendered doc — LEADS with that one-line passport, and the chat line announcing it
carries the same two facts. Home: communicator (the passport rule). [INV-51]

**During an away-stretch, windows accumulate — one opening at the end.** When the human has stepped
away (an overnight loop, an offline window [INV-35]), nothing opens a browser window mid-stretch:
artifacts accumulate on ONE page — the stretch's decisions/report page — and the stretch's end opens
that single window once; mid-stretch re-opening is legal only as the SAME page refreshed in place
(his 2026-07-06 word: «всё-всё-всё открыл бы в конце… если переоткрывать — аккумулировать»). Home:
communicator (the showing-cadence rule beside the offline window). [INV-52]

**The stretch's end is unmissable.** A report that exists but drowns above tool noise was never
delivered (his 2026-07-07 word after a 17-row night ended in what read to him as silence: «закончил
вообще непонятно, без ничего»). When a stretch ends — a loop iteration going to sleep, an
away-stretch closing, a session ending — the LAST rendered thing is one SHORT final line: what closed
· what's next · what's needed from him · when the agent wakes. The long report lives ABOVE it; the
final line comes LAST, after every tool call; a page deliverable repeats its passport [INV-51] in
that line. Delivery, not existence, is the law. Home: communicator. [INV-57]

**His word on a shown artifact is read as meant — and his cuts hold.** The lesson arrived through the
promoter window (2026-07-06 — three review rounds of one document rejected in a single evening, the
same failures repeating after they had been named; the confident-specialist VOICE core of that lesson
lives in the promoter's own voice skill by his placement word — the pack keeps only the general
spine). Two clauses. A phrasing the human KILLED in a review round stays killed in every later draft
of that artifact — the writer keeps the kill-list WRITTEN where the artifact's project keeps its
records (its journal, or the artifact's own notes file), never only in session memory: a wipe must not
resurrect a cut; a cut word resurfacing two rounds later is a defect, not a fresh idea. And a vivid phrase of his is adopted only as MEANT: a human sometimes writes
mockery of a bad draft, not guidance (the parody metaphor earnestly baked into copy as if prescribed),
so before his colorful phrase shapes the work its intent is read from context or asked [INV-4] —
never assumed prescriptive. The law's home is the communicator; two of the original wish's bans
already live in the pack (no empty drama — the no-disclaimers rule; no approval-begging — silence is
consent [INV-31]) and are cross-linked from there, never restated. [INV-42]

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
catches; the re-doored wish KEEPS its lane and re-enters the walk in place (no re-queue, no park —
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

**A face you can enter once owes a way back — or a written one-way.** A surface's FACES (a
first-visit door, an empty state, an onboarding screen, a one-time banner) are entered under
conditions — and a face whose condition can never re-arise is a dead end the state lenses miss: the
states all have exits, the FACE has no re-entry (tlvphoto's door, 2026-07-05 — a prover pass found
six seams and missed the one-way face; his words: «всегда в автомате должен быть луп — если есть гет,
есть сет»). The law: every conditionally-entered face states its deliberate RE-ENTRY path — or states
the one-way as a decision, by name. Trigger wording is the tell: "only on first visit", "only on
first run", "until dismissed" — each such clause owes its return sentence. The prover reads for it
(the entry-symmetry lens in product-prover's stress list); the fit walk's journey lens [INV-29]
already asks "where NEXT from every state" — this law extends the question to faces over the visit's
lifetime. [INV-50]

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
- Intake is parallel, integration is serial — **one landing at a time, per repo, under one PEN**: the
  **pen** is the right to write the shared truth — the spec, the architecture doc, the matrix, the queue,
  the integration of a delta into the shared tree, the closing of a row — and one lane holds it at a
  time. CLAIMING a lane is an atomic committed act — the session commits the row→in-work flip first, then
  re-checks under the fence [INV-11] immediately before its first shared-truth write; a re-check revealing
  a FOREIGN session's committed in-work row means the later claimant backs off and re-queues — foreign
  hands never share a repo's pen, so across sessions the law stands as it always stood. Within ONE
  assigned session, up to three trains may roll under the parallel-lanes law (below) [T-18] — but every pen-stage
  still lands one at a time, and a landing commit carries exactly one row's delta [INV-39]. Bounded
  delegated execution (workers) overlaps as it always did — disjoint brief-named files or an isolated
  tree, the edit fence armed [INV-11, ACT-3]. A new wish waits its turn unless it is a bug preempting
  (next section). [INV-2]
- **A pending question for you never stops the work** — the lane proceeds on the recommended option; the
  question stays open in the row, revisitable any time. [INV-4]
- **No silent micro-decisions** — every choice not in your wish is either asked, or recorded in the spec
  AND surfaced in the same report. The batched report carries this as its own postcondition: EVERY taken
  default, trim, and deliberate narrowing of the walk appears in it — a decision absent from the report
  is silent by definition, whatever the spec recorded. Nothing decided-and-buried. [INV-5]
- **Every landing cites its wish row** — the commit message or journal entry names it, so "why does this
  exist" is always answerable. [INV-3]

**Trains may roll — one pen writes.** Parallelism was born below the lane — workers on disjoint
files, read-only analysis riding the background while another wish walked the pipeline — and this law
lifts it to feature level where it is safe. One assigned session may hold UP TO THREE build lanes
in-work at once when the senior judges them pairwise independent — no surface two of them touch, no
spec section two of them must edit —
and says so: opening every additional lane is narrated, and all rolling trains appear on the departures board [INV-27].
What may overlap: everything that does not write the shared truth — a LATER train's code and tests,
each written in its own isolated copy of the tree ONLY (its delta reaches the shared tree through integration
under the pen; the brief-named disjoint-file road [ACT-3] stays legal WITHIN one lane, whose workers
land with that lane's own commit), read-only analysis and research, a prover run reading committed law.
What always takes the pen, one lane at a time: edits to every document both lanes share — the spec,
the architecture doc, the matrix, the queue, the journal and the resume file among them — the
integration (bringing a lane's delta into the shared tree and running its gate) and the closing of a
row. So the document stages of two lanes never interleave mid-edit: each lane's spec-delta is drafted
and proven against the spec as committed law, never against another lane's half-written draft — the
pen passes between trains while their long mechanical stages run. At most three build lanes roll at once
without asking [default] — his word 2026-07-06: don't sit on a hard two, take the independent work
that exists; a FOURTH lane opens only on the human's asked word — when more independent work waits
workable, the session ASKS whether he wants another train rolling, never opens it silently;
read-only background analysis never counts against that. The board shows every rolling train: each
in-flight row keeps its own station line [INV-27], and a lane waiting for the pen SAYS so and names
the row it waits behind ("at integration, waiting behind row N"). When several trains want the human's
word, the questions ride ONE batched decision page, every card naming its lane's row [E-22, INV-4].
A bug still cuts the line [T-9]: it takes the pen and the senior's hand at the end of the current
pen-stage — a pen-stage is never cut mid-edit; rolling background briefs may finish, but no lane takes
the pen back until the bug lands. And a milestone's whole-spec operations run with one train only —
no new lane opens mid-gate, and a milestone opens only once a single train rolls (the others land
or park first) [M-1]. [T-18]
While several trains roll, the landing stays pure: **a landing commit carries exactly one row's delta**,
and its gate — the full suite plus the guardrails — runs on a tree holding nothing of any other lane's
unfinished work; half of another train never rides a landing. When a lane lands, the shared
truth has moved — so every still-rolling lane's integration re-checks under the fence [INV-11] and re-runs its
gate against the tree as it now stands: landed-first wins, the later lanes re-verify, never the reverse. [INV-39]

The parallel-lanes law's edges, stated once. It fires when another workable, INDEPENDENT wish waits
while a rolling lane's long mechanical stage runs — the correction is idle waiting gone, a feature's
code hours no longer blocking another feature's document hours. It does NOT fire across sessions, on
wishes that share a surface or a spec section (those serialize as before), mid-milestone, or while a
bug holds the pen. Its only face is board and report lines, already governed by the line law — no
other visible surface, facets N/A [INV-28]. Non-goals: cross-session double-landing — not this time
(foreign sessions still back off); no automatic independence checker — the senior judges independence
and says so aloud; no fourth build lane unasked — beyond three, his word opens each next train (his
2026-07-06 word moved the cap itself from two); no per-lane sub-board. Success measure: the first real
double-lane run lands both rows clean with the board readable throughout — the human can say at any
moment where each train stands, checked by his own read of that run's reports [default]. [T-18]

**Lanes are picked by a graph, never by mood.** At queue-take the session reads the runnable head —
the next few rows workable without the human — and builds the mini DEPENDENCY GRAPH: an edge wherever
two rows share a surface, a spec section, a skill file, or a doc region. Lanes open on a
pairwise-independent set, up to the cap [T-18]; rows joined by an edge serialize inside one lane.
Rows that collide only at their INTEGRATION (one file, different concerns) may pre-roll their
isolated build stages with the integration ORDER DECLARED at claim time — first-declared lands first,
the later re-fences on the new truth [INV-39]. And the graph knows when NOT to parallelize: parallel
pays only when build stages dominate the pen work — tiny rows ride serial, and saying so aloud is
part of the board (the first graph night proved both directions in one hour: three medium rows rolled
as lanes, the next five, all tiny, went serial by the graph's own word, 2026-07-06). The chosen set
and the order are NARRATED at opening [INV-27]. [INV-49]

A wish can also end without landing; its row stays in the table: **declined** (you said no) · **deferred**
(parked with a named revisit trigger) · **superseded** (absorbed by another wish; the row points to the
absorbing one). And declining is not a black hole for what the declined wish had absorbed: a wish other
rows were superseded INTO lists them at its decline, and each listed row is either declined BY NAME in
the same breath (your no covered it too) or RETURNED to the queue as its own row again (your no was
about the absorber's shape, not the need) — a superseded wish never dies by pointer [INV-1]. [T-8]

What the wishes grow is the **spec (SPEC.md)** — the living statement of what the product is, one surface
= one name, everywhere. [E-4]

## Asking what the product does (the feature map on demand)

**The whole map is readable on one ask — transparency is a command, not archaeology.** The departures
board answers "how is the in-flight work going" at every report [INV-27], and intake places each arriving
wish on the map [INV-37]; this scenario answers the third question — «покажи все фичи», "what does the
product do today?" — with the map WHOLE, on demand. The answer is read off the living documents at
ask-time: the spec's scenario sections name the features, the header's current-vs-target paragraph splits
shipped from promised — at the granularity the [target] tag binds, so a scenario holding both shipped law
and promised parts reads "shipped, with promised parts (named)", never one blanket status [S-0] — and the
queue's open rows add the rest: each in-flight feature's station, and each wish whose `map:` verdict says
NEW but whose scenario is not yet written, shown as queued — a feature the queue already knows is on the
map before the spec meets it [INV-27, INV-37]. No
third document exists to maintain or drift — no feature list file, no cached copy; the spec's scenarios
and the architecture's nodes ARE the map [E-14], and the ask only reads them aloud. Each line of the
answer obeys the line law: a short descriptive name in the product's own words, what it gives its person,
the status trailing quietly — shipped · target · in-flight at its station [INV-28]. The map arrives in
chat by default; a rendered page comes on your word (the show rule) [default]. And it never fires
uninvited: routine reports keep the departures board's in-flight scope — the whole map comes only when
asked. In a host with nothing to read yet — no spec, no scenario sections — the answer says exactly that
and points at bootstrap or adoption, never an invented list. [INV-38]

The section's edges, stated once. Fences its birth must hold: the departures board's report scope is
unchanged [INV-27], intake placement is unchanged [INV-37], the no-third-document law is reaffirmed, not
amended [E-14]. Facets, skill kind: the feature's only surface is the answer itself (chat, or a rendered
page on ask) — layout, touch, accessibility, and performance belong to the medium that carries it; the
empty state is the nothing-to-read answer above; facets otherwise N/A [default]. Non-goals: no standing
feature document, no auto-refreshing dashboard, no per-feature history timeline — not this time. Success
measure: an ask yields a map whose feature set covers the spec's scenario sections one-to-one plus every
open NEW-verdict queue row, and whose shipped-vs-promised marks agree with the header and the [target]
tags at their own granularity — checkable by diffing the lists [default].

## When a bug cuts the line

A bug may interrupt the wish in-work. The interrupted wish moves to **parked**: a checkpoint is written
(failing test names if red, hypothesis, touched files — nothing red is ever committed), the bug takes the
lane, and the parked wish resumes as the immediate next landing — ahead of ANY queued wish, a quick win
included: a bubble [T-11] jumps only fresh queued wishes, never a resume. Should more bugs arrive while one holds
the lane, **critical** bugs head the waiting line (among themselves by arrival), the rest follow by
arrival; the parked wishes resume only once no bug waits. A bug already in the lane is never itself
interrupted — an arriving bug, critical included, joins the line, so at most one wish is ever parked
PER LANE: when several trains were rolling [T-18], the bug parks them all — each at its own checkpoint — and
they resume in their landing order. [T-9]

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

**A limping thing never dams the flow.** A KNOWN, owned problem — a recurring defect with its
mechanical owner named, a check red for an understood and recorded reason — is PARKED, not orbited:
the ledger line (or the owning row, or an expected-red note in the record) holds it, and every
unrelated lane keeps rolling (his 2026-07-07 word: «если одно не совсем работает — оно не затыкает
всё остальное»). Two teeth: hand-fixing loops cap at the ledger's own two-strikes law — the second
occurrence buys an owner, never another hand-pass; and once a defect HAS its named mechanical owner,
its instances are serviced in BATCH — fixed silently where the fence catches them, one ledger append
at the session's end — never a per-instance ceremony that interrupts the work and the human's reading
of it (the night this law landed, the clock drift had been hand-ceremonied ten times in one session
while its owner, the hook row, was open all along). A real NEW bug still preempts [T-9]; this law
governs the KNOWN limp. [INV-56]

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

**An approved look lives in its artifact — the clause that encodes it points there, and the build looks
at it.** Text cannot carry a feel: a spec clause born of an approved visual prototype was once rebuilt
from its own prose and shipped a cheap look-alike — 75 tests green, because tests derived from a misread
spec prove the misreading (tlvphoto's door and gallery, 2026-07-05). So when the human approves a sketch
as the look, the prototype becomes the **norm** for look and feel, and one law with four arms guards it.
The clause CITES its artifact — a `norm: <path>` pointer at the clause's line end beside its anchors,
the prose carrying the laws while the artifact keeps the look (spec-author owns the pointer's format).
Approval FREEZES the artifact into the project's records: a copy lands in `docs/norms/` with a dated
provenance line (what, approved when, from which sketch), and the pointer cites the frozen copy — a
norm pointer never reaches into a live prototype home, so the one-way fence stays absolute and the
sketch stays free to die [E-17, INV-17]. Building a surface whose clauses carry a norm-pointer OPENS
the artifact before the code step, and the landing records a one-line plan-vs-prototype diff — a
missing diff line is a defect at review (build-pipeline's code step); the verify step's feel bar reads
the same pointer [INV-30]. A story's declared mockup-first entry condition — "show me first, then
build" — is WRITTEN in the wish's queue row at intake ("entry: mockup-first") and is cancelled only by
the human naming it; a general "go build" moves priority, never that condition (the door step). And the prover reads visual clauses with the norm lens: a prototype-born
clause with no pointer, or clause text contradicting its own artifact, is a finding — the "wordless door
≠ no question" class (product-prover). The law binds forward — a clause owes its pointer at the first
landing that touches it, never retroactively en masse; a pointer names only a prototype the human
APPROVED as the look — an unapproved sketch stays plain evidence in its fence [E-17], and a text-born
clause carries no pointer. No visible surface — facets N/A. Non-goals this landing: no mechanical
pointer-grep guardrail (a candidate after real usage); the norm artifact's own format stays free —
whatever page or file the human approved. Success measure: the next prototype-born surface lands with
its pointer and its plan-vs-prototype diff line in the landing report, and the look-alike class does
not recur [default]. [INV-43]

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

**The project knows what KIND of thing it is — and the kind evolves.** Beside personal-vs-reusable,
founding asks the second shaping question: **what is this project** — a book · a backend service · a
static site · a fullstack app · a CLI · a skill pack — one plain line, recorded in the HOST profile
(`project.kind`, the settings ladder's host scope [E-13]); adoption owes the same ask at orient, with
the other founding questions [A-1, B-2]. This is NOT the per-wish work-kind [T-16] — three verdicts
share the intake breath and never collapse into one: the PROJECT kind says what the product IS and
seeds project-wide defaults (the usual work-kind, which facets and feel-lenses apply by default
[T-13, INV-30]); the wish's work-kind says what THIS wish builds; the placement [INV-37] says where it
lands on the map. The seed proposes, a written line disposes: a host that already records its own
default (`work-kind.host-default` [T-16, E-13]) keeps it — the project kind never silently overrides
an explicit profile line. And the ask is always the HUMAN's: no personal-profile line can say what a
host is, so B-2's profile-seeding arm never answers this question — it is asked at founding or orient,
every time. The kind vocabulary is CURATED the same way the work-kinds' is [T-16]: the list
above names shapes real projects already wear, and a custom kind joins through the queue with a named
project the list mis-served — his word expects custom kinds, the queue is their door. And the line is
ALIVE, not a founding fossil: the moment work notices the project has outgrown its kind — the static
site that grew a backend — the line updates on the human's word, journaled right then, never parked
for an audit. A project attached before this law owes no retro-ask: the line arrives at the next
landing that would lean on it, like any forward-binding intake law [T-16 kin]. (His word 2026-07-06:
«нужно понять — и апдейтить, если надо — какой это проект… всё эволюционирует».) [INV-36]

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
   mid-flight; and once a day the same walk also asks the PUBLIC repo whether the pack itself has moved,
   through the update check [E-25]. [A-7]

**How the skills arrive on a machine.** The pack ships one installer, `install.sh`: it copies every pack
skill into the agent's skills home (`~/.claude/skills/`), and it is idempotent — an existing copy is
backed up with a timestamp before being overwritten, never deleted — and the backup lands in an attic
folder BESIDE the skills home, never inside it, so the agent never scans a stale copy as a live skill
(the attic principle applied at install time). What the installer just wrote is exactly what A-7's record clause writes down in
`.live-spec/` — installing and recording are two halves of one seam. [E-21]

**How the machine learns a newer pack exists.** Freshness [A-7] re-reads what is already ON the
machine; delivery of a newer pack used to be a hand job nobody's walk owned. So the pack carries an
update check, `scripts/check-pack-update.sh`: once a day — at the first freshness point of the day,
throttled by a dated stamp in the machine's pack home (`~/.claude/live-spec/update-check-stamp`) — it
asks the public repo (the VERSION file on main) whether the pack moved past what this machine runs
(the walk hands it the installed version from its recorded home [M-7]), and when the remote is newer
it PROPOSES, in the session's own chat: both versions named, the what-changed pointer (the public
journal), and the road named — `install.sh`, whose attic backup already guards the overwrite [E-21],
or a plain pull where the repo itself runs the pack. It never installs anything: updating stays the
human's word, like every install gate [ACT-1]. No network — or an unreadable answer — reads as one
honest "check skipped" line naming the address it tried (a dead URL must not masquerade as a quiet
offline day), never a block, never a guess, and an offline day leaves the stamp unwritten so the next
session retries. A machine AHEAD of the public repo — the developer's, mid-work — reads as up to date:
the check proposes forward only, never a downgrade. It is E-23's outward twin: sync-skills keeps the machine's
copies true to the LOCAL repo, the update check tells when the PUBLIC repo has moved past both.
Its edges: non-goals — no background daemon (a proposal belongs where the human reads, in the
session), no auto-install ever, no per-skill remote diff (the pack version speaks for the whole);
its only face is the proposal line, governed by the line law — facets N/A [INV-28]; success measure:
the day a newer pack ships, the next session on another machine proposes it unasked [default]. [E-25]

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
[INV-10] NARROWED to the files its brief names — outside them it reads but never writes; a brief may
instead name an ISOLATED copy of the tree (a parallel lane's build stages work there), and that copy's
delta reaches the shared tree only through the senior's integration under the pen [T-18, INV-39]; files a
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

**A worker's green gets a second pair of eyes — verify can turn adversarial.** A worker's report is a
lead, never evidence, and on a large delegated landing the blind spot is structural: the same head
that wrote the brief reads the result, so "tasks completed, goal missed" ships green (the neighbours'
verifier lesson, row 107). So the verify step carries an ADVERSARIAL option: a FRESH-context checker
briefed with the SPEC sentences the landing claims (the anchors) and the artifact paths — never the
worker's summary, never the senior's plan — opens on the hypothesis "tasks completed, goal missed"
and walks each claimed fact up a fixed ladder: EXISTS (the artifact is there) → SUBSTANTIVE (not a
stub — the grep list lives in the pipeline's step 8: TODO / FIXME / placeholder / lorem / hardcoded
sample / empty body) → WIRED (reachable from the surface that claims it) → FLOWS (real values move
end to end). Findings become rows or red, never a nod. It fires MANDATORY when the code step was
delegated AND the delta is surface-sized (a new surface or a multi-file behaviour change); anywhere
else it is the senior's option; a skill or prose landing walks the same ladder in its kind's form —
the checker re-reads the SHIPPED text against the spec sentences. The checker is a worker like any
other — contract, checkpoint, ledger duty [ACT-3] — and its verdict rides the landing report. [INV-46]

**A brief is born from read files, never from memory of them.** Before authoring a brief that edits
existing files, the brief-writer READS IN FULL every file the work will modify, and the brief records
three lines per file: current state · what changes · what must survive. Every step carries a
back-reference to the spec sentence it serves, and every technical claim in the brief cites its
source — a file:line, a command's output — because a brief written from memory hands the worker the
senior's guess dressed as fact (the neighbours' story-file lesson, row 107; the night the anchors
were quoted from memory, the worker walked into a wall twice). [INV-53]

**A worker stops only on a named condition.** The brief carries the HALT list, closed and short: an
ambiguous requirement · two consecutive unexplained failures of one command · a missing config or
dependency · acceptance impossible as briefed. On any of these the worker STOPS with evidence;
otherwise it runs to completion — sharper than "ask if unsure", composing with the one-tier
escalation law [ACT-3]. (The list's first full night: three workers HALTed by it, every stop a real
defect and two of them the senior's own.) [INV-54]

**A brief is sized to its worker's head.** A brief targets a bounded share of the worker's context
and the work SPLITS above it — the default bound, concrete: the brief's own text stays within ~300
lines and names at most ~8 files to edit [default]; above either, the work splits into staged briefs.
And a brief passes PATHS, never inlined file bodies — the worker reads its own truth from disk, an
inlined body goes stale the moment a sibling edits the file. [INV-55]

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
a silent micro-decision. Re-carving the whole map IS legal — it arrives as a restructure placement's
own queue row [INV-37], walks this step, and is re-proven like any structure change. [E-14]

**The architecture owes numbers, not only names.** The architecture doc states MEASURABLE quality
budgets for what it builds, plus each budget's INSTRUMENTATION home: where the real numbers are
measured and where a human can read them (an export, a debug view, a report). And WHAT is measurable
is not one-size — **the project's KIND [INV-36] proposes the dimensions**, the architecture step asks
"what does quality MEAN here, in numbers?" before writing any: a user-facing product measures paint
and interaction times ("the first image appears within 2 s on a cold visit"); a backend service
measures latency, throughput, error rate; a CLI or pipeline measures run time on a typical input and
per-unit cost; a skill pack measures its evals' pass rate and suite wall-time; prose measures what
honestly HAS a number (a reader reaches X within one scroll) — and where a quality genuinely has no
honest number, the architecture SAYS so by name instead of inventing a vanity metric. A budget is
asserted by acceptance — a matrix row at a level that can see it — never a hope in prose; a surface
whose architecture names no budgets and no instrumentation home
is a derivation defect the prover flags, exactly like an unowned fact. The numbers themselves are the
host's taste — proposed with a recommendation, set on the human's word at the surface's first budget
landing. Like the two layers themselves [INV-15], the duty binds from the first landing that touches
the surface after the clause exists — never retroactively across a host's whole map. (Born of a real
miss: a gallery's first picture loaded long and the human found it before any check did — that
architecture had named no budget and measured nothing, 2026-07-06.) [INV-41]

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
  a today-dated prover record exists · the suite is green (its RUN scoped by the diff's reach — a
  prose-only diff stands the suite down by name, everything else runs it whole [INV-45]) · every anchor
  owned by exactly one node · no unchecked matrix-coverage box · the prototype fence (no prod file
  references into a prototype home [E-17, INV-17]), plus the opt-in concurrent-edit fence on commit. Still [target]: the
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

**The gate is thorough by REACH, not by ritual.** "Run everything before any push" reads rigorous and
double-misses: a README-only push pays minutes of behavioural tests that read no README line, while
the checks a prose diff CAN break run never (found in a host audit, 2026-07-06 — a one-file README
change paid a 795-test run; his word the same evening: understand what changed to know what to test —
build the dependency graph, a little conservative). So the push gate derives its check-set from a
declared **reach map** — which checks READ which file classes — mechanically from the diff's file
list, never self-judged. Three teeth keep it honest: the map is EXPLICIT (a named file in guardrails/,
patterns a human reads); it is CONSERVATIVE — an unmapped or new file means the FULL suite, fast paths
exist only for explicitly claimed prose classes, and "just .md" is no class: this repo's SPEC, matrix,
architecture, queue, and every SKILL.md are TESTED documents and stay full-reach; and it is
SELF-TESTED — the deciding script is red-proven on fixtures, and anything it cannot classify falls to
full by construction. The cheap gates (prover record, ownership, coverage, loadability, prototype
fence) never scope — they run at every push. "Full rigor" [INV-40] reads as: every check the diff can
reach, green — never fewer, and never a ritual run of checks that read nothing in the diff. [INV-45]

**A gate that blocks speaks one language.** Today each gate script fails in its own words — an agent
parses prose, a human hunts the fix. The contract (the neighbours' CLI lesson, row 107): every
BLOCKING gate, on red, emits ONE typed failure line — a parseable JSON object `{severity, code,
message, fix}` — beside its human lines, the `fix` field being the same sentence a person reads;
every check DECLARES itself blocking or advisory (an advisory check prints and never flips the exit
code); and a script that REBUILDS artifacts validates every output before writing any — no
half-written artifact ever lands on disk. The contract's operational home is the guardrails README
(the gate-authoring rules); it binds by deed from the first gate shipped under it and sweeps the rest
as each is next touched, never retroactively en masse. [INV-47]

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
- **The resume file is a digest with a hard cap:** NEXT_STEPS exists to be read in one minute at a
  cold start — growth is a design failure, so the whole file holds at most 100 lines [default] and a
  suite check owns the number (red on a bloated file, red-proven on a synthetic one). The cap and the
  restate-every-open-leg law [INV-26] resolve by FORM, never by dropping: an open leg is restated as
  ONE terse line — its name, what stays open, where the detail lives — and the detail flows to the
  journal, the queue row, or the record the line points at. Compaction moves prose to its home; it
  never silently drops an open leg. [INV-48]
- **Milestone (MINOR gate):** full spec re-prove + matrix audit (the coverage validation [E-15] re-walked
  against the CURRENT spec + architecture) + surface-composition check + the skill evals re-run [E-19] +
  the pack's skills re-walked through the standard skill-making skill (skill-creator's format /
  frontmatter / description-triggering lens — our evals test behaviour, this lens tests the CRAFT of the
  skill file itself; findings folded or rejected with a written reason in a dated record; and a skill
  newly JOINING the pack walks it at birth, not only at the gate) + doc
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
  communicator skill — and quoting a past moment's recorded time stays legal on this face too. And
  since the hand kept drifting even under the shipped law (the ledger's chat entry re-opened after
  repeated catches), the chat face grew a mechanical HAND of its own: a harness hook installed on the
  working machine — `scripts/clock-hook.sh`, wired as a prompt hook in the host's settings — injects
  the wall clock into every prompt's context, so the lead stamp is read off the machine, not off
  memory; where the hook is not installed, the law above stands alone. (The
  invented-time family: six catches in two days, hand-swept twice before the fences.) [INV-24]
- **Versions have named homes.** The package: a `VERSION` file at the repo root. Each skill: a version
  line in its SKILL.md frontmatter, under `metadata:` — where the skill-format validator reads it. A host: the installed set recorded in `.live-spec/` at attach and on
  every update. So the freshness check [A-7] compares version against version, not just file times, and
  its "old → new" journal note is finally writable. [M-7]
- **CI mirror** — the guardrails' native home is the local pre-push hook; a host may additionally
  mirror the same checks in its CI (Jenkins, GitHub Actions) as a second net. Same checks, one source
  of truth — CI runs the same scripts, never redefines them; and the second net runs the FULL set —
  the reach map [INV-45] is a local latency optimization, never a CI shortcut. The worked example is
  the pack repo's own workflow (`.github/workflows/gates.yml`); host guidance lives in the guardrails
  README. (ROADMAP row 14.) [M-5]
- **Push gate for live-spec itself** — this repo is public and is the method's own flagship, so EVERY push
  is preceded, in the same session, by (a) the concurrent-edit fence [INV-11] and (b) a fresh whole-spec
  re-check: a product-prover pass over SPEC.md as it stands, its record landing in docs/prover/ before the
  push (record name `YYYY-MM-DD[-suffix].md`; suffix mandatory when the date's file exists). Findings that
  are must-fix fold before pushing; folds produced by the gate's own pass do NOT re-trigger the gate — they
  ship with the same record; the rest become queue rows. No re-check record for the pushed state ⇒ the
  push should not have happened. The record ENUMERATES the folds applied from its own pass, and a fold
  stays LOCAL to the sections its finding named — a fold reaching wider re-triggers the gate. [M-6]

## When money or time run short (the economy ladder)

Rigor costs — suite runs, prover passes, senior-model hours. Today the pack spends at full rigor
always; this section names what a tight budget may LEGALLY shed, so economy is a setting you moved,
never an improvisation under pressure. [T-19]

The pressure is a setting on the ladder (`budget.pressure`, package default `full`): it moves ONLY on
your word — a session's word for today, a profile line to stand — exactly like proactivity and trust
[E-13, INV-9]; when you name money or time pressure the agent may PROPOSE a rung, never set one. And
the pack does not wait for pressure to surface the choice: at a project's SETUP — founding or
adoption — the economy rung is asked, or the standing default told, alongside `project.kind`
[INV-36], so the preference is yours from day one, not discovered mid-crisis. Three
rungs, each naming its legal sheds; every shed actually taken is SAID in the landing report — a silent
economy is a silent micro-decision, the exact thing the report exists to prevent [INV-5]:

- **full [default]** — as today: the full suite at every landing gate, the prover at its recorded
  cadence, the worker router picking tiers.
- **lean** — mid-work test runs may scope to the touched architecture node's rows (the full suite
  still runs at every LANDING gate and before every push); surface-add prover passes stay CROSS-LINK,
  and a FULL pass owed by the default cadence may defer to the next milestone — the deferral written
  as a dated debt line in its queue row, never just remembered; mechanical work rides one worker tier
  cheaper when the brief is airtight [D-2].
- **tight** — everything lean, plus: landing gates may BATCH — consecutive small landings share one
  full-suite run at the batch's end (each landing commit still carries exactly one row's delta
  [INV-39]; a red at batch end bisects by landing order before anything else lands; a push still
  requires the full gate green at HEAD [M-6]); the cheapest sufficient worker tier is the rule, senior
  hours spent on judgment alone [D-2].

What NEVER bends, at any rung — the never-bend list, stated once [INV-40]:
- the door law and its tripwires — poverty, like urgency, moves priority, never the door [T-12, INV-16];
- red-before-fix — a bug still gets its failing test before its fix;
- the human's gates — irreversible moves, publishing, authored content, taste [INV-9];
- the landing report, carrying its taken-defaults AND its named sheds [INV-5, INV-31];
- landing purity — one row's delta per commit, whatever the batching [INV-39];
- the push gate — work leaves the machine at full rigor only: every check the diff can REACH green at
  HEAD (the reach map's reading [INV-45]) plus the host's recorded prover cadence [M-6];
- the safety net no work-kind and no scope-cut touches — poverty is its third non-toucher [T-15, T-16];
- narration — it is cheap and stays whole at every rung [INV-35].

An explicit host line outlives any rung: a host profile pinning a tighter cadence (this repo's own
push gate) keeps it even under `tight` [E-13]. Non-goals: no numeric budgets or token meters — the
rung is qualitative, moved by your word; no automatic rung-switching. Success measure [default]: the
first budget-named session names its rung and its sheds aloud in its landing report, checked by your
read of it. [T-19]

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

**A version push re-opens the shopfront.** Publication is not only the first deposit: every push that
ships a new version changes the truth a public reader will read tomorrow — even when the diff never
touched a doc — so the shopfront rides every push. The README's CLAIMS (behaviour, counts, commands,
version homes) still match the pushed truth, and the kind-owed visuals ride along: a skill pack
re-checks its diagrams and flow pictures, a visual product re-shoots what changed on screen, a tool
re-runs its example — a stale shopfront is a false claim exactly like a stale screenshot [E-20]. The
walk is the publish skill's checklist read at push scale (the checklist's one home stays there); the
pipeline's commit-and-show step points at it, and the walk's outcome rides the landing report [INV-22]
— a push whose delta touches none of the shopfront's claims says so in one line ("shopfront checked —
current"), a stale claim found is fixed BEFORE the push. Freshness means claims, never cosmetics.
Non-goals this landing: no mechanical README-vs-diff checker (the reach map, row 147, is the candidate
owner); no auto-regenerated images. Success measure: no push lands whose README claims an older
behaviour or count, checked at milestone audits [default]. [INV-44]

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
| E-25 | pack update check: once a day (dated stamp) the first freshness point asks the public repo's VERSION; newer remote ⇒ a spoken proposal (versions, what-changed pointer, the install.sh/pull road) — never an install; offline ⇒ one honest skip line, stamp unwritten; no daemon | Adoption |
| T-1..T-7 | arrived → … → landed → reported | Throwing a wish |
| T-8 | exits: declined / deferred / superseded | Throwing a wish |
| T-9 | bug preempts, rolling wishes park with checkpoints (at most one parked per lane), resume in landing order | Bug cuts the line |
| T-10 | outside wish arrives via inbox, swept first | Package repo |
| T-11 | priority bends the lane order, visibly; one bubble then the queue head | Throwing a wish |
| T-12 | the door is named before any code | Throwing a wish |
| T-13 | feature spec step sweeps the standard facets (phone/touch/empty-error-loading/a11y/perf) | Throwing a wish |
| T-14 | touching a live surface: spec-delta opens with regression fences citing existing clauses | Throwing a wish |
| T-15 | scope, never time: a too-big wish is cut or staged (a time budget/estimate is never an input); proposals proceed on the recommended option, surfaced; the safety net uncuttable | Throwing a wish |
| T-16 | work-kind named at intake: product / infra / skill / prose; one kind per wish; curated vocabulary; host default in its profile | Throwing a wish |
| T-17 | one wish = one user story: multi-story wishes split at intake, each story its own row; sub-behaviours are acceptance, not stories; unclear count asked | Throwing a wish |
| T-18 | parallel lanes: one session may roll up to three independent build lanes without asking (max three [default], his 2026-07-06 word; a fourth opens only on the human's asked word); penless stages overlap (later trains write only in isolated trees; disjoint-file workers within one lane; read-only analysis free); pen-stages serialize (every shared doc, integration, row close; a pen-stage never cut mid-edit); opening narrated, every train on the board with a waiting lane naming whom it waits behind, cross-lane questions one batched page; not across sessions / dependent wishes / mid-milestone / while a bug holds the pen | Throwing a wish |
| T-19 | the economy ladder: `budget.pressure` ∈ full [default] · lean · tight, moved only by the human's word (session word or profile line, never the agent's); asked — or the default told — at a project's setup (founding/adoption) alongside project.kind; lean = node-scoped mid-work test runs (full suite still at every landing gate) + CROSS-LINK with an owed FULL deferrable to the next milestone as a dated debt line + one-tier-cheaper mechanical work; tight = lean + batched landing gates (one full-suite run per batch's end, red bisects by landing order) + cheapest sufficient worker tier; every taken shed named in the landing report | When money or time run short |
| INV-1 | no wish is ever lost | Throwing a wish |
| INV-2 | one landing at a time per repo, under one pen (shared-truth writes serialize); claiming stays the atomic committed flip; foreign sessions never share a pen | Throwing a wish |
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
| INV-24 | time read off the clock, never invented: no future-dated file name, journal heading, or ledger date (suite fence) AND no added line pairing today's date with a time past the commit clock (pre-commit fence) AND the chat face: a human-facing timestamp read at write time, never extrapolated (law in communicator, no mechanical fence) — plus the chat face's mechanical hand, a prompt hook injecting the wall clock into every prompt (per-machine install, `scripts/clock-hook.sh`); quoting a past wrong date or time stays legal | Rhythm |
| INV-25 | a done-claim is an evidence walk: claim → artifact → method version, walked now; verified vs asserted said apart | Who decides what |
| INV-26 | a row closes only whole: per-leg Done-when, no close with an unmet leg; LIVE-STATE supersession never compresses an open leg away | Throwing a wish |
| INV-27 | every intake is echoed back in one sentence (heard · door · name · row, plus the placement [INV-37]; silent arrivals echo in the next report); every status report names each in-flight feature's pipeline station | Throwing a wish |
| INV-28 | echo-names are plain descriptive phrases; a report line opens with the reader's outcome; every handle (codes, numbers, coined names) only trails; one fact = one standalone sentence; NEVER-list: bookkeeping numbers (test counts, suite sizes, version strings) never as message content — translated, trailing, or in the records; the done-claim walk [INV-25] keeps them as the answer; delivery: a prompt hook reminds every window of the language + narration laws (per-machine, the human's install; the skills stay the homes) | Throwing a wish |
| INV-29 | a feature-doored wish walks the kind-scaled FIT WALK at intake (journey / flows / trigger lenses); trivially-closable holes closed and written how; only genuine taste calls go out, batched; prover mode FEATURE-FIT | Throwing a wish |
| INV-30 | product-kind verify includes the visitor walk + feel pass against the prototype bar, in the medium's own form (motion for a browser, reading path for a book); findings become rows or red | Throwing a wish |
| INV-31 | a taste choice made without asking is told in the landing report — plain words, an example, a tweakable mark; no confirmation, silence is consent, never re-asked; the [default] tag keeps it findable | Throwing a wish |
| INV-32 | a decision card opens with what the choice changes for the person; options labelled by consequence, mechanism only if it helps | Throwing a wish |
| INV-33 | every pipeline step is worked wearing its craft's head (product manager at spec · architect at architecture · QA automation at matrix and tests · senior developer at code · the visitor's own eyes at verify); the step→craft ladder's one home: build-pipeline | Throwing a wish |
| INV-34 | the pre-report walk: before any movement-end/milestone report, the communicator rules are re-read and the draft passes phrase by phrase through the outside-reader question; trailing anchors stay legal; acceptance = the reader's own read; the walk's one home: communicator | Throwing a wish |
| INV-35 | while work runs, beats are narrated as they happen — a station passed, a load-bearing find, a turn — in plain roadmap terms, the reports' voice; every beat names the wish and station in hand (identity); a station's completion is a beat whose line digests what the station produced (digest); a long beatless grind gets a line naming what grinds (heartbeat), and a coming stretch that needs nothing from the human is told as an offline window — step away, an honest range (unknown said as unknown, never a guess dressed as a promise), what he is needed for at its end, and a beat when he is needed again; the window batches its questions to its end and says its own off-range end (overrun, done sooner, blocked on his word), the needed-again beat a chat line awaiting his return, never a summons — the trail accounts for the session's time; the per-command grind stays quiet; a narration line is chat, not a report (no pre-report walk, no questions, the plain-language and bookkeeping laws still bind); it replaces no report; the law's one home: communicator | Throwing a wish |
| INV-36 | the project's own kind (book / backend / static site / fullstack / CLI / skill pack / custom via the queue) asked at founding and at adoption's orient — always asked, never profile-seeded; one home: the host profile's `project.kind`; seeds project-wide defaults but never overrides an explicit host line; distinct from the per-wish work-kind and the placement; updated on the human's word the moment evolution is noticed, journaled | Bootstrap |
| INV-37 | every wish is placed on the product's feature map at intake, the placement SPOKEN with the echo and WRITTEN in the row (`map:` — changes feature X / new feature / restructure); the map = spec scenarios + architecture nodes, no third document; a restructure verdict queues its own row and re-carves only through the architecture step's re-prove | Throwing a wish |
| INV-38 | the whole feature map is readable on demand — read at ask-time off the spec's scenario sections, the current-vs-target header (statuses at the granularity the promised-tag binds, per S-0), and the queue's open rows (stations for in-flight, queued NEW-verdict wishes included); no third document; answer lines obey the line law; chat by default, rendered page on the human's word; never fires uninvited (reports keep the board's in-flight scope); a host with nothing to read is answered honestly | Asking what the product does |
| INV-39 | a landing commit carries exactly one row's delta; its gate runs on a tree clean of any other lane's unfinished work; after a landing, the waiting lane re-fences and re-runs its gate on the new truth — landed-first wins | Throwing a wish |
| INV-40 | the never-bend list holds at every economy rung: the door law + tripwires; red-before-fix; the human's gates; the landing report with named sheds; landing purity; the push gate at full rigor; the safety net; narration whole; and an explicit host line outlives any rung | When money or time run short |
| INV-41 | the architecture states measurable quality budgets plus each budget's instrumentation home (numbers measured and human-readable); the project's KIND proposes the dimensions (product: paint/interaction times; backend: latency/throughput/errors; CLI/pipeline: run time, per-unit cost; skill pack: eval pass rate, suite time; prose: what honestly has a number) and a quality with no honest number is said by name, never a vanity metric; each budget asserted by a matrix-row acceptance, never prose hope; no budgets + no instrumentation home = derivation defect; numbers are the host's taste, set on the human's word at the surface's first budget landing, binding never retroactively | From the spec to the tests |
| INV-42 | the human's word on a shown artifact is read as meant: a phrasing he killed in a review round stays killed in every later draft of that artifact (the writer keeps the kill-list written in the artifact's project records, never only in session memory — a resurfaced cut is a defect, not a fresh idea); a vivid phrase of his is adopted only as meant — mockery of a bad draft is not guidance, its intent read from context or asked, never assumed prescriptive; home: communicator | Throwing a wish |
| INV-43 | an approved prototype is the norm for look and feel, one law with four arms: the clause it fathered cites `norm: <path>` at line end, approval freezing the artifact into `docs/norms/` with a dated provenance line so the pointer never reaches a live prototype home (format: spec-author); a norm-pointered surface's build OPENS the artifact before the code step and the landing records a one-line plan-vs-prototype diff, a missing line = review defect, the verify feel bar reading the same pointer (build-pipeline code step); a declared mockup-first entry condition is written in the wish's queue row and cancels only by the human naming it, never a general "go build" (door step); prover lens: a prototype-born clause with no pointer, or clause text contradicting its own artifact = finding; binds forward, pointer only for prototypes the human APPROVED as the look | A prototype is not the product |
| INV-44 | a version push re-opens the shopfront: the README's claims match the pushed truth and the kind-owed visuals ride along (skill pack: diagrams; visual product: fresh screenshots; tool: example runs) — the walk is the publish skill's checklist at push scale (one home there), pointed at by the commit-and-show step, its outcome riding the landing report ("shopfront checked — current" when untouched); a stale claim is fixed before the push; never a version push past a stale shopfront | Publishing |
| INV-45 | the push gate derives its check-set from a declared reach map (which checks read which file classes), mechanically from the diff's file list, never self-judged: EXPLICIT (a named file in guardrails/), CONSERVATIVE (an unmapped or new file ⇒ the full suite; tested documents — SPEC, matrix, architecture, queue, SKILL.md — stay full-reach, "just .md" is no class), SELF-TESTED (the deciding script red-proven on fixtures, unclassifiable ⇒ full by construction); the cheap gates never scope; "full rigor" (INV-40) = every check the diff can reach, green | The machines that hold the bounds |
| INV-46 | verify's adversarial option: a FRESH-context checker briefed with the landing's SPEC sentences + artifact paths (never the worker's summary or the senior's plan), hypothesis "tasks completed, goal missed", ladder exists → substantive (stub greps: TODO/FIXME/placeholder/lorem/hardcoded sample/empty body; list's home: pipeline step 8) → wired → flows; findings become rows or red; MANDATORY when the code step was delegated AND the delta is surface-sized, optional elsewhere; kind-scaled for skill/prose (shipped text vs spec sentences); the checker is a worker under ACT-3, verdict rides the landing report | Who decides what |
| INV-47 | gate hygiene: every BLOCKING gate on red emits one typed failure line `{severity, code, message, fix}` beside its human lines (fix = the human sentence); every check declares blocking or advisory (advisory never flips the exit); artifact-rebuilding scripts validate all outputs before writing any; operational home: guardrails README; binds by deed from the first gate under it, sweeps as each is next touched | The machines that hold the bounds |
| INV-48 | the resume file is a digest with a hard cap: whole file ≤ 100 lines [default], a suite check owns the number (red-proven on a synthetic bloated file); open legs restate as one terse line each (name + what's open + where detail lives, INV-26 resolved by form); compaction moves prose to its home, never drops a leg | Rhythm |
| INV-49 | lanes are picked by a dependency graph at queue-take (edge = shared surface / spec section / skill file / doc region): open on a pairwise-independent set up to the T-18 cap; integration-only collisions pre-roll isolated build stages with the landing order DECLARED at claim (first-declared lands first, later re-fences); tiny rows ride serial — parallel pays only when build stages dominate; the set and order narrated at opening | Throwing a wish |
| INV-50 | a conditionally-entered face (first visit, empty state, onboarding, one-time banner) states its deliberate re-entry path or names the one-way as a decision; trigger wording "only on first visit/run", "until dismissed" owes its return sentence; prover carries the entry-symmetry lens; extends INV-29's where-next to faces over the visit's lifetime | Throwing a wish |
| INV-51 | anything handed/opened to the human leads with its passport: the project's NAME in the visible content (never only the URL) + the read contract ("needs your word: what, by when" or "just an update"); the announcing chat line carries the same two facts; home: communicator | Throwing a wish |
| INV-52 | during an away-stretch nothing opens a browser window: artifacts accumulate on ONE page, the stretch's end opens it once; mid-stretch re-open only as the same page refreshed; home: communicator | Throwing a wish |
| INV-53 | a brief editing existing files is born from READING them in full: three recorded lines per file (current state · what changes · what must survive); every step back-references its spec sentence; every technical claim cites a source (file:line / command output) | Who decides what |
| INV-54 | the worker HALT list, closed: ambiguous requirement · two consecutive unexplained failures of one command · missing config/dependency · acceptance impossible as briefed — stop with evidence; otherwise run to completion; composes with one-tier escalation | Who decides what |
| INV-55 | a brief targets a bounded share of the worker's context, splits above it (default bound: brief text ~300 lines, ~8 files to edit [default]); paths, never inlined file bodies | Who decides what |
| INV-56 | a limping thing never dams the flow: a KNOWN owned problem is parked (ledger line / owning row / expected-red note) and unrelated lanes keep rolling; hand-fix loops cap at two-strikes (second occurrence buys an owner); a defect with a named mechanical owner is serviced in batch (silent fence-fixes, one ledger append at session end), never per-instance ceremony; a real NEW bug still preempts (T-9) | When the workshop itself misbehaves |
| INV-57 | the stretch's end is unmissable: the last rendered thing is one short final line (what closed · what's next · what's needed · when the agent wakes), the long report above it, a page deliverable repeating its passport; delivery, not existence; home: communicator | Throwing a wish |
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
| ACT-3 | tiered workers, checkpoints; every brief carries the ledger walk + the clock [router target]; a brief may name an isolated tree — its delta integrates only under the pen | Who decides what |
| M-1 | milestone: re-prove + audit + compaction + gate list | Rhythm |
| M-2 | safe breakpoint; announced self-compaction | Rhythm |
| M-3 | documents versioned like code | Rhythm |
| M-4 | live-spec is its own host | Package repo |
| M-5 | CI mirror of the same checks: same scripts, second net runs the FULL set (the reach map stays local); worked example `.github/workflows/gates.yml` + guardrails-README host guidance | Rhythm |
| M-6 | push gate: prover re-check before every push | Rhythm |
| M-7 | version homes: VERSION file · SKILL.md frontmatter · host record | Rhythm |
| C-1 | canonical axes + provenance axis | Composing across axes |
| D-1 | attic layout | Open decisions |
| D-2 | tier routing override | Open decisions |
| D-3 | snapshot retention | Open decisions |
| D-4 | pack structure: package-is-source decided; mirrors = row 51 | Open decisions |
| D-5 | all-into-profile decided; rows 52–54 execute | Open decisions |
