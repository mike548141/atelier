- [ ] ⏳ **Rule-4 cold pass queued: the repo template scaffolds the per-item
      board (`010/240`).** Built by a worker of an orchestrated run (Opus 5.5,
      principal-opened, 2026-11-20 UTC), which queues this and does not take
      it or brief it. **Needs a brief.**
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine and template cold pass, per `method/REVIEW.md`
      rule 4.
      *Delta, scoped to paths:* `docs/build/templates/docs/ROADMAP.md`,
      `docs/build/templates/docs/roadmap/` (the legend, the starter section
      and the starter item), `docs/build/templates/docs/SESSIONS.md`,
      `docs/build/templates/docs/ARCHITECTURE.md`,
      `docs/build/templates/README.md`, `docs/build/README.md`,
      `docs/build/REPO-STANDARD.md` (the `roadmap/` bullet and both
      processes), `skills/create-repo/SKILL.md` (step 4 and the standardise
      section), `tools/test_templates.py` (`TemplateBoardTest`),
      `CHANGELOG.md`: the commit that closes `010/240`, on its worktree
      branch.
      *What to test hardest:* that a repo scaffolded from the template, by the
      skill's own steps, passes `board.py --check` and the floor with no hand
      edit; that the committed index cannot go stale against the starter
      files without a test failing; that the standardise path cannot
      overwrite an existing board or leave a one-file board in place; and
      that the child-facing legend carries nothing the full legend would
      contradict.
      *Finding prefix:* `TS` (no `TS1` under `docs/reviews/` or
      `docs/roadmap/` on 2026-11-20).
      *Intent record:*
      [`../010-board-store-migration-per-item-files-mik/240-the-repo-template-still-scaffolds-the-old-board.md`](../010-board-store-migration-per-item-files-mik/240-the-repo-template-still-scaffolds-the-old-board.md).
      No brief yet: a brief-writer this run did not start writes it. **Drain
      priority: not set by the principal; this run suggests low.**
