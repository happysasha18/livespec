# Prover pass — founding-questions + design-sync delta (B-2 + E-18), v0.13.0 → v0.14.0 (2026-07-05, founding-designsync)

Mode: **CROSS-LINK** on the two new clauses landed together (queue rows 83 + 88, one landing):

- **E-18** (SPEC L452–457, header L14, index L581) — **design-sync**, an OPTIONAL [target] machine in "The
  machines that hold the bounds": syncs the components a landing touched to the team's design project
  (claude.ai/design) where the human reviews rendered cards — "the show-the-real-render rule through a
  different window"; switched per host in its profile (`design-sync: off` the package default); every sync
  human-gated because it PUBLISHES; the pack itself (text) never syncs; wiring lands post-1.0 under row 86.
- **B-2** (SPEC L237–245, index L613) — **the founding questions are asked, never inferred**: before the
  first wish walks, the downstream-shaping questions get explicit answers in the new spec's opening —
  personal-tool-vs-reusable-product first; read from the human's profile when a line covers it, asked
  otherwise, never derived from examples; an inferred founding answer is the silent micro-decision [INV-5]
  at its most expensive; adoption asks the same at orient [A-1].
- Two Formal-index rows (E-18 L581, B-2 L613) + header target-list mention (E-18 L14) + header bump
  v0.13.0 → v0.14.0 (L1).

**Seams checked (task item 4).** E-18 vs **S-0** (target granularity); E-18 vs **E-13** (host-profile
switch, "off is package default" as a ladder default); E-18 vs **ACT-1** + irreversibility (human-gated
publish); E-18 vs the **communicator show rule** (second channel); E-18 vs **E-7** ("touched" vs
declared-scope) and **E-10** (surface authority); B-2 vs **INV-5** (silent-micro-decision framing); B-2 vs
**E-13/INV-14** (profile-read = override or default?); B-2 vs **A-1** (does orient bear the duty?); B-2 vs
**INV-12/INV-4** (ask-never-guess family, blocking vs proceed-on-default); the **Formal-index symmetry**
both directions.

**Prior-record check (task item 5).** `2026-07-05-intake-trio.md` (rows 77 + 85 → v0.13.0): all 9 findings
**FOLDED same sitting**; closing line "Nothing left for the queue from this pass." **Zero unfolded rows
carried forward.** Nothing owed into this pass. (The standing MINOR-under-CROSS-LINK FULL debt is owed at
the 1.0 milestone FULL audit / M-6 push gate — not a per-finding fold.)

