# live-spec — Product Spec (v1.1.9, 2026-07-12)

> **How to read this.** Each section describes one scenario: what the reader does and what the reader sees. The short codes in brackets are markers the machine uses — the prover, the tests, and searches — and the Formal index at the end lists where each one is defined. Edit history is in JOURNAL.md. This spec states what is true today.

**What's built, and what's planned.** This spec keeps the two apart.

Built and working today:
- the skills (the base rulebook and the working skills)
- the templates
- the adoption procedure
- the inbox
- the skill evals and their records
- this spec
- the queue
- and the first guardrails: the repo's own pre-push checks and the opt-in commit fence.

Planned, each tracked by a roadmap row:
- the host-facing guardrail checks and the surface registry [E-6, E-10];
- the snapshot machinery [E-7], used by the adoption baseline (A-6);
- and the optional design-sync machine [E-18].

A planned item carries a [target] tag on a line of its own; the tag never appears on the section around it.

The suite enforces the tag rather than trusting it: the suite ties each [target] to the open row that builds it, and goes red
- if that row ships with the tag still on,
- if the tag vanishes,
- or if the tag was never named. [S-0]

## What live-spec is

The user submits any request, of any size, at any time. live-spec breaks it into small pieces and processes them one at a time. Each piece runs the same proven pipeline, reaches a landing, and ships tested. The user is free to keep thinking about other things.

Behind the pipeline is a full set of roles:
- An analyst writes the spec.
- An architect stress-tests the design and finds the edge cases and dead ends before any code is written.
- A QA works out the tests and writes them.
- A project manager runs the process and reports back to the user.

These roles are real: they are the working skills (spec-author, product-prover, build-pipeline, test-author, communicator, publish, feedback-intake). One **base skill** holds the shared rulebook and the default settings the other skills work by [E-12].

Machines enforce the process at every step, which keeps it disciplined. Every claim earns a test, and nothing ships until that test passes. The pipeline drives each request all the way to a landing and keeps its scope contained. It brings the user in for the decisions that are theirs to make.

A project can adopt live-spec at the start or partway through work already under way. Adoption brings the document templates, a procedure for joining midstream, and the guardrails the project installs. The project that adopts it is the **host**.

The host owns everything about its own work: its spec, matrix, queue, journal, surface registry, inbox, feedback ledger, and a `.live-spec/` folder that holds its profile, its checkpoints, and the versions of the skills it runs. [E-1]

## The build loop — a wish becomes shipped, tested work

The everyday path a piece of work travels: a wish comes in, gets specified, gets tested, and ships.

### Throwing a wish  [feature: F-wish]

The user is busy with something else and says "and let the card also show…," then returns to their thought. That is a **wish**: one request, in plain words, any size, at any moment. [E-2]

Within that same minute, the wish becomes a row in the **queue (ROADMAP.md)**, the persistent, ordered home of every wish. Each row holds these fields:
- the user's words
- class: size, plus priority when it is not normal
- status
- acceptance criterion [E-3]

When the user speaks a wish, its row exists before anything else happens. The row survives even if the session ends immediately after. Rows are never deleted. A row closes only with a named exit.

At a milestone, a row closed with a terminal exit (landed, declined, or superseded) moves to a dated queue archive, where it stays, never edited, never lost.

A **deferred** row stays in the active queue, carrying its revisit trigger, until the trigger fires or the row resolves to a terminal exit.

The archive holds only wishes no longer due back. [INV-1]

From its row, the wish follows one path:
1. The classifier reads its size, priority, door, and work-kind, then states them back to the user in one intake line (the paragraphs below explain each).
2. A spec-delta is drafted.
3. The delta is validated against the whole spec. Only genuinely human questions go to the user, batched. Everything else proceeds on the recommended option, marked in the row.
4. The wish is queued, then goes in-work.
5. It lands when the suite is green, guardrails pass, the commit goes in, and the row closes with its acceptance met.
6. The pipeline reports to the user in one plain-language landing line: position on the map, what landed, what remains. [T-1..T-7]

#### Intake: classifying and shaping a wish

**Several open questions arrive on one decision page.** They arrive together instead of one at a time in chat.
- The page opens in its own window; the rest of the work carries on while it waits [INV-4].
- Each question is a card — the recommended answer marked, with room to write a different one.
- Once the page comes back answered, the pipeline files it in the project's `docs/decisions/` and folds every answer into its queue row the same session. An answer left unread is a decision lost.
- The person's word settles it; the click only records a first pick: an option picked and then taken back in plain speech is withdrawn, logged as answered-then-withdrawn, and asked again later in plainer terms. A pick made without understanding settles nothing that needs the person's considered word [INV-9].
- A withdrawn decision converges: after two withdrawals the recommended option is taken as a surfaced `[default]`. An answered question closes forever [INV-59], but a withdrawal re-asks in plainer terms with no cap of its own [INV-9], so a genuine taste call could loop unbounded. The bound is two: on the second withdrawal of the same decision the session takes the recommended option and surfaces it as a `[default]` in the landing report, silence stays consent from there and it is never re-asked [INV-31] — the same convergence an answered question already has [INV-59], now given to the withdrawal path. A later real change of mind rides the ordinary channel as a new wish, never a reopening of the closed decision. [INV-130]
- How the page works — the filename, the ordering, the round-trip — is written down once, in the communicator skill's rule 10 [INV-13].

[E-22]

**A decision card asks in consequences; the mechanism trails.** A decision card opens with what each option changes for the person: what it gives them, or what problem it removes, in the product's own words. The mechanism follows only where it aids the choice. Each option is labelled by its consequence, never by its implementation. A card that cannot be answered without understanding the mechanism is a defect of the card [INV-28 kin]. [INV-32]

**A wish is classified by size, priority, and work-kind.** Size uses one four-word vocabulary everywhere: bug, small, surface, large. The queue's class column uses the same four words and no second size scale. The door is a separate axis — where the wish enters the pipeline. Size is a separate question.

Priority is normal unless the row states otherwise, with two marks:
- **Critical** — the shipped product is broken for its user: an unusable surface, lost data, or a violated safety gate.
- **Quick win** — low effort, immediate value, no design decision inside.

When the classifier cannot call a size, a priority, or a work-kind [T-16], it asks the human at intake and does not guess. Until the human answers, the wish carries normal priority; its kind is the host's recorded default, or none; a kind not yet named scales nothing down [INV-22]. The open question stays in the row while the lane keeps moving [INV-4]. [INV-12]

**A large wish negotiates scope, never time.** The walk does not ask how long a wish will take, and does not accept an estimate in hours or days as an input. When a wish is larger than its worth, the walk answers in scope terms and proposes one of two moves:
- **cut the scope** — fewer surfaces in, plainer defaults on what stays;
- **split into stages** — each stage lands through the full pipeline on its own (the large size decomposes this way [INV-12]).

The proposal proceeds on the recommended option; the lane does not park on it [INV-4]. Every cut appears in the same batched report as every taken default [INV-18], and is never silent [INV-5].

**A proven artifact settles a fork before the human hears it.** Before surfacing a design choice, a session checks whether an existing proven artifact — the architecture, the spec, the invariants — already determines the answer. When it does, the session derives the requirement and says it back with the section cited as its ground, offering no fork. A fork reaches the human only for what the artifacts leave genuinely open: a taste call, or a real trade-off with no artifact-grounded winner. This is the read-the-doc twin of ask-never-guess [INV-4] — that rule forbids inventing an answer, this one forbids offering a choice the documents have already made. It sharpens the pre-ask scan's decide-or-verify-yourself gate [INV-4, INV-81] for design forks specifically. Its home is the base rulebook beside ask-never-guess; row 259's entry impact-analysis station cites it as the verdict of its three-source read. (Born of a track-coach session that offered the owner two options while its ARCHITECTURE.md layer split already determined the answer; his 2026-07-12 word: read the architecture, derive the requirement, stop handing forks.) [INV-121]

A cut surface returned later is a new wish. A scope cut changes scope only, never order: it is not a quick-win mark, and only priority moves the lane [T-11].

No cut touches the delta's mandatory sentences — the fences [T-14], a kept surface's facets [INV-18], the non-goals, and the success measure [INV-20, INV-21]. Scope adjusts richness. [T-15]

**One wish is one user story; a row closes only whole.** A wish carrying several user stories — several distinct things a person will do and see — is split at intake, each story its own row through the full pipeline.

This differs from a stage split: a stage slices one story's depth [T-15], while separate stories are never fused into one row. Sub-behaviours of one story — its hover face, its phone face, a backpointer — are that story's acceptance, folded into that same row.

The classifier asks the human at intake whether a wish is one story or two, and does not guess [INV-12]. A split loses nothing: every row it produces cites the one spoken wish it came from [INV-1]. [T-17]

**A multi-leg row enumerates per-leg acceptance.** Where a row still carries several legs — a legacy fusion or a harvested batch — its Done-when enumerates per-leg acceptance, and the row does not close with an unmet leg. Half-done is a status, never a landing. The resume file's LIVE-STATE supersession does not compress an unfinished leg out of existence: a leg still open at compaction is restated in full [M-2]. [INV-26]

#### Naming and reporting the work

**The system speaks every captured wish back to the user.** This immediate echo lets the user know the request was received and recorded.

The echo is one plain sentence that states four things:
- what was heard,
- which door the wish entered,
- the name the work goes by,
- and its row number — for example, "caught this request; it is a feature; it is called X; row N".

A wish that arrives silently — dropped into an inbox as a file, or pulled from a batch — takes its echo in the next status report rather than as an interruption.

**Every status report names each in-flight feature and the pipeline stage it sits at.** The pipeline has nine steps, in fixed order: spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show.

Each stage name is exactly one of these nine step names, one stage per step. A feature paused at a stage is reported under that stage's name. "landed" is a terminal state — the row closed completely — and is not itself a pipeline step.

The echo also states where the wish sits on the product's feature map, specified in the next rule [INV-37]. [INV-27]

**Every wish is placed on the product's feature map, and the placement is stated by default.** The feature map already lives in the documents the project keeps: the spec's scenario sections and the architecture's nodes together constitute it, so no separate map document exists [E-14].

Each wish's placement is exactly one of three verdicts:
- **changes an existing feature** — the delta extends that scenario section and names it;
- **a new feature** — a new scenario section, plus its own node at the architecture stage;
- **restructure** — the wish fits no existing division cleanly, or fitting it reveals that the modules have outgrown their structure.

A restructure verdict does not re-divide the structure on the spot. It opens its own row — the refactor door when only structure moves, the feature door when behaviour moves with it — and the re-division goes through the architecture stage and its re-proof [E-14].

A placement may report that the structure no longer fits, but only a completed change alters the structure. A bug's placement is the feature it repairs. When the classifier cannot determine a wish's feature, it asks the user, as with any attribute it cannot decide [INV-12].

The verdict is recorded as well as spoken: the wish's row carries a note — changes X, new, or restructure — so the placement stays searchable after the report scrolls away, as the fences stay searchable in their rows [T-14 kin]. [INV-37]

**The outcome does the talking: names are plain, and every handle trails.** Two arms, one law.

- **Naming:** a feature's echo-name is a short descriptive phrase in the product's own words. It says what the thing does, and a reader who missed its birth can parse it cold. Never a private metaphor. A name that needs its story told first is a handle. A real name stands on its own, understood without the story.
- **Lines:** a human-facing report or board line opens with what changed for the reader — what they can now do, see, or stop fearing. This covers chat reports, narration lines [INV-35], report pages, decision pages, and the capture echo, while method-internal docs keep their anchors. Every internal handle — spec codes, row and session numbers, any coined name the reader never chose to learn — may only trail in parentheses. And one fact gets one standalone sentence: a compression that needs the writer's own context to parse is a defect of the line — clarity outranks cleverness.

Bookkeeping numbers are handles too: a test count, a suite size, a version string, or a check tally is never message content. The message says what the number means for the reader — tested clean, saved, the method held — and the number may only trail as a quiet anchor or stay in the records.

One carve-out, by law: when the number is the asked substance — a direct question about it, or the done-claim evidence walk, whose claim lines pin artifact and method version [INV-25] — it speaks as the answer: the number itself is the content, this once.

This law and the narration law live in skills a window may never load, so both also have a mechanical voice on the working machine:
- A prompt hook, `scripts/chat-law-hook.sh`, installed beside the clock's hand, injects a short reminder of the chat laws into every prompt: plain words with codes trailing, narration's beats, the say-what-it-IS line — the contrast frame banned in every text, its home the personal profile (language.no-scissors) — and the routing line: the orchestrator seat routes work to the cheapest sufficient tier, whatever model leads, and workers locate their own anchors (base rule 5, the routing law [INV-69]). The skills and the profile stay the laws' homes; the hook only reminds and never legislates. A window that ignores the line breaks the same law every time.
- Before a human-facing artifact — a report, a decision page, a rendered doc — is shown, `scripts/preshow-lint.py` reads its prose and flags any line that opens with an internal handle (a spec code, a row or session number), so the agent rewrites the line to lead with the reader's outcome before the human ever sees it. It's a warning to clear, never a silent rewrite, and it reads only the shown surface, never the spec's own internals, whose trailing anchors are legal by design.

[INV-28]

**Anything shown to a human passes a register lint before it is shown.** Before a human-facing surface — a rendered page, an onboarding mockup, a decision page, a report artifact — reaches the human, `scripts/preshow-register-lint.py` reads its text and flags the pack's machine dialect: a coined internal metaphor shown raw, an English pack term loan-translated into Russian text (a calque), or a transliterated pack term. A red result blocks the showing. The author rewrites the flagged text into the reader's own plain words first; the surface reaches the human only after the lint is clean. This is a block, never an advisory warning: the sibling arm `preshow-lint.py` [INV-28] warns on a leading handle, but a machine-dialect leak is what the next reader calls nonsense before walking away (2026-07-10), so it stands the showing down. The pattern set covers the coined-metaphor, calque, and unexplained-term classes in both English and Russian; each pattern is the specific coined collocation, never its ordinary constituent words. The set grows by one per caught leak: a leak that reaches a human past the lint becomes a new pattern the same day, recorded with the source leak and its date. The residual beyond patterns has its own law — a pattern lint cannot judge a novel machine-flavoured abstraction it has never been shown; that residual belongs to the clean-reader check (a fresh agent, the pack not loaded, reads the shown surface as an outside reader — docs/spec-style.md). The lint is the floor; the clean-reader check is the ceiling. The law mechanizes the profile's no-calques and register lines, and its one home is the communicator skill's pre-show walk, beside the leading-handle arm [INV-34]. The lint's reach is the shown artifact — a rendered page, a mockup, a decision page, a report artifact; a chat line stays under the hook's reminder and the walk's own read, and a mechanical gate for chat is its own queued work (queue row 203).

[INV-83]

**No line certifies its own sincerity.** A sentence that praises its author's honesty, directness, or diligence — "we say so plainly", "deserves the same honest treatment", «честно говоря», «из честного», «проверил не по памяти» — carries no information: naming not-A informs only where not-A stood as a live alternative, and a report whose every line is meant to be true distinguishes nothing by saying so. The content carries the honesty; the label comes off. Each caught phrase joins the register lint's pattern family as its own class [INV-83], and the rule binds every surface: a shown artifact through the lint, chat through the session's own read and the hook's reminder. (Set by the owner 2026-07-10, off the pack's own README certifying itself twice in one day.) [INV-94] <!-- user-language -->


**The report law is walked — a live step each time.** Chat has no suite, so the enforcement takes the form of a performed step.

Before any movement-end or milestone report reaches the human, the agent re-reads the communicator rules and passes the draft phrase by phrase through one question: does this sentence stand for a reader who doesn't live inside the pack? Any pack surface it names either gets explained in the reader's own words, or dropped.

Quiet trailing anchors stay legal, since the walk governs what does the talking, never the handles that trail. The walk's one home is the communicator skill, and its acceptance belongs to the reader: a movement-end report that makes the reader ask "what is this?" is the walk not walked. [INV-34]

**A question to the human walks the same scan — never only reports.** Before any question is asked — in a report's batched tail, on a decision page, or as a lone ask in chat — it passes the same phrase-by-phrase read (every term grounded in the reader's own words), and one gate more, asked FIRST: can I decide or verify this myself? A question that fails that gate is work, done instead of asked [INV-4, INV-5]. A question that survives it arrives with its recommendation attached [INV-60]. The failure this closes is live: a session asked its human to decide a sync phrased in jargon he could not parse — a sync the agent could simply have done (2026-07-09). [INV-81]

**Work is narrated while it runs — the third voice between the echo and the report.** The intake has its echo [INV-27] and the landing has its report [INV-28]; between them, work is narrated as it happens — the human leads several windows at once, so otherwise silence is all he gets.

While work runs, the agent says each beat worth a sentence as it happens — a pipeline station just passed, a load-bearing find, a change of direction — in one or two plain sentences, in the roadmap's terms (which wish is in hand, what it gives, what just moved), in the same voice as the reports.

The mechanical grind stays quiet; narration marks beats, never per-command commentary. The law has three parts:

- **IDENTITY:** every narration beat names the work it belongs to — which wish is in hand and which pipeline station it stands at (outside the pipeline, in research, a harvest, or a docs sweep, the work's own name serves), and whether it mends something broken or builds something new. So a reader dropping into the chat mid-session can tell what's being worked on without scrolling back.
- **DIGEST:** a station's completion is itself a beat by law, and its line carries a short digest of what the station produced, in the work's own words. The spec station says what the delta promises; the architecture station says the shape (what parts, what changed structurally); the test station says what's now covered; the code station says what now works — two or three plain sentences, never the artifact pasted into chat. A station a delegated worker closed becomes the senior's beat the moment its result lands.
- **HEARTBEAT:** when a stretch runs long with no beat — a big suite, a worker batch, a long render — narration says what's grinding and roughly why it's taking so long. A beatless stretch past ~10 minutes owes its heartbeat [default].

The heartbeat tightens when the work runs detached. A background command or a delegated worker the chat does not stream writes only to its log and shows in no agent panel, so its silence reads as lost work — the owner twice lost a multi-minute suite run exactly this way (2026-07-10). Any operation expected to run past ~2 minutes detached opens with a START line (what runs, where its log lives, an honest range [INV-93]), keeps a beat landing every ~2 minutes or at each stage [default], and closes with a DONE digest of what it produced. The mechanism stays free — the owner said a background command and a worker are the same to him; visibility is the requirement. A waiting timer earns no beat: the cadence covers real work only.

The heartbeat has a second, forward-looking face: the offline window. When the coming stretch needs nothing from the human — a local suite run, a delegated worker batch, a long render, a pipeline stretch with no gate or taste call ahead — narration says so before it starts: that he may step away, an honest range for how long (read from the work's known shape or observed runs — an unknown duration is said as unknown, never a guess dressed as a promise), and what he'll be needed for when it ends.

When he's needed again, that's a beat too, said plainly, naming the gate or decision that waits. The window is a read on the work, never a dismissal:
- beats keep landing during it so the returning reader finds the trail whole;
- questions born inside the window batch to its end [INV-4];
- a window that ends off its spoken range says so — overrun, done sooner, or blocked on his word alone, the heartbeat's own duty;
- the needed-again beat is a chat line awaiting his return, never a summons (the machinery of reaching an absent human stays outside this law);
- no offline sentence fires when the very next beat needs the human.

Together the trail is the session's time accounting: read top to bottom, it answers where the time went in work terms — token and test counts stay bookkeeping [INV-28].

A narration line is an informal chat message, distinct from a report. It walks no pre-report walk (the walk scopes to movement-end and milestone reports, a deliberate line [INV-34]), it asks nothing [INV-31], and every law of human-facing lines still binds — the outcome talks, handles trail, bookkeeping stays out of the content [INV-28].

Working notes marked as the writer's own stay a separate, skippable register; narration is for the reader, and it replaces no report — milestones still get the full one. The law's one home is the communicator (its narration rule); the personal profile holds only the person's own tuning of it. [INV-35]

**Every ask hears its price in time, and the landing settles it.** The capture echo [INV-27] carries an honest time range for the work it registers, read from the work's known shape or observed runs — unknown said as unknown, never a guess dressed as a promise [INV-35]. Work expected to run long, an hour or more, is explained up front in plain steps: what has to happen and why it takes that long. While a long stretch runs, the trail occasionally says roughly how much remains, riding the heartbeat [INV-35]. The landing report closes the loop: it states the estimate beside the actual, overrun or under said plainly — the settling is what keeps the next range honest. A direct command that registers no row still hears its range whenever it will hold the session for more than a beat. The law's homes are the communicator's echo and report rules. (Set by the owner 2026-07-10 at the 1.0 release; raised the same day when a session's own reports ran loose on it.) [INV-93]

**A rewrite that removes substance accounts for it in the landing report.** A restyle or a restructure drops content as it tightens, and some of what it drops carries weight. A rewrite or restyle that removes substance — a section, an argument, a rationale, a worked example — lists every removal in its landing report, one line of judgment each: the fact was kept and where, the owner killed it by name, or the rewriter proposes dropping and asks. A removal the rewriter cannot justify becomes a question before the report closes. Never a silent cut of substance. The rule scopes to substance and leaves line-level wording free, so a tightened sentence or a reordered clause needs no accounting. The law's homes are the communicator's pre-report walk and build-pipeline's docs-only door. (Born of the night docs pass that compressed the README's account of why live-spec stands beside BMAD, Kiro, and spec-kit to a single pointer line; the section was restored the same session on the owner's word, 2026-07-10.) [INV-109]

**One spoken leave-word winds the session down to a shutdown-safe stop.** When the human says he is leaving — «я ухожу» or any phrasing that says the machine is about to close or sleep — the session stops taking new work and walks what is open to a safe point: background workers are halted or run to their landing (a sleeping machine kills them mid-write [INV-76]; one that cannot halt in time is recorded by the handoff discipline — id, write-set, liveness checks — and the closing line says it will die with the sleep), every open lane reaches its checkpoint (base rule 6; red work is never committed — the failing test name and hypothesis top the resume file), green work is committed under its standing gates, and the resume file says what resumes where. The walk's first beat answers in time terms — roughly how many minutes to the safe point [INV-93] — and its last is one closing line: safe to power off, plus what resumes where on return. The line is said only when every point above holds; until it is said, the machine is not safe to close. The twin habit rides long work even before any leave-word: an occasional plain remaining-minutes line on the heartbeat [INV-35, INV-93], so the human can plan his exit. Non-goals: the session never guesses the human is leaving from silence, and the command makes closing safe rather than closing anything itself. The law's homes are the communicator's reporting rules and the base checkpoint rule. (Set on the owner's word from the café, 2026-07-10: one command reaches the point where the laptop can close.) [INV-95] <!-- user-language -->


#### Showing work and asking for decisions

**Anything handed to the human opens with a one-line identifier.** A page that opens in the human's browser at midnight states two things: which project it belongs to, and whether it needs the human's attention. A page that states neither reads as noise.
- The project's name appears in the visible content, not only in the URL.
- The page states what it needs from the human: "needs a word: what, by when," or "just an update, no action."

Every artifact the agent hands over or opens leads with that one-line identifier, whether it is a report page, a decision page, or a rendered doc. The chat line announcing the artifact carries the same two facts. This rule lives in the communicator skill. [INV-51]

**During an away-stretch, artifacts accumulate and one window opens at the end.** When the human has stepped away for an overnight loop or an offline window [INV-35], the agent does not open a browser window mid-stretch. Artifacts accumulate on one page: the stretch's decisions and report page. Mid-stretch re-opening is allowed only as the same page, refreshed in place. This rule lives in the communicator skill, beside the offline window, as the showing-cadence rule. [INV-52]

**The showing channel matches where the session runs.** A session running on the human's machine shows a rendered artifact as a local page in a browser window. A session running remotely runs in the cloud and is read through a browser, so it cannot open a local page.

The same content goes through the remote session's own channel instead: an artifact page the host renders for the human, or the chat itself. Either channel carries the same identifier [INV-51] and the same round-trip.

The session reads where it runs from what it can reach — the platform, the display, and whose filesystem it sees — and names the channel it picked. Handing a local file path to a remote reader is a defect of the exchange, the same failure as a window that never opened. The personal profile's show line applies to the local case; it is one instance of the general rule. [INV-67]

**The current state of the work is answerable at any moment, in any setting.** The harness's own task list and activity line are a convenience of the local terminal. A remotely-running session, read through a browser, never shows them, and even on a local session they stop updating when the work becomes a long run of tool calls, so hours pass and the human cannot tell what is being worked on.

The live status therefore lives in the chat, the one surface present in every setting [INV-67], as a short status kept current:
- **Now** — the piece of work in hand and its pipeline stage;
- **Next** — what the queue holds next.

The status refreshes at every stage change and carries a heartbeat when a stretch runs long [INV-35], so a glance answers "what are we working on, and what comes next" whenever the human looks.

The harness task list, when the setting shows it, is kept in plain product words as a courtesy [INV-28] and is not the home of the status. On a local session, a rendered status page is an optional richer view of the same Now/Next [INV-67]. This applies to every project the pack runs, not only one host. [INV-71]

**The end of a stretch is delivered so the human cannot miss it.** A report that exists but sits above tool noise counts as undelivered.

When a stretch ends — a loop iteration going to sleep, an away-stretch closing, or a session ending — the last rendered thing is one short final line. It carries four fields:
- what closed,
- what is next,
- what is needed from the human,
- and when the agent wakes.

The long report sits above that line. The final line comes last, after every tool call. A page deliverable repeats its identifier [INV-51] in that final line. This lives in the communicator skill. [INV-57]

**A review surface shows its sources and accepts the human's edits.** Anything the agent shows for review carries per-claim provenance, whether it is a dossier, a claims page, or a draft with assertions.

The surface marks each claim by where it came from: read from the artifact, the human's own recorded word, or the agent's inference. Inferences are flagged most prominently.

The surface is commentable rather than a read-only wall. It gives line-by-line room for the human's word and captures the human's answers. The decision page's saved-answers rule [INV-32] extends to review pages, as one JSON round-trip back to the project. Its home is the communicator skill, beside the decision page rule. [INV-64]

**The human's word on a shown artifact is read as meant, and the human's cuts hold.** The confident-specialist voice at the core of this lesson lives in the promoter's own voice skill, by the human's placement decision; the pack keeps only the general structure. Two clauses follow.

First, a phrasing the human removed in a review round stays removed in every later draft of that artifact. The writer keeps the removal list written where the artifact's project keeps its records — its journal, or the artifact's own notes file — and not only in session memory. A memory wipe does not restore a cut phrasing. A cut word reappearing two rounds later is a defect, however fresh it may look.

Second, a vivid phrase from the human is adopted only as meant. A human sometimes writes mockery of a bad draft rather than guidance, and the parody metaphor can end up baked into copy as if it were prescribed. So before a colorful phrase shapes the work, the writer reads its intent from context or asks [INV-4], rather than assuming it is prescriptive.

The rule's home is the communicator skill. Two of the original wish's bans already live in the pack: no empty drama, which is the no-disclaimers rule; and no approval-begging, since silence is consent [INV-31]. Both are cross-linked from there and not restated. [INV-42]

**Approved text is frozen, and a revision applies only the named correction.** Once the human approves a text, it is settled material. A later revision applies exactly the correction the human named — trim what the human said to trim, swap what the human said to swap — and does not rewrite the surrounding text. Churn of approved material is a defect, related to a reappearing cut [INV-42]. Its home is the communicator skill, beside the removal-list rule. [INV-58]

**The removal list has a mechanical form.** For a host with taste-reviewed artifacts, the pack ships a removal-list template. It holds the human's cuts as dated literals, appended the moment a cut happens and never removed. The pack also ships guardrails guidance for a scanner: a test reads the table and greps the artifact's surfaces, and a removed literal reappearing turns the suite red. The rule stays INV-42's; this is its enforcement. [E-26]

**No question is asked twice, and dialogues converge.** Before any ask, the agent searches the recorded word — the decision archives, the review records, the journal, and the profile. Asking a question a record already answers is a defect.

Exchanges converge as well: an answered question closes permanently and is recorded into its row the same session. A problem the human named returns solved with evidence rather than re-described, so round N+1 carries only new material. Its home is the communicator skill's ask rules. [INV-59]

**A taste ask arrives carrying the agent's own researched proposal.** A genuine taste question arrives with work already done. The agent mines the material first: exemplars, precedents, and real options with citations. Then it asks, with a chosen recommendation and its evidence. Asking the human to supply what the agent should have mined is a defect. This sharpens the recommended-option rule [INV-4] for taste calls. Its home is the communicator skill. [INV-60]

#### Doors, kinds, and craft

**Priority changes the queue order, and the change is recorded.** A critical bug lands before everything, heading even the waiting-bug line (next section). Critical priority heads the queue whatever its door, so a critical-priority feature goes to the queue head too. Only the bug door preempts the in-work lane [T-9].

**Critical on a non-bug heads the queue; it does not stop the rolling lane, and the bound is echoed back at intake.** Preemption belongs to the bug door alone [T-9], so a critical non-bug heads the queue but never preempts a rolling lane — it lands as soon as the current lane reaches its checkpoint, ahead of everything else waiting, and a genuine live break that must stop the work now is a bug, which takes the pen at the end of the current pen-stage. The two are different promises, and a human who says "critical" for a live break means the bug one, so the bound is echoed back at intake: when a wish is marked critical on a non-bug door, the capture echo says plainly that it heads the queue and does not stop the lane, and only the bug door preempts — so the human hears the difference and can re-door it a bug if that is what he meant, rather than discovering at the next report that the work he thought was stopped kept running. The human's word still owns priority; this states what critical buys on each door, never refusing the mark. [INV-133]

A quick win can be promoted: when the lane frees, the agent may take it ahead of larger queued wishes, marking the promotion in its row rather than making it silently. After one promoted landing, the queue head goes next, so a stream of quick wins cannot starve a big wish forever.

An inbox wish is registered at the moment it arrives; that is when it first becomes a row the ordering rules can see. A file's own date never competes with spoken timestamps. Arrival ties resolve by queue row order, top to bottom. Within one sweep, an inbox batch is registered in filename-sorted order. [T-11]

**The door is named before any code is written.** Classification is an explicit step with fixed rules. Personal judgment does not settle it.

A row carries three axes, stated together in one intake line: size, priority, and door, plus the work-kind (what the wish builds, covered in the next paragraphs [T-16]). A wish too big for its worth is negotiated in scope, never in time [T-15]. Size, together with priority, says how big and how urgent.

The **door** says where the wish enters the pipeline: **feature · bug · refactor · docs-only · skip**. Size and door deliberately share one word: a wish sized "bug" is the bug door — one call stated once — and the door axis adds the other four entries. [T-12]

The door is decided by an ordered procedure. The tripwires fire first, before any judgment:

