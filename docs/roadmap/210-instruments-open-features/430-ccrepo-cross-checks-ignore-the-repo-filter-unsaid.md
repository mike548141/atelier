- [ ] 🔎 **`ccrepo`'s two cross-checks run over the whole scope when a
      `--repo` filter is set, and the output does not say so.** Found
      2026-11-12 on a run that excluded one repo with `--repo '!name'`; the
      reconciliation lines then carried totals that included the excluded
      repo, beside a table that did not. The principal asked for it on the
      board.
      **What the code says:** `reconcileSpend`'s comment records this as
      deliberate ("works over the whole date-comparable scope, not a
      dimension-filtered slice: the subscription fee is global"), and the
      ccusage cross-check does the same. The reasoning is sound for the plan
      fee. What is missing is the label: a reader of a filtered run sees two
      sets of totals with nothing saying they cover different scopes, and an
      excluded repo's usage appears in output meant to leave it out.
      **Shape:** when any dimension filter is set, print the cross-check
      lines with "(whole scope, filters not applied)" and the scope's own
      total, or offer a flag to suppress them; consider whether the ccusage
      check can be run on the filtered sessions, since ccusage reports per
      session. Test with a fixture that filters one repo out.
