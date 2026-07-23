# Cross-skill seam reconciliation — notes (2026-07-22)

Reconciliation pass over the eleven pack skills after ten independent register rewrites + the new
`text-audit` skill + spec-author's content update. Scope: seams only. Write set touched:
`skills/feedback-intake/{SKILL,README}.md`, six skill footers (`communicator`, `design-reviewer`,
`feedback-intake`, `live-spec-base`, `test-author`, `text-audit`), `README.md`, `OVERVIEW.md`.
No commits. tests/, guardrails/, scripts/, docs/, the spec, and the conversion/pilot/assembly dirs
were left untouched (read-only reference only).

## Task 1 — one name per concept: term divergences + resolutions

The winner is decided the pack's own way: the assembled spec's pooled glossary
(`prototype/2026-07-22-spec-format/assembly/PRODUCT_SPEC.md`, read-only) is authoritative; the
one-name gate's alias registry (`guardrails/one-name-aliases.json`) and the register lint
(`scripts/preshow-register-lint.py`) constrain the exact surface form.

| Concept | Diverged names | Glossary/registry verdict | Resolution |
|---|---|---|---|
| the intake classification / verdict on whether a handed-in item becomes a queue row | feedback-intake said **wish intake** (its rewriter renamed "wish door" → "wish intake"); build-pipeline + spec keep **door** | Glossary line 53 defines **door** (no "wish intake" entry). build-pipeline `request-kind-table.md:14` states the same concept as "the door's own verdict on the wish at intake". Register lint bans the two-word collocation "wish door" (`en-wish-door`). | **door** wins. Swept feedback-intake's 7 sites of "wish intake" → **the door** (bare "door", not the banned "wish door"): SKILL.md description + lines 27, 35, 53; README.md lines 33, 82, 88. "wish intake" is not pinned anywhere (verified), so the swap is pin-free. |
| the movement-end report | ALL skills uniformly say **landing report**; assembled spec says **delivery report** (assembly DELTA item 4: renamed in the source units) | Glossary canonical = **delivery report**. BUT `one-name-aliases.json` does NOT list "landing report" as an alias (the gate does not yet treat them as one thing), and "landing report" is **pinned** to skill bodies. | **No skill edit.** The eleven skills already agree with each other (one name: "landing report") and with the LIVE `PRODUCT_SPEC.md`. The rename to "delivery report" is part of the in-flight spec-format migration that another worker lands on the spec side; propagating it to skills now would (a) desync skills from the live spec and (b) break the "landing report" pins I may not edit. Flagged for the migration wave. |
| the harness's local task panel | ALL skills say **harness task list**; assembled spec says **harness task panel** | Glossary canonical = **harness task panel**. But `test_traceability.py:2512` pins "harness task list" in the LIVE spec. | **No skill edit** — same reasoning as delivery report; belongs to the spec-format migration wave. |

Divergence note: build-pipeline's own note recorded renaming "wish door" → **the door** in
`request-kind-table.md` (register-lint forced), so build-pipeline and the glossary already agreed;
only feedback-intake had drifted to "wish intake". After the sweep every skill uses **door** for this
concept and the term is a reference, defined once in the glossary + base rule 15.

## Task 2 — base-rule citations: drift check

Grepped every `base rule N` citation in the ten non-base skills (30 citations across build-pipeline,
communicator, product-prover, publish, and build-pipeline references). Read each cited rule's rewritten
text in `skills/live-spec-base/SKILL.md` and matched it to the citing context. Rules verified against
their citations: 1, 2, 4, 5, 6, 12, 13, 14, 15, 16, 18, 19, 30, 32 (every distinct rule number cited).

**No drift.** Rule numbers and meanings were preserved by the base rewrite. One citation worth a note:
`request-kind-table.md:14` cites "base rule 16" for "the outsider never writes the tree" — correct,
because rule 16 ("A prototype stays a sketch") ends with the clause "an outsider's route is an inbox
wish instead", which owns exactly that fact.

## Task 3 — no term defined twice (contradicting gloss → reference)

