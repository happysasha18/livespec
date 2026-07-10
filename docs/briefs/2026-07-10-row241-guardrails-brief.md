# Brief — row 241: the four host checks become runnable code (worker: cloud session)

You are a briefed implementation worker. This document is self-contained: every decision is
already made; you implement, test, and report. You never interpret the product spec beyond the
sentences quoted here, and you never decide scope. Date at briefing: 2026-07-10 ~16:59 (re-read
the machine clock yourself for any stamp you write).

## Ground rules (the worker contract)

- **Branch**: create `row241-guardrails` from current `main`. All commits go there. Push the
  branch when acceptance passes. NEVER commit to main, never merge, never tag.
- **Write-set** (writes fenced to exactly these; reads are free):
  - `scaffold/guardrails/**` (new files, plus its README.md)
  - `tests/test_scaffold_guardrails.py`
  - `tests/fixtures/scaffold_guardrails/**` (fixture trees)
  - `.live-spec/checkpoints/row241-worker.md` (your checkpoint — update AS you work)
- **Checkpoint discipline**: `.live-spec/checkpoints/row241-worker.md` holds done / in-progress /
  next, updated as you go, so a cut-off resumes instead of restarting. Record the red-run outputs
  there (see Red-first below).
- **HALT list** — stop WITH evidence in the checkpoint if: a requirement here is ambiguous in a
  way you cannot resolve from the quoted spec sentences · one command fails twice unexplained ·
  a dependency/config is missing · acceptance is impossible as briefed. Otherwise run to
  completion.
- **Workshop noise**: any tooling problem you hit (flaky command, missing dep) — log one line
  (signature, date, context) in your checkpoint under WATCHED.
- Python 3.9 stdlib ONLY — these files get copied into arbitrary host repos; no pip installs.

## The spec sentences this serves (verbatim, SPEC INV-97)

> The pack ships, under `scaffold/guardrails/`, a generic runnable form of the four checks the
> pipeline's teeth name — completeness, tests-present, behaviour-traces-to-spec, conflicts —
> parametrized by one host config file, never by editing check code. [...] Each check reads the
> config and the tree, exits green or red, and on red emits the typed failure line beside its
> human sentence [INV-47]. Failure behaviour is honest by construction: a missing config is red
> with an attach-me line, never a silent pass; a config pointing at a path that does not exist
> is red; a host that genuinely lacks a check's precondition (no render command yet) declares
> the waiver IN the config, where a reader sees it — an undeclared gap never passes quietly.

Gate-contract output (SPEC INV-47): on red, print human-readable lines AND one machine line:
`GUARDRAIL-FAIL {"severity":"error","code":"<check>.<reason>","message":"...","fix":"..."}`
(single line, valid JSON after the `GUARDRAIL-FAIL ` prefix; `fix` is the same sentence a person
reads). Green prints one line `OK (<check>): <summary>` and exits 0. Red exits 1.

## Deliverables

### 1. `scaffold/guardrails/guardrails.config.example.json`
```json
{
  "spec_path": "PRODUCT_SPEC.md",
  "matrix_path": "TEST_MATRIX.md",
  "queue_path": "ROADMAP.md",
  "tests_dir": "tests",
  "user_facing_globs": ["src/**/*.py", "templates/**/*.html"],
  "registry_path": "SURFACES.md",
  "render_command": null,
  "rendered_artifacts": ["dist/index.html"],
  "surface_discovery_pattern": "<section id=\"([^\"]+)\"",
  "waivers": {"completeness": "no rendered artifact yet — declared 2026-07-10, owner Alexander"}
}
```
Config resolution in every check: `$GUARDRAILS_CONFIG` env var if set, else
`./guardrails.config.json` at repo root. Missing → red `<check>.no-config`, fix line: "copy
guardrails.config.example.json to guardrails.config.json and fill your paths — see
scaffold/guardrails/README.md". Any declared path/glob-base that does not exist → red
`<check>.dead-path`. A check named in `waivers` prints
`WAIVED (<check>): <reason>` and exits 0 — visible, never silent.

