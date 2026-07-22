# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured with a command, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source unit body | 35,361 | `PRODUCT_SPEC.md` lines 48–276: the build-loop intro plus the first half of `### Throwing a wish` (its intro, Intake, Naming and reporting, Showing work and asking for decisions). |
| (b) Consumed Formal-index rows | 37,622 | The Formal-index rows for the 57 cited codes that carry one. Eight cited codes carry no index row — `F-wish` (the feature marker) and `T-1`..`T-7` (the wish-path transitions defined inline in the source's own numbered list, lines 73–78) — so 57 rows are counted, not 65. |
| (a+b) Combined source basis | 72,983 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 53,709 |
| — preamble (title + intro + code legend + carried-terms note) | 1,518 |
| — glossary additions (21 new domain nouns) | 2,969 |
| — requirements (33 requirements, 62 named cases, 136 criteria) | 49,220 |

## The two ratios

**Whole-basis: (c) / (a+b) = 53,709 / 72,983 = 0.736.**

**Prose-to-prose: requirements / (a) = 49,220 / 35,361 = 1.392.**

## What the ratios actually measure

The whole-basis 0.736 folds 37,622 bytes of Formal-index rows into the denominator. The new format does not rewrite those rows — it keeps pointing at the same index through the trailing code anchors, exactly as the source prose already did — so the index is shared infrastructure, unchanged on both sides. Putting it in the denominator makes the format look smaller than it is. Here that effect is milder than in the machinery-section pilot, whose 0.354 leaned on 113 mostly-long index rows: this unit cites only 57 rows, and they are shorter on average, so the index carries less of the basis and the whole-basis ratio sits far higher.

The prose-to-prose replacement is the honest measure of the format's own weight, and here it points the other way: **the structured requirements come out at about 1.39× the source prose they replace — a genuine growth**, the opposite of the machinery section's 0.68× shrink.

The cause is this section's character. It is behaviour-and-policy prose, not provenance-dense narrative. It carries almost no dates, named-instance stories, or inline hedging for the no-history law to strip — the two source lines that did carry provenance markers ("2026-07-…", "the owner's word") drop cleanly, but there was little of it to begin with. So the format's added scaffolding — a Context block and a User Story line per requirement, named-case headers, one-criterion-per-line, and 33 requirements each with its own frame — is added weight that little dropped history offsets. Where the machinery section paid for its scaffolding out of stripped history and still shrank, this section pays for its scaffolding out of nothing and grows.

## Where this unit sits in the whole-document picture

Three sections now measure their prose-to-prose replacement, and together they bracket the document-wide answer, since sections carry different history loads:

| Section | Prose-to-prose | Character |
|---|---:|---|
| Founding (pilot) | 1.003× | use-case prose, near the format already |
| This unit (Throwing a wish, first half) | 1.392× | behaviour-and-policy prose, little history |
| What holds the bounds (machinery) | 0.683× | provenance-dense machinery |

A use-case / behaviour section written to explain the product to a person grows under the format (the scaffolding is real cost and there is no history to reclaim), while a provenance-heavy machinery section shrinks (the no-history law reclaims more than the scaffolding costs). A document-wide replacement therefore lands **near or somewhat above the source body size**, its exact figure set by how much of the document reads like this behaviour prose against how much reads like the machinery section. This unit is the growth end of that bracket.

## The finding, in one line

Converting this behaviour-and-policy section to the requirements format **grows the prose to about 1.4× (1.392× body)** because the section carries little history for the no-history law to reclaim, so the format's per-requirement scaffolding is added weight; the 0.736 whole-basis ratio is not a shrink but an artifact of counting the unchanged Formal index — lighter here than in the machinery pilot — inside the source basis.
