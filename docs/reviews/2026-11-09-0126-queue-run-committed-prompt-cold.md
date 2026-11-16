# Cold pass — `/atelier:queue-run` reads the committed prompt, warns on a pending edit, and the teardown rule's three legs (`160/900`, QK1 and its counsel applied)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN, acts 1 and 2, by a Fable 5.1 reviewer under the principal's drain order of
2026-11-15 UTC (act 1 written 2026-11-15 UTC after a usage-limit cut and his word to resume; act 2
written 2026-11-16 UTC). PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 3 minor · 4 note (QC1–QC10),
all the principal's to decide. The sibling is folded beneath the reconcile by the
orchestrator.
**Sizing:** **medium** — one commit, 303 lines over eight files: a skill, its test, and four
doctrine surfaces, with process behaviour to re-drive.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1060-rule-4-cold-pass-queued-queue-run-reads-the-committed-prompt.md`.
**Why it earns a review:** Every queue run starts from this command, and what the command runs is an
instruction channel into every session it opens. Worst failure: a run executing prompt text that
nothing has checked, while saying it ran the committed copy; or a teardown rule that removes the
only copy of a worker's work.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched, which wrote it (per the
  queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `84e3aa7f` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). Neither authored any of this delta,
  and neither was started or instructed by the author. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing its briefs. It ran
  no review and used no Fable model. The principal's rule: whoever writes a brief does not run it.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  list of board items, the run constraints, and the principal's request verbatim, "Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done". It carried no framing of the
  work. The brief-writer had no contact with the author or its workers.
- **Who reviews:** a fresh Fable 5.1 session or subagent started for this pass alone, from a spawner
  that passes rule 4's criterion. **Barred from reviewing:** session `722ac2e2` and everything it
  started; session `84e3aa7f` (this brief-writer); session `74f2b8cd`. Whoever takes the pass states
  the spawn in the verdict (V7).
- **The principal's approval:** none yet for the pass. His request above covers this brief only. The
  pass waits for his explicit permission for Fable work.

⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):

- its dispatch text; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` whole; the
  house-form brief `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` through
  line 728, including its verdict (read for shape, another surface); the top of one sibling brief;
- the queue pointer whole; excerpts of the intent record: the lines naming the applied findings and
  the principal's answers, which include one-line summaries of the earlier verdict's findings;
- the delta body-free through `tools/coldsweep.py --commit 663b978a` (subject, stat, diff, never the
  message body), `--help` of `coldsweep`, `board`, `leakscan` and `reviewscan`, commit subjects
  through `git log`, and file names under `docs/reviews/` and
  `docs/roadmap/160-doctrine-review-owed/`;
- the last three index lines of `docs/SESSIONS.md` and one earlier session record, read for the
  format of its own closing record; and the results of the re-run lines below, held in the sibling.

It did **not** open `docs/ROADMAP-DONE.md`, any other session record, any other prior verdict, or
any delta commit's message body. Its harness also loaded user-level and repo instruction files and a
memory index, which hold private context this brief does not carry. Everything evaluative it formed
is in the sibling.

## The acceptance test

The principal's answer of 2026-11-08, as the delta records it in `skills/queue-run/SKILL.md` and
`docs/method/session-open/README.md`: *"Keep edit; read committed only"*. An answer to options
offered, not a ruling in his own words. The standing requirement it serves is his of 2026-10-18,
quoted in the same skill header: *"You need to ensure the there is no drift between the command and
the text file unless I authorise the drift"*.

## What the work is

