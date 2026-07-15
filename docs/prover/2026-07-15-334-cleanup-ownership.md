# Prover record — ROADMAP 334 / INV-162 (cleanup touches only what it owns)

- **Prover skill version:** product-prover under live-spec-base v1.0.17
- **Mode:** CROSS-LINK (single added invariant; seams against INV-157, INV-100, base rule 17, and the `check-broad-kill.sh` net)
- **Date:** 2026-07-15
- **Delta under review:** INV-162 body clause (PRODUCT_SPEC.md:661) + Formal-index row (line 2028); guardrail `guardrails/check-broad-kill.sh`; matrix M-311; gate j in `.github/workflows/gates.yml` + `guardrails/pre-push`; test `tests/test_broad_kill_guardrail.py`; build-pipeline worker-briefing guidance (SKILL.md:480–483)
- **Verdict:** NEEDS ANOTHER ITERATION. The LAW's prose is sound and well-grounded; the NET is weak. Four blocking net-coverage defects (F1–F4) plus one net-honesty defect (F5). The guardrail catches the exact incident and the obvious variants, but a broad kill slips past it four different ways, and the delete half of the stated class has no net at all.

## What was verified green (positives, by deed)

- Exact incident RED: `pkill -9 -f "chrome_crashpad_handler"` + `pkill -9 chrome` → guardrail exits 1, message names INV-162. The net is honest on the founding incident.
- Variants RED: `killall Chrome`, `killall "Google Chrome"`, and the python form `subprocess.run(["pkill","chrome"])` all red (the `[^;&|]*` window spans the comma inside a subprocess arg list).
- Legit path-scoped kill PASSES: `pkill -9 -f "$HOME/.cache/puppeteer/chrome/.*chrome"` → exit 0.
- Traceability intact: M-311 present (TEST_MATRIX.md:489, BUILT), gate j wired in both `gates.yml` and `guardrails/pre-push` (lines 69–70), build-pipeline carries the constraint (SKILL.md:480–483), the test asserts the worker briefing carries INV-162, Formal-index homes list is complete.
- Seam with INV-157/INV-100: INV-162 is a faithful GENERALIZATION of the harness's own owner-liveness reap — reap only your own process group, sweep only a dead-owner dir. No contradiction in spirit. (One wording friction — see F7.)

## Findings

| id | headline | kind | blocking | folded / rejected |
|----|----------|------|----------|-------------------|
| F1 | Scoped-allowlist false-positive: a broad kill passes if a path substring appears anywhere on the line | defect · boundary-issue (composition) | BLOCKING | |
| F2 | Net misses `kill $(pgrep chrome)` / `kill $(ps\|grep chrome)` — a broad name-kill via kill+pgrep/ps | defect · missing-scenario (state-space) | BLOCKING | |
| F3 | Repo-scan glob excludes `.js/.ts/.mjs/.cjs` — the puppeteer/Playwright teardown the law names is outside the gate | defect · boundary-issue (composition) | BLOCKING | |
| F4 | The delete/rm half of the stated class has no net at all | defect · missing-rule (invariant) | BLOCKING | |
| F5 | The "greps a brief" half of the net-claim is unbacked — no mechanical check greps a worker brief | defect · unenforceable-promise (discharge) | BLOCKING | |
| F6 | Variable-built kill (`PROC=chrome; pkill "$PROC"`) evades the regex | recommendation | no | |
| F7 | "THIS run provably created and owns" headline is narrower than INV-157's cross-run launch sweep | recommendation | no | |

---

### F1 — A broad kill passes the gate if any path substring appears anywhere on the line

> `SCOPED='\.cache/puppeteer|user-data-dir'` … `grep -nE "$FORBIDDEN" "$1" | grep -vE "$SCOPED"` — `guardrails/check-broad-kill.sh`

The allowlist filters out any FORBIDDEN-matching line that *mentions* `.cache/puppeteer` or `user-data-dir` anywhere on the line — it does not check that the path is the kill's TARGET. Verified: `pkill -9 chrome  # cleanup ~/.cache/puppeteer leftovers` → exit 0 (passes). A worker or a careless script that writes a bare `pkill chrome` and happens to carry a path token on the same line — a trailing comment, an echo, a second `--user-data-dir` flag in a multi-flag command — evades the gate entirely. The founding incident line itself, had it read `pkill -9 chrome # under user-data-dir`, would go green. This is the attacker-shaped bypass the pass was told to hunt.

