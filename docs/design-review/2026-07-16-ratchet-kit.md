# Design review — scoped, drawn by the second-sibling question (2026-07-16)

Design-reviewer skill version: 1.0.x (scoped form). Drawn by INV-169 at the intake of task 13:
the ratchet-adoption kit (`adopt/install-ratchet.sh`, INV-172) is the SECOND member of a kind an
existing surface already has — the installable check kit, whose first member is
`scaffold/guardrails/` (the four project-side checks, INV-97). This record is the first run of
the second-sibling channel since the law landed (row 341).

## The proposed group
One plain role sentence fits both: "a person attaches a pack-shipped mechanical check set to
their own repo by copying files and following a short walk." Members: `scaffold/guardrails/`
(first), the ratchet kit (second).

## Behaviour parity within the group
| Behaviour | scaffold kit | ratchet kit | Verdict |
|---|---|---|---|
| Config-driven, zero code edits | `guardrails.config.json` | same file read first, args as fallback | match |
| Stdlib-only, host-portable | yes | yes | match |
| One JSON line per red (gate contract, INV-47) | yes | yes (`ratchet-install` code) | match |
| Red-first proof in the attach walk | plant-a-defect step | plant-a-register-defect step (ADOPT.md) | match |
| Waiver/exception road | config `waivers` | cap file + guard test (the ratchet IS the exception road) | deliberate difference — a ratchet's exceptions must only shrink, a structural check's waivers are stable; stated in INV-172 |
| Source pin for update detection | none | `ratchet-manifest.json` (pack version + sha256) | divergence, first member LACKS the behaviour |

## Findings
1. **Recommendation** — the scaffold kit lacks the source-pin manifest the ratchet kit ships:
   a host cannot mechanically tell a stale vendored check from a current one. Both objects in
   hand: `scaffold/guardrails/check_completeness.py` (no pin anywhere) against
   `adopt/install-ratchet.sh` step c (writes `ratchet-manifest.json`). Recommend lifting the
   manifest to cover BOTH kits when the update-watcher (queued task 6) lands, so one mechanism
   reads both. Queued as part of task 6's acceptance rather than a new row — the watcher is the
   consumer that makes the pin worth writing.
2. No other divergence: gestures (CLI shape), transitions (install → green → ratchet/red), and
   affordances (README walk) behave alike.

Confidence: confident (defensible on the artifact texts alone). No question rides to the human.

## Disposition
| Finding | Outcome |
|---|---|
| 1 — source-pin parity for the scaffold kit | recommended — folded into task 6's acceptance line in NEXT_STEPS |
| 2 — parity otherwise | clean |
