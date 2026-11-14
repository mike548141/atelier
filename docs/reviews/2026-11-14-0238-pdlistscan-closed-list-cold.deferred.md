# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0238-pdlistscan-closed-list-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `fb2c22e6`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

## The brief-writer's own questions

1. **The fleet has moved since landing.** The docstring, the README section and the commit say no
   child declares itself public with a list, so for now the scanner reads only atelier. On
   2026-11-14 UTC, by a read-only count of `.atelier-floor.json` across this machine's child
   checkouts: 6 declare `private`, 3 declare `public`, 12 declare nothing. Each of the three public
   ones was in scope on 2026-11-14 with one `no-list` finding, warning and exit 0. On 2027-03-08
   each turns red unless a list is written, and a list entry is a grant only the principal makes.
   Is anything set to tell him before the date (A7, V1)? And are the 12 with no declaration all
   truly private (A1)?
2. **No key, no scope.** `260/050`'s cross-check, per its landing note, only warns on a missing
   declaration and is red only for says-private-is-public. So a public repo that never declares
   is out of scope here and only warned about there. Is the pair loud enough for the one breach
   that cannot be retracted (A1)?
3. **The exemption is wider than the test's.** `tools/test_personal_data.py` skips `tools/` and
   `instruments/` only when looking for markers; it reads them for listed strings, and atelier's
   list names files under `tools/` as places. The scanner skips those paths for both kinds. In
   atelier, a listed string added to an unnamed file under `tools/` is caught by the test and not
   by the scanner. Is "the same check" true (A2, A5, V1)?
4. **What the test checks and the scanner does not**: a closed set of entries (the test pins the
   IDs), an entry naming a place that no longer holds its string, a named place that matches no
   tracked file, and every entry carrying `Why held` and `Granted by`. In a child the list is the
   only record of a grant, and an empty or reasonless list passes the scanner. Deliberate, and is
   it said (A2)?
5. **Two marker grammars.** The scanner's `leakscan:allow:([a-z0-9,-]+):` is its own; `leakscan`
   builds its marker from `tools/allowmarker.py` (scope list `[A-Za-z0-9_-]+(,…)*`, optional
   whitespace, a reason that must start with a word or quote character, and code spans blanked so a
   mention is not a marker). So a marker mentioned inside backticks in a doc counts here and not
   there, and a reason-less marker, which `leakscan` treats as a mention, counts here too. The other
   direction (a marker `leakscan` honours that this scanner misses) was not probed (A3).
6. **Per-line, case-sensitive matching.** A pinned string wrapped across a line break (a two-word
   name in reflowed Markdown), or in a different case, is not seen; the in-suite test reads the
   whole text with the same case sensitivity, so the line-wrap case is not new, but is it said
   (A4)? Files over 4 MiB, binary files (a NUL byte), files missing from the working tree and the
   list itself are skipped with nothing reported; the coverage line counts only what was opened.
7. **Which tree the hook reads.** The scanner reads the working-tree copy of each path `git
   ls-files` lists, not the index. On the hook plane, a staged string removed from the working tree
   before committing is not seen, and an unstaged one is reported against a commit that does not
   carry it. The floor's window says "the tracked files … whole tree"; is that the commit (A4)?
8. **Any entry licenses any marker.** A personal-data marker is accepted in a file named by any
   entry's `May stand in`, not only the entry that holds the data the marker excuses. The test does
   the same. With one broad entry (atelier's account-name entry names `docs/roadmap/**` and
   `docs/reviews/*.md`), any personal-data marker in those stores passes. Intended?
9. **The parser fails quiet.** `parse_list` starts an entry only on `## PD<digits> ` (a space after
   the number). A heading written `## PD6:` or `### PD6 —` is not an entry; its bullets are folded
   into nothing, its strings are never checked and its places never license anything. A
   `May stand in` token that is prose (atelier's given-name entry) becomes a glob that matches no
   path. Which way does each failure fall: loud or silent (A6)?
10. **Output escaping.** `render` passes `detail` through `report.safe_text` but prints `f.path`
    raw. A tracked path with a control or bidi character is printed as is. `tracked()` decodes
    `git ls-files -z` output as strict UTF-8, so a non-UTF-8 path raises; does `guarded_main` turn
    that into exit 2 or into something read as clean? A tracked symlink is followed by `read()` out
    of the tree. The detail never echoes the matched string, which looks right.
11. **Duplicated code, two homes.** The scanner carries its own copies of `glob_rx`, `ticks`,
    `parse_list`, `PERSONAL_SCOPES` and `MECHANISM_PREFIXES` from the in-suite test (only the scope
    set is pinned against `leakscan`'s real rules, and only in the scanner's tests). A change to one
    copy reaches the other only by hand (V4).
12. **The date's order.** 2027-03-08 is four weeks after `attribscan`'s 2027-02-08, as stated; the
    other dated slices fall on 2027-01-11, 2027-05-03 and 2027-05-31, and slice 4 has no date. The
    floor's hook and CI templates pass no `--warn`; the advisory template does. The floor registry
    declares the grounding `Unmet` ("no test names the incident"). Worth a line?
13. **The test count.** The commit says 21 tests in `test_pdlistscan`; `def test_` counts 21 at
    `6607c0eb` and 24 at the brief's base (the three later ones are `641f017f`'s coverage tests).
    The floor contract test was "215 total there"; the brief-writer's run reports 255 at its base,
    which includes later commits, so not comparable without a run at `6607c0eb`.
14. **The `CHANGELOG.md` placement.** The entry sits under an empty `blockscan` heading that already
    stood bare before this commit (checked at `6607c0eb~1`), so the bare heading is not this
    delta's; the entry is headed 2026-11-09, the UTC day of the commit (02:52 +1300 on 2026-11-10
    local).

## What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC (base `8c06ad60`), foreground, load average about 5
on 12 cores.

- `git merge-base --is-ancestor 6607c0eb HEAD`: exit 0.
- `python3 tools/coldsweep.py --root . --commit 6607c0eb --path …` (the brief's six paths): exit 0,
  738 non-blank lines; the subject and the six-file stat print first.
- `git log --oneline 6607c0eb..HEAD -- tools/pdlistscan.py tools/test_pdlistscan.py
  docs/PERSONAL-DATA.md tools/test_personal_data.py`: `641f017f` only.
- `cd tools && python3 -m unittest test_pdlistscan`: 24 tests, OK, about 5 s.
- `cd tools && python3 -m unittest test_personal_data`: 11 tests, OK, under 1 s.
- `cd tools && nice python3 -m unittest test_floor`: 255 tests, OK, about 171 s. The run printed
  a board-rebuild line; the worktree stayed clean afterwards (`git status --short` empty).
- `python3 tools/pdlistscan.py --selftest`: `selftest OK — pdlistscan`, exit 0.
- `python3 tools/pdlistscan.py --root .`: clean, advisory 0, coverage 1,252 tracked files opened and
  183,447 lines read, exit 0. With `--json`: `clean` true, `in_scope` true, `blocking` false,
  `until` 2027-03-08, no findings.
- `python3 tools/floor.py --list --root . | grep pdlistscan`: one line, `enforced  fleet  decl 2/5`.
- `ls` for `tools/leakscan.py` across this machine's checkouts: one, atelier's own.
- The visibility count and the in-scope run in question 1: the scanner run read-only with `--json`
  against each child that declares public; each exit 0, `in_scope` true, one `no-list`.
- Not run: the 22-repo probe with the date patched to the flip (no recorded command; left to the
  pass), and any probe of questions 2 to 11.
