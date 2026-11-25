# Cold pass — the RK part-3 fixes to `ccfleet`, `modelguard` and the subject skills (`160/1810`)

**Board:** `docs/roadmap/160-doctrine-review-owed/1810-rule-4-cold-pass-queued-rk-part-3-fixes.md`
**Status:** BRIEF ONLY, 2026-11-25 UTC. Written by headless session `075cdcd9` (`atelier-e0`,
Opus 5.5), pinned at `6ddbead2` (`origin/main` when written). Not yet run.
**Approval:** one Fable pass plus its Opus brief, by a fresh session that wrote none of the fixes.
The principal's pick, 2026-11-25 ~05:40 UTC, recorded on `160/1810` (an answer, not a ruling),
verbatim: *"Approve one pass now"*; the option text he picked: *"One Fable pass on this week's <!-- datescan:allow: the principal's picked option text, quoted verbatim -->
budget, run by a fresh session soon, ahead of the drain. Spends weekly Fable budget now."* It does
not lift the general Fable hold: this pass and nothing else.

**Pass type:** a cold pass per `docs/method/REVIEW.md` rule 4: code, design and doctrine. The
routers' grants, the skills and their prompt templates, the hook that denies tool calls and the
mechanisms table are doctrine by function (rule 3); the instrument that runs them is reviewed with
them as one commitment.
**Tier:** Fable, the principal-named review tier, checked at selection by whoever takes the pass. A
session that cannot run on it stops (rule 4).
**Size of this pass:** large. Seven commits in scope, one read for context. At `6ddbead2`:
`instruments/ccfleet` 2,761 lines of standard-library Python, its tests 2,282 lines (136 tests,
about five minutes per interpreter on a loaded machine), a 1,968-line manual page, a new 207-line
reference queue, `tools/modelguard.py` 735 lines with a 274-line table-driven test, six routers and
their action files, and two guard tests (367 and 192 lines). The seven commits add about 3,000
lines and remove about 330. Budget the time; never thin the pass to fit it (`REVIEW.md`, *Budget
decides how many reviews run and when, never how a review is run*).

**What the verdict decides.** These fixes answer the findings of the pass that reviewed the
`ccfleet` drain, `review plan` and `review run`, and the command form. The principal's weekly drain
is due to move onto `/atelier:review plan` and `/atelier:review run`, driven by `ccfleet`, and
`160/1800` (a separate small pass) covers the drain-path part of the same fixes. So the verdict
must say plainly whether these commands, as part 3 leaves them, are safe to run a paid drain from,
and whether the grants every `/atelier:` command now carries are the narrowest that work.

**Why it earns a review.** `ccfleet` starts unattended headless Claude Code sessions in a worktree
of every repo an estate lists, with the user's credentials, decides from their output whether a
paid review's claim is released and its worktree removed, and now hands each one a slice of the
user-level instruction file chosen by the repo's visibility. `modelguard` sits in front of every
`Agent` and `Bash` call where it is wired, on every session on the machine. The routers' grants
pre-approve commands for every action under a subject. The worst failures:

- **Paid review work lost, silently redone, misread or mis-costed.** A pass cut off by a signal,
  a cap or a reboot whose session, claim, worktree or log cannot be recovered, or that a resume
  takes while the original still runs; a `PARTIAL` or `BLOCKED` read as settled when the work is
  not; a plan's cost figure that counts what it should not, or prices on a basis it does not say.
- **An unplanned paid pass.** A path from `ccfleet` or a skill to a paid launch that no seal
  stands in front of, now that the seal is the adopter's queue's contract and `ccfleet` only
  trusts an exit code.
- **A private fact in a public session.** The user-level instruction file appended to a public
  repo's session, by the import split or around it; the guard's `warn` mode; a settings copy left
  on disk.
- **A false allow or a false deny from the hook.** A launch with no model that `modelguard` now
  passes (the cost its own docstring accepts, and any it does not state); an ordinary command it
  refuses on every session.
- **A grant wider than its use, or too narrow to work.** A router grant that pre-approves a
  command an action never needs, or a needed read it does not grant, in either install shape.
- **A skill that stamps a wrong rule** into every adopter's sessions: the widest blast radius in
  the operating model (rule 4).

## Spawn provenance

- **Authors of the work under review:** session `0ee74059` (`atelier-c3`, Opus 5.5,
  principal-opened by `/atelier:work run`) and the four Opus workers it started, which wrote the
  fixes; `f4360a79` was written by one more Opus worker of the same session. Found from the board
  item's own text and the commits' subjects and timing; no delta commit's message body was read.
- **Who reviewed the work these fixes answer:** session `4a34637a` orchestrated that pass and its
  Fable reviewer formed the verdict; a brief-writer worker of queue run `0b4f93ef` wrote that
  brief, and queue run `9a08702f` widened it.
