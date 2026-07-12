<!-- Promoted from .live-spec/checkpoints/pending-audit-delegation-dedup.md (source, 2026-07-12) -->

# Pending audit — delegation/routing rule de-duplication

Auditor: Opus. Date: 2026-07-12. Status: PENDING owner review. No edits made anywhere; this file is the only write.

The owner flagged that the delegation/routing rules live in two homes and may have drifted into duplicates:

- **Home A — the pack** (method): `~/live-spec/skills/live-spec-base/SKILL.md` base rule 5 + the `worker.tiering` setting, whose normative home is the spec's routing law in `~/live-spec/PRODUCT_SPEC.md` (INV-69, D-2, ACT-2, ACT-3, T-19, INV-103, and the worker contract).
- **Home B — the personal cross-project playbook**: `~/.claude/playbook/PLAYBOOK.md` section "Delegation — I'm the lead, Sonnet is the junior" (lines 56-112), with a fragment in the pipeline section (line 414) and a shipped-design item in `PIPELINE_UPGRADE_ROADMAP.md` (lines 81-95). The playbook repo is READ-ONLY for this audit.

The pack's one-home law (base rule 4): each fact has ONE normative home; every other place points to it. Base rule 14 adds that a rule restated at a narrower scope — "a project's playbook copy, an installed skill" — goes stale the instant the broad rule changes.

---

## 1. Every rule statement, verbatim-anchored

### Home A — the pack (method + spec)

- A1. `SKILL.md:40-44` (base rule 5) — "Mechanical work goes to a junior; judgment stays senior." Tier ladder: "one-shot → haiku; multi-step mechanical → sonnet; judgment/design → senior." Junior pastes RAW output; raw output is evidence, prose is a lead; senior spot-checks by re-running. No SPEC anchor on this rule.
- A2. `SKILL.md:91` (base rule 13) — "rule 5's raw-output clause is this rule's delegation face." (pointer)
- A3. `SKILL.md:256` (settings, `worker.tiering`) — "router proposes the cheapest sufficient tier; senior may override, logged"; profile may fix a tier per size class (cites SPEC D-2).
- A4. `SKILL.md:191-202` (base rule 23) — the routing rule that broke mid-turn earned a live channel (every-prompt hook line + mechanical after-the-fact check, rows 253/254); the once-read files stay the normative homes.
- A5. `PRODUCT_SPEC.md:1383` (ACT-2) — the senior owns judgment; never routes down.
- A6. `PRODUCT_SPEC.md:1385-1389` — three tiers: no-decision one-shot on haiku; multi-step mechanical on sonnet; judgment on senior.
- A7. `PRODUCT_SPEC.md:1391,1403-1410` (INV-69) — the routing rule proposes the cheapest tier that can pass the brief; propose per unit, "never default it"; judgment → senior; one-shot → haiku; multi-step brief → sonnet; size class is only a coarse prior.
- A8. `PRODUCT_SPEC.md:1412-1416` (T-19) — the economy rung moves the threshold (full / lean / tight).
- A9. `PRODUCT_SPEC.md:1418-1420` (D-2) — proposal is advisory, senior overrides per wish, override logged: "proposed tier → chosen tier → why"; distinct from ACT-3's runtime escalation.
- A10. `PRODUCT_SPEC.md:1401` (ACT-3) — a failed-acceptance result escalates one tier (haiku → sonnet → senior), logged, never skips a rung, never retries silently.
- A11. `PRODUCT_SPEC.md:1393-1400` (worker contract) — worker inherits its session's write-ownership narrowed to briefed files; may name an isolated tree; same-session sibling writes are fence-benign; live setting lines ride into the brief; carries the clock; carries the problem-ledger duty.
- A12. `PRODUCT_SPEC.md:1429` (INV-69 success measure) — the first routed landing names proposal → choice → why for each delegated unit.
- A13. `PRODUCT_SPEC.md:1431` (INV-103) — the landed row's status cell carries its delegation accounting; a suite check reads it (missing line → red); binds forward from 2026-07-12.
- A14. `PRODUCT_SPEC.md:1433-1435+` — a worker's green gets a second pair of eyes; verify can go adversarial with a FRESH-context checker on a large delegated landing.

