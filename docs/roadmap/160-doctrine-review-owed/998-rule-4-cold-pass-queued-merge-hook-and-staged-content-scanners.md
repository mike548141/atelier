- [ ] ⏳ **Rule-4 cold pass queued: the `pre-merge-commit` hook, the repo-local
      seam documentation, and `spellscan` / `wrapscan` reading the staged index
      (`115/340`, `320/560`, `320/600` first slice).** The merge hook and the
      two scanners reach every child's hook plane and next CI run, and
      `GUARDS.md` gained a section, so the authoring session (a principal-opened
      Opus 5.5 queue run, session 4c65083c, 2026-11-03, which dispatched the
      Sonnet worker that wrote the code) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4,
      since `docs/method/GUARDS.md` changed.
      *Delta, scoped to paths:* `tools/pre-merge-commit.sample`,
      `.githooks/pre-merge-commit`, `.githooks/pre-commit`,
      `tools/pre-commit.sample`, `tools/test_precommit.py`, `tools/report.py`,
      `tools/spellscan.py`, `tools/test_spellscan.py`, `tools/wrapscan.py`,
      `tools/test_wrapscan.py`, `tools/floor.py`, `tools/README.md`,
      `docs/method/GUARDS.md`, `commands/install-hook.md`,
      `skills/create-repo/SKILL.md`, `CHANGELOG.md` (commits `b5e6ead`, `625f29a`
      and `7673da1`, on `main`, 2026-11-03).
      *Intent records:*
      [`../115-guardrail-architecture-mike-commissioned/340-merges-cherry-picks-and-rebases-skip-the-hook-plane.md`](../115-guardrail-architecture-mike-commissioned/340-merges-cherry-picks-and-rebases-skip-the-hook-plane.md),
      [`../320-child-filed-findings-via-pointing-up/560-the-repo-local-check-seam-is-absent-from-the-readme-and-method-docs.md`](../320-child-filed-findings-via-pointing-up/560-the-repo-local-check-seam-is-absent-from-the-readme-and-method-docs.md),
      [`../320-child-filed-findings-via-pointing-up/600-the-hook-plane-content-scanners-read-the-working-tree-not-the-staged-index.md`](../320-child-filed-findings-via-pointing-up/600-the-hook-plane-content-scanners-read-the-working-tree-not-the-staged-index.md).
