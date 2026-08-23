- [ ] 🎭 **The sixth instance is the checker written to enforce this item, and it
      failed the same way within the hour.** Recorded because it is the most
      self-incriminating evidence available that this class is not a matter of
      carelessness — the author was holding the rule in mind and shipped the
      defect anyway.
  - [ ] **What it was for.** `010` says: where an action is irreversible, a
        tool's own report is not sufficient evidence — corroborate from the
        artefacts. In docker-heap that means never taking the split tool's `✅`
        as grounds for deleting an original, and instead re-deriving the verdict
        from the five manifests on disk. A short shell loop was written to do
        exactly that.
  - [ ] 🛑 **What it actually did.** The loop was:

        ```sh
        s=$(sha256sum /w/src.$m | cut -d' ' -f1)
        d=$(sha256sum /w/dst.$m | cut -d' ' -f1)
        [ "$s" = "$d" ] && v=IDENTICAL
        ```

        With the manifest **absent**, `sha256sum` wrote to stderr and `s` came
        back empty. So did `d`. Empty equalled empty, and it printed
        **`IDENTICAL`** for a dimension it had never read. It ran clean against
        one folder — where the file happened to exist — and only exposed itself
        on the next folder, whose `ownmt` manifest had not been generated yet
        because that dimension is produced by `attest` rather than `verify`.
  - [ ] 🔑 **The sentence again, third noun.** *A verification that cannot
        display the passing state is not a verification* · *a guard that cannot
        recognise the state it exists to detect is not a guard* · **a check that
        cannot distinguish "the same" from "nothing at all" is not a check.**
        Absence and equality are different findings and must never print the
        same word.
  - [ ] ✅ **The fix, and the test that proves the fix.** Existence is now
        asserted before any comparison, an empty digest is its own failure mode,
        and a missing manifest prints `🛑 UNPROVEN` with a non-zero exit rather
        than a verdict. **It was then run against a deliberately broken fixture
        first** — one dimension differing, one matching, three absent — to prove
        it can *display* all three states before it was trusted with a real one.
        That negative test is the cheap generalisable part: an instrument gets
        one run against a known-bad input before its output means anything.
        ⚠️ Note the asymmetry it fixes: a legitimately **empty** manifest is
        fine and common (a tree with no symlinks yields a zero-line `links`
        manifest whose digest is the well-known `e3b0c442…` empty-input value).
        Empty is a result. Absent is not.
  - [ ] 🎯 **What follows, if anything.** The candidate practice is narrower than
        "test your tools": **any check whose output can authorise an
        irreversible act gets one run against a known-bad fixture before it is
        believed.** Cheap, mechanical, and it would have caught this one, the
        gateway filter in the table above, and the guard in `020`.
  - [ ] 📄 **Provenance.** docker-heap, 2026-08-23, found when the loop reported
        `IDENTICAL` for `ownmt` while `sha256sum` was printing
        `can't open '/w/src.ownmt'` two lines above it in the same output. The
        affected verdicts were re-run with the fixed checker and re-established
        rather than assumed to have been right — they had been right, which is
        luck and was not treated as evidence.
