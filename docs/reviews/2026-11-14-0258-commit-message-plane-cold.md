# Cold pass — the commit-message plane: a `commit-msg` hook and `floor.py --plane msg`

**Board:** `docs/roadmap/160-doctrine-review-owed/1390-rule-4-cold-pass-queued-commit-message-plane.md`
**Status:** act 1 written 2026-11-22 UTC by a Fable 5.1 cold reviewer (orchestrator session
`21422696`, drain session `eca14b23`); act 2 (reconcile) owed. Brief written 2026-11-14 UTC by a
headless Opus 5.5 brief-writer (`cclive` lists it as session `3e2239de`).

**Pass type:** code cold pass, first of its kind, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium. The landing commit adds 355 lines and removes 17: a 54-line
hook and its identical sample, 111 changed lines of `tools/floor.py`, 110 lines of tests, short
doc hunks in five files, and 5 lines of a board item. Add the shared message reader
`tools/commitmsg.py` (149 lines, added by a later commit) and one later 8-line hunk that refuses
three flags.
**Why it earns a review:** it is a new gate plane in the floor every child repo inherits, and it is
**fail-closed**: once installed, the hook refuses a commit whenever `floor.py`, `python3` or the
message file is missing, or any check on the plane exits non-zero. Two checks already run on it,
and both turn blocking by date with no edit (2027-05-03 and 2027-05-31). The worst failure is a
**false clear**: a green `msg plane` line read as "this commit's message was checked" while the
message never reached the checks (a clone without the hook, a commit path git runs no
`commit-msg` for, a child `flags` entry that turns a check into a no-op), so sessions stop reading
titles by hand. The second is the opposite: **a commit refused for a reason its author cannot
clear**, which trains every session to reach for `--no-verify`, and that skips every other hook too.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `3e2239de`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `3e2239de` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; **the queue pointer whole**; **the intent
  records `320/810` and `320/550` whole**, including the author's landing notes on both; the
  landing commit's subject and stat (through `git show --stat --format='%h %s'`, which printed no
  body); the delta's code and doc hunks through `tools/coldsweep.py --commit` for `55f23034` and
  `49f3d407`, and the `floor.py` hunks of `6b6110c9` and `b74cd5ef` in part, all body-free;
  `.githooks/commit-msg`, `tools/commitmsg.py`, the `msg`-plane parts of `tools/floor.py`, the
  namescan and quotescan `--help` text, and the test names of `MsgPlaneTest` and
  `CommitMsgHookTest` at HEAD; commit subjects through `git log`; and, read for house form, the
  same-day sibling brief `2026-11-14-0239-namescan-private-names-branches-titles-cold.md` **and its
  `.deferred.md` whole**, which carries that brief-writer's questions about namescan, some of which
  touch this plane. It opened **no prior verdict**. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words that commissioned the work, 2026-11-09, quoted on `320/810` (asked which of
six candidate checks to build): *"all six, warnings at first and then move to blocking action. With
a staggered turn on of each so they dont all hit at once"*. Two of the six read a commit message
rather than a tree ("private names in branch names and commit titles", and "a quote of him on
commits touching his prompt"), and nothing in the floor read a message: git runs `pre-commit`
before the message exists. **The plane is the run's design choice to carry those two, not his.**
His words fix only that the checks are built, warn first, and then block. Whether a fail-closed
`commit-msg` hook, a `msg` template on the shared registry and a report-only CI form are the right
carrier is yours to attack.

The plane also answers part (b) of an earlier hand-up, `320/550`, whose proposal reads, in part:
*"(b) in the commit-msg hook plane for the message being written, so a new hit cannot be added
while the older ones are waiting for a history rewrite"*. Part (b) is not built (`leakscan` does not
run on the plane); the plane is its prerequisite.

The pointer names two questions as worth the pass's time: **whether the fail-closed hook can stop a
commit for a reason a user cannot clear**, and **whether a child can pass the boundary through
`flags`**. Neither bounds the pass.

## What the work is

One landing commit on `main`, plus the shared reader and one hardening hunk from later commits.
First confirm your tree has them:

```
for c in 55f23034 6b6110c9 b74cd5ef 49f3d407 ba55be27; do git merge-base --is-ancestor $c HEAD || echo "MISSING $c"; done
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read each commit body-free:

```
python3 tools/coldsweep.py --root . --commit 55f23034 \
  --path .githooks/commit-msg --path tools/commit-msg.sample --path tools/floor.py \
  --path tools/test_floor.py --path tools/test_precommit.py --path docs/method/GUARDS.md \
  --path skills/create-repo/SKILL.md --path tools/README.md --path commands/install-hook.md \
  --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit 6b6110c9 --path tools/commitmsg.py --path tools/test_commitmsg.py
