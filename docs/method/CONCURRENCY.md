# Concurrency — running several lines of work at once, safely

The goal: build, test, document and ship more than one thing at a time without
the parallel lines corrupting each other or stepping on the live world. This is
the bulkhead principle (a failure in one partition can't cascade) applied to
*time* instead of to devices.

## The substrate: one worktree per line of work

Never run parallel work in a single working tree — two sessions editing the same
files race the git index and stomp each other's changes and test runs. Instead,
each independent line of work gets its **own git worktree**: its own checkout,
its own branch, off the same repo.

```sh
git worktree add ~/worktrees/<repo>-<feature> -b <feature>
```

- Worktrees live **outside iCloud** (`~/worktrees/…`) to avoid sync churn; the
  external venv is shared across them, which is what you want.
- Each parallel session = one worktree = one branch = one session-log entry that
  names its worktree and branch.
- They reconcile on `main` via PR/merge. `main` is the integration point; the
  worktrees are where divergence is allowed to happen.

## The trigger — knowing a session is the second one

The substrate rule only fires if a session *knows* it is concurrent. The gap
in practice was never the rule but the cue: git protects concurrent *commits*
(worst case a rejected push and a rebase), but nothing protects the
**uncommitted working tree** two sessions share — session B can overwrite
session A's in-flight edits or sweep them into its own commit, and nothing
errors. Two cues, both cheap, no locking machinery:

- **Say so at open (primary):** when the principal knows they are opening a
  second session on a repo already in use, they say so, and that session works
  in a worktree from its first action. The harness has native worktree
  support, so the ceremony is near-zero.
- **Dirty-tree backstop:** a session that finds uncommitted changes it did not
  make assumes another session is live and moves itself to a worktree. Never
  work around a stranger's in-flight edits and never absorb them into a
  commit — that silently merges two intentions, the exact clobbering this
  doctrine exists to prevent.

*Bearing:* atelier sessions 45–46 (2026-07-12) — session 45 ran two parallel
sessions in the same checkout and needed a *survival audit* afterwards
(everything intact, history linear — that time); session 46 named the gap:
the worktree rule had existed since this doc was written yet never fired,
because nothing told a session it was the second one. Good habits (small
commits, pushed fast) were standing in for a rule with no firing condition.

## The solo default — trunk-based, no standing ceremony

One session alone on a repo commits to the integration branch directly: small
commits, pushed immediately. Branch-per-session for solo work costs more than
it buys — every branch demands the put-away ceremony below and adds a merge
step for zero isolation gain (there is nothing to be isolated *from*).
Worktrees are for known-parallel work, not a tax on every session.

## Two kinds of parallelism — use the right one

- **Parallel *sessions* (worktrees)** — for independent, long-lived lines of
  work you want to *steer* (feature A here, feature B there). Human-in-the-loop
  on each.
- **Background *agents* (fan-out)** — for breadth *within one task* that you then
  synthesise: multi-file reviews, research sweeps, "check these 20 things". The
  agents return results into one context you drive; they are not long-lived
  independent developers.

Rule of thumb: **agents for breadth-within-a-task; worktrees for
parallel-tasks.**

## The safety rail: serialise real-world side-effects

Builds may run fully in parallel. **Actions that touch the live world must
not.** Anything that changes a device, deploys, publishes, or spends is
**serialised and announced**, even when the builds that produced them ran
concurrently.

- Two worktrees may both *prepare* a change to the same live device; only one
  *applies* at a time, and it says so.
- This is the apex + the AUTONOMY floor holding across concurrency: parallelism
  is a build-time convenience, never a licence to double up on irreversible or
  outward actions.

*Bearing:* tiki already applies serially per device (parallel across devices,
serial within one); this doctrine generalises that discipline to every outward
action across every parallel session.

## Integration hygiene

- **Sync bookends** shrink the collision window the substrate can't cover
  (two sessions legitimately landing on the same integration branch):
  `git pull --rebase --autostash` at session start; push after each commit,
  not in a batch at session end.
- Append-tail files (session logs, changelogs) will conflict when concurrent
  sessions both append — that conflict is *expected and trivial*: keep both
  entries, chronological order, move on. Design shared records so this is the
  worst case they present.
- **Record identifiers are coordination-free — a counter is that conflict's
  silent sibling.** A next-N counter (session `NN`, ADR `NNNN`) is a shared
  resource git does not police: two sessions allocating from their own stale
  views create *differently named* files carrying the same number, so no merge
  conflict fires and the collision lands silently. So every record series —
  session logs, ADRs, review briefs, anything similar — uses one form,
  **`<date>-<HHMM>-<slug>`** (start time, 24-hour), built from facts the
  session already owns: no shared state, safe to allocate at session open,
  citable immediately, and same-day records keep their order. Structurally,
  the worst case collapses into the append-tail case above: two sessions
  wanting the *same name* is a visible git conflict, the trivial kind. A
  running number adds nothing over the date — chronology was the only meaning
  it carried (Mike's ruling, 2026-07-13) — and costs a standing discipline to
  keep unique: the counter-plus-discipline fix tried first (allocate at
  landing, first landed wins) was retired the same day it was written, because
  its audience — a repo not yet migrated — can only ever receive it via the
  pin bump that delivers this rule in the same block (the ADR's addendum
  carries that deliberation). Files named under retired schemes keep their
  names and citations — the record is append-only; never rename history.

  *Bearing:* ros 2026-07-13 — two parallel sessions each computed "next NN"
  from a stale view: one had taken 03, the other took 03 and 04. Nothing
  conflicted at merge; the duplicate surfaced only on human read-through and
  was fixed by renumbering 03→05. Allocation at session open, with the push
  hours later, was the whole window.
- Rebase/merge small and often; a worktree that diverges for days is a merge
  hazard.
- Delete a worktree when its branch lands (`git worktree remove`); stale
  worktrees are the concurrency equivalent of a leaked file handle.
- If two lines of work both need the same live resource, that's a signal to
  sequence them, not to build a locking scheme — KISS over cleverness.

## Claiming work — make selection collide like naming does

Sync bookends and worktrees protect the *tree*; nothing protects the *queue*.
Two sessions that both open on "the next thing in the roadmap" each
`pull --rebase`, both read the same item unclaimed, and both build it — no git
conflict ever fires, because neither mutated a shared thing. This is the
silent-collision class again, one rung up from the record-identifier case
above: there the duplicate was two files carrying one number; here it is two
sessions on one item, and the cost is whole sessions of wasted model time.

The fix is the same *shape* of move — **force the collision onto one shared
line so git catches it.** (Where coordination-free naming *avoids* the shared
resource, claiming deliberately *manufactures* one: the same trivial-conflict
worst case, the opposite lever on shared state.) A session claims a roadmap item
the moment it **selects it from the shared queue** — not when it enters a
worktree — by editing *that item's own checkbox line, in place*, then committing
and pushing the claim **before it does any work**:

```
- [~] REACH backlog H2 — scope cookie-export … (claimed 2026-07-13-2140, wt: atelier-reach-h2)
```

**Where the claim lands is load-bearing.** The claim commit goes to the
**integration branch every session rebases onto** (`main`), *before* creating or
entering the worktree — the claim is a direct-to-`main` commit even though the
work that follows is not. A claim committed on a feature/worktree branch is
invisible to every other session (separate branches' pushes never collide) and
the mechanism silently does nothing. So: **claim on `main`, then branch.**

- **Push succeeds** → the item is yours; now enter the worktree and work.
- **Push rejected** → `pull --rebase`. If another session claimed the *same*
  item, both edited that one checkbox line and the rebase stops on it — the
  trivial conflict kind. They pushed first, so they own it: drop your claim,
  take the next unclaimed item.
- **Different items** → *usually* no conflict, both proceed. Usually, not
  always: two claims on **adjacent** one-line items raise a trivial *keep-both*
  rebase conflict (git's three-line diff context overlaps) — keep both claims
  and move on. Only a *same-item* claim is a real yield; put the `[~]` on the
  item's **checkbox line** so a same-item collision always fires on one line,
  even for a multi-line item.

**This is not worktree ceremony.** A claim is one small commit on `main` —
exactly the trunk-based small-commits-pushed-immediately the solo default
already does; it does not pull a solo session into branch/put-away ceremony. A
genuinely-alone session claims too, and its claim simply never collides — that
is a feature, not waste: it is what lets a *later*-opening parallel session read
the item as already `[~]` instead of grabbing it out from under a session
mid-way through it. Because claiming keys on **selection from the shared
queue**, no session that picks work is ever outside it — closing the gap a
session which didn't *know* it was parallel used to leave open.

Two more properties:

- **The claim mutates the item in place — never appends to a claims list.** An
  append-tail "who's on what" file would let two same-item claims land as two
  different lines, and the collision goes silent exactly as the next-N counter
  did. Mutating the contested checkbox line *is* what forces the conflict; that
  is the whole design.
- **Fan-out needs the leaves to exist as their own lines.** Two sessions both
  told "do the reviews" fan out only if each review is *already its own
  claimable line*. A bundled or themed line (the lean-roadmap habit — e.g. eight
  findings on one backlog line) is claimed as a **unit**: two sessions handed it
  collide on that one line and *serialise*, one taking the next theme rather
  than a sibling leaf. To fan a theme out, split it into per-leaf lines first.

**Release is put-away — with one added step.** A claim's life is its branch's
life. On completion the line goes to `[x]` as part of finishing. On
**abandonment** the branch put-away (next section) carries a line-reversion:
salvage → tag → delete → record → **revert `[~]`→`[ ]`**, so the queue never
shows a phantom claim. The revert is a real step; don't trust it to happen by
itself.

**Orphan claims — the unhappy path.** A session that dies mid-item leaves a
`[~]` with no live branch behind it. This is not a new failure mode: it is a
stale branch wearing a roadmap marker, judged the same mechanical way — **a
claim whose branch/worktree is gone and whose commits have stopped is stale and
reclaimable.** Branch-existence is the signal; the claim-*time* stamp is only a
tiebreak once branch-gone + commits-stopped already point to staleness (a large
in-progress item and a dead orphan can carry the same six-hours-ago stamp, so
the timestamp alone decides nothing). No auto-expiry, no lease timer, no lock
server — reclaiming a dead claim is a judgement on the evidence, inside this
doc's no-locking-machinery line.

**When the queue isn't a git-tracked text file.** Every moving part here —
editing a line, the same-line rebase conflict, `pull --rebase` before push —
assumes the queue *is* text under git. A backlog in an issue tracker (GitHub
Issues/Projects, Jira) has no shared text line to collide on, so this exact
mechanism doesn't apply — but the principle does: use the tracker's own claim
primitive (assign the issue to yourself, or move it to an in-progress column)
*before* starting, the tracker's equivalent of mutating the shared line. Out of
scope here, named so the rule isn't a dead end for adopters.

*Bearing:* atelier 2026-07-13 — several parallel evening sessions, each told
only "the next thing in the queue", self-selected the *same* roadmap item more
than once and duplicated the work before anyone noticed. The waste was model
time, and nothing in the tree or the record ever conflicted to warn them:
selection was the one coordination point this doctrine named a substrate for
(worktrees) and a trigger for (say-so / dirty-tree) but never gave a *claim*.

## Every branch ends put away

A branch that exists must mean exactly one thing: **open work**. The moment it
can mean anything else, every future session that sees it pays to re-derive
what it is — a half-closed branch reads identically to a live one. (This
governs lines of *work*; the integration branch and any deliberately permanent
line — a release/`stable` branch, a pages branch — are infrastructure, not
open work, and sit outside the rule.)

A branch ends in one of two ways, and both end with the branch **gone**:

- **Landed** — merged to the integration branch, then deleted. Turn on the
  host's delete-branch-on-merge setting so this is automatic, not a memory.
- **Abandoned or superseded** — never delete lazily, and never keep the branch
  "just in case" either. Close it deliberately: **salvage → tag → delete →
  record.** Compare it against the integration branch *mechanically* (not by
  recollection); salvage anything unique; put an annotated **archive tag** on
  the tip (`archive/<date>-<name>`, absolute-dated per RECORD — the message
  states what was salvaged where and
  what was consciously dropped); delete the branch; record the decision in
  the session log; and if the branch carried a claimed roadmap item, **revert
  its `[~]`→`[ ]`** (§ Claiming work) so the queue shows no phantom claim. The
  tag keeps every commit reachable forever; the branch namespace keeps meaning
  "open work".

Half-closing is the failure mode this rule exists for: a branch whose PR was
closed-not-merged, salvaged and even archive-tagged — but not deleted — gets
re-investigated by session after session, because nothing at the branch says
"already decided and closed". Careful-with-data and clean-namespace are not in
tension; the tag is how you get both.

*Bearing:* atelier `atelier-method-review` (2026-07-10/11) — one session did the
salvage and the archive tag properly and *deliberately* kept the branch as a
second archive copy; its status was still re-derived twice more (the PR #1
close-not-merge reciting the closure decision; session 34 hitting it again cold)
before the rule above closed it. Even a considered kept-branch generated the
re-derivation tax.
