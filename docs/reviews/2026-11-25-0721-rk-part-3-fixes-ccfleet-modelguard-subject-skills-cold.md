# Cold pass — the RK part-3 fixes to `ccfleet`, `modelguard` and the subject skills (`160/1810`)

**Board:** `docs/roadmap/160-doctrine-review-owed/1810-rule-4-cold-pass-queued-rk-part-3-fixes.md`
**Status:** VERDICT 2026-11-25 UTC: PASS-WITH-FINDINGS, 0 MAJOR, 5 MODERATE, 12 minor, 4 notes
(`PK1`–`PK21`; one Fable reviewer under off-tier orchestrator `14c2530d`; acts 1 and 2 written,
the sibling folded in below). Findings are the principal's to decide. Was: BRIEF ONLY, 2026-11-25 UTC. Written by headless session `075cdcd9` (`atelier-e0`,
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

---

# Verdict, act 1 (cold): the RK part-3 fixes (`160/1810`)

**Reviewer:** a fresh Fable session (model `claude-fable-5-2`, the principal-named review tier,
checked at selection), started for this pass alone. **Day:** 2026-11-25 UTC (started 07:59Z).
**Scope:** board `160/1810`; the delta answers to `210/600` and `210/610`. Seven commits
(`fc922383`, `4a9318b7`, `9b4a8f8f`, `53203833`, `2d8e05e3`, `564a7ca4`, `f4360a79`), with
`a1cc5f2d` read for context, reviewed as the tree stands at **`6d71ea91`** (my pinned HEAD, which
was `origin/main`). **Review worktree:** `<WT>` (branch `atelier-e7-pk-pass`), read-only to me but
for this file. **Scratch:** `<SCRATCH>`.

**Overall: PASS-WITH-FINDINGS. 0 MAJOR, 5 MODERATE, 11 minor, 4 notes** (`PK1`–`PK20`).

## Provenance (rule 4, V7)

- **Spawned by** session `14c2530d` (`atelier-e7`, Opus 5.5), principal-opened, as an off-tier
  orchestrator: it holds the context partition and commits the records, and by its own account
  forms no finding and writes no severity. It authored no part of the delta and no part of the
  brief (headless session `075cdcd9` wrote the brief). Its spawn prompt is recorded verbatim at
  the end of this act (*Spawn prompt, verbatim*), with the three path substitutions it named. It
  made no barred-set choice of its own: "The barred set is exactly the brief's; I add nothing and
  remove nothing." The release message does not exist yet; it goes into act 2.
- **Not started or instructed by** the authors (`0ee74059` and its workers) or the brief-writer.
  No author session contacted me. No contact from any session but the orchestrator's spawn.
- **Tier:** Fable, stated by my harness ("You are powered by the model named Fable 5.2"). I
  started no subagent; every reading, probe and judgement here is mine.
- **What I read, in order:** the spawn prompt; this brief whole; `docs/method/REVIEW.md` whole;
  the eight commits body-free (`coldsweep --commit`, each exit 0); `instruments/ccfleet` whole at
  HEAD; the reference queue and the example config whole; `skills/review/` (router, `run.md`,
  `plan.md`, the three prompts) whole; `skills/session/` router and `close.md` whole; the other
  routers, the fleet prompts and `sweep.md` as the diffs and their surrounding sections;
  `tools/modelguard.py` whole; the tests' relevant cases; the manual's changed sections and its
  THREATS; `CHANGELOG.md`'s new entries; `MECHANISMS.md`'s two changed passages; the two
  `README.md` entries that mirror `modelguard` and `ccfleet`; `00-APEX.md`'s section on the
  principal's authority; the *Ending the session* section of the session-open prompt (to see
  what `close.md` delivers, not to judge its wording).
- **Start-up reading:** I skipped the session-log step (rule 2). I read no session record, no
  prior verdict, no item under `docs/roadmap/160-doctrine-review-owed/`, no delta commit's message
  body, none of the brief's listed barred items, and I did not look for the held-back sibling.
  No `--include-barred` sweep was run.
- **Exposure to disclose.** (1) My harness loaded, unasked, the repo's instruction file, the
  user-level instruction file with what it imports, and a memory index, before I read a line of
  the brief. They hold private context this verdict does not carry. One entry there records the
  principal's approval of this one pass (the same words the brief's head quotes); nothing I met
  there gives an account of the delta or of the earlier verdict's findings. I did not open the
  private part myself. (2) The harness also showed the five newest commit subjects (claims on
  `160/1800` and `160/1810`), which name which sessions hold which pass and nothing evaluative.
  (3) The delta's own comments, tests and `CHANGELOG.md` cite `RK` numbers with a clause each
  (for example "RK4" beside the launcher-signal code); that is the delta, read as such, and I
  opened nothing to learn what the earlier verdict said of them.
- **Limits on this record.** The harness moved three long foreground commands to the background
  on its own after 180 s (the two `test_ccfleet` runs and one timing run); I waited for each and
  read its exit code. One static search of the CLI binary was stopped by me as too heavy and
  re-done with a cheaper method. The two full suites started at a one-minute load of 17.9 and
  5.5. Load was above the 24 threshold when one timing run of a subset of the tests started (37,
  at 08:23Z) and while the world's light commands ran (55, at 08:10Z). No wall-clock test
  failed, on any run.

## Method

1. **Floor first.** `git merge-base --is-ancestor f4360a79 HEAD` (exit 0); the brief's since-line
   at `6d71ea91` (empty); each commit body-free. Then every line of the re-run list (ledger
   below).
2. **Read the delta whole at HEAD**, naming my own load-bearing assumptions before the brief's
   claims list was used as a checklist (lens 1).
3. **A synthetic world** in `<SCRATCH>/w`, as the brief specifies, every name invented: two
   repos with no remote, two scratch `CLAUDE_CONFIG_DIR`s, a shim in front of the reference
   queue that logs each call, `claude_bin` `/usr/bin/false`; then a stand-in binary of my own
   (`<SCRATCH>/bin/fakeclaude`) that sleeps, records whether its settings and instructions files
   exist at its start and its end, and prints a JSON result, to drive the lifecycle by signal.
4. **Probes by script**, each kept in `<SCRATCH>/probes/` with its output beside it: the import
   inliner (22 shapes), the cost history (7 synthetic pass histories), the reference queue
   (routes, a late brief, seal lifetime), the verdict reader (10 final outputs), `modelguard`
   (84 launch shapes and 102 benign commands, on both interpreters, and 12 long adversarial
   inputs timed), `check` with a user-level `sandbox` block.
5. **Mutation** of scratch copies of `ccfleet`, the reference queue, `modelguard`, the routers,
   the action files, the manual, the example config and `MECHANISMS.md` (55 mutants), each run
   against the tests that should catch it (lens 3).
6. **Live behaviour:** one real launch tried within the brief's bounds; it could not log in
   (ledger below), so the live claims were re-driven statically instead, from the installed
   CLI's own bundled source and the public documentation, and are marked for what they are.
7. **Left out, and why:** any real config, rulings file, queue tool or real `CLAUDE_CONFIG_DIR`
   (the brief's non-goals); `a1cc5f2d`'s own fixes (`160/1800`'s); the wording of the
   session-open prompt; `/security-review` (discharged under V6). Private children: none read.

## Load-bearing assumptions (lens 1, named before the brief's claims were used)

Each is mine; each says what the delta rests on, the probe, and its state.

- **A1. A session's verdict can be read from a line it prints.** The whole release-and-remove
  decision rests on one `RESULT:` line and on the model keeping the prompt's rule about where
  such lines go. Probe: `<SCRATCH>/probes/harv.py`. **Damaged** (`PK4`): the fix for a later
  mention reads an earlier one.
- **A2. The harness does not follow an `@` import in a file given by
  `--append-system-prompt-file`, and loads no user-level `CLAUDE.md` when the `user` setting
  source is left out.** The import split's privacy claim rests on both. Live: NOT RUN (no login,
  see the live ledger). Static, first half: in the installed CLI (2.1.302) the option's file is
  read and decoded as plain text and joined to the prompt, with no import step in that path.
  Second half: unverified by me; it is the authors' "checked against claude 2.1.x" comment
  (`instruments/ccfleet:503`). **Confirmed in part, by reading, not by running.**
- **A3. A launcher's death is the only way a session outlives its bookkeeping.** `launch()`
  keeps the session alive on SIGTERM and SIGHUP and records its process id. Probe: stand-in
  session, SIGTERM to the launcher. **Damaged** (`PK1`, `PK2`): the session lives on, but its
  settings copies are removed under it, and only `resume` checks the record.
- **A4. `ps` shows a running session's id on its command line.** `live_session` needs it.
  Probe: a count over this machine's running `claude` processes (7 found, all 7 with their
  arguments shown; none quoted). **Confirmed** for this machine and CLI version; not pinned by
  any test against the real binary.
- **A5. The adopter's queue is a sound home for the control that stops an unplanned paid
  pass.** ccfleet trusts an exit code. Probe: the reference queue through the shim, sealed and
  unsealed, by two run ids. **Holds for `drain` and `pass`; narrower than it reads** (`PK3`,
  `PK10`): `run` and `resume` meet no gate, the reference offers reviews the seal never ranked,
  and it ignores the route a review was sealed to.
- **A6. Visibility decides what a session may be told, and the config knows the visibility.**
  A repo marked private that is public gets the private imports; the manual says so. Probe:
  none beyond reading `repo_facts` (the config's word wins over the forge's).
  **Stated, not defended** (`PK20`).
- **A7. A router's `allowed-tools` is applied by the harness as written, with the plugin root
  filled in, in both install shapes.** Live: NOT RUN. Static: the installed CLI passes a plugin
  skill's whole `allowed-tools` string through its plugin-root substitution before parsing it,
  so the `Read(/${CLAUDE_PLUGIN_ROOT}/**)` rule is filled in too. The public documentation
  promises that substitution only for Bash rules. **Confirmed by reading for 2.1.302; resting on
  behaviour the documentation does not promise** (`PK19`).
- **A8. A deny-list parser of shell text converges.** Probe: 186 commands. **Holds as a net,
  with a cost on both sides** (`PK13`): 12 launches of the shapes tried pass, and 28 ordinary
  commands of the shapes tried are refused, most of them in the class the docstring states.
- **A9. The words after a command are the principal's.** `run.md` and `close.md` treat them so.
  `MECHANISMS.md`, in the same delta, says a model can reach an action from a casual phrase.
  **Damaged** (`PK6`).
- **A10. Summing `total_cost_usd` over a pass's sessions gives the pass's cost.** True only if
  a resumed session reports its own run and not the conversation's running total. Live: NOT RUN.
  **Unverified** (`PK12`).

## Per-lens answers

**Lens 1, approach.** The pass lifecycle is now recoverable at every point I could drive: a
pass cut off by a signal, a cap or a kill keeps its claim, worktree and review log, its session
id is on its `START` line and its claim, and `resume` refuses while the session runs. The
approach is sound; two of its seams are not closed (`PK1`, `PK2`). Putting the seal in the
adopter's queue is defensible for a tool that must stay generic, and the reference queue makes
the contract readable in one sitting, as claimed. What an adopter who writes their own queue
gets is a prose contract and a fixture, with no conformance check: nothing in `ccfleet check`
tries `ranked`, `next` or `take` with an unsealed id and expects a refusal. The seal is also a
gate on two commands, not on paid launches: `ccfleet run` given the pass prompt, and `resume`,
call no queue command (by design for `resume`; unstated for `run`). The hook is a net and says
so; its widening this round traded one stated false allow for the removal of a broad false
deny, which I judge the right direction, with residue on both sides (`PK13`). Splitting the
instruction file by visibility is the right fix for what ccfleet itself appends; it does not
bound what the session can open, and the text it appends names the file it withholds (`PK5`).
The router grant is a real control in the CLI version read (`A7`). Does each fix close its
class? Three move the risk rather than close it: the verdict reader (`PK4`), the launcher
signal (`PK1`), the settled verdicts (`PK14`).

