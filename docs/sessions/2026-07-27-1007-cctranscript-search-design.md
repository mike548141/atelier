# 2026-07-27 · 1007 UTC · cctranscript search — design pass

**Model:** Opus 5 (1M) · **Where:** worktree `cctranscript-search-design`
**Ask:** Mike, having been shown the open queue across `ccrepo` / `cctranscript`
/ `ccarchive`: *"do a design for that please"* — the `cctranscript` search item.
**Output:** records only. Nothing built.

## The ask, and its shape

The roadmap item was Mike's from 2026-07-26 — search all transcripts, regex or
plain term, scoped by the flags that already exist. It carried **six questions
explicitly marked "none pre-decided"** and an instruction that the scoping half
is already built and must be reused verbatim, not reinvented.

So this pass had two jobs: answer the six, and stay inside the existing surface.
It did both, and the answers came from measurement rather than argument wherever
a measurement was available — the posture the ccarchive encryption design pass
set the week before.

## What was measured, and what it changed

Measured on this machine against the live store (440 sessions / 500 MB) and the
ccarchive mirror (860 logs / 235 MB compressed → 680 MB of text).

**Two roadmap premises were corrected.**

1. **The thinking layer is not searchable, because it is not written.** The
   roadmap asked whether the default search should include thinking. It cannot:
   a census of the whole live store finds **24,856 thinking blocks, 9 of which
   carry any text**, all between 2026-06-05 and 2026-07-04. Every block since
   carries a `signature` and no content. Confirmed behaviourally too —
   `cctranscript --think` renders no thinking turns on a current session. The
   question is void rather than answered, and the finding is bigger than the
   search item: **`--think` is a flag that no longer does anything**, which is a
   defect in the shipped tool that this pass merely tripped over.

2. **Search is I/O-bound, not parse-bound.** The roadmap treated "the first
   operation that reads *every* file" as the item's main cost risk. Reading every
   live log costs ≈2 s; parsing every line costs 5.9 s; **prefiltering raw lines
   and parsing only the survivors costs the same as the bare read**. So the
   expensive version is the obvious one, and the cheap version is a deliberate
   inversion that needs a comment in the code or a later tidy-up will "simplify"
   it back. An index is therefore not needed and is deferred with the sweep time
   named as the number to watch.

**A third measurement inverted an optimisation.** Case-insensitive matching via
`/term/i.test()` is free (1.8 s); doing it by lowercasing the text first costs
4.3 s; and the fastest option of all — decoding the bytes as latin1, 0.9 s — is
**rejected on correctness**, because it silently fails on non-ASCII and this
estate writes macrons on te reo Māori by standing convention. The one shortcut
that measurably paid was the one that would quietly break the text we most care
about getting right. Recorded in the design so a future optimisation pass finds
the reason attached to the speed.

**A fourth settled the excerpt question more sharply than expected.** The roadmap
worried about a hit inside a 3,000-line tool result. The size distribution says
the worry generalises: replies are genuinely small (max 8 KB), but a single
*prompt* reaches **848 KB** (a pasted blob is a prompt) and a tool result reaches
680 KB. So excerpting is unconditional across every layer rather than a special
case for tool output.

## The seventh question was not open

The roadmap flagged one doctrinal loose end: `instruments/README.md` justifies
cctranscript having **no** `--materialise` flag on the grounds that it never
bulk-reads, and search would make that justification stale.

Revisited, this needs no judgement. **Flags-follow-operation** (ratified
2026-07-23) says a flag is added when the tool genuinely performs the operation
it names — and search *is* the bulk read. cctranscript acquires `--materialise`
with its two siblings' exact meaning, and the README note is rewritten in the
same commit as the flag lands. The note keeps its role as the worked example of
the rule; it simply gains a second act, where the operation appeared and the word
followed it. Measured aside: **0 of 860 mirrors are currently evicted**, which is
one machine on one day and no reason to skip the work.

`--since`/`--until` resolve the same way — the operation *is* now genuinely
shared (narrowing a set before sweeping it), so the words carry over. One trap
named: filtering candidate files on `mtime` would drift from ccrepo's
message-timestamp semantics, so mtime is used only as a safe skip for `--since`
and the hits themselves are filtered on their own turn timestamps.

## The one reuse worth naming

Every hit row carries the citable `N.M` reference, and it is free — because the
refs are **gate-invariant**. `numberTurns` numbers only `you` and `claude` turns,
both of which `readTurns` collects regardless of `--tools`/`--think`. So a ref
printed by a search run means the identical thing when the session is reopened
with default flags. That is asserted as a DONE condition rather than assumed,
because nothing enforces it — it falls out of how `numberTurns` happens to be
written, so an unrelated change could break it silently.

## What was NOT done, and is not implied

- **Nothing was built.** No code, no tests, no flag. The design names DONE as
  fourteen testable conditions; none of them are met.
- **No decision was left for Mike.** Unlike the ccarchive encryption design,
  which ends on a 🎯, this one closes every question it was given. If that is
  wrong — if the `--search` naming or the no-default-cap call should be Mike's —
  it is a cheap correction, and both are argued explicitly in the design rather
  than buried.
- **Two new strands were opened, not closed:** the inert `--think` flag, and the
  417 subagent logs that sit outside every cctranscript view. Both are recorded
  on the roadmap with their grounding, and both were deliberately kept out of the
  search build rather than smuggled in.

## Honest limits

- The measurements are **one machine, one corpus, one day**. The 2 s sweep is
  this store's; a corpus an order of magnitude larger would revisit the
  deferred-index call, which is why the design names sweep time rather than file
  count as the trigger.
- The thinking-block finding is a **census of the live store only**. The archive
  mirror was not separately censused for text-bearing thinking blocks; the live
  store's 2026-06-05..2026-07-04 window is presumed to bound it, since the
  archive mirrors the same logs. Not checked, so not claimed.
- The `--search` naming decision runs against the standing "flags read as
  selectors" preference. The design argues the exception rather than ignoring the
  rule, but it is an argued exception, not a measured one.
- **No review is queued.** The pass authors no doctrine, so it sits where the
  ccarchive encryption design sits: review WARRANTED when it moves to build,
  because the build edits the flag-vocabulary note that is a ratified rule's
  worked example.

## Records

- Design → [`instruments/cctranscript.search.design.md`](../../instruments/cctranscript.search.design.md)
- Roadmap → the `cctranscript` search item rewritten to DESIGN DONE / BUILD not
  started, with the two corrected premises stated inline; two new strands added
  below it.
