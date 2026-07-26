# ccrepo v2 — flexible grouping, filters, and a message-grain cost engine

Status: **built** (2026-07-17) — every section below is implemented in
`instruments/ccrepo`; this doc stays as the grounded rationale. Two things
sharpened in the build, both recorded here for honesty: (1) the price *base* per
model was cross-checked against ccusage and came out to clean round numbers, so
the table stores published list prices, not observed fits — the reconciliation
stays genuinely independent and lands at ~0.05% drift; (2) subagent logs live in
`<session>/subagents/*.jsonl` and had to be walked recursively and folded into
their parent session, which is what closed the drift (and powers the `kind`
dimension). Numbers below are from the live machine at design time (284 sessions,
a ~6-week log window).

## 1. What changes, in one line

Grouping goes from *"repo is always outer, pick one child"* to **an ordered list
of dimensions, any subset, any order** — and the cost behind it moves from
*session-grain (trust ccusage)* to **message-grain (compute it ourselves, then
reconcile against ccusage)** so the new within-session dimensions are honest.

## 2. Grouping — `--group` / `-g`

One ordered, comma-separated flag. Leftmost = outermost parent. Replaces
`--by-model` / `--by-day` outright (clean break — no aliases kept).

```
ccrepo                       # default: -g repo, cost-descending
ccrepo -g month              # totals per month
ccrepo -g repo,model         # repo → model (old --by-model)
ccrepo -g model,repo         # model → repo (new: any order)
ccrepo -g repo,branch,month  # three levels
ccrepo -g total              # single grand-total row
```

Default stays **`repo`** — it answers "which repo is burning money", it's the
actionable view, and under ~30-day log retention a time default renders only 1–2
rows (see §8). Long flag names are primary; `-g` is the one short alias (hot
path). Existing `-z`, `-h` kept.

## 3. Dimensions and their data grain

The vocabulary you can **group by** is exactly the vocabulary you can **filter
by** (§5). Two grains:

| Dimension | Source | Grain | Notes |
|---|---|---|---|
| `repo` | ccrepo's UUID→path index | session | unchanged; from `~/.claude/projects/` path |
| `model` | per-message `model` | message | opus-4-8 / fable-5 / sonnet-5 / haiku-4-5 / sonnet-4-6 seen |
| `year` `month` `week` `day` `hour` | message `timestamp` | message | all five derivable; sub-day needs message grain (§4) |
| `branch` | message `gitBranch` | message | 49 distinct live — "what did this feature cost"; `HEAD` (detached) bucketed as-is |
| `kind` (main / subagent) | message `isSidechain` | message | subagent/fleet spend |
| `entrypoint` | message `entrypoint` | message | `cli` vs `claude-vscode` |
| `cc-version` | message `version` | message | 10 distinct — release-cost diagnostics |
| `agent` | message `agent` / ccusage | session | uniform `claude` today — wired but latent |

`repo` stays session-grained (stable; `cwd` can vary per message but rarely
matters). Everything marked *message* is attributed exactly, per message, not by
a session's dominant value — that's the whole point of the grain move.

## 4. Cost engine — compute at message grain, reconcile against ccusage

**Why we can't keep trusting ccusage's number directly:** ccusage reports cost
per *session*; branch/kind/version/entrypoint/hour all vary *within* a session,
so a per-session cost can't be split across them honestly. The raw logs carry
per-message **tokens + model** but **no cost** — so ccrepo computes it.

### Price table (embedded snapshot, overridable)

Cost per message = Σ over five token classes of `tokens × price(model, class,
tier)`:

| Token class | Log field |
|---|---|
| input | `usage.input_tokens` |
| output | `usage.output_tokens` |
| cache read | `usage.cache_read_input_tokens` |
| cache write 5-minute | `usage.cache_creation.ephemeral_5m_input_tokens` |
| cache write 1-hour | `usage.cache_creation.ephemeral_1h_input_tokens` |

The 5m/1h split is real and priced differently (≈1.25× vs ≈2× base) — lumping
them is a measurable error, so they're separate classes. `service_tier`
(all `standard` live; `priority`/`batch` carry multipliers) applies a tier
factor. `<synthetic>` model → zero cost. Unknown model → zero + a flag in the
drift report, never a silent guess.

### The reconciliation guard (the feature Mike asked for)

ccusage stays in the loop as the **oracle**. Every run:

1. Sum ccrepo's own per-message costs up to the **session** level.
2. Run `ccusage session --json` and read its `totalCost` per session.
3. Compare. Report **total drift ($ and %)**, the **worst-offending sessions /
   models**, and a best-effort **cause tag** per drift class.

Our per-message table is the working number; the ccusage cross-check is the
alarm that says *our snapshot has drifted and by how much*. A footnote states
the aggregate delta every run (e.g. `Reconciled against ccusage: +0.3% ($2.10)
— within tolerance`); drift past a threshold (say 1%) prints a louder warning.

**Known drift sources to name in the report**, not bury: stale price snapshot,
`server_tool_use` calls (web search etc. — see below), service-tier multipliers,
unknown/new models, cache-tier split.

