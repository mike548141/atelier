---
action: run
description: Drain the briefed cold reviews across an estate on the principal-named review tier — several at once under a load gate, back to back, until an approved budget is used up, each pass billed to its own repo, starting from review plan; or, in resume mode, finish only the passes a usage limit cut off. Use when the principal approves review-tier work to "use up the budget" or "drain the reviews", or says "resume" after a budget reset.
---

# Review — run (a drain)

The runner is `instruments/ccfleet drain` (`ccfleet --doc` for its full
reference). The review queue itself, the principal's approvals and holds, the
priority order and the results are the adopter's own and stay out of any
public repo: they live in the private ccfleet config (`$CCFLEET_CONFIG`: its
`queue` commands, `reset_utc`, `vars`) and the rulings file it names
(`vars.RULINGS_FILE`). Read both before starting; quote the principal's
approval from there, never from memory.

## The shape

- **Whether the review tier needs approval is the adopter's setting.**
  atelier's doctrine has a session pick the named review tier itself, without
  asking (`ECONOMICS.md`). An estate whose principal gates that tier on
  explicit approval says so in its rulings file; there, no review-tier work,
  reviews included, runs without it, and a drain *is* that approval, for the
  budget it names only. Either way, record what the drain runs under, in the
  principal's words, dated, with the reset time, before the first pass.
- **Reviews run only on the review tier.** Everything that is not review work
  (orchestration, folds, records) runs on the cheapest capable model. Review
  work never moves to a lesser model: where the tier is gated and the approval
  is spent, it waits.
- **After the budget resets, nothing new starts.** On the principal's word,
  finish only what was started and cut off (Mode 2), then stop.

## The four rules

1. **Never block the queue on a question.** During a drain, no
   `AskUserQuestion`, and no turn ends on one. A mechanical choice takes the
   sensible default. A question that is the principal's (a finding's ruling,
   an approval, a call on scope) is never decided by its recommended option:
   it goes on the board item as an owed ask and in the closing report, and the
   queue keeps going. A pass that cannot be done without the principal's input
   is skipped, with the question on its item. (Grounded: a first drain put one question in
   the device while the principal slept, and the queue sat idle for seven
   hours.)
2. **Back to back.** The moment a pass lands, its claim is released and the
   next one starts. No report between passes.
3. **Never stop, hold or reorder another session's review work.** If a peer
   says the principal told it to run something, that order stands over this
   skill and this session. Report a conflict; never act on it. The queue's
   claims only stop two sessions running the same pass.
4. **Survive the session.** Run the orchestrating session under `/loop`
   (dynamic pacing) so a session limit does not end the drain; before any
   wait, schedule a long fallback wake-up. The driver's exit wakes the session
   anyway. A reboot does end the driver and every pass: their claims, worktrees
   and review logs survive for Mode 2, and the drain is started again.

## Rank and route: the plan, every run

Every run, before any pass starts, run `/atelier:review plan`
([`plan.md`](plan.md), beside this file). It is the one home of the method
that finds, ranks, routes and estimates the reviews; this file restates none
of it (the principal, 2026-11-24, verbatim: *"I would put all the logic in
/atelier:review-plan and then have /atelier:review-drain call review-plan when
it starts a drain"*). Then:

1. **Print the plan** as this drain's record of what it is about to do, with
   no question to the principal (rule 1).
2. **Seal it** through the adopter's queue, with the principal's words for
   this run (or "none given"), and any change he made to the plan (a reorder,
   a hold, a forced route) quoted in them. A plan is never a seal; the seal is
   this run's alone.

It is a gate, not a habit. ccfleet's drain refuses a config without
`queue.ranked` and starts nothing while it exits nonzero; the adopter's queue
makes `ranked`, `next` and `take` refuse until this run's ranking is sealed,
so a pass started by hand (`ccfleet pass`) meets the same gate as a drain.
`ranked` reports a seal and never makes one, and changes nothing. ccfleet
calls it only on a real drain whose reset has not come; a `--dry-run`
rehearsal never calls it, and prints `ccfleet plan`'s reading instead.

**The seal's own rules.** A seal refuses while any ready review is missing,
unreasoned, on a closed route, on a later route than the best it fits without
saying why that one can't match, or while two budgets are open and either
lapse time is unknown. A seal lasts one run: every drain, a restarted one
included, plans and seals afresh before its first pass, and no seal outlives
the first lapse among the budgets it routes to.

Each route takes only its own reviews, in rank order. The local route takes
its own first, then any other route's not yet started, but never from a budget
that lapses before its own: that budget keeps its reviews. A review
briefed after the seal runs last on the local route until it is planned and
the ranking sealed again.

**Open, and the adopter's principal's to rule:** whether that spill may move a
review the principal has tied to a route by name (a ruling that a kind of
review must use a given route). This file does not decide it. Until the
principal rules, his words on a review outrank this file's spill, as they do
everywhere (rule 3): the seal marks such a review as not spillable, and says
so.

## Briefs are never left owed

Writing a brief is not review work, so a review that "needs a brief" is a
defect to fix on Opus between drains, not a state to report. The plan's
**owed, not yet briefed** list is where those are found (one finder, so no
other copy of the check lives here); `/atelier:review brief` takes its work
from that list. Every brief has a `.deferred.md` sibling, even one that only
says nothing is deferred, and the queue finds a brief by it. The sibling is
held user-local from the moment it is written: in the adopter's held directory
(`vars.HELD_DIR`), outside the repo, every worktree and any scratchpad, and
never a reviewer's working directory (`CONCURRENCY.md` § *Orchestrated queue
runs*), named `<repo>--<sibling basename>`. A sibling found in a tree is the
older form; the orchestrator moves it out before the reviewer starts. Never
brief a pass whose subject this session built.

