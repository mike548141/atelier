# Cold pass — the RK drain-path fixes (`RK2`, `RK5`) and the `REVIEW_MODEL` correction (`210/600` part 1)

**Board:** `docs/roadmap/160-doctrine-review-owed/1800-rule-4-cold-pass-queued-rk-drain-path-fixes.md`
**Status:** BRIEF ONLY. Written 2026-11-25 UTC by headless session `4da4abc0` (Opus 5.5), pinned
at `6ddbead2` (`origin/main` when written). Due before the principal's weekly drain, which starts
the evening of 2026-11-29 UTC and is the first to run on these commands.
**Approval:** one small Fable pass on the weekly budget current on 2026-11-25, by a fresh
session, plus its Opus brief.
The principal's pick, 2026-11-25 UTC, recorded on `160/1790` (an answer, not a ruling), verbatim:
*"Small Fable check, then switch (Recommended)"*; the option text he picked: *"After the 4
drain-path fixes and the trial pass, one small Fable review of just those fixes, run by a fresh
session before Monday. Benefit: keeps your review-before-use rule, and Monday runs on the new
commands. Cost: one small Fable pass this week."* It does not lift the general Fable hold beyond <!-- datescan:allow: the principal's picked option text, quoted verbatim -->
this one pass. Run only once the delta paths have stopped moving: re-check the since-line under
*What the work is* before you start, and stop if it shows a commit that counts.

**Pass type:** a cold pass per `docs/method/REVIEW.md` rule 4: code and prompt. The review
prompts are doctrine by function (rule 3): they instruct every orchestrator, reviewer and fold
session a drain starts. The instrument lines that decide what runs after a budget reset are
reviewed with them as one commitment.
**Tier:** Fable, the principal-named review tier, checked at selection by whoever takes the pass.
A session that cannot run on it stops (rule 4).
**Size of this pass:** small by its delta, not by its stakes. One commit, `a1cc5f2d`: seven
files, 97 lines added and 52 removed, one new test. The `ccfleet` test module it adds to holds
136 tests and took about five minutes per interpreter at a load near 8 on 12 cores. Budget the
time; never thin the pass to fit it (`REVIEW.md`, *Budget decides how many reviews run and when,
never how a review is run*).

**The question this pass answers for the principal.** The drain he runs from these commands
starts paid review passes unattended. The verdict must say plainly whether these three fixes are
right, whether they still hold at the head the drain will run, and whether anything in them can
lose, misread or mis-tier a paid pass.

**Why it earns a review.** These lines decide two things a drain cannot take back: what may still
run after a budget's reset, and what an unattended orchestrator, its reviewer and its fold read
and on which model the reviewer runs. The worst failures:

- **Paid work started that the reset should have stopped**, or a started pass stranded because
  the step that finishes it is refused.
- **A reviewer on the wrong tier, or on none**, from a model value the spawning tool reads
  differently than the prompt says, with nothing in the record that shows it.
- **A pass that reads outside its worktree**, in a repo where the path does not resolve, or
  where what it reads is not what the drain meant; or a prompt template that drifts from its one
  home.
- **A prompt that stamps a wrong instruction** into every pass of every repo a drain reaches:
  the widest blast radius in the operating model (rule 4).

## Spawn provenance

- **Authors of the work under review:** session `0ee74059` (`atelier-c3`, Opus 5.5,
  principal-opened by `/atelier:work run`) and the workers it started, who built `a1cc5f2d`.
  Found from the board's records and the commit's subject; no message body was used to find them.
- **The findings it answers** were formed by an earlier Fable pass, orchestrated by session
  `4a34637a`, on a brief written by queue run `0b4f93ef` and widened by `9a08702f`. That verdict
  is a prior verdict to this pass (rule 2; *Deferred reading* below).
- **Who wrote this brief:** headless session `4da4abc0` (Opus 5.5), started by principal-opened
  session `14c2530d` (`atelier-e7`, Opus 5.5) to write this brief and its held-back sibling only.
  Neither session authored, started or instructed any part of the delta. **Off-tier for review,
  disclosed: the brief-writer forms no finding and writes no severity**, used no Fable model,
  ran no review, and stops after writing.
