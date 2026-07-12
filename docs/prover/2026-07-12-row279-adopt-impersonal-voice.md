# Prover record — row 279: live-spec adopts the impersonal voice + wires the shipped-language gate

Date: 2026-07-12 ~21:20 · reviewer: build-worker (senior, own context) · mode: CROSS-LINK on the
changed clauses (INV-118, INV-120) plus their matrix rows, with a fresh-context adversarial audit
appended (INV-46, high-stakes: surface-sized + a method/invariant meaning change).

## Scope of the change

- PRODUCT_SPEC.md INV-118 clause + index row: the pack's self-exemption is retired; the clause now
  states the pack adopts the impersonal voice for its own shipped docs (dated 2026-07-12) and names the
  diaries (JOURNAL, NEXT_STEPS, ROADMAP, MIGRATION) as the home for candid attribution.
- PRODUCT_SPEC.md INV-120 index row: "not yet wired" → wired into the pack's own pre-push (gate i) and CI.
- TEST_MATRIX.md M-258 (INV-118), M-260 (INV-120): the same de-exemption / wired update; M-260 gains the
  two new wiring tests.
- guardrails/pre-push + .github/workflows/gates.yml: gate i runs check-shipped-language.sh.
- scripts/check-shipped-language.py: the gate's own machinery and prototype/ excluded from the scan.
- scripts/shipped-language-allowlist.json: user-language data files + one authorship-byline name_waiver.

## Findings

| # | Finding | Severity | Disposition |
|---|---|---|---|
| 1 | Does any shipped doc still assert the retired exemption? | must-fix if present | FOLDED — swept: M-258 and M-260 updated; the only remaining "pending the owner's decision" hits are NEXT_STEPS.md (orchestrator-owned diary, excluded) and dated docs/prover history (correct as history). |
| 2 | Does the gate reach zero on the swept tree without distorting any clause's meaning? | blocking | CLEAN — offences:0; every rewrite kept the rule's date and load-bearing reason, dropping only the personal name (INV-118's own recipe). No meaning changed to satisfy the machine. |
| 3 | Is the exclusion of the detector + allowlist + prototype/ backed, not a convenience hole? | should-clarify | CLEAR — the detector/allowlist are the gate's own machinery (scanning a detector against its own patterns is a false positive); prototype/ is a fenced non-product sketch (INV-17) that a prod allowlist may not reference (the prototype-fence gate). Each exclusion is documented in the detector docstring. |
| 4 | Do the authorship bylines belong under a carve-out or should they be rewritten? | should-clarify | CLEAR — "© Alexander Abramovich" is a copyright/authorship byline, exactly INV-120's named authorship-byline carve-out; a dated name_waivers entry spares it, not a rewrite. |
| 5 | Is the wiring red-first proven, and does it block on a new offence? | blocking | CLEAN — three wiring tests red before wiring, green after; a live seeded attribution reddened the wired gate (OVERVIEW.md:96), reverting greened it. |
| 6 | Cross-section: INV-118 clause ↔ INV-120 machine ↔ the diaries' scope — consistent? | must-fix if not | FOLDED — the INV-118 clause names ROADMAP/MIGRATION as diary homes; the machine's EXCLUDE set matches (JOURNAL, ROADMAP, NEXT_STEPS, MIGRATION), so the voice clause and the machine agree on what is a diary. |

0 open must-fix. The one ⟨DECIDE⟩-class question (adopt vs exempt) was the owner's, already answered ADOPT
(row 279). No new ⟨DECIDE⟩ opened.

## Adversarial audit (INV-46)

A fresh-context checker was briefed on the INV-118/INV-120 sentences the landing claims and the artifact
paths (primary sources only), opening hypothesis "tasks completed, goal missed". Its verdict rides the
landing report.
