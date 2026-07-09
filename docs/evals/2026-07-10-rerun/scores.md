# Scores — full eval re-run, all 7 working skills (2026-07-10)

Trigger: a general re-run request (night audit), and the 0.8.75→0.9.0 MINOR bump on 2026-07-08 fires the
milestone gate that feedback-intake and test-author's own Re-run sections name ("at any MINOR bump of
the pack") — both were last run 2026-07-07, before that bump, so both are due alongside the five
unconditional skills. Arms: one Sonnet worker each, bare vs with-skill (repo skill versions: build-pipeline
0.2.44 · communicator 0.1.41 · product-prover 0.1.15 · publish 0.1.3 · spec-author 0.1.24 ·
feedback-intake 0.1.0 · test-author 0.1.2). Bare arms used zero tool calls (verified); with-skill arms
used exactly one Read of the repo's own `skills/<name>/SKILL.md` (not the Skill tool, to avoid loading a
different globally-installed copy). Honest boundary (evals/README.md) applies throughout: bare is
bare-of-the-SKILL, loader-fed — a machine-global CLAUDE.md and personal profile still feed method into
every "bare" worker.

## build-pipeline

| Criterion | bare | with-skill |
|---|---|---|
| Door named aloud before any file touch (T-12) | RED — opens with "reproduce first," no door/kind named | GREEN — step 0 states door=bug, kind=infra, size, priority before any tool step |
| Work-kind named at intake (T-16) | RED — absent | GREEN — "work-kind: infra" |
| Fix the class, sweep look-alikes (rule 14) | MET BARE — step 10 greps for the same unguarded pattern elsewhere and fixes siblings | GREEN — named as its own step ("Class sweep (base rule 14)") |
| Red-on-bug test before code | MET BARE — step 9 writes a failing test first | GREEN — explicit red-first step, ties to matrix rows |
| A pending question never parks the lane (INV-4) | **RED (new form)** — decides the auto-create-vs-error question silently itself, with no flag that it's a judgment call needing sign-off, and no report step at all | GREEN — decided once, `[default]`-tagged, explicitly "told at landing, never asked/confirmed" |
| Guardrails run named before done | RED — no mention of any pre-commit/guardrail check | GREEN — "run the whole suite (reach-map law)" named as a step before commit |
| Verify by deed on the real artifact | MET BARE — step 12 manually re-runs the original repro command | GREEN — explicit real-command re-run against the fix and every sibling |
| Plain-language report to the owner before push | **RED (regression from prior MET BARE)** — no report/communication step appears anywhere in this bare run; it stops at "commit... consider it done" | GREEN — landing report step names the `[default]` choice, in plain words, with an example |
| Capture echo at intake (heard·door·name·row) | — (bare carries no echo concept) | GREEN — the intake line doubles as the echo (size·priority·door·kind·map) |
| Verify in the medium's own form (CLI = real command round-trip) | MET BARE — real re-run of the actual CLI command | GREEN — real command run against original + every sibling path |
| A taken default TOLD, never confirmed | RED — no defaults framing at all this run | GREEN — explicit "told... never asked/confirmed" |
| Delegation brief carries ledger walk + clock | — (bare plans no delegation) | PARTIAL — delegation is named with a self-contained brief (files, anchors, checks) but no clock/ledger-walk line, same gap as the 2026-07-06 batch-2 run |
| Steps worked in their craft's head | — | PARTIAL — substance is craft-true (matrix/test/verify read correctly for a CLI) but no hat is named, same as before |

## communicator

| Criterion | bare | with-skill |
|---|---|---|
| Plain product words, no dev jargon | MET BARE | GREEN |
| Icon map, one substance clause per line (rule 9) | RED — plain prose paragraphs, no icons, no explicit what-remains line | GREEN — ✅✅✅🙋 map, one substance clause per line |
| One decision asked cleanly with recommendation marked | MET BARE | GREEN |
| No internal bookkeeping doing the talking (rule 8 NEVER-list) | **RED — regression**: "All 64 checks pass. The new version is saved on my end..." leads with the check count and version-speak | GREEN — no version number anywhere; "saved and tested clean" carries the same fact in outcome language, numbers absent |
| Retell, don't reference: rows trail, never lead | MET BARE (no row numbers used at all) | GREEN (no row numbers surfaced; the message stays in feature-name language throughout) |
| In-flight feature named with its pipeline station (INV-27) | RED — "one piece is on hold" names no station | PARTIAL — "built and tested, one thing left before it ships" names the station in plain words (roughly: built, pending one decision) but doesn't use the literal departures-board handle from the skill |
| The outcome leads (rules 6/9, INV-28) | MET BARE — each of the three sentences opens with the user-visible outcome | GREEN — every ✅ line opens with what he can now see/do |
| Decision asked in consequences, not mechanisms (INV-32/rule 10) | PARTIAL — describes urgency vs. time abstractly, no concrete "what you'd see" framing | GREEN — "the thing most worth fixing is always what you see first," plus an offered side-by-side, concrete consequence framing |
| A taken default is TOLD, never confirmed (INV-31) | — (scenario carries no taken default, as noted at the 2026-07-06 run) | — (same scenario gap persists; still owed a scenario tweak) |

