# 2026-07-23 · 0346 UTC · archive sourcing finished + flag renamed

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 174+1 -->
- [2026-07-23 · 0346 UTC · archive sourcing finished + flag renamed (Opus, wt: archive-sourcing-finish)](2026-07-23-0346-archive-sourcing-finish.md) — two follow-ups on the 0327 work. **(1)** Renamed `--archive` → `--from-archive` across cctranscript (code, HELP, man roff, tests, README, CHANGELOG, ROADMAP) — the bare form read like an imperative ("archive the transcripts"); the tool never shipped `--archive`, so the living records take the final name. **(2)** Built `ccrepo --from-archive`, closing the observe-side sourcing seam: totals now reach past Claude Code's prune horizon over the same mirror, same shared `--dest`/`$CCARCHIVE_DEST` resolution + one `readLogText` gunzip choke-point + `_external` skip. Key divergence from cctranscript — ccrepo reads *every* file, so an iCloud-evicted mirror is **skipped-by-default and counted** (`⚠` + `meta.evicted`), `--materialise` opts into reading (the ccarchive `--verify`/`--materialise` two-step Mike already ruled on). ccusage cross-check auto-off in archive mode (it reads the live store the pruned sessions have left) with a footnote; actual-spend reconciliation still runs. SF_DATALESS ported with the same sim seam. node 156→160, ccrepo 34→41 (spawn contract over a synthetic `.jsonl.gz`, evicted-skip + materialise round-trip); tools/ 331 OK; both man pages lint clean; drift guards green. Smoke: `-g month` over the archive shows 2026-06/07 rollups. Records: combined CHANGELOG + ROADMAP-DONE entries, README seam **closed on observe side**, only the deferred rollup *precompute* ledger remains. No doctrine authored ⇒ no review pointer owed.


**Model:** Opus 4.8 · **Worktree:** archive-sourcing-finish · **Trigger:** two
follow-ups from Mike on the 0327 cctranscript work — (1) rename `--archive` to
`--from-archive` (the bare form read like an imperative, "archive the
transcripts", from a noob's view); (2) do the ccrepo half of the sourcing seam
I'd flagged as the one honest leftover.

## What landed

**1. Rename `--archive` → `--from-archive` (cctranscript).** Flag string, HELP,
man page (all roff tokens), tests, README, CHANGELOG, ROADMAP mentions. The tool
never shipped `--archive` to anyone, so renaming the living records to the final
name is honest, not history-editing. `--help` re-condensed to hold its
one-screen budget. 24 tests green.

**2. `ccrepo --from-archive`** — closes the observe-side sourcing seam. ccrepo
now reads the same compressed mirror, so token/cost totals reach back past
Claude Code's prune horizon. Built to the same pattern as cctranscript:

- **Shared vocabulary.** `--dest`/`$CCARCHIVE_DEST` resolve exactly as in
  ccarchive; `--dest` implies `--from-archive`. One `readLogText` gunzip
  choke-point keeps the walk byte-format-blind; `LOG_EXT` switches `.jsonl` ↔
  `.jsonl.gz`; `_external/` (ccarchive's history.jsonl home) is skipped.
- **Eviction: skip-by-default, not read-by-default — the key divergence from
  cctranscript.** cctranscript `--list` *peeks*; ccrepo's whole job is to *read
  every file*. On an iCloud-evicted (dataless) archive that would bulk-download
  the history. So an evicted mirror is skipped and counted as a stated gap (`⚠`
  footnote + `meta.evicted`), and `--materialise` opts into reading
  (re-downloading) them — the same two-step ccarchive's `--verify` /
  `--verify --materialise` established, which Mike already ruled on and
  understands. On a fully-local archive (this machine: `evicted: 0`) nothing is
  skipped and it just reads everything.
- **ccusage cross-check off in archive mode.** ccusage reads the live store,
  which no longer holds the pruned sessions, so the comparison would be
  structurally short rather than real drift — auto-off, with a footnote saying
  why. The actual-spend-vs-estimate reconciliation (which doesn't call ccusage)
  still runs, and is more useful over full history.
- ccarchive's SF_DATALESS check ported with the same `CCARCHIVE_SIMULATE_DATALESS`
  seam. Source/evicted surfaced in both the human footnotes and `meta` (JSON/CSV).

## Evidence

- node 156→160 total; ccrepo 34→41 (spawn-based archive contract test over a
  synthetic `.jsonl.gz`: prices the mirror at a known $30, `--dest` implies the
  flag, evicted-skip + `--materialise` round-trip, `readLogText`/`isDatalessFlags`
  units — offline via `--fx usd --no-billing`). tools/ 331 OK. Both man pages
  `mandoc -T lint` clean; both `--help` under budget; flag drift guards green.
- Smoke on the real archive: `ccrepo --from-archive -g month` shows 2026-06 +
  2026-07 historical rollups ($1.23 / $6,793.60 USD); cctranscript `--from-archive`
  renders a 31-turn session tagged `source: archive`. Archive totals sit just
  under live because ccarchive runs daily and today's in-flight sessions aren't
  mirrored yet — expected and honest (the archive only *exceeds* live once live
  starts pruning at the 30-day horizon).

## Records

CHANGELOG (one combined "both observers read the archive" entry, folding in the
earlier cctranscript entry + the rename rationale), README (ccrepo table row +
the sourcing-seam paragraph now **closed on the observe side**), ROADMAP-DONE
(single combined entry replacing the cctranscript-only one), ROADMAP § ccrepo
(seam closed; only the deferred rollup *precompute* ledger remains — a speed
layer, not a survival gap).

## Open

- The rollup precompute ledger (`ccrepo.design.md` §8): optional speed layer so a
  wide `--from-archive` run needn't re-walk the whole mirror. Not scheduled — the
  archive made it non-essential (raw logs preserved, any view recomputes).
- No doctrine text authored (tool code + records) ⇒ no review pointer owed;
  routine cold review rides the normal queue if wanted.
