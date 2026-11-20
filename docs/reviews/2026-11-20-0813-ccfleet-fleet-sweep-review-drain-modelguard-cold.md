# Cold pass — `ccfleet`, the `fleet-sweep` and `review-drain` skills, and `modelguard`

**Board:** `docs/roadmap/160-doctrine-review-owed/1450-rule-4-cold-pass-queued-ccfleet-fleet-sweep-review-drain-modelguard.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-20 UTC by a brief-writer worker of queue run
`08cd3b95` (Opus 5.5). Queued, waiting on the principal's explicit approval of Fable work; this
brief is not that approval.

**Pass type:** code and design cold pass, per `docs/method/REVIEW.md` rule 4. Two skills that
stamp behaviour into every plugin user, their prompt templates, and a hook that denies tool calls
are doctrine by function (rule 3); the instrument that runs them is reviewed with them as one
commitment.
**Tier:** Fable, the principal-named review tier, checked at selection by whoever takes the pass.
A session that cannot run on it stops (rule 4).
**Size of this pass:** large. Six commits; about 1,070 lines of standard-library Python, 630 lines
of tests, a 940-line manual page, 330 lines of skill text and prompt templates, a 180-line hook with
its 70-line test, and the README and changelog entries. Budget the time; never thin the pass to
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

## Spawn provenance

- **Authors of the work under review.** Session `559edaec` (Opus 5.5, headless, started
  2026-11-14 by an estate health sweep, orchestrator session `58027096`) wrote the first landing.
  Queue run `78ca9153` (Opus 5.5, principal-opened, 2026-11-16) and its workers wrote the manual
  page and the `--help` digest. Session `84b7932e` (Opus 5.5, principal-opened, 2026-11-18) and the
  workers it started wrote the gap fixes and the three fixes of the last commit.
- **Who wrote this brief:** a brief-writer worker (Opus 5.5) of queue run `08cd3b95`, a
  principal-opened orchestrator of 2026-11-20. Neither the worker nor its orchestrator authored,
  started or instructed any part of the delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model. Queue run `08cd3b95` will not start the pass.
- **Barred from running this pass:** session `08cd3b95` and every worker it started (whoever
  writes a brief does not run it); sessions `559edaec`, `58027096`, `78ca9153` and `84b7932e`, and
  everything each of them started or instructed.
- **Contact, disclosed (rule 4).** The brief-writer's only instruction came from its orchestrator
  `08cd3b95`: the item number, the rule-4 standing above, the delta's paths, the house form, and a
  list of where to test hardest (the permission-mode blast radius, the two skills' reach, the
  hook's false allow, the gap fixes and the last commit's three fixes, and whether the drain loses
  paid review work on a crash or a cap). That list restates the item's own pointer and the gating
  reason the board records; it is disclosed here because it shaped the brief's emphasis. No author
  session contacted the brief-writer.
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

## The acceptance test

Judge the work against what it claims (its docstrings, manual, skills and changelog) and against
the doctrine it must keep:

- **The principal's words.** 💬 Asked on 2026-11-18 when the estate's weekly drain should switch
  onto these, his pick, verbatim: *"After its review (Recommended)"*: the switch waits for this
  pass to come back clean. It is an answer to a question, not a ruling. The ruling that binds the
  drain's behaviour is quoted in `REVIEW.md` § *When to review*: *"Quality is more important than
  cost. If we run out of budget then we will resume the work when the budget replenishes"*. A
  drain that cannot resume what a spent budget cut off fails that sentence.
- **The rules the drain enforces on others.** `REVIEW.md` rule 1 (the deferred split and the
  context partition), rule 2 (barred reading), rule 4 (spawn criterion, tier at selection, the
  off-tier orchestrator's two conditions), *The lifecycle* (method record); `CONCURRENCY.md`
  § *Orchestrated queue runs* (where held-back material lives, never a scratchpad or a reviewer's
  working directory); `ECONOMICS.md` (tier set by risk; the model named on purpose).
- **The public-repo rule.** `docs/PERSONAL-DATA.md` and the repo-craft purpose rule: a generic
  tool in a public repo carries no estate's names, and its config example is fictional.

## What the work is

Six commits on `main`, in order:

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

Delta paths, read at HEAD and commit by commit:

- `instruments/ccfleet`, `instruments/ccfleet.example.json`, `instruments/test_ccfleet.py`,
  `instruments/man/ccfleet.1`, `instruments/README.md` (the `ccfleet` row and the requirements
  paragraph)
- `skills/fleet-sweep/` (`SKILL.md`, `worker-prompt.md`, `task-prompt.md`, `brief-prompt.md`)
- `skills/review-drain/` (`SKILL.md`, `orchestrator-prompt.md`, `resume-prompt.md`,
  `fold-prompt.md`)
- `tools/modelguard.py`, `tools/test_modelguard.py`, `tools/README.md` (§ *`modelguard.py`*)
- `CHANGELOG.md`: the four entries dated 2026-11-14 and 2026-11-18 that name `ccfleet`, the two
  skills or `modelguard`

First confirm the tree holds the whole delta, then read each commit body-free:

```
git merge-base --is-ancestor 1eb42f54 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit 4bfb4e16 --path instruments --path skills \
  --path tools/modelguard.py --path tools/test_modelguard.py --path tools/README.md \
  --path CHANGELOG.md
