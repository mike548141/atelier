# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0210-attribscan-unquoted-attribution-cold.md` (`REVIEW.md` rule
1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `a18861ae`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

## What the barred intent records say, in brief

- `320/100` carries, under the proposal, a later measurement by the author session (2026-11-12
  UTC): a whole-tree run over 30 local repositories gave 3,469 findings; a seeded random sample of
  200, sorted by a Sonnet agent and spot-checked, put precision at about 31% (roughly 25% to 38%).
  It names what fools the check (a bare "ruled" with no ruler, pending forms such as "to be ruled
  on", evidence outside the window or in forms the patterns miss, a review's own verdict word, the
  body of an ADR) and lists fixes it calls owed before 2027-02-08. Recall was not measured. On
  2026-11-14 no commit after `641f017f` had changed the scanner, so none of those fixes had landed.
- `320/810` records the slice-2 landing with the same fleet probe the changelog states (22 of 22
  exit 0 on the landing date and on the flip date), the 1,372 of 5,144 whole-tree share,
  "Tests: 32" (36 at HEAD, after `641f017f`), and that the dates are the run's choice.

## The brief-writer's own questions

1. **Precision against the flip.** The fleet probe counts exit codes on `--against HEAD^`, which
   reads one commit per repo. Does "0 non-zero exits" say anything about how often an ordinary
   commit after 2027-02-08 will be blocked? Set it beside the author's own later measurement above.
2. **Moves and splits.** `scan_against` runs `git diff --no-renames`, and the staged plane reads
   what git reports as added. A record moved or split into per-item files (a routine operation in
   this estate) makes every old line "added". Does a record-store split after the flip get blocked
   by its own history, and does the README's "an old record is never re-judged" survive that?
3. **Push depth.** The CI template is `--against HEAD^`. A push of several commits is read at its
   tip only. Is the hook the only cover for the others, and is that stated anywhere a reader of the
   registry would see it?
4. **The advisory form on CI.** The floor entry's comment says a floor-level softening selects the
   advisory argv on both planes, and on CI that argv (`--warn --staged`) is an empty diff. Does a
   child that declares the advisory form get a CI line that reads as a pass while reading nothing?
5. **Evidence that is not evidence.** Any double-quoted run of two or more characters (a quoted
   term, a file name), any `>` line, any `NNN/NNN` (the item's own id included), the bare word
   `transcript`, and `session` plus six hex characters all clear a hit. A board id need not exist.
   How cheap is a false clear, and is it cheaper than writing the allow marker?
6. **One marker, several hits.** The allow marker is searched across the whole block, so one
   reasoned marker exempts every attribution within three lines of it. Intended?
7. **Name-possessive grammar.** `[A-Z][a-z]+'s (ruling|directive)` fires on any capitalised word:
   a sentence-initial "Today's ruling", "Board's ruling", a reviewer's verdict word. And the role
   grammar has no `his decision`, `his call`, `he decided`, `he chose`, `per <name>`. Which way
   does the trade fall, and is the recall gap stated (the README says only "a grammar")?
8. **Printed paths.** The excerpt passes through `report.safe_text`; `f.path` in `render` does not.
   A file name with a control character from a diff or a walk: what does it print?
9. **The changelog entry's place.** In `20e7fc35` the new entry was inserted directly under an
   existing `### Added (2026-11-10 — blockscan ...)` heading, leaving that heading empty and a
   second `### Added (2026-11-09 — blockscan ...)` heading after the new entry. At HEAD the empty
   heading is still there (line 280 on 2026-11-14), now followed by a later slice's entry.
10. **Its own verdicts.** This repo's reviews and briefs say `ruled` about the principal often, with
    quotes on adjacent lines that may fall outside the window. Will the scanner block the repo's own
    review records after the flip?

## What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC unless stated, foreground, load average 5 to 6 on 12
cores, at `origin/main` `2c1f0296`.

- `cd tools && python3 -m unittest test_attribscan`: 36 tests, OK, exit 0, about 7 s.
- `cd tools && python3 -m unittest test_floor.AdvisoryCountContract`: 33 tests, OK, exit 0, about
  45 s. One fixture inside it prints a board-rebuild line to the terminal; the worktree stayed clean
  (`git status --short` empty afterwards).
- `python3 tools/attribscan.py --selftest`: `selftest OK`, exit 0.
- `python3 tools/attribscan.py --root . docs`: exit 0; 848 unquoted attributions in 337 of 1,175
  files; coverage 1,175 files, 171,549 lines. The first listed hit is in `docs/ROADMAP-DONE.md`, a
  line naming "the board-store ADR" with no number.
- `python3 tools/attribscan.py --against HEAD^ --root . docs`: exit 0, clean, 5 files read.
- `python3 tools/attribscan.py --against nosuchrev --root . docs`: exit 2, "cannot resolve
  revision".
- `python3 tools/floor.py --list --root .`: attribscan listed `enforced`, `fleet`, `decl 1/5`.
- The two `coldsweep --commit` lines in the brief: each exit 0, no body printed.
- `merge-base --is-ancestor` on `20e7fc35` and `641f017f`: both ancestors of `2c1f0296`.
- **Not run:** the fleet probe over child checkouts (left whole to the pass), and any probe of the
  questions above.
