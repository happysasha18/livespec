# Mapping — source codes and claims to sample.md criteria

`Rn.m` means Requirement n, Acceptance Criterion m in `sample.md`.

## 1. Code coverage

Every code cited in the source subsection, and the index row behind it, mapped to the criteria that carry it. Zero silent drops.

| Code | Carried by | Note |
|---|---|---|
| INV-1 | R6.6, R6.7 | split cites its source request; every request reaches a terminal state |
| INV-4 | R1.2, R1.3, R1.4, R3.14, R4.5 | pending question never blocks the queue; work proceeds on the recommended option |
| INV-5 | R4.7 | no silent micro-decision; every cut surfaced |
| INV-9 | R1.11, R1.12, R1.13, R1.14 | person's word settles; click is a first pick; levels set only by the person; withdrawal and re-ask |
| INV-12 | R3.10, R3.11, R4.4, R6.3 | ambiguous class asked at intake, never guessed; unclear story count asked |
| INV-13 | R1.18, R1.19 | one normative home; a full restatement is drift folded back |
| INV-18 | R4.6, R4.15, R4.16 | every aspect ends as a spec sentence, decided or default-tagged and reported |
| INV-20 | R4.17, R4.18 | non-goals sentence always written; scope-narrowing exclusion reported |
| INV-21 | R4.19 | one success measure per feature, decided or default-tagged |
| INV-22 | R3.12, R3.13, R3.15, R3.16 | work type scales each step; unnamed type scales nothing; safety checks always run |
| INV-26 | R6.8, R6.9, R6.10 | per-leg acceptance; no close with an unmet leg; open leg not compressed away |
| INV-28 | R2.4, R2.5, R2.6 | cited as kin on the card-defect line; plain-first human line; bookkeeping numbers never the message |
| INV-31 | R1.16, R4.8, R4.9 | converged decision: silence is consent; taste default told and taken as accepted |
| INV-32 | R2.1, R2.2, R2.3 | card opens in consequences; option labelled by consequence; mechanism only if it aids |
| INV-59 | R1.8, R1.9, R1.10 | search recorded answers first; re-asking a settled question is a defect; answered closes and is harvested |
| INV-81 | R5.4, R5.5, R5.6 | pre-ask gate; a self-answerable question becomes work; a surviving question carries its recommendation |
| INV-121 | R5.1, R5.2, R5.3 | proven artifact checked first; derive and cite; fork only where genuinely open |
| INV-130 | R1.15, R1.17 | converges after two withdrawals; a later change of mind is a new request |
| E-22 | R1.1, R1.5, R1.6, R1.7 | one decision page; recommended answer marked; archived and folded same session |
| T-11 | R4.10, R4.11 | priority bubbles to the queue head; nothing else reorders the queue |
| T-14 | R4.13, R4.14 | regression checks open a delta touching a live surface; a cut never removes them |
| T-15 | R4.1, R4.2, R4.3, R4.20, R6.4 | scope not time; cut or stage; safety net uncuttable; stage slices one story's depth |
| T-16 | R3.8, R3.9 | one work type from the curated vocabulary; project default in its profile |
| T-17 | R6.1, R6.2, R6.5 | one request one story; sub-behaviours fold in; separate stories never fused |
| M-2 | R6.10, R6.11 | open leg restated at compaction; the movement-end ritual |

All 25 cited codes carried. Dropped: none.

## 2. Claim coverage

Each atomic behavioural claim of the source subsection, mapped to the criterion that covers it. A claim without a home is a defect.

