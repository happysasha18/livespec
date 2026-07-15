# Prover record — 327 (browser test harness owned by the pack): INV-157 + INV-158

Ran under **product-prover v1.1.4** (base live-spec-base v1.0.17), 2026-07-15. Mode: **CROSS-LINK** —
a surface add, not a MINOR gate. Two new invariants proved at their seams against the existing spec
(git HEAD `7faec11`). The whole document stayed in view; findings are narrowed to the two new
invariants' seams. Movement plan is ROADMAP row 327 (in flight).

## Verdict — HOLDS-WITH-ONE-DEFECT

Both invariants are sound at their core and consistent with the boundaries they invoke. The
"removable in owned code" seam is stated the SAME way in INV-157 as in INV-155 — no contradiction,
no duplication of INV-155's or INV-80's content. One defect blocks a clean landing: INV-158's index
row homes the adopt mechanism at "build-pipeline's adopt path," a home that does not exist and is not
owed by row 327's Done-when — the adoption/update mechanism lives with the catch-up walk [INV-110]
and the adoption feature, not build-pipeline. Two recommendations sharpen the seams. The two
forward-referenced homes that ARE owed by this movement (the shipped harness template, test-author's
rule) are dependencies to close, not holes.

## Seam summary

- **INV-157 ↔ INV-155.** "Removable in owned code" means the same in both: the source of the fault is
  in code the project owns (test / product / harness) versus an external tool misbehaving at random.
  Both route the not-removable case to the problem ledger [INV-23]. Consistent, no contradiction.
- **INV-157 ↔ INV-80.** No duplication and no contradiction. INV-80's three legs (unrunnable skip,
  re-export completeness, exit-code-is-not-the-verdict) are distinct false-verdict mechanisms; none is
  the blanket-timeout false-red INV-157 names. They sit beside each other as siblings in the
  suite-hygiene / suite-must-not-lie family, correctly.
- **INV-157 ↔ INV-100 (unnamed by the brief, found in scope).** INV-157's reap-the-process-group leg
  and its mute leg are the test-hygiene family — INV-100 already owns "spawned processes" cleanup and
  "leaves the machine as it found it." INF-157 attributes all three legs to INV-155 and cites INV-100
  nowhere. See F2.
