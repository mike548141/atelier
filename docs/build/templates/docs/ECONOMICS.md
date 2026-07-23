# Model & token economics — working policy

The short version of the house policy this repo runs by.

## Who does what

- **Opus (plan-included)** — the workhorse: building, iterating, docs,
  exploration. Plan quota, not dollars.
- **Fable (plan-included, premium draw, capped share)** — the orchestrator,
  reviewer and hard-problem solver. It drinks the shared allowance fastest,
  and past its capped share the next token is silently real money — so keep
  it **scoped**: hand it a diff/file list; ask for *findings*, not rewrites;
  apply fixes back on Opus. See `reviews/README.md`. At the cap the exits are
  stop/delay or the principal choosing to pay — **never down-tier the work to
  dodge the cap**: tier is the work's risk profile's call, not the tank's.
- **Sonnet / Haiku (plan-included, cheapest draw)** — sub-agent fan-out and
  mechanical bulk (searches, scans, pattern-following reads) whose result the
  parent or the mechanical floor verifies.
- **Sub-agents** — fan-out, parallel slices, fresh-context verification; they
  buy context *isolation*, not token savings — and they run on the cheapest
  tier that genuinely does the read. The full economics — when, when-not,
  lossiness — live in the parent's *Sub-agents — isolation, not
  savings* (atelier `docs/method/ECONOMICS.md`).
- **Past your depth? Fail noisily and hand up** — stop improvising, say what
  exceeded you, record it, route up: workhorse → capable tier → principal.
  A silent stall or a quietly degraded attempt blocks the hand-up.

## Session hygiene

- **One task per session — a coherent *line* of work, not a single checkbox.**
  Related, already-grounded work sharing the context is the *same* task; keep
  going. Break for a genuine reason (an unrelated pivot, a principal-only
  decision, a real unreviewed dependency, cache/context degradation), **not
  because one item went green**. Then write the `SESSIONS.md` entry, start fresh.
- **Match the ceremony to the risk** — reviews, sweeps, session breaks are
  *spend*; apply them in proportion to the cost of being wrong, not uniformly.
- **Never switch model mid-session** — the prompt cache is per-model.
- **Point, don't paste** — give paths/line ranges; let the model read.

The canonical, fuller version is atelier's `docs/method/ECONOMICS.md`
(match-model-to-job, tiered authority, cache economics, ceremony-to-risk, review
triggering). This file carries only what's repo-local, or points up entirely.
