# Cold re-check — the `DP` fixes to `ccfleet`, the reference queue, `modelguard`, `pointerscan`, `REVIEW.md` and the review, work and fleet skills (`160/1870`)

**Board:** `docs/roadmap/160-doctrine-review-owed/1870-rule-4-cold-pass-queued-dp-fixes.md`
**Status:** RETIRED 2026-11-27, not run — released by the principal (board 460/040; his
typed answer "Release it as per your recommended option - but to clarify we now have a
better definition than just "are there any major findings"", recorded on `160/1870`)
**Status:** BRIEF ONLY, 2026-11-26 UTC. Approved, queued for the weekly drain that starts
2026-11-29 23:00 UTC, where it runs among the drain's other passes and gates nothing. Written by
headless session `664efda7` (`atelier-fc`, Opus 5.5), pinned at `40f96c01` (`origin/main` when
written). Not yet run.
**Approval:** exactly one Fable re-check pass over the `210/630` and `210/640` fixes, plus its
Opus brief, by a fresh session that wrote none of them. The principal's pick, 2026-11-26 ~03:20
UTC, recorded on `160/1870` (an answer, not a ruling), verbatim: *"Before the drain
(Recommended)"*; the option text he picked: *"One Fable review this week, by a fresh session, <!-- datescan:allow: the principal's picked option text, quoted verbatim -->
before Monday 12:00 NZDT. Benefit: keeps your 24 Nov rule that new drain code is reviewed before a
drain uses it; these fixes change how a paid review's verdict is read. Risk: spends weekly Fable
budget now, and if it finds a major problem, Monday falls back to the old /fable-drain."* Then,
2026-11-26 ~08:45 UTC, asked when it runs, his typed answer, verbatim: *"run it as part of the
drain"*. It does not lift the general Fable hold: this pass and nothing else.

**Pass type:** a rule-4 cold re-check per `docs/method/REVIEW.md`: code, design and doctrine.
The review skills, their prompt templates, the work and fleet skills' prompts, `REVIEW.md` itself,
the hook that denies tool calls and the scanner that polices review pointers are doctrine by
function (rule 3); the instrument that runs them and its reference queue are reviewed with them as
one commitment. Two halves: the delta cold, on its own terms (act 1); then each of `DP1`–`DP21`,
and the `DP17` leftover `210/640`, against its fix (act 2, *Process* below).
**Tier:** Fable, the principal-named review tier, checked at selection by whoever takes the pass.
A session that cannot run on it stops (rule 4).
**When:** inside the 2026-11-29 drain, among its other passes. It gates nothing: on the
principal's ruling recorded on `210/630` (quoted below) the drain already runs on this code, so
the verdict is read for its findings, not as a gate.
**Size of this pass:** large. 15 commits with content on the delta paths, plus four merges (one
of which carries 92 lines of its own conflict resolution), about 2,080 lines added and 290 removed
on 26 files. At the pin: `instruments/ccfleet` 3,372 lines of standard-library Python, its tests
2,891 lines plus a new 271-line `test_ccfleet_dp.py`, a 2,336-line manual page, the reference
queue 275 lines, `tools/modelguard.py` 1,014 lines with a 523-line test and a 311-line saved
`--help` fixture, `tools/pointerscan.py` 1,019 lines with a 687-line test, eleven skill files,
`REVIEW.md` and two guard tests. Budget the time.

**What the verdict is for.** These fixes answer the `160/1820` re-check (`DP1`–`DP21`), which
itself re-checked the fixes to two earlier passes over the drain path. The principal has said he
worries the chain is a loop of review and fix *"without proof of actual failures i.e. risks rather
than issues"* (quoted in full below). So, besides the usual verdict, **every finding says which it
is**: *reproduced* (a failure you drove, with the command and its output) or *risk* (the condition
under which it would bite, and what that condition costs to reach). That label is form, not
severity: severity stays yours to set as usual.

**Why it earns a review.** `ccfleet` starts unattended headless Claude Code sessions with the
user's credentials, decides from their output whether a paid review's claim is released and its
worktree removed, hands each session a slice of the user-level instruction file chosen by the
repo's visibility, writes and sweeps per-session settings copies, and now changes what every
session may read and whether it loads the repo's auto memory. `modelguard` sits in front of every
`Agent` and `Bash` call on every session where it is wired. The review prompts are stamped into
every pass a drain runs, and `REVIEW.md` rule 4 is the rule every rule-4 pass is held to. The worst
failures:

- **Paid review work lost, run twice, misread or mis-costed.** A verdict read from the wrong line,
  or a clean pass read as no verdict and kept; a drift counter that lets a run of bad ends go on
  spending; a fold let past the budget reset when no pass started in its worktree, or refused when
  one did; a seal left standing after a drain is stopped, or ended under a live one; a dry drain
  that reads a broken queue as merely unsealed, or a sealed one as broken.
- **An unplanned paid pass.** A queue `take` or `next` that offers a review the seal did not route
  to the asking route, or a session draining a brief it wrote.
- **A private fact in a public session.** The imported part of the user-level file, its path, the
  per-session copies on disk, the session records, the repo's auto memory, or any other channel the
  harness opens, reaching a public repo's session; or a record a pass leaves in a public repo.
- **A false allow or a false deny from the hook.** A launch with no model that `modelguard` now
  passes, or an ordinary command it now refuses on every session.
- **A skill or rule that stamps a wrong instruction** into every adopter's sessions, or a guard that
  reds the floor on a good change or stays green on a bad one: the widest blast radius in the
  operating model (rule 4).

## Spawn provenance

- **Authors of the work under review:** principal-opened session `5e236e34` (`atelier-cd`, Opus
  5.5, opened by `/atelier:work run`) and the four worker subagents it started (`mg`, `cfa`, `cfb`,
  `sk`, each Opus), which wrote the fixes; `5e236e34` itself wrote the merges, the changelog entry
  and the `210/640` fix. Found from the board items' text and the commits' subjects and timing; no
  delta commit's message body was read.
- **Who reviewed the work these fixes answer:** the `160/1820` pass, one Fable reviewer under
  off-tier orchestrator `01c055e5`; its brief was written by headless session `43d5be30`.
- **Who wrote this brief:** headless session `664efda7` (`atelier-fc`, Opus 5.5), started for this
  brief alone by principal-opened session `a2aeebc8` (`atelier-51`, Opus 5.5) at the principal's
  pick (his option text: one headless Opus brief-writer in this repo, which wrote none of the
  fixes). Neither session authored, started or instructed any part of the delta. **Off-tier for
  review, disclosed: the brief-writer forms no finding and writes no severity**, ran no review,
  used no Fable model, and stops after writing. It will not start the pass.
- **Who orchestrates the pass:** the drain's orchestrator for this item, a session `ccfleet` starts
  with `skills/review/orchestrator-prompt.md`, which spawns one Fable reviewer. If it is off-tier, it
  may hold the context partition, release the held-back sibling after act 1 is committed, and commit
  the records, only because it **forms no finding and writes no severity**, and only with that
  arrangement disclosed in the claim, the pointer and the verdict, its spawn prompt, barred-set
  choice and release message in the verdict's provenance (rule 4). Weigh that arrangement as part of
  V7.
- **Barred from running or orchestrating this pass:** `5e236e34` and its four workers (the
  authors); `664efda7` (whoever writes a brief does not run it); and everything any of them started
  or instructed. `a2aeebc8`, which started this brief-writer, wrote no part of the delta or of
  this brief.
- **Contact, disclosed (rule 4).** The brief-writer's only instruction came from `a2aeebc8`: a
  prompt stamped from `skills/fleet/brief-prompt.md` (**a delta file**: its final-output line is
  one of the `DP2` changes) carrying the item, the approval, the method, the landing steps, where
  the held-back sibling goes, the final-output shape, and a note naming the barred sessions, the
  previous re-check's brief as the model of form, the prefix rule, that the item is approved and
  queued for the drain, and that the delta is exactly the one the item names. No author session
  contacted the brief-writer.
- **Who reviews:** a fresh Fable session spawned for this pass alone, by a session that passes rule
  4's criterion.
- ⚠️ **Brief-writer's exposure, disclosed** (author-account and verdict material met before
  writing): its launch prompt (above); item `160/1870` whole (it quotes the principal's words and
  names the delta); items `210/630` and `210/640` whole (**they carry the authors' account of every
  fix**, the departures from the counsel and their test results); items `210/650` and `210/660`
  whole (the `DP1` and `DP18` leftovers, with the principal's answers and the authors' account of
  what was not built); the first 60 lines of `460/020` (the principal's words on the review-fix loop,
  and a session's proposal); the board hunks of the claim, brief, verdict and queuing commits of
  `160/1820` (`2068884e`, `8a591e0a`, `9e6712b4`, `9ff0e88c`, `2f64d49a`), **which summarise that
  verdict and its counsel**; the `160/1820` brief down to its first verdict divider, **plus that
  file's heading lines, which name each `DP` finding's title and severity**; `cclive`'s session
  titles; `skills/review/brief.md` whole; and, as a model of form for its own session file, the
  first 40 lines of the `160/1820` orchestrator's session file
  (`docs/sessions/2026-11-25-1913-dp-recheck-of-dv-and-pk-fixes.md`), **which also summarise that
  verdict**. It did not read the `160/1820` verdict's body or the session file the delta adds. The delta was read as `git diff` over the paths, the
  combined diffs of the four merges, and subjects and stats, never a delta commit's body. Its
  harness also loaded user-level and repo instruction files and a per-project memory index, which
  hold private context this brief does not carry. Everything evaluative it formed is in the
  held-back sibling.

## The acceptance test

Judge the work against what it claims (its docstrings, `--help`, manual, reference queue, skills,
prompts, README entries, comments, tests and changelog) and against the doctrine it must keep:

- **The principal's words.** On `210/630`, his pick 2026-11-25 ~21:45 UTC (an answer, not a
  ruling), verbatim: *"Fix all now, before Monday"*, option text *"Fix them this week. Benefit: <!-- datescan:allow: the principal's picked option text, quoted verbatim -->
  Monday runs on tighter code. Risk: the fixes change the drain's code after its review, so Monday
  falls back to the old /fable-drain unless another Fable re-check is run and comes back clean in
  time, which is more Fable budget this week."* Then, recorded on `210/630` as his ruling, in his <!-- datescan:allow: the principal's picked option text, quoted verbatim -->
  own words, verbatim: *"Given the low severity of the findings I am ruling that * This code is
  ready to use for the drain so we can continue to switch over to it * That we will fix the findings
  we know about * If those fixes cause work that then requires another review we can decide if that
  review is run in the interim or waits until the next drain, but I wont decide that until we have
  completed the fixes"*.
