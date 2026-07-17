#!/usr/bin/env python3
"""cleanup_notice.py — the shared shape for "a cleanup says what it ended" (SPEC INV-204, ROADMAP 417).

Every process this pack ends is reported with WHAT it was and WHY the run owned it — the PID, the
process group, or the owned path that proves ownership. An ending nobody expected then becomes visible
the moment it happens, rather than at the next unexplained loss of the person's work. This is the
minimum owed on a machine shared with someone who runs the same programs the pack does (python and its
Demucs, node, ffmpeg are live siblings of the proven chrome case), and it is what makes INV-162's
stricter form safe to land: the notice shows what the strict check would have refused before the strict
check starts refusing.

This module is the pack-side shared shape a cleanup path emits through. A vendored, standalone script
that cannot import the pack (the headless-harness template is one) carries its own inline emitter
printing the same `CLEANUP-NOTICE` marker line — the marker is the one fact the gate keys on, and its
one home is here.

The gate `guardrails/check-cleanup-notice.sh` reds any tracked cleanup path that ENDS a process without
emitting the notice.

The line's shape:
  CLEANUP-NOTICE ended=<ended> what=<what> owned-via=<owned_via>
  * ended     — the identity ended: a `pgid=<n>`, a `pid=<n>`, or a path.
  * what      — what it was, in plain words (e.g. "chrome (test browser this run launched)").
  * owned-via — the proof the run owned it: the recorded PID, the process group the run holds, or the
                path under the run's own tree.
"""
import sys

MARKER = "CLEANUP-NOTICE"


def cleanup_notice(ended, what, owned_via, out=None):
    """Emit one notice line naming what was ended and the proof the run owned it.

    Written to stderr by default so it lands beside the run's own diagnostics and never pollutes a
    tool's stdout. Returns the emitted line.
    """
    if out is None:
        out = sys.stderr
    line = "%s ended=%s what=%s owned-via=%s" % (MARKER, ended, what, owned_via)
    try:
        out.write(line + "\n")
        out.flush()
    except Exception:
        pass
    return line


if __name__ == "__main__":
    # A tiny self-check: `cleanup_notice.py ENDED WHAT OWNED_VIA` prints the line, so the shape is
    # exercisable on demand the way the other shared shapes are.
    a = sys.argv[1:]
    cleanup_notice(a[0] if len(a) > 0 else "pgid=0",
                   a[1] if len(a) > 1 else "(unnamed)",
                   a[2] if len(a) > 2 else "(unproven)",
                   out=sys.stdout)