### 2. `scaffold/guardrails/gate_lib.py` — tiny shared lib
Load+validate config · resolve waiver · emit the typed line · glob matching (use `pathlib` +
`fnmatch`; support `**`). No check logic here.

### 3. The four checks (each a standalone script, `python3 check_x.py [--base REF]`)

**`check_completeness.py`** — the registry file (`registry_path`) lists surfaces as markdown
rows: `| <surface-name> | <needle-or-regex> | <spec-anchors comma-sep> |` (header + separator
rows ignored). For each registered surface: the needle must match somewhere in the rendered
content (run `render_command` if non-null, else read every file in `rendered_artifacts`); a
non-match is red `completeness.registered-but-absent`. Empty match content (needle found but its
line/element empty — needle matched on a line with no other non-tag text) → red
`completeness.registered-but-empty`. If `surface_discovery_pattern` is non-null: every id the
pattern discovers in the rendered content must appear as a registry surface-name → red
`completeness.rendered-but-unregistered` (this is the self-closing direction).

**`check_tests_present.py`** — `git diff --name-only <base>...HEAD` (base = `--base` arg, else
`origin/main`, else config `"base_ref"`). If any changed file matches `user_facing_globs` AND no
changed file is under `tests_dir` → red `tests-present.missing-test` naming the offending files.
No changed user-facing files → green.

**`check_traces_to_spec.py`** — every registry row's third column must cite ≥1 anchor → red
`traces.unanchored-surface` if empty; every cited anchor must exist in `spec_path` (an anchor
`X-nn` exists if the spec contains `[X-nn]` or `| X-nn |`) → red `traces.dead-anchor`.

**`check_conflicts.py`** — four sub-checks over the docs: (a) duplicate anchor ids in the spec's
index (`| <id> |` table rows) → `conflicts.duplicate-anchor`; (b) an `INV-*` id present in the
spec index with NO matrix row citing it in `matrix_path` → `conflicts.invariant-without-row`;
(c) the literal marker `⟨DECIDE⟩` appearing on a line that also contains `RESOLVED` →
`conflicts.resolved-but-live`; (d) duplicate surface names in the registry →
`conflicts.surface-named-twice`.

### 4. Fixtures + tests — RED FIRST
`tests/fixtures/scaffold_guardrails/host-clean/` — a minimal fake host (tiny spec with an index,
matrix citing its INVs, registry with 2 surfaces, a rendered index.html, a config). Plus one
planted-defect variant per failure code above (share the clean tree, override the one file —
build variants in tmp inside the test, copying clean + patching, rather than 12 full trees).

`tests/test_scaffold_guardrails.py` (pytest/unittest, consistent with the repo's tests/):
- each check on the clean fixture → exit 0;
- each planted defect → exit 1 AND the `GUARDRAIL-FAIL` line parses as JSON with the expected
  `code`;
- no config → exit 1 with `<check>.no-config`; waived check → exit 0 with `WAIVED` in output.

**Red-first proof**: write the tests BEFORE the checks, run them (they fail — the scripts don't
exist), paste that run's tail into your checkpoint, then implement to green. This ordering is
the acceptance's first item; a checkpoint without the red tail fails review.

### 5. `scaffold/guardrails/README.md` — the ~15-minute attach walk
Numbered: copy the dir → copy+fill the config → run each check once → plant one defect and see
red (the walk's own red-first) → add the four lines to your pre-push hook (show the exact
lines) → declare waivers for what you honestly lack. State the boundary: structural defects
only; a semantic bug stays the prover's and the human's.

## Acceptance (all must hold before you push the branch)
1. Red-first tails recorded in the checkpoint (tests before code).
2. `python3 -m pytest tests/test_scaffold_guardrails.py -q` green.
3. FULL suite `python3 -m pytest -q` green (your files must not break existing gates).
4. `git diff --name-only main...row241-guardrails` shows ONLY write-set files.
5. Each check run manually once against the clean fixture from the repo root, outputs pasted
   into the checkpoint.
Then: push the branch, and end your session's reply with the suite log's LAST LINE verbatim.

Integration (matrix function-rows, attaching the pack repo itself as first host, retiring the
README Known-issues line, version bump) is the senior session's — not yours.
