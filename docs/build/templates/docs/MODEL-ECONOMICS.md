# Model & token economics — working policy

The short version of the house policy this repo runs by.

## Who does what

- **Opus (plan-included)** — the workhorse: building, iterating, docs,
  exploration. Plan quota, not dollars.
- **Fable (usage-billed: real money)** — the reviewer and hard-problem
  solver. Give it a **scoped** diff/file list; ask for *findings*, not
  rewrites; apply fixes back on Opus. See `reviews/README.md`.
- **Subagents (Explore, etc.)** — fan-out reading/searching so the main
  context stays lean.

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

The canonical, fuller version is atelier's `docs/method/MODEL-ECONOMICS.md`
(match-model-to-job, tiered authority, cache economics, ceremony-to-risk, review
triggering). This file carries only what's repo-local, or points up entirely.
