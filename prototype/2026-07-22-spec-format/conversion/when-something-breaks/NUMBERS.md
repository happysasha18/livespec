# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured with a command, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source section body | 10,274 | `PRODUCT_SPEC.md` lines 1056–1162, the whole `## When something breaks` section from its heading to the line before `## Starting and adopting a project`. |
| (b) Consumed Formal-index rows | 11,625 | The Formal-index rows for the 24 codes the section cites. Every cited code carries an exact index row (this scenario section names no inline-only feature code), so all 24 rows are counted. The two feature tags (`F-bug`, `F-problem-ledger`) have no index row and add nothing here. |
| (a+b) Combined source basis | 21,899 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 17,327 |
| — preamble (title + code legend + carried-terms note) | 1,570 |
| — glossary additions (4 new domain nouns) | 738 |
| — requirements (8 requirements, 24 named cases, 42 criteria) | 15,019 |

## The ratio

**(c) / (a+b) = 17,327 / 21,899 = 0.791.**

Read on its own this says the rewrite is 79% of the combined source-prose-plus-cited-index mass. That figure is honest arithmetic but easy to misread, so the next section states what it does and does not mean.

## What the ratio actually measures

The (a+b) denominator folds in 11,625 bytes of Formal-index rows. The new format does **not** rewrite those rows — it keeps pointing at the same index through the trailing code anchors (`[T-9]`, `[INV-23]`, …), exactly as the source prose already did. So the index is shared infrastructure, unchanged on both sides and counted once in each. Putting it in the denominator makes the format look like it shrinks the document, when what it really does is fold prose into structured prose and leave the index alone.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 15,019 / 10,274 = 1.462.**

The structured requirements come out at about one and a half times the source prose they replace — a genuine growth, and the opposite of the provenance-heavy machinery section (0.683). The cause is this section's own character. Its source is the most compressed prose in the document: the bug scenario states its behaviour as a terse numbered acceptance list, and the problem ledger states its as dense bullet lists (statuses, walk steps, seams, non-goals) with almost no dated provenance for the no-history law to strip. The requirements format then pays full price for its scaffolding — a Context block and a User Story line per requirement, a named-case header per group, one criterion per line, and full sentences where the source ran clipped bullets — with little history removed to offset it. A source already near a checklist grows when unfolded into stranger-readable requirements.

## The finding, in one line

Converting this scenario section to the requirements format **grows the prose by about half** (1.462× body) because the source is already terse, near-checklist bullets and numbered lists with little provenance to strip, so the format's Context, User Story, and named-case scaffolding is not offset by dropped history; the 0.791 whole-basis ratio is an artifact of counting the unchanged Formal index inside the source basis, and the replacement view is the one that answers "does this format grow the spec": here, it does.
