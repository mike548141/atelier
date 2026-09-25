# Cold pass — the staged-plane board check and its doctrine sweep

**Pass type:** code + doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/390-rule-4-cold-pass-queued-the-staged-plane-check.md`.
**Why it earns a review:** the board check is the hook's guard against a claim
commit that carries a stale or absorbed index; reading the wrong plane is
exactly the defect (BS1) it was funded to close, and the doctrine sweep is what
every claimer reads about it.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `4412be8` / `18c155f` (2026-09-20) — `board.py` checks the staged plane and
  rebuilds from it
- `b2a54f1` (2026-09-20) — the registry wiring at the hook, and the five interim
  doctrine surfaces swept

Delta paths:

- `tools/board.py` — the `--staged` / `--from-index` planes and the two
  `_*_sections` readers
- `tools/test_board.py` — the `StagedPlane` class
- `tools/README.md` § *board*
- `tools/floor.py` — the `board` Scanner's hook argv
- `docs/method/CONCURRENCY.md` §§ *On a split board* and *Claiming at a dirty
  primary checkout*
- `docs/roadmap/README.md` — the preamble
- `docs/decisions/2026-08-15-0610-board-store-per-item-files.md` — the
  2026-09-20 amendment

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

The plane question, driven not read: in a scratch clone with the hook installed,
construct a merge in progress, a partial `git add -p`, an intent-to-add file, a
renamed item file, a deleted item, and a sibling's unstaged state-line edit
beside your staged claim, and record what `--check --staged` says for each
against what the worktree check says. Whether `board.py` importing `harvestscan`
at module scope works for a child resolving tools through `$ATELIER_TOOLS`
(drive it from a scratch child). Whether the hook argv the registry passes is
the one the tool expects, on both planes. Whether the swept surfaces now agree
with each other and with the code. **Non-goal:** the BS1 ruling that funded the
work.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   check presumes "the index on both sides" is the hook's right question — find
   the state where it is the wrong one, or show there is none. Ask whether a
   registry wiring that a previous run refused as unsafe on 2026-09-19 is safe
   now, from the code, not the comment.
2. **Correctness & quality.** Read all of `board.py` and the `board` entry in
   `floor.py`. Run `--selftest`, `tools.test_board`, the full suite. Drive every
   state in *Scope*. Check `--from-index` rebuilds are byte-identical to
   worktree rebuilds on a clean tree.
3. **Completeness / harvest.** The interim surfaces the sweep claims to have
   covered: list every surface that described the hook's guarantee before
   2026-09-20 (`160/260`'s five, plus any others) and check each at HEAD. Does
   `CHANGELOG.md` carry it?
4. **Security & privacy** — mandatory. The tool reads the git index via
   subprocess; check its argument handling against a path with spaces or a
   leading `-`, and that a rebuild from the index can never write a sibling's
   *staged but private* text into the generated file. The house scanner is
   discharged by grounds (landed delta; pending = other passes' drafts) — say
   so, and deliver the code-altitude read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/board.py --selftest`; `python3 -m unittest tools.test_board
  tools.test_floor tools.test_precommit`; the full Python suite once
- the floor on both planes at HEAD, and the hook driven live in a scratch clone
  through every state in *Scope*
- `--from-index` vs worktree rebuild byte comparison

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/390-rule-4-cold-pass-queued-the-staged-plane-check.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` (⚠️ head and tail
  read by the brief-writer; the `010/020` section not opened)
- the verdict `docs/reviews/2026-08-17-1321-bs1-wording-cold.md` (BW — where
  BS1's fund was ruled)
- the board items `docs/roadmap/010-*/020-*.md`, `docs/roadmap/115-*/080-*.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/390-rule-4-cold-pass-queued-the-staged-plane-check.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `SG`: `SG1`, `SG2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.
