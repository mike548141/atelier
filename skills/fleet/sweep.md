---
action: sweep
description: Bring every child repo of an atelier estate to a healthy state — latest atelier pin with the floor re-copied verbatim, CI green at the pushed head, conformance with the current doctrine, every owed review briefed, the principal's queue of asks de-duplicated, every one-file record store split, nothing left behind by past sessions — each repo's work run as a headless session inside that repo so per-repo cost tools bill the repo. Use when the principal asks for a health sweep, to "bring the repos up to healthy", to bump every pin, or for one repo by name.
---

# Fleet health sweep

The runner is `instruments/ccfleet` (`ccfleet --doc` for its full reference).
Everything that belongs to one principal's estate stays out of this skill and
out of any public repo: the repo list, per-repo notes and tiers, the
principal's own words, the results. They live in the private ccfleet config
(`$CCFLEET_CONFIG`) and the rulings file it names (`vars.RULINGS_FILE`). Read
both before step 1; quote the principal's words from there, never from memory.

## What healthy means here

A repo is healthy when all seven hold. The principal may narrow or extend the
list in the rulings file; that file wins.

1. **Pin current**: the atelier pin is origin/main's, and the floor copy is
   identical (`tools/pins.py` says `current` and `identical`).
2. **CI green at the pushed head**, read from the CI runs, never from a
   worker's account.
3. **Conformance**: every mandatory item and dated obligation in the doctrine
   delta since the repo's old pin is applied.
4. **Every owed review has a brief**: `/atelier:review plan`'s *owed, not
   yet briefed* list is empty. The plan is the one finder of owed reviews and
   holds the definition of *owed* ([`../review/plan.md`](../review/plan.md),
   step 1); nothing here restates it.
5. **The principal's queue holds no duplicates**: open decisions, questions,
   rulings and actions waiting on the principal, de-duplicated within and
   across repos, answered ones marked with the citation.
6. **No record store kept as one growing file, and none missing**: session
   log → the folder `docs/sessions/` alone, one file per session, the folder
   its own index (RECORD.md § *The session log*); board → per-item files
   plus the generated index, done items included. A repo with **no board at
   all** fails this item too: it gets the empty store (`docs/roadmap/` with
   its `README.md`, and the generated index). A repo still keeping a session
   index (`docs/SESSIONS.md`, with any `SESSIONS-ARCHIVE.md`) fails it: atelier's
   `tools/archivecut.py --cut` retires it into the folder with its proof, and
   the worker then rewords the repo's own onramp and docs that tell a session
   to read or append to it (a `docs/sessions/README.md` the repo already kept
   is left above the tool's part, so its words need that reading too). A
   frozen `ROADMAP-DONE.md` is cut into the store by the same tool, entry by
   entry. Any other one-file list of entries → one file
   per entry with an index. **Exempt:** `CHANGELOG.md`, a release log in a
   standard format that outside readers expect and no session reads at
   start; and reference documents, which are not entry lists.
7. **Nothing left behind** by past sessions. Per repo: no stale open pull
   requests or branches, no leftover worktrees, stashes or untracked files, no
   claim held by a session that is no longer live. Per machine: no orphaned
   session or tool processes, no dead worktree or temporary directories, no
   temporary configuration a session added and forgot (a scheduled job, a
   permission or firewall rule, a service override). Act on what is provably
   this sweep's own or provably stale: merged into the mainline, its owner not
   live (`cclive`), nothing holding it open (`lsof`), and for a worktree a
   clean tree (`git status --porcelain` empty) and no held claim naming it (a
   board claim, or a review queue's claim on a pass cut off and kept for
   resume). A worktree is removed without `--force`, so git itself refuses a
   dirty one. Everything else goes to the principal as a list with its
   evidence. Never delete work you cannot prove is spent; a removal is
   reported with its proof.

## The billing rule (why the shape is what it is)

Per-repo cost tools label usage by the session's working-directory basename.
An `Agent` subagent runs in its parent's directory, so it bills the
orchestrator's repo. **Repo work never runs as an Agent of the orchestrator.**
Each repo's worker is a `claude -p --model <tier>` session that ccfleet starts
inside a worktree whose basename is the repo. The orchestrator's own repo is
done inline. A read that belongs to atelier (the doctrine digest, step 2) runs
as a headless session in atelier, not as an Agent.

## Steps

1. **Survey** (inline, cheap): `cclive`; `tools/pins.py --atelier <atelier>`
   (pin and floor copy per child); `tools/floorfleet.py`; per repo
   `gh run list -L 3`; per repo, whether the hook plane carries
   `.githooks/commit-msg` (a repo without it skips commit-message checks
   silently; the fix is a copy of `tools/commit-msg.sample`); and the form of
   each record store (healthy item 6); and the machine's leftovers (healthy
   item 7: `cclive`, `ps` for orphaned session and tool processes, the
   worktree and temporary directories, temporary configuration). The
   orchestrator's own repo counts too.
   **In scope: the repos the config lists**, and no others; a repo found on
   disk or on the forge that the config does not list is reported to the
   principal, never touched. Exempt even when listed, and left as they are:
   an archived repo, a fork, and a repo whose owner is not in the profile's
   `remote.account` (`/atelier:repo create`'s own check: another owner's repo is not
   yours to standardise). Read all three from the forge (`gh repo view
   <owner>/<name> --json isArchived,isFork,owner`); a repo whose owner cannot
   be read (no remote) is listed for the principal, not adopted. A listed,
   unexempt repo with no atelier pin is adopted in step 4 with
   [`adopt-prompt.md`](adopt-prompt.md), not put to the principal as a
   question: listing it in the config is what puts it in scope.
