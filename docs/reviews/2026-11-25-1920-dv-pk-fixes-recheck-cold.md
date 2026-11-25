# Cold re-check — the `DV` and `PK` fixes to `ccfleet`, the reference queue, `modelguard`, `pointerscan` and the review and close skills (`160/1820`)

**Board:** `docs/roadmap/160-doctrine-review-owed/1820-rule-4-cold-pass-queued-dv-and-pk-fixes.md`
**Status:** BRIEF ONLY, 2026-11-25 UTC. Written by headless session `43d5be30` (`atelier-1d`,
Opus 5.5), pinned at `6a44b08e` (`origin/main` when written). Not yet run; queued for one Fable
reviewer under off-tier orchestrator `01c055e5`.
**Approval:** exactly one Fable re-check pass over the `210/620` fixes, plus its Opus brief, by a
fresh session that wrote none of them. The principal's pick, 2026-11-25 ~08:30 UTC, recorded on
`210/620` (an answer, not a ruling), verbatim: *"Before, plus re-check"*; the option text he
picked: *"Land all fixes and run their Fable re-check before Monday, then switch. Benefit: Monday
runs on the most robust code. Cost: another Fable pass this week, and a real risk it isn't done in <!-- datescan:allow: the principal's picked option text, quoted verbatim -->
time, so Monday falls back to /fable-drain."* It does not lift the general Fable hold: this pass
and nothing else.

**Pass type:** a rule-4 cold re-check per `docs/method/REVIEW.md`: code, design and doctrine.
The review skills, their prompt templates, the close skill, the hook that denies tool calls and
the scanner that polices review pointers are doctrine by function (rule 3); the instrument that
runs them is reviewed with them as one commitment. Two halves: the delta cold, on its own terms
(act 1); then each of `DV1`–`DV11` and `PK1`–`PK21` against its fix (act 2, *Process* below).
**Tier:** Fable, the principal-named review tier, checked at selection by whoever takes the pass.
A session that cannot run on it stops (rule 4).
**Deadline:** the pass must come back before the weekly drain starts, 2026-11-29 23:00 UTC. Never
thin the pass to meet it: a pass not done in time means the drain runs on its old path, which the
principal's pick already provides for (`REVIEW.md`, *Budget decides how many reviews run and when,
never how a review is run*).
**Size of this pass:** large. 23 commits, about 1,870 lines added and 240 removed on the delta
paths. At the pin: `instruments/ccfleet` 3,099 lines of standard-library Python, its tests 2,601
lines, a 2,199-line manual page, the reference queue 245 lines, `tools/modelguard.py` 888 lines
with a 419-line test, `tools/pointerscan.py` 992 lines, seven skill files and three guard tests.
Budget the time.

**What the verdict decides.** These fixes answer the two cold passes that reviewed the drain path
and the part-3 fixes to `ccfleet`, `modelguard` and the subject skills. On the principal's pick
above, the weekly drain moves onto `/atelier:review plan` and `/atelier:review run`, driven by
`ccfleet`, only if this re-check comes back with **no MAJOR** before the drain starts. So the
verdict must state its MAJOR count on its first line, and say plainly whether these commands, as
the fixes leave them, are safe to run the principal's paid drain from.

**Why it earns a review.** `ccfleet` starts unattended headless Claude Code sessions with the
user's credentials, decides from their output whether a paid review's claim is released and its
worktree removed, hands each session a slice of the user-level instruction file chosen by the
repo's visibility, and now sweeps per-session settings copies it did not write in this process.
`modelguard` sits in front of every `Agent` and `Bash` call on every session where it is wired.
The review prompts are stamped into every pass a drain runs. The worst failures:

- **Paid review work lost, run twice, misread or mis-costed.** A pass whose verdict is read from
  the wrong line; a fold or resume let past the budget reset when no pass started, or refused
  when one did; two sessions in one worktree; a settings copy removed from under a live session;
  a log reopened by a later launch; a cost history that counts what it should not.
- **An unplanned paid pass.** A path to a review-tier launch that no seal stands in front of, or
  a queue that offers a review on a route the seal did not give it.
- **A private fact in a public session.** The imported part of the user-level file, or its path,
  reaching a public repo's session by what is appended, by what the session may read, or by the
  record a pass leaves in a public repo.
- **A false allow or a false deny from the hook.** A launch with no model that `modelguard` now
  passes, or an ordinary command it now refuses on every session.
- **A skill that stamps a wrong rule** into every adopter's sessions, or a guard that reds the
  floor on a good change or stays green on a bad one: the widest blast radius in the operating
  model (rule 4).

## Spawn provenance

- **Authors of the work under review:** session `b04df0da` (`atelier-f9`, Opus 5.5,
  principal-opened by `/atelier:work run`) and the three worker subagents it started (two Opus,
  one Sonnet), which wrote the 23 commits. Found from the board item's text and the commits'
  subjects and timing; no delta commit's message body was read.
- **Who reviewed the work these fixes answer:** the `DV` and `PK` passes, each a Fable reviewer
  under off-tier orchestrator `14c2530d`; their briefs were written by headless sessions
  `4da4abc0` and `075cdcd9`.
