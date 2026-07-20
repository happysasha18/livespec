# Prover + design-review + adversarial-audit record — v3.1.0, conduct-audit stories 2-3 (INV-242, INV-243)

Covers the MINOR-gate re-check for the landing that closes the conduct-audit movement: the
landing-refreshed-map gate (INV-242) and the config-health skill-copy arm (INV-243). Three fresh-context
passes ran concurrently over the proven spec, the architecture, and the two implementations. Clean
context: the orchestrator authored the law text and briefed the workers; each pass ran in a separate
fresh seat that did not author the change [INV-237, INV-46]. Guards both PRODUCT_SPEC.md and
ARCHITECTURE.md for the freshness rule [INV-116, M-6].

## Pass 1 — product-prover, FULL structural + cross-link

Verdict: PROCEED, nothing blocking. Both new laws name a net that exists and does what the clause claims;
the citation reconciles resolve (INV-238 → INV-241, INV-180 → INV-243); the regression fences hold (the
register judge INV-203, the config-health hook arm INV-175 and perms arm INV-216 untouched; neither new
gate calls a model, so the suite and push gate stay deterministic); the `landed` token matches the real
ROADMAP status vocabulary.

| # | Finding | Disposition |
|---|---|---|
| P1 | The named fix `sync-skills.sh` re-copied only on a SKILL.md version/mtime change, so a drift confined to a non-SKILL.md file reds the gate while re-running the fix skipped it as "unchanged" — a red with no working escape ("trains the guarded to route around it"). | FOLDED — `sync-skills.sh` now skips only when `diff -rq` shows the installed tree byte-identical to source, the same whole-tree compare the gate reds on. |
| P2 | INV-238's prose names the bucket-1 conduct judge descriptively with no `[INV-241]` anchor, while its Formal-index row carries it. | FOLDED — `[INV-241]` added to the prose clause at PRODUCT_SPEC.md. |
| P3 | The `guardrails/check-landing-next-steps.py` pin carried a `[target]` tag grouping it with genuinely-deferred checks, but the file exists and its suite test runs green. | FOLDED — `[target]` dropped from the live pin. |
| P4 | The real-env config-health suite test now runs the skill arm against the developer's real HOME, so a drifted local install reds the suite. | NO CHANGE — the same self-healing personal-layer property the hook and perms arms already carry by design; the atomicity claim is complete. |
| — | A ROADMAP row born already `landed` (added with no removed counterpart) counts as a landing. | NO CHANGE — the docstring is explicit and the behaviour is correct (a born-landed row still owes a forward-map refresh). |

## Pass 2 — design review (two same-kind groups)

Group A — the "suite-riding, no-push-letter" checks (far-tier, node-growth, listener-tripwire, transport-router, landing-next-steps).
Group B — the arms of `check-config-health.sh` (hook-diff, session-hooks, perms, the new skill-copy arm).

| # | Finding | Disposition |
|---|---|---|
| D1 | Group A: `check-landing-next-steps.py` declared it rides the suite for the reason its chat-surface siblings use ("no committed file to scan"), which is false for a commit-range check; the consequence was that its law was enforced nowhere on the real tree (fixtures only), where every enforcing sibling has a live-tree test. | FOLDED — the docstring and spec now state the true reason (the push-gate letters are exhausted, so it rides gate b, which still blocks the push), and a live-tree test (`test_real_repo_range_refreshes_next_steps`) now runs the check over the repo's own commit range so the law is enforced in-suite against real commits. |
| D2 | Group B: `diff -rq` on directories holds a shipped skill byte-pristine, so an extra file dropped inside a shipped skill's installed dir reds as drift — stricter than the flat-file hook arm, which the arm's comment over-claimed as "same asymmetry". | FOLDED — the comment and the spec sentence now state precisely that a whole personal-layer skill is left alone at the top level while a shipped skill is held byte-pristine, the stricter and intended contract for a directory unit. Behaviour unchanged. |

## Pass 3 — adversarial audit (built throwaway repos, ran each checker)

Opening hypothesis "green but hollow" REJECTED — every real-shaped drift reds, every false-positive probe stays green. INV-243 also caught 10 stale installed skills on the live machine at first run (re-synced).

| # | Finding | Disposition |
|---|---|---|
| A1 | INV-242 column-shift: `parse_row_cells` read the status at a fixed cell index, so an escaped (`\|`) or raw pipe in a wish cell shifted the status column and hid a landing (no live exposure today — 0 escaped pipes, all rows 5-column). | FOLDED — the parser splits on unescaped pipes only (`CELL_SPLIT_RE`), red-first proven against the real ROADMAP vocabulary; a bold-only detection rule was rejected because 27 real landed rows carry the token unbolded. Test `test_reds_landing_with_escaped_pipe_in_wish` added. |
| A2 | INV-243 misses an executable-bit-only drift (`diff -rq` compares content, not mode). | QUEUED far — ROADMAP 435; a robustness nit with no live exposure (skills load as markdown + referenced files, the installer preserves mode). |
| A3 | INV-242 empty-range blind spot (nothing checked when the range is empty). | NO CHANGE — documented "no range" behaviour, not reachable in normal flow (a fresh landing commit is always ahead of origin/main). |

## Composition / cross-cut

The cross-cut counter flags the build-pipeline ↔ guardrails pair at the threshold (3) — a signal, not a block; the two gates clearly belong in guardrails, boundary judged healthy. One known duplication recorded, unfolded: the commit-range base ladder now lives in three files (two shell, one Python), so no shared helper extracts across languages — the first Python instance, a compaction row on its second occurrence (base rule 19).

Suite 1682 green after all folds; freeze re-taken; VERSION + 10 skills + plugin.json stamped 3.1.0.
