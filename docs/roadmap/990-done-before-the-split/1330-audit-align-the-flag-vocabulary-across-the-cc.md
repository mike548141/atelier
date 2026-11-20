- [x] **Audit + align the flag vocabulary across the cc-tools — DELIVERED
  2026-07-23** (`85b17dd`, 0441 run). End-to-end read of all three tools'
  `--help`, man pages and arg parsers confirmed **zero drift** — `--dest`,
  `--from-archive`, `--materialise`, `--json`, `--repo` all consistent where they
  overlap; no renames. Landed a **vocabulary table** in `instruments/README.md`
  as the standing reference, with the `--materialise` asymmetry documented as
  deliberate (cctranscript has no bulk-read op to name).
