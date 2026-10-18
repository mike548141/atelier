- [x] **DONE 2026-10-18** (wt: atelier-qr-180-followups)
      **The public plugin tracks every commit, not a frozen version.** Mike,
      2026-10-18, asked how the plugin should version for GitHub installers,
      who get a copy frozen at `plugin.json`'s 0.2.0: *"Track every commit"*
      (his pick of the recommended option, which named the trade: installers
      also get doctrine whose review is still pending). Owed: drop the
      `version` field from `.claude-plugin/plugin.json` and the marketplace
      entry, so Claude Code versions the plugin by commit, and correct the
      README caveat that installs are frozen.

  **Closed 2026-10-18** (commit `140a190`). No `version` in either manifest.
  `claude plugin validate` passes with one warning (no version), which is
  the chosen trade. The README explains updating and notes that installed
  hooks must be re-run after every update. The principal's own install is
  unaffected: it loads in place from the checkout.