python3 tools/coldsweep.py --root . --commit 49f3d407 --path tools/floor.py --path tools/test_floor.py
```

Plain `git show` (and `git show --stat`) is barred: it prints the message body before the diff, and
reading is atomic (rule 1). Always pass `--path`: `55f23034` also edits a board item, and
`6b6110c9` and `b74cd5ef` each add a scanner whose own pass is elsewhere (non-goals, below). Of
`b74cd5ef` and `ba55be27`, read only their `floor.py` effect on this plane at HEAD: `MSG_CHECKS`,
the `quotescan` entry's `msg`/`ci`/`advisory` templates, and how `--declarations` and `--list`
treat `--plane msg`.

Review at HEAD too: `.githooks/commit-msg` and `tools/commit-msg.sample`; `tools/commitmsg.py`;
and in `tools/floor.py`, the module docstring's `msg` paragraph, `Scanner.msg` and
`Scanner.template`, `warns_only`, `MSG_CHECKS`, `MSG_PLANE` and why it is not in `PLANES`,
`FORBIDDEN_FLAGS` and `forbidden_flags`, `Flags`, `_render`, `plan`, `commit_msg_hook_note`, the
advisory selection in `run`, the `--message-file` refusal in `main`, and the selftest lines that
mention `msg`. Confirm what has landed since the brief was written:

```
git log --oneline 854838f8..HEAD -- .githooks/commit-msg tools/commit-msg.sample tools/commitmsg.py tools/floor.py
```

## What the delta claims (extracted, not evaluated)

- **Why a separate plane:** git runs `pre-commit` before the message exists, so a check on a
  commit's message can only run in `commit-msg`, one hook later; neither `pre-commit` nor any CI
  step can read the message before it lands.
- **The hook carries no policy:** it names no scanner; `floor.py --plane msg` decides what reads
  the message, and only checks that declare a `msg` template run there. `msg` is absent by default,
  so no existing scanner changed.
- **Fail-closed:** no message file, no `floor.py` under the resolved tools dir, or no `python3` on
  `PATH` each block the commit; so does any non-zero exit of `floor.py --plane msg`.
- **Refused, not defaulted:** `--plane msg` without `--message-file`, or `--message-file` on another
  plane, exits 1 (except with `--list` or `--declarations`), because "a message plane that read
  nothing would be a green tick over a message nobody looked at".
- **Report-only on CI:** a check that reads a message runs on CI over the pushed range through its
  own `ci` template and only reports, because a pushed message cannot be fixed without rewriting
  history. An advisory declaration on such a check keeps its CI argv.
- **A clone that predates the hook finds out:** the hook plane prints one `commit-msg` line, on
  that clone's own next commit, saying the commit-message checks did not run and where to copy the
  file. Nothing reaches into a clone to install it; `--no-verify` skips this hook too.
- **When it runs:** `commit-msg` runs for `git commit` and for a merge, after git has written the
  message and with `GIT_INDEX_FILE` still naming the index the commit will carry (`GUARDS.md`).
- **A child cannot re-aim it:** `--messages`, `--message-file` and `--range` join
  `FORBIDDEN_FLAGS`, so a child's `flags` "tune a check, they do not re-aim it"; and a `local`
  check cannot join the plane, because it has no message file to be handed.
- **One reader:** `commitmsg` cleans a message one way (comment lines and a verbose scissors
  section removed, `core.commentChar` honoured on the msg plane) and works out the pushed range one
  way, falling back to `HEAD^..HEAD` with a note rather than failing.
- **Installed everywhere new:** `create-repo` copies the hook beside `pre-commit` and
  `pre-merge-commit`; `commands/install-hook.md` installs `tools/commit-msg.sample`; the tracked
  hook and the sample are tested identical.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine. The lenses organise it; they do not bound it. Anything not named a
non-goal is in scope.

**Non-goals:** `namescan` as a scanner, which is `160/1410`'s pass; `quotescan` and
`leakscan --messages`, which are `160/1420`'s; `sweepscan` (`160/1400`); the floor-wide
declarations work of `ba55be27` (`160/1430`); the other checks of `320/810`. Each is read here only
as far as the plane depends on it, and each serves as a live specimen for driving the plane. A
defect in the plane that changes either check's result is in scope; a defect inside either check
that the plane does not cause is not, and is handed to its own pass.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **MH1.** `commit-msg` runs for every way a message enters a commit that the plane needs to
     cover. Measure on this machine's git, as `GUARDS.md` measured the pre-commit table:
     `git commit` with `-m`, `-F`, `-c/-C`, `--amend`, `--fixup`, `--allow-empty`, from a subdirectory and from a
     linked worktree; `git merge` (clean and after a conflict); `git merge --squash` then commit;
     `cherry-pick` with and without `-e`; `revert`; `rebase` and `rebase -i` reword; `commit
     --no-verify`. Does `GUARDS.md`'s new paragraph match what you measure, and does it say which
     paths the plane does not reach?
   - **MH2.** Fail-closed only refuses for reasons a user can clear (the pointer's first question).
     Find every path to a non-zero exit (hook preconditions, `floor.py` config errors, a check's
     exit 2 for a broken scan or a missing input, a relative or odd message-file path, a
     `core.commentChar` the reader mishandles, a message in another encoding) and, for each, whether
     the printed text tells the author what to do short of `--no-verify`.
   - **MH3.** A child cannot weaken or re-aim a msg-plane check through `.atelier-floor.json`
     (the pointer's second question). `FORBIDDEN_FLAGS` is a blocklist judged by prefix; drive
     `flags`, `advisory`, `disabled` and `scope` declarations against both msg-plane checks and see
     which outcomes a child can reach: a guaranteed exit 0, a dropped fail-closed argument, a
     different message read. Is a blocklist the right shape for a plane whose checks have so few
     options?
   - **MH4.** The "finds out on its next commit" note is true and is the right cover: it fires in
     a clone without the hook (main checkout and linked worktree, `core.hooksPath` relative,
     absolute or unset), stays quiet in one with it, and nothing a reader sees calls a clone
     without the hook covered. Compare every site that describes what happens in such a clone.
   - **MH5.** Report-only on CI is the right posture, and the CI line says what it did not see.
   - **MH6.** A separate `msg` template on the shared registry, absent by default, is the right
     altitude: no existing check's behaviour on `hook` or `ci` changed, and the selftest and
     `MSG_CHECKS` catch a new entry that starts reading messages without saying so.
   Ask too whether `commit-msg` is the right place at all against the alternatives the work could
   have chosen (a `prepare-commit-msg`, a `pre-push` reading the outgoing range, a CI-only check),
   given that a pushed message cannot be retracted from a public repo.
2. **Correctness & quality.** Diff each commit; drive the hook and `floor.py --plane msg` against
   scratch repos you build (fixtures and synthetic term lists of your own), with a scratch copy of
   the tools so a mutation never touches the worktree. Record each overclaim against the text that
   makes it: the hook's header comment, `floor.py`'s docstring and comments, `GUARDS.md`,
   `tools/README.md`, `CHANGELOG.md`, `commands/install-hook.md` and `create-repo`. Check the tests
   would fail on a broken change (drop the refusal in `main`, make `plan` list a msg check on the
   hook plane, make the note fire always).
3. **Completeness / harvest.** Every surface that states the same fact (V3): each place that says
   what a clone without the hook gets, which commands run `commit-msg`, or which checks run on the
   plane; any install path (`floorfleet`, `fleet-sweep`, a child's adoption steps) that installs
   `pre-commit` but not `commit-msg`. One home (V4); no contradiction (V5) between those sites.
   Compare with how the `pre-merge-commit` hook was added beside `pre-commit` (same
   conventions, same tests, same failure text?).
4. **Security & privacy** — mandatory. The hook runs `python3` from `PATH` and resolves the tools
   dir from `ATELIER_TOOLS`, `git config hooks.atelierTools` or the repo: who can steer each, and
   what runs if they do? The message file and `{msgfile}` pass through `str.format` and into an
   argv: a path with braces, spaces, a leading `-`, or a symlink. `commitmsg` reads the message with
   `errors="replace"` and runs regexes over it: a huge message, a hostile `core.commentChar`.
   `pushed_range` reads `GITHUB_EVENT_PATH` and `GITHUB_*` refs on CI: what a crafted event or ref
   can make it read or print. What reaches a public CI log from this plane. Check against OWASP
   ASVS input-handling, output-encoding and logging items, checked, not recalled.
   `/security-review` reads the session's pending diff, not this delta: aim it only at a scratch
   clone holding the delta as pending changes, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root unless it says otherwise, in the foreground, under a load average near 5 on 12 cores; its
results are held in the sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 and git
is 2.50.1 (Apple Git-155) on this machine.

- `cd tools && python3 -m unittest test_floor.MsgPlaneTest; echo $?`
- `cd tools && python3 -m unittest test_precommit.CommitMsgHookTest; echo $?`
- `cd tools && python3 -m unittest test_commitmsg; echo $?`
- `python3 tools/floor.py --selftest; echo $?`
- `python3 tools/floor.py --plane msg --list --root .; echo $?`
- `python3 tools/floor.py --plane msg --root .; echo $?` (the refusal with no message file)
- `python3 tools/floor.py --plane msg --root . --message-file <a scratch file holding a plain
  title>; echo $?`
- `diff .githooks/commit-msg tools/commit-msg.sample && echo IDENTICAL`
- The pointer's flags question, at the function: `python3 -c "import sys; sys.path.insert(0,
  'tools'); import floor; print(floor.forbidden_flags(['-h', '--help', '--he', '--mess',
  '--ran']))"`; then carry what it shows to a scratch repo's `.atelier-floor.json` and a real
  `floor.py --plane msg` run, which the brief-writer did not do.

