# 2026-07-17 · 0921 UTC · ccrepo v2 — flexible grouping, filters, message-grain cost engine

The build of the design captured two sessions earlier in `instruments/ccrepo.design.md`.
Mike: "build all the ccrepo related stuff we have talked about now — start coding."
Done in an isolated worktree (`ccrepo-v2`) because a parallel session was live
building `ccarchive`; landed as PR #8 after rebasing onto its two merged PRs.

## What shipped

A near-total rewrite of `instruments/ccrepo`. The pivot: **stop trusting ccusage
for cost — compute it here, per message, and reconcile against ccusage instead.**

- **Message-grain cost engine.** Reads the raw `~/.claude/projects/` logs directly
  and prices each assistant message from a local list-price table across five
  token classes — input, output, cache read, and the **5m/1h cache-write split**
  (they price differently; lumping them is a measurable error). The base price per
  model was cross-checked against ccusage and came out to clean round numbers
  (opus-4-8 $5, fable-5 $10, sonnet-5 $2, sonnet-4-6 $3, haiku-4-5 $1 per MTok
  input; ×5 output, ×0.1 read, ×1.25/×2 write), so the table holds **published
  prices, not fitted ones** — the reconciliation stays genuinely independent.
- **Reconciliation guard** (the feature Mike asked for): every run sums ccrepo's
  own per-session cost, runs `ccusage session --json`, and reports the drift ($
  and %, largest per-model). Lands at **−0.05%** on the live logs. A large drift
  would mean the price table has gone stale — it announces itself. `--no-reconcile`
  skips it; `~/.claude/ccrepo-pricing.json` overrides the table.
- **Ordered grouping** `-g a,b,c` over `repo · model · branch · kind · entrypoint
  · cc-version · agent · year/month/week/day/hour`, nested any order, `total` for
  one row. Default `-g repo`, cost-desc. `--by-model`/`--by-day` removed (clean
  break, no aliases). N-level tree; **Sessions is a distinct count at every level**.
- **Filters mirror the group vocabulary** (`--repo`/`--model`/`--branch`/`--kind`/
  `--entrypoint`/`--cc-version`/`--agent`/`--session` + `--since`/`--until`): OR
  within, `!` excludes, `*` globs, sessions by UUID prefix. `--sort` overrides the
  per-dimension defaults (time chronological, else cost-desc).
- **Output**: indented tree default; `--flat` (one column per level); tidy
  `--json`/`--csv` (one record per leaf, each dimension a named field, `meta`
  block with reconciliation + filters + range). Billing (Actual vs Est) carried
  forward.

## Two things the build surfaced (not in the design)

1. **Subagent logs.** `<repo>/<session>/subagents/*.jsonl` sit one level deeper
   than the flat session files; the reader had to walk recursively and fold them
   into their **parent session** (which is how ccusage counts them). This was ~$167
   of real spend — including it is what closed the reconciliation from −4% to
   −0.05%, and it powers the `kind` (main vs subagent) dimension.
2. **A repo-label bug, caught by verifying not assuming.** `eventFrom` defaulted an
   unknown repo to the literal `'—'`, which is truthy, so the post-walk
   re-resolution skipped it — subagent logs walked before their dir's main file
   locked in `'—'`. Fixed to a falsy default; a regression test guards it.

## Dedup detail (why the number is right)

Assistant messages stream partial-usage lines under one `(message.id, requestId)`;
only the final line carries complete counts. ccusage keeps the **last**; the first
draft kept the first and ran ~4% low. Last-wins dedup matches ccusage to 0.09% on
tokens.

## Verified

- 40 ccrepo unit tests (was 21) — pricing, parsing, N-level grouping, sorting,
  filters, reconciliation, the label regression. Full instrument suite 58 pass.
- Floor green: 247 tool tests, secret/leak/licen/link/size scans all clean.
- Driven live across every mode: default, `-g month|kind|model,repo|repo,branch,
  model|total`, `--flat`, `--json`, `--csv`, filters, `--sort`, error exits.

## Convergence with ccarchive

The parallel session's `ccarchive` (durable transcript preservation) is exactly
the retention-ledger idea flagged in design §8 — it makes time-based `-g month`
worthwhile long-term by outliving Claude Code's ~30-day cleanup. The two land
side by side.

## State

PR #8 (`ccrepo-v2`), rebased onto the ccarchive merges. `ccrepo.design.md` status
flipped to **built**. No open ccrepo follow-ups.
