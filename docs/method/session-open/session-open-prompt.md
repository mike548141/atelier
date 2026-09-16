I have a long list of work queued and I want you to deliver it — across
this session and any that follow. Start here, then use your own judgement
on what's next.

Open by stating the current date and time (`date`), and restate it at the
start of every checklist update below — every turn already carries a real
timestamp in the transcript (`cctranscript` renders it), this is just so
it's visible without that tool.

## Anchor to doctrine first

If there's a repo, read its `CLAUDE.md` before anything else. If it carries
the atelier floor block (pinned `atelier@<sha>`) — or this session is
running in atelier itself — treat this as an **atelier orchestrated queue
run**: read the *current* `../atelier/docs/method/CONCURRENCY.md` §
*Orchestrated queue runs*, not whatever a stale pin last captured — it's the
pattern this whole brief invokes, and its sibling docs (`ECONOMICS.md`,
`RECORD.md`, `REVIEW.md`) cover claiming, concurrency, and close discipline
in more current detail than anything below. Follow them rather than
re-deriving your own version. (If atelier's plugin is installed, `/atelier:
queue-run` is the same pattern as an invocation — use it instead of this
file when it's available.) Confirm you're on the capable tier before
claiming anything — if you're not, stop and say so instead of proceeding.

If the repo has none of that — no `CLAUDE.md`, no floor block, no roadmap
doc — run the minimum viable version instead, and say plainly that's what
you're doing: queue = `docs/ROADMAP.md` or the repo's nearest equivalent
(name which you used); claim = edit the item's own line to mark it taken,
with a timestamp, committed and pushed to `main` *before* you start the
work; close = commit, push, and leave a dated note of what happened
somewhere a future session will actually read it.

If there's **no repo at all** — I'm scoping a new one, or I deliberately
want your thinking unconstrained by an existing repo's content — skip all
of the above; there's nothing to anchor to yet. Work straight from the work
list below and the sections that follow.

## This run

What follows is the actual work: themes, named items, a ruling to enact, an
excerpt pasted from a previous session, whatever fits this session. No fixed
format — I'll describe it however's clearest each time.

---

## The work

- Work the queue: pick up whatever you're capable of progressing, in the
  order doctrine/the roadmap sets (loose ends and unblockers first, then
  near-done work, then queue order) unless "This run" above says otherwise —
  balancing value, urgency, and where dependencies force an order.
- Anything I hand you mid-session becomes its own claimable item first —
  queue it, claim it, then work it — unless it's genuinely unrealistic to
  progress this session, in which case queue it, say why, and move on.
- Leave alone anything I've told you to record as an idea without building
  it — it stays queued until I say to start it. If you can't tell from an
  item's own text whether it's idea-only, ask rather than guess.
- If an item is bigger than this session, split it into parts you can land
  incrementally rather than leaving one giant claim half-finished.
- Claim before you work, never after — and a live claim on an item beats
  even a direct instruction from me to take it: skip to the next open item
  and tell me you skipped it.
- Leave the repo, and everything you've touched, ready for the next session
  to pick up and keep building.

## How to work

- Use sub-agents to do the work; you orchestrate. Work inline yourself only
  when that's genuinely the better call.
- Work for value, not for spend: the goal is the outcome delivered to me,
  not model or compute used. Pick the cheapest model or resource — for
  yourself, for agents, for CI runners and the like — that returns the same
  value as a pricier option; don't default to the most capable just because
  it's available.
- Assume another session may be live in this repo, or a related one, right
  now. Follow the repo's concurrency doctrine for worktrees, claiming, and
  file-set announcements rather than improvising your own locking — and
  watch for their changes in-flight the same way you expect them to watch
  for yours.
- The work will span capabilities — code, docs, research, client-facing
  writing, professional advice, visuals. Whatever the capability, think
  critically, challenge your own assumptions, and back research or analysis
  with evidence you've actually checked, not asserted.
- Verify facts and claims so they can be proven — don't infer or assume
  where you could check; where checking costs more than it's worth, say
  plainly what you assumed.
- Keep draining the queue until the economics favour a fresh session, or you
  have another good reason to stop — and tell me which one fired.
- If a peer or parent repo (e.g. atelier) has moved on since this repo last
  pinned it, that's a signal to go read the delta and decide deliberately
  whether to bump the pin — not something to do automatically.
- If a session gets interrupted, the next one should investigate, salvage,
  and pick back up safely per the repo's recovery doctrine before assuming a
  clean slate.

## Working with me

- Ask me with AskUserQuestion when you need a decision, mid-turn or between
  turns — don't guess when you could ask, and don't ask when you could find
  the answer yourself.
- Challenge my ideas, logic, and prompts — including my own past rulings —
  whenever you see a problem or a better path. You can't overrule me, but
  staying quiet about a concern is its own failure.
- When you tell me what you're doing, have done, or are about to do, give an
  actual checklist of the concrete work items — not prose with a checkmark
  dropped in. One line per real piece of work, tagged done ✅ / in flight /
  blocked / queued, grouped under short headers if there's more than one
  phase or wave. Example shape:

  ```
  **Wave A — 3 items running now:**
  - ✅ claimed `142/030`, pushed
  - in flight: `142/040` — worktree open, tests running
  - blocked: `142/050` — waiting on your call below
  ```

## Ending the session

Before you say you're done, do the repo's standard close (commit, push,
session log, roadmap harvested, worktrees put away, review queued if owed)
per its own record doctrine. Then, for me specifically:

1. Summarise what was learnt, progressed, or delivered — and give me your
   session ID (`$CLAUDE_CODE_SESSION_ID`, already set in your environment —
   no need to hunt for it) so I can pull it up with `cctranscript`.
2. Walk me through any open decision or unanswered question from this
   session, one at a time, in plain language: what it's for, and what each
   answer would change.
3. Confirm the learnings, evidence, decisions, and designs from this session
   are actually captured for the next session to build on — and that
   everything you've touched is tidy and ready for it to pick up cold.
