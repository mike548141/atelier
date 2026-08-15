- [ ] **P8 — traffic harvest: keep the history GitHub's 14-day window
      discards (Mike directed 2026-08-06,** from a faves session). GitHub's
      traffic API (clones/views + referrers/paths, admin-only) is the only
      visibility into who copies a public repo, and it holds a rolling 14
      days — measured that day: atelier 1,737 clones / 338 uniques against
      3 unique human viewers (the scraper signature), `rpi` 180/32. A
      scheduled job fetches all four endpoints for every public estate repo
      (enumerate via `floorfleet --from-github`, filter to public) and
      appends per-day rows to a committed dataset; weekly cadence gives
      overlap inside the window, deduped on the day-stamp. Pattern
      precedent: B1's scheduled conformance job. Three calls to make at
      pickup, none pre-empted here: **storage home** (this repo vs the
      estate root — referrer data is mildly reconnaissance-ish, and P6's
      ruling may bear on where operational telemetry belongs), **token**
      (traffic endpoints need push-access scope per repo; mint down the
      estate root's credential ladder, B1's token as precedent — check
      whether its scope already covers this before minting anything), and
      **cadence/retention**. Matters most in the fortnight after any
      future flip (`ros`, `faves`) — the baseline is unrecoverable if the
      job starts late, so build it before the next flip, not after.
