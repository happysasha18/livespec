# Bare run — product-prover scenario (2026-07-05, Sonnet worker, tool uses: 0)

Scorer's summary (scored live from the full output on 2026-07-05; this record keeps the load-bearing
excerpts — the absence claims (no severities, no four-part shape, no tables) are re-provable at any
re-run and were checked against the full text at scoring time):
the bare run found most planted holes — the track/session model gap, persistence inconsistency, the
export snapshot-vs-live race, export concurrency, no failure path, the cross-view mute visibility risk,
cross-tab localStorage, stem sync drift — strong loader-fed substance. What it did NOT deliver: no
severity triage, no four-part findings (headline · pin · consequence · action), no extracted model or
"what I assumed" section, no coverage tables, no paste-ready properties; and it missed the
end-of-track dead-end entirely. Delivered as one flowing essay under bold topic headers.

Representative excerpts (verbatim):

---
**Core gap: no track/session model.** The spec never says whether the player is bound to one fixed
track or is a reusable component that loads different tracks. This isn't cosmetic — it decides whether
mute-state persistence is even coherent. […]

**Export is the riskiest underspecified area.**
- "Renders the current mix" — does that mean current volume AND current stem mutes, or just volume? […]
- Snapshot vs. live: if the user changes mute/volume *while* a render is in progress, does the export
  reflect the mix at click-time or whatever state exists when rendering finishes? Classic race
  condition, unaddressed.
- Concurrency: what happens if "Export mix" is clicked again while a previous export is still
  rendering […]
- No failure path: what does the user see if the render fails or times out? Spinner forever is the
  implicit default, which is bad.
- Cross-view visibility: since mutes are set in Detailed view but Export is presumably available in
  both views (not stated which), a user in Simple view has no visual indication that some stems are
  muted before they export — surprising-mix risk with no mitigation specified.

**Bottom line:** the happy path […] reads fine, but almost every non-happy-path question —
persistence scope, export snapshot semantics, concurrency, failure states, and what "current mix" even
means — is open.
---
