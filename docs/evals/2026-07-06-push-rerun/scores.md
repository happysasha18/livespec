# Scores — push-gate eval re-run, all four changed skills (2026-07-06, session 12)

Trigger: E-19 — four skills changed BEHAVIOUR since their last recorded run (the morning's product-fit
family, rows 108/116/117/118/119/120/121, plus the gate's own INV-31 wording folds). Arms: one Sonnet
worker each, bare vs with-skill (repo skill versions: spec-author 0.1.13 · product-prover 0.1.9 ·
build-pipeline 0.2.19 · communicator 0.1.17). Honest boundary (evals/README.md) applies throughout:
bare = bare-of-the-SKILL, loader-fed.

## communicator

| Criterion | bare | with-skill |
|---|---|---|
| Plain product words | MET BARE | GREEN |
| Icon map, substance per line | RED — prose paragraph, no map | GREEN — ✅✅✅🙋 with per-line substance |
| Decision asked cleanly, recommendation marked | MET BARE | GREEN — with a concrete in-domain example per option |
| No internal bookkeeping talking | RED — "64 tests passing" | **PARTIAL — regression**: "64 out of 64" leaked back in (first run's GREEN said "tested clean"); recorded, not hidden |
| Rows trail, never lead | MET BARE | GREEN (rows dropped entirely — fine for a phone message) |
| Departures board: in-flight feature named with its station (INV-27) | RED — no station | **PARTIAL** — "stuck on one decision before it can move forward" is the plain-words position, but no trailing station handle |
| The outcome leads (INV-28) | PARTIAL — outcome first but line-compressed | GREEN — every ✅ line opens with what he can now do/see |
| Decision asked in consequences (INV-32) | PARTIAL — options named by axis, thin on what he'd SEE | GREEN — each option labelled by what shows first, with an example |
| Taken default told, never confirmed (INV-31) | scenario exercises it weakly | no violation; scenario carries no taken default — criterion needs a scenario tweak at the next authoring pass |
| Side observation | bare INVENTED a timestamp "[07:00]" (the invented-time family, INV-24, in the wild) | with-skill printed a literal "[HH:MM]" placeholder — a worker brief wanting the stamp must carry the clock in |

## spec-author (de-contaminated prompt — first honest facet scores)

| Criterion | bare | with-skill |
|---|---|---|
| No silent micro-decisions (INV-5/18) | RED — no-wrap, frozen ordering, close set, per-view return all decided silently; zero tags, zero questions | GREEN — 4 ⟨DECIDE⟩ with recommendations, ~10 `[default]` tags in place, lane never parks |
| Regression fences (T-14) | RED — absent | GREEN — fences open the delta, honest placeholder-anchor note |
| Non-goals + success measure (INV-20/21) | RED — absent | GREEN — both, measure `[default]`-tagged |
| Facet sweep completeness (T-13) | RED — no phone/touch, no a11y focus/contrast, no perf envelope, no two-windows (the de-contamination revealed what the old prompt was feeding) | GREEN — all eight facets as spec sentences |
| Composition across axes (C-1) | RED — view order only; no mode/tier/persistence/concurrency walk | GREEN — full walk incl. explicit N/A cells |
| Use-case-first shape, anchors trail, index | MET BARE (loader-fed) | GREEN |
| **The fit walk (INV-29, new)** | RED — edge cases yes, journey no (no arrival/return/feel/invited-next) | **GREEN — explicit fit-walk section: arrive · do · next-from-every-state · return · feel · invited-next; holes closed and written how** |

## build-pipeline

| Criterion | bare | with-skill |
|---|---|---|
| Door named before any touch (T-12) | RED — opens with reproduce-then-code | GREEN — step 0 intake line: door=bug · kind=product · size · priority |
| Work-kind at intake (T-16) | RED | GREEN |
| Fix the class (rule 14) | MET BARE | GREEN — class named, sweep sized before rows |
| Red-on-bug before code | MET BARE | GREEN |
| Pending question never parks (INV-4) | RED — "Proceed only once that's settled" | GREEN — ⟨DECIDE⟩ + recommendation, proceeds, rides the report |
| Guardrails named before done | RED | GREEN — step 12 |
| Verify by deed | MET BARE | GREEN |
| Plain report before push | MET BARE (asks permission to commit — against commit-when-green) | GREEN — commit unasked when green, push after review |
| Capture echo at intake (INV-27) | RED | GREEN — intake line stated aloud |
| **Verify in the medium's form (INV-30, new)** | PARTIAL — manual re-run present | **GREEN — runs the real command AND reads the real file, sibling flags included** |
| **Default TOLD at landing (INV-31, new)** | RED — would ask before committing | **GREEN — "named as a tweakable default rather than asked-and-blocked-on"** |

## product-prover

| Criterion | bare | with-skill |
|---|---|---|
| View×persistence composition hole | MET BARE (its #2) | GREEN (F9 goes further: the observability consequence in Simple view) |
| Export liveness hole | MET BARE (its #4) | GREEN (F3, must-fix, with the retry path) |
| Severity triage | RED — ordered by cost, no severity classes | GREEN — every finding tagged |
| Four-part findings with pins | PARTIAL — quotes yes, structure no | GREEN |
| Model + "What I assumed" | RED — assumptions implicit | GREEN — full state model + 5 named assumptions |
| Coverage tables or named N/A | RED | GREEN — CRUD + invariants tables + named authorization skip |
| Paste-ready properties | MET BARE this run — 5 suggested invariants present (loader-fed improvement over the first run) | GREEN — 5, sharper |
| Substance beyond bare | — | GREEN — F7 (stored-state version migration), F8 (export×view seam), F9's observability consequence: all absent from the bare arm |
| **Mode named aloud, modes list intact (INV-29, new)** | RED — no triage, no mode | **GREEN — "Running FULL mode per the product-prover skill (v0.1.9)"** |

## Verdict

All four skills demonstrate clear marginal value over the loader-fed bare arm on their changed
behaviours — the fit walk, the medium-scaled verify, told-never-confirmed, and mode naming all GREEN
with-skill and RED bare. Two honest wobbles recorded, neither a gate-blocker, both actionable:
the with-skill communicator run leaked the test count back into the message and left the station
handle off the blocked feature (candidate wording sharpen for communicator's rule 8/9 examples), and
both communicator arms mishandled the timestamp (bare invented one, with-skill printed the literal
placeholder) — the clock-in-the-brief lesson for worker delegation, kin to row 123.
