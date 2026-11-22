- [ ] 🎯 **Rule-4 cold pass queued: a voided allow-marker is noted (`110/010`), and a review file's `board:` and dated `Status:` lines, warn-only (`320/440`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/allowmarker.py`, `tools/reviewscan.py`, their tests, `skills/review-brief/SKILL.md`, the reviews template, `tools/README.md`, `docs/method/REVIEW.md` step 5, `CHANGELOG.md` — the commit that closes `110/010`, on `main`.
      *Questions worth the pass's time:* whether the note can fire on a marker that is working; whether the boundary lets a backdated file escape the warning.
      *Intent record:* `110/010`, `320/440`.
      📝 BRIEF WRITTEN 2026-11-14 by session 64377cac (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.md`,
      with its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 2026-11-22T22:47Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session 1cdcd5c7 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-22T23:17Z: PASS RAN, both acts, Fable 5.1 reviewer spawned by
      orchestrator 1cdcd5c7 for drain session eca14b23 (neither forms a
      finding). Verdict **PASS-WITH-FINDINGS, 0 MAJOR / 3 MODERATE / 2 minor
      / 1 note** (`VH1`–`VH6`); no MAJOR stands, and the reconcile changed no
      severity. MODERATE: `VH1`, the unparseable-marker note echoes up to 40
      characters of a secret glued to the marker (a token written as the
      scope), the opposite of what the docstring, `tools/README.md` and the
      changelog say; `VH2`, the note names no file, line or count and reaches
      no machine reader, so the motivating incident would print one
      unlocatable line per repo; `VH3`, bears on blocking: check 3's boundary
      is the filename date the writer chooses, so an undated or backdated
      review file escapes on both planes and nothing enforces review-file
      names. Minor: `VH4` header-reader tolerance gaps; `VH5` in CI the
      warn-only output sits collapsed on a green step, and this tree prints
      six false notes. Note `VH6`, the two-line grammar has six homes.
      Confirmed sound: no note on 19 working-marker shapes, no result or exit
      status moved on either plane, all four recorded proofs reproduce.
      🎯 **Owed to him (rule 3, every finding is his):** (1) `VH1`, cut the
      note's head so a glued token can't print (counsel: cut at the second
      colon as the malformed warning does, plus a glued-token test); (2)
      `VH2`, give the note a count in the scanner's summary and its heads in
      `--json` (counsel: the one-line count first, file-and-line later); (3)
      `VH3`, before check 3 ever blocks, treat a staged added review file as
      new whatever its name and warn on a review file whose name breaks the
      template's rule (counsel: yes); (4) bulk-approve `VH4`–`VH5` as one
      application commit, `VH6` for awareness. Recommendation: approve all
      four, `VH1` first. *Routing:* an application session in this repo
      after his word; its diff earns its own cold pass. `VH1` also bears on
      the later widening `2b8bcd92` (item `160/1550`), whose pass should
      carry it forward. Verdict, folded sibling and review log:
      `docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.md`.
