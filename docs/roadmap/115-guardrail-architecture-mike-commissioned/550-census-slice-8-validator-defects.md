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
