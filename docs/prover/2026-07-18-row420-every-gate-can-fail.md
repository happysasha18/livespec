# Prover record — 2026-07-18 — ROADMAP 420 candidate 3: the meta-gate (every gate carries a known-red proof)

Fuller form: a cross-cutting delta. The gate reasons over the WHOLE push chain rather than one
surface, so it earns the full walk, though it adds one module (one gate + one registry) to the
guardrails node.

## Previous records clean

The prior record `docs/prover/2026-07-18-row420-ci-mirror-and-judge-listed-gates.md` (candidates 1 &
2, INV-210/INV-211) carries no unfolded rows and no open ⟨DECIDE⟩. Nothing outstanding is inherited.

## The delta in one line

One meta-gate, gate w (`guardrails/check-every-gate-can-fail.py`, INV-212): it enumerates the
`-- gate X:` markers `pre-push` invokes (the enumeration gate u already reads) and reds unless every
gate is classified in `guardrails/gate-red-proofs.json` — either a `proof` (a red-first test that
drives the gate's own check to a non-zero exit, tied to the gate by a `reds` token and verified by
structure) or a `covered` gate that runs no independent check and rides another gate's red. It turns
the sharpest lesson of this movement into a machine: a gate that cannot red is a check that looks at
nothing, the hollow authority-anchor gate (commit 8a0209f) and a worker's false "zero violations"
being the two instances the owner named when he asked for the audit in person (2026-07-17 ~18:27).

## The footprint verdict

Cross-cutting. The gate does not own a new product surface; it reads the entire gate chain and the
per-gate proof registry. Its own home is the guardrails node, but its subject is every other gate, so
the read spans the whole chain and the full pipeline ran from step 1.

## Verdict

- **Every spec fact has an owning node.** INV-212 is owned by the guardrails node in ARCHITECTURE.md,
  with pins for the two new files (`check-every-gate-can-fail.py`, `gate-red-proofs.json`). No unowned
  fact, no new node — the meta-gate lands under the existing guardrails node beside gates u and v.

- **No node stands without spec backing.** No new node was carved; the fitness test does not fire.

- **The proof-of-red convention is mechanical and does not drown.** The convention reuses the two
  registry patterns the chain already runs (`ci-mirror.json`, `judge-hooks.json`): a JSON map from
  gate letter to the red-first test that reds it, verified by reading the test's structure. The gate
  does NOT re-run each proof — the suite already runs every one under gate b, exactly as
  `check-ci-mirror.sh`'s own red-proof runs there — so the meta-gate stays a fast static scan and adds
  no duplicate subprocess load to the push. This was the one tradeoff to weigh (re-execute every proof
  for certainty, versus verify structure and let gate b execute), and the static read is the lightest
  form that is still mechanically checkable: it catches a proof that does not exist, is not defined, is
  not tied to the gate's check, or carries no non-zero-exit assertion (a bare "the gate ships" test).

- **Run against the real chain, nothing was back-filled.** The meta-gate checks 23 gates (a–w). Every
  gate that invokes a check of its own already carried a genuine red-proof test from its own landing —
  the discipline held, as the audit predicted ("most gates already ship fixtures"). The one gate that
  invokes no independent check, gate c, is classified `covered`: its anchor-ownership assertion rides
  the pytest suite (gate b), whose red-proof `test_broken_suite_fails` shows the suite reds. This
  mirrors the carve-out `ci-mirror.json` already declares for gate c (folded into the suite), so the
  treatment is consistent across both meta-gates rather than invented here.

- **No gate cannot red by construction.** The `cannot_red` map is empty: no gate in the chain is a
  gate-whose-only-job-is-to-pass. Gate c is not such a gate — its assertion still reds if the real
  tree breaks; it simply owns no separate check binary. The map exists so that if such a gate ever
  appears it reds loudly and stays surfaced, never papered as a carve-out.

- **Cross-section.** Gate w composes with gate u (CI-parity): gate w reads only repo files, so it is
  not a CI carve-out and represents itself as a CI step (`gate w`), and gate u then requires that
  mirror — asserted by `test_gate_mirrored_in_ci` and by gate u passing on the real tree. Gate w also
  composes with itself: its own row in the registry points at its own red-proof
  (`test_missing_proof_reds`), so the meta-gate is held to the same law it enforces.

- **Red-first proven.** 13 of the 17 new tests failed against the pre-delta tree (gate and registry
  absent; the 4 that passed were the doc-traceability checks, whose spec/index/architecture/matrix
  edits landed first in the same session), then green after the delta. The behavioural red-proofs each
  fire inside the green suite and were captured live: a fixture registry missing gate a's proof reds
  ("gate a runs in pre-push but is classified in neither proofs, covered, nor cannot_red"); a proof
  pointing at a function with no non-zero-exit assertion reds ("carries no non-zero-exit assertion");
  a reasonless covered reds; a `cannot_red` gate reds loudly.

- **The redundant hardcoded mirror test retired into the machine.** `test_skill_review.py`'s
  `test_ci_mirror_carries_every_local_gate` asserted a fixed list of four scripts present in
  `gates.yml`. Those four are gates p/q/r/s, none of them CI carve-outs (c/k/m/v), so gate u already
  machine-checks their CI mirroring. The fixed-list assertion is the "list of literals where the
  machine should read the class" anti-pattern; it was removed, a comment left in its place pointing at
  gate u and `test_ci_mirror.py`. Nothing gate u does not cover was lost: gate u's letter-mirroring
  law is strictly more general than the four-script substring check.

## Open ⟨DECIDE⟩

None touched by this surface.

## Must-fix

0.
