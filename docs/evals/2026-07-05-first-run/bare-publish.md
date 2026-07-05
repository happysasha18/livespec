# Bare run — publish scenario (2026-07-05, Sonnet worker, tool uses: 0)

Verbatim output:

---
1. Scan the working tree and full git history for secrets, API keys, tokens, personal file paths (e.g., `/Users/<name>/...`), emails, or other identifying data; scrub or rewrite history if anything is found.
2. Scan test fixtures and sample data for copyrighted MIDI files (real commercial songs) — replace with original/royalty-free or synthetic test MIDI if any real copyrighted material is present.
3. Remove all hardcoded local paths, machine-specific config, and debug artifacts (print statements, commented-out code, personal TODOs) from the codebase.
4. Add a `.gitignore` covering venv/virtualenv, `__pycache__`, `.DS_Store`, build artifacts, local output/cache directories, and any local test-output files.
5. Add packaging metadata (`pyproject.toml` or `setup.py`) with a proper CLI entry point, so it's pip-installable, and pin/declare dependency versions in a requirements file.
6. Run the full test suite fresh in a clean virtualenv (not just "works on my machine") to confirm it passes with no hidden local dependencies.
7. Check all third-party dependency licenses are compatible with public release (no GPL-in-permissive conflicts, etc.).
8. Write a README: what it does, install steps, usage examples with real (not synthetic-labeled) sample output, and any limitations.
9. Choose and add a LICENSE file.
10. Decide repo hygiene: whether to add a GitHub Actions CI workflow to run tests on push (optional but recommended for a public repo).
11. Check the name "chordscan" isn't already taken on GitHub/PyPI in a conflicting way.
12. Tag an initial version (e.g., v0.1.0) before or right after the first public push.
13. Create the GitHub repo under the intended account, set visibility to public, add description/topics, push, then verify by cloning fresh into a throwaway directory and running install + tests from scratch as an outside user would.

Questions to ask the producer before publishing:
- Which GitHub account/org should it go under, and what name/handle should be credited as author?
- Which license do you want (MIT, or another)?
- Is it OK to include the current test MIDI files publicly, or should any be swapped out (copyright)?
- Do you want CI (GitHub Actions) running tests on every push, or keep it minimal?
- Anything in the tool you consider not-ready-to-show or want held back from this first public version?
---
