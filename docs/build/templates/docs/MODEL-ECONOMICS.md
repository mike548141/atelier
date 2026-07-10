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

- **One task per session**; wrap up with a `SESSIONS.md` entry, start fresh.
- **Never switch model mid-session** — the prompt cache is per-model.
- **Point, don't paste** — give paths/line ranges; let the model read.

The canonical, fuller version is atelier's `docs/method/MODEL-ECONOMICS.md`
(match-model-to-job, tiered authority, cache economics, review triggering).
This file carries only what's repo-local, or points up entirely.