Use `cd tools && python3 -m unittest test_<name>`, never the dotted `tools.test_<name>` form, which
raises `ModuleNotFoundError` here. Run the tools from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** read-only. Runs over this repo's history and a fleet probe over local child
checkouts (does each carry `.githooks/commit-msg`, is it installed, what does `floor.py --plane
hook` print there) are reads, and are in scope. Any probe that would write to a real repo or forge
(staging, committing, pushing, installing a hook, editing a child's config) is **NOT RUN**: build a
scratch repo in your scratchpad instead.

- Never print a secret, and quote no line from a child repo. This repo is PUBLIC: report child
  results by count only, and name no child, host, client or private path. If a run's output shows
  anything that looks like a private term, stop, record the finding by shape only, and do not paste
  the output.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos and fixtures when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/` or
  `.githooks/`, and never install a hook into the worktree.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/` (the sibling briefs for `namescan` and `quotescan` and their
`.deferred.md` files included), the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0258-commit-message-plane-cold.deferred.md`, the delta commits' message
bodies, and the two intent records whole:
`docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`
and `docs/roadmap/320-child-filed-findings-via-pointing-up/550-no-scanner-reads-a-commit-message-body.md`.
Both carry the author's landing account under the commission and the proposal, and reading is
atomic, so neither can be read in part. What you need from them is quoted in *The acceptance test*
above.

The delta's own text carries the author's account of why (the hook's header, `floor.py`'s
docstring and comments, the README and `GUARDS.md` hunks); it is the delta, and reading the delta
is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1390-rule-4-cold-pass-queued-commit-message-plane.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/550-no-scanner-reads-a-commit-message-body.md \
  --also-exclude docs/reviews/2026-11-14-0258-commit-message-plane-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions MH1–MH6 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (`55f23034`,
`6b6110c9`, `49f3d407`: read body-free yes/no, findings by id), findings with stable IDs (prefix
`MP`: `MP1`, `MP2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** The plane is self-authored guard code that every child inherits and
that will carry two checks into blocking on dated flips, so it is doctrine by function (rule 3):
**the author applies nothing on its own**. Record all findings; they are the principal's to decide,
after a plain-language account. Counsel per finding is welcome, labelled as counsel and kept
beneath it, and a finding that bears on whether the 2027-05-03 or 2027-05-31 flip should happen on
this plane as built says so in its first line.

---

## Verdict (act 1), 2026-11-22 UTC

**FAIL — 1 MAJOR, 2 MODERATE, 4 minor, 1 note (MP1–MP8).** Written before the sibling
`2026-11-14-0258-commit-message-plane-cold.deferred.md` was opened; act 2 (reconcile) is owed.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. A fresh session started for this pass alone.
- **Spawned by:** a headless per-pass orchestrator, session `21422696` (Opus 5.5), itself started
  by drain session `eca14b23` (Opus 5.5), under the principal's drain order of 2026-11-23 NZDT
  (verbatim: *"Start a fable drain or whatever it is called now. Target 100% of weekly budget by
  11.30am NZT todat"*). Both orchestrators are off-tier and disclosed: they hold the context
  partition, formed no finding and wrote no severity. Session `eca14b23` wrote no brief and no
  delta and started no brief-writer. Neither orchestrator is, or was started by, `3e2239de`,
  `58027096` or `d0ca5d24`.
- **Day run:** 2026-11-22 UTC (`date -u`, 21:09Z–22:00Z). **Worktree:**
  `/Users/mike/worktrees/fable/atelier-160-1390-2107/atelier`, HEAD `ccae1163`, read-only to me
  except this file. Interpreter: `python3` on PATH, 3.14.6, as the brief's re-run list used; git
  2.50.1 (Apple Git-155).
- **What I read:** this brief; `docs/method/REVIEW.md`; the delta body-free through
  `tools/coldsweep.py --commit` (`55f23034`, `6b6110c9`, `49f3d407` whole; the `floor.py` hunks of
  `b74cd5ef`, `ba55be27`, `ef4972e6`, `b462fd7d`, `cf648679` for their effect on the plane); at
  HEAD the two hook copies, `tools/commitmsg.py`, the named parts of `tools/floor.py`, `GUARDS.md`
  § *Which commits the hook plane reaches*, `tools/README.md`, `CHANGELOG.md`,
  `commands/install-hook.md`, `skills/create-repo/SKILL.md`, `skills/fleet-sweep/SKILL.md`,
  `tools/deadhook.py`, `tools/floorfleet.py`'s hook lines, the three test modules, and the
  `.githooks/pre-commit` and `pre-merge-commit` hooks for convention. Board files were read for
  the matching line only, through coldsweep. **Not read:** the sibling, any session log, prior
  verdict, the queue pointer, the two intent records, any commit body. No `git show`.
- **Barred-file disclosure:** none opened. The harness loaded user-level and repo instruction
  files and a memory index at start, which carry private context this verdict does not use.
- **The review log** (method, every command, every result) is at
  `~/.claude/fable-drain/notes/atelier-160-1390-2107.md`, appended to this file at the fold.

### Lens 1 — approach and assumptions

The plane's design is sound at its altitude: a `commit-msg` hook is the only client-side point
that can read a message before it lands (measured, MH1), the hook carries no policy, and the
`msg` template is absent by default (MH6 confirmed). Against the alternatives the brief names:
`prepare-commit-msg` runs before the author has written anything and cannot refuse; `pre-push`
over the outgoing range can refuse a push but the commit already exists and a rewrite is the
only cure; CI-only cannot refuse at all. `commit-msg` is the right place for a check that must
stop a title entering history, and report-only on CI is the right posture for a message that
cannot be retracted (MH5). What the work gets wrong is not the carrier but the **reader** and the
**child boundary**: the one reader cleans the message as git would only on an editor path, and
the config seam lets a child turn a message check into a run that reads nothing. MH1, MH4, MH5,
MH6 confirmed; MH2 damaged in one place; MH3 damaged in two.

- **MH1 — confirmed, GUARDS.md incomplete (MP6).** Measured on git 2.50.1 with a logging hook
  (log step 7, step 8 P1/P1b). `commit-msg` runs for `git commit` with `-m`, `-F`, `-c`, `-C`,
  `--amend`, `--fixup`, `--allow-empty`, from a subdirectory and in a linked worktree (git passes
  an absolute message path there, relative `.git/COMMIT_EDITMSG` in the main checkout; the hook
  handles both); for a clean `merge --no-ff` (file `.git/MERGE_MSG`), a `merge --squash` finished
  by `commit`, a conflicted merge finished by `commit`; and for a `rebase -i` reword. It does not
  run for `cherry-pick` (with or without `-e`), `revert`, a non-interactive `rebase`, or
  `--no-verify`. `GIT_INDEX_FILE` was `.git/index` in every case run. GUARDS.md's paragraph is
  true as far as it goes and does not say which paths the plane misses.
- **MH2 — damaged in one place (MP5); otherwise confirmed.** Every non-zero path measured prints
  a reason and a remedy: no message file (cannot happen from git; the hook's own line names it),
  `floor.py` unresolvable (remedy: `hooks.atelierTools` / `ATELIER_TOOLS`), a config error (the
  `ConfigError` text), a missing or unreadable message file (scanner exit 2, floor's exit-2 note
  "a marker or an ignore glob will not clear it"), odd paths and encodings (P2, P4, P7 all pass).
  The `python3`-missing path prints one line and then only the bypass: the remedy `pre-commit`
  grew for the same case (EP9) was not carried.
- **MH3 — damaged (MP2, MP3).** The blocklist is the wrong shape for this plane. A child reaches a
  guaranteed exit 0 with a message nobody read by two declarations that need no `why`:
  `flags: ["--help"]` (or `-h`, `--he`) and `scope: ["<a path that does not exist>"]`. A real
  commit landed under the first (P8). `disabled` and `advisory` are visible, declared states and
  behave as documented; `--terms=`, `--message-file`, `--range`, `--messages` and their
  abbreviations are refused at load (P8d, re-run list). An allowlist for the msg plane, whose
  checks accept five options between them, would close the class rather than the instance.
- **MH4 — confirmed.** The note fires in every clone-without-the-hook shape probed (hooksPath
  unset, relative, absolute; a dead copy under `.git/hooks`; a non-executable file; a linked
  worktree whose tree lacks the file) and stays quiet when an executable hook is where git will
  run it (P13), in text and in `--json`. Every site that describes the clone says the same thing
  except `skills/fleet-sweep/SKILL.md`, which says "silently" (MP7).
- **MH5 — confirmed.** On the CI plane both specimens keep their `ci` argv under an `advisory`
  declaration (P11b), render `👁️ warn-only`, and print "(no pushed range known: reading HEAD
  only)" when the base is unknown (P12). The floor's own line does not carry that note; the
  specimen's does, which is where a reader looks.
- **MH6 — confirmed, with a nuance.** No existing entry changed on `hook` or `ci` (`--list` on
  both planes, mutation (d)). The selftest catches an entry that declares both `hook` and `msg`;
  it does **not** catch a new `hook=None` entry that reads messages without joining `MSG_CHECKS`.
  `MsgPlaneTest.test_only_a_check_written_for_it_declares_msg` does (mutation (e)). The README's
  "a test notices" is accurate; the selftest alone is not the guard.

### Lens 2 — correctness and quality

The hook, `floor.py`'s msg path and the reader do what their text says on the paths the brief
names, with the exceptions below. The tests catch three of the brief's four mutations: a msg
check listed on the hook plane, a note that fires always, and a registry entry that grows a `msg`
template (log step 9). They do **not** catch the refusal in `main` being removed (MP4). The hook
is byte-identical to its sample, executable, names no scanner, and fails closed with nothing in
history when `floor.py` is unresolvable (re-run list; `CommitMsgHookTest`). Overclaims, each
against the text that makes it: `floor.py` line 1312, *"A child's `flags` tune a check, they do
not re-aim it"* — a child's `--help` re-aims it at nothing (MP2); `floor.py` docstring and the
hook header, *"only those run"* / *"hands each the message file"* — true of the plane, while the
reader hands the scanner a message with its `#` lines removed, which is not the message that
lands under `-m` (MP1); `GUARDS.md` line 672 names the commands that run the hook and not the
ones that do not (MP6).

### Lens 3 — completeness and harvest

Mirror sites swept by coldsweep (log step 5). The hook is installed by `create-repo`,
`commands/install-hook.md`, and the `fleet-sweep` survey step; `deadhook.py` counts it as a floor
hook and `--status` warns on its absence; the tracked copy and sample are tested identical, as
`pre-merge-commit`'s are. Gaps: `floorfleet`'s `shim:` column reads `.githooks/pre-commit` only,
so the fleet board cannot show a child that tracks `pre-commit` and not `commit-msg`;
`commands/install-hook.md`'s frontmatter and opening still describe one pre-commit hook; the
`fleet-sweep` text contradicts the note (MP7). Convention against `pre-merge-commit`: same header
shape, same tools resolution, same identical-sample test, same fail-closed text; the `python3`
remedy differs (MP5). Local child checkouts, read-only, by count: 29 repos; 22 track
`.githooks/commit-msg`; 22 have a `commit-msg` hook git would run; 1 tracks `pre-commit` without
`commit-msg`.

### Lens 4 — security and privacy

`ATELIER_TOOLS` and `hooks.atelierTools` steer what `python3` runs on every commit; both are
per-clone, set by whoever installs the hook, and git transports neither: the same trust class as
`pre-commit`, whose header carries the TRUST NOTE this hook's does not (folded into MP7 as a
mirror gap, not a new exposure). Arguments travel as argv lists in the hook (quoted) and in
`floor.py` (`subprocess.run(argv)`), never through a shell; `{msgfile}` is a substituted value,
not re-parsed (P4). The hook never passes a path with a leading `-` because git names the file.
`commitmsg` reads with `errors="replace"` (P7) and its regexes are per line, so a large message
costs linear time. `_event_base` accepts only a 40–64 hex sha that is not all zeros, and
`pushed_range` builds only `<sha>..HEAD`, `HEAD^..HEAD` or `HEAD`. `commit_files` passes a parsed
sha to `git diff-tree` with no `--` and no shape check; a forged record would need a NUL inside a
commit body, which git refuses, so this is hardening (MP8). A ref name cannot carry a control
character, so `branch()` cannot inject into a log. What reaches a public CI log is what the
specimens print over the pushed range, which is already public on push. ASVS items (5.1, 5.3.8,
7.1) are cited from memory: no network tool was used in this pass, so that part is **recalled,
not checked**, and is stated as a limit. `/security-review` was not aimed: this worktree's
pending diff is this brief, and the delta is landed, not pending.

### The standing checklist V1–V7

- **V1** — three claims stronger than their evidence: "do not re-aim" (MP2), the reader's view of
  the message versus the landed one (MP1), the refusal's test (MP4).
- **V2** — every line of the re-run list re-run; ledger below; all as the brief expected.
- **V3** — swept; gaps in MP7.
- **V4** — the hook text has two copies by design, tested identical; the "which commands run
  `commit-msg`" fact has one home (GUARDS.md) and the hook header points at it. Discharged.
- **V5** — `fleet-sweep` "silently" versus the note (MP7). Cross-references checked for the rule
  reached: GUARDS.md's paragraph reaches `floor.py --plane msg`, the README reaches
  `commit_msg_hook_note`, the hook header reaches the same function; each holds the rule it is
  cited for.
- **V6** — lens 4 above; ASVS recalled, disclosed.
- **V7** — stated above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `55f23034` | yes (coldsweep, 10 paths) | MP2, MP3 (inherited seams), MP4, MP5, MP6, MP7 |
| `6b6110c9` | yes (coldsweep, 2 paths) | MP1, MP8 |
| `49f3d407` | yes (coldsweep, 2 paths) | none; the three flags and abbreviations refused |
| `b74cd5ef` `ba55be27` `ef4972e6` `b462fd7d` `cf648679` | yes, `floor.py` hunks | none |

### Findings

**MP1 — MAJOR. A title or line that starts with the comment character is never read by either
plane, and lands.** Bears on the 2027-05-03 and 2027-05-31 flips: a blocking gate that a `#` at
the start of the title walks past is not yet a gate.
`tools/commitmsg.py` `clean()` drops every line starting with `core.commentChar` and `commits()`
does the same with `#`, mirroring git's `strip` cleanup. Git strips those lines only when the
message is edited; with `-m`, `-F` or `--cleanup=whitespace|verbatim` it keeps them. Probe P5:
a message `# a title starting with hash` committed with `-m` → the plane read subject `body`
(the next line) and the commit landed with that `#` title; a one-line message reads as an empty
subject. On CI `commits()` strips the same lines from history, so the pushed-range read misses
them too. Every agent session in this estate commits with `-m` or a heredoc, and a Markdown
heading in a body is ordinary. *Counsel:* strip only what git will strip: the scissors section
and the trailing template block (which begins with the comment character and a known first
line), or read the subject and body from the raw text and the cleaned text both and check the
union; add a test that commits `-m "# <term>"` and expects the check to see it.

**MP2 — MODERATE. A child's `flags` can turn a msg-plane check into `--help`, which exits 0 and
reads nothing.** Bears on the flips. `forbidden_flags` judges only names longer than two
characters that start with `--` and are a prefix of a listed flag; `-h`, `--help` and `--he`
pass (re-run list), and no `why` is needed on a softenable check. Probe P8: with
`flags.namescan.args=["--help"]` namescan printed its usage and exited 0; floor rendered
`🔴 namescan enforced (declares an advisory count and printed none — the count contract has
drifted, not the findings)`, a misdiagnosis, and exited 0; a real commit landed. The line is red
only because both specimens declare `advisory_count`; a msg check without it would render ✅.
The seam predates the plane and is open on every plane, which widens the finding rather than
excusing it. *Counsel:* on the msg plane, allow only flags the entry's own parser declares and
that are not `--help`; or at least judge `-h` and `--help`; and treat a scanner that exits 0
without its count line as a failure (rc 1) on this plane. Mutation (f) shows no test pins `-h` as
allowed, so the fix is free of the suite.

**MP3 — MODERATE. A child's `scope` on a msg-plane check with a path that does not exist skips
the check with exit 0.** Bears on the flips. The msg templates carry no `{scope}`, so a scope has
no meaning for these checks, yet `Config.validate` accepts one without a `why` (both are
softenable) and `run` reaches the "no tree in this repo" skip (line 2851). Probe P9:
`scope.namescan.paths=["nosuchdir"]` → `⏭ namescan skipped (no nosuchdir tree in this repo)`,
exit 0, message unread. The line is visible but its reason is false: this check reads no tree.
*Counsel:* refuse `scope.<name>` at load for any name in `MSG_CHECKS` (the same shape as the
flags refusal), and say why in the error.

**MP4 — minor. The refusal in `main` is not pinned by its test.** Mutation (a) removed the
`--message-file` refusal and `MsgPlaneTest` still passed: with no file, each scanner is handed
`--message-file ""` and refuses it ("give exactly one of --message-file and --range", exit 2),
so `main` returns 1 for a different reason. The behaviour at HEAD is right (re-run list, exit 1
with the refusal's text); the test cannot tell the refusal from the scanners' own. *Counsel:*
assert the refusal's text, or patch `run` and assert it was never called.

**MP5 — minor. The hook's `python3` guard prints one line and then the bypass.**
`.githooks/commit-msg` lines 60–63 versus `.githooks/pre-commit` lines 73–81: `pre-commit` grew
a remedy for this exact case (ADR 0008 cold pass, EP9: "the one machine that cannot scan is also
the one told how to skip scanning"); the new hook repeats the shape EP9 fixed. MH2's question,
answered no for this path. *Counsel:* carry the same remedy lines; the sample must match.

**MP6 — minor. GUARDS.md names the commands that run `commit-msg` and not the ones that do not.**
Line 671–675 says the hook runs for `git commit` and for a merge, and that `--no-verify` skips
it; measured true. It does not say that `cherry-pick`, `revert` and a non-interactive `rebase`
write commits whose message no plane read, or that a `rebase -i` reword does run it (log step 7).
The following paragraph says this of trees, not messages. *Counsel:* one sentence after line
675, or a `commit-msg` column in the table above it, so the measured table carries both planes.

**MP7 — minor (V3, V5). Mirror sites behind the delta.** (a) `tools/floorfleet.py` line 675:
`SHIM_PATH = ".githooks/pre-commit"`, so the fleet board's `shim:` column cannot show a child
that tracks `pre-commit` without `commit-msg`; the `fleet-sweep` survey does that step by hand
(SKILL.md lines 74–76), and the child probe found one such repo. (b) `commands/install-hook.md`
frontmatter `description` and opening paragraph describe one pre-commit hook while the command
installs three. (c) `skills/fleet-sweep/SKILL.md` line 75–76 says a repo without the hook
"skips commit-message checks silently", which contradicts README line 715 and the hook header:
the hook plane prints the note; it is silent only where the hook plane itself is off. (d) The
hook header carries no trust note for `ATELIER_TOOLS`/`hooks.atelierTools`; `pre-commit`'s does,
and this hook resolves the same two. *Counsel:* (a) a second shim path or a list; (b)–(d) text.

**MP8 — note. `commitmsg.commit_files` passes a parsed sha to `git diff-tree` with no `--` and
no `SHA_RX` check.** A forged record would need a NUL inside a commit body, which git refuses,
so it is not reachable today; it is one line of hardening at a seam that already owns `SHA_RX`.

### Re-run ledger

All from the worktree root, `python3` 3.14.6, `nice -n 10`, one at a time, load 3.9–6.9 (12
cores), 2026-11-22 21:15Z–21:22Z:

| Line | Result | Exit |
|---|---|---|
| `test_floor.MsgPlaneTest` | Ran 10 tests, OK | 0 |
| `test_precommit.CommitMsgHookTest` | Ran 7 tests, OK | 0 |
| `test_commitmsg` | Ran 12 tests, OK | 0 |
| `floor.py --selftest` | ok (21 scanners, 0 failure(s)) | 0 |
| `floor.py --plane msg --list --root .` | namescan enforced, quotescan enforced | 0 |
| `floor.py --plane msg --root .` | the refusal line | 1 |
| `floor.py --plane msg --root . --message-file <plain title>` | ✅ ✅, 2 run · 2 listed | 0 |
| `diff .githooks/commit-msg tools/commit-msg.sample` | IDENTICAL | 0 |
| `forbidden_flags(['-h','--help','--he','--mess','--ran'])` | `['--mess', '--ran']` | — |
| carried to a scratch repo (P8, P8d, P9) | `--help` passes; `--terms=` refused; scope skips | |

### Follow-up checklist

- [ ] MP1: reader mirrors git's cleanup decision, or reads raw and cleaned both; test `-m "# …"`.
- [ ] MP2: msg-plane flags judged by allowlist, or `-h`/`--help` refused; no count line → rc 1.
- [ ] MP3: `scope` refused for `MSG_CHECKS` at load.
- [ ] MP4: refusal test asserts the refusal, not a downstream exit.
- [ ] MP5: `python3` remedy carried into `commit-msg` and its sample.
- [ ] MP6: GUARDS.md says which paths the plane does not reach.
- [ ] MP7: floorfleet shim list; install-hook.md text; fleet-sweep "silently"; hook trust note.
- [ ] MP8: `--` and `SHA_RX` in `commit_files`.
- [ ] Rule 3: the principal rules each; the author applies nothing on its own. MP1–MP3 bear on
      whether the 2027-05-03 and 2027-05-31 flips happen on the plane as built.
- [ ] Act 2: open the sibling and the barred records; append `### Reconcile`.
