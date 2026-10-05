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

## `210/180`: cctranscript's first-prompt column reads a bounded prefix

A Sonnet worker built it (`83d9b0b`). The merge and close are in the
commit after it. A 64 KB prefix read comes from a census of where the first
prompt sits; when the prefix holds no prompt, the whole-file read runs as
before. Listing output was byte-identical across three runs each, the
function's answer was identical on all 983 mirrors, and listing CPU fell
from about 27 s to about 7 s. The orchestrator re-ran the Node suite on
the merged tree: 411 pass. It also corrected the census date in a code
comment, which the worker had stamped from local time. The worker also
measured `--search` and left it alone, because a prefix cannot be
output-identical there.

## `130/020`: one unambiguous review-pointer state

An Opus worker built it (`b02c56d`, `952f78a`), and the merge closes it with
`130/010` and `320/460`. It needed no new state. `⏳` now means only
"queued, verdict not returned"; the verdict commit takes it off, and the
tri-state takes over, led by 🎯 when Mike's ruling is owed. `pointerscan`
warns on both miscounts. Over the board's whole history it fires on exactly
the 27 items `1d96efa` proved. `board.py` stops lifting glyphs out of code
spans. `160/670` was a real queued re-review hidden behind 🛑, and it now
counts. The worker proposed closing `160/460` and `160/510`, but each item's
own text holds its cycle open until `670` runs, so they stay open. The merge
conflicted only on the generated index, and a rebuild resolved it. Two
date stamps the worker took from local time were corrected to UTC. The
targeted suites pass on the merged tree (87 tests). The worker saw two
`BoundedMemory` timeouts while the machine's load average was about 270, and
those are re-run at close. Doctrine pass queued at `160/690`.

## `200/010`: `indexscan`, the generic index guard

An Opus worker built it (`8d10487`). It is opt-in per index, checks both
directions, and leaves the listed-but-missing direction to
`linkscan`/`pathscan`. It is warn-only on both planes. Its first run on
atelier found ten session detail files the session index never lists. The
orchestrator read each one. All ten are records-only captures or annexes
reached from another record, so each now carries a reasoned allow-marker
(why, who, session, not a ruling, when) instead of a back-dated index line.
That last part is the orchestrator's own judgement. A reviewer may prefer
index lines. Code pass queued at `160/700`.

## `115/240`: three enforced scanners stop calling themselves advisory

A Sonnet worker fixed the docstrings, the help text and the README
(`4553814`). Each scanner now names the commits that wired it blocking. The
orchestrator replaced a drifting "as of now" with a date. This was
description only, so no review is owed.

**Machine load.** By this point the machine's load average was 350–470.
That came from this run's parallel workers plus test runs in other repos'
live sessions. Two memory-bound tests (`BoundedMemory` in `test_pins` and
`test_spellscan`) timed out for three different workers, identically on an
untouched base. The run stopped dispatching new workers until the in-flight
ones drained, and re-runs those two tests at close.

## `200/050` and `200/020`: the reviewer checklist, and a test-evidence rule

An Opus worker wrote both (`90c42ec`, `be9a3ae`). `REVIEW.md` gains *The
standing checklist*: V1–V7 as seven one-line checks, each pointing at its
existing home and at grounding findings it opened before citing. The
review skill carries a stamped copy. One sentence goes past the record and
is flagged for the reviewer. `EVIDENCE.md` gains §15, *A test cannot
falsify its own code's assumption*. The drafting session chose EVIDENCE.md
over REVIEW.md, because the rule binds whoever writes the test. `050`
closes. `020` stays open under 🎯, because the item reserves sign-off on
the wording and the home to Mike. Both are covered by one doctrine pass at
`160/710`. The worker also found four defects in the record it worked from,
and they are filed at the run's close.

## Filed by this run, and `200/110` done inline

- `115/250`: pointerscan still walks the whole tree, including harness
  worktrees. It never got `110/110`'s fix. Claimed for a Sonnet worker.
- `200/110`: the `200` mining record and its section README hold stale
  statements. The README sentence is corrected, and the record carries a
  dated note under its head with its body unchanged. One of the worker's
  four reports was dropped: a 2026-07-22 count that was true when written.
- `320/490` gains its third atelier instance of committed tool-call markup.

⚠️ **Recorded against this run:** `200/110` was filed open, then done inline
without a claim commit in between. That breaks claim-before-work. The
exposure was nil, because no other atelier session was live and the item
was minutes old, but the rule has no "it was small" exception.

## `260/090` (P7): the `rpi` flip, read from its transcripts

An Opus worker read the three `rpi` sessions of the flip in full, plus
five more sources in part (`b2b1701`), and returned lessons as classes with
no estate detail. The orchestrator checked the block for names before
merging. Headline: every thinking block was empty, so the transcripts carry
narration and tool calls, not thought. `200`'s README is qualified on that
point. Four pre-flip-gate findings are filed together as `260/110` (P9).
One finding goes to `320/480` as a second shape of its class. Two
corrections belong in `rpi`'s own public records and are left for Mike's
report, not written there from here.

## `110/130`: leakscan and secretscan, three to five times faster

A Sonnet worker built it (`c938b58`). It uses lever 4, cheap per-rule gates
each pattern makes necessary. Lever 3 was declined with its reason
recorded. Levers 1 and 2 were out of scope. Output was byte-identical on
three corpora, and a 1.15-million-line differential fuzz found zero
mismatches. The fuzz caught two gate bugs of the worker's own before
commit. The orchestrator read every secretscan gate against its pattern
before merging, and checked that no named rule is case-insensitive, since
a literal gate would be unsound against an `(?i)` pattern. It also re-ran
the two modules' tests (306 OK) and both selftests. A wrong gate is a
silent miss on a blocking guard, so the cold pass at `160/720` is the one
to take first.