### Home B — the personal cross-project playbook (READ-ONLY)

- B1. `PLAYBOOK.md:56-59` — section title + "promoted to #2 on 2026-06-23"; "the always-on copy now lives in `~/.claude/CLAUDE.md`."
- B2. `PLAYBOOK.md:60-67` — Opus keeps the judgment, junior gets the grunt; delegate to `sonnet-worker` when ANY holds: "touches or reads more than three files for facts"; "a known script, suite, or pipeline runs longer than about 30 seconds"; "the output is a report, list, or dump rather than a decision"; "the exact edit strings or command line are already known."
- B3. `PLAYBOOK.md:68-73` — pick the cheapest model: one-shot no-decision → haiku; mechanical multi-step → sonnet; judgment/design → Opus; a single trivial command stays with the lead.
- B4. `PLAYBOOK.md:74-75` — several juniors can run in parallel as background agents.
- B5. `PLAYBOOK.md:76-78` — never delegate the hard part; "if briefing the worker means writing the answer myself, I just do it."
- B6. `PLAYBOOK.md:79-84` — raw output is evidence, prose is a lead; "I spot-check one delegated result per session by re-running it myself."
- B7. `PLAYBOOK.md:85-89` — long/background junior work writes to a persistent checkpoint file (done / in-progress / next) and resumes from it.
- B8. `PLAYBOOK.md:90-91` — "I report the savings each time I delegate."
- B9. `PLAYBOOK.md:92-109` — the standing junior task-list (default to junior, "I do not re-decide each time"): run a suite/script; translate; search many files; bulk edits/renames/formatting; scaffold matrix-derived tests; draft a CHANGELOG entry; regenerate a deterministic artifact; a whole-spec prover run stays senior. Tier discriminator: haiku for zero-decision, Sonnet the moment it correlates/filters/retries/touches a second source.
- B10. `PLAYBOOK.md:110-112` — each delegation carries a precise spec, a verify step, a "don't commit" line, a persistent output file with a checkpoint, and a "touch only file X" line.
- B11. `PLAYBOOK.md:414` — pipeline section: "`sonnet-worker` takes the grunt, high-volume, well-scoped work, while I stay on Opus for the judgment."
- B12. `PIPELINE_UPGRADE_ROADMAP.md:81-95` — "Model routing (smart agentness)": route each task to the cheapest sufficient model (haiku / sonnet / opus-fable); intake size classification doubles as the router; budget as a routing axis. (A roadmap item that INV-69 has since shipped.)

---

## 2. Overlap map

### DUPLICATES — same rule, stated in both homes (7 clusters)

| # | Playbook | Pack | The shared fact |
|---|---|---|---|
| Dup-1 | B3, B5, B11 | A1, A5 (ACT-2), A7 | judgment/design stays with the senior; grunt goes to a worker |
| Dup-2 | B3, B9 | A1, A6, A7 | the three-tier ladder: one-shot → haiku, multi-step mechanical → sonnet, judgment → senior |
| Dup-3 | B6 | A1, A2 | raw output is the evidence; the worker's prose is only a lead |
| Dup-4 | B3 (cheapest model) | A3 (`worker.tiering`), A7 (INV-69) | propose the cheapest sufficient tier |
| Dup-5 | B7 | A11, base rule 6 | delegated/long work keeps a persistent checkpoint and resumes from it |
| Dup-6 | B10 | A11 (worker contract) | each brief carries spec + verify + don't-commit + output file + touch-only-X |
| Dup-7 | B4 | base rule 7, T-18 | several workers run in parallel |

### DIVERGENCES — two homes stating DIFFERENT bars (the dangerous ones)

