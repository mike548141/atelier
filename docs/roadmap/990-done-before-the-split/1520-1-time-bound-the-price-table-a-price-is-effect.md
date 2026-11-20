- [x] **1. Time-bound the price table — a price is effective from A to B.**
  `PRICING` entries may be a list of `{from, to, base}` intervals (ISO dates,
  UTC, both ends inclusive, either end open) as well as a bare number, which
  still means "always" — the compatibility guarantee every existing
  `~/.claude/ccrepo-pricing.json` rests on, now pinned by a test. Each message is
  priced at the rate in force when it was **sent**, so a rate change no longer
  rewrites history. A timestamp inside no interval is **unpriced** — $0 and
  flagged, the same path an unknown model takes, never snapped to the nearest
  interval.
  - **Verified rather than assumed, exactly as the item asked:** no
    `ROLLUP_SCHEMA` bump was needed. `recipeSig` already `stableStringify`s the
    price table, so a flat and a time-bounded table sign differently and the
    ledger rebuilds itself; the event *shape* is unchanged, only its values move,
    which is what the signature covers. The previously-untested link (flat vs
    intervals actually signing differently) is now pinned; the
    mismatch-rebuilds half was already covered, so the new test says so rather
    than duplicating it.
  - **Live proof: ccusage cross-check Δ +$0.00 (+0.00%) over 423 sessions** — the
    oracle agreeing to the cent. Stated with its limit: that proves *no
    regression*, not that the post-2026-08-31 rate is right. Nothing can prove
    that yet, so the boundary is pinned in unit tests instead.
  - `sonnet-5`'s introductory `$2` (through 2026-08-31) and standard `$3` (from
    2026-09-01) are both entered, each correct on its own side of the date. This
    **dissolves the dated ⏳ watch** rather than doing it: the diary note became
    data, and the revert now needs nobody to remember it. Published numbers, not
    fitted ones.
  - **Unplanned, and worth keeping:** the unpriced footnote now names *which*
    gap it is. "Add to the price table" is wrong advice for a model already in
    it — that one needs an interval widened. The reason is derived at tally time
    rather than stored on the event, because a new cached field would have cost a
    `ROLLUP_SCHEMA` bump for something only the footnote reads.
