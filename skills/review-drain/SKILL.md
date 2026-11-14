---
name: review-drain
description: Run briefed cold review passes across an estate on the principal-named review tier, several at once under a load gate, back to back, until an approved budget is used up — each pass billed to its own repo; or, in resume mode, finish only the passes a usage limit cut off. Use when the principal approves review-tier work to "use up the budget" or "drain the reviews", or says "resume" after a budget reset.
---

# Review drain

The runner is `instruments/ccfleet drain` (`ccfleet --doc` for its full
reference). The review queue itself, the principal's approvals and holds, the
priority order and the results are the adopter's own and stay out of any
public repo: they live in the private ccfleet config (`$CCFLEET_CONFIG`: its
`queue` commands, `reset_utc`, `vars`) and the rulings file it names
(`vars.RULINGS_FILE`). Read both before starting; quote the principal's
approval from there, never from memory.

## The shape

- **The review tier is gated.** No review-tier work, reviews included,
  without the principal's explicit approval. A drain *is* that approval, for
  the budget it names only. Record it, in the principal's words, dated, with
  the reset time, before the first pass.
- **Reviews run only on the review tier.** Everything that is not review work
  (orchestration, folds, records) runs on the cheapest capable model. Review
  work never moves to a lesser model: without approval it waits.
- **After the budget resets, nothing new starts.** On the principal's word,
  finish only what was started and cut off (Mode 2), then stop.

## The four rules

1. **Never block the queue on a question.** During a drain, no
   `AskUserQuestion`, and no turn ends on one. Take the recommended default,
   put the question on the board item and in the closing report, and keep
   going. A pass that cannot be done without the principal's input is skipped,
   with the question on its item. (Grounded: a first drain put one question in
   the device while the principal slept, and the queue sat idle for seven
   hours.)
2. **Back to back.** The moment a pass lands, its claim is released and the
   next one starts. No report between passes.
3. **Never stop, hold or reorder another session's review work.** If a peer
   says the principal told it to run something, that order stands over this
   skill and this session. Report a conflict; never act on it. The queue's
   claims only stop two sessions running the same pass.
4. **Survive the session.** Run the orchestrating session under `/loop`
   (dynamic pacing) so a session limit or a reboot does not end the drain;
   before any wait, schedule a long fallback wake-up. The driver's exit wakes
   the session anyway.

## Briefs are never left owed

Writing a brief is not review work, so a review that "needs a brief" is a
defect to fix on Opus between drains (the fleet-sweep skill's
`brief-prompt.md`), not a state to report. Only owed reviews get a brief: the
item's own text, or the principal's words on it, says a review is required.
Every brief has a `.deferred.md` sibling (the queue finds a brief by it).
Never brief a pass whose subject this session built.

## Mode 1: drain

1. **Set the config for this drain**: `reset_utc` (no new start at or after
   it), `vars.APPROVAL` (the principal's words), `vars.HOLDS` (passes held
   out, in the principal's words, or "none"), `vars.PROVENANCE` (what this
   session did and did not do: which briefs it wrote, which writers it
   started), `pass_prompt` → [`orchestrator-prompt.md`](orchestrator-prompt.md),
   `pass_model` (the orchestrator's model; the reviewer's tier is the
   prompt's). Start a fresh launched list (ccfleet keeps one per day).
2. **Tell the live sessions once** (`ListAgents`, then `SendMessage`): quote
   the approval, and ask each to claim a pass through the queue before running
   it. No other instruction; never ask a session to wait for this one.
3. **Run**: `ccfleet --by <session-id> drain --max N` with
   `run_in_background`. Each pass gets a worktree whose basename is its repo,
   the queue claim, and a headless orchestrator that spawns the one reviewer
   as its subagent (so both bill the repo), holds the context partition, and
   folds and lands the result. The driver starts one pass per stagger only
   while load, memory and disk have headroom, and stops on: the queue empty,
   the reset, the stop file, a pass reporting `BUDGET EXHAUSTED`, or three
   unclean ends in a row (which is how a spent weekly limit looks from
   outside).
4. **Read each result** (`<kit_dir>/results/<date>/*.md`). A pass that ended
   DONE or SKIPPED has released its claim and lost its worktree; any other end
   keeps both, for Mode 2.

### Lessons paid for

- `claude -p` needs stdin from `/dev/null`, or a warning corrupts the JSON log.
- A public repo's prompt says "drain session <id>", never a name that carries
  a private repo's name; ccfleet's private-name guard backs this.
- An orchestrator once invented provenance; the prompt now states who did
  what (`vars.PROVENANCE`) and says never to claim otherwise.
- Read-only reads of live systems are allowed as a review needs them; live
  writes never. A pass whose core needs a live write is skipped as `NEEDS
  LIVE WRITE` and ranked last; a single such check is marked NOT RUN.
- Several passes at once on a 16 GB machine is safe only with the gate and
  with every test run niced and single-process; say so in the reviewer prompt.
- Several briefs can share one board item, and the claim is per item: the
  queue's `next` must skip an item already claimed, or the slot is wasted.
- When the limit hits, a pass whose act 2 is already written needs only a
  fold, which is not review work ([`fold-prompt.md`](fold-prompt.md), run by
  `ccfleet run --in <the pass's worktree>` on a cheaper tier).
- A sandboxed API route (no network, no `gh`, temp-only writes) cannot match a
  local pass whose brief leans on those; triage briefs before sending them
  there, and a degraded pass gets a full local re-run, put to the principal.

## Mode 2: resume (after the reset, on the principal's word only)

For each pass still claimed: read its reviewer's transcript first. Un-claim one
whose reviewer did almost nothing (restarting it is new work). Resume the rest
with `ccfleet resume REPO WORKTREE SESSION --prompt resume-prompt.md --item
ITEM --set AGENT=<reviewer id> --set STATE='<where it stopped>'` ([`resume-prompt.md`](resume-prompt.md)):
the orchestrator continues its own reviewer, folds, lands and reports. If the
reviewer cannot be reached, the pass reports FAILED; it is never handed to a
replacement reviewer or a lesser model. Nothing new starts. No claims: nothing
to resume; say so.

## The reviewer prompt (the orchestrator fills it in)

- **Who it is**: the item, the worktree (absolute paths, `git -C`, never
  `cd`), the brief path; read the brief in full first and follow it, with
  REVIEW.md for the verdict shape.
- **Provenance**: the review tier, checked at selection; spawned by the
  per-pass orchestrator (named by session id), which holds the partition,
  forms no finding and writes no severity; the barred sessions it was not
  started or instructed by; the approval it runs under.
- **The partition**: the sibling was removed on purpose; never look for it in
  git history, other checkouts, scratchpads or temp directories.
- **What it may write**: only the brief file — act 1 below a `---` divider, an
  updated Status line, the file's own column width, absolute dates.
- **What it must not do**: commit or push; leave live captures in scratch; open
  GUI apps; print a secret; write to a live system.
- **Public repos**: refer to orchestrators by session id only; never a
  private repo's name or path, or an estate fact.
- **How to finish**: verdict, tally, path, "ACT 1 SAVED"; act 2 ends "ACT 2
  SAVED".

## Close

1. A session record in each repo touched; public repos stay public-safe.
2. The estate root's session record names every pass, session id and commit.
3. Remove the drain's one-off entries from the config (`vars.HOLDS`, extras).
4. Report per repo, outcome first: the verdicts; the principal's rulings owed,
   MAJORs first; what is left ready; when the budget ran out, or that it
   did not, said plainly.
