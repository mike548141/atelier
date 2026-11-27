- [ ] 🔎 **Defects the enforcement census found in slice 8, in the
      validators' own stated contracts.** Found 2026-11-23 UTC by
      `020/220` slice 8
      (`docs/method/census/2026-11-23-1836-validators-personal-data-roadmap-summary.md`);
      reported, not fixed in passing. The orchestrator (queue run
      608d8123) checked item 7 against the tree.
      1. **The floor renders four checks as enforced that cannot block
         yet**: `attribscan`, `pdlistscan`, `namescan` and `quotescan`
         each sit in a dated warning period. Seen live this run: a
         personal-data string reached `main` through a green hook and
         went red only in CI's unit tests.
      2. **`datescan`'s registry `why` says "never a drifting today"**,
         while a bare "today" passes by design and a test pins that.
      3. **`tools/README.md` says a passing `--selftest` prints `selftest
         OK — <scanner>`**; 9 of 21 print another form.
      4. **The `licenscan` README says "not the per-commit hook"**; the
         registry runs it there for any repo that declares a licence.
      5. **Slice 2's `AUT14` row and the `115/110` headline are stale**:
         `quotescan` has read edits to the agent's own grant since
         2026-11-17, advisory only.
      6. **The README calls `harvestscan`, `pointerscan` and `pathscan`
         "advisory only"**, the floor's word for a child's softening, not
         for the parent's warn-only wiring.
      7. **`instruments/README.md` contradicts itself on `ccarchive
         --install-schedule`**: one place says it installs a schedule on
         request, another that it refuses the flag family; the code and
         tests accept it.
      8. **Atelier has no `docs/reviews/README.md`**, though the template
         ships one.

      **Progress 2026-11-27 (queue run `atelier-b2`, worker branch
      `qr-a209-census8`).** Each defect re-read against the tree first; item
      numbers are this list's.
      1. **Not done, by design of the item: owed to the principal.** Still true:
         `floor.py --list` prints `attribscan` and `pdlistscan` `enforced`, and
         `namescan`/`quotescan` render enforced on the msg plane. The three-state
         render (`Scanner.warns_only`, 2026-08-04) exists but derives only from a
         `--warn` flag or `warn_only=True`, and `test_floor`'s selftest pins
         `warn_only` to "advisory form equals hook form" in both directions; a
         dated warning period that then blocks is neither, so none of the four
         can be marked with an existing state. It needs a fourth state ("warns
         until `<date>`, then blocks") read from the scanner's own constant or a
         registry field, which changes what every child's board prints. Not
         built; question below.
      2. **Fixed.** `floor.py` `datescan` `why` now reads "records date in
         absolute UTC: no relative-time word where a date is meant (a bare
         'today' with no date cue passes by design)".
      3. **Fixed as text.** `tools/README.md`'s opening says the shared form
         `selftest OK — <scanner>` is printed by 13 of the 22 registry scanners
         (22 now, not 21; 9 still differ, the same nine) and names the three
         other forms and who prints them. The nine are not normalised: that
         would be a behaviour change and no ruling asks for it.
      4. **Fixed as text.** `tools/README.md` (`licenscan` section) and the
         `licenscan.py` docstring say it is pre-publish by purpose and opt-in in
         the floor: it runs, blocking, on the hook and CI where a repo declares
         a `licence`, and is skipped on both planes where none is declared.
      5. **Fixed as dated notes, no history rewritten.** Slice 2's census
         (`2026-11-16-1204-apex-autonomy-guards-propagation.md`) carries an
         update note after the autonomy table (`AUT14` enforced, partial, warns;
         `AUT15` partly read); `115/110` carries a dated note that its headline
         is the 2026-08-15 finding and the Progress note is current state.
      6. **Fixed.** `tools/README.md` headings for `harvestscan`, `pointerscan`
         and `pathscan` now read "(warn-only)", the floor's word for the
         parent's own report-only wiring.
      7. **Fixed.** `instruments/README.md`'s *Run by hand* bullet now matches
         its install section, the code and `ccarchive.test.js`: no schedule
         unless asked; `--install-schedule` sets a calendar one (`210/230`, the
         principal's ruling of 2026-10-05).
      8. **Fixed.** Atelier now carries `docs/reviews/README.md`: it is the
         pattern of its sibling `docs/sessions/README.md` and
         `docs/decisions/README.md`, `REPO-STANDARD.md` lists `reviews/` in the
         file set, the template's CONTRIBUTING link and `create.md`'s check name
         it. Adapted, not copied: a map of what the folder holds (briefs,
         `.deferred.md` siblings, `withdrawn/`, `drafts/`), pointing at
         `REVIEW.md` and restating none of it. The census's section is left
         as recorded and carries a dated update note.

      **Question for the principal (item 1).** Should a check in a dated warning
      period render as its own fourth state on the board (for example "warns
      until 2027-02-08"), with the date read from the scanner so it cannot
      drift from the code? Option A, build it: the board stops claiming a gate
      that cannot block, and the date is visible in every child's output; cost:
      a registry field or a read of each scanner's constant, a test that every
      `*_UNTIL` constant is carried (the census's third tripwire), and a changed
      render on every child's board. Option B, only relabel the four as
      `warn-only` until their dates: smallest change, but it says "can never
      block", which is false after the date, and someone must remember to flip
      it. Recommendation: A. Until then a personal-data string can pass a green
      hook, as seen.

      review: not warranted — items 2 to 7 are wording and factual corrections
      that add or change no rule, 5 is a dated note on records, and 8 is a map
      of a folder that restates no doctrine; the text fixes are what the code
      and tests already do. Item 1, when built, changes what binds on the
      board and will answer `Commitment:` / `Worst failure:` / `Why the floor
      misses it:` then.
      *Claim released 2026-11-27 at the close of session a2097e54 (`atelier-b2`): items 2 to 8
      are landed; item 1 waits on the principal's answer to the question above.*
      **His answer to item 1, 2026-11-27 ~23:55 UTC** (question device, session
      a2097e54 `atelier-b2`; the options and recommendation were the session's; an
      answer, not a ruling), his pick verbatim: *"Add the label (Recommended)"*. The
      option read: the board shows each as "warns until <date>", the date read from the
      guard itself so it cannot drift; a small build plus a test; every child's board
      output changes; one cold review owed. **Item 1 is now buildable** by any session.

