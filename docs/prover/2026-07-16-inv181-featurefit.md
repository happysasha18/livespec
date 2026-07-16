# Prover record — mirror release history, feature intake (2026-07-16, FEATURE-FIT)

Prover skill version: 2.1.1 (pack version, per INV-178). Mode: FEATURE-FIT on one delta (row 360, INV-181).

## The delta
One spec paragraph beside the attribution clause [INV-96]: every standalone mirror's README carries a generated release-history section (version · date · one story line per shipped version), harvested from the pack's git history by sync-mirrors.sh at every sync; JOURNAL.md stays the full story's home; README surface is the `[default]` pick, movable to a generated CHANGELOG on the owner's word. Code: `compute_release_history()` + `stamp_release_history()` + a `--print-release-history` verify mode; M-339 + `tests/test_mirror_release_history.py` (red-proven: print mode absent at HEAD).

## Fit walk
- **Arrival** — the section is written by the same sync that already rebuilds a mirror; no new entry path. Backed by the clause's "writes them fresh at every sync". HOLDS.
- **Return visit / accumulation** — rsync rebuilds the mirror README from the pack copy each sync, so the appended section never stacks; same mechanism the attribution line already rides. HOLDS.
- **Contradiction check** — INV-96 stamps README and SKILL.md; the history goes to README alone, stated as a decided boundary in M-339 (SKILL.md stays the machine surface). No clause conflicts. HOLDS.
- **Second-sibling question** — YES: this is the second sync-generated stamp on mirrors (the attribution line is the first). The two diverge on the SKILL.md surface, with the reason decided; the scoped design review this yes draws is covered by the full design review running at the 2.2.0 gate (SPEC INV-169, INV-141). NOTED.
- **Quantifier re-verify** — INV-96's "stamps the line onto each mirror's README.md and SKILL.md" stays true of the LINE; the publish node's anchor list gained INV-181; the guardrails README's gate enumeration is untouched (no new gate). HOLDS.
- **Edge conditions** — a repo with no version-shaped commits prints the header with zero lines (legal, empty history); a follow-up commit repeating a version number loses to the oldest (pinned by test: "prover record" absent, one 2.0.0 line). HOLDS.

## Disposition
| Finding | Kind | Disposition |
|---|---|---|
| row 360 (mirror release history) | feature | landed — INV-181, M-339, sync script + print mode, red-proven tests |

Verdict: the delta FITS; the one open rider is the `[default]` surface pick (README section), his word may move it to a CHANGELOG file.
