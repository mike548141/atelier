# 2026-07-27 · 2208 UTC · Policy-as-code programme — five tracks from a five-day transcript sweep

**Seat:** Opus 5 (1M context), worktree `policy-as-code-programme`.
**Ask:** *"Lets improve our policy as code for all the child repos and atelier.
There are a lot of learnings in the session transcripts between [2026-07-23 and
2026-07-27, both dates inclusive]. Lets read all of them and collect anything
useful to create a plan of work."* — the bracketed span is an editorial
restatement of a day-month-year phrasing, in ISO, so the record does not carry
an ambiguous date shape. The gate caught the verbatim original, which is the
class **E5** names: *describe, don't quote*.

## What was done

A sweep of every main-session transcript in the window, rendered through the
house instrument (`cctranscript`) rather than read raw, then consolidated into
one buildable programme on `ROADMAP.md`.

**Corpus:** 60 main sessions across 11 repos, 90 MB of raw JSONL, rendering to
6.5 MB of prompt-and-reply text. **2026-07-24 is a gap day** — no sessions at
all, which is worth knowing before anyone re-derives the window. 12 sessions
were read in full (selected by a policy-vocabulary ranking over all 60), the
other 48 mined by targeted extraction of their close-out and finding blocks.

**Method note worth keeping.** The two largest transcripts in the window are
~1.9 MB each and are dominated by pasted reference material, not session
content; ranking by policy vocabulary put both near the bottom and they were
correctly skipped. Sorting a transcript corpus by size selects for pasted bulk,
not for signal.

## The organising finding

The defect ADR 0008 exists to end kept reappearing **inside the fix**: *a check
that runs, exits 0, and covers nothing.* It appeared in the registry wiring
(absolute paths matched no staged path), in the boundary scanners (`--staged`
plus an absolute path scanned nothing), in the nested-worktree exemptions
(closed one scanner at a time, five left behind), and — per the 2026-07-26 cold
passes — in `scope` handling, in the hook plane's `leakscan`, and in
`floorfleet`'s own conformance claim.

That is one class, and it is why the five tracks are ordered as they are:
**A** fail-opens (the only live exposure) → **B** enumeration → **C** advisory
decay, with **D** registry completeness and **E** scanner precision following.

## Verified live, not inherited from a record

Every load-bearing claim in the programme was re-checked against the working
repos. Four mattered:

| Claim | Status |
|---|---|
| The parent was not running its own floor | ✅ true — `core.hooksPath` unset in the atelier clone; every child had it. Fixed by Mike the same day; hook plane now 9/9 enforced, proven on a real commit. |
| `stampscan` is not wireable as built | ✅ true — `--warn` still exits 2 on the live tree, tripped by a review file that merely *describes* its marker syntax. |
| The repo-local seam has adopters | ❌ false — **no repo declares a `local` check**. The seam shipped 2026-07-26; the tripwire that motivated it is still off. |
| Advisory declarations carry a reason | ❌ false — `advisory` is a bare list of names in the schema. **11 declarations across 8 children**, none with a reason, none with a date. |

One of those came from a review pass Mike had rejected on tier grounds, so it
was treated as a lead and re-derived from scratch rather than carried forward.
**A finding from a withdrawn pass is a lead, never a fact** — that discipline is
what turned it into evidence.

## What landed

- `ROADMAP.md` § *Policy-as-code programme — five tracks*: 24 new open items,
  refs-only pointers where work was already queued elsewhere (thin anchor, fat
  pointer), written out in full only where it was not.
- The nine cold-pass verdicts of 2026-07-26 now have a home as *work*. 56
  findings had been sitting in nine verdict files with nothing on the roadmap
  pointing at them as buildable items.
- `ROADMAP-DONE.md`: A5a harvested — **in the same commit**, not the next,
  dogfooding the rule Track A itself names.

**Pure insertion, zero deletions in both files** — shown to Mike before the
commit. This file lost a genuine item to an undiffed bulk edit on 2026-07-25,
and a large programme section is exactly the shape that would repeat it; the
zero-deletion property is what makes the review gate cheap rather than
ceremonial.

## Ruling cadence — decided this session

Mike deferred to a recommendation on whether to rule the 56 findings up front
or as the work proceeds. **Ruled at the point of work, batched per item, in
plain language with impacts** — a single cold sitting over 56 findings is an
under-contextualised ask, and most of them are self-evident once the work is in
front of you. Three exceptions are ruled up front, because they are live
fail-opens whose fix shape genuinely branches and whose blast radius is
immediate: **EP1** (unresolvable scope), **EP3** (leakscan term-list cover),
**C1** (the `advisory` schema change every child must migrate to).

## Split, and why

Mike stopped the session mid-flight: *"If this is too much for one session lets
split the work up. I worry about context size affect the quality of your
work."* Correct, and it is the same diagnosis this programme carries as its
root cause — **long session × mutating multi-repo state = maximum staleness
exposure**. Landing the plan is precisely what makes splitting safe: each track
can now start cold from the record instead of from a session's memory.

**Nothing in Tracks A–E was started.** The programme is a plan, and saying so
plainly is the point — a half-built track described as underway would be the
same half-extraction the apex forbids.

## Owed

- ⏳ **No review is owed for this capture.** It queues work and consolidates
  counsel; it writes no doctrine. The doctrine items *inside* it each carry
  their own rule-4 `⏳` for the session that lands them — and that review is
  Fable's.
- 🎯 The 56 rulings remain Mike's, now with a cadence and a home.
