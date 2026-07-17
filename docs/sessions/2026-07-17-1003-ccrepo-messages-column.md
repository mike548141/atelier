# 2026-07-17 · 1003 UTC · ccrepo — a Messages column + two roadmap items

Small follow-on to the ccrepo v2 build, in an isolated worktree (`ccrepo-messages`)
because a parallel review session is live (`worktree-fable-review`).

## Messages column

Mike: "since we are now dealing in messages, add a column that counts the number
of messages the same way we report the number of sessions." Now that the engine
is message-grain, each event *is* one deduped assistant message, so the count is
a natural sum: `messages` added to `zeroAgg`/`addTo` (threads through every
rollup), set to `1` per event in `eventFrom`, and surfaced as a **Messages**
column right after **Sessions** in the tree, `--flat`, `--json`, and `--csv`.

The two counts are deliberately different aggregations, and the contrast is the
point: **Sessions is a distinct count** (a session appears once no matter how many
messages or child buckets it spans), **Messages sums** (24,312 main + 1,423
subagent = 25,735 total, whereas the 287 distinct sessions don't sum across
main/subagent). Footnote updated to say so. +2 test assertions (67 total).

## Two roadmap items captured (Mike, mid-session)

Added under `ROADMAP.md` → instruments/ → `### ccrepo`:

1. **Tighten the ccusage reconciliation drift** — v2 lands at ~0.05%; chase the
   residual per-model (sonnet-5 ~1.5%), decide whether `server_tool_use` per-call
   pricing is worth adding, and where it can't reach zero, *name the cause* in the
   footnote.
2. **Actual spend (plan or usage) vs the API-usage estimate** — the money-side
   analog of the ccusage cross-check: compare what Mike genuinely pays (a Max
   5x/20x tier, or metered usage) against ccrepo's API-list-price estimate and
   show the delta. Needs a machine-local real-spend source (stays in `~/.claude`,
   never a repo — same boundary as `ccrepo-billing.json`).

Also flipped the man-page rollout note: ccrepo v2 has landed, so its `--help` is
stable and that item is unblocked (it belongs to the review session's man-page
convention line).

## Verified

67 instrument tests pass; sizescan + linkscan clean; Messages column driven live
in tree/flat/json/csv. No review owed (instrument, self-verifying).