**Regression flag:** the bookkeeping-leak criterion (rule 8) was bare-RED / with-skill-GREEN this run —
consistent with the shipped NEVER-list fix from row 126, not a new recurrence. No new regression found
in the with-skill arm this time.

## product-prover (FULL mode)

| Criterion | bare | with-skill |
|---|---|---|
| Finds the view×persistence composition hole | MET BARE — item 5 (only mutes persist; volume/view unaddressed) | GREEN — F7, framed as a class ("the reload question... left open for every other piece of session state"), must-fix |
| Finds the export liveness hole (no failure path) | MET BARE — item 4 | GREEN — F5, must-fix, with retry + max-duration |
| Severity triage on every finding | RED — items numbered 1–9 with no severity words, just a "resolve #1/#2 first" ranking | GREEN — every finding tagged must-fix / should-clarify / worth-considering |
| Four-part findings: headline · quoted pin · consequence · action | RED — flowing numbered paragraphs, no quoted spec pins | GREEN — each F-numbered finding: headline, `>` quoted spec line, consequence paragraph, then a concrete "state X" action |
| Model extracted first + stated assumptions | RED — no explicit entity/state model, no assumptions section | GREEN — Phase 1 states entities, per-entity states, actor-action table, and 4 named assumptions |
| Coverage tables or named N/A | RED — none | GREEN — CRUD table + invariants-per-state table + explicit "not applicable" for authorization |
| Paste-ready properties for the author | RED — advice is prose ("state explicitly...") not literal sentences to paste | GREEN — 4 verbatim paste-ready property sentences in Phase 5 |
| Substance beyond the bare run | — | GREEN — F1 (no-track precondition) and F9 (all-4-muted edge) are new findings the bare run never raised |
| Mode named aloud, modes list intact (INV-29) | RED — no mode/triage stated | GREEN — "Running in FULL mode (product-prover, whole-document review...)" plus an explicit Phase 0 TRIAGE line |

All nine criteria land exactly as the eval file predicts: MET BARE on the two "obvious" holes, RED→GREEN
on every structural/procedural promise.

## publish

| Criterion | bare | with-skill |
|---|---|---|
| Kind and target named first, checklist keyed to them | RED — no kind/target framing, opens straight into generic repo hygiene | GREEN — "Kind... infra/tool... Target: GitHub repo" opens the plan, and the walk is explicitly split into floor / kind-row / target-row sections |
| Floor: first-screen WHAT/WHO/HOW in reader's language, claims true today | PARTIAL — README planned with "what it does, how to install," no explicit reader-language or claims-true-today framing | GREEN — "answers WHAT chordscan is, WHO it's for, HOW to start — in the reader's language... every claim... true of the shipped code today" |
| Kind row (tool): a real run with real output; failure behaviour named | PARTIAL — mentions "real example command with real... output" but no failure-behaviour framing | GREEN — "at least one REAL run included" plus explicit failure-behaviour bullet (bad/corrupt/no-note-MIDI input) |
| Stood-down steps named, not silently skipped | RED — no such concept | GREEN — CI/release-notes-type steps aren't in this scenario, but the walk explicitly separates "fix before asking" from steps and names what a GitHub-target step is (screenshots "likely none... but if...") rather than silently dropping it |
| Fix everything first, then ask ONLY what's genuinely the human's, batched | RED — five questions asked up front (license, sample-file rights, account, name, credit), none marked as sequenced after fixing | GREEN — explicit "Fix before asking" section precedes the ask; the ask list narrows to license, sample-file rights, name-collision, and the push go/no-go — the same substance as bare's questions, but ordered fix-then-ask and framed as "only their call, not guessed" |
| The gate stays the human's | MET BARE — "I wouldn't publish until those are answered" | GREEN — explicit "the skill prepares the deposit; it doesn't authorize the push," repeated at the close |
| Public-repo hygiene: secrets/history sweep, fixture copyright, license compatibility, fresh-clone check, name collision | MET BARE — names secrets/history sweep, fixture-copyright (producer's own unreleased music), clean-env install; misses dependency-license compatibility and explicit name-collision check | GREEN — all five present, including dependency-license compatibility and a fresh-clone check named explicitly |

Same shape as the first-run record: the bare arm's public-repo-hygiene instincts stay strong (this run
it's short only the license-compatibility and name-collision items, both of which the with-skill arm
covers), while everything requiring the skill's own structure (kind/target framing, stood-down naming,
fix-before-ask ordering) stays RED bare / GREEN with-skill.

