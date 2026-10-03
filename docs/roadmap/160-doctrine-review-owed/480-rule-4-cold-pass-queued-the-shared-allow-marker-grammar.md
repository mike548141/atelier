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
