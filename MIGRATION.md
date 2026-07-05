# MIGRATION — livespec → live-spec (2026-07-05)

Alexander renamed the package on 2026-07-05: **livespec → live-spec** (hyphen), one name everywhere.
GitHub redirects keep old clone/remote URLs working after the repo rename, but every adopted host
carries the old name in a few places. This note is what a host's own session executes at its NEXT
update — nothing outside a host's own session ever writes that host's repo.

For each adopted host (at its next update session):

1. `git mv .livespec .live-spec` — the host's pack folder (profile, checkpoints, installed-versions
   record, adopt artifacts) keeps its history.
2. Sweep the host's own docs for `livespec` references (SPEC/ROADMAP/JOURNAL pointers to the pack,
   skill names in text) → `live-spec`; the host's JOURNAL history entries stay as written.
3. Re-record the installed skill set in `.live-spec/` — the base skill is now named `live-spec-base`.
4. Update the git remote URL at leisure: `git remote set-url ... live-spec.git` (the redirect works
   meanwhile).
5. One machine-level move, once per machine, not per host: `~/.claude/livespec/` (personal profile)
   → `~/.claude/live-spec/`, and the installed skill folder `~/.claude/skills/livespec-base` →
   `~/.claude/skills/live-spec-base`.

Journal the migration in the host's JOURNAL.md with date and time.
