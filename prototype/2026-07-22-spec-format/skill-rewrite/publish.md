# publish skill — register rewrite notes (2026-07-22)

Scope: register-only rewrite of `skills/publish/SKILL.md` and `skills/publish/README.md`.
Meaning, scope, force, code anchors (INV/SPEC/T/E), frontmatter trigger semantics, and
base-rule-by-number references all preserved.

## Counts

- Contrast-by-denial (scissors) fixed: 7
  1. `directory card — not your commit history` → positive: reader meets the surfaces; "The commit history stays behind them."
  2. `communicator's rule 5 rather than a publication` → "belongs to communicator's rule 5." + own boundary sentence "That in-session exchange is not a publication."
  3. `in the reader's language rather than the repo's internal vocabulary` → "in the reader's language, keeping the repo's internal vocabulary out"
  4. `install and run ... rather than assuming "works on my machine"` → "; do not assume it \"works on my machine\""
  5. `in the directory's own register rather than as repo prose` → "; repo prose does not fit a directory listing."
  6. `the taste comes from a real run rather than a promise` → "a real run that shows the product working."
  7. `it rides the suite, not the push chain — the note is a process artifact...` → "it rides the suite; the note is a process artifact with no committed file for a push gate to scan."
- Coined metaphors → plain mechanism words: 3
  1. `plus the seam where a publish target adds its own steps` → "plus the point where..."
  2. `The walk above is the trunk` → "The walk above is the shared base"
  3. `a diagram where structure beats words` → "a diagram where structure shows what words cannot"
- Boundary clause repositioned to its own positive sentence: 1
  - `— and never as decoration` (mid contrast) → "They never ride as decoration." (also split the Comparisons sentence into three shorter sentences)
- Register-lint (`scripts/preshow-register-lint.py`) findings fixed: 0 (file was clean before and after on both files)

### Second round (from cold-read round 1 blocking findings)

The cold reader (round 1) flagged four BLOCKING passages, all genuine register faults in
scope (tangled run-ons / ungrounded terms). Fixed:
- **Floor mega-paragraph** (was one ~20-line semicolon run-on): split into short SVO
  sentences and paragraph breaks. Every pinned needle kept verbatim and contiguous
  (N1/N2/N3, `made with live-spec`, the markdown attribution line, `an offer, never a gate`,
  `built with the pack`, `never re-asked`). N2 kept lowercase mid-sentence (one semicolon
  retained) and `an offer, never a gate` kept on a single line, because two tests read the
  file RAW (not whitespace-flattened): test_impersonal_shipped_docs (read_flat, case-sensitive)
  and test_made_with_attribution (raw read, line-wrap-sensitive).
- **`Shipped docs speak impersonally`**: same paragraph split into sentences; the em-dash
  after "and the reason" that broke the parallel is now a sentence boundary. N1 verbatim.
- **Opaque parenthetical** `the bare arm knew them and the skill didn't; evals cut both ways`
  → grounded/unpacked: "the no-skill baseline agent caught them and the skill's checklist did
  not — an eval measures the skill against that baseline in both directions."
- **Engine/instance ungrounded**: `An engine carved out of an instance` → grounded both terms
  at first use: "An engine — a reusable core lifted out of one live product, the instance it
  grew inside — published as a generic package...". Pinned needles ("proven first on a live
  instance", "landed in engine commit", "how each behaviour landed in code", [INV-119]) untouched.

## Lint verdict

- `preshow-register-lint.py skills/publish/SKILL.md` → OK (clean)
- `preshow-register-lint.py skills/publish/README.md` → OK (clean)

## Pins recorded (changed sentences that are pinned in tests/guardrails)

No pinned SENTENCE was rewritten. Every prose sentence I changed for register was verified NOT
pinned before editing (grepped tests/ and guardrails/ for distinctive fragments).

