# 2026-07-11 · the instruments code review's 10 findings, fixed + pinned (Fable)

Mike's ask: do all of atelier's review work, starting with the ten confirmed
findings from the earlier code review of `8536971` (the instruments test
floor) — still unfixed, and two of them affecting the floor that had just
landed.

## Recovering the findings

The review ran in a separate session (`738f1fbc`, high-effort /code-review: 8
finder angles, ~14 candidates, per-candidate empirical verification) but its
report lived only in that transcript — no brief in `docs/reviews/`, no ROADMAP
item. Recovered with `cctranscript --json` over the transcript (the instrument
reading its own review — the `ref` scheme built yesterday <!-- datescan:allow: date uncertain; wrapscan:allow: marker-inflated line -->
made the findings message directly addressable as turn 22.1). Now recorded
properly:
`docs/reviews/2026-07-11-instruments-test-floor-code-review.md` carries the
ten findings, the three cut-by-cap residuals, and the disposition.

## What was fixed (all ten, suite 20→26)

The floor-affecting pair first: the **timezone-fragile `--by-day` test**
(fixture timestamps 03:00Z/04:00Z straddled local midnight at UTC-4/-3:30;
moved to midday-UTC minutes apart, which shares a local calendar day in every
real offset — suite proven green under `TZ=UTC`, `America/Halifax`, and
`Pacific/Chatham`) and the **`test_*.js` → `*.test.js` rename**. One honest
correction to the review's suggested fix there: node:test *directory* args are
rejected on Node 22+ (proven locally on 24) and quoted globs need Node 21+, so
the documented/CI command became the **shell glob**
`node --test instruments/*.test.js` — expands at run time, works on every Node
the job might pin, and a future test file still can't silently skip CI.

Correctness: help/validation argv parsing moved out of module load in both
instruments (a host requiring them with `-h` in its argv was killed by
`process.exit` — proven live, then pinned by require-survival tests that spawn
exactly that host); `shortModel` made total; `.session` envelope guard;
dangling-symlink guard in ccrepo's walk (proven against a planted symlink);
`main().catch` so a failed run can't read as exit-0 silence (the EVIDENCE §14
class). Cleanups: `pt`/`paint` dedup via a defaulted `on` param; one
`sessionRecord()` constructor for walked and explicit-path sessions (real
`stat` mtime — list view no longer renders a blank timestamp); `buildIndex()`
returns its maps, `label()` takes the map explicitly.

The three cut-by-cap items (impure `readTurns` under a "pure functions"
comment — the comment was reworded in passing; `cwdFromLog` cross-instrument
duplication, deliberate per instruments/README; duplicate test spawn) stay
recorded in the brief, deliberately unfixed.

## Proof

Both instruments re-driven live after the fixes (ccrepo table byte-comparable;
cctranscript list/help/explicit-path, which now shows a real timestamp). Full
floor green: 205 Python + 26 Node tests, all three timezones, and the
secretscan/leakscan/licenscan/linkscan quartet clean. Records: review brief,
CHANGELOG "Fixed" block, ROADMAP filenames swept to the new names (CHANGELOG's
and SESSIONS' older entries left verbatim — they record what was true then).