- **Who orchestrates the pass:** session `14c2530d`, which wrote no part of the delta and no part
  of this brief. It may hold the context partition and commit the records off-tier, only if it
  forms no finding, writes no severity, and is disclosed in the claim, the pointer and the
  verdict, with its spawn prompt and release message in the verdict's provenance (rule 4).
- **Who reviews:** a fresh Fable session started for this pass alone by `14c2530d`.
- **Barred from running, orchestrating or reviewing this pass:** `0ee74059` and every worker it
  started (the authors); `4da4abc0` (whoever writes a brief does not run it).
- **Contact, disclosed (rule 4).** The brief-writer's only instruction came from `14c2530d`: the
  item, the approval (one Fable pass plus its Opus brief), the method files, the model brief to
  read down to its first verdict divider, the barred sessions, where the held-back sibling goes,
  and the house form. No author session contacted the brief-writer.
- ⚠️ **Brief-writer's exposure, disclosed** (author-account material met before writing): its
  launch prompt; `REVIEW.md` whole; `skills/review/brief.md` whole; the earlier pass's brief down
  to its first verdict divider, read as the house's shape model, so this writer has met the
  framing that pass was given but not its verdict; items `160/1800`, `160/1810`, `210/600` and
  `210/610` whole (**all carry the authors' account**, and `210/600` describes this delta and a
  live trial of it), and lines 100 to 124 of `160/1790`, which summarise the earlier verdict's
  plain lines and record the principal's picks (**so this writer has met a summary of that
  verdict**); the delta through one body-free `coldsweep --commit` read; the subjects and file
  stats of the later commits on the same paths; the two prompts' and the example config's diffs
  from `a1cc5f2d` to HEAD; `ccfleet` at HEAD around its reset checks and `resume`; `run.md` at
  HEAD (§ *Mode 1* step 1, § *Mode 2*, § *The variables the prompts need*, § *The reviewer
  prompt*); a hash-only `git log --grep` over message bodies, which printed no body; the results
  of the re-run lines below. Its harness also loaded user-level and repo instruction files and a
  memory index, which hold private context this brief does not carry. Everything evaluative it
  formed is in the held-back sibling.

## The acceptance test

Judge the work against what it claims (its comments, docstring, manual, prompts, skill text and
test) and against the doctrine it must keep:

- **The principal's words.** The drain's rule on finishing started work, as the example config
  models it: a resume and a fold run on his word to finish what was started, which is not the
  drain's approval (`run.md` § *Mode 2*; the `FINISH_WORDS` variable). His rule on review
  quality, quoted in `REVIEW.md` § *When to review*: *"Quality is more important than cost. If we
  run out of budget then we will resume the work when the budget replenishes"*. A reset that
  strands a started pass, or lets new paid work through, fails that sentence.
- **The rules the drain enforces on others.** `REVIEW.md` rule 1 (the deferred split and the
  context partition), rule 2 (barred reading), rule 4 (tier at selection; the off-tier
  orchestrator's two conditions), *The lifecycle* (method record); `ECONOMICS.md` (tier set by
  risk, the model named on purpose).
- **The public-repo rule.** `docs/PERSONAL-DATA.md`: the example config stays fictional, and no
  prompt carries an estate's names.
- **The earlier pass's findings `RK2`, `RK5` and `RK12`**, in phase 2 only (*Process* below).
  That verdict is
  [`2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`](2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md),
  barred until your act 1 is committed (rule 2). This brief neither quotes nor summarises it.

## What the work is

**The delta:** one commit on `main`, read body-free:

- **`a1cc5f2d`** — `review, ccfleet: the drain-path fixes RK2 and RK5, and REVIEW_MODEL (210/600
  part 1)` (2026-11-25)

