# live-spec — SPEC (v0.15.61, 2026-07-07)

> How to read: each section is a scenario — what you do and what you see. The short codes in brackets are
> quiet machine anchors (for the prover, the test matrix, and transcript greps); the Formal index at the end
> maps every anchor to its home section. Edit history lives in JOURNAL.md; this spec states today's truth.
> Restructured use-case-first 2026-07-04 (queue row 22) under an anchor-set guard: v0.4 carries exactly the
> anchor set of v0.3 — the shape changed, no rule was lost.

**Current vs target.** Shipped today: the skills (the base rulebook and its working skills), the
templates, the adoption procedure text, the inbox, the skill evals with their run records, this spec and
queue, and the first guardrails slice —
the pack repo's own pre-push gates and the opt-in commit fence, installed and tested. Target (each owned
by a ROADMAP row, not yet code): the guardrails' host-facing checks and surface registry [E-6, E-10], the
snapshot machinery [E-7] (the adoption baseline A-6 rides it), the optional design-sync machine [E-18]. This spec never claims shipped what isn't — clauses below marked [target] await their row, and
the tag binds at the granularity it is written: a surface is [target] only if its OWN clause carries the
tag, never merely a parent section or one leg of a split anchor. The promise is mechanized: the suite
holds the map from every [target]-marked index fact to its owning, still-open queue row — a target whose
row lands, vanishes, or was never named turns the suite red, and so does a node keeping the tag after
its pins became real. [S-0]

## What live-spec is

Pile on whatever you want — any wish, any size, any moment. live-spec slices it into small pieces and
lays them on a conveyor. Every piece runs the same proven pipeline, converges to a landing, and ships
tested. You stay free to think.

Behind the conveyor stands a whole software house in one package. An analyst who writes the spec. An
architect who stress-tests the design and hunts its edge cases and dead ends before any code. A QA who
derives and writes the tests. A project manager who runs the line and reports back to you. These roles
are real, and they are the working skills (spec-author, product-prover, build-pipeline, test-author,
communicator, publish, feedback-intake). One **base skill** carries the shared rulebook and the default
settings every other skill works by [E-12].

The discipline holds because machines hold the bounds at every step. Every wish takes the same route.
Every claim earns a test, and nothing ships until that test passes. The automated guardrails never
sleep. The process drives each wish all the way to a landing and keeps it from sprawling. You are
pulled in for the decisions that are genuinely yours.

A software project adopts live-spec at the start or halfway through work already under way. It brings
document templates, an adoption procedure for joining a project midstream, and mechanical guardrails
the project installs. The project that adopts it is the **host**, and the host owns everything about
its own work — its spec, matrix, queue, journal, surface registry, inbox, feedback ledger, and a
`.live-spec/` folder holding its profile, its checkpoints, and the versions of the skills it runs. [E-1]

## Throwing a wish

You are working on something else when you say "and let the card also show…", then go back to your thought. A **wish** is exactly that: one request, in plain words, of any size, spoken at any moment. [E-2]

Within that same minute, the wish becomes a row in the **queue (ROADMAP.md)** — the persistent, ordered home of every wish. Each wish is one row, holding these fields:
- your words
- class: size, plus priority when it isn't normal
- status
- acceptance criterion

[E-3]

A spoken wish means the row exists before anything else happens. It survives even if the session dies a second later. Rows are never deleted; you close a row only with a named exit. At a milestone, a row closed with a terminal exit — landed, declined, or superseded — moves to a dated queue archive, archived and never edited, never lost. A **deferred** row is not terminal. It stays in the active queue, carrying its revisit trigger, until the trigger fires or it re-resolves to a terminal exit. The archive never swallows a wish that is still due back. No wish is ever lost. [INV-1]

From its row, the wish walks one path:
- The classifier reads its size, priority, door, and work-kind, then states them back to you in one INTAKE line (the paragraphs below explain each).
- A spec-delta is drafted.
- The delta is validated against the whole spec. Here only genuinely-human questions go out to you, batched; everything else proceeds on the recommended option, marked in the row.
- The wish is queued, then goes in-work.
- It lands: green suite, guardrails, committed, and the row closed with its acceptance met.
- The pipeline reports to you in one plain-language LANDING line: position on the map, what landed, what remains.

[T-1..T-7]

**How batched questions reach you.** Several open picks never become a serialized chat questionnaire. They render as ONE interactive decision page: one card per question, the recommendation named, and room for a free-form answer on every card. The page opens in its own window while the lane keeps moving [INV-4]. The pipeline reads the answered file back, archives it in the project's `docs/decisions/`, and harvests every answer into its queue row the same session — an answer left un-harvested is a decision lost. An answer is the human's word, not merely his click. When he picks an option and then disavows it in plain speech — on 2026-07-05 he said in plain speech that he had not understood what he was confirming — the pick is withdrawn. It is recorded as answered-then-withdrawn, and the pick re-opens with a plainer explanation owed before it is asked again. An uninformed pick never settles a verdict that needs his word [INV-9]. That law was born the night of 2026-07-05, when the shell-separator verdict was picked at 23:49 and disavowed minutes later. The page's mechanics — the filename law, the ordinals, the JSON round-trip — live once, in the communicator skill's rule 10 [INV-13]. [E-22]

**A decision card asks in consequences, not mechanisms.** The shell-separator card explained how the failure worked, and the reader still could not tell what he was deciding; on 2026-07-06 he said he understood neither the problem, nor the consequences, nor what he was deciding — the same incident that birthed the withdrawn-answer law above. So every card on a decision page opens with what the choice CHANGES for the person: what he will see, get, or stop suffering under each option, in the product's words. The mechanism follows only if it helps. Each option is labelled by its consequence, never by its implementation. A card whose question cannot be answered without understanding the mechanism is a defect of the card [INV-28 kin]. [INV-32]

**How a wish is classified.** Size uses one four-word vocabulary everywhere — **bug / small / surface / large** — and the queue's class column speaks the same four words, never a second size scale. The door below is a different axis: where the wish enters the pipeline, not how big it is. Priority is **normal** unless the row says otherwise. Two marks exist. The first, **critical**, means the shipped product is broken for its user: an unusable surface, data being lost, or a safety gate violated. The second, **quick win**, means low effort, immediate value, and no design decision inside. When the classifier cannot call a size, a priority, or a work-kind [T-16], it asks you at intake and never guesses. Until you answer, the wish carries normal — a kind here is the host's recorded default, else none, and a kind not yet named scales nothing down [INV-22] — and the open question rides in the row while the lane keeps moving [INV-4]. [INV-12]

**A big wish negotiates scope, never time.** Nobody here asks "how long will it take", and an answer in hours or days is not an input the walk accepts. A time estimate out of a builder is a guess dressed as a number; on 2026-07-05 Alexander said you can play with scope rather than with timelines. When a wish looks bigger than it is worth, the walk answers in scope terms and proposes one of two moves:
- **cut the scope** — fewer surfaces in, plainer defaults on what stays;
- **split into stages** — each stage one landing through the full pipeline (the "large" size already decomposes this way [INV-12]).

The proposal proceeds on the recommended option; the lane never parks on it [INV-4]. Every cut rides the same batched report as every taken default [INV-18], never silent [INV-5], and your re-widen is simply a new wish. A scope cut bends scope only, never order. It is not a quick-win mark, and only priority moves the lane [T-11]. No cut may ever touch the delta's mandatory sentences: the fences [T-14], a kept surface's facets [INV-18], the non-goals and the success measure [INV-20, INV-21]. Scope dials richness; it never touches the safety net. [T-15]

**One wish = one user story; a row closes only whole.** This law is built on a failure: a project fused two stories, a door and a gallery, into one queue row, so the door half shipped, the row was declared complete, and the gallery stayed a rejected wall for four rebuilds. At intake, then, a wish carrying several user stories — several distinct things a person will do and see — is split, each story its own row through the full pipeline. This is kin to a stage split, but a different knife: stages slice one story's depth [T-15], while separate stories are never fused into one row to begin with. Sub-behaviours of one story — its hover face, its phone face, a backpointer — are that story's acceptance, not new stories. Whether something is one story or two is asked at intake, never guessed [INV-12]. A split loses nothing: every row born of it cites the one spoken wish it came from [INV-1]. [T-17] Where a row nonetheless carries several legs — a legacy fusion or a harvested batch — its Done-when enumerates per-leg acceptance, and the row cannot close with an unmet leg — half-done is a status, never a landing. The resume file's LIVE-STATE supersession never compresses an unfinished leg out of existence: a leg still open at compaction is restated, not summarized away [M-2]. [INV-26]

**A wish hears itself land, and progress reads like a departures board.** You toss a wish in passing, before sleep or mid-thought, and without an echo you cannot know it survived. So the intake line is not only written into the queue; the project speaks it back. One plain sentence says what was heard, the door called, the name the work will answer to, and its row number — caught this request, it's a feature, we'll call it X, row N. A wish that arrives silently, as an inbox file or a harvest, gets its echo in the next report, never as an interruption. Whenever status is reported, the project names every in-flight feature by that name with its pipeline STATION: spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show, plus the terminal landed. Progress then reads like a departures board at a glance, never prose archaeology. The station vocabulary is the pipeline's own step names, one station per step, all nine. A feature paused at proving the architecture or at commit & show reads under that station's own name, never an improvised one. Landed is a state, not a step: it says the row closed whole. (His word 2026-07-05, before sleep: name the captured request in plain words, then report how each feature moves down the pipeline.) The echo carries one more part — the wish's place on the product's map; its law lives in the next paragraph [INV-37]. [INV-27]

**Every wish is also PLACED on the product's map — "this changes feature X", "this is a new feature", or "the shape no longer fits" — and the placement is spoken, out of the box.** The echo above says what the work is: heard, door, name, row. The same breath says where it lands. The map is not a new document. The spec's scenario sections and the architecture's nodes already are the product's feature map [E-14]; this law only makes the until-now implicit mapping spoken. Three verdicts exist:

- **changes an existing feature** — the delta grows that scenario and names it.
- **a new feature** — a new scenario section, and at the architecture step its own node.
- **restructure** — the wish fits no existing carving cleanly, or fitting it in shows the modules have outgrown their shape; his words, the moment of forming the product's modular architecture.

A restructure verdict never re-carves in passing. It queues its own row — the refactor door when only structure moves, the feature door when behaviour moves with it — and the re-carve walks the architecture step with its re-prove [E-14]. The placement may say the shape no longer fits; only a landing may change the shape. A bug's placement is the feature it repairs, and a wish whose feature the classifier cannot call is asked like any uncallable axis [INV-12]. The verdict is written as well as spoken: the wish's queue row carries a `map:` note — changes X, new, or restructure — so placement stays greppable after the echo fades, the way the fences stay greppable in their rows [T-14 kin]. (His word 2026-07-06: when a new request arrives, understand which feature it concerns — whether it changes a feature, adds a new one, or needs restructuring — and this should be clear out of the box.) [INV-37]

**The outcome does the talking: names are chosen plain, and every handle trails.** The first real departures board passed its eval and failed its reader. Lines led with coined metaphor-titles such as "a walk through the evidence" or "the clock grows teeth", carried row numbers he never opens, and squeezed facts into riddles only their writer could parse — the jargon family's third strike in two days (2026-07-06 morning). Two arms, one law.

Naming: a feature's echo-name is a short descriptive phrase in the product's own words — what the thing does, parseable cold by a reader who missed its birth — never a private metaphor. A name that needs its story told first is a handle, not a name.

Lines: a human-facing report or board line opens with what changed for the reader — what they can now do, see, or stop fearing. This covers chat reports, narration lines [INV-35], report pages, decision pages, and the capture echo, while method-internal docs keep their anchors. Every internal handle — spec codes, row and session numbers, and any coined name the reader never chose to learn — may only trail in parentheses. And one fact = one standalone sentence: a compression whose parsing needs the writer's context is a defect of the line, not a flourish.

Bookkeeping numbers are handles too, and they kept walking into the message anyway — two consecutive eval runs put "all 64 checks green, v0.9.16" into the human's message body (2026-07-06). So the law carries an explicit never-list: a test count, a suite size, a version string, or a check tally is never message content. The message says what the number means for the reader — tested clean, saved, the method held — and the number may only trail as a quiet anchor or stay in the records. One carve-out, by law: where the number is the asked substance — a direct question about it, or the done-claim evidence walk, whose claim lines pin artifact and method version [INV-25] — it speaks as the answer, not as bookkeeping. This law and the narration law live in skills a window may never load; the day the field showed it, three windows leaked raw codes to their reader (2026-07-06). So they have a mechanical voice on the working machine. A prompt hook, `scripts/chat-law-hook.sh`, installed beside the clock's hand by the human's own command, injects a one-line reminder of both laws into every prompt. The skills remain the laws' homes; the hook only reminds and never legislates. A window that ignores the line is breaking the same law, not a different one. [INV-28]

**The report law is walked, not remembered.** The law above passed its evals and still failed on the senior's own chat: the session-13 closing report led with pack-internal names and loan-translated doc metaphors, and its reader bounced it — he asked what language the report was even written in (2026-07-06, the jargon family's fourth strike in two days and the first after the law landed). Chat has no suite, so the enforcement is a STEP, not another sentence. Before any movement-end or milestone report reaches the human, you re-read the communicator rules and pass the draft phrase by phrase through one question: does this sentence stand for a reader who does not live inside the pack. A pack surface it names is either explained in the reader's own words or dropped; quiet trailing anchors stay legal, since the walk governs what does the talking, never the handles that trail. The walk's one home is the communicator skill, and its acceptance belongs to the reader: a movement-end report that makes the reader ask "what is this?" is the walk not walked. [INV-34]

**Work is narrated while it runs — the third voice between the echo and the report.** The intake has its echo [INV-27] and the landing has its report [INV-28], but between them a working session used to go quiet, leaving the human — who leads several windows at once — reading silence. His word came twice in one day (2026-07-06): the morning ask wrote a personal-profile line, and by afternoon it returned — don't forget to report as the work goes, and record this in the communication skill too. A habit held only in a personal profile did not carry across sessions, so it is now pack law. While work runs, each beat worth a sentence — a pipeline station just passed, a load-bearing find, a change of direction — is said as it happens: one or two plain sentences in the roadmap's terms (which wish is in hand, what it gives, what just moved), in the same voice as the reports. The mechanical grind stays quiet — narration marks beats, never a per-command commentary. His third word in the family gave the law three teeth (2026-07-06 evening, when the landing reports had become good but the mid-work trail was still thin): a session goes off for half an hour to an hour, and it is unclear where the time actually went.

