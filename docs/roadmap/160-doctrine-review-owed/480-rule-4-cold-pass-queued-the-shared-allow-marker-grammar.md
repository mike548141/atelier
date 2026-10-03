- ⏳ **Rule-4 cold pass queued: the shared allow-marker grammar and ignore
      loader (`115/080` part 2).** The run authored this itself (its
      dispatched workers' output counts as the run's authorship). It was
      queued at landing, and the run neither takes it nor spawns a reviewer
      for it. *Tier:* Fable, the principal-named review tier, checked at
      selection. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/allowmarker.py` and
      `tools/test_allowmarker.py` (both new), and the marker and ignore-file
      code in `tools/{blockscan,conflictscan,datescan,leakscan,licenscan,`
      `linkscan,pathscan,pointerscan,reviewscan,secretscan,sizescan,`
      `spellscan,stampscan,wrapscan}.py`. It landed on `main` on 2026-10-03,
      in merge `5d087ec`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-03 0357 UTC for the review run** (wt:
      `atelier-review-430`, branch `review-430-1003`; brief
      `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`)
      by a Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any
      other work dependent on fable") that authored none of the delta and was
      not started or instructed by the authoring run. Shape, disclosed per rule
      4: reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree
      and outside the harness scratchpad; a fresh Fable subagent it spawns forms
      every finding and severity. Disclosed exposure: the authoring run told
      this session, over the cross-session channel, that the pointer existed
      and named its subject in a phrase; nothing else from it was read. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and
      exposure go in the verdict.