The floor-paragraph split, however, reflowed lines that CONTAIN pinned needle substrings. Those
substrings were held verbatim and contiguous. Two care points recorded because the split first
broke them and I corrected them:
- **`personal attribution and candid process voice`** (N2, `tests/test_impersonal_shipped_docs.py`,
  read_flat + case-sensitive). My split briefly capitalized it as a sentence opener ("Personal ...")
  and the needle went missing; reverted that one boundary to a semicolon so the needle stays
  lowercase mid-sentence. OLD in-file (broken): "comes off. Personal attribution and candid process
  voice stay" — NEW (restored): "comes off; personal attribution and candid process voice stay".
- **`an offer, never a gate`** (`tests/test_made_with_attribution.py`, RAW read, wrap-sensitive).
  My reflow wrapped it as "...is an\noffer, never a gate"; the raw-substring test failed. Rewrapped
  so "The line is an offer, never a gate:" sits on one line. OLD (broken wrap): "SKILL.md. The line
  is an\noffer, never a gate:" — NEW: "SKILL.md.\nThe line is an offer, never a gate:".

No pinning file was touched. Final needle-presence check + the four pinning test files all pass
(see Test verification below).

## Test verification

Ran (read-only) the tests that pin publish/SKILL.md strings:
- test_made_with_attribution.py, test_release_note.py, test_impersonal_shipped_docs.py,
  test_instance_engine_boundary.py — 36 passed.
- test_traceability.py publish assertions (checklist, shopfront, base-version pin) — pass.
Three test_traceability failures exist in the working tree (TestSkillEvals.test_skill_evals_present,
TestPackListParity.test_real_repo_lists_complete, TestWorkerContract.test_craft_ladder). Verified
NONE reference skills/publish — they are PRE-EXISTING, unrelated to this rewrite (text-audit eval
missing a "bare run:" date, pack-list parity, worker craft-ladder).

## Sentences left unchanged because rewriting risked meaning / pins

- **`the line is an offer, never a gate`** (floor, SKILL L54). An "X, never Y" contrast, but it
  is a pinned needle in `tests/test_made_with_attribution.py` ("an offer, never a gate") and a
  fixed pack phrase; rewriting would break the pin. Left verbatim.
- **`It never sends anything itself`** (SKILL L21). Pinned needle in
  `tests/test_traceability.py`; also a plain positive assertion, not a definitional contrast.
  Left verbatim.
- **`shopfront` / `the shopfront walk`** (SKILL L27/34-38, INV-44). A coined metaphor by the
  register bar, but an established SPEC/pack term of art pinned across tests
  (`test_traceability.py` needles: "the shopfront rides every push", "shopfront checked — current",
  and build-pipeline "shopfront" pointer). Renaming it here would desync spec, tests, and sibling
  skills. Out of register-only safe scope. Left as the standing term.
- **`tripwire`** (SKILL L79). A metaphor by the bar, but an established pack term used across the
  suite (test_listener_tripwire, spec-author "[target] tripwire rule", test_request_classifier
  "spec-motion tripwire fires"). Changing it only here creates inconsistency; left as the standing term.
- **The floor mega-sentence** (SKILL L42-61). One very long, semicolon-chained normative sentence
  carrying pinned needles N1/N2/N3 (impersonal-docs), the made-with attribution line, and multiple
  INV anchors. Only the single scissor clause inside it (#3 above) was fixed; the sentence was NOT
  restructured, because splitting it risks altering normative force and disturbing the pinned
  substrings. Left structurally intact by design.

## Cold-read rounds

- Round 1: fresh cold-reader subagent, zero context. Flagged 4 BLOCKING passages (floor
  mega-paragraph, the "bare arm / evals cut both ways" parenthetical, the impersonal-docs
  "and the reason —" broken parallel, and the ungrounded engine/instance section). All four
  fixed (see Second round above).
- Round 2: confirming read, fresh zero-context subagent. Verdict: NO blocking stops remain in
  either file; all four rewritten passages clear the stranger test. Remaining stops are
  NON-BLOCKING pack vocabulary (host, attach record, pair-split, program-data, shopfront) and
  bare pronouns ("his"/"he") — left out of register-only scope (established terms, pinned
  strings, or the separate impersonality gate at roadmap row 275, not yet landed).
