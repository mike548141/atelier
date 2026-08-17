# The rollout's record, swept — and a defect that only bites the human plane (2026-08-17, 1057 UTC)

**The ask.** Mike, opening the session: *"Now there are no other active sessions
do the 'board split' of the roadmap. Atelier repo details whats expected and
why"*, then *"Did you bump the aterlier pin as well? If not please do"*, then
*"Ask any questions etc you need to"*, and finally *"once all that is done lets
record everything, tidy up and be ready to close this session"*.

**Both halves of the work-instruction are child-shaped, and saying so was the
first useful act.** This is the standing fleet prompt — one session per repo —
reaching an atelier session for the second time today. atelier's own board split
landed 2026-08-15; the 0530 session had already done atelier's part of the
rollout, which is the spec rather than another migration. And **atelier has no
atelier pin**: the pin lives only in a child `CLAUDE.md`, `PROPAGATION.md` §5
makes bumping it a per-repo in-the-child act, and `tools/pins.py` is deliberately
read-only for exactly that reason. So *"if not please do"* had no target here,
and the honest move was to put it to Mike rather than either ignore it or invent
a target for it.

**Two questions asked, two ruled.**

1. **The pin.** Offered as three options — do nothing, nudge the stale child on
   the channel, or bump the children's pins from here under a recorded exemption.
   Mike: **"Nothing — it was for the children."** So no child was touched. The
   fleet state was read and recorded as evidence only: 14 of 17 children behind
   at the reading, `ros` 56 behind having just finished its own split without
   bumping, `shed` current at `0af3006` having bumped twice the same day.
2. **Scope.** Mike: **"Refresh + queue the bug properly"** — refresh the rollout
   record, and sharpen the 🔥 mixed-root scanner defect into a takeable brief
   **without building it**. `pathscan`, `wrapscan`, `linkscan`, `sizescan` and
   the seven others were not edited. That bound held.

---

## The premise was false again, in the same way

*"No other active sessions"* — `ListAgents` showed **24 peers, four of them
atelier**. The 0530 session recorded nineteen. This is now a pattern rather than
an incident, and it is worth naming as one: the standing prompt is written for a
session that is alone, and no session it reaches has been alone yet. So the
0530 discipline was repeated without rediscovering it — claim on `main` before
the worktree, stage two paths by name, re-read every measurement at head.

That last one earned its keep within the hour. **`cbom` split between two reads
twenty minutes apart in this session**: the first survey read a 1,367-line
monolith, the second read a 118-line generated index. Nothing was wrong with
either reading.

## The channel, used in both directions

A peer atelier session opened with a `290` section collision it had already
resolved by the doctrine's own tie-break, and asked what this session held. The
reply named the two files and the two rulings; nothing collided.

The peer then **re-ran this session's fleet count rather than taking it** — the
channel's own re-run rule — and came back with `cbom` split, which this session
had by then also caught. Two things came out of that exchange that would not have
come out of either half alone:

- 🔑 **`cbom` has no remote and no remote-tracking branch.** Its split exists on
  a local `main` only. "Pushed" is not a category there, so it is not equivalent
  to the other eight for anything that depends on origin. The peer flagged it
  rather than counting it silently, and it is now recorded on the item that way.
- The peer stated its **pattern and its timestamp** before its result. That is
  the 0530 session's keeper lesson applied by someone else: *a measurement that
  does not name what it counted can falsify a correct report*. Because both
  counts named their definition, the one difference between them resolved in a
  sentence instead of a round.

The peer also added `010/120` to the section this session was holding, announced
rather than merged silently. Different file; no conflict.

## What landed

### `010/030` — the rollout record, measured rather than adjusted

The item read *"`faves` done, `ros` and `shed` open"*. That was true for about
four hours. Measured 2026-08-17 1057 UTC, one pattern over every repo under the
estate root — a `docs/roadmap/` directory means split, `wc -l docs/ROADMAP.md` at
the split commit and at its parent for the two index figures:

**Nine children split, all on 2026-08-17, each in its own session.** `faves`
6,274 → 268 · `ros` 5,513 → 384 · `shed` 3,465 → 136 · `cbom` 1,367 → 118 ·
`kainga` 323 → 103 · `tuhura` 173 → 58 · `stewart-drive` 98 → 66 · `derry-hill`
74 → 69 · `rpi` — → 69. **Two monolithic boards remain:** `docker-heap` 302 and
`nova` 274. `numen` 24 is archived and never pushed, so it is out of scope rather
than outstanding.

