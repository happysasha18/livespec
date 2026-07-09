# Prover record — post-fold delta re-check (2026-07-10 night, second pass)

**Prover skill version:** product-prover **v0.1.15** (same lens set as tonight's full re-prove; base skill
referenced at v0.1.27). This is the delta-scoped push-gate re-check mandated by M-6: previous records
checked, the delta since them walked, a verdict — scaled to a small post-fold delta, not a fresh whole-spec
pass.

**Mode:** delta-scoped (M-6 reach map for process). **Trigger:** PRODUCT_SPEC.md moved from v0.16.13
(proven end-to-end in `docs/prover/2026-07-10-night-full-reprove.md`) to **v0.16.16**. The full record's F1,
F2, and F6 folds are now landed as text, and two new invariants (INV-83, INV-84) plus the tight-rung reword
arrived. This pass walks only that delta and checks it composes.

**Previous records checked:** `2026-07-10-night-full-reprove.md` (v0.16.13, six findings). Its F1/F2/F6
dispositions read "FOLDED … spec v0.16.14"; F3/F4/F5 read "QUEUE ROW". This pass confirms the three folds
landed as the actions demanded and that no unfolded row was silently dropped (F3/F4/F5 remain queue rows,
out of this delta's scope).

**Documents in view:** PRODUCT_SPEC.md v0.16.16 (whole doc read for seam context), the full re-prove record.

---

## The delta walked, point by point

### 1. The INV-82 folds as landed (F1 grant precondition, F2 peer fence, amended index row)

Read the landed INV-82 body (line 704) and its index row (line 1623) against the full record's F1 and F2
actions.

- **F1 discharge — confirmed.** F1 asked for the grant as an explicit precondition: "by rule" fires only
  where the profile records the INV-70/INV-9 grant; absent it, accepted work stays local and the first-push
  question is the grant question. Landed text: "The rule runs inside the human's standing push grant
  [INV-70, INV-9]: on a host whose remote exists but whose profile records no such grant, accepted work
  stays local, and the first push moment asks one contextual question — push on the agent's certification
  from here on, or hold each push for the human's word — recorded in the host profile." This is exactly the
  demanded fold. F1 discharged.
- **F2 discharge — confirmed.** F2 asked for a clause suppressing the by-rule push while a peer session is
  known live, returning coordination to the human per INV-11, with INV-11 cross-linked. Landed text: "while
  another session is known live in the repo, the by-rule push stands down: push coordination returns to the
  human [INV-11], and the accepted work waits local until the repo is single-session again." Cross-link
  present. F2 discharged.
- **No collision with the surviving clauses.** The three stay-local / wait conditions (no grant · peer live
  · human-named milestone) stack cleanly — each is an independent suppressor, none contradicts another. The
  README re-walk clause is downstream of an actual push, so a suppressed push simply skips it; no conflict.
  The named-milestone carve-out ("still waits for that word") is preserved verbatim. Index row 1623 faithfully
  mirrors the body. Live-spec's own repo is a granted host (line 406, "live-spec's own already does [M-6]"),
  so the grant precondition does not contradict M-6's every-push cadence for the flagship.
- **One residual seam (P1 below):** the create-remote path and the grant question can both fall at "the
  first push moment," and the phrase "Only a host with NO remote gets one question" invites a reading that
  caps that host at one question total — which would let a freshly-created remote auto-push before the grant
  question is asked.

### 2. NEW INV-83 (pre-show register lint) — composed against INV-28, INV-34, INV-27, INV-35, reach map

Read INV-83 body (line 162) and index row (line 1624).

- **Against INV-28's advisory arm — clean.** INV-83 states its own difference explicitly: `preshow-lint.py`
  [INV-28] "warns on a leading handle" (advisory), while `preshow-register-lint.py` "stands the showing
  down" (block). The block-vs-warn distinction is well-drawn and non-conflicting; the two arms live side by
  side in communicator's pre-show walk.
- **Clean-reader residual — clearly out of scope.** "The residual beyond patterns … belongs to the
  clean-reader check … The lint is the floor; the clean-reader check is the ceiling." The boundary between
  the pattern lint and the clean-reader ceiling is explicit. No finding.
- **Grows-by-one duty — enforceable enough.** A leak past the lint is caught by the clean-reader ceiling and
  folded same-day as a new pattern with source + date. The catch has an owner (the clean-reader check), so
  the duty closes rather than floating. No finding.
- **"A red blocks the showing" for every shown-surface kind — one gap (P2 below).** The opener says
  "Anything shown to a human," but the mechanism is a script that reads a rendered surface's text, and the
  enumerated kinds are all file/artifact surfaces (rendered page, mockup, decision page, report artifact). A
  chat report or a narration line [INV-35] is shown to the human yet is never written to a file the script
  reads (chat cannot be machine-gated). For the chat-surface kind, "a red blocks the showing" is
  mechanically undefined — its register duty rides INV-34's walk and the chat-law hook, not this script,
  and INV-83 does not say so. This is the same split INV-28 already draws (hook for chat, script for
  artifacts); INV-83 should mirror it.
- **Against the reach map [INV-45] — orthogonal, no collision.** INV-83 is a showing-time gate, not a
  push-time gate; like INV-28's arm it sits outside the push reach-map by design. No conflict.

### 3. NEW INV-84 (human-facing prose drafted by a clean writer) — composed against ACT-2/ACT-3, INV-83, the tight rung, the settled-text boundary

Read INV-84 body (line 668) and index row (line 1625).

- **Against the delegation contract (ACT-2/ACT-3) — clean.** The clean writer is a fresh briefed worker;
  ACT-3's brief carries the ledger walk and clock, while INV-84's brief carries facts, reader, and register
  laws. "Not loading the pack skills" (so the voice stays unmarinated) and "receiving a task brief" are not
  in tension — the register laws arrive via the brief, not as loaded pack files. ACT-2's ownership of
  judgment is untouched (the rules-loaded senior reviews and lands). No finding.
- **Against INV-83 — complementary.** Draft clean (INV-84) → senior reviews and lands → register lint before
  showing (INV-83). A clean-drafted text is the least likely to carry machine dialect, so the two reinforce
  rather than collide. No finding.
- **Does the drafting road survive lean/tight budgets, and against INV-34/INV-35 — one seam (P3 below).**
  INV-84's covers-list names "reports." INV-34 already assigns the movement-end/milestone report to the
  rules-loaded session, which drafts it and walks it phrase-by-phrase; INV-35's narration is likewise a
  rules-loaded chat line. INV-84 read literally says those reports are drafted by a separate fresh writer
  session — a second model of who writes a report, and, for frequent small chat reports under the tight
  rung's economy [T-19], a heavy per-report fixed cost the rung does not carve out. Which session drafts a
  movement-end report is left double-answered.
- **Settled-text boundary — imprecise (P4 below).** "The rule binds new text and any text that is currently
  being edited … settled text walks the road when … an edit opens that page anyway." The unit is unstated:
  does a one-line touch (a typo, a link, a version pin) to a settled page make the whole page "being
  edited" and owe a clean-writer redraft? Read literally, any edit that opens a settled page pulls it onto
  the road — re-admitting through the back door the blanket rewrite the same sentence refuses at the front.

### 4. The reach-scoped tight-rung reword (line 1371) — against INV-45 and M-6

F6 asked line 1365 to reword to "the reach-scoped gate green at HEAD per INV-45." Landed at line 1371:
"Even so, a push still requires the batch's reach-scoped gate [INV-45] green at HEAD [M-6]." This scopes
the tight-batch push to the batch's reach exactly as INV-45's reach map defines and as M-6's push gate
requires; a prose-only tight-rung batch no longer appears to be forced through the whole suite. F6
discharged, consistent with both anchors, no new collision. No finding.

---

## Findings

Delta-scoped. F1/F2/F6 of the prior record are confirmed discharged (above) and are not re-listed as open.
The four rows below are new seams introduced or left open by the delta. Disposition left for the senior.

| # | Finding | Lines | Severity | Disposition |
|---|---|---|---|---|
| P1 | Create-remote path can read as capping the host at one question, skipping the grant question | 704, 1623 | worth-considering · undefined-path (transitions) | QUEUE ROW 211 |
| P2 | INV-83's "anything shown" overreaches its artifact-only script; chat surfaces' register gate undefined | 162, 1624 | should-clarify · boundary-issue (composition) | QUEUE ROW 211 |
| P3 | INV-84's "reports" scope collides with INV-34/INV-35 report authorship and the tight-rung economy | 668, 1625 | should-clarify · boundary-issue (composition) | QUEUE ROW 212 |
| P4 | INV-84's settled-text trigger ("an edit opens that page") leaves the redraft unit undefined | 668, 1625 | should-clarify · missing-prerequisite (precondition) | QUEUE ROW 212 |

---

**P1 — A freshly created remote could read as auto-pushing before the grant question is asked.**

> "Only a host with NO remote gets one question, contextually, at the first push moment: create one (and where), or stay local … on a host whose remote exists but whose profile records no such grant, accepted work stays local, and the first push moment asks one contextual question — the grant question" — Push and CI gates [INV-82]

A newly attached host has neither a remote nor a grant. At its first push moment it gets the create-or-stay-local question; if the human says "create it," the host now has a remote and still no grant. The grant clause frames the grant as a standing precondition, so the by-rule push cannot fire without it — but the phrase "gets ONE question" invites a reader to cap the no-remote host at a single question total and let the by-rule push fire on the freshly created remote, skipping the grant question and pushing on the agent's certification the human never gave. The blast radius is narrow (only a brand-new host that creates its remote at first push), and the precondition framing already protects the intent; the wording is what admits the misread.

State the ordering: a host that creates its remote at the first push moment then gets the grant question in the same moment (two questions can co-occur), and no by-rule push fires on the newly created remote until a grant is recorded.

`worth-considering · undefined-path (transitions)`

---

**P2 — INV-83 promises the register block for "anything shown," but its script can only gate rendered surfaces; chat's register gate is left unnamed.**

> "Anything shown to a human passes a register lint before it is shown … `scripts/preshow-register-lint.py` reads its text … A red result blocks the showing." — Showing work [INV-83]

The mechanism reads a rendered surface's text and blocks the show; the enumerated kinds are all file/artifact surfaces. A chat movement-end report or a narration line [INV-35] is shown to the human yet is never written to a file the script reads before it is sent (chat cannot be machine-gated on this harness). For the chat-surface kind, "a red blocks the showing" describes a block no script can perform, so a reader takes the register block to cover chat lines when mechanically it cannot. INV-28 already draws exactly this split — the chat-law hook reminds chat, `preshow-lint.py` gates artifacts — and INV-83 should inherit it.

State the scope: `preshow-register-lint.py` gates surfaces rendered to a file before showing; chat lines carry their register duty through INV-34's walk and the chat-law hook, not this script. One added sentence in INV-83 and its index row.

`should-clarify · boundary-issue (composition)`

---

**P3 — INV-84 says a fresh writer drafts "reports," but INV-34/INV-35 already assign the report to the rules-loaded session, and the tight rung carves no exception.**

> "This covers documentation pages, product-spec prose, reports, decision pages, product copy … drafted by a fresh writer session that does not have the package rules loaded." — Rhythm [INV-84]

> "Before any movement-end or milestone report reaches the human, the agent re-reads the communicator rules and passes the draft phrase by phrase …" — Showing work [INV-34]

INV-34 has the rules-loaded session draft its own report and walk it; INV-35's narration is likewise a rules-loaded chat line. INV-84 read literally reassigns "reports" to a separate fresh writer session, so a movement-end report has two conflicting authors, and under the tight rung's economy [T-19] a fresh session per frequent small report is an unbudgeted fixed cost the rung does not exempt. An agent following the letter would either spin a clean writer for every chat report (heavy, and against INV-34's model) or ignore INV-84 for reports (leaving its "reports" scope dead).

Scope INV-84's "reports" to rendered/standalone reader documents (decision pages, published reports, docs, spec prose), and state that the routine chat movement-end/milestone report stays with the rules-loaded session under INV-34's walk — the clean-writer road scaling to the delta like the rest of the economy ladder.

`should-clarify · boundary-issue (composition)`

---

**P4 — INV-84's settled-text trigger pulls a whole page onto the clean-writer road on any edit, re-admitting the blanket rewrite it means to refuse.**

> "The rule binds new text and any text that is currently being edited … Settled text stays as it is until a human rejects a specific page or an edit opens that page anyway; the package refuses a blanket rewrite of settled text …" — Rhythm [INV-84]

The unit is unstated. A one-line touch to a settled page — a typo fix, a link, a version-pin bump — "opens that page," so by the letter the whole settled page becomes "being edited" and owes a clean-writer redraft. That is the very blanket rewrite the next clause refuses, now entering through the edit door one page at a time, and it forces a fresh writer session for a mechanical fix that changes no prose.

State the unit: an edit pulls only the passage it changes onto the clean-writer road, not the whole settled page, and a non-prose mechanical fix (typo, link, identifier, version pin) is not a prose redraft and stays with the editing session.

`should-clarify · missing-prerequisite (precondition)`

---

## What was probed and found sound

- The F1 grant precondition and F2 peer fence landed as the full record's actions demanded, with INV-11
  cross-linked and the named-milestone / README-re-walk clauses preserved; the three stay-local conditions
  stack without collision.
- INV-83's block-vs-advisory split against INV-28, its clean-reader ceiling, and its orthogonality to the
  push reach-map all compose cleanly; only the chat-surface scope (P2) is underdrawn.
- INV-84 against ACT-2/ACT-3 (brief carries the register laws; the unmarinated writer is still a briefed
  worker; the senior still reviews and lands) and against INV-83 (draft-clean then lint-before-show) compose
  cleanly; the seams are the "reports" scope (P3) and the settled-text unit (P4), both wording, not
  structure.
- The tight-rung reword (line 1371) inherits INV-45's reach map rather than overriding it; F6 discharged.

## Gate

Four findings, all new seams in the delta, none a prose regression. Zero must-fix: the two folds that the
full record flagged as blockers (F1 unauthorized push, F2 concurrent-session conflict) are confirmed
discharged in the landed text, and F6's wording nit is fixed. The four new rows are three should-clarify and
one worth-considering — bounded wording seams that can ride as queue rows; none authorizes an outward act,
contradicts a load-bearing rule, or regresses the prose.

**Verdict: safe to push v0.16.16.**