### Tightening (2026-07-22) — drift chased to ~0.00% per model

Three findings from reconciling against a live `ccusage session`, each grounded
in measurement, not estimate:

- **Dedup was last-wins; it undercounted.** Claude Code re-emits the same
  `(message.id, requestId)` on multiple JSONL lines (a streaming/replay
  artefact); a trailing line can carry partial or **zeroed** usage. Last-wins
  took that trailing line and lost tokens — visible almost entirely on
  `sonnet-5` (~1.5% short), the model whose logs carried the zero-tail pattern;
  other models were near-exact by luck, not correctness. Dedup now keeps the
  **richest** record per key (`keepRicher`, max-total-wins): the complete line is
  always the max, so this recovers it *and* is identical to last-wins on ordinary
  ascending streams. Result: per-model token/cost drift → **$0.00 on the static
  matched session set** (every model exact), and the live per-model footnote goes
  quiet (no model over the 1% threshold).
- **`server_tool_use` is not a contributor.** Measured live: the field is present
  on ~76k assistant messages but **every occurrence is all-zero**
  (`web_search_requests` and `web_fetch_requests` both 0) — zero billable calls,
  so **$0** effect on the drift. Per-call pricing deliberately *not* built; the
  earlier "named contributor" guess is retracted as measured-false. Revisit only
  if non-zero counts ever appear.
- **Fast mode is not a contributor either (measured 2026-07-26).** Fast mode on
  `opus-5`/`opus-4-8` bills $10/$50 per MTok — 2× the standard rate — so if it
  were in use, a single flat price per model would undercount it by half. The
  logs *do* record it: `speed` appears **90,703 times, every occurrence
  `standard`, zero `fast`**. So the effect today is **$0**, and no speed-aware
  pricing is built. Same treatment as `server_tool_use` above, and the same
  discipline: the honest response to a measured zero is to record the
  measurement and the date, not to build for the hypothetical. Revisit only if
  `"speed":"fast"` ever appears — and note the price table would then need a
  per-speed dimension, not just another row.

