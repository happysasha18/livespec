# Row 247 worker checkpoint — INV-112 remote-arm law (STOPPED, unresolved fill-in)

Briefed: 2026-07-12, applier role, mechanical landing from
.live-spec/checkpoints/pending-row247-analysis.md. Write-set fixed by the brief.

## Write-set (planned, per draft)
- .live-spec/checkpoints/row247-worker.md (this file)
- tests/test_inbox_remote_arm.py (NEW)
- PRODUCT_SPEC.md (clause insert block A after line 1592, index row block D after line 1723,
  header version bump)
- inbox/README.md (block B, append after line 18's commit-rule paragraph)
- adopt/ADOPT.md (block C, extend step 4 at line 50)
- scripts/grant-ask.md (NEW — block E, standalone home per draft's recommendation) — BLOCKED,
  see below
- ARCHITECTURE.md (block G, inbox node Owns column, line 47)
- TEST_MATRIX.md (block H, M-251 row after M-050, line 351)
- .live-spec/profile.md (block I, trust.github-grant line after line 28)
- VERSION (1.0.28 -> 1.0.29)
- .claude-plugin/plugin.json ("1.0.28" -> "1.0.29")
- ROADMAP.md (row 247 status cell)
- docs/prover/2026-07-12-row247-inbox-remote-arm.md (NEW)
- pending-row247-analysis.md (append APPLIED+CLOSED line)

## Anchors verified live before editing (2026-07-12, HEAD 8cc0368, tree clean)
- PRODUCT_SPEC.md:1592 "The outsider commits its one new file — a commit touching inbox/ only,
  its message naming the source. That commit is inside the read-only exception." — present verbatim.
- PRODUCT_SPEC.md:1723 "| INV-11 | concurrent-edit fence before write/commit | Package repo |" —
  present verbatim.
- inbox/README.md:15-18 "Commit your one new file (a commit touching inbox/ only, message naming
  the source)... in the harvest commit (git history keeps it)." — present verbatim (file is 18
  lines total, this is its tail).
- adopt/ADOPT.md:50-53 "4. **Settle the remote — a named deliverable (SPEC A-5).**"... through
  "...the pilot ended local-only that way)." — present verbatim (draft cited line 51, live is 50;
  content matches exactly, one-line drift, not a mismatch).
- ARCHITECTURE.md:47 "| inbox | parallel-safe intake door... E-11, T-10, INV-10 |
  `inbox/README.md:3`... `:14` (commit rule) |" — present verbatim.
- TEST_MATRIX.md:351 M-050 row — present verbatim (draft's "Homes touched" summary said line 345,
  but block H itself said "after M-050 (line 351)" — live matches 351, the block's own anchor).
- .live-spec/profile.md:28 "«сам пуши!...»); this answers the push-law grant question (SPEC
  INV-82) for this host." — present verbatim.

All anchors confirmed live and matching. No renumbering / drift beyond the two one-line summary
discrepancies noted above (both resolved in the block's own favor, matching live).

## Code-allocation re-verification (2026-07-12, landing order)
`grep -n "INV-112\|M-251" PRODUCT_SPEC.md ROADMAP.md TEST_MATRIX.md` — no `| INV-112 |` or
`| M-251 |` index/matrix rows exist anywhere. Two ROADMAP prose mentions (rows 242 and 250) note
both codes "stay free" for the next law-shaded row — consistent with this row consuming them.
INV-112 / M-251 CONFIRMED FREE at landing time.

## Live version values read (2026-07-12)
- VERSION (pack): 1.0.28 -> would be 1.0.29
- .claude-plugin/plugin.json: "1.0.28" -> would be "1.0.29"
- PRODUCT_SPEC.md header: "v1.0.20, 2026-07-12" -> would be "v1.0.21, 2026-07-12" (per row-233
  precedent: every landing that touches PRODUCT_SPEC.md content bumps this header +0.0.1)
- No skill frontmatter touched, per draft's block J (inbox/README.md and adopt/ADOPT.md carry no
  version field; feedback-intake untouched) — confirmed, no skill SKILL.md is in this row's
  write-set.

