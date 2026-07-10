# Guardrails — the four host checks, runnable (SPEC INV-97)

The pipeline's mechanical teeth as code a host attaches, never prose it re-implements:
**completeness**, **tests-present**, **behaviour-traces-to-spec**, **conflicts**. One
config file parametrizes everything — you never edit check code. Each check reads the
config and the tree, exits green (0) or red (1); on red it prints the human sentence
AND one machine line (`GUARDRAIL-FAIL {...}`, valid JSON — SPEC INV-47). Python 3.9
stdlib only; nothing to install.

Failure behaviour is honest by construction: a missing config is red with an attach-me
line, never a silent pass; a config pointing at a path that does not exist is red; a
precondition you genuinely lack is declared as a waiver IN the config, where a reader
sees it — `WAIVED (<check>): <reason>`, exit 0, visible, never silent.

## The attach walk (~15 minutes)

1. **Copy the directory** into your repo:

   ```sh
   cp -r scaffold/guardrails your-repo/guardrails
   ```

2. **Copy the config to your repo root and fill your paths**:

   ```sh
   cp guardrails/guardrails.config.example.json guardrails.config.json
   ```

   - `spec_path` / `matrix_path` — your product spec and test matrix.
   - `tests_dir` — where your tests live.
   - `user_facing_globs` — globs (with `**`) naming the files whose change demands a test.
   - `registry_path` — your surface registry: markdown rows
     `| <surface-name> | <needle-or-regex> | <spec-anchors comma-sep> |`
     (header and separator rows are ignored).
   - `render_command` — command whose stdout is your rendered content, or `null` to
     read the files in `rendered_artifacts` instead.
   - `surface_discovery_pattern` — regex with one capture group that discovers surface
     ids in the rendered content (the self-closing direction), or `null` to skip it.
   - Checks read `$GUARDRAILS_CONFIG` if set, else `./guardrails.config.json` at the
     repo root — run them from the root.

3. **Run each check once**:

   ```sh
   python3 guardrails/check_completeness.py
   python3 guardrails/check_tests_present.py --base origin/main
   python3 guardrails/check_traces_to_spec.py
   python3 guardrails/check_conflicts.py
   ```

   Each prints `OK (<check>): <summary>` and exits 0, or the failure lines and exits 1.

4. **Plant one defect and see red** — the walk's own red-first. Add a fake row to your
   registry (`| ghost | id="ghost" | INV-1 |`), run `check_completeness.py`, and watch
   it exit 1 with `completeness.registered-but-absent`. Remove the row, watch it green.
   A gate you have never seen red is a gate you are trusting, not testing.

5. **Add the four lines to your pre-push hook** (`.git/hooks/pre-push`, executable):

   ```sh
   python3 guardrails/check_completeness.py || exit 1
   python3 guardrails/check_tests_present.py || exit 1
   python3 guardrails/check_traces_to_spec.py || exit 1
   python3 guardrails/check_conflicts.py || exit 1
   ```

6. **Declare waivers for what you honestly lack.** No rendered artifact yet? Say so in
   the config, dated and owned, where a reader sees it:

   ```json
   "waivers": {"completeness": "no rendered artifact yet — declared 2026-07-10, owner Alexander"}
   ```

   The check prints `WAIVED (completeness): <your reason>` and exits 0. An undeclared
   gap never passes quietly — that is the whole point.

## What each check catches

| check | red when | codes |
| --- | --- | --- |
| `check_completeness.py` | a registered surface is absent or empty in the rendered content; a rendered surface is unregistered | `completeness.registered-but-absent`, `.registered-but-empty`, `.rendered-but-unregistered` |
| `check_tests_present.py` | the diff against the base touches `user_facing_globs` but nothing under `tests_dir` | `tests-present.missing-test` |
| `check_traces_to_spec.py` | a registry row cites no anchor, or cites one the spec does not contain | `traces.unanchored-surface`, `traces.dead-anchor` |
| `check_conflicts.py` | duplicate index anchors; an indexed INV-* no matrix row cites; ⟨DECIDE⟩ on a RESOLVED line; a surface registered twice | `conflicts.duplicate-anchor`, `.invariant-without-row`, `.resolved-but-live`, `.surface-named-twice` |

Every check also reds on `<check>.no-config` (config missing or unparseable) and
`<check>.dead-path` (a declared path or glob base that does not exist).

## Honest boundary

Guardrails catch **structural** defects only: empty surface, missing test, untraced
behaviour, id/naming conflict, partial artifact. A **semantic** bug — is the number
right? is the recommendation correct? — stays the prover's and the human's. Enforce
structure mechanically; reason about meaning with eyes open.