**Mechanical guard.** Delta anchor↔prose symmetry exact: **E-18** clause L457 / index L581 / header mention
L14 — appears once per surface, index one-liner ("optional machine, host-profile switch, human-gated
(publishes) [target]") tracks the prose; **B-2** clause L245 / index L613, one-liner tracks, slotted right
after B-1 (index L612→L613). No duplicate anchors. Header bumped v0.13.0 → v0.14.0. ROADMAP confirms rows 83
(design-sync, wiring post-1.0 with row 86) + 88 (founding questions) both in-work "lands with" each other.
The two clauses reverse no earlier-proven material — the seams below are one-home reconciliations, scope
clarifications, and a queue-ownership label mismatch, not contradictions of proven law.

**Done well (noted, no finding).**
- **S-0 granularity respected.** E-18 carries `[target]` on its OWN clause (L452) and the index row carries
  it too (L581); the header lists E-18 under the "Target (…)" umbrella exactly as it lists M-5 and ACT-3 —
  no inline over-claim of shipped. Same discipline the intake-trio pass praised in INV-21.
- **ACT-1 consistency, irreversibility direction correct.** "Every sync is gated by the human because a
  sync PUBLISHES" is a clean instance of ACT-1's "publish/push gates" — the outward/irreversible act is
  the human's, exactly as the irreversibility rule wants. The "pack itself, a text product, never syncs"
  carve-out mirrors E-17's text-product self-exemption.
- **INV-13 one-home held across the ask-never-guess family.** B-2 (founding) and INV-12 (size/priority) both
  APPLY the base skill's ask-never-guess rule to their own domain without restating it — two domain
  instances, one normative home in `live-spec-base`. No drift.

**Process note (MINOR bump under CROSS-LINK).** v0.13.0 → v0.14.0 is a MINOR (`0.x.0`) step; the prover skill
requires a FULL re-prove before a MINOR bump (M-1). As with the -facets / -fences / -intake-trio precedents:
the CROSS-LINK delta stands; the FULL whole-spec pass discharges at the **M-6 push gate for this landing** or
the **1.0 milestone audit (row 84)** — recorded so it is not lost.

**Worker verdict: 0 must-fix · 6 should-clarify · 1 worth-considering.** The two clauses are clean; every
seam resolves to a clarification, a one-home pointer, or a label fix — none blocks the build. Outcomes
**PENDING** — the senior triages. F7 is the top fold (the adoption path silently skips the founding ask
without it).

| # | Finding (one line) | Severity | Outcome |
|---|---|---|---|
| F1 | **Design-sync is a second review window, but E-18 never says whether it SUPPLEMENTS or REPLACES the in-session render for the human's design gate.** E-18 (L453): "the human reviews rendered cards — the show-the-real-render rule through a different window." The communicator's show-real rule already renders artifacts in-session for the human's taste/design decision [ACT-1]. When design-sync is ON, a touched component reaches claude.ai/design AND (per communicator) is shown in-session — two surfaces for one design-review decision, with no statement of which is authoritative. A senior can't tell where the human's design gate is discharged; the human may approve in one window while the other is treated as the record. Fix: one sentence — design-sync when ON is an ADDITIONAL rendering surface for the same show-real rule (communicator stays the rule's one home per INV-13); the human's approval on either window is the same gate, and E-18 references the communicator rule rather than creating a second decision home. | should-clarify · boundary-issue (composition) | **FOLDED**: design-sync SUPPLEMENTS the in-session render — the render stays the landing-gate authority, the design project is the team-review channel (E-18) |
| F2 | **`design-sync: off` is called "the package default," but E-13 says every package default's normative home is the base skill — and design-sync's is [target], so today no such home exists.** E-18 (L454): "`design-sync: off` is the package default." E-13 (L342–343): package defaults are "each value stated in the base skill beside the rule it tunes." Design-sync's rule/wiring is [target] under row 86, so the base-skill default entry is owed at that landing, not now — a reader following E-13 to the base skill for `design-sync: off` finds nothing (a phantom default). Also: turning it ON in a host profile is an override of a package default, which INV-14 makes a written+journaled act — worth naming. Fix: note the `design-sync: off` default's normative home lands in the base skill WITH the wiring (row 86); until then the spec states it descriptively (the M-6-push-gate precedent for naming a package default in prose), and flipping it on per host is an INV-14 journaled override. | should-clarify · boundary-issue (composition) | **FOLDED**: the switch + off-default land WITH the machine in the base skill's defaults (E-13); toggle-on = recorded profile line (INV-14) — no phantom default today |
| F3 | **E-18 says wiring lands under "its own queue row" but cites row 86 — which is the work-kind axis, not a dedicated design-sync row.** E-18 (L456–457): "Wiring lands under its own queue row, kin to the work-kind axis (queue row 86)." ROADMAP row 86 IS the work-kind axis; row 83's own note reads "wiring post-1.0 with row 86" — i.e., wiring RIDES WITH row 86, there is no dedicated design-sync-wiring row. S-0 requires every [target] clause to be owned by a ROADMAP row; the ownership is real (row 86, shared) but E-18's "its own queue row" over-claims a dedicated row that doesn't exist. A future guardrail checking [target]→row backing, or a human tracing the row, hits a mislabel. Fix: either open a dedicated wiring row and cite it, or reword to "wiring rides with the work-kind axis (row 86)" to match row 83's note — drop "its own." | should-clarify · hard-to-operate (ops-ux) | **FOLDED**: wiring got its own dedicated queue row (93), kin to row 86; E-18 cites it |
| F4 | **Design-sync syncs "the components a landing touched"; the snapshot [E-7] advances "only for the surfaces the change DECLARED" — two notions of what one landing changed, unaligned.** E-18 (L453) "components a landing touched" vs E-7 (L449) "the surfaces the change DECLARED." Touched (edited) and declared (scoped) can differ — a landing may touch more than it declares, or declare without a visual touch. If design-sync computes its set independently of the snapshot's declared-scope, the two machines disagree on a landing's footprint, and the design project shows components the diff baseline never advanced (or vice versa). Both are [target] so nothing ships broken today, but the shared concept should be named once. Fix: state that design-sync reuses the snapshot's DECLARED-scope set [E-7] — one landing, one notion of what it changed — resolved when the wiring lands (row 86). | worth-considering · boundary-issue (composition) | **FOLDED**: footprint aligned — the components the landing DECLARED, the same declared-scope notion the snapshot diffs by (E-7) |
| F5 | **B-2 frames an inferred founding answer as "the silent micro-decision [INV-5]," but INV-5's own remedy (record + surface) is exactly what B-2 forbids for founding questions — they must be ASKED or profile-read, and that blocks the first wish.** B-2 (L240–241): "read from the human's profile … asked otherwise, and never derived … An inferred founding answer is the silent micro-decision [INV-5] at its most expensive." INV-5 (L185) legalizes a micro-decision that is "recorded in the spec AND surfaced" — the proceed-on-default path INV-4/INV-12 take (size/priority defaults to normal, lane keeps moving). B-2 grants NO such default-and-proceed path: the answer is asked or profile-read before the first wish walks. So B-2 is a deliberate STRENGTHENING, not a plain instance — and a reader applying INV-5's record+surface remedy would wrongly let a founding default proceed unblocked. Fix: state that founding questions are the exception to the INV-4/INV-12 proceed-on-recommended-default rule — asked or profile-read, blocking the first wish, because the bootstrap gate precedes the lane and every later sentence leans on the answer (B-2's own reason). | should-clarify · internal-conflict (consistency) | **FOLDED**: named a deliberate STRENGTHENING — founding answers block the first wish, unlike the proceed-on-default habit (INV-4/INV-12 contrasted in prose) |
| F6 | **"Read from the human's profile" is a settings-ladder resolution, but B-2 neither cites E-13 nor states the SCOPE of personal-vs-reusable — nor whether a profile-read answer is surfaced.** B-2 (L240): "read from the human's profile when a line covers it (their standing word)." Personal-vs-reusable is a fact about the PROJECT, yet it is read from the PERSONAL profile — per E-13 a project-fact's home is the host profile, so the reader can't tell if this bypasses the ladder or is a personal-scope standing preference (how-the-human-works) that SEEDS the new project's default. And a founding answer silently read from the profile into the spec opening — the most load-bearing decision — sits close to the buried-decision INV-5 forbids unless it is surfaced/confirmed. Fix: cite E-13 and state the scope — personal-vs-reusable is the human's personal-scope standing preference that SEEDS the founding default (this project can still be declared personal on the human's word, the narrower scope winning); and a profile-read founding answer is surfaced/confirmed to the human, not silently adopted (INV-5/INV-14). | should-clarify · boundary-issue (composition) | **FOLDED**: resolves like any setting (E-13 cited); a profile line = personal-scope standing preference SEEDING the project default, and the seeding is said aloud |
| F7 | **B-2 asserts "Adoption asks the same questions at orient [A-1]," but A-1's own wording carries no such duty and no pointer back to B-2 — an adoption run reading the adoption section skips the founding ask.** B-2 (L244): "Adoption asks the same questions at orient [A-1]." A-1 (L256–258) is entirely about READING existing documents ("Every existing document is read BEFORE anything is touched … never assumes a blank slate") — it never mentions the founding questions. The reference is one-directional: B-2 names A-1 as the performance site, A-1 is silent. An adoption run guided by the adoption section founds/adopts with an inferred personal-vs-reusable answer — the exact expensive failure B-2 exists to prevent, now at the adoption door. Keeping INV-13 (B-2 stays the one normative home), fix with a back-POINTER in A-1, not a restatement: "orient also settles the founding questions [B-2] about the project it finds — read from the profile or asked, never inferred from the codebase (three of the human's own artifacts are its first users, not its definition)." | should-clarify · unclear-owner (actors) | **FOLDED**: A-1 gains the back-pointer (adopt orient owes the founding questions, home stays B-2 — INV-13 held) |

Seven findings, outcomes PENDING for the senior. F1/F2/F3/F4 are the E-18 seams (second-channel authority ·
package-default home · queue-ownership label · touched-vs-declared); F5/F6/F7 are the B-2 seams (blocking
exception vs INV-4/INV-12 · profile-read scope+surfacing · the A-1 back-pointer). Zero must-fix — the two
clauses are clean and buildable; every seam is a clarification or one-home pointer. F7 is the top fold (the
adoption path silently skips the founding ask without it). The FULL push-gate pass owed for the MINOR bump
(process note above) is where the whole-spec re-prove lands.

All seven findings folded same sitting by the senior (Fable). The FULL re-prove debt discharges at the milestone audit (row 84, tonight). Nothing left for the queue from this pass.
