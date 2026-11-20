- [x] **man-page convention rollout — cctranscript + ccrepo** (closed
      2026-07-21, wt: worktree-manpages). Closes the rollout the CLI-docs
      standard opened: the `--help`/`man` split (REPO-STANDARD § "An installed
      CLI ships both") was established with `ccarchive` as the reviewed worked
      example; this rolls it to the two remaining **installed** CLIs, so every
      tool the installer publishes to `PATH` now carries both registers. Each
      ships a full plain-language `instruments/man/<tool>.1` (NAME/SYNOPSIS/
      DESCRIPTION/OPTIONS/FILES/EXAMPLES/EXIT STATUS/NOTES/SEE ALSO, matching
      `ccarchive.1`'s roff style, `mandoc -T lint` clean) and a trimmed `--help`
      digest pointing at the manual (cctranscript 42→24 lines, ccrepo 67→35;
      rationale + worked examples relocated into the page — the page is the
      superset, so the two can't drift). **EXIT STATUS enumerated against every
      `process.exit()` path in each source** — the drift a prior ccarchive
      applied-batch review caught (`EXIT STATUS` predating the tool's non-zero
      paths), designed out here at authoring time. +6 doc-convention tests
      (digest-points-at-man, well-formed-roff, superset drift-guard), mirroring
      ccarchive's pattern; the installer already globs `man/*.1` so no install
      change. Verified: 92 instrument tests green, mandoc clean ×3, installer
      drive publishes all three pages into a throwaway MANPATH, leak/secret/
      link/size scans clean. Application of a reviewed convention, not new
      doctrine ⇒ no review cycle owed (REVIEW.md rule 4). Orchestrated: one Opus
      session + two parallel Opus agents (one per tool, disjoint files in the
      worktree), the orchestrator verifying and committing.
