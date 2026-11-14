# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0258-commit-message-plane-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `3e2239de`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

## What the barred intent records say, in brief

- `320/810` records the plane's landing (2026-11-10) as `floor.py --plane msg`,
  `.githooks/commit-msg` beside `pre-commit`, and a `msg` template on `Scanner` absent by default;
  that a clone predating the hook is told by one line on its own next commit and nothing reaches
  into it; and, twice, that **`floorfleet` does not yet check for this hook**, so until each
  existing clone installs `tools/commit-msg.sample` the two message checks do not run there and
  their CI report is the only cover.
- `320/550` records part (a), `leakscan --messages`, as built and report-only, and part (b), the
  same rules on this plane, as **not built**: wiring it is one registry line, but `leakscan` has
  no advisory form and blocks on a hit, so it would be a blocking check over every message body
  from day one with no warn-first period and no fleet measure behind it.
- The queue pointer scopes the delta to "the commit that adds the hook", but lists
  `tools/commitmsg.py` (added by `6b6110c9`, the namescan landing) and "the refused flags" (added
  by `49f3d407`, the `leakscan --messages` landing). The brief folds both in.

## The brief-writer's own questions

1. **`-h` through `flags`.** `forbidden_flags` judges only names longer than two characters that
   start `--` against a blocklist that has no `--help`. At the function, `-h`, `--help` and `--he`
   are all allowed (see the run below). Every atelier scanner uses argparse, where `-h` prints help
   and exits 0 without scanning. If `Config.load` does not refuse it by another route, a child's
   `flags: {"namescan": ["-h"]}` turns the check into a guaranteed pass on every plane. This is
   fleet-wide, not new with this plane, but it answers the pointer's second question directly.
   Not driven through a real config.
2. **The advisory form drops `--require-terms`.** namescan's `msg` template carries
   `--require-terms`; its `advisory` template does not. A child declaring namescan advisory gets a
   msg-plane run that passes silently with no term list. Is that the softening the advisory
   declaration is meant to grant, or a fail-closed argument lost on the way?
3. **A user who cannot clear the refusal.** namescan's msg template carries `--require-terms`, so
   in a repo declared public, a clone with no local term list (an outside contributor to a public
   repo, or a fresh machine) has every commit refused with exit 2, before and after the flip date.
   Is the text it prints enough to clear it without `--no-verify`? Does the scope check
   ("not declared public") run before the term-list check, so a private repo is never affected?
4. **"Silently" against "finds out".** `skills/fleet-sweep/SKILL.md` lines 53–54 say a repo
   without `.githooks/commit-msg` "skips commit-message checks silently"; the README, CHANGELOG
   and `floor.py` say such a clone is told on its own next commit. Both may be true of different
   things (the tracked file against the installed hook); V5 either way.
5. **"Once."** `commit_msg_hook_note`'s docstring says a clone finds out "on its own next commit,
   once, in a line". The code returns the note on every hook-plane run until the hook exists.
6. **The note in a linked worktree.** It builds the hook path as `root / <git rev-parse
   --git-path hooks/commit-msg>`. With `core.hooksPath` relative (`create-repo` sets it to
   `.githooks`), absolute or unset, in a linked worktree, does the path resolve to the hook git
   will actually run? (`create-repo` already records one worktree-only failure of this family: a
   relative `hooks.atelierTools` that blocked every worktree commit.)
7. **The message-file path.** git passes the hook a path; in a linked worktree or from a
   subdirectory, is it relative, and relative to what? `floor.py` hands it on unchanged in the
   scanners' argv. Check the scanners' working directory against it.
8. **Which commands run `commit-msg`.** `GUARDS.md` names `git commit` and a merge. The table above
   that paragraph was measured for `pre-commit`; nothing says the same was measured for
   `commit-msg` on `cherry-pick -e`, `revert` (which opens an editor by default), `rebase -i`
   reword, `merge --squash` then commit, or `commit --amend`.
9. **CI comment char.** `commits()` cleans every pushed message with `#`, ignoring the repo's
   `core.commentChar`, so a title beginning `#` is dropped on CI and the next line read as the
   title, while on the msg plane the repo's comment char is used. Two planes, two readings.
10. **The selftest's guard.** "no existing registry entry reads a message by accident" asserts only
    that no entry has both a `hook` and a `msg` template. `MSG_CHECKS` is said to be "named so a
    test notices"; check which test compares it to the registry, in both directions.
11. **The hook's tools-dir resolution.** `ATELIER_TOOLS` or `hooks.atelierTools` can point the hook
    at any `floor.py`; `python3` comes off `PATH`. Same shape as `pre-commit`, so likely not new,
    but the plane inherits it.
12. **`str.format` on templates.** `_render` formats each template element with the message path
    as a value; a path containing braces is safe as a value. Confirm no template element is built
    from user input.

## What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC, foreground, load average 4 to 6 on 12 cores, at
`origin/main` `854838f8`, on a detached HEAD.

- `merge-base --is-ancestor` on `55f23034`, `6b6110c9`, `b74cd5ef`, `49f3d407` and `ba55be27`: all
  ancestors.
- `cd tools && python3 -m unittest test_floor.MsgPlaneTest`: 10 tests, OK, exit 0.
- `cd tools && python3 -m unittest test_precommit.CommitMsgHookTest`: 7 tests, OK, about 3.5 s.
- `cd tools && python3 -m unittest test_commitmsg`: 12 tests, OK, about 2 s.
- `python3 tools/floor.py --selftest`: `floor selftest: ok (21 scanners, 0 failure(s))`, exit 0.
- `python3 tools/floor.py --plane msg --list --root .`: two rows, `namescan` and `quotescan`, both
  `enforced`, `fleet`; exit 0.
- `python3 tools/floor.py --plane msg --root .`: the `--message-file` refusal, exit 1.
- `floor.py --plane msg` with a scratch message file holding a plain title: both checks clean,
  both advisory counts 0, `✅` on both rows, exit 0.
- `diff .githooks/commit-msg tools/commit-msg.sample`: identical.
- `floor.forbidden_flags(['-h', '--help', '--he', '--mess', '--ran'])`: `['--mess', '--ran']`.
  The three help spellings pass the function; not carried to a real config.
- Not run: any hook install, any scratch-repo commit through the hook, any fleet probe, and
  `/security-review`.