- **His answers on the three leftovers** (2026-11-26 ~03:20 UTC, each an answer, not a ruling),
  which a fix that departs from the counsel is judged against:
  - `DP17` → `210/640`, verbatim: *"(2) This needs to be fixed."* The delta's `b3e17296` answers it.
  - `DP1` → `210/650`, verbatim: *"With (1) I'm ok with these commands and I understand that they
    carry a risk of data loss etc if the wrong commands are used. If there are ways to do this in a
    way that is measurably safer whilst still be effective (i.e. the job gets done well) then I am
    interested in making those changes. But I am not blocking these kinds of commands if there is
    not a better option."* `210/650` is open and is not part of this delta.
  - `DP18` → `210/660`, typed in place of the options, verbatim: *"Put it on the board to work on
    as a low priority until it is evidenced as an issue"*. `210/660` is open and is not part of this
    delta.
- **His concern on this chain**, 2026-11-26 ~08:45 UTC (recorded on `160/1870`), verbatim: *"I have
  already ruled that we are not waiting for this review to complete before we use the code at the
  next drain. However I have also approved a review, but I worry that we are stuck in a loop of
  review - fix --review -- fix without proof of actual failures i.e. risks rather than issues"*.
  The rule for when a finding is fixed was not answered; the findings go to him as before. Hence the
  *reproduced* / *risk* label above.
