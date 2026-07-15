# Prover record — feedback-collector (the pack's third arrow)

- **Prover skill version:** product-prover, live-spec pack, base `live-spec-base v1.0.17`
- **Mode:** CROSS-LINK — new surface `feedback-collector` (E-30 / T-21 / INV-161) against its named seams
- **Date:** 2026-07-15 (row 321)
- **Delta under review:** PRODUCT_SPEC.md lines 924–928 (subsection inside "Sending feedback in", between the feedback-intake paragraph [T-20, l.922] and "The section's edges, stated once" [l.930]); Formal-index rows E-30 (l.1948), T-21 (l.1950), INV-161 (l.2021)
- **Seams proven against:** feedback-intake (E-28 / T-20 / INV-68), silence-is-consent (INV-31), human's gate (base rule 17 / ACT-1, INV-9, INV-94), settings ladder + design-sync flag (E-13 / E-18 / INV-14 / INV-87), measurement family (INV-21, row 48), the two "digest" meanings (INV-35, INV-48)
- **Scope note:** review only, no spec edit. Blocking set is delta-scoped [INV-114].

## Triage

PROCEED — a stateful outbound surface with a trigger, a consent gate, an off-by-default flag, and a deposit home; enough to extract a model and prove its seams.

## Opening assessment

The delta adds a third arrow to the exchange: on a rare strong reaction the pack offers to send its authors a distilled, non-public "upstream note", deposited (not auto-sent) into `outbox/`, gated on the human's explicit yes, off by default. Three seams are handled genuinely well — the consent reversal from silence-is-consent is stated as a **deliberate** opposite with its rationale (not a silent contradiction), the new name is fenced explicitly away from both existing "digest" meanings, and the measurement-family boundary is drawn and repeated. The design needs another iteration on three delta-scoped defects: `outbox/` is a brand-new persistent home introduced with no location, naming/collision law, commit/privacy rule, or lifecycle; the claim that the collector and feedback-intake "never overlap" is false for the common case of a strong reaction that the human *hands in* (it is both field evidence under T-20 and a collector trigger), and the spec never says who owns that both-case; and "never fires on the authors' own origin machine" is asserted as a separate guarantee with no mechanism behind it but the off flag. All three fixes are local. Overall: needs another iteration.

## Findings

| id | headline | kind | blocking | folded / rejected |
|---|---|---|---|---|
| F1 | `outbox/` is an undeclared new home | defect · boundary-issue (composition) | blocking | |
| F2 | "never overlap" with feedback-intake is false; both-case unowned | defect · internal-conflict (consistency) | blocking | |
| F3 | "never on the origin machine" has no mechanism but the off flag | defect · unenforceable-promise (discharge) | blocking (small) | |
| F4 | `INV-94` mis-cited for the human's gate | defect · direct-contradiction (contradiction) | blocking (trivial) | |
| F5 | offer-record has no stated line shape in FEEDBACK.md | defect · boundary-issue (composition) | blocking (small) | |
| F6 | `feedback-upstream` flag not landed in the one settings catalog | recommendation | no | |
| F7 | no owning node / matrix rows yet for E-30 / T-21 / INV-161 | recommendation | no | |
| F8 | birth-fences list omits the collector's new fences | recommendation | no | |

---

### F1 — `outbox/` is a new persistent home introduced with none of a home's law

> "The pack DEPOSITS the note into the host's `outbox/` … The pack's side ends at a deposited, private, self-contained note." — l.926, T-21

`outbox/` appears nowhere else in the spec. Its inbound twin `inbox/` carries a full law: a naming-and-collision rule [E-11], a one-file-per-item discipline, a sweep [T-10], and a monitor [INV-147]. `outbox/` is declared with none of: where it lives (host root, like `inbox/`?), the naming/collision law when two notes are deposited, whether it is committed or git-ignored, and who clears it after the human sends. The privacy stakes make the commit question load-bearing: a note that is "non-public" but deposited into a tracked directory rides the next push, and the shipped-language machine [INV-120] checks Cyrillic and owner-names but not a note's user-derived content — so a distilled note about a real person can leak through a publish the delta never fenced.

