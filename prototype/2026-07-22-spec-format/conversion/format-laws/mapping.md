# MAPPING — codes, source coverage, and atomic-claim coverage

This file proves the authoring of `The document's own format laws` — the format-mechanism requirements INV-250..271 — dropped nothing from its source. The source is the stage-1-approved spec-delta `prototype/2026-07-22-spec-format/delta/spec-delta.md` (six requirements, 56 criteria), reviewed in `docs/prover/2026-07-22-row445-spec-format-delta.md` and its gates plan `prototype/2026-07-22-spec-format/delta/gates-plan.md`. The section is authored into the requirements genre as its own unit and inserted into the assembly right after `composing-across-axes`, last before the Reference tail — it is meta-law about the document itself.

`Rn` names Requirement n in `section.md`; `Rn.k` means Requirement n, criterion k.

## Part 1 — zero-drop over the 22 minted codes

The section homes the 22 format-law codes INV-250..271. Every one appears on a criterion in `section.md`; the table names each code's home criteria. Two codes are cross-references the section leans on, not homes it mints: `INV-198` (the pen's serialization of shared writes, home base-rulebook/parallel-lanes) at R3.12, and `INV-239` (the named-reference pair, home base-rulebook) at R2.7 where its description-field gate retires.

| Code | Law | Home criteria |
|---|---|---|
| INV-250 | the document shape: preamble, glossary, body of requirements in named cases | R1.1, R1.2, R1.3 |
| INV-251 | the criterion form: one rule per criterion, trailing anchor, lowercase-italic keywords, no all-caps, the style lint's red | R1.4, R1.5, R1.6 |
| INV-252 | a source hole is recorded as a `[GAP: ...]` line, never filled by invention | R1.7, R1.8 |
| INV-253 | history lives in `JOURNAL.md`; a dated or provenance sentence in the body is a defect | R1.9, R1.10 |
| INV-254 | closed vocabulary: every domain noun holds exactly one glossary entry | R1.11, R1.12 |
| INV-255 | one name per thing everywhere in the document | R1.13, R1.14 |
| INV-256 | a weak word fills every slot it opens, or the weak-word check reds | R1.15, R1.16 |
| INV-257 | an evaluative phrase names its judge and inputs, or the panel treats it as blocking | R1.17, R1.18 |
| INV-258 | the index is generated output, built from the criteria at freeze, never hand-edited | R2.1, R2.2 |
| INV-259 | body and build must agree, or the index gate reds (both directions) | R2.3, R2.4 |
| INV-260 | a spec-touching delivery declares a delta record, one delta kind per touched code | R3.1 |
| INV-261 | the classifier diffs old vs new criteria sets under normalization and reds on an undeclared appearance, disappearance, or text change; re-diffs after a merge | R3.2, R3.3, R3.4, R3.5, R3.13 |
| INV-262 | a sharpen replaces its old sentence: survival by normalized full-sentence match | R3.6, R3.7 |
| INV-263 | growth stays inside the declared new-criteria budget, sharpen and glossary bytes excluded | R3.8, R3.9, R3.10, R3.11 |
| INV-264 | the size ratchet: bytes-per-criterion recorded, moves only down, governs PRODUCT_SPEC.md alone | R4.1, R4.2, R4.3, R4.4, R4.5, R4.6, R4.7 |
| INV-265 | raising the bound is a change to Requirement 4, run through the pipeline | R4.8 |
| INV-266 | the mechanical layer runs first and free, and stops the section on a red | R5.1, R5.2 |
| INV-267 | the cold-reader panel; two consecutive zero-blocking reads pass; four failing rounds escalate | R5.3, R5.4, R5.5, R5.6 |
| INV-268 | a reader-named source hole becomes a queue row citing its criterion | R5.7 |
| INV-269 | every family gate states its reach on the green line; a zero-scan pass is marked reading nothing | R6.1, R6.2 |
| INV-270 | the whole spec converts in one delivery; every gate arms in that same delivery, none before | R1.19, R1.20 |
| INV-271 | the criteria and glossary are the authored home; the generated index carries locations only; the description-field gate retires | R2.5, R2.6, R2.7 |

All 22 minted codes present; `comm` of the delta's minted set (INV-250..271) against `section.md`'s present set is empty in both directions. No code below INV-250 is homed here — INV-198 and INV-239 ride as cross-references only.

## Part 2 — atomic-claim coverage against the source delta

The source delta is already written in the requirements genre, so its six requirements map one-to-one onto this section's six, criterion for criterion. Every delta criterion carries into the section under the same code with its behaviour unchanged; the two edits below are the only departures, both required by the laws this very section states.

