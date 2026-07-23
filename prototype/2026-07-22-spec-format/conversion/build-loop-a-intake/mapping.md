# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of source lines 48–276 — the build-loop intro and the first half of `### Throwing a wish [feature: F-wish]` (intake, naming and reporting, showing and deciding) — dropped nothing. Part 1 maps every code the source cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source prose to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; a code in several requirements is anchored in each. The mechanical zero-drop check passed: the cited-set minus the present-set is empty. The second half of `### Throwing a wish` (Doors, kinds, and craft; Specifying and building a feature; Parallel lanes) is another unit's; a code cited in both halves is anchored in both, and this check covers only lines 48–276.

## Part 1 — every cited code → its new home

| Code | New home | Index row consumed? |
|---|---|:--:|
| F-wish | R1 | no (feature marker, no index row) |
| E-2 | R1 | yes |
| E-3 | R1 | yes |
| E-14 | R13 | yes |
| E-22 | R4 | yes |
| E-26 | R33 | yes |
| INV-1 | R1, R2, R10 | yes |
| INV-4 | R4, R6, R7, R8, R18, R19, R29, R32 | yes |
| INV-5 | R7, R18 | yes |
| INV-9 | R4 | yes |
| INV-12 | R6, R7, R10, R13 | yes |
| INV-13 | R4 | yes |
| INV-18 | R7, R9 | yes |
| INV-20 | R9 | yes |
| INV-21 | R9 | yes |
| INV-22 | R6 | yes |
| INV-25 | R14 | yes |
| INV-26 | R11 | yes |
| INV-27 | R12, R19, R20 | yes |
| INV-28 | R5, R14, R19, R26 | yes |
| INV-31 | R4, R29 | yes |
| INV-32 | R5, R28 | yes |
| INV-34 | R15, R17, R18 | yes |
| INV-35 | R14, R19, R20, R22, R24, R26 | yes |
| INV-37 | R12, R13 | yes |
| INV-42 | R29, R30, R33 | yes |
| INV-51 | R23, R25, R27 | yes |
| INV-52 | R24 | yes |
| INV-57 | R27 | yes |
| INV-58 | R30 | yes |
| INV-59 | R4, R31 | yes |
| INV-60 | R18, R32 | yes |
| INV-64 | R28 | yes |
| INV-67 | R25, R26 | yes |
| INV-69 | R14, R15 | yes |
| INV-71 | R26 | yes |
| INV-76 | R22 | yes |
| INV-81 | R8, R18 | yes |
| INV-83 | R15, R16 | yes |
| INV-93 | R19, R20, R22 | yes |
| INV-94 | R16 | yes |
| INV-95 | R22 | yes |
| INV-109 | R21 | yes |
| INV-121 | R8 | yes |
| INV-130 | R4 | yes |
| INV-137 | R14 | yes |
| INV-146 | R12 | yes |
| INV-147 | R12 | yes |
| INV-163 | R33 | yes |
| INV-203 | R15, R16 | yes |
| INV-222 | R2 | yes |
| INV-223 | R2 | yes |
| T-1..T-7 | R3 | no (inline-only, no index row) |
| T-11 | R9 | yes |
| T-14 | R9, R13 | yes |
| T-15 | R7, R9, R10 | yes |
| T-16 | R6 | yes |
| T-17 | R10 | yes |
| M-2 | R11 | yes |

## Part 2 — consumed Formal-index rows

