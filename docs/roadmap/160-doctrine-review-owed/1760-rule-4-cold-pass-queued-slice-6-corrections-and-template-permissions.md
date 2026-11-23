- [ ] ⏳ **Rule-4 cold pass queued: least-privilege permissions in the CI
      templates, and the slice-6 doctrine corrections (`115/530` items
      1–4, 6).** What every new child copies changed, a test now pins it,
      and four doctrine files were restated against the tree, so it earns
      its own pass. The authoring session (608d8123, Opus 5.5, a
      principal-opened queue run, 2026-11-23 UTC, whose worker wrote the
      change) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine and code cold pass, per `method/REVIEW.md`
      rule 4.
      *Delta, scoped to paths:*
      `docs/build/templates/workflows/ci-python.yml`,
      `docs/build/templates/workflows/ci-static.yml`,
      `tools/test_templates.py` (`WorkflowLeastPrivilegeTest`),
      `docs/build/README.md`, `docs/build/REPO-STANDARD.md`,
      `SECURITY.md`, `README.md`: the four commits citing `115/530`, on
      `main`.
      *Intent record:*
      [`../115-guardrail-architecture-mike-commissioned/530-census-slice-6-doctrine-defects.md`](../115-guardrail-architecture-mike-commissioned/530-census-slice-6-doctrine-defects.md).
      *What to test hardest:* that no job in either template needs a
      wider token than `contents: read`; that the new test's exact-block
      match cannot pass a workflow that widens a job's own permissions;
      that each restated sentence is true against the tree.
      *Approval:* none yet; owed to the principal before the pass runs.
      💬 **Answered 2026-11-23 ~19:20 UTC (session 608d8123, AskUserQuestion), his pick:** *"Next drain (Recommended)"*:
      this pass and the other three of run 608d8123 (`160/1740`–`1770`)
      wait for his next weekly drain.
