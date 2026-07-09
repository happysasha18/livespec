# Prover record — pair-wave delta re-check (2026-07-10 night, third pass)

**Prover skill version:** product-prover **v0.1.15** (same lens set as tonight's full re-prove and postfold
delta; base skill referenced at v0.1.28). This is a delta-scoped re-check under the M-6 gate law: previous
records checked, the delta since them walked, a verdict — scaled to a small delta, not a fresh whole-spec pass.

**Mode:** delta-scoped (M-6 reach map for process). **Trigger:** PRODUCT_SPEC.md moved from **v0.16.16**
(proven in `docs/prover/2026-07-10-night-postfold.md`) to **v0.16.19** — three landings: the P1–P4 wording
folds, NEW INV-85 (engine/instance split at founding/orient), and NEW INV-86 + the F-pair pair-leading
scenario, plus the two new open decisions D-6/D-7. This pass walks only that delta and checks it composes.

**Previous records checked:**
- `2026-07-10-night-full-reprove.md` (v0.16.13, six findings F1–F6). Its F1/F2/F6 read FOLDED; F3/F4/F5 read
  QUEUE ROW. Out of this delta's scope; not re-opened.
- `2026-07-10-night-postfold.md` (v0.16.16, four findings P1–P4, verdict "safe to push v0.16.16"). P1 read
  QUEUE ROW 211, P2 QUEUE ROW 211, P3 QUEUE ROW 212, P4 QUEUE ROW 212. This pass confirms which of P1–P4 the
  three folds discharge, and checks the two new invariants + the F-pair scenario + D-6/D-7.

**Documents in view:** PRODUCT_SPEC.md v0.16.19 (whole doc read for seam context), the two prior records,
ARCHITECTURE.md not re-opened (this delta adds no shipped node; INV-85/86 are proposal + coordination law).

---

## The delta walked, point by point

### 1. The P1–P4 folds

- **P1 discharged.** Postfold P1 (freshly-created remote could read as capping the host at one question,
  skipping the grant question) asked for an explicit ordering: a host that creates its remote at the first
  push moment then gets the grant question in the same moment, no by-rule push until a grant is recorded.
  Landed INV-82 (line 704): "A host that just created its remote meets the grant question at that same first
  push moment: one question per gap, and the two questions never collapse into one." "One question per gap"
  kills the "one question total" misread; the standing grant precondition ("The rule runs inside the human's
  standing push grant … accepted work stays local") already blocks any by-rule push on the ungranted new
  remote. **P1 discharged.**
- **P2 discharged.** Postfold P2 (INV-83's "anything shown" overreaches its artifact-only script; chat's
  register gate undefined) asked for a reach sentence scoping the lint to rendered artifacts and routing chat
  to the hook + walk. Landed INV-83 (line 162): "The lint's reach is the shown artifact — a rendered page, a
  mockup, a decision page, a report artifact; a chat line stays under the hook's reminder and the walk's own
  read, and a mechanical gate for chat is its own queued work (queue row 203)." Exactly the demanded scope,
  mirroring INV-28's hook/script split. **P2 discharged.**
- **P3 discharged.** Postfold P3 (INV-84's "reports" scope collides with INV-34/INV-35 report authorship and
  the tight-rung economy) asked to scope "reports" to rendered/standalone reader documents and keep the
  routine chat report with the rules-loaded session. Landed INV-84 (line 668): "A report typed live in chat
  stays the session's own words under the register laws; the clean road binds the durable prose a human
  returns to — pages, documents, product copy, rendered report artifacts." The chat report is carved out; the
  clean road binds rendered report artifacts only. **P3 discharged.**
- **P4 partially discharged (see PW-2).** Postfold P4 (settled-text trigger "an edit opens that page" leaves
  the redraft unit undefined) asked for two things: (a) the unit = the passage the edit changes, not the whole
  page; (b) a non-prose mechanical fix (typo, link, identifier, version pin) is not a redraft and stays with
  the editing session. Landed INV-84 discharges (a): "the unit is the section the edit touches, and a whole
  page is redrafted only on the human's word." It does NOT discharge (b): the mechanical-fix carve-out is
  absent, and the exact phrase P4 flagged — "or an edit opens that page anyway" — survives verbatim and still
  says "page," in tension with the new "section" unit. Recorded as **PW-2**.

### 2. NEW INV-85 (engine/instance split proposal at founding/orient)

Read INV-85 body (line 1041) and index row (line 1644) against B-2, INV-36, INV-79, INV-75, the settings ladder.

- **Against B-2 (personal-vs-reusable) — clean.** The split fires only as a conditional follow-on to the
  reusable answer landing on a content-carrying product; "the agent proposes; the human's word decides; both
  outcomes are recorded [B-2]"; the never-derive-from-examples arm (line 1025) is respected. No finding.
- **Against INV-36 and the "three intake verdicts never collapse" clause — no structural break, one counting
  seam (PW-1).** The three intake verdicts (line 1045: project-kind, wish work-kind, placement) are per-wish
  verdicts that "share the intake breath." INV-85's split is a **founding** question, not an intake verdict —
  it is NOT added to that closed list, so "Three verdicts … never collapse into one" is untouched. The
  answer to the delta question is: a fourth breath does **not** break the three-intake-verdicts wording.
  BUT the delta introduces a counting inconsistency across the founding-question framing — see PW-1.
- **Against INV-79 (content contract) — clean.** Engine "carrying a content contract that names every place a
  concrete instance plugs in [INV-79]"; "A donor-specific constant found while carving becomes a named
  content-contract entry with a works-without-it test [INV-79]." Faithful to INV-79's two-halves law. No finding.
- **Against INV-75 (heavy binaries) — clean.** Instance home carries "the private fragments, with heavy binary
  content placed per the placement view's prompt [INV-75]." Consistent. No finding.
- **Settings-ladder home for the reuse note — named, but no field handle (PW-5).** On decline, "the agent
  records a one-line reuse note in the host profile." Home named (host profile = the ladder's host scope
  [E-13]), satisfying one-home-per-fact. Unlike `project.kind` and `work-kind.host-default`, the note carries
  no field handle to grep it back later. Recorded as **PW-5** (worth-considering).

