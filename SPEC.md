# live-spec — SPEC (v0.15.61, 2026-07-07)

> **How to read this.** Each section describes one scenario: what the reader does and what the reader sees. The short codes in brackets are markers the machine uses — the prover, the tests, and searches — and the Formal index at the end lists where each one is defined. Edit history is in JOURNAL.md. This spec states what is true today.

**What's built, and what's planned.** This spec keeps the two apart.

Built and working today: the skills (the base rulebook and the working skills), the templates, the adoption procedure, the inbox, the skill evals and their records, this spec, the queue, and the first guardrails: the repo's own pre-push checks and the opt-in commit fence.

Planned, each tracked by a roadmap row: the host-facing guardrail checks and the surface registry [E-6, E-10]; the snapshot machinery [E-7], used by the adoption baseline (A-6); and the optional design-sync machine [E-18].

A planned item carries a [target] tag on a line of its own; the tag never appears on the section around it. The suite enforces the tag rather than trusting it: the suite ties each [target] to the open row that builds it, and goes red if that row ships with the tag still on, if the tag vanishes, or if the tag was never named. [S-0]

## What live-spec is

The user submits any request, of any size, at any time. live-spec breaks it into small pieces and processes them one at a time. Each piece runs the same proven pipeline, reaches a landing, and ships tested. The user is free to keep thinking about other things.

Behind the pipeline is a full set of roles:
- An analyst writes the spec.
- An architect stress-tests the design and finds the edge cases and dead ends before any code is written.
- A QA works out the tests and writes them.
- A project manager runs the process and reports back to the user.

These roles are real: they are the working skills (spec-author, product-prover, build-pipeline, test-author, communicator, publish, feedback-intake). One **base skill** holds the shared rulebook and the default settings the other skills work by [E-12].

Machines enforce the process at every step, which keeps it disciplined. Every request follows the same route. Every claim earns a test, and nothing ships until that test passes. The pipeline drives each request all the way to a landing and keeps its scope contained. It brings the user in for the decisions that are theirs to make.

A project can adopt live-spec at the start or partway through work already under way. Adoption brings the document templates, a procedure for joining midstream, and the guardrails the project installs. The project that adopts it is the **host**. The host owns everything about its own work: its spec, matrix, queue, journal, surface registry, inbox, feedback ledger, and a `.live-spec/` folder that holds its profile, its checkpoints, and the versions of the skills it runs. [E-1]

## Throwing a wish

The user is busy with something else and says "and let the card also show…," then returns to their thought. That is a **wish**: one request, in plain words, any size, at any moment. [E-2]

Within that same minute, the wish becomes a row in the **queue (ROADMAP.md)**, the persistent, ordered home of every wish. Each row holds these fields:
- the user's words
- class: size, plus priority when it is not normal
- status
- acceptance criterion [E-3]

When the user speaks a wish, its row exists before anything else happens. It survives even if the session dies the next second. Rows are never deleted. A row closes only with a named exit. At a milestone, a row closed with a terminal exit (landed, declined, or superseded) moves to a dated queue archive, where it stays, never edited, never lost. A **deferred** row is not terminal: it stays in the active queue, carrying its revisit trigger, until the trigger fires or it resolves to a terminal exit. The archive holds only wishes no longer due back. No wish is ever lost. [INV-1]

From its row, the wish follows one path:
1. The classifier reads its size, priority, door, and work-kind, then states them back to the user in one intake line (the paragraphs below explain each).
2. A spec-delta is drafted.
3. The delta is validated against the whole spec. Only genuinely human questions go to the user, batched. Everything else proceeds on the recommended option, marked in the row.
4. The wish is queued, then goes in-work.
5. It lands when the suite is green, guardrails pass, the commit goes in, and the row closes with its acceptance met.
6. The pipeline reports to the user in one plain-language landing line: position on the map, what landed, what remains. [T-1..T-7]

### Intake: classifying and shaping a wish

**Several open questions arrive on one decision page.** They arrive together instead of one at a time in chat.
- The page opens in its own window; the rest of the work carries on while it waits [INV-4].
- Each question is a card — the recommended answer marked, with room to write a different one.
- Once the page comes back answered, the pipeline files it in the project's `docs/decisions/` and folds every answer into its queue row the same session. An answer left unread is a decision lost.
- The person's word settles it; the click only records a first pick: an option picked and then taken back in plain speech is withdrawn, logged as answered-then-withdrawn, and asked again later in plainer terms. A pick made without understanding settles nothing that needs the person's considered word [INV-9].
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

The proposal proceeds on the recommended option; the lane does not park on it [INV-4]. Every cut appears in the same batched report as every taken default [INV-18], and is never silent [INV-5]. A cut surface returned later is a new wish. A scope cut changes scope only, never order: it is not a quick-win mark, and only priority moves the lane [T-11]. No cut touches the delta's mandatory sentences — the fences [T-14], a kept surface's facets [INV-18], the non-goals, and the success measure [INV-20, INV-21]. Scope adjusts richness. [T-15]

**One wish is one user story; a row closes only whole.** A wish carrying several user stories — several distinct things a person will do and see — is split at intake, each story its own row through the full pipeline. This differs from a stage split: a stage slices one story's depth [T-15], while separate stories are never fused into one row. Sub-behaviours of one story — its hover face, its phone face, a backpointer — are that story's acceptance, folded into that same row. The classifier asks the human at intake whether a wish is one story or two, and does not guess [INV-12]. A split loses nothing: every row it produces cites the one spoken wish it came from [INV-1]. [T-17]

**A multi-leg row enumerates per-leg acceptance.** Where a row still carries several legs — a legacy fusion or a harvested batch — its Done-when enumerates per-leg acceptance, and the row does not close with an unmet leg. Half-done is a status, never a landing. The resume file's LIVE-STATE supersession does not compress an unfinished leg out of existence: a leg still open at compaction is restated in full [M-2]. [INV-26]

### Naming and reporting the work

**The system speaks every captured wish back to the user.** This immediate echo lets the user know the request was received and recorded. The echo is one plain sentence that states four things: what was heard, which door the wish entered, the name the work goes by, and its row number — for example, "caught this request; it is a feature; it is called X; row N". A wish that arrives silently — dropped into an inbox as a file, or pulled from a batch — takes its echo in the next status report rather than as an interruption.

**Every status report names each in-flight feature and the pipeline stage it sits at.** The pipeline has nine steps, in fixed order: spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show. Each stage name is exactly one of these nine step names, one stage per step. A feature paused at a stage is reported under that stage's name. "landed" is a terminal state — the row closed completely — and is not itself a pipeline step. The echo also states where the wish sits on the product's feature map, specified in the next rule [INV-37]. [INV-27]

**Every wish is placed on the product's feature map, and the placement is stated by default.** The feature map already lives in the documents the project keeps: the spec's scenario sections and the architecture's nodes together constitute it, so no separate map document exists [E-14]. Each wish's placement is exactly one of three verdicts:
- **changes an existing feature** — the delta extends that scenario section and names it;
- **a new feature** — a new scenario section, plus its own node at the architecture stage;
- **restructure** — the wish fits no existing division cleanly, or fitting it reveals that the modules have outgrown their structure.

A restructure verdict does not re-divide the structure on the spot. It opens its own row — the refactor door when only structure moves, the feature door when behaviour moves with it — and the re-division goes through the architecture stage and its re-proof [E-14]. A placement may report that the structure no longer fits, but only a completed change alters the structure. A bug's placement is the feature it repairs. When the classifier cannot determine a wish's feature, it asks the user, as with any attribute it cannot decide [INV-12]. The verdict is recorded as well as spoken: the wish's row carries a note — changes X, new, or restructure — so the placement stays searchable after the report scrolls away, as the fences stay searchable in their rows [T-14 kin]. [INV-37]

**The outcome does the talking: names are plain, and every handle trails.** Two arms, one law.

- **Naming:** a feature's echo-name is a short descriptive phrase in the product's own words. It says what the thing does, and a reader who missed its birth can parse it cold. Never a private metaphor. A name that needs its story told first is a handle. A real name stands on its own, understood without the story.
- **Lines:** a human-facing report or board line opens with what changed for the reader — what they can now do, see, or stop fearing. This covers chat reports, narration lines [INV-35], report pages, decision pages, and the capture echo, while method-internal docs keep their anchors. Every internal handle — spec codes, row and session numbers, any coined name the reader never chose to learn — may only trail in parentheses. And one fact gets one standalone sentence: a compression that needs the writer's own context to parse is a defect of the line — clarity outranks cleverness.

Bookkeeping numbers are handles too: a test count, a suite size, a version string, or a check tally is never message content. The message says what the number means for the reader — tested clean, saved, the method held — and the number may only trail as a quiet anchor or stay in the records. One carve-out, by law: when the number is the asked substance — a direct question about it, or the done-claim evidence walk, whose claim lines pin artifact and method version [INV-25] — it speaks as the answer: the number itself is the content, this once.

This law and the narration law live in skills a window may never load, so both also have a mechanical voice on the working machine:
- A prompt hook, `scripts/chat-law-hook.sh`, installed beside the clock's hand, injects a one-line reminder of both laws into every prompt. The skills stay the laws' homes; the hook only reminds and never legislates. A window that ignores the line breaks the same law every time.
- Before a human-facing artifact — a report, a decision page, a rendered doc — is shown, `scripts/preshow-lint.py` reads its prose and flags any line that opens with an internal handle (a spec code, a row or session number), so the agent rewrites the line to lead with the reader's outcome before the human ever sees it. It's a warning to clear, never a silent rewrite, and it reads only the shown surface, never the spec's own internals, whose trailing anchors are legal by design.

[INV-28]

**The report law is walked — a live step each time.** Chat has no suite, so the enforcement takes the form of a step actually performed. Before any movement-end or milestone report reaches the human, the agent re-reads the communicator rules and passes the draft phrase by phrase through one question: does this sentence stand for a reader who doesn't live inside the pack? Any pack surface it names either gets explained in the reader's own words, or dropped. Quiet trailing anchors stay legal, since the walk governs what does the talking, never the handles that trail. The walk's one home is the communicator skill, and its acceptance belongs to the reader: a movement-end report that makes the reader ask "what is this?" is the walk not walked. [INV-34]

**Work is narrated while it runs — the third voice between the echo and the report.** The intake has its echo [INV-27] and the landing has its report [INV-28]; between them, work is narrated as it happens — the human leads several windows at once, so otherwise silence is all he gets. While work runs, the agent says each beat worth a sentence as it happens — a pipeline station just passed, a load-bearing find, a change of direction — in one or two plain sentences, in the roadmap's terms (which wish is in hand, what it gives, what just moved), in the same voice as the reports. The mechanical grind stays quiet; narration marks beats, never per-command commentary. The law has three parts:

