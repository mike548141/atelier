# 2026-07-27 · 1007 UTC · cctranscript search — design pass

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 202+1 -->
- [2026-07-27 · 1007 UTC · cctranscript search — design pass, six open questions closed on measurement (Opus, wt: cctranscript-search-design)](2026-07-27-1007-cctranscript-search-design.md) — Mike's *"do a design for that please"* against the `cctranscript` search item, whose six questions were explicitly marked "none pre-decided". All six answered, and the seventh (`--materialise`) found to be **settled already** by ratified flags-follow-operation rather than open — search *is* the bulk read, so the flag follows the operation and the README's asymmetry note is rewritten in the same commit as the build. **Two roadmap premises corrected by measurement:** the thinking layer is not searchable **because it is not written** (24,856 blocks live, **9** carry text, none after 2026-07-04 — which also means the shipped `--think` flag renders nothing, a defect this pass tripped over rather than caused); and search is **I/O-bound, not parse-bound** — ≈2 s to sweep 440 sessions / 500 MB, where prefiltering raw lines and parsing only survivors costs the same as a bare read and the obvious parse-everything build costs 5.9 s, so an index is deferred with sweep time named as the trigger. A third measurement inverted an optimisation: `/i` matching is free (1.8 s), lowercasing first is not (4.3 s), and the fastest option — latin1 decode, 0.9 s — is **rejected**, because it silently fails on macrons and this estate writes te reo Māori with them. A fourth generalised the excerpt rule beyond the roadmap's worry: no layer is safe to print whole, since a *prompt* reaches 848 KB. Design → [`instruments/cctranscript.search.design.md`](../../instruments/cctranscript.search.design.md), 14 testable DONE conditions, **nothing built**; no 🎯 left open, and two new strands opened instead (the inert `--think`, and the 417 subagent logs outside every view). Review WARRANTED at build, not queued now.
<!-- archivecut:log-entry docs/SESSIONS.md 203+1 -->
- [2026-07-28 · addendum · two ccarchive capture items queued; the backfill measured to be free (Opus, main)](2026-07-27-1007-cctranscript-search-design.md) — following the search design's finding that subagent `.meta.json` sidecars are uncaptured, Mike ruled **capture them**, and asked for the already-archived transcripts to be backfilled too. Both queued on `ROADMAP.md`, and the second **changed shape under one artefact check**: `archiveOnce` walks the whole live tree and `shouldArchive` fires whenever no mirror exists, so the first daily run after the capture class lands backfills every sidecar still on disk — **no backfill pass is owed**, and the item now exists to verify that rather than build it. Measured to ground both: **425 live sidecars, 0 archived, 66 KB total**; of 418 archived subagent logs **417 are backfillable and 1 is gone for good**; `cleanupPeriodDays` is **395**, so the loss clock is real but roughly annual and is written up as such rather than dressed up as urgent. A census of all 425 also settles a candidate in the open *"`finished` counts logs, not successes"* strand — the sidecar carries `agentType`/`description`/`toolUseId`/`spawnDepth`/`model`/`worktreePath`/`parentAgentId` and **no outcome key of any kind**, because it is written at spawn and describes intent, not ending. Separately, Mike's batching question (2 GB solid gzip vs per-file mirrors) was answered by measurement and **not** recorded: solid gzip is 234.7 MB against 234.5 MB today — zero gain, because gzip's 32 KB window is already saturated by ~790 KB files.


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
