# ADLC Journal

Edit history lives here — the WHY behind every change. The spec and README state current truth; this file explains how we got there.

---

## 2026-07-04 — Package born

**What:** Created the ADLC skeleton repo — directory structure, four bundled skills, templates, adopt procedure, guardrails outline, install script.

**Why:** The method (spec → prove → reconcile → matrix → test → code → verify → commit) has been running in production on track-coach for over a year and is proven. It lives scattered: CLAUDE.md rules, four skill repos, a playbook, and a habit. The goal of ADLC is to make the whole thing one attachable package — clone it, run `./install.sh`, and the skills land in `~/.claude/skills/` ready for any project. One home, not four.

**Why "ADLC":** Alexander's coinage (2026-07-04). Working name; a better name may emerge (queued in ROADMAP).

**Status:** Skeleton only. Skills are read-only copies (source repos unchanged). No SPEC authored yet — that waits for Alexander's signal to publish, so spec-author runs on the full intended scope, not a moving target. Unpublished; local only.

**Decided:** Local-only for now. No GitHub creation, no push. When Alexander says publish, that is ROADMAP item 1 — create the repo, push, wire the skill install to the real source.
