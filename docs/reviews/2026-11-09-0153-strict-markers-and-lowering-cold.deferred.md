# Deferred reading for `2026-11-09-0153-strict-markers-and-lowering-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether any malformed form still exempts after the date; whether the new rule covers every way a
repo can soften a check.

## The brief-writer's questions

1. Patch the date in a scratch copy to after the cut-over: does every malformed form stop exempting
on every reader?
2. What does a child see on the day, and is there any path from "the date passed" to a noisy red
with no one told?
3. The lowering table: is every softening a child can do on the table, and is the "visible in the
fleet view" claim true for each?

## What the brief-writer held back

- The changelog credits a review-brief skill sentence to this work (AM11); the skill file is not in
  `6d26b058`'s file list. Check where that sentence landed.
- The grace date is a code constant, 2026-12-09; the cleanup of the warning path is left for after
  it.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`test_allowmarker`: 55 tests, OK, exit 0, under `/usr/bin/python3` 3.9, and again inside the full
suite under 3.14. `test_leakscan`: 395 OK. `test_pathscan`: 154 OK. `test_report`: 102 OK.
`test_reviewscan`: 49 OK. All exit 0. `allowmarker --census --root .`: exit 0, 11 malformed markers
(10 in test files, 1 in a scanner's source). `floor.py --plane ci`: exit 0, with 28 `secretscan`
advisories reported and not blocking. `--plane hook`: exit 0. Full suite under `python3` 3.14: 2,643
tests, OK, exit 0, 1,228 s at a load of about 20. `floorfleet --json`: exit 0; 23 rows, 1 parent, 21
wired children, 1 absent. Census over the 21 wired children: 1 hit, in 1 child, in a markdown file;
0 non-zero exits.