**Lens 2, correctness.** Of the brief's 31 claims: 18 re-driven and holding as written; 10
holding with a limit found (1, 2, 3, 5, 10, 14, 15, 18, 25, 29); 3 overclaimed (4: `check` does
not name each; 12: the reference does not keep the route rules `run.md` states beside the
seal's; 31: the changelog covers the skills only). Each is in the claims ledger below, with how
it was re-driven.

**Lens 3, completeness.** The surfaces disagree in three places (`PK8`, `PK9`, `PK14`); four
mirror sites were not swept (`PK15`); of 55 mutants the tests killed 42, and the 13 survivors
are listed under `PK16`.

**Lens 4, security and privacy.** No path found by which ccfleet itself appends an imported
file to a public or unknown-visibility repo's session: mutants that inline for every
visibility, that make the appended copy differ from what the guard reads, that silence the
guard, and that turn `refuse` into `warn` are all killed by the tests, and the world's runs show
the public copy carrying the import line as text only. What remains: the session can be told
where the private part is and may open it (`PK5`); a `resume` of a public repo's pass is not
pinned by any test to get the public copy (`PK16`); a launcher stopped by a signal strips its
live session of the settings copy that carries the kept deny rules and guard hooks (`PK1`);
`check` does not name a kept `sandbox` block that auto-allows shell commands (`PK11`). The
router grants pre-approve nothing that writes: plugin reads, one exact menu command, three exact
read-only git commands, and `ccclose`, which I read as read-only but for the fetch it says it
makes. Code altitude, by hand against ASVS V5 (validation), V12 (files) and V14 (configuration):
repo names, labels, items and session ids are validated or made safe before they reach a path
(`check_repo_name`, `safe`, the session-id pattern); every queue and git call is an argv list
with no shell; the settings copies are created owner-only (read at `:717` and `:725`, and seen as
mode 600 in the world, though no test pins it: `PK16`); the
import inliner reads any path a user-level file names, which is the operator's own file and a
private repo's session only. Not defended, and the operator's to know: a queue's `BRIEF` field
is joined to the worktree path unchecked (`one_pass`, `check_file`), so a queue that printed an
absolute path would have it accepted; the prompt travels on the command line, readable by other
local users in `ps`; the guard reads the prompt and the instruction file, not the settings copy
(a private name in a kept `env` value or hook command line is not looked for).

**The paid-drain path, on its own line.** Nothing I found breaks a drain that runs
undisturbed: seal refused → nothing starts; sealed → the pass is claimed with its session id,
launched, read, released only on a clean end with nothing unlanded, and kept whole on any other
end. The defects on this path need a second event: a signal to a launcher (`PK1`), a fold or an
un-claim decision taken while a session still runs (`PK2`), a final output that breaks the
prompt's own rule (`PK4`). Whether the estate's real queue keeps the seal and the route rules is
outside what this pass may open (`PK3`).

## The standing checklist

- **V1 (no claim stronger than its evidence):** run on every claim; overclaims at `PK1` (claim
  5), `PK3` (12), `PK5` (15), `PK11` (4), `PK12` (14), `PK15` (31).
- **V2 (re-run recorded proofs):** every re-run line run (ledger). Two "seen live" proofs in the
  delta could not be re-run and are marked so: the changelog's "seen live for
  `/atelier:session close`" and the test docstring's "a live probe showed the harness needs" the
  double slash (`PK19`).
- **V3 (a changed rule swept to its mirrors):** `PK15` (four sites), `PK8`.
- **V4 (one fact, one home):** the seal's rules live in five places (the docstring, the manual,
  `run.md`, the reference queue's docstring and code, the example config's comment). The four
  refusals agree across all five. The reference adds two the texts do not list as seal rules (a
  route the review does not fit; a brief this run's session wrote, which the texts mention
  apart). `run.md` alone holds the route-take and spill rules, and nothing implements them
  (`PK3`). The queue placeholders agree across the docstring, the manual and the code.
- **V5 (no internal contradiction; cross-references reach their rule):** contradictions at
  `PK8` and `PK14`. Cross-references checked for the rule reached: `run.md` → `man ccfleet`,
  *The seal* (reaches the four-bullet contract); the docstring → `run.md`, *The seal's own
  rules* (reaches that paragraph); `plan.md` → `REVIEW.md` rule 4 (reaches "queue the review
  pointer … naming the delta and the intent record"); `close.md` → the prompt's
  `## Ending the session` (present); `sweep.md` → `run.md` § *Briefs are never left owed*
  (present, holds the held-directory rule); the manual's THREATS → `check`'s `WIDENS:` lines
  (reached, and incomplete: `PK11`).
- **V6 (security and privacy, with `/security-review` where it can reach):** lens 4 above.
  `/security-review` is discharged with grounds: it reads the running session's pending diff,
  this delta is landed, my worktree is clean, and my session's working directory is not one I
  can aim; a run would scan nothing or the wrong tree. The code-altitude read was done by hand.
- **V7 (spawn provenance):** stated in the brief and repeated above.

## Findings

Every finding is the principal's to decide (rule 3). Counsel is labelled and kept beneath.

### PK1 (MODERATE, security) — a signalled launcher removes its live session's settings copies

*Claim tested:* claim 5, and `session_files`' own docstring: "They are not removed while it
runs, since a session may read its settings file again" (`instruments/ccfleet:703-707`); the
manual's FILES: "each pair lives only while the session does".
*Evidence:* `launch()` turns SIGTERM or SIGHUP into `SystemExit` and leaves the session running
(`:1184-1192`); `session_files` registered the removal with `atexit` (`:716`), which runs on that
exit. Probe, twice: a stand-in session logging whether its `--settings` and
`--append-system-prompt-file` paths exist. `start … settings=yes instr=yes`; SIGTERM to the
launcher (exit 143, `LAUNCHER STOPPED … is left running`); `<kit_dir>/settings/` empty while the
session still slept; `end … settings=no instr=no`.
*Why it matters:* that file is the session's whole user-level remainder: the kept deny and ask
rules and guard hooks, and the config's own grant. What a real session does when its `--settings`
file vanishes is NOT RUN (no live launch was possible). If it re-reads, it loses its grant (it
stalls) and its guards (it is unguarded where a permission flag in `claude_args` still stands).
*Criterion:* V1; lens 4. No test covers it: the signalled-launcher test never looks at the
copies.
*Severity:* MODERATE. *Recurrence prevention:* tie the copies' removal to the session's end, not
the launcher's: skip the removal on the signal path and sweep copies with no live session record
at the next start; and assert, in the signalled-launcher test, that both copies exist while
`live_session` is true.

### PK2 (MODERATE) — a fold is not refused while the pass's session still runs

*Claim tested:* claim 2 ("a resume is refused while it runs") against the lifecycle it protects.
*Evidence:* only `resume` calls `live_session` (`:2479`); `run --in WT --item ITEM` has no such
check. Probe, through the reference queue: a sealed pass claimed and started (a stand-in session
sleeping in its worktree), its launcher stopped by SIGTERM. `resume` of it: refused, exit 2, as
claimed. `run --in <that worktree> --item <its item>`: `START`, a second session in the same
worktree, `END … result=DONE`, exit 0; the queue's state then showed the claim released and the
item done, and the worktree was gone, while the first session's process record was still there
and its own end came ten seconds later, into a directory that no longer existed.
*Why it matters:* `run.md` tells the drain session to take the fold "before a resume" for a pass
whose act 2 is written. A session whose launcher was stopped looks, from the result files, like
a cut-off pass. The unlanded-work check still guards uncommitted files; it does not guard a
reviewer that is mid-thought with a clean tree.
*Severity:* MODERATE. *Counsel:* record the worktree in the process record and refuse any launch
into a worktree a recorded live session runs in; or give the fold the session id and check it.

### PK3 (MODERATE) — the reference queue's `next` ignores the route a review was sealed to

*Claim tested:* claim 12 (the reference "keeps this contract"), `run.md`: "Each route takes only
its own reviews, in rank order. The local route takes its own first, then any other route's not
yet started, but never from a budget that lapses before its own: that budget keeps its reviews."
*Evidence:* `next_pick` walks the sealed order and prints the first review not skipped, whatever
its route (`review_queue_reference.py:113-129`). Probe: two open routes, `credit` lapsing before
`local`; a review sealed to `credit`, another to `local`. `next` printed the `credit` review
first. ccfleet's drain runs every pick as a local session ("Every pass ccfleet launches is a
local session"), so the review planned for the credit budget is spent from the local one, from a
budget that lapses later: the exact case `run.md` forbids. The docstring's and the manual's
contract text, and the example config's `next` argv, carry no route at all.
*Why it matters:* the plan shows the principal a route and a cost per review; a queue built from
the reference spends otherwise. For the estate's own queue this is a non-goal I could not open,
so the verdict's drain line is conditional on it.
*Severity:* MODERATE. *Counsel:* say in the contract that `next` offers only what the sealed
ranking routes to the local route (plus the stated spill), make the reference do it, and pin it
with a two-route test.

### PK4 (MODERATE) — the first line beginning `RESULT:` wins, so an earlier mention is read

*Claim tested:* claim 1.
*Evidence:* `result_word` takes `found[0]` (`:960-967`); the shape line is required somewhere in
the text, not beside the `RESULT:` line. Probe, on a clean JSON end:
"The pass could not land. / RESULT: DONE is not what this is. / (blank) / RESULT: FAILED /
ITEM: r:i" reads **DONE**; "- RESULT: SKIPPED was considered / (blank) / RESULT: FAILED /
ITEM: r:i" reads **SKIPPED**. Both words release the claim and, on a clean tree, remove the
worktree. The mirrored case the fix answered (a mention after the real line) now reads right.
*Why it matters:* the control is the prompt's rule ("Write a line beginning `RESULT:` … nowhere
else"), and the docstring records that a model once broke the mirror of it. A FAILED pass read
as DONE is settled in the queue with its work undone: the brief's first worst failure.
*Severity:* MODERATE (the trigger needs a broken prompt rule; the consequence is the worst
class). *Counsel:* read the `RESULT:` line that stands directly above the `ITEM:` or `REPO:`
line, the shape the prompts fix, and read anything else as UNKNOWN.

### PK5 (MODERATE, privacy) — a public session is told where the withheld file is

*Claim tested:* claim 15: "a private name kept in an imported file reaches no public session."
*Evidence:* the copy appended for a public repo, captured from the world: its header names the
user-level file's absolute path, says its imports are "not followed (this repo is PUBLIC, and an
imported file is kept from such a repo's session)", and the body ends with the import line
itself, as text. The session's settings copy carries no deny rule for that path. The manual's
THREATS names the repo's files, outside text and the adopter's values as what steers a session,
and not this.
*Why it matters:* the claim holds for what ccfleet appends. It does not hold for what the
session can open: where the config's grant lets a session read outside its worktree (any bypass
mode, any broad `Read` rule), the private part is one tool call away and the appended text has
just pointed at it. A repo's own instruction file, or text a pull request carries, can ask for
that read. NOT RUN live: whether a model does so unprompted. In the default mode with no grant
the read would ask and be refused.
*Severity:* MODERATE. *Recurrence prevention:* for a public or unknown repo, add a deny rule
for each import target (ccfleet already resolves them for `check`) to the session's settings
copy, drop or neutralise the import line in the appended copy, and name the residual in THREATS.

