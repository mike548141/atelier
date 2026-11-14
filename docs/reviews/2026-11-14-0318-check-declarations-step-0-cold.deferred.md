# Held back — every check states its five declaration fields (`115/120`, step 0)

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `263945c1`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Does a `Declares` citation that resolves actually name the rule it claims?
2. Can an `Unmet` read as met in any view?

## The brief-writer's questions

3. The design note's table makes `window` `met` whenever a `fits` value is present. Three checks
   declare `fits="outside-warn-only"`, a statement that the licensing context is *outside* their
   window, and each reads `window ✅ met`. Does `met` there tell a reader the field is stated, or
   that the check passes the window test? Is a reader of `decl N/5` able to tell which?
4. `_MARKER_OPEN` says the fits answer "waits on the open question whether an allow-marker brings
   the licensing context inside the window". `2a6d7a41` (2026-11-12) recorded the principal's answer
   in `GUARDS.md`, and `tools/floor.py`, `tools/README.md` ("One question is carried, not settled")
   and the test that pins the text were not touched after it. Are six declarations, a README
   paragraph and a test now stating an open question that the record says is answered? Whose job
   was the sweep (V3)?
5. `purpose_gap` reads `met` when it is non-empty and not, case-insensitively, the `why` string
   verbatim. Is any of the registry's stated gaps a restated mechanism the test cannot see, and is
   "not identical to `why`" the bar the design note's "not the `why` text" meant?
6. `rule` turns `met` on any non-empty `reviewed` string. Nothing checks that it names a verdict
   file, or that the verdict read this rule against this check. Is that the machine's half, or a
   way to reach `met` with no verdict?
7. A grounding `incident` is accepted when it is `injected: …`, `board NNN/NNN`, or *any* file path
   that exists inside the base, not only a verdict under `docs/reviews/`. Could `README.md` stand
   as an incident? Does that match "a board item, a verdict path"?
8. `test_an_unreadable_replay_file_never_raises` asserts only that `grounding` reads `missing`. In
   `read_declaration`, any exception in any field sends all five fields to `missing`. Is one broken
   test file elsewhere in the repo meant to erase a check's whole declaration, including fields that
   resolved? Is `missing` (not declared) the honest state for "declared, and the reader failed"?
9. Two of the three replays name `injected:` incidents; the third names `board 010/020`. Does each
   replay fail when its check stops firing (LA3), or does it test a neighbouring behaviour?
10. `--json` on *any* plane, including `--plane hook --json`, computes `declarations_report`, which
    reads every cited file and parses every replay module. The hooks call `--plane hook` without
    `--json` today. Does "the hook plane pays nothing" hold for every caller, or only for the
    one invocation the hooks make?
11. `floorfleet`'s line is built from `floor.Config()`, an empty config, against this checkout's
    tree. It cannot see any child's `local` checks or their declarations. Does a fleet-board line
    that reads "21 checks" for every child say what it covers?
12. The CI line goes to stderr only on a text run; a `--plane ci --json` run carries the key and no
    line. The floor workflow runs the text plane (`floor.yml` line 134), so the line reaches every
    child's CI log, read from atelier's registry. Does a child reader of that line know it counts
    atelier's checks plus that child's `local` ones, and nothing of the child's purpose?
13. A child's `local.<name>.declares` text reaches `--declarations` output verbatim. If a floor
    workflow ever prints that table, or a reason string, inside Actions, can a crafted reason emit a
    `::` workflow command? Is `_safe_rel` enough against a symlink inside the child that points out
    of it (`Path.is_file` follows links)?
14. The census marked three windows as met that step 0 states as `Unmet` (per the commit body,
    barred until phase 2). Was moving a census ✅ to `Unmet` within step 0's brief ("`Unmet`
    wherever the census has no ✅"), or a departure from the design the principal approved?

## Facts read off the machine (2026-11-14 UTC, worktree at `672acdd9`)

1. `python3 tools/floor.py --root . --declarations --json`: 21 checks, 0 meet all five; field
   states across all 105 fields: 22 `met`, 7 `resolves`, 76 `unmet`, 0 `missing`. The commit body
   gives the same three totals.
2. `cd tools && python3 -m unittest test_floor`: 255 tests, OK, about 184 s. `test_floorfleet`: 127
   tests, OK, about 14 s.
3. `git log --oneline ba55be27..HEAD -- tools/floor.py tools/floorfleet.py tools/test_floor.py
   tools/test_floorfleet.py` prints nothing.
4. `docs/method/GUARDS.md` at HEAD has `## Before building a check: the evidence window` (line 151)
   and `## What every check declares` (line 214).
5. `test_the_open_marker_question_is_carried_not_settled` pins `_MARKER_OPEN` in the `window` of
   `leakscan`, `sizescan`, `datescan`, `attribscan`, `namescan` and `quotescan`.
6. The floor workflow parses `floor.py --list --plane ci` with
   `awk '$2!="disabled" && $3!="local"{print $1}'` (`.github/workflows/floor.yml` line 126). The
   new column comes after the origin column, so `$2` and `$3` keep their meaning; at HEAD the parse
   printed 21 names, including the 12-character `conflictscan`.
7. `.githooks/pre-commit` line 84 runs `floor.py --plane hook --root … --tools …`, with no `--json`.
8. `DeclarationConfigTest.GOOD` uses `"rule": ["docs/x.md"]`, which is not a form the citation
   grammar knows; it tests loading, not resolving.
9. The 2026-11-12 allow-marker answer is recorded in `115/120` line 96 onward and, through
   `2a6d7a41`, in `GUARDS.md` § *Before building a check*.
10. The design note's status line still reads "proposed (design only; nothing built and no check
    changed)" at HEAD, after step 0 built it.