- **Who wrote this brief:** headless session `43d5be30` (`atelier-1d`, Opus 5.5), started for this
  brief alone by principal-opened session `01c055e5` (Opus 5.5). Neither authored, started or
  instructed any part of the delta. **Off-tier for review, disclosed: the brief-writer forms no
  finding and writes no severity**, ran no review, used no Fable model, and stops after writing.
  It will not start the pass.
- **Who orchestrates the pass:** session `01c055e5`, which wrote no part of the delta and no part
  of this brief, spawns one Fable reviewer. It is off-tier (Opus 5.5): it may hold the context
  partition, release the held-back sibling after act 1 is committed, and commit the records,
  only because it **forms no finding and writes no severity**, and only with that arrangement
  disclosed in the claim, the pointer and the verdict, its spawn prompt, barred-set choice and
  release message in the verdict's provenance (rule 4). Weigh that arrangement as part of V7.
- **Barred from running or orchestrating this pass:** `b04df0da` and its three workers (the
  authors); `43d5be30` (whoever writes a brief does not run it); and everything any of them
  started or instructed.
- **Contact, disclosed (rule 4).** The brief-writer's only instruction came from `01c055e5`: the
  item, the approval, the method files, the sync and claim steps, the prefix rule, where the
  held-back sibling goes, the final-output shape, and five notes for the writer to verify (the
  barred sessions; later commits on four delta paths; that the authors' notes on `210/620` name
  two places the fixes depart from the counsel and a test result; that the earlier `PK` pass
  could make no live launch; the prefix check). Each is settled below or in the sibling. No
  author session contacted the brief-writer.
- **Who reviews:** a fresh Fable session started for this pass alone, by a session that passes
  rule 4's criterion.
- ⚠️ **Brief-writer's exposure, disclosed** (author-account and verdict material met before
  writing): its launch prompt (above); item `160/1820` whole; item `210/620` whole (**it carries
  the authors' account of every fix**, the departures and their test results); claim and
  brief lines 26–39 of item `160/1800`, and a few "Brief written" lines of other `160` items, read
  as models of the claim form; the first 30 lines of the newest session file (another work run's
  record, which names `b04df0da` as live and says nothing of the fixes); `cclive`'s session titles;
  `skills/review/brief.md` and `REVIEW.md` whole; the `PK` pass's brief down to its first verdict
  divider, **plus that file's heading lines, which name each `PK` finding's title, and about 25
  lines of its live-launch ledger** printed by a search for how it handled live launches. It did
  not open the `DV` pass's file. The delta was read as subjects, stats and `git diff` over the
  scoped paths, never a commit body. Its harness also loaded user-level and repo instruction
  files and a per-project memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the held-back sibling.

## The acceptance test

Judge the work against what it claims (its docstrings, `--help`, manual, example config,
reference queue, skills, prompts, README entries, comments, tests and changelog) and against the
doctrine it must keep:

- **The principal's words.** The commission on `210/620`, his pick 2026-11-25 UTC (an answer, not
  a ruling), verbatim: *"Fix all as advised (Recommended)"*, option text *"A fresh build session
  fixes all of them the way each reviewer suggested, starting with the 7 medium ones. Benefit:
  closes the gaps that only bite when something else also goes wrong, like a killed pass or a bad
  setting. Cost: Opus build time. A small Fable re-check would then be owed, and would wait for
  your approval."* And on one finding whose counsel was only to put it to him, his pick
  2026-11-25 ~11:30 UTC (an answer, not a ruling; the option text was written by the authoring
  session), verbatim: *"Obey, but say so (Recommended)"*, option text *"Your typed words can skip
  a step; the close names which step was skipped and that you asked. Benefit: your word wins, as
  the rest of the house rules say. Risk: a dropped or mistyped word could skip the record check,
  but the close says so in plain sight, so you'd see it."* The delta's `skills/session/close.md`
  answers it. Whether the delta keeps to it, and to the rest of the house's rules on the
  principal's typed words, is yours to judge.
