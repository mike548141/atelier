# Deferred — coverage accounting cold pass (brief-writer's held-back material)

**Board:** `docs/roadmap/160-doctrine-review-owed/1380-rule-4-cold-pass-queued-coverage-accounting.md`
**Status:** sibling of the unrun brief `2026-11-14-0259-coverage-accounting-cold.md`, written
2026-11-14 UTC by the brief-writer (session `2a99cef1`). Open only after phase-1 findings are
committed; fold in below the reconcile, then delete.

The brief-writer forms no finding and writes no severity. What follows is what it saw while
grounding the brief, held back so it cannot steer phase 1. Weigh each as a lead, not a result.

## Re-run results, 2026-11-14 UTC (load 3–5 on 12 cores, Python 3.14.6)

All exit 0, one at a time from `tools/`:

| module | tests | seconds |
|---|---|---|
| `test_report` | 110 | 12 |
| `test_datescan` | 100 | 13 |
| `test_wrapscan` | 71 | 16 |
| `test_spellscan` | 90 | 22 |
| `test_conflictscan` | 88 | 16 |
| `test_harvestscan` | 54 | 23 |
| `test_pointerscan` | 52 | 6 |
| `test_indexscan` | 57 | 12 |
| `test_licenscan` | 79 | 3 |
| `test_reviewscan` | 70 | 10 |
| `test_publishscan` | 60 | 28 |
| `test_sizescan` | 117 | 14 |
| `test_secretscan` | 272 | 20 |
| `test_leakscan` | 422 | 43 |
| `test_linkscan` | 89 | 6 |
| `test_pathscan` | 172 | 14 |
| `test_attribscan` | 36 | 7 |
| `test_blockscan` | 58 | 36 |
| `test_pdlistscan` | 24 | 5 |
| `test_signscan` | 18 | 49 |
| `test_stampscan` | 125 | 11 |

- `tools/floor.py --root .` (default plane, clean tree, nothing staged): exit 0, 29 s, 16
  `coverage:` lines, **10 of them `scanned nothing`**.
- `tools/floor.py --plane ci --root .`: exit 0, 33 s, 16 `coverage:` lines, 0 `scanned nothing`.
- Empty scratch repo, `spellscan --root <scratch>`: exit 0; output opens `✓ spellscan clean —
  no US spellings found.` and its third line is the `scanned nothing` warning.

## Leads the brief-writer noticed (not findings)

- **A1:** `publishscan`'s unit count is `len(NEVER_PUBLISH)`, a constant (69 at HEAD), so only its
  path count can reach zero. `reviewscan` passes `n_checked` as both counts. Whether either can
  report non-zero over nothing evaluated is the reviewer's to probe.
- **A4:** the default-plane floor run above printed the warning ten times on a clean tree with
  nothing staged. Whether a real hook run ever looks like that, and whether ten warnings there
  are signal or noise, is open.
- **A2 / wording:** the empty-repo run still leads with `✓ … clean`. The warning avoids "clean",
  but the scanner's own first line does not; whether the pair reads as the item's opening claim
  wants is the reviewer's call.
- **A6:** `sweepscan`, `namescan` and `quotescan` (added after `641f017f`) do not call
  `report.coverage_line` at HEAD (by `grep`). `floor.py --list --root .` shows 19 rows (`board`
  and `sweepscan` among them; `blockscan`, `signscan` and `stampscan` are not rows there), while
  both floor runs printed 16 coverage lines, one fewer than the 17 rows left after `board` and
  `sweepscan`. Which rows print none, and whether the `GUARDS.md` "every guard" sentence binds
  them, is open.
- The five-checkout probe is recorded only as counts in `CHANGELOG.md`; no command was found.

## Nothing else is deferred

The brief-writer read no commit body and no prior verdict, so it holds no author account beyond
what the brief's exposure line names.