```

Repeat the `--commit` line for each of the other five commits. Plain `git show` is barred: it
prints the message body before the diff, and reading is atomic (rule 1). Several of these commits
also touch the board, the intent record and a session record; those are barred until phase 2, so
always pass `--path`.

Then check what has landed on the delta paths since: `git log --oneline 1eb42f54..HEAD --
instruments/ccfleet instruments/ccfleet.example.json instruments/test_ccfleet.py
instruments/man/ccfleet.1 skills/fleet-sweep skills/review-drain tools/modelguard.py
tools/test_modelguard.py` (empty when this brief was written, at `71c867bc`). Review the code as
it stands at your HEAD, and pin that SHA in your verdict's scope.

**Machine-local surfaces no other review will catch** (read-only; report them in public-safe
terms, never a home path or a private name):

- The user-level `~/.claude/settings.json` wires `modelguard` as a `PreToolUse` hook on
  `Agent|Bash`, run as `/usr/bin/python3 -I <the primary checkout>/tools/modelguard.py`. That
  interpreter was Python 3.9.6 when this brief was written; the repo's tests ran on the
  `python3` on `PATH`, 3.14.6. The hook runs the primary checkout's copy, not a worktree's.
- `~/.local/bin/ccfleet` is a link to the primary checkout's `instruments/ccfleet`.
- The plugin manifest (`.claude-plugin/plugin.json`) declares no skill list; every directory
  under `skills/` ships to every plugin user.

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

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   Is a cwd basename the right billing key, and a literal name list the right privacy guard? Is
   "three unclean ends in a row" a sound reading of a spent budget, and the `RESULT` word in a
   session's last text a sound signal for releasing a paid claim? Is a hook reading Bash text the
   right control for "every launch names its model"? Does putting these in a public plugin, so
   that every adopter receives two skills that run unattended sessions, match the repo's own rules
   for a deliberate widening (`CLAUDE.md` § *Autonomy*; `AUTONOMY.md`)?
2. **Correctness & quality.** Re-drive the claims above against the code, by probe, not by
   reading. Trace what survives, and where, when a pass is interrupted at each point of its life:
   before the claim, after the claim and before `START`, mid-session (a usage cap; a `SIGKILL`; a
   reboot; the driver's terminal closed; the driver itself killed), after the session and before
   the release. For each, say whether the claim, worktree, session id, review log and verdict can
   be recovered with what the tool and skill record, and whether `resume` can take it from there.
   Record each overclaim against the text that makes it, including any claim no test pins.
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
   only from a clean tree; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once, on 2026-11-20 UTC, at `71c867bc`,
from the places named; its results are held in the sibling. Read exit codes explicitly. Check
`uptime` first; one heavy process at a time, under `nice -n 10`, foreground with a long timeout
(the `ccfleet` suite takes about a minute).

From the worktree root:

```
git merge-base --is-ancestor 1eb42f54 HEAD; echo "exit=$?"
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
`queue` whose `next`/`take`/`release` are a small scratch script that offers one pick until it is
in `{LAUNCHED}`. Then, with `--config` on each:

```
python3 instruments/ccfleet --config <cfg> check; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> gate; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <repo> --prompt <template> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <repo> --prompt <template naming the private name> \
  --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by <your id> drain --dry-run; echo "exit=$?"
```

Read `<kit_dir>` afterwards: `driver.log`, and every file the dry runs left. The brief-writer ran
this shape once; how it built its config is in the sibling.

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

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, every item under `docs/roadmap/160-doctrine-review-owed/` beyond its
title, the six delta commits' message bodies, `docs/method/census/` (it holds other sessions'
assessments of these tools), and beyond their first line:

- `docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md`
  (the intent record)
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md`
  (it carries the authors' account of the gap fixes)
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md`

**This brief's held-back sibling is not in the tree.** Whoever orchestrates the pass holds it
outside the repo and every worktree, and releases it to you only after your act 1 is committed; by
count it holds 14 questions and 6 facts. Never look for it in git history, other checkouts,
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
found loses or misreads paid review work.
