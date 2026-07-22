# Numbers — genre 3 (EARS + user story, with a closed vocabulary)

## Bytes

| Piece | Bytes |
|---|---|
| Source subsection ("Intake: classifying and shaping a wish"), from genre2 NUMBERS | 6,278 |
| Its 25 cited index rows, from genre2 NUMBERS | 11,019 |
| **Source total** | **17,297** |
| genre2 `sample.md` (glossary + 6 requirements, 68 criteria) | 12,000 |
| genre3 `sample.md` (glossary of 34 terms + 7 requirements, 98 criteria in 32 named cases, 3 GAP lines) | 26,977 |

A second cold read confirmed comprehension and listed nine stumbles; fixing them (six new glossary entries, a named channel for spoken withdrawals, the concrete owner of a three-source disagreement, the inbox file-date rule as its own criterion) added 1,256 bytes over the first genre3 draft (20,974). A third cold read listed ten precision stumbles; fixing them (the four code-prefix kinds named in the preamble, the provisional-click half-sentence, plain glosses for backpointer, safety gate, session counters, and the context-trim routine, the phrase-by-phrase pre-ask mechanism) added another 710 bytes. A fourth read left one blocking finding — the entry-route set and the bug route's behaviour were never named — and fixing it (the five routes in the glossary, the bug route's failing-test-first entry and its park-and-resume interrupt as criterion R3.7, codes T-9 and T-12 added) plus two term alignments added another 519 bytes. A fifth read from a different fresh reader raised three blocking terms — session, aspect, richness — and fixing them (a glossary entry for session; the feature-dimension list stated inline from the source's own facet sweep; the cut's adjustable content stated from the source's own cut definition) added another 415 bytes. A final two-reader panel returned seven blocking items — double names, unstated effects, and one word on two axes — and fixing them (one name per artifact: decision archive, the delivery report's batched section; the defect effect and the size-route tie stated from the source; two new glossary entries; one new GAP on the disagreement outcomes' routes) added another 1,085 bytes. On the owner's approval two format changes landed — criteria grouped into named cases (Requirements 3 and 4 renumbered, two compound criteria split) and the keywords set lowercase italic — together with the fourth law's relational-word sweep (nine slot fills: several, plainer, shortened, clean, oversized, and the cut's two comparatives), adding another 2,018 bytes.

## Deltas

- genre3 vs genre2: **+14,977 bytes** (26,977 / 12,000 = **2.248**, a 125% increase).
- genre3 vs source total: 26,977 / 17,297 = **1.560** (56% larger than the source it replaces).

genre3 is larger than the source, where genre2 was smaller (0.694). The three new laws are the cost. They buy the readability the owner asked for, and they do it by adding text rather than compressing it.

## Where the growth went

The three laws each add a measurable block. The rest of the increase is in the criteria themselves, which now name their judge and inputs (LAW 3) rather than stating a bare judgment.

| Cause | Bytes | Note |
|---|---|---|
| Glossary (LAW 1, closed vocabulary) | 3,866 | genre2's glossary held 5 terms; genre3's holds 31, one sentence each. |
| Context blocks (LAW 2) | 2,041 | Seven `**Context:**` blocks, 2–4 plain sentences each, one per requirement. |
| New Requirement 4, the three-source impact read (INV-128) | 1,805 | Added to answer owner complaint 5. genre2 did not carry this code in its `sample.md`; it appeared only in the genre2 COMPARE page. |
| Header and reading note (bracket-code line, the four prefix kinds, keyword note) | ~940 | Explains what the `[INV-x]` codes are, names the four prefix kinds (invariant, transition, entity, rhythm rule), and states what the keywords mean. |
| LAW 3 judge-and-input clauses, spread across the criteria | ~2,000 (est.) | The critical mark's effect (INV-133, R3.6–R3.10), the quick-win effect (R3.12–R3.13), the broken-by-three-tests inputs, the two `[GAP]` lines, the reader-check and self-answer test spelled out in plain words (R6.4–R6.5), the concrete owner of a three-source disagreement (R4.7), and the inbox file-date rule (R5.12). |

Sum of the four measured blocks: about 9,300 bytes. That accounts for 85% of the 10,940-byte increase. The remainder is the LAW 3 clauses and the plain-gloss rewrites distributed through the criteria.

## Did the three laws grow the text, and by how much

Yes. All three grow it.

- **LAW 1 (closed vocabulary)** added roughly 3,400 bytes: a glossary of 31 terms in place of genre2's 5.
- **LAW 2 (context before criteria)** added roughly 2,000 bytes: one Context block per requirement.
- **LAW 3 (name the judge and inputs)** added roughly 2,000 bytes to the criteria, plus it forced the new INV-133 and quick-win-effect lines that genre2 never stated.

The single largest addition, though, is content genre2 omitted rather than a law: Requirement 4 (INV-128, 1,805 bytes) exists only because the owner asked for the three-source read in plain words.

## Projection to the whole spec

genre2 projected the whole 783,678-byte spec at its 0.694 ratio to about 543,685 bytes. genre3's ratio to the same source is 1.560, so a flat projection gives about **1,222,000 bytes** — larger than the current spec.

This projection is rough and probably an overstatement. The glossary is a fixed cost paid once for the whole document, not per subsection, so its 3,216 bytes would not repeat across every area; amortised over the full spec it nearly vanishes. The Context blocks and the judge-and-input clauses do scale with the number of requirements. genre3 trades size for a first-read a stranger can follow. genre2 optimised for bytes; genre3 optimises for the owner's complaint that he could not understand genre2.