🔑 **`rpi` never migrated — it was born split.** There was no `ROADMAP.md` before
`4bd429c`; its board was *written* in the store form from nothing. That is the
stronger evidence for the form than any of the eight conversions, because it
shows the form is adoptable without a monolith to convert, which no migration
could have shown. It reads as the least interesting row in the table and is the
most interesting fact in it.

⚠️ **One figure was flagged rather than corrected.** `faves`' index measures 268
lines at `672ad17` under the definition above; the item previously recorded 271
under a definition it did not state. Three lines. Which point in that session was
counted is the likely difference, so it is recorded as a definitional gap and not
overwritten as an error — the 0530 lesson, applied to this session's own
temptation to book a small win.

The three figures the item *did* get wrong (5,213 / 3,125 / 1,853, all low,
`faves` alone out by 4,421) stay named on the item, because the failure mode
recurs and a corrected record that hides its correction teaches nothing.

### `010/110` — the brief, and a blast radius four times what was recorded

The item said the mixed-root defect was *"one shape, shared by at least four
tools"*. Swept at HEAD rather than estimated: **eleven**, every scanner that
takes both `--root` and a path list, minus one — `datescan`, `leakscan`,
`linkscan`, `pathscan`, `plainscan`, `reviewscan`, `secretscan`, `sizescan`,
`spellscan`, `stampscan`, `wrapscan`. `reviewscan` spells it `Path(p).resolve()`,
which is the same defect in different words. `board`, `publishscan` and
`harvestscan` accept a path list and ignore it; `coldsweep` walks from `root`.

Three findings the sweep produced that the estimate could not:

- 🔑 **`pointerscan` already gets it right** — `(root / raw) if not
  Path(raw).is_absolute() else Path(raw)`, at two call sites. So the fix needed
  no design decision: it is an in-tree reference implementation to copy, not a
  new convention to argue about. That is what turned "fix candidates, cheapest
  first" into "the fix, chosen".
- 🔑 **`floor.py:1485` pre-resolves before it calls anything**, so the hook plane
  and CI have handed every scanner an absolute path and have **never once
  exercised the defect**. The guard is correct wherever a machine calls it and
  wrong wherever a human does. That inverts the usual risk story — the plane with
  no coverage is the plane whose output a session reads, believes and reports
  from — and it explains a survival that otherwise looks like luck.
- 🔑 **It needs a path collision to bite, and the propagation model guarantees
  one.** Every tool exits 2 on a target that does not exist, so a relative
  argument only *silently* mis-resolves when the same relative path exists in
  both trees. `docs/ROADMAP.md`, `docs/method/`, `docs/SESSIONS.md` — every child
  carries them under the same names by design. The thing that makes the estate
  coherent is the thing that makes this bug reliable.

The brief also names the one judgement left (`root / p` still permits an
*absolute* path outside `root`, an explicit caller act rather than a silent
mis-resolution — a separate commit or a recorded acceptance, not a blocker), why
the shared-layer question at `115/080` does not gate it (eleven copies is a
better argument for the harness than four, and a false clean is in every
session's hand today), and the test that must exist: two temporary trees carrying
the same relative path with different content and different ignore files,
`chdir` into the second, call each tool's `main` with `--root` pointing at the
first, assert the finding names the first tree's file — **parametrised over the
eleven, not written eleven times**.

## Deliberately not done

- **The fix itself.** Mike ruled queue-not-build. Eleven tools untouched.
- **Any child's pin.** Mike ruled it, and `PROPAGATION.md` §5 says it anyway.
  `ros` is 56 behind after its own split; that belongs to a `ros` session, and
  the observation is recorded here rather than acted on from here.
- **`docker-heap` and `nova`.** Child work, in the child's session — the rule the
  whole rollout is built on. `docker-heap`'s tree was not clean at the reading,
  which is a second reason not to reach into it.
- **A rule-4 pointer.** Judged and stated rather than skipped: this delta is a
  board record and a specification, not self-authored doctrine and not a
  first-of-kind build, so rule 4's trigger does not fire. The eventual fix to the
  eleven tools will be code, and will queue its own.

## Verified, not asserted

`board.py rebuild` after each item edit; `linkscan` clean; `wrapscan` clean on
both edited files (the twelve findings in the tree are pre-existing frontmatter
and CHANGELOG lines, untouched here); the full hook ran on every commit, with
`board` enforced.
