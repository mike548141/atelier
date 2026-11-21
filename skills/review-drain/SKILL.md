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

## Rank and route the whole queue first

Every run, before any pass starts. The principal, 2026-11-20, verbatim:
*"when I run fable drain or its equivalent, and similar code/skills/whatever
that get fable reviews completed like using Agent SDK or Batch API it should
first look at all the reviews in all the repos to priortise the highest
priority ones based on either my direction or the reviews importance, urgency,
and the risks it mitigates or value of work it unlocks. Make sure that is
built into them so it happens everytime I run it"*. The same day the principal added that
each review goes to the cheapest route that still produces a review of the
same standard as a local pass: a batch route first where a review fits it,
then API credit, then the weekly budget, which a drain then uses up. The next
day the principal sharpened "cheapest": a budget or credit that is lost at a
set time is spent first when that time is near, since the aim is the most
benefit from the whole spend rather than the lowest cost of one job, and no
budget is free (a subscription pays for the included ones). So routing orders
the routes by when the budget each draws lapses, soonest first, and the cost
per review only breaks a tie.

It is a gate, not a habit. ccfleet's drain refuses a config without
`queue.ranked` and starts nothing while it exits nonzero; the adopter's queue
makes `ranked` (and `next`) refuse until this run's ranking is sealed. The
ranking and routing are the adopter's, kept private:

1. **Read every briefed, unrun review in every repo**, with what the judge
   needs: the item, its age, the principal's words on it, dates ahead, what it
   guards, what waits on its verdict, and what each route can and cannot do
   for it.
2. **Rank by judgement:** the principal's direction first (the words for this
   run, then standing words on an item); then importance, urgency (a real
   date first), the risk the review mitigates (credentials, public exposure,
   live or irreversible paths, money) and the value of the work it unlocks; a
   pass whose core needs a live write last; a standing repo order breaks ties
   only.
3. **Route each review to the route that reaches local quality and whose
   budget lapses soonest**, among the routes the principal has opened; the
   cost per review breaks a tie (two routes drawing one budget: the cheaper).
   Each budget's lapse time is known before the seal (a credit's expiry is
   read when the principal releases it). A review needing probes or
   re-run lines does not fit a single-request batch route; one needing tools
   only the local session has fits only local. Unsure means the dearer route:
   quality is never traded for price.
4. **Seal it**, with the principal's words for this run (or "none given").
   A seal refuses while any ready review is missing, unreasoned, on a closed
   route, on a later route than the best it fits without saying why that one
   can't match, or while two budgets are open and either lapse time is
   unknown. It lasts one budget.

Each route takes only its own reviews, in rank order. The local route takes
its own first, then any other route's not yet started, but never from a budget
that lapses before its own: that budget keeps its reviews. A review
briefed after the seal runs last on the local route until it is ranked and
the ranking sealed again.

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
   prompt's), `queue.ranked` (the gate above). Then rank, route and seal the
   queue (section above): the drain starts nothing until it is. ccfleet keeps one launched list per budget (keyed by
   `reset_utc`), and ignores a stop file older than the driver, saying so in
   its log.
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
   outside). The ceiling is live: to pace the drain against the budget, edit
   the number in `<kit_dir>/max` rather than stopping it.
4. **Read each result** (`<kit_dir>/results/<date>/*.md`). A pass that ended
   DONE or SKIPPED has released its claim and lost its worktree; any other end
   keeps both, for Mode 2.

### Lessons paid for

- `claude -p` needs stdin from `/dev/null`, or a warning corrupts the JSON log.
- `claude -p` kills a background subagent about ten minutes after the
  orchestrator's last turn unless `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`;
  the reviewer died mid-act. ccfleet sets it on every launch.
- `claude -p` prints only the last turn, so a pass whose last turn followed a
  background notification read as UNKNOWN though its report was written;
  ccfleet now reads the verdict from the session's transcript.
- Paths can hold spaces: every path in a prompt's shell commands is
  double-quoted, and a queue prints tab-separated fields.
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
  `ccfleet run --in <the pass's worktree>` on a cheaper tier, with `--set
  REVIEW_LOG=<the path the pass's prompt named>`).
- A sandboxed API route (no network, no `gh`, temp-only writes) cannot match a
  local pass whose brief leans on those; triage briefs before sending them
  there, and a degraded pass gets a full local re-run, put to the principal.

## Mode 2: resume (after the reset, on the principal's word only)

For each pass still claimed: read its reviewer's transcript first. Un-claim one
whose reviewer did almost nothing (restarting it is new work). Resume the rest
with `ccfleet resume REPO WORKTREE SESSION --prompt resume-prompt.md --item
ITEM --set AGENT=<reviewer id> --set STATE='<where it stopped>'` ([`resume-prompt.md`](resume-prompt.md)):
the orchestrator continues its own reviewer (which reads its own review log
first), folds, lands and reports. If the reviewer cannot be reached, the pass
reports FAILED; it is never handed to a replacement reviewer or a lesser
model. Nothing new starts. No claims: nothing to resume; say so.

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
- **The review log**: a review earns trust only if its method can be checked,
  so the reviewer keeps a running log at `{REVIEW_LOG}` (ccfleet sets one path
  per pass, outside the repo, so it survives a reboot): each check and its
  result, with the exact command or file and line; each candidate finding with
  its evidence and the criterion that decides it; each point checked and not
  raised. Enough for a third party to re-run the method and reach the same
  verdict. No secrets or live captures in it. Keep the wording to checks and
  evidence: a wider wording was refused by a model safeguard, and the
  orchestrators stopped at their first message.
- **Private while running, open once done**: until act 2 is saved, no other
  session reads, edits or comments on the log or steers the review, except on
  the principal's order or to stop harm. At the fold the orchestrator appends
  it verbatim to the review under *Review log (reviewer, verbatim; private
  while the pass ran, opened at the fold)* and deletes the file. A revived
  reviewer reads its own log first.
- **What it may write**: the review log, and otherwise only the brief file —
  act 1 below a `---` divider, an updated Status line, the file's own column
  width, absolute dates.
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
4. `<kit_dir>/review-logs/` is empty. A log left there is a pass whose fold
   did not take it in: append it verbatim to its brief under the review-log
   heading, land that, then delete it.
5. Count the verdicts from the rows: the result files
   (`<kit_dir>/results/<date>/*.md`) and the launched list, never from
   memory. A close once reported totals from memory and was wrong twice.
6. Report per repo, outcome first: the verdicts; the principal's rulings owed,
   MAJORs first; what is left ready; when the budget ran out, or that it
   did not, said plainly.