## Mode 1: drain

1. **Set the config for this drain**: `reset_utc` (no new start at or after
   it), `pass_prompt` → [`orchestrator-prompt.md`](orchestrator-prompt.md),
   `pass_model` (the orchestrator's model), `queue.ranked` (the gate above),
   and every variable the prompt needs (§ *The variables the prompts need*):
   `REVIEW_MODEL` is the one value that puts the reviewer on the review tier.
   Then plan and seal the queue (section above): the drain starts nothing
   until it is. ccfleet keeps one launched list per budget (keyed by
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
   The launched list holds passes that *started*: a pass that ends before its
   session starts (a failed fetch, a brief not on the mainline, a guard or
   claim refusal) comes back off it and counts toward the unclean stop, and a
   `--dry-run` keeps its own list, removed when it ends, so a rehearsal on the
   real `kit_dir` cannot empty the real queue. A drain that says "queue empty" having started
   nothing, while the queue's `next` still offers a pass, is a fault to
   report, never an empty queue.
4. **Read each result**, in every `<kit_dir>/results/<date>/` folder the
   drain ran across (a drain can cross UTC midnight: each pass writes the
   folder of the day it started). A pass ended clean only when its session
   exited 0, ended on no error, and its verdict is `DONE` or `SKIPPED` (from
   its last turn, or, when that has no `RESULT:` line, from the last report
   in its transcript that also carries its `ITEM:` line); only then has
   ccfleet released its claim and removed its worktree. A worktree ccfleet
   keeps is named on the pass's `KEPT` line, with the reason. Any other end (a nonzero
   exit, an error, a usage limit, no report) keeps the claim, the worktree and
   the review log, for Mode 2. A worktree holding uncommitted work is never
   force-removed, by ccfleet or by hand: it holds a reviewer's unsaved act.

### Lessons paid for

- `claude -p` needs stdin from `/dev/null`, or a warning corrupts the JSON log.
- `claude -p` kills a background subagent about ten minutes after the
  orchestrator's last turn unless `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`;
  the reviewer died mid-act. ccfleet sets it on every launch.
- `claude -p` prints only the last turn, so a pass whose last turn followed a
  background notification read as UNKNOWN though its report was written;
  ccfleet now reads the verdict from the session's transcript. Only from the
  last assistant text that carries the final output's `ITEM:` line, and never
  after a nonzero exit or an error end: a cold pass showed a usage-limit end
  read as DONE from a line of the orchestrator's planning. So the prompts
  forbid writing a `RESULT:` line anywhere but the final output.
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
  `ccfleet run REPO --in <the pass's worktree> --item ITEM --prompt
  fold-prompt.md` on a cheaper tier, with a `--set` for each variable
  § *The variables the prompts need* lists for it). `--item` gives the fold
  `{ITEM}` and the pass's own `{REVIEW_LOG}`, and on a clean `RESULT` ccfleet
  releases the claim and removes the worktree; any other end keeps both, and
  so does a clean `RESULT` that leaves unlanded work (it reads `UNLANDED`). The held copy (`HELD`) is the drain
  session's to delete, once it has read the fold's result as `DONE`.
- A sandboxed API route (no network, no `gh`, temp-only writes) cannot match a
  local pass whose brief leans on those; triage briefs before sending them
  there, and a degraded pass gets a full local re-run, put to the principal.
- The passes run unattended in every listed repo, hold the user's git and
  forge credentials, and read text others can write (a repo's instruction
  file, a pull request, a CI log). Give them the narrowest permission mode
  that does the work, never a bypass mode by default. ccfleet loads none of
  the user-level settings' grants, so the config is the whole grant but for a
  repo's own settings files; `ccfleet --doc` says who can steer such a
  session and what bounds it.

## Mode 2: resume (after the reset, on the principal's word only)