## spec-author

**Honest-boundary note carried forward:** this run used the de-contaminated prompt (no enumerated
failure-mode hints) per the 2026-07-06 fix, so bare's silent-decision count is read as genuine, not
prompt-fed.

| Criterion | bare | with-skill |
|---|---|---|
| No silent micro-decisions: every invented choice ⟨DECIDE⟩-asked or `[default]`-tagged, batched | RED — no-wraparound, resolve-at-press-timing implied by the invariant wording, per-view lightbox behavior, all decided silently; zero tags, zero questions | GREEN — one ⟨DECIDE⟩ (sequence-end behavior) plus six `[default]` tags, closed with a numbered batched-questions list |
| Regression fences open the delta when a live surface is touched (T-14) | RED — absent; states the grid/list invariant as prose with no anchor citation at all | GREEN — CR-LB-1 states the fence explicitly, with an honest ⟨cite pending⟩ flag rather than an invented anchor |
| Delta closes with non-goals + a success measure | RED — absent | GREEN — both present; the success measure is explicitly `[default]`-tagged as unconfirmed |
| Facet sweep completeness (a11y, performance, hierarchy, empty/error/loading) | RED — invariants cover close-paths and ordering only; no a11y, no performance envelope, no visual-hierarchy sentence | GREEN — full facet sweep: phone layout, touch, empty/error/loading, accessibility (focus trap via tab order, alt text), performance envelope (flagged as a picked number), visual hierarchy |
| Composition across canonical axes, incl. persistence/reopen | RED — view-consistency stated (LB-5) but mode/tier/persistence/concurrency/two-window axes untouched | GREEN — full axis walk incl. explicit mode N/A, tier ⟨DECIDE⟩-flagged N/A, persistence `[default]`, concurrency N/A, two-window independence stated |
| Use-case-first shape, anchors trail, index closes the doc | MET BARE — scenario prose with trailing codes, closing Formal index | GREEN — same shape, deeper (states/transitions/invariants sections plus the index) |
| The fit walk: arrival, where-next, return visit, cross-entry, invited-next; trivially-closable holes closed and written how | RED — no journey lens at all, purely a states/transitions description | GREEN — explicit "The fit walk" section covering arrival, what-they-do-here, where-next-from-every-state, return-visit, feel-against-a-prototype (correctly N/A'd, no prototype exists), invited-next |

All seven criteria reproduce cleanly: RED bare / GREEN with-skill on every promise, no MET-BARE
surprises beyond the one already expected (use-case-first shape, loader-fed).

## feedback-intake

Due this run per its own gate: the 0.8.75→0.9.0 MINOR bump (2026-07-08) postdates its last recorded run
(2026-07-07).

| Criterion | bare | with-skill |
|---|---|---|
| Field evidence has ONE home tied to the feature's success measure | RED — the friend's map remark became a "dated observation... watch-item," a separate ad hoc category, not the ledger; the visitor's praise went to "the journal," not a single evidence home either | GREEN — both the map remark and the visitor praise land as dated FEEDBACK.md lines citing the specific feature's scenario |
| A reaction never becomes a queue row on the agent's own judgment | PARTIAL — the map remark correctly stays out of the queue this run (no queued story), though it's routed to an invented "watch-item" category rather than a named ledger | GREEN — explicit "I don't open a queue row on my own judgment (that verdict belongs to the wish door)" |
| Wish-shaped items walk wish intake (door, echo, row) | GREEN — the slow-gallery report is queued to ROADMAP.md, dated, paraphrased | GREEN — same, framed as field evidence rather than an automatic queue row (a sharper reading of "vague symptom, not yet a request") |
| An answer closes forever and is harvested | GREEN — archived to docs/decisions/, blocked work released | GREEN — same, named as "closes it forever" |
| A fix-sized comment is fixed the same session, journal line, no queue | GREEN | GREEN |
| Workshop noise goes to the problem ledger, never the feedback home | GREEN — PROBLEMS.md row with both occurrences noted | GREEN — same, plus the explicit append-date-on-re-mention discipline named |
| The inbox sweep is ONE commit: route landed + file removed | RED — "the inbox file is cleared once the note is recorded" as two implied separate actions, the one-commit law never named | GREEN — explicit "one commit both lands this ledger line and removes the swept inbox file" |
| One echo per item, the route named back | PARTIAL — natural per-item replies given, but the discipline (exactly one echo, route named) isn't stated as a rule | GREEN — "every item gets exactly one echo sentence (receipt discipline)" stated as a cross-cutting rule, and each item's reply names its actual route |
| Re-mention appends its date, changes nothing else | RED — absent as a named rule (item 5's fix doesn't test this since the item's dependency is now installed) | GREEN — named explicitly for item 5 |

Reproduces the original red closely: the bare arm's instincts remain solid on the wish/decision/fix-sized
lanes (still green there, as the eval's floor note predicts), but it still lacks the single ledger home
for field evidence and the one-commit/one-echo/re-mention disciplines that are exactly this skill's
layer.

## test-author

Due this run per its own gate: the 0.8.75→0.9.0 MINOR bump (2026-07-08) postdates its last recorded run
(2026-07-07).

| Criterion | bare | with-skill |
|---|---|---|
| The matrix is an ARTIFACT: inventory first, rows derived, coverage checklist walked at close | RED — tests are derived criterion-by-criterion directly into prose, no named axis inventory, no closing checklist | GREEN — "State space (named before cells)" opens both sections before any row; a derivation-defect note (the assumption flag) closes the exercise |
| Every row states BOTH sides (do + never) | PARTIAL — most criteria carry a positive assertion only; a few (e.g. empty bug lane) are implicitly a never-claim but not labelled as such | GREEN — every row's table cell states "Does: ... Never: ..." explicitly, and several rows (BL-4, PL-3) exist specifically for the never side |
| A LEVEL pinned per row, by what the user would see broken | PARTIAL — levels named per test ("browser-computed," "DOM-structure") but the "why this level" reasoning is only given in the closing bullets, not per row | GREEN — a Level column on every row, with the closing bullets adding the "why this and not string/DOM-text" reasoning per case (e.g. PL-2's split DOM-text/browser-computed) |
| State space named before cells (view axes × data axes) | RED — axes are never named as such; fixtures are described per run-type without a stated cross-product | GREEN — axes explicitly named before any row for both sections (overlap-depth × run-type; run-type × viewport × playback-state) |
| Red-first proof discipline | RED — absent, no mention of proving any test red first | GREEN — "Every new row is proven red against the current build before its fix lands" stated as a closing rule |
| Pinned skip-set (an unexpected skip is a failure) | RED — absent | GREEN — "the skip-set is pinned exactly (e.g., no-audio run legitimately skips the currentTime-advance check... that skip is expected, not silent)" |
| Traceability as a STANDING test | PARTIAL — "every test case traces back to its criterion by anchor code" stated as a fact about this derivation, not as a suite-level enforced check | GREEN — "traceability then stands as its own enforced test, failing the suite on any row citing a missing test, duplicate id, or an anchor with zero rows against it" |
| Derivation defects routed to their source | RED — the two anchor-less bug-lane criteria are handled silently (given a level and a test, "[no anchor]" noted in the header but never flagged as a defect to route back) | GREEN — explicit reasoning for why the anchor-less rows are legitimate (matrix-local, citing a parent anchor) rather than a defect — and separately flags the one real ambiguity (which spec clause maps to which of INV-7/INV-9) as an assumption needing the author's confirmation, i.e., routed rather than silently guessed |

Reproduces the original red/green split; the with-skill run additionally demonstrates the "route a
derivation ambiguity back" behavior on a live ambiguity this scenario happened to contain (the
INV-7/INV-9 clause mapping), which the bare arm passed over without comment.

## Cross-skill verdict

All seven skills show clear, reproduced marginal value over the loader-fed bare arm on every RED→GREEN
criterion the eval files predict — no criterion flipped from GREEN with-skill to RED with-skill in this
run (no regression in the pack itself). Two items worth a note, neither a gate-blocker:

- **build-pipeline**: the bare arm's "pending question" behaviour changed shape from the original red
  (was: "I'd stop and ask") to a new red (this run: decides silently, states no report step at all) —
  still a genuine RED against the criterion, just a different failure mode; and the "plain report before
  push" criterion, MET BARE in the very first run, came back RED this time (no report step appears in
  this bare transcript at all) — both are properties of what a bare loader-fed run happens to produce on
  a given sampling, not of the skill, but worth folding into JOURNAL as a data point on bare-arm variance.
- **communicator**: the departures-board station-naming criterion (INV-27) scored PARTIAL rather than
  clean GREEN this run — the with-skill message names the station in plain words ("built and tested, one
  thing left before it ships") but doesn't use the skill's own trailing-station handle. Candidate for a
  sharper worked example in the skill file if this recurs on a third re-run.
