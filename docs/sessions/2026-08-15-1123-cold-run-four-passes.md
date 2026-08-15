# 2026-08-15 · 1123 UTC · Four cold passes run, one brief written — the two-session split works (Fable, wt: cold-run-0815-1123)

**Mike's instruction, verbatim, opening a cold session:** *"As a cold session
please do any review work, any work that is fable dependent, and write briefs
for any reviews that need them. If you write the brief then do not run the
review, that will require another cold review session."* Mid-session, after
an API session limit cut two reviewers off: *"We hit the session limit, can
you safely pick up where you left off?"*

This is the second half of the split the 1024 UTC session opened: that
session wrote four briefs and stopped; this session — which it neither
started nor instructed — ran them. And the pattern recursed once: the one
brief-less pointer left on the board (the reply-gate unwiring, `160-…/180`)
got its brief from this session, which then stopped on it.

## What the queue held, and what was done with it

| Pointer | Brief (written 1024 UTC by the other cold session) | This session | Result |
|---|---|---|---|
| Board-store migration `010-…/050` | `2026-08-15-1030-board-store-migration-cold` | **ran** | 🛑 1 MAJOR / 4 MODERATE / 5 minor / 4 note — cycle OPEN, BS1–BS14 to Mike |
| Laws removal `020-…/215` | `2026-08-15-1031-laws-removal-apex-cold` | **ran** | 🎯 0 MAJOR / 3 MODERATE / 2 minor / 4 note — cycle CLOSED, LR1–LR9 to Mike |
| `cctranscript --search` `160-…/010` | `2026-08-15-1032-cctranscript-search-cold` | **ran** | 🎯 0 MAJOR / 3 MODERATE / 6 minor / 5 note — cycle CLOSED, CS1–CS14 to Mike |
| COMMUNICATION enforcement clause `020-…/300` + plainscan rescope (README) | `2026-08-15-1033-communication-floor-cold` | **ran** | 🛑 FAIL — 1 MAJOR / 5 MODERATE / 2 minor / 2 note — cycle OPEN, CMF1–CMF10 to Mike |
| Reply-gate unwiring `160-…/180` | none | **brief written, NOT run** — `2026-08-15-1126-reply-gate-unwired-cold` + `.deferred.md` | ⏳ open for a later cold Fable taker |

No other Fable-dependent work was on the board: every other Fable mention is
a ruling round that is Mike's, and the two `⏳`-led items already verdicted
(`160-…/080`, `090`) are the subject of the `130-…` item and were left alone.

## How the passes were run

- **Claim on `main` first** (`3d0df11`): four pointers marked TAKEN/RUNNING,
  the 180 pointer claimed for brief-writing only. Worktree before the first
  edit. Pushed before any reviewer was spawned.
- **Orchestrator-held context partition** (REVIEW.md rule 1's structural
  shape): the four `.deferred.md` siblings were **moved out of the worktree**
  into the session scratchpad before spawning, so no reviewer's grep could
  reach them; one reviewer subagent per pass, all Fable, sharing the worktree
  read-only; every mutation probe in a per-reviewer scratch clone; reviewers
  ran no mutating git; the orchestrator committed each phase-1 verdict
  *before* releasing the sibling text by message, and each reconcile after.
- **Provenance disclosed in every verdict:** the orchestrator's own onramp
  had read the `SESSIONS.md` tail (index entries for these very deltas); the
  reviewers had not. The tail read is also why the RG brief was written
  without opening its intent record — the summary had already been seen, and
  the brief says so.
- **Prefix collision caught at spawn:** the 1033 brief said `CF`; `CF1`–`CF7`
  already exist in the 2026-07-20 concurrency-flip verdict. The reviewer used
  `CMF` and states the change in its provenance.