### 3. NEW INV-86 + the F-pair scenario (Running an engine and its instance as a pair)

Read INV-86 body (line 1143), the regression fence (1141), the load-bearing walk (1145), non-goals (1147),
and index row (1645) against E-1, E-14, E-11/INV-10/T-10, INV-11, T-17/INV-1, INV-56, INV-37, the one-window law.

- **Against E-1 (host) — clean.** Each repo "carry their own spec, queue, journal, and `.live-spec/` folder
  [E-1]"; E-1 = "host project + its `.live-spec/`". Each half is a full host, the pack attaches per-repo. No finding.
- **Against E-14 (no third document) — clean, and D-6-safe.** "No third document spans the pair; the
  no-third-document law holds across the seam." A future D-6 stitched reading view stays E-14-legal because
  D-6 fixes "the queues stay per-repo either way" — the view would be a derived lens, not a third source
  document. No finding.
- **Against E-11 / INV-10 / T-10 (inbox door, write-ownership, sweep-first) — clean law, one wording seam
  (PW-4).** The lesson-travel channel reuses the inbox door under write-ownership, sweep-first [T-10]; the
  cited laws hold. But sentence 7 of line 1143 says "the learning window files one new inbox file into the
  other repo … nothing in a lesson's travel ever writes a foreign repo" — a within-sentence tension (the
  inbox drop IS a sanctioned write into the foreign repo), reconciled only two sentences later by "save for
  that one inbox file." Recorded as **PW-4** (worth-considering).
- **Against INV-11 (fence) — clean.** "the concurrent-edit fence still binds inside each repo [INV-11]." No finding.
- **Against T-17 / INV-1 (split wishes) — clean.** A both-shaped wish is "two wishes, split at intake, one row
  in each queue, each citing the one spoken wish [T-17, INV-1]"; one-story-one-row holds across the seam. No finding.
- **Against INV-56 (parked debt) — clean.** The instance "parks its own half as a dated blocked-on-engine debt
  line, so the lane keeps moving [E-11, INV-10, INV-56]." Consistent with the limp-never-dams law. No finding.