One contradicting gloss found and fixed. feedback-intake's rewriter grounded "measurement family" at
first use as "the pack's measurement **skills**". The defining home (glossary line 107) says the
measurement family is "the **deferred machinery, still unbuilt**", and feedback-collector + the LIVE
spec both frame it as deferred/[target]. Calling it existing "skills" contradicts the deferred/unbuilt
status. Changed to "the pack's **deferred measurement machinery**" (SKILL.md ~line 90), matching the
home and keeping the cold-reader grounding.

Other added glosses checked and left (non-contradicting references, not second definitions): publish's
engine/instance grounding (its own INV-119 domain), publish's evals baseline gloss, communicator's
capture-echo gloss ("the human hears the caught request read back" — consistent with glossary line 18).

## Task 4 — pack lists: text-audit added

`text-audit` is the eleventh skill; it was absent from every pack roster. Added
"**text-audit** reads a text as a stranger and fixes where they stop" to all six closing footers
(communicator, design-reviewer, feedback-intake, live-spec-base, test-author, text-audit's own),
inserted before `**publish**`. Added a matching entry to README.md's one-line roster (before
`publish`) and an OVERVIEW.md bullet (before publish). Role phrase derived from text-audit's own
frontmatter description.

Result on `tests/test_traceability.py::TestPackListParity::test_real_repo_lists_complete`: the gap
list shrank from every-surface (SPEC + README + OVERVIEW + all footers) to **one residual**:
`SPEC working-skills text: text-audit`. The live `PRODUCT_SPEC.md` does not yet name text-audit; that
is the spec-side wiring another worker owns (the task forbids editing the spec). Known, reported.

## Task 5 — pins

**No pinned sentence was changed.** Every phrase I edited was grepped across `tests/` and `guardrails/`
first; all came back clean (no match):
- "wish intake" — not pinned (the `en-wish-door` fixtures in `test_preshow_register_lint.py` /
  `test_register_judge.py` hold their OWN strings, not feedback-intake's prose).
- "the pack's measurement skills" — not pinned.
- footer / README / OVERVIEW role phrases — not pinned (parity checks presence of the dir NAME as a
  substring, `_pack_list_gaps`; the footer test's negative fixture is a hardcoded old string, not a
  read of the files).

Two pins CONSTRAINED the pass (they are why "landing report" and "harness task list" were NOT renamed):
- `tests/test_no_silent_drop.py:29` asserts `"lists every removal in its landing report"` in
  `skills/communicator/SKILL.md` (and PRODUCT_SPEC.md).
- `tests/test_traceability.py:2131` asserts `"every taken shed named in the landing report"`.
- `tests/test_traceability.py:2512` asserts `"harness task list"` in the live spec.
These pinning files were not edited.

## Verify

- `scripts/preshow-register-lint.py` on all nine touched files: clean, EXCEPT `communicator/SKILL.md`,
  whose 9 hits (lines 211, 220-221, 459-460) are the PRE-EXISTING lawful quoted specimens documented in
  the communicator rewrite note (banned patterns cited inside the rules that ban them). None at my
  footer edit (~line 499). No new leak introduced.
- `scripts/spec-style-lint.py` on the touched skills: feedback-intake SKILL 0 errors, feedback-intake
  README 0 errors. Errors in communicator (1), design-reviewer (3), text-audit (4) are all PRE-EXISTING
  (quoted "X, not Y" specimens the skills teach, description caps, "What it is not" boundary headings),
  none at my edits. **No new scissors introduced.**
- `tests/test_traceability.py`: **168 passed, 3 failed.** All three are known:
  1. `TestWorkerContract::test_craft_ladder` — pins build-pipeline's OLD phrase "whose head you wear",
     which build-pipeline's rewrite changed to "which craft's standards judge each step". Re-pin sweep.
  2. `TestPackListParity::test_real_repo_lists_complete` — reduced to the single SPEC residual above;
     spec worker's wiring.
  3. `TestSkillEvals::test_skill_evals_present` — `evals/text-audit.md` carries no dated `bare run:`
     record (the eval was authored tonight without one). Outside this write set (evals/) and an honest
     record needs `docs/evals/` (also outside scope). Owned by the eval author; needs a real bare run.
