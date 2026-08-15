- [ ] **D4 — the repo-local seam has no adopters.** The extension point landed
      2026-07-26 and **no repo declares a `local` check** (verified
      2026-07-27). The case that motivated it — a networking child's
      estate-token tripwire, whose blocklist can never live in a shared public
      repo — is still switched off, with CI as the only remaining net. That
      wiring is the child repo's own work, not atelier's, but the seam is not
      proven until something uses it.
