# Three ways to write the same intake rules

This page puts one area of the spec — request intake — in three formats side by side: today's spec, prototype 1 (a compaction of today's genre), and genre 2 (an EARS-plus-user-story hybrid). Read the same behaviour in each and judge which one a reader can act on.

---

## (a) Today's spec

The behaviour lives in two places at once: a human-facing prose paragraph, and a dense index row that carries the full rule. Here is the prose:

> **A wish is classified by size, priority, and work-kind.** Size uses one four-word vocabulary everywhere: bug, small, surface, large. The queue's class column uses the same four words and no second size scale. The door is a separate axis — where the wish enters the pipeline. Size is a separate question.
>
> **A large wish negotiates scope, never time.** The walk does not ask how long a wish will take, and does not accept an estimate in hours or days as an input. When a wish is larger than its worth, the walk answers in scope terms and proposes one of two moves: cut the scope, or split into stages.

And here is the worst index row it leans on, INV-128, verbatim. One sentence carries the trigger, three routes, a disagreement rule, a re-classification rule, a boundary-health law, and a provenance note — all fused:

> | INV-128 | every request enters through a three-source impact read beside the door [T-12] and work-kind [T-16]: the footprint is read from the spec (what behaviour changes), the architecture (which module owns it), and the code (what gets touched) at one intake moment, producing one named footprint — presentation-only · single-module · cross-cutting — spoken in the capture echo and written in the row's `footprint:` note beside door/kind/map [INV-43, INV-108]; the footprint decides the route (presentation → light road; single-module → the matrix step against the module's interface; cross-cutting → the full pipeline), weight matched to reach, the footprint not the size picking the road; the read names any source disagreement as a finding routed to its owner (bug row / spec fix / restructure row [INV-37]) rather than silently trusting one source — pulling the architecture step's spec-to-code reconciliation forward to entry; the three-source read is the verdict derive-before-fork [INV-121] rests on (only the genuinely-open fork reaches the human); the footprint re-classifies mid-work when an edit reaches past its layer (mirroring the door re-fire), the landing report recording held-or-reclassified; the station carries the boundary-health law — a right boundary keeps a typical request in one module, repeated cross-cuts on the same module pair being the signal to move a boundary (only through the architecture step's re-prove [INV-37], on the recorded-footprint evidence not a hunch); recorded live 2026-07-12, the entry station (P1-P6) of the fourteen-principle architect draft, deeper mechanical enforcement on the follow-on rows | ... |

A reader who wants to know what the system does with a single-module request has to parse that whole run-on to find the one clause that answers them.

---

## (b) Prototype 1 — compaction of today's genre

Prototype 1 keeps the two-place shape but shortens both. The prose loses its repetitions:

> **A large wish negotiates scope.** The walk does not ask how long a wish will take and does not accept an estimate in hours or days as an input. When a wish is larger than its worth, the walk answers in scope terms and proposes one of two moves: cut the scope, or split into stages.

And the index row is cut to its Description sentence:

> | INV-128 | Every request gets a three-source impact read at intake — the spec for what behaviour changes, the architecture for which module owns it, the code for what actually gets touched — producing one named footprint of presentation-only, single-module, or cross-cutting that sizes how far the route reaches. related: T-12, T-16, INV-43, INV-108, INV-37, INV-121 |

This is far shorter and still readable. It stays one sentence per rule, so the routes and the disagreement handling remain packed into a single line.

---

## (c) Genre 2 — EARS criteria under a user story

Genre 2 drops the two-place split. Each rule becomes a user story with numbered criteria, one trigger and one response each, and the stable code trails every line. INV-128 as a requirement block:

### Requirement: Three-source impact read at intake
**User Story:** As a person throwing a request, I want its reach read at intake from the spec, the architecture, and the code, so that the route it takes matches how far it actually reaches.

#### Acceptance Criteria
1. WHEN a request arrives, the system SHALL read its impact from three sources: the spec for what behaviour changes, the architecture for which module owns it, and the code for what gets touched. [INV-128]
2. WHEN the impact read completes, the system SHALL name one footprint — presentation-only, single-module, or cross-cutting. [INV-128]
3. WHEN the footprint is presentation-only, the system SHALL route the request by the light road. [INV-128]
4. WHEN the footprint is single-module, the system SHALL route the request through the matrix step against the module's interface. [INV-128]
5. WHEN the footprint is cross-cutting, the system SHALL route the request through the full pipeline. [INV-128]
6. IF the three sources disagree, THEN the system SHALL name the disagreement as a finding routed to its owner rather than trusting one source. [INV-128]
7. IF an edit reaches past its layer mid-work, THEN the system SHALL re-classify the footprint and record the change in the delivery report. [INV-128]

And one more, straight from `sample.md`:

### Requirement 2: Consequence-first decision cards
**User Story:** As a person answering a decision, I want each card written in terms of what the options change for me, so that I can choose without first learning the machinery.

#### Acceptance Criteria
1. WHEN the system opens a decision card, the system SHALL state what each option changes for the person, in the product's own words. [INV-32]
2. WHEN the system labels an option, the system SHALL label it by its consequence. [INV-32]
3. IF the mechanism aids the choice, THEN the system SHALL add the mechanism after the consequence. [INV-32]
4. IF a card cannot be answered without understanding the mechanism, THEN the system SHALL count the card as a defect. [INV-28]

A reader who wants the single-module rule reads line 4 and stops. Each condition has its own address. The trade is length: the fused INV-128 sentence becomes seven lines.

---

## Numbers

| Format | Intake subsection + its cited index rows |
|---|---|
| (a) Today's spec | 17,297 bytes |
| (c) Genre 2 (`sample.md`) | 12,000 bytes |
| Ratio genre 2 / today | 0.694 |

Projected across the whole 783,678-byte spec at the same flat ratio: about 543,685 bytes. The assumption is that the whole spec is the same kind of material — a human rule backed by a dense index row — which holds for the behavioural core and less so for tables and history.