| # | Atomic claim | Home |
|---|---|---|
| 1 | Several open questions arrive together on one decision page, not one at a time in chat | R1.1 |
| 2 | The page opens in its own window | R1.2 |
| 3 | The rest of the work carries on while the page waits | R1.3, R1.4 |
| 4 | Each question is a card with the recommended answer marked and room for a different one | R1.5 |
| 5 | Once answered, the answers are filed in `docs/decisions/` | R1.6 |
| 6 | Every answer is folded into its backlog item the same session | R1.6 |
| 7 | An answer left unread is a decision lost | R1.7 |
| 8 | The person's word settles a decision; the click only records a first pick | R1.11 |
| 9 | A pick made without understanding settles nothing that needs the considered word | R1.11, R1.12 |
| 10 | An option taken back in plain speech is withdrawn and logged answered-then-withdrawn | R1.13 |
| 11 | A withdrawn option is asked again later in plainer terms | R1.14 |
| 12 | After two withdrawals the recommended option is taken as a surfaced `[default]` | R1.15 |
| 13 | An answered question closes forever | R1.9, R1.10 |
| 14 | From convergence on, silence is consent and it is never re-asked | R1.16 |
| 15 | A later real change of mind is a new request, never a reopening | R1.17 |
| 16 | The decision-page mechanism is written down once, in communicator rule 10 | R1.18 |
| 17 | A decision card opens with what each option changes for the person | R2.1 |
| 18 | Each option is labelled by its consequence, never by its implementation | R2.2 |
| 19 | The mechanism follows only where it aids the choice | R2.3 |
| 20 | A card unanswerable without the mechanism is a defect | R2.4 |
| 21 | A request is classified by size, priority, and work type | R3.1 |
| 22 | Size uses one four-word vocabulary: bug, small, surface, large | R3.2 |
| 23 | The queue's class column uses the same four words and no second size scale | R3.3 |
| 24 | The entry route is a separate axis from size | R3.4 |
| 25 | Priority is normal unless the backlog item states otherwise | R3.5 |
| 26 | Critical means the shipped product is broken: unusable surface, lost data, or violated safety gate | R3.6 |
| 27 | Quick win means low effort, immediate value, no design decision inside | R3.7 |
| 28 | Each request is tagged with one work type: product, infra, skill, or prose; project default in profile | R3.8, R3.9 |
| 29 | When size, priority, or work type cannot be called, ask at intake and do not guess | R3.10 |
| 30 | Until answered, the request carries normal priority; unnamed type is the default or none and scales nothing down | R3.11, R3.12, R3.13 |
| 31 | The open question stays in the backlog item while the queue keeps moving | R3.14 |
| 32 | A large request negotiates scope, not time; no hours or days estimate as input | R4.1 |
| 33 | A too-big request is cut in scope or split into stages, each stage through the full pipeline | R4.2, R4.3, R4.4 |
| 34 | The proposal proceeds on the recommended option; the queue does not park on it | R4.5 |
| 35 | Every cut is reported in the same batched report as every taken default, and none is silent | R4.6, R4.7 |
| 36 | A proven artifact settles a fork before the human hears it; an open choice still reaches the human | R5.1, R5.2, R5.3 |
| 37 | A cut surface returned later is a new request | R4.12 |
| 38 | A scope cut changes scope only, never order; it is not a quick-win mark; only priority moves the queue | R4.10, R4.11 |
| 39 | No cut touches the regression checks, a kept surface's aspects, the non-goals, or the success measure | R4.14, R4.15, R4.20 |
| 40 | Scope adjusts richness only | R4.20 |
| 41 | One request is one user story; a multi-story request is split at intake, each story its own item | R6.1 |
| 42 | Sub-behaviours of one story are that story's acceptance, folded into the same item | R6.2 |
| 43 | A stage split slices one story's depth; separate stories are never fused | R6.4, R6.5 |
| 44 | The classifier asks whether a request is one story or two, and does not guess | R6.3 |
| 45 | A split loses nothing: every item cites the one request it came from | R6.6, R6.7 |
| 46 | A multi-leg item enumerates per-leg acceptance and does not close with an unmet leg | R6.8, R6.9 |
| 47 | A leg still open at compaction is restated in full; supersession never compresses it away | R6.10 |

47 claims, all covered. Defects: none.

## 3. Vocabulary map

Coinages from the source replaced by standard words in `sample.md`.

| Source coinage | Standard word used |
|---|---|
| wish | request |
| queue row | backlog item |
| landing / landing report | delivery / delivery report |
| door | entry route |
| the classifier | the intake classifier |
| lane | queue (the running queue) |
| walk | pipeline |
| facet | aspect |
| fence / regression fence | regression check |
| work-kind / kind | work type |
| host | project |
| queue, pipeline, spec, test | kept as-is |
