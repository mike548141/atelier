---
name: fleet-sweep
description: Bring every child repo of an atelier estate to a healthy state — latest atelier pin with the floor re-copied verbatim, CI green at the pushed head, conformance with the current doctrine, every owed review briefed, the principal's queue of asks de-duplicated, every one-file record store split — each repo's work run as a headless session inside that repo so per-repo cost tools bill the repo. Use when the principal asks for a health sweep, to "bring the repos up to healthy", to bump every pin, or for one repo by name.
---

# Fleet health sweep

The runner is `instruments/ccfleet` (`ccfleet --doc` for its full reference).
Everything that belongs to one principal's estate stays out of this skill and
out of any public repo: the repo list, per-repo notes and tiers, the
principal's own words, the results. They live in the private ccfleet config
(`$CCFLEET_CONFIG`) and the rulings file it names (`vars.RULINGS_FILE`). Read
both before step 1; quote the principal's words from there, never from memory.

## What healthy means here

A repo is healthy when all six hold. The principal may narrow or extend the
list in the rulings file; that file wins.

1. **Pin current**: the atelier pin is origin/main's, and the floor copy is
   identical (`tools/pins.py` says `current` and `identical`).
2. **CI green at the pushed head**, read from the CI runs, never from a
   worker's account.
3. **Conformance**: every mandatory item and dated obligation in the doctrine
   delta since the repo's old pin is applied.
4. **Every owed review has a brief.** *Owed* means the item's own text, or the
   principal's words on it, says a review is required. A bare `⏳`, REVIEW.md's
   triggers, or a writer's view that it deserves one do **not** count; those
   go to the principal as a list, never into a brief.
5. **The principal's queue holds no duplicates**: open decisions, questions,
   rulings and actions waiting on the principal, de-duplicated within and
   across repos, answered ones marked with the citation.
6. **No record store kept as one growing file**: session log → index plus one
   file per session (RECORD.md); board → per-item files plus the generated
   index, done items included; any other one-file list of entries → one file
   per entry with an index.

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
   each record store (healthy item 6). The orchestrator's own repo counts too.
   Archived repos are exempt. A repo with no pin and not archived is a scope
   question for the principal.
2. **Digest**, if none exists for origin/main's short SHA: one headless Opus
   session in atelier reads `git diff <oldest pin> origin/main -- docs/method
   docs/build/templates` in full and writes the child obligations: mandatory on
   bump, dated gates, advisory, self-check commands, and greps for restatements
   the delta makes stale.
3. **Own repo inline**: bump the orchestrator's repo yourself (read its delta
   in full, re-copy the floor, record the bump in its own convention).
4. **Write the jobs file** (`repo<TAB>label<TAB>prompt<TAB>KEY=VALUE...`):
   red CI and the nearest dated gates first. Tier per `ECONOMICS.md`, the
   cheapest that does the seat well: a cheaper tier where `pins.py` and CI
   would catch a worker's mistake; Opus where a mistake is silent or cannot be
   recalled (public repos, a client's repo, anything near secrets). The
   repo's notes in the config carry every fact a worker would otherwise
   fetch, and every ruling it must not cross. The worker prompt is
   [`worker-prompt.md`](worker-prompt.md); a one-off task in a repo uses
   [`task-prompt.md`](task-prompt.md) with `TASK=@file:<path>`.
5. **Run**: `ccfleet --by <session-id> drive <jobs> --max 5` with
   `run_in_background`. The gate holds each start until load, free memory and
   free disk have headroom, with a stagger between starts. `touch
   <kit_dir>/stop` ends launching. A re-run skips jobs with a result for today.
6. **Read results** (`<kit_dir>/results/<date>/*.md`, each under 40 lines;
   read those, not the JSON logs). Verify every claim that matters: `pins.py`
   for the fleet, `gh run list` at each pushed head. A worker's "green" is not
   evidence; CI is.
   - **6a. Briefs owed** (item 4): one headless Opus brief-writer per brief
     ([`brief-prompt.md`](brief-prompt.md)), one writer at a time per repo
     (`drive --serial-per-repo`). Put healthy item 4's definition of *owed* in
     every writer's prompt. Never brief work this session built.
   - **6b. Asks de-duplicated** (item 5), in three phases. Per repo, a cheap
     headless session extracts every open item waiting on the principal to
     `<scratch>/<repo>/asks.tsv` (id, kind, 12-word gist, date, the words
     that make it the principal's). Once, an Opus session in the estate root
     finds duplicates within and across repos, items answered elsewhere (it
     searches the other repos' records for the answer) and items overtaken
     by events. Per repo again, only mechanical fixes are applied:
     cross-link duplicates to one home, mark answered with the citation.
     Merging or closing on a judgement goes to the principal as one list.
     Never delete a record; supersede it.
7. **Report to the principal**, outcome first: a table per repo (pin, CI,
   conformance, reviews pending, briefs written and still to write, 🎯
   decisions owed, actions owed, open work with an hours estimate), then the
   asks: the account as text, then the question device in the same turn
   (`COMMUNICATION.md`).
8. **Close**: the orchestrator's session record names every worker session id
   and commit; no job worktree is left behind.

## Limits paid for

- A public repo's prompt never names a private repo. ccfleet refuses to launch
  one that contains a configured private name; the list is only as good as its
  curation, so the worker prompt says it too.
- Workers never run review-tier work or cold passes, never write to live
  systems, never touch secrets, history, visibility, Actions switches, or
  bulk-remove from a record store. Each is a stop-and-report.
- `claude -p` needs stdin from `/dev/null`; ccfleet always does it.
- A split of a record store runs only when `cclive` shows the repo idle, and
  proves line preservation by script.
- The principal's words in a prompt are quoted, marked as an answer (💬) when
  they were a pick from options or a typed reply, and never called a ruling
  unless the principal said so.
