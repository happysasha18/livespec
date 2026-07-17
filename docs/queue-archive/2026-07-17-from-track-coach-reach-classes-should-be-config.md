# From track-coach: the reach map's infra/prose classes should be config, not hardcoded

**Date:** 2026-07-17
**From:** track-coach window (Alexander), during the 2.1.0 → 2.4.0 catch-up.
**Kind:** ergonomics wish (not a bug — the current behaviour is correct).

## What happened

Adopting the 2.3.0 scoped-run road (`guardrails/check-push-reach.sh`) into track-coach, the infra
and prose CLASSES had to be hand-edited inside the vendored script. The pack's defaults classify
`scripts/*` as infra — right for the pack, where `scripts/` holds helper tools. In track-coach
`scripts/` IS the product engine (the analysis pipeline), so copying the classes verbatim would have
let an engine change scope to a couple of tests and false-green. The fix was to edit `matches_infra`,
`matches_prose`, and `REFERRER_DIRS` in the host's copy of the script — editing vendored gate logic,
which then drifts from the pack's copy and complicates the next re-vendor.

## The wish

Make the reach classes a host CONFIG input rather than script-body constants. A host declares its own
infra dirs, prose files, and referrer dirs once (a natural home is `guardrails.config.json`, beside the
gated-doc list the ratchet already reads there, or a small `reach-classes` file). `check-push-reach.sh`
reads that config and keeps its logic identical, so a host adopts the road by declaring its layers —
the same shape `project.layers` already carries (SPEC INV-135) — without editing vendored code. The
pack's own values become that config's default.

This also composes with the per-kind layers idea: a project already declares its concrete layers, and
which of them are "safe to scope" is the same knowledge. A vendored script that must be hand-edited per
host is the ergonomics gap; a declared class list closes it.

No urgency — track-coach is unblocked (the hand-edit is in place and tested). Filed so the adoption
friction is visible where the road is owned.
