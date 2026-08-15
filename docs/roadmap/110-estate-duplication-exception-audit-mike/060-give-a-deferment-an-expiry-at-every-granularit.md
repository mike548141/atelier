- [ ] **Give a deferment an expiry at every granularity, not just `advisory`.**
      Raised by the ruling above. Today `review-by` is a floor-config field, so
      the only declarable deferment is a whole check. The two cases just dated
      are path-level, and a line marker has the same hole — `<guard>:allow:` is
      pure acceptance by construction, which is fine until someone writes one
      for a thing they mean to fix. Cheapest shape that keeps the ignore-file
      format: an optional `review-by: YYYY-MM-DD` recognised in the comment
      block attached to a glob, reported on the floor line and the fleet board
      exactly as an advisory's expiry is, red when lapsed. Deliberately not
      built here: it is a scanner-loader change across ten ignore-file readers
      plus board rendering, and it wants its own session. Until it exists,
      a path-level deferment's date is a promise, not a gate — which is
      precisely the thing `GUARDS.md` says a deferment must not be.