Its paths: `skills/review/orchestrator-prompt.md`, `skills/review/fold-prompt.md`,
`skills/review/run.md` (§ *Mode 2*, § *The variables the prompts need*, § *The reviewer
prompt*), `instruments/ccfleet` (`run_one`'s reset check and the `reset_utc` line of the
reference text `--doc` prints), `instruments/man/ccfleet.1` (`reset_utc`),
`instruments/test_ccfleet.py` (`test_a_fold_runs_after_the_reset_and_new_work_does_not`),
`instruments/ccfleet.example.json` (`REVIEW_MODEL`). It also touched three board files, which are
barred (below) and are not the delta.

First confirm your tree holds it, then read it body-free:

```
git merge-base --is-ancestor a1cc5f2d HEAD; echo "exit=$?"
python3 tools/coldsweep.py --root . --commit a1cc5f2d --path skills --path instruments; echo "exit=$?"
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Without `--path`, `coldsweep` leaves the board files out by default; never add a
`--path` that names them.

**Judged at HEAD, not at the commit.** The drain runs the head of `main`, and later commits have
changed the same files: `53203833`, `2d8e05e3`, `564a7ca4` and `4a9318b7` (the rest of the
`210/600` fixes, queued for their own pass as `160/1810`), `9b4a8f8f` (the changelog), and
`f4360a79` (`210/610`, a `ccfleet` change the brief-writer found no queued pass for). They are
not this pass's subject, but they are in its scope where they touch a line this delta wrote or a
line its three fixes depend on: whether each fix still holds, unchanged in effect, at your HEAD.
`skills/review/orchestrator-prompt.md` is unchanged since `a1cc5f2d`; the other six paths are
not. Read a later commit body-free the same way (`--commit <sha> --path <path>`).

Then check what has landed on the delta paths since this brief was pinned:

```
git log --oneline 6ddbead2..HEAD -- skills/review/orchestrator-prompt.md \
  skills/review/fold-prompt.md skills/review/resume-prompt.md skills/review/run.md \
  instruments/ccfleet instruments/man/ccfleet.1 instruments/test_ccfleet.py \
  instruments/ccfleet.example.json