- **INV-158 ↔ base rule 4.** Base rule 4 exists (`live-spec-base` SKILL.md:42, "One canonical home per
  fact") and INV-158 applies it correctly to test infrastructure. Sound.

## Referenced homes — satisfied / owed-this-movement

| Home cited | By | Status |
|---|---|---|
| INV-155's boundary (line 651) | INV-157 | **satisfied** — exists |
| INV-23 problem ledger (line 1869 / F-problem-ledger) | INV-157, INV-155 | **satisfied** — exists |
| base rule 4 (one home per fact) | INV-158 | **satisfied** — `live-spec-base` SKILL.md:42 |
| the pack's shipped harness template | INV-157, INV-158 | **owed-this-movement** — row 327 Done-when: "ships a canonical muted + hardened headless-harness template" |
| test-author's harness rule | INV-157 | **owed-this-movement** — row 327 Done-when: "test-author states the muted-clean-teardown rule"; test-author SKILL.md today has no harness/mute/process-group content |
| build-pipeline's adopt path | INV-158 | **NOT owed by row 327's Done-when** — build-pipeline SKILL.md has zero "adopt" content; see F1 |

## Formal-index integrity — PASS

- INV-157: exactly one prose anchor (line 653) and exactly one index row (line 2005). Section pointer
  "From the spec to the tests" resolves to the real header at line 633.
- INV-158: exactly one prose anchor (line 655) and exactly one index row (line 2006). Same section
  pointer, resolves. No stale or duplicate rows.

## Findings

| # | Finding | Kind | Disposition (author folds at gate) |
|---|---|---|---|
| F1 | INV-158 homes the adopt mechanism at "build-pipeline's adopt path" — a home that does not exist and is not owed by row 327; adoption lives with the catch-up walk [INV-110] / the adoption feature | defect · boundary-issue (composition) | **folded** — INV-158's prose and index row repointed to the catch-up walk [INV-110] (the adopt path); the nonexistent build-pipeline adopt path is gone |
| F2 | INV-157 attributes all three legs to INV-155, but mute + reap are the INV-100 test-hygiene family; the reap leg specializes INV-100's spawned-process cleanup without citing it | recommendation · over-general (abstraction) | **folded** — INV-157 now cites INV-100 for the mute + reap hygiene legs (the machine left as found) and INV-155 only for the deadline leg, in both prose and index row |
| F3 | INV-157's per-command-deadline leg reads adjacent to INV-155's "no raised timeout that hides the race" ban; a cross-link would keep a future reader from mistaking one for a violation of the other | recommendation · boundary-issue (composition) | **folded** — INV-157's deadline sentence now carries the [INV-155] cross-link with an explicit "never license to inflate a timeout that would bury a real race" guard |

---

### F1 — INV-158 cites a home that neither exists nor is owed by this movement's plan

> "homes — this clause + the pack's shipped harness template + build-pipeline's adopt path" — PRODUCT_SPEC.md line 2006 (INV-158 index row)

Follow the citation. `build-pipeline/SKILL.md` contains no "adopt" content at all (grep over the pack:
"adopt" resolves only in `live-spec-base`). The consumer-adopts-by-updating mechanism INV-158
describes is owned elsewhere in the pack — the **catch-up walk [INV-110]** (PRODUCT_SPEC.md line 1267,
"brings an adopted host's documentation or records onto the current package" when the recorded version
is behind) and the **adoption feature** (F-adoption, line 44). Row 327's Done-when schedules the
template and test-author's rule but never a build-pipeline adopt path, so unlike the other two
forward homes this one is not a dependency the movement will close — it is a pointer that will not
discharge. A reader tracing INV-158 to learn HOW a consumer adopts the harness lands on a
build-pipeline that says nothing about adoption. This is the one-home / traceability break the pack
exists to forbid (same class as F1 in the 322/323 record: a citation that does not discharge).

Repoint the home to the mechanism that actually owns adoption: **the catch-up walk [INV-110] and the
adoption procedure** (`the consumer adopts by updating the pack` = a version-delta catch-up), not
build-pipeline. If build-pipeline is instead meant to grow a new adopt step this movement, add that
step to row 327's Done-when so the home is owed and closable — but the derivable answer is that
adoption is already homed at INV-110.

`defect · boundary-issue (composition)`

---

### F2 — INV-157 files its whole content under INV-155, but two of its three legs are INV-100's hygiene family

> "This is INV-155's boundary made concrete for the harness itself" — PRODUCT_SPEC.md line 653 (INV-157)

INV-157 has three legs: mute, reap the process group, bound each command with a deadline. Only the
deadline leg belongs to INV-155's family — a blanket timeout that "reads a slow machine as a failed
test" is a false-red / determinism concern, INV-155's own ground. The other two are the **test-hygiene
family owned by INV-100** (line 639 / index 1976): INV-100 already states every test "removes what it
creates — … spawned processes …" and "a suite run leaves the machine as it found it." Reaping the
browser's process group IS the spawned-process half of INV-100, specialized to the browser's
helper/renderer/gpu children; muting so a run "leaves the system volume alone" is the same
leaves-the-machine-as-it-found-it hygiene. INV-157 cites INV-100 nowhere, in neither prose nor index
row. The consequence is a soft one-home break: the reap fact now reads as if INV-155 fathered it, and
a reader auditing INV-100's spawned-process reach will not find the browser-harness specialization
that extends it.

Split the parentage the way INV-155 itself splits determinism from ledger-noise: cite **INV-100 as
the parent of the mute + reap hygiene half** (INV-157 specializing INV-100's spawned-process cleanup
to the browser's whole process group) and **INV-155 as the parent of the deadline / false-red half**.
Add `[INV-100]` to INV-157's prose and its index-row homes list.

`recommendation · over-general (abstraction)`

---

### F3 — INV-157's deadline leg should cross-link INV-155's raised-timeout ban it deliberately threads

> "bounds each command it sends the browser with a real per-command deadline, so a slow machine waits patiently while a genuine hang still fails with a clear bounded error" — PRODUCT_SPEC.md line 653 (INV-157)

INV-155 forbids "a raised timeout that hides the race." INV-157 requires a per-command deadline that
a slow machine "waits patiently" under. Read together these are compatible — INV-157 replaces a
blanket I/O timeout with a bounded per-command deadline that still fails a genuine hang, so it does
not raise a timeout to mask a flake — but the two clauses live 200 lines apart with no pointer
between them, and a future reader hardening the harness could read INV-157's "waits patiently" as
license to inflate the deadline, which is exactly INV-155's forbidden mask. Nothing is broken; a
cross-link removes the trap.

Add a clause to INV-157's deadline sentence naming the boundary: the per-command deadline is bounded
and still fails a genuine hang, distinct from INV-155's forbidden raised-timeout that hides a race —
with an `[INV-155]` pointer at that spot (INV-157 already cites INV-155 for the parent boundary, so
this only sharpens where the deadline leg sits inside it).

`recommendation · boundary-issue (composition)`

---

## Do both invariants hold as written?

**INV-157 — holds.** Its core ("launches muted + reaps the process group + per-command deadline; a
harness-caused fault is removable in owned code and root-fixed, not retried") is sound and consistent
with INV-155's boundary and INV-23's routing; "removable in owned code" carries the identical meaning
in both. Its two owed homes (harness template, test-author's rule) are dependencies row 327 will
close, not holes. F2/F3 sharpen its parentage but do not block.

**INV-158 — holds in substance, but one cited home does not discharge (F1).** The one-canonical-home
principle it states is correct and base rule 4 backs it. The blocker is the "build-pipeline's adopt
path" home, which neither exists nor is owed by the movement — repoint it to the catch-up walk
[INV-110] / adoption, or add the step to row 327. The template home it shares with INV-157 is
owed-this-movement, not a hole.