One commit on `main`, `663b978a` (first confirm your tree has it: `git merge-base --is-ancestor
663b978a HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 663b978a \
  --path skills/queue-run/SKILL.md \
  --path tools/test_queue_run_single_source.py \
  --path docs/method/CONCURRENCY.md \
  --path docs/method/RECORD.md \
  --path docs/method/README.md \
  --path docs/method/session-open/README.md \
  --path README.md \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 663b978a..HEAD -- skills/queue-run/SKILL.md tools/test_queue_run_single_source.py docs/method/CONCURRENCY.md docs/method/RECORD.md docs/method/README.md docs/method/session-open/README.md README.md CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- The command reads the committed copy of the prompt (`git show HEAD:`) and never the working file,
  and says so when an edit is pending.
- An install that is not a git checkout reads the file and says so.
- The skill body adds no rule of its own, only delivery, and each addition is pinned by
  `tools/test_queue_run_single_source.py`.
- The teardown rule rests on three legs (marker, harness notice, a check of the worktree itself),
  and work is merged or pushed before removal.
- A run started by the command takes the away cadence by default.
- The identifiers list is `RECORD.md`'s alone.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** QK1's second counsel and QK5, which the principal has kept (the delta says so); the
prompt's own wording.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. The session-open prompt is an instruction channel, and
`docs/method/session-open/README.md` now carries a threat note for it. Test that note: who can
change what runs, what catches a hostile commit, and whether any step in the skill falls back to
unchecked text. Run `/security-review` only where it can reach the code; most of this delta is
markdown, where a clean pass means nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane hook --root .` and `--plane ci`
- `cd tools && python3 -m unittest test_queue_run_single_source test_templates`
- `R=<your worktree root>; git -C "$R" rev-parse --show-toplevel; git -C "$R" show HEAD:docs/method/session-open/session-open-prompt.md | wc -l; git -C "$R" status --porcelain -- docs/method/session-open/session-open-prompt.md | wc -l`

Reproduce the floor first with the full suite: `nice -n 10 python3 -m unittest discover -s tools`.
The brief-writer did **not** run that line, because the machine was at a load average of about 14
from other live sessions while it wrote this brief; the targeted lines above it did run.

## House rules for this run

**Live systems:** read-only reads of live systems as needed, no live writes. A check that would need
a write is marked **NOT RUN**, with what it would have checked. No push and no `gh` call that
writes, except committing this one file as the process below says.

- Never print a secret, and quote no key body, fixture bytes, personal data, private repo name or
  private path. This repo is PUBLIC; a child is referred to by type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Scratch
  repos, mutated copies and fixtures go under your session scratchpad and are deleted when you
  finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/` or
  `instruments/`.
- One heavy process at a time, foreground, long timeout, `uptime` first. Never run an installed tool
  by bare name from `PATH`: run it from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it only from a clean tree
  at a scratch clone of the code, or discharge it by grounds; never with this brief or its sibling
  dirty. A clean pass over markdown is weighed as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, The earlier verdict is
`docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md`. the queue pointer above, this
brief's sibling (its `.deferred.md` file, now folded below the verdict), every
delta commit's message body, and the intent record
`docs/roadmap/160-doctrine-review-owed/900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred. This pass reviews the application of an earlier pass's findings, so the delta's own
text carries that verdict's finding identifiers and decision stamps: `REVIEW.md` § *Applying
decisions to doctrine* names this as a residual exposure that cannot be closed. Review the edited
text at HEAD and commit your findings first.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1060-rule-4-cold-pass-queued-queue-run-reads-the-committed-prompt.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`663b978a`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `QC`: `QC1`, `QC2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling
is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it.

---

# Verdict — act 1 (2026-11-15 UTC)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 2 minor · 3 note (QC1–QC8).** The
delta does what it says at the behaviour level: the command, as the harness renders it, reads
`git show HEAD:` on the prompt from the clone, warns on a pending edit, falls back only where there
is no checkout, and the three-leg teardown rule is sound and reconciled with `RECORD.md`. What it
overstates is what the committed read *buys* (QC2, QC3) and how much its new test *pins* (QC1).

## Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection, run as a subagent for
  this pass alone. Spawned by headless orchestrator session `9cdae066` (Opus 5.5), itself started
  by drain session `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators as `REVIEW.md`
  rule 4 allows: they hold the context partition, formed no finding and wrote no severity. Neither
  wrote the brief or the delta. I was not started or instructed by any session the brief bars
  (`722ac2e2` and everything it started, `84e3aa7f`, `74f2b8cd`), and no session contacted me
  after the spawn.
- **The principal's permission:** his weekly Fable drain order of 2026-11-15 UTC (`/fable-drain`,
  06:53 NZDT on 2026-11-16). The pass was cut by the weekly usage limit at about 22:30 UTC, mid
  act 1, before anything was written to this file; it resumed at 23:54 UTC on his word, verbatim:
  *"resume to finish everything that was partly done i.e. in-progress"*. Nothing was lost but the
  full-suite run, which is re-run below; the work log carries both halves.
- **Orchestrator direction, as received (process only):** the item id; the worktree (its name is
  `atelier-160-1060-2215`; read-only to me except this file and the work log); the brief path;
  "act 2 is folded by the orchestrator, you write the reconcile only"; the partition (the
  `.deferred.md` sibling removed from the tree on purpose, not to be sought anywhere); a work-log
  path outside the repo; the write rules (this file only, no git writes, no live writes, no
  `gh` writes); the load rules (`nice -n 10`, one suite at a time, single process, `uptime`
  first); public-repo wording; the deliverable's shape and the two end lines. No question about
  the delta, no pointer to where risk lives, no request about any finding.
- **What I read before writing (exposure, disclosed):** the brief whole; `REVIEW.md` whole; the
  delta body-free through `coldsweep --commit 663b978a --path ×8` and the later `07892b82` through
  `--commit --path` on its two doctrine files only (its four board files left out by default);
  at HEAD: `skills/queue-run/SKILL.md`, `tools/test_queue_run_single_source.py`,
  `docs/method/session-open/README.md`, `session-open-prompt.md` (read to test the skill; its
  wording is a non-goal), `dispatch-brief.md`, `CONCURRENCY.md` lines 840–1290, `RECORD.md` lines
  90–215, `COMMUNICATION.md` lines 360–395, `tools/test_templates.py` lines 540–640, `README.md`,
  `docs/method/README.md`, the plugin manifests. Two board items **not** on the barred list, read
  for grounding and disclosed: `180/090` (one text for the command and the hand copy) and
  `180/020` (the teardown hand-up). I did **not** open `ROADMAP-DONE.md`, any session record, the
  prior verdict, the sibling, the queue pointer, the intent record past its title, or any commit
  body. My harness loaded user-level and repo instruction files and a memory index, which carry
  private context this verdict does not. I skipped the session-log onramp step (rule 2).
- **Two reads outside the repo, disclosed:** (a) the harness's plugin registry and the plugin
  cache directory on this machine, read-only, fields allowlisted, no path recorded here; (b) the
  public Claude Code plugin docs, fetched by a Haiku web-fetch agent that formed no finding. And
  one tool call to note: I invoked the `atelier:queue-run` skill through the Skill tool **only to
  read the text the harness renders**, and did not follow it; the rendered body is what a real run
  receives, so it is the delta's live behaviour. The run itself (a write-heavy act) was NOT RUN.
- **Load:** `uptime` before every heavy command; 15-minute load 5.4 at open, 2.5–3.4 later. Every
  suite under `nice -n 10`, one at a time, single process.

## The acceptance test

Met as stated. His 2026-11-08 answer *"Keep edit; read committed only"* is what the skill does:
the edit stays in the working tree (nothing in the skill touches or commits it) and the run reads
the committed copy. His 2026-10-18 requirement, no drift between the command and the text file
unless he authorises it, is served in the narrow sense (the command runs text that has a commit
behind it) and reopened in one place he owns: his prompt still says the command *"runs exactly
this file, so the command and this text cannot differ"*, which a pending edit now makes untrue
until committed (QC6, his to decide).

## Load-bearing assumptions, named first and probed

