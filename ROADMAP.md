# livespec Roadmap

The wish queue. Intake is continuous — a wish lands here the moment it is spoken. Execution is serial:
the current landing finishes before the next starts (bugs may preempt).

| # | Wish (plain words) | Size | Status | Decision / acceptance |
|---|---|---|---|---|
| 1 | Alexander's word to publish the repo | needs Alexander | waiting — README open in Sublime | Alexander reviews README, says publish |
| 2 | Author the package's own SPEC | M | **landed 2026-07-04** | SPEC.md v0.1 written (self-application run #1); prover pass = row 7 |
| 3 | Generic guardrails scaffold lifted from track-coach | M | queued | After prover pass on SPEC |
| 4 | Adopt-mode dry run on tlvphoto | M | queued, needs Alexander | Alexander confirms tlvphoto as pilot |
| 5 | skill-creator eval pass over the four skills | S | queued | After guardrails scaffold |
| 6 | Better name if one lands | — | closed 2026-07-04 | livespec is Alexander's pick |
| 7 | product-prover pass over livespec's own SPEC | M | **landed 2026-07-04** | 11 findings (4 must-fix), ALL folded same session → SPEC v0.2; docs/prover/2026-07-04.md |
| 8 | Adopt must ORIENT first: read ALL existing docs (roadmap/specs/tests) and re-engineer them into livespec shapes (Alexander 2026-07-04) | S | **landed 2026-07-04** | Spec'd in SPEC.md "Adopting a live project"; ADOPT.md update follows the prover pass |
| 9 | Superseded old files are ARCHIVED, never deleted — attic/ folder with a manifest (Alexander 2026-07-04) | S | **landed 2026-07-04** | Spec'd in SPEC.md; acceptance: no adopt run ever deletes a host file |
| 10 | Version-control gate: no git in host ⇒ init + recommend GitHub remote/backup before first landing (Alexander 2026-07-04) | S | **landed 2026-07-04** | Spec'd in SPEC.md; acceptance: adopt on a git-less folder refuses to land changes until VCS exists |
| 11 | Honest long-tail prior-art check (skill ecosystem, awesome-lists, GitHub topics) before README claims go public (Alexander challenged the "pioneers" claim 2026-07-04) | S | in-work | README claims match what the search actually found; overclaims corrected |