1. The wish is a **feature** — however casually it is asked — when any of these holds: a new user-visible surface appears; new persistent state appears; a new interaction lands on an existing surface; the touched surface is marked [target] in the spec (the canonical, machine-checkable form of "not yet specified / later surface"; the plain-prose equivalents bind too, but the author writes the tag); the change adds behaviour no spec clause backs.
2. No tripwire fired, but shipped behaviour is wrong against what the spec or product already promises → **bug**.
3. Behaviour stays identical, structure moves → **refactor**.
4. Only prose outside the normative spec changes (README, comments, guides) → **docs-only**. Rewording a spec rule changes what behaviour the spec backs, so it routes as feature or bug rather than docs-only.
5. The narrow case where all of these hold (a single file; no new state, element, or visible behaviour; an existing test level already covers the touched fact) → **skip**.

The tripwire verdict outranks a casual label. A wish called a "bugfix" that fires a feature tripwire is re-doored to feature, and the intake line records it [INV-5].

Queue-cutting [T-9] belongs only to the bug door, so a re-doored wish gets no preemption. The human's word can still raise its priority (priority belongs to the human), but no word lets a feature skip the spec step.

The door is also re-checked mid-work: the moment running work is about to create a user-visible surface or persistent state its current door does not grant, the work stops and the door step fires again. This catches the case where a change sounds like a simple edit until the surface actually exists. The re-doored wish keeps its lane and re-enters the pipeline in place, with no re-queue and no parking — parking stays a bug-preemption move [T-9].

**A mid-work re-door rebuilds the parallel-lanes independence graph.** When the mid-work re-door creates a surface or state that did not exist when the lanes were opened, the same re-check re-runs the independence edges [INV-49] against every rolling lane — the newly-created surface can now collide with a sibling that was independent a moment ago. A new edge pulls the re-doored lane back to serial: it waits behind the lane it now shares a surface with, and the departures board says so in a line, so the departures board never asserts a stale independence after the ground under it moved. The integration re-fence [INV-39] still catches such a collision at landing, so this is the observability the board owed all along rather than a new safety net — the board now tells the truth the moment the edge appears, not only when two landings collide. The senior still judges independence and says it aloud; the re-door is simply the moment that judgement is owed again. [INV-131]

One request lives outside the queue entirely: a request to merely see or try something, with no commitment to keep it, may be built as a labelled sketch (see "A prototype stays a sketch", which holds the ask-when-unclear rule).

Casual phrasing does not change the contract: a wish is routed through its door, never refused for being casual, and never hand-built past the pipeline because it sounded small. [INV-16]

**A fix touching a spec-backed literal owes its docs and test the same session.** The bug door and the skip door carry one added tripwire, fired by the door step before any code: does this edit touch a spec-backed literal or clause — a version string, a pinned count, a named vocabulary, a promised wording? A yes binds the docs-travel-with-the-change rule and the red-first small-fix path into one duty: the docs and the test land in the same session as the fix. The tripwire reads the edit's content. A one-word change to a spec-cited literal owes the same duty as a full feature; the size of the diff grants no exemption. This tripwire was born of the row 220 audit, where one-line fixes touching spec-backed literals shipped without same-session doc sync (2026-07-10). [INV-104]

**Every request enters through a three-source impact read, and the footprint decides the route.** Beside the door [T-12] and the work-kind [T-16], a third dimension is read at the same intake moment: the FOOTPRINT, read from three sources at once — the spec says what behaviour changes, the architecture says which module owns it, the code says what actually gets touched. The read produces one named footprint: **presentation-only** (the change touches what the audience meets and nothing behind it), **single-module** (it stays inside one owned layer), or **cross-cutting** (it moves a shared law or several layers at once). The footprint is spoken in the capture echo and written in the row's `footprint:` note, beside `door:`, `kind:`, and `map:`, so a wrong route is catchable after the fact rather than living in chat memory alone [INV-43, INV-108].

The footprint composes with the door rather than overriding it: the door decides which steps run [T-12], and the footprint decides how far each step reaches. The door's guarantees always hold, so a feature never skips the spec step whatever its footprint [INV-16] — the footprint sizes the reach of the steps the door grants, and it never promotes a feature past the spec step nor demotes the door's verdict. A cross-cutting change opens the full pipeline from the spec step, its architecture and matrix work spanning every layer it moves. A single-module change runs the steps its door grants with their scope narrowed to the one owned module — its architecture read, its matrix rows, and its tests bounded to that module's block and interface; a single-module bug or refactor takes the existing matrix-step entry, and a single-module feature keeps its spec step with the rest scoped down. A presentation-only change takes the lightest road its door already grants — the skip boundary or the docs-only door where the door routes it there, and the matrix-step minimum focused on the visible layer where it is a visible feature. A heavy process on a light change is as much a defect as a light process on a heavy one; the footprint, not the size, sizes the reach.

The read never silently picks a winner between the sources. When the three disagree — a surface the spec promises with no owning node, a behaviour in the code no spec clause backs, a node pinned to a line that moved — the read names the disagreement and routes it to the home that owns it: a bug row for code past spec, a spec fix for a moved pin, a restructure row for a missing node [INV-37]. This pulls the architecture step's spec-to-code reconciliation forward to the entry, so drift is a finding at intake rather than a surprise at code. The three-source read is also the verdict the derive-before-fork rule [INV-121] rests on: it is what tells whether a proven artifact already settles a question, so the only fork the human hears is what the three sources leave genuinely open.

The footprint is a guess read before the work, so it re-classifies mid-work. The moment an edit reaches past its named layer, the work stops and the footprint is read again — a presentation change that turns out to need a backend module escalates to single-module, a single-module change that touches a second module escalates to cross-cutting — and the landing report records the footprint held, or re-classified to X at step N. This mirrors the door's own mid-work re-fire.

The station carries the boundary-health law. A right module boundary shows one sign: an edit inside the module leaves its neighbours untouched, so a typical request lands in one module. Requests that repeatedly cut across the same several modules are the signal that a boundary sits in the wrong place, and the recorded footprints are the evidence; the boundary moves only through the architecture step and its re-prove [INV-37], never on a hunch and never in denial. (recorded live 2026-07-12: every incoming request gets an entry analysis reading the spec AND the architecture AND the code together, the footprint named before any work starts, the footprint deciding the route — the entry station of the fourteen-principle architect draft, its principles P1-P6. The deeper mechanical enforcement — the footprint-note suite check, the per-kind concrete-layers declaration, the cross-cut counter — rides the follow-on rows.) [INV-128]

