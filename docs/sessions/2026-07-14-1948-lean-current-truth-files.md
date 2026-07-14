# 2026-07-14 · lean current-truth files — `sizescan` + the harvest trigger (Opus)

**Mike's prompt:** key files keep getting too big/long — the ROADMAP in each
repo especially — the same class of problem the SESSIONS file hit before. Review
all the repos to understand the inefficiency (overly large files), and devise a
way to reduce it *without dropping the quality we've built up*.

## The diagnosis

Surveyed all 14 fleet repos for markdown size. The bloat is one root cause with
the fix already half-written in atelier's own doctrine but neither lived nor
enforced.

Offenders (current-truth files loaded every session): `ros/docs/ROADMAP.md`
**3197 lines**, `atelier/docs/ROADMAP.md` **1091**, `faves/docs/SESSIONS.md`
**1157** (never adopted the index split), `faves/docs/ROADMAP.md` 766. The
grepped-on-demand stores (ros SPECS 1328, ROADMAP-DONE 1285, atelier CHANGELOG
853) are less critical — they're destinations, meant to grow.

The **real growth dynamic** is subtler than "done items pile up": a finished
roadmap *item keeps accreting the story of how it got done* — a correction, a
review verdict, a live-proof note, a suite count. The item becomes a mini
session-log. That narration is valuable **case-law**, but it's *history* living
in a *current-truth* file, and every session pays to load it.

Why SESSIONS got fixed and ROADMAP didn't: `RECORD.md` already prescribed the
index/detail split — but nothing **triggered** it. SESSIONS was split once, by
hand; nothing fired when a file bloated again. No `sizescan` in the triad.

## Decisions (Mike, via scoping question)

- **Mechanism:** doctrine **+** a `sizescan` tool (a real signal, consistent with
  the scan-triad floors), not doctrine alone.
- **Backfill scope:** mechanism + **atelier only** (dogfood here first); ros +
  faves flagged as backlog for their own sessions.

## Built

- **`tools/sizescan.py`** — seventh house scanner, scan-triad pattern (zero-dep,
  `--selftest`, `--json`, allow/ignore hatches, fail-safe exit codes). Budgets
  only the files meant to stay lean; **excludes the append-only stores by
  design** (flagging the destination would punish the fix). Root-only rule for
  `README`/`CLAUDE` (a nested `tools/README.md` is a reference index — keeps the
  signal sharp). **Advisory by default** (exits 0 — bloat is recoverable, not a
  defect like a leaked secret); `--check` is the opt-in gate. 24 tests
  (`test_sizescan.py`). Fleet-proven: sharp on ros (3197) + faves (1157), silent
  on the seven healthy repos, gentle marginal nudges (shed SESSIONS +5).
- **`method/RECORD.md` § "The roadmap"** sharpened — the growth dynamic, the
  relocate-never-delete fix, the generalisation (*current-truth files stay lean;
  history relocates to an on-demand store*), and the harvest-at-close trigger.
- **`tools/README.md`** — full `sizescan` section + its honest residual (length
  is a proxy for token cost, not for bloat; it says "look at this", never "this
  is wrong") + the not-wired-yet note.

## Dogfood

- **`docs/ROADMAP.md` harvested 1091 → ~180 lines** (well under the 300 budget).
  ~800 lines of completed case-law moved **verbatim** to a new
  **`docs/ROADMAP-DONE.md`** (a slicing script did the move byte-exact, then
  accounted for every checkbox item across both files — **zero lost**, 5 new this
  session). Open items kept in place; done sections collapsed to one-line
  pointers. `sizescan` + `linkscan` clean on the result.

## Floor

240 tests OK · 6 scanner selftests OK · scan triad clean · sizescan clean ·
linkscan clean · full leakscan (structural + local terms) clean on the new files.

## Owed / handed back

- **Review-owed:** `sizescan` + the RECORD doctrine are net-new tooling → an
  un-briefed cold pass owed **before** wiring `sizescan` into `ci.yml` /
  `floor.yml` (`--check` mode). Don't-stack: nothing leans on it yet. Sharpest
  questions logged in ROADMAP: budget defensibility, the root-only masking risk,
  line-count-as-proxy honesty, advisory-exit-0 toothlessness.
- **Fleet backlog** (own sessions): ros ROADMAP harvest (3197, delicate case-law
  relocation), faves SESSIONS index/detail split (1157) + ROADMAP harvest (766).
- Handed back as a **branch + PR** (doctrine change → Mike merges), not
  self-merged.