- **R1 Context** and **R2 Context** were rewritten to the present tense, dropping the delta's "Before this migration … After it …" framing. The delta was a standalone document where a provenance sentence is lawful; as an assembled spec section it states today's behaviour only (INV-253, the no-history law this section homes). No criterion changed.
- **R2.5** drops the delta's leading "After the migration," clause for the same reason; the authored-home rule it states is unchanged.
- **R2 Context** folds in the authored-home statement (criteria and glossary the home, the table locations only) so the Context previews R2.5–R2.7; no new claim.
- **R5.3's GAP line** is reworded from the delta's "this delta does not state …" to a plain statement of the hole ("the number of cold readers that form one panel, and the actor that supplies them, are unstated"); the hole is the same one the gates plan carries, and `GAPS.md` records it.
- **R3.9** drops the delta's provenance tail ("whose seed value is the pilot rewrite's measured average bytes per criterion, stated in the pilot's `NUMBERS.md`"). The 500-byte cap — the normative value — stands; the reason the cap is 500 is provenance and lives in `JOURNAL.md`, per this section's own no-history law (INV-253). Two cold readers flagged the tail as the section violating the very rule it states.
- **R1.4** is reworded from the delta's "state one trigger and one response" to "state a single response, opened by at most one trigger" — true against the body, where an unconditional criterion carries a response and no trigger; the requirement-shape gate already treats trigger-counting as a cold-reader judgment, not a lint. From the cold-read panel (round 2), which caught the section's own criterion-form rule reading as violated by a third of its criteria.
- **R2** is one-named to "generated index" (title, Context, R2.1), the glossary tying it to "code-to-location table"; the round-2 panel flagged the three names (lookup index / code-to-location table / generated index) against the section's own one-name rule.
- **The criterion-form wording (glossary `criterion`/`response`, R1.4)** is aligned with the practice the shape gate deliberately holds: a criterion states one rule — a single situation with the duty that holds in it, its *shall* clauses joined where the duty has parts — and whether a line packs two rules is the cold reader's judgment, never a keyword count. The delta's literal "one trigger and one response" read as mandatory-trigger and single-clause, which the corpus (and the delta's own criteria) falsify; rounds 3–5 of the panel each caught a face of that mismatch. INV-251's duty is unchanged; the trigger stays at most one.
- **`entity`** gains a glossary addition (a numbered part of the product a code can name, as against a rule of behaviour) — round 5 flagged it as an undefined domain noun in R2.5.
- **One name for the arming event**: R2.7's "migration-end delivery" is renamed to "the conversion delivery", the name R1.20 already uses, and the term gains a glossary addition — rounds 5–6 caught the two names for one event against the section's own one-name law and the term's absence from the glossary.
- **R1.6 is added** (the panel's round-7 find): the style lint — the fourth mechanical lint R5.1 names — had no red-condition criterion while its three siblings each carry one; R1.6 states it (*if* a line breaks the criterion form or the capitals rule, *then* the style lint *shall* red), under INV-251, no new code minted. R1's later criteria renumber by one; the assembled criteria count grows to 57 for this unit.
- **Vocabulary closure from rounds 6–7**: glossary additions `evaluative phrase` and `conversion delivery`; the `delta kind` entry's "examples moved" reworded to "its placement moved"; R3.12 reworded from "the existing single-pen serialization" to "the pen — the one-writer-at-a-time serialization the shared spec document already carries" with `pen` added to the intro's imported-terms list; R3.13's "post-merge freeze baseline" reworded to "the criteria set of the freeze taken after that merge" (defined terms only); the `size ratchet` glossary entry aligned with R4.8's amendment road ("never raises on its own").
- **R2.5** spells "entity code" out inline ("a code that names an entity — a numbered part of the product") so the section reads self-contained, the assembled preamble's `E-` explanation not being in view of a section-standalone reader. **R6.2** is reworded from "mark the pass as reading nothing rather than printing a bare green line" to "print a line naming that it scanned nothing, and shall not print a bare green line" for a stranger to act on; INV-269's duty is unchanged. Both from the cold-read panel.

Every other criterion is the delta's criterion verbatim under its code. Verified by reading each section criterion back against the delta criterion its code names.

## Part 3 — glossary additions

The section's `## Glossary additions` block carries the 31 nouns the delta introduces, minus `gate` (already pooled from the assembly's shared additions) and minus the base-glossary nouns the delta itself does not restate (spec, journal, queue, backlog item, guardrail, suite, session, compaction, delivery). Each added noun is used in this section's body, so none is a dead entry; `check-vocabulary` over the assembled document confirms it.

## Coverage result

57 criteria over six requirements — the delta's 56 plus the panel-added R1.6 (the style lint's red condition, INV-251) — homing 22 codes (INV-250..271) with two cross-references (INV-198, INV-239). One source hole rides as a `[GAP]` line and is detailed in `GAPS.md`: the panel-size hole (R5.3) the delta already carried. No behavioural claim of the source delta is left uncovered, and no criterion carries a claim the source did not make beyond the declared R1.6. Panel history: eight rounds of two fresh zero-context readers each; every blocking finding fixed at source the same round; round 8's two reads both returned zero blocking — the two consecutive clean reads the comprehension gate demands.
