# 2026-07-26 · 0100 UTC · ccrepo reports how large context windows got — measured before chosen

**Model**: Opus 5 (1M context), design → build. **Final state**: one commit on
atelier main, instrument suite 180/180 green, floor 9/9, worktree closed.

## The ask

Mike: *"I would like the output of ccrepo to show context size in some way that
helps the user see when window sizes are getting large. But I'm also cognizant
that there are quite a few columns in ccrepo's output already."* He named the
three candidate shapes himself — group sum (*"probably not helpful"*), the
average or median per session, or the max — and asked which.

Mid-build, a second ask: *"in the machine readable version you should include
all the useful information, assuming there are additional columns/fields that
are useful but we can't fit into the CLI UI."*

## The answer was measured, not reasoned

Before recommending a shape, a throwaway probe walked the live logs and computed
every candidate statistic: **419 sessions, 107,902 assistant messages**. That is
what decided it, and two of the three candidates fell to the data:

| Repo | Sessions | Mean | Median | Max |
|---|---:|---:|---:|---:|
| ros | 239 | 191k | 179k | 528k |
| shed | 11 | 238k | **108k** | **578k** |
| hitchbots_guide | 5 | 470k | 283k | 934k |

- **Sum** — Mike's doubt was right, and for a specific reason worth writing down:
  every message carries the session's whole cached prefix, so summing message
  context counts one window over and over. Context is the only metric in ccrepo
  that must never go through `addTo`.
- **Mean** — skewed by exactly the outliers the column exists to catch (`shed`
  238k against a 108k median). Out of the table; kept in `--json`.
- **Median and max, together** — `shed` settled it. Max alone reads as the
  scariest repo on the board; median alone reads as the calmest. The pair says
  *usually fine, once wasn't*, which is the actual situation and which neither
  figure states by itself.

So: **one column, two numbers** — `110k/578k`. That answers the column-count
concern directly, spending one column rather than two on a table already eleven
wide.

**Grain mattered more than the statistic.** Peaks are per *session*, not per
message: sessions ramp from near-empty, so a message-grain median understates
what they actually reach — 122k against 168k across the same set. That also
matches what `cctranscript` already headlines, so "context" means one thing
across the instruments rather than two.

## The percentage column that couldn't be built

The first instinct was `% of window` — 148k is 74% of a 200k window but 15% of a
1M one, and the percentage is what "getting large" really means. It died on the
logs. Every model string is bare (`claude-opus-5`, `claude-opus-4-8`, …) with no
`[1m]` marker, so the 200k and 1M variants are **indistinguishable**. The
observed 934k peak proves 1M sessions are in the set; nothing says which ones.

Absolute tokens is the only honest form. This is now stated in a footnote and in
the man page rather than left for the next session to re-derive and re-abandon.

## The machine-readable side went deliberately wider

Mike's follow-on was the right instinct and reshaped the output: a terminal
column is width-bound, a data file is not. So `--json`/`--csv` carry the **whole**
distribution — `contextSessions/Min/P25/Median/P75/P90/Max/Mean` — where the
table shows two of the seven.

`shed` proves p90 earns its place: min 32k, median 110k, **p90 526k**, max 578k.
That is a genuinely bimodal repo, which the two-figure column alone would read as
one freak session. `p90` separates a lone outlier from a fat tail;
mean-against-median is the skew tell.

Under a billing config the records also carry `coveredTokens` and
`uncoveredCost` — the two inputs `Actual` is apportioned from — so the
apportionment can be *re-derived* rather than trusted. Fields stay **flat**, not
nested: the tidy-shape promise is what makes `--csv` a free by-product of the
same builder.

The grand total ships as `meta.total`, not as a row. Leaf records stay
subtotal-free as designed — *and* the whole-set context figures genuinely cannot
be re-aggregated downstream: peaks don't recompose once a session is split
across groups. A machine can re-sum tokens; it cannot re-derive a peak.

## The bug that was caught before it shipped

`ROLLUP_SCHEMA` went `/1` → `/2`, and this was load-bearing rather than
housekeeping. The rollup ledger validates a cached file by `(mtime, size)` — a
fingerprint that only proves the **source** is unchanged. A v1-cached event
lacking the new `context` field would have sailed through as valid, and every
warm `--from-archive` run would have reported a confident **zero** context,
forever, with nothing to signal it. Caught while designing the change rather
than after; a test now rewinds a ledger to `/1`, strips the field, and proves the
ledger is re-read rather than trusted.

The general rule, now written at the constant: the recipe signature catches
changed *values* (price table, covers list); the schema catches changed *shape*.

## Verification

- `node --test instruments/*.test.js` → **180/180 pass** (13 new assertions).
- `python3 tools/floor.py --plane hook --root . --tools tools` → **9/9, exit 0**.
- Live drives: default tree, `--flat -g repo,kind`, `--json`, `--csv`, `-h`.
- The rendered figures were cross-checked against the independent probe written
  before the implementation existed (ros 179k/528k, atelier 148k/483k,
  hitchbots_guide 283k/934k all matched).
- The `--kind` split independently confirms the footnote's subagent claim: in
  `shed`, subagent windows peak at 122k against the main thread's 578k.

The `--help` digest hit its 40-line ceiling during this work and the drift-guard
test caught it — the closing paragraph was compressed rather than the ceiling
raised. The constraint did its job.

## Left open

- **`opus-5` is unpriced** — the price table has no entry, so 1,314 messages
  currently count at **$0** and the run prints `⚠ Unpriced model(s)`. Pre-existing
  and unrelated to this change, but it means live totals understate. Not fixed
  here: a price must come from Anthropic's published list, never from a fitted
  guess, so it needs Mike. Queued on the roadmap.