## Baseline full suite (2026-07-12, before any edit)
`python3 -m pytest tests/ -q` -> **411 passed in 37.22s**. Matches the brief's expected baseline.

## STOP — Block E's grant-URL fill-in cannot be resolved mechanically

Block E's template carries a literal marker `<APP-REPO-ACCESS-URL>` that the draft explicitly
requires the applier to replace with the exact, live repository-access URL for the Claude GitHub
App, read from `github.com/settings/installations` -> the Claude app -> Configure -> Repository
access. The draft is explicit this must never be guessed or fabricated.

That settings page is a per-user, per-installation authenticated GitHub web page; the resulting
URL contains an installation ID unique to the owner's account and is not exposed through any API
reachable by this session's tools:

- No browser/WebFetch tool with an authenticated github.com session is available to this worker.
- `gh auth status` confirms the CLI is authenticated as `happysasha18` via a personal access
  token (not an OAuth app user-access token).
- `gh api /user/installations` was tried as the one plausible mechanical path and returned
  `403 — You must authenticate with an access token authorized to a GitHub App in order to list
  installations`.
- A repo-wide grep for any prior record of this URL, or any "settings/installations" /
  "APP-REPO-ACCESS" / "GitHub App" mention anywhere in the tree, found nothing — no precedent
  value exists to copy forward.

This matches the brief's own step 3 stop condition exactly: "if the draft left it as a marked
placeholder with instructions you cannot resolve mechanically, STOP and report." Per the brief's
top-level rule ("On anchor mismatch, ambiguity, or unpredicted red: STOP... commit nothing"),
halting the whole row here rather than partially applying blocks A-D/F-J and leaving block E
half-done, since blocks E's home (scripts/grant-ask.md) is itself part of Done-when clause (b)
("the grant ask is scripted with its exact path") — landing without the exact path would misstate
the row's own second Done-when clause as met when it is not.

## Status

STOPPED, 2026-07-12, before any edit was applied. Working tree untouched (still matches HEAD
8cc0368, clean). Nothing staged, nothing committed, nothing pushed. Red-first test file
(tests/test_inbox_remote_arm.py) was NOT yet created (would have been step 5, not reached — no
point red-proving before block E is resolved, since the STOP is upstream of the whole edit walk).

Needed to unstop: the owner (or a session with an authenticated browser to github.com, logged in
as happysasha18) visits github.com/settings/installations, opens the Claude app's Configure page,
and hands back the exact URL — or explicitly confirms a stable/generic URL is acceptable in place
of the installation-specific one, which would be a design call outside this applier's mandate.

## Resumed, 2026-07-12 ~02:37 — orchestrator's call on block E

The orchestrator resolved the STOP: use the STABLE settings path in the grant-ask template rather
than the per-installation numeric URL. Substitution for `<APP-REPO-ACCESS-URL>`:
`https://github.com/settings/installations (logged in as the repo owner) → Claude App →
Configure → Repository access → add the target repository`. Rationale (the orchestrator's own
words, recorded per the instruction to record it): the per-installation numeric URL is visible
only inside the owner's authenticated session and changes if the app is reinstalled; the stable
settings page with the named click path is exact, durable, and never guessed. This satisfies
Done-when (b).

Applied substitution: block E's template step 1 originally read "Open the app's
repository-access settings: <APP-REPO-ACCESS-URL>" followed by a second line "(read once from
github.com/settings/installations → the Claude app → Configure → Repository access)". Since the
substituted URL text already carries the full click path, the now-fully-redundant second line was
folded away rather than kept duplicate (both lines said the same thing once the placeholder was
filled) — final step 1 reads as one line: "Open the app's repository-access settings:
https://github.com/settings/installations (logged in as the repo owner) → Claude App → Configure
→ Repository access → add the target repository." Steps 2 and 3 unchanged from the draft.