| # | Assumption | Probe | Result |
| --- | --- | --- | --- |
| A1 | A local-path install loads the clone in place, so a working-file edit could run | The harness registry lists a cached copy of the plugin (pinned to a 2026-10-18 commit, not a git checkout) that lacks two skills added 2026-11-14; both appear in this session's skill list. The public docs say a relative-path plugin in a locally added marketplace "loads in place". | ✅ Confirmed; the cache is a stale artefact of the first install |
| A2 | `${CLAUDE_PLUGIN_ROOT}` is usable in the skill's commands | `echo ${CLAUDE_PLUGIN_ROOT:-UNSET}` in the shell tool prints `UNSET`; the Skill tool's rendered text carries the clone's absolute path in its place. | ⚠️ Holds because the harness substitutes it before the model reads; a model reading the file from disk would run `git -C ""`, which is the current directory (QC7) |
| A3 | A commit is a trust boundary: committed text "has met the hook, the tests and review" | The hook plane is scanners only (`floor.py --plane hook` lists no test); a local `git commit --no-verify` skips it; the tests run in CI on a push, which a local-path install does not need; the README's own third bullet says committed is not reviewed. | ❌ Damaged: a commit is a *trace*, not a check (QC2, QC3) |
| A4 | The additions are "each pinned by that test" | Seven mutations on scratch copies (below): the positive pins hold; the delivery-only and known-files checks pass four of six rule insertions. | ⚠️ Partly damaged (QC1) |
| A5 | The harness's finished notice reaches a live orchestrator only, and never for a separate-session worker | Consistent with `RECORD.md` (the "didn't finish" notice appears only on resume) and with the harness's shape (a notice goes to a parent; a session has none). Not live-driven: it would need a crash. | ✅ Reasoned, not re-driven |
| A6 | The marker is the worker's last line, so marker-in means stopped | A subagent's report arrives when it ends; a session worker's marker travels by its report. | ✅ Holds; for a subagent, leg 3 adds nothing (QC8) |
| A7 | Right altitude: fix the delivery skill, defer the say-so check to his ruling | The answer was to a delivery question; the stronger control is QK1's second counsel, a non-goal. | ✅ Right altitude; the README names the gap |

## The four lenses

1. **Approach & assumptions.** The right problem at the right altitude: the skill is the one
   place every run starts, and reading the committed copy there costs two git commands. The
   framing I attacked: the brief says the worst failure is "a run executing prompt text that
   nothing has checked, while saying it ran the committed copy". The delta closes the *working
   file* path to that failure and leaves the *commit* path open while describing the commit as a
   check (A3). That is the one approach-level defect, and it is in the words, not the mechanism.
2. **Correctness & quality.** Behaviour re-driven from the rendered skill: step 1's test is true
   on this machine (real path equals the path given; `rev-parse --show-toplevel` prints it);
   `git show HEAD:` returns 161 lines; `status --porcelain` on the file prints nothing (no pending
   edit); the clone is on `main`. Steps 1–3 are unambiguous for the two shapes they name and
   silent for a third (QC7). Overclaims recorded: QC1 (what the test pins), QC2 (what a commit has
   met), QC5 (where the away sentence sits).
3. **Completeness / harvest.** Mirror sites swept with `coldsweep` (barred set excluded by
   default plus the two `--also-exclude`): the answer quote sits on four surfaces and the
   `07892b82` relabel reached one (QC4); the teardown wording has one home plus the dispatch
   brief's marker line and no child-template restatement (clean); the identifiers list has one
   home (`RECORD.md` § *The session log*) and `CONCURRENCY.md` points at it (clean, V4). Tests that
   stay green on a broken change: QC1.
4. **Security & privacy** (V6). Threat note tested as the brief asks. *Who can change what runs:*
   anyone who lands a commit on the clone's checked-out branch (not only `main`: `HEAD:` is the
   checked-out branch), and any process running as the user, which can commit as easily as it can
   edit. *What catches a hostile commit* on a local-path install: a human reading the diff, and
   the history trace; the scanners are bypassable and the pins run in CI after a push the install
   does not need (QC3). *Does any step fall back to unchecked text:* step 3 reads the working
   file where there is no checkout or `git show` fails, and says so; the one unnamed branch is
   QC7. `/security-review`: **discharged with grounds** — the delta is landed, not pending; the
   worktree is dirty with the barred sibling's deletion and this brief, so the scanner would read
   the wrong thing; and the code in scope is a test that reads two repo files, with the rest
   markdown, where a clean pass weighs nothing. No personal data, secret or private name enters
   the delta (leakscan and pdlistscan green at HEAD).

## Standing checklist

- **V1** — three claims past their evidence: QC1, QC2, QC5.
- **V2** — every re-run line re-run (ledger below); all reproduce.
- **V3** — one partial sweep: QC4. Teardown and identifiers sweeps clean.
- **V4** — one home each for the identifiers list and the teardown rule; the README and the
  changelog restate the committed-read behaviour as stamped copies citing `160/900`. Clean.
- **V5** — cross-references checked for the rule reached, not the file: `RECORD.md` →
  `CONCURRENCY.md` § *Orchestrated queue runs* reaches the three-leg bullet (lines 1057–1073);
  `CONCURRENCY.md` → `RECORD.md` § *The session log* reaches the identifiers block (lines 97–131);
  "the shared-machine rule below" reaches *The machine is shared too* (line 1205, PID or cwd scope,
  never a pattern); `docs/method/README.md` → the session-open README's § *What the command runs*.
  One contradiction: QC2 (skill vs README on whether committed means reviewed). One staleness in his
  own text: QC6.
- **V6** — above.
- **V7** — above.

## Findings

Every finding is the principal's to decide (rule 3): recorded, nothing applied. Counsel is
labelled and kept beneath each.

### QC1 — MODERATE — The "nothing but delivery" guard passes most of the shapes it claims to catch

