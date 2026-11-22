# Cold pass — `ccfleet`, the `fleet-sweep` and `review-drain` skills, and `modelguard`

**Board:** `docs/roadmap/160-doctrine-review-owed/1450-rule-4-cold-pass-queued-ccfleet-fleet-sweep-review-drain-modelguard.md`,
with `docs/roadmap/160-doctrine-review-owed/1660-rule-4-cold-pass-queued-drain-ranks-and-routes-first.md`
folded in (one pass, one verdict, closing both)
**Status:** BRIEF ONLY, not run. Written 2026-11-20 UTC by a brief-writer worker of queue run
`08cd3b95` (Opus 5.5), at `71c867bc`. **Updated 2026-11-20 UTC to `bd9f6a9b`** by a second
brief-writer worker of the same run, taking in `c60dee8b` and `bd9f6a9b` (below) and folding in
`160/1660`, whose subject is `c60dee8b`. **Updated again 2026-11-21 UTC to `b68cf410`** by the
same run's orchestrator, which authored no part of the delta: that commit, by a worker of
session `19378351` (already barred below), rewords the fleet sweep's healthy item 6 and two of
its prompt templates for the session log's move into `docs/sessions/`. **Updated a third time
2026-11-21 UTC to `e002ea22`**, by the same orchestrator, on a delta note from that commit's
author session `64f984ac` (already barred).
**Approval:** the principal approved one Fable pass for this item on 2026-11-20 UTC, verbatim:
*"I approve one pass so that ccfleet can be fixed and is ready to use. But the parallel session
working in this repo right now is making changes based on my directions and they may change what
it is the reviewer is reviewing. Once that session is finished we can update the brief if things
have changed and then run the one fable review"*. One pass, covering `160/1660`'s subject too;
run only once the delta has stopped moving (re-check the since-line under *What the work is*
before you start, and stop if it is not empty).

**Pass type:** code and design cold pass, per `docs/method/REVIEW.md` rule 4. Two skills that
stamp behaviour into every plugin user, their prompt templates, and a hook that denies tool calls
are doctrine by function (rule 3); the instrument that runs them is reviewed with them as one
commitment.
**Tier:** Fable, the principal-named review tier, checked at selection by whoever takes the pass.
A session that cannot run on it stops (rule 4).
**Size of this pass:** large. Ten commits; at `bd9f6a9b`, about 1,090 lines of standard-library
Python, 640 lines of tests, a 950-line manual page, 540 lines of skill text and prompt templates
(all eight files of the two skills), a 180-line hook with its 70-line test, and the README and
changelog entries. Budget the time; never thin the pass to
fit it (`REVIEW.md`, *Budget decides how many reviews run and when, never how a review is run*).
**Drain priority:** normal (principal, 2026-11-18), as the item records.

**Why it earns a review.** `ccfleet` starts headless Claude Code sessions, with whatever
permission mode its config passes, inside a worktree of every repo an estate lists, unattended, and
decides from their output whether a review claim is released or held. The two skills are what a
plugin user's session follows when the principal says "sweep the repos" or "drain the reviews".
`modelguard` sits in front of every `Agent` and `Bash` call where it is wired. The worst failures:

- **Paid review work lost or silently redone.** A pass cut off by a usage cap, a crash, a reboot
  or a closed terminal whose claim, worktree, session id or review log cannot be recovered, so the
  budget spent on it is gone, or a finished pass misread as unfinished (or the reverse). This is
  why the principal gated the estate's drain switch on this pass (below).
- **Blast radius.** One config mistake (a permission mode, a repo list, a private name left off
  the list, a prompt variable) reaches every repo in one run; a public repo's prompt or record
  carrying a private name is a publication that cannot be retracted.
- **A false allow from the hook.** A `claude` launch with no model that `modelguard` passes is the
  silent failure: a green hook read as "every launch names its model". A false deny costs a retry;
  a false allow costs nothing visible.
- **A skill that stamps a wrong rule** into every adopter's sessions: the widest blast radius in
  the operating model (rule 4).
- **The wrong reviews bought, or quality traded for price.** Since `c60dee8b` a drain starts
  nothing until the adopter's queue says the whole queue is ranked and routed; the order and the
  route decide which paid reviews run and on which budget. A gate that can be passed without a
  ranking, or a routing rule that sends a review to a route that cannot match a local pass, spends
  the budget against the principal's rule.
- **A sweep that acts where it should ask.** Since `bd9f6a9b` the fleet sweep adopts every
  unarchived, unforked repo with no pin and gives a repo with no board an empty store, rather
  than putting either to the principal.

## Spawn provenance

- **Authors of the work under review.** Session `559edaec` (Opus 5.5, headless, started
  2026-11-14 by an estate health sweep, orchestrator session `58027096`) wrote the first landing.
  Queue run `78ca9153` (Opus 5.5, principal-opened, 2026-11-16) and its workers wrote the manual
  page and the `--help` digest. Session `84b7932e` (Opus 5.5, principal-opened, 2026-11-18) and the
  workers it started wrote the gap fixes and the three fixes of `1eb42f54`. Session `64f984ac`
  (Opus 5.5, principal-opened, 2026-11-20) wrote `c60dee8b`, the ranking gate, and queued its own
  pass as `160/1660`. Session `19378351` (principal-opened, 2026-11-20) wrote `bd9f6a9b`: the
  commit adds roadmap `010/240`, which names that session as its finder, and carries out what that
  session's item `010/230` owes the skill (the commit's body was not read; a search of it for a
  session id printed nothing).
- **Who wrote this brief:** a brief-writer worker (Opus 5.5) of queue run `08cd3b95`, a
  principal-opened orchestrator of 2026-11-20; a second worker of the same run updated it to
  `bd9f6a9b`. Neither worker nor their orchestrator authored, started or instructed any part of
  the delta. **Off-tier for review, disclosed: the brief-writers form no finding and write no
  severity**, and stop after writing. They ran no review and used no Fable model. Queue run
  `08cd3b95` will not start the pass.
- **Barred from running this pass:** session `08cd3b95` and every worker it started (whoever
  writes a brief does not run it); sessions `559edaec`, `58027096`, `78ca9153`, `84b7932e`,
  `64f984ac` and `19378351`, and everything each of them started or instructed.
- **Contact, disclosed (rule 4).** The brief-writer's only instruction came from its orchestrator
  `08cd3b95`: the item number, the rule-4 standing above, the delta's paths, the house form, and a
  list of where to test hardest (the permission-mode blast radius, the two skills' reach, the
  hook's false allow, the gap fixes and the last commit's three fixes, and whether the drain loses
  paid review work on a crash or a cap). That list restates the item's own pointer and the gating
  reason the board records; it is disclosed here because it shaped the brief's emphasis. No author
  session contacted the brief-writer.
- **Contact for the update, disclosed.** The updating worker's only instruction came from the same
  orchestrator: take in `c60dee8b`, `bd9f6a9b` and anything else on the delta paths since
  `71c867bc`; fold in `160/1660` and its "what to test hardest"; find `bd9f6a9b`'s author. That
  "what to test hardest" was written by `c60dee8b`'s author session (`64f984ac`) in its own queue
  item, so its four points, folded into the lenses below and marked **(1660)**, are an author's
  framing: a floor, never a fence. No author session contacted the updating worker.
- **Who reviews:** a fresh Fable session started for this pass alone, by a session that passes rule
  4's criterion. An orchestrator may hold the context partition and commit the records off-tier,
  only if it forms no finding, writes no severity, and is disclosed in the claim, the pointer and
  the verdict, with its spawn prompt and release message in the verdict's provenance.
- ⚠️ **Brief-writer's exposure, disclosed** (author-account material met before writing): its
  launch prompt; `skills/review-brief/SKILL.md` whole; `REVIEW.md` rules 1 to 4, the lenses, the
  re-run section, the checklist, the lifecycle and *When to review*; the held-back-material
  paragraph of `CONCURRENCY.md`; the queue pointer `160/1450` whole; the intent record `210/440`
  whole and the item `450/010` whole (**both carry the authors' account** of the work and of the
  gap fixes); the delta at HEAD read in full except the manual page (linted, not read); commit
  subjects and file stats (`git show --stat --format=`, which prints no message body); the first
  lines of item `115/410`; a recent brief and a brief-writer session record, for house form; the
  results of the re-run lines below. It did **not** open any prior verdict or any delta commit's
  message body. Its harness also loaded user-level and repo instruction files and a memory index,
  which hold private context this brief does not carry. Everything evaluative it formed is in the
  held-back sibling.
- ⚠️ **Updating worker's exposure, disclosed:** its launch prompt; this brief and its sibling
  whole; `160/1450` whole and `160/1660` whole (**both carry the authors' account**: the latter is
  `c60dee8b`'s author's own pointer, and the former now records the delta moving); items
  `010/230` and `010/240` whole (**both carry `bd9f6a9b`'s author's account** of the gap it
  closes); the two new commits read body-free through `coldsweep`, plus one search of
  `bd9f6a9b`'s body for a session id that printed nothing; the rule-4 paragraphs of `REVIEW.md` on
  disclosed contact; a `cclive` listing; the results of the re-run lines at `bd9f6a9b`; two
  searches of the session log and session records for the two authors' ids, which printed nothing.
  It opened no prior verdict and no session record. Everything evaluative it formed is in the
  sibling.

## The acceptance test

Judge the work against what it claims (its docstrings, manual, skills and changelog) and against
the doctrine it must keep:

