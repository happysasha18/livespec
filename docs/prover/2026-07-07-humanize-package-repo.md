# Prover cross-link — SPEC humanize batch: "The package repo: who may write, and two sessions at once" (2026-07-07, session 25)

Register rewrite of one scenario section (intro + four bold-lead paragraphs). Gates green: 8/8 tested
phrases re-matched section-scoped; bracket-code multiset identical to baseline (10 codes, each once:
[D-4], [E-11], [E-23], [INV-10], [INV-11], [INV-1], [M-4], [T-10], [T-20], [target]); full suite 175
green. Clean on first splice.

## Facts carried (all KEPT)
- INTRO [M-4]: live-spec eats its own cooking; pack repo push gates run mechanically on installed hooks
  (prover record, green suite, anchor ownership, matrix coverage, `guardrails/`); host-facing checks stay
  [target] with E-6; shared surface; two-parallel-sessions origin.
- BLOCK 1 [E-23]: keeps its skills fresh by name, not by habit; repo is the source [D-4], installed copies
  are mirrors; `scripts/sync-skills.sh` syncs the same session and reports every version change old → new;
  a hand-copy is the anti-pattern the tool retires.
- BLOCK 2 [INV-10]: only an assigned session writes the repo; every other session read-only, one exception
  (a new inbox wish file); the crisp "did the human ask ME" test; a host run's story lives in the HOST's
  journal.
- BLOCK 3 [E-11] + [INV-1] + [T-20] + [T-10]: the inbox is the parallel-safe door for wishes and feedback;
  one NEW file per item (`YYYY-MM-DD-<source>-<slug>.md`, `-2`/`-3` collision law base rule 18, a short
  session token on a slug race); never edits an existing file; outsider commits its one file inside the
  read-only exception; host-general, swept first, keeps "no wish is ever lost"; a live-spec session sweeps
  as its FIRST act and harvests each file into the home its route owns (wish → a queue row, feedback →
  routing law); harvest is one commit that lands the route and removes the file; interrupted harvest
  re-harvested exactly once.
- BLOCK 4 [INV-11]: re-check `git status` + HEAD before writing and before every commit; STOP + re-read on
  drift, or back off to the inbox; inbox new files benign; never push while another session is live;
  applies to live-spec and any shared host repo.

## Wording changes worth naming (meaning intact)
- The long inbox paragraph split into three shorter paragraphs (naming/collision, the outsider commit, the
  harvest sequence); compound sentences split throughout.
- The tested bold lead "keeps its skills fresh by name, not by habit" kept verbatim (a required phrase,
  not a newly-introduced scissors).
- "STOP … and only then proceed surgically — or back off" kept; no new dash-contrast added.

Verdict: **CLEAN.** Every fact and code carried; 8/8 tested phrases section-scoped; code multiset
identical; suite 175 green. No must-fix.