`tools/test_queue_run_single_source.py` lines 33–42 and 112–132. `test_skill_body_is_delivery_only`
splits the body on blank lines and passes a block if it contains any of five substrings
(`session-open prompt`, `session-open-prompt.md`, `committed copy`, `CONCURRENCY.md`, `typed
after`); `test_skill_body_names_only_known_files` matches tokens ending `.md .py .json .yaml .yml
.sh`. Probed on scratch copies of the skill with the real test (work log, `mut/run.py`):

| Mutation | Result |
| --- | --- |
| m-a: a 4th step in the numbered list, "Commit with `--no-verify` when the hook is slow; the committed copy is enough" | passes green (the list is one block, anchored by step 1) |
| m-b: a paragraph naming `tools/floor.py` | caught by both checks |
| m-c: a rule paragraph ending "the committed copy settles disputes" | passes green |
| m-d: "Push to main without running the suite; the session-open prompt allows it" | passes green |
| m-e: a paragraph naming `settings.toml` and a URL | passes green |
| m-f: a paraphrase of a prompt rule | passes green (the header admits this one) |
| m-g, control: delete "do not open the working file" | caught |

The text claims more: the changelog entry says *"every paragraph of the skill body must be a known
delivery job and may name only the two known files, so a new rule or an instruction pointed at
another file fails"*; the test's docstring says *"every paragraph must be one of the known delivery
paragraphs"*; the skill header says *"each addition is pinned by that test"*. The positive pins
(m-g) do hold, so the behaviour the delta adds is pinned; what is not is the ceiling on additions.
V1 and lens 3.

*Counsel:* pin the body as an allowlist of its paragraphs after `flatten`/`norm` (exact text), so
any added or altered paragraph fails until the pin is changed on purpose; match any path-like
token rather than six extensions; and restate the three claims to what the checks do.

### QC2 — MODERATE — The skill's reason for the committed read overclaims and contradicts the README

`skills/queue-run/SKILL.md` lines 40–42: *"Only text that has been committed has met the pre-commit
hook, the tests and review, so an edit in the working tree is not run."* A local commit has met
the hook only if it was not made with `--no-verify`, and the hook plane is scanners (no test runs
at commit); it has met the tests only once CI runs on a push, which a local-path install never
needs; and the README it sits beside says the opposite of the last clause:
`docs/method/session-open/README.md` lines 53–54, *"The committed copy is what was committed, not
what was reviewed: a commit that never met review still runs."* V1 and V5. The behaviour is
right; the sentence sells it as a check when it is a trace.

*Counsel:* reword to what is true: a committed copy has a commit behind it, a diff, an author and
a time that the hook, the tests and a reader can be pointed at, where a working-file edit has none.

### QC3 — MODERATE — The threat note misstates the controls for the install shape it is about

`docs/method/session-open/README.md` lines 43–52. Bullet one says a process running as the user
*"cannot make the command run it unless it also commits"*: it can commit, with one command and no
privilege, and `--no-verify` skips the hook. Bullet two lists what catches a hostile commit: *"the
pre-commit scanners …, the four phrase pins in `tools/test_templates.py` …, and a human reading the
diff"*. For a local-path install the scanners are bypassable and the pins run only in CI after a
push the install does not need, so two of the three named catches do not reach the case the
section opens with. What the committed read buys there is that the change becomes a recorded
commit (a diff and a trace) instead of a silent file edit; the note should say so, and name the
one control that would close it, which it already records as unbuilt. Lens 4, mandatory.

*Counsel:* rewrite bullets one and two as: a local process can edit and commit; the read turns its
edit into a commit on the record; the scanners and pins catch a *pushed* commit; a local commit is
caught by a reader or by the say-so check that is not built. QK1's second counsel is a non-goal
here and is not re-argued.

### QC4 — minor — The "answer, not a ruling" label reached one of four surfaces

`07892b82` relabelled the skill header to *"Mike's answer, 2026-11-08"*. The same quote stands bare
as *"Mike, 2026-11-08: …"* in `docs/method/session-open/README.md` lines 36–37, the test docstring
line 12, and the changelog entry. The brief itself calls it an answer to options, and
`COMMUNICATION.md`'s record marks (💬 and the words "an answer, not a ruling") landed 2026-11-10, a
day after the delta, so the delta broke no rule in force; the partial sweep is the defect (V3).

*Counsel:* label all three the same way the header now is.

### QC5 — minor — "In its closing paragraph" is not where the away sentence sits

`docs/method/CONCURRENCY.md` lines 1131–1133: *"His session-open prompt … now says he is away in
its closing paragraph"*. The sentence (*"I won't be here to answer for several hours"*) is the
third-from-last paragraph of `session-open-prompt.md` (lines 152–154); two paragraphs follow it.
The inference drawn from it, that a run started by the command takes the away cadence, holds. V1.

### QC6 — note — The principal's prompt now states something the delta made conditional

`session-open-prompt.md` lines 18–19, his text: *"(`/atelier:queue-run` runs exactly this file, so
the command and this text cannot differ.)"* With the committed read, the command and the file as
he sees it in his editor differ whenever an edit is pending, until he commits. The prompt's wording
is a non-goal and his alone to change; recorded so he rules with it in front of him.

### QC7 — note — Step 1 names two shapes and the skill is silent on a third

`skills/queue-run/SKILL.md` lines 44–57. Step 1 fires when `rev-parse --show-toplevel` *"prints
that same path"*; step 3 when the plugin *"is not a git checkout"* or `git show` fails. A plugin
root reached through a symlink, or sitting inside a larger checkout, prints a different path and
is a checkout: neither step names it. On this machine the real path equals the path given and the
toplevel matches (probed), so the case is latent. Related: the variable the steps use is unset in
the shell (A2) and works because the harness substitutes it in the rendered text.

*Counsel:* test "a checkout whose tree holds the file" (`git -C <root> ls-files --error-unmatch
<file>`) and read `HEAD:<file>` relative to that toplevel; or state that any other result takes
step 3.