- **Who wrote this brief:** headless session `075cdcd9` (`atelier-e0`, Opus 5.5), started for this
  brief alone by principal-opened session `14c2530d` (`atelier-e7`, Opus 5.5). Neither authored,
  started or instructed any part of the delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, ran no review, used no Fable model, and stops after
  writing. It will not start the pass.
- **Who orchestrates the pass:** session `14c2530d`, which wrote no part of the delta and no part of
  this brief, spawns one Fable reviewer. As an off-tier orchestrator it may hold the context
  partition and commit the records only if it forms no finding, writes no severity, and is disclosed
  in the claim, the pointer and the verdict, with its spawn prompt, barred-set choice and release
  message in the verdict's provenance (rule 4).
- **Barred from running or orchestrating this pass:** `0ee74059` and every worker it started (the
  authors); `075cdcd9` (whoever writes a brief does not run it); and everything any of them started
  or instructed.
- **Contact, disclosed (rule 4).** The brief-writer's only instruction came from `14c2530d`: the
  item, the method files, the model brief to read to its first divider, the sync and claim steps,
  the prefix rule, where the held-back sibling goes, and the final-output shape. No author session
  contacted the brief-writer.
- **Who reviews:** a fresh Fable session started for this pass alone, by a session that passes rule
  4's criterion.
- ⚠️ **Brief-writer's exposure, disclosed** (author-account material met before writing): its
  launch prompt; item `160/1810` whole and item `210/610` whole (**both carry the authors'
  account**; `210/610` was read to learn whether `f4360a79` has a pass of its own), the first three
  lines of item `160/1800`, and one earlier claim commit's message body (`26a4fe7e`, on `160/1790`,
  read as a model of the claim form); `skills/review/brief.md` whole; `REVIEW.md` from its start
  through § *The lifecycle*; the earlier pass's brief down to its first verdict divider (its scope,
  provenance, claims and questions, so this writer has met that pass's framing, not its findings);
  the delta's subjects, file stats and diffs, read body-free with `coldsweep --commit` and
  `git diff`; a `git log --grep=210/600` that printed hashes only; the docstrings of `modelguard`,
  `ccfleet` and the reference queue at HEAD; the results of the re-run lines below. It opened no
  delta commit's message body and no session record. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the held-back sibling.

## The acceptance test

Judge the work against what it claims (its docstrings, manual, skills, routers, comments, tests and
changelog) and against the doctrine it must keep:

- **The principal's words the delta quotes.** The command form and the menu, as the routers and
  `tools/test_subject_skills.py` quote them verbatim; the plan's commission and its link to
  `review brief`, as `skills/review/plan.md` quotes them; the close's no-drift rule, as
  `skills/session/close.md` quotes it; and his rule on review quality, quoted in `REVIEW.md`
  § *When to review*: *"Quality is more important than cost. If we run out of budget then we will
  resume the work when the budget replenishes"*.