Make the scope check bind the path to the kill target: require the path to appear as the argument of `-f` (e.g. match `pkill[^;&|]*-f[^;&|]*(\.cache/puppeteer|user-data-dir)`), not merely somewhere on the line. Anything killing a browser name with the path elsewhere reds.

`defect · boundary-issue (composition)`

### F2 — A broad name-kill via `kill $(pgrep …)` / `kill $(ps | grep …)` is invisible to the net

> `FORBIDDEN='(pkill|killall)([^;&|]*)(chrome|Chrome|crashpad|puppeteer)'` — `guardrails/check-broad-kill.sh`

The regex only matches `pkill`/`killall`, but the law forbids *any* broad name pattern. `kill -9 $(pgrep chrome)` and `kill $(ps aux | grep -i chrome | awk '{print $2}')` resolve the human's real Chrome PIDs by name and `kill -9` them — exactly as destructive as `pkill chrome` — and both pass the gate (verified, exit 0). The `pgrep`/`ps|grep` route is the idiomatic cross-platform substitute for `pkill`, so this is not an exotic path.

Extend FORBIDDEN to catch a name-resolving kill: add `pgrep` and `ps … grep` feeding a `kill`, i.e. red a line where `pgrep`/`ps`+`grep` names a browser and the same or a piped line kills it. At minimum red any `pgrep|pkill|killall` naming a bare browser token, scoped or not.

`defect · missing-scenario (state-space)`

### F3 — The push-gate scan skips `.js/.ts/.mjs/.cjs`, where the puppeteer/Playwright teardown actually lives

> `done < <(git ls-files '*.sh' '*.py' 'scripts/*' 2>/dev/null)` — `guardrails/check-broad-kill.sh` (the no-arg repo scan, the mode CI and pre-push run)

The regex itself would red a JS teardown — verified: passing `teardown.js` containing `execSync("pkill -9 chrome")` directly reds. But the gate never feeds it one: the repo scan globs only `.sh`, `.py`, and `scripts/*`, and the directory branch's `find` adds only `.txt`/`.md`. The law explicitly names `puppeteer` and Chrome-for-Testing — a JavaScript/TypeScript ecosystem whose global-teardown and cleanup scripts are `.js/.ts/.mjs/.cjs`. So the file type most likely to carry the footgun in a consuming project is outside the net, and a consumer's `package.json` scripts, a `Makefile`, or a `.yml` step are unscanned too.

Add `*.js *.ts *.mjs *.cjs *.yml *.yaml Makefile package.json` to the `git ls-files` set (and mirror them in the directory-branch `find`), so the scan covers where a browser teardown is actually written.

`defect · boundary-issue (composition)`

### F4 — The delete / temp-purge half of the stated class has no mechanical net

> "a temp purge, anything that removes or kills … the class is any shared resource — a process, a temp directory, a port, a file, a lock, the display" — PRODUCT_SPEC.md:661; "net — a guardrail greps a brief or script for a forbidden broad kill pattern" — Formal-index row, line 2028

The law's class is any shared resource and any *removal*, but the only named net greps kill patterns. `rm -rf /tmp/shared-cache` — a broad temp purge that wipes a sibling session's temp home — passes the guardrail (verified, exit 0), and there is no other net for it: INV-100's before/after temp-home diff is the pack's *own* suite catching *its own* test leaks, not a script that deletes a shared dir. Under the INV-160 parity every suite-honesty member names a net that reds a run on the violation; here the named net covers only the kill fraction of the class it declares, so the delete case is a stated law with no teeth.

Choose one: (a) add a delete leg to the guardrail — red an `rm -rf`/`find -delete` whose target is a shared/absolute path not proven owned (a recorded temp root or `$TMPDIR` prefix); or (b) narrow INV-162's declared class in the Formal index to "a broad browser-KILL" and move the temp-directory/file/lock removal cases under INV-100's hygiene net with their own diff. Preference: (a) — the incident class is "cleanup destroys a shared resource," and delete is squarely in it.