- **The rules the drain enforces on others.** `REVIEW.md` rule 1 (the split and the context
  partition), rule 2 (barred reading), rule 4 (spawn criterion, tier at selection, the off-tier
  orchestrator's two conditions, and the new placeholder sentence), *The lifecycle* (method
  record); `CONCURRENCY.md` § *Orchestrated queue runs*; `ECONOMICS.md` (tier set by risk).
- **The public-repo rule.** `docs/PERSONAL-DATA.md` and the repo-craft purpose rule: a generic tool
  in a public repo carries no estate's names, and its example config and reference queue are
  fictional.
- **The earlier verdict**, in act 2 only: `docs/reviews/2026-11-25-1920-dv-pk-fixes-recheck-cold.md`
  (`DP1`–`DP21`), barred until your act 1 is committed (rule 2). This brief neither quotes nor
  summarises it. The delta's own comments, tests and changelog cite `DP` numbers; reading the delta
  is never barred, but do not open the verdict to learn what a number means.

## What the work is

The pointer names its delta as every commit on `main` after `c0f6501b` up to and including the
commit that closes `210/640`, on a path list. That commit is `b3e17296`. In UTC order, 2026-11-26,
the commits with content on the delta paths:

- **`pointerscan` and the skills (worker `sk`):** `9fc276f9` (02:04) pointerscan matches the
  citing family; count only hashes bound as the delta · `835e9b38` (02:05) tell every prompt
  ccfleet reads what its reader needs · `a87d35cb` (02:07) review run says who passes the route,
  where the verdict is read, and reads `models=` · `0d080b99` (02:08) the fold's run-twice check
  matches its heading as a heading line · `6b734631` (02:09) quote every orchestrator message with
  path placeholders in a public repo · `73edeb34` (02:10) the typed-words guard in every skill that
  takes the principal's words. Merged by `0a6a6911` (02:14).
- **`ccfleet` privacy and the reference queue (worker `cfb`):** `3244ca7f` (02:14) reference
  queue's take keeps the route, fit and writer rule · `b9d094a1` (02:15) deny the kit folders,
  switch auto memory off, withhold every import. Merged by `02ad154e` (02:15).
- **`modelguard` (worker `mg`):** `a72a84f8` (02:17) restore the tmux, print-call denials and drop
  new false denies · `2e1a6b87` (02:18) the long-flag table is the saved v2.1.302 help, held by a
  test. Merged by `8c7adf87` (02:19).
- **`ccfleet` verdict reader and lifecycle (worker `cfa`):** `b296f17e` (02:19) read drifted
  verdicts where safe; count out-of-shape ends apart · `54621c8b` (02:20) tie a fold's reset pass to
  its own worktree; end the seal on SIGTERM · `acea648e` (02:21) name a route-less `queue.next` in
  check; date the drain's `.out` files. Merged by **`9e04ffc8` (02:27), which carries its own
  conflict resolution** in `instruments/ccfleet`, its manual and its tests (the authoring session
  joined the two `ccfleet` workers there): no worker commit holds those lines.
- **The landing:** `9bad3944` (02:27) the changelog entry, and a correction to an earlier entry.
- **`210/640`:** `b3e17296` (03:42) a queue's not-sealed refusal is exit 3, so a dry drain tells it
  from a failure. Its board hunks (`160/1870`, `210/640`, the index) are barred until act 2.

Four commits in the range touch only the board or the session log, with no content on the delta
paths: `0bbd5ad4`, `24868e07`, `1940fa4d`, `7e94e74f`. They are barred until act 2 (below).

Delta paths, read at your HEAD and commit by commit: `instruments/ccfleet`,
`instruments/test_ccfleet.py`, `instruments/test_ccfleet_dp.py`, `instruments/man/ccfleet.1`,
`instruments/fixtures/review_queue_reference.py`, `tools/modelguard.py`, `tools/test_modelguard.py`,
`tools/fixtures/claude-help-2.1.302.txt`, `tools/README.md`, `tools/pointerscan.py`,
`tools/test_pointerscan.py`, `tools/test_subject_skills.py`, `tools/test_work_run_single_source.py`,
`skills/fleet/{adopt,brief,task,worker}-prompt.md`,
`skills/review/{fold-prompt,orchestrator-prompt,plan,resume-prompt,run}.md`,
`skills/work/{plan,run}.md`, `docs/method/REVIEW.md`, `CHANGELOG.md` (the two entries dated
2026-11-26, and the one corrected line in the `PK` entry below them).
`instruments/ccfleet.example.json` and `instruments/README.md` are not delta files: no commit in
the range touches them, but the delta's text refers to the example.

First confirm your tree holds the whole delta, then read each commit body-free:

```
git merge-base --is-ancestor b3e17296 HEAD; echo "exit=$?"
python3 tools/coldsweep.py --root . --commit b296f17e --path instruments --path tools \
  --path skills --path docs/method/REVIEW.md --path CHANGELOG.md
```

Repeat the `--commit` line for each of the other 14 content commits. A `--path` that matches
nothing in a commit prints a note and still exits 0. With no `--path`, `--commit` leaves the board
store out; always pass `--path` here. **For the merges, `coldsweep --commit` shows the diff against
the first parent** (the whole side branch, which you read commit by commit anyway), not the
resolution. Read each merge's own lines with the combined diff, whose empty `--format=` prints no
subject and no body:

