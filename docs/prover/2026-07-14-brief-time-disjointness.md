# Prover record — 2026-07-14 — brief-time disjoint-write-set check before a second concurrent writer (row 314)

**Prover skill version:** product-prover **v1.1.1** (the lens set current at HEAD `84db0fc`; this pass ran the full adversarial-audit discipline of INV-46, not a phase-by-phase FULL review, since the delta is a single clause).

**Change under review:** a brief-time disjoint-write-set imperative added to the worker contract — "before spawning a second concurrent writer, the senior confirms the two briefs' write-sets are disjoint, or gives the later worker an isolated tree [INV-105]; because the fence stays silent between same-session siblings, this disjointness is settled when the briefs are written, ahead of either worker's first write." Homed in `PRODUCT_SPEC.md` (:1449, the fence-benign bullet of the worker contract), `skills/build-pipeline/SKILL.md` (worker contract), `skills/live-spec-base/SKILL.md` (rule 7). Extends **ACT-3 / INV-11**, no new invariant. Red-first: `tests/test_brief_time_disjointness.py`.

**Review mode:** independent fresh-eyes adversarial audit (SPEC INV-46) — did NOT author the clause. Opening hypothesis: "the clause contradicts the fence, or deserves its own invariant, or is a duplicate." I tried to confirm each of the five attacks the brief named.

**Verdict: CLEAR TO LAND — zero defects.** The clause strengthens the fence, extends ACT-3/INV-11 correctly rather than minting INV-143, is not a duplicate, names both branches, scopes "writer" against readers, and carries no contrast frame. Two minor recommendations below, both non-blocking (queue for a taste call per INV-140).

## Adversarial results

**1 — Contradiction with the fence? NO — it strengthens.** The concurrent-edit fence [INV-11] is reactive and deliberately silent between same-session siblings (PRODUCT_SPEC.md:1449). That silence is a real gap: the reactive net cannot catch two of the senior's own briefed workers colliding on a shared file (the tlvphotos incident). The clause fills exactly that gap with an upstream, proactive check, and its overlap branch routes to INV-105's own remedy (worktree isolation on overlap). It leaves the fence's silence unchanged, adds no reactive burden the fence disclaims, and cites the courtesy it depends on. No conflict with INV-11, INV-105, or the fence-benign courtesy.

**2 — Extend vs new invariant? Extending ACT-3/INV-11 is correct; INV-143 is not warranted.** The clause introduces no new state, entity, or safety property. The safety property "no two concurrent writers collide on a shared file" already exists as the union of INV-11 (foreign sessions, reactive) and INV-105 (overlapping lanes isolate). The clause assigns that property an actor (the senior) and a timing (brief-time), and generalizes INV-105's lane-overlap default to any second concurrent sibling worker — the timing is forced to brief-time precisely because the fence is silent later. That is an operational timing on existing rules, not a new obligation with its own law. The base-rulebook rule 7 already carries the summary line, so the extend leaves no missing summary home.

**3 — Redundancy? Not a strict duplicate.** INV-105 states the reactive remedy for lanes ("worktree isolation is the default when two concurrent lanes' write-sets overlap"). The new clause adds the proactive disjointness CHECK for any second concurrent writer plus the brief-time rationale — substance INV-105 does not carry. The three homes (spec body + build-pipeline + live-spec-base) are the pack's one-home-in-spec-plus-pointers convention, not duplication.

**4 — Completeness of the clause (dogfood INV-138). Two branches, exhaustive; "writer" well-scoped; one minor N>2 gap.** The must-overlap case is named (→ isolated tree). There is no genuine "unclear" third branch: ACT-3 (the bullet directly above, :1447) makes every write-set the brief's explicit finite file list, so disjointness of two explicit sets is always decidable at brief-time — the two branches (disjoint → proceed, overlap → isolate) are exhaustive over the decidable space, and that decidability is exactly why brief-time works. "Second concurrent **writer**" correctly excludes readers (ACT-3: "outside those files it reads, and never writes"). The one gap: the clause reads pairwise ("the two briefs"), but up to three lanes may roll (T-18), and the pairwise-against-every-already-running-writer iteration is left implicit → **R1**.

**5 — Wording. Plain, no scissors, codes conventional; one minor term drift.** Plain operational verbs; no "X — not Y" / "X, not Y" contrast frame in any added sentence (global ban clear). Codes: inline `[INV-105]` as the remedy cite plus the bullet's trailing `[INV-11, ACT-3]` home anchor — pack-conventional (inline cites to a specific law are used throughout the spec). `spec-style-lint.py` shows no hit on the changed lines (1445–1452); the 13 file errors are all pre-existing caps-shout in the formal-index rows (line 1917+). One drift: the isolated-copy concept is named three ways across the homes → **R3**.

## Test

Red-first honored (the file is new to this commit). `tests/test_brief_time_disjointness.py` — 3/3 green at HEAD. String level, correct for a doc-law; a single punctuation-identical needle (`"before spawning a second concurrent writer, the senior confirms the two briefs' write-sets are disjoint"`) matches all three homes verbatim (verified), so the traceability across homes is itself asserted. Appropriate level and coverage.

## Findings

| # | Finding | Kind · Severity | Disposition |
|---|---|---|---|
| R1 | The clause reads pairwise ("before spawning **a second** concurrent writer … **the two briefs'** write-sets are disjoint"), but T-18 permits up to three lanes rolling. When the third writer is spawned, the text literally describes only one pair; the intended rule is "disjoint from **every already-running** writer's brief." A pedantic senior could check writer 3 against writer 2 alone and miss a 3-vs-1 overlap. A competent senior reads it right, so it does not block. | recommendation · worth-considering (abstraction) | **Queued (taste call).** Optional: reword to "disjoint from every already-briefed concurrent writer's write-set" so the pairwise rule visibly iterates to N. |
| R3 | The isolated-copy concept is named three ways across the homes touched: "isolated **tree**" (PRODUCT_SPEC.md:1449 new clause), "isolated **worktree**" (build-pipeline), "isolated **copy of the tree**" (INV-105 row and PRODUCT_SPEC.md:1448). Mild one-surface-one-name drift; all three unambiguously mean git worktree isolation. | recommendation · worth-considering (consistency) | **Queued (taste call).** Optional: pick one surface form (spec already leans "isolated copy of the tree") and use it in the new clause too. |

**Considered and cleared (no finding):** (a) the Formal-index rows for ACT-3/INV-11/INV-105 do not summarize the new obligation — but INV-11's row is likewise terse and does not summarize the pre-existing fence-benign courtesy either, so a body elaboration under a terse index anchor is the pack's established convention, and rule 7 of the base rulebook carries the summary regardless; (b) an "unclear disjointness" third branch — foreclosed by ACT-3 making every write-set an explicit briefed file list.

**Register / language delta:** `spec-style-lint.py` — 13 errors / 114 warnings on the file, zero on the changed lines (all pre-existing formal-index caps-shout). No contrast-frame construction in any added sentence.

**Open ⟨DECIDE⟩ touched by this change:** none.

**Suite:** `tests/test_brief_time_disjointness.py` 3/3 green at HEAD `84db0fc`.

**Folded 2026-07-14 (outcome):** R1 and R3 both folded into the row-314 material on the human's word — R1 reworded to the N-ary form ("before spawning another concurrent writer, the senior confirms its brief's write-set is disjoint from every already-running writer's brief") across all three homes, and R3 unified the new clause's isolated-copy wording to "isolated worktree" in all three homes (INV-105's own text untouched). Test needle updated to the new stable substring; full suite green, spec-style-lint 0-new.