### PK6 (minor, doctrine) — the words after a command are taken as the principal's own

*Evidence:* `MECHANISMS.md`, as this delta changes it: "a model can start one on a casual phrase
… without anyone typing the command". `run.md`: "The words typed after `/atelier:review run` are
the principal's words for this run … into the seal, quoted verbatim … record them in the rulings
file, verbatim and dated". `close.md`: "The text the principal typed after the invocation". A
model that reaches the skill composes the arguments itself (the harness's skill call takes an
arguments string from the model). Nothing tells it to take the words from the principal's own
message instead. NOT RUN live.
*Why it matters:* a model's paraphrase can be sealed and filed in the rulings file as his words.
*Counsel:* where the command was not typed, the words are quoted from the principal's message in
the conversation, or "none given"; never from the call's own arguments.

### PK7 (minor, doctrine) — `close.md` runs a step the principal's own typed words would skip

*Evidence:* `skills/session/close.md:79-83`: "It never removes a step: where the typed words
would skip one, run the step anyway and say that the brief asked otherwise." The words are, by
the file's own account, the principal's. `00-APEX.md`: "The principal's authority is absolute".
His no-drift rule, quoted in the file's header, has an exception in his own hand: "unless I
authorise the drift".
*Why it is his to rule:* the delta chose that typed words are not that authorisation. That may
be what he wants (a dropped word must not skip the record check), or it may be a command that
overrules him at the one moment he is typing to it. *Counsel:* none beyond putting it to him.

### PK8 (minor) — `run.md` counts a refused claim as an unclean end; the code does not

*Evidence:* `skills/review/run.md:152-154`: "a pass that ends before its session starts (a
failed fetch, a brief not on the mainline, a guard or claim refusal) comes back off it and
counts toward the unclean stop". `instruments/ccfleet:1952-1958`: the claim-refused branch adds
to `refused`, "not counted as a bad end"; the manual agrees with the code; the test
`test_a_refused_claim_is_not_a_bad_end_and_is_not_offered_again` pins the code. *Criterion:* V5.

### PK9 (minor) — a dry drain before the seal ends as a queue error

*Evidence:* world, unsealed: `drain --dry-run` printed the plan reading, then
`DRAIN EXIT: queue error`, exit 1; the shim logged `next … --by run-A`; the driver log says
"queue next failed rc=1: refused: no ranking is sealed". Sealed by run-A, the same command
rehearsed one launch and exited 0; by run-B, queue error again. `plan.md`'s table and the
docstring describe the dry drain as the plan's reading "before its rehearsed launches", and
"a rehearsal reports, it does not stop".
*Counsel:* say that launches can be rehearsed only by the run that holds the seal, or have the
dry drain say "not sealed: no launches rehearsed" and exit 0.

### PK10 (minor) — what the seal does not bound