```
git show --cc --format= 9e04ffc8 -- instruments
git show --cc --format= 0a6a6911; git show --cc --format= 02ad154e; git show --cc --format= 8c7adf87
```

The first prints about 92 lines; the other three print nothing. Plain `git show` with its default
format is barred: it prints the message body before the diff, and reading is atomic (rule 1).
`git diff c0f6501b b3e17296 -- <the paths above>` gives the whole delta at once, body-free.

**Commits after the delta on its paths.** At the pin there are none:

```
git log --oneline b3e17296..HEAD -- instruments/ccfleet instruments/test_ccfleet.py \
  instruments/test_ccfleet_dp.py instruments/man/ccfleet.1 instruments/fixtures \
  instruments/ccfleet.example.json instruments/README.md tools/modelguard.py \
  tools/test_modelguard.py tools/fixtures tools/README.md tools/pointerscan.py \
  tools/test_pointerscan.py tools/test_subject_skills.py tools/test_work_run_single_source.py \
  skills docs/method/REVIEW.md CHANGELOG.md
```

It was empty at `40f96c01`. A later commit that touches only another tool's entry in
`CHANGELOG.md` or the READMEs is out of scope except where it changes, undoes or contradicts a line
the delta wrote. Any other commit on these paths means the delta moved: judge each fix as it stands
at your HEAD, attribute every line to the commit that wrote it (`git blame`, `git log -L`), and say
in your scope line which later commits you met. Pin your HEAD in the verdict.

**This pass runs inside a drain driven by the code under review.** The orchestrator that spawns
you was started by the delta's `ccfleet` with the delta's `orchestrator-prompt.md`, and its final
output will be read by the delta's verdict reader. You may record what you observe of your own run
as read-only evidence, never as the proof of a claim you have not re-driven, and never change how
the drain runs.

**Machine-local surfaces no other review will catch** (read-only; report them in public-safe
terms, never a home path or a private name). Each was read off the machine when this brief was
written:

- The user-level settings wire `modelguard` as a `PreToolUse` hook on `Agent|Task|Bash`, run as
  `/usr/bin/python3 -I <the primary checkout>/tools/modelguard.py`. That interpreter is Python
  3.9.6; the `python3` on `PATH` is 3.14.6. The primary checkout was at `89603481`, clean, and holds
  the delta, so **the hook in front of your own Bash calls runs the delta's `modelguard`**. Feed
  `modelguard` its probes from files (`python3 tools/modelguard.py < probe.json`), never as an
  inline command that names the binary, or the live hook judges your probe before the copy under
  review does.
- `ccfleet` on `PATH` is a link to the primary checkout's `instruments/ccfleet`; never run it by
  bare name.
- The atelier plugin's marketplace is a directory source at the primary checkout. The installed
  plugins record names a cache folder from 2026-10-18 that has no `skills/review/run.md`, yet this
  session's skill list offered `/atelier:review run`: observed, not traced, so the skills a session
  loads appear to be the primary checkout's.
- The installed Claude Code CLI reports version 2.1.302, a native executable (`strings` reads it,
  read-only). Its `claude --help` output was byte-identical to
  `tools/fixtures/claude-help-2.1.302.txt` at 2026-11-26 ~10:45 UTC.
- Sessions on this machine, including one `ccfleet` launches, are handed the harness's
  per-project memory index unless something switches auto memory off; the delta now tries to, for
  public and unknown repos.
- Free disk was about 88 GB; the load average ran between 8.7 and 10.9 on 12 cores, so `gate` may
  answer "hold" for reasons unrelated to the code.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the authors' claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1); these are a floor, never a fence.

**`ccfleet`: reading a verdict (`b296f17e`, `9e04ffc8`; `shaped_results`, `result_word`,
`result_line`, the drain loop)**

1. "A line that is only a code fence (```) is not counted as the last line, so a report fenced
   whole still ends on its RESULT. When the text holds no other RESULT line, blank lines may part
   the RESULT line from its ITEM: line, and the fleet block may hold blank lines … since with one
   RESULT line in the text there is nothing it could be mistaken for."
2. "A clean word … stands only when no other RESULT line in the text names a word that is not
   clean: a quoted, well-shaped DONE never outranks the session's own FAILED that drifted out of the
   shape, and a quoted stop word after a shaped DONE gives no verdict rather than halting a drain. A
   word in `stops` on a RESULT line out of the shape is kept only when no shaped verdict stands at
   all."
3. Every `END` line (pass, fold, resume, dry) carries `review_model=` ("the value its prompt was
   filled with when the prompt names {REVIEW_MODEL}, else -") and `result_line=` (`in-shape`,
   `out-of-shape` or `none`).
4. A drain reads an `UNKNOWN` whose `END` says `result_line=out-of-shape` as "a drifted report, not
   a spent budget": counted apart, "not as a bad end", claim and worktree kept for a resume; the
   drain's last line says how many.

**`ccfleet`: the fold, the seal and the queue (`54621c8b`, `acea648e`, `b3e17296`)**

5. "A fold passes the reset only for a pass ccfleet saw start in the fold's own worktree": the
   session log named for the worktree's folder, a session record naming it, a `START` line naming
   it, or "the pass's result file, written after this worktree was made"; "a pass on the same item
   in an earlier worktree, however long ago, does not count."
6. "A SIGTERM or SIGHUP ends the driver through its `finally`, so the queue still hears the run end
   (`queue.unseal`) and its lists are cleared; only a SIGKILL skips it. Its passes are detached and
   run on." A SIGHUP that `nohup` set to ignore stays ignored.
7. "The queue's 'not sealed' refusal is its own exit code, 3; any other failure of `next`, or a 3
   after a pick, is a queue error, exit 1"; a real drain is unchanged. The changelog's adopter
   action: "Your queue's `ranked`, `next` and `take` must refuse with exit 3 while this run holds no
   seal."