```

It was empty at `6ddbead2`. Any commit there means the delta moved: stop and hand back for the
brief to be updated. Otherwise review the work as it stands at your HEAD, and pin that SHA in your
verdict's scope.

**Machine-local surfaces no other review will catch** (read-only; report them in public-safe
terms, never a home path or a private name):

- `ccfleet` on `PATH` is a link to the primary checkout's `instruments/ccfleet`, and the plugin
  is installed in place from that checkout, so the drain runs the primary checkout's copies.
  The primary checkout was clean at `efeccf16` when this brief was written, which holds
  `a1cc5f2d`. Re-read where it stands when you start; never touch it.
- The `python3` on `PATH` is 3.14.6; `/usr/bin/python3` is 3.9.6. `ccfleet` claims Python 3.8
  or later, standard library only.
- The `model` the spawning tool accepts is a property of the harness, not of this repo. Read it
  off your own harness (the `Agent` tool's `model` parameter in your own tool schema) rather than
  from the delta's account of it.
- `ccfleet check` on this machine prints the user-level settings and instruction file a launched
  session keeps. Read it with a synthetic config only (below); quote no path or content from it.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the authors' claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1); these are a floor, never a fence.

**The reset (`RK5`'s fix)**

1. `reset_utc` stops new work only: "no new start at or after it (a budget reset); a resume or a
   fold, which finishes a started pass, still runs" (`--doc`); the manual says the same and adds
   "they run after it on the principal's word only".
2. A fold is `run --in WT --item ITEM`; `run_one` refuses at the reset unless the call is that
   shape (`existing and remove_adopted`), so "a plain run, and a run --in without --item, are
   still refused" (the new test's docstring).
3. `run.md` § *Mode 2*: "A pass whose act 2 is already written needs only the fold …, which costs
   no review budget: take it before a resume. Leave `reset_utc` as the drain set it: it stops new
   passes only, and ccfleet runs a `resume` and a fold … after it, since both finish a pass
   started before it."
4. The new test pins all of this, and the fold it runs after the reset starts one session and
   releases its claim.

**The reviewer prompt's home (`RK2`'s fix)**

5. The reviewer prompt's one home is the end of `orchestrator-prompt.md`, under *THE REVIEWER
   PROMPT*, "so every pass carries it in its own prompt and needs no read outside its worktree (a
   pass runs in another repo, where a path into this skill does not resolve)"; `run.md` "does not
   restate it".
6. The orchestrator prompt: "it is all here, so read no file outside this worktree for it".
7. The fold prompt: "Everything the fold needs is in the steps below: read no file outside this
   worktree but the held copy and the review log."
8. The moved bullets are the same text `run.md` held, moved, not rewritten.

**`REVIEW_MODEL`**

9. `REVIEW_MODEL` is "the review tier as the Agent tool names it: `fable`, `opus`, `sonnet` or
   `haiku`, never a full model id, which that tool refuses; the one value that puts the reviewer
   on the review tier" (`run.md`'s variables table); the example config now sets an alias.

## Scope

The widest the work admits: intent, decisions, assumptions, design, prompt text, code, test code
and live behaviour, for these three fixes as they stand at your HEAD. The lenses organise it;
they do not bound it. Anything not named a non-goal is in scope, and a non-goal that fences off
the risk is a finding.

**Non-goals:**

- The rest of the `210/600` fixes and `f4360a79`, except where they touch a line this delta wrote
  or depends on (above). Grounds: `160/1810` is their queued pass, and the principal's pick was a
  check of "just those fixes".
- Any estate's private ccfleet config, queue tool, rulings and run results, including the
  read-only check of a real config and the trial pass the record describes. Grounds: private by
  design, and this repo is public. Judge the contract through the example config and a synthetic
  queue; open no real config. In phase 2, say what the record's account of those can and cannot
  show from here (V1).
- The general drain design (`review plan`, the seal, Mode 1's ranking): reviewed by the earlier
  pass and changed under `160/1810`. In scope only where a fix here changes what they do.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   For each fix: is it the right fix for the defect as you find it in the code and prompts, or
   does it move the risk somewhere else? Is the way the code tells a fold from new work the right
   test? Is moving the reviewer prompt into the orchestrator prompt the right home, and what does
   it cost the one-home rule (V4)? Is a model alias the right value to put a reviewer on the
   review tier, and what does the record show about which model ran?
2. **Correctness & quality.** Re-drive the claims above against the code, the prompts and the
   test, by probe, not by reading. Drive `run_one`'s reset check through every launch shape the
   tool offers (`run`, `run --in`, `run --in --item`, `pass`, `drain`, `drive`, `resume`) on a
   synthetic config whose reset has passed, and say which start and which are refused, against
   what the doctrine says should. Render each review prompt through `ccfleet` and read what a
   pass, a resume and a fold are actually handed. Record each overclaim against the text that
   makes it, including any claim no test pins.
3. **Completeness / harvest.** Every surface that states the reset rule, the prompts' homes or
   the `REVIEW_MODEL` value agrees (docstring, `--doc`, `--help`, manual, `run.md`, the prompts,
   the example config, `instruments/README.md`, `CHANGELOG.md`: V3, V5). Find tests that would
   stay green on a broken fix by mutating a scratch copy of `ccfleet` and the prompts. What the
   fix should have covered and did not, in `resume-prompt.md` and the other prompts a drain hands
   out included.
4. **Security & privacy**, mandatory. Design altitude: what the reset change lets an unattended
   session do after a budget's reset that it could not before, and who decides it; what a prompt
   now carries into every repo a drain reaches, public ones included. Code altitude: the likely
   vectors for the class, checked against an open catalogue (OWASP ASVS or the domain's
   equivalent), not recalled: argument and config values flowing into the reset decision, the
   rendered prompt and the spawned model. Aim `/security-review` at the code only from a clean
   tree; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once, on 2026-11-25 UTC, at
`6ddbead2`, from the places named; the results are held in the sibling. Read exit codes
explicitly. Check `uptime` first; one heavy process at a time, under `nice -n 15`, foreground with
a long timeout: other sessions share this machine.

From the worktree root:

```
git merge-base --is-ancestor a1cc5f2d HEAD; echo "exit=$?"
mandoc -T lint -W style instruments/man/ccfleet.1; echo "exit=$?"
python3 instruments/ccfleet --doc | grep -n -A1 '^  reset_utc'
grep -nE 'run\.md|skills/review/' skills/review/orchestrator-prompt.md \
  skills/review/fold-prompt.md skills/review/resume-prompt.md; echo "exit=$?"
