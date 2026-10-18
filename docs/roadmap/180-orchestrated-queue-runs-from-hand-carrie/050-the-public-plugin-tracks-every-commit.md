- [~] (claimed 2026-10-18-0155, wt: atelier-qr-180-followups)
      **The public plugin tracks every commit, not a frozen version.** Mike,
      2026-10-18, asked how the plugin should version for GitHub installers,
      who get a copy frozen at `plugin.json`'s 0.2.0: *"Track every commit"*
      (his pick of the recommended option, which named the trade: installers
      also get doctrine whose review is still pending). Owed: drop the
      `version` field from `.claude-plugin/plugin.json` and the marketplace
      entry, so Claude Code versions the plugin by commit, and correct the
      README caveat that installs are frozen.
