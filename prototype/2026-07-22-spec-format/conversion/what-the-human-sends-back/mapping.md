# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of `## What the human sends back` (PRODUCT_SPEC.md lines 928–1055) dropped nothing. Part 1 maps every code the source cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

`Rn` names Requirement n in `section.md`; a code in several requirements is anchored in each. Zero codes are dropped: all 29 cited codes and both feature tags appear in `section.md` (verified mechanically — cited-set minus present-set is empty, and no extra code is present).

## Part 1 — every cited code → its new home

| Code | New home | Index row consumed? |
|---|---|:--:|
| E-11 | R2 | yes |
| E-14 | R8 | yes |
| E-28 | R1, R7 | yes |
| E-30 | R5 | yes |
| INV-1 | R7 | yes |
| INV-4 | R2 | yes |
| INV-10 | R7 | yes |
| INV-11 | R7 | yes |
| INV-14 | R6 | yes |
| INV-21 | R3 | yes |
| INV-23 | R3 | yes |
| INV-27 | R1, R8 | yes |
| INV-28 | R8 | yes |
| INV-31 | R6 | yes |
| INV-35 | R6 | yes |
| INV-37 | R8 | yes |
| INV-38 | R8 | yes |
| INV-48 | R6 | yes |
| INV-59 | R3 | yes |
| INV-64 | R2 | yes |
| INV-68 | R1, R6, R7 | yes |
| INV-108 | R3 | yes |
| INV-161 | R6 | yes |
| INV-179 | R6 | yes |
| S-0 | R8 | yes |
| T-10 | R2, R4 | yes |
| T-12 | R3 | yes |
| T-20 | R2, R3, R4, R5 | yes |
| T-21 | R6 | yes |

Feature tags: `F-feedback` carried in the titles of R1–R7; `F-feature-map` carried in the title of R8. Neither tag has a Formal-index row (they are feature-map tags, not codes), so neither enters the byte count of consumed index rows.

## Part 2 — consumed Formal-index rows

The section cites 29 distinct codes, and **all 29 carry a Formal-index row** — this scenario section names no inline-only feature code. Each row's meaning now lives at the home named in Part 1; no consumed index row is left without a home.

**Codes owned by this unit** (their Formal-index home is `Sending feedback in` or `Asking what the product does`) are the ones this rewrite fully converts: E-28, E-30, T-20, T-21, INV-68, INV-161, INV-38. INV-179 (index home `Throwing a wish`) is also fully converted here, since its anonymization behaviour is stated in this section's own prose and lands at R6.5.

**Pure cross-references** — a rule owned by another section that this section leans on rather than restates — are preserved as trailing anchors at the requirement that leans on them; the full behaviour stays defined in the home section: INV-27, INV-4, INV-64, E-11, T-10, T-12, INV-59, INV-21, INV-23, INV-108, INV-35, INV-48, INV-31, INV-14, INV-10, INV-11, INV-1, INV-37, S-0, E-14, INV-28.

**Cross-section glossary note.** A handful of domain nouns this section uses are owned by other sections and are defined in their home glossary, not repeated here: *wish*, *echo*, *wish echo*, *decision page*, *review page*, *decision archive*, *harvested row*, *feature map*, *station*, *departures board*, *node*, *tripwire*, *lane*, *checkpoint*, *milestone*, *problem ledger* (the last defined in the sibling unit `## When something breaks`), *measurement family*, *station-completion digest*, *resume file*. In a whole-document conversion these live once in the shared glossary; this unit's `## Glossary additions` block adds only the nouns it introduces (feedback, feedback ledger, field evidence, feedback-intake, feedback-collector, upstream note, outbox).

## Part 3 — atomic-claim coverage

Every behavioural claim of the source, in source order, mapped to the criterion (or criteria) that now carries it. "R1.3" means Requirement 1, criterion 3.

### Feedback and its ledger home (E-28, INV-68, INV-27)

| # | Source claim | Criterion |
|---|---|---|
| 1 | Feedback is anything a person hands back, at any size, moment, or channel; a host's own users' reports travel the same road once received. | glossary (feedback), R1 context |
| 2 | Two promises: nothing handed in is lost; every item is answered by a route. | R1 context, R1.1, R1.6 |
| 3 | Every received item lands the same session in its route's home — wish→row, answer→archive+harvested row, fix→commit+journal, noise→problem ledger. | R1.1 |
| 4 | Routes with no prior home (field evidence, plain reactions, wordless drops) land as dated lines in the feedback ledger FEEDBACK.md, append-only beside the queue. | R1.2, glossary |
| 5 | Each ledger line records when it arrived, who + channel, what it concerns on the feature map, the item in plain words, and where it went. | R1.3 |
| 6 | Every arrival is echoed in one sentence, one echo per item; a wish-shaped item takes the wish echo, any other a note of what was heard and where it went. | R1.4 |
| 7 | A re-mention appends the new date to the existing line and changes nothing else. | R1.5 |
| 50 | Success measure: the same item never has to be handed in twice; every received item is findable in the ledger, with its route, in the same session. | R1.6 |

