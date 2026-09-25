# Cold pass — the 2026-09-19 tier ruling — orchestration is no longer reserved for the top model, and the run-open stop is gone

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/330-rule-4-cold-pass-queued-the-tier-ruling.md`.
**Why it earns a review:** this rewording decides which model takes every seat
in every orchestrated run in the fleet, and removes a stop that used to halt
runs; if it leaves a route by which a session still asks the principal for a
tier, or removes a stop that was load-bearing, every future run inherits it.

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

- `c38b7da` (2026-09-20) — the landing commit

Delta paths:

- `docs/method/ECONOMICS.md` — the ruling paragraph in § *Match the model to the
  job*; the capable-seat definition and the role-check sentence in § *The
  orchestrated-run tier split*
- `docs/method/CONCURRENCY.md` § *Orchestrated queue runs* — the
  orchestrator/worker seat sentence, and *Tier at open — state it, don't ask*
  (formerly *Role check at open*)
- `skills/queue-run/SKILL.md` step 1
- `docs/method/session-open/session-open-prompt.md` — the anchor paragraph
- `docs/method/AUTONOMY.md` — the first-of-kind bullet
- `docs/method/REVIEW.md` — the reviewer-capability parenthesis
- `docs/method/README.md` — the `REVIEW.md` line

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Every surface that once said, or implied, that the most capable available model
takes the orchestrator seat, or that a session asks the principal which tier to
use — sweep for the old grammar at HEAD (`coldsweep` with the phrases the delta
removed, lifted from the diff), and say whether any survives. Whether the two
surviving stops are stated where a session meets them (at open; at `⏳`
selection) and read as stops rather than advice. Whether the rewording keeps
REVIEW.md rule 4's tier bar *for cold passes* intact and unambiguous — this
batch is itself running under that bar, and the reviewer may treat its own
session as a test case. **Non-goal:** the ruling — only its wording.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   ruling rests on "the cheapest model that can do a good job" being a judgement
   a session can make about *itself* at open — attack whether the wording gives
   a model any test for "good job" beyond its own confidence, and whether
   removing the run-open stop removed the only external check on that judgement.
2. **Correctness & quality.** Diff `c38b7da`. Check every cross-reference
   between the seven surfaces resolves and that they agree; check the renamed
   heading is not still linked by its old name anywhere.
3. **Completeness / harvest.** Search `skills/`, `docs/build/`, `CLAUDE.md`, the
   templates, and the session-open material for any surviving instance of the
   old rule or the old ranking language.
4. **Security & privacy** — mandatory. Doctrine prose; no code surface. The
   residual risk is a smaller model taking an irreversible seat under the new
   wording — check whether AUTONOMY's always-confirm floor still binds
   regardless of tier, and say so. Discharge the house scanner by grounds in one
   line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `coldsweep` at HEAD for the removed phrases (lift them from the diff), with
  `--also-exclude` on this brief and the board item
- `linkscan`, `pathscan`, `spellscan`, `wrapscan` over `docs/method` at HEAD;
  the floor on both planes

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
`docs/roadmap/160-doctrine-review-owed/330-rule-4-cold-pass-queued-the-tier-ruling.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`
- the board item `docs/roadmap/320-*/320-*.md` (the hand-up that carried the
  ruling ask) and any `docs/roadmap/*/…tier-question-back-to-the-principal.md`
  item

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/330-rule-4-cold-pass-queued-the-tier-ruling.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `TR`: `TR1`, `TR2`, …) and severities (MAJOR / MODERATE
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
