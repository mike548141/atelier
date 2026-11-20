- [x] **Secret-scan on push** — built 2026-07-10 as `tools/secretscan.py` (a
      zero-dep, self-written "equiv", not a gitleaks install — matches the house
      tool pattern + dodges the tool-install floor). Named vendor formats + a
      secret-named-assignment/entropy workhorse; skips the safe indirections
      (`!secret`/`${VAR}`/`<ph>`), code refs, public keys and URL paths.
      **Validated 0 FP over real tiki source/inventory/docs** (25→0 across three
      FP-class fixes) while still catching the fixture-secret shapes; report
      redacts to length+entropy. 47 tests; combined pre-commit sample runs it
      with leakscan; `.secretscanignore` + allow-marker escape hatches.
      Reviewed 2026-07-10 (batch review — pattern set + heuristic hold, skip-list
      verified against SECRETS.md's named forms; B4 renamed-file staged hole
      fixed + proven live, B6/B7 residuals stated). **Owed:** CI wiring (dead until atelier has a remote);
      hook portability to Mike's other repos. Closes the *detect* half of
      *detect → rotate → burn-cost-is-minutes*.
