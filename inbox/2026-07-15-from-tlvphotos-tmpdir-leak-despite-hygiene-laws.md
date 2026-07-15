# Incident wish — a 78 GB $TMPDIR leak got past the test-hygiene laws

- **From:** tlvphotos window, 2026-07-15 ~20:15
- **Kind:** wish / incident (the pack's own test-hygiene + harness laws have a hole this exposed)
- **Severity:** high — it silently degrades every long test session on the machine to false reds, then a meltdown

## What happened

During a long tlvphotos session (many gesture-suite runs, many of them killed/timed-out by the known
CDP flakes), the machine's `$TMPDIR` (`/var/folders/.../T/`) grew to **78 GB** of stale test temp:
hundreds of `tlv_<suite>_*` harness dirs (per-suite baked site + Chrome user-data-dir) plus
`.com.google.Chrome.*` / `com.google.Chrome.scoped_dir.*` profiles. The bloat starved and slowed Chrome:
full `--jobs 4` gates cascaded to 17/37, and even a **serial `--jobs 1`** gate came back 15/37 with
`door: TimeoutError` and pages booting partially — on identical code that had passed 36/37 forty minutes
earlier. It read as a code regression; it was the environment. Clearing the stale temp dropped `$TMPDIR`
78 GB → 2.2 GB and (verifying now) restores the gate. So the failure was invisible: nothing said "your
temp dir is full," the reds just looked like product breakage and cost a long detour.

## Why the existing laws did not catch it

The pack already states two relevant laws, and each has a precise hole:

1. **Row 222 / INV-100 (test-hygiene, "a suite leaves the machine as it found it").** Its own NON-GOAL
   says it does *not* sweep the system temp dir's pre-existing litter, "macOS purges it; only our prefix
   is watched." That assumption is false on macOS: `$TMPDIR` under `/var/folders` is NOT promptly purged —
   it survives across runs and across days, so pre-existing `tlv_*` litter accumulates unbounded. The
   before/after diff watches only the current suite's own prefix, so litter that an EARLIER killed run
   orphaned is never seen.

2. **The teardown cleanup is skipped exactly when a suite is killed or times out** — the precise condition
   under which temp is most likely to be orphaned. Row 327's own adversarial pass already found this shape
   for PROCESSES ("teardown reap skipped on a killed run") and fixed the reap to be unconditional. The same
   fix was never applied to the harness's TEMP DIRS. This makes a vicious cycle: flakes → killed suites →
   skipped temp cleanup → a fuller temp dir → more flakes.

3. **Row 327 / INV-157/158 (the canonical hardened harness with a boot-aware launch sweep) exists in the
   pack v1.7.0 (landed today) but the consumer had not adopted it** — tlvphotos runs the older pack (1.4.2),
   so it has no launch sweep at all. And even row 327's sweep, as described, targets a run's own crash
   leftovers, not the whole day's accumulated `tlv_<suite>_*` dirs.

## Suggested sharpening (the owner decides)

- **Fix the false assumption in INV-100's non-goal:** `$TMPDIR` on macOS is not self-purging; the harness
  owns its litter there and must remove it, not rely on the OS.
- **Make temp cleanup unconditional, like the process reap** — a temp dir is created under a guaranteed-cleanup
  context (try/finally + atexit + a tracked registry), so a killed/timed-out suite still frees its dir.
- **Add a startup sweep by prefix, age-bounded:** at the top of a run, the harness deletes every
  `tlv_<suite>_*` / Chrome temp dir older than the current invocation (a boot-aware sweep of ALL stale
  litter, not only this crash's). This is the one defense that survives kills regardless.
- **Surface the condition:** a run whose `$TMPDIR` (or the harness prefix) exceeds a threshold logs a loud
  line, so a full temp dir never masquerades as product reds again.
- **Close the adoption lag:** tlvphotos (and exhibition-engine) should adopt the pack's v1.7.0 harness
  template so the fix arrives by update, not by a hand-carried wish — this incident is the case for it.

The tlvphotos-side stopgaps are already owned in its own `.live-spec/PROBLEMS.md` (the glide-timing flake,
and this temp leak); this wish is only the pack-level generalization the owner may want to fold.
