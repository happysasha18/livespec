# Numbers

All byte counts are of the standalone slice files in this directory, measured with `wc -c`.

## Index slice (12 contiguous Formal-index rows, including INV-128)

| File | Bytes | What it holds |
|---|---|---|
| before-index.md | 8,715 | The 12 rows exactly as they stand in the spec today (anchor column, description column, section column). |
| after-index.md | 3,522 | New format: one row per code, `code \| rule`, where rule is the current Description-column sentence verbatim plus a trailing bare `related:` list. |
| journal-export.md | 5,731 | The anchor-column text harvested out, one verbatim block per code, bound for JOURNAL.md. |

Within this slice, INV-128 is the worst-accretion row: its anchor column is 1,653 bytes wrapping a 305-byte description sentence.

Index after/before ratio inside the spec file: 3,522 / 8,715 = **0.4041**. The harvested provenance (5,731 bytes) leaves PRODUCT_SPEC.md for JOURNAL.md, where it stays available, so it does not count toward the spec file's size.

## Body slice (one subsection: "Intake: classifying and shaping a wish")

| File | Bytes | What it holds |
|---|---|---|
| before-body.md | 6,278 | The subsection verbatim. |
| after-body.md | 5,151 | Phase-2 sample: tightened scenario prose that keeps every behavioural fact and every trailing code cite, drops sentences that only restate an index rule already carried by its code cite, and drops inline provenance. |

Body after/before ratio: 5,151 / 6,278 = **0.8205**.

## Extrapolation to the full file

Stated assumptions:

1. The full file is 783,678 bytes. The Formal index is 269,676 bytes of that; the remaining 514,002 bytes are body and other prose.
2. The 12-row index slice stands in for the whole index, applying its 0.4041 after/before ratio uniformly. The slice was chosen to include INV-128, the worst-measured accretion, so its ratio shows more shrink than a file-wide average would. The phase-1 projection below therefore leans optimistic.
3. Phase 1 touches only the index. It moves each anchor line's dates, provenance, and cross-reference narrative into the journal export and keeps the Description sentence plus a bare `related:` list. Body prose is unchanged by phase 1.
4. Phase 2 touches only body scenario prose, applying the body slice's 0.8205 ratio uniformly to the 514,002-byte non-index portion. The index is unchanged by phase 2, since phase 1 already reduced it.
5. Table and heading framing bytes are small and are treated as part of each slice.

Projected index after phase 1: 269,676 x 0.4041 = 108,984 bytes.

Projected body: unchanged by phase 1 at 514,002 bytes; after phase 2, 514,002 x 0.8205 = 421,731 bytes.

**Projected full file after phase 1 only: 108,984 + 514,002 = 622,986 bytes** (79.5% of today's 783,678; a reduction of 160,692 bytes).

**Projected full file after phase 1 + phase 2: 108,984 + 421,731 = 530,715 bytes** (67.7% of today's 783,678; a reduction of 252,963 bytes).

## Verification results

**1. Each after-index rule sentence is byte-identical to its Description-column source.** Check run: parse both `before-index.md` and `after-index.md` into columns on the pipe delimiter; for each after-index row, split the rule cell on the literal ` related: ` marker and compare the leading sentence against the Description column of the same code in the source. Result: 12/12 sentences byte-identical.

**2. Every code cited in before-body still appears in after-body.** Check run: extract every `[A-Z]{1,5}-[0-9]+` token from each file and diff the sets. before-body carries 25 distinct codes; after-body carries the same 25. Missing set is empty.

**3. journal-export.md contains every content sentence dropped from the 12 anchor lines.** Check run: for each of the 12 source rows, confirm the full anchor-column text is present verbatim as a substring of `journal-export.md`. Result: 12/12 anchor lines present verbatim. Because the whole anchor line is carried into the journal unmodified, every sentence it held is present.
