# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source range body | 3,069 | `PRODUCT_SPEC.md` lines 1–47: the title line, the how-to-read note, the built-and-planned block, and the whole `## What live-spec is` section up to the line before `## The build loop`. |
| (b) Consumed Formal-index rows | 2,372 | The Formal-index rows for the 8 codes the range cites (S-0, E-1, E-6, E-7, E-10, E-12, E-18, A-6). Every cited code carries an exact index row, so all 8 are counted. |
| (a+b) Combined source basis | 5,441 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 6,543 |
| — preamble (title + covering paragraph + code legend + reuse note) | 1,640 |
| — glossary additions (3 new domain nouns) | 544 |
| — requirements (3 requirements, 5 named cases, 11 criteria) | 4,359 |

## The ratio

**(c) / (a+b) = 6,543 / 5,441 = 1.203.**

Read on its own this says the rewrite is 120% of the combined source-prose-plus-cited-index mass — a growth even on the whole basis, which is unusual: the machinery and rules sections both came in below 1.0 on this basis because their cited-index mass was large. This opening cites only 8 short index rows, so the shared-index term barely pads the denominator, and the growth shows through.

## What the ratio actually measures

The (a+b) denominator folds in 2,372 bytes of Formal-index rows. The new format does **not** rewrite those rows — it keeps pointing at the same index through the trailing code anchors (`[E-1]`, `[S-0]`, …), exactly as the source prose already did. So the index is shared infrastructure, counted once in each and unchanged on both sides.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 4,359 / 3,069 = 1.420.**

The structured requirements come out at about one and two-fifths of the source prose they replace — the largest growth of the sections measured so far (the founding pilot at 1.003, the machinery section at 0.683, the rules section at 1.213). Two causes, both proper to an opening. First, the source range is terse introductory prose with no dated provenance for the no-history law to strip, so the format's scaffolding — Context blocks, User Story lines, named-case headers, one-criterion-per-line — is paid for by nothing. Second, this is a small unit carrying the whole document's preamble and code legend as a fixed cost; that cost is a constant the requirements do not amortize the way a large section does. The growth is real but it is front-loaded overhead, not a per-requirement tax that scales.

## The whole-file note

This unit is too small to project a document-wide figure from on its own, and its 1.420× is the top of the observed range precisely because it is the least history-bearing and most overhead-heavy region of the document. The document-wide replacement estimate is the one the machinery and rules `NUMBERS.md` files carry, bracketed by section character (0.683× for history-heavy machinery, 1.213× for history-light authority prose); this opening sits above that upper bracket because its preamble overhead is a one-time cost the assembled document pays once, not once per section.

## The finding, in one line

Converting the document's opening to the requirements format **grows the prose to about one and two-fifths** (1.420× body) because the passage carries no history to strip and shoulders the whole document's preamble-and-legend overhead as a fixed cost; the 1.203 whole-basis ratio is high for the same reason the others were low — this opening cites only a handful of short index rows, so the unchanged Formal index does not pad the basis here the way it does for a code-dense section.
