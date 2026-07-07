# Prover cross-link — SPEC humanize batch: "A prototype is not the product" (2026-07-07, session 24)

Per the humanize per-batch procedure (step 6): an OLD-vs-NEW fact table built from the section's `git
diff`, checking that the rewrite still carries every fact, precondition, and invariant the old prose
claimed. The rewrite is wording-only; no rule added, none removed. Register: neutral technical-writer
voice (communicator "The writing register").

## Mechanical gates (already green)
- **Phrase preservation** (`needle-extract --verify`, section-scoped): OK — 11/11 preserved.
- **Anchor set**, each still trailing a sentence carrying the same fact: `[E-17]`×2, `[E-17, INV-17]`,
  `[INV-16]`, `[T-12, INV-16]`, `[INV-10]`, `[ACT-2]`, `[E-6]`, `[E-10]`, `[target, E-6]`, `[S-0]`,
  `[INV-17]`, `[INV-30]`, `[INV-43]`, `[default]` — all present, unchanged, trailing.
- **Header string** `## A prototype is not the product` — unchanged. Entities `**prototype**` /
  `**norm**` still bold at first mention.

## Fact table (OLD claim → NEW carrier)
| # | Fact / precondition / invariant (old) | Anchor | Carried in new? |
|---|----------------------------------------|--------|-----------------|
| 1 | Exploring is legal; a prototype is a fenced sketch in its own named home (`prototype/` folder or branch) | — | ¶1 — yes |
| 2 | Every prototype artifact carries the PROTOTYPE label in its kind's form (page banner / `_prototype: true` / CLI first-line banner / bare-file marker) | E-17 | ¶2 — yes |
| 3 | Door-step boundary: HAVE-it = feature; SEE/TRY with no commitment = sketch, no lane, no spec; unclear ⇒ one plain question, no guess | INV-16 | ¶3 — yes |
| 4 | Opening a prototype home is a repo write under write-ownership; a senior judgment act; outside session files an inbox wish; a worker never opens one on its own brief | INV-10, ACT-2 | ¶4 — yes |
| 5 | The fence is one-way: never wired/linked/styled into a prod surface; shown only under label; nothing reaches the human AS product unless its surface walked the pipeline | — | ¶5 — yes |
| 6 | Promotion is not a merge: the feature enters at the spec step like any wish; prototype = evidence; its code holds no rights | T-12, INV-16 | ¶6 — yes |
| 7 | Machine leg: a prod file referencing a prototype home is RED (live for pack repo); the other two legs (surface-registry completeness, behaviour-traces-to-spec) are still targets | E-6, E-10, target/E-6 | ¶7 — yes |
| 8 | With all three legs: header honesty both ways — spec never claims what isn't built; build never contains what spec doesn't name; today fence enforced, rest promised/marked/owned | S-0, INV-17 | ¶8 — yes |
| 9 | Approved look lives in its artifact; clause points there, build reads it; text can't carry feel; look-alike incident (75 tests green, tlvphoto door+gallery 2026-07-05) | — | ¶9 — yes |
| 10 | Human approving a sketch as the look makes the prototype the norm; one law with four arms | — | ¶10 — yes |
| 11 | Arm 1: clause cites artifact via a `norm: <path>` pointer at line end beside anchors; prose carries laws, artifact keeps look; spec-author owns pointer format | — | ¶11 — yes |
| 12 | Arm 2: approval freezes artifact into records (copy to `docs/norms/` + dated provenance); pointer cites the frozen copy; a norm pointer never reaches into a live prototype home; fence stays absolute; sketch free to die | E-17, INV-17 | ¶12 — yes |
| 13 | Arm 3: building a norm-pointer surface opens the artifact before the code step; landing records a one-line plan-vs-prototype diff; a missing diff line is a defect at review; verify feel bar reads the same pointer | INV-30 | ¶13 — yes |
| 14 | Arm 4: prover reads visual clauses with the norm lens; finding = no-pointer clause OR clause contradicting its own artifact; "wordless door ≠ no question" class | — | ¶14 — yes |
| 15 | Mockup-first entry condition written in the queue row at intake ("entry: mockup-first"); cancelled only by the human naming it; a general "go build" moves priority, never that condition | — | ¶15 — yes |
| 16 | Law binds forward: pointer owed at the first landing that touches a clause, never retroactively en masse; pointer names only a human-approved prototype; unapproved sketch = plain evidence; text-born clause carries no pointer | E-17 | ¶16 — yes |
| 17 | No visible surface (facets N/A); non-goals: no mechanical pointer-grep guardrail yet; norm artifact format stays free | — | ¶17 — yes |
| 18 | Success measure: next prototype-born surface lands with its pointer + plan-vs-prototype diff line; look-alike class does not recur | default, INV-43 | ¶18 — yes |

## Verdict
PASS. Every old fact, precondition, and invariant has a carrier in the new prose. No anchor moved to a
weaker sentence. No rule added or dropped. Internal terms (fence, door step, one-way, prod surface,
lane) are now grounded in plain words at first use. The rewrite is safe to land.

## Addendum — iteration 2: restructure + positive title (2026-07-07 ~18:28)

The section gained structure (lists for the label forms, the three machine legs, and the four-arm
norm law; an H3 for the approved-look part) and a positive title. "A prototype is not the product"
(a scissors frame, banned by the register) became **"A prototype stays a sketch"**. The rename is
coordinated across all six live homes in one commit: the SPEC header, three Formal-index section
cells, base rule 16 in `live-spec-base`, and two checks in `test_traceability.py` (the door/prototype
needle and the base-rule-16 regex).

Gates: phrase preservation 11/11 (section-scoped, under the new name) · every anchor present and
trailing · full suite 175 green. No fact, precondition, or invariant changed from iteration 1 — this
is layout plus a title. Verdict: PASS.