- **The principal's words.** 💬 Asked on 2026-11-18 when the estate's weekly drain should switch
  onto these, his pick, verbatim: *"After its review (Recommended)"*: the switch waits for this
  pass to come back clean. It is an answer to a question, not a ruling. The ruling that binds the
  drain's behaviour is quoted in `REVIEW.md` § *When to review*: *"Quality is more important than
  cost. If we run out of budget then we will resume the work when the budget replenishes"*. A
  drain that cannot resume what a spent budget cut off fails that sentence. For the ranking gate,
  his words are quoted in the delta itself (`skills/review-drain/SKILL.md` § *Rank and route the
  whole queue first*); judge the gate and the routing rule against them and against the quality
  sentence above. For `bd9f6a9b`, his words of 2026-11-20, verbatim: *"I want all repos to use the
  doctrine way of managing work on its board. If the repo is archived or a fork of someone elses
  repo then it is an exception and its left as is"* · *"the estate health check skill needs to find
  things like this and fix them when a repo does not meet doctribe rule like this"*; and two
  answers (picks from offered options, not rulings): a never-adopted repo, *"Adopt it fully"*;
  `CHANGELOG.md`, *"Keep one file, exempt (Recommended)"*.
- **The rules the drain enforces on others.** `REVIEW.md` rule 1 (the deferred split and the
  context partition), rule 2 (barred reading), rule 4 (spawn criterion, tier at selection, the
  off-tier orchestrator's two conditions), *The lifecycle* (method record); `CONCURRENCY.md`
  § *Orchestrated queue runs* (where held-back material lives, never a scratchpad or a reviewer's
  working directory); `ECONOMICS.md` (tier set by risk; the model named on purpose).
- **The public-repo rule.** `docs/PERSONAL-DATA.md` and the repo-craft purpose rule: a generic
  tool in a public repo carries no estate's names, and its config example is fictional.

## What the work is

Eight commits on `main`, in order:

- **`4bfb4e16`** — `instruments: version the fleet kits as ccfleet, two skills and modelguard
  (210/440)` (2026-11-14)
- **`b2ea715c`** — `instruments: ccfleet man page and a one-screen --help (210/440)` (2026-11-16)
- **`17f158d2`** — `instruments: close ccfleet's generic gaps so an estate can switch onto it`
  (2026-11-18)
- **`d9d1589e`** — `review-drain: keep a private review log per pass and count verdicts from rows`
  (2026-11-18)
- **`a025636e`** — `fleet-sweep: nothing left behind, read each ask in context, search before
  asking` (2026-11-18)
- **`1eb42f54`** — `ccfleet: make a fresh kit_dir, stop on a failing queue, end dry passes`
  (2026-11-18)
- **`c60dee8b`** — `review-drain: rank and route the whole queue before a drain starts`
  (2026-11-20; the subject of `160/1660`, folded in)
- **`bd9f6a9b`** — `fleet-sweep: a missing board fails health; forks exempt; no-pin repos
  adopted` (2026-11-20)
- **`b68cf410`** — `sessions: retire the one-file index; the folder is the session log`
  (2026-11-20 UTC; on the delta paths only `skills/fleet-sweep/SKILL.md`, `task-prompt.md` and
  `worker-prompt.md`. The rest of that commit, the retirement tool and its doctrine, is the
  subject of its own pass, `160/1700`; read it only as far as the sweep now relies on it.)
- **`e002ea22`** — `review-drain: route to the budget that lapses first, cost breaks a tie`
  (2026-11-21 UTC; on the delta paths `skills/review-drain/SKILL.md` and its `CHANGELOG.md` entry)

No other commit touched the delta paths between `71c867bc` and `e002ea22`.

Delta paths, read at HEAD and commit by commit:

- `instruments/ccfleet`, `instruments/ccfleet.example.json`, `instruments/test_ccfleet.py`,
  `instruments/man/ccfleet.1`, `instruments/README.md` (the `ccfleet` row and the requirements
  paragraph)
- `skills/fleet-sweep/` (`SKILL.md`, `worker-prompt.md`, `task-prompt.md`, `brief-prompt.md`)
- `skills/review-drain/` (`SKILL.md`, `orchestrator-prompt.md`, `resume-prompt.md`,
  `fold-prompt.md`)
- `tools/modelguard.py`, `tools/test_modelguard.py`, `tools/README.md` (§ *`modelguard.py`*)
- `CHANGELOG.md`: the entries dated 2026-11-14, 2026-11-18, 2026-11-20 and 2026-11-21 that
  name `ccfleet`, the two skills or `modelguard`

First confirm the tree holds the whole delta, then read each commit body-free:

```
git merge-base --is-ancestor e002ea22 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit 4bfb4e16 --path instruments --path skills \
  --path tools/modelguard.py --path tools/test_modelguard.py --path tools/README.md \
  --path CHANGELOG.md
```

Repeat the `--commit` line for each of the other nine commits (`b2ea715c`, `17f158d2`,
`d9d1589e`, `a025636e`, `1eb42f54`, `c60dee8b`, `bd9f6a9b`, `b68cf410`, `e002ea22`). Plain `git show` is barred: it
prints the message body before the diff, and reading is atomic (rule 1). Several of these commits
also touch the board, the intent record and a session record (`c60dee8b` adds a session record
and `160/1660`; `bd9f6a9b` adds `010/240`; `b68cf410` touches doctrine, session records and
the board; `e002ea22` adds a session record section and a delta note on `160/1450`); those are barred until phase 2, so always pass
`--path`.

Then check what has landed on the delta paths since: `git log --oneline e002ea22..HEAD --
instruments/ccfleet instruments/ccfleet.example.json instruments/test_ccfleet.py
instruments/man/ccfleet.1 instruments/README.md skills/fleet-sweep skills/review-drain
tools/modelguard.py tools/test_modelguard.py` (empty when this brief was last updated, at
`e002ea22`). The principal's approval is for a pass over a delta that has stopped moving: if this
line is not empty, stop and hand back for the brief to be updated again. Otherwise review the code
as it stands at your HEAD, and pin that SHA in your verdict's scope.

**Machine-local surfaces no other review will catch** (read-only; report them in public-safe
terms, never a home path or a private name):

- The user-level `~/.claude/settings.json` wires `modelguard` as a `PreToolUse` hook on
  `Agent|Bash`, run as `/usr/bin/python3 -I <the primary checkout>/tools/modelguard.py`. That
  interpreter was Python 3.9.6 when this brief was written; the repo's tests ran on the
  `python3` on `PATH`, 3.14.6. The hook runs the primary checkout's copy, not a worktree's.
- `~/.local/bin/ccfleet` is a link to the primary checkout's `instruments/ccfleet`.
- The plugin manifest (`.claude-plugin/plugin.json`) declares no skill list; every directory
  under `skills/` ships to every plugin user.
- Free disk sat near the gate's default floor (20 GB) at both writings, below it at the update, so
  `gate` may answer "hold" on this machine for reasons unrelated to the code.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the authors' claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1); these are a floor, never a fence.

**`ccfleet`**

1. Per-repo cost tools label usage by the session's working-directory basename, so a `claude -p`
   session started in `<worktrees_root>/<label>-<HHMM>/<repo>` bills `<repo>`, and an `Agent`
   subagent bills its parent's repo. `run --in` refuses a worktree whose basename is not the repo.
2. "A public repo's prompt never names a private repo": rendering refuses (exit 5) a prompt for a
   public or unknown-visibility repo that contains a configured private name, or the name of a repo
   the config marks private, matched as a whole word; "it catches the names you list and nothing
   you forgot to list".
3. The headroom gate starts a session only while one- and five-minute load, free memory and free
   disk all have headroom, and an unreadable memory figure holds (fails closed) unless
   `min_mem_pct` is 0.
4. `--dry-run` prints the launch and starts nothing (its help text: "print the launch, start
   nothing"; the epilogue: "`--dry-run` prints the launch instead").
5. Every launch names its model, takes stdin from `/dev/null`, and runs with
   `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`, without which "`claude -p` kills a background subagent
   about ten minutes after the orchestrator's last turn".
6. When the last turn printed no `RESULT:` line, the verdict is read from the session's own
   transcript, and only entries stamped since the launch count, "so a resumed session never takes
   an earlier run's verdict".
7. The drain stops on: the queue empty, the reset, a stop file newer than the driver, a `RESULT`
   in `stop_on`, or three unclean ends in a row, which "is how a spent budget shows up from
   outside". A failing queue `next` stops it with exit 1 and is never read as an empty queue.
8. A pass that ends with a `RESULT` outside `release_on` keeps its claim and its worktree, for
   Mode 2 (`review-drain` Mode 1 step 4); `resume` finishes it in its own session, releases on a
   clean end, exits 2 and keeps the worktree when the release is refused.
9. A pass and its resume share one private review log path outside any repo, "so it survives a
   reboot" and "a revived reviewer finds it".
10. Children start in their own session, "so closing the driver's terminal does not end the
    sessions it started"; one driver per `kit_dir`; the ceiling in `<kit_dir>/max` is live; a stop
    file older than the driver is ignored and logged; the launched list is keyed by `reset_utc`
    so a drain crossing UTC midnight keeps one list.
11. A fresh `kit_dir` is made by the driver lock; a dry pass prints the same `END` line a real one
    does, so a dry drain no longer counts its passes as ended early.
12. Python, not zsh, "on purpose": a running driver is immune to an edit of its own file, while a
    job started after the edit runs the edited copy.
13. The exit codes (0, 1, 2, 3, 4, 5, 64) are as the docstring, `--help`, the manual and the
    README state, and every one is reachable.
14. "Runtime: Python 3.8 or later, standard library only".
15. The changelog's test counts ("17 tests" on 2026-11-14; "17 new tests" on 2026-11-18) and every
    flag `--help` prints being in the manual page (pinned by a test).

**The skills and their prompts**

16. `fleet-sweep`: its definition of healthy (the seven items), the billing rule ("repo work
    never runs as an Agent of the orchestrator"), and that item 7 acts only on what is "provably
    this sweep's own or provably stale" and lists the rest; the ask de-duplication's check before
    any bulk ask.
17. `review-drain`: the four rules (never block the queue on a question; back to back; never stop,
    hold or reorder another session's review work; survive the session), "reviews run only on the
    review tier", "after the budget resets, nothing new starts", and that a reviewer that cannot be
    reached at resume is never replaced or moved to a lesser model.
18. The per-pass orchestrator prompt keeps rule 1's partition (the sibling copied out of the
    worktree before the reviewer starts, released after act 1 is committed) and rule 4's two
    conditions on an off-tier orchestrator; the fold prompt runs no review-tier model.
19. Every placeholder a template uses is filled by `ccfleet` or by a config `vars` entry the skill
    tells the adopter to set, and an unfilled one is a refusal, "not a silent gap".
20. Neither skill, prompt nor example names a real estate, repo, person or host; every estate value
    comes from the adopter's private config.

**`modelguard`**

21. It denies every `Agent` call with no `model` (a fork is exempt) and every Bash command that
    starts or resumes a `claude` session with no `--model` (or `ANTHROPIC_MODEL=`), through the
    wrappers and shells it names; management subcommands and heredoc bodies pass; a malformed
    payload never blocks; a script that launches `claude` itself is invisible, a stated limit.
22. Its deny reason states the rule `ECONOMICS.md` holds, in words that agree with it.

**Added by `c60dee8b`: the ranking gate (`160/1660`, folded in)**

23. `drain` refuses a config whose `queue` lacks `ranked` ("a drain config without it is
    refused"), and calls `ranked` once, with `{BY}`, "before the first pick"; any nonzero exit
    "starts nothing": it prints `DRAIN EXIT: not ranked` and exits 1. The interface is "drain
    only": `run`, `drive` and `resume` do not call it.
24. `ranked` "exits 0 only when the whole queue, every repo's, has been ranked and routed for this
    run"; "the adopter's queue judges; ccfleet only refuses".
25. The skill's § *Rank and route the whole queue first*: it runs "every run, before any pass
    starts"; "it is a gate, not a habit"; the adopter's queue makes `ranked` (and `next`) refuse
    until this run's ranking is sealed. The rank order (the principal's direction first, then
    importance, urgency, risk mitigated and value unlocked; a pass whose core needs a live write
    last; a standing repo order breaks ties only); each review to "the cheapest route that reaches
    local quality", among routes the principal has opened, and "unsure means the dearer route:
    quality is never traded for price"; a seal that refuses while any ready review is missing,
    unreasoned, on a closed route or dearer than it fits without saying why, and "lasts one
    budget"; the expiring budget's route takes its own first, then any other route's not yet
    started; a review briefed after the seal runs last on the local route until re-ranked.
26. Mode 1 step 1 now names `queue.ranked`, and "the drain starts nothing until" the queue is
    ranked, routed and sealed.
27. The surfaces that state the queue interface agree on it: the docstring (`{next, ranked, take,
    release[, ended]}`), the manual ("Each of the four entries"), the example config and the
    changelog; two new tests pin the two refusals.

**Added by `bd9f6a9b`: the fleet sweep's board and scope rules**

28. Healthy item 6 now also fails a repo with "no board at all", which "gets the empty store"
    (`docs/roadmap/` with its `README.md`, and the generated index); a frozen pre-split archive is
    cut into the store "once roadmap `010/220` has built and proved the cut; until then it is
    reported, not touched"; `CHANGELOG.md` and reference documents are exempt, with the grounds the
    skill gives.
29. The survey: "archived repos and forks of another owner's repo are exempt, and are left as they
    are. Every other repo is in scope: one with no pin is adopted (`/atelier:create-repo`,
    standardise mode), not put to the principal as a question."

**Added by `b68cf410`: the sweep's record-store rule after the session log moved**

30. Healthy item 6 now reads: session log → "the folder `docs/sessions/` alone, one file per
    session, the folder its own index"; a repo "still keeping a session index (`docs/SESSIONS.md`,
    with any `SESSIONS-ARCHIVE.md`) fails it", is retired by `tools/archivecut.py --cut` "with its
    proof", and "the worker then rewords the repo's own onramp and docs that tell a session to read
    or append to it". A frozen `ROADMAP-DONE.md` "is cut into the store by the same tool". The task
    prompt now asks for "this repo's session file for the work (`docs/sessions/<date>-<HHMM>-<slug>.md`,
    start time in UTC)" in place of "this repo's session-log entry".

**Added by `e002ea22`: routes ordered by when each budget lapses**

31. Step 3 now routes each review "to the route that reaches local quality and whose budget
    lapses soonest", "the cost per review breaks a tie"; the seal refuses "while two budgets are
    open and either lapse time is unknown"; and "the local route takes its own first, then any
    other route's not yet started, but never from a budget that lapses before its own". The
    skill's paragraph above step 1 paraphrases the principal's clarification; his words are kept
    private (they carry figures), so the paraphrase is the public record. The author's own
    question: do the lapse-first order and that spill rule match the clarification as the skill
    states it? Also trace whether `ccfleet` or any other surface in the delta still says
    "cheapest first" or lets the expiring budget's route spill as before.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:**

- Any estate's private ccfleet config, rulings file, queue tool and run results. Grounds: they are
  private by the split `210/440` records, this repo is public, and the delta's claim is that the
  code is generic. Judge the design through `ccfleet.example.json` and synthetic configs. Do not
  open a real config.
- The other tools homed under `450/010` (the menu, the status line, `prefixhook`, `secretguard`,
  `deadhook`, `stashscan`, `treeline`, `pins.py --floor`); they have their own passes. In scope
  only where the delta relies on them (`tools/pins.py` for `{PIN}`).
- The user-level `fable-drain` skill the estate still runs; it is not in this repo.
- Any estate's own `ranked` command, its ranking, routes and seal, and the batch and API-credit
  routes themselves: the adopter's, kept private, as the skill says. Judge the gate's contract
  and the skill's rules, with a synthetic `ranked` script.
- Roadmap `010/210` and `010/220` (the index shape and the archive cut the skill defers to); they
  are not built in this delta. In scope only as far as the skill relies on them.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   Is a cwd basename the right billing key, and a literal name list the right privacy guard? Is
   "three unclean ends in a row" a sound reading of a spent budget, and the `RESULT` word in a
   session's last text a sound signal for releasing a paid claim? Is a hook reading Bash text the
   right control for "every launch names its model"? Does putting these in a public plugin, so
   that every adopter receives two skills that run unattended sessions, match the repo's own rules
   for a deliberate widening (`CLAUDE.md` § *Autonomy*; `AUTONOMY.md`)? Is an exit code from the
   adopter's own command a sound gate for "rank first, every run", when ccfleet cannot see what
   was ranked? **(1660)** Does the routing rule ("unsure means the dearer route") hold against the
   principal's rule that review quality is never traded for price? Is adopting a no-pin repo
   without asking the principal a reading of his words above, or a widening of them?
2. **Correctness & quality.** Re-drive the claims above against the code, by probe, not by
   reading. Trace what survives, and where, when a pass is interrupted at each point of its life:
   before the claim, after the claim and before `START`, mid-session (a usage cap; a `SIGKILL`; a
   reboot; the driver's terminal closed; the driver itself killed), after the session and before
   the release. For each, say whether the claim, worktree, session id, review log and verdict can
   be recovered with what the tool and skill record, and whether `resume` can take it from there.
   Record each overclaim against the text that makes it, including any claim no test pins.
   **(1660)** Can any drain path pick a pass before `ranked` returns 0: a dry run, a resume, a
   restarted driver? Is a config with no `ranked` refused everywhere it should be and nowhere else
   (`run` and `drive` do not need it)? For `bd9f6a9b`: what the sweep does to a repo with no
   board, a fork and a no-pin repo, traced through the skill's own steps.
3. **Completeness / harvest.** Every surface that states the queue contract, the exit codes, the
   template variables, the stop conditions or the drain's rules agrees (docstring, `--help`,
   manual, README, skills, prompts, changelog: V3 and V5). One home per fact (V4). Find tests that
   would stay green on a broken delta by mutating a scratch copy of `ccfleet` and of `modelguard`.
   What the delta duplicated or ignored that atelier already holds (the queue-run skill, the
   review-brief skill, `cclive`, `ccrepo`, `pins.py`).
4. **Security & privacy**, mandatory. Design altitude: an unattended session with a permission
   mode in every repo (what a wrong config or a hostile repo's `CLAUDE.md` can make it do), the
   private-name guard's reach, what the review log and result files collect and where they sit.
   Code altitude: the likely vectors for the class, checked against an open catalogue (OWASP ASVS
   or the domain's equivalent), not recalled: values from the config, the jobs file, the queue's
   output and session transcripts flowing into paths, argv, prompts and git commands; and, for
   `modelguard`, every way a launch with no model can pass the hook (a hook that fails open on a
   parse it cannot make is the same class as a false allow). Aim `/security-review` at the code
   only from a clean tree; weigh a clean pass over markdown as nothing. **(1660)** Is the
   principal's quote in the ranking section, and the paraphrase beside it, public-safe in a skill
   every plugin user receives?

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once, on 2026-11-20 UTC, at `71c867bc`,
and the updating worker ran every line again at `bd9f6a9b`, from the places named; both sets of
results are held in the sibling. Read exit codes explicitly. Check
`uptime` first; one heavy process at a time, under `nice -n 10`, foreground with a long timeout
(the `ccfleet` suite takes about a minute).

From the worktree root:

```
git merge-base --is-ancestor e002ea22 HEAD; echo "exit=$?"
mandoc -T lint -W style instruments/man/ccfleet.1; echo "exit=$?"
python3 instruments/ccfleet --help; echo "exit=$?"
```

From `instruments/` (the test loads `ccfleet` by path; run it on both interpreters, since the
runtime claim is 3.8 or later):

```
nice -n 10 python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 10 /usr/bin/python3 -m unittest -q test_ccfleet; echo "exit=$?"
```

From `tools/` (the second line is the interpreter the user-level hook runs under):

```
nice -n 10 python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 10 /usr/bin/python3 -m unittest -q test_modelguard; echo "exit=$?"
```

**A dry run on a synthetic config**, in your scratchpad only. Make a throwaway git repo with no
remote under a scratch `repos_root`; a config whose `kit_dir`, `repos_root` and `worktrees_root`
are scratch directories, `claude_bin` set to `/usr/bin/false` (so nothing can start a real
session), one repo marked public, one invented private name, a `pass_prompt` template, and a
`queue` whose `next`/`ranked`/`take`/`release` are a small scratch script that offers one pick
until it is in `{LAUNCHED}` and whose `ranked` exit code you can set; a copy of the config with
no `queue.ranked`, and its own `kit_dir`. Then, with `--config` on each:

```
python3 instruments/ccfleet --config <cfg> check; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> gate; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <repo> --prompt <template> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <repo> --prompt <template naming the private name> \
  --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by <your id> drain --dry-run; echo "exit=$?"
```

Then the ranking gate (**1660**), each against a fresh `kit_dir` unless the line says otherwise:

```
<ranked set to exit nonzero>  python3 instruments/ccfleet --config <cfg> --by <your id> \
  drain --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg without ranked> --by <your id> drain --dry-run; \
  echo "exit=$?"
python3 instruments/ccfleet --config <cfg without ranked> run <repo> --prompt <template> \
  --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by <your id> drain --dry-run; echo "exit=$?"
  # the same kit_dir as the first dry drain, the same day: a second rehearsal
```

Read `<kit_dir>` afterwards: `driver.log`, and every file the dry runs left, and the scratch
queue script's own log of the calls it received, in order. The brief-writers ran this shape once
each; how they built their configs is in the sibling.

**Live behaviour.** The claims about real `claude -p` (stdin, the JSON log, the wait ceiling, the
transcript store's layout and timestamps, the billing label) rest on a stand-in binary in the
tests. Re-drive what you can read-only: the transcript store's file layout and the shape of an
entry's `timestamp` and `type`, read through a scratch script that prints keys and counts, never
content; `ccrepo`'s labelling rule from its source. At most one real launch, and only if the
session running you may spend on it: `ccfleet run` on a throwaway repo under your scratchpad, the
cheapest model, a prompt that only prints a `RESULT:` line, no permission-mode argument; else mark
it NOT RUN with grounds. Never run `ccfleet` against a real repo, never `drive` or `drain` for
real, and never with a real config. The brief-writer ran none of this.

## House rules for this run

- **Live systems:** read-only reads as needed; no live writes. A check that needs a write is
  marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Other sessions' transcripts are read only through
  a script that prints keys and counts; quote none of their content. Probes use scratch copies and
  synthetic fixtures under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad, and
  never touch the primary checkout (the hook and the installed `ccfleet` run from it). Child repos
  are read-only and reported by count only, never by name or path.
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

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, every item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title (`160/1660` included), the eight delta commits' message bodies, `docs/method/census/`
(it holds other sessions' assessments of these tools), and beyond their first line:

- `docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md`
  (the intent record)
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md`
  (it carries the authors' account of the gap fixes)
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md`
- `docs/roadmap/010-board-store-migration-per-item-files-mik/230-every-repo-keeps-the-house-board.md`
  (it carries `bd9f6a9b`'s author's account of the gap; the principal's words in it are quoted in
  *The acceptance test* above)
- `docs/roadmap/010-board-store-migration-per-item-files-mik/240-the-repo-template-still-scaffolds-the-old-board.md`
  (added by `bd9f6a9b`; its author's account)

**This brief's held-back sibling is not in the tree.** Whoever orchestrates the pass holds it
outside the repo and every worktree, and releases it to you only after your act 1 is committed; by
count it holds 24 questions and 10 facts. Never look for it in git history, other checkouts,
scratchpads or temporary directories. Run by hand with no orchestrator, you open it yourself, as a
deliberate second act, after act 1 is committed, and disclose when.

The delta's own comments, docstrings, manual, skills, prompts and `CHANGELOG.md` entries carry the
authors' account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md \
  --also-exclude docs/roadmap/010-board-store-migration-per-item-files-mik/230-every-repo-keeps-the-house-board.md \
  --also-exclude docs/roadmap/010-board-store-migration-per-item-files-mik/240-the-repo-template-still-scaffolds-the-old-board.md \
  --also-exclude docs/method/census \
  "ccfleet|modelguard|fleet-sweep|review-drain"
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the
re-run list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you
were spawned, your tier, any orchestrator with its spawn prompt, what you read, the UTC day, the
HEAD you pinned), per-lens answers, V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (read body-free
yes/no, findings by id), findings with stable IDs (prefix `FL`: `FL1`, `FL2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger, the method record `REVIEW.md` § *The lifecycle* requires, and a follow-up checklist.
Then STOP: act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the authors' account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile.

The skills, prompts and hook are doctrine by function, and the item queues the whole delta as one
rule-4 pass, so every finding is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it. The estate's drain switch
waits on this verdict, so say plainly, in one line under the overall verdict, whether anything you
found loses or misreads paid review work. The verdict closes `160/1660` as well as `160/1450`:
name both items in its scope line, and give the ranking gate (claims 23 to 27) its own line in
the per-lens answers, so `160/1660`'s close can cite it.

---

# Verdict — act 1 (cold reviewer, 2026-11-22 UTC)

**Scope:** board items `160/1450` and `160/1660` (one pass, one verdict, both items), the ten
commits `4bfb4e16` … `e002ea22` on the delta paths, reviewed as the code stands at HEAD
`f767033a2fd48a4e31dad5945c27b5f466817119` (pinned). The since-line
(`git log --oneline e002ea22..HEAD -- <delta paths>`) printed nothing at start and again at
2026-11-22T01:45Z, so the delta had stopped moving.

**Overall: FAIL — 2 MAJOR, 9 MODERATE, 8 minor, 3 notes** (22 findings, `FL1`–`FL22`).

**Does anything lose or misread paid review work? Yes.** `FL1` (a cut-off pass can be read as
DONE, its claim released and its worktree force-removed with the verdict uncommitted), `FL4` (the
close step deletes the live log of a pass waiting for resume), and `FL5` (the sweep's staleness
test fits a cut-off pass's kept worktree) each lose or misread it; `FL2` loses none but ends a
drain saying "queue empty" with every ready review unrun, and `FL3` leaves a killed pass with no
recorded session id to resume from.

## Provenance (rule 4, V7)

- **Reviewer:** a fresh subagent session on Fable (`claude-fable-5-2`, stated by the harness),
  started for this pass alone. Tier checked at start: on the named tier.
- **Spawned by:** orchestrator session `5106cf48` (Opus 5.5, off-tier, disclosed in its prompt),
  which states it forms no finding and writes no severity and has read the brief but not the held
  sibling or any barred record. I have no evidence either way on whether `5106cf48` is one of the
  brief's barred sessions; it is not on the brief's list by id.
- **Spawn prompt, verbatim** except that three absolute paths are shortened to bracketed
  placeholders (a home path may not enter this public repo; the substitution is mine and form
  only):

  > You are the cold reviewer for one rule-4 pass in the atelier repo, running on Fable. The
  > principal approved exactly this one Fable pass (atelier board 160/1450, with 160/1660 folded
  > in).
  >
  > Your worktree: [worktrees]/atelier-rv1450 (branch review-1450, HEAD f767033a). Work only there
  > and in a scratch directory of your own under [orchestrator scratchpad]/rv1450/ (create it;
  > delete your probes when done). Never touch the primary checkout [primary checkout] or any
  > other worktree.
  >
  > Your brief, which is your only instruction on substance:
  > [worktrees]/atelier-rv1450/docs/reviews/2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md
  > Read it whole and follow it, together with docs/method/REVIEW.md rules 1-4. Skip the
  > session-log step of the repo read order (rule 2 bars it).
  >
  > This prompt is process only. I am the orchestrator, session 5106cf48 (Opus 5.5, off-tier): I
  > form no finding, write no severity, and have read the brief but not its held-back sibling or
  > any barred record. Quote this prompt verbatim in your verdict's provenance.
  >
  > Process:
  > - Do act 1 (Phase 1 in the brief) only. Append your verdict below a `---` divider at the end
  >   of the brief file, and edit no other file. Run no git command that writes (no add, commit,
  >   stash, checkout, push); I commit act 1 for you. Read-only git is fine.
  > - Run tests and probes in the foreground with a long timeout (up to 600000 ms); never in the
  >   background. Never run an installed tool by bare name from PATH; run the worktree's copy.
  > - Dates from `date -u`. The repo is public: no secrets, home paths, private names or estate
  >   facts in what you write.
  > - When act 1 is written in full, stop and reply to me in at most three lines: that act 1 is
  >   written, the overall line with finding counts by severity, and whether anything loses or
  >   misreads paid review work. Do not look for the held-back sibling; I release it to you after
  >   act 1 is committed, and you then do act 2.

- **Barred-set choice:** the brief's own (its *Deferred reading* section); the orchestrator added
  none. **Release message:** none yet; act 2 has not begun.
- **Review worktree:** `atelier-rv1450` (branch `review-1450`), read-only to me except this file.
  The brief's `Status:` line is left as written (I was told to append only).
- **What I read:** this brief whole; `REVIEW.md` lines 1–608 and, by search, its budget
  paragraph; the delta at HEAD: `instruments/ccfleet` whole, `ccfleet.example.json` whole, the
  manual page whole as rendered text, both skills and all six prompt templates whole,
  `tools/modelguard.py` and its test whole, the `modelguard` section of `tools/README.md`, the
  `ccfleet` row of `instruments/README.md`, the named `CHANGELOG.md` entries; of
  `instruments/test_ccfleet.py` the header, the stand-ins, the test names and one test body.
  Outside the delta, as far as it relies on them: `CONCURRENCY.md` 1017–1030, `ECONOMICS.md`
  44–56 and 300–330, `AUTONOMY.md` *Always confirm*, `skills/create-repo/SKILL.md` 253–277,
  `tools/archivecut.py --help`, `tools/pins.py --help`, `instruments/ccrepo` 741–771, the plugin
  manifest.
- **Exposure, disclosed.** (a) My harness loaded user-level and repo instruction files and a
  memory index before the brief. They hold private context this verdict does not carry,
  including the principal's own words on review drains and on routing by lapse time, and one
  index line naming three operating cautions for `ccfleet drive`. I used none of it as evidence;
  where it bears on a finding (`FL11`, `FL18`) I say so. (b) The harness also showed five recent
  commit subjects of this branch (brief updates and a claim). (c) One hand-written
  `grep -rn` for five placeholder names swept `docs/method` recursively, which includes the
  barred `docs/method/census`; it printed no line from there. Every other tree sweep was scoped
  to named delta files. I opened no session record, no prior verdict, no `160/` item, none of
  the five barred items, no commit message body, and did not look for the sibling.
- **Contact:** none from any author session.

## Method record

Order: floor first (the brief's re-run lines), then a full read of the code and prompts at HEAD
with my own assumption list written before any probe, then probes against a synthetic fixture,
then mutation of scratch copies, then the doctrine cross-reads. All probes ran under a scratch
directory of my own with throwaway git repos, local bare remotes, and a stand-in `claude` that
starts no model; nothing touched a real repo, a real config, the primary checkout or the network,
except three read-only fetches of OWASP ASVS 4.0.3 pages (one returned 404). Scratch is deleted.

Left out, with grounds: the seven earlier commits' diffs were read by stat and first screen
only, their content reviewed at HEAD instead (the five later, smaller diffs were read whole or on
the delta paths whole); `test_ccfleet.py` bodies beyond one were judged by mutation rather than
read; **no real launch** (see the re-run ledger); `/security-review` was not run (it reads the
session's pending diff, which here is this brief alone, and the delta is landed: discharged on
those grounds; the code-altitude read was done by hand against ASVS 5.1.4, 5.2.4, 5.3.8, 12.3.1,
12.3.2 and 12.3.5, fetched during the pass). One mutation batch was moved to the background by
the harness at 180 s, not by me; I waited for it and ran later batches in pieces under that
limit.

### Re-run ledger

| # | Command (from where the brief says) | Result |
|---|---|---|
| R1 | `git merge-base --is-ancestor e002ea22 HEAD` | exit 0 |
| R2 | `mandoc -T lint -W style instruments/man/ccfleet.1` | exit 0, no output |
| R3 | `python3 instruments/ccfleet --help` | exit 0 |
| R4 | `nice -n 10 python3 -m unittest -q test_ccfleet` (3.14.6) | 42 tests OK, exit 0, 50.6 s |
| R5 | `nice -n 10 /usr/bin/python3 -m unittest -q test_ccfleet` (3.9.6) | 42 tests OK, exit 0 |
| R6 | `test_modelguard` on both interpreters | 3 tests OK, exit 0, twice |
| R7 | `ast.parse(src, feature_version=(3, 8))` on `ccfleet` and `modelguard.py` | both parse |
| R8 | `check`, `gate`, `run --dry-run` on the synthetic config | exit 0, 0, 0 |
| R9 | `run --dry-run`, template naming the private name | refused, exit 5 |
| R10 | `drain --dry-run`, fresh `kit_dir` | `DRAIN EXIT: queue empty`, exit 0, 1 started |
| R11 | `drain --dry-run`, `ranked` exiting 7, fresh `kit_dir` | `not ranked`, exit 1; only `ranked` called |
| R12 | `drain --dry-run`, config without `queue.ranked` | refused, exit 64; `kit_dir` not made |
| R13 | `run --dry-run` and `pass --dry-run`, config without `ranked` | exit 0 both |
| R14 | `drain --dry-run` again, same `kit_dir`, same day | `queue empty`, **exit 4**, 0 started (`FL2`) |
| R15 | coldsweep `--commit` for all ten commits with the brief's `--path` set | exit 0 each |
| R16 | test counts per commit (`git show <sha>:instruments/test_ccfleet.py`) | 17, 19, 36, 37, 40, 42 |

Queue calls logged by the scratch queue for R10 then R14, in order: `ranked`, `next` ×3;
`ranked`, `next` ×1. `kit_dir` after the dry runs held `driver.log`, `launched-<date>.txt` (one
line), `logs/pass-*.out`; `driver.pid` and `max` were removed.

**NOT RUN — the one permitted real launch.** Grounds: it could not reach the live claims that
carry the risk (what a usage-capped `claude -p` prints, the ten-minute wait ceiling, whether a
resumed headless session can still reach its earlier subagent), and it would have written a new
label into the principal's cost records and transcript store. So claims 5 and 6 as they concern
the real binary, and the resume mechanism of claim 17, are **unverified by this pass** (`FL20`).
Read-only instead: the transcript store's layout through a script printing counts and key
shapes only (1,559 files at `projects/*/<uuid>.jsonl`; assistant entries all stamped
`YYYY-MM-DDTHH:MM:SS.mmmZ`; none flagged as a sidechain in main files; subagent files sit a
level deeper, outside the glob), which matches `transcript_result`; and `ccrepo`'s rule from
source (`cwdLabelFor`, line 771: the label is `path.basename(cwd)` of the main session file).

### Probe ledger (stand-in sessions; `P` numbers are cited by the findings)

| # | Probe | Returned |
|---|---|---|
| P3 | dry drain, then a real drain, same `kit_dir` and day | real drain: 0 sessions, `queue empty`, exit 4 |
| P4 | five-pick drain with the remote gone (fetch fails) | 5 "ended early rc=1", all 5 on the launched list, `queue empty (5 started)`, **exit 0**, 0 sessions; remote restored, drain again: exit 4, 0 sessions |
| P4b | passes ending `RESULT: FAILED`, `--max 1` | stop `failures` after 3, exit 0, 3 claims kept |
| P5 | session writes an uncommitted file, narrates "…finish with RESULT: DONE…" into its transcript, then prints a usage-limit error as its result and exits 1 | `END rc=1 result=DONE`; `release` called; worktree gone, file with it; result file holds the narration |
| P6a | SIGKILL the session only | `result=UNKNOWN session=` (empty); `ended` called with an empty session; claim and worktree kept; log 0 bytes |
| P6b | SIGKILL the pass process and its session | "ended early rc=-9"; `take` only, no `ended`; worktree kept; no session id anywhere under `kit_dir`; drain again: not re-picked, exit 4 |
| P6c | SIGKILL the driver (by `driver.pid`) | pass and session live on; stale `driver.pid` and `max` left; a second driver starts and runs 2 sessions under `--max 1` |
| P7 | `pass`, `release` exiting 1, `RESULT: DONE` | "release refused" printed; **exit 0**; worktree removed |
| P8 | `run`, session commits one file, leaves one uncommitted, exits 1 with no RESULT | exit 0, `UNKNOWN`; worktree removed; the commit on no ref; then `drive` of that job: "skip job1 (result exists…)" |
| P9 | `resume` in a directory whose basename is not the repo; in a missing one | first: runs, exit 0; second: `FileNotFoundError` traceback, exit 1 |
| P10 | `RESULT: SKIPPED NEEDS LIVE WRITE` | read as `SKIPPED NEEDS`; claim and worktree kept; counted unclean |
| P11 | the example config's `vars` against each shipped prompt, `--dry-run` | every one refused, exit 5 (lists in `FL12`) |
| P12 | 38 payloads to `modelguard.py` under `/usr/bin/python3 -I` and PATH `python3` | 23 launches with no model allowed (`FL7`); identical on both interpreters |
| P13 | claim refused (`take` exits 1) | exit 2, no worktree left |
| P14 | bad JSON, missing config, malformed `reset_utc` | Python traceback, exit 1, each |
| P15 | `run ../repos/pubrepo --dry-run` | accepted; visibility `UNKNOWN`; worktree path leaves the per-job folder |
| P16 | `RESULT_RX.findall` on nine endings | `DONE WITH FINDINGS` → `DONE WITH`; a backticked word → none; a narrated "…RESULT: BUDGET EXHAUSTED if the limit hits" → `BUDGET EXHAUSTED`; the prompt's own `<DONE\|SKIPPED\|…>` → none |
| P17 | `review_log()` for (`app-web`, `010`), (`app`, `web-010`), (`app`, `web/010`) | one path for all three; a file left at a pass's path is still there after the next pass on that item |

### Mutation ledger (scratch copies; a mutant "survives" when the suite stays green)

The scratch copy sits outside a git checkout, so `test_pin_is_resolved…` fails there on the
unchanged code (control run); a mutant failed by that test alone is counted as surviving.

- **`ccfleet`, survived (6 of 18):** `resume` launched with no `--model`; the bad-end count never
  reset by a clean end; `harvest` taking the first RESULT in a text, not the last; the
  private-name match made case-sensitive; a reset before any start exiting 0, not 3; `pass`
  skipping the brief-exists check. **Inconclusive (1):** stdin not from `/dev/null` survives
  whenever the test runner's own stdin is empty, as mine was, because the test asserts only that
  the stand-in read nothing.
- **`ccfleet`, killed (11):** `ranked`'s exit code ignored; `ranked` not required in the config; guard ignoring repos marked private; worktree removed on any pass
  result; `resume` removing the worktree on a refused release; config `env` overriding the wait
  ceiling; `--in` accepting any basename; release on any result; `stop_on` ignored; `drive`
  never skipping; the gate ignoring the five-minute load.
- **`modelguard`, survived (1 of 12):** any `subagent_type` exempt, not `fork` alone.
  **Killed (11).**

## Load-bearing assumptions (named before probing), each with its fate

| # | Assumption | Fate |
|---|---|---|
| A1 | A cwd basename is the billing key | **Confirmed** from `ccrepo` source; enforced by `run --in`, not by `resume` (`FL17`) |
| A2 | The last `RESULT:` word a session prints, or failing that any since launch in its transcript, is a safe signal to release a paid claim and delete its worktree | **Damaged** (`FL1`, P5; `FL14`, P10) |
| A3 | The launched list means "started" | **Damaged** (`FL2`, P3, P4) |
| A4 | Three unclean ends in a row is how a spent budget looks | **Partly damaged**: holds when sessions end with no RESULT (P4b shape); a setup failure is not an "end" at all and never counts (P4); a cap read as DONE resets the count (`FL1`) |
| A5 | What ccfleet records is enough to resume a cut-off pass | **Damaged** for any end but a clean exit (`FL3`, P6a, P6b) |
| A6 | A literal name list is the right privacy guard | **Stands as stated** ("the names you list and nothing you forgot"); whole-word, any case, fails closed on unknown visibility (R9); case-insensitivity is unpinned |
| A7 | A hook reading Bash text can hold "every launch names its model" | **Damaged** (`FL7`) |
| A8 | An exit code from the adopter's own command is a sound "ranked first" gate | **Stands for `drain`** (R11, R12; restart re-asks); it cannot see what was ranked, and `pass` does not ask (`FL16`) |
| A9 | The principal's words carry the sweep's new scope rule | **Damaged** (`FL8`) |
| A10 | An unattended session with a permission mode in every repo is adequately bounded by its prompt | **Not shown**: no threat enumeration in the delta (`FL10`) |

## Per-lens answers

**Lens 1, approach.** The structure is sound where it is simplest: one session per repo in a
worktree named for the repo, argv lists and no shell, a pass that owns its own claim so the
driver's death harms nothing (P6c). It is unsound at the two points where it infers state from
weak signals: a RESULT word read from any assistant text decides a destructive clean-up (`FL1`),
and a list written before a start stands in for "started" (`FL2`). The hook is the wrong strength
of control for the sentence its documentation prints (`FL7`). The sweep's no-pin rule widens the
quoted words (`FL8`). Whether two skills that start unattended sessions belonged in the plugin
without a recorded call is the principal's question (`FL21`). "Unsure means the dearer route"
uses price as a stand-in for quality after the same section stopped ordering routes by price
(`FL11`).

**Lens 2, correctness.** Claims confirmed by probe or re-run: 1 (from `ccrepo` source and the suite), 2, 3 (by unit test
and R8), 5 for `run` and `pass` (the suite; stdin inconclusive, `resume` unpinned), 7 in part, 8 for `resume`, 9 (same path, but see `FL15`), 10, 11, 14 (grammar only, and 3.9.6 run),
15, 23, 26, 27. Not tested: 12 (ordinary interpreter behaviour; the children are started from
the file on disk). Claims damaged: 4 (`FL2`), 6 (`FL1`), 7 and 8 in part (`FL2`, `FL13`), 13
(`FL13`, `FL17`), 16 (`FL5`, `FL8`), 17 (`FL3`, `FL20`), 18 (`FL9`), 19 (`FL12`), 21 (`FL7`),
22 (`FL18`), 28–30 as carried out (`FL8`). Interruption trace, by point of life:

| Cut at | Claim | Worktree | Session id | Review log | `resume` from here? |
|---|---|---|---|---|---|
| before the claim (setup fails) | none | removed or never made | none | none | nothing to resume; the pick is burnt for the budget (`FL2`) |
| after the claim, before START | held | kept | none | none | no session to resume; un-claim by hand |
| mid-session, usage cap | held if read UNKNOWN; **released if read DONE** (`FL1`) | kept, or **removed** (`FL1`) | in END, the result file and `ended` if the capped output is JSON carrying one (unverified) | kept | yes when held and the id was printed |
| mid-session, session SIGKILL | held | kept | **empty** in every record | kept | only by finding the transcript by hand (`FL3`) |
| reboot, or the pass process killed | held | kept | **none recorded** | kept if `kit_dir` survives a reboot | as above (`FL3`) |
| driver's terminal closed, or driver killed | unaffected | unaffected | unaffected | unaffected | not needed; the pass finishes and releases itself (P6c) |
| after the session, before the release | held | removed when the RESULT was clean (`FL13`), else kept | recorded | folded or kept | n/a |

**Lens 2, the ranking gate (claims 23–27; `160/1660`'s line).** As built, the gate holds for
`drain`: a config without `queue.ranked` is refused with exit 64 before `kit_dir` is touched
(R12); `ranked` is called once, with `{BY}`, before the first `next` (R10, R11 call logs); any
nonzero exit prints `DRAIN EXIT: not ranked`, exits 1 and starts nothing (R11); a dry run and a
restarted driver ask again; `run`, `pass` and `resume` neither need nor call it (R13). Two tests
pin the two refusals, and both mutants of the gate were killed by them. Three limits, none a defect
in the code: `ccfleet pass` run by hand takes a claim with no ranking asked (`FL16`); the gate is
an exit code and cannot see what was ranked, so "gate, not a habit" is exactly as strong as the
adopter's `ranked`; and the docstring's exit-code line does not list "not ranked" under 1
(`FL19`). The routing text has findings of its own (`FL11`), and the surfaces agree on the
interface apart from `FL19`. On the code and contract alone, `160/1660`'s subject is sound; its
doctrine text is not yet.

**Lens 3, completeness.** Surfaces mostly agree (docstring, `--help`, manual, README, example,
skills); the disagreements are in `FL12`, `FL13` and `FL19`. The mutation ledger names what the
tests would not catch. Duplication with what atelier already holds: the reviewer-prompt section
restates the review-brief skill's rules by hand and has drifted from `REVIEW.md` (`FL9`); the
"lessons" live in three places (docstring, manual, skill), consistent today, unstamped (V4).

**Lens 4, security and privacy.** Code altitude: no shell anywhere, every child is an argv list
(ASVS 5.3.8 met; 5.2.4 n/a); queue output, jobs fields and the `repo` argument reach
`os.path.join` and `git` unvalidated (5.1.4, 12.3.1, 12.3.2: P15; the inputs are the adopter's
own, so minor, in `FL17`); `modelguard` fails open on a payload it cannot parse and on 23 command
shapes (`FL7`). Design altitude: `FL10` (no threat enumeration; the example ships the widest
permission mode), `FL22` (the approval is published verbatim on public items), `FL15` (a review
log outlives its pass). The ranking section's quote carries no personal data; the paraphrase
beside it states a budget structure in generic terms and no figure (`FL22`).

## Standing checklist

- **V1** No claim stronger than its evidence: fails at claims 4, 6, 13, 19, 21 and the `drive`
  "resumes it" sentence (`FL1`, `FL2`, `FL6`, `FL7`, `FL12`, `FL13`).
- **V2** Re-run: done (ledger). Live claims on the real binary NOT RUN, with grounds (`FL20`).
- **V3** Mirror sweep: `bd9f6a9b` changed the skill and not the worker prompt that carries it
  out (`FL8`); `b68cf410` left `brief-prompt.md` on "session-log entry" (`FL19`); `160/910`'s
  two reader-side rules are not in the reviewer-prompt section (`FL9`).
- **V4** One home: three homes for the lessons, unstamped (note under lens 3); the queue
  contract's homes agree but for `FL19`.
- **V5** Contradiction: `FL4`, `FL8` (against `create-repo`), `FL11` (inside one section), `FL13`,
  `FL18`. Cross-references checked for the rule reached: `RECORD.md` and `010/270` not opened
  (the item is on the board, outside the delta); `REVIEW.md` rule 3 and *Budget decides…* reach
  the rules cited; `ECONOMICS.md` does not hold the hook's last clause (`FL18`).
- **V6** Security and privacy: run at both altitudes; `/security-review` discharged on grounds
  (method record).
- **V7** Provenance: stated in the brief, repeated above.

## Per-commit ledger

| Commit | Read body-free | How far | Findings |
|---|---|---|---|
| `4bfb4e16` | yes | stat and first screen; content at HEAD | FL1 (in part), FL2, FL6, FL7, FL10, FL12, FL13, FL14, FL17, FL18, FL21 |
| `b2ea715c` | yes | stat; manual read whole at HEAD | FL19 |
| `17f158d2` | yes | stat; content at HEAD | FL1, FL3, FL13 |
| `d9d1589e` | yes | stat; content at HEAD | FL4, FL9, FL15 |
| `a025636e` | yes | stat; content at HEAD | FL5 |
| `1eb42f54` | yes | stat; content at HEAD | FL2 |
| `c60dee8b` | yes | stat; content at HEAD | FL11, FL16, FL19, FL22 |
| `bd9f6a9b` | yes | whole diff | FL8 |
| `b68cf410` | yes | whole diff on the three delta paths | FL8, FL19 |
| `e002ea22` | yes | whole diff | FL11 |

## Findings

Every finding is the principal's to decide (rule 3). Nothing is applied. Counsel is labelled.

### FL1 — MAJOR — A cut-off pass can be read as DONE, released and its worktree deleted

**Evidence.** P5. `harvest` (`instruments/ccfleet` 384–406) falls back to the transcript whenever
the last turn has no `RESULT:` line, and `transcript_result` (354–381) takes the newest assistant
text since launch that matches, whatever it was for. A last turn that is a usage-limit error is
such a turn. The session's exit code is printed (`rc=1`) and never consulted. `run_one` then
calls `release` and `git worktree remove --force` (590–593). In the probe the "report" harvested
was a line of planning narration, the claim was released, and the uncommitted file in the
worktree was gone. A narrated `RESULT: BUDGET EXHAUSTED` would instead stop a healthy drain
(P16).
**Criterion.** Claim 6; the brief's first worst failure; the ruling quoted in `REVIEW.md`
§ *When to review* (a spent budget's work is resumed, not lost).
**Limits of the evidence.** Two links are unmeasured here: that a real capped `claude -p` prints
JSON carrying a session id (without one there is no fallback and the pass reads UNKNOWN, safely),
and how often an orchestrator writes a RESULT line before its last turn. The mechanism is proven;
its rate is not.
**Tests.** `test_a_result_only_in_the_transcript_is_harvested` pins only the benign case.
*Counsel:* never treat an end as clean when the exit code is nonzero or the output flags an
error; take the fallback only from the last assistant text that also carries the `ITEM:` line of
the final-output shape; never force-remove a worktree with uncommitted changes.

### FL2 — MAJOR — The launched list records offers, not starts, and nothing corrects it

**Evidence.** R14, P3, P4. `drain` appends the pick to the launched list before the pass is
spawned (883–884) and in dry mode too. A pass that then fails before START (a failed fetch, a
brief not on the branch, a guard refusal, a refused claim) logs "ended early", is not counted as
an unclean end (840–841), and stays on the list for the whole budget. Results: a `--dry-run`
rehearsal on the real `kit_dir` makes the real drain exit 4 "queue empty" having started
nothing; a drain during an outage exits **0** with "5 started" and no session run, and the next
drain of that budget exits 4. In both, the queue is full and the tool says it is empty.
**Criterion.** Claim 4 ("print the launch, start nothing"; the manual's FILES entry calls the
list "what a drain has started"); claim 7 (a failing queue is never read as empty; a failing
*pass* is); the skill's Mode 1 step 3, which stops on "queue empty".
**Paid work.** None lost; the budget goes unspent on a false all-clear.
**Tests.** `test_a_dry_drain_reads_its_passes_as_ended` and `test_a_queue_offering_a_launched…`
pin the two halves and not their meeting.
*Counsel:* a dry drain writes no list (or its own); an early end takes the pick back off the
list, and counts toward the stop.

### FL3 — MODERATE — A killed pass leaves no session id, and the skill does not say how to find one

**Evidence.** P6a, P6b. The id is learnt only from the session's final JSON. After a SIGKILL of
the session the END line, result file and `ended` hook all carry an empty id; after a kill of the
pass process (or a reboot) no record under `kit_dir` holds one and `ended` is never called.
`resume` requires SESSION; Mode 2 says "read its reviewer's transcript first" and gives no way to
locate it. The claim, worktree and review log do survive, and the transcript can be found by hand
from the worktree's path, which no surface says. `--set AGENT=<reviewer id>` has the same gap.
**Criterion.** Claims 8, 9, 17; lens 2's interruption trace.
*Counsel:* have `pass` look the session up by its worktree path when the log gives none, and
record it; say the method in Mode 2.

### FL4 — MODERATE — The close step folds and deletes the live log of a pass awaiting resume

**Evidence.** `skills/review-drain/SKILL.md` Close step 4: "`<kit_dir>/review-logs/` is empty. A
log left there is a pass whose fold did not take it in: append it verbatim to its brief …, then
delete it." Mode 1 step 4 and Mode 2 keep a cut-off pass's claim, worktree and log for resume;
the reviewer-prompt section makes the log private "until act 2 is saved" and has a revived
reviewer "read its own log first". A drain that ends on a spent budget is the ordinary case, and
its close, followed as written, publishes a half-finished log into the brief before act 1 is
committed and removes the file the revived reviewer is told to read.
**Criterion.** V5; rule 1 (nothing of the reviewer's is opened before its findings are
committed); the brief's first worst failure (a pass misread, here as finished-but-unfolded).
*Counsel:* step 4 excludes every pass whose claim is still held.

### FL5 — MODERATE — The sweep's staleness test fits a cut-off pass's kept worktree

**Evidence.** `skills/fleet-sweep/worker-prompt.md` 2b acts on "a branch or worktree whose commits
are all on `{BR}` and that nothing holds open". A drain's kept worktree is detached at the
mainline with the verdict uncommitted in the brief file: its commits are all on the branch and
nothing holds it open. The prompt protects "the primary checkout's own working changes" only;
"never delete work you cannot prove is spent" is in the skill's item 7, which the worker never
reads. `git worktree remove` without `--force` would refuse a dirty tree; that default is the
only guard, and the prompt does not forbid `--force`. Not probed with a model; this is a reading
of the two prompts side by side.
**Criterion.** Claim 16 ("provably stale"); the two skills ship together and the sweep runs
between a budget's end and the resume.
*Counsel:* add "and a clean tree" to the test, and exempt any worktree a held queue claim names.

### FL6 — MODERATE — `run` deletes a cut-off worker's work, and `drive` does not retry it

**Evidence.** P8. For `run` there is no `post` hook, so `cleanup()` always runs (592–593): the
worktree is force-removed after an UNKNOWN end, the session's unpushed commit is left on no ref
and its uncommitted file is gone. The result file is written for every end, and `drive` skips any
job that has one, so a re-run the same UTC day skips exactly the jobs a cap cut off; the manual
says running the file again "resumes it". `drive` fixes `day` at its own start while `run`
names the folder at each job's start, so across UTC midnight the skip misses and finished jobs
run again. This is sweep work, brief-writers included, not review work.
**Criterion.** V1 against the manual's `drive` entry and fleet-sweep step 5.
*Counsel:* keep the worktree unless the RESULT is clean; skip on a clean result only.

### FL7 — MODERATE — `modelguard` passes 23 ordinary launch shapes with no model

**Evidence.** P12, each a `claude` launch with no `--model`, each allowed, on both interpreters:
the body of `for … do`, `if … then` and `while … do`; `timeout N`; `stdbuf`; `bash -lc` and
`zsh -ic`; `eval "…"`; `find -exec`; `sudo -u name`; a backtick assignment; a brace group; `!`;
any earlier word holding `#` (shlex ends the line there, the shell does not); the text
`ANTHROPIC_MODEL=` anywhere in the command, or set empty; a heredoc fed to a shell; `<<` inside
arithmetic followed by a newline; a prompt or an option value that is a subcommand word
(`claude -p "update"`); `--model` with no value; the binary held in a variable; `npx`. Three
payload shapes exit 1 with a traceback, which the harness treats as allow; a tool named `Task`
is not matched. False denies found: `command -v claude`, and `--model` on an unindented
continuation line. The docstring's "Known limit" names scripts only; `tools/README.md` heads the
section "every Claude session a session starts names its model". One mutant survives.
**Criterion.** Claim 21; the brief's third worst failure. Security class: a control that fails
open. **Recurrence prevention:** a table-driven test of launch shapes that must deny, grown with
every bypass found, and a documented statement of what the hook does not see.
*Counsel:* invert the parse for the common case: any segment in which a word whose basename is
`claude` appears as a command word after shell keywords and unknown wrappers are skipped; and
say plainly that the hook is a net, not a proof.

### FL8 — MODERATE — The sweep's "adopt every no-pin repo, never ask" widens the words and has no step

**Evidence.** The quoted ruling is about boards, with two exceptions (archived, a fork). The
answer "Adopt it fully" was a pick about a never-adopted repo. `SKILL.md` step 1 now puts every
unarchived, unforked repo in scope for full adoption "not put to the principal as a question".
(a) `create-repo`'s standardise process says "Don't touch a third-party repo … a repo whose owner
is not in your profile's `remote.account` is not yours to standardise": a repo owned by someone
else that is not a fork is in scope by one text and barred by the other. (b) No step or prompt
carries adoption out: the jobs use `worker-prompt.md`, whose task 1 runs
`git diff {PIN} origin/main`, and `{PIN}` for such a repo is the word `UNRESOLVED`. (c) The same
holds for "a repo with no board gets the empty store" and for the `ROADMAP-DONE.md` cut: both are
in `SKILL.md` item 6 and in no prompt a worker reads. (d) How a repo is found to be archived or a
fork, and what population "every other repo" ranges over, is unstated.
**Criterion.** Lens 1 (a reading or a widening); V3; V5; the brief's sixth worst failure.
*Counsel:* scope the rule to repos the config lists, keep `create-repo`'s owner check as a third
exemption, and give adoption and the empty board a prompt of their own.

### FL9 — MODERATE — The reviewer-prompt template drops two of `REVIEW.md`'s reader-side duties

**Evidence.** Rule 4 makes the off-tier orchestrator's first condition checkable only if "the
reviewer puts it in the verdict's provenance: the spawn prompt, the barred-set choice and the
release message, verbatim or as an attached file", and says the conditions "are not optional".
Rule 2 has a cold reviewer skip the session-log step, "and its spawn prompt and the brief say so
too". Neither is in the skill's § *The reviewer prompt* or in `orchestrator-prompt.md` step 4.
Every drain pass runs under an off-tier orchestrator, so every drain verdict would lack the
record unless its brief happens to ask for it.
**Criterion.** Claim 18; V3 (`160/910`, applied 2026-11-09, five days before this skill landed).

### FL10 — MODERATE (security) — No threat enumeration; the example ships the widest permission mode

**Evidence.** `ccfleet.example.json` line 8 sets `claude_args` to
`["--dangerously-skip-permissions"]`; the manual's whole treatment is "Choose them on purpose".
The sessions run unattended in every listed repo, are told to follow each repo's own `CLAUDE.md`
and to read its pull requests and CI output, hold the user's git and `gh` credentials, and push
to the mainline. Nothing in the delta's own text names who could steer such a session (a repo's
instruction file, an outside contributor's pull-request text, a CI log) or what bounds it; the
only mechanical guard is the private-name list. The intent record is barred until act 2 and may
hold one; the delta does not.
**Criterion.** Lens 4, design altitude: "Absent enumeration is the finding."
**Recurrence prevention:** a short threat section in the manual, an example that does not model
the bypass, and a line from `check` whenever a bypass mode is configured.

### FL11 — MODERATE — The routing rule is stricter than the direction the same section reports

**Evidence.** The section's own paraphrase: a lapsing budget "is spent first when that time is
near". Step 3: route "to the route that reaches local quality and whose budget lapses soonest",
cost "only breaks a tie". The condition "when near" is gone, so with no lapse near the earlier
order the section also reports (the cheapest capable route first) never applies: cost decides
only between routes on one budget. Second, "Unsure means the dearer route: quality is never
traded for price" survives from the cost-ordered version; the section now says no budget is free
and stops ranking routes by price, so "dearer" no longer names the route surest to reach local
quality and can name a sandboxed one. Third, "It lasts one budget" does not say which when two
are open. The spill rule ("never from a budget that lapses before its own") is consistent with
step 3 as written. Disclosure: the principal's fuller words were in my harness context; I judge
here against the skill's paraphrase only, as the brief asks, and found nothing in the paraphrase
that misstates them beyond the dropped condition.
**Criterion.** Claim 31 and its author's question; V5; the (1660) lens-1 question.
*Counsel:* "unsure means the local route"; state the order for when no lapse is near.

### FL12 — minor — The shipped prompts need variables no surface tells the adopter to set

**Evidence.** P11, refused with exit 5 on the example's `vars`: orchestrator `{APPROVAL}`
`{HELD_DIR}` `{HOLDS}` `{PROVENANCE}` `{REVIEW_MODEL}`; worker `{DIGEST}`; task `{TASK}`; brief
`{ITEM}` `{NOTE}` `{QUOTE}` `{SOURCE}` `{SUBJECT}`; resume `{AGENT}` `{APPROVAL}` `{REVIEW_LOG}`
`{STATE}`; fold `{APPROVAL}` `{BRIEF}` `{HELD}` `{ITEM}` `{REVIEW_LOG}`. The skill names
`APPROVAL`, `HOLDS`, `PROVENANCE`, `TASK`, `AGENT`, `STATE` and `REVIEW_LOG`; `REVIEW_MODEL`,
`HELD_DIR`, `HELD`, `DIGEST` and the brief-writer's five appear in no skill, manual or example.
The example carries `REVIEW_APPROVAL` and none of the drain's three. `REVIEW_MODEL` is the one
value that puts the reviewer on the review tier; `HELD_DIR` is where the held sibling lives, and
`CONCURRENCY.md`'s rule for it (outside the repo, every worktree and any scratchpad; never a
reviewer's working directory) reaches the adopter only as "outside any temp directory a reboot
wipes". The resume prompt reuses `{APPROVAL}` for a different utterance (the word to finish),
so an unchanged config quotes the drain approval as that word.
**Criterion.** Claim 19. The refusal fails closed, hence minor.

### FL13 — minor — After a refused release a pass still removes its worktree and exits 0; a fold releases nothing

**Evidence.** P7: `one_pass` discards `ended_hooks`' answer; the docstring's exit line says "2
claim refused (or a release refused)", true for `resume` only. `fold-prompt.md` ends "Do NOT
remove the worktree, release the queue claim, or delete the held copy: the launcher does that";
`run --in` keeps the worktree, calls no queue command, and nothing in the delta ever deletes a
held copy. **Criterion.** Claims 8 and 13; V5.

### FL14 — minor — The two-word RESULT capture misreads plain endings

**Evidence.** P10, P16: `RESULT: SKIPPED NEEDS LIVE WRITE` (the skill's own phrase
for that skip) reads `SKIPPED NEEDS`; `RESULT: DONE WITH FINDINGS` reads `DONE WITH`; a
backticked word reads UNKNOWN. Each keeps the claim and worktree (the safe direction) and counts
toward the three-unclean stop. `harvest` taking the last match is unpinned (mutation ledger).

### FL15 — minor — A review log outlives its pass and is handed to the next reviewer of the item

**Evidence.** The path is `<kit_dir>/review-logs/<repo>-<item>.md` with unsafe characters
folded, so `app-web`+`010` and `app`+`web/010` share one file (P17). A log left by a pass that
failed, was un-claimed or was withdrawn stays; the next pass on that item gets the same path and
its reviewer is told "read it first if it already exists". **Criterion.** Rule 2 (an earlier
reviewer's account is barred to a cold one); the withdrawal rule in *The lifecycle*.

### FL16 — minor — The ranking gate does not cover a pass started by hand

**Evidence.** R13: `ccfleet pass` takes a claim and runs with no `ranked` call, by design
("drain only"). The skill says the adopter's queue makes "`ranked` (and `next`) refuse" until the
seal; it does not ask the same of `take`. **Criterion.** Claim 25's "gate, not a habit".

### FL17 — minor — Unchecked inputs and unhandled errors

**Evidence.** P9: `resume` accepts a worktree whose basename is not the repo (claim 1 is enforced
by `run --in` alone) and dies with a traceback on a missing one. P14: bad JSON, a missing config
and a malformed `reset_utc` are tracebacks, exit 1, not the documented 64. P15: a `repo` given
as a path is accepted, misses its config entry and moves the worktree out of its job folder.
`resume` without `--item` still calls `ended` with an empty item. `--max 0` falls back to the
config's ceiling. A second driver does not count a dead driver's still-running passes (P6c).
`DriverLock` is check-then-write. `resume` launching with no `--model` would pass the suite.

### FL18 — minor — The hook's reason and the skill state an approval rule doctrine does not hold

**Evidence.** The deny reason ends "A review runs on the tier the principal names, and only with
the approval that tier needs", under the label "The standing rule (atelier ECONOMICS.md)";
`review-drain` opens "The review tier is gated. No review-tier work … without the principal's
explicit approval." A search of `docs/method/*.md` for an approval rule on a tier finds none, and
`ECONOMICS.md` 50–54 says a session picks "the named tier for review … without putting it to the
principal first". The first three clauses of the reason do agree with `ECONOMICS.md`.
Disclosure: my harness context shows this is one estate's standing rule; the generic doctrine
has no home for it. **Criterion.** Claim 22; V4; V5.

### FL19 — minor — Small disagreements between surfaces

The manual is dated 2026-11-18 and was changed on 2026-11-20. "Each of the four entries is an
argument list" sits above five (`ended` is one). The docstring's exit-code line and `--help`
omit "not ranked" under 1. `brief-prompt.md` still asks for "a short session-log entry" after
`b68cf410`. The skill reads results from `results/<date>/`, one folder, for a drain that may
cross UTC midnight. The manual's `pass` entry and FILES entry ("empty after a clean drain") do
not cover the refused-release and cut-off cases.

### FL20 — note — Live claims this pass could not test

What a usage-capped `claude -p` prints and returns; the ten-minute wait ceiling and its switch;
whether a session resumed with `--resume` can message the subagent it spawned before it died
(Mode 2 rests on it, and a FAILED pass has no stated next step); and rule 4 of the skill, that
running under `/loop` means "a reboot does not end the drain" (a reboot ends the driver and every
pass; P6b shows the state left). *Counsel:* one canary pass on a throwaway repo, cut off on
purpose and resumed, before the estate's switch.

### FL21 — note — Shipping the two skills to every plugin user is a call the delta does not show

The manifest lists no skills, so every folder under `skills/` ships. These two differ in kind
from the others: they start unattended sessions across repos. `CLAUDE.md` § *Autonomy* keeps "a
plugin/skills bundle" as the principal's call. The records that might show the call are barred
until act 2.

### FL22 — note — Privacy of the principal's words in public surfaces

The verbatim quote in the ranking section carries no personal data. The paraphrase beside it
tells every plugin user the estate's budget structure in generic terms, with no figure.
Separately, `orchestrator-prompt.md` has the approval recorded "quoting the principal" on the
item of every repo it runs in, public ones included, and the private-name guard checks only
listed names: an approval that carries a figure or an estate fact is published by design.

## Follow-up checklist

- [ ] `FL1`, `FL2`: the principal's rulings; both gate the estate's drain switch.
- [ ] `FL3`–`FL11`: rulings, MODERATE; `FL4` and `FL5` are one-line text changes.
- [ ] `FL7`, `FL10`: security findings; each carries its recurrence-prevention step above.
- [ ] `FL12`–`FL19`: minor; batchable.
- [ ] `FL20`: a canary cut-off-and-resume on a throwaway repo before any real drain on `ccfleet`.
- [ ] Act 2: open the sibling and the barred records, screen the ten commit bodies, reconcile.
