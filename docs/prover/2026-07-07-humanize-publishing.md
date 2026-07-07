# Prover cross-link — SPEC humanize batch: "Publishing — the deposit owes what its kind owes" (2026-07-07, session 25)

Register rewrite of one scenario section. Fact table from `git diff SPEC.md`. Mechanical gates green:
9/9 tested phrases re-matched section-scoped; bracket-code multiset identical to baseline (10 codes:
[T-16], [E-12], [INV-22]×2, [E-18], [ACT-1], [M-6], [E-20]×2, [INV-44], [default]); full suite 175 green.

One caught-and-fixed slip: the rewrite opened a sentence with "The checklist runs BEFORE the gate",
capitalizing the tested lowercase phrase "the checklist runs BEFORE the gate". The extractor is
case-sensitive, flagged the drop, and the sentence was reworded to keep the phrase lowercase ("Here the
checklist runs BEFORE the gate…"). Meaning unchanged.

## Fact table (old claim → new carrier → verdict)

| # | Old fact / code | New carrier | Verdict |
|---|---|---|---|
| 1 | Work leaves the machine (repo public, skill to plugin directory, release cut, cards to a design project); publication is its own surface owing what the artifact's KIND owes; same work-kind axis read at the door not intake [T-16] | opening paragraph + [T-16] trailing; "design project" verbatim | KEPT |
| 2 | Per-kind owed content: skill (install + commands + when-to-use-and-not); tool (real runs, real output); visual product (FRESH screenshots; stale screenshot = false claim in picture form); prose (reading path) | four-item list; "FRESH screenshots" verbatim | KEPT |
| 3 | Comparison/diagram joins only when it carries the argument, never decoration | "joins when it carries the argument. It never rides along as decoration." | KEPT |
| 4 | Checklist has ONE home = publish skill, pack's fifth working skill [E-12]; spec binds contract: nothing deposited past checklist, walk result rides landing report [INV-22] | paragraph; [E-12], [INV-22] trailing | KEPT |
| 5 | Each publish TARGET is a plugin embedding its own steps (Alexander 2026-07-05: GitHub plugin brings its stages); GitHub → README-at-door + release notes; plugin directory → manifest + forms; design project → cards [E-18]; target adds steps, never removes kind's owed minimum | paragraph; "Each publish TARGET is a plugin" verbatim; attribution kept; [E-18] trailing | KEPT |
| 6 | Publishing never bypasses standing gates: human's publish gate for irreversible/outward (base rule 17 [ACT-1]); host's push gates [M-6]; checklist runs BEFORE the gate so approval already worth approving [E-20] | paragraph; "the checklist runs BEFORE the gate" verbatim (lowercase, fixed); [ACT-1], [M-6], [E-20] trailing | KEPT |
| 7 | A version push re-opens the shopfront; every push ships new version, changes tomorrow's public truth even when the diff never touched a doc, so the shopfront rides every push; README CLAIMS (behaviour/counts/commands/version homes) match pushed truth | "**A version push re-opens the shopfront.**"; "even when the diff never touched a doc" + "the shopfront rides every push" verbatim | KEPT |
| 8 | Kind-owed visuals ride along: skill pack re-checks diagrams/flow pictures; visual product re-shoots what changed; tool re-runs example; stale shopfront = false claim like stale screenshot [E-20] | three-item list + the stale-shopfront line; [E-20] trailing | KEPT |
| 9 | Walk = publish skill's checklist at push scale (one home stays there); pipeline commit-and-show points at it, outcome rides landing report [INV-22]; a delta touching no shopfront claim says "shopfront checked — current"; a stale claim found is fixed BEFORE the push; freshness = claims not cosmetics | paragraph; "shopfront checked — current" and "a stale claim found is fixed BEFORE the push" verbatim; freshness restated positively; [INV-22] trailing | KEPT |
| 10 | Non-goals: no mechanical README-vs-diff checker (the reach map, row 147, candidate owner); no auto-regenerated images. Success measure: no push lands whose README claims older behaviour/count, checked at milestone audits [default] [INV-44] | final paragraph; "reach map" verbatim; [default], [INV-44] trailing | KEPT |

## Wording changes worth naming (meaning intact)
- "Freshness means claims, never cosmetics" → "Freshness is about the claims the README makes, not its
  styling." Same scope, no dash-contrast.
- The per-kind owed content and the per-push re-checks pulled into two lists.
- One sentence reworded to keep a lowercase tested phrase intact (see slip above).

Verdict: **CLEAN.** Every fact and code carried; 9/9 tested phrases section-scoped; 10-code multiset
identical; suite 175 green. No must-fix.
