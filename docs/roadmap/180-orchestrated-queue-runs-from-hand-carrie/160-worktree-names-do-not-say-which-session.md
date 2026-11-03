- [x] **DONE 2026-11-03** (wt: atelier-qr-4c65-dispatch) 🔎 **Worktree names do not say which session made them, and a
      brief-writer misread authorship because of it.** Two queue runs were
      live at once on 2026-10-18 (`e1d4097c`, `8e498ef1`). Both named
      worktrees `atelier-qr-<item>`. A brief-writer dispatched by `8e498ef1`
      saw an `atelier-qr-…` commit inside its review delta, concluded its
      own run had authored it, and refused the brief under rule 4. The
      orchestrator disproved that from git and resumed it (`180/110`). The
      refusal was the safe failure. The cost was a resumed agent and a
      record correction. Wherever a record cites a `wt:` name as provenance,
      in claims, briefs and commit bodies, the name carries no author.
      **Shape:** worktree names carry the session's short id
      (`atelier-qr-8e49-210-290`), and the claim fragment's `wt:` shows it.
      ✅ **Landed 2026-11-03.** `CONCURRENCY.md` § *Orchestrated
      queue runs*: a run's worktree names take the form
      `<repo>-qr-<id>-<slug>`, the session id's first four characters, so a
      claim's `wt:` names its session; the dispatch brief's worktree line
      carries the form. No house text named the old pattern
      (`atelier-qr-` matched nothing in `docs/method/`, `skills/` or
      `commands/`), and records were not rewritten.
      Review owed: `160/995`.