Declare `outbox/` as a home the way `inbox/` is declared: its location at the host root, a one-note-per-deposit naming/collision rule, a stated git posture (recommend git-ignored by default, since the human's separate send is out-of-band and the content is user-derived), and a clear-after-send lifecycle owner. Add the outbox to the publish gate's privacy check or state its exemption by name.

`defect · boundary-issue (composition)`

---

### F2 — "The two never overlap" is false for a handed-in strong reaction, and the both-case is unowned

> "This is the inverse of feedback-intake's arrow — feedback-intake stays quiet on the agent's own observation [T-20], and this arm IS exactly that observation, so the two never overlap" — l.924, E-30

The disjointness is argued on one axis (source of the signal) but breaks on the most common case. feedback-intake's fifth quiet case is "something the human merely mentions without handing it in" — there the collector fires alone, cleanly disjoint. But when the human *hands in* a strong reaction to a shipped feature ("this is the best tool I've used"), T-20 routes it to **field evidence** — a real route, a real FEEDBACK.md line [INV-68, l.909] — **and** it is exactly the "genuinely strong reaction" the collector fires on. So one moment triggers both arms. The spec's "never overlap" is therefore false, and it never states who owns the both-case: does intake log the field-evidence line while the collector independently offers the upstream note? A downstream author reading "never overlap" will build one arm to suppress the other and drop either the ledger line or the offer.

Replace the "never overlap" claim with the true composition: a strong reaction the human hands in is logged by feedback-intake as field evidence **and** may trigger the collector's offer — the two do disjoint *work* (one records locally, one offers to carry a note up) on the same moment, rather than never co-firing. State that both fire and neither suppresses the other.

`defect · internal-conflict (consistency)`

---

### F3 — "Never fires on the authors' own origin machine" is a separate guarantee with no separate mechanism

> "the arm … never fires on the authors' own origin machine." (the measure, l.928) — and l.926's "the authors' own origin machine leaves it off, having no upstream above it"

INV-161's measure lists "honours the off-by-default flag" **and** "never fires on the authors' own origin machine" as two clauses, implying two guarantees. But the only mechanism the delta gives for the second is the first: the origin machine "leaves it off". There is no defined way to detect "this is the authors' origin machine" independent of the flag's value. So if the flag is ever flipped on there — by a test, a copy-paste of a downstream profile, a mistake — the stated guarantee "never on origin machine" is violated with nothing to catch it. As written the clause is either redundant (it says nothing the off-default does not) or an unenforceable promise (a guarantee with no discharge).

Choose one: (a) fold the clause into off-by-default and state plainly that the origin machine's protection **is** the default being off (drop the second guarantee's separate standing); or (b) if a real second guard is wanted, define "origin machine" by a detectable fact (e.g. the pack's own repo identity / an `is-pack-origin` marker) and make "off on origin regardless of flag" a stated hard rule. Recommend (a) — it matches how design-sync's off-default is stated and adds no new detection surface.

`defect · unenforceable-promise (discharge)`

---

### F4 — `INV-94` mis-cited as the human's-gate ground

> "because sending outward is the human's gate [base rule 17, INV-94 kin]." — l.926, T-21

`base rule 17` is correct — it is the human's publish gate [ACT-1, l.841]. But `INV-94` is the honesty-disclaimer rule ("no line certifies its own sincerity", l.1907) — unrelated to an outward-send gate. The pin is false. The human's gates are enumerated at INV-9 ("irreversible moves, publishing, authored content, taste", l.1577) and ACT-1 is base rule 17. The T-21 index row (l.1950) cites only `[base rule 17]` and is correct; the stray error is the prose's "INV-94 kin".

Replace `INV-94 kin` with `INV-9` (the human's-gates enumeration) or drop it and keep `[base rule 17 / ACT-1]` alone.

`defect · direct-contradiction (contradiction)`

---

### F5 — The offer-record reuses FEEDBACK.md without stating its line shape

> "the two share FEEDBACK.md only as the local record that an offer was made and answered." — l.928, INV-161

FEEDBACK.md's line schema is route-based [INV-68, l.1951]: who · channel · concerns · plain words · **route**, where route is exactly one of the five (wish · fix · answer · field evidence · noise). An "offer made and answered" is none of those five, and it is not a "received item" the schema was built for. So the collector writes a sixth kind of line into a file whose one home-law does not describe its shape — a one-home-per-fact strain: a different fact-kind sharing FEEDBACK.md with no stated form.

State the offer-record's line shape explicitly (e.g. an `upstream-offer` line: date · the strong moment in plain words · offered/declined/sent), either as a named sixth line-kind in FEEDBACK.md with its own schema sentence, or give it its own record and stop overloading the route-based ledger.

`defect · boundary-issue (composition)`

---

### F6 — The `feedback-upstream` flag should land in the one settings catalog, like design-sync

> "a package-default `feedback-upstream: off` [INV-14]" — l.928; homes "… + the `feedback-upstream` package default" — l.2021, INV-161

The settings' one normative home is the package-defaults table in the base skill [INV-87, l.1298; l.1290], and every setting must be a row there marked card-visible or internal, with completeness checked both ways. Design-sync's switch did this fully — "the switch lives off-by-default in the base skill's defaults table [E-13], under the name design-sync" (l.1632, E-18). The delta names "the feedback-upstream package default" as a home but does not land it as a marked row in that table nor cite E-13/INV-87, so INV-87's completeness sweep has nothing to trace to.

Register `feedback-upstream: off` as a row in the package-defaults table, mark it card-visible or internal, and cite [E-13, INV-14, INV-87] the way design-sync does. Recommend card-visible — a downstream host needs to see the opt-in exists.

`recommendation`

---

### F7 — No owning node or matrix rows yet for E-30 / T-21 / INV-161 (forward obligation)

> "homes — the third-arrow clause + feedback-collector's SKILL.md + the `feedback-upstream` package default" — l.2021, INV-161

Expected at the spec stage — CROSS-LINK proves the spec seams, not the architecture — but flagged for traceability so the next steps do not drop it. The architecture step owes an owning node for `feedback-collector` and for `outbox/` (feedback-collector's SKILL.md does not yet exist; it is a forward reference), and the matrix step owes rows for E-30 / T-21 / INV-161, including a test that the arm stays silent when the flag is off and that no note is written on a silence-or-unclear answer.

Carry `feedback-collector` SKILL.md creation, an `outbox/` node, and E-30/T-21/INV-161 matrix rows into the architecture and matrix steps.

`recommendation`

---

### F8 — The birth-fences list omits the collector's new fences

> "#### Fences its birth must hold" — l.932–938

The fences list preserves the inbound section's invariants (inbox one-file, wish echo, answered-question harvest, problem ledger, no-wish-lost) but names none of the outbound arm's new fences — no auto-send, off-by-default honoured on every read, non-public/no-raw-material. The section now has an outbound edge its own "edges, stated once" list does not cover.

Add the collector's birth fences to the list: no note leaves without the human's explicit yes; the arm is inert while `feedback-upstream` is off; the note carries the distilled point alone, never raw material.

`recommendation`

---

## Seams that hold (noted, no finding)

- **Consent reversal from INV-31 — clean.** The delta states the reversal as "the deliberate opposite of silence-is-consent [INV-31]", cites it, and gives the rationale (an outbound send about a real person). This is a stated deliberate difference, not a silent contradiction — the seam is handled correctly.
- **Digest one-name discipline — clean.** T-21 explicitly fences "Upstream note" away from both existing "digest" meanings — the station-completion digest [INV-35] and the resume-file digest [INV-48]. Confirmed both use "digest" (l.1891, l.1925); the new name does not collide.
- **Measurement-family fence — clean.** "It is no measurement machine … the reading machinery stays [target] with the measurement family [INV-21]" and "does not aggregate … that stays the measurement family's" are consistent with the field-evidence clause (l.909, row 48). The one fine line — "reads one strong moment" vs "does not grade sentiment" — is drawn explicitly with the conservative explicit-signal floor.
- **off = fully inert.** "off means the arm never fires, never reads for a strong moment, never asks" closes the hole of an off machine still reading or scoring.

## ⟨DECIDE⟩ touched

None. The delta introduces no ⟨DECIDE⟩ and touches none of the three open ⟨DECIDE⟩ items in the doc (l.1761–1766, all unrelated — attic layout, pair queues, pair specs).

## Verdict

**Needs another iteration.** Five delta-scoped defects, all with local fixes: F1 (`outbox/` undeclared home — the one with real privacy stakes), F2 (false "never overlap" claim + unowned both-case), F3 (origin-machine guarantee with no mechanism), F4 (INV-94 mis-pin), F5 (offer-record shape). Three recommendations queue for a taste call (F6 settings-catalog row, F7 forward traceability, F8 birth fences). The consent reversal, the digest naming, and the measurement fence are handled well and need no change.