- **The per-model footnote was scoped wrong.** It compared *mine-all* vs
  *ccusage-all*, so a session only one side had (window-edge date clip, log
  pruning) smeared into a fake per-model delta (once read as "fable +8.9%, opus
  +7.0%"). Per-model is now scoped to the **matched** sessions, same as the total;
  one-sided sessions are reported as a scope gap (`myOnly`/`cuOnly`), never as
  drift.

### Context size (2026-07-26) — added as a peak, not a sum

Mike asked for a reading of "when window sizes are getting large", and named the
three candidate shapes himself: group total, average/median, or max. Measured
across the live logs (419 sessions, 107,902 assistant messages) before choosing:

| Repo | Sessions | Mean | Median | Max |
|---|---:|---:|---:|---:|
| ros | 239 | 191k | 179k | 528k |
| shed | 11 | 238k | **108k** | **578k** |
| hitchbots_guide | 5 | 470k | 283k | 934k |

- **Sum is meaningless** and was rightly doubted: every message carries the whole
  cached prefix, so summing message context sizes counts one window repeatedly.
  Context is the only metric here that must not go through `addTo`.
- **Median and max are both needed.** `shed` is the case that settled it: max 578k
  reads as the scariest repo on the board, median 108k reads as the calmest. One
  blow-out against a light habit — a fact neither figure states alone. So the
  column carries `median/max` in one cell, spending one column rather than two.
- **Mean is out** of the table (dragged by exactly those outliers: `shed` 238k vs
  a 108k median) but ships in `--json`.
- **Grain is per-session peak, not per-message.** Sessions ramp from near-empty,
  so a message-grain median understates what sessions actually reach: 122k
  against 168k across the same set. Matches what `cctranscript` already
  headlines, so "context" means one thing across the instruments.

**A percentage of window can't be built, and that's now recorded rather than
re-derived.** The obvious framing — 148k is 74% of a 200k window but 15% of a 1M
one — dies on the logs: every model string is bare (`claude-opus-5`,
`claude-opus-4-8`, …) with no `[1m]` marker, so the 200k and 1M variants are
indistinguishable. The observed 934k peak proves 1M sessions are in there;
nothing says which. Absolute tokens is the only honest form. Revisit only if the
logs ever start recording the window.

Implementation: each tree node's `sessions` Set became a **Map of session → peak**
— same `.size` for the distinct Sessions count, plus the peaks the column needs,
at one entry per session per node (bounded by session count, not message count).
`ROLLUP_SCHEMA` went to `/2`: the file fingerprint only proves the *source* is
unchanged, so a v1-cached event lacking the new `context` field would have passed
as valid and reported a confident zero on every warm archive run.

### Machine-readable output is deliberately wider than the table (2026-07-26)

Mike's follow-on: the machine-readable form should carry everything useful, since
it isn't width-bound like the terminal. So `--json`/`--csv` carry the **full**
context distribution (`contextSessions/Min/P25/Median/P75/P90/Max/Mean`) where the
table shows two of the seven — `p90` is what separates a lone outlier from a fat
tail, and mean-vs-median is the skew tell. `shed` again proves it earns its place:
min 32k, median 110k, **p90 526k**, max 578k — a genuinely bimodal repo, which the
two-figure column alone would read as one freak session.

Under a billing config the records also carry `coveredTokens` and `uncoveredCost`,
the two inputs `Actual` is apportioned from, so a consumer can re-derive it rather
than trust it. Fields stay **flat**, not nested under a `context` object: §7's
tidy-shape promise is what makes `--csv` a free by-product of the same builder.

The grand total ships as `meta.total` rather than as a row — leaf records stay
subtotal-free per §7, *and* the whole-set context figures genuinely can't be
re-aggregated downstream: peaks don't recompose once a session is split across
groups. A machine can re-sum tokens; it cannot re-derive a peak.

## 5. Filters — mirror the grouping vocabulary

Filters pick which messages/sessions enter; grouping arranges them. **AND across
dimensions, OR within a comma list.** Every group dimension gets a filter:

| Filter | Flag | Example |
|---|---|---|
| repo | `--repo` | `--repo ros,faves` · `--repo '!scanme'` excludes |
| model | `--model` | `--model opus` (short-name match) |
| branch | `--branch` | `--branch 'client-*'` (glob) |
| kind | `--kind` | `--kind main` \| `--kind subagent` |
| entrypoint | `--entrypoint` | `--entrypoint cli` |
| cc version | `--cc-version` | `--cc-version 2.1.209` |
| session | `--session` | `--session 01c3,ff97` (UUID prefix) |
| date range | `--since` / `--until` | day-grained; **now applied by ccrepo itself** (was ccusage passthrough) so the reconciliation runs ccusage with the same window |

**Session IDs are UUIDs, not numbers** — no stable ordinal exists (a new session
or a pruned log shifts any ordinal), so we filter by UUID prefix. A synthetic
`#n` may appear as a *display label* only, never a filter key.

## 6. Sorting — `--sort`

**Per-dimension defaults** (no flag): time dimensions (`year`…`hour`) →
chronological ascending; everything else → **cost descending**.

**Override:** `--sort <spec>`, a comma list aligned to the `-g` levels (a single
value broadcasts to all). Keys: `cost · tokens · count · name · time`, optional
`:asc`/`:desc` (default `name`/`time` asc, metrics desc).

```
ccrepo -g repo,month --sort count,time   # repos by session count; months chrono
ccrepo -g repo --sort name               # alphabetical
```

## 7. Output

- **Default — indented tree.** Extends today's `· ` child prefix to `· `,
  `· · ` per depth; each internal node prints a subtotal row, then its children,
  then the grand `TOTAL`. One "Group" column carries the hierarchy.
- **`--flat` — one column per level** (`Repo │ Month │ Model │ …metrics`), parent
  cells blank-filled. Spreadsheet/pivot shape.
- **`--json` — tidy, never the rendered tree.** One flat record per **leaf**
  group, each grouping dimension as its own named field + metrics; **no subtotal
  rows** (a machine re-aggregates); a top-level meta block (currency, FX rate,
  filters applied, date range, reconciliation delta). Loads straight into `jq` /
  pandas / sqlite.
- **`--csv`** — the same tidy shape, for free.

```json
{"meta": {"currency":"NZD","rate":1.7126,"range":["2026-06-05","2026-07-17"],
          "filters":{"repo":["ros"]},"reconciliation":{"deltaPct":0.3,"delta":2.10}},
 "rows": [{"repo":"ros","month":"2026-07","model":"opus-4-8",
           "sessions":3,"cost":42.10,"totalTokens":21742561}]}
```

## 8. Time retention (context, not a v2 feature)

The data floor is **local log retention**, not ccrepo: logs read only from
`~/.claude/projects/`, no server history, pruned = gone. Live window is ~6 weeks
(earliest 2026-06-05), bounded by Claude Code's `cleanupPeriodDays` (~30 default).
So any time grouping is permanently shallow until history is persisted.

**Deferred idea (not v2):** a small append-only rollup ledger so month/quarter
views survive pruning — the thing that eventually makes a time-based default
worthwhile. Out of scope here; noted so it isn't re-derived.

## 9. Build sequence

1. **Message-grain aggregator + price table + reconciliation guard** — the
   foundation; prove the drift number small before anything leans on it.
2. **`-g` ordered grouping + N-level tree render** (drop `--by-*`).
3. **Filters** (all dimensions, AND/OR, UUID-prefix sessions).
4. **`--sort` full spec.**
5. **`--flat`, tidy `--json`, `--csv`.**

Each slice is a self-verifying instrument change (tests + live drive); no review
gate (ceremony ∝ risk). The reconciliation delta is its own live proof that
slice 1 is correct.

## 10. Deferred / out of scope

Server-tool-use per-call pricing · service tiers beyond `standard` · the
retention ledger · synthetic-ordinal session numbers as filter keys · `agent`
dimension while it stays uniform.
