# Content-preservation proof — ARCHITECTURE.md Nodes conversion (row 456)

**Verdict: PASS — every word token and every punctuation mark cancels; zero content delta**

Compared the OLD `## Nodes` table content (22 data rows, four cells each) against the NEW node sections' content (22 `### [node: ...]` sections, read back through archformat.py), word-token multiset and punctuation multiset, over the content region only. Stage 1 relocates nothing and rewrites nothing, so no content delta is declared and every token must cancel.

## Excluded scaffolding (reported, not compared)

- **Old table framing** — the header row (12 word tokens) and the `|---|` separator, excluded from the old side; the per-row `|` cell framing is dropped by the cell split.
- **New section scaffolding** — the `### [node: <name>]` headings and the `**responsibility** —` / `**owns** —` / `**pins** —` labels, excluded by the reader; roughly 88 fixed scaffolding word tokens across 22 sections (the word `node` plus three field labels each), carrying no row content.

## Residuals (must all be empty)

- word-token residual (new minus old): empty
- punctuation residual (new minus old): empty

