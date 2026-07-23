# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured with a command, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source section body | 38,126 | `PRODUCT_SPEC.md` lines 2031–2092: `### Composing across axes` and its nested `#### Document provenance` subsection, from the heading to the line before `### Open decisions`. |
| (b) Consumed Formal-index rows | 18,913 | The Formal-index rows for the 18 codes whose index home is `Composing across axes` — the codes this rewrite converts in full (`C-1`, `INV-72`, `INV-125`, `INV-126`, `INV-127`, `INV-138`, `INV-163`, `INV-172`, `INV-173`, `INV-175`, `INV-176`, `INV-178`, `INV-180`, `INV-217`, `INV-226`, `INV-243`, `INV-244`, `INV-248`). The other 39 cited codes are cross-references whose rows are consumed by their home units, so their rows are not counted here. |
| (a+b) Combined source basis | 57,039 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 47,661 |
| — preamble (title + code legend + carried-terms note) | 1,585 |
| — glossary additions (5 new domain nouns) | 1,124 |
| — requirements (19 requirements, 51 named cases, 111 criteria, 2 GAP lines) | 44,952 |

## The two ratios

**(c) / (a+b) = 47,661 / 57,039 = 0.836.** The whole-basis ratio: the output is 84% of the combined source-prose-plus-cited-index mass. This figure folds the 18,913 bytes of Formal-index rows into the denominator; the new format does not rewrite those rows — the trailing anchors keep pointing at the same index — so the index is shared infrastructure counted once on each side, and putting it in the denominator flatters the format. The prose-to-prose ratio is the honest measure of the format's own weight.

**Requirements bytes / source body = 44,952 / 38,126 = 1.179.** The structured requirements come out about 18% larger than the source prose they replace.

## What the ratio means, and why this section grows

This section is the mirror image of the bounds machinery pilot, which shrank to 0.683× of its source. The difference is history density. Bounds was the document's most provenance-heavy section — thick with dates, named-instance narratives, and row-number cross-references — and the no-history law stripped that weight, more than paying for the format's added scaffolding.

This composition essay carries almost no strippable history in its prose. Its provenance sits in short parenthetical incidents ("the worked incident: an inspect zoom … 2026-07-16", "recorded 2026-07-09", "the 2.5.0 design review's finding 2") that the no-history law removes, but those parentheticals are a small share of the source bytes. The bulk of the source is dense law prose — long single-sentence clauses, each packing a full invariant and its cross-references. Converting that prose into the requirements form adds Context blocks, User Story lines, named-case headers, and one-criterion-per-line structure, and there is little history to offset the addition. So the section grows.

The growth is also honest about what the format buys: the source's longest paragraphs (INV-244 at roughly 3,400 bytes, INV-248 at roughly 2,100) were single blocks a stranger could not enter; they are now 14 and 9 numbered criteria a first-time reader can walk one line at a time. The format trades a modest byte increase for a large legibility increase on exactly the paragraphs that were least legible.

## The finding, in one line

Converting `### Composing across axes` to the requirements format **grows the prose by about 18%** (1.179× body) because the essay is dense law prose with little strippable history, so the format's scaffolding is not offset the way it was in the history-heavy bounds section; the 0.836 whole-basis ratio only looks like a shrink because it counts the unchanged Formal index inside the source basis.
