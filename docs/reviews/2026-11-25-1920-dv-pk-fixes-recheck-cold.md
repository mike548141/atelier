# Cold re-check — the `DV` and `PK` fixes to `ccfleet`, the reference queue, `modelguard`, `pointerscan` and the review and close skills (`160/1820`)

**Board:** `docs/roadmap/160-doctrine-review-owed/1820-rule-4-cold-pass-queued-dv-and-pk-fixes.md`
**Status:** VERDICT 2026-11-25 UTC: PASS-WITH-FINDINGS, 0 MAJOR, 5 MODERATE, 11 minor, 5 notes
(`DP1` to `DP21`; one Fable reviewer under off-tier orchestrator `01c055e5`; act 1 committed as
`785fa79e`, reconcile and folded sibling below it). Every finding is the principal's to rule.
Was: BRIEF ONLY, 2026-11-25 UTC. Written by headless session `43d5be30` (`atelier-1d`,
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

---

## Verdict, act 1 (cold): the `DV` and `PK` fixes, `160/1820`

**MAJOR: 0.** PASS-WITH-FINDINGS: 0 MAJOR · 5 MODERATE · 11 minor · 4 notes (`DP1`–`DP20`).
Written 2026-11-25 UTC, before the held-back sibling, either earlier verdict or any barred record
was opened. Act 2 (the fix ledger for `DV1`–`DV11` and `PK1`–`PK21`) is not in this text.

**Scope.** Board `160/1820`; the delta answers to `210/620`. Every commit on `main` after
`932a0185` up to and including `77fc8f42` (23 commits) on the brief's path list, judged as it
stands at my HEAD, pinned at `9e6712b4`. `git merge-base --is-ancestor 77fc8f42 HEAD` exits 0. The
brief's later-commit check (`git log --oneline 6a44b08e..HEAD -- <the delta paths>`) printed
nothing, so the delta has not moved since the brief's pin; the two commits after `6a44b08e` touch
this brief and the `160/1820` item only.

### Provenance (rule 4, V7)

- **How I was spawned.** As a subagent of session `01c055e5` (`atelier-4c`, Opus 5.5), which
  describes itself as an off-tier orchestrator opened by the principal for this one pass. I was
  started for this pass alone, with the prompt below and nothing else. No author session and no
  brief-writer contacted me. Contact after the spawn: none before this text was written.
- **My tier and the model I find myself running as.** The harness tells me I am powered by the
  model named Fable 5.2, model id `claude-fable-5-2`. That is the review tier the brief names. I
  started no subagent; every reading, probe, finding and severity here is mine.
- **The orchestrator's arrangement, weighed (V7).** Its spawn prompt is process only: paths, the
  no-git-writes rule, load, the stand-in world, the two acts, the reply shape. It asks no question
  about the delta, points at no risk and asks for no finding. It discloses its own exposure
  (the intent record `210/620` whole, counts and one-line counsel of the earlier verdicts,
  fragments of three earlier findings) and says it passes none of it on; nothing in the prompt
  carries any of it. The barred set it chose is exactly the brief's. I see no breach of rule 4's
  two conditions. One limit, stated: a reader can check the prompt, not what the orchestrator
  knows; its exposure is wider than a cold orchestrator's would be, and it is disclosed.
- **The spawn prompt, verbatim** (it reached me as a file plus a one-paragraph wrapper; absolute
  paths are written as the named placeholders `<WT>`, `<SCRATCH>` and `<PRIMARY>`, as the prompt
  itself asks for a public repo; nothing else is changed).

  The wrapper message:

  > Your full instructions are in this file; read it first and follow it exactly. It is also the
  > text you record verbatim in your verdict's provenance, with the absolute paths written as
  > `<WT>`, `<SCRATCH>` and `<PRIMARY>`, as it explains: `<SCRATCH>/dp-spawn-prompt.md` . The
  > placeholders in that file stand for: `<WT>` = `<WT>` · `<SCRATCH>` = `<SCRATCH>` ·
  > `<PRIMARY>` = `<PRIMARY>`. (This wrapper message is the only text sent besides that file;
  > record it too, with those three paths written as their placeholders.)

  The file:

~~~~text
You are the reviewer for one rule-4 cold pass in the atelier repo. You run on Fable, the
principal-named review tier. State the model you find yourself running as in your verdict's
provenance.

**The brief:** `<WT>/docs/reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md` (board
`160/1820`, finding prefix `DP`). Read it whole first, then follow it and
`docs/method/REVIEW.md` exactly. It defines the scope, the barred reading, the re-run list, the
live-behaviour bounds, the deliverable and the two acts. Nothing here changes it.

**Your worktree:** `<WT>` (branch `atelier-4c-dp-pass`, HEAD `9e6712b4`, which is `origin/main`
as I spawn you). The only commit after the brief's landing (`8a591e0a`) is my claim, which adds
five lines to the `160/1820` board item, on your barred list. `git merge-base --is-ancestor
77fc8f42 HEAD` exits 0 there. Run every command from the worktree, with absolute paths. It is
read-only to you except the brief file, where you append your verdict.

**Your scratch directory:** `<SCRATCH>/dp/` (create it). All probes, scratch clones, synthetic
configs, stand-in binaries, fixtures and working notes go there. Delete your fixtures when you
finish act 2.

**Who I am, disclosed (rule 4):** session `01c055e5` (`atelier-4c`), Opus 5.5, opened by the
principal to brief and run this one pass. I am an off-tier orchestrator: I hold the context
partition, commit the records and release the held-back sibling after your act 1 is committed.
I form no finding and write no severity. I authored no part of the delta and no part of the
brief: I started its writer, headless session `43d5be30` (Opus 5.5), with a process-only prompt
plus five notes for it to verify (the brief's *Spawn provenance* lists them). My exposure before
spawning you, disclosed in full: items `160/1820` and `210/620` whole (**`210/620` carries the
authors' account of every fix, two departures from the counsel and a test result**); the route
paragraph of item `450/010` (row 2's steps A to D); the record of the session that ran the `DV`
and `PK` passes (**it gives each verdict's counts and one-line counsel, not the findings'
text**); from the `DV` pass's file, its heading outline, the spawn prompt in its verdict's
provenance, and a handful of lines a heading search printed (**fragments of three findings'
text, about the spawn prompt's absolute paths and the model a session reports**); this brief's
header, *Spawn provenance*, *House rules* and *Process* sections, and its heading outline; the
brief-writer's commit message. I have not opened the held-back sibling, the authors' session
record, or any delta commit's body. None of that is yours to read before act 1, and I pass none
of it to you beyond this paragraph. The barred set is exactly the brief's; I add nothing and
remove nothing.

**Process rules:**

1. **No git writes.** No commit, add, checkout, switch, stash, reset, push or worktree command in
   `<WT>` or anywhere else. Read-only git (log, diff, merge-base, ls-files, grep, and commits via
   `tools/coldsweep.py`) is fine. I commit. A scratch clone under your scratch directory is yours.
2. **Never touch the primary checkout** `<PRIMARY>`: the live hook, the linked `ccfleet` and the
   in-place plugin run from it. Where the brief asks where it stands, use read-only `git -C
   "<PRIMARY>" log -1 --format=%h` and `git -C "<PRIMARY>" status --short` only, and read no file
   there; your worktree has the same commits. Never run an installed tool by bare name from
   `PATH`.
3. **Machine load.** Other sessions are live on this machine (the load has swung from about 10 to
   about 58 on 12 cores this evening). Check `uptime` before each heavy step; run one heavy
   process at a time under `nice -n 15`, in the foreground with a 600000 ms timeout (the `ccfleet`
   suite takes several minutes per interpreter). If the harness moves a long command to the
   background, wait for it and disclose that.
4. **No real launches.** The brief decides that no live launch reaches a model; keep to its
   stand-in world. No real config, no real repo, no `drive`, no real `drain`, no `claude` call.
5. **Subagents:** if you start any, give each an explicit `model`, keep it read-only, and have it
   write its report to a file in your scratch directory and return three lines. Any subagent that
   reads the delta and forms judgement must be Fable; the findings and severities are yours.
6. **Public repo.** Quote no secret, email address, home path, private repo name, estate fact or
   other session's transcript content. When you put this prompt in your provenance, write the
   absolute paths as `<WT>`, `<SCRATCH>` and `<PRIMARY>`, as they are here. Absolute ISO 8601
   dates from `date -u`; NZ English; prose wrapped at about 100 columns. Finding prefix `DP`.
7. **Act 1:** append your verdict below a `---` divider at the end of the brief file, complete per
   the brief's *Process*, then STOP and reply to me in at most five lines: that act 1 is written,
   the overall line with counts (MAJOR first), and anything I must know to commit it. Do not open
   the held-back sibling or either earlier verdict. The sibling is not in the tree; I release its
   path to you by message after I commit act 1.
8. **Act 2** starts only on my release message. Do it as the brief's *Process* says, then reply in
   at most five lines.
9. **If a usage limit or error stops you,** stop where you are; your transcript persists and I
   will resume you by message. Keep working notes in your scratch directory so a resume loses
   nothing.

Record this file verbatim in your provenance; it is saved at `<SCRATCH>/dp-spawn-prompt.md`.
Budget the time this pass needs; never thin it to fit.
~~~~

- **Barred-set choice.** The brief's, unchanged (the spawn prompt says so). **Release message:**
  none yet; act 2 has not begun.
- **What I read.** The brief whole; `docs/method/REVIEW.md` whole; `instruments/ccfleet` whole at
  HEAD (3,099 lines); `instruments/fixtures/review_queue_reference.py` and
  `instruments/ccfleet.example.json` whole; each of the 23 commits body-free through
  `tools/coldsweep.py --commit <sha> --path instruments --path tools --path skills --path
  CHANGELOG.md` (ledger below); `skills/review/run.md`, `skills/review/orchestrator-prompt.md` and
  `skills/session/close.md` whole at HEAD; the final-output blocks of the four fleet prompts and
  the tails of `fold-prompt.md` and `resume-prompt.md`; `tools/modelguard.py` lines 1–300 and
  372–480 plus its whole delta; the manual's *THREATS* section rendered; two public documentation
  pages of the harness (permissions, memory).
- **What I did not read.** `docs/sessions/`, every prior verdict, every `160` item beyond its
  title, the board items the brief bars, the delta commits' message bodies, `docs/method/census/`.
  I skipped the session-log step of the repo's read order.
- **Exposure to disclose.**
  1. The harness loaded, before the brief, the user-level instruction files, this repo's
     `CLAUDE.md` and a per-project memory index. They hold private context this verdict does not
     carry, and one-line titles of earlier review work in this repo. None gives an account of the
     delta or of a `DV` or `PK` finding. The harness's status snapshot showed five recent commit
     subjects, one of them a board commit about review doctrine; a title, no account.
  2. One read-only process listing (`ps`), run to learn whether the installed CLI keeps its
     arguments visible, printed other sessions' command lines. I read no transcript and quote
     none of it. What I took from it is one fact, used under assumption A2 below.
  3. `pointerscan`'s full-tree output went to a scratch file; I printed its counts and the path
     prefixes of three `160` items (titles only).
  4. The harness moved seven commands to the background after 180 seconds: five long runs (both
     `ccfleet` suites, one mutant batch, the combined-mutant suite, the whole `tools` suite) and
     two waits of my own. I waited for each and ran no second heavy process beside it; light
     probes ran meanwhile.
  5. One of my own Bash calls was refused by a live hook of this machine (a secret-path guard
     that read a search pattern as a file name). I re-ran it without the pattern. No finding.
  6. `--include-barred` was never used.

### The floor, reproduced

Every line of the brief's re-run list was run from the place it names; the ledger is at the end.
All exit 0: the manual lints clean at style level; both `ccfleet` suites pass (152 tests, Python
3.14.6 and 3.9.6); the four `tools` suites pass on both interpreters; the pushed floor is green on
`a033f023`, whose tree holds the delta (the run on `77fc8f42` itself was cancelled, as the brief
says). The synthetic world behaved as the delta claims on every line of the brief's list.

### Lens 1 — approach and assumptions

My load-bearing assumptions, named before I read a line of the delta (my working notes carry the
time, 2026-11-25T20:35Z), each with what the probes did to it:

| | Assumption the work rests on | State | Probe |
|---|---|---|---|
| A1 | The last turn's text can carry a verdict; position tells a real verdict from quoted text | **damaged** | `DP2`, `DP6`: 26 final outputs through `harvest`, old reader beside new |
| A2 | A launcher's pid and the session record say reliably that a session is live | confirmed, one caveat | SIGTERM, SIGHUP, SIGKILL probes; the installed CLI's arguments are visible to `ps` on this machine, so the record's check has something to match. By reading only: where `ps` cannot be run the record is removed as dead (it fails open) |
| A3 | Files under `kit_dir` say honestly that a pass started | **damaged** | `DP13` |
| A4 | Withholding import lines plus a `Read` deny keeps imported private text from a public session | **damaged** | `DP3`, `DP4`, `DP18` |
| A5 | The queue keeps the route; a seal stands before every review-tier launch | holds for `ccfleet`'s side; **damaged** for the reference queue's `take` | `DP7`, `DP8` |
| A6 | A deny-list hook over shell shapes converges | **damaged** | `DP1`, `DP9`, `DP10`: this round removed denials the hook had |
| A7 | `models=` from the log is what the reviewer ran on | not testable without a launch; the record has no reader | `DP15`; live half NOT RUN |
| A8 | Date-and-second log names are unique and pair with their `.end` | confirmed for `.json` logs | world listing; `DP20` for the `.out` files |
| A9 | The stand-in in the tests stands for the real CLI | holds for what `ccfleet` hands a session; not for what the harness then does | live ledger |
| A10 | Prompt wording is the control for tier and fork | unchanged by the delta: wording plus a self-report | `DP15` |
| A11 | The principal's typed words can be told from a skill call's arguments | plausible; fixed in two skills of at least four | `DP12` |

The brief's own lens-1 questions:

- **Class or instance?** The worktree and settings-copy fix is aimed at the class and holds for
  every signal and every launch shape I drove. The verdict reader, the reset exemption, the
  import withholding, the hook's additions, the long-flag table, the typed-words guard and the
  pointer check are each aimed at the shape that was reproduced: `DP2`, `DP13`, `DP3`/`DP4`/`DP18`,
  `DP1`/`DP9`, `DP10`, `DP12`, `DP19`.
- **Is the last turn's text a sound basis for releasing a paid claim?** Sound enough, because a
  release also needs exit 0, no error flag, a word in `release_on` and a worktree with nothing
  unlanded, and because nearly every misreading falls to `UNKNOWN`, which releases nothing. One
  shape reads the other way (`DP6`).
- **Is the reset exemption a control or a convention?** A convention, and the manual says so
  (*THREATS*: a plain `run` with the right label writes the file the fold looks for). It stops the
  accident, not a session that means to. It also refuses one honest case (`DP13`).
- **Is withholding plus a `Read` deny the right fix?** It is right as far as it reaches. It
  reaches the appended text and one tool. Two other channels to the same private text stay open
  and unnamed (`DP3`, `DP4`).
- **Is the widening deny-list converging?** No, on this round's evidence: the tmux reading turned
  seven launches the hook denied into passes, and the round added false denies (`DP1`, `DP9`).
- **Does each fix close its class or move the risk?** Moved: the verdict fix moved the risk from
  an earlier mention to format drift (`DP2`) and to a quoted pair (`DP6`); the hook fix moved it
  into the option parsing it added (`DP1`).

### Lens 2 — correctness and quality

Confirmed by probe, as claimed (claim numbers are the brief's):

- **1, 2** the exact review shape and the exact fleet shape read correctly; an earlier mention
  no longer settles a pass; two shaped verdicts that disagree read `UNKNOWN`; a stop word is kept.
- **3, 4** SIGTERM, SIGHUP and SIGKILL to a launcher each leave the session running with its
  record, its worktree and both copies; a fold and a resume into that worktree exit 2; another
  launch's sweep leaves the copies while the session lives and takes them once it has ended; a
  session killed outright reads `ERROR` and its copies go with the launcher.
- **5** after the reset a fold runs for a pass with a result file or a drain `START` line, exits 3
  for an item with neither, and exits 64 when its template is `pass_prompt`.
- **6** a public repo's session is handed the shared text with the import line replaced by a note
  naming no path, under a header naming no path, and a deny rule for the imported file; a private
  repo's gets it inlined, with no deny. Both copies are mode 0600.
- **7** `check` printed `MANAGED:` and the import line; `WIDENS: sandbox`, `KEPT, not classified`
  and `VISIBILITY MISMATCH` are covered by the delta's own tests, which pass.
- **8** the reference queue's `next` keeps to the route it is asked for, with the stated spill.
- **9, 10** an unsealed dry drain exits 0 and says no launch was rehearsed; a sealed one names its
  pick; another run's id is refused; `unknown` cannot seal; a real drain's end calls `unseal`, and
  a second drain then exits 1 as not ranked.
- **11** the example keeps no `FINISH_WORDS`; the shipped fold prompt is refused without it.
- **12, 13** `.json` logs carry date and second, each with a `.end`; the cost history counted the
  one clean pass and not the pass whose launcher was signalled; `END` lines carry `models=`.
- **14, 16** the shapes the docstrings name are denied or flagged as written.
- **17–22** the skill and prompt sentences are there as claimed.

Not as claimed: `DP1`, `DP2`, `DP5`, `DP7`, `DP9`, `DP10`, `DP13`, `DP17`, `DP20`. Nothing in the
delta is a stub presented as done.

### Lens 3 — completeness and harvest

- **Mirror sites (V3).** Two older sentences the delta should have reached still state the rule
  it replaced (`DP11`). The typed-words guard reached two skills (`DP12`). `REVIEW.md` rule 4 still
  says "verbatim" where the prompt now says placeholders (`DP16`). The fleet prompts were not told
  the shape the reader now demands (`DP2`).
- **One home (V4).** The seal and the route rule appear in the manual, the `ccfleet` docstring,
  the reference queue and `run.md`; each of the first three points at `run.md` as the home, which
  is the right shape. `run.md` and the changelog then say something of `ccfleet` that is not so
  (`DP7`).
- **Tests that stay green on a broken delta.** Seven of the mutants I wrote survive the whole
  `ccfleet` suite together (`DP5`).
- **What the fixes should have touched and did not.** `skills/work/run.md` and `plan.md` for the
  typed-words guard; the four fleet prompts for the shape; `REVIEW.md` for the placeholder rule;
  *THREATS* for auto memory and the settings folder.

### Lens 4 — security and privacy

Design altitude, threats named for the class (an unattended session with the user's credentials,
steerable by text others write; a reader of that session's own words; a hook in front of every
tool call):

- *What a public repo's session can still reach of the user-level files.* The appended text is
  clean of the imported file and of its path where the import stands alone on a line. Left open:
  the settings folder beside its own copy (`DP3`), the harness's auto memory (`DP4`), an import
  line of five other shapes (`DP18`), and the residuals the manual already names (a shell command,
  a known path, an import inside a sentence).
- *What the sweep may delete.* Only files in `<kit_dir>/settings/` whose name matches
  `<session>.<pid>.json` or `-user-instructions.md`, whose launcher pid is dead and which no live
  record lists. It cannot be steered outside that folder by a file name. A reused pid keeps a
  file; it never deletes a live one. Sound.
- *What hostile text can make the verdict reader do.* It can turn a real verdict into `UNKNOWN`,
  halt a drain with a quoted stop word, or, with a drifted real verdict, be read as the verdict
  (`DP6`). Each needs the session to copy a line-initial `RESULT:` line into its final output,
  which the prompts forbid.
- *A hostile repo's settings and instruction files.* Unchanged by the delta; *THREATS* names them.

Code altitude, checked against OWASP ASVS 4.0 chapters V1 (trust boundaries), V4 (access
control), V5 (validation and injection), V7 (logging), V8 (data protection) and V12 (files), by
reading and by `grep`:

- *Injection.* `grep -n "shell=True\|os\.system\|os\.popen\|eval(\|exec(\|pickle"` over the four
  code files prints nothing. Queue output, config values, import paths and the forge's answer
  reach `subprocess` only as argv lists. A model name is stripped of spaces and commas before it
  is printed on an `END` line, so it cannot forge a field.
- *Paths.* `check_repo_name` and `safe()` stand in front of every label and repo used in a path;
  a session id is matched against `[A-Za-z0-9_-]+` before it reaches a glob or a lock name.
- *Permission rules.* The deny rule is built from a path the operator's own file names. A path
  holding a glob character would widen or break the rule; not probed, since the operator writes
  the path.
- *Data at rest.* The two copies are 0600. The folders `settings/`, `sessions/` and `logs/` are
  0755 and logs and results 0644; older behaviour, recorded, not hunted.

**`/security-review` (V6): discharged by grounds.** It reads the session's pending diff. My
worktree is clean and must stay so (the brief is the only file I may touch, and the scanner must
never run over a dirty brief), so it has nothing to read; a scratch clone holding the diff would
still be scanned from this session's own tree, not the clone. The landed delta is covered by the
catalogue check and the probes above instead.

### The paid-drain path, on its own line

**`/atelier:review plan` and `/atelier:review run`, with `ccfleet` as the fixes leave it: I found
nothing that loses a paid pass, runs one twice, or lets one start without the seal.** A drain of
two stand-in passes ran, sealed, claimed, released, unsealed and costed as the manual says, with a
signal to one launcher on the way. The risks I leave on this path are: a pass whose final output
puts a blank line between its `RESULT:` and `ITEM:` lines now reads `UNKNOWN` and counts toward
the three-bad-ends stop (`DP2`); the route rule is the queue's alone, and two texts say `ccfleet`
passes the route when only the example config does (`DP7`); and the adopter actions in the
changelog must be made in a config and a queue I was not allowed to see.

### The standing checklist

- **V1 — no claim stronger than its evidence.** Findings `DP1`, `DP5`, `DP7`, `DP9`, `DP10`,
  `DP17`, `DP20`.
- **V2 — recorded proofs re-run.** Every line of the re-run list, both interpreters; the pushed
  floor read. The skills test class says each of its tests "was seen to fail on the unfixed
  text"; they are literal sentence pins, which fail when the sentence goes, and I did not re-drive
  each. For `ccfleet`'s tests I ran the converse (mutants), and seven survive (`DP5`).
- **V3 — a changed rule is swept to its mirrors.** `DP2`, `DP11`, `DP12`, `DP16`.
- **V4 — one fact, one home.** Holds for the seal and route rule (pointers to `run.md`) and for
  the reviewer prompt (one home, pinned by a test). `DP7` is a wrong copy, not a second home.
- **V5 — no internal contradiction.** `DP7` (`run.md` against the docstring and manual), `DP11`,
  `DP16`. Cross-references checked for the rule they reach: the manual's "see *The seal*" reaches
  the route rule; `run.md`'s pointer to `man ccfleet` (*The seal*) reaches the contract;
  `close.md`'s pointer reaches the *Ending the session* heading (pinned by its test).
- **V6 — security and privacy.** Lens 4 above; the scanner discharged by grounds.
- **V7 — spawn provenance.** In the brief and repeated above, with the prompt verbatim.

### Per-commit ledger

Each commit was read body-free with `coldsweep --commit`; every run printed its confirmation line
and exit 0. For six `ccfleet` commits I first read the code at HEAD and the commit's manual and
test hunks, then the commit's code hunks.

| Commit | Subject (short) | Body-free | Findings |
|---|---|---|---|
| `9d52835a` | pointerscan: delta named by citation alone | yes | `DP19` |
| `5d3265e2` | modelguard: the launches found, the refusal text | yes | `DP1`, `DP9`, `DP10` |
| `127f3fef` | tools README: modelguard and pointerscan entries | yes | `DP9` |
| `b7a3a694` | skills: the review texts' findings | yes | `DP14`, `DP15`, `DP16` |
| `001d9b42` | skills: typed close words may skip a step | yes | `DP12` |
| `7a2ec7e9` | skills: work run step 1, a linked plugin root | yes | `DP12` |
| `be31d53b` | skills: fleet sweep, a settled end | yes | none |
| `1c3488ad` | tools: pin the review prompts and `run.md` | yes | none |
| `db4984c1` | skills: how a fold passes the reset; the route | yes | `DP7`, `DP11` |
| `422b5b5c` | ccfleet: `RESULT` only in the final-output shape | yes | `DP2`, `DP6`, `DP11` |
| `e6a27480` | ccfleet: a live session's copies and worktree | yes | `DP3`, `DP5`, `DP11` |
| `acfd0d59` | ccfleet: a fold passes the reset for a started pass | yes | `DP13` |
| `4ae0f05e` | ccfleet: models on the `END` line | yes | `DP15` |
| `7db38b4b` | ccfleet: the reference queue's `next` and the route | yes | `DP7`, `DP8` |
| `a8d5e35b` | ccfleet: withhold the import lines and deny them | yes | `DP3`, `DP4`, `DP18` |
| `afa9aec7` | ccfleet: test the two copies by suffix | yes | none |
| `3c824d40` | ccfleet: the finish word per call | yes | none |
| `be934126` | ccfleet: an honest dry drain; `unseal` | yes | `DP17` |
| `d07c0682` | ccfleet: `check` names kept keys and visibility | yes | none |
| `389b9424` | ccfleet: log names; a later session's own end | yes | `DP20` |
| `f58cc435` | ccfleet: manual residuals | yes | none |
| `36ec7901` | ccfleet: pin five mutants | yes | `DP5` |
| `77fc8f42` | the landing: changelog, README, `run.md` | yes (board hunks left out by `--path`) | `DP7` |

Later commits on the delta's paths: none since the brief's pin. The three the brief lists
(`f239dc3b`, `e8c7d631`, `6e11c551`) change, undo or contradict no delta line that I found.

## Findings

Every finding is the principal's to decide (rule 3). Counsel is labelled and sits beneath its
finding. "Old" below means the hook or reader as it stood at `932a0185`, extracted to my scratch
directory with `git cat-file -p` and driven by the same probe.

### DP1 — MODERATE — the hook's tmux reading passes launches it denied before the fix

`tools/modelguard.py` `tmux_hit` (added by `5d3265e2`) keeps skipping words that look like tmux
options after the command it found has begun. `-c`, `-p`, `-t`, `-e` and `-s` are in its
value-taking set, so the command's own `-c 'script'` or `-p x` is thrown away with its value.

Probe (`mg_probe2.py`, each command through the hook's own entry as a `PreToolUse` payload, old
hook beside new, same result on 3.14 and 3.9):

| Command | old | new |
|---|---|---|
| `tmux new -d sh -c 'claude -p x'` | deny | **pass** |
| `tmux new -d bash -c 'claude -p x'` | deny | **pass** |
| `tmux new-window sh -c 'claude -p x'` | deny | **pass** |
| `tmux split-window -h bash -lc 'claude -p x'` | deny | **pass** |
| `tmux new -ds w claude -p x` | deny | **pass** |
| `tmux if-shell true 'claude -p x'` | deny | **pass** |
| `tmux new -d script -q /dev/null claude -p x` | deny | **pass** |
| `tmux new -d claude -p x` | pass | deny |

The last row is the shape the fix was written for, and it works. The seven above it are a launch
with no model that the hook refused before this delta and passes now: the brief's "a launch with
no model that `modelguard` now passes". The docstring and changelog say tmux launches are denied;
the deny table pins only the shapes that happen to work. Criterion: the hook's own rule (a
session start with no model is denied) and V1. Not MAJOR: `ccfleet` names the model itself, so
the drain does not lean on this hook, and the docstring calls it a net.

*Counsel:* stop reading tmux's options once the first command word is found (everything after it
is the command's), and treat any `claude` word after a tmux run or send subcommand as a launch
unless a model is named. Add the seven rows to the deny table.

### DP2 — MODERATE — ordinary final outputs now read as no verdict; the prompts were not told

`shaped_results` (`422b5b5c`) takes a fleet verdict only when the `RESULT:` line is the last
non-blank line of the text and its block, up to a `REPO:` line, holds no blank line. It takes a
review verdict only when `RESULT:` sits directly above `ITEM:`.

Probe (`rw_probe.py`, 26 final outputs through `harvest` on a clean JSON end):

| Final output | old | new |
|---|---|---|
| fleet block inside a code fence | DONE | **UNKNOWN** |
| fleet block, one blank line before `RESULT:` | DONE | **UNKNOWN** |
| fleet block, blank lines between fields | DONE | **UNKNOWN** |
| fleet block, a closing sentence after `RESULT:` | DONE | **UNKNOWN** |
| fleet block, a multi-line field with a blank line | PARTIAL | **UNKNOWN** |
| review shape, a blank line between `RESULT:` and `ITEM:` | DONE | **UNKNOWN** |
| exact shapes, bold keys, CRLF, trailing spaces, a reason on the line | same | same |

End to end in the synthetic world, a fenced fleet report and one with a blank line before its
last line each ended `result=UNKNOWN` with `KEPT worktree … RESULT UNKNOWN is not clean`.

The four fleet prompts introduce their block as "Final message (plain text, this shape, under N
lines)". None says the block must hold no blank line, must not be fenced, or must end the
message; several of its fields are "one line each" lists, where a blank line is the natural
separator. The delta tightened the reader and left the prompts as they were, and its own test
pins the blank-line case as intended. The cost falls in the safe direction: nothing is released.
But a finished fleet job is kept and run again by the next `drive`, and on the paid path a review
pass that drifts by one blank line reads `UNKNOWN`, keeps its claim and worktree for a resume, and
counts as a bad end, three of which in a row stop a drain with budget unspent. How often a model
drifts this way I could not measure (no launch; the estate's results are a non-goal). Criterion:
lens 1 (class or instance), V3, and the brief's "misread".

*Counsel:* either say the constraint in every prompt whose output is read (no blank line in the
block, nothing after it, no fence), or loosen the reader where loosening is safe: ignore a closing
fence, and allow blank lines between `RESULT:` and the shape line when no other `RESULT:` line
stands. Count an out-of-shape `RESULT:` apart from a missing one in the drain's log, so three in
a row are not read as a spent budget.

### DP3 — MODERATE — a public session's settings folder holds what the fix withholds from it

`<kit_dir>/settings/` holds every running session's two copies. A private repo's copy holds the
imported file inlined. A public repo's own settings copy holds the deny rule, which spells the
withheld file's absolute path. Every session is told `{SCRATCH}`, which is
`<kit_dir>/scratch/<repo>/`, so the folder is two steps from a path it was handed; its session id
is `{SESSION}`.

Probe (synthetic world, a private-repo session held open by the stand-in while a public-repo
session ran):

```
--- settings dir while the private session runs:
-rw------- <sid>.22895-user-instructions.md
-rw------- <sid>.22895.json
--- files there naming the invented private name:
<S>/world/kit/settings/<sid>.22895-user-instructions.md
--- the public session's deny rules:
Read(/<S>/world/cc/CLAUDE-extra.md)
covers kit_dir/settings: False
```

The files are owner-only, and every session runs as the owner. Whether a public session can read
them rests on its grant: the harness's documentation says a read outside the working directory
needs approval, so a config that grants nothing refuses it. A review pass is not such a config:
its reviewer writes `{REVIEW_LOG}` under `<kit_dir>/review-logs/` and reads the held copy in act
2, so a drain's sessions hold a grant outside the worktree, and a drain runs public and private
repos side by side. The delta lengthens the copies' life (they now outlive a signalled
launcher until the next launch). *THREATS* says the public session "is not told where they are";
its own settings file tells it. Criterion: claim 6, lens 4, V1. The live half (the harness
enforcing or not enforcing a read of that folder) is NOT RUN.

*Counsel:* add `Read` deny rules for `<kit_dir>/settings/` (and `sessions/`) to every session's
settings, public and private, since no session needs to read either; and say in *THREATS* that
the folder exists beside every session.

### DP4 — MODERATE — auto memory is a second channel into a public session, unguarded, unnamed

The harness's memory documentation (fetched 2026-11-25) says each project has a memory directory
under the config directory, that "all worktrees and subdirectories within the same repo share one
auto memory directory", and that the first 200 lines or 25 KB of its `MEMORY.md` are loaded into
every session with auto memory on. It is switched by a setting (`autoMemoryEnabled`) or an
environment variable, neither of which `--setting-sources project,local` touches.

So a session `ccfleet` starts in a worktree of a public repo is handed that repo's memory index,
written by the operator's own earlier sessions, which may name anything those sessions knew.
`grep -n -i "auto memory\|MEMORY.md" instruments/ccfleet instruments/man/ccfleet.1` prints
nothing: `ccfleet` neither switches it off for a public repo nor runs the private-name guard over
it, and *THREATS*, which the changelog says "names what remains", does not name it. The brief
records that sessions on this machine are handed such an index. This channel is older than the
delta and is no wider than what an interactive session in the same repo gets; it is a finding
here because the fix's claim is about what a public session is handed, and the guard's promise
("a private name … reaches no public session by what ccfleet appends") reads wider than it is to
anyone who does not know the second channel exists. Live half NOT RUN (no launch).

*Counsel:* for a public or unknown repo, set auto memory off in the session's settings copy or
its environment, or read the index with the private-name guard and refuse or warn as
`instructions_guard` says; name it in *THREATS* either way.

### DP5 — MODERATE — seven broken versions of the fixes pass the whole suite

Claim 23 and the changelog say the tests pin the fixes "and the mutants that survived". I applied
seven one-line mutations together to a scratch clone at my HEAD and ran the whole `ccfleet` suite
on Python 3.9: `Ran 152 tests in 224.593s`, `OK`. Each also survived its own targeted run first.
Of fifteen mutants run, the suite killed six (the stop-word reading, the withholding, the deny
rule's presence, the kept copies after a signal, the worktree refusal on a fold, the pid in a
copy's name), which is the delta's tests working.

| | Mutation | What a regression there would do |
|---|---|---|
| M1 | the sweep ignores live session records | the next launch deletes a running session's settings copy |
| M4 | `pass_started` ignores `START` lines | a fold of a cut-off drain pass is refused after the reset |
| M8 | the deny rule is written for the path only, not its real path | a config folder reached through a link is denied by one name only |
| M9 | `resume` no longer checks the worktree | a resume of another session id starts beside a live session |
| M10 | a dry drain calls `unseal` too | a rehearsal ends the real run's seal |
| M11 | a review briefed after the seal is offered on every route | an unplanned pass on a route other than local |
| M13 | a fleet `RESULT:` line need not be the last line | a verdict is read from the middle of a block |

M1 is the fix's central hold: the test that covers it launches nothing between the signal and the
session's end, so the sweep never runs while a record is live (my probe did run one, and the
copies stayed). Two further survivors are equivalent or unreachable and are not counted.
Criterion: lens 3,
V1, and the brief's "a guard that … stays green on a bad one".

*Counsel:* one test per row; for M1, start an unrelated launch while the signalled session still
runs and assert its copies remain.

### DP6 — minor — a quoted, well-shaped pair outranks the session's own drifted verdict

With the session's own verdict out of shape and a shaped pair quoted later in the same text, the
reader takes the quote. Probe: a final output whose own lines are a `RESULT: FAILED` line, a
blank line and its `ITEM: r:i` line, then a NOTES line and an indented quote of a `RESULT: DONE`
line above an `ITEM: r:i` line, read FAILED on the old reader and **DONE** on the new. This is
the one misreading I found in the unsafe direction: a `DONE` releases the claim and removes a
clean worktree. It needs two things at once (the drift of `DP2`, and a line-initial quote the
prompts forbid), so it is minor. A second
shape: after a shaped `DONE`, a last line that begins `RESULT: BUDGET EXHAUSTED` (a quote in the
notes, say) is read as a second shaped verdict and halts the drain (old reader: `DONE`).

*Counsel:* let a clean word stand only when no other `RESULT:` line in the text names a word that
is not clean.

### DP7 — minor — two texts say `ccfleet` passes the route; only the example config does

`skills/review/run.md:115` ("ccfleet calls the queue's `next` with `--route local`") and
`CHANGELOG.md:55` ("ccfleet now calls it with `--route local`"). `grep -n -- "--route"
instruments/ccfleet` finds the words in the docstring alone, which says, correctly, that "the
example passes" it; the call is `queue_call(cfg, "next", {"LAUNCHED": …, "BY": …})`. An adopter
who reads the changelog's action and changes nothing gets no route argument. The reference queue
defaults to `local`, so the fixture is safe; an adopter's own queue is not bound to. `run.md` is
what a drain session reads to learn what protects it. Criterion: V1, V5.

*Counsel:* say "the config's `queue.next` passes the route (the example does)" in both places, and
have `check` say when `queue.next` names no route.

### DP8 — minor — the reference queue's `take` keeps neither the route nor the writer rule

Probe (`q1.py`, the reference queue alone):

- The sealing run writes a brief after it sealed: `next` offers it and `take` by that same run
  exits 0. The rule that a session may not drain a brief it wrote is checked only when sealing.
- A review briefed after the seal whose `fits` does not list `local` is offered on `local`.
- A review sealed to another route that does not fit `local` spills to `local`.
- `take` of a review sealed to another route, as a hand-run `ccfleet pass` would call it, exits 0,
  though that budget lapses first and so "keeps its reviews".

The docstring says a pass started by hand "meets the same gate as a drain's"; it meets the seal,
not the route. The after-seal rule is stated openly in `run.md` ("a paid pass that no plan
showed"); whether that is wanted is the principal's. Criterion: claim 8, lens 1, the brief's "an
unplanned paid pass".

*Counsel:* have `take` apply the checks `seal` and `next` apply (the route, `fits`, `briefed_by`).

### DP9 — minor — ordinary commands the hook now refuses, and its advice is untrue for two heads

New false denies, each a pass on the old hook (`mg_probe.py`): `screen -r claude`,
`screen -x claude`, `screen -d -r claude`, `screen -dmS claude vim notes.txt`,
`tmux new -ds claude`, `tmux new -As claude` (a session named for the tool);
`msg=$(echo 'run claude -p later'); bash -c 'ls'` (text echoed inside any substitution is replayed
when any later shell runs a `-c` string); `echo "$(echo claude --version)"; sh -c 'ls'` (dashed
words are dropped from the echoed text, leaving a bare `claude`); and any command nested past
depth four that holds the letters `claude` anywhere, such as five nested `$( )` around a path
under the config directory or under the harness's own scratch root, whose name holds those
letters on this machine. The refusal and `tools/README.md` say `claude` "straight after a short
option" passes; after `screen` or `tmux` it does not. Each is rare. Criterion: the brief's "an
ordinary command it now refuses", V1.

*Counsel:* match the binary as a word, not a substring, past the depth limit; keep `-r`, `-x` and
clustered `-…s` as name-taking for `screen` and `tmux`.

### DP10 — minor — the long-flag table is still not the snapshot it says it is

The comment reads "`claude --help`, v2.1.302: long flags no common tool shares". The installed CLI
reports 2.1.302. Its help holds claude-only long flags the table lacks after the six were added:
`--tools`, `--safe-mode`, `--restricted`, `--cloud`, `--permission-prompts` and others, and
`--append-system-prompt-file` (named in the help as `--append-system-prompt[-file]`). Probe:
`somewrapper -q claude --tools Bash x`, and the same with `--safe-mode`, `--restricted`, `--cloud`,
`--permission-prompts` and `--append-system-prompt-file`, each pass;
`somewrapper -q claude --settings s.json x` is denied. The fix added the six instances named; the
class is "every flag in that help". Every flag in the table is in the help, and every flag
`ccfleet` passes exists in the binary.

*Counsel:* a test that reads a saved copy of the help and fails when a long flag is in neither the
table nor a stated list of shared flags.

### DP11 — minor — two older sentences still state what the delta replaced

- `skills/review/run.md:182` (Mode 1, step 4): a pass's verdict is "the first line beginning"
  with the result key "in its last turn". The reader now takes the line in the shape, and an
  earlier first line gives nothing. Written by `2d8e05e3`, before the delta.
- `instruments/man/ccfleet.1:191`: the settings file is `<kit_dir>/settings/<session>.json`. It
  is `<session>.<pid>.json`; the manual's own *FILES* entry says the name carries the pid.

Criterion: V3, V5.

### DP12 — minor — the typed-words guard reached two skills, not the others that take them

`run.md` (review) and `close.md` now say that where a model reached the skill, there are no typed
words and nothing is taken from the call's own arguments. `grep -rn "skill call's own arguments"
skills` finds those two only. `skills/work/run.md:68` ("The text the principal typed after the
invocation is that prompt's *This run* section") and `skills/work/plan.md:29` carry no such
guard, and `skills/work/run.md` is a delta file, edited for another point. A work run reached on
a casual phrase would take a model-composed brief as his. Criterion: lens 1 (class, not
instance), V3.

On `close.md` itself: the sentence the delta wrote keeps to the principal's recorded answer
("Obey, but say so"): skip, and name each step skipped and that the typed words asked. It is
pinned by text and by the body's digest. I found no house rule on his typed words that it breaks.

### DP13 — minor — the reset exemption refuses a pass that did start, and says it never started

`pass_started` looks for a result file or a drain's `START` line. A pass run by hand
(`ccfleet pass`, which the manual treats as a normal way in) whose launcher is then stopped has
neither: its `START` went to the terminal and no result file is written without an `END`. Probe
(`life1.sh`): such a pass, with its claim held and its session's log and record on disk, then a
fold after the reset:

```
RESET reached; not starting privrepo-010: no pass on privrepo:010 started (no result file or
START line for privrepo-010 under kit_dir), so this fold would be new work
exit=3
```

A resume passes the reset and writes the result file, after which the same fold runs (shown in
the same probe), so nothing is lost; the message is false and `run.md` says to take the fold
before a resume. The check is also unbounded in time: a result file from any earlier pass on the
same item satisfies it. Criterion: claim 5, V1.

*Counsel:* count the session's own log (`<label>-<HHMM>-<stamp>.json`, written at launch) and its
session record as evidence of a start.

### DP14 — minor — the fold's run-twice check matches the heading's words anywhere in the brief

`fold-prompt.md` step 0 now says to search the brief for the words of step 2's heading, without
its date, and, "if it is there", to treat the sibling as already folded. A brief or a verdict
that quotes those words, as any review of the review skills will, satisfies the search before any
fold has run. The fold then appends no sibling, can still end `DONE`, and the drain session
deletes the held copy on a `DONE`. This verdict avoids writing the phrase for that reason; it is
at `skills/review/fold-prompt.md` line 9. Criterion: claim 20, lens 1.

*Counsel:* match it as a heading line (at a line's start, after `#` marks), not as a phrase.

### DP15 — minor — `models=` is written and nothing is told to read it

The `END` line now carries `models=`. No step of `run.md` (step 4, Mode 2 or *Close*) tells the
drain session to read it or to compare it with the review tier, and `ccfleet` does not. The
docstring says the record shows the reviewer's model "beside the `REVIEW_MODEL` it was told";
the `END` line and the result file hold no `REVIEW_MODEL`. The manual's rule ("a pass whose only
model is the orchestrator's spawned no reviewer on another tier") has no reader either, and what
else a real log lists in `modelUsage` (a small housekeeping model, say) is NOT RUN. The tier
check that binds is still a prompt sentence and the reviewer's own statement. Criterion: claim 13.

*Counsel:* have `run.md` step 4 read `models=` on each `END` line and flag a pass that names no
model of the review tier.

### DP16 — minor — the placeholder rule covers the spawn prompt only; `REVIEW.md` lacks it

The orchestrator prompt now has a public repo's verdict quote the spawn prompt with absolute paths
as placeholders. Step 6 still has the release message carry "the held copy's absolute path" and go
into the provenance "verbatim", and the same bullet lists "any resume message"; the public-repo
bullet says "no home path". The held directory is user-local, so the contradiction the fix
removed for one message stands for the other two. `docs/method/REVIEW.md` rule 4, the canonical
home, still says "verbatim or as an attached file" with no public-repo exception. Criterion: V3,
V5, claim 17.

### DP17 — note — two small overclaims about a drain's end

The manual says `unseal` is called when a real drain ends "however it ends". It sits in a
`finally`, so a driver ended by SIGTERM or SIGKILL does not call it (the seal then simply holds
until it lapses, which is harmless). And a dry drain reads every failure of the queue's `next` as
"not sealed" and exits 0, so a broken queue rehearses as merely unsealed; the refusal text is
printed beside it.

### DP18 — note — five import-line shapes are neither withheld nor denied

`withhold_imports` takes a bare line and a `-`, `*` or `+` bullet. A numbered item
(`1. @file`), a block quote, a heading, a task-list item and an import followed by any other text
on its line stay as text that names the path, with no deny rule (probe: 13 line shapes). *THREATS*
names only "an import inside a sentence"; `check` lists none of them, and in the world it said
"Imports found: 1" beside a file that held two.

### DP19 — note — the pointer check keys on one phrase, and any two hashes silence it

`delta_by_citation` fires on "commit(s) citing" only ("commits that cite", "commits naming" pass),
and is silenced by two hex strings anywhere in the pointer, bound or not. Advisory by design; it
fired on three real pointers in the tree, so it works where the phrase is used.

### DP20 — note — the `.out` files the cost history and the reset check read carry no date

The docstring says "Log names carry the date and second, so no later launch reopens one". That is
true of the `.json` logs. A drain's `pass-<repo>-<item>-<HHMMSS>.out` carries the time of day
only and is opened for writing; a pass of the same item at the same second of another day would
reopen it. The odds are about one in 86,400 per repeat.

### Older lines, recorded and not hunted

- A second session's `seal` silently replaces a live run's seal in the reference queue; the first
  run's next `next` then fails and its drain ends as a queue error.
- `kit_dir` folders are 0755 and logs, results and review logs 0644.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE (`DP1`–`DP5`) · 11 minor (`DP6`–`DP16`) ·
4 notes (`DP17`–`DP20`).**

- **Does anything found lose, misread or mis-cost paid review work?** Nothing loses a pass or
  mis-costs one. Two things can misread one: a drifted final output reads `UNKNOWN` (`DP2`, safe,
  but it keeps a finished pass's claim and counts toward the stop), and a drifted verdict beside a
  quoted pair reads as the quote (`DP6`, unsafe, and it needs two unlikely things at once).
- **Are `/atelier:review plan` and `/atelier:review run`, with `ccfleet` as the fixes leave it,
  safe to run the principal's paid weekly drain from?** Yes: no MAJOR. Before the first pass,
  make the changelog's adopter actions in the private config and queue (the review tier's alias,
  `FINISH_WORDS` per call, the route on `queue.next`, since `ccfleet` does not add it), and read
  the first pass's `END` line for `result=UNKNOWN` before trusting the pace.
- **Can anything in the delta put private context into a public repo's session?** The delta adds
  no new channel and closes one. Two older channels stay open beside it and unnamed: the settings
  folder a session can reach from the scratch path it is handed (`DP3`), and the harness's auto
  memory (`DP4`); and five import-line shapes still name the path (`DP18`).

## Re-run ledger

All from `<WT>` at `9e6712b4`, 2026-11-25 UTC, between 20:33Z and 21:28Z. Heavy steps ran under
`nice -n 15`, one at a time; the load average fell from about 19 to about 3 over the pass.

| Line | Result |
|---|---|
| `git merge-base --is-ancestor 77fc8f42 HEAD` | exit 0 |
| `mandoc -T lint -W style instruments/man/ccfleet.1` | exit 0, no output |
| `python3 instruments/ccfleet --help` | exit 0 |
| `python3 instruments/fixtures/review_queue_reference.py --help` | exit 0 |
| `python3 tools/modelguard.py </dev/null` | exit 0, no output |
| `python3 tools/pointerscan.py --selftest` | exit 0, `ok (0 failure(s))` |
| `python3 tools/pointerscan.py --root . .` | exit 0; 22 advisory findings (6 grammar, 16 queue state), 3 of them the new citation warning |
| `python3 tools/coldsweep.py --selftest` | exit 0, `selftest OK` |
| `test_ccfleet`, Python 3.14.6 (from `instruments/`) | exit 0, `Ran 152 tests in 566.548s`, `OK` (moved to the background by the harness) |
| `test_ccfleet`, `/usr/bin/python3` 3.9.6 | exit 0, `Ran 152 tests in 269.864s`, `OK` (moved to the background) |
| `test_modelguard`, 3.14 and 3.9 (from `tools/`) | exit 0 and 0, 13 tests each |
| `test_pointerscan`, 3.14 and 3.9 | exit 0 and 0, 61 tests each |
| `test_subject_skills`, 3.14 and 3.9 | exit 0 and 0, 37 tests each |
| `test_session_close_single_source`, 3.14 and 3.9 | exit 0 and 0, 17 tests each |
| the whole `tools` suite, once (`unittest discover -q`, 15-minute load 7.1 on 12 cores) | exit 0, `Ran 3539 tests in 995.962s`, `OK` (moved to the background) |
| `gh run list … --commit 77fc8f42…` | `floor`: cancelled |
| `gh run list … --commit a033f023…` | `floor`: success |
| `git merge-base --is-ancestor 77fc8f42 a033f023` | exit 0 |
| the brief's `coldsweep` sweep, as written | exit 0, 22 hits over 778 files, all in delta files |
| world: `check` | exit 0 |
| world: `plan` | exit 0, one evidence row, `local: no measurement` |
| world: `--by run-A drain --dry-run`, unsealed | exit 0, `DRY not sealed: no launches rehearsed` |
| world: `seal --by run-A` | exit 0 |
| world: `--by run-A drain --dry-run`, sealed | exit 0, `DRY rehearsed launch:` naming `privrepo 010` and its dummy brief |
| world: `--by run-B drain --dry-run` | exit 0, not sealed: "the sealed ranking is run run-A's, not run-B's" |
| world: `seal --by unknown` | exit 1, refused |
| world: `run <public> --dry-run` | exit 0, `END … result=DRY` |
| world: `run <public>` | exit 0, `result=DONE … models=model-orch,model-review` |
| world: `run <private>` | exit 0, `result=DONE` |

The world's `kit_dir` afterwards held `driver.log`, `logs/` with a `.json`, `.err` and `.end` per
session and one dry `pass-*.out`, `results/<date>/`, an empty `settings/` and no `sessions/`
record. Further probes built on it, each a file in my scratch directory with its output:
`life1.sh` (SIGTERM to a hand-run pass; fold, resume, sweep, reset), `life2.sh` (a two-pass drain
with a signal), `life3.sh` (SIGHUP, SIGKILL, a killed session), `q1.py` (the reference queue),
`rw_probe.py` (the reader, old beside new), `mg_probe.py`, `mg_probe2.py`, `mg_probe3.py` (the
hook, old beside new, both interpreters), `mutate.py` with `mutrun.sh` (mutants on a scratch
clone), and a 13-line probe of `withhold_imports`.

## Live-behaviour ledger

No launch of the real CLI reached a model, as the brief decides. Read-only checks made instead:

| Claim resting on real behaviour | What I did | Live half |
|---|---|---|
| every flag `ccfleet` passes exists in 2.1.302 | `claude --version` (2.1.302); `claude --help` to a scratch file; `strings` on the binary for `--append-system-prompt-file` (12 hits; the help names it as `--append-system-prompt[-file]`) | read, not run |
| the six long flags the hook added exist; none is missing | each of the six is in the help; the table still lacks others (`DP10`) | read |
| the harness follows no `@` import in an appended file | not established: I did not find a decisive string in the binary and stopped; the tests rest on the stand-in | **NOT RUN**: a synthetic config directory has no sign-in, and a real one would load the operator's private file and spend budget beyond this pass's approval |
| a `Read(//path)` deny rule, by path or real path | the permissions page: `//path` is an absolute path from the root; a deny rule applies "when either the requested path or the file it resolves to matches"; it is applied, best effort, to Grep and Glob and to file commands the harness recognises in Bash | **NOT RUN**, same grounds |
| a read outside the working directory needs approval | the same page's table (read-only tools: no approval "within the working directory and additional directories") | **NOT RUN**, same grounds |
| auto memory reaches a worktree's session | the memory page, quoted in `DP4` | **NOT RUN**, same grounds |
| `modelUsage` names a subagent's model | the stand-in only | **NOT RUN**, same grounds |
| a session outlives a signalled launcher | the stand-in (a child in its own process session), under SIGTERM, SIGHUP and SIGKILL | **NOT RUN** for the real CLI, same grounds |
| the CLI's arguments stay visible to `ps` | one read-only `ps` of running sessions on this machine: they are | read |

## Method record

What I examined, in order, and why:

1. The spawn prompt, the brief whole, `REVIEW.md` whole. Tree check and the later-commit check.
2. My own assumptions A1–A11, written to my notes before any delta line.
3. `instruments/ccfleet` whole at HEAD, then the reference queue and the example config, noting
   candidate defects to probe; then each commit body-free in the order the brief lists them.
4. The floor: the light re-run lines, then the two `ccfleet` suites, then the four `tools` suites.
5. The hook: 80 commands through its entry on both interpreters, the same set through the old
   hook, then a tmux and screen set and a long-flag set.
6. The synthetic world, built by `mkworld.py` (two throwaway repos, a scratch config directory
   whose instruction file imports a second file naming one invented private name, a stand-in CLI
   that records what it is handed and never runs a model, the reference queue from my worktree);
   the brief's ten commands; then the lifecycle, queue, reader and withholding probes.
7. Mutants on a scratch clone: fifteen run in targeted test classes (six killed, nine survived),
   two of the nine set aside as equivalent or unreachable, the other seven run together through
   the whole suite.
8. The harness's two documentation pages, the CLI's help, the manual's *THREATS* rendered.
9. Sweeps for mirror sites with `grep` over `skills`, the manual and the changelog, and the
   brief's `coldsweep` line.

What I left out, and why: the whole of `tools/modelguard.py` between lines 300 and 372 and past
480 was read only where the delta touched it (the older parser is not the delta); the binary was
not searched further for import handling (stopped as inconclusive); `/security-review` was
discharged by grounds; the estate's own config, queue and results are non-goals; the three later
commits' own content belongs to their passes. Non-findings checked and not raised: the sweep
cannot leave its folder or delete a live launch's copies; a pid reused by another process keeps a
copy and deletes none; a resumed session's record replaces its pass's; the cost history reads old
and new log names; a model name cannot forge an `END` field; the dry drain touches no real
launched list and calls no `ranked` or `unseal`; `release` works after `unseal`, so a pass still
running when its drain ends can release; `close.md` keeps to the principal's recorded answer.

## Follow-up checklist

- [ ] `DP1`: stop `tmux_hit` reading options past the command; seven rows to the deny table.
- [ ] `DP2`: state the shape in each prompt whose output is read, or loosen the reader where safe;
      count an out-of-shape verdict apart in the drain's log.
- [ ] `DP3`: deny reads of `<kit_dir>/settings/` and `sessions/` in every session; name the folder
      in *THREATS*.
- [ ] `DP4`: auto memory off, or guarded, for a public or unknown repo; name it in *THREATS*.
- [ ] `DP5`: a test for each of M1, M4, M8, M9, M10, M11, M13.
- [ ] `DP6`: a clean word stands only when no other `RESULT:` line names an unclean one.
- [ ] `DP7`: correct `run.md:115` and the changelog; `check` names a `queue.next` with no route.
- [ ] `DP8`: the reference queue's `take` applies the route, `fits` and brief-writer checks.
- [ ] `DP9`, `DP10`: word match past the depth limit; name-taking options for `screen` and
      `tmux`; a help-derived test for the long-flag table.
- [ ] `DP11`: `run.md:182` and the manual's line 191.
- [ ] `DP12`: the typed-words guard in `skills/work/run.md` and `plan.md`, and any other skill
      that takes typed words.
- [ ] `DP13`: count the session's own log or record as a start; correct the message.
- [ ] `DP14`: match the fold's heading as a heading line.
- [ ] `DP15`: a step in `run.md` that reads `models=`.
- [ ] `DP16`: the release and resume messages in a public repo; `REVIEW.md` rule 4.
- [ ] `DP17`–`DP20`: wording, at the principal's pleasure.
- [ ] Before the weekly drain (2026-11-29 23:00 UTC): the adopter actions in the private config
      and queue, which this pass could not see.
- [ ] Act 2: the fix ledger for `DV1`–`DV11` and `PK1`–`PK21`, after this text is committed.

### Reconcile (act 2, 2026-11-25 UTC)

Act 1 above was committed unrevised as `785fa79e` before any of this was read; my worktree's HEAD
is that commit, its tree is clean, and `git diff HEAD~1 --stat` shows the one file, 856 lines
added. No act-1 text is changed below.

**The orchestrator's release message, verbatim**, the held copy's absolute path written as the
placeholder `<HELD>` (a user-local folder outside the repo, every worktree and every scratchpad):

> Release for act 2: act 1 is committed unrevised as 785fa79e and pushed to origin/main. The
> commit hook passed: datescan raised nothing on the quoted prompt, and the only red was
> pathscan's advisory, already there, in docs/build/README.md. Your worktree HEAD is now
> 785fa79e. The held-back sibling is at
> `<HELD>/atelier--2026-11-25-1920-dv-pk-fixes-recheck-cold.deferred.md` (read it there; do not
> copy it into the tree, and I fold it in after you finish). You may now open it, the two earlier
> verdicts, the barred records and the delta commits' bodies, and do act 2 exactly as the brief's
> Process says: append `### Reconcile` beneath your verdict, never revising act-1 text. Same
> process rules as before (no git writes, primary checkout untouched, load-gated heavy steps;
> load is about 4 now). Reply in at most five lines when done, with the overall line restated,
> MAJOR count first, and any new DP ids.

It is one paragraph as sent, wrapped here. It asks nothing about the delta and steers no finding.

**Read for act 2, in this order:** the held-back sibling, whole (20 questions, 14 facts); the
`DV` verdict's findings (`DV1`–`DV10`) and its reconcile whole (`DV11` is there); the `PK`
verdict's findings (`PK1`–`PK20`) and its reconcile from *Against the authors' account* to its
end (`PK21` is there); the intent record `210/620` whole; the 23 delta commits' message bodies;
the *Ending the session* section of the session-open prompt (for sibling question 16). Not read:
the rest of the two verdict files (their briefs, method records and folded siblings), the other
barred board items, `docs/sessions/`: nothing in the ledger turned on them.

**Residual risk, named.** The fix ledger below is anchored on the two earlier verdicts by design:
I read each finding and then looked for its answer. Act 1 is the cold half, and it stands as
written.

#### The fix ledger

"Re-driven" names a command or probe run at `785fa79e` on 2026-11-25 UTC; `mut2.py` applies one
named mutation to a scratch clone and runs the test the fix added (20 mutants, all 20 killed).
The states are the brief's.

| Finding | Counsel (pointer) | What answers it | How I re-drove it | State |
|---|---|---|---|---|
| `DV1` | `DV` verdict, *Findings*, `DV1`, counsel: key the exemption on the pass's result file or `START` line; refuse `pass_prompt`; say it in *THREATS* | `acfd0d59`; `instruments/ccfleet` `pass_started`, `run_one`; the manual's *THREATS* | Its own reproduction: reset passed, fold shape, item 777 never taken, a review-tier model named: `RESET reached … no pass on privrepo:777 started`, exit 3 (it exited 0 and started a session before). A fold with `pass_prompt`: exit 64 | **Fixed as counselled.** Residue: `DP13`; and the threat the manual now names is real (a plain `run` labelled `privrepo-777` before the reset, then the same fold after it: `START … model=model-review`, exit 0) |
| `DV2` | `DV2`, counsel: say `ccfleet` checks no word; one home, per call | `3c824d40`, `b7a3a694`; the example config; the manual at `reset_utc`; `run.md` Mode 2 and *Close* step 3 | `check --prompt` on the shipped fold prompt: `UNSET: {BRIEF} {FINISH_WORDS} {HELD}`; a dry fold without it: exit 5; the example's `vars` hold no such key | **Fixed as counselled** |
| `DV3` | `DV3`, counsel: three changes (the prompt stops on a refused model and bars a fork; the reviewer states its model; `models=` on the `END` line) | `b7a3a694` (`orchestrator-prompt.md` step 4 and the model bullet), `4ae0f05e` | All three are there and pinned; `END … models=model-orch,model-review` in the world; mutants "END line without models" and "example a full id" killed | **Fixed as counselled.** `check` still accepts any value (not counselled). Residue: `DP15` |
| `DV4` | `DV4`, counsel: the fleet prompts' `{ATELIER}` sentence, or have `run.md` say "no read of this skill" | `b7a3a694`, `run.md` *The reviewer prompt* | `grep`: "needs no read of this skill" present, "no read outside its worktree" gone (pinned) | **Fixed as counselled**, by the second of the counsel's two routes. The authors call it a departure; it is not one. That route corrects the claim and leaves the behaviour the finding saw (a reviewer in a repo whose doctrine sits outside the worktree may be handed "the worktree's `REVIEW.md` or none"), which the counsel allowed |
| `DV5` | `DV5`, counsel: one changelog entry with the adopter's action in bold | `77fc8f42`, `CHANGELOG.md` | Read: the entry leads with **Adopter actions** | **Fixed**, with one clause that is not so (`DP7`) |
| `DV6` | `DV6`, counsel: say whose id `--by` carries | `b7a3a694`, `run.md:283` | Its own reproduction on the reference queue: a pass taken by `run-D`; the fold under `run-E` ends `DONE`, then `release refused … not held by run-E`, exit 2, worktree kept; under `run-D`, exit 0 | **Fixed as counselled** (the wording route; the behaviour is the contract's) |
| `DV7` | `DV7`, counsel: three assertions and a fourth | `1c3488ad`, `acfd0d59`, `4ae0f05e` | Mutants M5, M8, M9, M10, M11 re-made: each killed | **Fixed as counselled** |
| `DV8` | `DV8` (note) | `b7a3a694`: step 4 points at the bullets; the load and live-systems rules moved into them | Read; pinned by `test_the_reviewer_instructions_have_one_home` | **Fixed** |
| `DV9` | `DV9` (note) | `b7a3a694`, `run.md` Mode 2 | Read; pinned | **Fixed** |
| `DV10` | `DV10` (note) | `b7a3a694`, the Provenance bullet | Read; pinned | **Partly fixed**: the spawn prompt only (`DP16`) |
| `DV11` | `DV` reconcile, `DV11` (note) | `acfd0d59`, *THREATS*: "In a bypass permission mode an unattended session can itself run ccfleet in either shape after the reset" | Read | **Fixed** (stated) |
| `PK1` | `PK` verdict, `PK1`, recurrence prevention: tie removal to the session's end; sweep at the next start; assert both copies while the session lives | `e6a27480`, `afa9aec7` | Its own reproduction under SIGTERM, SIGHUP and SIGKILL: both copies present while the session ran, after an unrelated launch's sweep too, gone after its end and one more launch | **Fixed as counselled.** The sweep's hold on live records is pinned by no test (`DP5`, M1) |
| `PK2` | `PK2`, counsel: record the worktree and refuse any launch into it | `e6a27480` | Its own reproduction: fold beside the live session, exit 2, nothing released, worktree kept | **Fixed as counselled** |
| `PK3` | `PK3`, counsel: say it in the contract, make the reference do it, a two-route test | `7db38b4b` | A review sealed to an earlier-lapsing route is not offered to `local` (`q1.py`, Q4); mutant "next ignores the route" killed | **Fixed as counselled.** Residue: `DP7` (who passes the route), `DP8` (`take`) |
| `PK4` | `PK4`, counsel: read the line directly above the shape line, anything else `UNKNOWN` | `422b5b5c` | Its two probe texts are the delta's own tests, which pass; mutant "first line wins" killed | **Fixed another way**: the authors added a second shape for the fleet prompts. The departure was needed (the counsel alone would read every sweep as `UNKNOWN`, since those prompts put `REPO:` first) and it meets the finding. It went further than the need: "last line, no blank line in the block" is what makes `DP2`, and the pairing of two shapes is what makes `DP6` |
| `PK5` | `PK5`, recurrence prevention: a deny rule per import target, neutralise the line, name the residual | `a8d5e35b` | The world: note in place of the line, header without a path, `Read(//…)` deny; a private repo unchanged | **Fixed as counselled.** What the same session can still reach: `DP3`, `DP4`, `DP18` |
| `PK6` | `PK6`, counsel: quote his message or "none given", never the call's arguments | `b7a3a694` (`run.md`), `001d9b42` (`close.md`) | Read; pinned | **Fixed as counselled** in the two files the finding named; the class is wider (`DP12`) |
| `PK7` | `PK7`: put it to him | `001d9b42`; his recorded answer on `210/620`, "Obey, but say so" | Mutant "run the step anyway" killed; the sentence read against his answer and against the close section it runs, which names no step as beyond his word | **Fixed as he answered.** The sentence does what the option text says and no more |
| `PK8` | `PK8` | `b7a3a694`, `run.md` Mode 1 step 3 | Mutant killed | **Fixed** |
| `PK9` | `PK9`, counsel, second option; the reconcile's addition (name the pick) | `be934126` | The world: unsealed exit 0 "not sealed"; sealed, "DRY rehearsed launch" naming the pick | **Fixed as counselled** |
| `PK10` | `PK10`, counsel: refuse `unknown`; an optional `unseal`; say what the seal does not gate | `be934126`, `b7a3a694` | `seal --by unknown` exit 1; a drain's end leaves no seal and a second drain exits 1; the manual and `run.md` say it; mutant killed | **Fixed as counselled.** Point (d) (a review outside the sealed order is offered and taken) is unchanged and now said in `run.md`; see `DP8`, `DP17` |
| `PK11` | `PK11`, recurrence prevention: an unknown kept key is "kept, not classified" | `d07c0682` | A user-level `sandbox` block and an unknown key: `WIDENS: sandbox`, `KEPT, not classified: someFutureKey`, `MANAGED:` | **Fixed as counselled.** The `NO GRANT` line beside them still says every asking call is refused |
| `PK12` | `PK12`, counsel: date-and-second names; read a later session's own `END` | `389b9424` | Log names in the world; mutant "history ignores `.end`" killed | **Fixed as counselled.** Its point (d), what a resumed session's total holds, is still tested by no one (live, NOT RUN) |
| `PK13` | `PK13` and its reconcile additions | `5d3265e2`, `127f3fef` | Seven of its named launches, old hook beside new: each pass → deny; `print('claude', …)`, `console.log` and `say` now pass; the two accepted refusals still refuse; the six flags | **Fixed as counselled for every shape it named; regressed beside them**: `DP1`, `DP21`; new false denies `DP9`; the table `DP10` |
| `PK14` | `PK14` | `be31d53b`, `f58cc435` | A drive: `BLOCKED`, skipped on the next drive, run again once its result file is deleted | **Fixed** |
| `PK15` | `PK15`, four mirror sites | `77fc8f42`, `127f3fef`, `7a2ec7e9` | Each site read at HEAD; a linked root prints its target | **Fixed** |
| `PK16` | `PK16`, counsel: tests for M11, M15, M21, Q2; pin R4, R6 | `36ec7901`, `1c3488ad`, `5d3265e2` | M11, M15, M21, Q2, R4, R5, R6 and G6 re-made: each killed | **Fixed as counselled** |
| `PK17` | `PK17` (note) | `f58cc435`, *THREATS* | Read | **Fixed** (stated; behaviour unchanged) |
| `PK18` | `PK18` (note) | `b7a3a694`, `fold-prompt.md` step 0 | Mutant killed | **Fixed**; the fix moved the risk (`DP14`) |
| `PK19` | `PK19` (note) | `f58cc435`, *THREATS* | Read | **Fixed** (stated) |
| `PK20` | `PK20` (note) | `d07c0682`, `f58cc435` | The delta's stubbed-`gh` test passes; in the world, with no forge name known, `check` prints no visibility line at all | **Fixed** (the check half; the residual stated) |
| `PK21` | `PK` reconcile, `PK21`, counsel: `pointerscan` warns on citation alone | `9d52835a`; this delta's own pointer names a range | It fires on three real pointers in the tree | **Fixed as counselled**; `DP19` |

Of 32: 30 fixed (27 as counselled or as stated, one as the principal answered, one another way
that meets the finding, one with a wrong clause), one partly fixed (`DV10`), one fixed and
regressed beside it (`PK13`), none unfixed. The authors' "all 32 applied as counselled" holds
but for `DV10` and `PK13`.

#### Against the authors' account

- **The two departures they name.** `PK4`: judged in the ledger; needed, and wider than needed.
  `DV4`: not a departure.
- **Their test claim** ("3,499 tests, one failure … under load; `test_ccfleet` 152 OK"). My
  whole-suite run at `9e6712b4`: 3,539 tests, `OK`, with the load low. The count has grown with
  later commits; no failure reproduced.
- **`1c3488ad`'s body**: "Each was run against the unfixed text or a mutant and failed." For the
  seven I re-made, yes. They are sentence pins: they fail when the words go, not when a sentence's
  meaning is turned with its words kept (sibling question 20). That is the nature of a prose
  pin; I add it to `DP5`.
- **`e6a27480`'s body**: the sweep takes copies "that no live session record holds". True of the
  code; no test would notice it stop (`DP5`).
- **`5d3265e2`'s body** lists the new denies and does not see that the tmux reading passes what
  the old hook denied (`DP1`).
- **The commit bodies of `77fc8f42` and `db4984c1`** carry the route claim of `DP7` ("next
  --route local").

#### My act-1 findings against the sibling's questions

| Finding | Sibling question | After reconcile |
|---|---|---|
| `DP1` | none reaches it | Stands, MODERATE |
| `DP2` | 7, from the other side | Stands, MODERATE |
| `DP3` | 8, in part | Stands, MODERATE, with an addition |
| `DP4` | 11 asks it; fact 13 saw it | Stands, MODERATE, with an addition |
| `DP5` | 20 | Stands, MODERATE, with an addition |
| `DP6` | 6, 7 | Stands, minor, with an addition |
| `DP7` | 1 asks it directly | Stands, minor. Found cold; the same suspicion |
| `DP8` | none | Stands, minor |
| `DP9` | 13 | Stands, minor |
| `DP10` | 14 | Stands, minor |
| `DP11`, `DP12` | 16, in part | Stand, minor |
| `DP13` | 2 | Stands, minor |
| `DP14`–`DP16` | 19 reaches `DP15` | Stand, minor |
| `DP17` | 18 | Stands, note, with an addition |
| `DP18` | 9, 10 | Stands, note, with an addition |
| `DP19` | 15 | Stands, note |
| `DP20` | none | Stands, note |

**Questions act 1 answered without a finding.** 2 and 3: a sealed dry drain's `pass-*.out`
holds no `START` line (checked again on the world's file: none), so neither `pass_started` nor
the cost history reads it as a pass; the `run --label` route is real and the manual says so. 4:
a reused pid keeps a copy and deletes none, and both copies are 0600; the manual does not say a
kept copy can outlive its session this way. A session whose record was never written falls in
a window of two statements, between the launch and the record. 5: I found no other way into an
existing worktree; `pass` and `drive` make a fresh stamped folder. 8: by the harness's
documentation the rule matches the requested path or the path it resolves to, and is applied to
Grep, Glob and the file commands the harness recognises in Bash; a script is not stopped, as the
manual says. 16: the skip rule agrees with `run.md` (skipping a close step grants no approval),
with the close section, which names no step as beyond his word, and with its test. 17: every
value the reviewer needs reaches it through the orchestrator prompt.

**Question act 1 did not reach: 12.** Probed now; it is `DP21`.

**The sibling's facts** agree with my re-runs line for line but for run times and for the whole
`tools` suite, which the brief-writer could not finish and I could. Fact 13 I could not have
seen: it is a live observation, and it goes to `DP4`.

#### Additions to act-1 findings (formed at reconcile; severities unchanged)

- `DP3`: the `DV` verdict's reconcile records the authors' statement that the estate's own
  sessions run in a bypass permission mode. I have not seen that config. If it is so, the read of
  the settings folder needs no grant at all, and the deny rule added for `PK5` covers the
  original file while its inlined copy sits unprotected beside every running private pass. The
  principal knows his config and can weigh it; I do not raise the severity on a file I may not
  open.
- `DP4`: the sibling's fact 13 is the live half I marked NOT RUN. The brief-writer's own session,
  started by `ccfleet run` into this public repo from the operator's real config, was handed the
  import line withheld, as designed, and "the harness's per-project memory index, which names
  private repos and estate facts". That is the brief-writer's observation, not mine; it matches
  the documentation.
- `DP5`: the skills' fixes have wording pins only, which is all prose can have; what a pin
  cannot see is a sentence turned with its words kept.
- `DP6`: "stopping is the safe direction" is not safe for a budget that lapses unspent; a quoted
  stop word that halts a drain costs the rest of that budget (question 6).
- `DP17`: a driver ended by a signal leaves its seal, so a drain restarted under the same `--by`
  runs on the earlier ranking until the seal lapses, against `run.md`'s "a restarted one
  included, plans and seals afresh" (question 18).
- `DP18`: `check` prints "inlined" for an import beside a public repo, where that repo's session
  gets it withheld; the sentence above the line says so, the line itself does not (question 9).

#### Finding formed at reconcile

**`DP21` (note, formed at reconcile, from sibling question 12). The hook's print-call skip keys
on the call's name, so a call of that name that runs its argument now passes.** `PRINT_CALL`
skips a string literal whose preceding text ends in `print(`, `puts(`, `say(`, `warn(` and the
like. Probe (`mg_probe4.py`, old hook beside new):
`python3 -c "import os; os.warn = os.system; os.warn('claude -p x')"` and
`node -e "const say = require('child_process').execSync; say('claude -p x')"` were each denied
by the old hook and pass the new one. Ruby and Perl backtick literals inside `puts(` and
`print(` are still denied. Both passing shapes are contrived, which is why this is a note; it is
the same class as `DP1`, a denial the hook had and lost to this round's loosening.

#### Overall, restated

**PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE (`DP1`–`DP5`) · 11 minor (`DP6`–`DP16`) ·
5 notes (`DP17`–`DP21`).** 21 findings; one, `DP21`, formed at reconcile. No act-1 finding is
raised, lowered or withdrawn. Of the 32 earlier findings, none is unfixed, one is partly fixed
(`DV10`) and one is fixed with a regression beside it (`PK13`).

The three plain lines, restated, unchanged in substance:

- **Lose, misread or mis-cost paid review work?** No loss and no mis-costing found. A drifted
  final output reads `UNKNOWN` (`DP2`); a drifted one beside a quoted pair reads as the quote
  (`DP6`).
- **Safe to run the paid weekly drain from?** Yes: 0 MAJOR, and every earlier MODERATE is fixed
  at HEAD. First make the changelog's adopter actions in the private config and queue, and the
  three private-config points the `DV` verdict's reconcile names (the pass prompt's path, the
  review tier's alias, no standing finish word), none of which this pass could open. Read the
  first pass's `END` line before trusting the pace. The decision is the principal's.
- **Private context into a public repo's session?** Not by what `ccfleet` appends. Open, and
  older than the delta: the settings folder (`DP3`) and auto memory (`DP4`, now seen live by the
  brief-writer).

Scratch fixtures (the synthetic world, the scratch clone, the old copies of the hook and of
`ccfleet`) were deleted after this was written; the probe scripts and their outputs stay in my
scratch directory. The held copy of the sibling is left for the orchestrator.

---

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-25)

Held out of the tree by the brief-writer and the orchestrator, at a held user-local path, until
act 1 was committed (`785fa79e`); released to the reviewer for act 2 by the message quoted in
the reconcile; folded here verbatim by the orchestrator, `01c055e5`, which formed no finding.

# Held-back sibling — `2026-11-25-1920-dv-pk-fixes-recheck-cold.md` (`160/1820`)

Written by the brief-writer, headless session `43d5be30` (`atelier-1d`, Opus 5.5), 2026-11-25 UTC.
Held outside the repo, every worktree and every scratchpad. Released to the reviewer by the
orchestrator only after act 1 is committed (`REVIEW.md` rule 1). It holds the brief-writer's own
seeded questions, the authors' account it met on the intent record, and the results of the
brief's re-run lines and of its synthetic world. These are claims to weigh, not findings: the
brief-writer forms no finding and writes no severity.

## Questions (20)

1. The changelog says "ccfleet now calls it with `--route local`". In the code, `ccfleet` calls the
   queue's `next` exactly as the config's `queue.next` template says; `--route local` is in the
   example config, not added by `ccfleet`. Is the changelog's claim true of the tool, or only of
   the example? What does an adopter whose `next` template omits `--route` get, with the
   reference queue (default `local`) and with a queue of their own? Does any surface tell an
   adopter they must add it?
2. `pass_started` treats a pass as started when `results/*/<repo>-<item>.md` exists under
   `kit_dir`, or a `START` line for that label is in `logs/pass-*.out`. Can a caller make that
   true without a pass having started, for example `run REPO --label <repo>-<item>` of some
   other job, or a `drive` jobs file using that label, or a sealed `drain --dry-run` (which the
   brief-writer saw leave a `logs/pass-*.out` file)? If so, is the reset exemption a control or a
   convention, and is that stated?
3. Does a sealed dry drain's `pass-*.out` carry a `START` line, and if so does the cost history
   (`pass_history`) or `pass_started` read it as a real pass?
4. The copies' sweep keeps a copy while its launcher's pid is alive. A launcher pid reused by an
   unrelated process keeps a copy (holding the user-level env block and instruction text) on
   disk indefinitely. Is that bounded, said, and owner-only? Conversely, can the sweep remove a
   copy a live session still reads: a session whose record was never written (the launcher died
   between `Popen` and the record write), or a record an older `ccfleet` wrote with three fields
   and no copies?
5. `refuse_live_worktree` is called for `run --in` and for `resume`. Is there any other way into an
   existing worktree (a `pass` or a `drive` job whose worktree path collides, a `drain` pick for an
   item whose earlier pass's session still runs under another launcher)?
6. `result_word` honours a stop word found on *any* RESULT line when no shaped verdict stands.
   Can text a reviewed repo puts into a session's final output (a quoted `RESULT: BUDGET
   EXHAUSTED` in NOTES) stop a paid drain? Is "stopping is the safe direction" true for a drain
   whose budget then goes unspent before it lapses?
7. The `PK4` fix reads a RESULT line that closes a block holding `REPO:` as a verdict (the fleet
   prompts' shape), beyond the counsel's "directly above". Can a final output that quotes a
   block from a reviewed repo or a log, ending in `RESULT: DONE` after a `REPO:` line, satisfy
   that test while the session's own verdict says otherwise?
8. A `Read(//<path>)` deny rule stops the Read tool. Does anything stop `cat`, `grep` or a
   script under a granted Bash rule, or the Glob/Grep tools, from opening the withheld file? Is
   "each imported file denied for reading" an overclaim for any config that grants Bash? Does
   2.1.302 match deny rules by the path given, by real path, or both, and through a symbolic
   link?
9. `ccfleet check` printed `INSTRUCTIONS IMPORT: @private.md -> <path>: inlined` with a public
   and a private repo configured. Does "inlined" mislead an operator about what a public session
   gets?
10. `withhold_imports` and `expand_imports` must agree on what an import line is. Is there an
    `@path` form the harness follows that `expand_imports` (and so `withhold_imports`) does not
    treat as an import, so its text reaches a public session unwithheld (a path only, but a path
    the fix says is never named)?
11. The import withholding covers what `ccfleet` appends. The harness also hands a session its
    per-project memory index (the brief's machine-local list). Is the delta's privacy claim
    scoped honestly to what `ccfleet` appends, and does any surface tell an adopter about the
    channels it does not control?
12. `modelguard` skips a string literal whose preceding program text ends in a call named
    `print`, `printf`, `console.log`, `puts`, `say`, `warn` or `alert`. Does an alias or a
    function of one of those names that runs its argument (for example
    `os.warn = os.system; os.warn("…")`, or a user function `say(cmd)` that execs) now pass a
    launch the earlier version denied?
13. The new depth rule denies any command naming `claude` past four levels. Does that refuse
    ordinary commands sessions run (a deeply nested `git -c alias` or `bash -c` that merely
    mentions the word), and is the cost stated?
14. Do the six long flags added to the table match `claude --help` for 2.1.302 exactly, and does
    `--help` list any other flag only `claude` takes that the table still lacks?
15. `pointerscan`'s bound test passes any pointer with two distinct hex runs of seven or more
    characters that contain a digit. Can a pointer pass with two hashes that bound nothing (an
    intent record's commit and a brief's pin)? And it fires only on the phrase "commits citing":
    does it miss "the commits that cite", "commits referencing", or "the `X` commits"?
16. The `PK7` change lets the principal's typed words skip a close step. Does that agree with
    `run.md` ("Typed words never stand in for an approval the rulings file says is needed"), with
    the session-open prompt's own close text, and with `test_session_close_single_source.py`? Is
    the option text's "as the rest of the house rules say" true?
17. The `DV4` fix took `run.md`'s "no read of this skill" route rather than having the prompt read
    the skill. Does every value the reviewer needs now reach it through the orchestrator prompt
    alone, and does `run.md` still say anything that only a reader of `run.md` would know?
18. `queue.unseal` is called after the drain's loop. Is it reached on every way a real drain ends
    (the stop file, the reset, a queue error, the unclean-stop count, a signal to the driver, an
    exception)? A seal left in place lasts until its lapse: does a restarted drain with the same
    `--by` then run on a ranking sealed for the earlier run?
19. `models=` on the `END` line comes from the log's `modelUsage`, which sums the session and its
    subagents. Does it show the reviewer's model distinctly enough to meet `DV3`'s purpose (a
    pass whose reviewer ran off-tier is visible in the record)? What does it print for a session
    whose launcher was signalled (no JSON yet)?
20. Several new tests in `test_subject_skills.py` pin sentences of the skills. Would each fail on a
    revert of its fix's *meaning* with the words kept, or only on a change of words? Which fixes
    have only a wording pin and no behaviour test?

## Facts (14)

1. **The authors' account, from the intent record `210/620` (session `b04df0da`'s done note),
   verbatim in part:** "Two places the fix departs from the letter of the counsel, for the
   re-check to weigh: `PK4` also accepts a `RESULT:` line that closes a block holding `REPO:`,
   since the fleet prompts put `REPO:` first and the counsel's "directly above" alone would read
   every sweep as UNKNOWN; `DV4` took `run.md`'s "no read of this skill" route, since ccfleet
   fills no `{ATELIER}` for the review prompts."
2. **The authors' test claim, same note, verbatim:** "Full tools suite on 3.14: 3,499 tests, one
   failure (a spellscan memory-bound test that passes alone, under load); `test_ccfleet` 152 OK on
   3.9 and 3.14."
3. **The authors' mapping of fixes to commits, same note, verbatim:** "`DV1`, `DV3`, `DV7` (M5),
   `DV11`, `PK1`–`PK5`: `422b5b5c`..`afa9aec7` (Opus worker). The skill texts, `DV2`–`DV4`,
   `DV6`–`DV10`, `PK6`–`PK10`, `PK14`–`PK16`, `PK18`: `b7a3a694`..`1c3488ad`, `db4984c1` (Sonnet
   worker, and this session). `PK13`, G6, `PK15` (`tools/README.md`), `PK21`:
   `9d52835a`..`127f3fef` (Sonnet worker). The ccfleet minors and notes, `DV2`, `PK9`–`PK12`,
   `PK14`, `PK16`, `PK17`, `PK19`, `PK20`: `3c824d40`..`36ec7901` (Opus worker). The changelog
   (`DV5`, `PK15`) and the rest of `PK15` land with this close." Note that this commit order is
   by worker, not by time: `9d52835a`..`127f3fef` interleaves with the skills commits in time.
4. **The re-run lines, as the brief-writer ran them** at `2068884e`, 2026-11-25 from about 19:20
   UTC, from the places the brief names: `merge-base --is-ancestor 77fc8f42 HEAD` exit 0;
   `mandoc -T lint -W style` exit 0, no output; `ccfleet --help` exit 0; the reference queue's
   `--help` exit 0; `modelguard </dev/null` exit 0; `pointerscan --selftest` "ok (0 failure(s))"
   exit 0; `coldsweep --selftest` "selftest OK" exit 0. The unit-test lines and the whole-suite
   line: see fact 14.
5. **`pointerscan --root . .` at `2068884e`:** exit 0 (advisory), "22 finding(s) … (6 grammar · 0
   cycle state · 16 queue state)", 919 roadmap files, 1,203 items. Three of the six grammar
   findings are the new "names its delta's commits by citation alone" text, on items `160/1750`,
   `160/1760` and `160/1770`; the `160/1820` pointer itself is not flagged.
6. **The pushed floor.** The `ci.yml` run (named `floor`) on `77fc8f42` completed `cancelled`
   (cancel-in-progress, superseded within two minutes). The first green run whose tree holds the
   delta is on `a033f023` (2026-11-25 13:28 UTC), `success`; `77fc8f42` is its ancestor. That
   workflow runs `python3 -m unittest discover -s tools` and `-s instruments` on Python 3.12.
7. **The brief-writer's synthetic world** (in its own scratchpad, deleted after): two repos with
   no remote, one public and one private; a scratch `CLAUDE_CONFIG_DIR` whose `CLAUDE.md` read
   `# shared instructions`, a blank line, `@private.md`, a blank line, `plain shared line`, and a
   `private.md` holding one invented private name; `instructions_guard` `refuse`; the reference
   queue on a one-review state; `claude_bin` a stand-in shell script that recorded argv, copied
   the `--settings` and `--append-system-prompt-file` files, and printed a JSON result with the
   session id, `"REPO: x\nRESULT: DONE"` and a `modelUsage` of one invented model name.
8. **What `check` printed in that world:** exit 0; a `NO GRANT` line; a `GRANT` line ("Left out:
   nothing"); a `MANAGED:` line; an `INSTRUCTIONS:` line saying a public repo's session gets
   "each import line withheld (a note that names no path), no imported file, and a deny rule for
   Read of each file listed here. Imports found: 1."; then `INSTRUCTIONS IMPORT: @private.md ->
   <path>: inlined`; no `VISIBILITY` line at all (neither repo has a `github` value or a GitHub
   `origin`, so `check_visibility` skipped both silently); no `KEPT, not classified` line (the
   scratch settings were empty).
9. **The dry drains in that world:** unsealed, exit 0, "DRY not sealed: no launches rehearsed
   (queue next refused: refused: no ranking is sealed)", then "DRAIN EXIT: not sealed: no
   launches rehearsed". After `seal --by run-A` (exit 0): the same command as `run-A` printed
   "DRY rehearsed launch: pubrepo 100/010 docs/reviews/brief.md" and "DRAIN EXIT: queue empty",
   exit 0, and left `logs/pass-pubrepo-100-010-<HHMMSS>.out` under `kit_dir`. As `run-B`: exit
   0, "not sealed … the sealed ranking is run run-A's, not run-B's". `seal --by unknown`: exit 1,
   "refused: `unknown` is no run's id".
10. **What the stand-in was handed** by `run <public repo>` (real launch of the stand-in, exit 0,
    `END … rc=0 result=DONE … models=stub-model-a`): an instructions file headed `# The
    operator's user-level instructions` with no path, the sentence "it is passed here with its
    @-imports withheld", the shared text, and the import line replaced by `<!-- ccfleet: an
    @-import line withheld from this session -->`; the private name absent; a settings file
    whose `permissions` were `{'deny': ['Read(//<scratch path>/cfg/private.md)']}` (a double
    slash, then the absolute path). By `run <private repo>`: the header names the file's path,
    the import is inlined between `<!-- ccfleet: @private.md inlined from <path> -->` and `<!--
    ccfleet: end of <path> -->`, the private name present, and no `permissions` key. Copy names
    were `<session>.<launcher pid>.json` and `<session>.<launcher pid>-user-instructions.md`;
    neither copy remained in `kit_dir/settings/` after the launcher exited.
11. **What the runs left in `kit_dir`:** `children.tsv`, `driver.pid`, `driver.log`; for each run
    `logs/<repo>-<HHMM>-<YYYYMMDDTHHMMSS>.json`, a `.json.err` and a `.json.end` holding the `END`
    line; `results/<day>/<repo>.md`; the dry drain's `pass-*.out`. No `sessions/` record remained.
12. **The `dry-run` of `run <public repo>`** printed the argv it would launch: `nice -n 5
    <stand-in> -p --session-id <id> --setting-sources project,local --settings <copy>.json
    --append-system-prompt-file <copy>-user-instructions.md --model <model> --output-format json
    <prompt> < /dev/null`, and an `END … result=DRY` line naming a log under `logs/` with the new
    date-and-seconds name.
13. **A live observation outside the synthetic world.** The brief-writer's own session was
    launched by `ccfleet run` into this public repo from the operator's real config. Its system
    prompt carried the user-level instructions under the header "The operator's user-level
    instructions" with no path, the sentence "ccfleet loads no user-level settings, so Claude Code
    does not load this file itself; it is passed here with its @-imports withheld, and binds as
    it would have", and a `<!-- ccfleet: an @-import line withheld from this session -->` line
    where the import had been. The same session also received the harness's per-project memory
    index, which names private repos and estate facts; `ccfleet` did not hand it that, and the
    brief-writer did not test what else the session could read.
14. **The unit-test and whole-suite lines**, run by the brief-writer at `2068884e`, 2026-11-25
    UTC, under `nice -n 15`, one at a time, from the places the brief names: from `instruments/`,
    `test_ccfleet` on 3.14 "Ran 152 tests in 471.494s / OK" exit 0, and on `/usr/bin/python3`
    (3.9) "Ran 152 tests in 341.761s / OK" exit 0. From `tools/`, each on 3.14 then 3.9:
    `test_modelguard` 13 tests OK and 13 OK; `test_pointerscan` 61 OK and 61 OK;
    `test_subject_skills` 37 OK and 37 OK; `test_session_close_single_source` 17 OK and 17 OK;
    all exit 0. The script ended at 19:34:24 UTC. **The whole `tools` suite did not finish:**
    started 19:34:35 UTC with the 15-minute load about 10.4 on 12 cores, it was stopped by the
    brief-writer's one-hour background limit, with the load having climbed to 58 (one-minute) /
    28 (five-minute) from other sessions. It printed no result (`-q` reports failures only at the
    end), so it proves nothing either way. It was not restarted, because at 20:34 UTC the
    15-minute load was 17, over the brief's own gate for that line. The pushed floor for this
    delta is the `ci.yml` run on `a033f023` (fact 6), which ran the whole `tools` and
    `instruments` suites on 3.12, `success`. The authors' full-suite claim (fact 2) is therefore
    re-run by no one but that CI run so far.