```

From `instruments/` (the tests load `ccfleet` by path; run on both interpreters, since the
runtime claim is 3.8 or later):

```
nice -n 15 python3 -m unittest -q test_ccfleet.EndToEnd.test_a_fold_runs_after_the_reset_and_new_work_does_not; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_ccfleet.EndToEnd.test_a_fold_runs_after_the_reset_and_new_work_does_not; echo "exit=$?"
nice -n 15 python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 15 /usr/bin/python3 -m unittest -q test_ccfleet; echo "exit=$?"
```

From `tools/` (the guard over the skill files the delta edits):

```
nice -n 15 python3 -m unittest -q test_subject_skills; echo "exit=$?"
```

**One mutation, in your scratchpad.** Copy `instruments/ccfleet` and `instruments/test_ccfleet.py`
into `<scratch>/instruments/`, replace the line `    if reset_reached(cfg) and not (existing and
remove_adopted):` in the copy with `    if reset_reached(cfg):`, confirm the old text is gone
(`grep -c 'not (existing and remove_adopted)' <scratch>/instruments/ccfleet` prints 0), and from
`<scratch>/instruments/` run the named test above under `nice -n 15 python3`. Read its exit code.
More mutations are yours to choose (lens 3).

**A dry run on a synthetic config**, in your scratchpad only. Make a throwaway git repo with no
remote under a scratch `repos_root`, marked private; a config whose `kit_dir`, `repos_root` and
`worktrees_root` are scratch directories, `claude_bin` set to `/usr/bin/false` (so nothing can
start a real session), one invented private name, `reset_utc` in the past, `pass_prompt` at your
worktree's `skills/review/orchestrator-prompt.md`, the five adopter variables `run.md` names for
that prompt plus `FINISH_WORDS`, and a plain run template with no placeholder but `{REPO}`; and a
copy that adds a `queue` whose `next`, `ranked`, `take` and `release` are a small scratch script
that logs every call it receives and exits 0. Make one scratch worktree of the repo whose
basename is the repo's name. Then, with `--config` on each, from the worktree root:

```
python3 instruments/ccfleet --config <cfg> check --prompt skills/review/orchestrator-prompt.md; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> check --prompt skills/review/fold-prompt.md; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> check --prompt skills/review/resume-prompt.md; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <repo> --prompt <plain template> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <repo> --prompt <plain template> --in <scratch wt> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <repo> --prompt skills/review/fold-prompt.md \
  --in <scratch wt> --item 020 --set BRIEF=<any> --set HELD=<any> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg with queue> run <repo> --prompt skills/review/fold-prompt.md \
  --in <scratch wt> --item 020 --set BRIEF=<any> --set HELD=<any> --dry-run; echo "exit=$?"