### QC8 — note — Leg 3 is evidence for session workers only, and the rule could say so in one clause

`docs/method/CONCURRENCY.md` lines 1064–1073. Leg 3 (`lsof +D`, "no process still running with the
worktree as its working directory") sees a worker that is its own session. A subagent worker runs
inside the orchestrator's process with the orchestrator's working directory and drives the worktree
by absolute path, so leg 3 reports nothing running while it is mid-verify: the 2026-09-07 shape.
The rule stays safe because removal also waits for the marker, and the leg's own last sentence
scopes it; a reader weighing the legs as alternatives could still misread.

*Counsel:* add "for a subagent, only the marker or the notice says stopped; a quiet `lsof` is not
evidence either way".

## Per-commit ledger

| Commit | Read body-free | How | Findings |
| --- | --- | --- | --- |
| `663b978a` | yes | `coldsweep --commit --path ×8`; 0 board files, 0 barred files touched | QC1, QC2, QC3, QC5, QC7, QC8 |
| `07892b82` | yes | `coldsweep --commit --path skills/queue-run/SKILL.md --path docs/method/RECORD.md`; its four board files left out | QC4 |

## Re-run ledger (2026-11-15 UTC, from the worktree root, `python3` 3.14 on PATH)

| Line | Result |
| --- | --- |
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | exit 0; every enforced check green |
| `… --plane ci` | exit 0; one 🟡 advisory (declarations), no red |
| `cd tools && python3 -m unittest test_queue_run_single_source test_templates` | 60 tests, OK |
| `git rev-parse --show-toplevel` · `git show HEAD:<prompt> \| wc -l` · `git status --porcelain -- <prompt> \| wc -l` | the worktree root · 161 · 0 |
| Full suite, `nice -n 10 python3 -m unittest discover -s tools` | first run cut with the session at ~22:30 UTC (no failure seen before the cut); re-run after the resume: see the line below |
| Full suite, re-run after the resume (load 3.4 at start) | 3134 tests in 729 s, OK, exit 0 |

**NOT RUN, with reasons.** A live `/atelier:queue-run` with a pending edit planted in the clone,
to watch the warning print: planting the edit is a write to a checkout that is not mine, and the
run itself writes; the behaviour was read from the rendered skill text instead. A crash of a live
orchestrator to re-drive leg 2: destructive. `/security-review`: discharged above.

## Follow-up checklist

- [ ] QC1 — the principal rules on narrowing the delivery-only guard to a paragraph allowlist and
      restating the three claims.
- [ ] QC2 — rule on rewording the skill's lines 40–42.
- [ ] QC3 — rule on rewriting the threat note's first two bullets.
- [ ] QC4 — rule on labelling the three remaining surfaces as an answer.
- [ ] QC5 — rule on "closing paragraph" → "a late paragraph".
- [ ] QC6 — his own text; his call whether lines 18–19 of the prompt change.
- [ ] QC7, QC8 — notes; counsel above if he wants them.
- [ ] Act 2: open the sibling and the barred records on release; reconcile beneath this verdict.

### Reconcile — act 2, written 2026-11-16 UTC

**Opened after act 1 was committed (`bf5e9312`) and the orchestrator released it:** the held
`.deferred.md` sibling (read at the orchestrator's user-local path, read-only, not copied; the fold
beneath this section is the orchestrator's); the queue pointer `160/1060` and the intent record
`160/900` whole; the message bodies of `663b978a` and `07892b82`; the prior verdict
`docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md` at QK1, QK6, QK9 and its whole
reconcile; `docs/SESSIONS.md` index lines for the 2026-10-18 and 2026-10-25 runs; the author's
session record `docs/sessions/2026-11-08-1059-ruling-round-722a.md` to line 40; `tools/quotescan.py`
header and `floor.py`'s message-plane wiring. **Not opened:** any other session record, any other
prior verdict, `docs/ROADMAP-DONE.md` beyond a search that returned nothing for `160/900`,
`160/1060` or `180/090`. Act-1 text above is unchanged; every change of view is stated here.

**The sibling.** The pointer's two questions and eight of the brief-writer's; nothing in it is a
finding, and nothing in it steered act 1, which was written before it was opened. Its re-run
results agree with mine in substance (56 tests then at `c132cc1c`, 60 now at HEAD, the two modules
having grown; the git triple the same). Its `pathscan` note, that the prompt's line 13 names a
`../atelier` path that does not resolve from the repo root, is the reason the bundled doctrine
path exists (QK3) and stands.

**Per finding, against the sibling's questions and the author's account:**

- **QC1 — stands, MODERATE, strengthened.** The author's account says the test "bars new rules and
  unknown files in the skill body" (`663b978a` body) and the intent record says QK9 was applied
  "as counselled". QK9's counsel was *"a check that the skill's body, comment aside, contains
  nothing but the pointer lines"*; what landed is five anchor substrings per block. The test's
  own comment claims it closes QK9's mutation m2 (a new instruction the prompt never had); my
  m-c and m-d are m2's shape and pass. The sibling's Q5 (what checks that a session actually
  read HEAD) is the same gap one level up: the test pins words, not behaviour, and the opening
  line "ran the committed copy" is self-report (QC10 below gives it a checkable trace).
- **QC2 — stands, MODERATE.** Q3 is the question. `HEAD:` is whichever commit is checked out:
  a feature branch, a detached head, an unpushed commit, a clone behind `origin/main`. The
  README's third bullet already concedes committed is not reviewed; the skill's sentence does
  not. No record claims otherwise.
- **QC3 — stands, MODERATE; one fact added, one strengthened.** Added: QK1's second counsel was
  built on 2026-11-10 as `tools/quotescan.py` on the commit-message plane (the intent record;
  warn-only until 2027-05-31 by the run's own choice; it reads the *form* of a quote, never
  whose words), so a local commit touching the prompt now meets one more check when the
  commit-msg hook is installed and not bypassed. That does not change the analysis: a
  user-level process bypasses hooks with one flag, and a form check cannot tell his words from
  anyone's. Strengthened by Q4: `git -C <root> show` runs under that repo's own config, so the
  same process can alias `show` or set a `core.pager` and have the "committed read" print what
  it likes; the threat note's "cannot make the command run it unless it also commits" is wrong
  in one more way. Q1 (what makes `git show` fail on demand): a renamed or untracked prompt
  path, a damaged object store, no `git` on `PATH`; step 3 then reads the working file and
  *says so*, which is a disclosed fail-open, not a silent one. Counsel for the principal, added:
  fail closed instead (stop and say the committed copy could not be read) on a checkout where
  `git show` fails; keep the working-file read for the no-checkout case only.
- **QC4 — stands, minor.** `07892b82`'s body says it "labels Mike's pick in the skill comment as
  his answer": one surface, by its own account. The intent record carries the 💬 mark correctly.
- **QC5 — stands, minor.** Q6: the record shows he was told the away sentence rides every
  command-started run (`180/090`'s 🚩, and the prior reconcile at QK7, "so he knows"); the
  inference is his to own and the position word is the only defect.
- **QC6 — stands, note.** QK1's own text in the prior verdict read the same sentence as "true of
  the working tree and false of the reviewed text"; after the delta it is true of the committed
  copy and false of the file he edits, which is the inverse. His to decide; counsel unchanged.
- **QC7 — stands, note, with Q2's case added.** A case-folding disk returns the on-disk spelling
  from `rev-parse --show-toplevel`; a root given in another case fails the text compare the
  same way a symlink does. The counsel (test by `ls-files --error-unmatch`) covers both.
- **QC8 — stands, note.** The pointer's second question (followable by a separate-session worker)
  is answered yes by the text itself; QC8 is the inverse case. Q7's three parts: `lsof +D` is
  slow on a large tree and the rule's safety does not depend on its speed; a worker still
  pushing while the orchestrator merges is safe because a pushed branch is at a whole commit;
  a worktree left when no marker comes is the rule's stated cost, said out loud in the report.
  QK6's counsel was applied as written.

**Findings formed at reconcile (marked as such):**

### QC9 — minor — The README says the say-so check "is not built"; it was, on 2026-11-10

*(Formed at reconcile, from Q8 and the intent record.)*

`docs/method/session-open/README.md` lines 50–52: *"Nothing yet reads whether a commit to this file
carries the principal's say-so: that check is not built (`160/900` QK1 counsel, awaiting his
ruling)."* True when the delta landed on 2026-11-09. `tools/quotescan.py` landed the next day
(the intent record's entry; `CHANGELOG.md` 2026-11-10; wired as `MSG_CHECKS` in `floor.py`), and
the README's only later commit (`9f3ece82`) did not touch the sentence. Not the delta's defect;
a V3 staleness at HEAD in the file this pass reviews.

*Counsel:* replace the sentence with what quotescan does and does not read (form, not
authorship; warn until 2027-05-31), so the threat note's second bullet names all its catches.

### QC10 — note — The opening report does not say which commit's prompt ran

*(Formed at reconcile, from the pointer's first question and Q3, Q5.)*

A stale clone, a feature branch or a detached head all pass steps 1–2 and run older or
sideways committed text; the report says "the committed copy" and nothing else, so neither the
principal nor a later reader can tell which text a run followed, and the test's "ran HEAD" is
unverifiable (Q5).

*Counsel:* add one line to the opening report: the short SHA of the prompt's last commit (`git
-C <root> log -1 --format=%h -- <prompt>`) and whether `HEAD` is behind `origin/main`. One line,
and the self-report becomes a trace a reader can check against `main`.

**Revised overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (QC1, QC2, QC3) · 3 minor (QC4,
QC5, QC9) · 4 note (QC6, QC7, QC8, QC10).** Changes from act 1: QC1 and QC3 strengthened on the
records, no severity moved; QC9 and QC10 added at reconcile. Because no MAJOR stands, `REVIEW.md`'s
close rule applies: the application of these rulings closes without another queued pointer, and
what remains is decided into the backlog. Every finding is the principal's to decide (rule 3);
nothing is applied. Follow-up checklist additions: QC9 — the README sentence; QC10 — the one
report line; QC3 — the fail-closed counsel.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

*Released to the reviewer only after its act-1 findings were committed (the commit "reviews
160/1060: act 1 of the queue-run committed-prompt cold pass", `bf5e9312` before it was rebased onto
`main`); folded here verbatim (headings demoted two levels) and the sibling file removed, per the
brief. The orchestrator (headless Opus 5.5 session `9cdae066`, started by drain session
`21a271a5`, itself Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-queue-run-committed-prompt-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

#### The queue pointer's questions (author-written, verbatim)

> whether an agent following the skill can still end up running uncommitted prompt text (a checkout
that is not the plugin root, a detached head, a stale clone); whether the three-leg teardown rule is
followable by a separate-session worker.

#### The brief-writer's own questions

1. Step 3's fallback reads the working file when `git show` fails. What can make `git show` fail on
demand, and is that a fail-open route to the very text the rule refuses?
2. "Prints that same path": a path compared as text, on a machine with symlinks and a case-folding
disk. What happens with a symlinked plugin root?
3. `HEAD` is whichever branch the checkout is on: a feature branch, a detached head, an unpushed
commit. Does "committed" deliver what the skill says it delivers?
4. `git status` and `git show` in the plugin root run under that repo's config. Does the threat note
account for it?
5. The test pins text in a skill an agent then interprets. What checks that a session actually read
HEAD?
6. The away-cadence inference: is it what the prompt says, and did the principal say so for every
run started by the command?
7. Three-leg teardown: `lsof +D` cost and reliability on a large worktree; a worker still pushing
while the orchestrator merges; worktrees left forever when the marker never comes.
8. A later series of commits touched these doctrine files after `663b978a`. Check the delta's text
still stands at HEAD.

#### What the brief-writer ran, and what it got

- `qr`: python3 3.14: 56 tests OK, exit 0.
- `skillcmds`: the first prints the worktree root; the prompt is 161 lines at HEAD; 0 lines pending.
- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*The Fable 5.1 reviewer's own work log, kept while it ran and unread by any other session until
act 2 was saved; appended verbatim (headings demoted two levels). Form fixes only, if any, are
listed here: none beyond the heading demotion.*

### Work log — atelier 160/1060 cold pass (Fable 5.1 reviewer)

Worktree: /Users/mike/worktrees/fable/atelier-160-1060-2215/atelier
Brief: docs/reviews/2026-11-09-0126-queue-run-committed-prompt-cold.md
Spawned by headless orchestrator 9cdae066 (Opus 5.5), itself by drain session 21a271a5 (Opus 5.5).
Public-safe log: commands, files, evidence only.

#### Act 1

- 2026-11-15T22:17Z `date -u; uptime` -> load 5.78. `git status --short` -> only ` D` of the
  .deferred.md sibling (removed on purpose, rule 1). HEAD 30c61dbd (board claim commit).
- Read brief in full (lines 1-218).
- Read docs/method/REVIEW.md whole (698 lines): rules 1-4, lenses, V1-V7, the 2026-11-15 method
  record ruling (verdict must record what it examined and reasoning).
- `git merge-base --is-ancestor 663b978a HEAD` -> exit 0 (delta is in the tree).
- `git log --oneline 663b978a..HEAD -- <8 delta paths>`: many later commits; per path:
  SKILL.md only 07892b82; test file none; session-open/README.md only 9f3ece82;
  CONCURRENCY.md 15; RECORD.md 13; docs/method/README.md 3.
- `tools/coldsweep.py --root <wt> --commit 663b978a --path x8` -> exit 0, 539 lines to scratch
  delta.diff; read whole. Banner: body not printed, 0 board files, 0 barred files touched.
- `coldsweep --commit 07892b82 --path skills/queue-run/SKILL.md --path docs/method/RECORD.md`:
  a 4-line SKILL header reflow ("Mike's answer, 2026-11-08") and a RECORD.md reflow. Its 4
  board files left out by default (not read).
- Read at HEAD: skills/queue-run/SKILL.md (whole, 66 lines); tools/test_queue_run_single_source.py
  (whole, 161); docs/method/session-open/README.md (whole, 132); session-open-prompt.md (whole,
  161; read to test the skill, its wording is a non-goal); CONCURRENCY.md 840-1290 (interrupted
  session + § Orchestrated queue runs); RECORD.md 90-215 (identifiers block, close rules);
  tools/test_templates.py 540-640 (queue-run pins); README.md 95-125; docs/method/README.md tail;
  session-open/dispatch-brief.md (whole); .claude-plugin/plugin.json + marketplace.json;
  COMMUNICATION.md 360-395 (answer vs ruling record marks).
- Board items read, NOT barred by the brief, disclosed: 180/090 (one text for command and hand
  copy) and 180/020 (teardown hand-up). Neither is the intent record or the pointer.
- coldsweep sweeps (barred set excluded by default + the two --also-exclude): 'Keep edit; read
  committed only' -> CHANGELOG:1470, session-open/README.md:37, test docstring:12 (no "answer"
  label on any of the three; SKILL header got it in 07892b82). 'WORKER DONE|harness.s notice|...'
  -> CONCURRENCY.md x3, dispatch-brief.md:34, board 180/020, 180/120 only (no child template
  restates the teardown rule). "an answer, not a ruling|Mike's answer" -> rule home is
  COMMUNICATION.md ~line 362-380 plus many stamped uses.
- Probe, local plugin install (read-only; registry fields allowlisted; paths not recorded): the
  harness registry lists a cache installPath (version 0.2.0, installed 2026-10-18T00:08Z,
  pinned sha b12c76d2) that is NOT a git checkout and whose files equal that sha's tree plus 69
  working-tree strays (.DS_Store, __pycache__). Its skills dir lacks review-drain and fleet-sweep
  (added 2026-11-14, 4bfb4e16) yet both appear in this session's skill list => the harness loads
  the plugin in place from the clone; the cache is a stale 2026-10-18 artefact. Clone: realpath ==
  path; `rev-parse --show-toplevel` == plugin root; HEAD on main; prompt has 0 pending edits.
- Web doc check (haiku web-fetch agent, code.claude.com plugin docs): relative-path plugins in a
  locally added marketplace load in place; CLAUDE_PLUGIN_ROOT points at the source directory;
  edits take effect at next session start or /reload-plugins; nothing said about git.
- Probe: `echo ${CLAUDE_PLUGIN_ROOT:-UNSET}` in the Bash tool -> UNSET. Invoked the Skill tool on
  atelier:queue-run ONLY to read the rendered text (did not follow it): the harness substitutes
  ${CLAUDE_PLUGIN_ROOT} with the clone's absolute path in the skill body, so steps 1-2 run as
  written. The rendered path is a private home path; not recorded.
- Re-run: floor --plane hook exit 0 (all enforced checks green); --plane ci exit 0 (🟡
  declarations advisory only). `cd tools && python3 -m unittest test_queue_run_single_source
  test_templates` -> 60 tests OK. Git triple from worktree root: toplevel printed; 161 lines;
  0 pending.
- Mutation probes on scratch copies of SKILL.md + the real test (scratch mut/run.py):
  m-a 4th list item "commit with --no-verify" -> passes green; m-b paragraph naming tools/floor.py
  -> caught (delivery_only + known_files); m-c rule paragraph containing "committed copy" ->
  passes; m-d rule paragraph containing "session-open prompt" -> passes; m-e paragraph naming
  settings.toml + a URL -> passes; m-f paraphrase of a prompt rule -> passes (known limit);
  m-g control, delete "do not open the working file" -> caught.
- Full suite (`nice -n 10 python3 -m unittest discover -s tools`, load 2.45 at start, 2026-11-15
  ~22:25Z) was moved to the background by the shell cap at 600 s and then cut with the session by
  the weekly usage limit at ~22:30Z: no summary line, process gone. Partial output showed no F/E.
- INTERRUPTED by the weekly usage limit during act 1, ~2026-11-15T22:30Z. Resumed 2026-11-15T23:54Z
  on Mike's order "resume to finish everything that was partly done i.e. in-progress". Brief file
  unchanged (act 1 not yet saved); worktree still ` D` sibling only, HEAD 30c61dbd; scratch files
  survived. Re-running the full suite to a scratch file with an exit line (load 3.41 at start).
- 2026-11-16T00:0xZ: Status line edited; act 1 appended below a `---` divider (verdict,
  provenance incl. the interruption, acceptance test, assumptions A1-A7, four lenses, V1-V7,
  QC1-QC8 with severities 0 MAJOR / 3 MODERATE / 2 minor / 3 note, per-commit ledger, re-run
  ledger with a FULL-SUITE-RESULT placeholder, NOT RUN list, follow-ups). Prose rewrapped to
  <=100 columns by a scratch script; table rows left wide (wrapscan exempts table rows,
  tools/wrapscan.py _is_table_row; an accepted brief in docs/reviews has 19 such rows).
  Self-check for private paths/names in the act-1 text: none (two "shed" hits were inside
  "finished").
- Waiting on the full-suite re-run (background, exit line in scratch suite2.txt) before running
  the repo gates on the brief (one heavy process at a time).
- Full suite re-run finished 2026-11-16T00:06Z: "Ran 3134 tests in 728.990s", OK, exit 0 (scratch
  suite2.txt). Placeholder in the re-run ledger replaced with that result.
- Gates on the brief: `floor.py --plane hook` exit 0 but it reads the staged set (0 briefs seen);
  `floor.py --plane ci` (whole tree, working files) exit 0, no finding names the brief; the
  individual scanners were then run directly on the brief file (next entry).
- Scratch mutation trees (mut/) deleted; scratch keeps only the diff and gate/suite outputs.
- Direct scanner runs on the brief file (--root <wt> <brief>): datescan 0 findings (494 lines
  read); reviewscan "1 review brief(s) keep deferred material out of the brief"; leakscan 0;
  attribscan clean. wrapscan and spellscan opened 0 files: docs/reviews is in .wrapscanignore and
  .spellscanignore, so the brief's own <=100-column rule is the one that binds (0 prose lines over
  100 by awk; table rows exempt). quotescan and pdlistscan take no file argument; both were green
  in the whole-tree ci plane (exit 0).
- 2026-11-16T00:1xZ ACT 1 SAVED in the brief (unstaged; the orchestrator commits). Worktree:
  ` M` the brief, ` D` the sibling. Stopping; waiting for the release message before act 2.

#### Act 2 (released by the orchestrator after act 1 was committed as bf5e9312)

- 2026-11-16T00:10Z act 1 confirmed committed as bf5e9312 (brief only). Release received.
- Read the held sibling (orchestrator's user-local path, read-only, not copied anywhere): the
  pointer's two questions verbatim; eight brief-writer questions; its re-run results (56 tests at
  c132cc1c; pathscan 3 warn-only findings incl. session-open-prompt.md:13).
- Read the barred records: queue pointer 1060 (whole); intent record 900 (whole: Mike's 💬
  answer of 2026-11-08, the APPLIED entry, his 2026-11-09 answers on QK4/QK5, and QK1's second
  counsel BUILT 2026-11-10 as tools/quotescan.py, warn until 2027-05-31); commit bodies of
  663b978a and 07892b82 (`git show -s --format=%B`); prior verdict
  docs/reviews/2026-10-18-0517-...-cold.md: QK1, QK6, QK9 findings (lines 379-405, 512-528,
  561-589) and the whole reconcile (659-770); SESSIONS.md index lines 324-326; session record
  docs/sessions/2026-11-08-1059-ruling-round-722a.md lines 1-40; tools/quotescan.py header;
  floor.py msg-plane wiring (MSG_CHECKS). ROADMAP-DONE.md: grep for 160/900, 160/1060, 180/090
  returned nothing (not read further).
- 2026-11-16T00:2xZ `### Reconcile` appended beneath the act-1 verdict: what was opened / not
  opened; the sibling's questions answered per finding; author's account screened (663b978a body
  claims "bars new rules" -> QC1 strengthened: the test's own comment claims m2 is closed and
  m-c/m-d show it is not; 07892b82 body confirms the one-surface relabel -> QC4); QC3 gains
  quotescan (built 2026-11-10, form-only, warn until 2027-05-31) and Q4's repo-config vector;
  reconcile-formed QC9 (minor: README "not built" sentence stale at HEAD since quotescan) and
  QC10 (note: opening report does not say which commit's prompt ran). Overall restated: 0 MAJOR
  / 3 MODERATE / 3 minor / 4 note (QC1-QC10); no severity moved. Status line updated to PASS RAN.
  Two long headings shortened to fit 100 columns. Act-1 text untouched.
- Gates after act 2: see the next entry.
- Gates after act 2: datescan 0, leakscan 0, attribscan 0 (598 lines read each); reviewscan "1
  review brief(s) keep deferred material out of the brief"; whole-tree `floor.py --plane ci` exit
  0 (🟡 declarations advisory only); 0 prose lines over 100 characters in acts 1-2 (table rows
  exempt); no private path or held-store name in the brief.
- 2026-11-16T00:14Z ACT 2 SAVED (brief unstaged; the orchestrator commits and folds the sibling).
  Scratch holds only the delta diff and gate/suite outputs; the orchestrator's own scratch files
  were left alone. No git writes, no live writes, no file outside the brief and this log touched.