### The three channels (T-20, INV-4, INV-64, E-11, T-10)

| # | Source claim | Criterion |
|---|---|---|
| 8 | Three channels meet one contract. | R2 context |
| 9 | Spoken or typed: a remark in the conversation or a note in a file the human points at. | R2.1 |
| 10 | A comment on something shown: decision/review pages capture answers as saved data; each saved answer is a feedback item whose home is the decision archive and its harvested row. | R2.2 |
| 11 | A dropped file (screenshot/log/document) from the human or an outside session via the inbox arrives as one new file under the wish naming/collision law, swept in by the host's own session. | R2.3 |
| 12 | A wordless file draws one plain question; the ledger records no guess. | R2.4 |

### The five routes (T-20, T-12, INV-27, INV-59, INV-21, INV-23, INV-108)

| # | Source claim | Criterion |
|---|---|---|
| 13 | Every item takes exactly one route; each route has its law and home; the product/workshop seam decides the last two. | R3 context |
| 14 | Wish route: walks wish intake with its own echo, door, and row; the row is home. | R3.1 |
| 15 | Fix-sized comment fixed same session (commit+journal home); story-sized comment queues as a wish. | R3.2 (+ GAP: fix-sized/story-sized boundary) |
| 16 | Answered question closes for good, harvested same session into the decision archive and harvested row. | R3.3 |
| 17 | Field evidence: a reaction to a shipped feature lands in the ledger citing the feature's scenario; grows into a wish only on the person's word or a tripwire verdict. | R3.4 |
| 18 | Workshop noise routes to the problem ledger; the seam sends product behaviour to FEEDBACK.md, workshop behaviour to PROBLEMS.md; a standing rule's mid-turn break is one problem-ledger entry the once-read-rules sweep reads. | R3.5 |

### feedback-intake (T-20)

| # | Source claim | Criterion |
|---|---|---|
| 19 | feedback-intake owns this behaviour; communicator carries work out, feedback-intake carries it back. | R4 context, glossary |
| 20 | Fires the moment any session receives an item, and at every inbox sweep for a feedback-carrying file. | R4.1 |
| 21 | Stays quiet on the agent's own output, a question the agent asked, and something merely mentioned. | R4.2 |
| 22 | When unsure whether a remark was handed in, asks one plain question. | R4.3 |
| 23 | Never opens a queue row on its own judgment; the intake door owns that verdict. | R4.4 |

### The third arrow, feedback-collector (E-30, T-20)

| # | Source claim | Criterion |
|---|---|---|
| 24 | A third arrow carries an occasional note to the pack's authors, so they learn what delighted or hurt real use. | R5 context |
| 25 | On a genuinely strong reaction the pack offers in one line to send the authors a short note; rare; silent on a mild or routine reaction; "strong" is a conservative floor with a finer form deferred. | R5.1 (+ GAP: strong-reaction measure) |
| 26 | This arm reads the agent's own observation, exactly the moment feedback-intake leaves alone; the two do disjoint work — on a handed-in moment intake logs the field-evidence line and the collector offers when strong; on the agent's own observation only the collector reads. | R5.2, R5.3 |
| 27 | It is no measurement machine: it reads one moment and does not score or aggregate; the reading machinery stays with the measurement family. | R5 context, R7.5 |

### The upstream note (T-21, INV-161, INV-179, INV-35, INV-48)

| # | Source claim | Criterion |
|---|---|---|
| 28 | On the person's positive word the pack writes a short distilled account carrying its own context, holding no raw material, transcript, script, or private content past what the point needs. | R6.3 |
| 29 | It deposits into the host's gitignored outbox/ named by date, cleared once delivered; delivery upstream is the person's own step; the pack opens no network connection and no public request. | R6.4 |
| 30 | The pack's side ends at a deposited, private, self-contained note. | R6.4 |
| 31 | "Upstream note" is this arm's own name, distinct from the station-completion digest and the resume-file digest. | R6.6 |
| 32 | Consent is a positive word, the opposite of silence-is-consent; nothing is sent without an explicit yes, asked every time; a silence or unclear answer leaves the note unwritten. | R6.1 |
| 33 | Off by default under a package-default flag; never offers on a machine not switched on; a downstream host turns it on by a recorded profile line; the authors' origin machine leaves it off; the flag is honoured on every read (off = never fires/reads/asks). | R6.2 |
| 34 | feedback-collector owns the arm, a sub-skill beside feedback-intake; they share FEEDBACK.md only as the local record of an offer made and answered — one dated ledger line (when · offer · answer · outbox filename when yes), a sixth line-kind. | R6.7, R5 context |
| 35 | v1 does not deliver over the network or open a real request (deposits and stops); does not read emotion by a trained model (reads an unmistakable explicit signal); does not aggregate. | R6.4, R5.1 |
| 36 | The draft is anonymized before the user reads it at consent: host entities become neutral role words, the pack's public names stay; the approved note is the travelling note. | R6.5 |

