# 2026-07-17 · 2235 UTC · File-size hygiene — ros pivot, then the faves harvest (Opus)

Mike's themed session: **File-size hygiene (own focused sessions)** and the
doctrine backlog. Solo-ish on `main` alongside a live parallel atelier session
(`instruments-audit`, ccarchive `--audit`) and a live **ros** session.

## The ros pivot (why the flagship harvest didn't run)

The biggest fleet file-size offender is `ros/docs/ROADMAP.md`, which `sizescan`
now flags at **4933 lines** — grown from the **3197** recorded when the roadmap
item was filed. Claimed it in atelier's ROADMAP (`[~]`), pushed the claim, and
set up a ros worktree.

But the branch/worktree vanished between commands, and the cause surfaced: **a
live ros session was actively committing to ros `main`** — including
`495def8 chore(roadmap): claim RADIUS home slice 1`, a commit ~3 minutes old
that *edits `docs/ROADMAP.md`* (claiming a roadmap item). That is a direct
collision with a wholesale harvest of the same file: severe merge conflicts, and
a real risk of clobbering the other session's live claims. The roadmap item's
own words — "its own focused ros session" — are literal: the harvest can't run
concurrent with an active ros session.

**Action:** released the claim (`[~]`→`[ ]`), kept the corrected line count, and
recorded a **liveness-check hazard** on the item so the next taker checks ros is
quiet first. Cleaned up the ros worktree/branch. Pivoted to a quiet repo.

## The faves harvest (done, `sizescan` clean)

faves was idle since 2026-07-12 (clean tree) — safe. All three flagged
current-truth docs brought under budget:

- **`SESSIONS.md` 1157→234.** Adopted the index **rotation** the ros/tiki
  convention implies but faves had never made (its header claimed the convention
  in name only): the recent tail stays in the always-loaded index; the older
  entries moved **verbatim** to a new `docs/SESSIONS-ARCHIVE.md` growth store —
  the same current-truth/history split as `ROADMAP`→`ROADMAP-DONE`. Rotated one
  extra entry when this session's own log entry needed the headroom.
- **`ROADMAP.md` 766→299.** The current-truth/history split. Every *resolved*
  item — shipped, decided-against (✗), or owner-parked — moved verbatim to a new
  `docs/ROADMAP-DONE.md` behind a lean ✅/⚑ pointer; the genuinely-open and future
  work (constraint analyses, Theme 6/8, the recommended sequence) stayed. Done
  by a **scripted line-range partition** with a coverage check (no gap/overlap
  over the whole themed body) and a byte-identical verbatim assertion per moved
  block; the theme-heading set was proven unchanged.
- **`ARCHITECTURE.md` 276→250.** Trimmed without losing architecture facts: the
  Hosting section collapsed to the made decision (the AWS-fallback deliberation
  lives in ADR 0004 + `DEPLOY.md`); the stale "deferrable to Phase 7" hosting
  row corrected; ranking / `ordering` / personal-layer prose de-duplicated
  against `ranking.js` and the roadmap; the rot-prone exhaustive `js/` module
  enumeration condensed to one-per-concern.

Three faves commits `dba7658..ab6a12d`, fast-forward merged to `main` + pushed,
worktree removed. No review owed — mechanical relocation, verified verbatim, no
doctrine change.

## atelier bookkeeping

faves item marked `[x]`; the ros item released with the hazard note; the
fleet-children floor note updated (faves now harvested, so adopting the
`sizescan --check` gate there is safe — a separate step, not done here). Kept
atelier's own `ROADMAP.md` ≤300 (its CI gates on `sizescan`, so this is
load-bearing, not just dogfood).
