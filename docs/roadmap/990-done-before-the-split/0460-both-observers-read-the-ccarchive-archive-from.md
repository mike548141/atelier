- [x] **Both observers read the ccarchive archive (`--from-archive`) — DONE
      2026-07-23** (Mike's direct ask, in two steps; wts:
      cctranscript-archive-read then archive-sourcing-finish). **Closes the
      README's "sourcing seam" on the observe side.** Both `cctranscript` and
      `ccrepo` take `--from-archive` to read the compressed mirror instead of the
      live logs Claude Code prunes, sharing `--dest`/`$CCARCHIVE_DEST` resolution
      verbatim with ccarchive (so one vocabulary points every tool at the same
      mirror; `--dest` alone implies the flag) and one transparent-gunzip
      `readLogText` choke-point per tool (parsers stay byte-format-blind).
      - **cctranscript**: every view (list, render, `--json`, UUID/prefix, explicit
        `.jsonl.gz` path — the last needs no flag) renders a pruned session word
        for word. Eviction-aware because `--list` peeks inside every candidate for
        cwd/first-prompt: it never reads an iCloud-evicted (dataless) mirror
        (listed with an `evicted` marker; `--repo` still matches it by
        dash-encoded folder suffix, its label being lossy), while rendering one
        chosen session deliberately faults its bytes back. Suite 150→156.
      - **ccrepo**: totals reach back past the prune horizon. Because ccrepo reads
        *every* file to sum spend, an evicted mirror is skipped by default and
        counted as a stated gap (`⚠` footnote + `meta.evicted`); `--materialise`
        opts into reading (re-downloading) them. The ccusage cross-check is off in
        archive mode (ccusage reads the live store, which no longer holds the
        pruned sessions) with a footnote saying so; the actual-spend-vs-estimate
        reconciliation still runs. Suite 34→41.
      - ccarchive's SF_DATALESS check is ported into each tool with the same
        `CCARCHIVE_SIMULATE_DATALESS` seam; both man pages + `--help` updated under
        the flag drift guard. The flag is `--from-archive`, not `--archive`: the
        bare form read as an imperative ("archive the transcripts"), not a source
        selector (Mike's call). What remains of the seam is only the deferred
        rollup *precompute* ledger (`ccrepo.design.md` §8) — a speed layer, not a
        survival gap, since the raw logs are preserved (ROADMAP § ccrepo).
