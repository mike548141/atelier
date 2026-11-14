# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0239-namescan-private-names-branches-titles-cold.md`
(`REVIEW.md` rule 1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session
`51ccf0f9`), which authored none of the delta. Open this only after act 1 is committed. Everything
here is a floor, never a fence, and none of it is a finding: the brief-writer read the code once
and probed none of these past what is recorded below.

## What the barred intent records say, in brief

- `160/360` carries, under the earlier pass's summary, the author's landing note for this check:
  `NP2` built 2026-11-10 as `tools/namescan.py`, and **the counsel's pre-push shape was not
  built**: the commit-msg hook reads the branch at commit time, so a branch renamed afterwards is
  seen only by CI's pushed-range report. The same item carries a 2026-11-09 note that `NP5` is
  still the principal's.
- `320/810` records the slice-5 landing with the same measurement and fleet probe the changelog
  states, "Tests: 14 … plus `tools/test_commitmsg.py` (12)", that the date is the run's choice
  (four weeks after the three already set, in the order built), and that existing clones need
  `tools/commit-msg.sample` installed for the message-plane checks to run, with `floorfleet` not
  yet checking for that hook.
- The landing commit's body says the failure "had recurred in head refs", and gives the same
  measurement and probe.

## The brief-writer's own questions

1. **Push-time refs.** The harm in the doctrine was a head ref and a title in a public PR list. A
   ref named only at push (`git push origin HEAD:<name>`, the form this estate's own worktree
   sessions use from a detached HEAD) never passes a commit-msg hook that can see it, and
   `commitmsg.branch` returns empty on a detached HEAD, so the message plane reads no branch at
   all there. Which surface, if any, reads such a ref before it is public?
2. **CI with no term list.** The CI template has no `--require-terms`, and a hosted runner has no
   `~/.claude/leakscan-terms.txt`. So on CI the check reads structural shapes only, which do not
   include a repo or client name. The cover note says so on stdout; does anything a reader of the
   board or the floor list sees say so? Is CI's "clean" for the pushed ref name meaningful?
3. **PR titles and bodies.** `NP2` and `PROPAGATION.md` rule 2 name PR titles; nothing here reads
   one. `PROPAGATION.md` § *Report without harming the parent* still says a branch-name and title
   lint "is not built". Stale now, or still true for the push-time rung? Either way, V3.
4. **A subject cannot exempt itself.** `scan_message` calls `allowmarker.present` on the whole
   message, subject included. Does a title of the form `x: <name> namescan:allow: y` exempt itself?
   And does one body marker also exempt the branch name, which the author may not have looked at?
5. **Ref-name separators.** Branch names use `-`, `_` and `/` where a term list holds words. Does a
   term bound by `\b` still match `report-<name>-1`? (The test says yes for `-`.) What of
   `report_<name>`, `<name>/x`, a camel-cased or squashed form?
6. **Leak through the check.** The excerpt is leakscan's redacted excerpt cut to 60 characters.
   Is that excerpt redaction of the term, or of the span around it? What does `--json` carry, and
   the stderr note `allowmarker` prints for an unparseable marker ("the head of the marker, up to
   forty glued characters")? A public repo's CI log is public.
7. **Option injection.** `--range` is passed straight to `git log` after the format argument. A
   spec beginning with `-` (for example `--output=<path>`) is read as an option. Only a local user
   or a template sets it, so is this a finding or a one-line hardening?
8. **Comment-char stripping on CI.** `commits()` cleans each pushed message with `#` as the comment
   character, so a title starting with `#` is dropped and the next non-blank line read as the
   subject. Does a title like `#123: <name>` escape the CI report?
9. **Scope key.** A repo public on the forge but not declaring `"visibility": "public"` is silently
   out of scope (`not declared public: out of scope.`, exit 0). Is the declaration checked against
   the forge anywhere?
10. **Malformed floor config.** `pdlistscan.declared_public` raises its own `ConfigError`, a
    `RuntimeError` subclass, so `guarded_main` turns it into exit 2. Confirm, and confirm the
    message-plane hook then blocks the commit (fail-closed) for a reason the user can clear.
11. **The clean head on a whole-history run** says "on the pushed range" for any `--range`, not only
    `pushed`.
12. **Tests.** No test covers a structural shape in a title, the CI plane's `GITHUB_HEAD_REF` /
    `GITHUB_REF_NAME` read, `--json`, or the NA4 property on stderr. The 14 tests count matches
    HEAD.

## What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC unless stated, foreground, load average 4 to 6 on 12
cores, at `origin/main` `461fdf92`, on a detached HEAD.

- `merge-base --is-ancestor` on `6b6110c9`, `b74cd5ef` and `ba55be27`: all ancestors.
- `cd tools && python3 -m unittest test_namescan`: 14 tests, OK, about 3 s.
- `cd tools && python3 -m unittest test_commitmsg`: 12 tests, OK, exit 0.
- `cd tools && python3 -m unittest test_floor.MsgPlaneTest`: 10 tests, OK, exit 0.
- `cd tools && python3 -m unittest test_precommit.CommitMsgHookTest`: 7 tests, OK, exit 0.
- `python3 tools/namescan.py --selftest`: `selftest OK — namescan`, exit 0.
- `python3 tools/namescan.py --range pushed --root . --warn`: exit 0, clean, with the note "no
  pushed range known: reading HEAD only"; advisory count 0.
- `python3 tools/namescan.py --range HEAD --root . --warn`: clean over 2,325 commits (the landing
  measured 2,285), with this machine's term list present; about 0.5 s.
- `python3 tools/namescan.py --range nosuch..HEAD --root . --warn`: exit 2, git's own error text.
- `python3 tools/floor.py --plane msg --list --root .`: `namescan enforced fleet decl 0/5`.
- The `coldsweep --commit 6b6110c9` line in the brief, with the five non-tool paths: exit 0, no body
  printed, the two board-store files left out by default.
- `git status --short` after the test runs: empty.
- **Not run:** the fleet probe over child checkouts, a read of the forge's PR titles and head refs,
  and any probe of the questions above. All are left whole to the pass.