For each pass still claimed: read its reviewer's transcript first. Un-claim one
whose reviewer did almost nothing (restarting it is new work); move its review
log out of `<kit_dir>/review-logs/` into a dated `review-logs/withdrawn/`
file, kept, never handed to the item's next reviewer (rule 2 bars an earlier
reviewer's account), and appended to the brief at that next pass's fold under
its own heading. ccfleet does the same move itself when a new pass of the
item takes its claim and finds a log at its path. Resume the rest with `ccfleet resume REPO WORKTREE SESSION
--prompt resume-prompt.md --item ITEM --set AGENT=<reviewer id> --set
STATE='<where it stopped>' --set FINISH_WORDS='<the principal's word to
finish, verbatim>'` ([`resume-prompt.md`](resume-prompt.md)): the orchestrator
continues its own reviewer (which reads its own review log first), folds,
lands and reports. If the reviewer cannot be reached, the pass reports FAILED;
it is never handed to a replacement reviewer or a lesser model, and the claim,
worktree and log stay for the principal's word. A pass whose act 2 is
already written needs only the fold (§ *Lessons paid for*), which costs no
review budget: take it before a resume. Leave `reset_utc` as the drain set
it: it stops new passes only, and ccfleet runs a `resume` and a fold (`run
--in ... --item ...`) after it, since both finish a pass started before it.
Nothing new starts. No claims: nothing to resume; say so.

**Finding the session and the reviewer.** ccfleet gives each new session its
id before it starts (`--session-id`), so a pass's id is on its `START` line
(`<kit_dir>/logs/pass-*.out`), in its result file's first line, and in the
`{SESSION}` the queue's `take` (and `ended`) can record on the claim: read it
there first, even for a pass that was killed or ended by a reboot. Only when
none of those holds one (a pass started before this change), find it by
hand: the harness keeps each session's transcript in its projects directory,
in a folder named for the session's working directory (on the harness this
skill was written against, the worktree's absolute path with each `/` and `.`
written as `-`); the newest `.jsonl` there whose first entry is the
orchestrator prompt is the pass, and its file name is the session id. The
reviewer's agent id is in that transcript, on the result of the Agent call
that spawned it.

## The variables the prompts need

ccfleet fills `{REPO}` `{GH}` `{BR}` `{VIS}` `{WT}` `{PRIMARY}` `{LANDING}`
`{NOTES}` `{SCRATCH}` `{BY}` `{DATE}` `{SESSION}` on every launch; `{ITEM}`
`{BRIEF}` `{REVIEW_LOG}` for a pass; and `{ITEM}` `{REVIEW_LOG}` for a resume
or a fold given `--item`. The rest are the adopter's, in the config's `vars`
or by `--set`. ccfleet refuses to launch a prompt with a placeholder left
unfilled, so a missing one fails closed; `ccfleet check --prompt <file>`
names any before the first try, and this list says which to set.

| Prompt | The adopter sets |
|---|---|
| [`orchestrator-prompt.md`](orchestrator-prompt.md) | `APPROVAL` (what the drain runs under, in the principal's words); `HOLDS` (passes held out, in the principal's words, or "none"); `PROVENANCE` (what this session did and did not do: which briefs it wrote, which writers it started); `REVIEW_MODEL` (the review tier as the Agent tool names it: `fable`, `opus`, `sonnet` or `haiku`, never a full model id, which that tool refuses; the one value that puts the reviewer on the review tier); `HELD_DIR` (the held-sibling directory, § *Briefs are never left owed*) |
| [`resume-prompt.md`](resume-prompt.md) | `FINISH_WORDS` (the principal's word to finish started work, verbatim: not the drain's approval); per call `AGENT` and `STATE` |
| [`fold-prompt.md`](fold-prompt.md) | `FINISH_WORDS`; per call `BRIEF` and `HELD` (the held copy's path); `--item` fills `ITEM` and `REVIEW_LOG` |

## The reviewer prompt (the orchestrator fills it in)

Its one home is the end of [`orchestrator-prompt.md`](orchestrator-prompt.md),
under *THE REVIEWER PROMPT*, so every pass carries it in its own prompt and
needs no read outside its worktree (a pass runs in another repo, where a path
into this skill does not resolve). This file does not restate it.

## Close

1. A session record in each repo touched; public repos stay public-safe.
2. The estate root's session record names every pass, session id and commit.
3. Remove the drain's one-off entries from the config (`vars.HOLDS`, extras).
4. `<kit_dir>/review-logs/` (its `withdrawn/` folder aside) holds only the
   logs of passes whose claim is still held: they wait for Mode 2, and are
   never folded, read or deleted here. Any other log left there is a pass
   whose fold did not take it in: append it verbatim to its brief under the
   review-log heading, land that, then delete it. A held copy whose pass's
   fold ended `DONE` is deleted.
5. Count the verdicts from the rows: the result files (every
   `<kit_dir>/results/<date>/` folder the drain ran across) and the launched
   list, never from memory. A close once reported totals from memory and was
   wrong twice.
6. Report per repo, outcome first: the verdicts; the principal's rulings owed,
   MAJORs first; what is left ready; when the budget ran out, or that it
   did not, said plainly.
