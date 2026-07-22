# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source section body | 98,299 | `PRODUCT_SPEC.md` lines 1843–2025, the whole `## What holds the bounds` section from its heading to the line before `## Reference`. |
| (b) Consumed Formal-index rows | 106,813 | The Formal-index rows for the 113 codes the section cites. Every cited code carries an exact index row (this machinery section names no inline-only feature code), so all 113 rows are counted. Several of these rows are among the longest in the index, carrying two long description columns. |
| (a+b) Combined source basis | 205,112 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 72,601 |
| — preamble (title + code legend + reuse note) | 1,465 |
| — glossary additions (24 new domain nouns) | 4,012 |
| — requirements (37 requirements, 100 named cases, 177 criteria) | 67,124 |

Figures include the cold-reader panel's fixes: six in-line glosses for named sub-mechanisms, one glossary entry (far tier), one new `[GAP]` line (the conflicts check), two enumerations the source carries (the three fitness questions, the four bounded documents), the round-2 grounding of the two-objects shape, the base ladder, the traceability-net/feature-coverage-check distinction, and the reminder-history's ledger home, and the round-3 prover-record glossary entry and the three orchestration-law glosses at the conduct judge.

## The ratio

**(c) / (a+b) = 72,601 / 205,112 = 0.354.**

Read on its own this says the rewrite is 35% of the combined source-prose-plus-cited-index mass. That figure is honest arithmetic but easy to misread, so the next section states what it does and does not mean.

## What the ratio actually measures

The (a+b) denominator folds in 106,813 bytes of Formal-index rows. The new format does **not** rewrite those rows — it keeps pointing at the same index through the trailing code anchors (`[INV-202]`, `[E-11]`, …), exactly as the source prose already did. So the index is shared infrastructure, unchanged on both sides and counted once in each. Putting it in the denominator makes the format look like it shrinks the document, when what it really does is fold prose into structured prose and leave the index alone. The index weighs more here than in the founding-section pilot because this machinery section cites more than a hundred codes, many of them the longest rows in the table.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 67,124 / 98,299 = 0.683.**

The structured requirements come out at about two-thirds of the source prose they replace — a genuine shrink, and the opposite of the pilot's 1.003 (essentially flat). The cause is this section's own character: it is the most provenance-dense section in the document. Its source prose is thick with dates, named-instance narratives ("the owner named it …", "the worked instance was …", "recorded live …"), row-number cross-references, and long inline hedging — exactly the material the no-history law strips. The format's added scaffolding (Context blocks, User Story lines, named-case headers, one-criterion-per-line) is more than paid for by the dropped history, so the structured version is smaller.

## The whole-file projection

Whole-file measured totals (from the pilot's own measurement, unchanged):

| Region | Bytes |
|---|---:|
| Body (everything before the Formal index) | 514,001 |
| Formal index (heading to end of file) | 269,676 |
| Body + index | 783,678 |

**Projection 1 — the literal ratio applied to body+index.**
0.354 × 783,678 ≈ **277,400 bytes.** This treats the whole document the way (a+b) treated the section, counting the unchanged index inside the basis. Because the index is not actually rewritten, this understates a converted document's true size; it is reported for completeness because the task defines the ratio that way.

**Projection 2 — the replacement view (the honest one).** The pilot's founding section measured 1.003× on its prose; this machinery section measures 0.683×. Neither is the document-wide figure — different sections carry different history loads. Taken together they bracket the real answer: a use-case section written close to the format already (founding) stays flat, while a provenance-heavy machinery section shrinks by a third. A document-wide replacement estimate therefore lands **at or below the source body size**, not above it. Using this section's own 0.683× as a lower bound and the pilot's 1.003× as an upper bound:

| Component | Bytes | Basis |
|---|---:|---|
| Requirements prose (whole body) | ~351,100 to ~515,400 | 514,001 × 0.683 (this section) to × 1.003 (pilot) |
| Formal index (unchanged) | 269,676 | measured |
| Pooled glossary additions (one-time) | ~14,000 | estimate, shared once across sections |
| **Total** | **~635,000 to ~799,000** | |

Against today's 783,678 bytes, a full conversion lands somewhere between **−20%** (if the whole document sheds history at this section's rate) and **+2%** (the pilot's flat rate). The truth sits between, since most sections carry less provenance than this one.

## The finding, in one line

Converting this machinery section to the requirements format **shrinks the prose to about two-thirds** (0.683× body) because the section is the document's most history-dense and the no-history law strips that weight; the eye-catching 0.354 whole-basis ratio is an artifact of counting the unchanged Formal index — which is unusually heavy here — inside the source basis, and the replacement view is the one that answers "does this format grow the spec": here, it does not.
