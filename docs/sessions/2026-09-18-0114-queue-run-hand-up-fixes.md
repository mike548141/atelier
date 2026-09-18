# 2026-09-18 · Queue run — the hand-up fixes

**Session:** Opus 5 (VS Code) orchestrating, Sonnet 5 workers in isolation
worktrees · `main` for claims and inline items · in progress; each item closes
in its own commit, so this record grows per item.

## The ask

Mike's standing queue-run brief: *"I have a long list of work queued and I want
you to deliver it — across this session and any that follow. Start here, then
use your own judgement on what's next."* Run per `CONCURRENCY.md` §
*Orchestrated queue runs*. Tier check at open: Opus 5 orchestrating, which
the orchestrator-tier clause permits as Mike's per-run call; the `⏳` review
pointers all name Fable, so this run takes none of them.

## Opening state

`main` at `899af73`, clean, a closing entry for the last sitting present, no
open PRs, one worktree. No live claims on the board.

## Items

### 320/250 — the child block's overturned ask wording (inline)

The item said `PROPAGATION.md` held the one surviving copy of the ask wording
DA1 overturned (*"the session reply* first*"*). Checked at HEAD: true there,
and **a second copy the item's grep could not see** — its search was scoped
to `docs/method/*.md`, and `docs/build/templates/CLAUDE.md` is the scaffold
that stamps the same bullet into every new child. Both harmonised to
`COMMUNICATION.md` § *Asking for a ruling*: the account must have *reached*
the principal before the choice is put, in the same reply or — where the
display mode hides mid-turn text — in a completed message before the ask.
The item's second question (should a doctrine-changing ruling carry a
mechanical check that the block's copy moved with it) is a decision, not
work this item can finish; it moved to its own item, `320/300`. The open
`⏳` at `160/290` already covered this bullet, so its delta list was widened
rather than a second pointer queued.

### Triage, then wave 2

A read-only triage (Sonnet 5, four sub-agents, ~33 items) classified the open
non-ruling items against HEAD: build-ready, needs-ruling, idea-only, stale.
Its picks were re-checked before claiming; its "stale" call on `160/250` was
not acted on yet (the instance is gone, but the item is about `pointerscan`
missing the class, which a clean scan does not disprove).

Six code items went to Sonnet workers in isolation worktrees, each reviewed
by reading the diff before a `--no-ff` merge that carries the item's close:
`110/020` b–e, `020/060` + the tilde class of `320/170`, `210/110`,
`010/090` + `020/340`, `210/100`, `320/290`. Two worker drafts were sent back
at review:

- **`210/100`** numbered a mid-turn message as a new exchange, which would
  have shifted every `N` / `N.M` ref already cited in committed records. Now
  `N+K`, pinned by a byte-identical-refs test.
- **`320/290`**'s URL exclusion hid a credential in a signed URL's query
  string (`?sig=…`). Now scoped to scheme + host + path; the worker also
  found `=` in the entropy regex's lookbehind hid every `key=value` under an
  unrecognised key, anywhere. That widens a blocking net, so it is held
  unmerged until an estate probe (old vs new, every sibling repo) reads back.

### Rulings taken this run (question device, Mike's words)

- `120/010`: *"Add guard, close"* — then made moot by the plainscan removal
  below, since the flaky tests are the reply hook's own.
- `320/200`: *"New conflictscan"*, enforced.
- `320/240`: *"Always match plurals"*.
- `110/020` (a): *"Compare to origin/main"*.
- Mid-session, unprompted by the queue — Mike: *"What is the impact of
  completly removing plainscan? I had so much trouble with it prior I ordered
  it be "unwired""* and *"I think as a guard its possibly more dangerous than
  it is beneficial"*. Impact measured first (reply hook already unwired and
  under a Fable DESTROY verdict; the floor scanner warn-only everywhere and
  printing ~6,050 findings per commit), then asked. Ruled: *"Remove the hook
  and archive the engine in case we ever want the code again"* — filed as
  `020/360`.

### Doctrine inline — `320/260`, `310/110`, `320/210`, `320/220`

The drift command reads `..origin/main` after a fetch in all three places it
is spelled. "Self-removing" became "removable at the next pin bump, watched
by nobody until `310/020` lands". The session-start bookend gained its two
gates (read `git status` first; no remote, no bookend), harmonised into the
block, the template and atelier's own onramp, which all stated it
unconditionally. And a new **Verify the act, not the absence of an error**
bullet in § *Integration hygiene*: atelier had no read-the-output rule for
the clause to extend. Queued as `160/310`; the self-removing change widens
`160/300` instead.
