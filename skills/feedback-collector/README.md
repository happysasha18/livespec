# feedback-collector

**On a rare, genuinely strong reaction, offers — with your explicit yes — to draft a short private note to the pack's authors about what happened. Off by default, never sends on its own. A [Claude Code](https://claude.com/claude-code) skill, part of the [live-spec pack](https://github.com/happysasha18/live-spec).**

Sometimes a moment lands hard — a real delight, a real frustration. This skill notices such a moment and offers to draft a short **upstream note** to the people who wrote the pack, so they learn what worked or what hurt in real use. It asks first, every time; it drafts privately; and it never sends — delivery stays your own step.

It is the third of the pack's feedback directions. The [communicator](https://github.com/happysasha18/live-spec/tree/main/skills/communicator) skill carries work out to you. The [feedback-intake](https://github.com/happysasha18/live-spec/tree/main/skills/feedback-intake) skill carries what you hand back. This skill carries an occasional note up to the authors.

This skill ships inside the live-spec pack. Install the pack to get it. Used on its own, this README reads as plain advice about sending feedback upstream.

---

## Off by default

The arm does nothing until a host turns it on with one recorded line in its profile:

```
- `feedback-upstream: on`   # this host sends occasional notes up to the pack's authors (dated)
```

A host that adopted the pack turns it on to send notes up. The authors' own machine leaves it off — there is no upstream above it. Off means the arm reads nothing, offers nothing, stays silent.

---

## What it does, in four moves

1. **Notices** one genuinely strong, unmistakable reaction — rare by design, silent on anything mild or routine.
2. **Offers**, in one line, to draft a note to the authors — and asks for an explicit yes. A silence or an unclear answer leaves the note unwritten.
3. **Drafts** a short, distilled, non-public note that carries its own context — the point of what happened, never the transcript, never your private content.
4. **Deposits** it into a gitignored `outbox/`. It never sends. Delivery upstream is your own step, however you choose.

---

## What it is not

- **Not [feedback-intake](https://github.com/happysasha18/live-spec/tree/main/skills/feedback-intake).** That receives what you hand in and files it. This notices a strong moment and offers to carry a note up. Opposite directions.
- **Not a measurement machine.** It reads one moment and offers. It does not score, grade, or aggregate sentiment.
- **Not an auto-sender.** No yes, no note. Even on a yes, it deposits — it does not send.

---

## Install

Install the [live-spec pack](https://github.com/happysasha18/live-spec); this skill ships inside it. Then, on any host that wants to send notes up, add `` `feedback-upstream: on` `` to that host's `.live-spec/profile.md`.
