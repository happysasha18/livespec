<!-- Promoted from .live-spec/checkpoints/pending-audit-once-read-rules.md (source, 2026-07-12) -->

# Pending audit — the once-read-rules walk (INV-108's first sweep)

Auditor: Opus. Repo HEAD 93cf950, tree clean. Stamp 2026-07-12 ~03:22.
Scope of this checkpoint: ONE audit item toward the 1.1.0 (MINOR) gate — the once-read-rules
walk that INV-108 names as its own first sweep. Read-only audit; this is the only file written.

## What the law's walk is (as stated)

INV-108 (`PRODUCT_SPEC.md:1506`, matrix row `PRODUCT_SPEC.md:1785`, base rule 23
`skills/live-spec-base/SKILL.md:191`, roadmap row 256 `ROADMAP.md:154`, test M-246
`TEST_MATRIX.md:147`): a standing behavioural rule keeps its normative home in a once-read file —
the loader, a profile, a skill's text. When such a rule breaks mid-turn a **second** time despite
that home, it earns a **live channel** that same moment: either an **every-prompt hook line** that
reminds at the decision point, or a **mechanical after-the-fact check** that turns the suite red.
The pick is recorded where the rule lives. The clause's last sentence: "The 1.1.0 audit's once-read
walk is this law's first sweep."

So the sweep = walk the once-read behavioural rules, and flag any rule that has broken mid-turn
**twice** yet carries **no live channel**. INV-108 is explicitly "kin of rule 19's
second-occurrence law," so its break-record is the same one rule 19 keeps: the problem ledger
`.live-spec/PROBLEMS.md` (E-24, INV-23). A rule with zero recorded mid-turn breaks passes trivially;
a rule with two recorded breaks must show its channel. A finding = a twice-broken once-read
behavioural rule with no hook line and no suite-red check.

## The input the walk needs, and where it lives

The walk needs a record of which once-read behavioural rules broke mid-turn, and how many times.
The authoritative record per rule 19 / INV-23 is `.live-spec/PROBLEMS.md`. It exists and is
current (last append this session, 2026-07-12 ~00:22–01:25). One gap in the input, named not
improvised: the ledger is **not the single home** for every behavioural-rule break. The routing /
delegation rule — INV-108's own worked proof — broke mid-turn twice but its breaks are recorded in
the ROADMAP (rows 253/254/256) and JOURNAL, **not** in PROBLEMS.md. So the break-record for
behavioural rules is split across the ledger and the roadmap. This does not change any verdict below
(a rule that already carries a channel is never a finding, wherever its break is logged), but it
means a future run of this walk must read both the ledger and the roadmap's channel-landing rows,
not the ledger alone. Candidate follow-up: route behavioural-rule breaks to the ledger too, so one
home holds them (one-home law, INV-11).

## Per-item findings (the active ledger rows + the worked-proof rule)

| # | Once-read behavioural rule | Mid-turn breaks | Live channel? | Verdict |
|---|---|---|---|---|
| 1 | Separators are `---`, never bare `===` (workshop convention) | 4 (`PROBLEMS.md:11`) | YES — PreToolUse hook `block-triple-equals.sh`, proven by deed | PASS |
| 2 | No future-dated stamps (files/entries dated tomorrow) | 3 (`PROBLEMS.md:12`) | YES — suite-red `test_no_future_dated_stamps` | PASS |
| 3 | No same-day stamp ahead of the wall clock | 4 (`PROBLEMS.md:14`) | YES — pre-commit `guardrails/check-future-times.sh` | PASS |
| 4 | Chat lead `[HH:MM]` read from the clock, not feel (communicator rule 7 + the date-before-any-stamp habit) | 20+ (`PROBLEMS.md:15`) | YES — every-prompt clock-injection hook (row 134) + commit fence | PASS with residue |
| 5 | Keep a test-needled phrase on one source line | 1 (`PROBLEMS.md:16`) | n/a — only ONE occurrence, no second break | PASS (channel not yet owed) |
| 6 | Route mechanical work to a cheaper seat; carry the delegation line (INV-108's worked proof, home = base rule + pipeline law) | 2 (ROADMAP rows 253/254) | YES — every-prompt routing reminder in the chat hook + suite-red delegation check M-241 | PASS |

Rows NOT in scope (present in the ledger, not standing behavioural rules with a once-read home):
- `PROBLEMS.md:17` push-gate prover-freshness red mid-batch — a design tooth (M-6) firing as
  intended, not a rule that "breaks"; recommended AGREED NON-PROBLEM.
- `PROBLEMS.md:18` GitHub Actions Node 20 deprecation — infra annotation, not behavioural.

## Note on item 4 (the residue)

The chat-stamp rule carries its channels, so INV-108 is satisfied — the law requires that a channel
be *earned*, not that residual drift reach zero. The known residue: the prompt hook covers the
prompt moment only; mid-turn stamps still drift and lean on the date-before-any-stamp habit plus the
commit fence (recurred again this session, `PROBLEMS.md:15` tail; NEXT_STEPS "Standing habits"
notes it; row 134's zero-drift field leg stays open). This is a standing open field leg, tracked,
with a channel in place — not a missing-channel finding, so it does not block the bump.

## Sweep verdict

PASS. Every once-read behavioural rule with two or more recorded mid-turn breaks already carries a
live channel — a hook line, a suite-red check, or both. No twice-broken once-read behavioural rule
sits on prose alone. **Nothing in this item blocks the 1.1.0 bump.**

Counts: 6 rules walked, 0 missing-channel findings, 1 pass-with-residue (item 4, tracked open field
leg), 1 input gap named (behavioural-rule breaks split across PROBLEMS.md and the ROADMAP — a
one-home follow-up candidate, not a blocker).