- **Against INV-37 (the map echo) — engine-half placement covered by the universal law.** The walk narrates
  the instance-side placement explicitly ("Intake places it on the instance's map"); the engine-half is filed
  as an engine inbox wish and "lands … through the full pipeline," whose intake runs INV-37 and places it on
  the **engine's** map. INV-37 binds every intake, so the engine-half placement is defined by the general law
  though not restated symmetrically in the walk. Covered — no finding.
- **Against the one-window bootstrap law — clean.** "One window serves one repo of the pair; unsure means ask,
  never infer; a window is read-only on the pair's other half save for that one inbox file [INV-10]." Matches
  the CLAUDE.md bootstrap verbatim in intent. No finding.
- **Entry / exit stated — yes.** Entry (line 1145): "the human throws a wish at the instance window." Exit:
  "the visitor filters this gallery; the next instance inherits the feature with no engine work; both journals
  hold their half, and the spoken wish traces to both rows [INV-1]." Both present.
- **Deadlock / liveness net (PW-3).** No circular wait: the instance waits on the engine; the engine waits on
  nothing but a session opening. The failure mode is "instance parked, engine window never opened" — a stall,
  not a deadlock. A liveness net **exists** via general law: the debt line is **dated**, and the instance's
  status report [INV-27] names each in-flight feature's station every report, so a never-opened engine
  surfaces as an **aging** blocked-on-engine station the human sees each report. But the F-pair section does
  not name this net, so a reader can read the parked row as waiting silently. Recorded as **PW-3**
  (worth-considering) — the net is real, just unstated.

### 4. The two new open decisions D-6 / D-7

- **D-6 (pair queues: stitched view or strictly two) — truly open.** No clause silently assumes the
  stitched-view answer: INV-86 describes two per-repo queues, which is the "queues stay per-repo either way"
  invariant D-6 holds across both outcomes, not the open half. Genuinely open; default (two plain queues) is
  the safe pick. No finding.
