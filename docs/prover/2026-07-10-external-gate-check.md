# External adversarial gate check — the gates hold (2026-07-10 ~18:18, his web analyst)

An outside session (his web analyst, own clone, no coaching from this window) planted three
desyncs and read the exit codes directly, with a control revert after each:

1. Dead anchor — a registry surface citing a spec anchor that does not exist → exit 1,
   code traces.dead-anchor, precise diagnosis; anchor added → exit 0.
2. Unanchored surface — a registry row with an empty anchor column (behaviour with no spec
   backing) → exit 1, traces.unanchored-surface.
3. Unchecked matrix-coverage box → exit 1; box checked → exit 0.

Its summary, paraphrased: the gates DISTINGUISH broken from clean rather than passing
everything; the scaffold checks are generic, config-driven, stdlib-only code a host wires by
config, so the old Known-issues line no longer describes reality; pre-push sums the gates and
blocks on any red. The differentiating claim — executable gates block the push — is now
verifiable in two commands and held under attack.

Two caveats it raised, with their status here:
- Its environment showed 2 failures in the recursive self-tests (a shallow clone + a nested
  suite run); on this machine's full clone the whole suite reads 346 green the same evening.
  A fresh-full-clone re-run is queued as tomorrow's verification item all the same.
- Fail-closed no-config behaviour is correct but can read as breakage to a first-time host:
  the attach walk's step one (create guardrails.config.json) gets emphasized — row 251.