Second, related fix: block C's new_string (adopt/ADOPT.md) as drafted ends "...Script that ask
with its exact settings path (see the grant-ask template, block E)." — "block E" is the draft's
own internal lettering (pending-row247-analysis.md), not a home that exists in the shipped tree.
The draft's own block-E preamble states its recommended home is the standalone
`scripts/grant-ask.md`, "so the exact URL has one home and the prose homes point to it" — i.e. the
draft's own stated intent is for ADOPT.md to point AT that file. Applied block C with "block E"
replaced by "scripts/grant-ask.md" so the pointer resolves to a real, stable home instead of a
draft-internal label. This is not a new design choice — it completes the draft's own explicit
intent for where its prose homes should point.

Re-checked what the clock moved since the first pass (2026-07-12 ~02:34 -> ~02:37): `git log -1`
still HEAD 8cc0368, `git status` still clean — no new commits landed elsewhere in the interim. All
anchors, the baseline suite (411 passed), and the INV-112/M-251 free-code check from the first
pass stand unchanged; not re-run.

## Walk completed, 2026-07-12 ~02:41

- RED FIRST: tests/test_inbox_remote_arm.py created (block F verbatim), run alone against the
  pre-delta tree -> 4 failed (all four asserts, as expected — no home carried the needles, no
  INV-112 anchor).
- Applied verbatim: block A (spec clause after :1592), block D (index row after INV-11 :1723),
  block B (inbox/README.md after :18), block C (adopt/ADOPT.md step 4, with one pointer fix — see
  below), block G (ARCHITECTURE.md :47 owns column), block H (TEST_MATRIX.md M-251 after M-050
  :351), block I (.live-spec/profile.md trust.github-grant line after :28).
- Applied with the orchestrator's substitution: block E (scripts/grant-ask.md, NEW) — see the
  "Resumed" section above for the exact substitution text and the block-C pointer fix
  ("block E" -> "scripts/grant-ask.md").
- Version bumps (block J): VERSION 1.0.28 -> 1.0.29; .claude-plugin/plugin.json "1.0.28" ->
  "1.0.29"; PRODUCT_SPEC.md header "v1.0.20, 2026-07-12" -> "v1.0.21, 2026-07-12" (per row-233
  precedent, every content-touching spec landing bumps this header). No skill frontmatter touched,
  matching block J's own note.
- tests/test_inbox_remote_arm.py run alone after edits: 4 passed in 0.03s.
- FULL SUITE after edits: `python3 -m pytest tests/ -q` -> **415 passed in 42.45s** (411 baseline +
  4 new).
- ROADMAP.md row 247 status cell updated: build legs LANDED 2026-07-12 ~02:41, session 37; field
  leg OPEN on Done-when clause (c), named as closable only by the owner's real browser cloud
  deposit, no self-certification [INV-94]; delegation line records the block-E STOP and the
  orchestrator's resolution; DECIDE (GitHub Issues stranger door) recorded as split into its own
  follow-up row, not folded in, per the draft's recommendation.
- Full suite re-run after the ROADMAP edit: 415 passed in 43.25s, 0 failed.
- pending-row247-analysis.md: appended "APPLIED + CLOSED at landing 2026-07-12 (row247-worker.md;
  field leg open)" plus a short note on the block-E resolution.
- Prover short form written: docs/prover/2026-07-12-row247-inbox-remote-arm.md (0 must-fix, 0
  should-clarify; fill-in note + open-field-leg line + DECIDE-resolution line included).

## Status

DONE, 2026-07-12 ~02:41. Green tail: `415 passed in 43.25s` (final re-run after ROADMAP edits).
Landed with one recorded deviation (block E's URL fill-in resolved by the orchestrator's call, not
the draft's original per-installation-URL instruction) and one field leg left open by design
(Done-when clause c). Next: commit (named files, -f for the gitignored checkpoint), push, read CI
verdict, run scripts/sync-skills.sh.