- **D-7 (pair specs: instance cites engine facts, or only the contract) — open, its recommended answer
  consumed but explicitly tagged.** INV-86 body ("cites the engine only by its contract entries' handles
  (D-7)") and index row both adopt D-7's recommended answer AND tag `(D-7)` at the point of use. That is the
  sanctioned `[default]`-tag pattern, not a silent assumption: if D-7 flips, the tagged dependents are
  findable. Genuinely open, dependency traceable. No finding.

---

## Findings

Delta-scoped. P1/P2/P3 of the prior record are confirmed discharged (above); P4 is partially discharged
(PW-2). The five rows below are new or residual seams in this delta. Disposition left for the senior.

| # | Finding | Lines | Severity | Disposition |
|---|---|---|---|---|
| PW-1 | Founding shaping-questions counted inconsistently — split is "one more" (1041) yet "a fourth breath" (1141); project.kind is "a second shaping question" (1043); "breath" names both the three-verdict intake group (1045) and the split (1141) | 1041, 1043, 1045, 1141 | should-clarify · internal-conflict (consistency) | FOLDED same pass (fences now say "its own founding question", the intake three stay closed) |
| PW-2 | INV-84's P4 fold is partial — the section-unit landed, but the mechanical-fix carve-out is absent and "or an edit opens that page anyway" still says "page" | 668 | should-clarify · missing-prerequisite (precondition) | FOLDED same pass (section-unit finished + the mechanical-correction carve-out added to INV-84) |
| PW-3 | F-pair liveness net (dated debt surfaced by the instance's status report [INV-27]) is real but unnamed in the scenario; a reader can read the parked row as silently waiting | 1145 | worth-considering · stuck-state (liveness) | QUEUE ROW 213 |
| PW-4 | INV-86 line 1143 sentence 7: "files one new inbox file into the other repo … nothing ever writes a foreign repo" is a within-sentence tension, reconciled only two sentences later | 1143 | worth-considering · boundary-issue (composition) | QUEUE ROW 213 |
| PW-5 | INV-85's decline record ("a one-line reuse note in the host profile") has a named home but no field handle, unlike project.kind / work-kind.host-default | 1041, 1644 | worth-considering · hard-to-operate (ops-ux) | QUEUE ROW 213 |

---

**PW-1 — The founding shaping-questions are counted three different ways, and "breath" now names two different groupings.**

> "founding asks one more shaping question: is the generic mechanism worth its own home" — Founding / [INV-85]

> "founding asks a second shaping question: what is this project" — Founding (project.kind)

> "Three verdicts share the intake breath, and they never collapse into one" — Founding (line 1045)

> "the split ask is a fourth breath that fires only when reusable lands on a content-carrying product" — Running an engine and its instance as a pair / [INV-86 regression fence]

Structurally nothing breaks: the three intake verdicts (project-kind, work-kind, placement) stay a closed
three, and the split is a founding question, not a fourth intake verdict — so the delta question "does a
fourth breath break the three-intake-verdicts wording?" answers **no**. But a reader trying to count the
founding questions gets contradictory ordinals: project.kind is "a second shaping question," the split is
"one more shaping question" (reads as the second too, and it is documented physically before project.kind)
yet also "a fourth breath." And "breath" is used both for the three intake verdicts that "share the intake
breath" and for the split as "a fourth breath," inviting a reader to miscount the split as a fourth item in
the closed three-verdict list. A reader onboarding to founding cannot say from the text how many founding
questions there are or which ordinal the split holds.

Pick one counting frame and make the ordinals agree: state the founding questions as an explicit short list
(personal-vs-reusable · project.kind · economy rung · the conditional split), give the split one ordinal, and
reserve "breath" for one grouping — e.g. keep "the intake breath" for the three intake verdicts and reword the
split's "fourth breath" to "a further, conditional founding question," so the two metaphors stop colliding.

`should-clarify · internal-conflict (consistency)`

---

**PW-2 — INV-84's settled-text fold defined the unit but dropped the mechanical-fix carve-out, and left the old "page" trigger in tension with the new "section" unit.**

> "the unit is the section the edit touches, and a whole page is redrafted only on the human's word … Settled text stays as it is until a human rejects a specific page or an edit opens that page anyway" — Rhythm / [INV-84]

P4 asked for two things; only the first landed. The unit is now the section (good — the whole-page-onto-the-road
concern is cut). But the mechanical-fix carve-out is absent: a typo, a link, an identifier, or a version-pin
bump inside a settled prose section is "text currently being edited," so by the letter that section is pulled
onto the clean-writer road and owes a fresh-writer redraft for a change that alters no prose — an unbudgeted
session cost, now section-scoped rather than page-scoped. And the exact phrase P4 flagged — "or an edit opens
that page anyway" — survives and still says "page," in tension with "the unit is the section the edit touches."
Blast radius is low (a sensible agent reads "durable prose" and won't spin a writer for a version bump), but
the letter still admits it.

Add the carve-out P4 named: an edit pulls only the passage it changes onto the road; a non-prose mechanical fix
(typo, link, identifier, version pin) is not a prose redraft and stays with the editing session. Reword "an
edit opens that page anyway" to "an edit opens that section anyway" so the trigger's unit matches the stated unit.

`should-clarify · missing-prerequisite (precondition)`

---

**PW-3 — The F-pair scenario's liveness net exists in general law but is not named in the scenario, so a never-opened engine reads as a silent stall.**

> "parks its own half as a dated blocked-on-engine debt line, so the lane keeps moving [E-11, INV-10, INV-56]" — Running an engine and its instance as a pair (the walk)

The scenario cannot deadlock — the wait is not circular (the instance waits on the engine; the engine waits
only on a session opening). The single stall is "the human never opens the engine window," which leaves the
parked instance feature blocked. A net does exist: the debt line is dated, and the instance's status report
[INV-27] names each in-flight feature's pipeline station at every report, so a never-swept engine surfaces as
an **aging** blocked-on-engine station the human sees each time. But the F-pair section leans on INV-56 alone
and never names this visibility net, so a reader takes the parked row to wait silently, and an aging cross-repo
block can read as "fine, parked" rather than "the human still needs to open the engine."

Add one clause to the walk: the dated blocked-on-engine debt appears in the instance's status report [INV-27]
every report until the engine ships, so a never-opened engine surfaces as an aging block the human is reminded
of, not a silent stall.

`worth-considering · stuck-state (liveness)`

---

**PW-4 — INV-86 says the lesson channel "writes one inbox file into the other repo" and, in the same sentence, that "nothing ever writes a foreign repo."**

> "the learning window files one new inbox file into the other repo and journals the hand-off in its own tree; nothing in a lesson's travel ever writes a foreign repo [E-11, INV-10, T-10]" — Running an engine and its instance as a pair / [INV-86]

Filing a committed inbox file into the other repo IS a write into that repo — the one sanctioned write the
inbox door [E-11] allows. Sentence 7 states the write and then denies any write in the same breath; the intent
("nothing beyond that one inbox file writes the foreign repo's own content") is recoverable only two sentences
later, from "a window is read-only on the pair's other half save for that one inbox file." A careful reader
reconciles it against E-11/INV-10; a literal reader hits a contradiction.

Tighten sentence 7 to "nothing in a lesson's travel writes a foreign repo beyond that one inbox file," so the
sanctioned-door carve-out sits inside the sentence that raises the tension.

`worth-considering · boundary-issue (composition)`

---

**PW-5 — INV-85's decline record has a named home but no field handle, so a later session cannot grep the reuse decision back.**

> "when the human declines the split, the agent records a one-line reuse note in the host profile and raises the offer again only when the product outgrows one home" — Founding / [INV-85]

The reuse note's home is named (the host profile — the settings ladder's host scope), satisfying one-home-per-fact.
But unlike `project.kind` and `work-kind.host-default`, which carry field handles, the reuse note is "a one-line
note" with no key. The re-raise trigger ("a second instance appears, or the content and the mechanism start
fighting for the same file") is a judgment call, so no machine reads the note — but a later session wanting to
confirm "was the split already offered and declined here?" has no handle to search and may re-raise the offer
mid-work, which INV-85 means to gate to setup + real-outgrowth moments only.

Give the note a field handle in the host profile (e.g. `reuse.split-declined: <date>`), so the decline is
greppable and the re-raise gate has a stored fact to check.

`worth-considering · hard-to-operate (ops-ux)`

---

## What was probed and found sound

- **P1, P2, P3 folds** land exactly as the postfold record's actions demanded: "one question per gap" (P1),
  the artifact-vs-chat reach sentence (P2), the chat-report vs durable-prose split (P3). P4 is partial (PW-2).
- **INV-85 against B-2, INV-79, INV-75** composes cleanly; the split is correctly a conditional founding
  proposal (reusable + content-carrying), never imposed, both outcomes recorded, and it does **not** add a
  fourth item to the closed three-intake-verdicts list.
- **INV-86 / F-pair against E-1, E-14, INV-11, T-17/INV-1, INV-56, INV-37, and the one-window law** composes
  cleanly; the cross-seam channel reuses the inbox door / write-ownership / fence without redefining them; the
  engine-half map placement is covered by INV-37's universal binding; entry and exit are stated; the scenario
  cannot deadlock, and a real (if unnamed) liveness net exists (PW-3).
- **D-6 and D-7 are genuinely open.** No clause silently assumes D-6's stitched-view answer; INV-86 consumes
  D-7's recommended answer but explicitly tags `(D-7)` at every point of use, the sanctioned pattern for a
  recommended-but-open decision.
- **Anchor citations spot-checked** (E-1, E-3, E-11, T-10, INV-9, INV-10, INV-15, INV-44, INV-70, B-3) resolve
  to their index homes; INV-85/86 both resolve to a home section (Bootstrap) and an index row; no orphan or
  double-owner spotted by read.

## Gate

Five findings, none a prose regression, **zero must-fix**. Two should-clarify are wording/consistency seams
(PW-1 founding-question counting, PW-2 the P4 mechanical-fix residual); three worth-considering are a stated
liveness net (PW-3), a within-sentence write tension (PW-4), and a missing field handle (PW-5). None
authorizes an outward or irreversible act, none breaks a load-bearing rule, none regresses settled prose. The
three folds discharge P1/P2/P3 and the structural half of P4; INV-85, INV-86, the F-pair scenario, and D-6/D-7
compose soundly. All five rows can ride as queue rows.

**Verdict: safe to push v0.16.19.**