```

Read the output of each, `<kit_dir>` afterwards, and the scratch queue's log. How the
brief-writer built its config, and what it saw, is in the sibling. Go beyond these to the launch
shapes lens 2 names.

**Live behaviour.** The prompts' effect rests on a model following prose, and the record's live
trial ran on a private config this pass cannot open. Re-drive what you can read-only. At most a
few real launches, and only if your orchestrator's spawn prompt says you may spend on them, all
on the cheapest model, in a throwaway repo under your scratchpad, with no permission-mode argument
and a scratch config like the one above with `claude_bin` set to the real binary: one `ccfleet
run` of the orchestrator prompt against a stand-in queue and a dummy brief, `REVIEW_MODEL` set to
the cheapest alias, reading afterwards, through a scratch script that prints tool names, paths
and counts and never content, which files its sessions read and which model its reviewer was
spawned with. Otherwise mark it NOT RUN with grounds. Never run `ccfleet` against a real repo,
never `drive` or `drain` for real, and never with a real config. The brief-writer ran no real
launch.

## House rules for this run

- **Live systems:** read-only reads as needed; no live writes. A check that needs a write is
  marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Other sessions' transcripts are read only through
  a script that prints keys and counts; quote none of their content. `ccfleet check` prints the
  user-level settings and instruction-file path: quote neither. Probes use scratch copies and
  synthetic fixtures under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad, and
  never touch the primary checkout (the installed `ccfleet` and the in-place plugin run from it).
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
pass's above included), every item under `docs/roadmap/160-doctrine-review-owed/` beyond its
title, the delta commit's message body and those of the later commits named above,
`docs/method/census/`, and beyond their first line:

- `docs/roadmap/210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md`
  (the intent record: it gives the authors' account of this delta and of a live trial of it)
- `docs/roadmap/210-instruments-open-features/610-ccfleet-follows-the-private-import-for-private-repos-only.md`

All of these carry an author's account of the work, or the earlier verdict's findings.

**This brief's held-back sibling is not in the tree.** Whoever orchestrates the pass holds it
outside the repo and every worktree, and releases it to you only after your act 1 is committed;
by count it holds 16 questions and 14 facts. Never look for it in git history, other checkouts,
scratchpads or temporary directories. Run by hand with no orchestrator, you open it yourself, as
a deliberate second act, after act 1 is committed, and disclose when.

The delta's own comments, docstring, manual, prompts, skill text, test and `CHANGELOG.md` entries
carry the authors' account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/600-fix-ccfleet-subject-skills-and-modelguard-rk1-rk29.md \
  --also-exclude docs/roadmap/210-instruments-open-features/610-ccfleet-follows-the-private-import-for-private-repos-only.md \
  --also-exclude docs/method/census \
  "reset_utc|REVIEW_MODEL|THE REVIEWER PROMPT"
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the
re-run list, over the three fixes as they stand at your HEAD, cold: you have not read the earlier
verdict, so judge the code and prompts on their own terms, not as fixes. Append your verdict below
a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, your
orchestrator with its spawn prompt, what you read, the UTC day, the HEAD you pinned), per-lens
answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption damaged or
confirmed with its probe, a ledger of the later commits you read and what each did to a line this
delta wrote, findings with stable IDs (prefix `DV`: `DV1`, `DV2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger, the method record `REVIEW.md` § *The lifecycle* requires, and a follow-up checklist. Then
STOP: act 1 is committed, unrevised, **before** the sibling or the earlier verdict is opened.
Edit no other file.

**Phase 2 (act 2).** Open the sibling, the earlier verdict and the barred records; screen the
delta commit's body. Append `### Reconcile` beneath your verdict, with:

- **The RK ledger, one row each for `RK2`, `RK5` and `RK12`, and one for the `REVIEW_MODEL`
  correction:** what the earlier verdict counselled (by pointer, not restated at length), the
  file:line at your HEAD that answers it, how you re-drove it (the command and its result, or the
  earlier verdict's own reproduction re-run), and its state: *fixed as counselled* · *fixed
  another way* (and whether that way meets the finding) · *partly fixed* · *not fixed* ·
  *regressed* · *outside this repo* (for a check that only an estate's private config can show,
  with what the record claims and what V1 makes of it). Reading a fix is not re-driving it (V2).
- Per-finding notes on your act-1 findings against the sibling's questions and the authors'
  account; any finding formed at reconcile, marked as such, with a `DV` id after your last.
- The residual risk, named: act 2 reads the earlier verdict, so the RK ledger is anchored on it
  by design; act 1 is the cold half.
- The overall line restated.

Never revise act-1 text. Then fold the sibling in below the reconcile.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per
finding is welcome, labelled as counsel and kept beneath it. Under the overall verdict, say
plainly in two lines: whether anything you found loses, misreads or mis-tiers paid review work;
and whether the drain may run on these three fixes as they stand at your HEAD, and if not, what
must change first. Name `160/1800` in your scope line, and `210/600` as the item the fixes answer
to.
