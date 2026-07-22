# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured with a command, not estimated. The unit is `PRODUCT_SPEC.md` lines 277–620 (the second half of `### Throwing a wish` in `## The build loop`).

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source unit body | 96,745 | `sed -n '277,620p' PRODUCT_SPEC.md | wc -c` — the three assigned `####` blocks. |
| (b) Consumed Formal-index rows | 90,635 | The `### Formal index` table rows for the 131 cited codes that carry one (of 132 cited; `T-7` has no row), matched by first-column code and summed with `wc -c`. |
| (a+b) Combined source basis | 187,380 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 103,931 |
| — preamble (title + code legend + carried-terms note) | 1,535 |
| — glossary additions (19 new domain nouns) | 2,646 |
| — requirements (61 requirements, 116 named cases, 223 criteria) | 99,750 |

The three parts sum to the total (1,535 + 2,646 + 99,750 = 103,931).

## The ratio

**(c) / (a+b) = 103,931 / 187,380 = 0.555.**

Read on its own this says the rewrite is 55% of the combined source-prose-plus-cited-index mass. That figure is honest arithmetic but easy to misread, so the next section states what it does and does not mean.

## What the ratio actually measures

The (a+b) denominator folds in 90,635 bytes of Formal-index rows. The new format does **not** rewrite those rows — it keeps pointing at the same index through the trailing code anchors (`[INV-133]`, `[T-12]`, …), exactly as the source prose already did. So the index is shared infrastructure, unchanged on both sides and counted once in each. Putting it in the denominator makes the format look like it shrinks the document, when what it really does is fold prose into structured prose and leave the index alone.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 99,750 / 96,745 = 1.031.**

The structured requirements come out at about the same size as the source prose they replace — a shade above flat, close to the founding-section pilot's 1.003 and the opposite of the bounds machinery section's 0.683 shrink. The cause is this unit's own character: it is a use-case-and-procedure section, not a provenance-dense machine catalogue. Its source prose carries some history the no-history law strips (named-incident dates, row-number cross-references, probe-repo verification stamps), but far less than the bounds section, and the format's added scaffolding — Context blocks, User Story lines, named-case headers, one-criterion-per-line, and the split of long compound source sentences into separate `shall` criteria — very nearly balances the dropped history. The result is flat.

## The whole-file projection

Whole-file measured totals (from the pilot's own measurement, unchanged):

| Region | Bytes |
|---|---:|
| Body (everything before the Formal index) | 514,001 |
| Formal index (heading to end of file) | 269,676 |
| Body + index | 783,678 |

**Projection 1 — the literal ratio applied to body+index.**
0.555 × 783,678 ≈ **434,900 bytes.** This treats the whole document the way (a+b) treated the unit, counting the unchanged index inside the basis. Because the index is not actually rewritten, this understates a converted document's true size; it is reported for completeness because the task defines the ratio that way.

**Projection 2 — the replacement view (the honest one).** Three converted sections now bracket the real answer: the founding section measured 1.003× on its prose, the bounds machinery section 0.683×, and this build-loop unit 1.031×. None is the document-wide figure — different sections carry different history loads — but together they place a document-wide replacement estimate **at or just under the source body size**. Using the bounds section's 0.683× as a lower bound and this unit's 1.031× as an upper bound:

| Component | Bytes | Basis |
|---|---:|---|
| Requirements prose (whole body) | ~351,100 to ~529,900 | 514,001 × 0.683 (bounds) to × 1.031 (this unit) |
| Formal index (unchanged) | 269,676 | measured |
| Pooled glossary additions (one-time) | ~14,000 | shared once across sections |
| **Total** | **~635,000 to ~814,000** | |

Against today's 783,678 bytes, a full conversion lands between roughly **−19%** (if the whole document sheds history at the bounds rate) and **+4%** (this unit's near-flat rate). The truth sits between, since the provenance-heavy machinery section is the outlier and most sections read closer to this build-loop unit.

## The finding, in one line

Converting this build-loop unit to the requirements format leaves the prose **essentially flat** (1.031× body) — it is use-case-and-procedure text carrying modest history, so the format's scaffolding nearly balances the history the no-history law strips; the 0.555 whole-basis ratio is an artifact of counting the unchanged Formal index inside the source basis, and the replacement view is the one that answers "does this format grow the spec": here, it barely moves it.