- **HEAD moved twice under the reviewers.** The 1033 brief's surfaces had
  been rewritten by `cd6232b` (the unwiring) after the brief was written; the
  reviewer was told to form its lens-1 judgement on the Stop-hook control
  from the hook documentation *before* reading that commit, and did (a
  timestamped scratch note, 1144 UTC, precedes the read at 1156 UTC), then
  found the same mechanism the commit asserts. And `origin/main` moved five
  commits past the worktree during the LR pass (`738afd9`..`1b46d05`), two
  of which bear on LR2/LR3; the LR reviewer's scratch clone landed on that
  main, it read those commits' doctrine hunks (never their records), and the
  verdict names them as out-of-scope facts, formed after phase 1.
- **The session limit.** After LR and CS had closed, an API session limit
  killed the BS reviewer mid-reconcile and the CMF reviewer mid-re-run. On
  Mike's "pick up where you left off": both were **resumed from their own
  transcripts** by message rather than re-spawned — BS had already received
  the deferred material, so a fresh reviewer could not have reconciled
  honestly; CMF had not, so its independence was intact and its scratch
  state survived. Both disclose the interruption in one sentence. Nothing
  was re-run blind and no tier was lowered.

## What the passes found — the headline per pass

- **BS1 (MAJOR)** — the split board's hook-plane guarantee, *a stale index
  cannot be committed*, is asserted in four places and fails in two
  live-probed slips: a rebuilt-but-unstaged index passes the hook, and a
  sibling session's dirty item state line is absorbed by `rebuild` under
  CONCURRENCY's own "stage your claim alone" recipe, landing a wrong `✅`
  on `main` under a green hook. The migration itself is lossless (line
  multiset compared).
- **CMF1 (MAJOR)** — the reply plane's premise is false by the hook
  contract: a `Stop`-hook block cannot make the flawed reply unread. This is
  the finding the unwiring session reached the same day from transcripts;
  the reviewer reached it from the documentation, blind to that commit, which
  is worth having in the record. CMF2–CMF6 say the give-up path was neither a
  give-up nor visible, the doctrine's measurement figures misstate the
  measurement, the rescope's argument is a class but its code is three paths,
  P1 fires on product identifiers, and no threat was enumerated for a
  machine-wide fail-open hook.
- **LR** — the removal was executed cleanly on the doctrine; the misses are
  at the board's edge (a live item the delta edited still says
  "three-element floor"; a principal-authored open item was deleted rather
  than closed — since restored by `1b46d05`) and in the fleet ("children shed
  the sentence at their next pin bump" is unenforced; 13 of 17 pinned
  children still carry a Laws sentence).
- **CS** — three MODERATEs on the search tool: `--regex` gate and probe run
  against different texts so anchored or escaped patterns can never hit;
  a trailing `--search` silently renders a transcript at exit 0; no threat
  step or output caution for a tool that prints excerpts of a private corpus.
  The design was never reviewed before it was built to (CS13).

## A finding of this session's own, queued

`/security-review` reads the **session's** pending diff, whatever path it is
aimed at — three reviewers aimed it at their scratch clones and each got the
shared worktree's dirty state, which at that moment was the RG brief and its
sibling being written. Cross-pass, different subject, disclosed by all three;
no reviewer's own sibling was reachable because they were out of the tree.
Queued as `160-…/190` with counsel, nothing decided: this is the SL2 channel
class for the third, fourth and fifth time, and under the partition shape
the reviewer does not control what is pending.

## Pointers after this session

Closed cycles (LR, CS) and open ones (BS, CMF) are all rewritten as ruling
items with **no queue glyph** — a `🎯`/`🛑` lead, the counts, the MAJOR and
MODERATEs in one paragraph, the verdict link, the delta and intent record —
so a future taker's grep for `⏳` finds only the one genuinely open pointer
(the RG brief). That is the `130-…` item's option (a) applied by hand, not
ruled; pointerscan is clean either way.

Floor green on the hook plane at every commit; the ci-plane run on the
pushed merge is the all-clear and is named in the close-out below.