`defect · missing-rule (invariant)`

### F5 — The net claims to "grep a brief," but no mechanical check reads a worker brief

> "net — a guardrail greps a brief or script for a forbidden broad kill pattern and reds" — Formal-index row, line 2028; PRODUCT_SPEC.md:661 ("a guardrail greps a brief or a script")

The guardrail scans `git ls-files` — tracked scripts only. A worker brief is ephemeral text handed to a spawned agent, never a tracked file, so nothing mechanical greps it. Worker coverage is prose-only: build-pipeline's worker-briefing guidance (SKILL.md:480–483) tells a worker the constraint, which is a soft net, not the mechanical grep the clause claims. Under the INV-160 "each names its net" parity this is a member naming a net it does not have.

Reword the net-claim to what exists: the SCRIPT half is the mechanical guardrail (blocking in CI/pre-push); the BRIEF half is the build-pipeline briefing plus the prover's read — a soft net, not a grep. Or, if a brief-grep is truly wanted, name the surface it would scan (a deposited brief file under a tracked path) so the claim is dischargeable.

`defect · unenforceable-promise (discharge)`

### F6 — A variable-built kill evades the regex

> `FORBIDDEN='(pkill|killall)([^;&|]*)(chrome|Chrome|crashpad|puppeteer)'` — `guardrails/check-broad-kill.sh`

`PROC=chrome; pkill "$PROC"` passes (verified, exit 0): the browser token is in a variable, not adjacent to `pkill` on the kill line. This needs deliberate indirection, so it is lower-likelihood than F1–F3, but it is a clean bypass of an intentional footgun and worth a note. Full coverage of indirection is not tractable by grep; a lint that flags a `pkill`/`killall` whose target is a bare variable (not an `-f` path literal) would raise the bar. Queue as a taste call.

`recommendation · later · boundary-issue (composition)`

### F7 — The "THIS run created and owns" headline reads narrower than INV-157's own launch sweep

> "acts only on what THIS run provably created and owns" — PRODUCT_SPEC.md:661; vs INV-157: "on launch it also sweeps any stale process group a previous run left behind"

Read literally, INV-162's headline forbids INV-157's launch sweep, which reaps a *prior* run's orphan group — a resource this run did not create. The body reconciles it ("a recorded owner marker … sweeps only a profile dir whose recorded owner is dead"), so the intent is owned-lineage-with-dead-owner, not strictly this-run. But a reader applying the headline class would flag the harness's own sweep. Add the owned-lineage/dead-owner case to the class sentence so the generalization is airtight and INV-157 is visibly an instance, not an exception. Not blocking — the body already carries the reconciliation.

`recommendation · later · internal-conflict (consistency)`

## On the two adversarial questions posed

- **"provably owns" — defined enough?** For the KILL case, yes: the law names concrete owned-identity forms (recorded PID, process group, install path such as `~/.cache/puppeteer`, lock file, open handle, recorded owner marker) and an operational rule (unprovable ownership → left untouched). It is not hand-wavy. The one soft edge — "unprovable ownership left untouched" risks strays accumulating forever — is closed by INV-157's marker (ownership is made provable at launch), so the pair is coherent. See F7 for the wording friction.
- **Does the law cover DELETE as well as KILL?** The law's PROSE does (temp purge / file / lock / temp dir are in the stated class). The NET does not — F4. So the gap is net-coverage, not law-coverage.

## Net-honesty verdict on the guardrail

Honest on the exact incident and the obvious `pkill`/`killall` variants (RED, verified). Weak on four axes: the allowlist matches line-mention not kill-target (F1), the `kill $(pgrep …)` route is unmatched (F2), the JS/TS/yaml teardown files are unscanned (F3), and the delete half is unnetted (F4). The founding incident is caught; a mildly-obfuscated or JS-hosted version of it is not. Fold F1–F4 before the clause's "a guardrail reds a forbidden broad kill" claim is true across the class it names.