8. `check` prints `QUEUE ROUTE` when `queue.next` names no route; "ccfleet passes no route itself".
9. A drain's `.out` names carry the date and second; "readers glob `pass-*.out`, so the time-only
   names an earlier ccfleet wrote are still read."

**`ccfleet`: what a session is handed and may read (`b9d094a1`, `9e04ffc8`)**

10. "Every session's settings deny Read of `<kit_dir>/settings/` and `<kit_dir>/sessions/`, by path
    and real path"; "No session reads either: Claude Code reads its own two copies at start, by the
    flags, not by a tool."
11. A public or unknown repo's session has auto memory off, by `autoMemoryEnabled: false` and
    `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in the copy's `env` block, "since the documentation does
    not say the setting is read from `--settings`"; "Not tested against a live session."
12. "Imports led by a number, block quote, heading or task box are handled like a bare import line;
    one inside a sentence is withheld from a public session and denied; `check` counts and
    describes every import."
13. The manual's *THREATS* now states that the deny rule "binds Claude Code's own file tools and the
    shell commands it recognises (`cat`, `head`, `sed`), by its documentation on a best-effort
    basis"; that in a bypass mode "Claude Code's documentation says deny rules hold in every mode";
    and that "None of this is tested here against a live session."

**The reference queue (`3244ca7f`, `b3e17296`)**

14. "`take` makes the checks `next` makes (the route, default local; what the review fits; who
    wrote its brief), so a pass started by hand (`ccfleet pass`) can take only what a drain's `next`
    would offer on that route, in any order."
15. "On every route, a review is offered only where its `fits` lists that route, and never to the
    run that wrote its brief (`briefed_by` is the asking --by)."
16. `ranked`, `next` and `take` refuse with exit 3 before the seal; "every other refusal exits 1".

**`modelguard` (`a72a84f8`, `2e1a6b87`)**

17. "tmux's options end where its command begins, so `tmux new -d sh -c 'claude -p x'` and six
    similar launches are denied again"; `if-shell`'s words are read as shell and tmux commands.
18. "It no longer refuses `screen -r/-x claude`, `tmux new -ds claude`, a later `-c` after an
    echoed substitution, or paths holding the letters past the depth limit"; it now refuses
    `screen -d claude` and, past the depth limit, a read-only path to the binary (both named in its
    docstring as accepted false positives); "a bare `claude` last after an unknown runner
    (`script -q /dev/null claude`, in tmux or not)" passes, stated as a cost.
19. "The long-flag table covers the whole saved `claude --help` (v2.1.302), held by a test."
20. "A print-named call that is renamed, or is a method of another object, no longer exempts its
    text."

**`pointerscan` (`9fc276f9`)**

21. It flags "commits citing", "commits that cite", "commits naming" "and the rest of that
    family"; "a bare present-tense verb … selects none, so it is not matched"; only a commit range,
    or "a list of two or more hashes in a sentence that names the delta or carries the citation",
    silences it.

**The skills, the prompts and `REVIEW.md` (`835e9b38`, `a87d35cb`, `0d080b99`, `6b734631`,
`73edeb34`, `b3e17296`)**

22. Every prompt `ccfleet` reads now says: "no code fence around it, no blank line inside it,
    nothing after its `RESULT:` line" (the fleet prompts), or `RESULT:` "directly above the
    `ITEM:` line" (the review prompts).
23. `run.md`: the config's `queue.next` passes the route; a pass "that names no model of the review
    tier this drain set" on its `models=` "ran no reviewer on that tier, whatever its verdict says:
    mark it off-tier, do not trust its verdict, and put it to the principal"; a resume's and a
    fold's `models=` are read with the stated differences; a dry drain's refusal is exit 3.
24. The fold's run-twice check matches "a line that starts with `#` marks … whatever follows those
    words"; "the same words anywhere else … are not a fold".
25. In a public repo "the spawn prompt, the release message and any resume message are quoted with
    each absolute path replaced by a named placeholder", now in `REVIEW.md` rule 4, the orchestrator
    prompt and the resume prompt.
26. The typed-words guard ("Where he did not type the command (a model reached this skill on a
    casual phrase), there are no typed words … Never take it from this skill call's own arguments")
    now stands in `review/plan.md`, `work/plan.md` and `work/run.md`.

**The guards' tests**

27. "Seven mutants the suite missed are now killed (`DP5`)"; the authors' record says each fix's
    test was seen failing on the unfixed code or a hand-applied mutant first.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:**

- Any estate's private `ccfleet` config, rulings file, queue tool, lane records and run results,
  the real user-level instruction file's content, and the real config directory. Grounds: private
  by design, this repo is public, and the delta's claim is that the code, the reference queue and
  the skills are generic. Judge the contract through the example config, the reference queue and a
  synthetic world (below). Whether an adopter's private queue has made the exit-3 change is not
  yours to check; whether the contract change is stated where an adopter will meet it is.
- The two open leftovers' future work (`210/650`, `210/660`): judge only whether the delta states
  its own remaining gap truly, against the principal's answers quoted above.
- Code the delta did not change, except as far as a fix builds on it or changes what it does. A
  defect you meet in an older line is recorded, not hunted.
- The drain this pass runs in: observe, never steer.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   For each `DP` finding the fixes answer, is the fix aimed at the class or at the instance the pass
   reproduced? Is loosening the verdict reader (blank lines, fences, a lone RESULT line) while
   tightening it elsewhere (a clean word overruled by any unclean RESULT line) a sound trade for a
   reader whose output releases a paid claim? Is a drift counter that never counts toward the
   three-failures stop bounded? Is a worktree's folder name, a directory's modification time and a
   session record a sound basis for "a pass started here"? Are permission deny rules, plus a
   setting and an environment variable the harness may or may not honour from `--settings`, the
   right control for keeping private context out of public sessions, given every channel a session
   has? And the re-check's own question: does each fix close its class, or move the risk somewhere
   the fix did not look?
