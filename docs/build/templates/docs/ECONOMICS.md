# Model & token economics — working policy

The short version of the house policy this repo runs by.

## Who does what

Seats are **roles assigned by risk**; billing facts are **read off the current
plan at session open, never off this file** — a hard-coded model↔billing
mapping here went stale once already when the provider moved the plan
(atelier `docs/method/ECONOMICS.md`, billing states of the marginal token).
Which model fills each seat, and each one's billing state, are plan details
held person-local, not in this repo.

- **Workhorse seat** — building, iterating, docs, exploration: the cheapest
  model that genuinely does the items' builds, safe because the mechanical
  floor catches its failures.
- **Capable seat** — the orchestrator, reviewer and hard-problem solver. For
  reviews and hard problems keep it **scoped**: hand it a diff/file list; ask
  for *findings*, not rewrites; apply fixes back on the workhorse (see
  `reviews/README.md`). Orchestration is the long-running exception — it runs
  the parent's orchestrated-run tier split, not scoped-and-short. If this
  seat's model is capped on the current plan, at the cap the exits are
  stop/delay or the principal choosing to pay — **never down-tier the work to
  dodge the cap**: tier is the work's risk profile's call, not the tank's.
- **Fan-out seat** — sub-agent fan-out and mechanical bulk (searches, scans,
  pattern-following reads) whose result the parent or the mechanical floor
  verifies: the cheapest tier that genuinely does the read.
- **Sub-agents** — fan-out, parallel slices, fresh-context verification; they
  buy context *isolation*, not token savings — and they run on the cheapest
  tier that genuinely does the read. The full economics — when, when-not,
  lossiness — live in the parent's *Sub-agents — isolation, not
  savings* (atelier `docs/method/ECONOMICS.md`).
- **Past your depth? Fail noisily and hand up** — stop improvising, say what
  exceeded you, record it, route up: workhorse → capable tier → principal.
  A silent stall or a quietly degraded attempt blocks the hand-up.

## Session hygiene

- **Stay in one line of work; an unrelated pivot earns a fresh session.** The
  cost is context carried for no use, not tasks done: several tasks in one
  session is the expected case. Related, already-grounded work sharing the
  context is the *same* line; keep going. Break for a genuine reason (an
  unrelated pivot, a principal-only decision, a real unreviewed dependency,
  cache/context degradation), **not because one item went green**. Then write
  the session file, start fresh.
- **Match the ceremony to the risk** — reviews, sweeps, session breaks are
  *spend*; apply them in proportion to the cost of being wrong, not uniformly.
  Risk decides whether a review is owed and of what kind; once owed, no budget
  thins it (atelier's `docs/method/REVIEW.md`, *Budget decides how many
  reviews run and when, never how a review is run*).
- **Never switch model mid-session** — the prompt cache is per-model.
- **Point, don't paste** — give paths/line ranges; let the model read.

The canonical, fuller version is atelier's `docs/method/ECONOMICS.md`
(match-model-to-job, tiered authority, cache economics, ceremony-to-risk, review
triggering). This file carries only what's repo-local, or points up entirely.