2. **Digest**, if none exists for origin/main's short SHA: one headless Opus
   session in atelier reads `git diff <oldest pin> origin/main -- docs/method
   docs/build/templates` in full and writes the child obligations: mandatory on
   bump, dated gates, advisory, self-check commands, and greps for restatements
   the delta makes stale.
3. **Own repo inline**: bump the orchestrator's repo yourself (read its delta
   in full, re-copy the floor, record the bump in its own convention).
4. **Write the jobs file** (`repo<TAB>label<TAB>prompt<TAB>KEY=VALUE...`):
   red CI and the nearest dated gates first. **Every label is unique in the
   file**: a label names one job's result (`results/<date>/<label>.md`), not
   the batch, and ccfleet refuses a jobs file whose labels repeat before
   anything starts. Use the repo's name, or the repo and the task. Tier per `ECONOMICS.md`, the
   cheapest that does the seat well: a cheaper tier where `pins.py` and CI
   would catch a worker's mistake; Opus where a mistake is silent or cannot be
   recalled (public repos, a client's repo, anything near secrets). The
   repo's notes in the config carry every fact a worker would otherwise
   fetch, and every ruling it must not cross. The worker prompt is
   [`worker-prompt.md`](worker-prompt.md); a repo being adopted uses
   [`adopt-prompt.md`](adopt-prompt.md) (its pin cannot be read yet, so the
   worker prompt's bump does not apply); a one-off task in a repo uses
   [`task-prompt.md`](task-prompt.md) with `TASK=@file:<path>`. The variables
   each prompt needs are in § *The variables the prompts need*.
5. **Run**: `ccfleet --by <session-id> drive <jobs> --max 5` with
   `run_in_background`. The gate holds each start until load, free memory and
   free disk have headroom, with a stagger between starts. `touch
   <kit_dir>/stop` ends launching. **One driver per `kit_dir`**: a second
   `drive` or `drain` on the same `kit_dir` is refused while one runs; give a
   second, separate sweep its own `kit_dir`. One drive writes every result
   under one day's folder, the day it started (UTC). A re-run skips a job
   only when its result there is a clean end; a job cut off (a nonzero exit,
   an error, no RESULT line, a time limit) keeps its worktree and its work,
   and runs again. A re-run after UTC midnight of a drive begun the day
   before passes `--day <that day>`, or every job runs again. A job whose
   worktree holds uncommitted work is never force-removed: the re-run or the
   principal's list takes it.
6. **Read results** (`<kit_dir>/results/<day>/*.md`, the drive's one day
   folder, each under 40 lines; read those, not the JSON logs; a kept
   worktree is named on its job's `KEPT` line in `logs/run-<label>.out`). Verify every claim that matters: `pins.py`
   for the fleet, `gh run list` at each pushed head. A worker's "green" is not
   evidence; CI is.
   - **6a. Briefs owed** (item 4): run `/atelier:review plan` and take its
     *owed, not yet briefed* list as the worklist; one headless Opus
     brief-writer per brief ([`brief-prompt.md`](brief-prompt.md)), one writer
     at a time per repo (`drive --serial-per-repo`). Put the plan's
     definition of *owed* in every writer's prompt. The writer saves the brief's held-back sibling
     straight to `HELD_DIR`, never in the tree (`/atelier:review run`,
     § *Briefs are never left owed*). Never brief work this session built.
   - **6b. Asks de-duplicated** (item 5), in three phases and a check. Per
     repo, a cheap headless session extracts every open item waiting on the
     principal to `<scratch>/<repo>/asks.tsv` (id, kind, 12-word gist, date,
     the words that make it the principal's). Once, an Opus session in the
     estate root finds duplicates within and across repos, items answered
     elsewhere (it searches the other repos' records for the answer) and
     items overtaken by events. Per repo again, only mechanical fixes are
     applied: cross-link duplicates to one home, mark answered with the
     citation. Merging or closing on a judgement goes to the principal as one
     list. Never delete a record; supersede it.
     **The check (phase 2b), before any bulk ask**: an Opus session reads
     every judgement row in its source context (the item, its thread, the
     record it cites), not the 12-word gist. It splits the rows by what
     "approve" would do, and a row that is really a question is asked as a
     question: it is never offered for approval. A gist alone once put rows
     in front of the principal that could not be approved with confidence.
   - **6c. Leftovers** (item 7): the machine's leftovers from step 1, acted
     on or listed by the same rule as the workers'.
7. **Report to the principal**, outcome first: a table per repo (pin, CI,
   conformance, leftovers cleared and listed, reviews pending, briefs written
   and still to write, 🎯 decisions owed, actions owed, open work with an
   hours estimate), then the asks: the account as text, then the question
   device in the same turn (`COMMUNICATION.md`). Before asking anything,
   search every repo's records (board items, session logs, decision records,
   review files) for the principal's earlier answer to the same question; one
   found is cited and marked answered, never asked again. Give each ask its
   evidence up front: what it is, where it came from, what each answer does.
8. **Close**: the orchestrator's session record names every worker session id
   and commit; no job worktree is left behind unaccounted: a kept one (a job
   cut off, uncommitted work) is taken by a re-run or listed for the
   principal with its evidence.

## The variables the prompts need

ccfleet fills `{REPO}` `{GH}` `{BR}` `{VIS}` `{WT}` `{PRIMARY}` `{LANDING}`
`{NOTES}` `{SCRATCH}` `{BY}` `{DATE}` `{SESSION}` on every launch, and `{PIN}`
when a prompt uses it. The rest are the adopter's, in the config's `vars` or
as a job's `KEY=VALUE`. ccfleet refuses to launch a prompt with a placeholder
left unfilled, so a missing one fails closed; `ccfleet check --prompt <file>`
names any first, and this list says which to set.

| Prompt | The adopter sets |
|---|---|
| [`worker-prompt.md`](worker-prompt.md) | `ASK` (the principal's request, verbatim); `ATELIER` (the atelier checkout); `REVIEW_APPROVAL` (what review-tier work is approved, usually none); `DIGEST` (the step-2 digest's path) |
| [`adopt-prompt.md`](adopt-prompt.md) | `ASK`; `ATELIER`; `REVIEW_APPROVAL` |
| [`task-prompt.md`](task-prompt.md) | `ASK`; `REVIEW_APPROVAL`; `TASK` (`@file:<path>`) |
| [`brief-prompt.md`](brief-prompt.md) | `ASK`; `ATELIER`; `HELD_DIR` (held siblings: outside the repo, every worktree and any scratchpad); per job `ITEM`, `SUBJECT`, `SOURCE`, `QUOTE`, `NOTE` |

## Limits paid for

- A public repo's prompt never names a private repo. ccfleet refuses to launch
  one that contains a configured private name; the list is only as good as its
  curation, so the worker prompt says it too.
- Workers never run review-tier work or cold passes, never write to live
  systems, never touch secrets, history, visibility, Actions switches, or
  bulk-remove from a record store. Each is a stop-and-report.
- The workers run unattended in every listed repo, hold the user's git and
  forge credentials, and read text others can write (a repo's instruction
  file, a pull request, a CI log). Give them the narrowest permission mode
  that does the work, never a bypass mode by default; `ccfleet --doc` says
  who can steer such a session and what bounds it.
- `claude -p` needs stdin from `/dev/null`; ccfleet always does it.
- Three prompts work in the atelier checkout, outside the worker's own
  worktree: `adopt-prompt.md` reads the `repo create` action there and runs
  its tools, `brief-prompt.md` reads the `review brief` action, and
  `worker-prompt.md` runs its git, `archivecut.py` and `pins.py`. Those
  texts are long and move with the doctrine, so they are read where they
  live, not copied into the prompts. The config is the whole grant
  (`ccfleet --doc`), so it must allow reading the atelier checkout (a `Read`
  rule on its absolute path, written with a leading `//`, for example
  `Read(//path/to/atelier/**)`) and the commands those steps run. Without
  it the session is refused at that step, and each prompt tells its worker
  to stop there and report BLOCKED rather than work from memory.
- A split of a record store runs only when `cclive` shows the repo idle, and
  proves line preservation by script.
- The principal's words in a prompt are quoted, marked as an answer (💬) when
  they were a pick from options or a typed reply, and never called a ruling
  unless the principal said so.
