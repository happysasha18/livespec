# Prover check — the iterativity sentence (E-14 delta, SPEC v0.7.2; 2026-07-05, ~14:10)

**Scope:** CROSS-LINK check of one added fact — the architecture doc is iterative, never written
milestones ahead (row 58; born from tlvphoto's agent asking whether to architect several milestones
forward) — against its seams. **Whole-spec state for the push gate (M-6):** SPEC entered today's pushes
under two green records (`2026-07-05-lost-layers.md` full pass, `2026-07-05-architecture.md` ownership
walk over all 69 anchors); this delta adds one sentence to E-14's home section and no anchor. This
record + those two are the re-check for the pushed state; no unfolded rows carried from either.

## Seams checked

| Seam | Question | Verdict |
|---|---|---|
| S-0 (shipped vs target honest) | Does "never milestones ahead" contradict [target] nodes? | No — the sentence NAMES the only legal forward reference: a [target] node backed by a spec promise AND an owned queue row, pin empty. Exactly S-0's own rule, and exactly what F1 enforced this morning (rows 55–56). |
| INV-15 (no landing without node+row) | Can "a node earns existence when its landing arrives" starve a landing of its node? | No — E-14 already lets a landing CREATE or ASSIGN the node it needs; iterativity forbids nodes nobody's landing needs, not nodes the current landing does. |
| E-15 / coverage walk | Does a late-created node break the matrix? | No — the walk re-runs at every derivation (and mechanically in the suite); a new node gets its block when it gets its facts. |
| A-3 (adoption re-engineering) | Consistent with adoption? | Reinforces it — adoption pins nodes to the REAL code structure; it never invents future ones. |
| INV-5 (no silent micro-decisions) | Is the parallel fair? | Yes — a speculative node is unbacked structure, the structural twin of an unasked behaviour; prover already flags "node without spec backing", so the teeth exist today. |

## Findings

None must-fix. One note: the tlvphoto question is the proof the gap was real — a host agent could not
answer "how far ahead?" from the method; now build-pipeline step 3 answers it in one sentence
(NO — by the method, not by taste). Homes updated in the same landing: SPEC E-14 (v0.7.2),
ARCHITECTURE.template.md, build-pipeline SKILL.md 0.2.1 (installed copy synced).

**Verdict: GREEN for push.**
