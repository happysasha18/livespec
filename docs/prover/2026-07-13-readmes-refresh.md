# Prover record — refresh the live-spec and product-prover READMEs

Date: 2026-07-13 · reviewer: orchestrator (senior, own context) · mode: feature-fit on a docs replacement
(the owner authored new READMEs; this lands them as the pack's copies).

## Scope of the change

- `README.md`: replaced with the owner's rewritten live-spec README (117 → 182 lines). Same product, fuller
  voice — install steps, the executable-gates claim, the "what it cannot do" boundary, prior-art credits,
  known issues, the skills table.
- `skills/product-prover/README.md`: replaced with the owner's rewritten product-prover README (the mirror
  source). The mirror banner + "made with live-spec <VERSION>" line are refreshed by scripts/sync-mirrors.sh.

## Findings

| # | Finding | Severity | Disposition |
|---|---|---|---|
| 1 | Do the new READMEs carry a name the shipped-language gate flags? | blocking | CLEAN — only the "© Alexander Abramovich" byline, already spared by the `*README.md` name_waiver (INV-120). Gate reads 0 offences. |
| 2 | Are the factual claims current? | should-clarify | Superpowers "quarter-million stars" VERIFIED (251.3k, obra/superpowers). Skill count (eight) and shared-rule count (twenty-four) match the live pack. The "62 style-lint findings / 11 redundancy candidates" line is the owner's curated debt count; the raw linter currently reports 115 warnings+errors — a different metric, left as the owner's editorial number, flagged to the owner. |
| 3 | Does the product-prover source keep the read-only-mirror contract? | should-clarify | CLEAR — the source carries the mirror note; sync-mirrors.sh stamps the banner and the version line from VERSION, so the mirror stays honest and the version never goes stale by hand. |

0 open must-fix. No new ⟨DECIDE⟩ opened.
