# NUMBERS — the size of the format-laws section

All figures are bytes (UTF-8), measured on `section.md`.

## The source

The source is the stage-1-approved spec-delta `prototype/2026-07-22-spec-format/delta/spec-delta.md`, already written in the requirements genre: six requirements, 56 criteria, glossary additions of 31 nouns; the cold-read panel added one criterion (the style lint's red condition) and three glossary nouns. This section is not a prose-to-requirements conversion but a genre-to-genre landing — the delta's requirements authored into an assembly unit and de-historied to the no-history law (INV-253) they themselves state.

## The produced output

| Item | Bytes |
|---|---:|
| `section.md` total | 21,282 |
| — head (title, preamble, glossary additions) | 6,027 |
| — criterion lines (57 criteria) | 9,151 |
| — the rest (requirement headings, Context, User Story, case headers) | 6,104 |

| Measure | Value |
|---|---:|
| Requirements | 6 |
| Named cases | 25 |
| Criteria | 57 (the delta's 56 plus the panel-added style-lint red, R1.6) |
| Glossary additions | 34 |
| **Bytes per criterion (criterion lines only)** | **160.5** |

## Reading the ratio

The section's 160.5 bytes per criterion sits well under both the spec-wide size ratchet (209.0, INV-264) and the 500-byte per-new-criterion cap the delta seeds (INV-263). The criteria are terse trigger-response lines by construction, and the format-law domain carries no history to strip, so the density is naturally high. Folded into the assembly, the whole document's bytes-per-criterion falls to 206.9 (from 209.0), because the 57 dense criteria pull the mean down — the ratchet lowers to 206.9 at the freeze.

## The finding, in one line

The format-law section adds 57 criteria at 160.5 bytes each and **lowers** the document's bytes-per-criterion ratchet rather than raising it.
