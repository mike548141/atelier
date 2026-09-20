- [~] (claimed 2026-09-20-2239, wt: at-harness-walk; FUNDED by Mike 2026-09-20; part 1 of 3 DONE, parts 2–3 owed) **Single-source the scanner harness, re-grounded on Mike's own upstream
      test.** The finding already exists: GA1, a minor raised by the 2026-08-05
      guards-and-allowances cold pass and still awaiting its ruling round. It
      reads that the reason-required loader is ten per-scanner copies, *"the
      propagation mechanism the build's own survey diagnosed"*, and counsels
      single-sourcing it or recording standalone copies as the decided design —
      *"either answer, not silence."* This item does not restate that finding;
      it adds the evidence that has landed since, and the test that decides it.
      **What landed since.** On 2026-08-09 the duplication produced exactly the
      defect it predicted: a shared parsing rule, copied per scanner, silently
      voided nine live allow-markers across three children. A voided marker and
      an absent one produce identical output, so it survived a review that had
      explicitly triaged one of the affected lines. The fix took fourteen regex
      sites across twelve files. Beyond the loader, the divergence is already
      real rather than latent: `datescan` requires a word boundary and a
      non-empty reason where several siblings accept a bare substring match.
      **A second gap, found while writing this section.** `plainscan` has no
      allow-marker grammar at all — no marker constant, no reason parser, no
      suppression path. So a verbatim principal quote, which must not be
      reworded, cannot be exempted from its long-sentence rule at any
      granularity. Two findings in this section's own README are exactly that
      and are left standing. Tolerable while the check is warn-only; less so
      since its repo plane was rescoped to the prose Mike reads, which is what
      board files are. A shared grammar would give it one for free.
      **The test that decides it is Mike's own** (2026-07-19, on fixing upstream
      rather than accumulating downstream mitigations): a fix is downstream when
      correcting it requires patching N separate locations and the next
      correction will require N more. Ten to eleven copies, fourteen sites, is
      that signature.
      **Scope, if funded:** one ignore-file loader, one allow-marker grammar,
      one exit and reporting contract, and namespaced finding identifiers so a
      rule stays individually suppressible. The precedent is unanimous on the
      last point — every mature engine consolidated the engine and kept the
      rules granular. **Explicitly not in scope:** merging any two guards'
      *intents*. No precedent found does that, and one suppression would then
      silence a whole concern.
      **Framing note, 2026-08-15.** This item was written in the first pass's
      breadth frame — many narrow checks versus one broad one. The build it
      asks for is unaffected and the reasoning above still holds. But the
      question it was answering was the wrong one: item `120` carries the right
      one, and this item is a consolidation of *plumbing*, not an answer about
      how guards should be organised.
      📈 **Third piece of evidence, and the largest: 2026-09-20's bounded-memory
      work copied a whole new mechanism ten times.** `020/380` converted the
      guard layer to a streamed walk and a bounded line reader — and because
      each scanner is standalone, `_walk_files` now exists as **ten separate
      definitions** (`secretscan`, `leakscan`, `conflictscan`, `linkscan`,
      `sizescan`, `datescan`, `wrapscan`, `spellscan`, `pathscan`,
      `licenscan`), with the window/overlap constants and the
      finding-materialisation cap copied alongside them in four more. That is
      not drift waiting to happen; it is the same shape as the allow-marker
      loader, at ten times the surface, written in one sitting. **Mike's own
      test applies unchanged:** the next correction to the walk — the
      gitignored-nested-worktree skip `020/160` already documents, for
      instance — is ten edits.
      🔑 **And it sharpens the scope question:** the window sizes deliberately
      *differ* per guard (256 KiB for links and headings, 4 MiB for
      credentials), so single-sourcing here means sharing the **mechanism with
      per-guard parameters**, not one constant for everyone. A shared harness
      that forces one window would be worse than the duplication.
      📈 **Fourth piece of evidence, 2026-09-20 — and it is the prediction
      coming true rather than another example of the same shape.** This item
      said in as many words that *"the next correction to the walk — the
      gitignored-nested-worktree skip `020/160` already documents, for
      instance — is ten edits."* `020/160` was built that day. It was **eleven**
      edits (`stampscan` carries a copy the earlier count missed), plus
      **eleven test files**, for a one-line change: adding
      `and not Path(dirpath, d, ".git").is_file()` to a pruning expression.
      **Twenty-two files for one line** is Mike's upstream test answered by
      demonstration, on the exact case this item nominated in advance.
      🔑 *And the divergence it warns about is now measurable rather than
      predicted:* eleven copies of a line written by one worker in one sitting
      should be byte-identical today, and whether they still are next quarter
      is the thing nobody will check. That is the drift this item exists for.
      ---
      ✅ **FUNDED by Mike, 2026-09-20.** Put to him with the counter-argument
      stated — that `115/170`'s unruled proportionality question sits upstream
      of this whole section, and that funding this adds to the layer that item
      warns about. He ruled build it. The concern is recorded, not carried
      forward as an objection.
      **Split into three landable parts, so a claim this size is never left
      half-finished** (the run's own instruction). Each part lands on `main`
      with the suite green and every scanner's output proved unchanged before
      the next begins:
      - **Part 1 — the walk and its parameters.** One `_walk_files`, with the
        per-guard window/overlap constants and the finding-materialisation cap
        passed in rather than copied. Eleven copies, written in one sitting on
        2026-09-20, so they should still be identical today — which makes this
        the lowest-risk slice and the one with the sharpest test.
      - **Part 2 — the allow-marker grammar and the ignore-file loader.** The
        original GA1 finding: fourteen regex sites across twelve files, and
        the divergence here is **already real**, not latent — `datescan`
        requires a word boundary and a non-empty reason where several siblings
        accept a bare substring. Higher risk precisely because unifying it
        changes behaviour somewhere.
      - **Part 3 — the exit and reporting contract, and namespaced finding
        identifiers** so a rule stays individually suppressible. The precedent
        is unanimous on that last point.
      🔑 **The standing constraint, from this item's own text:** share the
      **mechanism with per-guard parameters**, never one constant for
      everyone. The window sizes differ deliberately — 256 KiB for links and
      headings, 4 MiB for credentials — and a harness that forced one window
      would be worse than the duplication it replaced.
      **Explicitly not in scope, unchanged:** merging any two guards' intents.
      ---
      ✅ **PART 1 LANDED 2026-09-20 — `tools/filewalk.py`.** Eleven copies of
      `_walk_files` become one shared generator; each scanner keeps a one-line
      wrapper passing its own skip-set.
      **The difference analysis was the work, not the extraction.** Ten walk
      bodies were already byte-identical. `licenscan`'s differed in exactly one
      respect — it also prunes `dist` and `build`, because a licence check has
      no reason to inspect built output. **That is a genuine per-guard choice,
      so it stays a parameter** rather than being flattened into one shared
      constant, which would have silently changed `licenscan`'s output. Every
      other difference across the eleven was docstring prose, an incident
      citation, or a variable name (`SKIP_DIR_NAMES` vs `sizescan`'s
      `NON_CONTENT_DIR_NAMES`).
      ⚠️ **A claim this session made and now corrects.** An orchestrator hash
      of the eleven copies reported *"9 distinct variants — already diverged
      within a day"*. That measured **prose**, not logic: the hash covered
      docstrings and comments. Behaviourally, ten of eleven were identical and
      the eleventh's difference was deliberate. The correct statement is far
      weaker than the one first published — textual divergence inside a day,
      no logic drift — and it is recorded because a wrong figure that flatters
      this item's own thesis is exactly the kind this estate keeps producing.
      **Evidence:** byte-identical stdout, stderr **and exit code** for all
      eleven, old against new, over the real tree. The `020/160` linked-worktree
      skip preserved unchanged, and the standing suite already carries a
      per-scanner regression test for it — the floor, not a scratch probe.
      Suite **1,564 tests OK**, matching the baseline exactly, re-run
      independently by the orchestrator after the merge.
      🛑 **Part 1's scope as written was WRONG, and the worker was right to
      refuse it.** Both this item's text and the dispatch brief put the
      window/overlap constants and the finding-materialisation cap in part 1.
      They are not one mechanism with per-guard parameters — they are three or
      four genuinely different readers, one of which carries markdown fence
      state. Folding them would have risked the merge of distinct guards'
      intents this item forbids outright. Split to `115/220` as its own
      decision.
      📐 **Two counts in this item's own text, corrected by measurement:** the
      walk was in **eleven** files, not ten; the finding-materialisation cap is
      in **three**, not "four more".
      **Parts 2 and 3 remain owed** and the claim stands for them: part 2 the
      allow-marker grammar and ignore-file loader (where divergence is already
      *behavioural* — `datescan` requires a word boundary where siblings accept
      a bare substring), part 3 the exit/reporting contract and namespaced
      finding identifiers.
      Rule-4 `⏳` at `160/420` covers part 1; this run may not take it.

