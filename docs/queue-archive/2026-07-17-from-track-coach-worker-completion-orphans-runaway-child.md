# feedback: a worker's completion should also reap its spawned OS subprocesses

**The item (a worker-hygiene rule for the pack's orchestration).** When a subagent finishes, that
signals the AGENT is done; the OS processes it spawned can still be alive. The pack should treat worker
teardown as two separate duties: the agent completes, AND its process group is reaped so no orphaned
child survives it. Alongside, a detection habit worth stating: when a status line shows a worker as
running while its output file has gone idle, the truth lives in `ps` — look for a child process at high
CPU, confirm by the output file's mtime, then reap the scoped process group (`kill -TERM -<pgid>`) after
checking only the orphan's PIDs share it.

**Why (what happened, 2026-07-17, track-coach s77).** A background worker doing a library regression
re-render returned its full result and finished ~48 minutes before it was noticed. Its status line still
read "running 12m10s", and the owner saw it as live. The real cause was an orphaned child: the worker had
launched `difflib.SequenceMatcher(None, a, b, autojunk=False)` over a widget's ~500 KB single-line data
blob — quadratic on that one line, so effectively unbounded — and that child was left behind when the
worker completed through a different diff path. It burned a full CPU core at 100% for 46 minutes doing
work nobody would read. A scoped process-group kill cleared it.

**Two things the pack could carry from this.** First, reap a worker's process group at teardown so a
heavy or blocked child (a pathological diff, a hung heredoc, a stuck browser) cannot outlive the agent.
Second, a plain caution for worker code: comparing giant single-line payloads wants a parsed field-diff;
`SequenceMatcher(autojunk=False)` on a ~500 KB line is a foot-gun.

**Who threw it.** track-coach window (this Mac), session s77, 2026-07-17. Kin to the pack's existing
worker-liveness-via-mtime note and the scoped-reap rule for test browsers.
