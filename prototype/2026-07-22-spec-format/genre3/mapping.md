# Mapping — source codes and claims to genre3 sample.md

`Rn.m` means Requirement n, Acceptance Criterion m in `sample.md`. On the owner's approval the criteria were regrouped into named cases: Requirements 3 and 4 renumbered (two compound criteria also split — the bug route into R3.23-24, the disagreement's trust clause into R4.8); the other requirements kept their numbers.

This mapping carries forward genre2's coverage. Every code and claim genre2 covered is still covered here. Two codes are added, both to answer the owner's complaints: **INV-128** (the three-source impact read, complaint 5) and **INV-133** (the critical mark's procedural effect, a genre2 cold-read hole). No genre2 code or claim is dropped.

## 1. Code coverage

| Code | Carried by | Note |
|---|---|---|
| INV-1 | R7.6, R7.7 | split cites its source request; every request reaches a terminal state |
| INV-4 | R1.2, R1.3, R1.4, R3.22, R5.5 | open decision never blocks the queue; work proceeds on the recommended option |
| INV-5 | R5.7 | no silent scope cut; every cut surfaced |
| INV-9 | R1.11, R1.12, R1.13, R1.14 | person's word settles; click is a first pick; levels set only by the person; withdrawal and re-ask |
| INV-12 | R3.18, R3.19, R5.4, R7.3 | ambiguous class asked at intake, never guessed; stage decomposes; unclear story count asked |
| INV-13 | R1.18, R1.19 | one normative home; a full restatement is drift folded back |
| INV-18 | R5.6, R5.16, R5.17 | every dimension of a feature ends as a spec sentence, decided or default-tagged and reported |
| INV-20 | R5.18, R5.19 | non-goals sentence always written; scope-narrowing exclusion reported |
| INV-21 | R5.20 | one success measure per feature, decided or default-tagged |
| INV-22 | R3.16, R3.17, R3.20, R3.21 | work type scales each step; unnamed type scales nothing; guardrails always run |
| INV-26 | R7.8, R7.9, R7.10 | per-part acceptance; no close with an unmet part; open part not compressed away |
| INV-28 | R2.5, R2.6, R2.7 | card-defect line; plain-first human line; bookkeeping numbers never the whole message |
| INV-31 | R1.16, R5.8, R5.9 | settled decision: silence is consent; taste default told and taken as accepted |
| INV-32 | R2.1, R2.2, R2.3, R2.4 | card states each option's effect; person picks one option; option labelled by effect; mechanism trails |
| INV-59 | R1.8, R1.9, R1.10 | search recorded answers first; re-asking a settled decision is a defect; answered closes and is folded in |
| INV-81 | R6.4, R6.5, R6.6 | pre-ask reader check and self-answer test; a self-answerable question becomes work; a surviving one carries its recommendation |
| INV-121 | R6.1, R6.2, R6.3 | proven document checked first; derive and cite; bring only the open choice |
| INV-128 | R4.1–R4.10 | **added.** three-source read (spec/architecture/code); one footprint; footprint picks route; a disagreement routes to the document owning the disputed fact (bug item / spec fix / restructure item); mid-work re-name; footprint recorded |
| INV-130 | R1.15, R1.17 | converges after two withdrawals; a later change of mind is a new request |
| INV-133 | R3.6, R3.7, R3.8, R3.9, R3.10 | **added.** critical = product broken by three tests; heads the queue; keeps running work running; bound stated at intake; person's word owns priority |
| E-22 | R1.1, R1.5, R1.6, R1.7 | one decision page; recommended option marked; archived and folded same session |
| T-9 | R3.24, R1.9, R2.5 | **added round 4.** the bug entry route interrupts running work; running work parks at a clean stopping point and resumes in its original order; a defect of the product opens its own item on the bug route (rounds 6: R1.9, R2.5) |
| T-11 | R3.6, R3.11, R3.12, R3.13, R5.10, R5.11, R5.12 | broken tests; quick-win mark and promotion; critical bubbles to head; nothing else reorders; an inbox file's own date never reorders |
| T-12 | R3.4, R3.23 | **added round 4.** a bug enters at the test-matrix step with the break reproduced as a failing test first; the route set is closed at five (glossary: entry route); size bug and the bug route share one word on purpose (R3.4) |
| T-14 | R5.14, R5.15 | regression checks open a change touching a live surface; a cut never removes them |
| T-15 | R5.1, R5.2, R5.3, R5.21, R7.4 | scope not time; cut or stage; mandatory sentences uncuttable; stage slices one story's depth |
| T-16 | R3.14, R3.15 | one work type from the curated vocabulary; project default in its profile |
| T-17 | R7.1, R7.2, R7.5 | one request one story; sub-behaviours fold in; separate stories kept separate |
| M-2 | R7.10, R7.11 | open part restated at compaction; the movement-end routine |

All 25 genre2 codes carried, plus INV-128 and INV-133 added in round 1 and T-9 and T-12 added in round 4. Codes: 29. Dropped: none.

## 2. Claim coverage

Every atomic behavioural claim of the source subsection, mapped to its home. genre2's 47 claims are all carried; claims 48–55 are added for the two new codes and the newly stated procedural effects the owner flagged.

| # | Atomic claim | Home |
|---|---|---|
| 1 | Several open decisions arrive together on one decision page, not one at a time in chat | R1.1 |
| 2 | The page opens in its own window | R1.2 |
| 3 | The rest of the work carries on while the page waits | R1.3, R1.4 |
| 4 | Each decision is a card with the recommended option marked and room for a different answer | R1.5 |
| 5 | Once answered, the answers are filed in `docs/decisions/` | R1.6 |
| 6 | Every answer is folded into its backlog item the same session | R1.6 |
| 7 | An answer left unread is a decision lost | R1.7 |
| 8 | The person's word settles a decision; the click only records a provisional choice, changeable in chat until the decision closes | R1.11 |
| 9 | A pick made without understanding settles nothing that needs the considered word | R1.11, R1.12 |
| 10 | An option taken back in plain speech is withdrawn and logged answered-then-withdrawn | R1.13 |
| 11 | A withdrawn option is asked again later in plainer words | R1.14 |
| 12 | After two withdrawals the recommended option is taken as a surfaced default mark | R1.15 |
| 13 | An answered decision closes for good | R1.9, R1.10 |
| 14 | From settlement on, silence is consent and it is never re-asked | R1.16 |
| 15 | A later change of mind is a new request, never a reopening | R1.17 |
| 16 | The decision-page mechanism is written down once, in communicator rule 10 | R1.18 |
| 17 | A decision card opens with what each option changes for the person | R2.1 |
| 18 | Each option is labelled by its effect | R2.3 |
| 19 | The mechanism follows only where it helps the choice | R2.4 |
| 20 | A card unanswerable without the mechanism is a defect, and a defect of the product opens its own item on the bug route | R2.5 |
| 21 | A request is classified by size, priority, and work type | R3.1 |
| 22 | Size uses one four-word vocabulary: bug, small, surface, large | R3.2 |
| 23 | The queue's class column uses the same four words and one size scale | R3.3 |
| 24 | The entry route is a separate axis from size | R3.4 |
| 25 | Priority is normal unless the backlog item states another value | R3.5 |
| 26 | Critical means the product is broken: unusable surface, lost data, or violated guardrail | R3.6 |
| 27 | Quick win means low effort, immediate value, no design decision inside | R3.11 |
| 28 | Each request is tagged with one work type: product, infra, skill, or prose; default in profile | R3.14, R3.15 |
| 29 | When size, priority, or work type cannot be called, ask at intake and do not guess | R3.18 |
| 30 | Until answered, the request carries normal priority; unnamed type is the default or none and scales nothing down | R3.19, R3.20, R3.21 |
| 31 | The open decision stays in the backlog item while the queue keeps moving | R3.22 |
| 32 | A large request negotiates scope, not time; no hours or days estimate as input | R5.1 |
| 33 | A larger-than-worth request is cut in scope or split into stages, each stage through the full pipeline | R5.2, R5.3, R5.4 |
| 34 | The proposal proceeds on the recommended option; the queue does not park on it | R5.5 |
| 35 | Every cut is reported in the same batched report as every taken default, and none is silent | R5.6, R5.7 |
| 36 | A proven document settles a fork before the human hears it; an open choice still reaches the human | R6.1, R6.2, R6.3 |
| 37 | A cut surface returned later is a new request | R5.13 |
| 38 | A scope cut changes scope only, never order; it is not a quick-win mark; only priority moves the queue | R5.10, R5.11 |
| 39 | No cut touches the regression checks, a kept surface's dimension sentences, the non-goals, or the success measure | R5.15, R5.16, R5.21 |
| 40 | A cut adjusts only how much ships — fewer surfaces, plainer defaults on what stays | R5.21 |
| 41 | One request is one user story; a multi-story request is split at intake, each story its own item | R7.1 |
| 42 | Sub-behaviours of one story are that story's acceptance, folded into the same item | R7.2 |
| 43 | A stage split slices one story's depth; separate stories are kept separate | R7.4, R7.5 |
| 44 | The classifier asks whether a request is one story or two, and does not guess | R7.3 |
| 45 | A split loses nothing: every item cites the one request it came from | R7.6, R7.7 |
| 46 | A multi-part item enumerates per-part acceptance and does not close with an unmet part | R7.8, R7.9 |
| 47 | A part still open at compaction is restated in full; supersession never compresses it away | R7.10 |
| 48 | Every request gets a three-source impact read at intake: spec, architecture, code | R4.1 |
| 49 | The read produces one named footprint: presentation-only, single-module, or cross-cutting | R4.2 |
| 50 | The footprint decides the route, and the footprint (not the size) picks it | R4.3, R4.4, R4.5, R4.6 |
| 51 | A source disagreement is named as a finding routed to its owner, and no single source is trusted in silence | R4.7, R4.8 |
| 52 | The footprint re-names mid-work when an edit reaches past its module | R4.9 |
| 53 | The named footprint is recorded in the backlog item | R4.10 |
| 54 | A critical mark on a non-bug heads the queue while the running work keeps going, and the bound is stated at intake | R3.7, R3.8, R3.9 |
| 55 | A quick win may be promoted ahead of larger queued items, marked in its item; after one promoted delivery the queue head goes next | R3.12, R3.13 |
| 56 | A request arriving as an inbox file is ordered by its registration moment; the file's own modification date never reorders the queue | R5.12 |
| 57 | A bug enters at the test-matrix step with the break reproduced as a failing test first; the bug route alone interrupts running work, which parks at a resumable stopping point and resumes in its original order | R3.23, R3.24 |
| 58 | The entry-route set is closed at five: feature, bug, refactor, docs-only, skip; the route decides which pipeline steps run | Glossary (entry route), R3.4 |
| 59 | Size and route share the word bug on purpose: a request sized bug enters by the bug route, one call stated once | R3.4 |
| 60 | A defect of the product opens its own backlog item on the bug entry route | R1.9, R2.5 |

60 claims, all covered. Defects: none.

## 3. Vocabulary map

Coinages from the source and from genre2 replaced by standard words in genre3.

| Source or genre2 term | genre3 standard word | Reason |
|---|---|---|
| wish | request | banned coinage |
| walk | pipeline | banned coinage |
| landing / landing report | delivery / delivery report | banned coinage |
| door | entry route | banned coinage |
| net / regression fence | guardrail / regression check | banned coinage |
| station | step | banned coinage |
| movement | movement (kept as ordinary English for a unit of work; the routine it names is spelled out in R7.11) | ordinary word, not a coined mechanism name |
| queue row | backlog item | standard word |
| lane | queue (the running queue) | standard word |
| facet (source T-13/INV-18) | dimension of a feature, the standard set named inline (phone, touch, empty/error/loading, accessibility, performance) | plain word with the source's own list (R5.16, R5.17) |
| richness (source T-15) | how much ships — fewer surfaces taken in, plainer defaults on what stays | plain statement from the source's cut definition (R5.21) |
| same session (source E-22/M-2) | session, now defined in glossary (one conversation, start to close or memory wipe) | was undefined through round 4 |
| batched report / landing report (source INV-5/INV-18 vs INV-130) | one artifact: the delivery report and its batched section | one name per thing; the relation stated in the glossary (delivery report) |
| decision archives (source INV-59) | the decision archive, defined in glossary as the docs/decisions/ folder | one name per thing; R1.6 and R1.8 now share it |
| journal (source M-2/INV-59) | journal, defined in glossary as the dated work log JOURNAL.md | was undefined through round 5 |
| trust and proactivity levels (source INV-9) | glossed inline: settings that widen or narrow what the system may do on its own word | plain statement of the source meaning (R1.12) |
| work-kind / kind | work type | standard word |
| host | project | standard word |
| light road | shortened pipeline | plain description |
| capture echo | statement at intake | plain description |
| document stack (genre2 glossary) | document chain | plain, defined in glossary; the chain is spec → architecture → matrix → code → docs |
| outside-reader read (genre2 criterion) | re-read the question as a stranger would | plain description (R6.4) |
| can-I-decide-or-verify-it-myself gate (genre2 criterion) | test whether it can decide or verify the answer itself | plain description (R6.5) |
| compaction, resume file | kept, now defined in glossary | were undefined in genre2 |
| communicator skill (genre2 criterion) | rule 10 of the reporter role's instruction file | plain pointer; `skill` defined in glossary |
| in plain speech (genre2 criterion) | in chat, in the person's own words | names the channel |
| a file's own date (source T-11) | an inbox file's modification date, kept out of the queue order (R5.12) | plain statement of the source meaning |
| backpointer (source T-17) | a link from the delivered result back to the request that caused it | plain description (R7.2) |
| compacts its own context (source M-2) | trims its own working notes so the session can be wiped or resumed with nothing lost | plain statement of the source meaning (R7.11) |
| safety gate (source prose) | guardrail | uses the defined term (R3.6) |
| footprint | kept, now defined in glossary | needed for the three-source read |
| queue, pipeline, spec, test | kept as-is | already plain |
