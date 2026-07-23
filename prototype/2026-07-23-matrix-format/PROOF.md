# Content-preservation proof — row 477 matrix conversion

_This proof covers the mechanical conversion. Run it at conversion time, BEFORE the row-477 close flips M-448/M-449/M-450 from todo to built (an intended, separate delta that repoints their owning-test cells to the now-existing tests); re-running after that flip is expected to show those three rows as a residual and is not a conversion defect._

**Verdict: PASS — every token difference is a declared delta**

Compared `git show HEAD:TEST_MATRIX.md` (old) against the converted `TEST_MATRIX.md` (new), over the inventory + matrix-rows region, word-token multiset and punctuation multiset, modulo the named deltas below. Data rows counted: 449 (built 411 · todo 38 · retired 0).

## Named deltas (excluded regions)

- **Preamble rewritten** — excluded from both sides. Old preamble 525 word tokens; new preamble 353 word tokens.
- **`## Coverage validation` section retired** — excluded from the old side; 230 word tokens removed with it.
- **Generated `## Reference` section** — excluded from the new side; 896 word tokens (built by scripts/build-matrix-reference.py, not compared).
- **Node-block table headers and separators reshaped** — excluded from both sides by structure (a separator, or a header row whose first cell is `ID` or `Artifact`).

## Named deltas (reconciled in the compared region)

- **Status lowercased** (word): removed {'BUILT': 411, 'TODO': 38, 'RETIRED': 0}; added {'built': 411, 'todo': 38, 'retired': 0}.
- **Caps-emphasis sweep** (word): every leftover all-caps emphasis word in the Fact cells lowercased (one proper noun, ENGLISH -> English, aside; code anchors, acronyms, file names, and id-prefixes excepted) — 192 unique tokens, 346 occurrences each side; full removed/added map is `CAPS_SWEEP_REMOVED`/`CAPS_SWEEP_ADDED` in this script.
- **Status italicised** (punctuation): added `*` × 898 (two per row).
- **Spec-ref moved into the fact sentence, wrapped in one bracket** (punctuation): added `[` × 449 and `]` × 449; the anchor word tokens are unchanged by the move (position move) — proven by the empty word residual below.
- **Row narrowed six cells to five** (punctuation): removed `|` × 449 (one per row).

## Residuals (must all be empty)

- word tokens removed beyond the named deltas: empty
- word tokens added beyond the named deltas: empty
- punctuation removed beyond the named deltas: empty
- punctuation added beyond the named deltas: empty
- named word-removal not found in the diff: empty
- named word-addition not found in the diff: empty
- named punctuation-removal not found in the diff: empty
- named punctuation-addition not found in the diff: empty