The section cites 59 distinct code tokens. **Fifty-seven carry a consumed Formal-index row**, whose meaning now lives at the home named in Part 1. **Eight codes are inline-only, carrying no Formal-index row**: `F-wish`, the feature marker for the scenario, and `T-1` through `T-7`, cited as the range `[T-1..T-7]`. The seven transitions are defined not in the index but in the source's own numbered wish-path list (source lines 73–78), and that whole behaviour is carried into R3's five criteria. (`T-8`, `T-9`, and up carry index rows and belong to the section's other half; `T-1..T-7` do not.)

**Codes this unit owns and fully converts** (their behaviour is stated in this unit's prose, and its home is the `Throwing a wish` scenario or a communicator rule): E-2, E-3, E-22, E-26, INV-1, INV-4, INV-5, INV-9, INV-12, INV-13, INV-18, INV-20, INV-21, INV-22, INV-26, INV-27, INV-28, INV-31, INV-32, INV-34, INV-35, INV-37, INV-42, INV-51, INV-52, INV-57, INV-58, INV-59, INV-60, INV-64, INV-67, INV-71, INV-81, INV-83, INV-93, INV-94, INV-95, INV-109, INV-121, INV-130, T-11, T-14, T-15, T-16, T-17, and the inline T-1..T-7.

**Pure cross-references** — a rule owned by another section that this unit leans on rather than restates — are preserved as trailing anchors at the requirement that leans on them; the full behaviour stays defined in the home section, not re-converted here: E-14 (the architecture doc / feature map), INV-25 (the done-claim evidence walk), INV-69 (the routing rule), INV-76 (background-worker liveness), INV-137 (the reader-worker dispatch), INV-146, INV-147 (the stranger arm and its monitor), INV-163 (the pack-to-host body axis), INV-203 (the register judge), INV-222, INV-223 (the far tier and its self-surfacing), M-2 (the safe breakpoint and self-compaction).

**Cross-section glossary note.** A handful of domain nouns this unit uses are owned by other sections and are defined in their home glossary, not repeated here (per the reuse-by-reference rule): *capture echo*, *seat*, *movement*, *milestone*, *delivery report*, *checkpoint*, *worker*, *lane*, *register judge*, *far tier*, *resume file*. In a whole-document conversion these live once in the shared glossary; this unit's `## Glossary additions` block adds only the 21 nouns it introduces (wish, intake, door, size, priority, work-kind, decision page, decision card, decision archive, feature map, user story, leg, regression fence, facet, success measure, status report, narration, heartbeat, offline window, register lint, removal list).

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order, mapped to the criterion that now carries it. "R4.3" means Requirement 4, criterion 3. History (dates, provenance, and the reasons behind past choices) is dropped by law 6 and lives in the journal, so it is not a behavioural claim to carry.

### The build loop and the wish (source 48–62; E-2, E-3, INV-1, F-wish)

| # | Source claim | Criterion |
|---|---|---|
| 1 | The build loop is the path a wish travels: it comes in, is specified, is tested, and ships. | R1 (Context); R3 |
| 2 | A wish is one request, plain words, any size, any moment. | R1.1 |
| 3 | Within that same minute the wish becomes one queue (ROADMAP.md) row holding the person's words, its class of size and priority, its status, and its acceptance criterion. | R1.1 |
| 4 | The row exists before anything else happens and survives an immediate session end. | R1.2 |
| 5 | Rows are never deleted; a row closes only with a named exit. | R1.3 |
| 6 | Every wish reaches a recorded terminal state (no wish is ever lost). | R1.4 |

### The row's homes: archive, deferred, far (source 64–70; INV-1, INV-222, INV-223)

| # | Source claim | Criterion |
|---|---|---|
| 7 | At a milestone a terminal-exit row (landed, declined, superseded) moves to a dated queue archive, unedited. | R2.1 |
| 8 | The archive holds only wishes no longer due back. | R2.2 |
| 9 | A deferred row stays in the active queue carrying its revisit trigger until it fires or the row resolves. | R2.3 |
| 10 | A far row stays in the queue with no trigger and no plan, kept so the thought is not lost. | R2.4 |
| 11 | The runnable report stands the far tier down by name and shows it on the person's request. | R2.5 |

### The wish path (source 72–78; T-1..T-7)

| # | Source claim | Criterion |
|---|---|---|
| 12 | Step 1: the classifier reads size, priority, door, and work-kind and states them in one intake line. | R3.1 |
| 13 | Step 2–3: a spec-delta is drafted and validated against the whole spec; only human questions go up, batched; everything else proceeds on the recommended option, marked in the row. | R3.2 |
| 14 | Step 4: the wish is queued, then goes in-work. | R3.3 |
| 15 | Step 5: it lands when the suite is green, guardrails pass, the commit goes in, and the row closes with its acceptance met. | R3.4 |
| 16 | Step 6: the pipeline reports in one plain-language landing line — position on the map, what landed, what remains. | R3.5 |

### The decision page (source 82–90; E-22, INV-4, INV-9, INV-13, INV-31, INV-59, INV-130)

| # | Source claim | Criterion |
|---|---|---|
| 17 | Several open questions arrive together on one decision page, in its own window, while the rest carries on. | R4.1 |
| 18 | Each question is a card with the recommended answer marked and room to write another. | R4.2 |
| 19 | Once answered, the page is filed in `docs/decisions/` and every answer folded into its row the same session; an unread answer is a decision lost. | R4.3 |
| 20 | The person's word settles it; a click records only a first pick; a pick taken back in plain speech is withdrawn, logged answered-then-withdrawn, and re-asked plainer. | R4.4 |
| 21 | A pick made without understanding settles nothing that needs the considered word. | R4.5 |
| 22 | A withdrawn decision converges: on the second withdrawal the recommended option is taken, surfaced as a `[default]` in the landing report, silence-is-consent, never re-asked. | R4.6 |
| 23 | An answered question closes forever; a later change of mind rides as a new wish, never a reopening. | R4.7 |
| 24 | How the page works (filename, ordering, round-trip) is written once in communicator rule 10. | R4.8 |

### The decision card (source 92; INV-32, INV-28)

| # | Source claim | Criterion |
|---|---|---|
| 25 | A card opens with what each option changes for the person; options labelled by consequence, mechanism only where it aids the choice. | R5.1 |
| 26 | A card unanswerable without understanding the mechanism is a defect of the card. | R5.2 |

### Classification by size, priority, work-kind (source 94–100; INV-12, T-16, INV-22)

| # | Source claim | Criterion |
|---|---|---|
| 27 | Size uses one four-word vocabulary everywhere — bug, small, surface, large — and the queue's class column uses the same four with no second scale. | R6.1 |
| 28 | The door is a separate axis from size. | R6.2 |
| 29 | One work-kind per wish (product/infra/skill/prose), host default where none is named. | R6.3 |
| 30 | Priority is normal unless marked: critical (product broken — unusable surface, lost data, violated safety gate) or quick win (low effort, immediate value, no design decision). | R6.4 (+ GAP: quick-win measure) |
| 31 | An uncallable size/priority/work-kind is asked at intake, never guessed. | R6.5 |
| 32 | Until answered: normal priority, host-default or no kind, an unnamed kind scales nothing down; the open question stays in the row while the lane moves. | R6.6 |

### The large wish and scope, never time (source 102–106; T-15, INV-4, INV-5, INV-18, INV-12)

| # | Source claim | Criterion |
|---|---|---|
| 33 | The walk never asks duration and never accepts an hours/days estimate as an input. | R7.1 |
| 34 | When a wish is larger than its worth, the walk answers in scope terms and proposes cut-the-scope or split-into-stages (each stage the full pipeline). | R7.2 (+ GAP: worth measure) |
| 35 | The proposal proceeds on the recommended option; the lane does not park. | R7.3 |
| 36 | Every cut appears in the batched report alongside every taken default, never silent. | R7.4 |

### A proven artifact settles a fork (source 108; INV-121, INV-4, INV-81)

| # | Source claim | Criterion |
|---|---|---|
| 37 | Before surfacing a fork the session checks whether a proven artifact determines it; when it does, it derives the requirement and cites the section, offering no fork. | R8.1 |
| 38 | A fork reaches the person only for a genuinely open taste call or an artifact-ungrounded trade-off. | R8.2 |
| 39 | This is the design-fork sharpening of the pre-ask decide-or-verify gate. | R8.3 |

### Scope cut moves scope only; uncuttable sentences (source 110–112; T-11, T-14, INV-18, INV-20, INV-21, T-15)

| # | Source claim | Criterion |
|---|---|---|
| 40 | A cut surface returned later is a new wish. | R9.1 |
| 41 | A scope cut changes scope only, is no quick-win mark; only priority moves the lane order. | R9.2 |
| 42 | No cut touches the mandatory sentences — regression fences, a kept surface's facets, the non-goals, the success measure. | R9.3 |
| 43 | Scope adjusts richness; the mandatory sentences stand whole. | R9.4 |

### One wish is one user story (source 114–118; T-17, INV-12, INV-1)

| # | Source claim | Criterion |
|---|---|---|
| 44 | A wish with more than one user story is split at intake, each story its own row through the full pipeline. | R10.1 |
| 45 | Sub-behaviours (hover face, phone face, backpointer) are that story's acceptance, folded into the same row. | R10.2 |
| 46 | Separate stories are never fused; distinct from a stage split that slices one story's depth. | R10.3 |
| 47 | The classifier asks whether one story or two and does not guess. | R10.4 |
| 48 | Every row a split produces cites the one spoken wish it came from. | R10.5 |

### The multi-leg row (source 120; INV-26, M-2)

| # | Source claim | Criterion |
|---|---|---|
| 49 | A multi-leg row enumerates per-leg acceptance in its Done-when and does not close with an unmet leg. | R11.1 |
| 50 | Half-done is a status, never a landing. | R11.2 |
| 51 | The resume file's live-state supersession never compresses an open leg away; a leg open at compaction is restated in full. | R11.3 |

### The capture echo and the status report (source 124–138; INV-27, INV-146, INV-147, INV-37)

| # | Source claim | Criterion |
|---|---|---|
| 52 | Every captured wish is echoed back in one sentence: what was heard, the door, the name, the row number. | R12.1 |
| 53 | A silently-arriving wish (inbox file, batch) takes its echo in the next status report, not as an interruption. | R12.2 |
| 54 | A stranger-Issue-bridged wish also takes its echo on the Issue, since the stranger reads no host status report. | R12.3 |
| 55 | Every status report names each in-flight feature and its pipeline stage, one of the nine fixed steps. | R12.4 |
| 56 | A paused feature is reported under its stage; landed is a terminal state, not a pipeline step. | R12.5 |
| 57 | The echo also states where the wish sits on the feature map. | R12.6 |

### The feature-map placement (source 140–151; INV-37, E-14, INV-12, T-14)

| # | Source claim | Criterion |
|---|---|---|
| 58 | Every wish is placed on the feature map (spec scenarios + architecture nodes, no third document) by one of three verdicts: changes an existing feature (and names it), new feature (new scenario + node), or restructure. | R13.1 |
| 59 | A restructure opens its own row (refactor door for structure-only, feature door for behaviour) and re-divides only through the architecture stage and its re-proof. | R13.2 |
| 60 | A placement may report the structure no longer fits, but only a completed change alters structure. | R13.3 |
| 61 | A bug's placement is the feature it repairs; an undeterminable feature is asked. | R13.4 |
| 62 | The verdict is written in the row as a note (changes X / new / restructure), searchable after the report scrolls. | R13.5 |

### The outcome does the talking (source 153–166; INV-28, INV-35, INV-25, INV-69, INV-137)

| # | Source claim | Criterion |
|---|---|---|
| 63 | A feature's echo-name is a short descriptive phrase in product words, parsable cold, never a private metaphor. | R14.1 |
| 64 | A name that needs its story told first is a handle, not a name. | R14.2 |
| 65 | A human-facing line (chat report, narration, report page, decision page, capture echo) opens with the reader's outcome; every internal handle (codes, row/session numbers, coined names) trails in parentheses. | R14.3 |
| 66 | One fact gets one standalone sentence; a context-needing compression is a defect of the line. | R14.4 |
| 67 | Bookkeeping numbers (test count, suite size, version string, check tally) are never message content; the message says what the number means, the number trails or stays in records. | R14.5 |
| 68 | Carve-out: when the number is the asked substance — a direct question, or the done-claim evidence walk pinning artifact + method version — the number is the content. | R14.6 |
| 69 | A prompt hook (`hooks/chat-law-hook.sh`) reminds every prompt of the chat laws including the routing line (orchestrator routes to the cheapest tier, workers locate their own anchors); the skills and profile stay the homes. | R14.7 |
| 70 | Before showing, `scripts/preshow-lint.py` flags a line opening with an internal handle, a warning to clear, reading only the shown surface. | R14.8 |

### The register lint (source 168–170; INV-83, INV-203, INV-69, INV-34)

| # | Source claim | Criterion |
|---|---|---|
| 71 | Anything shown passes `scripts/preshow-register-lint.py`; a red result blocks the showing until the text reads plain (coined metaphor, calque, transliterated pack term). | R15.1 |
| 72 | It is a block not an advisory warning; its reach is the shown artifact (page, mockup, decision page, report page). | R15.2 |
| 73 | The literal pattern set is the free first pass and grows by nobody's duty, a growing list staying one escape behind. | R15.3 |
| 74 | The residual class is held by the register judge at the cheapest routed tier, the ceiling the list cannot reach. | R15.4 |
| 75 | The chat line is held by the register judge's chat arm. | R15.5 |

### No line certifies its own sincerity (source 172; INV-94, INV-203, INV-83)

| # | Source claim | Criterion |
|---|---|---|
| 76 | A self-praising sincerity line carries no information and is stripped; the content carries the honesty. | R16.1 |
| 77 | It binds every surface — shown artifact through the lint, chat through the session's read and the hook. | R16.2 |
| 78 | The register judge holds the class; a caught phrase informs the judge and the first pass; the list grows by nobody's duty. | R16.3 |

### The report law is walked (source 175–179; INV-34)

| # | Source claim | Criterion |
|---|---|---|
| 79 | Before any movement-end/milestone report, the communicator rules are re-read and the draft walked phrase by phrase against the outside-reader question. | R17.1 |
| 80 | Any named pack surface is explained in the reader's words or dropped; trailing anchors stay legal. | R17.2 |
| 81 | A report that makes the reader ask "what is this?" is the walk not walked; acceptance is the reader's. | R17.3 |

### A question walks the scan and one gate more (source 181; INV-81, INV-4, INV-5, INV-60, INV-34)

| # | Source claim | Criterion |
|---|---|---|
| 82 | Every question (report tail, decision page, lone ask) walks the phrase-by-phrase outside-reader read. | R18.1 |
| 83 | It first passes the gate "can I decide or verify this myself?"; a failing question is work done. | R18.2 |
| 84 | A surviving question arrives with its recommendation. | R18.3 |

### Work is narrated while it runs (source 183–208; INV-35, INV-27, INV-28, INV-93, INV-4)

| # | Source claim | Criterion |
|---|---|---|
| 85 | While work runs, each beat worth a sentence is said in one or two plain roadmap-term sentences; the mechanical grind stays quiet. | R19.1 |
| 86 | Identity: every beat names the work — which wish, which stage, and whether it mends or builds. | R19.2 |
| 87 | Digest: a station's completion is a beat carrying a short digest of what it produced, in the work's words. | R19.3 |
| 88 | Heartbeat: a long beatless stretch gets a line naming what grinds and why; owed past ~10 min as a default. | R19.4 |
| 89 | A detached run past ~2 min opens with a start line (what runs, log, honest range), beats every ~2 min or per stage, and closes with a done digest. | R19.5 |
| 90 | Offline window: a stretch needing nothing from the person is announced before start — step away, honest range (unknown said as unknown), what he's needed for at the end. | R19.6 |
| 91 | When needed again, a plain beat names the gate or decision; questions born inside the window batch to its end. | R19.7 |
| 92 | A narration line is chat-register: no pre-report walk, asks nothing, replaces no report; every human-facing-line law binds. | R19.8 |

### Every ask hears its price in time (source 210; INV-93, INV-27, INV-35)

| # | Source claim | Criterion |
|---|---|---|
| 93 | The capture echo carries an honest time range from the work's shape or observed runs; unknown said as unknown. | R20.1 |
| 94 | Work of an hour or more is explained up front in plain steps; the heartbeat says how much remains as it runs. | R20.2 |
| 95 | The landing report states the estimate beside the actual, overrun or under said plainly. | R20.3 |
| 96 | A direct command registering no row still hears its range when it holds the session past a beat. | R20.4 |

### A rewrite that removes substance (source 212; INV-109)

| # | Source claim | Criterion |
|---|---|---|
| 97 | A rewrite/restyle that removes substance (section, argument, rationale, worked example) lists every removal with one line of judgment: kept and where, killed by name, or proposed-and-asked. | R21.1 |
| 98 | An unjustifiable removal becomes a question before the report closes; never a silent cut of substance. | R21.2 |
| 99 | The rule scopes to substance; a tightened sentence or reordered clause needs no account. | R21.3 |

### One spoken leave-word (source 214; INV-95, INV-76, INV-93, INV-35)

| # | Source claim | Criterion |
|---|---|---|
| 100 | On a leave-word the session stops taking new work and halts or lands background workers, recording an unhaltable one by the handoff discipline. | R22.1 |
| 101 | Every open lane reaches its checkpoint; green work committed under gates, no red work committed, the failing test topping the resume file. | R22.2 |
| 102 | The resume file says what resumes where. | R22.3 |
| 103 | The first beat gives minutes-to-safe; the last is one closing line (safe to power off + what resumes where), said only when every point holds. | R22.4 |
| 104 | The remaining-minutes habit rides long work before any leave-word; the session never guesses leaving from silence. | R22.5 |

### The one-line identifier (source 219–223; INV-51)

| # | Source claim | Criterion |
|---|---|---|
| 105 | The project's name shows in a handed page's visible content, not only the URL. | R23.1 |
| 106 | The page states what it needs (a word — what, by when — or only an update, no action). | R23.2 |
| 107 | Every handed/opened artifact (report page, decision page, rendered doc) leads with that identifier; the announcing chat line carries the same two facts. | R23.3 |

### The away-stretch showing cadence (source 225; INV-52, INV-35)

| # | Source claim | Criterion |
|---|---|---|
| 108 | During an away-stretch (overnight loop, offline window) nothing opens a browser window mid-stretch; artifacts accumulate on one page. | R24.1 |
| 109 | A mid-stretch re-open is allowed only as that same page refreshed in place. | R24.2 |

### The showing channel (source 227–231; INV-67, INV-51)

| # | Source claim | Criterion |
|---|---|---|
| 110 | The session reads where it runs (platform, display, filesystem) and names the channel it picked. | R25.1 |
| 111 | A local session shows a local browser page; a remote session shows through its own channel (host-rendered page or chat), same identifier and round-trip. | R25.2 |
| 112 | The seat is re-read after any move between machines; a local path handed to a remote reader is a defect. | R25.3 |

### The current state is answerable (source 233–241; INV-71, INV-67, INV-35, INV-28)

| # | Source claim | Criterion |
|---|---|---|
| 113 | The live status lives in the chat as a short Now (work in hand + stage) and Next (what the queue holds). | R26.1 |
| 114 | It refreshes at every stage change and carries a heartbeat on a long stretch. | R26.2 |
| 115 | The harness task panel, where shown, is kept in plain product words as a courtesy, never the home of the status. | R26.3 |
| 116 | A rendered status page is an optional richer view on a local session; this binds every project the pack runs. | R26.4 |

### The end of a stretch is delivered (source 243–251; INV-57, INV-51)

| # | Source claim | Criterion |
|---|---|---|
| 117 | At a stretch's end (loop to sleep, away-stretch closing, session ending) the last rendered thing is one short final line: what closed, what's next, what's needed, when the agent wakes. | R27.1 |
| 118 | The long report sits above; the final line comes last, after every tool call. | R27.2 |
| 119 | A page deliverable repeats its identifier in that final line. | R27.3 |

### The review surface (source 253–257; INV-64, INV-32)

| # | Source claim | Criterion |
|---|---|---|
| 120 | A review surface marks each claim by source — artifact, the person's recorded word, or the agent's inference — inferences flagged most prominently. | R28.1 |
| 121 | It is commentable and open, with line-by-line room and answer capture. | R28.2 |
| 122 | The decision page's saved-answers rule extends to review surfaces as one round-trip back to the project. | R28.3 |

### The word read as meant, cuts hold (source 259–265; INV-42, INV-4, INV-31)

| # | Source claim | Criterion |
|---|---|---|
| 123 | A phrasing the person cut in a review round stays cut in every later draft; the removal list lives in the project's records, not session memory. | R29.1 |
| 124 | A cut word reappearing a later round is a defect however fresh; a memory wipe restores no cut phrasing. | R29.2 |
| 125 | A vivid phrase is adopted only as meant; before it shapes the work its intent is read from context or asked, mockery not assumed prescriptive. | R29.3 |
| 126 | The two standing bans (no self-praising drama, no approval-begging under silence-is-consent) are cross-linked, not restated. | R29.4 |

### Approved text is frozen (source 267; INV-58, INV-42)

| # | Source claim | Criterion |
|---|---|---|
| 127 | Once approved, a text is settled material. | R30.1 |
| 128 | A revision applies exactly the named correction (trim/swap) and leaves the surrounding text untouched. | R30.2 |
| 129 | Churn of approved material is a defect, kin of a reappearing cut. | R30.3 |

### No question asked twice (source 271–273; INV-59)

| # | Source claim | Criterion |
|---|---|---|
| 130 | Before any ask the recorded word is searched (decision archives, review records, journal, profile); asking an already-answered question is a defect. | R31.1 |
| 131 | An answered question closes permanently and is recorded into its row the same session. | R31.2 |
| 132 | A named problem returns solved with evidence, not re-described; round N+1 carries only new material. | R31.3 |

### The taste ask carries its research (source 275; INV-60, INV-4)

| # | Source claim | Criterion |
|---|---|---|
| 133 | A taste ask mines the material first (exemplars, precedents, options with citations) and then asks with a chosen recommendation and evidence. | R32.1 |
| 134 | Asking the person to supply what the agent should have mined is a defect; this sharpens the recommended-option rule. | R32.2 |

### The removal list's mechanical form (source 269; E-26, INV-42, INV-163)

| # | Source claim | Criterion |
|---|---|---|
| 135 | The pack ships a removal-list template holding the person's cuts as dated literals, appended on a cut and never removed. | R33.1 |
| 136 | It also ships guardrails guidance for a scanner that greps the artifact's surfaces and reds the suite when a cut literal reappears. | R33.2 |
| 137 | The scanner stays per-project (ship-the-shape pole): the pack ships the template and guidance; each host owns the greps over its own surfaces and its own dated cuts. | R33.3 |
| 138 | A genuinely generic seam a host's scanner grows is lifted to the pack; the host-specific greps stay home. | R33.4 |

### Coverage result

138 behavioural claims mapped, covering all 33 requirements and all 136 criteria. No behavioural `shall`-claim of the source is left uncovered. The two source holes are recorded as `[GAP]` lines at R6.4 and R7.2 and detailed in `GAPS.md`. Two source non-goal / policy framings are carried as negative-side or context statements rather than converted to standalone `shall` criteria: the large-wish rule's "scope, never time" is stated positively as R7.1's refusal criteria, and the leave-word rule's "the command makes closing safe rather than closing anything itself" is carried in R22's Context as a scope statement. No source claim moved.

### Prover MUST-FIX wave (row 445 audit, F6) — declared sharpen

- **`F-wish` moves from a criterion bracket to its owning heading**: R1.4 carried `F-wish` in its trailing anchor list, against the convention that a feature code rides a scenario heading as a `[feature: F-...]` tag. The code moves to R1's heading (`## Requirement 1: A wish is captured as a queue row that is never lost  [feature: F-wish]`); R1.4 keeps `[INV-1]`. Behaviour unchanged.

### Final restoration wave (re-pin sweep) — declared additions

- **R19.9 (narration digest + time accounting).** Restores the source's dropped digest clause — a station a delegated worker closed becomes the senior's beat — and the time-accounting line, token and test counts stay bookkeeping. Owed by `test_traceability::TestProblemLedger::test_narration_three_teeth`. [INV-35, INV-28]
- **R19.10 (the offline window's honest edges).** Restores the four dropped offline-window rules: never a guess dressed as a promise; a window off its spoken range saying so; the needed-again beat a chat line awaiting his return, never a summons; no offline sentence fires when the very next beat needs the human. Owed by `test_offline_window`. The source's "blocked on his word alone" is carried as "blocked on the human's word alone" — `check-no-history` bans the recorded-word marker "his word" (INV-253). [INV-35, INV-4]
