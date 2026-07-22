# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source section body | 33,211 | `PRODUCT_SPEC.md` lines 1617–1842, the whole `## The rules and who applies them` section from its heading to the line before `## What holds the bounds`. |
| (b) Consumed Formal-index rows | 52,893 | The Formal-index rows for the 76 codes the section cites. Every cited code carries an exact index row (this section names no inline-only feature code), so all 76 rows are counted. Several of these rows — INV-230, INV-235, INV-237, T-18, T-19, and INV-145 among them — are among the longest in the index. |
| (a+b) Combined source basis | 86,104 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 43,693 |
| — preamble (title + code legend + reuse note) | 1,541 |
| — glossary additions (13 new domain nouns) | 1,885 |
| — requirements (23 requirements, 45 named cases, 102 criteria) | 40,267 |

## The ratio

**(c) / (a+b) = 43,693 / 86,104 = 0.508.**

Read on its own this says the rewrite is 51% of the combined source-prose-plus-cited-index mass. That figure is honest arithmetic but easy to misread, so the next section states what it does and does not mean.

## What the ratio actually measures

The (a+b) denominator folds in 52,893 bytes of Formal-index rows. The new format does **not** rewrite those rows — it keeps pointing at the same index through the trailing code anchors (`[INV-69]`, `[E-13]`, …), exactly as the source prose already did. So the index is shared infrastructure, unchanged on both sides and counted once in each. Putting it in the denominator makes the format look like it shrinks the document, when what it really does is fold prose into structured prose and leave the index alone.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 40,267 / 33,211 = 1.213.**

The structured requirements come out at about one and a fifth of the source prose they replace — a genuine growth, and close to the founding-section pilot's 1.003 (essentially flat) rather than the machinery section's 0.683 (a third smaller). The cause is this section's own character: it is authority-and-role prose, tightly packed conceptual sentences with far less of the dated provenance the machinery section carried. There is less history for the no-history law to strip here, so the format's added scaffolding — Context blocks, User Story lines, named-case headers, one-criterion-per-line — is not paid for by dropped dates, and the structured version comes out larger. What history the source does carry (the worked-proof narratives, the row-number cross-references) is stripped, which is why the growth stays near flat rather than climbing higher.

## The whole-file projection

Whole-file measured totals (from the pilot's own measurement, unchanged):

| Region | Bytes |
|---|---:|
| Body (everything before the Formal index) | 514,001 |
| Formal index (heading to end of file) | 269,676 |
| Body + index | 783,678 |

**Projection 1 — the literal ratio applied to body+index.**
0.508 × 783,678 ≈ **398,100 bytes.** This treats the whole document the way (a+b) treated the section, counting the unchanged index inside the basis. Because the index is not actually rewritten, this understates a converted document's true size; it is reported for completeness because the task defines the ratio that way.

**Projection 2 — the replacement view (the honest one).** Three sections are now measured on their prose: the founding-section pilot at 1.003×, the machinery section at 0.683×, and this rules section at 1.213×. They bracket the real answer by section character: a provenance-heavy machinery section shrinks by a third, a use-case section written close to the format stays flat, and an authority-and-role section with little history to strip grows by a fifth. A document-wide replacement estimate therefore lands **near the source body size**, the growth of history-light sections offsetting the shrink of history-heavy ones. Using this section's 1.213× as the upper bound and the machinery section's 0.683× as the lower bound:

| Component | Bytes | Basis |
|---|---:|---|
| Requirements prose (whole body) | ~351,100 to ~623,500 | 514,001 × 0.683 (machinery) to × 1.213 (this section) |
| Formal index (unchanged) | 269,676 | measured |
| Pooled glossary additions (one-time) | ~14,000 | estimate, shared once across sections |
| **Total** | **~635,000 to ~907,000** | |

Against today's 783,678 bytes, a full conversion lands somewhere between **−19%** (if the whole document sheds history at the machinery rate) and **+16%** (this section's history-light rate). The truth sits between, weighted by how much provenance each section carries.

## The finding, in one line

Converting this authority-and-role section to the requirements format **grows the prose to about one and a fifth** (1.213× body) because the section carries little of the dated provenance the no-history law strips, so the format's own scaffolding is not paid for by dropped history; the 0.508 whole-basis ratio is an artifact of counting the unchanged Formal index inside the source basis, and the replacement view is the one that answers "does this format grow the spec": for a history-light section, modestly, yes.
