- [x] **Cold review of the plugin bundle (PR #3)** — RAN 2026-07-11 (Fable,
      cold session, isolated worktree): **PASS-WITH-FINDINGS, nothing blocks
      the merge** — verdict in `reviews/2026-07-11-plugin-bundle.md`. Proven
      live: install end-to-end (root-as-plugin delivers tools/+docs/ at the
      consumer end), `/atelier:scan` honest in a foreign repo, install-hook
      blocks/passes/fails-closed as documented, and merge-is-go-live proven
      directly (marketplace add from GitHub fails today — no manifest on
      main). 5 findings: 1–3 **[fixed] on the branch** (`030f185`, PR #3
      updated — update-invalidates-hooks warning, skills' plugin-root refs
      made location-relative, all three companions named); 4–5 notes, no
      action. User config verified clean after (install fully undone). **The
      merge (go-live) is Mike's call, now review-cleared.**
      **MERGED 2026-07-11 (Opus, session 38) — Mike authorised go-live.** PR #3
      merged to `main` (`a0ef731`) after resolving a CHANGELOG append-conflict
      with the intervening ccrepo work and re-running the floor green on the
      merged head (`6245986`: 34 Node + 205 Python + 4 scanners); CI green on
      the head SHA before merge. `main` now carries `.claude-plugin/plugin.json`
      + `marketplace.json`, so `/plugin marketplace add mike548141/atelier` →
      `/plugin install atelier@atelier` resolves — the doctrine now travels as
      behaviour. Branch deleted local+remote. **This is the first deliberate
      widening spent from the live-floor item below.**
