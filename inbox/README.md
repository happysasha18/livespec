# inbox — parallel-safe intake for wishes and feedback

The one door into this repo for a session NOT assigned to live-spec itself (a host's adopt run, any passing
conversation). Such a session may do exactly one thing here: **create one NEW file per item** — a wish or a
piece of feedback. It never edits
the spec, the queue, the journal, the skills — and never an existing inbox file (SPEC INV-10).

Why a folder of files: creating a fresh file cannot collide with anyone; editing a shared file can.

**Format:** `YYYY-MM-DD-<source>-<slug>.md` (name taken? append `-2`, `-3`, … — the pack's one collision law, base rule 18; two sessions racing one slug: add a short session token to the source mark) — a few plain lines:
- the item, in plain words (a wish, a reaction, an answer, a report)
- why (what broke / what was missing, with the primary source if there is one)
- who threw it (which host / which conversation)

Commit your one new file (a commit touching inbox/ only, message naming the source) — that commit is part
of the exception. A live-spec session sweeps this folder as its first act, harvests each file into the home
its route owns (a wish into a ROADMAP row, feedback by the routing law — SPEC T-20), and removes the file
in the harvest commit (git history keeps it).

**From a remote seat, over git.** A remote seat reaches a repo only through git, so it also pushes.
The deposit stays one new file here, committed touching inbox/ only with the source named, and then pushed
under a per-repo grant recorded in the host profile like the push grant. A seat with no grant fails honestly:
it names the grant it lacks and hands the owner the one action that supplies it (SPEC INV-112).
