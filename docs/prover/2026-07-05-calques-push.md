# Prover pass — no-calques rule delta, push gate for pack 0.5.3 ("Row 73 lands: no calques") (2026-07-05, session 7)

Mode: **CROSS-LINK** on the rule delta only. The M-6 push gate for pack version 0.5.3.

**Why not FULL.** SPEC.md is UNCHANGED since v0.11.1 (header reads `v0.11.1, 2026-07-05`), which passed a
FULL push-gate pass ~1h ago with zero must-fix (`2026-07-05-v11-push.md`, whole-spec sweep, all nine
lenses; nothing left owed to the queue). No spec change and no MINOR spec bump ⇒ no FULL spec re-prove is
owed (prover.cadence: FULL before every MINOR bump / CROSS-LINK on surface add; the host tightens to a
whole-spec re-check before every push, which v11-push already discharged and this delta does not disturb).
The delta since that push is **skill-text only**: base rule 2 gained the no-calques sentence; communicator
rule 6 gained its calque elaboration + the ❌/✅ example; the four working skills' base pin bumped to
v0.1.6; pack VERSION → 0.5.3. This pass proves the seams that delta touches.

**Verdict: ready-to-push, zero must-fix.** The no-calques rule states ONE rule in one normative home
(base rule 2) with communicator rule 6 pointing to it and elaborating its own domain — clean INV-13, no
drift. The settings ladder, the anchor convention, and every other skill compose without contradiction.

## Seam checks (the rule delta against what it composes with)

**Seam 1 — base rule 2 (normative) ↔ communicator rule 6 (elaboration), per INV-13.** Consistent, one
rule, correct split. Base rule 2 legislates it: "a term or metaphor coined in the docs language is never
loan-translated into chat — no calques: say what actually happens in natural chat-language words; the
original term may trail in parentheses like any anchor." Communicator rule 6 does NOT re-legislate — it
names the base ("Calques are the same bug across a language split (base rule 2)") and elaborates only its
own domain (HOW to speak: "restate the mechanism in natural chat-language words, the original may trail in
parentheses") plus the concrete ❌/✅ pair ("вердикт растяжки старше ярлыка" → "фиксированный чек-лист
решает, фича это или багфикс (tripwires, T-12)"). This is exactly the INV-13 pattern the base skill's
opening paragraph describes: base states THAT, communicator teaches HOW. No second full statement of the
rule. Green.

**Seam 2 — personal profile `language.no-calques` ↔ the package rule.** Same direction, no contradiction.
The profile line (`in Russian chat NEVER loan-translate English doc/pack terms or metaphors («растяжки»
for tripwires, «та же семья» for the same incident family, «посадка» for landing) — say it in natural
Russian or state the mechanism itself`, Alexander 2026-07-05) points the same way as base rule 2, only
narrower: it pins his chat language (Russian) and names the concrete calque terms to avoid. No-calques is
a universal always-on RULE (base rule 2), not a toggleable settings-ladder default — there is no
package-default row that the profile could contradict or invert; the profile line legitimately narrows
the universal rule to his concrete example set and reaffirms it. No divergence.

**Seam 3 — the calque sentence ↔ rule 2's own anchor convention.** No contradiction; the calque clause
RELIES on the convention. The calque clause governs chat, and rule 2's chat convention is "the anchor may
trail the sentence in parentheses." The calque sentence explicitly permits the original-language term to
"trail in parentheses like any anchor" — i.e. the original term is allowed in parens, exactly as an
anchor is. It never forbids the original term appearing; it forbids the LITERAL TRANSLATION carrying the
meaning. Consistent both faces (chat parens / doc square-brackets untouched). Green.

**Seam 4 — any other skill that speaks about language/wording.** Swept: `calque`/`loan-translat` appears
in exactly two homes — base rule 2 and communicator rule 6 — nowhere else (spec-author, build-pipeline,
product-prover carry only the shared-rules banner pointer "plain words, anchors trail" and their own
domain uses of "plain words," none restating the calque rule). No drift, no third home to keep in sync.

## Mechanical guard (senior-run, all pass)

- pack `VERSION` = **0.5.3** ✓
- All four working skills pin the base as **`live-spec-base` (v0.1.6)** (communicator, build-pipeline,
  product-prover, spec-author — grep confirmed) ✓; `live-spec-base` metadata version = 0.1.6 ✓
- The five installed copies at `~/.claude/skills/*/SKILL.md` are **byte-identical** to the repo copies
  (`cmp -s` clean for all five: live-spec-base, spec-author, product-prover, build-pipeline,
  communicator) ✓
- SPEC.md header = `v0.11.1` — UNCHANGED since the v11 FULL pass; anchor set untouched ✓

| # | Finding (one line) | Severity | Outcome |
|---|---|---|---|
| — | No must-fix, no should-clarify. The no-calques delta states one rule (base rule 2), elaborated once (communicator rule 6) with a plain pointer back — clean INV-13. Settings ladder, anchor convention, and all sibling skills compose without contradiction. | green | PENDING |

Nothing must-fix, nothing owed to the queue. No spec re-prove owed (SPEC unchanged, no MINOR bump). This
record ships with the 0.5.3 push.

Zero findings — nothing to fold; gate green, pushed same sitting.
