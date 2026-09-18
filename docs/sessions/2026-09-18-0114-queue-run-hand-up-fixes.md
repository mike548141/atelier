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
  unrecognised key, anywhere. That widens a blocking net, so it was held
  until an estate probe (old vs new, every sibling repo's tracked content)
  read back: one repo turns red at its next pin bump on a public document
  link's query id, one already-red repo gains 15, one false positive goes.
  Merged, with the cost stated in the item.

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

### Wave 3 — the ruled builds

Four more Sonnet workers built what Mike ruled, and a fifth took the
main-boundary check (`140/010` = `115/180`, one build filed twice):

- **`020/360` plainscan removed.** Tag `archive/plainscan-2026-09-18` →
  `3a6ae81`, pushed. The worker stopped rather than bypass the hook when
  linkscan blocked on four links in two review records that pointed at the
  deleted files. It was right to stop. The orchestrator added scoped
  `linkscan:allow:missing-file` markers naming the ruling (an annotation,
  not a rewrite) and committed with the hook. This settles `290/070` and
  `020/310`, and makes `120/010` moot.
- **`320/200` conflictscan**, enforced, zero findings across atelier and
  every sibling. Its own merge produced a live conflict in the registry list
  it joined, which was resolved and scanned clean with it.
- **`110/020` (a)** `worktree list` against `origin/<main>`.
- **`140/010`** the parent-row boundary check, live green.
- **`320/240`** plurals, merged below.

Six small closes inline: `160/250` (resolved by its author in `419fdac`),
`010/040` (swept, nothing wrong — monolith wording is still current for the
children).

### 🛑 This run thrashed Mike's machine

The first estate probe walked each sibling's full working tree. Over the
largest repo, `secretscan` grew to ~9 GB. A loop that `pkill` was meant to
stop moved on to the next repo and kept running. Combined with a worker's
`leakscan` probe, the 16 GB machine went ~21 GB into swap at load 54. A
peer session in another repo traced the PIDs and asked for them to be
stopped. All were killed and the peer was told. A second 9 GB run over the
same repo belonged to another session and was left alone. Two lessons, both
recorded: probe tracked content only (`git archive HEAD`, what CI sees), one
process at a time; and after a `pkill`, check that nothing matching is left
before assuming it worked. The class is filed as `020/370`. This record
does not claim the machine was fine meanwhile. It was not, and the owner
found out from someone else.

### Close

**Stop condition: everything left is blocked**, plus the machine. What
remains open is almost all 🎯, waiting on Mike, or `⏳` Fable-tier review
this Opus run may not take. The two exceptions are `110/010` (its own text
waits for a second instance before building) and the new `020/370`, which
needs heavy scanning of the very repo that just thrashed the machine. That
is a poor thing to start at load 38.

**Closed this run (22 items):** `320/250`, `320/290`, `110/020`,
`020/060`, `210/110`, `010/090`, `020/340`, `210/100`, `320/260`, `310/110`,
`320/210`, `320/220`, `160/250`, `010/040`, `020/360`, `290/070`,
`020/310`, `120/010`, `320/200`, `140/010`, `115/180`, `320/240`.
**Partly:** `320/170` (one class of three). **Filed:** `320/300` 🎯,
`020/360` (then closed), `020/370` 🔥. **Queued for review:** `160/310`
(doctrine), `160/320` (registry code); `160/260`, `160/290` and `160/300`
widened.

**🎯 New decisions this run surfaced** (the rest of the board's 🎯 are
unchanged): `320/300` — should a doctrine ruling carry a check that the
child block's copy moved with it. Two items the triage marked build-ready
turned out to hold rulings: `115/030` (stampscan's inverted verdicts: how
to permit compression while forbidding narrowing) and `320/010`
(pathscan's package-root anchor).

**🚩 Awareness:** one child turns red at its next pin bump on a public
document link's query id (secretscan now scans query values); the remedy
is a scoped allow-marker in that repo. ADR 0008's 2026-08-23 amendment says
`main` has no ruleset, but one is now active (`140/020`'s ground).

Tests 1376 → 1430 Python (−51 with plainscan's removal), 261 → 277 node;
floor green before every push. All worktrees and branches put away.

### Addendum 2026-09-18 — the thrash is a defect, not a workload

Mike, on reading the close: *"that means there is a defect in secretscan, it
should not matter how much it scans it should no have this affect. Put work
on the board to fix that, and the same for all the other guards"*. He is
right, and the close framed it wrongly: it treated the large repo as the
problem and prescribed probing around it. `020/370` is rewritten as a
`secretscan` defect with a testable requirement (memory bounded whatever the
input size; time linear; skips reported, never silent). It lists the likely
causes read from the code, marked unmeasured. `020/380` carries the same
requirement for every other guard, one box each, closed only on measured
evidence. The tracked-content-only probe practice is now marked interim.