- **The rules the drain enforces on others.** `REVIEW.md` rule 1 (the split and the context
  partition), rule 2 (barred reading), rule 4 (spawn criterion, tier at selection, the off-tier
  orchestrator's two conditions), *The lifecycle* (method record); `CONCURRENCY.md` §
  *Orchestrated queue runs*; `ECONOMICS.md` (tier set by risk).
- **The public-repo rule.** `docs/PERSONAL-DATA.md` and the repo-craft purpose rule: a generic
  tool in a public repo carries no estate's names, and its example config and reference queue are
  fictional.
- **The two earlier verdicts**, in act 2 only: `docs/reviews/2026-11-25-0720-rk-drain-path-fixes-cold.md`
  (`DV1`–`DV11`) and
  `docs/reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md`
  (`PK1`–`PK21`), both barred until your act 1 is committed (rule 2). This brief neither quotes nor
  summarises them. The delta's own comments, tests and changelog cite `DV` and `PK` numbers;
  reading the delta is never barred, but do not open a verdict to learn what a number means.

## What the work is

The pointer names its delta as every commit on `main` after `932a0185` up to and including
`77fc8f42`, the commit that landed the pointer, on a path list. All 23 commits in that range touch
the list; none outside it does. In UTC order, 2026-11-25:

- **`pointerscan`, `modelguard` and the tools README:** `9d52835a` (11:21) pointerscan warns on a
  pointer whose delta is named by citation alone · `5d3265e2` (11:29) modelguard denies the
  launches PK13 found and says only what is true · `127f3fef` (11:30) README modelguard and
  pointerscan entries match the code.
- **The skills:** `b7a3a694` (11:23) close the review texts' cold-pass findings · `001d9b42`
  (11:23) typed close words may skip a step, and the close says so · `7a2ec7e9` (11:24) work run
  step 1 handles a plugin root reached through a link · `be31d53b` (11:25) fleet sweep says a
  settled end is not re-run, and how to force it · `1c3488ad` (11:26) pin the review prompts and
  run.md sentences the cold passes found loose · `db4984c1` (12:51) review run says how a fold
  passes the reset and that next takes the local route.
- **`ccfleet`, the MODERATEs:** `422b5b5c` (11:51) read RESULT only where the final-output shape
  puts it · `e6a27480` (11:53) keep a live session's settings copies and its worktree its own ·
  `acfd0d59` (11:56) let a fold pass the reset only for a pass that started · `4ae0f05e` (11:58)
  name the models a session ran on its END line · `7db38b4b` (11:59) have the reference queue's
  next keep to the sealed route · `a8d5e35b` (12:00) withhold the import lines from a public
  session and deny them · `afa9aec7` (12:30) test the session's two copies by suffix.
- **`ccfleet`, the minors and notes:** `3c824d40` (13:07) keep the finish word per call, out of
  the example's vars · `be934126` (13:09) rehearse a dry drain honestly and let the queue see a run
  end · `d07c0682` (13:10) have check name every kept key and the forge's visibility · `389b9424`
  (13:11) never reuse a log name, and read a later session's own end · `f58cc435` (13:12) name the
  settled re-run, the inliner's limits and two residuals · `36ec7901` (13:14) pin the five mutants
  the tests did not notice.
- **The landing:** `77fc8f42` (13:18) `CHANGELOG.md` entries, two README lines, and the board
  (`210/620`, the pointer, a line on `450/010`, the index). Its board hunks are barred until act 2.

Delta paths, read at your HEAD and commit by commit: `instruments/ccfleet`,
`instruments/test_ccfleet.py`, `instruments/man/ccfleet.1`, `instruments/ccfleet.example.json`,
`instruments/fixtures/review_queue_reference.py`, `instruments/README.md`, `tools/modelguard.py`,
`tools/test_modelguard.py`, `tools/pointerscan.py`, `tools/test_pointerscan.py`,
`tools/README.md`, `skills/fleet/sweep.md`, `skills/review/fold-prompt.md`,
`skills/review/orchestrator-prompt.md`, `skills/review/plan.md`, `skills/review/run.md`,
`skills/session/close.md`, `skills/work/run.md`, `tools/test_subject_skills.py`,
`tools/test_session_close_single_source.py`, `CHANGELOG.md` (the entry headed *the `DV` and `PK`
cold-pass fixes, `210/620`*).

First confirm your tree holds the whole delta, then read each commit body-free:

```
git merge-base --is-ancestor 77fc8f42 HEAD; echo "exit=$?"
python3 tools/coldsweep.py --root . --commit 422b5b5c --path instruments --path tools \
  --path skills --path CHANGELOG.md
```

Repeat the `--commit` line for each of the other 22 commits. A `--path` that matches nothing in a
commit prints a note and still exits 0. Plain `git show` is barred: it prints the message body
before the diff, and reading is atomic (rule 1). With no `--path`, `--commit` leaves the board
store out; always pass `--path` here. `git diff 932a0185 77fc8f42 -- <the paths above>` gives the
whole delta at once, body-free.

**Commits after the delta on its paths.** Three later commits, by other sessions, touch four of
the delta's paths. None is part of the fixes, and each has its own queued pass:

- `f239dc3b` `skills/review/brief.md` (board `320/910`, pass `160/1830`);
- `e8c7d631` `CHANGELOG.md`, `instruments/README.md` (board `210/580`, pass `160/1840`);
- `6e11c551` `CHANGELOG.md`, `tools/README.md` (board `320/900`, pass `160/1860`).

How to treat them: **judge each fix as it stands at your HEAD**, since that is what the drain
will run, and attribute every line to the commit that wrote it (`git blame` or `git log -L`). A
later hunk is in this pass's scope only where it changes, undoes or contradicts a line the delta
wrote; then it is a finding against the fix's surviving state, naming the later commit. A defect
you meet in a later hunk that touches no delta line is one line in your verdict naming the owning
pass, never a `DP` finding. `skills/review/brief.md` is not a delta file at all (the delta's
`skills/` changes are the seven files above). Then check what else has landed since the pin:

```
git log --oneline 6a44b08e..HEAD -- instruments/ccfleet instruments/test_ccfleet.py \
  instruments/man/ccfleet.1 instruments/ccfleet.example.json instruments/fixtures \
  instruments/README.md tools/modelguard.py tools/test_modelguard.py tools/pointerscan.py \
  tools/test_pointerscan.py tools/README.md skills tools/test_subject_skills.py \
  tools/test_session_close_single_source.py CHANGELOG.md
```

It was empty at `6a44b08e`. A commit that touches only another tool's entry in `CHANGELOG.md` or
the READMEs falls under the rule above. Any other commit on these paths means the delta moved:
stop and hand back for the brief to be updated. Otherwise pin your HEAD in your verdict's scope.

**Machine-local surfaces no other review will catch** (read-only; report them in public-safe
terms, never a home path or a private name):

- The user-level settings wire `modelguard` as a `PreToolUse` hook on `Agent|Task|Bash`, run as
  `/usr/bin/python3 -I <the primary checkout>/tools/modelguard.py`. That interpreter is Python
  3.9.6; the `python3` on `PATH` is 3.14.6. The primary checkout was on `main` at `6a44b08e` with a
  clean tree when this brief was written, so **the hook in front of your own Bash calls already
  runs the delta's `modelguard`**. Feed `modelguard` its probes from files (`python3
  tools/modelguard.py < probe.json`), never as an inline command that names the binary, or the
  live hook judges your probe before the copy under review does.
- `ccfleet` on `PATH` is a link to the primary checkout's `instruments/ccfleet`; never run it by
  bare name. The plugin is installed in place from the primary checkout, so the skills a session
  loads are the primary checkout's.
- The installed Claude Code CLI reports version 2.1.302, the version `modelguard`'s long-flag
  table names. It is a native executable, not a script package: there is no JavaScript source on
  disk to read, only the binary (`strings` reads it, read-only) and `--help`.
- Sessions on this machine, including a session `ccfleet` launches, are also handed the
  harness's per-project memory index, which `ccfleet` neither writes nor filters.
- Free disk was about 26 GB when this brief was written, above the gate's default floor (20 GB);
  the load average ran between 13 and 20 on 12 cores, so `gate` may answer "hold" for reasons
  unrelated to the code.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the authors' claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1); these are a floor, never a fence.

**`ccfleet`: reading a verdict (`422b5b5c`, docstring and `shaped_results`, `result_word`)**

1. "The verdict is the RESULT line that stands in that shape: directly above the ITEM: or REPO:
   line (the review prompts), or the last line of a block that holds one (the fleet prompts); any
   other RESULT line is no verdict."
2. "Two shaped verdicts that disagree are none. A word in `stops` on any RESULT line is kept when
   no shaped verdict stands, since stopping is the safe direction."

**`ccfleet`: the worktree, the settings copies and the reset (`e6a27480`, `acfd0d59`,
`afa9aec7`)**

3. "A SIGTERM or SIGHUP to a launcher leaves its session running … with its worktree and its
   settings copies; a resume, and any launch into that worktree (a fold), is refused while it
   runs (RK4, PK2), and its copies stay until it ends (PK1)."
4. The copies are named `<session>.<launcher pid>.json` (and `-user-instructions.md`), "so a
   sweep never takes the copies of a launch that has not yet recorded its session"; the next
   launch sweeps a copy only when its launcher is gone and no live session record lists it.
5. "A fold passes the reset only for a pass ccfleet saw start (its result file, or a `START` line
   for `<repo>-<item>`); its template is never `pass_prompt`"; a fold whose template is
   `pass_prompt` exits 64.

**`ccfleet`: what a session is handed (`a8d5e35b`, `d07c0682`)**

6. "A public repo's session gets the shared part of the user-level file with its import lines
   withheld, no path named, and each imported file denied for reading", by a `Read(//<path>)`
   deny rule for the path and its real path; "a private name kept in an imported file reaches no
   public session by what ccfleet appends, and the session is not told where that file is".
7. `check` names `WIDENS: sandbox`, a `MANAGED:` line, `KEPT, not classified` for any kept
   user-level key outside a stated list, and with `gh` a `VISIBILITY MISMATCH` line where the
   config's visibility and the forge's disagree.

**`ccfleet`: the queue, the seal and the record (`7db38b4b`, `be934126`, `3c824d40`,
`389b9424`, `4ae0f05e`)**

8. "Your queue's `next` must offer only what the sealed ranking routes to the local route, plus
   the stated spill: ccfleet now calls it with `--route local`" (the changelog); the reference
   queue's `next` takes `--route` (default `local`) and spills only from a budget that does not
   lapse before the asking route's, never one sealed `"spillable": false`.
9. "A dry drain before the seal exits 0, saying no launches were rehearsed"; a sealed one names
   its rehearsed pick.
10. A real drain that passed `ranked` calls the optional `queue.unseal` "once when [it] ends";
    the reference queue refuses `unknown` as a sealing id.
11. `FINISH_WORDS` is passed per call and never kept in `vars`; "ccfleet does not check it", and
    a launch with it unfilled is refused.
12. "Log names carry the date and seconds, with a `.end` file beside each, and the cost history
    reads a later session's own `END` line"; "A pass run by hand leaves no .out and is not
    counted, nor is one whose launcher a signal stopped (no END line)."
13. "`END` lines carry `models=` from the session's log", so a pass's record shows the model its
    reviewer ran on beside the `REVIEW_MODEL` it was told.

**`modelguard` (`5d3265e2`, `127f3fef`)**

14. It now denies "`screen`, `tmux`, `systemd-run`, process substitution, `echo` piped into a
    shell through any stage, `awk` `system()`, nesting past depth four, six long flags the table
    lacked"; "its refusal text says only what is true; printed literals and notification commands
    no longer read as launches."
15. Its docstring lists the passes it accepts and the false positives it accepts, and says "Each
    bypass found is added to the deny table in tools/test_modelguard.py".

**`pointerscan` (`9d52835a`)**

16. It warns, under `grammar`, on a pointer that names its delta's commits by citation alone
    ("the commits citing `X`") with neither a commit range nor two or more distinct hashes
    written out; one start hash is not a bound; advisory only.

**The skills and prompts (`b7a3a694`, `001d9b42`, `7a2ec7e9`, `be31d53b`, `db4984c1`)**

17. The orchestrator prompt stops with `RESULT: FAILED` if the Agent tool refuses the review
    model, never spawns a reviewer without it or as a fork, and stops if the reviewer reports it is
    not on the review tier; the reviewer states the model it runs as; the reviewer's instructions
    have one home (the end of `orchestrator-prompt.md`); in a public repo the quoted spawn prompt
    replaces each absolute path with a named placeholder.
18. `run.md`: what the seal does not gate (`run` with the pass prompt, and `resume`); whose id
    `--by` carries; a fold runs on the config's model for the repo, so it costs no review budget
    only where that is not the review tier; words the principal did not type are never taken from
    the skill call's own arguments.
19. `close.md`: "Where the typed words ask to skip a step, skip it, and name in your reply each
    step you skipped and that the typed words asked for it."
20. `fold-prompt.md`: the run-twice check searches for the step 2 heading without its date.
21. `skills/work/run.md`: a plugin root reached through a symbolic link still counts as the checkout's
    top; a pending edit to the session-open prompt may be another session's and is left alone.
22. `sweep.md`: the next `drive` never re-runs a settled job; delete its result file or run under
    another `--day` to force one.

**The guards' tests (`1c3488ad`, `36ec7901`, and the tests in each commit)**

23. The new tests pin the review prompts, the sentences the passes found loose, and "the mutants
    that survived", so a revert of any fix turns a test red.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and
live behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in
scope, and a non-goal that fences off the risk is a finding.

**Non-goals:**

- Any estate's private `ccfleet` config, rulings file, queue tool, lane records and run results,
  the real user-level instruction file's content, and the real config directory. Grounds: private
  by design, this repo is public, and the delta's claim is that the code, the reference queue and
  the skills are generic. Judge the contract through the example config, the reference queue and
  a synthetic world (below).
- The three later commits' own content (above), except where they touch a delta line.
- Code the delta did not change, except as far as a fix builds on it or changes what it does. A
  defect you meet in an older line is recorded, not hunted.
- The wording of the session-open prompt, *Ending the session* included: it is the principal's own
  text. Whether `close.md` runs it faithfully is in scope where the delta changed `close.md`.
- The user-level drain command the estate still runs, outside this repo.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   For each MODERATE the fixes answer, is the fix aimed at the class or at the instance the pass
   reproduced? Is a verdict read from the shape of the last turn's text a sound basis for
   releasing a paid claim? Is keying the reset exemption on files `ccfleet` writes under
   `kit_dir` a control or a convention? Is withholding import lines plus a `Read` deny rule the
   right fix for keeping private context out of public sessions, given every other channel a
   session has? Is a deny-list hook that keeps widening converging on a sound net? And the
   re-check's own question: does each fix close its class, or move the risk somewhere the fix did
   not look?
2. **Correctness & quality.** Re-drive the claims above by probe, not by reading. Trace each
   interruption point of a pass's life (before the claim, after the claim and before `START`,
   mid-session by `SIGTERM`, `SIGHUP`, `SIGKILL`, a usage cap, a reboot, after the session and
   before the release, during a fold or a resume run twice) through the new worktree refusal, the
   copies' sweep and the reset exemption. Drive the verdict reader with final outputs of both
   prompt shapes, mentions before and after, quoted text from a reviewed repo, disagreeing
   verdicts and stop words. Drive the seal and the route filter through the reference queue. Drive
   the cost history with the new and old log names, `.end` files present and absent, a dry run's
   files. Drive `modelguard` with the shapes its docstring names and those it does not. Record
   each overclaim against the text that makes it, including any claim no test pins.
3. **Completeness / harvest.** Every surface that states the verdict rule, the reset exemption,
   the worktree refusal, the copies' lifetime, the queue contract, the seal, the route rule,
   `FINISH_WORDS`, the exit codes and the import withholding agrees: docstring, `--help`, manual,
   example config, reference queue, skills, prompts, both READMEs, changelog (V3, V5). One home per
   fact (V4): the seal and the route rule now appear in the manual, `run.md` and the reference
   queue. Find tests that would stay green on a broken delta by mutating scratch copies. What the
   fixes should have touched and did not, given what they claim to fix.
4. **Security & privacy**, mandatory. Design altitude: what an unattended public-repo session can
   still receive or reach of the user-level files after the fix (the appended text, the imported
   files, their paths, the settings copies on disk and their lifetime and permissions, any other
   channel the harness itself opens); what the sweep may delete; what a hostile repo's settings,
   instruction file, pull request or reviewed text can make a session or the verdict reader do.
   Code altitude: the likely vectors for the class, checked against an open catalogue (OWASP ASVS
   or the domain's equivalent), not recalled: values from the config, the queue's output, the
   instruction file's import lines and the forge flowing into paths, argv, permission rules,
   prompts and git commands; for `modelguard`, every way a launch with no model can pass, and
   every ordinary command it now refuses. `/security-review` reads the session's pending diff, not
   this delta: aim it at the code only from a scratch clone holding the diff, never with this brief
   dirty, else discharge it by grounds; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once, on 2026-11-25 UTC, at `2068884e`
(which differs from the pin only by one board item), from the places named; its results are held
in the sibling. Read exit codes explicitly. Check `uptime` first; one heavy process at a time,
under `nice -n 15`, in the foreground with a long timeout (the `ccfleet` suite takes several
minutes per interpreter on a loaded machine). Other sessions share this machine.

From the worktree root:

```
git merge-base --is-ancestor 77fc8f42 HEAD; echo "exit=$?"
mandoc -T lint -W style instruments/man/ccfleet.1; echo "exit=$?"
python3 instruments/ccfleet --help >/dev/null; echo "exit=$?"
python3 instruments/fixtures/review_queue_reference.py --help >/dev/null; echo "exit=$?"
python3 tools/modelguard.py </dev/null; echo "exit=$?"
python3 tools/pointerscan.py --selftest; echo "exit=$?"
python3 tools/pointerscan.py --root . .; echo "exit=$?"
python3 tools/coldsweep.py --selftest; echo "exit=$?"
```

From `instruments/` (the tests load their subjects by path; run on both interpreters, since the
runtime claim is 3.8 or later and the manual says 3.9 and 3.14 are tested):

```
nice -n 15 python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_ccfleet; echo "exit=$?"
```

From `tools/` (`/usr/bin/python3` is the interpreter the user-level hook runs under):

```
nice -n 15 python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_pointerscan; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_pointerscan; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_subject_skills; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_subject_skills; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_session_close_single_source; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_session_close_single_source; echo "exit=$?"
```

The whole `tools` suite, once, only while the 15-minute load average is under the core count
(from `tools/`): `nice -n 15 python3 -m unittest discover -q; echo "exit=$?"`. A failure you
judge to be load, not code, is re-run alone and both results recorded. The brief-writer started this
line at 19:34 UTC; it was still running when the brief landed, so its result is added to the
sibling when it ends, not here.

**The pushed floor.** The CI run on the landing commit itself was cancelled by a newer push
(cancel-in-progress), so it proves nothing; read the first green run whose tree holds the delta
(read-only):

```
gh run list -R mike548141/atelier --commit 77fc8f42f32fbfcb398f25dd9ecc7a89faaea28e \
  --json name,status,conclusion
gh run list -R mike548141/atelier --commit a033f023ca9ba60f9ffc451295b53e450daad357 \
  --json name,status,conclusion
git merge-base --is-ancestor 77fc8f42 a033f023; echo "exit=$?"
```

**A synthetic world**, in your scratchpad only, every name invented. Two throwaway git repos with
no remote and mainline `main` under a scratch `repos_root`, each holding a dummy brief; a scratch
`CLAUDE_CONFIG_DIR` holding `settings.json` of `{}` and a `CLAUDE.md` that imports a second file
by `@` path on a line of its own, only the second file naming one invented private name; a config
whose `kit_dir`, `repos_root` and `worktrees_root` are scratch directories, `stagger_seconds` 0,
`gate` open, one repo `public` and one `private`, that private name in `private_names`,
`instructions_guard` `refuse`, a scratch `pass_prompt` using `{ITEM}` `{BRIEF}` `{REVIEW_LOG}`,
and a `queue` whose commands call `instruments/fixtures/review_queue_reference.py` from your
worktree in the example config's shape, `unseal` included; a state file with one open `local`
route and one briefed review; `REVIEW_QUEUE_STATE` and `REVIEW_QUEUE_NOW` set. For `claude_bin`,
a **stand-in script** you write: it records its argv, copies each file passed after `--settings`
and `--append-system-prompt-file` into a capture folder, and prints a canned JSON log (`type`
`result`, `subtype` `success`, the `--session-id` it was given, a `result` text in the final-output
shape, a `modelUsage` object). It never runs a model. Name it so its path does not contain the
real binary's name, or the live hook will read your commands as launches. Then, with
`CLAUDE_CONFIG_DIR` pointing at the scratch directory throughout, from the worktree root:

```
python3 instruments/ccfleet --config <cfg> check; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> plan; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-A drain --dry-run; echo "exit=$?"
python3 instruments/fixtures/review_queue_reference.py seal --by run-A --ranking <file> --words synthetic; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-A drain --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-B drain --dry-run; echo "exit=$?"
python3 instruments/fixtures/review_queue_reference.py seal --by unknown --ranking <file>; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <public repo> --prompt <plain template> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <public repo> --prompt <plain template>; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <private repo> --prompt <plain template>; echo "exit=$?"
```

The ranking file is one JSON array entry naming the briefed review, route `local` and a reason.
The plain template asks for nothing and ends with the fleet prompts' final-output shape. Then
read `<kit_dir>` (`driver.log`, `logs/` with its `.end` files, `results/`, `settings/`, any
`sessions/` record) and the capture folder: what each session was handed, what was left on disk
and what was removed. Build the rest of your probes (a stand-in that sleeps, then a signal to the
launcher; a fold after the reset; a mutated copy) on the same world. How the brief-writer built
its world, and what it saw, is in the sibling.

**Live behaviour.** The claims that rest on real `claude -p` behaviour (whether the harness
follows an `@` import inside a file given to `--append-system-prompt-file`; how it matches a
`Read(//<path>)` deny rule, by path or real path, and whether anything else reads the file; the
JSON log's `modelUsage` when a subagent runs on another model; how a session behaves when its
launcher is signalled) rest on a stand-in binary in the tests. **This pass makes no launch of the
real CLI that reaches a model, decided here, before the pass.** Grounds: a synthetic
`CLAUDE_CONFIG_DIR` has no sign-in, so a launch there fails before any model is reached (the
earlier `PK` pass met exactly this); a launch from the real config directory would load the
operator's private instruction file and credentials into an experimental session and spend budget
beyond the one approval this pass runs under (exactly one Fable pass and its Opus brief). So each
such claim is re-driven read-only instead, and its live half marked NOT RUN with these grounds:

- `claude --version` and `claude --help` (no model is reached, and no sign-in is needed): confirm
  every flag `ccfleet` passes and every long flag `modelguard` added exists in 2.1.302, and none
  is missing from the table;
- the installed binary read read-only with `strings` for the handling of an appended file's `@`
  lines and of permission-rule paths, stated as reading the binary, not as a live result;
- the harness's published documentation for permission-rule path syntax and memory imports;
- the stand-in binary above for what `ccfleet` hands a session, which is what `ccfleet` controls.

Never run `ccfleet` against a real repo, never `drive` or `drain` for real, never with a real
config, and never `ccfleet check` against the real config directory (it prints the operator's
hooks and instruction-file path). The brief-writer ran no launch of the real CLI.

## House rules for this run

- **Live systems:** read-only reads as needed; no live writes. A check that needs a write is
  marked NOT RUN, with why. No push, no write to GitHub, no network service changed. `gh repo
  view` and `gh run list` are reads.
- **Never print a secret** or any personal data. Other sessions' transcripts are not read.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file and
  your review log. Other sessions may be live on this machine: touch nothing outside your
  worktree and scratchpad, and never touch the primary checkout (the hook, the linked `ccfleet`
  and the in-place plugin run from it). Child repos are read-only and reported by count only,
  never by name or path.
- Never run an installed tool by bare name from `PATH`: use `instruments/ccfleet` or `python3
  tools/<x>.py` from your worktree.
- This pass is pending while you run it: anything you write to a pointer or a commit subject
  before act 2 names the held-back sibling by count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at about 100 columns; NZ English. This
  repo is PUBLIC: quote no secret, email address, home path, private repo name or estate fact.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

**Reviewer's start-up reading:** skip the session-log step of the repo's read order, whatever your
spawn prompt says; the log is on rule 2's barred list. If you met any of it anyway, disclose what.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material is held outside the repo under the rule-1 split and released only after the reviewer's act-1 findings are committed -->

Rule 2 bars until act 2: `docs/sessions/`, every prior verdict in `docs/reviews/` (the two above
included), every item under `docs/roadmap/160-doctrine-review-owed/` beyond its title, the delta
commits' message bodies, `docs/method/census/`, and beyond their first line:

- `docs/roadmap/210-instruments-open-features/620-fix-ccfleet-and-the-review-skills-dv1-dv11-pk1-pk21.md`
  (the intent record; it carries the authors' account of each fix; the principal's words it holds
  that bear on this pass are quoted above)
- `docs/roadmap/210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md`
- `docs/roadmap/210-instruments-open-features/610-ccfleet-follows-the-private-import-for-private-repos-only.md`
- `docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md`
- `docs/roadmap/210-instruments-open-features/470-fix-ccfleet-and-its-two-skills-fl1-fl25.md`
- `docs/roadmap/210-instruments-open-features/500-modelguard-reads-a-lookup-of-claude-as-a-launch.md`
- `docs/roadmap/210-instruments-open-features/560-ccfleet-cannot-see-inherited-permissions-and-a-kept-worktree-loses-its-claim.md`
- `docs/roadmap/210-instruments-open-features/570-modelguard-refuses-ssh-as-the-claude-user.md`
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md`
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/020-every-command-is-subject-then-action.md`
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/030-a-close-command-so-the-close-text-is-not-pasted.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/210-a-plan-mode-that-shows-the-drain-before-it-runs.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/240-a-work-plan-mode-for-work-run.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/500-census-slice-4-doctrine-defects.md`

All of these carry an author's account of the work or of its predecessors, and some carry earlier
verdicts' findings. The board index, `docs/ROADMAP.md`, lists items by title; read no further in
it than a title.

**This brief's held-back sibling is not in the tree.** Whoever orchestrates the pass holds it
outside the repo and every worktree, and releases it to you only after your act 1 is committed; by
count it holds 20 questions and 14 facts. Never look for it in git history, other checkouts,
scratchpads or temporary directories. Run by hand with no orchestrator, you open it yourself, as a
deliberate second act, after act 1 is committed, and disclose when.

The delta's own comments, docstrings, manual, skills, prompts, tests and `CHANGELOG.md` entries
carry the authors' account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/620-fix-ccfleet-and-the-review-skills-dv1-dv11-pk1-pk21.md \
  --also-exclude docs/roadmap/210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md \
  --also-exclude docs/roadmap/210-instruments-open-features/610-ccfleet-follows-the-private-import-for-private-repos-only.md \
  --also-exclude docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md \
  --also-exclude docs/roadmap/210-instruments-open-features/470-fix-ccfleet-and-its-two-skills-fl1-fl25.md \
  --also-exclude docs/roadmap/210-instruments-open-features/500-modelguard-reads-a-lookup-of-claude-as-a-launch.md \
  --also-exclude docs/roadmap/210-instruments-open-features/560-ccfleet-cannot-see-inherited-permissions-and-a-kept-worktree-loses-its-claim.md \
  --also-exclude docs/roadmap/210-instruments-open-features/570-modelguard-refuses-ssh-as-the-claude-user.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/020-every-command-is-subject-then-action.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/030-a-close-command-so-the-close-text-is-not-pasted.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/210-a-plan-mode-that-shows-the-drain-before-it-runs.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/240-a-work-plan-mode-for-work-run.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/500-census-slice-4-doctrine-defects.md \
  --also-exclude docs/method/census \
  --also-exclude docs/ROADMAP.md \
  "withhold_imports|pass_started|refuse_live_worktree|shaped_results|--route"
```

`--include-barred` only with disclosure in the verdict.

## Process

**Act 1.** Reproduce the floor first; work the lenses, your own assumptions and the re-run list,
over the whole delta as it stands at your HEAD, cold: you have not read the earlier verdicts, so
judge the code and skills on their own terms, not as fixes. Append your verdict below a `---`
divider in THIS file: provenance repeated (how you were spawned, your tier and the model you find
yourself running as, the orchestrator with its spawn prompt, what you read, the UTC day, the HEAD
you pinned), per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing
assumption damaged or confirmed with its probe, a per-commit ledger (read body-free yes/no,
findings by id), findings with stable IDs (prefix `DP`: `DP1`, `DP2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts and the
MAJOR count first, a re-run ledger, a live-behaviour ledger (each NOT RUN with its grounds), the
method record `REVIEW.md` § *The lifecycle* requires, and a follow-up checklist. Give the paid-drain
path its own line in the per-lens answers. Then STOP: act 1 is committed, unrevised, **before** the
sibling or either earlier verdict is opened. Edit no other file.

**Act 2.** Open the sibling, the two earlier verdicts and the barred records; screen the delta
commits' bodies. Append `### Reconcile` beneath your verdict, with:

- **The fix ledger, one row for each of `DV1`–`DV11` and `PK1`–`PK21`:** what the earlier
  verdict counselled (by pointer, not restated at length), the commit and file:line that answers
  it, how you re-drove it at your HEAD (the command and its result, or that verdict's own
  reproduction re-run), and its state: *fixed as counselled* · *fixed another way* (and whether
  that way meets the finding) · *partly fixed* · *not fixed* · *regressed*. Reading a fix is not
  re-driving it (V2). Where a fix went beyond or against the counsel, or where the principal's
  recorded answer shaped it, say so and judge it. A finding whose counsel was to put it to the
  principal is judged against his recorded answer.
- Per-finding notes on your act-1 findings against the sibling's questions and the authors'
  account; any finding formed at reconcile, marked as such, with a `DP` id after your last.
- The residual risk, named: act 2 reads the earlier verdicts, so the fix ledger is anchored on
  them by design; act 1 is the cold half.
- The overall line restated, MAJOR count first.

Never revise act-1 text. Then the orchestrator folds the sibling in below the reconcile.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per
finding is welcome, labelled as counsel and kept beneath it. Under the overall verdict, say
plainly in three lines: whether anything you found loses, misreads or mis-costs paid review work;
whether `/atelier:review plan` and `/atelier:review run`, with `ccfleet` as the fixes leave it, are
safe to run the principal's paid weekly drain from, and if not, what must change first; and
whether anything in the delta can put private context into a public repo's session. Name
`160/1820` in your scope line, and `210/620` as the item the delta answers to.