2. **Correctness & quality.** Re-drive the claims above by probe, not by reading. Drive the verdict
   reader with final outputs of both prompt shapes: fenced, spaced, with quoted RESULT lines before
   and after, from a reviewed repo's text, with stop words, through the transcript fallback; and
   check that `result=` and `result_line=` on one `END` line never disagree. Trace a pass's life
   through each interruption point (before the claim, after the claim and before `START`,
   mid-session by `SIGTERM`, `SIGHUP`, `SIGKILL`, a usage cap, a reboot, after the session and
   before the release, during a fold or a resume run twice) through the new fold evidence, the
   signal handler and the seal. Drive the reference queue's `take`, `next`, `fits` and `briefed_by`
   on every route. Drive `modelguard` with the shapes its docstring names and those it does not
   (tmux and screen subcommands that type or run text, `if-shell`, clustered options, substitutions,
   renamed print calls, deep nesting). Record each overclaim against the text that makes it,
   including any claim no test pins.
3. **Completeness / harvest.** Every surface that states the verdict rule, the drift count, the
   `END` fields, the fold evidence, the signal behaviour, the not-sealed code, the route rule, the
   deny rules, auto memory, the import handling, the placeholder rule and the typed-words guard
   agrees: docstring, `--help`, manual, reference queue, skills, prompts, `REVIEW.md`, both
   READMEs, changelog (V3, V5). One home per fact (V4). Find tests that would stay green on a broken
   delta by mutating scratch copies. What the fixes should have touched and did not, given what
   they claim to fix, including the merge resolution no worker wrote.
