# The waiting list

TOUCHPOINT-KIND: waiting-list

Chat scrolls, and a question parked for you or an answer you never saw scrolls away with it. This file
is where they wait instead. It lives at the top of the project so it is always one glance away, and it
renders into a readable page through `scripts/render-doc.py` when you want to look.

An item clears only when you acknowledge it. Nothing here is ever dropped on a timer: an answer you have
not read stays until you read it. When the top of the list is full, the oldest item there moves down
into the list below, whole and alive — it is never deleted. An item you acknowledge, or one a later
answer supersedes, moves to the attic with a line recording what it was.

Your status answer prints what is at the top, in front of you, and adds one line naming this list — how
many items it holds and that it opens whenever you ask. [[wait]]

The list opens on request, and the first time it does it will show you how it works: an item waits until
you acknowledge it, and you can ask for the whole list any time. [[teach]]

## In front of you
<!-- board:shown -->
(nothing waiting)

## The rest of the list — opens on request
<!-- board:list -->
(nothing waiting)

## Cleared to the attic — on your acknowledgement
<!-- board:attic -->
(nothing cleared yet)

## Moved from the top into the list — nothing vanishes
<!-- board:demotions -->
(nothing demoted yet)
