# Numbers — "When agents work together" conversion

All counts are UTF-8 bytes.

## Source

| Piece | Bytes |
|---|---|
| Source section body (`PRODUCT_SPEC.md` lines 1440–1616) | 57,639 |
| Consumed Formal-index rows (76 distinct cited codes, one row each) | 69,994 |
| **Source total read (body + consumed index rows)** | **127,633** |

The section cites 76 distinct Formal-index codes, and every one has an index row; all 76 rows are consumed (mapped to a criterion in `mapping.md`).

## Output — `section.md`

| Piece | Bytes |
|---|---|
| Preamble | 788 |
| Glossary additions (22 new terms) | 3,364 |
| Requirements (R1–R9, 100 criteria) | 29,971 |
| **section.md total** | **34,123** |

## Ratio

| Comparison | Ratio |
|---|---|
| section.md total ÷ source section body | 0.592 |
| section.md total ÷ (source body + consumed index rows) | 0.267 |
| requirements block ÷ source section body | 0.520 |

The converted section is about **0.57×** the source section body's bytes, and about **0.26×** the full source read once the consumed index rows are counted in — the requirements format states the same behaviour more compactly than the source prose, which carries its rationale, its provenance, and its history inline (all of which move to the journal under the no-history law).