- **IDENTITY: every narration beat names the work it belongs to** — which wish is in hand and which pipeline station it stands at (outside the pipeline, in research, a harvest, or a docs sweep, the work's own name serves), and whether it mends something broken or builds something new. So a reader dropping into the chat mid-session can tell what is being worked without scrolling back.
- **DIGEST:** a station's completion is itself a beat by law, and its line carries a short digest of what the station produced, in the work's own words. The spec station says what the delta promises; the architecture station says the shape (what parts, what changed structurally); the test station says what is now covered; the code station says what now works — two or three plain sentences, never the artifact pasted into chat; a station a delegated worker closed becomes the senior's beat the moment its result lands.
- **HEARTBEAT:** when a stretch runs long with no beat — a big suite, a worker batch, a long render — narration says what is grinding and roughly why it takes long; a beatless stretch past ~10 minutes owes its heartbeat [default].

The heartbeat has a second, forward-looking face — the OFFLINE WINDOW (his word 2026-07-06: sometimes say when he can go offline, for example while tests run locally; the same evening's ask again, pulled back every half hour by a question). When the coming stretch needs nothing from the human — a local suite run, a delegated worker batch, a long render, a pipeline stretch with no gate or taste call ahead — narration says so before it starts: that he may step away, an honest range for how long (read from the work's known shape or observed runs; an unknown duration is said as unknown, never a guess dressed as a promise), and what he will be needed for when it ends. When he is needed again, that too is a beat, said plainly, naming the gate or decision that waits. The window is a read on the work, never a dismissal: beats keep landing during it so the returning reader finds the trail whole; questions born inside the window batch to its end [INV-4]; a window that ends off its spoken range says so — overrun, done sooner, or blocked on his word alone — the heartbeat's own duty; the needed-again beat is a chat line awaiting his return, never a summons (the machinery of reaching an absent human stays outside this law); and no offline sentence fires when the very next beat needs the human.

Together the trail is the session's time accounting: read top to bottom, it answers where the time went in work terms — token and test counts stay bookkeeping [INV-28]. A narration line is chat, not a report: it walks no pre-report walk (the walk scopes to movement-end and milestone reports, a deliberate line [INV-34]), it asks nothing [INV-31], and every law of human-facing lines still binds — the outcome talks, handles trail, bookkeeping stays out of the content [INV-28]. Working notes marked as the writer's own remain a separate, skippable register; narration is for the reader, and it replaces no report — milestones still get the full one. The law's one home is the communicator (its narration rule); the personal profile holds only the person's own tuning of it. [INV-35]

**Anything handed to the human opens with its passport.** A page that opens in his browser at midnight must say two things: which project it belongs to, and whether it wants him. A page that says neither is noise. His 2026-07-06 word, said twice in one minute: put the project's name in the visible content, never only the URL. Then say what the page needs from him: "needs your word: what, by when", or "just an update, no action". Every artifact you hand or open leads with that one-line passport — a report page, a decision page, a rendered doc alike. The chat line that announces the artifact carries the same two facts. Home: communicator (the passport rule). [INV-51]

**During an away-stretch, windows accumulate — one opening at the end.** When the human has stepped away for an overnight loop or an offline window [INV-35], nothing opens a browser window mid-stretch. Artifacts accumulate on ONE page: the stretch's decisions and report page. The stretch's end opens that single window once. Mid-stretch re-opening is legal only as the SAME page refreshed in place. This is his 2026-07-06 word: he would open everything at the very end, and if anything re-opens mid-stretch it only accumulates onto the same page. Home: communicator (the showing-cadence rule beside the offline window). [INV-52]

**The showing channel matches the session's seat.** A session seated on the human's machine shows a rendered artifact as a local page in a browser window. A session seated remotely runs in the cloud and is read through a browser, so it can open nothing local. The same content goes through the remote seat's own channel: an artifact page the host renders for the human, or the chat itself. Either way, same passport [INV-51], same round-trip. The session reads its seat from what it can actually reach — the platform, the display, whose filesystem — and names the channel it picked. So a local file path handed to a remote reader is a defect of the exchange, the twin of the window that never opened. The personal profile's show line is the local seat's arm, never the law itself. His word, 2026-07-07 morning. [INV-67]

**The stretch's end is unmissable.** A report that exists but drowns above tool noise was never delivered. This is his 2026-07-07 word after a 17-row night: the night ended in a way that read to him as nothing at all, unclear, with no closing word. When a stretch ends — a loop iteration going to sleep, an away-stretch closing, a session ending — the LAST rendered thing is one SHORT final line. It carries four fields: what closed, what's next, what's needed from him, and when the agent wakes. The long report lives ABOVE it. The final line comes LAST, after every tool call. A page deliverable repeats its passport [INV-51] in that final line. Delivery, not existence, is the law. Home: communicator. [INV-57]

**A review surface shows its sources and takes his pen.** Anything you show for review carries per-claim provenance. That covers a dossier, a claims page, or a draft with assertions. The surface marks each claim by where it came from: read from the artifact, his own recorded word, or the agent's inference. The inferences are flagged LOUDEST. In the promoter case, unmarked inference cost a review round — he said he did not know where the agent had got it all from. The surface is COMMENTABLE, never a read-only wall. It gives line-by-line room for his word and captures his answers. The decision page's saved-answers law [INV-32] extends to review pages, as one JSON round-trip home. This is his standing cross-project word, 2026-07-06. Its home is the communicator, beside the decision page rule. [INV-64]

**His word on a shown artifact is read as meant — and his cuts hold.** This lesson arrived through the promoter window on 2026-07-06. Three review rounds of one document were rejected in a single evening, the same failures repeating after they had been named. The confident-specialist voice core of that lesson lives in the promoter's own voice skill, by his placement word; the pack keeps only the general spine. Two clauses follow. First, a phrasing the human KILLED in a review round stays killed in every later draft of that artifact. The writer keeps the kill-list written where the artifact's project keeps its records — its journal, or the artifact's own notes file — never only in session memory. A wipe must not resurrect a cut. A cut word resurfacing two rounds later is a defect, not a fresh idea. Second, a vivid phrase of his is adopted only as meant. A human sometimes writes mockery of a bad draft, not guidance — the parody metaphor earnestly baked into copy as if prescribed. So before his colorful phrase shapes the work, the writer reads its intent from context or asks [INV-4], never assuming it prescriptive. The law's home is the communicator. Two of the original wish's bans already live in the pack: no empty drama, the no-disclaimers rule; and no approval-begging, since silence is consent [INV-31]. Both are cross-linked from there, never restated. [INV-42]

**Approved text is frozen — a revision applies only the named correction.** Once the human approved a text, it is settled material. A later revision applies exactly the correction he named — trim what he said to trim, swap what he said to swap — never a fresh rewrite around it. A rewrite of an approved opener once introduced a banned pattern the approved wording never had; that was the promoter case, 2026-07-07. Churn of approved material is a defect, kin of a resurfaced cut [INV-42]. Its home is the communicator, beside the kill-list rule. [INV-58]

**The kill-list has a mechanical face.** For a host with taste-reviewed artifacts, the pack ships the kill-list template. It holds the human's cuts as dated literals, appended the moment a cut happens, never removed. The pack also ships the guardrails guidance for a scanner. A test reads the table and greps the artifact's surfaces, and a killed literal reappearing turns the suite red. A banned pattern once returned into a campaign's most visible line, even after the ban was spelled out in the plainest terms; only the executable scanner ended it. That was the promoter case, 2026-07-07. The law stays INV-42's; this is its teeth. [E-26]

**No question is asked twice — and dialogues converge.** Before any ask, the agent searches the recorded word — the decision archives, the review records, the journal, the profile. Here, a question a record already answers is a DEFECT, not a question. This was his escalation in the promoter case: a stack of similar questions had already been answered, and he asked that the dialogues converge. Exchanges also converge. An answered question closes forever and is harvested into its row the same session. A problem he named returns solved with evidence, never re-described, so round N+1 carries only new material. Its home is the communicator's ask rules. [INV-59]

**A taste ask arrives carrying the agent's own researched proposal.** A genuine taste question never arrives empty-handed. The agent mines the material first — exemplars, precedents, real options with citations. It then asks with a chosen recommendation and its evidence. Asking the human to supply what the agent should have mined is a defect. This was his word in the promoter case: find it yourself, propose, then show. This sharpens the recommended-option law [INV-4] for taste calls. Its home is the communicator. [INV-60]

**Priority bends the lane order, visibly.** A critical bug lands before everything, heading even the waiting-bug line (next section). Critical priority heads the queue whatever its door, so a critical-priority feature goes to the queue head too. But only the bug door preempts the in-work lane [T-9]. A quick win may bubble up. When the lane frees, the agent may take it ahead of larger queued wishes, marking the jump in its row, never silent. After one bubbled landing the queue head goes next, so a stream of quick wins cannot starve a big wish forever. An inbox wish's arrival is its harvest moment — that is when it first becomes a row the ordering rules can see. A file's own date never competes with spoken timestamps. Arrival ties resolve by queue row order, top to bottom. Within one sweep, an inbox batch harvests in filename-sorted order. [T-11]

**The door is named before any code.** Classification is an explicit step with fixed rules, settled by no one's gut feeling. A row carries three axes, stated together in ONE intake line: size · priority · door · the work-kind (what the wish builds — next paragraphs [T-16]). A wish too big for its worth is negotiated in scope, never in time [T-15]. Size, with priority, says how big and how urgent. The **door** says where the wish enters the pipeline: **feature · bug · refactor · docs-only · skip**. The size and door axes share one word deliberately: a wish sized "bug" IS the bug door, one call stated once, and the door axis only adds the other four entries. [T-12]

The door is decided by an ordered procedure. Tripwires fire first, before any judgment.

1. It IS a **feature** — however casually asked — when ANY of these holds: a new user-visible surface appears · new persistent state appears · a new interaction lands on an existing surface · the touched surface is marked [target] in the spec (the canonical, machine-checkable form of "not yet specified / later surface"; the plain-prose cousins bind too, but the author writes the tag) · the change adds behaviour no spec clause backs.
2. No tripwire fired, but shipped behaviour is wrong against what the spec or product already promises → **bug**.
3. Behaviour stays identical, structure moves → **refactor**.
4. Only prose OUTSIDE the normative spec changes (README, comments, guides) → **docs-only**. Rewording a spec rule is NOT docs-only: it changes what behaviour the spec backs, and routes as feature or bug.
5. The narrow all-hold boundary (single file · no new state, element, or visible behaviour · an existing test level already covers the touched fact) → **skip**.

The tripwire verdict outranks a casual label. A wish called a "bugfix" that fires a feature tripwire is re-doored to feature, and the intake line says so [INV-5]. Queue-cutting [T-9] belongs ONLY to the bug door, so a re-doored wish takes no preemption. Your word can still raise its priority (priority is yours), but no word makes a feature skip the spec step. The door is also re-checked mid-work. The moment running work is about to create a user-visible surface or persistent state its current door doesn't grant, work STOPS and the door step fires again — "it sounded like loading until the surface existed" is exactly the failure this catches. The re-doored wish KEEPS its lane and re-enters the walk in place (no re-queue, no park — parking stays a bug-preemption move [T-9]). One request lives outside the lane entirely: asking to merely SEE or TRY something, with no commitment to keep it, may be built as a labelled sketch (see "A prototype stays a sketch" — the ask-when-unclear rule lives there). Casual loading stays the contract: a wish is routed through its door, never refused for being casual, and never hand-built past the pipeline because it sounded small. [INV-16]

**The intake line also names WHAT is being built.** Size says how big, the door says where the wish enters, and the **work-kind** says what kind of thing the work produces — and with it which pipeline machinery earns its keep. Four kinds today:

- **product** — something the host's own user faces;
- **infra** — tooling that serves the project itself (scripts, hooks, CI, pipelines);
- **skill** — a behaviour document an agent works by (a SKILL.md, a prompt pack);
- **prose** — a document written for a human to read (an overview, an article, a spec's own text).

The kind is called from what the wish PRODUCES, one kind per wish. A wish genuinely producing two kinds is two wishes, split at intake; a kind the classifier can't call is asked like an uncallable size [INV-12]. A host with ONE usual kind may record it as a host-profile default the intake line starts from [E-8, E-13] (track-coach's would be product). A host whose wishes genuinely span kinds — live-spec itself ships skills, prose, and infra — records none and calls each wish on its own. The vocabulary is CURATED like the facet list [T-13]: each kind above is earned by real work the pack has already routed (track-coach's widget — product; render-doc.py — infra; the pack's five skills — skill; OVERVIEW.md — prose), and a fifth joins only with a named wish the four mis-served, re-justified at milestones. The law binds forward: a row queued before it carries no kind and owes no retro-fill — it names its kind the moment it next moves (its in-work claim is its intake for this axis). [T-16]

**A kind scales the steps — it never skips one silently.** The door picks WHICH steps run [T-12]; the kind picks the FORM each running step takes, never whether the walk happens. The per-kind meaning of every step — what "architecture" means for a one-file script, what "verify by deed" means for a document a human reads — has its normative home in the build-pipeline skill, one table for every project, the skill's own domain [E-12]. This spec binds the contract around it. At landing, every pipeline step has either APPLIED in the form the table states for the wish's kind, or STOOD DOWN by name in the landing's report ("design-sync — text product, stands down"), so a skipped step is always a written fact, never an omission. An unresolved kind scales nothing down: while the kind question rides the row [INV-12], every step applies in full, because standing a step down requires a NAMED kind to answer for it. What no kind may ever touch: the door law and its tripwires [T-12, INV-16], the delta's mandatory sentences — fences, facets, non-goals, success measure [T-14, INV-18, INV-20, INV-21] — and ask-at-intake [INV-12]. The kind dials the machinery, never the safety net — the same law a scope cut obeys [T-15]. [INV-22]

**Each step is worked in its craft's mindset.** One generalist head walking the whole pipeline produces generalist artifacts — a spec that reads like a coder's notes, a matrix that checks what was convenient to check. So every step names the profession whose head you wear while walking it:

- the spec — a strong product manager;
- the architecture — a software architect;
- the matrix and the tests — a QA automation engineer;
- the code — a senior developer;
- the two prove steps — the prover's own formal-reviewer head;
- commit & show — a careful release hand whose reader is the human;
- the verify walk — the visitor's own eyes, not the builder's [INV-30 kin].

The full step→craft ladder has ONE home, build-pipeline's step list [E-12]. Each artifact is judged by its craft's standards, and the landing report's step accounting speaks in them. And the craft, like the step's form, wears the KIND's face [INV-22, INV-30 kin]: on a prose product the code step is worked as a strong writer, on infra as a toolsmith — the ladder names the archetypes, the wish's kind says what their standards look like in its medium. (His word 2026-07-06: when you write the product spec you are a strong product manager, when the architecture a strong software architect, when the test matrix a strong QA automation engineer.) [INV-33]

**A feature is specified past what you know to ask.** You say "add a room where photos hang." You do not say "and decide what happens on a phone," because you cannot know that is a question. So when a wish's door says feature, drafting its spec-delta walks a fixed sweep of the **standard facets** — the dimensions every visible feature has whether or not anyone names them:

- layout on a phone or narrow window
- touch where the design assumed a mouse (anything hover-only needs a touch answer)
- the empty, error, and loading states of each new surface
- accessibility: reachable by keyboard, readable contrast
- the performance envelope (at what input size it must stay usable)
- visual hierarchy: the gap between separate things larger than the gap within one thing, and a heading never dimmer or smaller than its body
- two windows at once (the same stored state open twice)
- a missing source (an input file renamed or gone)

The facet list lives in one place, the spec-author skill, one list for every project. That list is curated: a facet joins only with a named real incident it would have caught, and it is re-justified at milestones. A checklist that grows by taste rots into a forty-row form. This spec binds that the sweep runs and what counts as done. The sweep scopes to the feature's visible surfaces. A feature with none — new persistent state only, say a cache — satisfies it with one explicit sentence, "no visible surface — facets N/A", never a silent skip. A wish re-doored to feature mid-work [INV-16] walks the sweep before work resumes, because the late-recognized surface is exactly the one whose facets nobody looked at. A fenced prototype is NOT swept, since a sketch has no facets to promise [E-17]; the sweep fires when promotion makes it a feature. [T-13]

**Every facet ends as a spec sentence — silence is not an option.** A facet sentence gets written one of two ways. Decided: you, or the walk's batched questions, called it. Defaulted: the recommended option is taken so the lane keeps moving. A defaulted sentence carries the literal tag `[default]` at its line end, so a later prover tells a taken default from a hole, and the matrix derives the facet's test row either way [E-15]. The landing report's defaults list then tells the choice as a plain-words tradeoff in your product's terms ("on a phone this gallery stacks into one column — tweakable"). It never pings once per facet and never asks you to confirm, because silence is consent [INV-31]; your veto simply becomes a new wish. A facet with no sentence — neither decided nor defaulted — is a spec defect the prover flags. That is the exact hole the Room shipped through: hover-only openings, no phone layout. On an adopted or promoted surface that already lives [A-10], a default is read from the shipped truth and reconciled like any re-engineered claim [A-3], never invented greenfield against live behaviour. The sweep and the axis rule [C-1] split one dimension by time. The sweep AUTHORS the facet sentences when the feature is first specified. The axes compose and test them across views once the surface exists. [INV-18]

**A feature is interrogated for how it fits the product — a small prover on the wish itself.** The device facets above ask what every visible feature owes. Nobody has yet asked how this feature sits in the person's path. Path holes ship green because no clause ever promised the way out — enter, browse, re-enter, then stuck at the tenth picture with no way on. So a feature-doored wish's spec-delta also walks the fit walk, scaled to the wish's kind. A product or UX wish walks the visitor's journey: how the person arrives at the new thing, what they do there, where they go next from every state it can be in, what a return visit or entry through another door changes, what neighbouring behaviour it implies (no-repeat needs remembered state), what the feel owes against the approved prototype's bar [E-17], and what next feature it invites. An infra wish walks its flows: inputs to outputs, data lifecycle, failure paths. A skill wish walks trigger, correction, and when NOT to fire. The walk interrogates the feature, never the person. Derive each answer from the existing spec and the shipped truth first. A hole that is trivially closable is closed by the walker, and the closing is written down (his word 2026-07-06: close the hole and write down how it was closed). The rest are written decided or `[default]`-tagged, and only the genuine taste calls go out, batched [INV-4, INV-18]. Do not torment the user with a barrage of questions (Alexander 2026-07-06, with tlvphoto's shipped evidence in hand). The prover gains the matching focused mode, FEATURE-FIT: given one feature's delta, it walks the journey seams against the whole spec the way CROSS-LINK walks a new surface's seams. The prover already thinks in flows, states, and transitions; this pulls that thinking forward to intake. Lens lists live once, in spec-author's sweep section, curated like the facet list [T-13]. The law binds forward: a landed feature owes its walk at the first landing that touches it, never retroactively en masse [INV-21 kin]. [INV-29]