4. **Security & privacy**, mandatory. Design altitude: what an unattended public-repo session can
   still receive or reach of the user-level files after the fix (the appended text, the imported
   files, their paths, the per-session copies and records on disk, every other folder under
   `kit_dir` and their contents, the repo's auto memory, any other channel the harness opens); what
   the sweep may delete; what a hostile repo's settings, instruction file, pull request or reviewed
   text can make a session or the verdict reader do. Code altitude: the likely vectors for the
   class, checked against an open catalogue (OWASP ASVS or the domain's equivalent), not recalled:
   values from the config, the queue's output, the instruction file's import lines and the forge
   flowing into paths, argv, permission rules, prompts and git commands; for `modelguard`, every way
   a launch with no model can pass, and every ordinary command it now refuses. `/security-review`
   reads the session's pending diff, not this delta: aim it at the code only from a scratch clone
   holding the diff, never with this brief dirty, else discharge it by grounds; weigh a clean pass
   over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once, on 2026-11-26 UTC between 10:40
and the brief's landing, at `40f96c01`, from the places named; its results are held in the
sibling. Read exit codes explicitly. Check `uptime` first; one heavy process at a time, under
`nice -n 15`, in the foreground with a long timeout (the `ccfleet` suite takes several minutes per
interpreter on a loaded machine). Other sessions share this machine, and in the drain other passes
run beside you.

From the worktree root:

```
git merge-base --is-ancestor b3e17296 HEAD; echo "exit=$?"
mandoc -T lint -W style instruments/man/ccfleet.1; echo "exit=$?"
python3 instruments/ccfleet --help >/dev/null; echo "exit=$?"
python3 instruments/fixtures/review_queue_reference.py --help >/dev/null; echo "exit=$?"
python3 tools/modelguard.py </dev/null; echo "exit=$?"
python3 tools/pointerscan.py --selftest; echo "exit=$?"
python3 tools/pointerscan.py --root . .; echo "exit=$?"
python3 tools/coldsweep.py --selftest; echo "exit=$?"
```

From `instruments/` (the tests load their subjects by path; run on both interpreters, since the
manual says 3.9 and 3.14 are tested):

```
nice -n 15 python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_ccfleet_dp; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_ccfleet_dp; echo "exit=$?"
```

From `tools/` (`/usr/bin/python3` is the interpreter the user-level hook runs under):

```
nice -n 15 python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_pointerscan; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_subject_skills; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_work_run_single_source; echo "exit=$?"
```

and the same four lines with `/usr/bin/python3` in place of `python3`.

The whole `tools` suite, once, only while the 15-minute load average is under the core count (from
`tools/`): `nice -n 15 python3 -m unittest discover -q; echo "exit=$?"`. The authors' record gives
a whole-suite count at the landing head; it is barred until act 2, so compare only then. A failure
you judge to be load, not code, is re-run alone and both results recorded.

**The saved help.** From the worktree root, read-only (no model is reached, no sign-in needed):

```
claude --help > <scratch>/help-now.txt; diff -q <scratch>/help-now.txt tools/fixtures/claude-help-2.1.302.txt; echo "exit=$?"
```

**The pushed floor.** The CI run on `b3e17296` itself was cancelled by a newer push
(cancel-in-progress), so it proves nothing; read the first green run whose tree holds the delta
(read-only):

```
gh run list -R mike548141/atelier --commit b3e17296 --json name,status,conclusion
gh run list -R mike548141/atelier --commit 21bf60b2 --json name,status,conclusion
git merge-base --is-ancestor b3e17296 21bf60b2; echo "exit=$?"
```

**Probes to build: a synthetic world.** These are your probes, not re-run lines: **the
brief-writer did not build this world or run these commands**, so the brief states no expected
result beyond what the delta claims. In your scratchpad only, every name invented: two throwaway
git repos with no remote and mainline `main` under a scratch `repos_root`, each holding a dummy
brief; a scratch `CLAUDE_CONFIG_DIR` holding `settings.json` of `{}` and a `CLAUDE.md` that imports
one file by `@` path on a line of its own (and one led by a number, a quote marker, a heading and a
task box) and another inside a sentence, only the imported files naming one invented private name;
a config whose `kit_dir`, `repos_root` and `worktrees_root` are scratch directories,
`stagger_seconds` 0, `gate` open, one repo `public` and one `private`, that private name in
`private_names`, `instructions_guard` `refuse`, a scratch `pass_prompt` using `{ITEM}` `{BRIEF}`
`{REVIEW_LOG}` `{REVIEW_MODEL}`, and a `queue` whose commands call
`instruments/fixtures/review_queue_reference.py` from your worktree in the example config's shape,
`unseal` included, once with `--route local` in `queue.next` and once without; a state file with
routes and reviews that exercise `fits`, `briefed_by`, spill and a review briefed after the seal;
`REVIEW_QUEUE_STATE` and `REVIEW_QUEUE_NOW` set. For `claude_bin`, a **stand-in script** you write:
it records its argv and environment, copies each file passed after `--settings` and
`--append-system-prompt-file` into a capture folder, and prints a canned JSON log (`type` `result`,
`subtype` `success`, the `--session-id` it was given, a `result` text you vary across the verdict
shapes above, a `modelUsage` object). It never runs a model. Name it so its path does not contain
the real binary's name, or the live hook will read your commands as launches. A queue stand-in that
exits 1, 2, 3, 126 and by signal drives the dry drain's reading. Then, with `CLAUDE_CONFIG_DIR`
pointing at the scratch directory throughout, from the worktree root: `check`, `plan`,
`drain --dry-run` before and after the seal and under another `--by`, a real `drain` and a `pass`
against the stand-in, `run` on each repo with a plain template, a stand-in that sleeps and a
signal to the launcher and to the drain driver, a fold before and after the reset in a worktree
`ccfleet` made and in one it did not. Read `<kit_dir>` (`driver.log`, `logs/` with its `.end`
files, `results/`, `settings/`, `sessions/`) and the capture folder: what each session was handed,
what its settings deny, what was left on disk and what was removed.

**Live behaviour.** The claims that rest on real `claude -p` behaviour (whether the harness honours
`autoMemoryEnabled` and an `env` block from a `--settings` file; how it matches a `Read(//<path>/**)`
deny rule, by path or real path, and for which tools and shell commands; whether it follows an `@`
import inside a file given to `--append-system-prompt-file`; the JSON log's `modelUsage` when a
subagent runs on another model; how a session behaves when its launcher or the drain driver is
signalled) rest on a stand-in binary in the tests. **This pass makes no launch of the real CLI that
reaches a model, decided here, before the pass.** Grounds: a synthetic `CLAUDE_CONFIG_DIR` has no
sign-in, so a launch there fails before any model is reached; a launch from the real config
directory would load the operator's private instruction file and credentials into an experimental
session and spend budget beyond the one approval this pass runs under (exactly one Fable pass and
its Opus brief). So each such claim is re-driven read-only instead, and its live half marked NOT
RUN with these grounds:

- `claude --version` and `claude --help` (no model is reached): every flag `ccfleet` passes and
  every long flag `modelguard` lists exists in 2.1.302;
- the installed binary read read-only with `strings` for the handling of `autoMemoryEnabled`,
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY`, an appended file's `@` lines and permission-rule paths, stated
  as reading the binary, not as a live result;
- the harness's published documentation for permission-rule path syntax and the tools a `Read`
  rule binds, settings precedence and `--settings`, auto memory, and memory imports;
- the stand-in binary above for what `ccfleet` hands a session, which is what `ccfleet` controls.

Never run `ccfleet` against a real repo, never `drive` or `drain` for real, never with a real
config, and never `ccfleet check` against the real config directory (it prints the operator's hooks
and instruction-file path). The brief-writer ran no launch of the real CLI.

## House rules for this run

- **Live systems:** read-only reads as needed; no live writes. A check that needs a write is marked
  NOT RUN, with why. No push beyond the orchestrator's own landing of the records, no write to
  GitHub, no network service changed. `gh repo view` and `gh run list` are reads.
- **Never print a secret** or any personal data. Other sessions' transcripts are not read.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file and your
  review log. Other sessions and other passes are live on this machine: touch nothing outside your
  worktree and scratchpad, and never touch the primary checkout (the hook, the linked `ccfleet` and
  the skills run from it) or the drain's own `kit_dir`. Child repos are read-only and reported by
  count only, never by name or path.
- Never run an installed tool by bare name from `PATH`: use `python3 instruments/ccfleet` or
  `python3 tools/<x>.py` from your worktree.
- This pass is pending while you run it: anything you write to a pointer or a commit subject before
  act 2 names the held-back sibling by count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at about 100 columns; NZ English. This repo
  is PUBLIC: quote no secret, email address, home path, private repo name or estate fact.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it, and says whether it
  is *reproduced* or a *risk*.

**Reviewer's start-up reading:** skip the session-log step of the repo's read order, whatever your
spawn prompt says; the log is on rule 2's barred list. If you met any of it anyway, disclose what.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material is held outside the repo under the rule-1 split and released only after the reviewer's act-1 findings are committed -->

Rule 2 bars until act 2: `docs/sessions/` (the delta adds one session file), every prior verdict in
`docs/reviews/` (the `160/1820` file above included, brief half and all), every item under
`docs/roadmap/160-doctrine-review-owed/` beyond its title, the delta commits' message bodies,
`docs/method/census/`, and beyond their first line:

- `docs/roadmap/210-instruments-open-features/630-fix-ccfleet-modelguard-and-the-review-skills-dp1-dp21.md`
  and `docs/roadmap/210-instruments-open-features/640-a-dry-drain-tells-a-queue-refusal-from-a-failure.md`
  (the intent records; they carry the authors' account of each fix, its departures and its test
  results; the principal's words they hold that bear on this pass are quoted above)
- `docs/roadmap/210-instruments-open-features/650-a-measurably-safer-tmux-rule-for-modelguard.md`
  and `docs/roadmap/210-instruments-open-features/660-ccfleet-loads-a-mid-sentence-import-in-a-private-repo.md`
  (the `DP1` and `DP18` leftovers, with the authors' account of what was not built)
- `docs/roadmap/210-instruments-open-features/620-fix-ccfleet-and-the-review-skills-dv1-dv11-pk1-pk21.md`
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
- `docs/roadmap/460-the-bar-before-a-fable-review-is-ordered-mike-comm/010-diagnose-then-set-a-checkable-bar.md`
- `docs/roadmap/460-the-bar-before-a-fable-review-is-ordered-mike-comm/020-write-the-bar-into-the-review-rules.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/210-a-plan-mode-that-shows-the-drain-before-it-runs.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/240-a-work-plan-mode-for-work-run.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/500-census-slice-4-doctrine-defects.md`

All of these carry an author's account of the work or of its predecessors, and some carry earlier
verdicts' findings or the principal's concern about this chain (quoted above). The board index,
`docs/ROADMAP.md`, lists items by title; read no further in it than a title.

**This brief's held-back sibling is not in the tree.** Whoever orchestrates the pass holds it
outside the repo and every worktree, and releases it to you only after your act 1 is committed; by
count it holds 20 questions and 12 facts. Never look for it in git history, other checkouts,
scratchpads or temporary directories. Run by hand with no orchestrator, you open it yourself, as a
deliberate second act, after act 1 is committed, and disclose when.

The delta's own comments, docstrings, manual, skills, prompts, tests and `CHANGELOG.md` entries
carry the authors' account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/630-fix-ccfleet-modelguard-and-the-review-skills-dp1-dp21.md \
  --also-exclude docs/roadmap/210-instruments-open-features/640-a-dry-drain-tells-a-queue-refusal-from-a-failure.md \
  --also-exclude docs/roadmap/210-instruments-open-features/650-a-measurably-safer-tmux-rule-for-modelguard.md \
  --also-exclude docs/roadmap/210-instruments-open-features/660-ccfleet-loads-a-mid-sentence-import-in-a-private-repo.md \
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
  --also-exclude docs/roadmap/460-the-bar-before-a-fable-review-is-ordered-mike-comm/010-diagnose-then-set-a-checkable-bar.md \
  --also-exclude docs/roadmap/460-the-bar-before-a-fable-review-is-ordered-mike-comm/020-write-the-bar-into-the-review-rules.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/210-a-plan-mode-that-shows-the-drain-before-it-runs.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/240-a-work-plan-mode-for-work-run.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/500-census-slice-4-doctrine-defects.md \
  --also-exclude docs/method/census \
  --also-exclude docs/ROADMAP.md \
  "shaped_results|pass_started|kit_denies|NO_AUTO_MEMORY|queue_broke|QUEUE_NOT_SEALED_RC|print_call|TMUX_SHELL"
```

`--include-barred` only with disclosure in the verdict.

## Process

**Act 1.** Reproduce the floor first; work the lenses, your own assumptions and the re-run list,
over the whole delta as it stands at your HEAD, cold: you have not read the earlier verdict, so
judge the code, prompts and skills on their own terms, not as fixes. Append your verdict below a
`---` divider in THIS file: provenance repeated (how you were spawned, your tier and the model you
find yourself running as, the orchestrator with its spawn prompt, what you read, the UTC day, the
HEAD you pinned), per-lens answers, V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (read body-free
yes/no, findings by id; the merge resolution in `9e04ffc8` as a row of its own), findings with
stable IDs (prefix `DQ`: `DQ1`, `DQ2`, …), severities (MAJOR / MODERATE / minor / note) and the
*reproduced* / *risk* label, an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts and the
MAJOR count first, a re-run ledger, a live-behaviour ledger (each NOT RUN with its grounds), the
method record `REVIEW.md` § *The lifecycle* requires, and a follow-up checklist. Give the paid-drain
path its own line in the per-lens answers. Then STOP: act 1 is committed, unrevised, **before** the
sibling or the earlier verdict is opened. Edit no other file.

**Act 2.** Open the sibling, the earlier verdict and the barred records; screen the delta commits'
bodies. Append `### Reconcile` beneath your verdict, with:

- **The fix ledger, one row for each of `DP1`–`DP21`, and one for `210/640`:** what the earlier
  verdict counselled (by pointer, not restated at length), the commit and file:line that answers it,
  how you re-drove it at your HEAD (the command and its result, or that verdict's own reproduction
  re-run), and its state: *fixed as counselled* · *fixed another way* (and whether that way meets
  the finding) · *partly fixed* · *not fixed* · *regressed*. Reading a fix is not re-driving it (V2).
  Where a fix went beyond or against the counsel, say so and judge it; where the authors' record
  names a departure and the principal answered it (`DP1` and `210/650`, `DP17` and `210/640`, `DP18`
  and `210/660`), judge the fix against his recorded answer, quoted above.
- Per-finding notes on your act-1 findings against the sibling's questions and the authors'
  account; any finding formed at reconcile, marked as such, with a `DQ` id after your last.
- The residual risk, named: act 2 reads the earlier verdict, so the fix ledger is anchored on it by
  design; act 1 is the cold half.
- The overall line restated, MAJOR count first, with how many findings are *reproduced* and how
  many are *risks*.

Never revise act-1 text. Then the orchestrator folds the sibling in below the reconcile.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it. Under the overall verdict, say plainly in
three lines: whether anything you found loses, misreads or mis-costs paid review work, in the drain
this pass ran in or the next; whether `/atelier:review plan` and `/atelier:review run`, with
`ccfleet` as the fixes leave it, are safe to keep running the principal's paid weekly drain from,
and if not, what must change first; and whether anything in the delta can put private context into
a public repo's session. Name `160/1870` in your scope line, and `210/630` and `210/640` as the
items the delta answers to.

---
