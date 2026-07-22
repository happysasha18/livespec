# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured with a command, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source section body | 15,201 | `PRODUCT_SPEC.md` lines 928–1055, the whole `## What the human sends back` section from its heading to the line before `## When something breaks`. |
| (b) Consumed Formal-index rows | 16,022 | The Formal-index rows for the 29 codes the section cites. Every cited code carries an exact index row (this scenario section names no inline-only feature code), so all 29 rows are counted. The two feature tags (`F-feedback`, `F-feature-map`) have no index row and add nothing here. |
| (a+b) Combined source basis | 31,223 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 18,100 |
| — preamble (title + code legend + carried-terms note) | 1,543 |
| — glossary additions (7 new domain nouns) | 1,268 |
| — requirements (8 requirements, 22 named cases, 42 criteria) | 15,289 |

## The ratio

**(c) / (a+b) = 18,100 / 31,223 = 0.580.**

Read on its own this says the rewrite is 58% of the combined source-prose-plus-cited-index mass. That figure is honest arithmetic but easy to misread, so the next section states what it does and does not mean.

## What the ratio actually measures

The (a+b) denominator folds in 16,022 bytes of Formal-index rows. The new format does **not** rewrite those rows — it keeps pointing at the same index through the trailing code anchors (`[T-20]`, `[INV-68]`, …), exactly as the source prose already did. So the index is shared infrastructure, unchanged on both sides and counted once in each. Putting it in the denominator makes the format look like it shrinks the document, when what it really does is fold prose into structured prose and leave the index alone.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 15,289 / 15,201 = 1.006.**

The structured requirements come out essentially flat against the source prose they replace — the same result the founding-section pilot measured (1.003), and unlike the provenance-heavy machinery section (0.683, a third smaller). The cause is this section's own character: it is a use-case scenario section, already written close to the format, with little dated provenance for the no-history law to strip. Its source prose does carry some hedging and cross-reference narration, but the format's added scaffolding (Context blocks, User Story lines, named-case headers, one-criterion-per-line) roughly balances what the rewrite drops, so the structured version lands at the source's own size.

## The finding, in one line

Converting this scenario section to the requirements format holds the prose **flat** (1.006× body) because the section carries little history for the no-history law to remove; the 0.580 whole-basis ratio is an artifact of counting the unchanged Formal index inside the source basis, and the replacement view (about 1×) is the one that answers "does this format grow the spec": here, it does not.