- **IDENTITY:** every narration beat names the work it belongs to — which wish is in hand and which pipeline station it stands at (outside the pipeline, in research, a harvest, or a docs sweep, the work's own name serves), and whether it mends something broken or builds something new. So a reader dropping into the chat mid-session can tell what's being worked on without scrolling back.
- **DIGEST:** a station's completion is itself a beat by law, and its line carries a short digest of what the station produced, in the work's own words. The spec station says what the delta promises; the architecture station says the shape (what parts, what changed structurally); the test station says what's now covered; the code station says what now works — two or three plain sentences, never the artifact pasted into chat. A station a delegated worker closed becomes the senior's beat the moment its result lands.
- **HEARTBEAT:** when a stretch runs long with no beat — a big suite, a worker batch, a long render — narration says what's grinding and roughly why it's taking so long. A beatless stretch past ~10 minutes owes its heartbeat [default].

The heartbeat has a second, forward-looking face: the offline window. When the coming stretch needs nothing from the human — a local suite run, a delegated worker batch, a long render, a pipeline stretch with no gate or taste call ahead — narration says so before it starts: that he may step away, an honest range for how long (read from the work's known shape or observed runs — an unknown duration is said as unknown, never a guess dressed as a promise), and what he'll be needed for when it ends. When he's needed again, that's a beat too, said plainly, naming the gate or decision that waits. The window is a read on the work, never a dismissal:
- beats keep landing during it so the returning reader finds the trail whole;
- questions born inside the window batch to its end [INV-4];
- a window that ends off its spoken range says so — overrun, done sooner, or blocked on his word alone, the heartbeat's own duty;
- the needed-again beat is a chat line awaiting his return, never a summons (the machinery of reaching an absent human stays outside this law);
- no offline sentence fires when the very next beat needs the human.

Together the trail is the session's time accounting: read top to bottom, it answers where the time went in work terms — token and test counts stay bookkeeping [INV-28]. A narration line is an informal chat message, distinct from a report. It walks no pre-report walk (the walk scopes to movement-end and milestone reports, a deliberate line [INV-34]), it asks nothing [INV-31], and every law of human-facing lines still binds — the outcome talks, handles trail, bookkeeping stays out of the content [INV-28]. Working notes marked as the writer's own stay a separate, skippable register; narration is for the reader, and it replaces no report — milestones still get the full one. The law's one home is the communicator (its narration rule); the personal profile holds only the person's own tuning of it. [INV-35]

### Showing work and asking for decisions

**Anything handed to the human opens with a one-line identifier.** A page that opens in the human's browser at midnight states two things: which project it belongs to, and whether it needs the human's attention. A page that states neither reads as noise.
- The project's name appears in the visible content, not only in the URL.
- The page states what it needs from the human: "needs a word: what, by when," or "just an update, no action."

Every artifact the agent hands over or opens leads with that one-line identifier, whether it is a report page, a decision page, or a rendered doc. The chat line announcing the artifact carries the same two facts. This rule lives in the communicator skill. [INV-51]

**During an away-stretch, artifacts accumulate and one window opens at the end.** When the human has stepped away for an overnight loop or an offline window [INV-35], the agent does not open a browser window mid-stretch. Artifacts accumulate on one page: the stretch's decisions and report page. Mid-stretch re-opening is allowed only as the same page, refreshed in place. This rule lives in the communicator skill, beside the offline window, as the showing-cadence rule. [INV-52]

**The showing channel matches where the session runs.** A session running on the human's machine shows a rendered artifact as a local page in a browser window. A session running remotely runs in the cloud and is read through a browser, so it cannot open a local page. The same content goes through the remote session's own channel instead: an artifact page the host renders for the human, or the chat itself. Either channel carries the same identifier [INV-51] and the same round-trip. The session reads where it runs from what it can reach — the platform, the display, and whose filesystem it sees — and names the channel it picked. Handing a local file path to a remote reader is a defect of the exchange, the same failure as a window that never opened. The personal profile's show line applies to the local case; it is one instance of the general rule. [INV-67]

**The current state of the work is answerable at any moment, in any setting.** The harness's own task list and activity line are a convenience of the local terminal. A remotely-running session, read through a browser, never shows them, and even on a local session they go dark when the work becomes a long run of tool calls, so hours pass and the human cannot tell what is being worked on. The live status therefore lives in the chat, the one surface present in every setting [INV-67], as a short status kept current:
- **Now** — the piece of work in hand and its pipeline stage;
- **Next** — what the queue holds next.

The status refreshes at every stage change and carries a heartbeat when a stretch runs long [INV-35], so a glance answers "what are we working on, and what comes next" whenever the human looks. The harness task list, when the setting shows it, is kept in plain product words as a courtesy [INV-28] and is not the home of the status. On a local session, a rendered status page is an optional richer view of the same Now/Next [INV-67]. This applies to every project the pack runs, not only one host. [INV-71]

**The end of a stretch is delivered so the human cannot miss it.** A report that exists but sits above tool noise counts as undelivered. When a stretch ends — a loop iteration going to sleep, an away-stretch closing, or a session ending — the last rendered thing is one short final line. It carries four fields: what closed, what is next, what is needed from the human, and when the agent wakes. The long report sits above that line. The final line comes last, after every tool call. A page deliverable repeats its identifier [INV-51] in that final line. Delivery is the rule; existence alone does not satisfy it. This lives in the communicator skill. [INV-57]

**A review surface shows its sources and accepts the human's edits.** Anything the agent shows for review carries per-claim provenance, whether it is a dossier, a claims page, or a draft with assertions. The surface marks each claim by where it came from: read from the artifact, the human's own recorded word, or the agent's inference. Inferences are flagged most prominently. The surface is commentable rather than a read-only wall. It gives line-by-line room for the human's word and captures the human's answers. The decision page's saved-answers rule [INV-32] extends to review pages, as one JSON round-trip back to the project. Its home is the communicator skill, beside the decision page rule. [INV-64]

**The human's word on a shown artifact is read as meant, and the human's cuts hold.** The confident-specialist voice at the core of this lesson lives in the promoter's own voice skill, by the human's placement decision; the pack keeps only the general structure. Two clauses follow.

First, a phrasing the human removed in a review round stays removed in every later draft of that artifact. The writer keeps the removal list written where the artifact's project keeps its records — its journal, or the artifact's own notes file — and not only in session memory. A memory wipe does not restore a cut phrasing. A cut word reappearing two rounds later is a defect, however fresh it may look.

Second, a vivid phrase from the human is adopted only as meant. A human sometimes writes mockery of a bad draft rather than guidance, and the parody metaphor can end up baked into copy as if it were prescribed. So before a colorful phrase shapes the work, the writer reads its intent from context or asks [INV-4], rather than assuming it is prescriptive.

The rule's home is the communicator skill. Two of the original wish's bans already live in the pack: no empty drama, which is the no-disclaimers rule; and no approval-begging, since silence is consent [INV-31]. Both are cross-linked from there and not restated. [INV-42]

**Approved text is frozen, and a revision applies only the named correction.** Once the human approves a text, it is settled material. A later revision applies exactly the correction the human named — trim what the human said to trim, swap what the human said to swap — and does not rewrite the surrounding text. Churn of approved material is a defect, related to a reappearing cut [INV-42]. Its home is the communicator skill, beside the removal-list rule. [INV-58]

**The removal list has a mechanical form.** For a host with taste-reviewed artifacts, the pack ships a removal-list template. It holds the human's cuts as dated literals, appended the moment a cut happens and never removed. The pack also ships guardrails guidance for a scanner: a test reads the table and greps the artifact's surfaces, and a removed literal reappearing turns the suite red. The rule stays INV-42's; this is its enforcement. [E-26]

**No question is asked twice, and dialogues converge.** Before any ask, the agent searches the recorded word — the decision archives, the review records, the journal, and the profile. Asking a question a record already answers is a defect. Exchanges converge as well: an answered question closes permanently and is recorded into its row the same session. A problem the human named returns solved with evidence rather than re-described, so round N+1 carries only new material. Its home is the communicator skill's ask rules. [INV-59]

**A taste ask arrives carrying the agent's own researched proposal.** A genuine taste question arrives with work already done. The agent mines the material first: exemplars, precedents, and real options with citations. Then it asks, with a chosen recommendation and its evidence. Asking the human to supply what the agent should have mined is a defect. This sharpens the recommended-option rule [INV-4] for taste calls. Its home is the communicator skill. [INV-60]

### Doors, kinds, and craft

**Priority changes the queue order, and the change is recorded.** A critical bug lands before everything, heading even the waiting-bug line (next section). Critical priority heads the queue whatever its door, so a critical-priority feature goes to the queue head too. Only the bug door preempts the in-work lane [T-9].

A quick win can be promoted: when the lane frees, the agent may take it ahead of larger queued wishes, marking the promotion in its row rather than making it silently. After one promoted landing, the queue head goes next, so a stream of quick wins cannot starve a big wish forever.

An inbox wish is registered at the moment it arrives; that is when it first becomes a row the ordering rules can see. A file's own date never competes with spoken timestamps. Arrival ties resolve by queue row order, top to bottom. Within one sweep, an inbox batch is registered in filename-sorted order. [T-11]

**The door is named before any code is written.** Classification is an explicit step with fixed rules. No one's gut feeling settles it. A row carries three axes, stated together in one intake line: size, priority, and door, plus the work-kind (what the wish builds, covered in the next paragraphs [T-16]). A wish too big for its worth is negotiated in scope, never in time [T-15]. Size, together with priority, says how big and how urgent. The **door** says where the wish enters the pipeline: **feature · bug · refactor · docs-only · skip**. Size and door deliberately share one word: a wish sized "bug" is the bug door — one call stated once — and the door axis adds the other four entries. [T-12]

The door is decided by an ordered procedure. The tripwires fire first, before any judgment:

1. The wish is a **feature** — however casually it is asked — when any of these holds: a new user-visible surface appears; new persistent state appears; a new interaction lands on an existing surface; the touched surface is marked [target] in the spec (the canonical, machine-checkable form of "not yet specified / later surface"; the plain-prose equivalents bind too, but the author writes the tag); the change adds behaviour no spec clause backs.
2. No tripwire fired, but shipped behaviour is wrong against what the spec or product already promises → **bug**.
3. Behaviour stays identical, structure moves → **refactor**.
4. Only prose outside the normative spec changes (README, comments, guides) → **docs-only**. Rewording a spec rule changes what behaviour the spec backs, so it routes as feature or bug rather than docs-only.
5. The narrow case where all of these hold (a single file; no new state, element, or visible behaviour; an existing test level already covers the touched fact) → **skip**.

The tripwire verdict outranks a casual label. A wish called a "bugfix" that fires a feature tripwire is re-doored to feature, and the intake line records it [INV-5]. Queue-cutting [T-9] belongs only to the bug door, so a re-doored wish gets no preemption. The human's word can still raise its priority (priority belongs to the human), but no word lets a feature skip the spec step.

The door is also re-checked mid-work: the moment running work is about to create a user-visible surface or persistent state its current door does not grant, the work stops and the door step fires again. This catches the case where a change sounds like a simple edit until the surface actually exists. The re-doored wish keeps its lane and re-enters the pipeline in place, with no re-queue and no parking — parking stays a bug-preemption move [T-9].

One request lives outside the queue entirely: a request to merely see or try something, with no commitment to keep it, may be built as a labelled sketch (see "A prototype stays a sketch", which holds the ask-when-unclear rule). Casual phrasing does not change the contract: a wish is routed through its door, never refused for being casual, and never hand-built past the pipeline because it sounded small. [INV-16]

**The intake line also names what is being built.** Size says how big, the door says where the wish enters, and the **work-kind** says what kind of thing the work produces, and with it, which pipeline machinery is warranted. There are four kinds today:
- **product** — something the host's own user faces;
- **infra** — tooling that serves the project itself (scripts, hooks, CI, pipelines);
- **skill** — a behaviour document an agent works by (a SKILL.md, a prompt pack);
- **prose** — a document written for a human to read (an overview, an article, a spec's own text).

The classifier calls the kind from what the wish produces, one kind per wish. A wish that genuinely produces two kinds is two wishes, split at intake; a kind the classifier cannot call is asked about, the same as an uncallable size [INV-12]. A host with one usual kind may record it as a host-profile default that the intake line starts from [E-8, E-13] (track-coach's would be product). A host whose wishes genuinely span kinds — live-spec itself ships skills, prose, and infra — records no default and calls each wish on its own.

The vocabulary is curated like the facet list [T-13]: each kind above is earned by real work the pack has already routed (track-coach's widget — product; render-doc.py — infra; the pack's five skills — skill; OVERVIEW.md — prose), and a fifth kind joins only with a named wish the four failed to serve, re-justified at milestones. The law binds forward: a row queued before the kind axis existed carries no kind and owes no retroactive fill. It names its kind the moment it next moves (its in-work claim is its intake for this axis). [T-16]

**The kind scales the steps; it never silently skips one.** The door picks which steps run [T-12]. The kind picks the form each running step takes, never whether the pipeline runs at all. The per-kind meaning of every step — what "architecture" means for a one-file script, what "verify by deed" means for a document a human reads — has its normative home in the build-pipeline skill, one table for every project, and is that skill's own domain [E-12]. This spec sets the contract around it.

At landing, every pipeline step has either applied in the form the table states for the wish's kind, or stood down by name in the landing report (for example, "design-sync — text product, stands down"), so a skipped step is always a written fact rather than an omission. An unresolved kind scales nothing down: while the kind question is still open on the row [INV-12], every step applies in full, because standing a step down requires a named kind to account for it.

No kind may ever change the following: the door law and its tripwires [T-12, INV-16]; the delta's mandatory sentences — fences, facets, non-goals, success measure [T-14, INV-18, INV-20, INV-21]; and ask-at-intake [INV-12]. The kind adjusts the machinery, never the mandatory checks — the same rule a scope cut obeys [T-15]. [INV-22]

**Each step is worked with its craft's standards.** A single generalist working the whole pipeline produces generalist artifacts: a spec that reads like a developer's notes, a matrix that checks whatever was convenient to check. Each step therefore names the profession the agent works it as:
- the spec — a strong product manager;
- the architecture — a software architect;
- the matrix and the tests — a QA automation engineer;
- the code — a senior developer;
- the two prove steps — the prover's own formal-reviewer role;
- commit & show — a careful release engineer whose reader is the human;
- the verify walk — the visitor's own outside eyes [INV-30 kin].

The full step-to-craft ladder has one home, build-pipeline's step list [E-12]. Each artifact is judged by its craft's standards, and the landing report's step accounting speaks in them. The craft, like the step's form, follows the kind [INV-22, INV-30 kin]: on a prose product the code step is worked as a strong writer; on infra, as a tool builder. The ladder names the archetypes; the wish's kind says what their standards look like in its medium. [INV-33]

### Specifying and building a feature

**A feature is specified past what the human knows to ask.** The human says "add a room where photos hang." The human does not say "and decide what happens on a phone," because the human cannot know that's a question. So when a wish's door says feature, drafting its spec-delta walks a fixed sweep of the **standard facets** — the dimensions every visible feature has, whether or not anyone names them:
- layout on a phone or narrow window
- touch where the design assumed a mouse (anything hover-only needs a touch answer)
- the empty, error, and loading states of each new surface
- accessibility: reachable by keyboard, readable contrast
- the performance envelope (at what input size it must stay usable)
- visual hierarchy: the gap between separate things larger than the gap within one thing, and a heading never dimmer or smaller than its body
- two windows at once (the same stored state open twice)
- a missing source (an input file renamed or gone)

The facet list lives in one place, the spec-author skill, one list for every project. That list is curated: a facet joins only with a named real incident it would have caught, and it gets re-justified at milestones. A checklist that grows by taste rots into a forty-row form. This spec binds that the sweep runs, and what counts as done.

The sweep scopes to the feature's visible surfaces. A feature with none — new persistent state only, say a cache — satisfies it with one explicit sentence, "no visible surface — facets N/A," never a silent skip. A wish re-doored to feature mid-work [INV-16] walks the sweep before work resumes, because the late-recognized surface is exactly the one whose facets nobody looked at. A fenced prototype is not swept, since a sketch has no facets to promise [E-17]; the sweep fires when promotion makes it a feature. [T-13]

**Every facet ends as a spec sentence; silence is not an option.** A facet sentence gets written one of two ways. Decided: the human, or the walk's batched questions, called it. Defaulted: the recommended option gets taken so the lane keeps moving. A defaulted sentence carries the literal tag `[default]` at its line end, so a later prover can tell a taken default from a hole, and the matrix derives the facet's test row either way [E-15]. The landing report's defaults list then tells the choice as a plain-words tradeoff in the human's product's terms ("on a phone this gallery stacks into one column — tweakable"). It never pings once per facet and never asks the human to confirm, because silence is consent [INV-31]; the human's veto becomes a new wish.

A facet with no sentence — neither decided nor defaulted — is a spec defect the prover flags. That's the exact hole: hover-only openings, no phone layout.

On an adopted or promoted surface that already lives [A-10], a default is read from the shipped truth and reconciled like any re-engineered claim [A-3], never invented greenfield against live behaviour. The sweep and the axis rule [C-1] split one dimension by time. The sweep authors the facet sentences when the feature is first specified. The axes compose and test them across views once the surface exists. [INV-18]

**A feature is interrogated for how it fits the product — a small prover on the wish itself.** The device facets above ask what every visible feature owes. Nobody's yet asked how this feature sits in the person's path. Path holes ship green because no clause ever promised the way out — enter, browse, re-enter, then stuck at the tenth picture with no way on.

So a feature-doored wish's spec-delta also walks the fit walk, scaled to the wish's kind:
- A product or UX wish walks the visitor's journey: how the person arrives at the new thing, what they do there, where they go next from every state it can be in, what a return visit or entry through another door changes, what neighbouring behaviour it implies (no-repeat needs remembered state), what the feel owes against the approved prototype's bar [E-17], and what next feature it invites.
- An infra wish walks its flows: inputs to outputs, data lifecycle, failure paths.
- A skill wish walks trigger, correction, and when not to fire.

The walk interrogates the feature, never the person. The agent derives each answer from the existing spec and the shipped truth first. A hole that's trivially closable gets closed by the walker, and the closing gets written down. The rest get written decided or `[default]`-tagged, and only the genuine taste calls go out, batched [INV-4, INV-18].

The prover gains the matching focused mode, FEATURE-FIT: given one feature's delta, it walks the journey seams against the whole spec the way CROSS-LINK walks a new surface's seams. The prover already thinks in flows, states, and transitions; this pulls that thinking forward to intake. Lens lists live once, in spec-author's sweep section, curated like the facet list [T-13]. The law binds forward: a landed feature owes its walk at the first landing that touches it, never retroactively en masse [INV-21 kin]. [INV-29]

**A face that can be entered once owes a way back — or a written one-way.** A surface's faces get entered under conditions: a first-visit door, an empty state, an onboarding screen, a one-time banner. A face whose condition can never re-arise is a dead end the state lenses miss. The law: every conditionally-entered face states its deliberate re-entry path, or states the one-way as a decision, by name. Trigger wording is the tell: "only on first visit," "only on first run," "until dismissed" — each such clause owes its return sentence. The prover reads for it, through the entry-symmetry lens in product-prover's stress list. The fit walk's journey lens [INV-29] already asks "where next from every state"; this law extends the question to faces over the visit's lifetime. [INV-50]

**Verify-by-deed walks the visit and watches the feel.** For the product kind, the verify step now includes a named visitor walk: the whole journey as the person will live it. The agent walks the first visit, the return visit, entry through another door, "where am I and how do I move on" from any point, and the exits. The agent also runs a feel pass: the agent judges motion quality — easing, duration, choreography — and each affordance's craft against the approved prototype as the bar [E-17]. Findings become rows or red, never a vibe or a mental note.

The walk's checklist lives in the build-pipeline step-8 product cell [E-12, INV-22]; this clause binds that it runs for anything a person visits. It runs in the form the medium actually has: a browser product walks motion and affordance craft, a book walks its reading path and chapter flow, a CLI its command round-trip. The product's context applies the feel lens as a partial skill, never a frontend checklist forced on prose. [INV-30]

**A taste choice made without asking is told, never confirmed.** While building a feature, the walk makes small taste calls itself so the lane keeps moving — an animation's speed, a button's shape, a caption's wording. The agent writes each one into the spec with its `[default]` tag [INV-18]. The law: the landing report names each choice made without asking, in plain words with an example, marked as tweakable — and that's all. The agent requests no confirmation; silence is consent; the agent re-asks nothing later. The person asks when they want something changed, and the `[default]` tags keep every such choice findable in the spec forever. [INV-31]

**A tunable parameter is set to a sensible default and told, never asked.** Some choices are a knob with a range rather than a taste call — an image's resolution, a batch size, a timeout, a sampling rate. The walk sets each such knob to a sensible value itself and keeps the lane moving, the same way it makes a taste call [INV-31]. It chooses the value for a reasonable balance, cheaper or faster wherever quality allows (for example, a lower image resolution), writes it with its `[default]` tag [INV-18], and names it in the landing report with what it trades. The human tunes it afterwards only if they want a different point on the range; at most the parameter gets updated together later, and re-asking is never owed.

This carries the taste-told law [INV-31] to numeric and config knobs, and it's the same idea the economy ladder applies to cost [T-19]. So the agent never stalls a task on a knob it can reasonably set. It moves every task it can and reserves a real question for what it genuinely can't decide [INV-4]. The push to production rides the same trust: where the human has granted it, the agent ships to prod on its own certification once the work is sound, the push gate resolving to the agent's judgment — live-spec's own already does [M-6] — and the grant stays the human's to give or withdraw [INV-9]. [INV-70]

**The smallest sample is judged before the full artifact.** For a taste-heavy deliverable — voice, copy, visual style, spec prose — the build stops at the cheapest judgeable sample: one paragraph, one card, two sections. The human's word on that sample sets the bar before the full build spends anything. Here's the kin split, stated: the mockup-first entry condition [INV-43] is the human's declared "show me first." This law is the agent's own discipline: build smallest first, even unasked, when taste rules the deliverable. [INV-62]

**A rejected artifact reopens its source.** When the human rejects an artifact, the fix starts at the artifact's source — the spec clause, the card, or the brief that produced it. The agent corrects the source first, then rebuilds the artifact from it. Patching the rejected output line-by-line against an unchanged source is the five-round trap by name, and it's banned. [INV-63]

**What already works is promised before the agent touches it.** When a feature-doored wish touches a surface that already lives, its spec-delta opens with **regression fences**, before the facet sweep authors anything new [T-13]. A fence is one sentence for a neighbouring promise that must stay true through the change — for example, "the catalog still opens on click" or "the player keeps playing across a view switch." Each fence cites the existing spec clause it guards. A fence isn't new law and earns no new matrix row: the cited clause's own row already carries its never-side [INV-6], and the landing's full-suite run proves the fence held.

So "fixed one thing, quietly broke the neighbour" turns red before it ships. The delta thereby splits everything it touches in two: promises that stay are fenced, cited, untouched; behaviour being changed is never fenced — the agent re-authors it as new law through the normal walk.

A fence that finds no clause behind it has discovered an unwritten promise. That promise gets reconciled from the shipped truth like an adopted claim [A-3], written as its own spec fact with its own row, and surfaced, never silently assumed [INV-5]. Likewise, touching a neighbour whose claim is adoption-born and still unverified triggers that claim's reconciliation before it can be fenced.

The wish's queue row names its fences by the anchors they cite ("fences: …"), so "untouched and still true" becomes a greppable claim; the landing line stays its one-line self [T-7]. Fence-authoring belongs to the feature door. The bug and refactor doors inherit only the catching — their full-suite runs exercise every never-side — and a prototype fences nothing because it promises nothing [E-17]. [T-14, INV-19]

**A feature also says what it is not doing — and how we'd know it worked.** Every feature's spec-delta closes with two short sentences. Both are always written — like the facets, silence is not an option.

- **Non-goals:** what's deliberately left out ("version comparison, excluded this time"). "Nothing deliberately left out this time" is itself a valid sentence; only a missing sentence is a hole. A non-goal that narrows what the wish asked for is a scope decision, so it rides the same batched report as every taken default [INV-4, INV-18], never a silent narrowing [INV-5]. [INV-20]
- **A success measure:** how we'd notice the feature worked for its person, a number where one exists ("the producer opens the evidence panel at least once per session"), decided or `[default]`-tagged like any facet, the tag marking provenance only. No matrix row derives from a success measure. The machinery that reads them — KPI dashboards, A/B runs, segmentation — stays [target] under its own queue rows. Until then a measure is a written promise the human checks by eye, honestly labelled so. The quantification questions — is there an analytics tag? how will we measure? is an A/B worth it? — ride the facet sweep's batched report [T-13, INV-18]. [INV-21]

Both sentences bind forward from features specified after this rule lands. An adopted feature owes its pair at the first landing that touches it [A-3], never retroactively en masse. A prototype writes neither — it promises nothing [E-17].

### Parallel lanes, one pen

While the session walks, four things hold:
- Intake is parallel, integration is serial — **one landing at a time, per repo, under one pen**. The **pen** is the right to write the shared truth: the spec, the architecture doc, the matrix, the queue, the integration of a delta into the shared tree, the closing of a row. One lane holds it at a time. Claiming a lane is an atomic committed act. The session commits the row→in-work flip first, then re-checks under the fence [INV-11] right before its first shared-truth write. If that re-check finds a foreign session's committed in-work row, the later claimant backs off and re-queues. Foreign hands never share a repo's pen, so across sessions the law stands as it always stood. Within one assigned session, up to three trains may roll under the parallel-lanes law (below) [T-18]. Every pen-stage still lands one at a time, and a landing commit carries exactly one row's delta [INV-39]. Bounded delegated execution (workers) overlaps as it always did — disjoint brief-named files or an isolated tree, the edit fence armed [INV-11, ACT-3]. A new wish waits its turn unless it is a bug preempting (next section). [INV-2]
- **A pending question for the human never stops the work** — the lane proceeds on the recommended option; the question stays open in the row, revisitable any time. [INV-4]
- **No silent micro-decisions** — every choice not in the human's wish gets either asked, or recorded in the spec and surfaced in the same report. The batched report carries this as its own postcondition: every taken default, trim, and deliberate narrowing of the walk appears in it. A decision absent from the report is silent by definition, whatever the spec recorded. Nothing decided-and-buried. [INV-5]
- **Every landing cites its wish row** — the commit message or journal entry names it, so "why does this exist" is always answerable. [INV-3]

**Trains may roll — one pen writes.** Parallelism was born below the lane: workers split disjoint files, and read-only analysis rode the background while another wish walked the pipeline. This law lifts that parallelism to feature level, where it is safe. One assigned session may hold up to three build lanes in-work at once. The senior allows this only when the lanes are pairwise independent (no surface two of them touch, no spec section two of them must edit) and says so aloud. Opening every additional lane gets narrated, and all rolling trains appear on the departures board [INV-27].

What may overlap — everything that does not write the shared truth:
- a later train's code and tests, each written in its own isolated copy of the tree only (its delta reaches the shared tree through integration under the pen; the brief-named disjoint-file road [ACT-3] stays legal within one lane, whose workers land with that lane's own commit);
- read-only analysis and research;
- a prover run reading committed law.

What always takes the pen, one lane at a time:
- edits to every document both lanes share — the spec, the architecture doc, the matrix, the queue, the journal, and the resume file among them;
- the integration, which brings a lane's delta into the shared tree and runs its gate;
- the closing of a row.

So the document stages of two lanes never interleave mid-edit. Each lane's spec-delta is drafted and proven against the spec as committed law, never against another lane's half-written draft. The pen passes between trains while their long mechanical stages run.

At most three build lanes roll at once without asking [default]: the session does not stop at two, taking the independent work that exists. Beyond three, a fourth lane opens only on the human's asked word. When more independent work waits workable, the session asks whether the human wants another train rolling, and never opens it silently. Read-only background analysis never counts against that cap.

The board shows every rolling train. Each in-flight row keeps its own station line [INV-27]. A lane waiting for the pen says so and names the row it waits behind ("at integration, waiting behind row N"). When several trains want the human's word, the questions ride one batched decision page, every card naming its lane's row [E-22, INV-4].

A bug still cuts the line [T-9]. It takes the pen, and the senior takes over, at the end of the current pen-stage. A pen-stage is never cut mid-edit. Rolling background briefs may finish, and no lane takes the pen back until the bug lands. A milestone's whole-spec operations run with one train only. No new lane opens mid-gate, and a milestone opens only once a single train rolls, after the others land or park first [M-1]. [T-18]

While several trains roll, the landing stays pure: **a landing commit carries exactly one row's delta**. Its gate — the full suite plus the guardrails — runs on a tree holding nothing of any other lane's unfinished work. So half of another train never rides a landing. When a lane lands, the shared truth has moved. Every still-rolling lane's integration then re-checks under the fence [INV-11] and re-runs its gate against the tree as it now stands: landed-first wins, the later lanes re-verify, never the reverse. [INV-39]

Here are the parallel-lanes law's edges, stated once. It fires when another workable, independent wish waits while a rolling lane's long mechanical stage runs. The correction is idle waiting gone: a feature's code hours no longer block another feature's document hours. It does not fire across sessions, nor on wishes that share a surface or a spec section — those still serialize as before. It also does not fire mid-milestone or while a bug holds the pen. Its only face is board and report lines, already governed by the line law; no other visible surface, so facets are N/A [INV-28].

Non-goals: this iteration adds no cross-session double-landing, since foreign sessions still back off; no automatic independence checker, because the senior judges independence and says so aloud; no fourth build lane unasked, since beyond three the human's word opens each next train; and no per-lane sub-board.

Success measure: the first real double-lane run lands both rows clean with the board readable throughout — the human can say at any moment where each train stands, checked by the human's own read of that run's reports [default]. [T-18]

**Lanes are picked by a graph, never by mood.** At queue-take the session reads the runnable head — the next few rows workable without the human — and builds the mini dependency graph. It draws an edge wherever two rows share a surface, a spec section, a skill file, or a doc region. Lanes open on a pairwise-independent set, up to the cap [T-18]. Rows joined by an edge serialize inside one lane. Rows that collide only at their integration — one file, different concerns — may pre-roll their isolated build stages with the integration order declared at claim time: first-declared lands first, and the later re-fences on the new truth [INV-39].

The graph also knows when not to parallelize. Parallel pays only when build stages dominate the pen work, so tiny rows ride serial, and saying so aloud is part of the board. The chosen set and the order get narrated at opening [INV-27]. [INV-49]

A wish can also end without landing, and its row stays in the table in one of three end-states:
- **declined** — the human said no;
- **deferred** — parked with a named revisit trigger;
- **superseded** — absorbed by another wish, so the row points to the absorbing one.

Declining preserves what the declined wish had absorbed. A wish that other rows were superseded into lists them at its decline. Each listed row then either gets declined by name in the same breath, when the human's no covered it too, or returned to the queue as its own row again, when the human's no was about the absorber's shape and not the need. A superseded wish never dies by pointer [INV-1]. [T-8]

What the wishes grow is the **spec (SPEC.md)** — the living statement of what the product is, one surface = one name, everywhere. [E-4]
## Sending feedback in

A person looks at what shipped and something occurs to them. It might be a reaction, an answer, a screenshot with a red circle, or a log file. **Feedback** is anything a person hands back to the project, at any size, any moment, through any channel. The person is usually the host's human. When the host's product has users of its own, their reports travel the same road once a session receives them. [E-28]

The promise is simple: nothing handed in is ever lost, and everything handed in is answered by a route. Every received item lands in the same session, in the home its route owns:

- a wish lands in its queue row;
- an answer lands in its decision archive and harvested row;
- a fix lands in its commit and journal line;
- workshop noise lands in the problem ledger.

Some routes had no home before this section. They get one now: the **feedback ledger (FEEDBACK.md)**, an append-only file beside the queue at the host root [default]. It owns field evidence, plain reactions, and wordless drops that still await their question. Each item is one dated line. The line records when it arrived, who handed it in and through which channel, what it concerns on the feature map, the item in plain words, and where it went.

The session echoes every arrival back in one sentence, one echo per item. A wish-shaped item's echo is the wish echo [INV-27]. Anything else gets a note back saying what was heard and where it went.

If someone mentions an already-recorded item again, the session appends its date to the existing line and changes nothing else. That's the problem ledger's own discipline, applied here. [INV-68]

### Three channels, one contract [T-20]

- **Spoken or typed** — a remark in the conversation, or a note in a file the human points at.
- **A comment on something shown** — decision pages and review pages capture answers as saved JSON [INV-4, INV-64]. Each saved answer is a feedback item; the capture law already names its home, the archive and its harvested row.
- **A dropped file** — a screenshot, a log, or a document. It comes straight from the human in the conversation, or from any outside session through the host's inbox door. Each one arrives as one new file, under the same naming and collision law that wishes use [E-11], and the host's own sessions sweep it in [T-10]. If a file arrives with no words, the session asks one plain question about what it means; the ledger never records a guess.

### The five routes

Every item takes exactly one route, and each route already has its law and its home.

- **Wish** — Ask for new behaviour, and it's a wish. It walks wish intake with its own echo, door, and row; that row is its home [T-12, INV-27].
- **Fix-sized comment** — A fix-sized comment on shown work gets fixed the same session; the commit and its journal line are its home. A story-sized comment queues as a wish instead.
- **Answered question** — Answer an open question, and it closes forever. The session harvests it right then, into the decision archive and the harvested row [INV-59].
- **Field evidence** — React to a shipped feature, and that's field evidence. It lands in the ledger, and the line cites the feature's scenario. The feature's success-measure sentence [INV-21] finally gets a place where real signals pile up — the ledger is the first honest slice of the reading machinery. That machinery itself (measurement plugins, aggregation) stays [target], under its own long-lived row (row 48). Evidence only grows into a wish when the human says so, or a tripwire fires a verdict.
- **Workshop noise** — A flaky tool or a missing dependency is workshop noise; it belongs to the problem ledger [INV-23]. The seam decides it: the product's behaviour goes to FEEDBACK.md, the workshop's behaviour goes to PROBLEMS.md — one home each.

The skill that owns this behaviour is **feedback-intake**, the pack's intake half of the exchange. The pack splits the exchange: communicator carries work out to the human, and feedback-intake carries what comes back. It fires the moment any session receives a handed-in item. It also fires at every inbox sweep, for files that carry feedback rather than a wish.

feedback-intake stays quiet in three cases:

- the agent's own output;
- a question the agent asked;
- something the human merely mentions without handing it in.

When unsure whether a remark was handed in, ask one plain question. feedback-intake never opens a queue row on its own judgment; the wish door owns that verdict. [T-20]

The section's edges, stated once.

### Fences its birth must hold

- The inbox stays one new committed file per outside item [E-11], swept first [T-10].
- The wish echo and intake path don't change [INV-27, T-12].
- Answered questions still close and get harvested by the convergence law [INV-59].
- The problem ledger still holds workshop noise alone [INV-23].
- This section extends the queue's no-wish-ever-lost law, never amends it [INV-1].

### Composition

- Outside sessions never edit the ledger. They use the inbox door, and only the assigned session appends FEEDBACK.md. The write-ownership and fence laws carry this [INV-10, INV-11].
- The ledger is append-only and archives like the queue, never trimmed [INV-1].

### Facets and skill kind

- The feature's surfaces are the ledger file and the chat echo, prose read in place.
- Layout, touch, accessibility, and performance belong to the media that carry them.
- The empty state is a ledger holding only its header, which is healthy.
- Facets otherwise N/A [default].

### Non-goals

- No end-user feedback widget on a host's own product. A site's visitors writing in ride the measurement family (row 48) or their own wish.
- No automatic reading, scoring, or aggregation of the ledger; the reading machinery stays [target].
- No new door mechanics; the inbox is reused as it stands.

**Success measure.** The same item never has to be handed in twice. Every received item is findable in the ledger, with its route, in the same session [default].
## Asking what the product does (the feature map on demand)

Three standing questions describe the product. The departures board reports in-flight work status at every report [INV-27]. Intake places each arriving wish on the map [INV-37]. Those two questions are answered on their own surfaces. This ask answers the third — what the product does today — with one answer containing the whole product map, current as of the request, on demand.

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
## When a bug cuts the line

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

**Postcondition:** the bug's fix is landed; every parked feature is back in work (or landed) in its
original order; no red work was committed anywhere.

## When the workshop itself misbehaves (the problem ledger)

Some noise comes from the workshop itself: the test harness flakes, a dependency goes missing, the shell eats a command, a tool times out. The session retries and moves on — but the same noise then eats the same minutes, session after session.

**The problem ledger** is the host's dynamic list of this operational noise. It lives in one git-tracked file, `.live-spec/PROBLEMS.md` (the template ships in the pack). Within `.live-spec/`, only the checkpoints stay ignored [E-8]. The ledger is born on its first entry.

An entry is a **signature**: a short, greppable plain phrase, such as "element not clickable: #ex-skip" or "zsh eats a bare ===". Each signature carries its dated occurrences and one status [E-24]:

- **WATCHED** — seen once.
- **OWNED** — a named queue row will solve it.
- **AGREED NON-PROBLEM** — dated, the human's word.
- **SOLVED** — its row landed, date kept.

### The ledger walk

The moment noise fires mid-work, grep the ledger for the signature. What the grep returns decides the next move.

- **Not listed:** write one WATCHED line — signature, date, one line of context — then keep working. This write replaces the silent retry. It never takes the lane. A defect of the product is a bug; it goes to the bug lane instead [T-9].
- **Listed (second occurrence):** it gets an owner right then: a queue row (someone will solve it) or a dated agreed non-problem in the human's own word. That verdict belongs to the human alone [INV-9]. Write the recommended owner right away, and let the ask ride the batched report [INV-4, E-22]. The lane never stalls on it.
- **Third recurrence, no owner:** this exposes a defect of the method, one that reaches past a single day. It leaves the host as a wish to the pack's own queue — one inbox file, from a host window [E-11, INV-10] — citing the signature and its dates [INV-23].

After the owner is written, the entry only collects dates:

- A recurrence on an OWNED or AGREED entry just appends its date; nothing else changes.
- Re-raising an agreed non-problem is the human's move — he re-raises it from the growing date list.
- When a landing closes an OWNED entry's queue row, that same session flips the entry to SOLVED. The entry never waits for an audit to learn its row landed.

### Keeping the limp parked

**A limping thing never dams the flow.** A known, owned problem stays parked while every unrelated lane keeps rolling. That's either a recurring defect with a named mechanical owner, or a check held red for an understood, recorded reason. Its ledger line, or the owning row, or an expected-red note in the record, holds it in place: when one thing doesn't quite work, it should leave everything else free to move.

Two rules keep the limp parked:

- Hand-fixing loops cap at the ledger's own two-strikes law: the second occurrence buys an owner, never another hand-pass.
- Once a defect has its named mechanical owner, its instances get serviced in batch: the fence fixes them silently wherever it catches them, then appends one ledger line at session's end. It's never a per-instance ceremony that interrupts the work or the human reading it.

A real new bug still preempts [T-9]. This law governs only the known limp [INV-56].

### Seams

- **Write-ownership.** Sessions write the ledger. A worker reports noise in its checkpoint; the session carries it over. A worker whose brief names the ledger among its files may write it directly. The brief is what states the write-ownership law [ACT-3].
- **Concurrent edit.** Two sessions on one host share the file under the concurrent-edit fence, like any doc [INV-11].
- **Same problem?** Grep and eyes decide whether two entries are really one problem. Signatures stay short so the grep stays honest. One problem found under two wordings merges into a single entry at the milestone compaction.
- **Archival.** At that compaction, SOLVED and agreed entries move to a dated ARCHIVED tail of the same file [M-1]. One file stays the one home, and the ledger never grows unboundedly.
- **Product versus workshop.** This is the workshop's law; the product keeps its own. A recurring product bug re-doors to a feature under the pipeline's rule, distinct by what broke.
- **Facets.** No visible surface, so facets are N/A.

### Scope for this landing

Non-goals:

- No mechanical guardrail yet. The named candidate — a pre-push check that no entry crosses a milestone unowned — earns its row after real usage.
- No automated signature matching.
- The first foreign-host ledgers (tlvphoto, track-coach) open from their own windows. This landing opens the pack's own.

**Success measure.** The next operational hiccup in a live-spec session lands as a ledger line instead of a silent retry, checked at the milestone audit [default].

### Reuse before reinventing

**Before reinventing a fix, search for an existing skill.** Two moments trigger that search:

- **At a project's setup** — founding, or adoption's orient, beside the founding questions [B-2, B-3] — the pack scans the skills already installed and the catalogs it can reach. It looks for matches to the project's kind and crafts, then proposes a fit list with a recommendation. The human's word picks.
- **At a struggle** — a ledger entry reaching its second occurrence [INV-23], a taste artifact rejected twice [INV-62 kin], any failure family that keeps returning — the next attempt waits for one search. An existing skill or published checklist may already own this failure class. Adopt or reject a found skill by name, and record the verdict where the struggle lives: the ledger entry, the kill-list, or the row.

Borrowing follows one practice: invoke a found skill as it ships. Paraphrase a lesson into our own documents and credit its source by name. Verbatim text travels only under its license, with the notice kept. Unlicensed text is never republished [INV-65].
## A prototype stays a sketch

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

When all three legs land, the header's honesty rule holds in both directions: the spec never claims what isn't built [S-0], and the build never contains what the spec does not name. Today only the fence leg is enforced; the rest is promised, marked, and owned by its rows. [INV-17]

### An approved look lives in its artifact

Text cannot carry a feel. A rebuild made from prose alone, with no artifact to check against, can pass every test and still ship a look-alike instead of the approved look.

Once the human approves a sketch as the look, that prototype becomes the **norm** for look and feel. One law with four arms guards it:

1. **The clause cites its artifact.** A `norm: <path>` pointer sits at the clause's line end, beside its anchors. The prose carries the laws; the artifact keeps the look. spec-author owns the pointer's format.
2. **Approval freezes the artifact** into the project's records. A copy lands in `docs/norms/` with a dated provenance line — what it is, when it was approved, and which sketch it came from. The pointer cites this frozen copy. A norm pointer never reaches into a live prototype home, so the one-way fence stays absolute and the sketch stays free to die. [E-17, INV-17]
3. **The build reads the artifact.** When building a surface whose clauses carry a norm pointer, open the artifact before the code step. The landing report records a one-line plan-vs-prototype diff — a missing line is a defect, caught at build-pipeline's code step. The verify step's feel bar reads the same pointer. [INV-30]
4. **The prover reads visual clauses with the norm lens.** It flags a prototype-born clause with no pointer, or a clause contradicting its own artifact. Both belong to the "wordless door ≠ no question" class.

A story can declare that the human must see a mockup before the build starts — "show me first, then build." Write this in the wish's queue row at intake as "entry: mockup-first." Only the human cancels it, by naming it; a general "go build" moves priority but never cancels that condition, which the door step holds.

This rule looks forward only — add a clause's pointer at the first landing that touches it, never retroactively across the whole spec at once. A pointer names only a prototype the human approved as the look; an unapproved sketch stays plain evidence in its fence [E-17], and a text-born clause carries no pointer.

This landing shows no visible surface, so facets are N/A. Non-goals for this landing: no mechanical pointer-grep guardrail (a candidate after real usage); the norm artifact's own format stays free. Success measure: the next prototype-born surface lands with its pointer and its plan-vs-prototype diff line in the landing report, and the look-alike class does not recur. [default] [INV-43]
## Starting a new project (bootstrap)

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

### Founding questions

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

**The project knows what kind of thing it is — and the kind can change.** Beside personal-vs-reusable, founding asks a second shaping question: **what is this project** — a book, a backend service, a static site, a fullstack app, a CLI, a skill pack. Record it in one plain line in the host profile (`project.kind`, the settings ladder's host scope [E-13]). Adoption owes the same ask at orient, alongside the other founding questions [A-1, B-2].

These three intake verdicts stay separate from the per-wish work-kind [T-16]. Three verdicts share the intake breath, and they never collapse into one:

- the project kind says what the product is, and seeds project-wide defaults — the usual work-kind, which facets and feel-lenses apply by default [T-13, INV-30];
- the wish's work-kind says what this wish builds;
- the placement [INV-37] says where it lands on the map.

The seed proposes; a written line decides. If a host already records its own default (`work-kind.host-default` [T-16, E-13]), keep it — the project kind never silently overrides an explicit profile line. The ask always belongs to the human: no personal-profile line can say what a host is, so B-2's profile-seeding arm never answers this question — the agent asks it at founding or orient, every time.

Curate the kind vocabulary the same way work-kinds are curated [T-16]. The list above names the shapes real projects already wear, and a custom kind joins through the queue when a named project the list didn't serve well shows up. Expect custom kinds — the queue is their door.

The line stays alive, continuously updated: the moment work notices the project has outgrown its kind — the static site that grew a backend — update the line on the human's word, and journal it right then, never park it for an audit [INV-36]. A project attached before this law owes no retro-ask; the line arrives at the next landing that would lean on it, like any forward-binding intake law [T-16 kin].
## Attaching to a live project (adoption)

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
   - An existing spec becomes SPEC.md sections — keep the original claims, but mark them
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

### How the skills arrive on a machine

The pack ships one installer, `install.sh`.
- It copies every pack skill into the agent's skills home (`~/.claude/skills/`).
- It's idempotent: it backs up an existing copy with a timestamp before overwriting, and never
  deletes.
- The backup lands in an attic folder beside the skills home, never inside it, so the agent never
  scans a stale copy as a live skill — the attic principle applied at install time.
- The installer writes exactly what A-7's record clause writes to `.live-spec/`. Installing and
  recording are two halves of one seam [E-21].

### How the machine learns a newer pack exists

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
</content>
## One rulebook behind the skills

Open any skill in the pack and the same working rules greet the reader. Until now each skill carried its own near-copy of them. Copies drift, and the pack's own sweep proved it twice: the anchor convention was told two ways across skills, and the concurrent-edit fence appeared only in the adoption text, though every skill that writes shared files needs it.

The five rules every skill works by are these:

- **Ask, never guess** — when a fact is missing, ask for it.
- **Plain words, with the code trailing quietly** at the end of the clause it anchors.
- **One surface, one name** — a thing is called the same everywhere it appears.
- **One canonical home per fact** — each fact is stated in a single place.
- **A junior resumes from a checkpoint** after a cut-off, picking the work back up.

**So the shared rules live once, in the base skill.** The base skill is the pack's shared rulebook, and it sits beside the working skills in the folder `live-spec-base`. The package itself is the source; the standalone repos are read-only mirrors of it [D-4]. The base states each shared rule normatively, right next to the package's default settings [E-13].

Every working skill opens with one line. That line names the base skill and the base version the skill was written against. This version pin is swept in the same session that bumps the base, so it never goes stale. After that line, the skill references the shared rules instead of restating them.

A working skill elaborates only its own domain. The communicator skill, for example, teaches how to speak plainly. The rule that we speak plainly at all belongs to the base. A skill used standalone, outside the pack, still stands on its own: the opening line reads as plain advice, and nothing in the skill's own domain needs the base to be installed [E-12].

As the pack evolves, one thing stays true. **A shared rule has exactly one normative home, the base skill. A second full statement of it inside a working skill is drift, a defect to fold back.** The compaction pass prunes restatements older than the base at milestones, one skill at a time, so no single risky rewrite is needed [M-1]. [INV-13]

**Every place the pack lists its skills names the same complete set.** That list lives in several reader-facing spots: the working-skills sentence up top, the closing lists the skills carry, and the README's table. A list is exactly the kind of fact that drifts. The communicator's closing list was once found naming four skills after the pack had grown past six, with two skills missing since their birth. A check runs at every commit, and a list that misses a skill goes red [INV-66].

## Who decides what

### Human authority and evidence

**The human owns taste, design, irreversible calls, publish and push gates, domain wording, and the human's own working contract.** [INV-9] [ACT-1] The settings ladder resolves to that contract, as described below.

- The human's personal profile holds the lines about the human — proactivity mode (ask-at-max | max-proactive), trust level, language, domain vocabulary — and follows the human everywhere.
- The **host profile**, at `.live-spec/profile.md`, narrows those lines for one project, when the human says so. It is created at attach and lives git-tracked in the host repo, like the adopt artifacts [A-8]. Inside `.live-spec/`, only the checkpoints stay ignored [ACT-3] [E-8].
- Communicator reads the resolved contract before every human-facing exchange; it resolves the whole ladder, never just one file [E-13].

**Mode and trust are written only on the human's word.** The agent may propose them; it never sets them, and never raises its own trust or proactivity level. [INV-9]

**A done-claim is answered by walking the evidence fresh each time, and it carries the method version it was done by.** A fluent story can answer any done-claim — "did that project run the tests by the method?" — and the story might even be right, but it does not distinguish verified from narrative, which is the whole point of the method. So no one answers a done-claim from memory: every claim pins to a checkable artifact, walked now — an adoption record, a prover record, a suite run with its count, a git commit, a matrix row. This is the claims-need-primary-source rule, applied to the answering exchange itself.

The answer states plainly what the walk verified, apart from what it merely asserts, and it names the method version the work was done by — the pack and skill versions read from that host's installed set (the version homes, [M-7]). One claim line reads claim → artifact → version, for example: "suite green — 795 tests, tonight's run, commit `193d39d` — done by live-spec 0.8.x, prover 0.1.8." If the host has no installed set (never adopted, or the work predates adoption), the answer says exactly that: an absent version is itself an honest answer, never an invented one. [INV-25]

### Settings and the ladder

**Settings climb a ladder of four nested scopes, and the narrowest word wins.** Every way the pack behaves for the human is a named setting, and each setting has a home in exactly one scope, depending on what it describes:

- about the pack itself → the **package defaults**, each value stated in the base skill beside the rule it tunes [E-12];
- about the human, following the human across every project (language for docs/commits vs. conversation, proactivity mode, trust, the human's domain vocabulary) → the human's **personal profile**, one file per human at `~/.claude/live-spec/profile.md`;
- about this project → the **host profile** [E-8];
- about right now → the **session scope**, the human's live word in one conversation.

The scopes nest: the package holds every human, a personal profile holds every project that human touches, and a host holds every session run inside it. A setting made at a broad scope is inherited down through the narrower ones, until a narrower one overrides it on the human's word — an all-English project overriding the human's Russian-chat line, or a "today, answer me in English" overriding both for one sitting. Resolution reads from the narrowest scope out: session beats host beats personal beats package default.

Profiles are re-read at the same freshness points as skills [A-7]. When a profile line falls outside the current pack's vocabulary (written under an older vocabulary), the pack ignores it aloud: a dated note in the host's journal, plus a line in the session's next report. The journal half is durable, so a session that dies before its report still leaves the trace, never a silent drop, never an error. [E-13]

**No override is ever silent.** An override exists only as a written line in its profile file: setting one leaves a dated journal note in the home it governs — the host's journal for a host line, the package's journal for a default change. This is the no-silent-micro-decisions rule [INV-5], applied to settings. Live-spec's own push gate [M-6] is the worked example: the package default asks for a full prover pass before a minor bump, and live-spec's own host contract tightens that to "before every push" — recorded, visible, never assumed.

The session scope is the one that's never a file. A session override lives only in the human's spoken word and dies with the conversation; the agent never writes it anywhere on its own. If it should outlive the session, that's a promotion into the profile it describes (personal or host), made on the human's word and journaled like any other override. An announced self-compaction [M-2] carries the live session lines forward in its summary. A full wipe ends the sitting, and the session lines die with it by design — that loss is the human's own move, never the agent's. [INV-14]

**The human's profile is the one home of the personal layer, and the global instruction file is a thin loader.** Everything personal — who the human is, how the human likes to be spoken to, the human's standing working rules — lives in the personal profile, gathered in one place. The machine-global instruction file (on this stack, `~/.claude/CLAUDE.md`) shrinks to a thin loader: it points to the profile, and states only the bootstrap lines that must hold before any pack file loads. The which-project disambiguation rule is the type specimen — the rule that stops a session writing into a foreign repo can't itself wait for that repo's files to load. The loader is the one home for those bootstrap lines, and the profile never restates them. [INV-13]

Migrating an existing rule file into this shape is a fork by scope — each rule moves to the scope it describes:

- a method rule the pack already states stays the pack's (a second copy is drift [INV-13]);
- a personal line moves to the profile;
- a project line moves to that project's host profile.

A rule-by-rule mapping proves the move lossless, and the old file stays in the attic [INV-7], so one move rolls the whole change back. The fork writes only what the running session owns: pack rules land in the pack, and the personal profile lives on the human's machine, outside any host or pack repo — a private repo the human owns may serve as its git home.

Sitting outside any repo fence [INV-11], a promotion re-reads the file immediately before appending, and that git home is its recovery net. A project line becomes a written migration note, and the project's own session lands it at its next update — so nothing in this migration writes a foreign repo [INV-10]. [E-16]

### Delegation and workers

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

**The proposal is advisory, the senior may override per wish, and the override is logged.** [D-2] A brief that looked mechanical but hides a real decision routes up; a rare over-cautious default routes down. Either way, one line rides the checkpoint and the landing report: proposed tier → chosen tier → why. This assignment-time override is distinct from ACT-3's failed-acceptance escalation — one is the senior's choice before the work, the other a runtime bump after a miss. Both get logged, on different lines. A silent tier change is the defect this closes.

The router never hardens into a mechanical gate the senior cannot overrule, and it never touches the human's gates or ACT-2's ownership of judgment. No visible surface — facets N/A.

Non-goals:
- no token meters or numeric budgets (the rung stays qualitative [T-19]);
- no fourth tier and no renaming of the three;
- no auto-routing that overrides the senior's word.

Success measure [default]: the first routed landing names, in its report, the proposal → choice → why for each delegated unit, and the human checks it by reading it. [INV-69]

**A worker's green gets a second pair of eyes, and verify can turn adversarial.** A worker's report is a lead, no more. It never counts as evidence. On a large delegated landing the blind spot is structural: the same head that wrote the brief reads the result, so "tasks completed, goal missed" can ship green. So the verify step carries an adversarial option: a FRESH-context checker is briefed with the SPEC sentences the landing claims (the anchors) and the artifact paths, never the worker's summary, never the senior's plan. It opens on the hypothesis "tasks completed, goal missed" and walks each claimed fact up a fixed ladder:

- exists — the artifact is there;
- substantive — real content, checked against the pipeline's step 8 grep list (TODO / FIXME / placeholder / lorem / hardcoded sample / empty body);
- wired — reachable from the surface that claims it;
- flows — real values move end to end.

Findings become rows or red, never a nod. It fires mandatory when the code step was delegated and the delta is surface-sized (a new surface or a multi-file behaviour change); anywhere else it stays the senior's option. A skill or prose landing walks the same ladder in its kind's form — the checker re-reads the shipped text against the spec sentences. The checker is a worker like any other — contract, checkpoint, ledger duty [ACT-3] — and its verdict rides the landing report. [INV-46]

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

**A brief is sized to its worker's head.** A brief targets a bounded share of the worker's context, and the work splits above it. The default bound is concrete: the brief's own text stays within ~300 lines and names at most ~8 files to edit [default]. Above either limit, the work splits into staged briefs. A brief passes paths, never inlined file bodies — the worker reads its own truth from disk, and an inlined body goes stale the moment a sibling edits the file. [INV-55]

## From the spec to the tests: two layers that must not be skipped

**The test-author skill owns the test method; build-pipeline just calls it.** test-author runs the matrix derivation and the test writing (the pipeline's steps 5–6). It keeps the level ladder (string / DOM-text / browser-computed / pixel), real-artifact assertions, red-first proof, the pinned skip-set, and traceability as a standing test. build-pipeline calls test-author the same way steps 1–2 call spec-author and product-prover: the method lives in the skill, the pipeline keeps order and gates [E-27].

The spec says what the product is. Tests prove facts about the shipped artifact. Two documents sit between them, and if they stay implicit, they get skipped — a lost layer.

**ARCHITECTURE.md describes how the product is built.** It is a short list of named nodes: pipeline stages, modules, surface owners.

- Each node carries one responsibility and one name — the one-surface-one-name rule, applied to structure.
- Every spec fact belongs to exactly one node.
- In a live codebase, every node pins to its owning place. The named thing is the pin: a function, a marker comment, a selector, a heading. The `:line` beside it is a convenience cache and can lag, so the name is resolved and a drift check re-greps it. Skip that and pins rot silently — a wrong-with-confidence pin is worse than none.

Drafting the architecture is where spec claims are reconciled against shipped reality. Every pin comes from a command that was run, never from the doc's own prose. It is written from the proven spec (template: `ARCHITECTURE.template.md`), and, like the spec, proved before anything derives from it — a product-prover pass with the architecture lens. That lens checks three things:

- every spec fact has an owning node;
- no node stands without spec backing;
- every seam between nodes is named.

Keeping the doc up to date:

- A large or surface-class wish updates the doc before the matrix is touched. A bug or small wish just cites the node it lands in.
- A fact with no owner yet gets assigned to the nearest fitting node, recorded in the doc. Assignment alone triggers no re-prove, so the fix still lands.
- Re-prove exactly when the structure changes.
- The doc stays iterative: it maps the product as it stands, plus the landing in flight. A node exists for what ships today, or for what the spec already promises under an owned row (marked [target], pin empty). Never design it milestones ahead — a speculative node is unbacked structure. Re-carving the whole map is legal: it arrives as its own row under a restructure placement [INV-37], walks this step, and gets re-proven [E-14].

**The architecture owes numbers, not just names.** The doc states measurable quality budgets for what it builds, plus each budget's instrumentation home — where the numbers get measured and where a human reads them (an export, a debug view, a report). What is measurable depends on the project's kind [INV-36], so ask "what does quality mean here, in numbers?" before writing any:

- a user-facing product — paint and interaction times ("first image within 2 s on a cold visit");
- a backend service — latency, throughput, error rate;
- a CLI or pipeline — run time on a typical input, and per-unit cost;
- a skill pack — its evals' pass rate and suite wall-time;
- prose — whatever honestly has a number (a reader reaches X within one scroll).

Where a quality has no honest number, say so by name instead of inventing a vanity metric. A budget counts only once a matrix row at the right level can see it — a hope in prose does not. A surface with no budget and no instrumentation home is a derivation defect, flagged like an unowned fact. The numbers are the host's taste: the architecture proposes them with a recommendation, and the human's word sets them at the surface's first budget landing. Like the two layers themselves [INV-15], this duty binds from the first landing that touches the surface after the clause exists, never retroactively [INV-41].

**The matrix is derived, never just filled in.** The matrix [E-5] organizes rows by **architecture node × spec fact** — a structured grid: every fact gets at least one row, and every row pins a test level. Derivation closes with the **coverage validation** — a checklist that lives in the matrix template, and it is walked:

- every spec anchor appears in ≥ 1 row;
- every artifact-inventory entry owns ≥ 1 rendered-level row;
- every visibility / layout / colour / interaction fact sits at level ≥ browser-computed;
- every node carries its negative-side rows [INV-6];
- no row cites an anchor or node that no longer exists (stale rows retire, they never vanish).

A fact with no row, or a row at too weak a level, is a derivation defect. The prover catches it at derivation time, before any user hits it [E-15].

While both layers live, one rule holds: **no wish lands whose facts lack an owning architecture node and a matrix row at the right level.** The bridge from spec to tests is walked layer by layer, never jumped. A project that predates these layers brings them up as an owned landing, and the invariant binds from the landing that creates its ARCHITECTURE.md and matrix, never retroactively [INV-15].
## The machines that hold the bounds

What keeps "it works" honest — each one a named machine:

- **The matrix (TEST_MATRIX.md)**
  - Every fact gets at least one row, and each row is pinned to a test level [E-5].
  - Rows are organized by architecture node × spec fact, produced by the derivation method above [E-14, E-15].
  - Each row states both sides: what the fact does, and what it must never do. That negative side is the regression fence [INV-6].

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

### The push gate's reach and its blocking contract

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
## The package repo: who may write, and two sessions at once

live-spec runs on its own method: this spec, this queue, and these rules govern live-spec's own development. The pack repo's push gates run mechanically on installed hooks — a fresh prover record, a green suite, anchor ownership, and matrix coverage, all under `guardrails/`. The host-facing checks stay [target] with E-6. [M-4] That makes its repo a shared surface.

**The developer's own machine keeps its skills fresh by a named step, run deliberately.** The repo is the source [D-4]. The installed copies under the agent's skills home are mirrors. A session that edits a skill syncs the installed copy the same session, through the named tool `scripts/sync-skills.sh`. That tool copies each repo skill over its installed twin, and it reports every version change old → new — the exact line A-7's re-read rule fires on. A hand-copy is the anti-pattern the tool retires: it syncs silently, so nothing tells the next breakpoint what changed. [E-23]

**Only a session assigned to live-spec itself writes this repo** (spec, queue, journal, skills, templates, adopt procedure). Every other session is read-only here — a host adopt run, a skill install, anything that merely reads the package. It has exactly one exception: creating a new wish file in the inbox. The test is crisp. If the session cannot say "the human asked me, in this conversation, or via a standing routine the human created for live-spec, to change live-spec", it does not write. A host run's story lives in the host's journal, never here. [INV-10]

**The inbox (inbox/)** is the parallel-safe intake door for wishes and feedback born outside a live-spec session. Each item arrives as one new file, named `YYYY-MM-DD-<source>-<slug>.md`. If the name is taken, append `-2`, `-3`, and so on — the same one collision law, base rule 18. When two sessions race one slug, they add a short session token to the source mark. A file holds a few plain lines, and it never edits an existing file: creating a fresh file cannot collide, while shared files can.

The outsider commits its one new file — a commit touching inbox/ only, its message naming the source. That commit is inside the read-only exception. The door is host-general: every host carries its own inbox/ under the same law, swept first by that host's own sessions. That is what keeps "no wish is ever lost" [INV-1] true when two contributors' sessions share one host. [E-11]

A live-spec session sweeps the inbox as its first act. It harvests each file into the home its route owns — a wish file into a queue row as always, a feedback file by the routing law [T-20]. An item must never sit durably-recorded but operationally invisible. The harvest commit removes the file; git history keeps it, and this internal removal is not an attic case, which protects host files. Each harvest is one commit that both lands the route — the row, the ledger line — and removes its file. The landing names the source file. So an interrupted harvest commits nothing and leaves the file untouched for the next sweep, which harvests it exactly once. A committed harvest leaves no file behind to re-harvest. So "spoken means it exists" holds without the outside session touching the queue. [T-10]

**Before writing to a repo — and again before every commit** — the agent re-checks `git status` and HEAD against what it last read. Suppose HEAD moved, or the tree holds changes it did not make. Then it must stop, re-read the changed files, and only then proceed surgically — or back off to the inbox. New files under inbox/ are the expected benign case; the fence stays clear for them. The agent never pushes while another session is known to be live in the repo; push coordination belongs to the human. This applies to live-spec and to any host repo two sessions might share — the concurrency axis of the composition rule, made mechanical. [INV-11]

## The rhythm: breakpoints, milestones, pushes

### Breakpoints, resume, and milestones

- **Safe breakpoint (end of every movement):** every movement ends the same way — replace the NEXT_STEPS live state (never stack it), add a dated journal entry, and commit. Session memory can then be wiped with zero loss. NEXT_STEPS may be gitignored, so the journal entry is the durable net. A long session should take this offer. At a breakpoint the agent compacts its own context and says so, never silently. A full wipe or clear is the human's move. On the way back, re-check skill freshness [A-7]. [M-2]

- **The resume file is a digest with a hard cap:** the agent reads NEXT_STEPS in one minute at a cold start — growth is a design failure. The whole file holds at most 100 lines [default], and a suite check owns the number. It goes red on a bloated file — proven with a synthetic one. The cap and the restate-every-open-leg law [INV-26] are reconciled by form, never by dropping content: the agent restates an open leg as one terse line —
  - its name,
  - what stays open,
  - where the detail lives.

  The detail itself flows to the journal, the queue row, or the record the line points at. Compaction moves prose to its home; it never silently drops an open leg. [INV-48]

- **Milestone (minor gate):** a milestone runs the full gate:
  - full spec re-prove;
  - matrix audit: re-walk the coverage validation [E-15] against the current spec and architecture;
  - surface-composition check;
  - re-run skill evals [E-19];
  - walk the pack's skills through skill-creator, the skill-making skill. It checks format, frontmatter, and the description-triggering lens — the craft of the skill file. Our evals already test behaviour; this checks the craft. Fold or reject each finding, with a written reason, in a dated record.
    - A newly joining skill walks this at birth, before it ever reaches the gate.
  - doc compaction: strip redundancy from spec/matrix/queue/skills/ledger [E-24], and sweep the test suite the same way. Delete a duplicate or superseded test only when the matrix audit shows its rows still covered by a live test. Nothing grows unboundedly. Queue compaction archives closed rows, never deletes [INV-1].
  - re-list every open human gate and every unharvested inbox/ file, one line each;
  - re-check the formal index against the prose — it's a derived map, never a second truth;
  - re-pin the derived docs' headers to the spec version, then prove them;
  - **the thin loader stays thin** [E-16]: re-read the personal layer's global instruction file line by line. Every line must pass one test — must this hold before any pack file loads? The audit report states the line count. A rule that survives there without passing the test migrates to its real home (profile or pack); it never lingers. [M-1]

### Versioning

- **Documents are versioned** like code. The queue and this spec carry dated versions, so a reader can always tell which roadmap version a decision was made under. [M-3]

- **Versions have named homes.** The package uses a `VERSION` file at the repo root. Each skill carries a version line in its SKILL.md frontmatter under `metadata:`, where the skill-format validator reads it. A host records its installed set in `.live-spec/` at attach and on every update. The freshness check [A-7] compares version against version, exact strings rather than bare file times — its "old → new" journal note is now writable. [M-7]

### Time discipline

- **Time is read off the clock, never invented.** Every date a session writes — a file name, a journal or queue stamp, a ledger occurrence — comes from the machine's clock at write time. In doubt, git is the arbiter. The rule takes four forms:
  - **File and journal dates (mechanical, pre-push):** no repo file name, journal entry heading, or ledger date may sit later than the current clock. A future-dated stamp turns the suite red as a real defect. Prose that quotes a past incident's wrong date stays legal.
  - **Same-day times (mechanical, at commit):** the check reddens any added line that pairs today's date with a clock time later than the commit moment. "Pairs" means the adjacent stamp shape (`date [~]time`), so a line that legally quotes another moment's time beside today's date stays green. The commit clock is the reference, so the check can't race. The known cost is deliberate: a future plan is spelled out without writing it as a date-time stamp.
  - **Chat timestamps (law only, no mechanical fence):** a human-facing timestamp — the [HH:MM] a reply leads with, or any moment spoken to the human — is read off the clock at write time, never continued or extrapolated from an earlier stamp. This law lives in the communicator skill, where the human-facing exchange shapes live. Quoting a past moment's recorded time stays legal here too.
  - **The mechanical hand for chat:** a harness hook on the working machine — `scripts/clock-hook.sh`, wired as a prompt hook in the host's settings — injects the wall clock into every prompt's context, so every lead stamp is read off the machine's clock. Where the hook isn't installed, the law above stands alone.

  [INV-24]

### Push and CI gates

- **CI mirror.** The guardrails' native home is the local pre-push hook. A host may also mirror the same checks in its CI, such as Jenkins or GitHub Actions, as a second net. There is one source of truth: CI runs the same scripts and never redefines them. The second net runs the full set — the reach map [INV-45] is a local latency optimization, never a CI shortcut. The pack repo's own workflow (`.github/workflows/gates.yml`) is the worked example; host guidance lives in the guardrails README (ROADMAP row 14). [M-5]

- **Push gate for live-spec itself.** This repo is public and the method's own flagship, so every push is preceded, in the same session, by two steps:
  1. the concurrent-edit fence [INV-11];
  2. a fresh whole-spec re-check — a product-prover pass over SPEC.md as it stands, with its record landing in docs/prover/ before the push.

  The record name is `YYYY-MM-DD[-suffix].md`, and the suffix is mandatory when the date's file already exists. Must-fix findings are folded before pushing. Folds produced by the gate's own pass do not re-trigger the gate; they ship with the same record. The rest become queue rows. No re-check record for the pushed state means the push should not have happened. The record enumerates the folds applied from its own pass. A fold stays local to the sections its finding named; a fold reaching wider re-triggers the gate. [M-6]

### Scaling process to the delta

- **Process bookkeeping scales to the delta — the record's reach map.** A tiny row pays the same fixed bookkeeping as a whole surface: its own claim commit, its own full-page re-check record, its own journal chapter, and a resume rewrite. That runs roughly forty percent of its wall time, and none of it is the safety net. The principle: an iteration should run long only when the work needs it — where it doesn't, find what can be cut without sacrificing quality.

  So the reach idea [INV-45] applies to process too. The re-check before a push keeps its rigor always — previous records checked, the delta walked, a verdict — but scales its form:
  - a small delta (skill, prose, or infra kind, with no new surface and no structure change) ships a short-form record of three lines: previous records clean; the delta in one line; the verdict;
  - a surface-sized or structural delta keeps the full walk.

  Claims batch per declared lane, one commit. The journal chapter and the resume rewrite come once per landing batch, never per tiny row. The irreducible core stays fixed regardless of scale: the law's own text written well, the red-first test, the delta's cross-link prove, and the gates. That is quality itself, never scaled. [INV-61]
## When money or time run short (the economy ladder)

Rigor costs money and time: suite runs, prover passes, senior-model hours. Today the pack always spends full rigor. This section names what a tight budget may legally shed, so economy is a setting the human moved, never an improvisation under pressure. [T-19]

The pressure lives as one setting on the ladder: `budget.pressure`, with package default `full`. It moves only on the human's word: a session's word for today, or a profile line to stand. This works exactly like proactivity and trust [E-13, INV-9]. When the human names money or time pressure, the agent may propose a rung. The agent never sets one.

The pack surfaces the choice before pressure arrives. At a project's setup, whether founding or adoption, the pack asks the economy rung, or tells the standing default, alongside `project.kind` [INV-36]. The preference is the human's from day one.

Three rungs each name their legal sheds. Every shed the agent actually takes is said in the landing report. A silent economy is a silent micro-decision, and the landing report exists to prevent it [INV-5].

- **full [default]** — the full suite runs at every landing gate. The prover runs at its recorded cadence. The worker router picks tiers by the routing rule [INV-69].
- **lean** — mid-work test runs may scope to the touched architecture node's rows. The full suite still runs at every landing gate and before every push. Surface-add prover passes stay CROSS-LINK. A full pass owed by the default cadence may defer to the next milestone; the agent writes the deferral as a dated debt line in its queue row, never just from memory. Mechanical work rides one worker tier cheaper when the brief is airtight [INV-69].
- **tight** — everything lean, plus landing gates may batch: consecutive small landings share one full-suite run at the batch's end. Each landing commit still carries exactly one row's delta [INV-39]. A red at batch end bisects by landing order before anything else lands. Even so, a push still requires the full gate green at HEAD [M-6]. The cheapest sufficient worker tier is the rule, and senior hours go to judgment alone [INV-69].

What never bends at any rung — the never-bend list, stated once [INV-40]:

- the door law and its tripwires: poverty, like urgency, moves priority, never the door [T-12, INV-16];
- red-before-fix: a bug still gets its failing test before its fix;
- the human's gates: irreversible moves, publishing, authored content, taste [INV-9];
- the landing report, carrying its taken-defaults and its named sheds [INV-5, INV-31];
- landing purity: one row's delta per commit, whatever the batching [INV-39];
- the push gate: work leaves the machine at full rigor only. Every check the diff can reach is green at head, per the reach map [INV-45], plus the host's recorded prover cadence [M-6];
- the safety net that no work-kind and no scope-cut touches: poverty is its third non-toucher [T-15, T-16];
- narration: it is cheap and stays whole at every rung [INV-35].

An explicit host line outlives any rung. A host profile pinning a tighter cadence keeps it even under `tight` [E-13]. Non-goals: no numeric budgets or token meters, since the rung is qualitative and moves by the human's word; and no automatic rung-switching. Success measure [default]: the first budget-named session names its rung and its sheds aloud in its landing report, checked by the human's read [T-19].

## Publishing — the deposit owes what its kind owes

Sooner or later a piece of work leaves the machine: a repo goes public, a skill enters a plugin directory, a release is cut, rendered cards go to a **design project**. **A publish owes the reader what the artifact's kind owes.** This work-kind axis is already used at wish intake; here it applies again at the door of publishing [T-16].

### What each kind owes

Each kind owes its reader a different minimum:

- a **skill** shows how to install it, the commands to run, and when to use it and when not;
- a **tool** shows real runs with real output;
- a visual **product** shows fresh screenshots — a stale screenshot is a false claim in picture form;
- **prose** shows its reading path.

A comparison or a diagram joins only when it carries the argument; it never rides along as decoration.

### The checklist

The publish skill owns the per-kind checklist — the pack's fifth working skill [E-12]. This spec sets the contract the checklist follows. Nothing gets deposited outward without passing the checklist first, and the walk's result rides the landing report like any other step [INV-22].

### Targets add steps, never remove the minimum

**Each publish target is a plugin that embeds its own steps into the walk.** For example:

- GitHub brings a README-at-the-door plus release notes;
- a plugin directory brings its manifest and forms;
- the design project brings its cards [E-18].

The target adds steps. It never removes the kind's owed minimum.

### Gates already standing

The checklist never bypasses the gates already standing. The human's publish gate guards anything irreversible or outward (base rule 17 [ACT-1]), and the host's own push gates guard the push [M-6]. The checklist runs before the gate, so by the time the human approves, it is already worth approving [E-20].

### A version push re-opens the shopfront

**A version push re-opens the shopfront.** Every push that ships a new version changes the truth a public reader will read tomorrow — even when the diff never touched a doc — so the shopfront rides every push. The README's claims (behaviour, counts, commands, version homes) still have to match the truth just pushed. The kind-owed visuals ride along too:

- a skill pack re-checks its diagrams and flow pictures;
- a visual product re-shoots what changed on screen;
- a tool re-runs its example.

A stale shopfront is a false claim, exactly like a stale screenshot [E-20].

This shopfront check is the publish skill's checklist, read at push scale — same one home, no second checklist. The pipeline's commit-and-show step points at it, and the walk's outcome rides the landing report [INV-22]. When a push's changes touch none of the shopfront's claims, say so in one line: "shopfront checked — current." Find a stale claim and fix it before the push. Freshness is about the claims the README makes; styling is a separate concern.

### Non-goals

Non-goals this landing: no mechanical README-vs-diff checker, since the reach map (row 147) is the candidate owner; and no auto-regenerated images. Success measure: no push lands whose README claims an older behaviour or count, checked at milestone audits [default] [INV-44].
## Composing across axes

Some parts of a host project hold state: a screen, a panel, a saved file — anything the user can change and find again later. Call each of these a **stateful surface**. Review every stateful surface from a fixed list of angles, called axes. Each axis is one question about the surface's behavior:

- in each view
- in each mode
- at each user tier
- at each viewport size
- when it is closed and reopened
- concurrency, wherever two writers can genuinely act on the surface at once

A surface's spec is complete once every axis on the list has an answer.

### Document provenance (the adoption axis)

Adoption adds one axis: **document provenance** — where a spec claim came from.

- A claim is *native* when it was written fresh under live-spec. It is trusted from the start [C-1].
- A claim is *re-engineered* when it was recovered from documents the project had before adoption. It starts unverified and stays unverified until it is reconciled under the adoption rules, which pin it to real code or remove it [A-3].
## Open decisions

- ⟨DECIDE⟩ attic/ layout: flat with a manifest and source-dir prefix on collision (current pick) vs dated
  subfolders — revisit at the next real adopt run. [D-1]
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
| INV-35 | while work runs, beats are narrated as they happen — a station passed, a load-bearing find, a turn — in plain roadmap terms, the reports' voice; every beat names the wish and station in hand (identity); a station's completion is a beat whose line digests what the station produced (digest); a long beatless grind gets a line naming what grinds (heartbeat), and a coming stretch that needs nothing from the human is told as an offline window — step away, an honest range (unknown said as unknown, never a guess dressed as a promise), what he is needed for at its end, and a beat when he is needed again; the window batches its questions to its end and says its own off-range end (overrun, done sooner, blocked on his word), the needed-again beat a chat line awaiting his return, never a summons — the trail accounts for the session's time; the per-command grind stays quiet; a narration line is chat-register, distinct from a report (no pre-report walk, no questions, the plain-language and bookkeeping laws still bind); it replaces no report; the law's one home: communicator | Throwing a wish |
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
