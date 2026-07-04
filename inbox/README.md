# inbox — parallel-safe wish intake

The one door into this repo for a session NOT assigned to livespec itself (a host's adopt run, any passing
conversation). Such a session may do exactly one thing here: **create one NEW file per wish**. It never edits
the spec, the queue, the journal, the skills — and never an existing inbox file (SPEC INV-10).

Why a folder of files: creating a fresh file cannot collide with anyone; editing a shared file can.

**Format:** `YYYY-MM-DD-<source>-<slug>.md` — a few plain lines:
- the wish, in plain words
- why (what broke / what was missing, with the primary source if there is one)
- who threw it (which host / which conversation)

The next livespec session harvests each file into a ROADMAP row and removes the file in the harvest commit
(git history keeps it).
