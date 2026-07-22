# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured, not estimated except where a line says "estimate".

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source section body | 49,554 | `PRODUCT_SPEC.md` lines 1163–1438, the whole `## Starting and adopting a project` section from its heading to the line before the next `##`. |
| (b) Consumed Formal-index rows | 46,063 | The 95 index rows whose code the section cites (every cited code except the 5 inline feature codes `F-*`, which have no index row). Each row carries two long description columns. |
| (a+b) Combined source basis | 95,617 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 54,244 |
| — preamble (title + format note) | 738 |
| — glossary additions (new domain nouns) | 3,812 |
| — requirements (21 requirements, 63 named cases) | 49,694 |

## The ratio

**(c) / (a+b) = 54,244 / 95,617 = 0.567.**

Read on its own this says the rewrite is 57% of the combined source-prose-plus-cited-index mass. That figure is honest arithmetic but it is easy to misread, so the next section states what it does and does not mean.

## What the ratio actually measures

The (a+b) denominator folds in 46,063 bytes of Formal-index rows. The new format does **not** rewrite those rows. It keeps pointing at the same index through the trailing code anchors (`[INV-8]`, `[A-5]`, …), exactly as the source prose already did. So the index is shared infrastructure that is unchanged on both sides and counted once in each. Putting it in the denominator makes the format look like it shrinks the document, when what it really does is fold prose into structured prose and leave the index alone.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 49,694 / 49,554 = 1.003.**

The structured requirements come out at essentially 1:1 with the source prose they replace. The format's added scaffolding — Context blocks, User Story lines, named-case headers, one-criterion-per-line — is paid for almost exactly by what it drops: history and provenance sentences (this section's reconciliation clauses, dated notes), and the removal of long inline hedging. The two roughly cancel.

## The whole-file projection

Whole-file measured totals:

| Region | Bytes |
|---|---:|
| Body (everything before the Formal index) | 514,001 |
| Formal index (heading to end of file) | 269,676 |
| Body + index | 783,678 |

**Projection 1 — the literal ratio applied to body+index.**
0.567 × 783,678 ≈ **444,600 bytes.**
Stated plainly, this treats the whole document the way (a+b) treated the section: it counts the index inside the basis. Because the index is not actually rewritten, this number understates the true size of a fully converted document. It is the figure the ratio formula yields, reported for completeness.

**Projection 2 — the replacement view (the honest one).**
Assumptions, stated plainly:

1. **Shared glossary counted once.** The glossary is written one time for the whole document, not per section. Sample.md's base glossary (~2.6 KB, ~34 terms) already exists once. This section's new-noun additions were 3,812 bytes for ~24 nouns; across the whole document the pooled additions block is a one-time cost, estimated at ~14 KB (many nouns are shared across sections and counted once).
2. **History/provenance drop included.** The new format omits dates, provenance, and past-choice reasoning. That drop is already inside the 1.003 requirements-to-body figure, which is why the structured prose is not larger than the source despite its extra scaffolding.
3. **The Formal index is unchanged.** The anchors keep pointing at it; it is neither expanded nor rewritten.

Projected whole-document size:

| Component | Bytes | Basis |
|---|---:|---|
| Requirements prose | ~515,400 | 514,001 × 1.003 |
| Formal index (unchanged) | 269,676 | measured |
| Pooled glossary additions (one-time) | ~14,000 | estimate, shared once |
| **Total** | **~799,000** | |

Against today's 783,678 bytes, a full conversion lands at roughly **+2%** — essentially flat.

## The finding, in one line

Converting this spec to the requirements format is **size-neutral on the prose** (1.00× body, the added structure paying for the dropped history) and **near-flat on the whole document** (~+2%, a one-time shared glossary). The eye-catching 0.567 ratio is an artifact of counting the unchanged Formal index inside the source basis; it is reported because the task defines the ratio that way, but the replacement view is the one that answers "does this format grow the spec".
