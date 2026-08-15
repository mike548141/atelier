- [ ] **Two children were bootstrapped with `--no-verify`** — the gate they were
      installing already failed on their pre-existing content, so it blocked its
      own installation. Once is the honest resolution; twice would not be. Both
      commits say so in full and list what was found. **Their reds are now their
      own work**: broken internal links (repo-root-relative paths written inside
      `docs/` files two levels deep), decision records with no review line, and
      in one case a credential-shaped string repeated across records that needs
      eyes rather than an exemption. Deliberately not fixed by the rollout —
      another repo's records are its own call.
