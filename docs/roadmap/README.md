# atelier ROADMAP — the board

**One file per item** (board-store ADR, Mike ruled 2026-08-15). Each item lives
in `<NNN>-<section>/<NNN>-<slug>.md`: its checkbox line first, detail beneath,
its own `git log` as provenance — which commit flipped its state, and what work
that commit carried. Each section's narrative lives in that section's
`README.md`. [`../ROADMAP.md`](../ROADMAP.md) is the **generated index**
(`tools/board.py`; the `board` floor check blocks a commit whose index is stale
— on CI always, at the hook only for what was staged to match the worktree —
and after a merge conflict on the index, rebuilding *is* the resolution). The
session-start read is the index; open item files on demand. Completed detail
from before the split lives frozen in [`../ROADMAP-DONE.md`](../ROADMAP-DONE.md);
a done item now simply stays in its file as `[x]` — there is no harvest step.
Sequencing rule from the 2026-07-10 review still binds: **mechanism before more
content** — a repo that inherits docs but not the propagation + review cadence
has inherited the costume, not the doctrine.

Checkbox states — a **work-owed tri-state**, never a disposition (Mike's
ruling, 2026-07-**23**; the 2026-07-22 date this legend carried until
2026-08-19 was the day the *question* was captured, not the day it was
answered — `310/080`): `[ ]` work still owed · `[x]` **no more work owed** — delivered,
superseded, or declined, with the disposition said in the item's own text (a
dated note), never a fourth bracket · `[~]` **claimed** by a live parallel
session — `(claimed <date>-<HHMM>, wt: <branch>)`, optionally extended in place
with a resume breadcrumb (`· at: <step>` — CONCURRENCY § Surviving an
interrupted session) — don't start a `[~]` item;
take the next open one (`method/CONCURRENCY.md` § Claiming work) ·
`⏳` **review queued** for a non-author to take — any spawner passing rule 4's
criterion may take it, **on the principal-named review tier (currently
Fable): tier is checked at selection, and a session that cannot honour the
bar stops rather than takes**; the taker writes the brief
(`method/REVIEW.md` rule 4).
**The pointer is refs only** — name the delta and the intent record, no
evaluative account; the account lives in the session record, so a taker meets
the work cold (REVIEW.md rule 4's ceiling, stated here at the point of use).
And the delta list stays *complete*: a later commit that touches a queued
delta's doctrine surfaces — even for hygiene — widens the pointer's delta
list in the same commit (AW6 ruling, 2026-07-23). The pointer itself is
queued **in the commit that lands the work** — landing = queuing, so no
window exists where landed doctrine sits unpointed and untracked (AWA2
ruling, 2026-07-23; its enacting batch exercised exactly that window). The same
landing-equals-bookkeeping rule binds the other two state changes (enacted
2026-08-03; the split board simplifies both): a `[x]` flips **in the item's own
file, in the commit that finishes the work** — the old rule's second half, "and
its harvest to `ROADMAP-DONE.md` in the same commit", is retired because the
harvest itself is (its red-window failure mode — 2026-07-26: `d847866` red,
`0485540` green — goes with it). And an **inline claim** (`wt: none`) **closes
in the commit that lands its work** — a worktree merge forces a return to the
item's file, an inline claim has no such forcing step, and the one item that
skipped the worktree skipped its close with it (2026-07-26, cleared hours after
`b89a306` had shipped). State changes rebuild the index **in the same commit**
— the `board` check makes that mechanical, not remembered.
