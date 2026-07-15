"""Behavioural net for the harness's launch sweep (ROADMAP 333, prover F2) — the age-based reap DELETES
directories, so its young/old/live/dead discrimination is proven BY DEED here, not only by a string grep.

The template is importable (no side effects beyond locating Chrome). We monkeypatch its `_temp_roots` to a
controlled dir, plant the four cases, and assert the sweep reaps exactly the provably-not-in-use ones and
leaves a live run's dir and a young ownerless dir untouched. This is the net a directory-deleting cleanup
owes under INV-162 (never a shared resource in use). Landed 2026-07-15."""
import importlib.util
import os
import time
import tempfile
from conftest import ROOT

_spec = importlib.util.spec_from_file_location(
    "headless_harness", os.path.join(ROOT, "templates", "headless_harness.py"))
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)


def _mkdir(root, name):
    p = os.path.join(root, H.PROFILE_PREFIX + name)
    os.makedirs(p)
    return p


def _mark(path, pid, boot):
    with open(os.path.join(path, H.OWNER_PID_FILE), "w") as f:
        f.write("%s\n%s\n" % (pid, boot))


def _backdate(path, seconds_ago):
    t = time.time() - seconds_ago
    os.utime(path, (t, t))


def _dead_pid():
    # a pid that is not alive: allocate one by spawning `true` and reaping it, then reuse its number.
    import subprocess
    p = subprocess.Popen(["true"])
    p.wait()
    return p.pid


def test_sweep_reaps_only_the_provably_not_in_use(monkeypatch):
    boot = H._boot_id()
    with tempfile.TemporaryDirectory() as root:
        monkeypatch.setattr(H, "_temp_roots", lambda: [root])

        young_ownerless = _mkdir(root, "young_ownerless")          # no marker, fresh → survives
        old_ownerless = _mkdir(root, "old_ownerless")              # no marker, old   → reaped
        _backdate(old_ownerless, H.OWNERLESS_STALE_AGE + 600)
        live_owner = _mkdir(root, "live_owner")                    # our own live pid → survives
        _mark(live_owner, os.getpid(), boot)
        _backdate(live_owner, H.OWNERLESS_STALE_AGE + 600)         # old, but owner is ALIVE → survives
        dead_owner = _mkdir(root, "dead_owner")                    # dead pid, same boot → reaped
        _mark(dead_owner, _dead_pid(), boot)

        H._sweep_stale_profiles()

        assert os.path.isdir(young_ownerless), "a young ownerless dir (a possible live sibling) was reaped"
        assert not os.path.isdir(old_ownerless), "an old ownerless dir (killed-run litter) survived"
        assert os.path.isdir(live_owner), "a LIVE run's dir was reaped — the F1 failure"
        assert not os.path.isdir(dead_owner), "a dead-owner dir survived"


def test_sweep_never_reaps_the_current_run_exclude(monkeypatch):
    # the running browser passes its own profile as `exclude`; the sweep must never touch it.
    with tempfile.TemporaryDirectory() as root:
        monkeypatch.setattr(H, "_temp_roots", lambda: [root])
        mine = _mkdir(root, "mine_current")
        _backdate(mine, H.OWNERLESS_STALE_AGE + 600)               # old + ownerless, but it is excluded
        H._sweep_stale_profiles(exclude=mine)
        assert os.path.isdir(mine), "the sweep reaped the current run's own excluded dir"
