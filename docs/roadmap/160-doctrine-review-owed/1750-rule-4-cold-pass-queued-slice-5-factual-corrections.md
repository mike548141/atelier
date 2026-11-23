- [ ] ⏳ **Rule-4 cold pass queued: the slice-5 census corrections, five
      doctrine statements and `signscan`'s coverage line (`115/510` items
      1, 3–6).** Doctrine text changed, one change restates the signing
      plane's status, and a guard's output changed shape, so it earns its
      own pass. The authoring session (608d8123, Opus 5.5, a
      principal-opened queue run, 2026-11-23 UTC, whose worker wrote the
      change) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine and code cold pass, per `method/REVIEW.md`
      rule 4.
      *Delta, scoped to paths:* `tools/signscan.py`,
      `tools/test_signscan.py`, `docs/method/TOOLBOX.md`,
      `docs/method/SIGNING.md`, `docs/method/README.md`,
      `docs/method/STORAGE.md`, `docs/method/session-open/README.md`: the
      four commits citing `115/510`, on `main`.
      *Intent record:*
      [`../115-guardrail-architecture-mike-commissioned/510-census-slice-5-doctrine-defects.md`](../115-guardrail-architecture-mike-commissioned/510-census-slice-5-doctrine-defects.md).
      *What to test hardest:* that each corrected statement is true
      against the tree and history it describes, the signing status
      above all; that `signscan`'s `--json` stays compatible for a child
      reading `signatures_verified`; that each new TOOLBOX row matches the
      instrument's own help.
      *Approval:* none yet; owed to the principal before the pass runs.
      💬 **Answered 2026-11-23 ~19:20 UTC (session 608d8123, AskUserQuestion), his pick:** *"Next drain (Recommended)"*:
      this pass and the other three of run 608d8123 (`160/1740`–`1770`)
      wait for his next weekly drain.
