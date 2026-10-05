# 2026-10-05 · 1120 UTC — Queue run: closes on evidence, then builds

**Tier:** Opus 5.5 orchestrating, stated at open per `ECONOMICS.md`
§ *The orchestrated-run tier split*. Workers: Opus 5.5 for doctrine-text and
structural items, Sonnet 5.5 for pattern-following builds, each in its own
isolation worktree and its own scratch directory. Read-only triage on Opus 5.5.

**The brief.** The standard queue-run prompt. Mike would be away for several
hours: *"Try not to stop and ask me questions until you have done all the
work."* So rulings are gathered for the close, not asked mid-run.

**Per-item close.** This file is written as each item closes, so a cut costs
at most the item in flight.

## At open

- The tree was clean, in sync with `origin/main` at `2c689ef`, and the floor
  was green on that SHA. There was one worktree and no stash. The last
  session closed cleanly. No other atelier session was live; five sessions
  were live in other repos.
- Triage: three read-only Opus passes read all 140 open items that carry no
  `🎯`, `🛑` or `⏳`. Each "buildable" or "already done" call had to quote
  the item's own line. The orchestrator then re-read every such call against
  the item before claiming it. Re-reading overturned one call: `140/020` was
  marked "already done", but ADR 0008's 2026-08-23 amendment says `main`
  carries "no ruleset", and a live read shows ruleset `20603641` active. That
  is the open AR1 finding, so the item stays open.

## Closed on evidence (claim `e33f774`)

Ten items whose own text was already answered, each closed with its evidence
in the item:

- **Moot since plainscan's removal (Mike, 2026-09-18, `020/360`):**
  `020/260`, `020/280`, `020/290`.
- **Already delivered:** `030/110`, the canonical drift range (`54201e0`);
  `320/510`, fixed with `320/500`; `210/080`, the man page line.
- **Decided by the ruling the item waited on:** `200/070`.
- **No work of their own:** `110/070`, a pointer; `030/060`, resolved in its
  own text.
- **`115/140` diagnosed from the logs.** The estate conformance job is not
  broken; it reports real reds. All of the last 60 runs failed. The latest
  read every enrolled repo with none unreadable. The red is three children's
  own floors, each with a blocking secretscan finding of its own. Those reds
  are the children's work, and their detail stays out of this public record.
  Making a standing red reach a person is `115/100`, which awaits Mike.

## `300/020`: the guard board re-ranked against the fourth requirement

Claim `97c7ace`, merge `27586aa`, closed `f87ffb2`. An Opus worker declared
100 guards and guard items: 20 landed, 80 open. It flagged seven where the
honest answer is *forbids the act, and nothing makes the failure cheaper*.
Two of those are landed guards, `leakscan` and `publishscan`. The other
five are open items: G3, the before-plane, quotescan and two proposed
working rules. Nothing was unwired. The pass's sharpest cross-cutting
finding: **only the hook forbids anything**, because CI runs after a push
and on a public repo the push is publication. The worker's four Sonnet
classifier passes read the 136 candidate items. The worker re-read every
flagged or overridden row itself. It screened out 115 more items by title
and section, and the result block names them. One finding was filed as
`115/240`: three enforced scanners still call themselves advisory. A worker
has claimed it.
