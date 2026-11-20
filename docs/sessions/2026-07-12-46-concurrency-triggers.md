# 2026-07-12 · 46 — concurrency triggers and sync bookends (Fable)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 69+1 -->
- [2026-07-12 · concurrency triggers and sync bookends (Fable)](2026-07-12-46-concurrency-triggers.md) — Mike named his real working style (parallel sessions across repos, sometimes several on one repo, atelier/shed flowing down so nothing is fully independent) and asked if it could be managed better — sketching branch/worktree-per-session while honestly unsure it helps. Assessment first: the only real hazard is same-repo-multi-session, and the danger is the **shared uncommitted working tree** (silent clobber/absorb), not concurrent commits; the doctrine already existed (CONCURRENCY worktrees, PROPAGATION pin) but had **no firing condition** — session 45's survival audit was good habits standing in for a trigger. Codified on "yes codify it": CONCURRENCY gains *the trigger* (say-so-at-open + dirty-tree backstop), *the solo default* (no branch-per-session ceremony — Mike's sketch assessed as costing more than it buys for lone sessions), and *sync bookends* (pull `--rebase --autostash` at start, push per commit, append-tail conflicts expected-and-trivial); the child doctrine block gains a **Concurrency** line reaching the fleet on normal pin bumps; CLAUDE.md read order now opens with the bookend (lived this session — pulled before editing).


Mike named his real working style and asked whether it could be managed
better: multiple repos in parallel (one or more sessions each), sometimes
multiple sessions on *one* repo, sometimes several repos from one session —
with atelier/shed flowing down into the children, so "independent" repos never
quite are. His own sketch: maybe every session opens a branch or worktree and
closes it at session end — offered with the honest caveat that he didn't know
if that helps or just adds work. Standing note: issues have been occasional
and light so far.

## Assessment (delivered before any edit)

- Of the three modes, only **same repo, multiple sessions** is the real
  hazard — and the danger is not concurrent commits (git handles those; worst
  case a rejected push and a rebase) but the **shared uncommitted working
  tree**: session B can overwrite session A's in-flight edits or sweep them
  into its own commit, and nothing errors. iCloud sync churn layers the same
  problem again.
- The doctrine already existed: `CONCURRENCY.md` prescribes one worktree per
  parallel line of work; `PROPAGATION.md`'s pin handles the parent→child
  flow-down (eventual consistency is the right model — no change there).
- The gap was the **firing condition**: nothing tells a session it is the
  second one on a repo, so the worktree rule never actually fired. "Gotten off
  light" was short commit-to-push windows standing in for a trigger.
- Mike's branch-per-*every*-session sketch was assessed as costing more than
  it buys: each branch demands the put-away ceremony for zero isolation gain
  when the session is alone on the repo.

## Codified ("yes codify it")

- **`method/CONCURRENCY.md`** — three new pieces: *the trigger* (say-so-at-open
  primary cue + dirty-tree backstop: uncommitted changes a session didn't make
  ⇒ another session is live, move to a worktree, never work around or absorb
  them), *the solo default* (trunk-based, small commits pushed immediately —
  worktrees are for known-parallel work, not a standing tax), and *sync
  bookends* under integration hygiene (`git pull --rebase --autostash` at
  session start, push per commit, append-tail conflicts expected-and-trivial).
  Bearing recorded: sessions 45–46 — session 45's post-hoc survival audit
  (two parallel sessions, same checkout) as the concrete instance of good
  habits standing in for a rule that never fired.
- **`method/PROPAGATION.md`** — the standard child doctrine block gains a
  **Concurrency** line (bookends + backstop), so the trigger reaches the fleet
  on each repo's next deliberate pin bump. The narrowing-free-restatement note
  now names the line's source so pin-bump reviews know what to check it
  against.
- **`CLAUDE.md`** — read order now opens with the sync bookend + dirty-tree
  check (lived this session: pulled before editing).

## Owed

- New/changed doctrine ⇒ the usual cold-review sweep will pick these sections
  up; nothing else outstanding. Children adopt via normal pin bumps — no
  fleet-wide retrofit run needed.
