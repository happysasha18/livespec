# Template audit + whole-SPEC consistency scan (2026-07-07, session 25)

## SPEC template — audited, already in the register (no rewrite)
`templates/SPEC.template.md` (83 lines) is instructional authoring prose. Checked against the 14-rule
register: scenarios lead, codes trail as anchors, a "How to read" note opens it, the Formal index closes it.
No scissors "X — not Y", no invented mechanism names, no Cyrillic. Its one tested literal ("Founding
answers (B-2)") is present. It already models the genre D1 asks every new spec to be born in. **Outcome:
no change needed** — a rewrite would be churn on clean guidance prose.

## Whole-SPEC.md consistency scan (all 18 sections now humanized)
- `— not ` occurrences (3): "version comparison — not this time" (L199), "no per-feature history timeline
  — not this time" (L313), "SUBSTANTIVE — not a stub" (L572). All three are non-goal LABELS or a
  definitional gloss, not the banned "define the point by negating an alternative" scissors. CLEAN.
- Stale prototype cross-reference: NONE (fixed in wish-walk chunk 6).

## ONE real finding — flagged for Alexander's decision (NOT auto-edited)
Section "Asking what the product does (the feature map on demand)" (authored an earlier session, before the
strict register enforcement) still carries, in its bold lead (SPEC L309):
  1. a Cyrillic trigger phrase: «покажи все фичи»
  2. a scissors construction: "transparency is a command, not archaeology"

Why this is HIS call, not an autonomous loop edit:
- The scissors phrase is a TESTED literal (`tests/test_traceability.py:1877`) and is ECHOED in the
  communicator skill (SKILL.md L277). De-scissoring it is a coordinated 3-home change (SPEC prose + the
  needle + the skill echo), and the replacement wording is a taste call.
- «покажи все фичи» is his own voiced trigger phrase, also embedded in communicator's DESCRIPTION (skill
  metadata that affects triggering, SKILL.md L3/L25/L264). Whether to English it in the SPEC while keeping
  it as his trigger example, or keep it verbatim as a real example user utterance, is his policy call.

Proposed options to put to him (when back):
- (a) De-scissor + keep the Russian as an example utterance: reword to e.g. "transparency is a command: one
  word hands you the whole map" (updating the SPEC line, the tested needle, and the communicator echo in one
  commit); keep «покажи все фичи» as the illustrative trigger.
- (b) Full English-gate: also render «покажи все фичи» as "show all features" in the SPEC prose (leaving the
  skill's trigger metadata as-is, since it lists real user phrases).
- (c) Leave as-is: he confirms this pre-ban copy is deliberately kept.

Everything else in SPEC.md reads as one voice after the sweep.