*Evidence, each by probe on the reference queue:* (a) with one open route and no lapse time the
seal never expires (`ranked` exit 0 seventeen months of clock later); "A seal lasts one run" is
kept only by the id changing. (b) `--by` defaults to `unknown` (`ccfleet:2656`), which the
reference seals and honours, so two sessions that pass no id share a seal. (c) a drain restarted
under the same id needs no new seal, though `run.md` says "every drain, a restarted one
included, plans and seals afresh". (d) `take` accepts an item that is in the queue and not in
the sealed order; `next` offers a review briefed after the seal (by `run.md`'s design, "runs
last"), which is a paid pass no plan showed. (e) `ccfleet run` with the pass prompt and
`--set`, and `resume`, call no queue command.
*Counsel:* refuse `unknown` as a sealing id; give the seal an end the queue can see (the
drain's exit could call an optional `unseal`); say plainly in *The seal* which launches it does
not gate.

### PK11 (minor, security) — `check` does not name each thing that widens the grant

*Claim tested:* claim 4: "What still widens it (`check` names each) … and managed settings."
*Evidence:* (a) a user-level `sandbox` block is kept (only three permission keys and approving
hooks are taken out) and the CLI has `sandbox.autoAllowBashIfSandboxed`; probe with such a
block: `check` lists `sandbox` among "Kept:" with no `WIDENS:` line, and still prints "NO GRANT …
every call that would ask (an edit, most shell commands) is refused". (b) `check` prints nothing
about managed settings; only the manual does. (c) A repo's own skills can carry `allowed-tools`.
The public skills documentation, read 2026-11-25: "Claude Code applies a project skill's
`allowed-tools` even in a `-p` run in a folder you've never trusted." The project source loads
in every ccfleet session, so a repo's skill pre-approves what it lists for the turn that
invokes it; the `WIDENED` lines read the two settings files only, and the manual's widening
list does not name skills.
*Recurrence prevention:* treat an unknown kept top-level key as "kept, not classified" in
`check`'s output instead of silence, so a new harness key cannot widen unseen.

### PK12 (minor) — the cost history can under-count, and one of its assumptions is untested

*Evidence (probe `hist.py`):* (a) a resume's log is named to the minute with no date
(`resume-<repo>-<item>-<HHMM>.json`), and a pass's to the minute too: a second resume in the
same minute, or at the same time on a later day, opens the same file for writing. A pass of 7,
a failed resume of 3 and a clean resume of 2 read as 9, and the first resume's log is gone.
(b) a later session counts as finishing the pass on its log's word alone, read with exit 0
assumed, so a resume ccfleet itself read as `UNLANDED` or as an error exit counts as completed.
(c) a pass whose launcher was stopped has no `END` line and is not "seen" at all. (d) `A10`.
*Counsel:* date-and-second log names; read a later session's own `END` line where there is one.

### PK13 (minor) — `modelguard`: its refusal's advice is not always true; gaps both ways

*Evidence (probe `mg.py`, identical on 3.14.6 and 3.9.6):* (a) the refusal says to give
`claude` "as an option's value (`-u claude`)" and the docstring says that form "passes". It
passes only after a short option: `docker run --name claude -p 8080:80 nginx` is refused, and
so is `mytool --dir /opt/claude 'some text'`. (b) string literals in interpreter code are read
as an argv when the first is `claude` and a later one holds a space:
`python3 -c "print('claude', 'hello world')"` is refused, and so is the `node -e` twin. (c) Of
the 102 benign commands tried, 28 are refused: those 4, 3 where a quoted argument that mentions
`claude` is read as a command (`say 'claude -p is a flag'`), and 21 in the class the docstring
states (an unknown head, `claude` as a positional, then `-p`, `-c` or `-r`), among them
`python3 x.py claude -c cfg`, `./run.sh claude -p prod` and `go test ./claude -p 4`. (d) Of the
84 launches tried, 13 pass: the one the docstring states and 12 more, among them
`screen -dm claude -p x`, `tmux new -d claude`, `bash <(echo 'claude -p x')`,
`echo 'claude -p x' | tee /dev/null | sh`, `sh -c "$(echo claude -p x)"` and an `awk`
`system()` call; a launch nested past the depth limit of four passes too. By the docstring's
own rule ("Each bypass found is added to the deny table") these are owed to the table, as
passes it accepts or as denies. No slow input found (12 adversarial inputs up to 205 kB, worst
0.37 s). The stale `README.md` entry is under `PK15`.

### PK14 (minor) — a settled end is never re-run, including the one the new prompts create

*Evidence:* the fleet prompts now end `RESULT: BLOCKED` when the config lacks the read grant.
Probe: two jobs ended BLOCKED and PARTIAL (the second leaving an untracked file); the next
`drive` of the same jobs file logged "skip … settled … not run again" for both, the kept
worktree included. `sweep.md` step 5 gives the reason as "running it again would only repeat
it", which is false once the operator has fixed the grant; step 8 says a `PARTIAL` or `BLOCKED`
that left unlanded work "is taken by a re-run", which the drive does not do. Nothing in the
manual says how to force one (deleting the result file, or another `--day`, does).

### PK15 (minor) — four mirror sites were not swept (V3)

- `CHANGELOG.md`: the entry `9b4a8f8f` adds covers the skills. Nothing records ccfleet's part-3
  changes (the seal contract, settled verdicts, the launcher-signal behaviour, the cost
  history's new basis, the instructions guard, the import split) or `modelguard`'s. One of them
  changes a default: an adopter whose user-level file names a private name now has every public
  repo's launch refused with exit 5.
- `tools/README.md`, the `modelguard` entry: still says it "fails closed after a head it does
  not know", the behaviour `fc922383` replaced.
- `instruments/README.md`, the `ccfleet` entry: still gives the requirements as python and git,
  and says nothing of the instruction-file guard, the settled verdicts or `plan`.
- `skills/work/run.md`, the twin of `close.md` ("the same stamped-copy rule"): `close.md` learned
  that a plugin root reached through a symbolic link prints the link's target, and that a
  pending edit may be another session's; `run.md` step 1 still says "prints that same path", so
  on such an install its test can read as failed and send the session to step 3, the working
  file.

### PK16 (minor) — what the tests would not notice (mutation, lens 3)

*Method:* 55 single-edit mutants of scratch copies (`<SCRATCH>/probes/mutate.py`, results in
`<SCRATCH>/mut/`), each run against the test classes that should catch it; **42 killed, 13
survived**. The six survivors in `ccfleet` and the reference queue were then applied together
and the whole `test_ccfleet` suite run once against them: 135 of 136 passed (exit 1); the one
failure, `test_pin_is_resolved_per_repo_or_said_unresolved`, fails the same way on the
unmutated copy, which is not a git checkout, so it is the copy's and not the mutants'. The
seven others were run against their whole test files, and their phrases appear in no other
test (grep).

What the tests hold firmly (killed): imports inlined for a public repo, an appended copy that
differs from what the guard reads, a silenced guard, `refuse` behaving as `warn`, copies never
removed, a signalled launcher that kills its session, a lost process record, settled words, the
first-line verdict, the shape line, the history's sum over sessions, an unranked drain, fences,
the hop limit, a refused claim counted as bad, each named widening, home paths, the drive's
reset, the fold after the reset, an unfilled placeholder, five of the six reference-queue rules
tried, eight of nine `modelguard` behaviours, each router's grant, the routers' shared text, the
close's body, an action file's grant, the example config's command shape, and the manual's
contract line.

What they would not notice (survived):

| Mutant | What it means |
|---|---|
| `M11` a `resume` treats every repo as private | nothing tests that a public repo's resumed session gets the public copy; claim 15's last clause is pinned for a private repo only |
| `M15`, `M15b` the two copies written world-readable | "owner-only" is in the manual and in no test |
| `M21` a settled end releases the claim | "A claim is never released on one" (`ccfleet:297-301`) is in no test |
| `M9b` the history counts a pass its resume left unfinished | "finished clean by a resume or fold" is tested only where the resume was clean |
| `Q2` the reference's `next` ignores the seal | the contract's "`ranked`, `next` and `take` each exit nonzero" is tested for `ranked` and `take` |
| `G6` an unparsable command naming `claude` is allowed | claim 19's deny is tested through the coarse path only, not the catch-all |
| `R3` `plan.md` loses "this file governs until it is fixed" | unpinned |
| `R4` `run.md` lets typed words stand in for an approval | unpinned; the one sentence that guards a paid approval |
| `R6` `run.md`'s un-claim rule weakened to allow a replacement reviewer | unpinned |
| `R5` `fold-prompt.md` loses its run-twice step | the prompt's steps are read by no test (placeholders only) |
| `R10` `MECHANISMS.md` reverts to "only when deliberately invoked" | unpinned |
| `R12` the bare-menu skill grants any python again | the six routers' grants are pinned; this seventh skill's is not |

*Counsel:* a test each for `M11`, `M15`, `M21` and `Q2` (they guard privacy, the claim and the
seal); the `run.md` sentences of `R4` and `R6` join the pinned phrases the delta already keeps
for that file.

### PK17 (note) — where the inliner and the harness part company (private repos only)

Probe `imp.py`: an import in an indented code block and one inside a block HTML comment are
inlined (the harness skips code blocks and strips block comments); an import inside a sentence
is left as text, which the harness would follow, and `check` does not list it, so a private
repo's session can silently lack a file the operator's own sessions get. The user-level
`rules/` directory is not appended at all. Four hops, cycles, relative paths, `~`, fences, code
spans, quoted paths, escaped spaces, a missing file, a directory, CRLF and a symlink all behave
as the comment at `ccfleet:612-620` says.

### PK18 (note) — the fold's run-twice check keys on a heading that carries the date

`fold-prompt.md` step 0 searches for "that step's heading"; step 2's heading ends
"(orchestrator, {DATE})" and the pass's own fold writes "<ISO date>". A fold re-run on a later
UTC day is asked to find a heading it would write differently. No test reads the prompt's steps
(mutant `R5`).

### PK19 (note) — what rests on the harness, and how far each was checked

See the live ledger. The read grant works in the CLI version installed here by a substitution
the documentation promises only for Bash rules; a future CLI that kept to the documentation
would turn every action's first read into a refusal in a headless session. In an in-place
install the read grant covers the whole checkout, its untracked files included.

### PK20 (note) — two stated residuals worth a line each

The config's `visibility` wins over the forge's answer, so a repo that went public and is still
marked private gets the private imports; the manual says so, and `check` could compare the two
where `gh` is there. And a launcher killed between its claim and its `START` line (no handler
is installed yet) leaves the claim, the worktree and both settings copies with no session; the
session id is on the claim, so it can be found, by hand.

## The claims ledger (the brief's 31, each re-driven)

State: **H** holds as written · **L** holds, with a limit found (the finding named) · **O**
overclaimed.

| # | State | How it was re-driven |
|---|---|---|
| 1 | L (`PK4`) | `harv.py`: a later mention no longer wins; an earlier one does |
| 2 | L (`PK1`, `PK2`) | SIGTERM and SIGHUP to a launcher (exit 143, 129): session left, record kept, `resume` exit 2 |
| 3 | L (`PK14`) | stand-in ends `BLOCKED` and `PARTIAL`: worktree removed, or kept with its untracked file; a re-run `drive` skips both |
| 4 | O (`PK11`) | `check` over a user-level `sandbox` block; grep of `check` for managed settings |
| 5 | L (`PK1`) | normal end: `<kit_dir>/settings/` empty; signal: emptied while the session ran |
| 6 | H | `check --prompt` on the three review prompts; a template with an unknown placeholder: exit 5 |
| 7 | H | a config with `vars` a list: exit 64; `~/x` and `~` expanded, `~user/x` and `a~/b` left |
| 8 | H | `repo_facts` on a no-remote repo with `branch` set: the branch read |
| 9 | H | both suites on 3.14.6 and 3.9.6; the three programs parse as 3.8 grammar; 3.8 itself not run (none here) |
| 10 | L (`PK10`) | world: unsealed `drain` exit 1 "not ranked"; hand `pass` exit 2; another run's id refused |
| 11 | H | reference `seal --by <the brief-writer's id>`: refused, exit 1 |
| 12 | O (`PK3`) | two-route probe; the command shapes compared with the example config (they match) |
| 13 | H | the shim's log of each call's arguments, beside `queue_call` |
| 14 | L (`PK12`) | `hist.py`: a clean pass, a resume, a fold on another model summed and split per model; a dry `.out` and a no-`END` pass not counted |
| 15 | L (`PK5`, `PK16`) | world runs with two config directories, `refuse` and `warn`; the appended copies captured |
| 16 | H | `mg.py`: `somewrapper -q claude -p x` passes, as stated |
| 17 | H | `mg.py` and the test table: each named shape denied |
| 18 | L (`PK13`) | 12 more shapes pass than the list names |
| 19 | H | an unbalanced quote naming `claude`: denied; empty stdin: exit 0; tests green on both |
| 20 | H (note `PK19`) | the pinned-grant tests; mutants `R1`, `R1b`, `R7` |
| 21 | H | read; pinned by `test_router_states_the_root_and_the_first_word_rule`; substitution read statically |
| 22 | H | read: the one rule, the one command |
| 23 | H | read at `MECHANISMS.md:22` and `:41-45` |
| 24 | H | read at `plan.md:57-73`, `:80-92`, `:93-103` |
| 25 | L (`PK6`) | read at `run.md:16-23`, `:159-168`; the clean test matches `harvest` |
| 26 | H | read at `run.md:223-251`; a fold wrote the pass's own result file in the world |
| 27 | H (note `PK18`) | read |
| 28 | H (`PK7` questions the rule, not the claim) | read at `close.md:42-91` |
| 29 | L (`PK14`) | read; the settled re-run probed |
| 30 | H | 19 and 16 tests, both interpreters, exit 0 |
| 31 | O (`PK15`) | grep of `CHANGELOG.md` for each ccfleet and `modelguard` change: none |

## Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `fc922383` (`modelguard`) | yes | `PK13`, `PK15` |
| `4a9318b7` (skills, grants) | yes | `PK6`, `PK7`, `PK16`, `PK19` |
| `9b4a8f8f` (changelog) | yes | `PK15` |
| `53203833` (pass lifecycle) | yes | `PK1`, `PK2`, `PK4`, `PK14`, `PK16` |
| `2d8e05e3` (lifecycle wording) | yes | `PK8`, `PK14`, `PK18` |
| `564a7ca4` (seal, cost, guard) | yes | `PK3`, `PK5`, `PK9`, `PK10`, `PK11`, `PK12`, `PK16` |
| `f4360a79` (import split) | yes | `PK5`, `PK16`, `PK17`, `PK20` |
| `a1cc5f2d` (context only) | yes | none recorded; nothing of `RK2`, `RK5` or `REVIEW_MODEL` was hunted or met as a defect |

## Re-run ledger

All from `<WT>`, 2026-11-25 UTC, exit codes read explicitly.

| Line | Result |
|---|---|
| `git merge-base --is-ancestor f4360a79 HEAD` | exit 0 |
| the since-line, `6ddbead2..HEAD`, on the delta paths | empty, exit 0 |
| `coldsweep --commit`, eight commits | exit 0 each |
| `mandoc -T lint -W style instruments/man/ccfleet.1` | no output, exit 0 |
| `python3 instruments/ccfleet --help` | exit 0 |
| `menu.py --selftest`, `menu.py review`, `menu.py session` | exit 0 each; `session` lists `close` and `onramp` |
| `review_queue_reference.py --help` | exit 0 |
| `python3 tools/modelguard.py </dev/null` | exit 0 |
| `nice -n 15 python3 -m unittest -q test_ccfleet` (3.14.6) | 136 tests, OK, 531.7 s, exit 0 |
| `nice -n 15 /usr/bin/python3 -m unittest -q test_ccfleet` (3.9.6) | 136 tests, OK, 636.5 s, exit 0 |
| `test_atelier_menu` | 4 tests, OK, exit 0 |
| `test_modelguard`, both interpreters | 8 tests, OK, exit 0, twice |
| `test_subject_skills`, both interpreters | 19 tests, OK, exit 0, twice |
| `test_session_close_single_source`, both interpreters | 16 tests, OK, exit 0, twice |
| the coldsweep line of *Deferred reading* | exit 0; hits in `ccfleet`, its example, manual and tests, and `modelguard` only |
| the CI floor at `6d71ea91` (`gh run list`, read-only) | `floor: completed success`; at `f4360a79` its own run was cancelled, which is not a pass at that commit |

The synthetic world's sixteen lines, with `CLAUDE_CONFIG_DIR` at the scratch directory:

| Line | Result |
|---|---|
| `check` | exit 0: `NO GRANT`, `GRANT`, `INSTRUCTIONS … Imports found: 1`, `INSTRUCTIONS IMPORT: @extra.md … inlined`, no guard line (only the imported file names the name) |
| `check --prompt <pass template>` | exit 0; the template printed twice (it is also `pass_prompt`) |
| `gate` (the gate's defaults) | `hold`, exit 1: load 55 and 3 GB of free disk at that moment; environmental |
| `plan`, `plan --json` | exit 0: one evidence row, one owed row, `local: no measurement` |
| `--by run-A drain --dry-run`, unsealed | the plan reading, then `DRAIN EXIT: queue error`, exit 1 (`PK9`) |
| `--by run-A drain`, unsealed | `refused: no ranking is sealed`, `DRAIN EXIT: not ranked`, exit 1 |
| `--by run-A pass <public repo> …`, unsealed | `claim refused: … no ranking is sealed`, exit 2; the worktree it had made was removed |
| `seal --by <the briefed_by id>` | refused: that session wrote the brief; exit 1 |
| `seal --by run-A … --words synthetic` | exit 0 |
| `--by run-A drain --dry-run`, sealed | one rehearsed pass (in its own `.out`), `DRAIN EXIT: queue empty`, exit 0 |
| `--by run-B drain --dry-run` | `queue error`, exit 1: "the sealed ranking is run run-A's" |
| `plan` with no `queue.evidence` | exit 64 |
| `run <public> --prompt <private-name template> --dry-run` | exit 5, the name printed |
| `run <public> --prompt <plain> --dry-run` | exit 0, `vis=PUBLIC` |
| `run <private> --prompt <plain> --dry-run` | exit 0, `vis=PRIVATE` |
| second config directory (the name in the file's own text): public, `refuse` | exit 5, before any worktree |
| the same, private repo | exit 0 |
| the same, `warn`, public | `INSTRUCTIONS name private name …` then the launch; exit 0 |
| the same, `warn`, private | exit 0, no line |

What the runs left, read afterwards: `driver.log` (each refusal and each end, as above); result
files for the real runs against `/usr/bin/false` (each `ERROR`, worktree `KEPT`); the claim on
the one drained pass held by `run-A` with its session id, result and log (the `ended` call); no
file under any `<kit_dir>/settings/` after a normal end; a `launched-<day>.txt` created even by
the drain that was refused at `ranked` (harmless); the shim's log in call order, with `ranked`
called once, by the real drain only, and never by a dry one or by `plan`.

## Live behaviour ledger

One real launch was tried, exactly inside the brief's bounds (haiku, a scratch directory, a
synthetic `CLAUDE_CONFIG_DIR`, a clean environment, the plugin loaded from `<WT>`, the bare
`/atelier:review`). It ended at once: "Not logged in", exit 1, `is_error` true, cost 0. On this
machine the CLI's sign-in belongs to the real config directory, the bounds bar that directory,
and no key is in the environment. So **every launch below is NOT RUN, on those grounds**, and
what could be learned without one is said beside it.

| Claim | Live | What was learned otherwise |
|---|---|---|
| an appended file's `@` imports are not followed | NOT RUN | CLI 2.1.302's bundled source: the file is read, decoded as text and joined; no import step |
| no user-level `CLAUDE.md` loads without the `user` source | NOT RUN | not established by me; the authors' comment only |
| the router grant, with the plugin root filled in | NOT RUN | bundled source: a plugin skill's whole `allowed-tools` string is substituted, then parsed; the documentation promises Bash rules only |
| bare `/atelier:review`, `review plan`, `session close` in a session with no grant | NOT RUN | none |
| `modelUsage`, `total_cost_usd` on a resumed session | NOT RUN | none (`A10`) |
| `--session-id` on the command line of the running process | NOT RUN with ccfleet | `ps` on this machine shows the arguments of all 7 running `claude` processes |
| a session whose `--settings` file is removed under it | NOT RUN | none (`PK1`) |
| an error end is never read as clean | seen once | the failed launch itself: exit 1, `is_error` true, `subtype` success; `harvest` reads that as ERROR |

A reviewer or the principal with a signed-in session can close these in a quarter of an hour;
the three that matter most are the first two rows and the last but one.

## Overall

**PASS-WITH-FINDINGS: 0 MAJOR, 5 MODERATE (`PK1`–`PK5`), 11 minor (`PK6`–`PK16`), 4 notes
(`PK17`–`PK20`).** The floor reproduces on both interpreters; the fixes do what their texts say
in every undisturbed path I could drive; the findings sit at the seams (a signal, a second
session, a broken prompt rule, a second route) and in what the texts claim beyond the code.

In three lines, as the brief asks:

1. **Does anything found lose, misread or mis-cost paid review work?** Not in an undisturbed
   run. With a second event, yes: a failed pass whose output carries an earlier line beginning
   `RESULT:` is read as done (`PK4`); a fold started beside a still-running session can release
   its claim and remove its worktree (`PK2`); the cost history can under-count a pass that was
   resumed twice (`PK12`). None of these loses a reviewer's written act that sits uncommitted
   in a worktree: the unlanded-work check held in every probe.
2. **Are `/atelier:review plan` and `/atelier:review run`, with `ccfleet` as part 3 leaves it,
   safe to run the principal's paid weekly drain from?** Yes, on three conditions that are not
   code changes: the estate's own queue keeps the seal on `ranked`, `next` and `take` and
   offers the drain only what is routed to the local budget (`PK3`; this pass could not open
   it); nobody signals a pass's launcher, and before any fold or un-claim the drain session
   reads `<kit_dir>/sessions/` and waits for a session still listed there (`PK1`, `PK2`); and
   the drain session reads each result file's text, not only its first line, before it counts
   a pass as done (`PK4`). Nothing found must change in the code first.
3. **Can anything in the delta put private context into a public repo's session?** Not by what
   ccfleet appends, as far as a stand-in and a reading of the installed CLI can show: the
   imported file is left out, the guard reads the same text that is appended, and a private name
   in the shared part refuses the launch. Two things remain open: the session is told where the
   private part is and nothing stops it reading the file where its grant reaches (`PK5`), and
   the two harness behaviours the split rests on were not run live (`A2`).

## Follow-up checklist

- [ ] `PK1`: decide where the settings copies' lifetime is tied; test them across a launcher
  signal.
- [ ] `PK2`: refuse a fold into a worktree a recorded live session runs in.
- [ ] `PK3`: put routes into the contract's `next`; make the reference keep `run.md`'s route
  rules; a two-route test.
- [ ] `PK4`: read the `RESULT:` line beside the shape line.
- [ ] `PK5`: deny the import targets to a public session; name the residual in THREATS.
- [ ] `PK6`, `PK7`: the principal's rulings on whose words the arguments are, and on whether
  typed words may skip a close step.
- [ ] `PK8`, `PK9`, `PK14`, `PK15`: bring `run.md`, the dry drain's account, `sweep.md` and the
  three mirror sites into step with the code.
- [ ] `PK10`, `PK11`, `PK12`, `PK13`: the seal's stated limits; `check`'s unclassified kept
  keys; dated log names; the hook's refusal text and its table.
- [ ] `PK16`: the tests named there.
- [ ] The live ledger's NOT RUN rows, by a signed-in session: an appended file's import, the
  user-level file under `--setting-sources project,local`, a session whose settings file is
  removed, and the three router commands in a session with no grant.
- [ ] Act 2: the `RK` ledger and the reconcile, on the orchestrator's release.

## Spawn prompt, verbatim (rule 4)

The orchestrator's wrapper message, the only text sent besides the file it names:

> Your full instructions are in this file; read it first and follow it exactly. It is also the
> text you record verbatim in your verdict's provenance, with the path substitutions it names:
> `<SCRATCH>/../pk-spawn-prompt.md` (This wrapper message is the only text sent besides that
> file; record it too.)

The file, whole, with the worktree written `<WT>`, the scratch directory `<SCRATCH>` and the
primary checkout `<PRIMARY>` as it asks; one further substitution is mine and of the same kind,
the other reviewer's worktree path, written `<the other pass's worktree>`:

````text
You are the reviewer for one rule-4 cold pass in the atelier repo. You run on Fable, the
principal-named review tier. State your model in your verdict's provenance.

**The brief:**
`<WT>/docs/reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md`
(board `160/1810`, finding prefix `PK`). Read it whole first, then follow it and
`docs/method/REVIEW.md` exactly. It defines the scope, the barred reading, the re-run list, the
deliverable and the two acts. Nothing here changes it.

**Your worktree:** `<WT>` (branch `atelier-e7-pk-pass`, HEAD
`6d71ea91`, which is `origin/main`). The commits after the brief (`0bdcbfe2`) are claims and
answers on board items under `docs/roadmap/160-doctrine-review-owed/`, which is on your barred
list; one of them records the principal's answer that `f4360a79` belongs in this pass, which the
brief already provides for. I ran the brief's since-line at `6d71ea91`: empty. Run every command
from the worktree, with absolute paths. It is read-only to you except the brief file, where you
append your verdict.

**Your scratch directory:**
`<SCRATCH>/`
(create it). All probes, scratch clones, synthetic configs, a synthetic `CLAUDE_CONFIG_DIR`,
fixtures and working notes go there. Delete your fixtures when you finish act 2.

**Who I am, disclosed (rule 4):** session `14c2530d` (`atelier-e7`), Opus 5.5, opened by the
principal with the instruction to brief and run this pass and one other (`160/1800`, the
drain-path fixes, whose Fable reviewer is running now in its own worktree). I am an off-tier
orchestrator: I hold the context partition, commit the records and release the held-back sibling
after your act 1 is committed. I form no finding and write no severity. I authored no part of the
delta. I wrote no part of the brief: I started its writer, headless session `075cdcd9` (Opus 5.5),
with a process-only prompt (the item, the method files, the model brief to read down to its first
verdict divider, the barred sessions, where the sibling goes, the house form). My exposure before
spawning you, disclosed in full: this brief's head, *What the work is* in part, the end of
*Re-run obligation* (*Live behaviour*) and *Process*; the `160/1800` brief most of the way;
`skills/review/brief.md` and `run.md` whole, `SKILL.md`; board items `160/1800` and `160/1810`
whole and `160/1790`'s first 60 lines (**authors' and earlier pass's accounts**); the two newest
session records whole, one of them the authors' own (**authors' account of this delta**); from
the earlier pass's file, its section outline, its *Spawn provenance* and *Process* sections and
its verdict's *Provenance* section (**so I have met that verdict's headings and provenance, not
its findings' text**); both brief-writers' closing notes. I have not opened the held-back
sibling. None of that is yours to read before act 1, and I pass none of it to you beyond this
paragraph. Record this prompt verbatim in your provenance, writing the worktree path as `<WT>`,
the scratch directory as `<SCRATCH>` and the primary checkout as `<PRIMARY>` (this repo is
public); it is saved at
`<SCRATCH>-spawn-prompt.md`.
The barred set is exactly the brief's; I add nothing and remove nothing.

**Process rules:**

1. **No git writes.** No commit, add, checkout, switch, stash, reset, push or worktree command in
   your worktree or anywhere else. Read-only git (log, diff, merge-base, ls-files, grep, and
   commits via `coldsweep`) is fine. I commit. A scratch clone under your scratch directory is
   yours to do as you like with.
2. **Never touch the primary checkout** `<PRIMARY>`: the live hook, the installed
   `ccfleet` and the in-place plugin run from it. Where the brief asks where it stands, use
   read-only `git -C <it> log -1 --format=%h` and `git -C <it> status --short` only, and read no
   file there; your worktree has the same commits. Never run an installed tool by bare name from
   `PATH`. Stay out of the other reviewer's worktree, `<the other pass's worktree>`.
3. **Machine load.** Other sessions are live on this machine, the other Fable reviewer among them;
   load was high (about 30 to 40 on 12 cores) shortly before I spawned you. Check `uptime` before
   each heavy step and wait while the one-minute load is above about 24; one heavy process at a
   time under `nice -n 15`, in the foreground with a 600000 ms timeout (the `ccfleet` suite takes
   about five minutes per interpreter). If the harness moves a long command to the background on
   its own, wait for it and disclose that. A wall-clock test that fails under load is
   environmental until re-run on a quieter machine; say which.
4. **Real launches:** you may spend on the brief's *Live behaviour* launches only: at most one
   `ccfleet run` of a public scratch repo and three headless `claude -p` sessions (bare
   `/atelier:review`, `/atelier:review plan`, `/atelier:session close`), all on the cheapest model
   (`haiku`), in throwaway directories under your scratch directory, with a synthetic
   `CLAUDE_CONFIG_DIR` and no permission-mode argument, exactly as the brief bounds them. No real
   config, no real repo, no `drive`, no real `drain`, never the real `CLAUDE_CONFIG_DIR`.
5. **Subagents:** if you start any, give each an explicit `model`, keep it read-only, and have it
   write its report to a file in your scratch directory and return three lines. Any subagent that
   reads the delta and forms judgement must be Fable; the findings and severities are yours.
6. **Public repo.** Quote no secret, email address, home path, private repo name, estate fact or
   other session's transcript content, and never open the private part of the user-level
   instruction file. Absolute ISO 8601 dates from `date -u`; NZ English; prose wrapped at about
   100 columns. Finding prefix `PK`.
7. **Act 1:** append your verdict below a `---` divider at the end of the brief file, complete per
   the brief's *Process*, then STOP and reply to me in at most five lines: that act 1 is written,
   the overall line with counts, and anything I must know to commit it. Do not open the held-back
   sibling or the earlier verdict. The sibling is not in the tree; I release its path to you by
   message after I commit act 1.
8. **Act 2** starts only on my release message. Do it as the brief's *Phase 2* says, then reply in
   at most five lines.
9. **If a usage limit or error stops you,** stop where you are; your transcript persists and I
   will resume you by message. Keep working notes in your scratch directory so a resume loses
   nothing.

Budget the time this large pass needs; never thin it to fit.
````

### Reconcile (act 2, 2026-11-25 UTC)

**Provenance of act 2.** Act 1 was committed unrevised as `a247f7f0` by the orchestrator before
anything below was opened; the review worktree was at that commit, clean, when I began
(2026-11-25T09:21Z), and the brief's since-line from my act-1 pin `6d71ea91` was empty (the two
commits between are the `160/1800` pass's verdict and its board item). The orchestrator's
release message, verbatim, with the held folder written `<HELD>`:

````text
Release: act 1 is committed unrevised as a247f7f0 on main (your worktree is rebased onto it; the only other commits since your HEAD 6d71ea91 are 49c7c56d and f790fe27, the 160/1800 pass's verdict file and its board item, neither on a delta path). I changed only the brief's Status line, to "ACT 1 COMMITTED … act 2 pending". Start act 2 per the brief's Phase 2. The held-back sibling is at <HELD>/atelier--2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.deferred.md (write it as a held user-local path in the record, never the home path). The earlier verdict and the barred records are now open to you; the 160/1800 verdict (docs/reviews/2026-11-25-0720-rk-drain-path-fixes-cold.md) is a sibling pass's, open to you now too, and you may note where it overlaps yours. Fold the sibling in verbatim below your reconcile; do not delete the held copy — I delete it after checking your fold. Update the Status line to the final verdict when you finish. Same process rules (no git writes; I commit). Reply in at most five lines when act 2 is written, and delete your fixtures.
````

It carries no question about the delta and asks for no finding to be revised.

**Opened in act 2, in this order:** the sibling whole (26 questions, 16 facts); the earlier
verdict's findings (`RK1` to `RK28`), its reconcile, `RK29` and its restated lines (its brief,
method record and folded sibling not read: the ledger needs the findings and their evidence);
the intent records `210/600` and `210/610` whole; the seven delta commits' message bodies; this
pass's own board item, its head; the `160/1800` verdict by its findings' headings, its restated
overall and a search for what touches mine. Not opened, with grounds: `docs/sessions/`,
`docs/method/census/` and the other barred items (no row of the ledger turns on them). One
thing to disclose: to answer the sibling's question 20 I ran the installed CLI's `--help` by
its bare name, a read of its flag list and nothing else. No real launch was made. Act-1 text
is unchanged.

**Residual risk, named.** The RK ledger is anchored on the earlier verdict by design: I re-drove
what it found, where it found it. Act 1 is the cold half; `PK1` to `PK20` were formed before any
of this was read.

#### The RK ledger

Each row re-driven at `a247f7f0` on 2026-11-25 UTC, in scratch, unless it says "text" (a finding
about wording, where the changed text at HEAD is the re-drive) or "static" (the installed CLI's
bundled source, where a launch was not possible). "Counsel" points at the earlier verdict's own
words under each id.

| RK | Answered by | Re-driven at HEAD | State |
|---|---|---|---|
| `RK1` an action's read is refused | `4a9318b7`: each router's `allowed-tools`, line 5 | live: NOT RUN (no login in a synthetic config directory; act 1's ledger). Static: CLI 2.1.302 fills the plugin root in a plugin skill's whole `allowed-tools`. The authors' own live run is in the commit body and cannot be re-run by me | **Fixed as counselled** (the counsel's first branch: `Read` in the router's grant). Seen to work by the authors, not by this pass. Residue: `PK19` |
| `RK3` last `RESULT:` wins | `53203833`: `RESULT_RX` `ccfleet:284`, `result_word` `:954-967`, `harvest` `:1044-1047` | the earlier verdict's three reproductions: the NOTES mention reads FAILED; the one-sentence end reads UNKNOWN; a non-JSON log holding the line reads UNKNOWN | **Fixed as counselled**, to the letter ("take the first … and require the shape line"). The counsel itself moves the risk to an earlier mention: `PK4` |
| `RK4` a signalled launcher's session runs unwatched | `53203833`: `launch` `:1143-1203`, `live_session` `:1116-1136`, `resume` `:2479-2484`, `drain` `:1967-1978` | SIGTERM and SIGHUP: session left, record kept, `resume` exit 2; a second resume beside a live one: exit 2; the drain's line, by test and mutants `M5`, `M6`, `M31` (killed) | **Fixed as counselled** for `resume` and the drain's line. Not closed for the fold (`PK2`); the fix's exit path removes the settings copies (`PK1`) |
| `RK6` what a resume and a fold leave | `53203833` (`pass_result_path`, `write_result`), `2d8e05e3` (`run.md`, `fold-prompt.md`) | a resume and a fold each headed the pass's own result file in the world; `run.md` prints `--by <session-id>` on both commands (text); the fold's default label is `<repo>-<item>`; "almost nothing" is defined (text); the fold has a run-twice step (text) | **Fixed as counselled**, all four parts and the reconcile's addition. Residue: `PK18`; the run-twice step and the un-claim rule are pinned by no test (`PK16`) |
| `RK7` the seal has no interface | `564a7ca4`: docstring *THE SEAL*, manual *The seal*, the reference queue, `RKGrant` tests | world: unsealed drain exit 1, hand pass exit 2, another run's id refused; the seal's refusals by test and mutants `Q1`, `Q3`–`Q6` (killed) | **Fixed as counselled** (contract stated where the queue commands are; a reference queue the tests drive). Limits: `PK3`, `PK10`; `next`'s refusal unpinned (`Q2`, `PK16`) |
| `RK8` the cost estimate | `564a7ca4`: `pass_history` `:2156-2248`, `plan.md` step 4 | `hist.py`: resumes and folds joined and summed, per repo and per model; "for a review of that size" is gone from `plan.md` (text); notional said (text and plan output) | **Fixed as counselled**, with the reconcile's notional-figure point. The reviewer's-share question is answered by `modelUsage` on the authors' reading of old logs, "no launch"; a hand-run pass is still not counted, and said. Residue: `PK12` |
| `RK9` ordinary commands refused | `fc922383`: `launch_like`, the unknown-head loop `modelguard.py:608-624` | the earlier verdict's sixteen refused commands and `docker run --name claude img`, on the hook's interpreter: none refused; the refusal now says how to rephrase | **Fixed as counselled.** The cost moved, as the body says, to a stated false allow; unstated residue on both sides: `PK13` |
| `RK10` the instruction file unscanned | `564a7ca4` (`guard_instructions`), then `f4360a79` | world: refused by default (exit 5), `warn` prints a line per name; mutants `M2`, `M3` killed | **Fixed as counselled, and then beyond it** (`210/610`: the principal's answer, a shared file importing a private one). The going-beyond is sound for what is appended; `PK5`, and `M11` in `PK16` |
| `RK11` the copies never removed | `564a7ca4`: `session_files` `:716` | removed after every normal end in the world; mutant `M4` killed | **Fixed, and regressed at one seam:** the body says "atexit, so the session has ended; never while it runs". On the `RK4` path the process exits while the session runs (`PK1`) |
| `RK12` more exceptions than listed; silent when nothing is granted | `564a7ca4` (`WIDENING_KEPT`, `PERMISSION_FLAGS`, `NO GRANT`), `4a9318b7` (the fleet prompts) | `check` in the world prints `NO GRANT`; `WIDENS` lines by test and mutants `M22`, `M28` (killed) | **Fixed as counselled** for every key the earlier verdict named. The class is open: `PK11`. The estate-side half is `160/1800`'s |
| `RK13` "owed" narrower than the doctrine | `4a9318b7`: `plan.md:57-73`, `:104-115` | text | **Fixed as counselled**, with the reconcile's "near" point. "This file governs" is unpinned (`R3`) |
| `RK14` typed words have no home | `4a9318b7`: `run.md:16-23` | text | **Fixed as counselled.** It now meets the trigger-phrase route: `PK6` |
| `RK15` nine shapes pass | `fc922383` | the nine, on the hook's interpreter: all denied; `Workflow` named as unseen (text) | **Fixed as counselled.** More shapes found: `PK13` |
| `RK16` a traceback with no `queue` | `53203833`: `one_pass` `:2422-2427`, `resume` `:2477-2478` | `pass` with no queue: exit 64, no worktree made; `resume --item` with no `release`: exit 64 | **Fixed as counselled** |
| `RK17` landing line names `None`; branch left | `53203833` (`worktree_branch`), `2d8e05e3` (the fleet prompts) | the two tests named for it pass; in the world's no-remote repos, every cleanly removed worktree's `fleet/` branch is gone and only kept worktrees have one | **Fixed as counselled** |
| `RK18` `check --prompt` misfiles names | `564a7ca4`: `check` `:2610-2638` | `check --prompt` on the three review prompts: `{BRIEF}` is UNSET, `{ITEM}` and `{REVIEW_LOG}` listed apart | **Fixed as counselled** |
| `RK19` the prose guards | `4a9318b7`: both guard tests | five of the earlier verdict's named mutations re-made: a rule added inside an anchored paragraph, the plugin root one level up, the read-only rule replaced, "every run" made optional, an action that does not exist: all killed; a widened grant killed (`R1`) | **Fixed as counselled**, by digests where anchors had failed. What the digests do not cover: `PK16` |
| `RK20` the close's delivery text | `4a9318b7`: `close.md:42-91` | text; `ccclose` is read-only by its own help | **Fixed as counselled** for the four points. **Against the reconcile's addition:** it had noted that typed words "may narrow a step away"; the fix forbids it outright, which is a rule the earlier verdict did not ask for (`PK7`). The twin file was not swept (`PK15`) |
| `RK21` the example's `take` records no id | `564a7ca4`: the example config | the shim's log: `take … --set session=<uuid>`; mutant `R8` killed | **Fixed as counselled** |
| `RK22` the rename's mirrors | `4a9318b7` (manifests, onramp, the wider sweep), `9b4a8f8f` (changelog) | manifests list sixteen and count sixteen (test); the changelog's entries read against the code | **Fixed as counselled** for what it named. The same class recurs for part 3 itself: `PK15` |
| `RK23` small disagreements | `564a7ca4` | each of the nine read at HEAD: skills point at the manual's THREATS; `plan` is among what starts nothing; a failed `next` exits 1; the example's `branch` sits on a no-remote repo; `~/` expanded (probed); per-command placeholders; two earlier log names; `{PIN}` in `run.md`; the manual's date | **Fixed for those named.** New ones: `PK8`, `PK14` |
| `RK24` `PARTIAL` and `BLOCKED` re-run for ever | `53203833` (`SETTLED_ON`), `2d8e05e3` (`sweep.md`) | world: both settled, the clean one's worktree removed, a re-run skips both | **Fixed as counselled.** The fix meets a new source of `BLOCKED` made in the same delta: `PK14`; "a claim is never released on one" is unpinned (`M21`) |
| `RK25` (note) refused claims; `drive` and the reset | `53203833` | by test and mutants `M18`, `M24` (killed) | **Fixed.** `run.md` still states the old behaviour: `PK8` |
| `RK26` (note) what the suites do not pin | `53203833`: three tests | the three run and pass; `--force` re-made as a mutant: killed. The two `modelguard` mutants re-made: the parse-failure deny switched off stays green (`G6`), and so does `--resume` taken out of the session flags | **Partly fixed:** three of five. The body says so of the other two ("not in ccfleet"); nothing took them up |
| `RK27` (note) `work plan`, the first word, `MECHANISMS.md` | `4a9318b7` | text; mutant `R11` killed, `R10` survived | **Fixed as counselled** |
| `RK28` (note) the runtime line | `564a7ca4` | text, in the docstring, `--help` and the manual; both tested interpreters run by me | **Fixed as counselled.** `instruments/README.md` still gives the old requirements (`PK15`) |
| `RK29` a standing yes to any python and git | `4a9318b7`: each router, line 5; `test_router_grant_is_pinned` | mutants `R1`, `R1b`, `R7` killed | **Fixed as counselled**, both halves (narrowed, and pinned). The seventh skill, the bare menu, is narrowed and unpinned (`R12`) |

**In sum, of 27:** 24 fixed as counselled (most with a residue named above), one fixed and
taken beyond the counsel on the principal's own answer (`RK10`), one fixed and regressed at a
seam (`RK11`), one partly fixed (`RK26`). **None is not fixed.** Three fixes moved a risk
rather than ending it: `RK3` (to `PK4`), `RK4` with `RK11` (to `PK1`, and `PK2` left open),
`RK24` (to `PK14`). One went against the direction the earlier reconcile pointed (`RK20`,
`PK7`). **`RK2` and `RK5` are `160/1800`'s:** I met neither as a defect; my mutant of the
fold-after-reset exemption (`M29`) was killed.

#### Against the authors' account (commit bodies and `210/600`, `210/610`)

- `564a7ca4`'s body: the copies are removed "atexit, so the session has ended; never while it
  runs". False on the signal path the sibling commit `53203833` made (`PK1`). The two workers'
  fixes meet at that seam and neither body sees the other.
- `53203833`'s body names what moved for `RK25`; `210/600` adds "the live-session check rests on
  `ps` showing the session id" (my `A4`, confirmed on this machine). Neither names the fold
  (`PK2`) or the earlier-mention reading (`PK4`).
- `4a9318b7`'s body records three headless probes: a single-slash read rule still refused, the
  double-slash one "let session close run end to end", a bare word showing the menu. That is
  better evidence than the changelog's one clause suggests, and it agrees with what I read in
  the CLI. I could not repeat it.
- `fc922383`'s body states its trade plainly and matches the code. Its "28 NAMED rows" are data
  uses; none is a long option's value followed by `-p` (`PK13`).
- `564a7ca4` on `RK8`: `modelUsage` "checked against the shape of existing CLI logs, no launch".
  So `A10` (whether a resumed session's total is its own run's) is untested by anyone.
- `f4360a79` and `210/610`: "checked on it: the public text names no private name and does not
  reach the imported part … a fresh session loads both". The last clause is about an ordinary
  session, not a ccfleet one; whether the harness follows an import in an appended file is
  claimed by neither, and `A2` stays as act 1 left it.
- `9b4a8f8f`'s body lists what its entries cover; it was written before the three `ccfleet`
  commits landed, which is how `PK15`'s first bullet came about.
- `210/600` hands two things down to the estate root: its drain config's `pass_prompt` path,
  and a choice on `instructions_guard`. Both are outside this pass and both gate a paid drain.

#### Against the sibling's questions

| Q | Outcome |
|---|---|
| 1 | Checked in act 2: the seven commits touch nothing outside the brief's path list, and no other commit after `a1cc5f2d` touches it, so the brief's scoping was right. The pointer's grammar is **new at reconcile: `PK21`** |
| 2 | **Found in act 1** as `PK9` |
| 3 | Seen in act 1 (the re-run ledger: the rehearsed pass is "in its own `.out`") and not raised. Added to `PK9` |
| 4 | **Found in act 1** as `PK10` |
| 5 | Not found in act 1. Added to `PK10` |
| 6 | Checked in act 1 by reading: the drain re-asks `next` per pick and each pass calls `take`, so a lapse stops new picks on a queue that keeps the contract; one that checks only `ranked` does not, and nothing tests an adopter's queue (lens 1) |
| 7 | **Checked in act 1** (`A4`): the process id and the session id on its command line; a record whose process is gone is removed when read; a reused id belonging to something else does not hold the session id, so no refusal for ever |
| 8 | **Found in act 1** as `PK14` |
| 9 | **Found in act 1**: `PK1`, and `M15` in `PK16`. Nothing sweeps them; the manual says to delete them by hand |
| 10 | Checked in act 1: the earlier end is kept below in both paths (`write_result`); two resumes are locked; a fold beside a session is `PK2`; a fold beside a resume has no lock (same class) |
| 11 | **Checked in act 1**: with a dry `.out` and a real one in `logs/`, `plan` read "1 pass(es) seen" |
| 12 | Checked in act 1 (`hist.py`): a fold's model takes its own row in the per-model split, so "per model" is every session's model, not the reviewer's share alone; `plan.md` says "per model" and no more. No finding |
| 13 | By reading: a pass is found only through a `pass-*.out`, so a run job's log is never counted and a hand-run pass is missed, as the note says |
| 14 | **Act 1, `A2`:** not live; by the CLI's source, no |
| 15 | **Act 1, `A2`:** unverified |
| 16 | Act 1, lens 4, in part: the match ignores case (`re.I`); a name split across lines is not caught (a literal match); an unknown-visibility repo is never inlined; the settings copy's `env` and hook commands are not read |
| 17 | Not raised. The manual gives the reason refusal is the default; under `warn` the line is in a `.out` nobody reads live. It is the adopter's stated choice. No finding |
| 18 | **Found in act 1** as `PK17`: `..`, an absolute path and a symlink all reach outside the directory (the operator's own file, a private repo's session only); an unclosed fence swallows the rest, as Markdown does |
| 19 | Probed in act 2: of the nine named, the eight known wrappers are caught; `systemd-run --user -q claude -p x` passes (the stated class). Added to `PK13` |
| 20 | Probed in act 2. Added to `PK13` |
| 21 | Probed in act 2: of the five, only `kubectl logs claude -c main` is refused, as the docstring says |
| 22 | **Act 1, `A7`:** static, yes |
| 23 | **Checked in act 1**: `ccclose` writes nothing. A repo cannot put another `ccclose` ahead on the path without a hook or an `env` block of its own, which is the manual's first threat already |
| 24 | By reading: the bare-menu skill is installed by a link into the user-level skills folder in both shapes, so the path is right unless the config directory is moved; unpinned (`R12`) |
| 25 | **Found in act 1** as `PK7` |
| 26 | **Found in act 1** as `PK6`, from the other side: the two statements agree only if the model passes the action as the first word, and then the remaining words are its own |

Of 26: act 1 had found or checked 17; four carry text added here (3, 5, 19, 20); one is a new
finding (1); one was probed now with no finding (21); three are answered now by reading, with
no finding (13, 17, 24).
Act 1 raised findings no question reaches: `PK2`, `PK3`, `PK4`, `PK5`, `PK8`, `PK11`, `PK12`,
`PK15`, `PK16`. The sibling's facts agree with my re-run ledger wherever both ran the same
line; its world gave the local route a lapse time and mine did not, which is why only mine met
`PK10`'s first point.

#### Finding formed at reconcile

**`PK21` (minor, formed at reconcile, from question 1 and `210/610`). The queue pointer named
its delta by citation, and one change to a privacy guard landed with no pointer at all.** The
`160/1810` pointer says "the commits citing `210/600`"; three of the seven commits on its own
path list do not (`fc922383`, `9b4a8f8f`, `f4360a79`). The brief-writer caught it by reading
paths. `210/610` is doctrine by function (it decides what an unattended session in a public repo
is told), was landed by the authoring session, and its item closed with no review line; it is in
this pass only because the brief took it in and the principal then answered that it belongs
here. Criterion: `REVIEW.md` rule 4, landing is queuing, and *omission is the bug*.
*Counsel:* a pointer names its delta by path and bound; `pointerscan` could warn on one that
names it by citation alone.

#### Additions to act-1 findings (formed at reconcile; severities unchanged)

- `PK9`: with the seal, the dry drain's own output ends "queue empty" and names no pick; the
  rehearsed launch is only in the pass's `.out` and the driver log (question 3).
- `PK10`: the reference's refusal to seal a brief-writer's own brief binds only where the
  drain's id is the writer's own; a writer is usually a worker with another id, and the id is
  the caller's to choose (question 5). The texts say it "may refuse", which is as far as it goes.
- `PK13`: the long-flag table is "`claude --help`, v2.1.302", and that help lists flags the
  table lacks, among them `--settings`, `--effort`, `--background`, `--worktree`, `--tmux` and
  `--bare`; after a short option, a launch that carries only those and a prompt passes. Nothing
  notices the CLI's flags moving (question 20). `systemd-run --user -q claude -p x` joins the
  passes (question 19).
- `PK15`: the sibling pass found the same of its own three fixes (`DV5`).
- `PK2`: the sibling pass's `DV6` is the other face of the same seam: on the reference queue a
  fold under another id cannot release. Both say the fold's identity is not checked against
  the pass it finishes.

#### Per-finding state after reconcile

`PK1` to `PK20` stand as written in act 1, at their act-1 severities; none is raised, lowered or
withdrawn. Against the authors' account: `PK1` is contradicted by a commit body and stands on
the probe; `PK4` is the counsel applied as given; `PK7` is the authors' own addition; `PK19`'s
live gap is narrower than I wrote, since the authors did run it. `PK21` is added.

**Overall, restated: PASS-WITH-FINDINGS. 0 MAJOR, 5 MODERATE (`PK1`–`PK5`), 12 minor
(`PK6`–`PK16`, `PK21`), 4 notes (`PK17`–`PK20`).** 21 findings; one, `PK21`, formed at
reconcile. Of the 27 earlier findings this delta answers, none is unfixed, one regressed at a
seam (`RK11`, `PK1`) and one is partly fixed (`RK26`).

The three plain lines, restated, unchanged in substance:

1. **Lose, misread or mis-cost paid review work?** Not undisturbed. With a second event: `PK4`
   (an earlier `RESULT:` line), `PK2` (a fold beside a live session), `PK12` (a twice-resumed
   pass under-counted).
2. **Safe to run the paid weekly drain from?** Yes, with no code change required first, on the
   three operating conditions of act 1, and on the two hand-downs `210/600` names for the
   estate's own config (its `pass_prompt` path; its `instructions_guard` choice), which this
   pass could not open. The decision is the principal's.
3. **Private context into a public repo's session?** Not by what ccfleet appends. Open: the
   session is told where the private part is (`PK5`); a public repo's resume is unpinned
   (`M11`); and the two harness behaviours stand on reading, not on a run (`A2`).

Scratch fixtures were deleted after this was written. The held copy of the sibling is left for
the orchestrator, as it asked.

## Deferred sibling, folded below the verdict (reviewer, 2026-11-25)

Held user-local by the orchestrator at
`<HELD>/atelier--2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.deferred.md`,
outside the repo, every worktree and any scratchpad, until act 1 was committed as `a247f7f0`;
released to the reviewer for act 2; folded here verbatim by the reviewer, headings and all.

# Held back: seeded questions and facts for the `160/1810` cold pass

Sibling of `docs/reviews/2026-11-25-0721-rk-part-3-fixes-ccfleet-modelguard-subject-skills-cold.md`
(atelier). Written by the brief-writer, headless session `075cdcd9` (`atelier-e0`, Opus 5.5), on
2026-11-25 UTC, at pin `6ddbead2`. Held user-local, outside the repo, every worktree and every
scratchpad. The orchestrator releases it to the reviewer only after the reviewer's act 1 is
committed; the reviewer then folds it in below its reconcile and this file is deleted.

These are the brief-writer's own seeded questions: a floor, never a fence (rule 1). They are what
an off-tier, non-reviewing writer noticed while extracting claims; none is a finding, none carries
a severity, and their topics say where this writer looked, not where the risk is.

## Questions (26)

**Scope**

1. The item's pointer names its delta as "the commits citing `210/600`" after `a1cc5f2d`. Two RK
   fixes on its own path list (`fc922383`, `modelguard`; `9b4a8f8f`, the changelog, citing `RK22`
   in its subject) do not cite `210/600` in subject or message, and `f4360a79` (`210/610`) rewrote
   the guard after the pointer was written, with no pass of its own. Is the pointer grammar a
   recurring defect class (a landing that queues by citation rather than by path), and should
   `pointerscan` or the queueing rule catch it? Was it right for this brief to take all three in?

**The seal and the drain path**

2. With no seal, `drain --dry-run` exits 1 with `DRAIN EXIT: queue error`, because `next` refuses
   (fact 9). `run.md` prints the plan, then seals. Is a dry drain before the seal now useless as a
   rehearsal, and does "queue error" read to an operator as a fault rather than "not sealed yet"?
3. With the seal, the dry drain's stdout ends `DRAIN EXIT: queue empty` though `driver.log` says it
   "started" one pick (fact 11). Does any skill or operator read the dry drain's stdout for what
   would run, and does the pick line belong there?
4. The seal is keyed by `--by`. A hand `ccfleet pass` with the drain's own `--by` meets the seal as
   that run's (fact 10). Is a seal a control against an unplanned pass, or only against a pass from
   a session that does not know the run's id? Who else can learn it?
5. The reference queue refuses a seal by the session that wrote a brief (`briefed_by == by`,
   fact 12). Brief-writers are often workers whose ids differ from the drain session's, and a
   drain's `--by` is chosen by the caller. Does that check bind anything real, and does the manual
   or `run.md` overstate it?
6. `ccfleet` calls `ranked` once and trusts its exit. Does a seal that lapses mid-drain (the
   first lapse among routes) stop new picks, given `next` and `take` re-check it per call in the
   reference queue but an adopter's queue might check only `ranked`?

**The pass lifecycle**

7. A launcher sent `SIGTERM` or `SIGHUP` leaves its session running and its pid in
   `<kit_dir>/sessions/`; a resume is refused while it runs. How is "still runs" decided: by pid
   alone? After a reboot or pid reuse, can a resume be refused for ever, or allowed while a reused
   pid belongs to something else?
8. `PARTIAL` and `BLOCKED` are settled: a drive will not start the job again, and a no-claim run's
   worktree is removed when it holds no unlanded work. A `BLOCKED` caused by a missing grant
   (`sweep.md`'s new rule) is transient; is it now never retried, and does anything put it in front
   of the principal?
9. The settings copies are removed `atexit`. On `SIGKILL` of the launcher, or a reboot, they stay
   under `<kit_dir>/settings/`. What do they hold (kept `env`, hooks, MCP approvals), with what file
   permissions, and does anything sweep them?
10. A resume or a fold now writes its verdict into the pass's own result file. Is the pass's
    cut-off end kept below in every path, and can two folds, or a fold and a resume, race on it?

**The cost history**

11. A dry drain leaves a `pass-*.out` with `result=DRY` under `logs/` (fact 11). Does the cost
    history skip it in every path, and does `passes_seen` count it?
12. A pass finished by a fold on a cheaper tier is one completed pass summed over its sessions, and
    split per model by `modelUsage`. Is the per-model split the reviewer's model share, or does a
    fold's model take a share of "the pass", and does `plan.md`'s estimate say which?
13. The hand-run note now reads "a pass run by hand (no .out; its log is not told apart from a run
    job's)". Can a run job's log be counted as a pass, or a pass's log be missed?

**The instructions file and the guard**

14. For a public repo, the appended file carries the import line as text. Does the real harness
    follow an `@` import inside a file given by `--append-system-prompt-file`? If it does, the
    private part reaches every public session, and the guard reads only the line. Live-drivable
    with a synthetic `CLAUDE_CONFIG_DIR` and a marker.
15. Does `--setting-sources project,local` stop the harness loading the user-level `CLAUDE.md` on
    its own, across CLI versions (the code's comment says "checked against claude 2.1.x")? If not,
    the guard reads one copy and the session gets two.
16. The guard matches the config's `private_names` against the appended text. Does it catch a name
    split across lines, in another case, inside an inlined import for an unknown-visibility repo,
    or in the kept hooks' commands and `env` the settings copy carries into a public session?
17. `instructions_guard: warn` appends the file anyway with a line per name. Who sees that line in
    an unattended drain, and should `warn` be refused for a public repo, as a prompt naming a
    private name is (exit 5)?
18. The inliner's rules ("relative to the importing file, `~` is home, four hops, none inside
    code"): does an import path with `..` or a symlink reach outside the user-level directory, and
    does a fenced block that never closes swallow later imports?

**`modelguard`**

19. Which real wrappers are "unknown heads" given a short option before `claude` and so pass
    (`caffeinate -i`, `script -q`, `stdbuf -o0`, `ionice -c3`, `taskset`, `chrt`, `unbuffer`,
    `flock -n`, `systemd-run --user -q`)? Each is a launch with no model that passes.
20. `CLAUDE_LONG_FLAGS` is pinned to CLI 2.1.302. When the CLI adds a session flag, does the hook
    fail open after an unknown head? Does any test or check notice the CLI moving?
21. Which ordinary commands does the widened reading now refuse (`kubectl logs claude -c main` is
    named; `docker exec -it claude bash -c "…"`, `journalctl -u claude -p err`, `ps -o pid -p …`,
    a `git -c core.pager=` with `claude` in a pager command used for search)? Each refusal blocks
    every session that types it.

**The routers and skills**

22. The grants use `${CLAUDE_PLUGIN_ROOT}` in front matter, and `Read(/${CLAUDE_PLUGIN_ROOT}/**)`
    relies on the root being absolute so the leading slash makes `//`. Does the harness substitute
    that placeholder in `allowed-tools` at all? If not, every router's grant names a literal string
    and the RK1 fix does nothing. Live-drivable.
23. `Bash(ccclose:*)` pre-approves any `ccclose` on `PATH` with any arguments, while the session
    skill is active. Does `ccclose` have a mode that writes, and can a repo's own files put another
    `ccclose` ahead on `PATH`?
24. `instruments/atelier-menu/SKILL.md` grants `python3 ~/.claude/skills/atelier/menu.py`, a
    user-level path, not the plugin's. Is that the path that skill runs from in both install shapes?
25. `close.md` now says the typed brief "never removes a step: where the typed words would skip
    one, run the step anyway". The typed words are the principal's. Does that override his own
    narrowing, against the apex's *The principal's authority is absolute*?
26. `MECHANISMS.md` now says a casual phrase can reach an action through a router's trigger words
    ("wrap up" can reach the close). The routers say a first word not in the table shows the menu.
    When a model reaches the skill on a phrase, what first word does it pass, and do the two
    statements agree?

## Facts (16)

Read off the machine by the brief-writer on 2026-11-25 UTC, at `94f2b9a3` unless stated.

1. Root lines: `merge-base --is-ancestor f4360a79 HEAD` exit 0; `mandoc -T lint -W style` exit 0, no
   output; `ccfleet --help` exit 0; `menu.py --selftest` exit 0 ("lists subjects' actions and plain
   skills, one subject on its own, skips junk"); `menu.py session` exit 0; `menu.py review` exit 0
   (at `6ddbead2`); `review_queue_reference.py --help` exit 0; `modelguard.py </dev/null` exit 0, no
   output.
2. `test_ccfleet`: 136 tests OK on 3.14.6 (exit 0, 291 s) and on `/usr/bin/python3` 3.9.6 (exit 0,
   293 s), load average about 8 to 17 during the runs. `test_atelier_menu`: 4 OK.
3. `test_modelguard`: 8 test methods (table-driven), OK on both interpreters (about 15 s each).
   `test_subject_skills`: 19 OK on both. `test_session_close_single_source`: 16 OK on both.
4. Every `coldsweep --commit` read of the seven delta commits exited 0 (with the path set in the
   brief; `CHANGELOG.md` matched nothing in `4a9318b7` and printed a note). The since-line at
   `6ddbead2` was empty. The brief's sweep command exited 0 (output not read by the writer).
5. `git log --grep=210/600 a1cc5f2d..HEAD` lists `08db83fd` (board and session record only),
   `564a7ca4`, `2d8e05e3`, `53203833`, `4a9318b7`; not `fc922383`, `9b4a8f8f` or `f4360a79`.
   `210/610` is closed with no review pointer; no `160/` item names `f4360a79` or `210/610`.
6. Synthetic world: built by a script under the writer's scratchpad (deleted at the end), as the
   brief describes; the queue shim logged each call and ran the reference queue from the worktree;
   `REVIEW_QUEUE_NOW` 2030-01-05T10:00, route `local` open, lapsing 2030-01-06T23:00.
7. `check` exit 0. It printed the config, then lines headed `NO GRANT` (default mode, "every call
   that would ask" refused), `GRANT` (the config is the whole grant; `--setting-sources
   project,local`; left out: nothing), `INSTRUCTIONS` (the scratch `CLAUDE.md` appended; a private
   repo's session gets imports inlined, a public or unknown one gets it as it stands),
   `INSTRUCTIONS IMPORT: @<path> -> <path>: inlined`, `REPO SETTINGS` (a repo's own settings still
   load; each launch prints `WIDENED`), and `PROMPT …: 3 placeholder(s)`. `check --prompt` exit 0.
8. `gate` exit 0 with the config's permissive gate; it read disk 7 G free (6 G by `df -g` later).
9. `plan` and `plan --json` exit 0: one evidence row ("in the queue's own order (not a ranking)"),
   one owed row, `local: no measurement`, four NOTE lines (local only; per completed pass summed
   over sessions, reviewer subagent included, no size measured; list price, notional on a
   subscription plan; a hand-run pass not counted). Unsealed `--by run-A drain --dry-run`: the same
   reading prefixed `DRY plan:`, then `DRY queue.ranked not called`, `DRAIN EXIT: queue error`,
   exit 1 (`driver.log`: `queue next failed rc=1: refused: no ranking is sealed`).
10. Unsealed `drain` (real, `claude_bin` false): `refused: no ranking is sealed`, `DRAIN EXIT: not
    ranked`, exit 1. Unsealed hand `pass … --by run-A`: `claim refused: refused: no ranking is
    sealed`, exit 2; the shim logged `take` with `--set session=<uuid>`.
11. Seal by the `briefed_by` id: refused ("wrote its brief, so it may not run it"), exit 1. Seal by
    `run-A`: exit 0. Sealed `--by run-A drain --dry-run`: stdout the plan, `DRY queue.ranked not
    called`, `DRAIN EXIT: queue empty`, exit 0; `driver.log`: `started pubrepo 100/010 (1/1 …)`,
    `END … rc=0 result=DRY`, `queue: nothing launchable now`, `drain down: queue empty (1
    started)`; it left `logs/pass-pubrepo-100-010-<HHMMSS>.out` holding the DRY lines. No
    `launched-dry.txt` remained afterwards; `launched-reset-2030-01-06T2300.txt` existed, empty.
12. Sealed `--by run-B drain --dry-run`: `DRAIN EXIT: queue error`, exit 1 (`driver.log`: "the
    sealed ranking is run run-A's, not run-B's").
13. No `queue.evidence`: `plan` exit 64 ("plan needs queue.evidence in the config …").
14. Public repo with a prompt naming the private name: `refused: the prompt for pubrepo (PUBLIC)
    names private name(s) …`, exit 5. Plain prompt, public and private repos, scratch `CLAUDE.md`
    whose import holds the name: both exit 0, `DRY argv` carrying `--session-id`,
    `--setting-sources project,local`, `--settings <kit_dir>/settings/<uuid>.json` and
    `--append-system-prompt-file <kit_dir>/settings/…`. `<kit_dir>/settings/` was empty after each
    process exited.
15. With a second scratch `CLAUDE.md` naming the private name in its own text: public repo refused
    (`… names private name(s) …, and pubrepo is PUBLIC; take the names out of it, or set
    instructions_guard to …`), exit 5; private repo exit 0; public repo under `warn`: an
    `INSTRUCTIONS name private name …` line, then the DRY launch, exit 0.
16. The queue shim's call order across the whole run: `evidence, owed` ×3 (plan, plan --json, dry
    drain), `next --skip-file <kit_dir>/launched-dry.txt --by run-A`, `ranked --by run-A`, `take
    pubrepo:100/010 --by run-A --brief … --set session=<uuid>`, `evidence, owed`, `next` ×2 (sealed
    dry drain), `evidence, owed`, `next --by run-B`. Machine: the user-level hook runs
    `/usr/bin/python3 -I <primary>/tools/modelguard.py` on `Agent|Task|Bash`; the primary checkout
    was at `efeccf16`, clean, on `main`; `~/.local/bin/ccfleet` links to the primary's copy;
    `ccclose` is on `PATH`; CLI 2.1.302; one enabled plugin entry in the user-level settings.