### Fences, composition, facets, non-goals (E-11, T-10, INV-1, INV-10, INV-11, INV-27, INV-59, INV-23, T-20, INV-68, T-21, INV-161, INV-179, INV-14, INV-31)

| # | Source claim | Criterion |
|---|---|---|
| 37–45 | The section's stated edges: inbox stays one new committed file swept first; the wish echo/intake path unchanged; answered questions still close and harvest; the problem ledger still holds workshop noise alone; this extends the no-wish-ever-lost law; the outbound arm adds a third arrow and never changes inbound routing; the arm sends nothing without a positive word and opens no network/public request; the note stays distilled/non-public and outbox is gitignored so no note rides the repo; off by default. | R2.3, R3.3, R3.5, R6.1, R6.2, R6.3, R6.4, R7.2 |
| 46 | Composition: outside sessions never edit the ledger; only the assigned session appends FEEDBACK.md, under the write-ownership and concurrent-edit fences. | R7.1 |
| 47 | The ledger is append-only and archives like the queue, never trimmed. | R7.2 |
| 48 | Facets: the empty state is a ledger holding only its header, which is healthy; the surfaces are the ledger file and the chat echo, layout/touch/accessibility/performance belonging to the media. | R7.3 (empty state; the media-owns-facets note is carried as facet prose, no new behaviour) |
| 49 | Non-goals: no end-user feedback widget (visitors ride the measurement family or their own wish); no automatic reading/scoring/aggregation; no new door mechanics. | R7.4, R7.5 |

### The feature map on demand (INV-38, INV-27, INV-37, S-0, E-14, INV-28)

| # | Source claim | Criterion |
|---|---|---|
| 51 | Three standing questions describe the product; the departures board reports in-flight, intake places each wish, and those two answer on their own surfaces. | R8 context |
| 52 | This ask answers the third — what the product does today — with one whole map current as of the request, on demand. | R8.1 |
| 53 | Read live from the living documents: spec scenario sections name features; the header separates shipped from promised at the target granularity; a scenario holding both is marked shipped with named promised parts; the queue's open rows supply the remainder, showing a feature on the map before the spec documents it. | R8.1, R8.3 |
| 54 | The spec's scenarios and the architecture's nodes constitute the map; no third document (no feature-list file, no cached copy). | R8.2 |
| 55 | Each line follows the line law: echo-name, what it gives its person, status followed by station. | R8.4 |
| 56 | Delivered in chat by default, a rendered page on request; routine reports keep the departures board's in-flight scope; the whole map returns only on request. | R8.5 |
| 57 | A host with no spec/scenario sections is told the condition, directed to bootstrap or adoption, and answered only for what exists. | R8.6 |
| 58 | Fences: the departures board keeps its report scope, intake keeps its placement rule, the no-third-document law stands. | R8.7 |
| 59 | Facets: the only surface is the answer itself; the empty state is the nothing-to-read answer. | R8.6 (empty state; the medium-owns-facets note carried as facet prose) |
| 60 | Non-goals: no standing feature document, no auto-refreshing dashboard, no per-feature history timeline. | R8.2, R8 context |
| 61 | Success measure: the map covers the spec's scenario sections one-to-one plus open new-verdict rows; its shipped-versus-promised marks agree with the header and the target tags. | R8.8 |

### Coverage result

Sixty-one source claims mapped, covering all 8 requirements. Two source holes are recorded as `[GAP]` lines at R3.2 (the fix-sized / story-sized boundary) and R5.1 (the reading of a strong reaction) and detailed in `GAPS.md`. Three non-goal / policy blocks state what the system deliberately does not do; they are carried as policy criteria (R7.4, R7.5) or as facet prose in a requirement's Context rather than converted to a positive `shall` where the source itself only denies a mechanism. No behavioural `shall`-claim of the source is left uncovered.