- **DIV-1 — delegation trigger.** Playbook B2 fires on hard proxies: ">3 files for facts", ">~30 seconds", "report not a decision", "edit strings known". Pack A7 (INV-69) routes on judgment-vs-mechanical only, with size an explicit "coarse prior." They can disagree: a 4-file *judgment* read trips the playbook's ">3 files" trigger (delegate) while INV-69 keeps it senior. The playbook uses a proxy the pack deliberately demoted.
- **DIV-2 — default vs propose.** Playbook B9: standing tasks "default to the junior... I do not re-decide each time." Pack A7 (INV-69): "propose its tier (never default it)" per unit of work. Direct contradiction of the same act.
- **DIV-3 — verification bar.** Playbook B6: "spot-check one delegated result per session." Pack A14 (INV-103 area): worker green is never evidence; a large delegated landing gets a FRESH-context adversarial checker. The playbook's one-per-session is a weaker bar than the pack's structural second-eyes.

### SINGLE-HOME — exists in only one place

- Pack-only: A8 economy rung shifts the threshold (T-19); A9 override log line proposal→choice→why (D-2); A10 ACT-3 escalation ladder; A11 the full worker contract (write-ownership, isolated tree, fence-benign siblings, clock, ledger); A12/A13 INV-69 success measure + INV-103 landed-row accounting with a red-on-miss suite check; A14 adversarial fresh checker; A4 base rule 23's hook + suite live channel.
- Playbook-only: B8 "report savings each delegation" (the pack records accounting on the landed row per INV-103, not per delegation); B9 the concrete standing task-list (translate / search / scaffold / CHANGELOG / regenerate); B2's numeric triggers; B12 the roadmap model-routing item, now shipped as INV-69.

---

## 3. Recommendation per overlap

**Normative home = the pack (base rule 5 → SPEC INV-69 family).** It carries the tests and the convergence lock the playbook does not: INV-103's red-on-miss suite check, base rule 23's every-prompt hook + after-the-fact check (rows 253/254), and the T-19 rung. The playbook is a narrower personal scope; base rule 14 already declares a playbook copy stale the instant the broad rule moves. Direction: collapse Home B into a pointer, delete the diverging bars, and keep only what is genuinely personal.

Per overlap:

- Dup-1..Dup-7: the playbook lines become a single pointer — "Delegation runs by the pack: base rule 5 and the spec's routing law INV-69 (tier ladder, propose-per-unit, override logging, escalation, landed-row accounting)." No second full statement.
- DIV-1: DELETE the playbook's numeric triggers (>3 files / >30s / known-strings). Adopt INV-69's judgment-vs-mechanical wording. The proxies are exactly the kind INV-69 demoted.
- DIV-2: DELETE "I do not re-decide each time." Adopt INV-69's "propose the tier per unit, never default it." A standing hint-list may stay as a *prior*, never as a skip of the proposal.
- DIV-3: REPLACE "spot-check one per session" with a pointer to the pack's verification bar (worker green is a lead; adversarial fresh checker on large landings, INV-103).
- B8: REPLACE "report savings each delegation" with a pointer to INV-103's landed-row accounting.
- B12 (roadmap): mark the model-routing item SHIPPED and point it at INV-69, so the roadmap stops reading as open design.
- Intra-pack tidy: base rule 5 (A1) states the routing rule but carries NO spec anchor, while the `worker.tiering` setting cites D-2. Add an `[INV-69]` anchor to base rule 5 so the pointer chain is explicit. (Pack-internal; not a cross-home divergence.)

### OWNER-DECIDES

- **OD-1** — Is delegation's normative home the pack (method, INV-69) or the personal playbook (its self-declared cardinal-adjacent principle #2)? Both currently claim to be the home. One sentence for the owner: *do you want the pack to own the delegation mechanism outright and the playbook to hold only a pointer plus your personal "why it's #2" note, or do you want the playbook to stay a full parallel statement for non-live-spec projects?*
- **OD-2** — Should the playbook's concrete standing junior task-list (B9: translate / search / scaffold / CHANGELOG / regenerate) migrate into the pack as elaboration, or stay in the playbook as personal detail pointing to INV-69? One sentence: *does the task-list belong to the method (all live-spec projects) or to your personal cross-project habits?*
