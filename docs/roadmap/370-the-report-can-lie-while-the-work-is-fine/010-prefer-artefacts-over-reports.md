- [ ] 🎯 **Decide whether "prefer artefacts over reports" earns a line, and where.**
      The three mechanisms below are each worth a sentence in passing; the
      generalisation is the part that might be doctrine.
  - [ ] **The candidate rule, stated tightly enough to be checkable:**
        **where an action is irreversible, a tool's own report is not sufficient
        evidence for it — corroborate from the artefacts.** Narrow on purpose. A
        rule that said "distrust your tools" would be ignored within a day, and
        should be.
  - [ ] **One line prevents the nastiest mechanism**, and it is worth having
        whether or not the rule above lands: **never overwrite an executable that
        a running invocation is reading.** Write to a new path and rename over it,
        or version the filename. Bash reads a script by byte offset; replacing it
        underneath makes execution resume at an offset that now lands mid-token,
        and the process keeps going and keeps printing.
  - [ ] 🔎 **Where it likely lives.** This is a *how we work* rule rather than a
        floor — it stops nothing catching fire on its own, but the case it guards
        is a 348 GB deletion authorised by a corrupted `✅`. Worth deciding
        alongside `350`, since both are the apex rule applied to a place it is not
        usually applied: `350` to the strength of a check, this to the trustworthiness
        of the report of one.
  - [ ] ⚠️ **Do not reach for a mechanical check.** There is no grep for "this
        output came from a corrupted process". The only mechanical piece worth
        anything is the write-then-rename convention, and that belongs in whatever
        governs how tools are written rather than in a scanner.
  - [ ] 🔑 **Carry the provenance, because it is what makes the case.** All three
        instances came from one session, and two of them were found only because
        the owner asked for evidence he could check rather than accepting a
        verdict. **The check that caught the false `✅` was re-deriving the result
        from the manifests on disk — five digests recomputed and the raw diffs
        re-run — instead of reading the run's own summary.** The two agreed. They
        did not have to, and the whole item exists because of the gap between
        those two sentences.