**A landed feature-or-refactor row carries its footprint note, and a suite check holds it.** The footprint the intake read named [INV-128] — presentation-only, single-module, or cross-cutting — is written in the landing row's `footprint:` note beside `door:`, `kind:`, and `map:`, and a suite check reads the queue (ROADMAP.md): a landed feature-or-refactor row without a footprint note goes red. This is the mechanical floor under the footprint read, the same shape the delegation-accounting check [INV-103] gives the routing rule — prose states the read, the check holds it on every landing. It binds forward from the footprint read's own arrival: a feature-or-refactor row landed once the impact-analysis station was law (2026-07-12, at the station's landing) carries the note, while rows that landed before it stay as they landed. A forward-landed feature-or-refactor row never omits its footprint note. [INV-134]

**The intake line also names what is being built.** Size says how big, the door says where the wish enters, and the **work-kind** says what kind of thing the work produces, and with it, which pipeline machinery is warranted. There are four kinds today:
- **product** — something the host's own user faces;
- **infra** — tooling that serves the project itself (scripts, hooks, CI, pipelines);
- **skill** — a behaviour document an agent works by (a SKILL.md, a prompt pack);
- **prose** — a document written for a human to read (an overview, an article, a spec's own text).

The classifier calls the kind from what the wish produces, one kind per wish. A wish that genuinely produces two kinds is two wishes, split at intake; a kind the classifier cannot call is asked about, the same as an uncallable size [INV-12].

A host with one usual kind may record it as a host-profile default that the intake line starts from [E-8, E-13] (track-coach's would be product). A host whose wishes genuinely span kinds — live-spec itself ships skills, prose, and infra — records no default and calls each wish on its own.

The vocabulary is curated like the facet list [T-13]: each kind above is earned by real work the pack has already routed (track-coach's widget — product; render-doc.py — infra; the pack's own skills — skill; OVERVIEW.md — prose), and a fifth kind joins only with a named wish the four failed to serve, re-justified at milestones.

The law binds forward: a row queued before the kind axis existed carries no kind and owes no retroactive fill. It names its kind the moment it next moves (its in-work claim is its intake for this axis). [T-16]

**A skill-kind wish's verify also walks skill-creator's review.** Whenever the classifier names the work-kind `skill` — a pack skill created or edited — the verify step additionally runs the installed skill-creator's review of the touched skill: the craft of the skill file (format, frontmatter, the description-triggering lens — does the skill load when it should) and its evals where applicable. Each finding is folded or rejected by name in the landing record. The classifier is the trigger, and the walk fires on every skill-kind landing; mood plays no part. The milestone gate's whole-pack walk stays the catch-up sweep for skills landed before this law [M-1]. The walk's cell lives in the pipeline's work-kind table, the verify row. [INV-99]

**The kind scales the steps; it never silently skips one.** The door picks which steps run [T-12]. The kind picks the form each running step takes, never whether the pipeline runs at all. The per-kind meaning of every step — what "architecture" means for a one-file script, what "verify by deed" means for a document a human reads — has its normative home in the build-pipeline skill, one table for every project, and is that skill's own domain [E-12]. This spec sets the contract around it.

At landing, every pipeline step has either applied in the form the table states for the wish's kind, or stood down by name in the landing report (for example, "design-sync — text product, stands down"), so a skipped step is always a written fact rather than an omission.

An unresolved kind scales nothing down: while the kind question is still open on the row [INV-12], every step applies in full, because standing a step down requires a named kind to account for it.

No kind may ever change the following:
- the door law and its tripwires [T-12, INV-16];
- the delta's mandatory sentences — fences, facets, non-goals, success measure [T-14, INV-18, INV-20, INV-21];
- and ask-at-intake [INV-12].

The kind adjusts the machinery, never the mandatory checks — the same rule a scope cut obeys [T-15]. [INV-22]

**Each step is worked with its craft's standards.** A single generalist working the whole pipeline produces generalist artifacts: a spec that reads like a developer's notes, a matrix that checks whatever was convenient to check. Each step therefore names the profession the agent works it as:
- the spec — a strong product manager;
- the architecture — a software architect;
- the matrix and the tests — a QA automation engineer;
- the code — a senior developer;
- the two prove steps — the prover's own formal-reviewer role;
- commit & show — a careful release engineer whose reader is the human;
- the verify walk — the visitor's own outside eyes [INV-30 kin].

The full step-to-craft ladder has one home, build-pipeline's step list [E-12]. Each artifact is judged by its craft's standards, and the landing report's step accounting speaks in them.

The craft, like the step's form, follows the kind [INV-22, INV-30 kin]: on a prose product the code step is worked as a strong writer; on infra, as a tool builder. The ladder names the archetypes; the wish's kind says what their standards look like in its medium. [INV-33]

#### Specifying and building a feature

**A feature is specified past what the human knows to ask.** The human says "add a room where photos hang." The human does not say "and decide what happens on a phone," because the human cannot know that's a question. So when a wish's door says feature, drafting its spec-delta walks a fixed sweep of the **standard facets** — the dimensions every visible feature has, whether or not anyone names them:
- layout on a phone or narrow window
- touch where the design assumed a mouse (anything hover-only needs a touch answer)
- the empty, error, and loading states of each new surface
- accessibility: reachable by keyboard, readable contrast
- the performance envelope (at what input size it must stay usable)
- visual hierarchy: the gap between separate things larger than the gap within one thing, and a heading never dimmer or smaller than its body
- two windows at once (the same stored state open twice)
- a missing source (an input file renamed or gone)

The facet list lives in one place, the spec-author skill, one list for every project. That list is curated: a facet joins only with a named real incident it would have caught, and it gets re-justified at milestones.

A checklist that grows by taste rots into a forty-row form. This spec binds that the sweep runs, and what counts as done.

The sweep scopes to the feature's visible surfaces. A feature with none — new persistent state only, say a cache — satisfies it with one explicit sentence, "no visible surface — facets N/A," never a silent skip.

A wish re-doored to feature mid-work [INV-16] walks the sweep before work resumes, because the late-recognized surface is exactly the one whose facets nobody looked at. A fenced prototype is not swept, since a sketch has no facets to promise [E-17]; the sweep fires when promotion makes it a feature. [T-13]

**Every facet ends as a spec sentence; silence is not an option.** A facet sentence gets written one of two ways.
- Decided: the human, or the walk's batched questions, called it.
- Defaulted: the recommended option gets taken so the lane keeps moving.

A defaulted sentence carries the literal tag `[default]` at its line end, so a later prover can tell a taken default from a hole, and the matrix derives the facet's test row either way [E-15]. The landing report's defaults list then tells the choice as a plain-words tradeoff in the human's product's terms ("on a phone this gallery stacks into one column — tweakable").

It never pings once per facet and never asks the human to confirm, because silence is consent [INV-31]; the human's veto becomes a new wish.

A facet with no sentence — neither decided nor defaulted — is a spec defect the prover flags. That's the exact hole: hover-only openings, no phone layout.

On an adopted or promoted surface that already lives [A-10], a default is read from the shipped truth and reconciled like any re-engineered claim [A-3], never invented greenfield against live behaviour.

The sweep and the axis rule [C-1] split one dimension by time. The sweep authors the facet sentences when the feature is first specified. The axes compose and test them across views once the surface exists. [INV-18]

**The spec names its cross-cutting laws in one place, and every section answers them.** A product declares laws that cut across every surface — measurement, accessibility, error handling, a register of speech: whatever it holds itself to everywhere. The spec keeps that list in ONE declared-laws home, and each new surface's section states its line against each declared law — the clause, or a dated exemption — before the prover ever reads it (spec-author owns the habit). The prover's walk carries the matching station: per declared law, enumerate every surface and transition and demand the clause or the dated exemption per item; a missing clause ranks as a broken invariant (the worked miss: analytics covered some beats while whole surfaces emitted nothing, and only the human's eye found it, 2026-07-10). For this pack's own product the declared laws are three — the plain-language register on every human-facing surface [INV-28, INV-34, INV-83], clock-honest stamps on every dated line [INV-24], no self-certification on any claim of done [INV-94] — with two dated exemptions: measurement (the measurement family is deferred, rows 47-49/96, no live audience yet; dated 2026-07-12) and accessibility (the shopfront renders as GitHub markdown, the renderer's own accessibility carries it; dated 2026-07-12). [INV-101]

**A feature is interrogated for how it fits the product — a small prover on the wish itself.** The device facets above ask what every visible feature owes. Nobody's yet asked how this feature sits in the person's path. Path holes ship green because no clause ever promised the way out. A visitor can enter, browse, and return, and still reach a point in the flow with no way to continue.

So a feature-doored wish's spec-delta also walks the fit walk, scaled to the wish's kind:
- A product or UX wish walks the visitor's journey: how the person arrives at the new thing, what they do there, where they go next from every state it can be in, what a return visit or entry through another door changes, what neighbouring behaviour it implies (no-repeat needs remembered state), what the feel owes against the approved prototype's bar [E-17], and what next feature it invites.
- An infra wish walks its flows: inputs to outputs, data lifecycle, failure paths.
- A skill wish walks trigger, correction, and when not to fire.

The walk interrogates the feature, never the person. The agent derives each answer from the existing spec and the shipped truth first.

A hole that's trivially closable gets closed by the walker, and the closing gets written down. The rest get written decided or `[default]`-tagged, and only the genuine taste calls go out, batched [INV-4, INV-18].

The prover gains the matching focused mode, FEATURE-FIT: given one feature's delta, it walks the journey seams against the whole spec the way CROSS-LINK walks a new surface's seams. The prover already thinks in flows, states, and transitions; this pulls that thinking forward to intake.

Lens lists live once, in spec-author's sweep section, curated like the facet list [T-13]. The law binds forward: a landed feature owes its walk at the first landing that touches it, never retroactively en masse [INV-21 kin]. [INV-29]

**A face that can be entered once owes a way back — or a written one-way.** A surface's faces get entered under conditions: a first-visit door, an empty state, an onboarding screen, a one-time banner. A face whose condition can never re-arise is a dead end the state lenses miss.

The law: every conditionally-entered face states its deliberate re-entry path, or states the one-way as a decision, by name. Trigger wording is the tell: "only on first visit," "only on first run," "until dismissed" — each such clause owes its return sentence.

The prover reads for it, through the entry-symmetry lens in product-prover's stress list. The fit walk's journey lens [INV-29] already asks "where next from every state"; this law extends the question to faces over the visit's lifetime. [INV-50]

**Verify-by-deed walks the visit and watches the feel.** For the product kind, the verify step now includes a named visitor walk: the whole journey as the person will live it. The agent walks the first visit, the return visit, entry through another door, "where am I and how do I move on" from any point, and the exits.

The agent also runs a feel pass: the agent judges motion quality — easing, duration, choreography — and each affordance's craft against the approved prototype as the bar [E-17]. Findings become rows or red, never a vibe or a mental note.

The walk's checklist lives in the build-pipeline step-8 product cell [E-12, INV-22]; this clause binds that it runs for anything a person visits.

It runs in the form the medium actually has: a browser product walks motion and affordance craft, a book walks its reading path and chapter flow, a CLI its command round-trip. The product's context applies the feel lens as a partial skill, never a frontend checklist forced on prose. [INV-30]

**A taste choice made without asking is told, never confirmed.** While building a feature, the walk makes small taste calls itself so the lane keeps moving — an animation's speed, a button's shape, a caption's wording. The agent writes each one into the spec with its `[default]` tag [INV-18].

The law: the landing report names each choice made without asking, in plain words with an example, marked as tweakable — and that's all. The agent requests no confirmation; silence is consent; the agent re-asks nothing later.

The person asks when they want something changed, and the `[default]` tags keep every such choice findable in the spec forever. [INV-31]

**A tunable parameter is set to a sensible default and told, never asked.** Some choices are a knob with a range rather than a taste call — an image's resolution, a batch size, a timeout, a sampling rate. The walk sets each such knob to a sensible value itself and keeps the lane moving, the same way it makes a taste call [INV-31].

It chooses the value for a reasonable balance, cheaper or faster wherever quality allows (for example, a lower image resolution), writes it with its `[default]` tag [INV-18], and names it in the landing report with what it trades. The human tunes it afterwards only if they want a different point on the range; at most the parameter gets updated together later, and re-asking is never owed.

This carries the taste-told law [INV-31] to numeric and config knobs, and it's the same idea the economy ladder applies to cost [T-19]. So the agent never stalls a task on a knob it can reasonably set. It moves every task it can and reserves a real question for what it genuinely can't decide [INV-4].

The push to production rides the same trust: where the human has granted it, the agent ships to prod on its own certification once the work is sound, the push gate resolving to the agent's judgment — live-spec's own already does [M-6] — and the grant stays the human's to give or withdraw [INV-9]. [INV-70]

**The smallest sample is judged before the full artifact.** For a taste-heavy deliverable — voice, copy, visual style, spec prose — the build stops at the cheapest judgeable sample: one paragraph, one card, two sections. The human's word on that sample sets the bar before the full build spends anything.

Here's the kin split, stated: the mockup-first entry condition [INV-43] is the human's declared "show me first." This law is the agent's own discipline: build smallest first, even unasked, when taste rules the deliverable. [INV-62]

**A rejected artifact reopens its source.** When the human rejects an artifact, the fix starts at the artifact's source — the spec clause, the card, or the brief that produced it. The agent corrects the source first, then rebuilds the artifact from it. Patching the rejected output line-by-line against an unchanged source is the five-round trap by name, and it's banned. [INV-63]

**What already works is promised before the agent touches it.** When a feature-doored wish touches a surface that already lives, its spec-delta opens with **regression fences**, before the facet sweep authors anything new [T-13].

A fence is one sentence for a neighbouring promise that must stay true through the change — for example, "the catalog still opens on click" or "the player keeps playing across a view switch." Each fence cites the existing spec clause it guards.

A fence restates existing law and earns no new matrix row: the cited clause's own row already carries its never-side [INV-6], and the landing's full-suite run proves the fence held.

So "fixed one thing, quietly broke the neighbour" turns red before it ships. The delta thereby splits everything it touches in two: promises that stay are fenced, cited, untouched; behaviour being changed is never fenced — the agent re-authors it as new law through the normal walk.

A fence that finds no clause behind it has discovered an unwritten promise. That promise gets reconciled from the shipped truth like an adopted claim [A-3], written as its own spec fact with its own row, and surfaced, never silently assumed [INV-5].

Likewise, touching a neighbour whose claim is adoption-born and still unverified triggers that claim's reconciliation before it can be fenced.

The wish's queue row names its fences by the anchors they cite ("fences: …"), so "untouched and still true" becomes a greppable claim; the landing line stays its one-line self [T-7].

Fence-authoring belongs to the feature door. The bug and refactor doors inherit only the catching — their full-suite runs exercise every never-side — and a prototype fences nothing because it promises nothing [E-17]. [T-14, INV-19]

**A feature also says what it is not doing — and how we'd know it worked.** Every feature's spec-delta closes with two short sentences. Both are always written — like the facets, silence is not an option.

- **Non-goals:** what's deliberately left out ("version comparison, excluded this time"). "Nothing deliberately left out this time" is itself a valid sentence; only a missing sentence is a hole. A non-goal that narrows what the wish asked for is a scope decision, so it rides the same batched report as every taken default [INV-4, INV-18], never a silent narrowing [INV-5]. [INV-20]
- **A success measure:** how we'd notice the feature worked for its person, a number where one exists ("the producer opens the evidence panel at least once per session"), decided or `[default]`-tagged like any facet, the tag marking provenance only. No matrix row derives from a success measure. The machinery that reads them — KPI dashboards, A/B runs, segmentation — stays [target] under its own queue rows. Until then a measure is a written promise the human checks by eye, honestly labelled so. The quantification questions — is there an analytics tag? how will we measure? is an A/B worth it? — ride the facet sweep's batched report [T-13, INV-18]. [INV-21]

Both sentences bind forward from features specified after this rule lands. An adopted feature owes its pair at the first landing that touches it [A-3], never retroactively en masse. A prototype writes neither — it promises nothing [E-17].

#### Parallel lanes, one pen

While the session walks, four things hold:
- Intake is parallel, integration is serial — **one landing at a time, per repo, under one pen**.
  - The **pen** is the right to write the shared truth: the spec, the architecture doc, the matrix, the queue, the integration of a delta into the shared tree, the closing of a row. One lane holds it at a time.
  - Claiming a lane is an atomic committed act. The session commits the row→in-work flip first, then re-checks under the fence [INV-11] right before its first shared-truth write. If that re-check finds a foreign session's committed in-work row, the later claimant backs off and re-queues. "Later" is read by a total order, never by wall-clock: the claim whose commit is the ancestor in git history holds, and the descendant backs off; on a genuine concurrent claim with no ancestry between the two commits, the claim whose session identity [INV-117] sorts lower holds, and the other backs off. The row→in-work flip records the claiming session's identity, so a peer re-checking under the fence reads both identities and computes the same order from either side. Because every session carries an identity and identities are distinct and totally ordered, exactly one session backs off and mutual back-off cannot happen. [INV-11, INV-2, INV-117]
  - **Each session carries a stable identity, minted at its start.** Before its first act — before the inbox sweep [T-10] — a session mints one identity and records it in its session checkpoint under `.live-spec/`, unchanged for the session's life. Where the context carries a harness session id, that id is the identity, unique by construction; where it carries none, the identity is minted once from the session's start time joined with its worktree path and a nonce, carrying enough entropy to be unique — distinct worktrees already differ under [INV-105]. This identity is what the pen tie-break orders on, and it exists for every session, not only one that raced an inbox slug. The inbox source-mark's short session token is a projection of this same identity — its leading characters — so a filename never mints a second identity scheme. [INV-117]
  - Foreign hands never share a repo's pen, so across sessions the law stands as it always stood. Within one assigned session, up to three trains may roll under the parallel-lanes law (below) [T-18]. Every pen-stage still lands one at a time, and a landing commit carries exactly one row's delta [INV-39].
  - Bounded delegated execution (workers) overlaps as it always did — disjoint brief-named files or an isolated tree, the edit fence armed [INV-11, ACT-3]. A new wish waits its turn unless it is a bug preempting (next section). [INV-2]
- **A pending question for the human never stops the work** — the lane proceeds on the recommended option; the question stays open in the row, revisitable any time. [INV-4]
- **No silent micro-decisions** — every choice not in the human's wish gets either asked, or recorded in the spec and surfaced in the same report. The batched report carries this as its own postcondition: every taken default, trim, and deliberate narrowing of the walk appears in it. A decision absent from the report is silent by definition, whatever the spec recorded. Nothing decided-and-buried. [INV-5]
- **Every landing cites its wish row** — the commit message or journal entry names it, so "why does this exist" is always answerable. [INV-3]

**Trains may roll — one pen writes.** Parallelism was born below the lane: workers split disjoint files, and read-only analysis rode the background while another wish walked the pipeline. This law lifts that parallelism to feature level, where it is safe.

One assigned session may hold up to three build lanes in-work at once. The senior allows this only when the lanes are pairwise independent (no surface two of them touch, no spec section two of them must edit) and says so aloud. Opening every additional lane gets narrated, and all rolling trains appear on the departures board [INV-27].

What may overlap — everything that does not write the shared truth:
- a later train's code and tests, each written in its own isolated copy of the tree only (its delta reaches the shared tree through integration under the pen; the brief-named disjoint-file road [ACT-3] stays legal within one lane, whose workers land with that lane's own commit);
- read-only analysis and research;
- a prover run reading committed law.

What always takes the pen, one lane at a time:
- edits to every document both lanes share — the spec, the architecture doc, the matrix, the queue, the journal, and the resume file among them;
- the integration, which brings a lane's delta into the shared tree and runs its gate;
- the closing of a row.

So the document stages of two lanes never interleave mid-edit. Each lane's spec-delta is drafted and proven against the spec as committed law, never against another lane's half-written draft. The pen passes between trains while their long mechanical stages run.

At most three build lanes roll at once without asking [default]: the session does not stop at two, taking the independent work that exists.

Beyond three, a fourth lane opens only on the human's asked word. When more independent work waits workable, the session asks whether the human wants another train rolling, and never opens it silently. Read-only background analysis never counts against that cap.

The board shows every rolling train. Each in-flight row keeps its own station line [INV-27]. A lane waiting for the pen says so and names the row it waits behind ("at integration, waiting behind row N").

When several trains want the human's word, the questions ride one batched decision page, every card naming its lane's row [E-22, INV-4].

A bug still cuts the line [T-9]. It takes the pen, and the senior takes over, at the end of the current pen-stage. A pen-stage is never cut mid-edit. Rolling background briefs may finish, and no lane takes the pen back until the bug lands.

A milestone's whole-spec operations run with one train only. No new lane opens mid-gate, and a milestone opens only once a single train rolls: the other lanes either land first or enter a distinct **held-for-milestone** state — each quiesced at a clean checkpoint the way a park writes one, but named apart from bug-**parked** because nothing failed. The gate runs on the quiesced tree, and every held lane resumes in its landing order once the milestone lands [M-1]. [T-18]

A milestone gate is one indivisible pen-stage. A bug arriving mid-gate waits for the gate to finish rather than preempting a half-run audit — an audit stopped halfway leaves its verdict incoherent — and takes the pen the moment the milestone lands, ahead of the held lanes' resume. That is the one exception to "a bug cuts the line at the end of the current pen-stage" [T-9]: the milestone gate is the pen-stage, whole [T-18].

While several trains roll, the landing stays pure: **a landing commit carries exactly one row's delta**. Its gate — the full suite plus the guardrails — runs on a tree holding nothing of any other lane's unfinished work. So half of another train never rides a landing.

When a lane lands, the shared truth has moved. Every still-rolling lane's integration then re-checks under the fence [INV-11] and re-runs its gate against the tree as it now stands: landed-first wins, the later lanes re-verify, never the reverse. [INV-39]

Here are the parallel-lanes law's edges, stated once. It fires when another workable, independent wish waits while a rolling lane's long mechanical stage runs. The correction is idle waiting gone: a feature's code hours no longer block another feature's document hours.

It does not fire across sessions, nor on wishes that share a surface or a spec section — those still serialize as before. It also does not fire mid-milestone or while a bug holds the pen. Its only face is board and report lines, already governed by the line law; no other visible surface, so facets are N/A [INV-28].

Non-goals: this iteration adds
- no cross-session double-landing, since foreign sessions still back off;
- no automatic independence checker, because the senior judges independence and says so aloud;
- no fourth build lane unasked, since beyond three the human's word opens each next train;
- and no per-lane sub-board.

Success measure: the first real double-lane run lands both rows clean with the board readable throughout — the human can say at any moment where each train stands, checked by the human's own read of that run's reports [default]. [T-18]

**Lanes are picked by a graph, never by mood.** At queue-take the session reads the runnable head — the next few rows workable without the human — and builds the mini dependency graph. It draws an edge wherever two rows share a surface, a spec section, a skill file, or a doc region.

Lanes open on a pairwise-independent set, up to the cap [T-18]. Rows joined by an edge serialize inside one lane. Rows that collide only at their integration — one file, different concerns — may pre-roll their isolated build stages with the integration order declared at claim time: first-declared lands first, and the later re-fences on the new truth [INV-39].

The graph also knows when not to parallelize. Parallel pays only when build stages dominate the pen work, so tiny rows ride serial, and saying so aloud is part of the board. The chosen set and the order get narrated at opening [INV-27]. [INV-49]

**Deferred rows are revisited at every queue-take, not only at milestones.** A deferred row carries a revisit trigger [T-8], and a time-bound one — before the next release, when the campaign ships — can come true and then lapse in the gap between two milestone gates, so the milestone re-scan [M-1] reads the triggers too rarely to catch a window that opens and closes between gates. So the milestone gate is not the trigger's only reader: at every queue-take the session also re-scans each deferred row's revisit trigger against the current moment, and a fired trigger returns its row to the runnable head [INV-49] right then. The two cadences read the same triggers by the same rule — queue-take and milestone — so a deferred wish never waits on a trigger nobody reads [INV-1], whichever cadence comes first. The trigger vocabulary stays free-form, since a reader now runs at queue cadence rather than only at the milestone. [INV-129]

A wish can also end without landing, and its row stays in the table in one of three end-states:
- **declined** — the human said no;
- **deferred** — parked with a named revisit trigger;
- **superseded** — absorbed by another wish, so the row points to the absorbing one.

Declining preserves what the declined wish had absorbed. A wish that other rows were superseded into lists them at its decline.

Each listed row then either gets declined by name in the same breath, when the human's no covered it too, or returned to the queue as its own row again, when the human's no was about the absorber's shape and not the need. A superseded wish never dies by pointer [INV-1]. [T-8]

What the wishes grow is the **spec (PRODUCT_SPEC.md)** — the living statement of what the product is, one surface = one name, everywhere. [E-4]
### A prototype stays a sketch  [feature: F-prototype]

Exploring an idea before committing to it is allowed — a room is sometimes sketched before the house is built. A **prototype** is that sketch. It lives fenced off in its own clearly named home, such as a `prototype/` folder or branch. Fenced off means the code sits apart, and nothing in the product reaches into it.

Every artifact a prototype produces carries the PROTOTYPE label, in whatever form its kind can show:

- **A rendered page** — an on-screen banner.
- **An API or data payload** — a `_prototype: true` field or header.
- **A script or CLI** — a first-line PROTOTYPE banner.
- **A bare file** — the marker in its name or header line. [E-17]

**Is it a feature or just a sketch?** The boundary sits at the door step — the point where a request becomes a product feature.

- A wish to have something in the product is a feature. [INV-16]
- A request to merely see or try something, with no commitment, may live as a sketch inside the fence — no lane (no path through the build pipeline) and no spec.
- When which was meant is unclear, ask one plain question; do not guess.

Opening a prototype home is a repo write like any other:

- The write-ownership law governs it. [INV-10]
- The assigned senior makes that judgment call. [ACT-2]
- An outside session files an inbox wish instead — a worker never opens a prototype home on its own brief.

The fence runs one way: influence crosses out of the prototype, never in.

- Never wire a prototype into a prod surface.
- Never link to a prototype from a prod surface.
- Never style a prod surface to match a prototype.

A prod surface is any part of the shipped product a user meets. Show a prototype to the human only under its label — nothing reaches the human as the product unless its surface walked the full pipeline.

Promotion enters the sketch's earned feature at the spec step, without merging its code. When a sketch earns its place, its feature enters at the spec step like any wish. [T-12, INV-16] The prototype serves as evidence for that spec; its code holds no rights.

The machine enforces the fence with a guardrails check that has three legs:

- **Live today** (for the pack repo): a prod file that references anything inside a prototype home turns red. [E-6]
- **Still a target**: the surface registry's completeness scan. [E-10]
- **Still a target**: the behaviour-traces-to-spec check. [target, E-6]

When all three legs land, the header's honesty rule holds in both directions: the spec never claims what isn't built [S-0], and the build never contains what the spec does not name.

Today only the fence leg is enforced; the rest is promised, marked, and owned by its rows. [INV-17]

#### An approved look lives in its artifact

Prose alone cannot record how a design looks and feels. A rebuild made from prose alone, with no artifact to check against, can pass every test and still ship a look-alike instead of the approved look.

Once the human approves a sketch as the look, that prototype becomes the **norm** for look and feel. One law with four arms guards it:

1. **The clause cites its artifact.** A `norm: <path>` pointer sits at the clause's line end, beside its anchors. The prose carries the laws; the artifact keeps the look. spec-author owns the pointer's format.
2. **Approval freezes the artifact** into the project's records. A copy lands in `docs/norms/` with a dated provenance line — what it is, when it was approved, and which sketch it came from. The pointer cites this frozen copy. A norm pointer never reaches into a live prototype home, so the one-way fence stays absolute and the sketch stays free to die. [E-17, INV-17]
3. **The build reads the artifact.** When building a surface whose clauses carry a norm pointer, open the artifact before the code step. The landing report records a one-line plan-vs-prototype diff — a missing line is a defect, caught at build-pipeline's code step. The verify step's feel bar reads the same pointer. [INV-30]
4. **The prover reads visual clauses with the norm lens.** It flags a prototype-born clause with no pointer, or a clause contradicting its own artifact. Both belong to the "wordless door ≠ no question" class.

A story can declare that the human must see a mockup before the build starts — "show me first, then build." Write this in the wish's queue row at intake as "entry: mockup-first." Only the human cancels it, by naming it; a general "go build" moves priority but never cancels that condition, which the door step holds.

This rule looks forward only — add a clause's pointer at the first landing that touches it, never retroactively across the whole spec at once. A pointer names only a prototype the human approved as the look; an unapproved sketch stays plain evidence in its fence [E-17], and a text-born clause carries no pointer.

This landing shows no visible surface, so facets are N/A.

Non-goals for this landing: no mechanical pointer-grep guardrail (a candidate after real usage); the norm artifact's own format stays free.

Success measure: the next prototype-born surface lands with its pointer and its plan-vs-prototype diff line in the landing report, and the look-alike class does not recur. [default] [INV-43]
### From the spec to the tests: two layers that must not be skipped  [not a scenario]

**The test-author skill owns the test method; build-pipeline just calls it.** test-author runs the matrix derivation and the test writing (the pipeline's steps 5–6). It keeps the level ladder (string / DOM-text / browser-computed / pixel), real-artifact assertions, red-first proof, the pinned skip-set, and traceability as a standing test.

build-pipeline calls test-author the same way steps 1–2 call spec-author and product-prover: the method lives in the skill, the pipeline keeps order and gates [E-27].

**Tests clean up after themselves, and their files are born in a temp home.** Every test removes what it creates — temp files, fixtures on disk, spawned processes, mutated shared state — and a suite run leaves the machine as it found it; a leak is a defect of the test. The placement half: a test's files are born in the system temp home or the host's gitignored state dir and erased at the run's end; a user-visible folder — Downloads, Desktop, Documents — is never a test's workspace, and a headless browser's download directory is pointed at the temp home explicitly (the worked incident: 42 files in a Downloads folder before the human's eye caught it, both harnesses fixed the same hour, 2026-07-10). The pack's own suite holds the law mechanically: its temp artifacts carry the suite's own prefix, and a session-scoped before/after diff of the temp home fails the run on a surviving file. [INV-100]

**A test's expected value derives independently of the code under test.** A test compares the code's output against an expected value, and that expected value must come from a source other than the code under test. Never recompute the code's own formula and assert the result as the expected value. Such an assertion is a mirror that can never catch the formula being wrong, because the code is only ever asserted equal to itself. Three sources of an expected value are legal: a hand-computed constant, an independent derivation, or a recorded real output reviewed by a human. The ban has a boundary. A round-trip or property test over the outputs is legal, because it asserts an invariant rather than a recomputed value; the ban strikes only an assertion whose expected value is produced by the same formula the code runs. Born of row 220's audit: green suites missed real walk bugs because tests recomputed the code's own formula as the expected value (2026-07-10). [INV-102]

**The ladder tops out below the real device — the suite names that boundary honestly.** Touch physics, scroll snapping, and background throttling live past a desktop headless browser's reach (a momentum swipe on a real phone, a tab throttled in the background). A behaviour living there gets a **real-device walk row**: a matrix row the suite can never turn green, owed to the human's own hands before ship — kin of the feel gate [INV-30]. The suite says what it cannot see; a green run over such a fact claims nothing about it. [INV-77]

**A geometry fact is asserted relative, wide, and long.** A centering or positioning fact asserts relative geometry — |center(element) − center(viewport)| ≤ ε — at two or more viewport sizes, and after N consecutive steps of the interaction, so cumulative drift shows. An absolute-pixel assertion at one viewport after one step passes forever while each next step lands further off; the drift hides from it by construction. [INV-78]

**An engine extracted from an instance tests on its own generic fixtures.** When a generic engine is carved out of a working project, the donor's data keeps the donor's shape — and a suite running only on it proves the donor, never the engine. The engine's suite runs on engine-shaped fixtures (its own ids, its own content model); the donor's data may stay as an extra real-data suite, never as the only one. And every donor-specific constant the extraction finds — an id format, a hardcoded wordmark, a path — becomes a named entry in the engine's content contract, with a test that the engine works without it. [INV-79]

**The suite's own plumbing must not lie.** Three legs of one class — the harness lying about its own verdict. A skip path executes even when never taken: the skip helper imports at module load, so a skip that cannot run is red instead of a silent pass on the machine that needed it. An engine/instance shim owes a re-export completeness test — a missing re-export once kept a whole suite silently red. And a wrapper's exit code is never the verdict for a background or delegated run — the gate reads the suite log's own tail line (the pinned skip-set law's sibling; a foreground gate reading its own child's exit stays legal). [INV-80]

The spec says what the product is. Tests prove facts about the shipped artifact. Two documents sit between them, and if they stay implicit, they get skipped — a lost layer.

**ARCHITECTURE.md describes how the product is built.** It is a short list of named nodes: pipeline stages, modules, surface owners.

- Each node carries one responsibility and one name — the one-surface-one-name rule, applied to structure.
- Every spec fact belongs to exactly one node.
- In a live codebase, every node pins to its owning place. The named thing is the pin: a function, a marker comment, a selector, a heading. The `:line` beside it is a convenience cache and can lag, so the name is resolved and a drift check re-greps it. Skip that and pins rot silently — a wrong-with-confidence pin is worse than none.

Drafting the architecture is where spec claims are reconciled against shipped reality. Every pin comes from a command that was run, never from the doc's own prose.

It is written from the proven spec (template: `ARCHITECTURE.template.md`), and, like the spec, proved before anything derives from it — a product-prover pass with the architecture lens. That lens checks six things, each judged at the project's kind scale:

- every spec fact has an owning node;
- no node stands without spec backing;
- every seam between nodes is named;
- the quality budgets are stated with their instrumentation homes [INV-41];
- the runtime view walks every promised flow [INV-74];
- the placement view says where every node runs [INV-75].

The lens grew from three items to six on observed evidence: a real derivation passed the three-item lens and shipped with no budgets and no views — a mandate with no checking seam gets skipped (tlvphoto validation, 2026-07-09).

Keeping the doc up to date:

- A large or surface-class wish updates the doc before the matrix is touched. A bug or small wish just cites the node it lands in.
- A fact with no owner yet gets assigned to the nearest fitting node, recorded in the doc. Assignment alone triggers no re-prove, so the fix still lands.
- Re-prove exactly when the structure changes.
- The doc stays iterative: it maps the product as it stands, plus the landing in flight. A node exists for what ships today, or for what the spec already promises under an owned row (marked [target], pin empty). Never design it milestones ahead — a speculative node is unbacked structure. Re-carving the whole map is legal: it arrives as its own row under a restructure placement [INV-37], walks this step, and gets re-proven [E-14].

**Every new or carved node passes a three-question fitness test at its birth.** Before an extraction or a new node stands, it answers three questions: can it be tested alone, does a real second place need it, and can it and its neighbour be worked in parallel without queuing on shared files. Three yes answers make the node right. A single no is a flag to answer before the carve stands — name the plan that turns it to a yes (a promised second caller, a real testability gain) or fold the carve back into its caller — and two or more no make it premature outright. The product-prover speculative-node flag is exactly this flag raised on the second question: a node with one caller and no promised second is flagged for that answer, never auto-rejected, so the birth gate and the prover agree on the one-no case. The test's first home is the architecture step, where new abstractions are born; its second home is product-prover, extending the speculative-node flag — a node with one caller and no promised second is flagged. This is the structural face of the reusability-and-parallelism principle: the right abstractions are the ones that make the work more testable, more reusable, and workable in parallel. (Born of the six-principle design wish, principle 7; his 2026-07-12 word.) [INV-122]

**A deliberate redesign re-shapes the document, not only its pins.** When structure is deliberately redesigned — layers restacked, a surface's ownership moved, nodes merged or split — the architecture document is re-shaped to the new form and re-proven with the architecture lens in the same movement. Updating the pins alone is scoped to a boundary shift that leaves the document's shape standing; after a real redesign the old shape itself lies, so fresh pins on a stale shape are a defect. The re-carve routing [INV-37] carries such a redesign as its own row [E-14]; this states what that row owes the document. (Born of the tlvphotos second-finger redesign, 2026-07-11: a UI-layer rethink was ordered and the pack forced only a pins update, not a re-shaping.) [INV-113]

**The architecture owes numbers, not just names.** The doc states measurable quality budgets for what it builds, plus each budget's instrumentation home — where the numbers get measured and where a human reads them (an export, a debug view, a report).

What is measurable depends on the project's kind [INV-36], so ask "what does quality mean here, in numbers?" before writing any:

- a user-facing product — paint and interaction times ("first image within 2 s on a cold visit");
- a backend service — latency, throughput, error rate;
- a CLI or pipeline — run time on a typical input, and per-unit cost;
- a skill pack — its evals' pass rate and suite wall-time;
- prose — whatever honestly has a number (a reader reaches X within one scroll).

Where a quality has no honest number, say so by name instead of inventing a vanity metric. A budget counts only once a matrix row at the right level can see it — a hope in prose does not. A surface with no budget and no instrumentation home is a derivation defect, flagged like an unowned fact.

The numbers are the host's taste: the architecture proposes them with a recommendation, and the human's word sets them at the surface's first budget landing. Like the two layers themselves [INV-15], this duty binds from the first landing that touches the surface after the clause exists, never retroactively [INV-41].

**The architecture traces each flow at runtime.** The spec's person-facing scenarios are flows — a visitor opens the door, walks the gallery, answers the quiz. The feature coverage table names which nodes implement a feature [E-29]; the runtime view shows how. For every flow the spec promises, the doc walks the running product: which node serves each step, what data crosses at each hop, where the flow can fail — and what happens then: every named failure point carries its fallback (a degrade, a retry, a guard), so "if X fails, Y happens" is readable per flow; a failure point with no fallback sentence is an unfinished walk. One short walk per flow is enough — a numbered line or a table row per hop. A flow the doc cannot walk end to end is a finding: a node is missing or a seam is unnamed [INV-74].

**The architecture says where everything runs.** Every node states its place: build-time on the author's machine · static file on a CDN · client browser · edge worker · external service. Where a load-bearing technology choice exists (the embedding model, the render harness, the store), the place names it too — and the same table says where secrets live and which tier holds each verdict that must not be decided on the client; a secret's place is architecture, never an implementation footnote. The placement is first-class — a column in the node table or its own small table — so a reader answers "where does this run" for any node at a glance [INV-75].

Both views scale by the project's kind [INV-36]. A book runs in one place and its flows cross no machines: one sentence per view says so and satisfies the duty. A fullstack or data project owes both views in full. The duty binds from the first landing that touches the architecture after the clause exists, never retroactively [INV-15].

**The doc reads tiers-first.** It opens with the shape at a glance — the tiers named in a few lines — then the nodes, then the flows walking those tiers, then budgets; an LLD reader lands oriented before any table detail (the reading order Kiro's design doc and BMAD's architecture template follow; his word, 2026-07-09). The placement table IS the tiers-and-technology table.

**The matrix is derived, never just filled in.** The matrix [E-5] organizes rows by **architecture node × spec fact** — a structured grid: every fact gets at least one row, and every row pins a test level.

Derivation closes with the **coverage validation** — a checklist that lives in the matrix template, and it is walked:

- every spec anchor appears in ≥ 1 row;
- every artifact-inventory entry owns ≥ 1 rendered-level row;
- every visibility / layout / colour / interaction fact sits at level ≥ browser-computed;
- every node carries its negative-side rows [INV-6];
- no row cites an anchor or node that no longer exists (stale rows retire, they never vanish).

A fact with no row, or a row at too weak a level, is a derivation defect. The prover catches it at derivation time, before any user hits it [E-15].

While both layers live, one rule holds: **no wish lands whose facts lack an owning architecture node and a matrix row at the right level.** The bridge from spec to tests is walked layer by layer, never jumped.

A project that predates these layers brings them up as an owned landing, and the invariant binds from the landing that creates its ARCHITECTURE.md and matrix, never retroactively [INV-15].
### The rhythm: breakpoints, milestones, pushes  [not a scenario]

#### Breakpoints, resume, and milestones

- **Safe breakpoint (end of every movement):** every movement ends the same way — replace the NEXT_STEPS live state (never stack it), add a dated journal entry, and commit. Session memory can then be wiped with zero loss. NEXT_STEPS may be gitignored, so the journal entry is the durable net. A long session should take this offer. At a breakpoint the agent compacts its own context and says so, never silently. A full wipe or clear is the human's move. On the way back, re-check skill freshness [A-7]. [M-2]

- **A landing closes the checkpoints it shipped.** A landing that ships a checkpoint's items flips that checkpoint to its closed state in the same landing. The movement that writes the work into git history also marks the checkpoint done, so a returning session never reopens finished work. A checkpoint whose items all live in git history is stale by definition and reads as a resume defect. The closing sweep rides beside the NEXT_STEPS replacement, so a checkpoint left reading "not started" after its items shipped fails the landing. (Born of the audit: two engine checkpoints still read "not started" after everything in them shipped, so a resuming session would have redone done work, 2026-07-10.) [INV-107]

- **The resume file is a digest with a hard cap:** the agent reads NEXT_STEPS in one minute at a cold start — growth is a design failure. The whole file holds at most 100 lines [default], and a suite check owns the number. It goes red on a bloated file — proven with a synthetic one. The cap and the restate-every-open-leg law [INV-26] are reconciled by form, never by dropping content: the agent restates an open leg as one terse line —
  - its name,
  - what stays open,
  - where the detail lives.

  The detail itself flows to the journal, the queue row, or the record the line points at. Compaction moves prose to its home; it never silently drops an open leg. [INV-48]

- **A background worker outlives a memory wipe — the resume protocol proves it dead or alive.** A worker spawned in a session keeps running and keeps writing the shared tree after the chat's memory is cleared or handed off. The OS process list and the harness task list show nothing for it, so neither is proof of death; liveness is proven by deed. The handoff note that records a worker states three things: the worker's recorded id (pointing at the worker's own checkpoint file), the exact files its brief lets it write [ACT-3], and the three checks a resuming session runs before touching those files — watch the write-set's file times over a short window (~30 s [default]; anything changing means a live writer), read the worker's heartbeat on its checkpoint file (a worker touches that file on a fixed interval whatever its work writes [ACT-3], so a heartbeat moved within the last ~2 min [default] means a live writer even when no product file has, the case of a compute-bound run mid-computation), and send one message to the recorded id (a live worker answers; allow ~2 min [default]). Life on any one check ⇒ reconnect and treat its files as claimed; a dead verdict requires all three quiet together — a still write-set, a stale heartbeat, and an unanswered probe — declared in one written line, then proceed. Until that verdict, the worker's output is never framed as finished. A worker from a PRIOR context is a foreign writer until verified — the same-session fence-benign courtesy [ACT-3] never crosses a wipe. The fence extends the same way: no second worker onto a shared tree until the first has confirmed halted by its own reply or been declared dead by all three checks [INV-11]. Before a wipe, prefer halting the workers or letting them finish, so the next session starts single-writer — and a handoff says plainly when a worker dies with a closed window or a sleeping machine, so no one is told the worker will simply be recognized. A dead verdict only frees the files the worker owned. Whether the work is done is a separate question, read from the worker's checkpoint carrying its own finished marker, or from the independent verification walk; a dead worker's partial output is integrated only after that check. (Born of a real two-writer race, 2026-07-09, and of the prover finding that a compute-bound worker, writing no file for minutes and slow to service the probe, read dead on both original checks though it was live, 2026-07-12.) [INV-76]

- **Human-facing prose is drafted by a clean writer.** Any text a human will read is drafted by a fresh writer session that does not have the package rules loaded. This covers documentation pages, product-spec prose, reports, decision pages, product copy, and the package's own rule texts while they are being edited. The rules-loaded session writes a plain brief for the writer, and that brief carries the facts, the intended reader, and the register laws. The writer session returns the draft, and the rules-loaded session reviews it and lands it. The rule binds new text and any text that is currently being edited; the unit is the section the edit touches, and a whole page is redrafted only on the human's word. A report typed live in chat stays the session's own words under the register laws; the clean road binds the durable prose a human returns to — pages, documents, product copy, rendered report artifacts. Settled text stays as it is until a human rejects a specific page or an edit opens one of its sections anyway; a mechanical correction — a typo, a broken link, a version number — is no drafting and rides the ordinary hand. The package refuses a blanket rewrite of settled text, because meaning can shift during bulk restructures. (Born in the field: nine clean-drafted reader docs passed the owner's bar the first time, while a marinated session's onboarding text bounced three times the same night, 2026-07-10.) [INV-84]

- **Milestone (minor gate):** a milestone runs the full gate:
  - full spec re-prove, and a full architecture re-prove beside it: the prover reads ARCHITECTURE.md the way it reads the spec, so the component contracts, the owning-node edges, and the cross-section composition between components meet the same structured review; the architecture pass records in docs/prover/ beside the spec's [INV-116];
  - matrix audit: re-walk the coverage validation [E-15] against the current spec and architecture;
  - surface-composition check;
  - re-run skill evals [E-19];
  - walk the pack's skills through skill-creator, the skill-making skill. It checks format, frontmatter, and the description-triggering lens — the craft of the skill file. Our evals already test behaviour; this checks the craft. Fold or reject each finding, with a written reason, in a dated record.
    - A newly joining skill walks this at birth, before it ever reaches the gate.
  - doc compaction: audit every living document — spec, matrix, queue, skills, ledger [E-24], and the test suite — for redundant information, and compact it. Compact means there is no redundant information: a fact lives once, in one home, with a pointer from everywhere else that needs it. A pass removes only the redundancy — the same fact stated again at full length in a second home, history that belongs in the journal, a table row that only restates its own prose — and keeps everything whose removal would change the meaning or a reader's understanding. What reads as a redundant second statement can be a fact's only home: the Formal-index rows read verbatim by the traceability suite are the worked proof, since an ad-hoc flatten of them reddened the suite (2026-07-12), kin to one invariant carried across three laws [INV-39]. So compaction is per-item judgment, and a pass that removes substance accounts for each removal [INV-109]. Restructure a document only when a faster reading shape is needed, and only through the content-preserving layout vehicle with its multiset proof [INV-111]. Delete a duplicate or superseded test only when the matrix audit shows its rows still covered by a live test. Nothing grows unboundedly, and queue compaction archives closed rows, never deletes [INV-1]. [INV-115]
  - **Compaction is a scheduled station for code as well as docs.** The doc-compaction pass above is one half; the station widens to CODE — duplicate logic merges, dead weight leaves with its listing [INV-109], and a ripened abstraction is extracted only through the three-question fitness gate [INV-122], never a speculative carve. Two triggers fire it: this milestone gate, and — apart from the milestone — the second occurrence of the same problem, base rule 19's moment, which opens the duplication's OWN compaction row that moment (the owner base rule 19 demands) rather than waiting for the next gate; that row then lands through the ordinary pipeline, one row's delta per commit [INV-39], so a known duplication never blocks the lane it was found in [INV-56]. Each pass locks its reached level — a new test or lint where the level is newly reached, otherwise the existing suite that already holds it green — so a compaction never silently regresses (the convergence law, rows 216-218 [INV-98]). [INV-123]
  - re-list every open human gate and every unharvested inbox/ file, one line each;
  - re-scan every deferred queue row's revisit trigger; a fired trigger returns the row to the runnable queue, so a deferred wish never waits on a trigger nobody reads [INV-1];
  - re-check the formal index against the prose — it's a derived map, never a second truth;
  - re-pin the derived docs' headers to the spec version, then prove them;
  - **the thin loader stays thin** [E-16]: re-read the personal layer's global instruction file line by line. Every line must pass one test — must this hold before any pack file loads? The audit report states the line count. A rule that survives there without passing the test migrates to its real home (profile or pack); it never lingers. [M-1]

#### Versioning

- **Documents are versioned** like code. The queue and this spec carry dated versions, so a reader can always tell which roadmap version a decision was made under. [M-3]

- **Versions have named homes.** The package uses a `VERSION` file at the repo root. Each skill carries a version line in its SKILL.md frontmatter under `metadata:`, where the skill-format validator reads it. A host records its installed set in `.live-spec/` at attach and on every update. The freshness check [A-7] compares version against version, exact strings rather than bare file times — its "old → new" journal note is now writable. [M-7]

#### Time discipline

- **Time is read off the clock, never invented.** Every date a session writes — a file name, a journal or queue stamp, a ledger occurrence — comes from the machine's clock at write time. In doubt, git is the arbiter. The rule takes four forms:
  - **File and journal dates (mechanical, pre-push):** no repo file name, journal entry heading, or ledger date may sit later than the current clock. A future-dated stamp turns the suite red as a real defect. Prose that quotes a past incident's wrong date stays legal.
  - **Same-day times (mechanical, at commit):** the check reddens any added line that pairs today's date with a clock time later than the commit moment. "Pairs" means the adjacent stamp shape (`date [~]time`), so a line that legally quotes another moment's time beside today's date stays green. The commit clock is the reference, so the check can't race. The known cost is deliberate: a future plan is spelled out without writing it as a date-time stamp.
  - **Chat timestamps (law only, no mechanical fence):** a human-facing timestamp — the [HH:MM] a reply leads with, or any moment spoken to the human — is read off the clock at write time, never continued or extrapolated from an earlier stamp. This law lives in the communicator skill, where the human-facing exchange shapes live. Quoting a past moment's recorded time stays legal here too.
  - **The mechanical hand for chat:** a harness hook on the working machine — `scripts/clock-hook.sh`, wired as a prompt hook in the host's settings — injects the wall clock into every prompt's context, so every lead stamp is read off the machine's clock. Where the hook isn't installed, the law above stands alone.

  [INV-24]

#### Push and CI gates

- **CI mirror.** The guardrails' native home is the local pre-push hook. A host may also mirror the same checks in its CI, such as Jenkins or GitHub Actions, as a second net. There is one source of truth: CI runs the same scripts and never redefines them. The second net runs the full set — the reach map [INV-45] is a local latency optimization, never a CI shortcut. The pack repo's own workflow (`.github/workflows/gates.yml`) is the worked example; host guidance lives in the guardrails README (ROADMAP row 14). [M-5]

- **Accepted work reaches the project's remote.** Where the host has a remote — GitHub, GitLab, whatever the human names — work that is same or better and has passed every gate the diff reaches is PUSHED, by rule, never parked locally waiting for perfect. The remote is discovered from the tree first: the agent never asks what `git remote -v` already answers. Only a host with NO remote gets one question, contextually, at the first push moment: create one (and where), or stay local — a named choice recorded in the host profile. The rule runs inside the human's standing push grant [INV-70, INV-9]: on a host whose remote exists but whose profile records no such grant, accepted work stays local, and the first push moment asks one contextual question — push on the agent's certification from here on, or hold each push for the human's word — recorded in the host profile like the remote choice itself. A host that just created its remote meets the grant question at that same first push moment: one question per gap, and the two questions never collapse into one. And while another session is known live in the repo, the by-rule push stands down: push coordination returns to the human [INV-11], and the accepted work waits local until the repo is single-session again. And every push to a remote re-walks the README against the pushed truth: the shopfront law [INV-44] at every-push cadence for remoted hosts — the README stays crisp and current, a stale claim is fixed before the push. A milestone gate the human named in person (a version bump "on his word") still waits for that word; the law moves routine accepted work, never his named gates. [INV-82]

- **The push walk reads the remote gate's verdict.** A push does not end at the push. Where the host mirrors its checks in a remote gate [M-5], the push step reads the remote gate's own verdict (the CI run the push triggered), read with one `gh run` in a matter of minutes, no human wait. A red verdict is the pushing session's own immediate bug: it preempts by the bug lane [INV-2], the fix lands the same session and is re-pushed before anything else, and the human never learns of the red from his mailbox. He hears the outcome from the session's report with the fix already done. Where the remote gate is slow, the session watches it to the verdict, a background watch riding the detached-work visibility cadence [INV-35]. Never a push left standing on an unread verdict, never a red run the human meets first in a GitHub email. (Born of the owner's word, 2026-07-10 ~11:00: why does a GitHub email tell him a deploy failed that the session should have caught and fixed itself.) [INV-106]

- **Push gate for live-spec itself.** This repo is public and the method's own flagship, so every push is preceded, in the same session, by two steps:
  1. the concurrent-edit fence [INV-11];
  2. a fresh re-check — a product-prover pass over PRODUCT_SPEC.md and ARCHITECTURE.md as they stand, its record landing in docs/prover/ before the push; the architecture carries the spec's freshness rule, so a change to either document owes a fresh record and a record predating the last ARCHITECTURE.md change is as stale as one predating the last spec change [INV-116].

  One carve-out, scoped by the diff: a push whose diff is exactly one new file under inbox/ — the remote deposit's shape [INV-112] — changes no spec-backed content, so it owes the fence and no re-check record; a diff carrying anything more rides the full gate.

  The record name is `YYYY-MM-DD[-suffix].md`, and the suffix is mandatory when the date's file already exists. Must-fix findings are folded before pushing. Folds produced by the gate's own pass do not re-trigger the gate; they ship with the same record. The rest become queue rows. No re-check record for the pushed state means the push should not have happened. The record enumerates the folds applied from its own pass. A fold stays local to the sections its finding named; a fold reaching wider re-triggers the gate. [M-6]

#### Scaling process to the delta

- **Process bookkeeping scales to the delta — the record's reach map.** A tiny row pays the same fixed bookkeeping as a whole surface: its own claim commit, its own full-page re-check record, its own journal chapter, and a resume rewrite. That runs roughly forty percent of its wall time, and none of it is the safety net. The principle: an iteration should run long only when the work needs it — where it doesn't, find what can be cut without sacrificing quality.

  So the reach idea [INV-45] applies to process too. The re-check before a push keeps its rigor always — previous records checked, the delta walked, a verdict — but scales its form:
  - a small delta (skill, prose, or infra kind, with no new surface and no structure change) ships a short-form record of three lines: previous records clean; the delta in one line; the verdict;
  - a surface-sized or structural delta keeps the full walk.

  Claims batch per declared lane, one commit. The journal chapter and the resume rewrite come once per landing batch, never per tiny row. The irreducible core stays fixed regardless of scale: the law's own text written well, the red-first test, the delta's cross-link prove, and the gates. That is quality itself, never scaled. [INV-61]
### Publishing — the deposit owes what its kind owes  [feature: F-publish]

Sooner or later a piece of work leaves the machine: a repo goes public, a skill enters a plugin directory, a release is cut, rendered cards go to a **design project**.

**A publish owes the reader what the artifact's kind owes.** This work-kind axis is already used at wish intake; here it applies again at the door of publishing [T-16].

#### What each kind owes

Each kind owes its reader a different minimum:

- a **skill** shows how to install it, the commands to run, and when to use it and when not;
- a **tool** shows real runs with real output;
- a visual **product** shows fresh screenshots — a stale screenshot is a false claim in picture form;
- **prose** shows its reading path.

A comparison or a diagram joins only when it carries the argument; it never rides along as decoration.

#### The checklist

The publish skill owns the per-kind checklist [E-12]. This spec sets the contract the checklist follows. Nothing gets deposited outward without passing the checklist first, and the walk's result rides the landing report like any other step [INV-22].

#### Targets add steps, never remove the minimum

**Each publish target is a plugin that embeds its own steps into the walk.** For example:

- GitHub brings a README-at-the-door plus release notes;
- a plugin directory brings its manifest and forms;
- the design project brings its cards [E-18].

The target adds steps. It never removes the kind's owed minimum.

#### Gates already standing

The checklist never bypasses the gates already standing. The human's publish gate guards anything irreversible or outward (base rule 17 [ACT-1]), and the host's own push gates guard the push [M-6]. The checklist runs before the gate, so by the time the human approves, it is already worth approving [E-20].

#### A version push re-opens the shopfront

**A version push re-opens the shopfront.** Every push that ships a new version changes the truth a public reader will read tomorrow — even when the diff never touched a doc — so the shopfront rides every push. The README's claims (behaviour, counts, commands, version homes) still have to match the truth just pushed. The kind-owed visuals ride along too:

- a skill pack re-checks its diagrams and flow pictures;
- a visual product re-shoots what changed on screen;
- a tool re-runs its example.

A stale shopfront is a false claim, exactly like a stale screenshot [E-20].

This shopfront check is the publish skill's checklist, read at push scale — same one home, no second checklist. The pipeline's commit-and-show step points at it, and the walk's outcome rides the landing report [INV-22].

When a push's changes touch none of the shopfront's claims, say so in one line: "shopfront checked — current." Find a stale claim and fix it before the push. Freshness is about the claims the README makes; styling is a separate concern.

**Everything built with the method says so.** Every publication of an artifact built with the pack — a skill, a tool, a site, a repo going public — carries one attribution line, "made with live-spec" linking to the pack repo (github.com/happysasha18/live-spec), on the publication's landing surface: the README's footer, and for a skill also its SKILL.md. The line names the pack version the project runs — read from the host's attach record at write time, refreshed at catch-ups, never a number invented — so the line doubles as the adoption tracker: who runs what is readable from the shopfronts themselves (his 2026-07-10 word). The exact wording lives once, in the publish skill's shared floor; this clause states only the duty. The line is an OFFER, never a gate — the owner's taste rules his own shopfront: the publish walk checks for the line and, when absent, says so once and proposes it; the owner's word decides, and a declined offer is closed, never re-asked [INV-16]. Each built-with project applies the line through its own queue, the pack never writing foreign trees. The pack's own standalone mirror repos are the one mechanical case: the offer stands accepted once, at pack level, for the owner's own repos, and the sync script stamps the line onto each mirror's README.md and SKILL.md from the live VERSION file at every sync — a mirror is rebuilt from the pack folder, so a hand-written footer there would carry an invented number and be wiped by the next sync. (Set on the owner's word, 2026-07-10; softened the same day by his own correction — a wish, never an obligation; the mirror case recorded 2026-07-11, row 246.) [INV-96]

**Shipped product docs state each requirement impersonally.** A product's shipped docs — the spec, the test matrix, the README, a skill card — reach everyone the project touches: a contributor, an auditor, a future user, the author in three months. Each requirement reads as three plain parts: the rule, the actor as a role (the user, the producer, the target user), and the reason it holds. The reason is load-bearing and stays — a reader has to know why the rule stands — while the personal attribution drops. A dated decision keeps the date as a plain anchor and drops the name, so the provenance a reader can act on survives even as the person's name comes off. Personal attribution and candid process voice have one home: the local-only diaries, the JOURNAL and NEXT_STEPS, which no publish ships. spec-author writes each shipped clause this way from the first draft, and the publish floor reads the shipped docs for a stray personal name before the deposit leaves. This pack's own spec, matrix, and roadmap keep a deliberate owner-attribution provenance for now — a dated exemption pending the owner's decision on whether the pack's own docs adopt the impersonal voice or keep attribution as their provenance record (row 279's staged decision; dated 2026-07-12). (Born of track-coach's 2026-07-12 shipped-artifact audit, which found a shipped spec carrying many owner attributions accumulated over months.) [INV-118]

**A machine holds the shipped tree's language line.** A shipped artifact carries no Cyrillic outside a user-language string the program deliberately emits, and no owner or personal name in a requirement's statement; the publish gate holds this with a machine (`guardrails/check-shipped-language.sh`) that reports each offence as file:line, so the fix is mechanical, while candid process-notes and attribution live only in the local-only diaries. The machine covers the two mechanical offences; a coined non-English metaphor is left to the register lint and the human. A generalized package spares its deliberate program data and its authorship bylines through a dated allowlist, the same equivalence-gate discipline the pack uses elsewhere — a new offence reds, a listed one is counted debt. [INV-120]

#### Non-goals

Non-goals this landing: no mechanical README-vs-diff checker, since the reach map (row 147) is the candidate owner; and no auto-regenerated images. Success measure: no push lands whose README claims an older behaviour or count, checked at milestone audits [default] [INV-44].
## What the human sends back

The two ways the human speaks back to the workshop: a piece of feedback, or a question about what the product does.

### Sending feedback in  [feature: F-feedback]

A person looks at what shipped and something occurs to them. It might be a reaction, an answer, a screenshot with a red circle, or a log file.

**Feedback** is anything a person hands back to the project, at any size, any moment, through any channel. The person is usually the host's human. When the host's product has users of its own, their reports travel the same road once a session receives them. [E-28]

The promise is simple: nothing handed in is ever lost, and everything handed in is answered by a route. Every received item lands in the same session, in the home its route owns:

- a wish lands in its queue row;
- an answer lands in its decision archive and harvested row;
- a fix lands in its commit and journal line;
- workshop noise lands in the problem ledger.

Some routes had no home before this section. They get one now: the **feedback ledger (FEEDBACK.md)**, an append-only file beside the queue at the host root [default]. It owns field evidence, plain reactions, and wordless drops that still await their question.

Each item is one dated line. The line records
- when it arrived,
- who handed it in and through which channel,
- what it concerns on the feature map,
- the item in plain words,
- and where it went.

The session echoes every arrival back in one sentence, one echo per item. A wish-shaped item's echo is the wish echo [INV-27]. Anything else gets a note back saying what was heard and where it went.

If someone mentions an already-recorded item again, the session appends its date to the existing line and changes nothing else. That's the problem ledger's own discipline, applied here. [INV-68]

#### Three channels, one contract [T-20]

- **Spoken or typed** — a remark in the conversation, or a note in a file the human points at.
- **A comment on something shown** — decision pages and review pages capture answers as saved JSON [INV-4, INV-64]. Each saved answer is a feedback item; the capture law already names its home, the archive and its harvested row.
- **A dropped file** — a screenshot, a log, or a document. It comes straight from the human in the conversation, or from any outside session through the host's inbox door. Each one arrives as one new file, under the same naming and collision law that wishes use [E-11], and the host's own sessions sweep it in [T-10]. If a file arrives with no words, the session asks one plain question about what it means; the ledger never records a guess.

#### The five routes

Every item takes exactly one route, and each route already has its law and its home.

- **Wish** — Ask for new behaviour, and it's a wish. It walks wish intake with its own echo, door, and row; that row is its home [T-12, INV-27].
- **Fix-sized comment** — A fix-sized comment on shown work gets fixed the same session; the commit and its journal line are its home. A story-sized comment queues as a wish instead.
- **Answered question** — Answer an open question, and it closes forever. The session harvests it right then, into the decision archive and the harvested row [INV-59].
- **Field evidence** — React to a shipped feature, and that's field evidence. It lands in the ledger, and the line cites the feature's scenario. The feature's success-measure sentence [INV-21] finally gets a place where real signals pile up — the ledger is the first honest slice of the reading machinery. That machinery itself (measurement plugins, aggregation) stays [target], under its own long-lived row (row 48). Evidence only grows into a wish when the human says so, or a tripwire fires a verdict.
- **Workshop noise** — A flaky tool or a missing dependency is workshop noise; it belongs to the problem ledger [INV-23]. The seam decides it: the product's behaviour goes to FEEDBACK.md, the workshop's behaviour goes to PROBLEMS.md — one home each. A standing behavioural rule breaking mid-turn belongs there too: its break is one ledger entry in PROBLEMS.md — the single home the once-read-rules sweep [INV-108] reads — and the rule's live-channel landing (a hook line, a suite-red check, its ROADMAP row) points back to that entry as the break-record rather than doubling as a second one. The routing/delegation rule's mid-turn breaks are logged this way, joining the workshop conventions already in the ledger, so the sweep reads one source (the one-home principle, base rule 4).

The skill that owns this behaviour is **feedback-intake**, the pack's intake half of the exchange. The pack splits the exchange: communicator carries work out to the human, and feedback-intake carries what comes back.

It fires the moment any session receives a handed-in item. It also fires at every inbox sweep, for files that carry feedback rather than a wish.

feedback-intake stays quiet in three cases:

- the agent's own output;
- a question the agent asked;
- something the human merely mentions without handing it in.

When unsure whether a remark was handed in, ask one plain question. feedback-intake never opens a queue row on its own judgment; the wish door owns that verdict. [T-20]

The section's edges, stated once.

#### Fences its birth must hold

- The inbox stays one new committed file per outside item [E-11], swept first [T-10].
- The wish echo and intake path don't change [INV-27, T-12].
- Answered questions still close and get harvested by the convergence law [INV-59].
- The problem ledger still holds workshop noise alone [INV-23].
- This section extends the queue's no-wish-ever-lost law, never amends it [INV-1].

#### Composition

- Outside sessions never edit the ledger. They use the inbox door, and only the assigned session appends FEEDBACK.md. The write-ownership and fence laws carry this [INV-10, INV-11].
- The ledger is append-only and archives like the queue, never trimmed [INV-1].

#### Facets and skill kind

- The feature's surfaces are the ledger file and the chat echo, prose read in place.
- Layout, touch, accessibility, and performance belong to the media that carry them.
- The empty state is a ledger holding only its header, which is healthy.
- Facets otherwise N/A [default].

#### Non-goals

- No end-user feedback widget on a host's own product. A site's visitors writing in ride the measurement family (row 48) or their own wish.
- No automatic reading, scoring, or aggregation of the ledger; the reading machinery stays [target].
- No new door mechanics; the inbox is reused as it stands.

**Success measure.** The same item never has to be handed in twice. Every received item is findable in the ledger, with its route, in the same session [default].
### Asking what the product does (the feature map on demand)  [feature: F-feature-map]

Three standing questions describe the product. The departures board reports in-flight work status at every report [INV-27]. Intake places each arriving wish on the map [INV-37]. Those two questions are answered on their own surfaces.

This ask answers the third — what the product does today — with one answer containing the whole product map, current as of the request, on demand.

The ask reads its answer live from the living documents:

- the spec's scenario sections name the features;
- the header's current-vs-target paragraph separates shipped features from promised features, at the granularity the [target] tag binds to. A scenario containing both shipped law and named promised parts is marked "shipped, with promised parts (named)," each status stated at that same granularity [S-0];
- the queue's open rows supply the remainder: each in-flight feature's station, and each wish whose `map:` verdict is new while its scenario is still unwritten. The queue shows a feature on the map before the spec documents it [INV-27, INV-37].

The spec's scenarios and the architecture's nodes constitute the map. No third document exists to maintain or drift out of date — no feature-list file, no cached copy [E-14]. The ask reads the living documents directly.

Each line follows the line law [INV-28]:

- a short descriptive name, in the product's own words;
- what the feature gives its person;
- the feature's status — shipped, target, or in-flight — followed by its station.

The ask delivers the map in chat by default. The ask delivers a rendered page instead on request, per the show rule [default]. Routine reports retain the departures board's in-flight scope. The ask returns the whole map only on request.

If a host has no spec and no scenario sections, the ask states that condition. The ask directs the requester to bootstrap or adoption when that condition holds. The ask reports only what currently exists [INV-38].

The section's edges are stated once.

- **Fences** the birth of this section holds: the departures board keeps its report scope [INV-27], intake keeps its placement rule [INV-37], and the no-third-document law stands, reaffirmed [E-14].
- **Facets** (skill kind): the feature's only surface is the answer itself, in chat or a rendered page on request. Layout, touch, accessibility, and performance belong to the medium that carries the answer. The empty state is the nothing-to-read answer stated above. Facets are otherwise N/A [default].
- **Non-goals**: the section adds no standing feature document, no auto-refreshing dashboard, and no per-feature history timeline for this iteration.
- **Success measure**: an ask yields a map whose feature set covers the spec's scenario sections one-to-one, plus every open new-verdict queue row. Its shipped-versus-promised marks agree with the header and the [target] tags, at their own granularity. Verification proceeds by diffing the lists [default].
## When something breaks

What happens when the normal flow is interrupted: a live bug, or the workshop itself misbehaving.

### When a bug cuts the line  [feature: F-bug]

**User story:** as the product owner, I report a bug in the shipped product and it gets fixed before
anything else; the feature that was mid-build comes back on its own afterwards, and no work gets lost.

Mid-feature, the human reports: "the card is broken on the phone." The feature is set aside at a checkpoint,
the bug takes the lane, and once no bug is waiting, the feature returns as the very next thing to
finish.

**Precondition:** a feature is in work when the bug report arrives (with nothing in work, the bug
takes the lane).

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
6. On resume, before it integrates, a parked feature re-fences and re-proves its delta against the
   now-committed truth, the way a later lane does under [INV-39]: the bug's fix may have moved the law
   the delta was built against, so a delta proven only against the pre-bug truth is re-verified on the
   new tree, never integrated blind. [T-9, INV-39]

**Postcondition:** the bug's fix is landed; every parked feature is back in work (or landed) in its
original order, each re-fenced and re-proven against the truth the bug's fix left behind; no red work was
committed anywhere.

#### The class hunt before a bug closes

**A confirmed bug drives a class hunt before it closes.** A confirmed bug is a sample of its class, and before the fix is called done the method drives four moves rather than one. First, name the defect abstractly — the KIND of mistake it is, a scope too narrow, a missing guard, an assumption that holds in one place and fails in the neighbour — then actively search every surface where that kind could live and fix every sibling found in the same change [INV-56]. This is the active face of the class rule: the search goes looking for the siblings not yet seen, past the one instance already in hand. Second, ask whether the bug has a structural cause — a boundary the architecture drew wrong or left silent, a node owning what it should not; a yes updates ARCHITECTURE.md in the same change, since a cluster recurring in one district reads as an architecture smell rather than bad luck. Third, ask whether the spec even describes the broken behaviour; a spec silent on it or under-describing its composition is the real defect — the spec is fixed first so the prover can flag it, then the code fix lands under it [INV-15]. Fourth, escalate to the human when the class boundary needs his read — which behaviours are one class, what the intended design was, whether a whole area wants a rethink — the method stops and asks rather than guessing the boundary [INV-4]. The product-prover carries a class lens for the same three questions raised on a found defect: does the same kind live elsewhere, does the architecture account for it, does the spec describe it. The four moves are the bug door's close condition, so a point fix that leaves the siblings standing is a status, never a landing [INV-26]. This sharpens the class rule from fixing the class already in view to going and finding the rest of the class not yet seen [INV-56], and it generalizes the spec-under-describes-composition lesson to every bug. (Born of the exhibition's pinch-zoom bug, where naming the class — a browser zoom desyncing the scroll animator, guarded on only some gestures — turned one report into five live siblings, all real and all fixed together with the spec updated to match; the owner's standing word 2026-07-12.) [INV-124]

### When the workshop itself misbehaves (the problem ledger)  [feature: F-problem-ledger]

Some noise comes from the workshop itself: the test harness flakes, a dependency goes missing, a shell command fails for a reason outside the product, a tool times out. The session retries and moves on — but the same noise then eats the same minutes, session after session.

**The problem ledger** is the host's dynamic list of this operational noise. It lives in one git-tracked file, `.live-spec/PROBLEMS.md` (the template ships in the pack). Within `.live-spec/`, only the checkpoints stay ignored [E-8]. The ledger is born on its first entry.

An entry is a **signature**: a short, greppable plain phrase, such as "element not clickable: #ex-skip" or "zsh eats a bare ===". Each signature carries its dated occurrences and one status [E-24]:

- **WATCHED** — seen once.
- **OWNED** — a named queue row will solve it.
- **AGREED NON-PROBLEM** — dated, the human's word.
- **SOLVED** — its row landed, date kept.

#### The ledger walk

The moment noise fires mid-work, grep the ledger for the signature. What the grep returns decides the next move.

- **Not listed:** write one WATCHED line — signature, date, one line of context — then keep working. This write replaces the silent retry. It never takes the lane. A defect of the product is a bug; it goes to the bug lane instead [T-9].
- **Listed (second occurrence):** it gets an owner right then: a queue row (someone will solve it) or a dated agreed non-problem in the human's own word. That verdict belongs to the human alone [INV-9]. Write the recommended owner right away, and let the ask ride the batched report [INV-4, E-22]. The lane never stalls on it.
- **Third recurrence, no owner:** this exposes a defect of the method, one that reaches past a single day. It leaves the host as a wish to the pack's own queue — one inbox file, from a host window [E-11, INV-10] — citing the signature and its dates [INV-23].

After the owner is written, the entry only collects dates:

- A recurrence on an OWNED or AGREED entry just appends its date; nothing else changes.
- Re-raising an agreed non-problem is the human's move — he re-raises it from the growing date list.
- When a landing closes an OWNED entry's queue row, that same session flips the entry to SOLVED. The entry never waits for an audit to learn its row landed.

#### Parking a known, owned problem

**A known, owned problem never blocks unrelated work.** It stays parked while every unrelated lane keeps rolling. That's either a recurring defect with a named mechanical owner, or a check held red for an understood, recorded reason.

Its ledger line, or the owning row, or an expected-red note in the record, holds it in place: when one thing doesn't quite work, it should leave everything else free to move.

Two rules keep a known problem parked:

- Hand-fixing loops cap at the ledger's own two-strikes law: the second occurrence buys an owner, never another hand-pass.
- Once a defect has its named mechanical owner, its instances get serviced in batch: the fence fixes them silently wherever it catches them, then appends one ledger line at session's end. It's never a per-instance ceremony that interrupts the work or the human reading it.

A real new bug still preempts [T-9]. This law governs only the known, owned problem [INV-56].

#### Seams

- **Write-ownership.** Sessions write the ledger. A worker reports noise in its checkpoint; the session carries it over. A worker whose brief names the ledger among its files may write it directly. The brief is what states the write-ownership law [ACT-3].
- **Concurrent edit.** Two sessions on one host share the file under the concurrent-edit fence, like any doc [INV-11].
- **Same problem?** Grep and eyes decide whether two entries are really one problem. Signatures stay short so the grep stays honest. One problem found under two wordings merges into a single entry at the milestone compaction.
- **Archival.** At that compaction, SOLVED and agreed entries move to a dated ARCHIVED tail of the same file [M-1]. One file stays the one home, and the ledger never grows unboundedly.
- **Product versus workshop.** This is the workshop's law; the product keeps its own. A recurring product bug re-doors to a feature under the pipeline's rule, distinct by what broke.
- **Facets.** No visible surface, so facets are N/A.

#### Scope for this landing

Non-goals:

- No mechanical guardrail yet. The named candidate — a pre-push check that no entry crosses a milestone unowned — earns its row after real usage.
- No automated signature matching.
- The first foreign-host ledgers (tlvphoto, track-coach) open from their own windows. This landing opens the pack's own.

**Success measure.** The next operational hiccup in a live-spec session lands as a ledger line instead of a silent retry, checked at the milestone audit [default].

#### Reuse before reinventing

**Before reinventing a fix, search for an existing skill.** Two moments trigger that search:

- **At a project's setup** — founding, or adoption's orient, beside the founding questions [B-2, B-3] — the pack scans the skills already installed and the catalogs it can reach. It looks for matches to the project's kind and crafts, then proposes a fit list with a recommendation. The human's word picks.
- **At a struggle** — a ledger entry reaching its second occurrence [INV-23], a taste artifact rejected twice [INV-62 kin], any failure family that keeps returning — the next attempt waits for one search. An existing skill or published checklist may already own this failure class. Adopt or reject a found skill by name, and record the verdict where the struggle lives: the ledger entry, the kill-list, or the row.

Borrowing follows one practice: invoke a found skill as it ships. Paraphrase a lesson into our own documents and credit its source by name. Verbatim text travels only under its license, with the notice kept. Unlicensed text is never republished [INV-65].
## Starting and adopting a project

How live-spec enters a project: a fresh start, or attaching to work already under way.

### Starting a new project (bootstrap)  [feature: F-bootstrap]

**The version-control gate runs first**, in the same order adoption keeps [A-0].

- Git has to exist — initialize it if it's missing.
- Settle on a remote, or decline one explicitly, before creating anything else: a gate can't protect files older than itself.
- Copy the templates — SPEC, ARCHITECTURE, TEST_MATRIX, ROADMAP, JOURNAL, NEXT_STEPS — plus the suite scaffold (`test_scaffold.py` into `tests/`).

The scaffold is the minimal runnable suite, and it defines what "green" means for landing #1:

- the document set exists;
- every header is genuinely filled in (a leftover placeholder counts as red);
- the coverage checklist is in place;
- there's one live-state block.

That green is a starting floor — landing #1 ships its own first real test beside the scaffold, and traceability checks grow from there.

Offer hooks at bootstrap the same way as at adoption [E-6]: never impose them, plain words first. Then the first wish enters the queue, and the pipeline runs from intake [B-1].

This is an always-rule: never land into an unversioned host. Version control has to exist, and a remote either exists or is explicitly declined — recorded, not just recommended — before the first landing [INV-8].

#### Founding questions

**Ask the founding questions; do not infer them.** Before the first wish walks, answer the questions that shape everything downstream, right in the new spec's opening.

First among them: **personal tool, or reusable product?**

- A founding answer resolves like any setting [E-13]: check the human's profile first — if a personal-scope standing preference covers it, that seeds this project's default, and the agent says so out loud, never silently. Otherwise, ask.
- Never derive the answer from examples: naming three of the human's own artifacts doesn't mean the product is those artifacts — they might just be its first users [B-2].
- This question is deliberately stronger than the walk's usual proceed-on-default habit [INV-4, INV-12]: an ordinary open question can ride the row while the lane keeps moving, but a founding answer can't — it blocks the first wish until the agent asks or reads the profile.
- Every later sentence leans on this answer, so an inferred one is the silent micro-decision [INV-5] at its most expensive.
- Adoption owes the same question at orient — A-1 carries the pointer.

**Learn who the agent is working with before any founding question resolves.** At founding, at adoption's orient [A-1], and at the first session on a new machine or with a new human, run one step first: look for the personal profile at its one home [E-13].

- If the profile exists, load it and say so: name the file, and read any unrecognized line aloud rather than skip it silently, under the ladder's own law [E-13].
- If it's absent, offer to create it from the template (`templates/profile.template.md`).
- The human tells the agent about themselves — chat and docs language, how to address them, what they do, their own vocabulary — and can name sources for the agent to read: their repos, their docs, a public page. From a named source, propose lines.
- Every line lands on the human's word: write a told line faithfully, and accept or drop a proposed line one at a time — a dropped proposal stays dropped [INV-9 is this rule's ceiling: mode and trust move only on their word].
- The human can decline the whole step. Then the session runs on package defaults and says so, and the offer comes back at the next project setup, never mid-work.
- Skip the step where there's nothing left to do. Once the profile exists, a later session just loads it.
- A worker session never onboards anyone; its brief already carries the setting lines it needs [ACT-3].
- The template marks every placeholder as a placeholder, so nothing in it can pass for the human's word [B-3].

**When the product is an instance of a reusable mechanism, founding proposes the split — it never imposes it.** The personal-vs-reusable answer has a third face the question alone does not reach: a product can be reusable and still ship as one concrete thing a real person uses today — a gallery that happens to hang these photos, a coach that happens to read these tracks. The moment the reusable answer lands on a product that carries content of its own, founding asks one more shaping question: is the generic mechanism worth its own home, apart from the content it serves right now? The agent proposes; the human's word decides; both outcomes are recorded [B-2]. The proposal names two homes and what each owns: an engine repo — public by default, generic, tested on its own generic fixtures, carrying a content contract that names every place a concrete instance plugs in [INV-79] — and an instance home — the content itself, the corrections the content earns, and the private fragments, with heavy binary content placed per the placement view's prompt [INV-75]. The engine owns the how; the instance owns the what. A donor-specific constant found while carving becomes a named content-contract entry with a works-without-it test [INV-79]. A single-repo project is a first-class, complete outcome; when the human declines the split, the agent records a one-line reuse note in the host profile under the fixed key `reuse.split-declined: <date>` and raises the offer again only when the product outgrows one home — a second instance appears, or the content and the mechanism start fighting for the same file [INV-36's live-line discipline]. When the human takes the split, the pair-leadership rules bind from that moment. Adoption owes the same proposal at orient, alongside the other founding questions [A-1, B-2]. [INV-85]

**The project knows what kind of thing it is — and the kind can change.** Beside personal-vs-reusable, founding asks a second shaping question: **what is this project** — a book, a backend service, a static site, a fullstack app, a CLI, a skill pack. Record it in one plain line in the host profile (`project.kind`, the settings ladder's host scope [E-13]). Adoption owes the same ask at orient, alongside the other founding questions [A-1, B-2].

These three intake verdicts stay separate from the per-wish work-kind [T-16]. Three verdicts share the intake breath, and they never collapse into one:

- the project kind says what the product is, and seeds project-wide defaults — the usual work-kind, which facets and feel-lenses apply by default [T-13, INV-30];
- the wish's work-kind says what this wish builds;
- the placement [INV-37] says where it lands on the map.

The seed proposes; a written line decides. If a host already records its own default (`work-kind.host-default` [T-16, E-13]), keep it — the project kind never silently overrides an explicit profile line.

The ask always belongs to the human: no personal-profile line can say what a host is, so B-2's profile-seeding arm never answers this question — the agent asks it at founding or orient, every time.

Curate the kind vocabulary the same way work-kinds are curated [T-16]. The list above names the shapes real projects already wear, and a custom kind joins through the queue when a named project the list didn't serve well shows up. Expect custom kinds — the queue is their door.

The line stays alive, continuously updated: the moment work notices the project has outgrown its kind — the static site that grew a backend — update the line on the human's word, and journal it right then, never park it for an audit [INV-36].

**A project's founding declares its concrete layers and its concrete proof kinds.** The entry impact read, the footprint categories [INV-128], and the test ladder are kind-abstract stations: the pack states them once, and each project kind fills them with its own concrete decomposition. The three footprints hold past code — a presentation-only change touches what the audience meets and nothing behind it, a single-module change stays inside one owned layer, a cross-cutting change moves a shared law or several layers — but the layers themselves are the project's own, and so are the proofs. So the founding line that records `project.kind` [INV-36] carries two more, in the host profile: a `project.layers` line naming this project's concrete layers (its footprint categories) and a `project.proofs` line naming its concrete proof kinds (its test-ladder rungs) — a codebase splits frontend, backend, and store and proves with tests and rendered checks; a photo site splits content, rendering engine, and deployment and proves with a byte-diff of the baked output and the owner's eye-walk; a promotion campaign splits message, channels, and assets and proves with a register lint and the owner's review. A founding check reads the profile: a `project.kind` recorded with no declared layers and no declared proofs is incomplete, flagged at adoption the way an unbacked surface is [A-10]. The per-kind fill is the project's own ratchet from there — the footprint check [INV-134] and the test-level rule read the project's declared categories rather than a hardcoded code list — and ARCHITECTURE.md carries the per-kind footprint-and-proof table beside the node-structure-by-kind scaffold, spec-author and test-author reading the declared layers and proofs instead of assuming code. [INV-135]

A project attached before this law owes no retro-ask; the line arrives at the next landing that would lean on it, like any forward-binding intake law [T-16 kin].
### Attaching to a live project (adoption)  [feature: F-adoption]

Adoption runs as a sequence; each phase finishes before the next starts. Run the version-control
gate first, before touching or moving anything, so the whole run stays reversible [A-5]. The step
numbers below just name the phases — they don't force an order. A phase marked [target] gets
recorded and skipped until its machine ships, and the journal records the deferral [A-0].

1. **Orient — read everything first.** Adoption never assumes a blank slate.
   - Read every existing document before touching anything: README, any roadmap, any spec, any
     test suite, journals, TODO files, any wikis in the repo.
   - Answer the project's founding questions about what is found — personal-vs-reusable comes
     first, per the rule at the bootstrap [B-2] [A-1].

2. **Inventory.** List the code, the user-facing surfaces, and the document set from the orient
   pass — each entry with its owner (file:line for surfaces) [A-2].
   - Listing the surfaces seeds the host's surface registry [E-10].
   - Adoption's working artifacts — the orient digest, this inventory, reconcile notes — live in
     the host's `.live-spec/adopt/`, tracked in git as the run's audit trail. They never scatter
     into the host's own folders [A-8].

3. **Re-engineer the existing documents into live-spec shapes.** Nothing existing gets ignored,
   and nothing gets trusted unreconciled.
   - An existing spec becomes PRODUCT_SPEC.md sections — keep the original claims, but mark them
     unverified.
   - The inventory's file:line seeds ARCHITECTURE.md [E-14]: its nodes come from the real code
     structure, so the architecture layer is already in place at adoption.
   - Existing tests become matrix rows, cited at their real level and filed under those nodes
     [E-15].
   - An existing roadmap or TODO becomes queue rows.
   - Reconcile every unverified claim — pin it to file:line, or remove it — at the first landing
     that touches its surface, and reconcile whatever is left by the first milestone, whichever
     comes first [A-3].

   Every unbacked live surface needs one verdict. Some inventoried surface reaches the user but
   carries no spec backing — a de-facto prototype, the most common residue in an adopted host —
   so flag it at orient [A-10]. The human then decides, per surface:
   - **promote** — it enters at the spec step as a feature [INV-16].
   - **quarantine** — move it into a prototype home and label it [E-17]. This is itself a
     production change: the human is choosing that users lose the surface, or see it relabelled.
     Leave a dated one-line provenance record at the prototype home (what, why, date) — the attic
     manifest's mirror.
   - **attic** — archive it instead [A-4].

4. **Attic over deletion.** No adopt or rework run deletes a host file — superseded files move to
   `attic/` with a manifest line [INV-7].
   - Any file superseded during adoption or rework moves to the attic (`attic/`), the host's
     archive folder.
   - The attic is append-only: one manifest line per file (what it was, why moved, date).
   - On a basename collision, prefix the name with its source directory; if the name is still
     taken, append a numeric ordinal — `-2`, `-3`. This is the pack's one collision law, stated
     once in the base skill (rule 18) [E-9].
   - Flat-with-manifest versus dated subfolders stays an open decision [D-1] [A-4].
   - One exception passes only through a gate: adoption may offer a cruft sweep — clearly
     regenerable junk (caches, build leftovers, already-gitignored files) — listing file counts
     and sizes, and delete only on the human's explicit OK, never silently. Authored content
     never qualifies; it always goes through the attic [A-9].

5. **Version-control gate — done first** (see the note above) [A-5].
   - If the host has no git, init it, write a `.gitignore` that excludes heavy generated or media
     artifacts, and make a pristine baseline commit — this doubles as the diff baseline.
   - Settle the remote as a named deliverable: by the first landing, a remote (e.g. GitHub) either
     exists or the human has explicitly declined one, and the run's journal records the outcome.
   - A recommendation alone does not close the gate [INV-8].

6. **Baseline snapshot [target].** Render or produce the current artifacts as they are, and save
   them — this is the diff baseline the snapshot machinery [E-7] will guard [A-6].

7. **Incremental thereafter.** The host now runs on the same wish lifecycle as a bootstrapped
   project [A-7].
   - Record installed skill versions in `.live-spec/` at attach time.
   - On any version change — live-spec itself or any installed skill — re-read the changed
     SKILL.md before continuing; never coast on the stale in-memory version. Write a one-line
     journal note naming old → new.
   - The re-check also runs at every safe breakpoint [M-2]: re-stat the installed skills and the
     package on disk (version and file mtime), and re-read whatever changed — a parallel session
     may have shipped an update mid-flight.
   - The same walk asks the public repo once a day whether the pack itself has moved, through the
     update check [E-25].

### Bringing an adopted host up to the current pack (catch-up)  [feature: F-catchup]

The catch-up walk brings an already-adopted host's documents and records onto the current package. The host's owner asks in any wording; the ask might read "re-layout the documentation" or "catch up to the current pack". The ask names no procedure, so the package names one. The walk's operating guide is MIGRATION.md in the package repo. The adoption guides open by routing: a host that never adopted goes to adoption, and a host that already adopted goes to this walk. The walk is the host-side half of the package's own movement: when a release changes something hosts must act on, the release writes the instructions, and the hosts' own sessions execute them through this walk.

**A release that owes its hosts actions ships a dated migration chapter.** When a package version changes something a host must act on, that release lands one dated, versioned chapter in MIGRATION.md stating the host-side steps; a release owing nothing adds no chapter, and its changelog entry says the release carries no host actions. The catch-up walk is version-chained: orient reads the host's recorded package version, and the work list is the ordered chain of migration chapters from that version to the current one, oldest first. A record that carries no readable package version, such as commit pins or no record at all, starts the chain at the earliest chapter, and the half-done-state law makes over-application harmless [INV-89]. One plan carries the whole chain, however far behind the host is, and the half-done-state law makes a partially applied chain resumable [INV-89]. [INV-91]

**What must keep working.** First adoption's phases stay exactly as specified [A-0..A-10]. Superseded host files move to the attic with a manifest line and are kept [INV-7, E-9]. One window serves one repo of an engine-and-instance pair and stays read-only on the other half, save one inbox file [INV-86, INV-10]. The owner's named gates stay in force: the cruft-sweep delete gate [A-9] and the version-control gate [A-5].

**The walk runs four phases in order.** [A-11]

1. **Orient on the delta.** The session reads the host's installed-set record and the tree as found. It reads the package's current VERSION and journal. The work list is the difference between what the host carries and what the current package expects. Preconditions written in the guide are checked against the tree, and the tree is the truth when they disagree.
2. **Plan, behind the owner's gate.** The session writes one plan document into the host's `.live-spec/adopt/`, where it lives through the whole walk [A-8]. It lists every file that moves, merges, or retires, every record that reformats, every offered rename, and every open conflict. The owner's word on the plan comes before any file moves. A walk that finds nothing to do reports that and ends.
3. **Execute, preserving facts.** The phase opens with a clean-tree baseline commit in the host, so the walk's own changes stay reversible [A-5]. The walk runs under the checkpoint discipline: its checkpoint names the plan document and the per-step state, and an interrupted walk resumes from the checkpoint under the already-given gate. Each step follows the half-done-state law and the preserve-and-re-home law below.
4. **Verify and re-record.** The host's own gates run, including the test suite where one exists. A red gate is the walk's own open defect: the walk stays open until the gates read green, and the checkpoint carries the red state across sessions. The installed-set record is re-recorded in the current format. The walk lands one journal chapter. The plan document and the superseded files rest in the attic and the adopt records.

**Pair routing.** The walk covers exactly one host. When the ask arrives at one window of an engine-and-instance pair and means both halves, the window executes its own repo's walk and files one inbox wish naming the other half's catch-up debt [INV-86]. A pair half that carries no `.live-spec` records of its own is an under-attached host; its walk opens with the full adoption run for that repo [A-0..A-10] before the catch-up items.

**Machine-level steps run once per machine.** Steps that touch the machine's shared homes, the installed-skills folder and the personal profile, run once per machine. The guide states each such step's already-done check: the directory that exists, or the record that reads current. A step whose check passes is reported done and skipped.

**Every step is safe on a half-done state.** [INV-89] Every catch-up step opens by reading its precondition from the tree. A step whose end state already holds is reported done and skipped. A step that finds both the old and the new form present merges file by file. A file with identical content on both sides drops the old copy to the attic. A profile file with differing content is reconciled by where each line's home sits under the settings ladder: a host-profile line whose home is the personal profile under the current ladder moves up, and a host-scoped line stays. A move up writes a machine-shared file, so it follows the promotion law and re-reads that file immediately before appending [E-16]. Any other differing file, and any remaining conflict, rides the plan to the owner's gate. A directory is never nested inside its replacement, and the new form is never overwritten by the old. An installed-set record kept in an outdated format, such as commit pins, retires to the attic; the new record is read from the version lines of the skills actually installed on the machine and from the package VERSION [M-7]. The skills installed on disk are the authoritative set, and a stale record is corrected from them.

**The walk preserves facts and re-homes them.** [INV-90] The host's recorded facts survive the walk. Content moves into the current shapes, and a fact leaves its home only by moving to a better one. Settled prose is rewritten only where the owner rejected it or where the new shape cannot hold it as written; the plan carries each proposed rewrite and the gate decides. The package's canonical document set and names live in one list in the adoption guide, ADOPT.md, and every other guide points at that list. A host that adopted under its own names, such as a product spec named SPEC.md, keeps its names, recorded as one host-profile line (`spec.file: SPEC.md`); the plan may offer the rename together with its pointer sweep, and the package's guides read "PRODUCT_SPEC.md" as the host's spec file under its recorded name. The `spec.file` key carries its own row in the package-defaults table, so the settings card traces it like any recorded line [E-13, INV-87]. A line the walk re-homes shows on the settings card at the card's next render, under the card's own render-moment rule [INV-87]. Stray state files re-home: a checkpoint file at the repo root moves to `.live-spec/checkpoints/`, a closed one to the attic, and a look-alike state directory merges under the half-done-state law [INV-89].

**The walk proves itself with a before-and-after comparison.** Before any file moves, the walk records a pre-walk inventory beside the plan in `.live-spec/adopt/`: every document with a content fingerprint, the host spec's anchor multiset, and the test suite's verdict and count as found. After the execute phase, the walk records the same inventory again and compares the two. Every difference must be accounted for by a plan item: a file is unchanged, re-homed to a named new path, merged from named sources, or resting in the attic under its manifest line; an anchor delta must match a change the plan names; the suite reads at least as green as before. A difference outside the plan blocks the verify phase until the owner's gate accepts it as a plan amendment or the step is reverted. [INV-92]

**The pre-walk state stays restorable.** The baseline commit is the walk's restore point: the plan document names that commit and states the one command that returns the host to the pre-walk state. The attic keeps every superseded file readable without any restore. [INV-92]

The walk changes documents and records. It creates no visible product surface, so the standard facet sweep does not apply, and the plan document opens by the ordinary show rule.

**Skill behaviour.** The trigger is the owner's ask to bring an adopted host's documentation or records onto the current package, in any wording. The correction routes that ask to this one named walk with a written plan and the owner's gate, where an unnamed procedure would scatter ad-hoc edits over the tree. The walk does not fire on a first adoption, which the adoption phases own; on a single-document edit, which the docs-only door owns; or on a restructure of the host's own product, which is the host's own queue row and pipeline. The catch-up walk fires only when the host's recorded package version is behind the current package VERSION. A docs restructure that carries no version delta is the host's own queue row through its pipeline, whatever wording the ask used. The trigger wordings are examples under this test. A wording never decides the routing; the version delta decides. [INV-110]

**A same-version docs-layout pass rides one sanctioned light vehicle.** The routing sends an adopted host's ask to its own queue when the ask restructures the host's own documents with no package-version delta [INV-110]. That pass runs one named shape. The owner's decisions are locked in a checkpoint before any file moves [INV-107]. The work builds on a clean pushed base, so one command restores the pre-pass tree. The pass proves content survived by a word-token multiset check AND a punctuation multiset check, since word-token identity alone passes a reflow that dropped or moved punctuation. The pass also reads the full suite green on the restructured tree, from the log's own line [INV-39], since a reflow can break a suite-owned doc check that no multiset reads. The pass lands one journal chapter naming what moved and why. A pass that rides a branch back to main closes through the restructure merge gate [INV-114], where this vehicle's multiset proof serves as the gate's first part; a pass landing directly on main owes its green suite on its own. A host never improvises a layout pass; it cites this vehicle. [INV-111]

**A restructure or migration merge gate judges the delta.** When a restructure or a migration is gated for merging back into main, the gate judges the delta. It has three parts: load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check [INV-111]; the full suite green on the merged tree [INV-39]; and a full prover pass on both sides whose blocking set is delta-scoped — an unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change. Pre-existing findings equal on both sides route to queue rows in the same landing and never block. And a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation. The token-identity part scopes to a content-preserving restructure. A deliberate redesign changes content by intent, so it routes by the architecture-redesign law [INV-113], and its merge stands on the green suite and the delta-scoped prover pass, with no token-identity demand over text the redesign meant to change. (Born of a strictly-improving restructure merge parked on the old side's pre-existing clarity debts because a spoken «prover finds nothing both sides» was over-sharpened into «any finding parks the merge», corrected live 2026-07-12.) [INV-114]

**Non-goals.** No script automates the walk; the session executes it as a procedure. No rename is forced. No package-side registry of hosts' catch-up states exists, since each host's own records carry its state. **Success measure.** The first real catch-up, the tlvphoto pair, runs from the hosts' own windows with every procedural step answered by the guides. A question back to the package window that reveals a guide hole counts against this measure, and a taste question to the owner does not. `[default]`

### Meeting your settings  [feature: F-onboarding]

The founding questions themselves do not change: `project.kind` is still always asked. [INV-36]
The profile is still found or founded at setup on the human's word. [B-3]
Defaults stay told, never interrogated; the card adds a showing, and no questionnaire appears. [INV-31]
The package-defaults table stays the settings' one normative home, and the card is a derived view of it. [E-13]

At the end of founding, and again at the end of adoption's orient — once `project.kind` and the economy rung have settled — the session renders the settings card. You reach it twice: here at setup's end without asking, and any later time by asking. You read one page that shows what the pack has set up for you and what is yours to change, and nothing is asked of you. From any row you move by speaking its change-line in chat; a return visit re-renders from the current truth, so the card never goes stale, and its feel follows the frozen norm below.

**The card shows at setup's end.** The settings card lists every setting the pack knows. Each row gives the setting's plain-words name, its current value for this project where one is recorded, and one line saying how to change it in plain speech. A personal value, such as a name or a language, prints as the reader's own and is labelled theirs to change; where nothing is recorded yet the row shows the rule alone, which is exactly how the approved norm page looks. Each value is read from the settings ladder: the reader's own profiles and this host's recorded lines. The card opens by the show rule, a new browser window on a local seat and its own channel on a remote seat [INV-67]. The card's showing passes the pre-show register lint before it opens, on the fixed copy and the rendered values alike. [INV-83]

**The same card answers the standing question.** At any later moment the person may ask what they can customize, in any wording. The answer is the same card, re-rendered from the current truth at that moment. A stale hand-kept copy never answers.

**One catalog home.** The card and the standing answer derive from one source: the package-defaults table in the base skill, joined with the reader's own profile files and the host's recorded lines. No second hand-kept settings list exists anywhere. The base table marks each row card-visible or internal; internal rows are workshop machinery, such as a checkpoint path or worker tiers, that would clutter a reader's page. Completeness runs both ways: every card-visible table row appears on the card, the host's recorded profile lines appear in the card's own project-rules part, and every card row traces to a marked table row or a recorded profile line. A card missing a card-visible row is a defect, and a card row with no source is a defect. [INV-87]

**The copy states rules, and personal values stay the reader's own.** The card's fixed copy describes each setting as a rule anyone can read. For example, conversation follows whatever language the person writes, and written work is in the project's recorded documentation language, good English out of the box. The fixed copy states the rule frame, and the current value comes from the settings themselves. A personal value, a language or a name, appears on the card only as the reader's current value, labelled as theirs to change. The fixed copy never presents one person's value as the product's prescription. (Set by the owner on 2026-07-10, after a mockup showed his own language and name as if the product prescribed them.) [INV-88]

**The look follows a frozen norm.** The card's look and feel follows the approved artifact. `norm: docs/norms/onboarding-card-2026-07-10.html`

**A script renders the card.** A build-time script (`scripts/onboarding-card.py`) reads the package-defaults table and the profile files and produces the card as a rendered page. A malformed table row fails the render loudly, and a silently dropped row is a defect. A missing personal profile renders the card on package defaults, says plainly that no profile exists yet, and names how the founding offer creates one. When the defaults table grows a row, that row's card rule-copy is drafted on the clean-writer road before it first renders. [INV-84]

On a phone or narrow window the card reads as one column, top to bottom. [default]
The card is a static rendered page; nothing on it depends on hover. [default]
A missing personal profile is the card's empty state: package defaults shown, the absence said plainly, the founding offer named. A malformed catalog row is the error state: the render fails loudly. The language check runs before any showing and is the card's blocked state: flagged text stops the showing. A blocked card is not shown until the flagged text is fixed. The block names what it flagged. Loading states do not apply to a static page.
The card is plain structured HTML: headings, readable contrast, keyboard-scrollable. [default]
Rendering the card is read-only, so two sessions can render it at the same time without collision. An open card shows the truth of its render moment; a setting changed afterward, by this session or another, does not update the open page, and asking again renders a fresh card. [default]
The card holds independently beside any other open window, whether a decision page, a report, or a chat exchange; nothing hands off and nothing clears. The card needs nothing from the person, so it may stay open through any long unattended stretch.
The card renders in under a second on a pack-sized catalog; the render script's own run is where the number is read. [default]

Non-goals: no interactive questionnaire, since setup's own questions already exist and stay; no editing surface, since a change is spoken and profiles stay plain files; no new machine-readable catalog format, since the existing table is parsed as it stands. Success measure: a person new to the pack, given the card, changes any setting by saying that row's own change-line, checked at the first real onboarding. [default]

### Running an engine and its instance as a pair  [feature: F-pair]

Regression fences first — what must keep working: a project that answers personal, or answers reusable and declines the split, runs exactly as today (one spec, one queue, one journal, one inbox, one window); the founding questions never fuse — the split ask is its own founding question, and it fires only when reusable lands on a content-carrying product; the three intake verdicts stay a closed three [B-2, INV-36]; the cross-seam channel reuses the inbox door, the write-ownership law, and the concurrent-edit fence exactly as they stand [E-11, INV-10, INV-11]; the content contract and the heavy-binary prompt keep their meaning, cited, never redefined [INV-79, INV-75]; and one-story-one-row holds across the seam [T-17, INV-1].

**Each repo of the pair is a full live-spec host — the pack attaches to each, never to the pair.** The engine repo and the instance home each carry their own spec, queue, journal, and `.live-spec/` folder [E-1]. No third document spans the pair; the no-third-document law holds across the seam as it holds within one host [E-14]. The engine's spec states what the mechanism does for any instance, and its content contract is that promise's public face; it cites no instance's content — a spec that names these photos has stopped being generic [INV-79]. The instance's spec states what this product is for its real user, in that user's domain words, and cites the engine only by its contract entries' handles (D-7). Each host's wishes ride its own queue; a wish that is genuinely both engine- and instance-shaped is two wishes, split at intake, one row in each queue, each citing the one spoken wish [T-17, INV-1]. Each host carries its own inbox; the instance's inbox is the human's front door, since the instance is the product they actually hold [E-11, INV-37]. A lesson travels engine↔instance only through the inbox door under write-ownership: the learning window files one new inbox file into the other repo and journals the hand-off in its own tree; nothing in a lesson's travel writes a foreign repo beyond that one inbox file [E-11, INV-10, T-10]. One window serves one repo of the pair; unsure means ask, never infer; a window is read-only on the pair's other half save for that one inbox file [INV-10], and the concurrent-edit fence still binds inside each repo [INV-11]. [INV-86]

**The engine's spec crosses the boundary clean — its own public provenance and neutral mechanism names.** A feature proven first on a live instance and then generalized into the engine leaves its instance origins at the seam [INV-86]. The engine's spec records how each behaviour landed in its own code: a reconciliation log headed "how each behaviour landed in code", each entry citing the engine's own public commit ("landed in engine commit `<hash>`"), opened by one sentence stating the normal intake path — a feature proven first on a live instance, then generalized — so no entry re-explains it. A private instance's commit, invisible to the engine's reader, stays out of the engine's provenance. And a mechanism carries a neutral internal name in the engine's own vocabulary — the unfold step, the show-more control; where a running instance shows a locale-specific label for it, the spec notes that string as instance-supplied copy [INV-79] and the neutral term stays the mechanism's one name [E-4]. The publish gate checks a generalized package for the two leaks this prevents — a private-instance provenance hash, and an instance's locale label standing as a mechanism name [E-20]. (Born of the exhibition-engine public-publish pass, 2026-07-12.) [INV-119]

**The pair's load-bearing walk — a producer wish crosses the seam.** Entry: the human throws a wish at the instance window ("let a visitor filter the gallery by year"). Intake places it on the instance's map and finds two parts — a generic part any instance could use, and this instance's own part; at the seam that is two wishes, split at intake [INV-37, T-17]. The instance window, an outsider to the engine, files the engine-shaped part as one engine inbox wish and parks its own half as a dated blocked-on-engine debt line, so the lane keeps moving [E-11, INV-10, INV-56]. The dated debt line appears in the instance's every status report until the engine ships the wish, so an engine window that never opens appears as an aging block in each report [INV-27]. The engine's session sweeps its inbox first and lands the wish through the full pipeline on the engine's own generic fixtures; a new plug-in point becomes a named contract entry with a works-without-it test; the engine ships and versions on its own rhythm [T-10, INV-79, E-3]. The instance then updates to that engine version, plugs its real content into the new entry, and verifies on the real product — the instance's suite proves what the engine's generic suite by construction cannot; the parked row un-parks and closes whole [INV-56, T-17]. Exit: the visitor filters this gallery; the next instance inherits the feature with no engine work; both journals hold their half, and the spoken wish traces to both rows [INV-1].

Non-goals: no repo-layout mandate (a declined split forces nothing, and a one-repo-two-scopes variant queues on its own if a real project needs it); no automatic extraction (the split is the human's word, the carving is ordinary pipeline work); no cross-repo atomicity (the parked-debt line and the inbox hand-off are the coordination); no new sharing model beyond which tree a window may write. Success measure: one real producer wish, thrown at the instance, ends with the generic part landed in the engine on generic fixtures with a contract entry, the instance verified on real content, both journals holding their half, and a second instance able to inherit the feature with zero engine work — measured on the first real pair, read-only from this window.

#### How the skills arrive on a machine

The pack ships one installer, `install.sh`.
- It copies every pack skill into the agent's skills home (`~/.claude/skills/`).
- It's idempotent: it backs up an existing copy with a timestamp before overwriting, and never
  deletes.
- The backup lands in an attic folder beside the skills home, never inside it, so the agent never
  scans a stale copy as a live skill — the attic principle applied at install time.
- The installer writes exactly what A-7's record clause writes to `.live-spec/`. Installing and
  recording are two halves of one seam [E-21].

#### How the machine learns a newer pack exists

Freshness [A-7] only re-reads what's already on the machine — delivering a newer pack was nobody's
job before this. The pack carries an update check, `scripts/check-pack-update.sh`:
- It runs once a day, at the first freshness point of the day, throttled by a dated stamp in the
  machine's pack home (`~/.claude/live-spec/update-check-stamp`).
- It asks the public repo — the VERSION file on `main` — whether the pack has moved past what this
  machine runs, handing it the installed version from its recorded home [M-7].
- When the remote is newer, it proposes in the session's own chat: naming both versions, pointing
  to what changed (the public journal), and naming the road forward — `install.sh`, whose attic
  backup already guards the overwrite [E-21], or a plain pull where the repo runs the pack itself.
  It never installs anything; updating stays the human's word, like every install gate [ACT-1].
- If there's no network, or the answer is unreadable, it reports one honest "check skipped" line
  naming the address it tried — a dead URL must never masquerade as a quiet offline day. It never
  blocks and never guesses.
- An offline day leaves the stamp unwritten, so the next session retries.
- A machine ahead of the public repo — the developer's, mid-work — reads as up to date; the check
  only proposes forward, never a downgrade.
- It's E-23's outward twin: sync-skills keeps the machine's copies true to the local repo, while
  the update check tells when the public repo has moved past both.

This has non-goals:
- no background daemon (a proposal belongs where the human reads, in the session),
- no auto-install ever,
- no per-skill remote diff (the pack version speaks for the whole).

The check's only face is the proposal line, governed by the line law, facets N/A [INV-28]. Success
measure: the day a newer pack ships, the next session on another machine proposes it unasked
[default]. [E-25]

## The rules and who applies them

The shared rulebook, who holds authority over what, and how the work scales down when money or time run short.

### One rulebook behind the skills  [not a scenario]

Open any skill in the pack and the same working rules greet the reader. Until now each skill carried its own near-copy of them.

Copies drift, and the pack's own sweep proved it twice: the anchor convention was told two ways across skills, and the concurrent-edit fence appeared only in the adoption text, though every skill that writes shared files needs it.

The five rules every skill works by are these:

- **Ask, never guess** — when a fact is missing, ask for it.
- **Plain words, with the code trailing quietly** at the end of the clause it anchors.
- **One surface, one name** — a thing is called the same everywhere it appears.
- **One canonical home per fact** — each fact is stated in a single place.
- **A junior resumes from a checkpoint** after a cut-off, picking the work back up.

**So the shared rules live once, in the base skill.** The base skill is the pack's shared rulebook, and it sits beside the working skills in the folder `live-spec-base`.

The package itself is the source; the standalone repos are read-only mirrors of it [D-4]. The base states each shared rule normatively, right next to the package's default settings [E-13].

Every working skill opens with one line. That line names the base skill and the base version the skill was written against. This version pin is swept in the same session that bumps the base, so it never goes stale. After that line, the skill references the shared rules instead of restating them.

A working skill elaborates only its own domain. The communicator skill, for example, teaches how to speak plainly. The rule that we speak plainly at all belongs to the base.

A skill used standalone, outside the pack, still stands on its own: the opening line reads as plain advice, and nothing in the skill's own domain needs the base to be installed [E-12].

As the pack evolves, one thing stays true. **A shared rule has exactly one normative home, the base skill. A second full statement of it inside a working skill is drift, a defect to fold back.** The compaction pass prunes restatements older than the base at milestones, one skill at a time, so no single risky rewrite is needed [M-1]. [INV-13]

**Every place the pack lists its skills names the same complete set.** That list lives in several reader-facing spots: the working-skills sentence up top, the closing lists the skills carry, and the README's table.

A list is exactly the kind of fact that drifts. The communicator's closing list was once found naming four skills after the pack had grown past six, with two skills missing since their birth. A check runs at every commit, and a list that misses a skill goes red [INV-66].

### Who decides what  [not a scenario]

#### Human authority and evidence

**The human owns taste, design, irreversible calls, publish and push gates, domain wording, and the human's own working contract.** [INV-9] [ACT-1] The settings ladder resolves to that contract, as described below.

- The human's personal profile holds the lines about the human — proactivity mode (ask-at-max | max-proactive), trust level, language, domain vocabulary — and follows the human everywhere.
- The **host profile**, at `.live-spec/profile.md`, narrows those lines for one project, when the human says so. It is created at attach and lives git-tracked in the host repo, like the adopt artifacts [A-8]. Inside `.live-spec/`, only the checkpoints stay ignored [ACT-3] [E-8].
- Communicator reads the resolved contract before every human-facing exchange; it resolves the whole ladder, never just one file [E-13].

**Mode and trust are written only on the human's word.** The agent may propose them; it never sets them, and never raises its own trust or proactivity level. [INV-9]

**A done-claim is answered by walking the evidence fresh each time, and it carries the method version it was done by.** A fluent story can answer any done-claim — "did that project run the tests by the method?" — and the story might even be right, but it does not distinguish verified from narrative, which is the whole point of the method.

So no one answers a done-claim from memory: every claim pins to a checkable artifact, walked now — an adoption record, a prover record, a suite run with its count, a git commit, a matrix row. This is the claims-need-primary-source rule, applied to the answering exchange itself.

The answer states plainly what the walk verified, apart from what it merely asserts, and it names the method version the work was done by — the pack and skill versions read from that host's installed set (the version homes, [M-7]).

One claim line reads claim → artifact → version, for example: "suite green — 795 tests, tonight's run, commit `193d39d` — done by live-spec 0.8.x, prover 0.1.8." If the host has no installed set (never adopted, or the work predates adoption), the answer says exactly that: an absent version is itself an honest answer, never an invented one. [INV-25]

#### Settings and the ladder

**Settings climb a ladder of four nested scopes, and the narrowest word wins.** Every way the pack behaves for the human is a named setting, and each setting has a home in exactly one scope, depending on what it describes:

- about the pack itself → the **package defaults**, each value stated in the base skill beside the rule it tunes [E-12];
- about the human, following the human across every project (language for docs/commits vs. conversation, proactivity mode, trust, the human's domain vocabulary) → the human's **personal profile**, one file per human at `~/.claude/live-spec/profile.md`;
- about this project → the **host profile** [E-8];
- about right now → the **session scope**, the human's live word in one conversation.

The scopes nest: the package holds every human, a personal profile holds every project that human touches, and a host holds every session run inside it.

A setting made at a broad scope is inherited down through the narrower ones, until a narrower one overrides it on the human's word — an all-English project overriding the human's Russian-chat line, or a "today, answer me in English" overriding both for one sitting. Resolution reads from the narrowest scope out: session beats host beats personal beats package default.

Profiles are re-read at the same freshness points as skills [A-7]. When a profile line falls outside the current pack's vocabulary (written under an older vocabulary), the pack ignores it aloud: a dated note in the host's journal, plus a line in the session's next report.

The journal half is durable, so a session that dies before its report still leaves the trace, never a silent drop, never an error. [E-13]

**No override is ever silent.** An override exists only as a written line in its profile file: setting one leaves a dated journal note in the home it governs — the host's journal for a host line, the package's journal for a default change. This is the no-silent-micro-decisions rule [INV-5], applied to settings.

Live-spec's own push gate [M-6] is the worked example: the package default asks for a full prover pass before a minor bump, and live-spec's own host contract tightens that to "before every push" — recorded, visible, never assumed.

The session scope is the one that's never a file. A session override lives only in the human's spoken word and dies with the conversation; the agent never writes it anywhere on its own.

If it should outlive the session, that's a promotion into the profile it describes (personal or host), made on the human's word and journaled like any other override. An announced self-compaction [M-2] carries the live session lines forward in its summary.

A full wipe ends the sitting, and the session lines die with it by design — that loss is the human's own move, never the agent's. [INV-14]

**The human's profile is the one home of the personal layer, and the global instruction file is a thin loader.** Everything personal — who the human is, how the human likes to be spoken to, the human's standing working rules — lives in the personal profile, gathered in one place.

The machine-global instruction file (on this stack, `~/.claude/CLAUDE.md`) shrinks to a thin loader: it points to the profile, and states only the bootstrap lines that must hold before any pack file loads. The which-project disambiguation rule is the type specimen — the rule that stops a session writing into a foreign repo can't itself wait for that repo's files to load. The loader is the one home for those bootstrap lines, and the profile never restates them. [INV-13]

Migrating an existing rule file into this shape is a fork by scope — each rule moves to the scope it describes:

- a method rule the pack already states stays the pack's (a second copy is drift [INV-13]);
- a personal line moves to the profile;
- a project line moves to that project's host profile.

A rule-by-rule mapping proves the move lossless, and the old file stays in the attic [INV-7], so one move rolls the whole change back. The fork writes only what the running session owns: pack rules land in the pack, and the personal profile lives on the human's machine, outside any host or pack repo — a private repo the human owns may serve as its git home.

Sitting outside any repo fence [INV-11], a promotion re-reads the file immediately before appending, and that git home is its recovery net. A project line becomes a written migration note, and the project's own session lands it at its next update — so nothing in this migration writes a foreign repo [INV-10]. [E-16]

#### Delegation and workers

**The senior agent owns judgment** — spec deltas, matrix levels, findings triage, this document. [ACT-2]

**Workers (tiered) own mechanical execution.** Each keeps a persistent checkpoint file in the host's `.live-spec/checkpoints/` (gitignored, never `/tmp`, since a reboot must not erase a resume point). Three tiers stand:

- a no-decision one-shot on **haiku**;
- multi-step mechanical work on **sonnet**;
- judgment on the **senior**.

The routing rule below decides which tier a unit of work is proposed at, before the senior may overrule it. [INV-69]

**The worker contract binds every delegation:**

- A worker inherits its session's write-ownership [INV-10], narrowed to the files its brief names. Outside those files it reads, and never writes.
- A brief may instead name an isolated copy of the tree, where a parallel lane builds its stages. That copy's delta reaches the shared tree only through the senior's integration, under the pen [T-18, INV-39].
- Files a same-session sibling worker just wrote are fence-benign: the concurrent-edit fence [INV-11] alarms on foreign sessions and stays quiet for the agent's own briefed hands. The senior who briefed both owns their seams.
- The session's live setting lines [E-13] ride into the brief verbatim. A worker never resolves the ladder itself — it cannot hear the human's spoken word.
- The brief arms the worker for the workshop: it carries the host's problem-ledger path with the watched-line duty. Any noise the worker hits goes into its checkpoint as a ledger line (signature, date, one line of context). The worker never silently retries. The senior carries those lines into the ledger at verify, unless the brief names the ledger among the worker's own files [INV-23].
- It carries the clock — the date and time read at briefing — so a worker's stamps come off the brief's clock, never invented. [INV-24]
- It touches its checkpoint file on a fixed interval (~60 s [default]) as a bare heartbeat, whatever else its work writes. A compute-bound run — a long render, a large test pass — can write no product file for minutes, and this heartbeat is what proves it still alive to the resume protocol's death check, so a busy worker is never mistaken for a dead one [INV-76].
- A result that fails its brief's acceptance escalates one tier with a logged line (haiku → sonnet → senior). It never retries silently on the same tier, and never skips a rung. [ACT-3]

**The routing rule proposes the cheapest tier that can pass the brief, and the senior may overrule it aloud.** Before anyone delegates a unit of work, they propose its tier (never default it), and the proposal reads what the work is, looking past the row's size alone.

- A judgment step — a spec delta, a prove pass, an architecture carve, the matrix's level calls, findings triage, any taste call — proposes the senior. That is ACT-2's own ground [ACT-2], and it never routes down.
- A mechanical step proposes a worker:
  - a no-decision one-shot (a grep, a dump, a known-string edit) → the **haiku** tier;
  - a self-contained multi-step brief (edits across named files, a pipeline run, tests written to a fixed matrix) → the **sonnet** tier.

The size class is only a coarse prior: a large row carries more delegable mechanical mass, a small one is often all-judgment, and the step inside it decides.

**The economy rung moves the threshold** [T-19]:

- at `full` the map stands as written;
- at `lean` an airtight brief rides one tier cheaper — a sonnet brief that leaves the worker nothing to decide may propose haiku, and the bar for keeping a step on the senior rises;
- at `tight` the proposal is always the cheapest sufficient tier, and the senior spends its hours on judgment alone.

**The proposal is advisory, the senior may override per wish, and the override is logged.** [D-2] A brief that looked mechanical but hides a real decision routes up; a rare over-cautious default routes down. Either way, one line rides the checkpoint and the landing report: proposed tier → chosen tier → why.

This assignment-time override is distinct from ACT-3's failed-acceptance escalation — one is the senior's choice before the work, the other a runtime bump after a miss. Both get logged, on different lines. A silent tier change is the defect this closes.

The router never hardens into a mechanical gate the senior cannot overrule, and it never touches the human's gates or ACT-2's ownership of judgment. No visible surface — facets N/A.

Non-goals:
- no token meters or numeric budgets (the rung stays qualitative [T-19]);
- no fourth tier and no renaming of the three;
- no auto-routing that overrides the senior's word.

Success measure [default]: the first routed landing names, in its report, the proposal → choice → why for each delegated unit, and the human checks it by reading it. [INV-69]

**The landed row's status cell carries its delegation accounting.** Every landed queue row records what its delegation was: the unit that went to a worker with a rough saving, or a stood-down line naming why the senior kept the work. The line lives in the landed row's status cell, and a suite check reads it: a landed row without the line goes red. The duty binds the orchestrator seat regardless of model, whatever tier leads the seat. It binds forward from its landing date, so a row landed 2026-07-12 or later carries the line while earlier rows stay as they landed. Prose alone did not hold this routing rule: the delegation report line already lived in the pipeline's text, yet a session could drop it unseen until the human asked what stops the glitch (2026-07-12). A forward-landed row never omits its delegation accounting. [INV-103]

**A worker's green gets a second pair of eyes, and verify can turn adversarial.** A worker's report is a lead, no more. It never counts as evidence. Whenever a single head both makes the work and judges it the blind spot is structural — the same head that wrote a brief reads the result, or the same session that authored a method law runs its own review of it — so "tasks completed, goal missed" can ship green.

So the verify step carries an adversarial option: a FRESH-context checker is briefed with the SPEC sentences the landing claims (the anchors) and the artifact paths, never the worker's summary, never the senior's plan. It opens on the hypothesis "tasks completed, goal missed" and walks each claimed fact up a fixed ladder:

- exists — the artifact is there;
- substantive — real content, checked against the pipeline's step 8 grep list (TODO / FIXME / placeholder / lorem / hardcoded sample / empty body);
- wired — reachable from the surface that claims it;
- flows — real values move end to end.

Findings become rows or red, never a nod. It fires mandatory when the change is high-stakes and its only review is the author's own. High-stakes means one of two things: the delta is surface-sized (a new surface or a multi-file behaviour change), or the change edits the method itself — a rule whose meaning changed, a new or re-scoped invariant (a wording-only edit that changes no rule's meaning is not a method edit). The author's own review means no independent read has happened, where an independent read is a differently-contexted head briefed from the primary sources on the "goal missed" hypothesis; a prover pass run in the author's own context never counts as one, and delegation never makes the review independent — the same head that briefed the worker reads the result. One fresh checker per landing batch covers every law in the batch [INV-61] — the batch rhythm scales the audit's form, never its freshness. Anywhere else it stays the senior's option. (Sharpened 2026-07-12: a self-built method law — the entry impact-analysis station [INV-128] — passed its author's own prover pass clean, and a fresh-context adversarial pass on the "goal missed" hypothesis caught a real contradiction with the door law [INV-16]; the audit that the old delegated-and-surface-sized trigger left optional is the one that caught the defect.)

A skill or prose landing walks the same ladder in its kind's form — the checker re-reads the shipped text against the spec sentences. The checker is a worker like any other — contract, checkpoint, ledger duty [ACT-3] — and its verdict rides the landing report. [INV-46]

**A brief is born from read files, never from memory of them.** Before writing a brief that edits existing files, the brief-writer reads in full every file the work will modify. The brief records three lines per file:

- current state;
- what changes;
- what must survive.

Every step carries a back-reference to the spec sentence it serves, and every technical claim in the brief cites its source — a file:line, a command's output. A brief written from memory hands the worker the senior's guess dressed up as fact. [INV-53]

**A worker stops only on a named condition.** The brief carries the halt list, closed and short:

- an ambiguous requirement;
- two consecutive unexplained failures of one command;
- a missing config or dependency;
- acceptance impossible as briefed.

On any of these the worker stops with evidence. Otherwise it runs to completion. This is sharper than "ask if unsure," and it composes with the one-tier escalation law [ACT-3]. [INV-54]

**A brief is sized to its worker's head.** A brief targets a bounded share of the worker's context, and the work splits above it. The default bound is concrete: the brief's own text stays within ~300 lines and names at most ~8 files to edit [default].

Above either limit, the work splits into staged briefs. A brief passes paths, never inlined file bodies — the worker reads its own truth from disk, and an inlined body goes stale the moment a sibling edits the file. [INV-55]

### When money or time run short (the economy ladder)  [not a scenario]

Rigor costs money and time: suite runs, prover passes, senior-model hours. Today the pack always spends full rigor. This section names what a tight budget may legally shed, so economy is a setting the human moved, never an improvisation under pressure. [T-19]

The pressure lives as one setting on the ladder: `budget.pressure`, with package default `full`. It moves only on the human's word: a session's word for today, or a profile line to stand. This works exactly like proactivity and trust [E-13, INV-9].

When the human names money or time pressure, the agent may propose a rung. The agent never sets one.

The pack surfaces the choice before pressure arrives. At a project's setup, whether founding or adoption, the pack asks the economy rung, or tells the standing default, alongside `project.kind` [INV-36]. The preference is the human's from day one.

Three rungs each name their legal sheds. Every shed the agent actually takes is said in the landing report. A silent economy is a silent micro-decision, and the landing report exists to prevent it [INV-5].

- **full [default]** — the full suite runs at every landing gate. The prover runs at its recorded cadence. The worker router picks tiers by the routing rule [INV-69].
- **lean** — mid-work test runs may scope to the touched architecture node's rows. The full suite still runs at every landing gate and before every push. Surface-add prover passes stay CROSS-LINK. A full pass owed by the default cadence may defer to the next milestone; the agent writes the deferral as a dated debt line in its queue row, never just from memory. Mechanical work rides one worker tier cheaper when the brief is airtight [INV-69].
- **tight** — everything lean, plus landing gates may batch: consecutive small landings share one full-suite run at the batch's end. Each landing commit still carries exactly one row's delta [INV-39]. A red at batch end bisects by landing order to name the culprit, then reverts the batch to its last green base and re-applies the clean landings, holding the culprit row out for its own fix — so HEAD never sits red across a breakpoint. Even so, a push still requires the batch's reach-scoped gate [INV-45] green at HEAD [M-6]. The cheapest sufficient worker tier is the rule, and senior hours go to judgment alone [INV-69].

What never bends at any rung — the never-bend list, stated once [INV-40]:

- the door law and its tripwires: poverty, like urgency, moves priority, never the door [T-12, INV-16];
- red-before-fix: a bug still gets its failing test before its fix;
- the human's gates: irreversible moves, publishing, authored content, taste [INV-9];
- the landing report, carrying its taken-defaults and its named sheds [INV-5, INV-31];
- landing purity: one row's delta per commit, whatever the batching [INV-39];
- the push gate: work leaves the machine at full rigor only. Every check the diff can reach is green at head, per the reach map [INV-45], plus the host's recorded prover cadence [M-6];
- the safety net that no work-kind and no scope-cut touches: poverty is its third non-toucher [T-15, T-16];
- narration: it is cheap and stays whole at every rung [INV-35].

An explicit host line outlives any rung. A host profile pinning a tighter cadence keeps it even under `tight` [E-13].

Non-goals: no numeric budgets or token meters, since the rung is qualitative and moves by the human's word; and no automatic rung-switching.

Success measure [default]: the first budget-named session names its rung and its sheds aloud in its landing report, checked by the human's read [T-19].

## What holds the bounds

The machinery that enforces the rules: the checks and gates, and the write-access rules on the package repo.

**Every process converges on its goal — always.** The owner's principle (2026-07-10): convergence covers every process and every kind of artifact; there is a goal, and the work walks toward it. Every piece of work names its goal up front as an artifact the work can be held against — a frozen norm, an exemplar bank, a failing test, a written acceptance. A paraphrase cannot serve as the goal. Every iteration measures its distance to the goal itself; a proxy never replaces the goal, and measuring against a proxy is where a look-alike is born. The distance only shrinks, and a reached level locks by a mechanism — a norm template, a conformance test, a lint floor that only grows, a cap that only ratchets down; the machines this section lists are the principle's hands, and the norm-conformance rows and the lock tests are its first teeth (rows 216/217). A deliberately divergent stretch — exploration, a labelled prototype — is legal only when named and bounded by its convergence point. The working statement for every skill lives in the base rulebook (rule 22); the principle's chapter lives in the private playbook. [INV-98]

**A behavioural rule that breaks mid-turn twice earns a live channel.** A standing behavioural rule keeps its normative home in a once-read file — the loader, a profile, a skill's text. When such a rule breaks mid-turn a second time despite that home, it earns a live channel that same moment: an every-prompt hook line that reminds at the decision point, or a mechanical after-the-fact check that turns the suite red. The pick is recorded where the rule lives. The once-read homes remain the rule's normative homes; the live channel only carries the rule to the moment it is needed. Prose in a once-read file loses to mid-turn momentum, and attention alone holds nothing across sessions. This is the convergence principle's hand for behaviour, kin of the problem-ledger's second-occurrence law: a thing that recurs twice gets a mechanism that moment, never a third suffering. The worked proof: the routing rule lived in once-read files since June and broke mid-turn until the every-prompt hook line and the mechanical after-the-fact check landed (rows 253/254, 2026-07-12), the same cure that killed invented clock stamps. The 1.1.0 audit's once-read walk is this law's first sweep. A rule's mid-turn breaks are recorded in one home — the problem ledger PROBLEMS.md — so this sweep reads one source; the live-channel landing (the ROADMAP row, the hook, the check) points back to that ledger entry rather than standing as a second break-record (the one-home principle, base rule 4). [INV-108]

### The machines that hold the bounds  [not a scenario]

What keeps "it works" honest — each one a named machine:

- **The matrix (TEST_MATRIX.md)**
  - Every fact gets at least one row, and each row is pinned to a test level [E-5].
  - Rows are organized by architecture node × spec fact, produced by the derivation method above [E-14, E-15].
  - Each row states both sides: what the fact does, and what it must never do. That negative side is the regression fence [INV-6].

- **The feature-coverage trace** — a second traceability layer above the matrix, keyed to the project's PRIMARY UNIT [E-29]. Every project declares its type once, and the type names the unit: a web or app product counts user-facing features, a CLI its commands, a package the guarantees it promises, a book its arguments. Each unit carries a stable inline tag on the heading where it lives, and one coverage table in ARCHITECTURE.md maps each unit to the node(s) that implement it and a test that exercises it. live-spec is a package, but its scenarios ARE its features, so each person-facing scenario heading tags itself `[feature: F-x]` and the table names its implementers and its test.
  - The check reads BOTH directions and fails the push either way [INV-73]: every tagged unit resolves to a real implementer node and a real test, and every scenario the pack promises carries its tag — a scenario added without one, or a tag dropped, goes red.
  - **The reverse direction has teeth through a heading convention.** For the check to catch a scenario whose tag was forgotten, an untagged heading must be unambiguous, and it is not on its own — the checker cannot tell a new scenario missing its tag from a machinery, rules, or reference section that never had one. So every H3 heading in this spec carries either its `[feature: F-x]` tag, marking it a person-facing scenario the coverage table maps, or the explicit `[not a scenario]` marker, marking it a section that states machinery, a rule, or reference and is legitimately untagged. An H3 that carries neither is unambiguously red — a forgotten scenario tag can no longer ship uncovered, and a new machinery section states its marker rather than passing silently. The convention lives on H3 headings, the level every scenario uses; its sub-parts nest under a heading already tagged or marked. This makes the reverse direction of the two-way check mechanical rather than a hand-walk, and its home beside the tag law is the spec-author skill. [INV-132]
  - The machines that work behind the scenes — the guardrails, the host contract, the settings ladder — implement guarantees rather than user-facing features, and sit outside this layer by the project type's own definition of its unit.
  - The mechanism reuses the anchor-ownership machinery a level up rather than adding a new one; the format's authoring home is the spec-author skill.

- **The guardrails** — mechanical checks, wired to the pre-push hook [E-6]. They run live today for the pack repo itself. Each push must show:
  - a today-dated prover record exists
  - the suite runs green — the run scopes to the diff's reach, so a prose-only diff stands the suite down by name, and everything else runs it whole [INV-45]
  - every anchor owned by exactly one node
  - no unchecked matrix-coverage box
  - the prototype fence: no prod file references into a prototype home [E-17, INV-17]
  - the opt-in concurrent-edit fence on commit

  Still [target]: the host-facing set — completeness against the surface registry, tests-present, behaviour-traces-to-spec, and declared-scope diff vs snapshot. On a host, hooks are offered, never imposed: they install only where the host uses git, and only after asking the human in plain words, since the human may not know what a git hook is.

- **The snapshot [target: the machine; the design is decided]** — the saved artifact of the last accepted run: HTML, JSON, files, numbers. The next run diffs against it as the baseline [E-7].
  - Lives in `.live-spec/snapshot/`: one folder per declared surface, plus one manifest line per surface recording what it is, the landing that set it (row, date), and a content hash — the attic manifest's sibling.
  - The baseline only advances at *landed*, and only for the surfaces the change declared; undeclared surfaces keep their old baseline. That asymmetry catches the unasked change: the guardrails' declared-scope check [E-6] goes red when a rendered surface differs from its baseline but the landing never declared it.
  - Adoption saves the first baseline from the artifacts as found [A-6]. The working tree keeps only the last baseline; git history is the archive. The snapshot folder is git-tracked, and of `.live-spec/` only the checkpoints stay ignored [E-8], so any older baseline can be checked out.
  - A too-heavy surface keeps only its manifest line and hash in git; the bytes live outside, and only the hash gets diffed.

  The machine's design is decided; it stays [target] until its first mechanical slice lands, riding the guardrails scaffold.

- **Design-sync [target: the machine; the wiring is live]** — an optional machine for hosts with visual components [E-18]. It syncs the components a landing declared — the same declared-scope notion the snapshot diffs by [E-7] — to the team's design project (claude.ai/design), where the human reviews rendered cards. It supplements the in-session render: the real render stays the authority for the landing gate; the design project is just the team-review channel.
  - Wired today (row 93's pack-side half): the switch lives off-by-default in the base skill's defaults table [E-13], under the name `design-sync`. A host that turns it on writes a recorded profile line [INV-14], and the channel lines stand in communicator and in the pipeline's commit-and-show step.
  - Still [target]: the machine itself — the first real sync on a visual host closes row 93.

  Every sync is gated by the human, because a sync publishes outside the machine [ACT-1]. The pack itself, a text product, never syncs — the work-kind axis says so mechanically [T-16]: the machine applies to product-kind work on a visual host, and every other kind stands it down by name [INV-22].

- **The skill evals** — test the pack's own skills at the level that matters for a skill: behaviour [E-19].
  - Each working skill owns at least one recorded eval: a scenario where a bare session errs and the skill's text fixes it — the skill's own red-first test, proven red at authoring with a dated run record.
  - Evals live in `evals/` in the pack repo, one file per skill: the scenario prompt, the recorded bare failure (date + run record), what a with-skill run must show, and the checks a re-run walks.
  - Evals re-run at milestones (the M-1 list carries the item) and at any landing that changes a skill's own behaviour; a bump that only sweeps a pin or version line owes no re-run.
  - A working skill without its eval is a defect the milestone audit flags.

- **The surface registry [target]** — one named list per host of every user-facing surface.
  - The preferred form is executable [E-10]: the list lives as a declared map inside a completeness-gate test, so a mismatch is a failing test in both directions — rendered-but-unregistered, and registered-but-empty.
  - The `.md` file stays the honest fallback for a host with no test harness.
  - When a real host arrives with the executable form already working, adoption recognizes it rather than asking it to step back into a document.
  - The completeness check scans the real rendered artifact against the list, so a surface that renders but isn't registered goes red — the registry is self-closing.

#### The push gate's reach and its blocking contract

- **The gate's thoroughness comes from reach.** "Run everything before any push" sounds rigorous but double-misses: a prose-only push pays for behavioural tests that never read a single changed line, while the checks a prose diff can actually break never run at all. Understand what changed to know what to test, and build the dependency graph a little conservatively.

- So the push gate derives its check-set from a declared reach map — which checks read which file classes — mechanically, from the diff's file list, never self-judged. Three teeth keep it honest:
  - the map is explicit: a named file in guardrails/, with patterns a human can read;
  - it is conservative: an unmapped or new file triggers the full suite, and fast paths exist only for explicitly claimed prose classes — "just .md" isn't a class, since SPEC, matrix, architecture, queue, and every SKILL.md are tested documents and stay full-reach;
  - it is self-tested: the deciding script is red-proven on fixtures, and anything it can't classify falls to full.

  The cheap gates (prover record, ownership, coverage, loadability, prototype fence) never scope; they run at every push. "Full rigor" [INV-40] means every check the diff can reach, green [INV-45].

- **A gate that blocks speaks one language.** Today each gate script fails in its own words: an agent has to parse prose, a human has to hunt for the fix. Every blocking gate, on red, emits one typed failure line — a parseable JSON object `{severity, code, message, fix}` — beside its human-readable lines. The `fix` field is the same sentence a person reads.
  - Every check declares itself blocking or advisory. An advisory check prints its finding and never flips the exit code.
  - A script that rebuilds artifacts validates every output before it writes any, so no half-written artifact lands on disk.
  - The contract's operational home is the guardrails README. It binds by deed: the first gate ships under it now, and each other gate picks it up the next time someone touches it, never all at once [INV-47].

- **The four project-side checks are code a host attaches, never prose it re-implements.** The pack ships, under `scaffold/guardrails/`, a generic runnable form of the four checks the pipeline's teeth name — completeness, tests-present, behaviour-traces-to-spec, conflicts — parametrized by one host config file, never by editing check code. The config declares the host's real shape: document paths (spec, matrix, queue), the tests directory, the user-facing source globs, the surface registry's path, and — where a check needs the artifact itself — the host's own render command. Each check reads the config and the tree, exits green or red, and on red emits the typed failure line beside its human sentence [INV-47]. Failure behaviour is honest by construction: a missing config is red with an attach-me line, never a silent pass; a config pointing at a path that does not exist is red; a host that genuinely lacks a check's precondition (no render command yet) declares the waiver IN the config, where a reader sees it — an undeclared gap never passes quietly. Attachment is the adopt walk's step: the checks wire into the host's pre-push hook beside its suite, and the pack repo itself attaches them as the first host — proof by its own gates. Acceptance for a new host is measured: attach by config alone in about fifteen minutes [default], and each check proves itself red-first on one planted defect before it counts as attached. Non-goals, stated where they bind: the checks catch structural defects only — a semantic bug stays the prover's and the human's [E-6]; the registry's content stays the host's authorship, never auto-generated [E-10]. (Raised by the web session's read, 2026-07-10 — the curator gap the README now names; this contract's code landing retires it.) [INV-97]

### The package repo: who may write, and two sessions at once  [not a scenario]

live-spec runs on its own method: this spec, this queue, and these rules govern live-spec's own development.

The pack repo's push gates run mechanically on installed hooks — a fresh prover record, a green suite, anchor ownership, and matrix coverage, all under `guardrails/`. The host-facing checks stay [target] with E-6. [M-4] That makes its repo a shared surface.

**The developer's own machine keeps its skills fresh by a named step, run deliberately.** The repo is the source [D-4]. The installed copies under the agent's skills home are mirrors.

A session that edits a skill syncs the installed copy the same session, through the named tool `scripts/sync-skills.sh`. That tool copies each repo skill over its installed twin, and it reports every version change old → new — the exact line A-7's re-read rule fires on.

A hand-copy is the anti-pattern the tool retires: it syncs silently, so nothing tells the next breakpoint what changed. [E-23]

**Only a session assigned to live-spec itself writes this repo** (spec, queue, journal, skills, templates, adopt procedure). Every other session is read-only here — a host adopt run, a skill install, anything that merely reads the package. It has exactly one exception: creating a new wish file in the inbox.

The test is crisp. If the session cannot say "the human asked me, in this conversation, or via a standing routine the human created for live-spec, to change live-spec", it does not write. A host run's story lives in the host's journal, never here. [INV-10]

**The inbox (inbox/)** is the parallel-safe intake door for wishes and feedback born outside a live-spec session. Each item arrives as one new file, named `YYYY-MM-DD-<source>-<slug>.md`.

If the name is taken, append `-2`, `-3`, and so on — the same one collision law, base rule 18. When two sessions race one slug, they add a short session token to the source mark — a short projection of the session's stable identity [INV-117], never a second identity scheme. A file holds a few plain lines, and it never edits an existing file: creating a fresh file cannot collide, while shared files can.

The outsider commits its one new file — a commit touching inbox/ only, its message naming the source. That commit is inside the read-only exception.

**The inbox has a remote arm.** A shared filesystem is not the only way in. A remote seat is a cloud session, a scheduled routine, or another machine. A remote seat reaches a repo only through git. Its deposit stays one new file in inbox/, committed touching inbox/ only with the source named in the message, and then pushed. The push runs under a per-repo grant: the owner links the Claude environment to the GitHub account once, and grants each repo to the app once, and the grant is recorded in the host profile like the push grant [INV-82]. The deposit composes with the peer fence by its shape: a remote seat cannot see which sessions are live, and one fresh inbox/ file is the fence's expected benign case [INV-11]. The live-session stand-down [INV-82] holds no bar over the deposit either: the one new inbox/ file is additive and races nothing, so the deposit push proceeds, while any push beyond that one file still stands down. A push the remote rejects retries after a pull, and the deposit never edits an existing file. A seat with no grant fails honestly. It names the grant it lacks and hands the owner the one action that supplies it, the same honest failure as a window that never opened [INV-67]; it never fails silently and never guesses a workaround. (Born of the owner thinking the cloud seat through mid-session, 2026-07-10: today's inbox law assumed a shared filesystem, and a live routine alert was the first seat to hit the gap.) [INV-112]

The door is host-general: every host carries its own inbox/ under the same law, swept first by that host's own sessions. That is what keeps "no wish is ever lost" [INV-1] true when two contributors' sessions share one host. [E-11]

A live-spec session sweeps the inbox as its first act. It harvests each file into the home its route owns — a wish file into a queue row as always, a feedback file by the routing law [T-20]. An item must never sit durably-recorded but operationally invisible.

The harvest commit removes the file; git history keeps it, and this internal removal is not an attic case, which protects host files. Each harvest is one commit that both lands the route — the row, the ledger line — and removes its file. The landing names the source file.

So an interrupted harvest commits nothing and leaves the file untouched for the next sweep, which harvests it exactly once. A committed harvest leaves no file behind to re-harvest. So "spoken means it exists" holds without the outside session touching the queue. [T-10]

**Before writing to a repo — and again before every commit** — the agent re-checks `git status` and HEAD against what it last read. Suppose HEAD moved, or the tree holds changes it did not make. Then it must stop, re-read the changed files, and only then proceed surgically — or back off to the inbox.

New files under inbox/ are the expected benign case; the fence stays clear for them. The agent never pushes while another session is known to be live in the repo; push coordination belongs to the human. This applies to live-spec and to any host repo two sessions might share — the concurrency axis of the composition rule, made mechanical. [INV-11]

**One canonical state directory, and worktree isolation by default where lanes overlap.** The host keeps one state directory, and the canonical state directory is named `.live-spec`, once. It holds the host's records, its checkpoints, and its adopt working artifacts, and no second directory competes for that role. A near-miss directory found at attach or resume is a red finding: `.livespec`, `.live_spec`, a bare `livespec/`, any look-alike carrying a rival profile beside the real one. The adoption sweep retires it to the attic under a manifest line naming the path, the reason, and the canonical directory that absorbs it [INV-7]. Never a look-alike left standing beside `.live-spec`, never two directories each claiming to be the host's records. For concurrent work the fence gains its own rule: worktree isolation is the default when two lanes' write-sets overlap, so the later lane builds in its own isolated copy of the tree and that copy reaches the shared tree only through integration under the pen [INV-11, T-18, INV-39]. Never a second lane writing a shared file the first lane still holds open. (Born of the audit's ghost `.livespec` dir, found beside the real `.live-spec` with a different profile, 2026-07-10.) [INV-105]

## Reference

Supporting material: how the axes compose, the open questions still on the table, and the index of every short code.

### Composing across axes  [not a scenario]

Some parts of a host project hold state: a screen, a panel, a saved file — anything the user can change and find again later. Call each of these a **stateful surface**.

Review every stateful surface from a fixed list of angles, called axes. Each axis is one question about the surface's behavior:

- in each view
- in each mode
- at each user tier
- at each viewport size
- when it is closed and reopened
- concurrency, wherever two writers can genuinely act on the surface at once
- alongside every other surface that can be present at the same time, whether or not that other surface holds state — a sibling sharing the screen, or a surface the flow reaches just before or after this one (a static end screen counts)

A surface's spec is complete once every axis on the list has an answer.

**The axis authors forget is the last one: every other live surface.** A surface holding state rarely lives alone. Others share its screen, and the flow reaches it with a surface still showing from the step before. For each such neighbour, say what this surface does while that one is present — does it hold, clear, or hand off? The seam nobody writes is the classic stranding bug: a caption still naming the previous photo once the closing screen arrives, because "what the caption shows when the finale is in view" was never written as a sentence.

**The prover hunts the seam the author never wrote.** The prover reads the whole axis list [C-1] actively, deriving each surface's reachable situations for itself rather than trusting the author to have filled every one. For a stateful surface it walks every axis: the views, modes, and tiers; the viewport shapes and reopens it passes through while already shown; and — the axis authors forget most — every other surface that can be present at the same time, siblings on its screen and the surfaces one step before and after it in the flow. For each situation it asks one question: is this surface's behavior stated there? A reachable situation with a blank answer is a finding, of the same class as a fact no node owns [E-14]; a state the spec leaves out while the running product still reaches it is the exact hole. The hunt rides both the whole-spec pass and the surface-add pass [M-6]. It reports the missing seam and leaves the sentence to the author, who writes it as a composition invariant [C-1], decided or `[default]`-tagged the same way the facet sweep tags its own [INV-18, INV-31]; the prover invents no answer and asks the human for nothing. [INV-72]

**A cross-surface policy is stated at the surface-class level and held uniform across its siblings.** When a decision governs a KIND that recurs across several sibling surfaces or elements — a gesture policy (browser pinch-zoom refused), an affordance (a long-press reveals the gracious line), an input-to-action mapping (a single input steps exactly one frame), a state transition that repeats (the same open and close animation on every card), or a feature and its repeated element shared across places (a filter, a caption, a control that looks and behaves alike everywhere it appears) — the spec states it once at the surface-class level: the clause names the class and enumerates the surfaces it governs, rather than writing the policy for the single surface where the decision was born. Consistency of this kind is itself an invariant — the behaviour, transition, or element that must hold the same across a class of similar surfaces. A policy written for one surface while siblings of the same kind exist is a spec defect. The prover carries the check, writing itself the station his steer asked for: for each interaction policy it enumerates the surfaces of that kind from the surface registry [E-10] and flags any the clause does not cover, the same finding class as a reachable situation with a blank answer [INV-72]. For a product with a DOM the completeness guardrail family holds it mechanically: a policy asserted for one surface root is asserted across every registered sibling root, red until all are covered, so the non-uniformity goes red the day the single-surface fix lands rather than surfacing under a human's thumb on a real device [INV-97]. The spec-class rule is the root, moving the catch upstream of code; the guardrail is the mechanical floor a rendered product instantiates (this pack, a skill with no DOM, ships the rule and the prover lens and leaves the DOM-wide assertion to the products it serves). This is the preventive twin of the class hunt [INV-124]: the class hunt sweeps the siblings once a bug is confirmed, this holds the policy uniform before a bug is ever filed. (Born of tlvphotos's pinch-zoom policy shipped for the walk alone while the door, the series side-room, and the polaroid table kept the browser default — every test green because the suite asserted the one surface the clause named, the gap found only when the owner pinched each surface by hand on a real phone, 2026-07-12.) [INV-125]

**Both directions of a paired state change get the same craft, or a stated reason they do not.** When a surface has a pair of opposite state changes — open and close, enter and exit, expand and collapse, show and hide — a transition crafted for one direction is a decision about the pair, so the other direction is stated too. The default is symmetry: the exit mirrors the enter's feel unless a reason is written. A shorter exit or a deliberately instant one is a valid answer, and it is a stated, decided answer rather than a silence. This rides the standard-facet sweep as its own facet [INV-18], where the author writes the pair's answer as a spec sentence — mirror, a named shorter exit, or deliberately instant — decided or `[default]`-tagged like any facet [INV-31]. Motion feel is the human's own gate [INV-30], so where the author cannot judge the pair the question is surfaced to the human rather than shipping a crafted-in and instant-out pair silently. The prover carries the check: a paired state change with one direction's transition described and the opposite direction unstated is a finding, the same blank-answer class as an unwritten seam [INV-72]. This is the temporal twin of cross-surface uniformity [INV-125] — that holds a policy the same across sibling surfaces in space, this holds a transition the same across the two directions of one paired change in time; both catch a decision made for one member of a pair and silently not carried to the other. (Born of tlvphotos's polaroid side-room revealed under a soft black veil in one breath and closed on a hard cut with no transition at all, the asymmetry nobody decided on purpose, found only by the owner feeling it on a real phone, 2026-07-12.) [INV-126]

**Each scenario states how it is entered and how it exits.** A person-facing scenario is a flow, and a flow has edges: it is entered from somewhere with something already true, and it exits to somewhere leaving something behind. The scenario states both — its entry (from where the walk arrives and what must already hold: the prior scenario or state that leads in, the preconditions the walk assumes) and its exit (to where the person lands and what it leaves true: the postcondition the next scenario inherits). This lifts the per-operation precondition and postcondition lenses to the SCENARIO level, kin of the entry-symmetry lens [INV-50] that asks a conditionally-entered face for its re-entry path and the runtime view's flow walks [INV-74] that trace a flow through the nodes. The prover carries the scenario-level lens: a flow whose entry or exit is unstated is a finding, the same blank-answer class as an unwritten seam [INV-72]. The duty binds forward [INV-15] — a new scenario states its edges from the first draft, and the prover flags an existing scenario's unstated edge as a finding rather than blocking the lane. An entry or exit that is trivially none — a top-level scenario entered from nowhere, a terminal scenario exiting to nowhere — is stated as such in one short clause, so a reader tells a decided edge from an overlooked one. (recorded 2026-07-09: the prover should say, where needed, which preconditions and postconditions hold — how a scenario is ENTERED, how it is EXITED — deferred as a large theme and revived at the next prover-method landing.) [INV-127]

#### Document provenance (the adoption axis)

Adoption adds one axis: **document provenance** — where a spec claim came from.

- A claim is *native* when it was written fresh under live-spec. It is trusted from the start [C-1].
- A claim is *re-engineered* when it was recovered from documents the project had before adoption. It starts unverified and stays unverified until it is reconciled under the adoption rules, which pin it to real code or remove it [A-3].
### Open decisions  [not a scenario]

- ⟨DECIDE⟩ attic/ layout: flat with a manifest and source-dir prefix on collision (current pick) vs dated
  subfolders — revisit at the next real adopt run. [D-1]
- ⟨DECIDE⟩ pair queues: one reading view stitched across the pair's two queues, or strictly two? The queues
  stay per-repo either way; recommended — two plain queues, no stitched view until real friction (flipping
  between two windows to follow one wish's halves) earns it. [D-6]
- ⟨DECIDE⟩ pair specs: may the instance's spec cite engine facts, or only the content contract? Recommended —
  the instance cites the engine's contract entries by their handle and nothing deeper: an entry is the
  engine's versioned public promise, an internal rots at the engine's next refactor. [D-7]
Resolved decisions stay here as one-line pointers so their anchors keep a live home; the full dated
rationale moved to JOURNAL.md.

- Decided 2026-07-07 (row 56): the model tier is proposed, never mechanically fixed — the routing rule
  reads the work's step, kind, and the economy rung, and the senior may override per wish, logged. Home:
  the delegation scenario [INV-69]. [D-2]
- Decided 2026-07-07 (row 55): snapshot retention is last-only in the working tree, git history the
  archive; a heavy surface keeps only its hash. Home: the snapshot machine [E-7]. [D-3]
- Decided 2026-07-05: the pack structure is package-is-source — the pack repo is the single truth and the
  standalone repos are read-only mirrors. Execution: queue row 51. [D-4]
- Decided 2026-07-05: the personal-settings split is all-into-profile — every personal setting climbs the
  nested scopes and CLAUDE.md shrinks to a thin loader. Home: the settings-ladder and thin-loader
  paragraphs [E-13, E-16]; the onboarding step is row 54. [D-5]

### Formal index  [not a scenario]

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
| E-25 | pack update check: once a day (dated stamp) the first freshness point asks the public repo's VERSION; newer remote ⇒ a spoken proposal (versions, what-changed pointer, the install.sh/pull road) — install stays manual; offline ⇒ one honest skip line, stamp unwritten; no daemon | Adoption |
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
| INV-99 | every skill-kind landing's verify walks the installed skill-creator's review of the touched skill (format, frontmatter, description-triggering — does the skill load when it should; evals where applicable), findings folded or rejected by name in the landing record; the work-kind classifier is the trigger, never mood; the milestone gate's whole-pack walk [M-1] is the catch-up for skills landed before the law | Throwing a wish |
| INV-101 | the spec names its cross-cutting laws in one declared-laws home (measurement, accessibility, error handling, register — what the product declares); every new surface's section states its line against each declared law (the clause or a dated exemption) before the prover reads it; the prover's station: per declared law, enumerate every surface and transition, demand the clause or dated exemption per item — a missing clause ranks as a broken invariant; the pack's own list: register + clock-honesty + no-self-certification, two dated exemptions | Throwing a wish |
| INV-104 | the bug door and the skip door carry one added door-step tripwire: does this edit touch a spec-backed literal or clause (version string, pinned count, named vocabulary, promised wording)? a yes binds the docs-travel-with-the-change rule and the red-first small-fix path into one duty — the docs and the test land in the same session as the fix; the tripwire reads the edit's content, so a one-word change to a spec-cited literal owes the same duty as a full feature; born of the row 220 audit (one-line fixes touching spec-backed literals shipped without same-session doc sync, 2026-07-10) | Throwing a wish |
| INV-128 | every request enters through a three-source impact read beside the door [T-12] and work-kind [T-16]: the FOOTPRINT is read from the spec (what behaviour changes), the architecture (which module owns it), and the code (what gets touched) at one intake moment, producing one named footprint — presentation-only · single-module · cross-cutting — spoken in the capture echo and written in the row's `footprint:` note beside door/kind/map [INV-43, INV-108]; the footprint decides the route (presentation → light road; single-module → the matrix step against the module's interface; cross-cutting → the full pipeline), weight matched to reach, the footprint not the size picking the road; the read names any source disagreement as a finding routed to its owner (bug row / spec fix / restructure row [INV-37]) rather than silently trusting one source — pulling the architecture step's spec-to-code reconciliation forward to entry; the three-source read is the verdict derive-before-fork [INV-121] rests on (only the genuinely-open fork reaches the human); the footprint re-classifies mid-work when an edit reaches past its layer (mirroring the door re-fire), the landing report recording held-or-reclassified; the station carries the boundary-health law — a right boundary keeps a typical request in one module, repeated cross-cuts on the same module pair being the signal to move a boundary (only through the architecture step's re-prove [INV-37], on the recorded-footprint evidence not a hunch); recorded live 2026-07-12, the entry station (P1-P6) of the fourteen-principle architect draft, deeper mechanical enforcement on the follow-on rows | Throwing a wish |
| INV-129 | deferred rows are revisited at every queue-take, not only at milestones: a deferred row's revisit trigger [T-8] can be time-bound (before the next release, when the campaign ships) and so come true and lapse between two milestone gates, making the milestone re-scan [M-1] too rare a reader; at every queue-take the session also re-scans each deferred row's trigger against the current moment, a fired trigger returning its row to the runnable head [INV-49] right then; the two cadences read the same triggers by the same rule so a deferred wish never waits on a trigger nobody reads [INV-1] whichever cadence comes first, and the trigger vocabulary stays free-form since a reader now runs at queue cadence; homes — the queue-take clause + build-pipeline's queue-take walk; prover finding F3, 2026-07-12 | Throwing a wish |
| INV-130 | a withdrawn decision converges: after two withdrawals the recommended option is taken as a surfaced `[default]`; an answered question closes forever [INV-59] but a withdrawal re-asks in plainer terms with no cap of its own [INV-9], so a genuine taste call could loop unbounded — the bound is two, and on the second withdrawal of the same decision the session takes the recommended option and surfaces it as a `[default]` in the landing report, silence staying consent from there and it never re-asked [INV-31], the same convergence an answered question already has now given to the withdrawal path; a later real change of mind rides the ordinary channel as a new wish, never a reopening of the closed decision; homes — the decision-page clause + communicator's rule 10; prover finding F6, 2026-07-12 | Throwing a wish |
| INV-131 | a mid-work re-door [INV-16] rebuilds the parallel-lanes independence graph: when the re-door creates a surface or state that did not exist when the lanes opened, the same re-check re-runs the independence edges [INV-49] against every rolling lane, since the new surface can now collide with a sibling that was independent a moment ago; a new edge pulls the re-doored lane back to serial (it waits behind the lane it now shares a surface with) and the departures board says so in a line, so the board never asserts a stale independence after the ground moved; the integration re-fence [INV-39] still catches the collision at landing, so this closes the observability gap the board owed rather than adding a safety net — the board tells the truth the moment the edge appears, not only when two landings collide; the senior still judges independence and says it aloud, the re-door being the moment that judgement is owed again; homes — the mid-work re-door clause + build-pipeline's door re-fire; prover finding F7, 2026-07-12 | Throwing a wish |
| INV-133 | a critical non-bug heads the queue but never preempts a rolling lane, and the bound is echoed back at intake: "critical" is defined in bug terms but liftable onto any door [T-11], so a critical non-bug could head the queue and then wait for the current lane while a human who said "critical" for a live break expected bug-like preemption; preemption belongs to the bug door alone [T-9], so a critical non-bug lands as soon as the current lane reaches its checkpoint (ahead of everything else waiting) but never stops the rolling lane — a genuine live break that must stop the work now is a bug; the capture echo [INV-27] says the bound back when a wish is marked critical on a non-bug door (it heads the queue, does not stop the lane, only the bug door preempts), so the human hears the difference and can re-door it a bug rather than discovering at the next report that the work kept running; the human's word still owns priority [INV-9], the clause stating what critical buys on each door and never refusing the mark; homes — the priority clause + communicator's capture echo; prover finding F5, 2026-07-12 | Throwing a wish |
| INV-132 | the reverse direction of the feature-coverage check [INV-73] has teeth through a heading convention: every H3 heading carries either its `[feature: F-x]` tag (a person-facing scenario the coverage table maps [E-29]) or the explicit `[not a scenario]` marker (a machinery, rules, or reference section legitimately untagged), and an H3 carrying neither is unambiguously red — the checker could not otherwise tell a scenario whose tag was forgotten from a section that never had one, so an untagged scenario could ship green and uncovered; the convention lives on H3 headings (the level every scenario uses, sub-parts nesting under an already-tagged-or-marked heading), making the reverse direction mechanical rather than a hand-walk; homes — this feature-coverage clause + spec-author; prover finding F4, 2026-07-12 | Machines |
| INV-134 | a landed feature-or-refactor row carries its `footprint:` note (presentation-only · single-module · cross-cutting [INV-128]) and a suite check reads the queue (ROADMAP.md), reddening a landed feature-or-refactor row that omits the note — the mechanical floor under the footprint read, the same shape the delegation-accounting check [INV-103] gives the routing rule; binds forward from the footprint read's own landing (2026-07-12, the impact-analysis station [INV-128]), earlier rows staying as they landed; homes — this enforcement clause + the ROADMAP row template's footprint field + the footprint-note suite check; the mechanical follow-on INV-128 deferred, row 291 | Throwing a wish |
| INV-135 | the process stations are kind-abstract, and a project's founding declares its concrete layers and its concrete proof kinds: the entry impact read, the footprint categories [INV-128], and the test ladder are stations the pack states once, each project kind filling them with its own decomposition — the three footprints hold past code but the layers and proofs are the project's own; `project.kind` [INV-36] recorded at founding gains two companion lines in the host profile, `project.layers` (the concrete footprint categories) and `project.proofs` (the concrete test-ladder rungs); a founding check reds a kind recorded with no declared layers and no declared proofs, flagged at adoption like an unbacked surface [A-10]; the per-kind fill is the project's own ratchet — the footprint check [INV-134] and the test-level rule read the declared categories, not a hardcoded code list; ARCHITECTURE.md carries the per-kind footprint-and-proof table, spec-author and test-author reading the declared layers and proofs instead of assuming code; homes — base rule 24 + this founding clause + the host-profile founding record + the ARCHITECTURE per-kind table + spec-author/test-author + the founding check; P0k of the fourteen-principle architect draft, row 292 | Throwing a wish |
| INV-105 | one canonical state directory named `.live-spec`, stated once and no second directory competing; a near-miss directory (`.livespec`, `.live_spec`, `livespec/`) found at attach or resume is a red finding retired to the attic under a manifest line [INV-7]; worktree isolation is the default when two concurrent lanes' write-sets overlap, the later lane building in its own isolated copy and integrating under the pen [INV-11, T-18, INV-39]; born of the audit's ghost `.livespec` dir found beside the real `.live-spec` with a different profile (2026-07-10) | Package repo |
| INV-106 | the push walk does not end at the push: the pushing session reads the remote gate's own verdict (the CI run the push triggered, one `gh run` read, minutes, no human wait); a red verdict is the session's own immediate bug, preempting by the bug lane [INV-2], fixed and re-pushed the same session, so the human never meets the red first in a GitHub email; a slow gate is watched to its verdict on the detached-work cadence [INV-35]; born of the owner's word (2026-07-10 ~11:00) | Rhythm |
| T-17 | one wish = one user story: multi-story wishes split at intake, each story its own row; sub-behaviours are acceptance, folded into that same row; unclear count asked | Throwing a wish |
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
| INV-112 | the inbox door's remote arm: a seat that reaches a repo only through git deposits one new file in inbox/, commits it touching inbox/ only with the source named, and pushes it, under a per-repo grant recorded in the host profile like the push grant [INV-82] (the owner links the Claude environment to GitHub once, grants each repo once); the deposit push is exempt from the live-session stand-down [INV-82] by its additive one-file shape, anything beyond the one file still standing down; a seat with no grant fails honestly — it names the grant it lacks and hands the owner the one action, the honest failure of a window that never opened [INV-67], never silent, never a guessed workaround; born of the owner thinking the cloud seat through (2026-07-10) | Package repo |
| INV-12 | ambiguous size/priority/work-kind is asked at intake, never guessed | Throwing a wish |
| INV-13 | one normative home per shared rule: the base skill | One rulebook |
| INV-14 | no silent override; every profile line recorded + journaled | Who decides what |
| INV-15 | no landing without an owning node + a right-level matrix row | From spec to tests |
| INV-16 | feature tripwires are mechanical, fixed rules; casual asks still route | Throwing a wish |
| INV-17 | prototype fence one-way; build⊆spec honesty (fence live, other legs [target]) | A prototype stays a sketch |
| INV-18 | every facet ends as a spec sentence — decided, or `[default]`-tagged + reported | Throwing a wish |
| INV-19 | a fence cites its clause and discharges through that clause's existing never-side; fences named by anchor in the wish's row | Throwing a wish |
| INV-20 | the non-goals sentence is always written ("nothing left out" is valid); scope-narrowing non-goals ride the batched report | Throwing a wish |
| INV-21 | every feature states one success measure, decided or `[default]`-tagged (provenance only, no row yet); reading machinery [target]; binds forward | Throwing a wish |
| INV-22 | kind scales each step's FORM; a step applies or stands down BY NAME in the landing report — always named explicitly; the safety net is kind-proof | Throwing a wish |
| INV-23 | workshop noise: first sight = WATCHED line (never a silent retry); second occurrence gets an owner that moment (row, or the human's agreed non-problem); a third unowned recurrence is a METHOD defect → the pack's queue | Workshop misbehaves |
| INV-24 | time read off the clock, never invented: no future-dated file name, journal heading, or ledger date (suite fence) AND no added line pairing today's date with a time past the commit clock (pre-commit fence) AND the chat face: a human-facing timestamp read at write time, never extrapolated (law in communicator, no mechanical fence) — plus the chat face's mechanical hand, a prompt hook injecting the wall clock into every prompt (per-machine install, `scripts/clock-hook.sh`); quoting a past wrong date or time stays legal | Rhythm |
| INV-25 | a done-claim is an evidence walk: claim → artifact → method version, walked now; verified vs asserted said apart | Who decides what |
| INV-26 | a row closes only whole: per-leg Done-when, no close with an unmet leg; LIVE-STATE supersession never compresses an open leg away | Throwing a wish |
| INV-27 | every intake is echoed back in one sentence (heard · door · name · row, plus the placement [INV-37]; silent arrivals echo in the next report); every status report names each in-flight feature's pipeline station | Throwing a wish |
| INV-28 | echo-names are plain descriptive phrases; a report line opens with the reader's outcome; every handle (codes, numbers, coined names) only trails; one fact = one standalone sentence; NEVER-list: bookkeeping numbers (test counts, suite sizes, version strings) never as message content — translated, trailing, or in the records; the done-claim walk [INV-25] keeps them as the answer; delivery: a prompt hook reminds every window of the language + narration laws (per-machine, the human's install; the skills stay the homes) + a mechanical PRE-SHOW arm — `scripts/preshow-lint.py` flags a human-facing line that OPENS with an internal handle before it is shown, a warning to clear (born of a report that led with "rows 166 and 148", 2026-07-08) | Throwing a wish |
| INV-29 | a feature-doored wish walks the kind-scaled FIT WALK at intake (journey / flows / trigger lenses); trivially-closable holes closed and written how; only genuine taste calls go out, batched; prover mode FEATURE-FIT | Throwing a wish |
| INV-30 | product-kind verify includes the visitor walk + feel pass against the prototype bar, in the medium's own form (motion for a browser, reading path for a book); findings become rows or red | Throwing a wish |
| INV-31 | a taste choice made without asking is told in the landing report — plain words, an example, a tweakable mark; no confirmation, silence is consent, never re-asked; the [default] tag keeps it findable | Throwing a wish |
| INV-32 | a decision card opens with what the choice changes for the person; options labelled by consequence, mechanism only if it helps | Throwing a wish |
| INV-33 | every pipeline step is worked wearing its craft's head (product manager at spec · architect at architecture · QA automation at matrix and tests · senior developer at code · the visitor's own eyes at verify); the step→craft ladder's one home: build-pipeline | Throwing a wish |
| INV-34 | the pre-report walk: before any movement-end/milestone report, the communicator rules are re-read and the draft passes phrase by phrase through the outside-reader question; trailing anchors stay legal; acceptance = the reader's own read; the walk's one home: communicator | Throwing a wish |
| INV-35 | while work runs, beats are narrated as they happen — a station passed, a load-bearing find, a turn — in plain roadmap terms, the reports' voice; every beat names the wish and station in hand (identity); a station's completion is a beat whose line digests what the station produced (digest); a long beatless grind gets a line naming what grinds (heartbeat), and a coming stretch that needs nothing from the human is told as an offline window — step away, an honest range (unknown said as unknown, never a guess dressed as a promise), what he is needed for at its end, and a beat when he is needed again; the window batches its questions to its end and says its own off-range end (overrun, done sooner, blocked on his word), the needed-again beat a chat line awaiting his return, never a summons — the trail accounts for the session's time; the per-command grind stays quiet; a narration line is chat-register, distinct from a report (no pre-report walk, no questions, the plain-language and bookkeeping laws still bind); it replaces no report; a detached run (a background command or a delegated worker the chat does not stream) expected past ~2 minutes opens with a START line (what runs, where its log lives, an honest range), keeps a beat every ~2 minutes or per stage, and closes with a DONE digest — detached work writes only to its log and shows in no agent panel, so silence reads as lost; the mechanism stays free, visibility is the requirement; the law's one home: communicator | Throwing a wish |
| INV-81 | a question to the human walks the pre-ask scan wherever it rides (report tail, decision page, lone ask): the phrase-by-phrase outside-reader read [INV-34] plus the first gate "can I decide or verify this myself?" [INV-4, INV-5] — a failing question is work done instead of asked; a surviving one carries its recommendation [INV-60]; one home: communicator | Throwing a wish |
| INV-82 | accepted (same-or-better, all reached gates green) work is pushed to the host's remote by rule, never parked locally; the rule runs inside the human's standing push grant [INV-70, INV-9] — a remoted host with no recorded grant keeps work local and asks the grant question once, at its first push moment; it stands down while a peer session is known live in the repo (push coordination returns to the human [INV-11]); the remote discovered from the tree first; a host with no remote gets ONE contextual question at the first push moment (create — GitHub/GitLab/named — or stay local), recorded in the host profile; every push re-walks the README against the pushed truth (the shopfront law [INV-44] at every-push cadence, README crisp and current); the human's personally named milestone gates still wait for his word | Rhythm |
| INV-83 | anything shown to a human (rendered page, mockup, decision page, report artifact) passes scripts/preshow-register-lint.py before it is shown; a red result blocks the showing (a block, never an advisory warning [cf. INV-28]) until the flagged text is rewritten into the reader's plain words; the pattern set covers the coined-metaphor / calque / transliterated-pack-term classes in English and Russian, each pattern the specific coinage never its ordinary constituent word; the set grows by one per caught leak, each leak folded in as a pattern the same day with its source and date; the residual beyond patterns (a novel machine-flavoured abstraction) is owned by the clean-reader check (a fresh agent, pack not loaded — docs/spec-style.md); mechanizes the profile's no-calques + register lines (internal coinages live in docs only); one home: communicator's pre-show walk beside the leading-handle arm [INV-28, INV-34] | Throwing a wish |
| INV-84 | human-facing text is drafted by a fresh writer session from a plain brief carrying the facts, the intended reader, and the register laws; the rules-loaded session briefs, reviews, and lands, and never writes the prose itself; binds new and in-edit text only (the unit = the touched section, a whole page only on the human's word; live chat stays the session's own words, the road binds durable prose); a blanket rewrite of settled text is refused (meaning can shift in bulk restructures); settled text walks the road when a human rejects a specific page or an edit opens it anyway | Rhythm |
| INV-85 | when the reusable answer lands on a product carrying content of its own, founding (and adoption's orient) proposes the engine/instance split, never imposes it; the human's word decides, both outcomes recorded — declined = a one-line reuse note (`reuse.split-declined: <date>`), the offer returns only when the product outgrows one home; taken = engine repo (public, generic fixtures, content contract [INV-79]) + instance home (content, corrections, private fragments; heavy binaries per [INV-75]) and the pair rules bind | Bootstrap |
| INV-86 | leading a pair: each repo is a full host (own spec/queue/journal/inbox/.live-spec, no third document across the seam [E-14]); one spec each, the engine's cites no instance content, the instance cites engine contract-entry handles only (D-7); two queues, a both-shaped wish splits at intake into one row per queue citing the spoken wish [T-17, INV-1]; the instance's inbox is the human's front door; lessons travel only through the inbox door under write-ownership [E-11, INV-10]; one window serves one repo of the pair, unsure ⇒ ask, read-only on the other half save one inbox file | Bootstrap |
| INV-87 | Card and standing answer derive from one catalog home — the package-defaults table (each row marked card-visible or internal) joined with profile lines; every card-visible row shows, host lines show as project rules, every card row traces back, completeness both ways. | Meeting your settings |
| INV-88 | Fixed card copy states each setting as a readable rule; a personal value shows only as the reader's own, labelled theirs to change, never as the product's prescription. | Meeting your settings |
| INV-89 | every catch-up step reads its precondition from the tree: end-state-holds skips as done; old-and-new-both-present merges file by file (identical → old copy to attic; differing → reconciled by the settings ladder's homes; leftover conflicts → the plan's gate); a directory never nests into its replacement, the new form never overwritten by the old; an outdated installed-set record retires to the attic and is re-read from installed version lines [M-7] | Catch-up |
| INV-90 | the catch-up preserves facts and re-homes them: settled prose rewritten only on the owner's rejection or a shape that cannot hold it (each rewrite rides the plan to the gate); the canonical doc set and names live once in ADOPT.md, other guides point there; a host keeps its own doc names, recorded as a `spec.file` host-profile line, a rename only offered; stray root checkpoints re-home to `.live-spec/checkpoints/` | Catch-up |
| INV-91 | a release that changes something hosts must act on lands one dated, versioned MIGRATION.md chapter with the host-side steps (a release owing nothing adds no chapter and its changelog says so); the catch-up walk is version-chained — the work list is the ordered chapter chain from the host's recorded version to the current one, oldest first, one plan for the whole chain, resumable under INV-89; a record with no readable version starts the chain at the earliest chapter | Catch-up |
| INV-92 | the walk's own self-test: a pre-walk inventory (document fingerprints + the host spec's anchor multiset + the suite's verdict) recorded beside the plan, re-recorded after execute, compared — every difference accounted for by a plan item, an unplanned difference blocks verify until gated or reverted; the baseline commit is the named restore point (the plan states the one restore command), the attic readable without any restore | Catch-up |
| INV-110 | the catch-up routing's discriminator: the walk fires only when the host's recorded package version is behind the current package VERSION; a docs restructure carrying no version delta is the host's own queue row through its pipeline, whatever wording the ask used; the trigger wordings (re-layout the documentation, catch up to the current pack) are examples under the version test, and a wording never decides the routing; homes: the F-catchup skill-behaviour paragraph + MIGRATION's When-to-run section; born of the track-coach audit (2026-07-10) | Catch-up |
| INV-111 | a same-version docs-layout pass rides one sanctioned light vehicle: a host restructuring its own documents with no package-version delta [INV-110] runs one named shape; the owner's decisions are locked in a checkpoint before any file moves [INV-107], the work builds on a clean pushed base with a one-command restore, content is proven by a word-token multiset check AND a punctuation multiset check (word-token identity alone passes a reflow that moved punctuation), the full suite reads green on the restructured tree [INV-39], and one journal chapter lands; a branch-riding pass closes through the merge gate [INV-114]; a host never improvises a layout pass and cites this vehicle; born of the track-coach s63 audited pass (2026-07-10) | Catch-up |
| INV-93 | every ask hears an honest time range at its capture echo, read from the work's shape or observed runs (unknown said as unknown, never a guess dressed as a promise); long work is explained up front in plain steps — what has to happen and why it takes that long; a long stretch occasionally says roughly how much remains, riding INV-35's heartbeat; the landing report states the estimate beside the actual, overrun or under said plainly | Throwing a wish |
| INV-94 | no line certifies its own sincerity: a sentence praising its author's honesty or directness ("we say so plainly", «честно говоря», «из честного») carries no information — naming not-A informs only where not-A was a live alternative; the content carries the honesty, the label comes off; each caught phrase joins the register lint's pattern family [INV-83]; binds shown artifacts (the lint) and chat (the session's read + the hook) <!-- user-language --> | Throwing a wish |
| INV-95 | one spoken leave-word winds the session down to a shutdown-safe stop: workers halted or run to their landing (a sleeping machine kills them mid-write [INV-76]; an unhaltable one recorded by the handoff discipline, its death-with-sleep said aloud), every lane at its checkpoint (base rule 6; red never committed, the failing test tops the resume file), green work committed under standing gates, the resume file saying what resumes where; first beat gives minutes-to-safe [INV-93], last is one closing line — safe to power off + what resumes where — said only when every point above holds; the remaining-minutes habit rides long work before any leave-word [INV-35]; never guessed from silence, never closes anything itself | Rhythm |
| INV-96 | everything built with the method is offered its say-so: the standard attribution line — "made with live-spec" linking to the pack repo, trailing the pack version the project runs (read from the attach record, refreshed at catch-ups — the line doubles as the adoption tracker) — on a built-with publication's landing surface (README footer; a skill also in its SKILL.md); wording lives once in the publish skill's floor; the line is an OFFER, never a gate — the walk says once when absent and proposes, the owner's word decides, a declined offer closed and never re-asked [INV-16]; each project applies it through its own queue, the pack never writes foreign trees; the pack's own mirrors get the line stamped by the sync script from the live VERSION at each sync | Publishing |
| INV-97 | the four project-side checks (completeness · tests-present · behaviour-traces-to-spec · conflicts) ship as generic runnable code under scaffold/guardrails/, parametrized by ONE host config (document paths, tests dir, user-facing globs, registry path, render command where needed), never by editing check code; gate-contract output [INV-47]; honest failure: missing config = red attach-me, dead path = red, a lacking precondition is a DECLARED waiver in the config, never a quiet pass; attachment rides the adopt walk, the pack repo attaches first as its own proof; acceptance measured — config-only attach ~15 min [default], each check red-proven on a planted defect; structural defects only [E-6], registry content stays the host's [E-10] | Rhythm |
| INV-36 | the project's own kind (book / backend / static site / fullstack / CLI / skill pack / custom via the queue) asked at founding and at adoption's orient — always asked, never profile-seeded; one home: the host profile's `project.kind`; seeds project-wide defaults but never overrides an explicit host line; distinct from the per-wish work-kind and the placement; updated on the human's word the moment evolution is noticed, journaled | Bootstrap |
| INV-37 | every wish is placed on the product's feature map at intake, the placement SPOKEN with the echo and WRITTEN in the row (`map:` — changes feature X / new feature / restructure); the map = spec scenarios + architecture nodes, no third document; a restructure verdict queues its own row and re-carves only through the architecture step's re-prove | Throwing a wish |
| INV-38 | the whole feature map is readable on demand — read at ask-time off the spec's scenario sections, the current-vs-target header (statuses at the granularity the promised-tag binds, per S-0), and the queue's open rows (stations for in-flight, queued NEW-verdict wishes included); no third document; answer lines obey the line law; chat by default, rendered page on the human's word; never fires uninvited (reports keep the board's in-flight scope); a host with nothing to read is answered honestly | Asking what the product does |
| INV-39 | a landing commit carries exactly one row's delta; its gate runs on a tree clean of any other lane's unfinished work; after a landing, the waiting lane re-fences and re-runs its gate on the new truth — landed-first wins | Throwing a wish |
| INV-40 | the never-bend list holds at every economy rung: the door law + tripwires; red-before-fix; the human's gates; the landing report with named sheds; landing purity; the push gate at full rigor; the safety net; narration whole; and an explicit host line outlives any rung | When money or time run short |
| INV-41 | the architecture states measurable quality budgets plus each budget's instrumentation home (numbers measured and human-readable); the project's KIND proposes the dimensions (product: paint/interaction times; backend: latency/throughput/errors; CLI/pipeline: run time, per-unit cost; skill pack: eval pass rate, suite time; prose: what honestly has a number) and a quality with no honest number is said by name, never a vanity metric; each budget asserted by a matrix-row acceptance, never prose hope; no budgets + no instrumentation home = derivation defect; numbers are the host's taste, set on the human's word at the surface's first budget landing, binding never retroactively | From the spec to the tests |
| INV-42 | the human's word on a shown artifact is read as meant: a phrasing he killed in a review round stays killed in every later draft of that artifact (the writer keeps the kill-list written in the artifact's project records, never only in session memory — a resurfaced cut is a defect, however fresh it looks); a vivid phrase of his is adopted only as meant — mockery of a bad draft is not guidance, its intent read from context or asked, never assumed prescriptive; home: communicator | Throwing a wish |
| INV-43 | an approved prototype is the norm for look and feel, one law with four arms: the clause it fathered cites `norm: <path>` at line end, approval freezing the artifact into `docs/norms/` with a dated provenance line so the pointer never reaches a live prototype home (format: spec-author); a norm-pointered surface's build OPENS the artifact before the code step and the landing records a one-line plan-vs-prototype diff, a missing line = review defect, the verify feel bar reading the same pointer (build-pipeline code step); a declared mockup-first entry condition is written in the wish's queue row and cancels only by the human naming it, never a general "go build" (door step); prover lens: a prototype-born clause with no pointer, or clause text contradicting its own artifact = finding; binds forward, pointer only for prototypes the human APPROVED as the look | A prototype stays a sketch |
| INV-44 | a version push re-opens the shopfront: the README's claims match the pushed truth and the kind-owed visuals ride along (skill pack: diagrams; visual product: fresh screenshots; tool: example runs) — the walk is the publish skill's checklist at push scale (one home there), pointed at by the commit-and-show step, its outcome riding the landing report ("shopfront checked — current" when untouched); a stale claim is fixed before the push; never a version push past a stale shopfront | Publishing |
| INV-45 | the push gate derives its check-set from a declared reach map (which checks read which file classes), mechanically from the diff's file list, never self-judged: EXPLICIT (a named file in guardrails/), CONSERVATIVE (an unmapped or new file ⇒ the full suite; tested documents — SPEC, matrix, architecture, queue, SKILL.md — stay full-reach, "just .md" is no class), SELF-TESTED (the deciding script red-proven on fixtures, unclassifiable ⇒ full by construction); the cheap gates never scope; "full rigor" (INV-40) = every check the diff can reach, green | The machines that hold the bounds |
| INV-98 | every process converges on its goal: the goal named up front as an artifact the work can be held against (frozen norm, exemplar bank, failing test, written acceptance); a paraphrase cannot serve as the goal; every iteration measures distance to the goal itself and a proxy never replaces the goal; the distance only shrinks and a reached level locks by a mechanism (norm template, conformance test, growing lint floor, downward ratchet); a deliberately divergent stretch is legal only named and bounded by its convergence point; working statement: base rule 22, chapter: the private playbook; first teeth rows 216/217 | The machines that hold the bounds |
| INV-108 | a standing behavioural rule that breaks mid-turn twice earns a live channel that moment: an every-prompt hook line (a reminder at the decision point) or a mechanical after-the-fact check (a suite red), the pick recorded where the rule lives; the once-read homes (loader, profile, skill text) stay the rule's normative homes and the live channel only carries it; the convergence principle's hand for behaviour, kin of the problem-ledger's second-occurrence law; the 1.1.0 audit's once-read walk is its first sweep; a rule's mid-turn breaks live in one home — PROBLEMS.md — and the live-channel landing points back rather than doubling as the break-record, so the sweep reads one source (the one-home principle, base rule 4) | The machines that hold the bounds |
| INV-46 | verify's adversarial option: a FRESH-context checker briefed with the landing's SPEC sentences + artifact paths (never the worker's summary or the senior's plan), hypothesis "tasks completed, goal missed", ladder exists → substantive (stub greps: TODO/FIXME/placeholder/lorem/hardcoded sample/empty body; list's home: pipeline step 8) → wired → flows; findings become rows or red; MANDATORY when the change is high-stakes (the delta is surface-sized · OR it edits the method itself — a rule whose meaning changed, a wording-only edit not counting) AND its only review is the author's own (no independent read, where an independent read is a differently-contexted head briefed from primary sources on the goal-missed hypothesis — a same-context prover pass never counts, delegation never makes the review independent); one fresh checker per landing batch covers the batch [INV-61] (form scaled, freshness never); optional elsewhere; kind-scaled for skill/prose (shipped text vs spec sentences); the checker is a worker under ACT-3, verdict rides the landing report; trigger broadened 2026-07-12 (a self-built method law passed its author's prover clean, a fresh adversarial pass caught a real INV-16 contradiction) | Who decides what |
| INV-47 | gate hygiene: every BLOCKING gate on red emits one typed failure line `{severity, code, message, fix}` beside its human lines (fix = the human sentence); every check declares blocking or advisory (advisory never flips the exit); artifact-rebuilding scripts validate all outputs before writing any; operational home: guardrails README; binds by deed from the first gate under it, sweeps as each is next touched | The machines that hold the bounds |
| INV-48 | the resume file is a digest with a hard cap: whole file ≤ 100 lines [default], a suite check owns the number (red-proven on a synthetic bloated file); open legs restate as one terse line each (name + what's open + where detail lives, INV-26 resolved by form); compaction moves prose to its home, never drops a leg | Rhythm |
| INV-107 | a landing closes the checkpoints it shipped: a landing that ships a checkpoint's items flips that checkpoint to its closed state in the same landing (the movement writing the work into git history marks the checkpoint done), so a returning session never reopens finished work; a checkpoint whose items all live in git history is stale by definition and reads as a resume defect; the closing sweep rides the NEXT_STEPS replacement, a checkpoint left reading "not started" after its items shipped fails the landing; homes: the breakpoint clause + base rule 6 | Rhythm |
| INV-49 | lanes are picked by a dependency graph at queue-take (edge = shared surface / spec section / skill file / doc region): open on a pairwise-independent set up to the T-18 cap; integration-only collisions pre-roll isolated build stages with the landing order DECLARED at claim (first-declared lands first, later re-fences); tiny rows ride serial — parallel pays only when build stages dominate; the set and order narrated at opening | Throwing a wish |
| INV-50 | a conditionally-entered face (first visit, empty state, onboarding, one-time banner) states its deliberate re-entry path or names the one-way as a decision; trigger wording "only on first visit/run", "until dismissed" owes its return sentence; prover carries the entry-symmetry lens; extends INV-29's where-next to faces over the visit's lifetime | Throwing a wish |
| INV-51 | anything handed/opened to the human leads with its passport: the project's NAME in the visible content (never only the URL) + the read contract ("needs your word: what, by when" or "just an update"); the announcing chat line carries the same two facts; home: communicator | Throwing a wish |
| INV-52 | during an away-stretch nothing opens a browser window: artifacts accumulate on ONE page, the stretch's end opens it once; mid-stretch re-open only as the same page refreshed; home: communicator | Throwing a wish |
| INV-53 | a brief editing existing files is born from READING them in full: three recorded lines per file (current state · what changes · what must survive); every step back-references its spec sentence; every technical claim cites a source (file:line / command output) | Who decides what |
| INV-54 | the worker HALT list, closed: ambiguous requirement · two consecutive unexplained failures of one command · missing config/dependency · acceptance impossible as briefed — stop with evidence; otherwise run to completion; composes with one-tier escalation | Who decides what |
| INV-55 | a brief targets a bounded share of the worker's context, splits above it (default bound: brief text ~300 lines, ~8 files to edit [default]); paths, never inlined file bodies | Who decides what |
| INV-56 | a known, owned problem never blocks unrelated work: it is parked (ledger line / owning row / expected-red note) and unrelated lanes keep rolling; hand-fix loops cap at two-strikes (second occurrence buys an owner); a defect with a named mechanical owner is serviced in batch (silent fence-fixes, one ledger append at session end), never per-instance ceremony; a real NEW bug still preempts (T-9) | When the workshop itself misbehaves |
| INV-57 | the stretch's end is unmissable: the last rendered thing is one short final line (what closed · what's next · what's needed · when the agent wakes), the long report above it, a page deliverable repeating its passport; delivery required, existence alone falls short; home: communicator | Throwing a wish |
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
| E-29 | the feature-coverage trace: a per-project-type primary unit (a feature, command, guarantee, or argument) tagged inline on its heading, mapped in ARCHITECTURE.md to implementer node(s) + a test; a second traceability layer above the anchor matrix, reusing the anchor-ownership machinery; the format's authoring home is the spec-author skill | Machines |
| T-20 | three intake channels (spoken/typed · comment on something shown · dropped file, outside sessions via the inbox door) → exactly one of five routes (wish intake · same-session fix · closing answer · field evidence beside the feature's success measure · problem ledger), the route named in the ledger line; the skill fires on receipt and at inbox sweep, never on the agent's own output, and never opens a queue row by itself | Sending feedback in |
| INV-68 | nothing handed in is lost: every received item lands the same session in its route's own home (wish→row · fix→commit+journal · answer→archive+row · noise→problem ledger), and the routes with no prior home — field evidence, reactions, wordless drops — land as dated feedback-ledger lines (who · channel · concerns · plain words · route); one echo per item; a re-mention appends its date; only the assigned session writes the ledger, outsiders use the inbox door | Sending feedback in |
| INV-62 | taste-heavy deliverables build smallest-first: the cheapest judgeable sample (a paragraph, a card, two sections) gets the human's word BEFORE the full build spends; the agent's own discipline, distinct from the human-side mockup-first entry (INV-43) | Throwing a wish |
| INV-63 | a rejected artifact reopens its SOURCE (spec clause / card / brief): source corrected first, artifact rebuilt from it; line-patching rejected output against an unchanged source = the five-round trap, banned | Throwing a wish |
| INV-69 | the routing rule: a unit of work's tier is PROPOSED by its step and kind (judgment→senior, never routed down; one-shot→haiku; multi-step mechanical→sonnet); size alone never decides it; the economy rung moves the threshold; the proposal is advisory — the senior may override per wish, override logged (proposed→chosen→why) on the checkpoint and landing report; closes D-2 | Who decides what |
| INV-70 | a tunable parameter (resolution, batch size, timeout, sampling rate) is set by the agent to a sensible default and TOLD in the landing report with its `[default]` tag, never asked — the human tunes it after if wanted (updated together at most), re-asking never owed; carries the taste-told law [INV-31] to numeric/config knobs, kin to the economy ladder [T-19]; the agent moves every task it can and reserves questions for the genuinely undecidable [INV-4]; where the human GRANTS it, the agent pushes to prod on its own certification when the work is sound [M-6, INV-9] | Throwing a wish |
| INV-71 | where we are now is answerable in any seat: a short NOW (work in hand + its pipeline station) and NEXT (what the queue holds) status kept current in the CHAT — the one surface every seat shows [INV-67] — refreshed at each station change and carrying a heartbeat on a long stretch [INV-35]; the harness task list is a local-terminal convenience (kept plain-worded [INV-28], absent in a browser), never the status's home; a rendered status page is the local seat's optional richer view; binds for every project live-spec runs | Throwing a wish |
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
| A-11 | the catch-up walk for an already-adopted host, entered by routing from the adoption guides, operating guide MIGRATION.md: orient on the delta → plan behind the owner's gate → execute preserving facts → verify + re-record; one host per walk (a pair's other half gets one inbox wish, an under-attached half attaches first); machine-level steps once per machine, each with an already-done check | Catch-up |
| ACT-1 | the human: taste, gates, wording | Who decides what |
| ACT-2 | senior agent: judgment | Who decides what |
| ACT-3 | tiered workers, checkpoints; every brief carries the ledger walk + the clock; a brief may name an isolated tree — its delta integrates only under the pen | Who decides what |
| M-1 | milestone: re-prove + audit + compaction + gate list | Rhythm |
| M-2 | safe breakpoint; announced self-compaction | Rhythm |
| M-3 | documents versioned like code | Rhythm |
| M-4 | live-spec is its own host | Package repo |
| M-5 | CI mirror of the same checks: same scripts, second net runs the FULL set (the reach map stays local); worked example `.github/workflows/gates.yml` + guardrails-README host guidance | Rhythm |
| M-6 | push gate: prover re-check before every push; one carve-out — a push whose diff is exactly one new inbox/ file (the remote deposit [INV-112]) owes the fence and no record | Rhythm |
| M-7 | version homes: VERSION file · SKILL.md frontmatter · host record | Rhythm |
| INV-72 | the prover reads the whole axis list [C-1] actively, deriving each stateful surface's reachable situations for itself — every axis it passes through while already shown (view, mode, tier, viewport, reopen) and every other surface present at the same time (siblings on its screen, one step before and after it in the flow, stateful or not) — and asks for each whether behavior is stated there; a reachable situation with a blank answer is a finding, the same class as a fact no node owns [E-14]; rides the whole-spec and surface-add passes [M-6]; reports the gap, invents no answer and asks the human nothing, the author writing the sentence as a C-1 composition invariant tagged like the facet sweep [INV-18, INV-31] | Composing across axes |
| INV-73 | the feature-coverage check is two-way: every tagged unit resolves to a real implementer node and a real test, and every scenario the pack promises carries its `[feature: F-x]` tag; a dropped tag or an orphan coverage row goes red; the infra machines implement guarantees not features and sit outside the layer; reuses the anchor-ownership machinery [E-29] | Machines |
| INV-74 | the runtime view: for every flow the spec promises, the architecture walks the running product — which node serves each step, what data crosses at each hop, where the flow can fail AND what happens then (every failure point carries its fallback; one without is an unfinished walk); one short walk per flow; a flow the doc cannot walk end to end is a finding (a missing node or an unnamed seam); scales by kind [INV-36] — a book's one sentence satisfies it; binds forward [INV-15] | From the spec to the tests |
| INV-75 | the placement view — THE tiers-and-technology table: every node states its place (build-time on the author's machine · CDN static · client browser · edge worker · external service) plus the load-bearing technology choice where one exists; says where secrets live and which tier holds each non-client verdict; first-class and at a glance; the doc reads tiers-first (opens with the shape at a glance, then nodes, then flows through the tiers); scales by kind [INV-36] — a book's one sentence satisfies it; binds forward like INV-74 [INV-15] | From the spec to the tests |
| INV-76 | a background worker outlives a memory wipe: the handoff note records the worker's id (→ its checkpoint file), its briefed write-set [ACT-3], and the three liveness checks (file times over ~30 s [default] + the worker's heartbeat touched on its checkpoint file on a fixed interval [~60 s default], stale when untouched past ~2 min [default] + one message to the id, ~2 min [default]); the OS process list and the harness task list are never proof of death; life on any one check ⇒ reconnect, files claimed; a dead verdict requires all three quiet together — a still write-set, a stale heartbeat, and an unanswered probe — declared in one written line; output never framed finished before the verdict; a prior-context worker is a foreign writer until verified; no second worker onto a shared tree until the first halts by its own reply or is declared dead by all three checks [INV-11]; dead ≠ done — a dead verdict frees the files, doneness is read from the checkpoint's finished marker or the verify walk [INV-46] | Rhythm |
| INV-77 | the real-device boundary: touch physics, scroll snapping, background throttling live past a desktop headless browser; such a behaviour gets a real-device walk row the suite can never green, owed to the human's hands before ship (kin of the feel gate [INV-30]); the suite names what it cannot see | From the spec to the tests |
| INV-100 | test hygiene, two halves: every test removes what it creates (temp files, fixtures, processes, mutated shared state) and a suite run leaves the machine as it found it — a leak is a defect of the test; placement — test files are born in the system temp home or the host's gitignored state dir and erased at run's end, a user-visible folder (Downloads, Desktop, Documents) is never a test's workspace, a headless browser's download directory is pointed at the temp home explicitly; the pack's own suite: prefixed temp artifacts + a session before/after temp-home diff | From the spec to the tests |
| INV-102 | a test's expected value derives independently of the code under test: never recompute the code's own formula and assert it as the expected value, since such an assertion is a mirror that only proves the code equals itself; legal sources of an expected value — a hand-computed constant, an independent derivation, a recorded real output reviewed by a human; boundary — a round-trip or property test over the outputs is legal because it asserts an invariant, the ban strikes only an assertion whose expected value the code's own formula produced; born of row 220's audit (green suites missed real walk bugs, 2026-07-10) | From the spec to the tests |
| INV-103 | every landed queue row carries its delegation accounting in the landed row's status cell — what went to a worker with a rough saving, or a stood-down line naming why the senior kept the work; a suite check reads the queue (ROADMAP.md) and a landed row without the line goes red; binds forward from its landing date (a row landed 2026-07-12 or later carries the line, earlier rows stay stock); the duty binds the orchestrator seat regardless of model; born the night prose alone did not hold the routing rule (2026-07-12) | Who decides what |
| INV-109 | a rewrite or restyle that removes substance (a section, an argument, a rationale, a worked example) lists every removal in its landing report, one line of judgment each — the fact kept and where, the owner killed it by name, or the rewriter proposes dropping and asks; a removal the rewriter cannot justify becomes a question before the report closes; never a silent cut of substance; scopes to substance and leaves line-level wording free; homes: communicator's pre-report walk + build-pipeline's docs-only door; born of a compressed README section restored the same session (2026-07-10) | Throwing a wish |
| INV-113 | a deliberate architecture redesign re-shapes and re-proves the document in the same movement: when structure is redesigned (layers restacked, a surface's ownership moved, nodes merged or split) ARCHITECTURE.md is re-shaped to the new form and re-proven with the architecture lens in that movement, not only re-pinned; the pins-only path is scoped to a boundary shift that leaves the document's shape standing, since after a real redesign the old shape itself lies and fresh pins on a stale shape are a defect; the re-carve routing [INV-37, E-14] carries the row, this states what the row owes the document; homes: the architecture-doc clause + build-pipeline's architecture step + the refactor line; born of the tlvphotos second-finger redesign (2026-07-11) | From the spec to the tests |
| INV-114 | a restructure or migration merge gate judges the delta: three parts — load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check [INV-111], the full suite green on the merged tree [INV-39], and a full prover pass on both sides whose blocking set is delta-scoped (an unmatched token, a red suite, a new-side finding absent on the old side, an unnamed meaning change); pre-existing findings equal on both sides route to queue rows in the same landing and never block; the token-identity part scopes to content-preserving restructures, and a content-changing redesign routes by INV-113; and a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation; homes: the spec clause + product-prover's restructure-merge gate + build-pipeline's restructure door; born of a strictly-improving merge parked on the old side's pre-existing debts, corrected live (2026-07-12) | Catch-up |
| INV-115 | the full pass audits every living document for redundant information and compacts it, meaning always preserved: compact means no redundant information — a fact lives once, in one home, with a pointer from everywhere else; a pass removes only redundancy (a fact restated at full length in a second home, history owed to the journal, a table row restating its prose) and keeps anything whose removal would change the meaning or a reader's understanding; a redundant-looking second statement can be a fact's sole home (the traceability-read index rows are the worked proof, kin to INV-39), so compaction is per-item judgment and a pass removing substance accounts for each removal [INV-109]; restructure only for a faster reading shape and only through the content-preserving layout vehicle [INV-111]; nothing grows unboundedly [INV-1]; home: the M-1 milestone gate's doc-compaction step, owned by build-pipeline; born of the owner's compaction definition (2026-07-12) | Throwing a wish |
| INV-116 | the full pass proves the architecture beside the spec: every milestone gate [M-1] and every push gate [M-6] runs the product-prover over ARCHITECTURE.md as well as PRODUCT_SPEC.md, so the design-level seams — component contracts, owning-node edges, the cross-section composition between components — meet the same structured review the spec gets; the architecture pass records in docs/prover/ beside the spec's and carries the spec's freshness rule (a record predating the last ARCHITECTURE.md change is stale); the prover's own method already covers design / HLD / LLD documents, so this points the standing gate at the architecture rather than adding a new review; home: the M-1 milestone-gate walk and the M-6 push gate, owned by build-pipeline and executed by product-prover [M-6]; born of the owner's word and this session's for-fun prover run against the spec (2026-07-12) | Rhythm |
| INV-117 | every session carries a stable identity minted at its start — before its first act, recorded in its session checkpoint under `.live-spec/`, unchanged for the session's life: the harness session id where the context carries one (unique by construction), else the start time joined with the worktree path and a nonce (distinct worktrees already differing under INV-105); the parallel-lanes pen tie-break orders on this identity for a genuine concurrent claim with no git ancestry [INV-2, INV-11] — the row→in-work flip records the claiming session's identity so a peer reads both and computes the same order from either side, so exactly one session backs off (never mutual back-off, never a shared pen); the inbox source-mark's short session token is a projection of this same identity, never a second scheme; homes — the spec clause and base-rulebook's fence rule; born of the for-fun prover run's F1 (2026-07-12) | Package repo |
| INV-118 | shipped product docs (spec, matrix, README, skill card) state each requirement impersonally — the rule, the actor as a role (the user, the producer, the target user), and the reason; the load-bearing rationale stays and the personal attribution drops; a dated decision keeps the date as a plain anchor and drops the name; personal attribution and candid process voice live only in the local-only diaries (JOURNAL, NEXT_STEPS), which no publish ships; spec-author writes each shipped clause impersonally from the first draft and the publish floor reads the shipped docs for a personal name before the deposit leaves; the pack's own spec/matrix/roadmap keep a deliberate owner-attribution provenance as a dated exemption pending the owner's decision (row 279); homes — the spec Publishing clause + spec-author guidance + the publish floor; born of track-coach's 2026-07-12 shipped-artifact audit | Publishing |
| INV-119 | crossing the instance→engine boundary clean: a generalized engine's spec records how each behaviour landed in its OWN code — a reconciliation log ("how each behaviour landed in code"), each entry citing the engine's own public commit ("landed in engine commit <hash>"), one intro sentence stating the normal intake path (proven first on a live instance, then generalized), no private-instance hash standing as engine provenance; a mechanism carries a neutral internal name and a visible instance label is marked instance-supplied [INV-79], the neutral term the one name [E-4]; the publish gate checks a generalized package for the two leaks — a foreign provenance hash (fails to resolve in the engine's own history, mechanical) and an instance locale label as a mechanism name (tripwire + advisory read) [E-20]; three homes — the F-pair clause, spec-author's boundary section, publish's generalized-engine check; born of the exhibition-engine public-publish pass (2026-07-12) | Bootstrap |
| INV-120 | a shipped artifact carries no Cyrillic outside a user-language string the program deliberately emits, and no owner/personal name in a requirement's statement; the publish gate holds this with a machine (guardrails/check-shipped-language.sh) reporting each offence as file:line, candid process-notes and attribution living only in the local-only diaries; the machine covers the two mechanical offences (Cyrillic, owner-name) and leaves a coined non-English metaphor to the register lint and the human; a dated allowlist spares deliberate program data and authorship bylines (equivalence-gate: a new offence reds, a listed one is counted debt); proven on fixtures, not yet wired to the pack's own provenance tree (row 279); composes with INV-118 (the voice this holds); born of track-coach's 2026-07-12 audit | Publishing |
| INV-121 | a proven artifact settles a fork before the human hears it: before surfacing a design choice, a session checks whether an existing proven artifact — the architecture, the spec, the invariants — already determines the answer; when it does, it derives the requirement and says it back with the section cited, offering no fork; a fork reaches the human only for what the artifacts leave genuinely open (a taste call, or a real trade-off with no artifact-grounded winner); the read-the-doc twin of ask-never-guess [INV-4] — that forbids inventing an answer, this forbids offering a choice the documents already made; home: base rulebook rule 1 beside ask-never-guess + this clause, cited by row 259's entry impact-analysis station; born of a track-coach session offering two options while its ARCHITECTURE.md layer split already determined the answer (2026-07-12) | Throwing a wish |
| INV-122 | every new or carved architecture node passes a three-question fitness test at its birth: can it be tested alone · does a real second place need it · can it and its neighbour be worked in parallel without queuing on shared files — three yes make it right, a single no is a flag to answer (name the plan or fold), two or more no make it premature (the carve folds back into its caller); first home the architecture step, second home product-prover extending the speculative-node flag (a node with one caller and no promised second is flagged for that answer, not auto-rejected, so both homes agree on the one-no case); the structural face of the testable/reusable/parallel principle; born of the six-principle design wish, principle 7 (2026-07-12) | From the spec to the tests |
| INV-123 | compaction is a scheduled station for code as well as docs: beyond the doc-compaction pass [INV-115] the station widens to CODE — duplicate logic merges, dead weight leaves with its listing [INV-109], a ripened abstraction is extracted only through the three-question fitness gate [INV-122]; two triggers fire it — the milestone gate, and the second occurrence of the same problem (base rule 19) that opens the duplication's own compaction row that moment (rule 19's owner; the row lands through the ordinary pipeline, one row's delta [INV-39], never blocking its lane [INV-56]), not an instant in-place fix; each pass locks its reached level with a test or lint so a compaction never silently regresses (the convergence law, rows 216-218 [INV-98]); homes: the milestone-rhythm compaction section + build-pipeline's before-a-MINOR gate; born of the six-principle design wish, principles 4-6 (2026-07-12) | Rhythm |
| INV-124 | a confirmed bug drives a class hunt before it closes — four moves, not one: (1) name the defect abstractly and actively search every surface for un-seen siblings, fixing all in the same change (the active face of the class rule — go find the class not yet seen, past the one in hand [INV-56]); (2) an architecture check — a structural cause updates ARCHITECTURE.md, a cluster in one district reading as an architecture smell; (3) a spec check — a spec silent on or under-describing the broken behaviour is the real defect, fixed first so the prover can flag it [INV-15], then the code lands under it; (4) escalate to the human when the class boundary needs his read [INV-4]; the product-prover carries the class lens for the same three questions (same kind elsewhere · architecture accounts for it · spec describes it); the four moves are the bug door's close condition, a point fix leaving siblings standing being a status not a landing [INV-26]; sharpens base rule 14 from fix-the-class-in-view to go-find-the-class and generalizes the spec-under-describes-composition lesson; homes: this F-bug clause + build-pipeline bug entry + product-prover class lens + base rule 14; born of the exhibition's pinch-zoom bug (one report → five live siblings, 2026-07-12) | When a bug cuts the line |
| INV-125 | a cross-surface policy is stated at the surface-CLASS level and held uniform across its siblings: when a decision governs a KIND that recurs across sibling surfaces or elements (a gesture policy, an affordance, an input-to-action mapping, a repeating state transition, a feature or repeated element shared across places — consistency itself is an invariant), the spec states it once at the class level — the clause names the class and enumerates the surfaces it governs — and a policy written for one surface while siblings of the same kind exist is a spec defect; the prover writes itself the check (enumerate the surfaces of that kind from the surface registry [E-10], flag any the clause does not cover, same finding class as INV-72); a product with a DOM instantiates the completeness guardrail [INV-97] to assert the policy across every registered sibling root, red until all covered (the pack ships the rule + the prover lens, leaving the DOM-wide assertion to the products it serves — it has no DOM of its own); the spec-class rule is the root (catch upstream of code), the guardrail the mechanical floor; the preventive twin of the class hunt [INV-124] — that sweeps siblings once a bug is confirmed, this holds the policy uniform before a bug is filed; homes — this composition clause + product-prover's cross-surface-policy lens + build-pipeline's completeness guardrail; born of tlvphotos's pinch-zoom policy shipped for the walk alone (2026-07-12) | Composing across axes |
| INV-126 | both directions of a paired state change (open/close, enter/exit, expand/collapse, show/hide) get the same craft or a stated reason they do not: a transition crafted for one direction is a decision about the pair, so the other direction is stated too; the default is symmetry (the exit mirrors the enter's feel unless a reason is written), a shorter or deliberately-instant exit being a valid STATED answer rather than a silence; rides the standard-facet sweep as its own facet [INV-18], the author writing the pair's answer as a spec sentence (mirror / named shorter exit / deliberately instant) decided or `[default]`-tagged [INV-31]; motion feel is the human's gate [INV-30] so an undecidable pair is surfaced to the human, never a crafted-in/instant-out pair shipped silently; the prover flags a pair with one direction's transition described and the opposite unstated (the blank-answer class of INV-72); the temporal twin of INV-125 (that holds a policy the same across sibling surfaces in space, this holds a transition the same across the two directions of one change in time); homes — this composition clause + the facet list in spec-author + product-prover's paired-transition check; born of tlvphotos's polaroid room revealed under a soft veil and closed on a hard cut (2026-07-12) | Composing across axes |
| INV-127 | each person-facing scenario states how it is ENTERED (from where the walk arrives, what must already hold — the prior scenario/state, the preconditions assumed) and how it EXITS (to where the person lands, what it leaves true — the postcondition the next scenario inherits); the per-operation precondition/postcondition lenses lifted to the SCENARIO level, kin of the entry-symmetry lens [INV-50] and the runtime view's flow walks [INV-74]; the prover carries the scenario-level lens — a flow whose entry or exit is unstated is a finding (the blank-answer class of INV-72); binds forward [INV-15] (a new scenario states its edges from the first draft, the prover flags an existing gap as a finding rather than blocking), a trivially-none entry/exit stated as such in one clause; homes — this composition clause + the entry/exit duty in spec-author + product-prover's scenario-level lens; recorded 2026-07-09 (deferred large theme, revived at the next prover-method landing) | Composing across axes |
| INV-78 | a geometry fact asserts relative, wide, and long: the distance between the element's center and the viewport's center stays ≤ ε, at ≥ 2 viewport sizes, after N consecutive interaction steps so cumulative drift shows; an absolute one-viewport one-step assertion hides the drift by construction | From the spec to the tests |
| INV-79 | an engine extracted from an instance tests on its own generic fixtures (engine-shaped ids and content model), never only the donor's data (the donor's suite may stay as an extra); every donor-specific constant found at extraction becomes a named content-contract entry with a works-without-it test; two halves, one law: fixtures (test-author) + the contract entries (spec-author) | From the spec to the tests |
| INV-80 | the suite's own plumbing must not lie, three legs: a skip path executes even when never taken (skip helper imports at module load — an unrunnable skip is red); an engine/instance shim owes a re-export completeness test; a wrapper's exit code is never the verdict for a background or delegated run — the gate reads the suite log's own tail line (sibling of the pinned skip-set) | From the spec to the tests |
| C-1 | canonical axes (view · mode · tier · viewport · reopen · concurrency · every other live surface) + provenance axis | Composing across axes |
| D-1 | attic layout | Open decisions |
| D-2 | tier routing decided (row 56): proposed not fixed, senior overrides logged → the routing rule INV-69 | Open decisions |
| D-3 | snapshot retention | Open decisions |
| D-4 | pack structure: package-is-source decided; mirrors = row 51 | Open decisions |
| D-5 | all-into-profile decided; rows 52–54 execute | Open decisions |
| D-6 | pair queues: stitched reading view or strictly two — open; recommended two plain queues until real friction earns a view | Open decisions |
| D-7 | pair specs: the instance cites engine contract-entry handles and nothing deeper — open, recommended | Open decisions |