- **The rules the drain enforces on others.** `REVIEW.md` rule 1 (the deferred split and the context
  partition), rule 2 (barred reading), rule 4 (spawn criterion, tier at selection, the off-tier
  orchestrator's two conditions), *The lifecycle* (method record); `CONCURRENCY.md` § *Orchestrated
  queue runs* (where held-back material lives); `ECONOMICS.md` (tier set by risk; the model named on
  purpose).
- **The public-repo rule.** `docs/PERSONAL-DATA.md` and the repo-craft purpose rule: a generic tool
  in a public repo carries no estate's names, and its config example and reference queue are
  fictional.
- **The earlier pass's findings**, in phase 2 only (*Process* below): the item names `RK1`, `RK3`,
  `RK4` and `RK6`–`RK29` as fixed here. That verdict is
  [`2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`](2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md),
  barred until your act 1 is committed (rule 2). This brief neither quotes nor summarises it. The
  delta's own comments cite some `RK` numbers; reading the delta is never barred, but do not open
  the verdict to learn what they mean.

## What the work is

The item's pointer names its delta as "the commits citing `210/600`, on `main`, after `a1cc5f2d`",
on a path list. Read against the history at the pin, that grammar and that list disagree, so this
brief takes in every commit after `a1cc5f2d` that touches the item's paths, and says why for the
three the grammar alone would miss. Treat this scoping as the brief's claim, attackable like any
other.

**The commits whose subjects cite `210/600`:**

- **`4a9318b7`** — `skills: narrow the routers' grants and fix the subject-skill wording (210/600
  part 3)` (2026-11-25)
- **`53203833`** — `ccfleet: close the pass-lifecycle gaps of the 210/600 cold pass` (2026-11-25)
- **`2d8e05e3`** — `review: say the pass lifecycle as ccfleet now runs it (210/600 RK6, RK17,
  RK24)` (2026-11-25)
- **`564a7ca4`** — `ccfleet: state the seal, measure what plan's cost is, guard the instructions
  file (210/600 part 3)` (2026-11-25)

**On the item's paths, landed by the same session inside its claim, with no `210/600` in subject
or message:**

- **`fc922383`** — `modelguard: read a claude after an unknown head only as a launch`
  (2026-11-25). The only commit after `a1cc5f2d` on `tools/modelguard.py` and its test, both on the
  item's path list.
- **`9b4a8f8f`** — `changelog: the rename, the plans, the whole grant and this pass's fixes (RK22)`
  (2026-11-25). `CHANGELOG.md` is on the item's path list.

**After the item was queued, on its paths, with no pass of its own:**

- **`f4360a79`** — `ccfleet: follow the instructions file's imports for private repos only`
  (2026-11-25; board `210/610`, which is closed and queues no review). It rewrites what the
  instructions-file guard added by `564a7ca4` reads, so it is reviewed here as part of that guard.

**Read for context only:** `a1cc5f2d` (`210/600` part 1, the drain-path fixes, under its own pass
`160/1800`). `ccfleet` and the review skills at HEAD carry it, so review them whole as far as part 3
touches them; a defect you meet in `a1cc5f2d`'s own lines is recorded, not hunted.

Delta paths, read at HEAD and commit by commit:

- `instruments/ccfleet`, `instruments/test_ccfleet.py`, `instruments/man/ccfleet.1`,
  `instruments/ccfleet.example.json`, `instruments/fixtures/review_queue_reference.py` (new)
- `tools/modelguard.py`, `tools/test_modelguard.py`
- `skills/` whole as the four commits change it: the six routers' grants, placeholder text and
  menu step; `skills/review/plan.md`, `run.md`, `fold-prompt.md`; `skills/session/close.md` and
  `onramp.md`; `skills/work/plan.md` and `run.md`; `skills/fleet/sweep.md` and its prompt
  templates; the action files that lost a grant line
- `instruments/atelier-menu/SKILL.md` (its grant), `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json`, `docs/method/MECHANISMS.md` (two lines)
- `tools/test_subject_skills.py`, `tools/test_session_close_single_source.py`
- `CHANGELOG.md`: the entries `9b4a8f8f` adds or changes

First confirm the tree holds the whole delta, then read each commit body-free:

```
git merge-base --is-ancestor f4360a79 HEAD; echo "exit=$?"
python3 tools/coldsweep.py --root . --commit 4a9318b7 --path instruments --path skills \
  --path tools --path .claude-plugin --path CHANGELOG.md --path docs/method/MECHANISMS.md
```

Repeat the `--commit` line for each of the other six commits and for `a1cc5f2d`. A `--path` that
matches nothing in a commit prints a note and still exits 0. Plain `git show` is barred: it prints
the message body before the diff, and reading is atomic (rule 1). Several commits on these days also
touch board items and session records; those are barred until phase 2, so always pass `--path`.

Then check what has landed on the delta paths since this brief was pinned:

```
git log --oneline 6ddbead2..HEAD -- instruments/ccfleet instruments/ccfleet.example.json \
  instruments/test_ccfleet.py instruments/man/ccfleet.1 instruments/fixtures \
  instruments/atelier-menu tools/modelguard.py tools/test_modelguard.py \
  tools/test_subject_skills.py tools/test_session_close_single_source.py skills .claude-plugin \
  CHANGELOG.md docs/method/MECHANISMS.md
```

It was empty at `6ddbead2`. A commit that only touches another tool's entry in `CHANGELOG.md` does
not count (read its diff body-free to tell). Any other commit means the delta moved: stop and hand
back for the brief to be updated. Otherwise review the work as it stands at your HEAD, and pin that
SHA in your verdict's scope.

**Machine-local surfaces no other review will catch** (read-only; report them in public-safe terms,
never a home path or a private name):

- The user-level settings wire `modelguard` as a `PreToolUse` hook on `Agent|Task|Bash`, run as
  `/usr/bin/python3 -I <the primary checkout>/tools/modelguard.py`. That interpreter is Python
  3.9.6; the `python3` on `PATH` is 3.14.6. The primary checkout was at `efeccf16` with a clean
  tree when this brief was written, so the hook every session meets already runs `fc922383`.
- `~/.local/bin/ccfleet` is a link to the primary checkout's `instruments/ccfleet`; `ccclose` is on
  `PATH`. The installed Claude Code CLI reports version 2.1.302, the version `modelguard`'s flag
  table names.
- The plugin is installed in place from the primary checkout (a local-path marketplace), so the
  routers and their grants a session loads are the primary checkout's. A plugin user installing
  from the remote marketplace gets a copy instead; judge the grants and the plugin-root path under
  both.
- The user-level instruction file on this machine is now split: a shared file that imports a
  private one (the operator split it the same session `f4360a79` landed). `ccfleet check` reports
  how it would hand that file to a public and to a private repo's session. Read it with a
  synthetic config and a synthetic `CLAUDE_CONFIG_DIR` only (below); quote no path or content from
  the real one, and never open the private part.
- Free disk sat at about 6 to 7 GB when this brief was written, below the gate's default floor
  (20 GB), so `gate` may answer "hold" here for reasons unrelated to the code.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the authors' claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1); these are a floor, never a fence.

**`ccfleet`: the pass lifecycle (`53203833`, from its docstring, constants and manual)**

1. "The verdict is the first line BEGINNING RESULT:, beside that shape line on the last turn too; a
   mention inside NOTES once read DONE."
2. "A SIGTERM or SIGHUP to a launcher leaves its session running (it may hold unsaved work) and its
   process id recorded in `<kit_dir>/sessions/`; a resume is refused while it runs."
3. `PARTIAL` and `BLOCKED` are settled verdicts: "A `run` with no claim removes its worktree when it
   holds no unlanded work, and a drive does not start it again. A claim is never released on one."
   A drive skips a job whose result file records a clean `RESULT`, "or a settled PARTIAL or
   BLOCKED", and "starts nothing once reset_utc is reached".
4. "What still widens it (`check` names each): those repo files, a kept hook whose script approves,
   kept keys such as enabledPlugins, env and the MCP approvals, and managed settings. A config that
   grants nothing runs in the default mode, where every call that would ask is refused; `check`
   says so." `PERMISSION_FLAGS` now also names `--mcp-config`, `--plugin-dir`, `--tools` and
   `--permission-prompt-tool`.
5. "The two per-session copies (`<kit_dir>/settings/`) are removed when the ccfleet process that
   launched the session exits."
6. A resume and a fold given `--item` fill `{ITEM}` and `{REVIEW_LOG}`; only `pass` fills
   `{BRIEF}`; a placeholder left unfilled refuses the launch, and `check --prompt` names any and
   lists apart the two only a resume or a fold fills.
7. A leading `~/` (or a bare `~`) in a `vars` or `env` value is expanded to the home folder;
   `vars` that is not an object is refused (exit 64).
8. A repo's `branch` is "the mainline, read only for a repo with no remote".
9. "Runtime: Python 3.8 or later (tested on 3.9 and 3.14 only), standard library only; git, nice and
   ps on PATH, and memory_pressure on macOS (the gate's memory reading); gh optional."

**`ccfleet`: the seal, the cost history, the instructions file (`564a7ca4`, `f4360a79`)**

10. "THE SEAL. ccfleet never makes or checks a seal; it calls ranked once and trusts its exit. What
    stops an unplanned paid pass is the adopter's queue, by this contract": `ranked`, `next` and
    `take` each exit nonzero until this run's ranking is sealed, "so a pass started by hand
    (`ccfleet pass`, whose take carries its own --by) meets the same gate as a drain's"; a seal
    lasts one run and no longer than the first lapse among the budgets it routes to.
11. "Whether a session that wrote a brief may then drain it is the adopter's queue's to refuse (the
    reference queue refuses to seal it) and otherwise rests on that session's own account."
12. `instruments/fixtures/review_queue_reference.py` "keeps this contract, which the tests drive",
    and every name in it is fictional; the example config's queue entries have "this exact command
    shape".
13. Each queue entry's placeholders: `ranked` gets `{BY}`; `next` `{LAUNCHED}` `{BY}`; `evidence` and
    `owed` `{FETCH}`; `take` every prompt value and `{ITEM}` `{BRIEF}` `{LOG}` `{SESSION}`;
    `release` and `ended` every prompt value and `{ITEM}` `{BRIEF}` `{SESSION}` `{RESULT}` `{LOG}`.
14. The cost history counts each completed pass ("clean in one session, or finished clean by a
    resume or fold") as the sum over its sessions of `total_cost_usd`, `duration_ms` and
    `num_turns`; count, median and max, pooled, per repo and per model (`modelUsage`'s `costUSD`);
    "The CLI prices at list price; on a subscription plan the figure is notional, not money spent.
    No size is measured, so no figure is per size." Only `local` is measured. "Nothing is
    estimated."
15. A public or unknown repo's launch is refused when the user-level instruction file it appends
    names a private name (`instructions_guard` `refuse`, the default); `warn` appends it anyway
    with a line per name. "That file's @-imports are inlined for a private repo only; a public or
    unknown one gets the import lines as text, which is what the guard reads, so a private name kept
    in an imported file reaches no public session." The inliner follows "the harness's rules:
    relative to the importing file, `~` is home, four hops, none inside code"; `resume` looks up
    visibility as a run does.

**`modelguard` (`fc922383`)**

16. After a head it does not know, a later `claude` word is a launch only when a session flag
    (`-p`, `-c`, `-r`, or a long flag only `claude` takes) or a prompt (an argument holding a
    space) follows it; where `claude` is a short option's value, only a long flag counts. "The cost
    of that, stated: an unknown wrapper given a short option just before the binary (`somewrapper
    -q claude -p x`) passes."
17. It now reads, as code: `echo|printf … | sh` (wrapped shells too), text fed to `at`/`batch`, a
    `function` body, `set -- claude …; "$@"`, `git -c alias.x='!…'` and the `git -c` keys git runs
    as commands, and the string literals of `python3 -c`, `node -e`, `perl -e`, `ruby -e`,
    `osascript -e`; it expands a variable set in the same command text and reads a word whose
    literal part can only spell `claude` as `claude` when a session flag or prompt follows.
18. What it does not see is listed as a net, not a proof: a launch from inside a script, the
    `Workflow` tool (named as "the third route"), an alias or function or variable from outside the
    command text, whether the model named is right, an inherited `ANTHROPIC_MODEL`, an unwired
    session. "Each bypass found is added to the deny table."
19. "A command that names `claude` and cannot be parsed at all is denied"; a malformed payload never
    blocks. Its tests pass on both interpreters.

**The routers and skills (`4a9318b7`, `2d8e05e3`, `564a7ca4`)**

20. "THE GRANT (allowed-tools) is the narrowest that lets the router work, and the test pins it
    line for line": a read of the plugin's own files (`Read(/${CLAUDE_PLUGIN_ROOT}/**)`, "the
    double slash makes the path absolute"), the menu by its exact command, under `session` and
    `work` only the read-only git commands that fetch the committed prompt, and under `session` the
    close's report (`ccclose` by bare name and by plugin path). "Nothing wider: … any python or any
    git here would let a run push or reset unasked." "An action's own file carries no
    allowed-tools: it is read, not loaded as a skill, so the harness never applies one there."
21. The router names the plugin root as `${CLAUDE_PLUGIN_ROOT}`, "filled in as this file loaded",
    and runs the menu by that path; a first word not in the table shows the menu and says "the first
    of them is not an action here (a later word that names an action does not make it one)".
22. `instruments/atelier-menu/SKILL.md` grants exactly `Bash(python3
    ~/.claude/skills/atelier/menu.py)`.
23. `MECHANISMS.md`: a slash command is "Typed, or reached through its subject's skill: the router's
    description carries trigger phrases, so a casual phrase can reach an action" ("wrap up" can reach
    the session close).
24. `skills/review/plan.md`: a review is owed when its item carries a review pointer (a `⏳` naming
    the delta and its intent record), or its own text or the principal's words say one is required;
    anything else is a **review candidate**, listed for the principal, "never into a brief"; where
    `queue.owed` disagrees, "this file governs until it is fixed". "Near" is judged per run; the
    estimate is the route's or repo's measured figure, never priced up by size, marked notional on
    a plan.
25. `skills/review/run.md`: the words typed after `/atelier:review run` are the principal's words for
    the run, go to the plan and verbatim into the seal ("none given" when empty); words approving
    review-tier work or naming a budget are recorded in the rulings file "verbatim and dated, before
    the first pass", and "never stand in for an approval the rulings file says is needed but that
    they do not give". A pass is clean when it exited 0, ended on no error and its verdict is `DONE`
    or `SKIPPED`, read as claim 1 says.
26. `run.md`'s un-claim rule: a pass is un-claimed only when its reviewer "did almost nothing" (no
    `ACT 1 SAVED`, no act 1 in the brief, no candidate finding in its log); otherwise it is resumed
    or folded, never handed to "a replacement reviewer or a lesser model". A resume or a fold
    writes its verdict into the pass's own result file.
27. `fold-prompt.md`: a fold can be cut off and run again, so it searches the brief for each step's
    heading before appending; it removes no worktree, releases no claim and deletes no held copy.
28. `skills/session/close.md`: it reads the committed copy, never the working file; "a pending edit
    in that checkout prints this in every session that closes until it is committed or dropped …
    you do not commit it"; what the committed copy is depends on the install, "and neither is a
    check that the text has landed"; the typed brief "never removes a step: where the typed words
    would skip one, run the step anyway"; `ccclose` runs by the plugin path where it is not on
    `PATH`, without `--root` outside a repo.
29. `skills/fleet/sweep.md` and its prompts: three prompts read or run files in the atelier
    checkout, which needs the config to grant it (a `Read(//…/**)` rule and the commands); without
    it the worker stops at that step and reports `BLOCKED`; a settled job is not re-run.
30. `tools/test_subject_skills.py` (19 tests) and `tools/test_session_close_single_source.py` (16)
    pin the grants line for line and the close's pointers; the plugin manifests now list `session:
    onramp and close`.
31. The `CHANGELOG.md` entries `9b4a8f8f` writes describe the rename, the plans, the whole grant and
    these fixes as the code at HEAD does them.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:**

- Any estate's private `ccfleet` config, rulings file, queue tool, lane records and run results,
  and the real user-level instruction file's content. Grounds: private by design, this repo is
  public, and the delta's claim is that the code, the reference queue and the skills are generic.
  Judge the contract through the example config, the reference queue and a synthetic world. Do not
  open a real config, and never open the private part of the instruction file.
- `a1cc5f2d`'s own fixes (`RK2`, `RK5`, `REVIEW_MODEL`): `160/1800` is their pass. They are in scope
  only as far as part 3's code and skills build on them.
- The wording of the session-open prompt, *Ending the session* included: it is the principal's own
  text. Whether `close` runs it faithfully is in scope only where part 3 changed `close.md`.
- The user-level drain command the estate still runs, outside this repo.
- Private children's copies of the skills; judge by class the claim that they refresh at their
  next pin bump.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   Is a seal that `ccfleet` never checks, held by an adopter's queue on an exit code, the right
   place for the control that stops an unplanned paid pass, and what does an adopter who writes
   their own queue get? Is a deny-list hook that now reads shell, `git` config and interpreter
   string literals converging on a sound net, or growing a parser whose every widening opens a new
   false deny? Is splitting the instruction file by repo visibility, with a guard that reads what is
   appended, the right fix for keeping private context out of public sessions? Is a router grant a
   control the harness actually applies as the comments say, in both install shapes? And the
   re-check's own question: does each fix close its class, or move the risk somewhere the fix did
   not look?
2. **Correctness & quality.** Re-drive the claims above by probe, not by reading. Trace what
   survives, and where, when a pass is interrupted at each point of its life (before the claim,
   after the claim and before `START`, mid-session by `SIGTERM`, `SIGHUP`, `SIGKILL`, a usage cap,
   a reboot, after the session and before the release, and during a fold or a resume run twice),
   and whether `resume` refuses or takes it correctly each time. Drive the seal contract through
   the reference queue: every way a paid launch can start with no seal, with another run's seal, or
   after a lapse. Drive the cost history with synthetic logs: a clean pass, a pass finished by a
   resume, by a fold on another model, a hand-run pass, a dry run's `.out`. Drive the import inliner
   with cycles, depth, relative and `~` paths, an import inside a code fence, and a private name
   split across lines. Drive `modelguard` with the shapes its docstring names and the wrappers it
   does not know. Record each overclaim against the text that makes it, including any claim no
   test pins.
3. **Completeness / harvest.** Every surface that states the queue contract, the seal, the
   placeholders, the exit codes, the settled verdicts, the grants and the cost basis agrees
   (docstring, `--help`, manual, example config, reference queue, skills, routers, prompts,
   changelog, `MECHANISMS.md`: V3 and V5). One home per fact (V4): the seal's rules now appear in
   the manual, `run.md` and the reference queue; look for drift between them. Find tests that would
   stay green on a broken delta by mutating scratch copies of `ccfleet`, `modelguard`, the reference
   queue and a router. What part 3 should have touched and did not, given what it claims to fix.
4. **Security & privacy**, mandatory. Design altitude: what an unattended session in a public repo
   can now receive from the user-level files (the appended instruction file and its imports, the
   kept hooks and keys `check` lists, the settings copies on disk and their lifetime and
   permissions); what the router grants pre-approve for every action under a subject; what a
   hostile repo's own settings, instruction file or pull request can make a session do. Code
   altitude: the likely vectors for the class, checked against an open catalogue (OWASP ASVS or the
   domain's equivalent), not recalled: values from the config, the jobs file, the queue's output
   and the instruction file's import lines flowing into paths, argv, prompts and git commands (path
   traversal through an import, a symlink in an import chain); for `modelguard`, every way a launch
   with no model can pass, and every ordinary command it now refuses. Aim `/security-review` at the
   code only from a clean tree; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once, on 2026-11-25 UTC, at `94f2b9a3`
(the `menu.py review` line, the since-line and the sweep at `6ddbead2`, which differs from it only
by one board item), from the places named; its results are held in the sibling. Read exit codes explicitly. Check `uptime` first; one heavy process at a time, under
`nice -n 15`, in the foreground with a long timeout (the `ccfleet` suite took about five minutes per
interpreter). Never run the whole suite: other sessions share this machine.

From the worktree root:

```
git merge-base --is-ancestor f4360a79 HEAD; echo "exit=$?"
mandoc -T lint -W style instruments/man/ccfleet.1; echo "exit=$?"
python3 instruments/ccfleet --help >/dev/null; echo "exit=$?"
python3 instruments/atelier-menu/menu.py --selftest; echo "exit=$?"
python3 instruments/atelier-menu/menu.py review; echo "exit=$?"
python3 instruments/atelier-menu/menu.py session; echo "exit=$?"
python3 instruments/fixtures/review_queue_reference.py --help; echo "exit=$?"
python3 tools/modelguard.py </dev/null; echo "exit=$?"
```

From `instruments/` (the tests load their subjects by path; run `ccfleet`'s on both interpreters,
since the runtime claim is 3.8 or later and the manual says 3.9 and 3.14 are tested):

```
nice -n 15 python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_atelier_menu; echo "exit=$?"
```

From `tools/` (`/usr/bin/python3` is the interpreter the user-level hook runs under):

```
nice -n 15 python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_subject_skills; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_subject_skills; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_session_close_single_source; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_session_close_single_source; echo "exit=$?"
```

**A synthetic world**, in your scratchpad only, every name invented. Two throwaway git repos with no
remote and mainline `main` under a scratch `repos_root` (one marked public, one private in the
config, each holding a dummy brief); a scratch `CLAUDE_CONFIG_DIR` holding an empty
`settings.json` and a `CLAUDE.md` that imports a second file by `@` path, only the second file
naming one invented private name; a config whose `kit_dir`, `repos_root` and `worktrees_root` are
scratch directories, `claude_bin` set to `/usr/bin/false` (so nothing can start a real session),
that one private name, `instructions_guard` `refuse`, a pass template using `{ITEM}` `{BRIEF}`
`{REVIEW_LOG}`, a plain run template, a template naming the private name, and a `queue` whose
entries call a small shim that logs each call and then runs
`instruments/fixtures/review_queue_reference.py` from your worktree, with the example config's
command shape; a state file holding one open `local` route, one briefed review (with a `briefed_by`
id) and one owed one; `REVIEW_QUEUE_STATE` and `REVIEW_QUEUE_NOW` set; a copy of the config with no
`queue.evidence` and its own `kit_dir`. Then, with `CLAUDE_CONFIG_DIR` pointing at the scratch
directory throughout:

```
python3 instruments/ccfleet --config <cfg> check; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> check --prompt <pass template>; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> gate; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> plan; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> plan --json; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-A drain --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-A drain; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-A pass <public repo> <item> <brief>; echo "exit=$?"
python3 instruments/fixtures/review_queue_reference.py seal --by <the briefed_by id> --ranking <file>; echo "exit=$?"
python3 instruments/fixtures/review_queue_reference.py seal --by run-A --ranking <file> --words synthetic; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-A drain --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by run-B drain --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg without evidence> plan; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <public repo> --prompt <private-name template> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <public repo> --prompt <plain template> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <private repo> --prompt <plain template> --dry-run; echo "exit=$?"
```

The ranking file is one JSON array entry naming the briefed review, route `local` and a reason. Then
repeat the last two `run` lines with a second scratch `CLAUDE_CONFIG_DIR` whose `CLAUDE.md` names the
private name in its own text, once with the config as is and once with `instructions_guard` `warn`
and its own `kit_dir`. Read `<kit_dir>` afterwards: `driver.log`, every file the runs left (and any
they should have left and did not, or should have removed and did not), and the shim's log of the
calls it received, in order. How the brief-writer built its world, and what it saw, is in the
sibling.

**Live behaviour.** The claims about real `claude -p` (`--append-system-prompt-file` and whether the
harness follows an `@` import in an appended file, `--setting-sources`, `--settings`, the JSON log's
`modelUsage` and `total_cost_usd`, `--session-id`, how a session behaves when its launcher is sent
`SIGTERM`) rest on a stand-in binary in the tests, and the routers' grants rest on the harness
substituting `${CLAUDE_PLUGIN_ROOT}` in front matter. Re-drive what you can read-only. At most a few
real launches, and only if the session running you may spend on them, all on the cheapest model, in
a throwaway repo under your scratchpad, with no permission-mode argument and a synthetic
`CLAUDE_CONFIG_DIR` (never the real one): one `ccfleet run` of a public scratch repo whose prompt
asks the session to report whether its system prompt holds the imported file's marker text, then
prints a `RESULT:` line; and headless `claude -p` sessions started in a scratch directory with the
plugin loaded from your worktree, sending a bare `/atelier:review`, `/atelier:review plan` and
`/atelier:session close`, each told to report what it read and ran, which tool calls it was asked to
approve, and to make no write outside that directory. Otherwise mark them NOT RUN with grounds.
Never run `ccfleet` against a real repo, never `drive` or `drain` for real, and never with a real
config. The brief-writer ran none of these launches.

## House rules for this run

- **Live systems:** read-only reads as needed; no live writes. A check that needs a write is marked
  NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Other sessions' transcripts are read only through a
  script that prints keys and counts; quote none of their content. `ccfleet check` against the real
  user-level directory prints its hooks and instruction-file path: do not run it there.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine, one of them briefing or running `160/1800` over the same
  tool: touch nothing outside your worktree and scratchpad, and never touch the primary checkout
  (the hook, the installed `ccfleet` and the in-place plugin run from it). Child repos are
  read-only and reported by count only, never by name or path.
- Never run an installed tool by bare name from `PATH`: use `instruments/ccfleet` or
  `python3 tools/<x>.py` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief dirty.
- This pass is pending while you run it: anything you write to a pointer or a commit subject before
  phase 2 names the held-back sibling by count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at about 100 columns; NZ English. This repo
  is PUBLIC: quote no secret, email address, home path, private repo name or estate fact.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

**Reviewer's start-up reading:** skip the session-log step of the repo's read order; the log is on
rule 2's barred list.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material is held outside the repo under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/sessions/`, every prior verdict in `docs/reviews/` (the earlier
pass's above included), every item under `docs/roadmap/160-doctrine-review-owed/` beyond its title,
the delta commits' message bodies, `docs/method/census/`, and beyond their first line:

- `docs/roadmap/210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md`
  (the intent record; it carries the authors' account of each fix)
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

All of these carry an author's account of the work, and two carry earlier verdicts' findings.

**This brief's held-back sibling is not in the tree.** Whoever orchestrates the pass holds it
outside the repo and every worktree, and releases it to you only after your act 1 is committed; by
count it holds 26 questions and 16 facts. Never look for it in git history, other checkouts,
scratchpads or temporary directories. Run by hand with no orchestrator, you open it yourself, as a
deliberate second act, after act 1 is committed, and disclose when.

The delta's own comments, docstrings, manual, skills, prompts, tests and `CHANGELOG.md` entries carry
the authors' account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md \
  --also-exclude docs/roadmap/210-instruments-open-features/470-fix-ccfleet-and-its-two-skills-fl1-fl25.md \
  --also-exclude docs/roadmap/210-instruments-open-features/500-modelguard-reads-a-lookup-of-claude-as-a-launch.md \
  --also-exclude docs/roadmap/210-instruments-open-features/560-ccfleet-cannot-see-inherited-permissions-and-a-kept-worktree-loses-its-claim.md \
  --also-exclude docs/roadmap/210-instruments-open-features/570-modelguard-refuses-ssh-as-the-claude-user.md \
  --also-exclude docs/roadmap/210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md \
  --also-exclude docs/roadmap/210-instruments-open-features/610-ccfleet-follows-the-private-import-for-private-repos-only.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/020-every-command-is-subject-then-action.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/030-a-close-command-so-the-close-text-is-not-pasted.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/210-a-plan-mode-that-shows-the-drain-before-it-runs.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/240-a-work-plan-mode-for-work-run.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/500-census-slice-4-doctrine-defects.md \
  --also-exclude docs/method/census \
  "instructions_guard|SETTLED_ON|CLAUDE_LONG_FLAGS|THE SEAL"
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list, over the whole delta as it stands at your HEAD, cold: you have not read the earlier verdict, so
judge the code and skills on their own terms, not as fixes. Append your verdict below a `---` divider
in THIS file: provenance repeated (how you were spawned, your tier, the orchestrator with its spawn
prompt, what you read, the UTC day, the HEAD you pinned), per-lens answers, V1–V7 each answered or
discharged with grounds, each load-bearing assumption damaged or confirmed with its probe, a
per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix `PK`:
`PK1`, `PK2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, the method record `REVIEW.md` § *The
lifecycle* requires, and a follow-up checklist. Give the paid-drain path its own line in the
per-lens answers. Then STOP: act 1 is committed, unrevised, **before** the sibling or the earlier
verdict is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling, the earlier verdict and the barred records; screen the delta
commits' bodies. Append `### Reconcile` beneath your verdict, with:

- **The RK ledger, one row for each of `RK1`, `RK3`, `RK4` and `RK6`–`RK29`:** what the earlier
  verdict counselled (by pointer, not restated at length), the commit and file:line that answers it,
  how you re-drove it at your HEAD (the command and its result, or that verdict's own reproduction
  re-run), and its state: *fixed as counselled* · *fixed another way* (and whether that way meets the
  finding) · *partly fixed* · *not fixed* · *regressed*. Reading a fix is not re-driving it (V2).
  Where a fix went beyond or against the counsel, or where the principal's recorded answer on a
  finding shaped the fix, say so and judge it. `RK2` and `RK5` are `160/1800`'s; name any you met.
- Per-finding notes on your act-1 findings against the sibling's questions and the authors' account;
  any finding formed at reconcile, marked as such, with a `PK` id after your last.
- The residual risk, named: act 2 reads the earlier verdict, so the RK ledger is anchored on it by
  design; act 1 is the cold half.
- The overall line restated.

Never revise act-1 text. Then fold the sibling in below the reconcile.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it. Under the overall verdict, say plainly in three
lines: whether anything you found loses, misreads or mis-costs paid review work; whether
`/atelier:review plan` and `/atelier:review run`, with `ccfleet` as part 3 leaves it, are safe to run
the principal's paid weekly drain from, and if not, what must change first; and whether anything in
the delta can put private context into a public repo's session. Name `160/1810` in your scope line,
and `210/600` and `210/610` as the items the delta answers to.