**A face you can enter once owes a way back — or a written one-way.** A surface's faces are entered under conditions: a first-visit door, an empty state, an onboarding screen, a one-time banner. A face whose condition can never re-arise is a dead end the state lenses miss. The states all have exits, yet the face has no re-entry (tlvphoto's door, 2026-07-05 — a prover pass found six seams and missed the one-way face; his words: a state machine should always have a loop: if there is a get, there is a set). The law: every conditionally-entered face states its deliberate RE-ENTRY path, or states the one-way as a decision, by name. Trigger wording is the tell. "only on first visit", "only on first run", "until dismissed" — each such clause owes its return sentence. The prover reads for it, through the entry-symmetry lens in product-prover's stress list. The fit walk's journey lens [INV-29] already asks "where NEXT from every state"; this law extends the question to faces over the visit's lifetime. [INV-50]

**Verify-by-deed walks the visit and watches the feel.** "Eyes on the artifact" used to mean only "it renders and clicks." Cheap-feeling motion and an ugly affordance both shipped green through the whole pipeline (tlvphoto's transitions, 2026-07-06). So for the product kind the verify step now includes a named VISITOR WALK: the whole journey as the person will live it. You walk the first visit, the return visit, entry through another door, "where am I and how do I move on" from any point, and the exits. You also run a FEEL pass: you judge motion quality — easing, duration, choreography — and each affordance's craft against the approved prototype as the bar [E-17]. Findings become rows or red, never a vibe or a mental note. The walk's checklist lives in the build-pipeline step-8 product cell [E-12, INV-22]; this clause binds THAT it runs for anything a person visits. It runs in the form the medium actually has: a browser product walks motion and affordance craft, a book walks its reading path and chapter flow, a CLI its command round-trip. The product's context applies the feel lens as a partial skill, never a frontend checklist forced on prose (Alexander 2026-07-06). [INV-30]

**A taste choice made without asking is TOLD, never confirmed.** While building a feature, the walk makes small taste calls itself so the lane keeps moving — an animation's speed, a button's shape, a caption's wording. You write each one into the spec with its `[default]` tag [INV-18]. What went wrong the first time was silence: a product piled up eight untold choices and read unfinished everywhere (tlvphoto, 2026-07-06). The law: the landing report NAMES each choice made without asking, in plain words with an example, marked as tweakable — and that is ALL. You request no confirmation; silence is consent; you re-ask nothing later. The person asks when they want something changed, and the `[default]` tags keep every such choice findable in the spec forever (Alexander 2026-07-06: if everything is fine for him, no confirmation is needed, and later the user will ask if they want something changed). [INV-31]

**The smallest sample is judged before the full artifact.** For a taste-heavy deliverable — voice, copy, visual style, spec prose — the build STOPS at the cheapest judgeable sample: one paragraph, one card, two sections. The human's word on that sample sets the bar BEFORE the full build spends anything. A neighbour project shipped five full media-packs that died on one tone failure a one-paragraph sample would have caught (2026-07-06). Here is the kin split, stated: the mockup-first entry condition [INV-43] is the HUMAN's declared "show me first." This law is the AGENT's own discipline: build smallest first even unasked when taste rules the deliverable. [INV-62]

**A rejected artifact reopens its SOURCE.** When the human rejects an artifact, the fix starts at the artifact's source — the spec clause, the card, or the brief that produced it. You correct the source first, then rebuild the artifact FROM it. Patching the rejected output line-by-line against an unchanged source is the five-round trap by name, and it is banned (each round re-patched the output while the unchanged card re-made the same failure; promoter case, 2026-07-06). [INV-63]

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

## Sending feedback in

You look at what shipped and something occurs to you. It might be a reaction, an answer, a screenshot with a red circle, or a log file. **Feedback** is anything a person hands back to the project, at any size, any moment, through any channel. The person is usually the host's human. When the host's product has users of its own, their reports travel the same road once a session receives them. [E-28]

The promise is simple: nothing handed in is ever lost, and everything handed in is answered by a route. Every received item lands the same session, in the home its route owns:

- a wish lands in its queue row;
- an answer lands in its decision archive and harvested row;
- a fix lands in its commit and journal line;
- workshop noise lands in the problem ledger.

Some routes had no home before this section. They get one now: the **feedback ledger (FEEDBACK.md)**. This is an append-only file beside the queue at the host root [default]. It owns field evidence, plain reactions, and wordless drops that still await their question. Each item is one dated line. The line records when it arrived, who handed it in and through which channel, what it concerns on the feature map, the item in plain words, and where it went.

Every arrival is echoed back in one sentence, one echo per item. A wish-shaped item's echo IS the wish echo [INV-27]. Everything else hears what was heard and where it went.

A re-mention of an already-recorded item appends its date to the existing line and changes nothing else. This is the problem ledger's own discipline, applied here. [INV-68]

**Three channels, one contract.** [T-20]

- **Spoken or typed** — a remark in the conversation, or a note in a file the human points at.
- **A comment on something shown** — decision pages and review pages already capture answers as saved JSON [INV-4, INV-64]. Each saved answer is a feedback item, and the capture law already names its home: the archive and its harvested row.
- **A dropped file** — a screenshot, a log, or a document. It comes from the human directly in the conversation, or from any outside session through the host's inbox door. Each item arrives as one NEW file, under the same naming and collision law wishes use [E-11], and the host's own sessions sweep it in [T-10]. A file arriving with no words gets one plain question about what it means; the ledger never records a guess.

Every item takes exactly one route, and each route already has its law and its home.

- An item asking for new behaviour is a wish. It walks wish intake with its own echo, door, and row, and the row is its home [T-12, INV-27].
- A fix-sized comment on shown work is fixed the same session; the commit and its journal line are the home. A story-sized comment queues as a wish.
- An answer to an open question closes it forever and is harvested the same session; the decision archive and the harvested row are the home [INV-59].
- A reaction to a shipped feature is FIELD EVIDENCE and lands in the ledger. The line cites the feature's scenario. The feature's success-measure sentence [INV-21] gains a place where real signals accumulate, and the ledger is the reading machinery's first honest slice. The machinery itself — measurement plugins, aggregation — stays [target] under its own long-lived row (row 48). Evidence grows into a wish only by the human's word or a tripwire verdict.
- A flaky tool or a missing dependency is workshop noise, and it belongs to the problem ledger [INV-23]. The seam is the subject: the product's behaviour goes to FEEDBACK.md, and the workshop's behaviour goes to PROBLEMS.md, one home each.

The skill that owns this behaviour is **feedback-intake**, the pack's intake half of the exchange. The pack splits the exchange: communicator carries work out to the human, and feedback-intake carries what comes back. It fires the moment any session receives a handed-in item. It also fires at every inbox sweep, for files that carry feedback rather than a wish.

feedback-intake stays quiet in three cases: on the agent's own output, on a question the agent asked, and on something the human merely mentions without handing it in. When you are unsure whether a remark was handed in, ask one plain question. feedback-intake never opens a queue row on its own judgment; the wish door owns that verdict. [T-20]

The section's edges, stated once.

**Fences its birth must hold.**

- The inbox stays one new committed file per outside item [E-11], swept first [T-10].
- The wish echo and intake path are unchanged [INV-27, T-12].
- Answered questions still close and harvest by the convergence law [INV-59].
- The problem ledger still holds workshop noise alone [INV-23].
- The queue's no-wish-ever-lost law is extended, never amended [INV-1].

**Composition.**

- Outside sessions never edit the ledger. They use the inbox door, and only the assigned session appends FEEDBACK.md. The write-ownership and fence laws carry this [INV-10, INV-11].
- The ledger is append-only and archives like the queue, never trimmed [INV-1].

**Facets and skill kind.**

- The feature's surfaces are the ledger file and the chat echo, prose read in place.
- Layout, touch, accessibility, and performance belong to the media that carry them.
- The empty state is a ledger holding only its header, which is healthy.
- Facets otherwise N/A [default].

**Non-goals.**

- No end-user feedback widget on a host's own product. A site's visitors writing in ride the measurement family (row 48) or their own wish.
- No automatic reading, scoring, or aggregation of the ledger; the reading machinery stays [target].
- No new door mechanics; the inbox is reused as it stands.

**Success measure.** You never have to hand in the same item twice. Every received item is findable in the ledger, with its route, the same session [default].

## Asking what the product does (the feature map on demand)

**Ask «покажи все фичи» and one answer hands you the whole product map — transparency is a command, not archaeology.** Two of the three standing questions already have homes: the departures board reports how the in-flight work is going at every report [INV-27], and intake places each arriving wish on the map [INV-37]. This scenario answers the third — "what does the product do today?" — with the map whole, on demand.

The answer is read live off the living documents at ask-time. The spec's scenario sections name the features. The header's current-vs-target paragraph splits shipped from promised, at the granularity the [target] tag binds: a scenario that holds both shipped law and promised parts reads "shipped, with promised parts (named)", each status sitting at that same granularity [S-0]. The queue's open rows add the rest — each in-flight feature's station, and each wish whose `map:` verdict says NEW while its scenario is still unwritten, shown as queued, a feature the queue already knows is on the map before the spec meets it [INV-27, INV-37]. The spec's scenarios and the architecture's nodes ARE the map, so a third document to maintain or drift stays absent — no feature-list file, no cached copy [E-14] — and the ask only reads the living ones aloud. Each line obeys the line law: a short descriptive name in the product's own words, what it gives its person, and the status trailing quietly — shipped · target · in-flight at its station [INV-28]. The map arrives in chat by default; a rendered page comes on your word, the show rule [default]. Routine reports keep the departures board's in-flight scope; the whole map comes only when asked. In a host with nothing to read yet — no spec, no scenario sections — the answer says exactly that and points at bootstrap or adoption, staying honest to what is there [INV-38].

The section's edges, stated once. Fences its birth must hold: the departures board's report scope stays as it was [INV-27], intake placement stays as it was [INV-37], and the no-third-document law is reaffirmed and left standing [E-14]. Facets, skill kind: the feature's only surface is the answer itself — chat, or a rendered page on ask; layout, touch, accessibility, and performance belong to the medium that carries it. The empty state is the nothing-to-read answer above. Facets otherwise N/A [default]. Non-goals: no standing feature document, no auto-refreshing dashboard, no per-feature history timeline — not this time. Success measure: an ask yields a map whose feature set covers the spec's scenario sections one-to-one plus every open NEW-verdict queue row, and whose shipped-vs-promised marks agree with the header and the [target] tags at their own granularity — checkable by diffing the lists [default].

## When a bug cuts the line

**User story:** as the product owner, I report a bug in the shipped product and it gets fixed before
anything else; the feature that was mid-build comes back on its own afterwards, and no work gets lost.

Mid-feature, you report: "the card is broken on the phone." The feature is set aside at a checkpoint,
the bug takes the lane, and once no bug is waiting, the feature returns as the very next thing to
finish.

**Precondition:** a feature is in work when the bug report arrives (with nothing in work, the bug
simply takes the lane).

**Acceptance criteria:**
1. A bug report arriving mid-feature moves the feature to **parked**, with a checkpoint written first:
   the failing test names (if any are red), the current hypothesis, the touched files. Work with
   failing tests is never committed. [T-9]
2. The bug takes the lane and runs to completion. An arriving bug, critical included, joins the
   waiting line and interrupts nothing.
3. Waiting bugs order critical-first; bugs of equal priority go by arrival.
4. Once no bug waits, parked features resume ahead of the whole queue. Nothing jumps a resume, a
   quick win included: a bubble jumps only fresh queued wishes. [T-11]
5. At most one feature is parked per lane. When several trains were rolling [T-18], a bug parks them
   all, each at its own checkpoint, and they resume in their landing order.

**Postcondition:** the bug's fix is landed; every parked feature is back in work (or landed) in its
original order; no red work was committed anywhere.

## When the workshop itself misbehaves (the problem ledger)

Some noise comes from the workshop itself. The test harness flakes. A dependency goes missing. The shell eats a command. A tool times out. You retry and move on, and the same noise then eats the same minutes in session after session.

**The problem ledger** is the host's dynamic list of this operational noise. It lives in one git-tracked file, `.live-spec/PROBLEMS.md` (the template ships in the pack). Within `.live-spec/`, only the checkpoints stay ignored [E-8]. The ledger is born on its first entry.

An entry is a **signature**: a short, greppable plain phrase such as "element not clickable: #ex-skip" or "zsh eats a bare ===". Each signature carries its dated occurrences and one status [E-24]:

- **WATCHED** — seen once.
- **OWNED** — a named queue row will solve it.
- **AGREED NON-PROBLEM** — dated, the human's word.
- **SOLVED** — its row landed, date kept.

**The walk, the moment noise fires mid-work: grep the ledger for the signature.** What you find decides the next move.

- **Not listed:** write one WATCHED line — signature, date, one line of context — and keep working. This write replaces the silent retry. It never takes the lane; a defect of the PRODUCT is a bug and goes to the bug lane instead [T-9].
- **Listed:** this is the second occurrence, and it gets an owner THAT MOMENT. Give it either a queue row (the problem will be solved) or the human's dated agreed non-problem. That verdict belongs to the human alone [INV-9]. The agent recommends, writes the recommended owner now, and the ask rides the batched report [INV-4, E-22]. The lane never stalls on it.
- **Third recurrence, no owner:** this exposes a defect of the METHOD, reaching past the single day. It leaves the host as a wish to the pack's own queue — from a host window, one inbox file [E-11, INV-10] — citing the signature and its dates [INV-23].

After the owner is written, the entry only collects dates. A recurrence on an OWNED or AGREED entry appends its date and changes nothing else. Re-raising an agreed non-problem is the human's move, and the growing date list is what he re-raises from. When a landing closes an OWNED entry's queue row, the same session flips the entry to SOLVED. The entry never waits for an audit to learn its row landed.

**A limping thing never dams the flow.** A known, owned problem stays parked while every unrelated lane keeps rolling. Such a problem is a recurring defect with its mechanical owner named, or a check held red for an understood and recorded reason. Its ledger line — or the owning row, or an expected-red note in the record — holds it in place. The human stated the principle this way on 2026-07-07: when one thing does not quite work, it should leave everything else free to move.

Two rules keep the limp parked:

- Hand-fixing loops cap at the ledger's own two-strikes law. The second occurrence buys an owner, never another hand-pass.
- Once a defect has its named mechanical owner, its instances are serviced in BATCH. The fence fixes them silently where it catches them, with one ledger append at the session's end. This is never a per-instance ceremony that interrupts the work and the human's reading of it.

The night this law landed, the clock drift had been hand-ceremonied ten times in one session while its owner, the hook row, stayed open the whole time. A real NEW bug still preempts [T-9]; this law governs the KNOWN limp [INV-56].

The seams, stated:

**Write-ownership.** Sessions write the ledger. A worker reports noise in its checkpoint, and the session carries it over. A worker whose brief names the ledger among its files may write it directly. The brief stays the write-ownership law [ACT-3].

**Concurrent edit.** Two sessions on one host share the file under the concurrent-edit fence, like any doc [INV-11].

**Same problem?** Grep and eyes decide whether two entries are one problem. Signatures stay short so the grep stays honest. One problem found under two wordings merges into one entry at the milestone compaction.

**Archival.** At that compaction, SOLVED and agreed entries move to a dated ARCHIVED tail of the same file [M-1]. One file stays the one home, and the ledger never grows unboundedly.

**Product versus workshop.** This is the workshop's law; the product keeps its own. A recurring product bug re-doors to a feature under the pipeline's rule, distinct by what broke.

**Facets.** No visible surface, so facets are N/A.

**Non-goals this landing.**

- No mechanical guardrail yet. The named candidate — a pre-push check that no entry crosses a milestone unowned — earns its row after real usage.
- No automated signature matching.
- The first foreign-host ledgers (tlvphoto, track-coach) open from their own windows. This landing opens the pack's own, with tonight's live entries.

**Success measure.** The next operational hiccup in a live-spec session lands as a ledger line instead of a silent retry, checked at the milestone audit [default].

**Before the workshop reinvents a fix, it searches for an existing skill.** Two moments trigger the search.

At a project's SETUP — founding, or adoption's orient, beside the founding questions [B-2, B-3] — the pack scans the skills already installed and the catalogs it can reach. It looks for ones matching the project's kind and its crafts, then proposes the fit list with a recommendation. The human's word picks.

At a STRUGGLE — a ledger entry reaching its second occurrence [INV-23], a taste artifact rejected twice [INV-62 kin], any failure family that keeps returning — the next attempt waits one search. An existing skill or published checklist may already own this failure class. A found skill is adopted or rejected BY NAME, and the verdict is recorded where the struggle lives: the ledger entry, the kill-list, or the row.

This law was born of a real morning: five review rounds died on a voice failure that a public skill had carried as a written checklist for months, when the search would have cost a minute and saved the five rounds (promoter, stop-slop, 2026-07-07).

Borrowing follows one practice. Invoke a found skill as it ships. Paraphrase a lesson folded into our own documents, and credit its source by name. And verbatim text travels only under its license, notice kept; never republish unlicensed text [INV-65].

## A prototype stays a sketch

Exploring an idea before you commit to it is allowed. Sometimes you sketch a room before building the house. A **prototype** is that sketch. It lives fenced off in its own clearly named home, such as a `prototype/` folder or branch. "Fenced off" means the code sits apart, and nothing in the product reaches into it.

Every artifact a prototype produces carries the PROTOTYPE label, in whatever form its kind can show:

- **A rendered page** — an on-screen banner.
- **An API or data payload** — a `_prototype: true` field or header.
- **A script or CLI** — a first-line PROTOTYPE banner.
- **A bare file** — the marker in its name or header line. [E-17]

**Is it a feature or just a sketch?** The boundary sits at the door step — the point where a request becomes a product feature.

- A wish to HAVE something in the product is a feature. [INV-16]
- A request to merely SEE or TRY something, with no commitment, may live as a sketch inside the fence — no lane (no path through the build pipeline) and no spec.
- When you cannot tell which was meant, ask one plain question. Do not guess.

Opening a prototype home is a repo write like any other. The write-ownership law governs it [INV-10], and the assigned senior makes that judgment call [ACT-2]. An outside session files an inbox wish instead, and a worker never opens a prototype home on its own brief.

The fence runs one way: influence crosses out of the prototype, never in. You never wire a prototype into a prod surface, link to it from one, or style it to match one. A prod surface is any part of the shipped product a user meets. You show a prototype to the human only under its label. Nothing reaches the human AS the product unless its surface walked the full pipeline.

Promotion is not a merge. When a sketch earns its place, its feature enters at the spec step like any wish [T-12, INV-16]. The prototype serves as evidence for that spec; its code holds no rights.

The machine enforces the fence with a guardrails check that has three legs:

- **Live today** (for the pack repo): a prod file that references anything inside a prototype home turns RED. [E-6]
- **Still a target**: the surface registry's completeness scan. [E-10]
- **Still a target**: the behaviour-traces-to-spec check. [target, E-6]

When all three legs land, the header's honesty rule holds in both directions. The spec never claims what isn't built [S-0], and the build never contains what the spec does not name. Today the fence leg is enforced; the rest is promised, marked, and owned by its rows. [INV-17]

### An approved look lives in its artifact

Text cannot carry a feel. One spec clause, born from an approved visual prototype, was later rebuilt from its own prose and shipped a cheap look-alike. Seventy-five tests passed, because tests derived from a misread spec only prove the misreading (tlvphoto's door and gallery, 2026-07-05).

So when the human approves a sketch as the look, the prototype becomes the **norm** for look and feel. One law with four arms guards it:

1. **The clause cites its artifact.** A `norm: <path>` pointer sits at the clause's line end, beside its anchors. The prose carries the laws; the artifact keeps the look. spec-author owns the pointer's format.
2. **Approval freezes the artifact** into the project's records. A copy lands in `docs/norms/` with a dated provenance line — what it is, when it was approved, and which sketch it came from. The pointer cites this frozen copy. A norm pointer never reaches into a live prototype home, so the one-way fence stays absolute and the sketch stays free to die. [E-17, INV-17]
3. **The build reads the artifact.** Building a surface whose clauses carry a norm pointer opens the artifact before the code step. The landing records a one-line plan-vs-prototype diff, and a missing diff line is a defect at review, checked at build-pipeline's code step. The verify step's feel bar reads the same pointer. [INV-30]
4. **The prover reads visual clauses with the norm lens.** It flags a prototype-born clause with no pointer, or a clause contradicting its own artifact. Both belong to the "wordless door ≠ no question" class.

A story can declare that the human must see a mockup before the build starts — "show me first, then build". You write this in the wish's queue row at intake as "entry: mockup-first". It is cancelled only by the human naming it. A general "go build" moves priority; it never cancels that condition, which the door step holds.

The law binds forward. A clause owes its pointer at the first landing that touches it, never retroactively across the whole spec at once. A pointer names only a prototype the human approved as the look. An unapproved sketch stays plain evidence in its fence [E-17], and a text-born clause carries no pointer.

This landing shows no visible surface, so facets are N/A. Non-goals for this landing: no mechanical pointer-grep guardrail (a candidate after real usage); the norm artifact's own format stays free. Success measure: the next prototype-born surface lands with its pointer and its plan-vs-prototype diff line in the landing report, and the look-alike class does not recur. [default] [INV-43]

## Starting a new project (bootstrap)

**The version-control gate runs FIRST**, in the same order adoption keeps [A-0]. Git exists (init if not). A remote is settled or explicitly declined, before anything else is created, because a gate cannot protect files older than itself. Then copy the templates — SPEC, ARCHITECTURE, TEST_MATRIX, ROADMAP, JOURNAL, NEXT_STEPS — **plus the suite scaffold** (`test_scaffold.py` into `tests/`). That scaffold is the minimal runnable suite that DEFINES what "green" means for landing #1: the document set is present, every header is really filled (a leftover placeholder is red), the coverage checklist is in place, one live-state block. That green is a floor, not a ceiling. Landing #1 ships its own first real test beside the scaffold, and traceability checks grow from there. Hooks are OFFERED at bootstrap exactly as at adoption [E-6], never imposed, plain words first. Then the first wish enters the queue, and the pipeline runs from intake [B-1]. The gate is an always-rule: **no landing into an unversioned host**. Version control exists, and a remote either exists or is explicitly declined (recorded, not merely recommended), before the first landing [INV-8].

**The founding questions are asked, never inferred.** Before the first wish walks, the questions that shape everything downstream get explicit answers in the new spec's opening. First among them: **personal tool, or reusable product?** A founding answer resolves like any setting [E-13]. The human's profile answers when a line covers it: a personal-scope standing preference seeds this project's default, and the seeding is SAID, not silent. Otherwise the pack asks. It never derives the answer from examples — naming three of his own artifacts does not mean the product IS those artifacts, since they may be its first users. This is deliberately STRONGER than the walk's proceed-on-default habit [INV-4, INV-12]. An ordinary open question rides the row while the lane moves. A founding answer blocks the FIRST wish until asked or profile-read. Every later sentence leans on it, which makes an inferred one the silent micro-decision [INV-5] at its most expensive. Adoption owes the same questions at orient — A-1 carries the pointer. Origin (2026-07-05): a fresh project was founded as "a personal agent for three artifacts", the reusable-product question was never asked, and the human's standing answer was reusable [B-2].

**The pack learns WHO it is working with before any founding question resolves.** At founding, at adoption's orient [A-1], and at the first session on a new machine or with a new human, one step runs first: look for the personal profile at its one home [E-13]. When the profile exists, the pack loads it and SAYS so: the file is named, any unrecognized line is ignored aloud under the ladder's own law [E-13]. When it is absent, the pack OFFERS to create it from the template (`templates/profile.template.md`). The human tells about themselves — chat and docs language, how to address them, what they do, their own vocabulary — and may name sources for the pack to read: their repos, their docs, a public page. From a named source the pack PROPOSES lines. Every line lands on the human's word: a told line is written faithfully, a proposed line is accepted or dropped one at a time, a dropped proposal stays dropped [INV-9 is this rule's ceiling: mode and trust move only on their word]. The human may decline the whole step. The session then runs on package defaults and says so, and the offer returns at the next project setup, never mid-work. The step stands down where it has nothing to do. Once the profile exists, a later session simply loads it. A worker session never onboards anyone; its brief carries the setting lines it needs [ACT-3]. The template seeds the profile with every placeholder marked as a placeholder, so nothing in it can pass for the human's word [B-3].

**The project knows what KIND of thing it is — and the kind evolves.** Beside personal-vs-reusable, founding asks the second shaping question: **what is this project** — a book, a backend service, a static site, a fullstack app, a CLI, a skill pack. One plain line records it in the HOST profile (`project.kind`, the settings ladder's host scope [E-13]). Adoption owes the same ask at orient, with the other founding questions [A-1, B-2]. This is NOT the per-wish work-kind [T-16]. Three verdicts share the intake breath and never collapse into one:

- the PROJECT kind says what the product IS and seeds project-wide defaults — the usual work-kind, which facets and feel-lenses apply by default [T-13, INV-30];
- the wish's work-kind says what THIS wish builds;
- the placement [INV-37] says where it lands on the map.

The seed proposes, a written line disposes. A host that already records its own default (`work-kind.host-default` [T-16, E-13]) keeps it: the project kind never silently overrides an explicit profile line. The ask is always the HUMAN's. No personal-profile line can say what a host is, so B-2's profile-seeding arm never answers this question — it is asked at founding or orient, every time. The kind vocabulary is CURATED the same way the work-kinds' is [T-16]. The list above names shapes real projects already wear, and a custom kind joins through the queue with a named project the list mis-served. Custom kinds are expected, and the queue is their door. The line is ALIVE, not a founding fossil. The moment work notices the project has outgrown its kind — the static site that grew a backend — the line updates on the human's word, journaled right then, never parked for an audit. A project attached before this law owes no retro-ask. The line arrives at the next landing that would lean on it, like any forward-binding intake law [T-16 kin]. Origin (his word 2026-07-06): understand which kind of project this is, and update it when it changes, because everything evolves [INV-36].

## Attaching to a live project (adoption)

Adoption runs as a sequence, and each phase completes before the next begins. You perform the version-control gate FIRST, before anything is touched or moved, so the whole run stays reversible [A-5]. The codes below name meanings only; they impose no fixed order (proven on the first real run, tlvphoto 2026-07-04). A phase marked [target] is recorded and skipped until its machine lands. The journal names the deferral (the pilot's baseline snapshot is the precedent) [A-0].

1. **Orient — read everything first.** The agent reads every existing document BEFORE anything is touched: README, any roadmap, any spec, any test suite, journals, TODO files, wikis in the repo. Adoption never assumes a blank slate. It owes the project the founding questions about what it finds (personal-vs-reusable first; the rule lives at the bootstrap [B-2]) [A-1].
2. **Inventory.** List the code, the user-facing surfaces (seeding the host's surface registry [E-10]), and the document set from the orient pass, each with its owners (file:line for surfaces) [A-2]. Adoption's working artifacts — the orient digest, this inventory, reconcile notes — live in the host's `.live-spec/adopt/`, tracked in git as the run's audit trail, never scattered into the host's own folders (the pilot polluted the host's `data/`) [A-8].
3. **Re-engineer the existing documents into live-spec shapes.** An existing spec becomes SPEC.md sections; you keep the original claims and mark them unverified. The inventory's `file:line` pins seed ARCHITECTURE.md [E-14]. Its nodes come from the real code structure, so the architecture layer arrives at adoption. Existing tests become matrix rows that cite them at their real level, filed under those nodes [E-15]. An existing roadmap or TODO becomes queue rows. Nothing existing is ignored, and nothing is trusted unreconciled. You reconcile an unverified claim — pin it to file:line, or remove it — at the FIRST landing that touches its surface, and all remaining ones at the first milestone, whichever comes first [A-3].
   One verdict is mandatory per unbacked LIVE surface. Some inventoried surface reaches the user but carries no spec backing — a de-facto prototype, the adopted host's most common residue. The agent flags it at orient [A-10]. The human then decides per surface:
   - **promote** — it enters at the spec step as a feature [INV-16].
   - **quarantine** — moved into a prototype home and labelled [E-17]. This is itself a production change: the human is choosing that users lose the surface or see it relabelled. The move leaves a dated one-line provenance record at the prototype home (what, why, date), the attic manifest's mirror.
   - **attic** [A-4].
4. **Attic over deletion.** Any file superseded during adoption or rework moves to the **attic (attic/)**, the host's archive folder. The attic is append-only, with one manifest line per file (what it was, why moved, date). On a basename collision the source directory prefixes the name. A name STILL taken appends a numeric ordinal `-2`, `-3`. This is the pack's one collision law, stated once in the base skill (rule 18) [E-9]. Flat-with-manifest versus dated subfolders stays an open decision [D-1] [A-4]. The rule behind it never bends for anything authored: no adopt or rework run deletes a host file, and superseded files move to attic/ with a manifest line [INV-7]. One exception passes only through a gate. Adoption may OFFER a cruft sweep: clearly-regenerable junk (caches, build leftovers, already gitignored) listed with file counts and sizes, deleted only on the human's explicit OK, never silently. Authored content never qualifies and always goes through the attic [A-9].
5. **Version-control gate (done FIRST — see the note above).** If the host has no git, the agent inits it, writes a `.gitignore` that excludes heavy generated or media artifacts, and makes a pristine baseline commit (this doubles as the diff baseline). It settles the remote as a NAMED deliverable. By the first landing a remote (GitHub) either exists or the human has explicitly declined one, and the run's journal records the outcome. A recommendation alone does not close the gate; the pilot ended local-only on a mere recommendation [INV-8]. [A-5]
6. **Baseline snapshot [target].** Render or produce the current artifacts as they are and save them. This is the diff baseline the snapshot machinery [E-7] will guard [A-6].
7. **Incremental thereafter.** The host now works by the same wish lifecycle as a bootstrapped project. The agent records installed skill versions in `.live-spec/` at attach time. On any version change — live-spec or any installed skill — the agent RE-READS the changed SKILL.md before continuing. It never coasts on the stale in-memory version. It writes a one-line journal note naming old → new. The check is not event-only. At every safe breakpoint [M-2] the agent re-stats the installed skills and the package on disk (version and file mtime) and re-reads what changed, since a parallel session may have shipped an update mid-flight. The same walk asks the PUBLIC repo once a day whether the pack itself has moved, through the update check [E-25]. [A-7]

**How the skills arrive on a machine.** The pack ships one installer, `install.sh`. It copies every pack skill into the agent's skills home (`~/.claude/skills/`). It is idempotent: an existing copy is backed up with a timestamp before being overwritten, never deleted. The backup lands in an attic folder BESIDE the skills home, never inside it, so the agent never scans a stale copy as a live skill (the attic principle at install time). What the installer wrote is exactly what A-7's record clause writes down in `.live-spec/`. Installing and recording are two halves of one seam [E-21].

**How the machine learns a newer pack exists.** Freshness [A-7] re-reads what is already ON the machine. Delivery of a newer pack used to be a hand job nobody's walk owned. So the pack carries an update check, `scripts/check-pack-update.sh`. It runs once a day, at the first freshness point of the day, throttled by a dated stamp in the machine's pack home (`~/.claude/live-spec/update-check-stamp`). It asks the public repo — the VERSION file on main — whether the pack moved past what this machine runs; the walk hands it the installed version from its recorded home [M-7]. When the remote is newer the check PROPOSES in the session's own chat: both versions named, the what-changed pointer (the public journal), and the road named — `install.sh`, whose attic backup already guards the overwrite [E-21], or a plain pull where the repo itself runs the pack. It never installs anything; updating stays the human's word, like every install gate [ACT-1]. No network, or an unreadable answer, reads as one honest "check skipped" line naming the address it tried (a dead URL must not masquerade as a quiet offline day). It never blocks and never guesses. An offline day leaves the stamp unwritten, so the next session retries. A machine AHEAD of the public repo — the developer's, mid-work — reads as up to date; the check proposes forward only, never a downgrade. It is E-23's outward twin: sync-skills keeps the machine's copies true to the LOCAL repo, and the update check tells when the PUBLIC repo has moved past both.

Its edges are non-goals:
- no background daemon (a proposal belongs where the human reads, in the session),
- no auto-install ever,
- no per-skill remote diff (the pack version speaks for the whole).

Its only face is the proposal line, governed by the line law, facets N/A [INV-28]. Success measure: the day a newer pack ships, the next session on another machine proposes it unasked [default]. [E-25]

## One rulebook behind the skills

Open any skill in the pack and the same working rules greet you. Until now each skill carried its own near-copy of them. Copies drift, and the pack's own sweep proved it twice: the anchor convention was told two ways across skills, and the concurrent-edit fence appeared only in the adoption text, though every skill that writes shared files needs it.

The five rules every skill works by are these:

- **Ask, never guess** — when a fact is missing, you ask for it.
- **Plain words, with the code trailing quietly** at the end of the clause it anchors.
- **One surface, one name** — a thing is called the same everywhere it appears.
- **One canonical home per fact** — each fact is stated in a single place.
- **A junior resumes from a checkpoint** after a cut-off, picking the work back up.

**So the shared rules live once, in the base skill.** The base skill is the pack's shared rulebook, and it sits beside the working skills in the folder `live-spec-base`. The package itself is the source; the standalone repos are read-only mirrors of it [D-4]. The base states each shared rule normatively, right next to the package's default settings [E-13].

Every working skill opens with one line. That line names the base skill and the base version the skill was written against. This version pin is swept in the same session that bumps the base, so it never goes stale. After that line, the skill references the shared rules instead of restating them.

A working skill elaborates only its own domain. The communicator skill, for example, teaches you how to speak plainly. The rule that we speak plainly at all belongs to the base. A skill used standalone, outside the pack, still stands on its own: the opening line reads as plain advice, and nothing in the skill's own domain needs the base to be installed [E-12].

As the pack evolves, one thing stays true. **A shared rule has exactly one normative home, the base skill. A second full statement of it inside a working skill is drift, a defect to fold back.** The compaction pass prunes restatements older than the base at milestones, one skill at a time, so no single risky rewrite is needed [M-1]. [INV-13]

**Every place the pack lists its skills names the same complete set.** That list lives in several reader-facing spots: the working-skills sentence up top, the closing lists the skills carry, and the README's table. A list is exactly the kind of fact that drifts. The communicator's closing list was found naming four skills after the pack had grown past six, on 2026-07-07, when a worker halted and surfaced it, with two skills missing since their birth. A check runs at every commit, and a list that misses a skill goes red [INV-66].

## Who decides what

**You (the human) own taste, design, irreversible calls, publish and push gates, domain wording — and your own working contract** [INV-9]. [ACT-1] That contract is what the settings ladder RESOLVES to, described in the next paragraph. The lines about you — proactivity mode (ask-at-max | max-proactive), trust level, language, domain vocabulary — live in your personal profile and follow you everywhere. The **host profile** at `.live-spec/profile.md` narrows them for one project when you say so. It is created at attach and git-tracked in the host repo like the adopt artifacts [A-8]. Of `.live-spec/` only the checkpoints stay ignored [ACT-3] [E-8]. Communicator reads the resolved contract before every human-facing exchange, resolving the ladder rather than opening one file [E-13]. **Mode and trust are written ONLY on your word.** The agent may propose them, and it never sets them; it never raises its own trust or proactivity level. [INV-9]

**Answer "Did you actually do X?" by walking the evidence, and let the answer wear its method version.** You ask whether something was done, adopted, or true — "did that project run the tests by the method?" — and a fluent story comes back. The story may even be right, yet you cannot tell VERIFIED from NARRATIVE, and that difference is the whole point of the method. So a done-claim is never answered from memory. Each claim in the answer is pinned to a checkable artifact — an adoption record, a prover record, a suite run with its count, a git commit, a matrix row — walked NOW rather than recalled. This is the claims-need-primary-source rule applied to the answering exchange itself. What the walk verified is stated apart from what is merely asserted, in plain words. Because "done by live-spec" means nothing without a version, the answer names the METHOD VERSION the work was done by — the pack and skill versions read from that host's installed set (the version homes, [M-7]). One claim line reads claim → artifact → version: "suite green — 795 tests, tonight's run, commit `193d39d` — done by live-spec 0.8.x, prover 0.1.8". Where the host HAS no installed set — never adopted, or the work predates adoption — the answer says exactly that in plain words: an absent version is itself an honest answer, never an invented one. Born 2026-07-05: the track-coach answer was right, and he still could not tell which half of it was checked. [INV-25]

**Settings climb a ladder of four NESTED scopes, and the narrowest word wins.** Every way the pack behaves for you is a named setting with a home in exactly one scope, and the scope is chosen by what the setting DESCRIBES:

- about the pack itself → the **package defaults**, each value stated in the base skill beside the rule it tunes [E-12];
- about YOU, following you across every project (language: docs and commits vs conversation · proactivity mode · trust · your domain vocabulary) → your **personal profile**, one file per human at `~/.claude/live-spec/profile.md`;
- about THIS project → the **host profile** [E-8];
- about RIGHT NOW → the **session scope**, your live word in one conversation.

The scopes nest: the package holds every human, a personal profile holds every project that human touches, and a host holds every session run inside it. A setting made at a broad scope is INHERITED down through the narrower ones until a narrower one overrides it on your word — an all-English project overriding your Russian-chat line, or a "today answer me in English" overriding both for one sitting. Resolution therefore reads from the narrowest scope out: session beats host beats personal beats package default. Profiles are re-read at the same freshness points as skills [A-7]. A profile line the current pack does not recognize (written under an older vocabulary) is ignored ALOUD — a dated note in the host's journal plus a line in the session's next report. The journal half is durable, so a session dying before its report still leaves the trace; the line is never a silent drop and never an error. [E-13]

**No override is ever silent.** An override exists only as a written line in its profile file, and setting one leaves a dated journal note in the home it governs — the host's journal for a host line, the package's journal for a default change. This is the no-silent-micro-decisions rule [INV-5] applied to settings. Live-spec's own push gate [M-6] is the worked example: the package default asks for a full prover pass before a MINOR bump, and live-spec's own host contract tightens it to "before every push" — recorded, visible, never assumed. The session scope is the one that is never a file. A session override lives only in your spoken word and dies with the conversation; the agent never writes it anywhere on its own. If it should outlive the session, that is a PROMOTION into the profile it describes (personal or host), made on your word and journaled like any other override. An announced self-compaction [M-2] carries the live session lines forward in its summary. A full wipe ends the sitting, and session lines die with it by design — that loss is your own move, never the agent's. [INV-14]

**Your profile is the ONE home of the personal layer, and the global instruction file is a thin loader.** Everything personal — who you are, how you like to be spoken to, your standing working rules — lives in the personal profile, gathered in one place. The machine-global instruction file (on this stack, `~/.claude/CLAUDE.md`) shrinks to a thin loader: the pointer that loads the profile, plus ONLY the bootstrap lines that must hold before any pack file is read. The which-project disambiguation rule is the type specimen: the rule that stops a session writing into a foreign repo cannot itself wait for that repo's files to load. The loader is those bootstrap lines' ONE home, and the profile never restates them [INV-13]. Migrating an existing rule file into this shape is a fork by scope — each rule moves to the scope it describes: a method rule the pack already states stays the pack's (a second copy is drift [INV-13]); a personal line → the profile; a project line → that project's host profile. It is proven lossless by a rule-by-rule mapping, with the old file kept in the attic [INV-7] so one move rolls the whole change back. The fork only WRITES what the running session owns: pack rules land in the pack, and the personal profile lives on the human's machine outside any host or pack repo. A PRIVATE repo the human owns may serve as its git home; sitting outside any repo fence [INV-11], a promotion RE-READS the file immediately before appending, and that git home is its recovery net. A project line becomes a written migration note that the project's OWN session lands at its next update, so nothing in this migration writes a foreign repo [INV-10]. [E-16]

**The senior agent** owns judgment: spec deltas, matrix levels, findings triage, this document. [ACT-2]

**Workers (tiered)** own mechanical execution, with persistent checkpoint files in the host's `.live-spec/checkpoints/` (gitignored; never /tmp, since a reboot must not erase a resume point). Three tiers stand:

- a no-decision one-shot on **haiku**;
- multi-step mechanical work on **sonnet**;
- judgment on the **senior**.

Which tier a unit of work is PROPOSED at, before the senior may overrule it, is the routing rule below [INV-69].

**The worker contract** binds every delegation:

- A worker inherits its session's write-ownership [INV-10] NARROWED to the files its brief names; outside them it reads and never writes.
- A brief may instead name an ISOLATED copy of the tree (a parallel lane's build stages work there), and that copy's delta reaches the shared tree only through the senior's integration under the pen [T-18, INV-39].
- Files a same-session SIBLING worker just wrote are fence-benign: the concurrent-edit fence [INV-11] alarms on foreign sessions and stays quiet for your own briefed hands, and the senior who briefed both owns their seams.
- The session's live setting lines [E-13] ride INTO the brief verbatim, because a worker never resolves the ladder itself — it cannot hear the human's spoken word.
- the brief ARMS the worker for the workshop: it carries the host's problem-ledger path with the WATCHED-line duty. Noise the worker hits goes into its checkpoint as a ledger line — signature, date, one line of context — never a silent retry; the senior carries the lines into the ledger at verify unless the brief names the ledger among the worker's files [INV-23].
- It carries the CLOCK — the date and time read at briefing — so a worker's stamps come off the brief's clock, never invented [INV-24] (the day the briefs carried no clock, both eval arms led their reports with a wrong hour, 2026-07-06).
- A result that fails its brief's acceptance escalates ONE tier with a logged line (haiku → sonnet → senior), never a silent retry on the same tier, never a skipped rung. [ACT-3]

**The routing rule — propose the cheapest tier that can pass the brief, and the senior may overrule it aloud.** Before a unit of work is delegated its tier is PROPOSED, never defaulted, and the proposal reads what the work IS, looking past the row's size alone. A judgment step — a spec delta, a prove pass, an architecture carve, the matrix's level calls, findings triage, any taste call — proposes the senior, ACT-2's own [ACT-2] and never routed down. A mechanical step proposes a worker:

- a no-decision one-shot (a grep, a dump, a known-string edit) → the **haiku** tier;
- a self-contained multi-step brief (edits across named files, a pipeline run, tests written to a fixed matrix) → the **sonnet** tier.

The size class is only a coarse prior: a large row carries more delegable mechanical mass, a small one is often all-judgment, and the STEP inside it decides. **The economy rung moves the threshold** [T-19]:

- at `full` the map stands as written;
- at `lean` an airtight brief rides one tier cheaper (a sonnet brief that leaves the worker nothing to decide may propose haiku, and the bar to keep a step on the senior rises);
- at `tight` the cheapest sufficient tier is always the proposal, the senior spending its hours on judgment alone.

**The proposal is advisory — the senior may override per wish, and the override is LOGGED** [D-2]. A brief that looked mechanical but hides a real decision routes UP; a rare over-cautious default routes down; either way one line rides the checkpoint and the landing report — proposed tier → chosen tier → why. This assignment-time override is distinct from ACT-3's failed-acceptance escalation: one is the senior's choice BEFORE the work, the other a runtime bump AFTER a miss; both logged, different lines. A silent tier change is the defect this closes. The router never hardens into a mechanical gate the senior cannot overrule, and it never touches the human's gates or ACT-2's ownership of judgment. No visible surface — facets N/A. Non-goals: no token meters or numeric budgets (the rung stays qualitative [T-19]); no fourth tier and no renaming of the three; no auto-routing that overrides the senior's word. Success measure [default]: the first routed landing names, in its report, the proposal → choice → why for each delegated unit, checked by your read of it. [INV-69]

**A worker's green gets a second pair of eyes, and verify can turn adversarial.** A worker's report is a lead and no more; it never counts as evidence. On a large delegated landing the blind spot is structural: the same head that wrote the brief reads the result, so "tasks completed, goal missed" ships green (the neighbours' verifier lesson, row 107). So the verify step carries an ADVERSARIAL option. A FRESH-context checker is briefed with the SPEC sentences the landing claims (the anchors) and the artifact paths — never the worker's summary, never the senior's plan. It opens on the hypothesis "tasks completed, goal missed" and walks each claimed fact up a fixed ladder:

- EXISTS — the artifact is there;
- SUBSTANTIVE — not a stub (the grep list lives in the pipeline's step 8: TODO / FIXME / placeholder / lorem / hardcoded sample / empty body);
- WIRED — reachable from the surface that claims it;
- FLOWS — real values move end to end.

Findings become rows or red, never a nod. It fires MANDATORY when the code step was delegated AND the delta is surface-sized (a new surface or a multi-file behaviour change); anywhere else it is the senior's option. A skill or prose landing walks the same ladder in its kind's form — the checker re-reads the SHIPPED text against the spec sentences. The checker is a worker like any other — contract, checkpoint, ledger duty [ACT-3] — and its verdict rides the landing report. [INV-46]

**A brief is born from read files, never from memory of them.** Before authoring a brief that edits existing files, the brief-writer READS IN FULL every file the work will modify. The brief records three lines per file: current state · what changes · what must survive. Every step carries a back-reference to the spec sentence it serves, and every technical claim in the brief cites its source — a file:line, a command's output. A brief written from memory hands the worker the senior's guess dressed as fact (the neighbours' story-file lesson, row 107; the night the anchors were quoted from memory, the worker walked into a wall twice). [INV-53]

**A worker stops only on a named condition.** The brief carries the HALT list, closed and short:

- an ambiguous requirement;
- two consecutive unexplained failures of one command;
- a missing config or dependency;
- acceptance impossible as briefed.

On any of these the worker STOPS with evidence; otherwise it runs to completion. This is sharper than "ask if unsure", and it composes with the one-tier escalation law [ACT-3]. (The list's first full night: three workers HALTed by it, every stop a real defect and two of them the senior's own.) [INV-54]

**A brief is sized to its worker's head.** A brief targets a bounded share of the worker's context, and the work SPLITS above it. The default bound is concrete: the brief's own text stays within ~300 lines and names at most ~8 files to edit [default]; above either, the work splits into staged briefs. A brief passes PATHS, never inlined file bodies — the worker reads its own truth from disk, and an inlined body goes stale the moment a sibling edits the file. [INV-55]

## From the spec to the tests: two layers that must not be skipped

**The test method lives in one skill, and the pipeline invokes it.** The matrix derivation and the test writing (the pipeline's steps 5–6) are worked by the **test-author** skill: the level ladder (string / DOM-text / browser-computed / pixel), real-artifact assertions, red-first proof, the pinned skip-set, and traceability as a standing test. build-pipeline invokes it exactly the way steps 1–2 invoke spec-author and product-prover. The method's one home is the skill; the pipeline keeps the order and the gates. This method was born of a real failure: two visible bugs passed ~660 string-only tests, and the rebuild's method knowledge had no durable home until this extraction (track-coach, 2026-07-02..04; extracted 2026-07-07) [E-27].

The spec says WHAT the product is. Tests prove facts about the shipped artifact. Between them live two documents that were once implicit, and an implicit layer is a lost layer. Alexander caught the gap 2026-07-05: the pack taught a matrix template but never the layers that produce it.

**The architecture doc (ARCHITECTURE.md)** describes how the product is BUILT. It is a short list of named nodes: pipeline stages, modules, and surface owners. Each node carries one responsibility and one name — the one-surface-one-name rule applied to structure. Every spec fact is OWNED by exactly one node.

In a live codebase every node pins to its owning place, and the NORMATIVE pin is the named thing: a function, a marker comment, a selector, a section heading. The `:line` beside it is a convenience cache that may lag. A reader resolves the name, and a drift check re-greps it. Pins rot silently otherwise: one real host drifted 7 of 17 pins in ONE working session, and a wrong-with-confidence pin is worse than none.

Drafting the architecture IS where spec claims get reconciled against shipped reality. Each pin comes from a command actually run, never from the doc's own prose. You write it from the proven spec (template: `ARCHITECTURE.template.md`). Like the spec, it is PROVEN before anything derives from it: a product-prover pass with the architecture lens. That lens checks that every spec fact has an owning node, that no node stands without spec backing, and that the seams between nodes are named.

A large or surface-class wish updates the doc before the matrix is touched. A bug or small wish cites the existing node it lands in. When its fact has no owner yet, it ASSIGNS that fact to the fitting existing node — recorded in the doc, and an assignment alone triggers no re-prove — so no fix lands the thing the rules forbid. The doc is re-proven when its structure CHANGES, not on every landing.

The doc is ITERATIVE, like the spec it serves. It maps the product as it stands plus the landing in flight. A node exists for what ships today, or for what the spec already promises under an owned queue row (marked [target] with an empty pin). It is never designed several milestones ahead. A future feature earns its node when its landing arrives. Speculative nodes are unbacked structure — the architecture's own silent micro-decision. Re-carving the whole map IS legal: it arrives as a restructure placement's own queue row [INV-37], walks this step, and is re-proven like any structure change [E-14].

**The architecture owes numbers, not only names.** The architecture doc states MEASURABLE quality budgets for what it builds. It also states each budget's INSTRUMENTATION home: where the real numbers are measured, and where a human reads them — an export, a debug view, a report. What is measurable is not one-size; **the project's KIND [INV-36] proposes the dimensions**. The architecture step asks "what does quality MEAN here, in numbers?" before writing any. The answer depends on the kind:

- A user-facing product measures paint and interaction times ("the first image appears within 2 s on a cold visit").
- A backend service measures latency, throughput, and error rate.
- A CLI or pipeline measures run time on a typical input and per-unit cost.
- A skill pack measures its evals' pass rate and suite wall-time.
- Prose measures what honestly HAS a number (a reader reaches X within one scroll).

Where a quality genuinely has no honest number, the architecture SAYS so by name instead of inventing a vanity metric. A budget is asserted by acceptance: a matrix row at a level that can see it. A hope in prose does not count. A surface whose architecture names no budgets and no instrumentation home is a derivation defect the prover flags, exactly like an unowned fact.

The numbers themselves are the host's taste. The architecture proposes them with a recommendation, set on the human's word at the surface's first budget landing. Like the two layers themselves [INV-15], the duty binds from the first landing that touches the surface after the clause exists. It never binds retroactively across a host's whole map. This duty was born of a real miss: a gallery's first picture loaded long, and the human found it before any check did — that architecture had named no budget and measured nothing (2026-07-06) [INV-41].

**The test spec — the matrix is DERIVED, never just filled.** The matrix [E-5] is not a bucket of rows. Derivation is a method with a checkable output. Rows are organized **architecture node × spec fact**. Every fact gets at least one row. Every row pins a test level. Derivation closes with the **coverage validation**, a checklist whose home is the matrix template, actually walked:

- Every spec anchor appears in ≥1 row.
- Every artifact-inventory entry owns ≥1 rendered-level row.
- Every visibility/layout/colour/interaction fact sits at level ≥ browser-computed.
- Every node carries its negative-side rows [INV-6].
- No row cites an anchor or node that no longer exists (stale rows retire, they never vanish).

A fact with no row, or a row at a too-weak level, is a derivation defect. The prover catches it at derivation time, before the user ever hits it [E-15].

While both layers live, one thing holds: **no wish lands whose facts lack an owning architecture node and a matrix row at the right level.** You walk the bridge from spec to tests layer by layer, never jumping it. A project that predates these layers — this pack itself included — brings them up as an OWNED landing. The invariant binds from the landing that creates its ARCHITECTURE.md and matrix, never retroactively. The pack's own bring-up is queue row 50 [INV-15].

## The machines that hold the bounds

What keeps "it works" honest — each one a named machine:

- **The matrix (TEST_MATRIX.md)** — at least one row per fact, each row pinned to a test level [E-5]. It is organized architecture node × spec fact, produced by the derivation method above [E-14, E-15]. Every row states the positive AND the negative side — what the fact does and what it must never do; the negative side is the regression fence [INV-6].

- **The guardrails** — mechanical checks wired to the pre-push hook [E-6]. They run live for the pack repo itself, where each push must show:
  - a today-dated prover record exists;
  - the suite green — its RUN scoped by the diff's reach, so a prose-only diff stands the suite down by name and everything else runs it whole [INV-45];
  - every anchor owned by exactly one node;
  - no unchecked matrix-coverage box;
  - the prototype fence — no prod file references into a prototype home [E-17, INV-17];
  - plus the opt-in concurrent-edit fence on commit.

  Still [target]: the host-facing set — completeness against the surface registry, tests-present, behaviour-traces-to-spec, and declared-scope diff vs snapshot. On a host, hooks are OFFERED, never imposed. They install only where the host uses git, and only after asking the human with a plain-words explanation, because the human may not know what a git hook is (Alexander 2026-07-05).

- **The snapshot [target: the machine; the design is decided]** — the saved artifact of the last accepted run (HTML, JSON, files, numbers), the baseline the next run is diffed against [E-7]. Its home is `.live-spec/snapshot/`: one folder per declared surface, plus one manifest line per surface — what it is, the landing that set it (row, date), and a content hash — the attic manifest's sibling. The baseline advances only at *landed*, and only for the surfaces the change DECLARED; undeclared surfaces keep the old baseline. That asymmetry catches the unasked change: the guardrails' declared-scope check [E-6] goes red when a rendered surface differs from its baseline while the landing never declared it. Adoption saves the first baseline from the artifacts as found [A-6]. Retention is last-only in the working tree, and git history is the archive: the snapshot folder is git-tracked, and of `.live-spec/` only the checkpoints stay ignored [E-8], so any older baseline is one checkout away. A too-heavy surface keeps its manifest line and hash while the bytes live outside git — only the hash is diffed. (D-3 decided with this design, 2026-07-07; the machine itself stays [target], its first mechanical slice rides the guardrails scaffold, row 3.)

- **Design-sync [target: the machine; the wiring is live]** — an OPTIONAL machine for hosts with visual components [E-18]. It syncs the components a landing DECLARED — the same declared-scope notion the snapshot diffs by [E-7] — to the team's design project (claude.ai/design), where the human reviews rendered cards. It SUPPLEMENTS the in-session render: the real render stays the authority for the landing gate, and the design project is the team-review channel. It is WIRED today (row 93's pack-side half): the switch lives off-by-default in the base skill's defaults table [E-13] under the name `design-sync`, a host turning it on writes a recorded profile line [INV-14], and the channel lines stand in communicator and in the pipeline's commit-and-show step. Still [target]: the machine itself — the first real sync on a visual host closes row 93. Every sync is gated by the human, because a sync PUBLISHES outside the machine [ACT-1]. The pack itself, a text product, never syncs, and the work-kind axis says so mechanically [T-16]: the machine applies to product-kind work on a visual host, and every other kind stands it down by name [INV-22].

- **The skill evals** — the pack's own skills are tested at the level that matters for a skill: BEHAVIOUR [E-19]. Each working skill owns at least one recorded eval — a scenario where a bare session errs and the skill's text corrects it, the skill's own red-first test, proven red at authoring with a dated run record. The eval home is `evals/` in the pack repo, one file per skill: the scenario prompt, the recorded bare failure (date + run record), what a with-skill run must show, and the checks a re-run walks. Evals re-run at milestones (the M-1 list carries the item) and at any landing that changes a skill's own BEHAVIOUR; a bump that only sweeps a pin or version line owes no re-run. A working skill without its eval is a defect the milestone audit flags.

- **The surface registry [target]** — one named list per host of every user-facing surface, and the PREFERRED form is executable [E-10]. The list lives as a declared map inside a completeness-gate test, so a mismatch IS a failing test in both directions — rendered-but-unregistered, and registered-but-empty. The `.md` file stays the honest fallback for a host with no test harness; a real host arrived with the executable form already working, and adoption recognises it rather than asking it to step backwards into a document. The completeness check scans the real rendered artifact against the list, so a surface that renders but isn't registered is RED, and the registry is self-closing.

**The gate is thorough by REACH, not by ritual.** "Run everything before any push" reads rigorous and double-misses. A README-only push pays behavioural tests that read no README line, while the checks a prose diff CAN break run never — a host audit 2026-07-06 saw a one-file README change pay a 795-test run; his word: understand what changed to know what to test, build the dependency graph, a little conservative. So the push gate derives its check-set from a declared reach map — which checks READ which file classes — mechanically from the diff's file list, never self-judged. Three teeth keep it honest:
- the map is EXPLICIT — a named file in guardrails/, patterns a human reads;
- it is CONSERVATIVE — an unmapped or new file means the FULL suite, fast paths only for explicitly claimed prose classes; "just .md" is no class, so SPEC, matrix, architecture, queue, and every SKILL.md are TESTED documents and stay full-reach;
- it is SELF-TESTED — the deciding script is red-proven on fixtures, and anything it cannot classify falls to full.

The cheap gates (prover record, ownership, coverage, loadability, prototype fence) never scope; they run at every push. "Full rigor" [INV-40] reads as: every check the diff can reach, green. [INV-45]

**A gate that blocks speaks one language.** Today each gate script fails in its own words — an agent parses prose, a human hunts the fix. The contract comes from the neighbours' CLI lesson, row 107: every BLOCKING gate on red emits ONE typed failure line — a parseable JSON object `{severity, code, message, fix}` — beside its human lines, the `fix` field the same sentence a person reads. Every check DECLARES itself blocking or advisory; an advisory check prints and never flips the exit code. A script that REBUILDS artifacts validates every output before writing any, so no half-written artifact lands on disk. The contract's operational home is the guardrails README. It binds by deed from the first gate shipped under it and sweeps the rest as each is next touched, never retroactively en masse. [INV-47]

## The package repo: who may write, and two sessions at once

live-spec eats its own cooking: this spec, this queue, and these rules govern live-spec's own development. The pack repo's push gates run mechanically on installed hooks — a fresh prover record, a green suite, anchor ownership, and matrix coverage, all under `guardrails/`. The host-facing checks stay [target] with E-6. [M-4] That makes its repo a shared surface, and one evening of two parallel sessions taught us the rules.

**The developer's own machine keeps its skills fresh by name, not by habit.** The repo is the source [D-4]. The installed copies under the agent's skills home are mirrors. A session that edits a skill syncs the installed copy the SAME session, through the named tool `scripts/sync-skills.sh`. That tool copies each repo skill over its installed twin, and it reports every version change old → new — the exact line A-7's re-read rule fires on. A hand-copy is the anti-pattern the tool retires: it syncs silently, so nothing tells the next breakpoint what changed. [E-23]

**Only a session you assigned to live-spec itself writes this repo** (spec, queue, journal, skills, templates, adopt procedure). Every other session is read-only here — a host adopt run, a skill install, anything that merely reads the package. It has exactly one exception: creating a new wish file in the inbox. The test is crisp. If the session cannot say "the human asked ME, in this conversation, or via a standing routine the human created FOR live-spec, to change live-spec", it does not write. A host run's story lives in the HOST's journal, never here. [INV-10]

**The inbox (inbox/)** is the parallel-safe intake door for wishes and feedback born outside a live-spec session. Each item arrives as one NEW file, named `YYYY-MM-DD-<source>-<slug>.md`. If the name is taken, append `-2`, `-3`, and so on — the same one collision law, base rule 18. When two sessions race one slug, they add a short session token to the source mark. A file holds a few plain lines, and it never edits an existing file: creating a fresh file cannot collide, while shared files can.

The outsider COMMITS its one new file — a commit touching inbox/ only, its message naming the source. That commit is inside the read-only exception. The door is host-general: every host carries its own inbox/ under the same law, swept first by that host's own sessions. That is what keeps "no wish is ever lost" [INV-1] true when two contributors' sessions share one host. [E-11]

A live-spec session sweeps the inbox as its FIRST act. It harvests each file into the home its route owns — a wish file into a queue row as always, a feedback file by the routing law [T-20]. An item must not wait durably-recorded but operationally invisible. The harvest commit removes the file; git history keeps it, and this internal removal is not an attic case, which protects HOST files. Each harvest is ONE commit that both lands the route — the row, the ledger line — and removes its file. The landing names the source file. So an interrupted harvest commits nothing and leaves the file untouched for the next sweep, which harvests it exactly once. A committed harvest leaves no file behind to re-harvest. So "spoken means it exists" holds without the outside session touching the queue. [T-10]

**Before writing to a repo — and again before every commit** — the agent re-checks `git status` and HEAD against what it last read. Suppose HEAD moved, or the tree holds changes it did not make. Then it must STOP, re-read the changed files, and only then proceed surgically — or back off to the inbox. New files under inbox/ are the expected benign case, not a fence trip. The agent never pushes while another session is known to be live in the repo; push coordination belongs to the human. This applies to live-spec and to any host repo two sessions might share — the concurrency axis of the composition rule, made mechanical. [INV-11]

## The rhythm: breakpoints, milestones, pushes

- **Safe breakpoint (end of every movement):** Every movement ends the same way. You replace the NEXT_STEPS live state (never stack it), add a dated JOURNAL entry, and commit. Then session memory can be wiped with zero loss. NEXT_STEPS may be gitignored, so the journal entry is the durable net. A long session SHOULD take this offer. At a breakpoint the agent compacts its own context and SAYS so, never silently. A full wipe or clear is the human's move. On the way back, re-check skill freshness [A-7]. [M-2]

- **The resume file is a digest with a hard cap:** You read NEXT_STEPS in one minute at a cold start. Growth is a design failure. The whole file holds at most 100 lines [default], and a suite check owns the number. It goes red on a bloated file and red-proven on a synthetic one. The cap and the restate-every-open-leg law [INV-26] resolve by FORM, never by dropping. An open leg is restated as ONE terse line: its name, what stays open, where the detail lives. The detail flows to the journal, the queue row, or the record the line points at. Compaction moves prose to its home. It never silently drops an open leg. [INV-48]

- **Milestone (MINOR gate):** A milestone runs the full gate:
  - full spec re-prove;
  - matrix audit: the coverage validation [E-15] re-walked against the CURRENT spec and architecture;
  - surface-composition check;
  - skill evals re-run [E-19];
  - the pack's skills re-walked through the standard skill-making skill. This applies skill-creator's format, frontmatter, and description-triggering lens. Our evals test behaviour; this lens tests the CRAFT of the skill file. Findings are folded or rejected with a written reason in a dated record. A newly JOINING skill walks it at birth, before it ever reaches the gate.
  - doc COMPACTION: redundancy removed from spec/matrix/queue/skills/ledger [E-24], and the TEST SUITE swept the same way. A duplicate or superseded test is deleted only when the matrix audit shows its rows still covered by a live test. Nothing grows unboundedly. Queue compaction ARCHIVES closed rows, never deletes [INV-1].
  - a re-listing of every open human gate AND every unharvested inbox/ file, one line each;
  - the formal index re-checked against the prose, a derived map and never a second truth;
  - the derived docs' headers re-pinned to the spec version, then proven;
  - **the thin loader stays thin** [E-16]: the personal layer's global instruction file is re-read line by line. Every line must pass the "must this hold BEFORE any pack file loads?" test. The audit report states the line count. A rule that survives there without passing the test migrates to its real home (profile or pack), never lingers. [M-1]

- **Documents are versioned** like code. The queue and this spec carry dated versions, so "decided under which roadmap" is answerable. [M-3]

- **Time is read off the clock, never invented.** Every date a session writes comes from the machine's clock at write time. This covers a file name, a journal or queue stamp, and a ledger occurrence. In doubt, git is the arbiter.

  The fence is mechanical. It lives in the suite, and so in the pre-push walk. No repo file NAME, no journal entry heading, and no ledger date may sit LATER than the current clock. A future-dated stamp turns the suite red as a real defect. Prose QUOTING a past incident's wrong date stays legal.

  A second arm covers the TIME variant, since the date fence cannot see same-day times and the hand guessed them ahead three sessions running. At COMMIT, an ADDED line pairing today's date with a clock time LATER than the commit moment is red. "Pairs" means the ADJACENT stamp shape (`date [~]time`). So a line legally quoting other moments' times beside today's date stays green. The fence's first live run proved the broader reading wrong when it flagged the ledger's history lines. The commit clock is the reference, so the check is not racy. The known cost is taken deliberately: a future plan is spelled without writing it as a date-time stamp.

  The family also has a CHAT face no mechanical fence can reach. A human-facing timestamp is the [HH:MM] a reply leads with, or any moment spoken to the human. It is read off the clock AT WRITE TIME, never continued or extrapolated from an earlier stamp. Mid-session leads ran up to seven minutes fast, twice in two days, 2026-07-05/06. Where no fence exists, the rule is stated as law where the human-facing exchange shapes live, the communicator skill. Quoting a past moment's recorded time stays legal here too.

  The hand kept drifting even under the shipped law, and the ledger's chat entry re-opened after repeated catches. So the chat face grew a mechanical HAND of its own. A harness hook on the working machine — `scripts/clock-hook.sh`, wired as a prompt hook in the host's settings — injects the wall clock into every prompt's context. Every lead stamp is then read off the machine's clock. Where the hook is not installed, the law above stands alone. (The invented-time family: six catches in two days, hand-swept twice before the fences.) [INV-24]

- **Versions have named homes.** The package uses a `VERSION` file at the repo root. Each skill carries a version line in its SKILL.md frontmatter under `metadata:`, where the skill-format validator reads it. A host records the installed set in `.live-spec/` at attach and on every update. So the freshness check [A-7] compares version against version and looks past bare file times. Its "old → new" journal note is finally writable. [M-7]

- **CI mirror.** The guardrails' native home is the local pre-push hook. A host may also mirror the same checks in its CI, such as Jenkins or GitHub Actions, as a second net. There is one source of truth: CI runs the same scripts and never redefines them. The second net runs the FULL set. The reach map [INV-45] is a local latency optimization and never a CI shortcut. The worked example is the pack repo's own workflow (`.github/workflows/gates.yml`). Host guidance lives in the guardrails README (ROADMAP row 14). [M-5]

- **Push gate for live-spec itself.** This repo is public and the method's own flagship. So EVERY push is preceded, in the same session, by two steps. First, the concurrent-edit fence [INV-11]. Second, a fresh whole-spec re-check: a product-prover pass over SPEC.md as it stands, with its record landing in docs/prover/ before the push. The record name is `YYYY-MM-DD[-suffix].md`, and the suffix is mandatory when the date's file exists. Must-fix findings fold before pushing. Folds produced by the gate's own pass do NOT re-trigger the gate; they ship with the same record. The rest become queue rows. No re-check record for the pushed state means the push should not have happened. The record ENUMERATES the folds applied from its own pass. A fold stays LOCAL to the sections its finding named, and a fold reaching wider re-triggers the gate. [M-6]

- **Process bookkeeping scales to the delta — the record's reach map.** A night of eighteen landings measured it. A TINY row pays the same fixed bookkeeping as a whole surface: its own claim commit, its own full-page re-check record, its own journal chapter, and a resume rewrite. That runs roughly forty percent of its wall time, and none of it is the safety net. This answers his 2026-07-07 question, rendered in plain English: each iteration is very long — fine when necessary, but when not, find what can be done without sacrificing quality.

  So the reach idea [INV-45] applies to PROCESS. The re-check before a push keeps its RIGOR always: previous records checked, the delta walked, a verdict. It scales its FORM. A SMALL delta (skill, prose, or infra kind, with no new surface and no structure change) ships a SHORT-FORM record of three lines:
  - previous records clean
  - the delta in one line
  - the verdict

  A surface-sized or structural delta keeps the full walk. Claims batch per declared lane, one commit. The journal chapter and the resume rewrite come once per landing BATCH, never per tiny row. The irreducible is named: the law's own text written well, the red-first test, the delta's cross-link prove, and the gates. That is quality itself, never scaled. [INV-61]

## When money or time run short (the economy ladder)

Rigor costs money and time: suite runs, prover passes, senior-model hours. Today the pack always spends full rigor. This section names what a tight budget may LEGALLY shed, so economy is a setting you moved, never an improvisation under pressure. [T-19]

The pressure lives as one setting on the ladder: `budget.pressure`, with package default `full`. It moves ONLY on your word — a session's word for today, or a profile line to stand. This works exactly like proactivity and trust [E-13, INV-9]. When you name money or time pressure, the agent may PROPOSE a rung. The agent never sets one.

The pack surfaces the choice before pressure hits. At a project's SETUP, whether founding or adoption, the economy rung is asked, or the standing default told, alongside `project.kind` [INV-36]. So the preference is yours from day one.

Three rungs each name their legal sheds. Every shed you actually take is SAID in the landing report. A silent economy is a silent micro-decision, and the report exists to prevent exactly that [INV-5].

- **full [default]** — the full suite runs at every landing gate. The prover runs at its recorded cadence. The worker router picks tiers by the routing rule [INV-69].
- **lean** — mid-work test runs may scope to the touched architecture node's rows. The full suite still runs at every LANDING gate and before every push. Surface-add prover passes stay CROSS-LINK. A FULL pass owed by the default cadence may defer to the next milestone; write the deferral as a dated debt line in its queue row, never just remembered. Mechanical work rides one worker tier cheaper when the brief is airtight [INV-69].
- **tight** — everything lean, plus landing gates may BATCH: consecutive small landings share one full-suite run at the batch's end. Each landing commit still carries exactly one row's delta [INV-39]. A red at batch end bisects by landing order before anything else lands. Even so, a push still requires the full gate green at HEAD [M-6]. The cheapest sufficient worker tier is the rule, and senior hours go to judgment alone [INV-69].

What NEVER bends, at any rung — the never-bend list, stated once [INV-40]:

- the door law and its tripwires: poverty, like urgency, moves priority, never the door [T-12, INV-16];
- red-before-fix: a bug still gets its failing test before its fix;
- the human's gates: irreversible moves, publishing, authored content, taste [INV-9];
- the landing report, carrying its taken-defaults AND its named sheds [INV-5, INV-31];
- landing purity: one row's delta per commit, whatever the batching [INV-39];
- the push gate: work leaves the machine at full rigor only. Every check the diff can REACH is green at HEAD, per the reach map [INV-45], plus the host's recorded prover cadence [M-6];
- the safety net that no work-kind and no scope-cut touches: poverty is its third non-toucher [T-15, T-16];
- narration: it is cheap and stays whole at every rung [INV-35].

An explicit host line outlives any rung. A host profile pinning a tighter cadence keeps it even under `tight` [E-13]. Non-goals: no numeric budgets or token meters, since the rung is qualitative and moves by your word; and no automatic rung-switching. Success measure [default]: the first budget-named session names its rung and its sheds aloud in its landing report, checked by your read [T-19].

## Publishing — the deposit owes what its kind owes

Sooner or later a piece of work leaves the machine. A repo goes public, a skill enters a plugin directory, a release is cut, rendered cards go to a **design project**. **Publication is a surface of its own, and it owes the reader what the artifact's KIND owes.** This is the same work-kind axis you already apply, read at the door of publishing rather than at wish intake [T-16].

Each kind owes its reader a different minimum:

- a **skill** shows how to install it, the commands to run, and when to use it and when not;
- a **tool** shows real runs with real output;
- a visual **product** shows FRESH screenshots; a stale screenshot is a false claim in picture form;
- **prose** shows its reading path.

A comparison or a diagram joins when it carries the argument. It never rides along as decoration.

The per-kind publish checklist has ONE home — the publish skill, the pack's fifth working skill [E-12]. This spec binds the contract. Nothing is deposited outward past the checklist, and the walk's result rides the landing report like any step [INV-22].

**Each publish TARGET is a plugin that embeds its own steps into the walk** (Alexander 2026-07-05: a GitHub plugin brings its stages). GitHub brings a README-at-the-door plus release notes. A plugin directory brings its manifest and forms. The design project brings its cards [E-18]. The target adds steps. It never removes the kind's owed minimum.

Publishing never bypasses the gates that already stand. The human's publish gate guards anything irreversible or outward (base rule 17 [ACT-1]), and the host's own push gates guard the push [M-6]. Here the checklist runs BEFORE the gate, so what the human approves is already worth approving [E-20].

**A version push re-opens the shopfront.** Every push that ships a new version changes the truth a public reader will read tomorrow, even when the diff never touched a doc, so the shopfront rides every push. The README's CLAIMS — behaviour, counts, commands, version homes — still match the pushed truth. The kind-owed visuals ride along too:

- a skill pack re-checks its diagrams and flow pictures;
- a visual product re-shoots what changed on screen;
- a tool re-runs its example.

A stale shopfront is a false claim, exactly like a stale screenshot [E-20].

The walk is the publish skill's checklist read at push scale; the checklist's one home stays there. The pipeline's commit-and-show step points at it, and the walk's outcome rides the landing report [INV-22]. A push whose delta touches none of the shopfront's claims says so in one line, "shopfront checked — current", and a stale claim found is fixed BEFORE the push. Freshness is about the claims the README makes, not its styling.

Non-goals this landing: no mechanical README-vs-diff checker, since the reach map, row 147, is the candidate owner; and no auto-regenerated images. Success measure: no push lands whose README claims an older behaviour or count, checked at milestone audits [default] [INV-44].

## Composing across axes

Some parts of a host project hold state: a screen, a panel, a saved file — anything the user can change and find again later. The spec calls each of these a **stateful surface**, and it reviews every stateful surface from a fixed list of angles, called axes. Each axis is one question you ask about the surface: how it behaves in each view, in each mode, at each user tier, at each viewport size, and what happens when it is closed and reopened. Where two writers can genuinely act on the surface at once, concurrency joins the list. A surface's spec is complete once every axis on the list has an answer.

Adoption adds one axis: **document provenance** — where a spec claim came from. A claim is *native* when it was written fresh under live-spec, and *re-engineered* when it was recovered from documents the project had before adoption. The two start in different states. A re-engineered claim starts unverified and stays unverified until it is reconciled under the adoption rules, which pin it to real code or remove it [A-3]. A native claim is born inside the pipeline, so it is trusted from the start. [C-1]

## Open decisions

- ⟨DECIDE⟩ attic/ layout: flat with a manifest and source-dir prefix on collision (current pick) vs dated
  subfolders — revisit at the next real adopt run. [D-1]
- Decided 2026-07-07 (row 56): the model tier is **proposed, never mechanically fixed** — the routing rule
  reads the work's STEP and kind (not size alone) and the economy rung, proposes the cheapest sufficient
  tier, and the senior may override per wish with the override logged (proposed → chosen → why, on the
  checkpoint and the landing report). The rule's home is the delegation scenario [INV-69]. [D-2]
- Decided 2026-07-07 (row 55): snapshot retention is **last-only in the working tree; git history is
  the archive** — the snapshot folder is git-tracked, an older baseline is one checkout away; a heavy
  surface keeps only its hash in git. Revisit if a dispute ever needs history git cannot serve. [D-3]
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
| E-11 | inbox: one new committed file per outside item (wish or feedback) | Package repo |
| E-12 | base skill: shared rules + defaults, stated once | One rulebook |
| E-13 | settings ladder: four nested scopes, session > host > personal > package default | Who decides what |
| E-14 | architecture doc: named nodes own spec facts, pinned to file:line, proven | From spec to tests |
| E-15 | test spec: matrix derived node × fact, coverage validated per level | From spec to tests |
| E-16 | personal layer lives in the profile; global instruction file = thin loader | Who decides what |
| E-17 | prototype: fenced home, visible label | A prototype stays a sketch |
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
| T-10 | outside item arrives via inbox, swept first into the home its route owns (wish→row, feedback→by T-20) | Package repo |
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
| INV-17 | prototype fence one-way; build⊆spec honesty (fence live, other legs [target]) | A prototype stays a sketch |
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
| INV-43 | an approved prototype is the norm for look and feel, one law with four arms: the clause it fathered cites `norm: <path>` at line end, approval freezing the artifact into `docs/norms/` with a dated provenance line so the pointer never reaches a live prototype home (format: spec-author); a norm-pointered surface's build OPENS the artifact before the code step and the landing records a one-line plan-vs-prototype diff, a missing line = review defect, the verify feel bar reading the same pointer (build-pipeline code step); a declared mockup-first entry condition is written in the wish's queue row and cancels only by the human naming it, never a general "go build" (door step); prover lens: a prototype-born clause with no pointer, or clause text contradicting its own artifact = finding; binds forward, pointer only for prototypes the human APPROVED as the look | A prototype stays a sketch |
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
| INV-58 | approved text is frozen: a revision applies exactly the named correction, never a fresh rewrite around it; churn of approved material = a defect, kin of a resurfaced cut; home: communicator | Throwing a wish |
| INV-59 | no question asked twice: recorded answers searched before any ask (archives, records, journal, profile) — an already-answered question is a defect; dialogues converge (answered = closed + harvested same session; named problems return solved with evidence; round N+1 only new); home: communicator | Throwing a wish |
| INV-60 | a taste ask carries the agent's own researched proposal (mined exemplars/options with citations + a chosen recommendation); asking the human to supply what the agent should have mined = a defect; sharpens INV-4; home: communicator | Throwing a wish |
| INV-61 | process bookkeeping scales to the delta: the pre-push re-check keeps its rigor but scales its form — a small delta (skill/prose/infra, no new surface/structure) ships a three-line SHORT-FORM record (previous clean · delta one line · verdict), surface/structural deltas keep the full walk; claims batch per lane, journal + resume once per batch; the irreducible named (law text, red-first, delta prove, gates) | Rhythm |
| INV-64 | anything shown FOR REVIEW carries per-claim provenance (artifact · his recorded word · the agent's inference — inferences loudest) and is commentable with answer capture (the decision page's JSON law extends to review pages); never a read-only wall, never an unmarked inference | Throwing a wish |
| INV-65 | search for an existing skill at setup and at every struggle; adopt or reject by name; invoke as shipped · paraphrase + named credit · verbatim only under license | When the workshop itself misbehaves |
| INV-66 | every place the pack lists its skills names the same complete set — checked mechanically, a missing name goes red | One rulebook behind the skills |
| INV-67 | the showing channel matches the session's seat — local window vs the remote seat's own channel, detected and said | Throwing a wish |
| E-26 | the kill-list's mechanical face: the pack's template (dated literals, appended, never removed) + guardrails scanner guidance — a killed literal reappearing in the artifact's surfaces goes red; the law is INV-42's, this is its teeth | Throwing a wish |
| E-27 | the test method's one home — the test-author skill, invoked at the pipeline's matrix and test steps | From the spec to the tests |
| E-28 | feedback: anything a person hands back to the project; its home is the feedback ledger FEEDBACK.md, append-only beside the queue | Sending feedback in |
| T-20 | three intake channels (spoken/typed · comment on something shown · dropped file, outside sessions via the inbox door) → exactly one of five routes (wish intake · same-session fix · closing answer · field evidence beside the feature's success measure · problem ledger), the route named in the ledger line; the skill fires on receipt and at inbox sweep, never on the agent's own output, and never opens a queue row by itself | Sending feedback in |
| INV-68 | nothing handed in is lost: every received item lands the same session in its route's own home (wish→row · fix→commit+journal · answer→archive+row · noise→problem ledger), and the routes with no prior home — field evidence, reactions, wordless drops — land as dated feedback-ledger lines (who · channel · concerns · plain words · route); one echo per item; a re-mention appends its date; only the assigned session writes the ledger, outsiders use the inbox door | Sending feedback in |
| INV-62 | taste-heavy deliverables build smallest-first: the cheapest judgeable sample (a paragraph, a card, two sections) gets the human's word BEFORE the full build spends; the agent's own discipline, distinct from the human-side mockup-first entry (INV-43) | Throwing a wish |
| INV-63 | a rejected artifact reopens its SOURCE (spec clause / card / brief): source corrected first, artifact rebuilt from it; line-patching rejected output against an unchanged source = the five-round trap, banned | Throwing a wish |
| INV-69 | the routing rule: a unit of work's tier is PROPOSED by its step and kind (judgment→senior, never routed down; one-shot→haiku; multi-step mechanical→sonnet), not its size alone; the economy rung moves the threshold; the proposal is advisory — the senior may override per wish, override logged (proposed→chosen→why) on the checkpoint and landing report; closes D-2 | Who decides what |
| B-1 | bootstrap: templates → gate → first wish | Bootstrap |
| B-2 | founding questions asked, never inferred — personal-vs-reusable first; profile answers when it can | Bootstrap |
| B-3 | onboarding: the profile found or founded at setup, every line on the human's word | Bootstrap |
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
| ACT-3 | tiered workers, checkpoints; every brief carries the ledger walk + the clock; a brief may name an isolated tree — its delta integrates only under the pen | Who decides what |
| M-1 | milestone: re-prove + audit + compaction + gate list | Rhythm |
| M-2 | safe breakpoint; announced self-compaction | Rhythm |
| M-3 | documents versioned like code | Rhythm |
| M-4 | live-spec is its own host | Package repo |
| M-5 | CI mirror of the same checks: same scripts, second net runs the FULL set (the reach map stays local); worked example `.github/workflows/gates.yml` + guardrails-README host guidance | Rhythm |
| M-6 | push gate: prover re-check before every push | Rhythm |
| M-7 | version homes: VERSION file · SKILL.md frontmatter · host record | Rhythm |
| C-1 | canonical axes + provenance axis | Composing across axes |
| D-1 | attic layout | Open decisions |
| D-2 | tier routing decided (row 56): proposed not fixed, senior overrides logged → the routing rule INV-69 | Open decisions |
| D-3 | snapshot retention | Open decisions |
| D-4 | pack structure: package-is-source decided; mirrors = row 51 | Open decisions |
| D-5 | all-into-profile decided; rows 52–54 execute | Open decisions |
