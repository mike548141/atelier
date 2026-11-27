- [ ] 🔎 **Defects the enforcement census found in slice 7.** Found
      2026-11-23 UTC by `020/220` slice 7
      (`docs/method/census/2026-11-23-1813-decisions-skills-commands-plugin.md`);
      reported, not fixed in passing. The orchestrator (queue run
      608d8123) checked the first two against the tree.
      1. **`/atelier:install-hook` installs the hook untracked**, against
         ADR 0008 decision 4 ("The hook is tracked": `.githooks/pre-commit`
         plus `core.hooksPath`).
      2. **`create-repo`'s bundled-mode proof cannot pass**: it reads the
         plugin manifest's `version`, and the manifest has had no `version`
         key since 2026-10-18.
      3. **Decision-record statuses drift**: 4 of 5 `draft` records are
         already in force, and 2 use a `proposed` status the decisions
         README does not define; 3 of 8 records' review lines say "queued"
         beside a finished pass.
      4. **`/atelier:scan` runs 4 of the 21 floor checks** and calls them
         the publish-safety floor.
      5. **Lists that drift**: `session-onramp`'s companion list omits 2
         skills, both manifest descriptions omit 3; the never-list sits in
         5 places in 3 wordings, the reviewer prompt in 2.
      6. **"Owed" in two senses** between `fleet-sweep` and `REVIEW.md`
         rule 4 (named as a doubt, not a verdict).
      ✅ **Items 3–5 fixed 2026-11-23** (queue run 608d8123, a Sonnet
      worker, read by the run before landing). 3: four `draft` records
      whose own review stamps quote the principal's acceptance and whose
      rules are built are `accepted`, each with a dated addendum naming the
      evidence; the two `proposed` are `draft` (open designs); the
      exception register stays `draft` (its re-review and ruling are
      owed); four review lines that said "queued" beside a finished pass
      now say it ran. 4: `/atelier:scan` and the root README say it runs
      four of the floor's scanners and point at `tools/floor.py`; what it
      runs is unchanged. 5: `session-onramp`'s companion list and both
      manifest descriptions name all six skills and four commands. Seen,
      not unified (a wording choice): the never-list's five forms and the
      reviewer prompt's two, places listed in the worker's report and
      the census rows. Cold pass queued as `160/1770`. **Still open:** 1
      (install-hook untracked against ADR 0008), 2 (the manifest has no
      `version` for `create-repo`'s proof), 6, and the never-list wording.

      **Round 2, 2026-11-27 UTC** (queue run 9c5fa72c, a Sonnet worker, read by
      the run before landing). Each numbered defect was checked against the tree.
      **1 fixed:** `/atelier:repo hook` now installs the tracked form, as ADR
      0008 decision 4 and `repo create` step 6 say: it copies `.githooks/`'s
      three hooks into the repo, sets `core.hooksPath .githooks`, tells the user
      to commit `.githooks/`, and says why `.git/hooks/` is the wrong home. It
      had copied the `tools/*.sample` files into git's own hooks directory.
      Reproduced first by `test_subject_skills.py`
      `test_repo_hook_installs_the_tracked_form`, which failed; it passes now.
      The root README's `hook` bullet and `tools/README.md`'s wiring bullet
      said the untracked form and now say the tracked one. **6 already fixed**
      by `10b32435` (the review plan holds the one definition of *owed*, a `⏳`
      pointer that names a delta included; `fleet/sweep.md` item 4 defers to it
      and restates nothing; no "bare ⏳ does not count" text is left). **5, the
      rest, fixed:** the reviewer prompt's two homes were already one
      (`test_the_reviewer_instructions_have_one_home`, DV8); the never-list is
      now one text in the four fleet prompts (the stricter list wins, as the
      layer-override rule says: the adopt prompt gained the record-store
      examples, the brief prompt gained five clauses), the sweep's *Limits paid
      for* line names the full set, and
      `test_the_never_list_is_one_text_in_every_fleet_prompt` pins it (it failed
      first on adopt and brief). The review-only first clause of the brief
      prompt stays its own.
      **Left for the principal: 2** (`create-repo`'s bundled-mode proof and
      `<VERSION>`). The manifest has no `version` on his 2026-10-18 pick
      ("Track every commit"), and `PROPAGATION.md` says putting one back is his
      call. The other way, changing the canonical bundled-mode text so the pin's
      referent is something else (the installed commit, or the `CHANGELOG.md`
      head), rewrites text stamped into every bundled child and rests on how
      Claude Code names an install directory for a plugin with no `version`,
      which this tree cannot show (the one local cache entry predates the
      change). So which side moves is his; the question and a recommendation are
      in the run's report. Items 3 and 4 and the rest of 5 stand as before.
      review: not warranted — item 1 syncs a command's text to a decision already
      accepted (ADR 0008 decision 4) and to the step `repo create` already
      carries; its failure is loud (the step's own proof runs `deadhook.py
      --status`, which exits 1 when commits would go unscanned, and a test pins
      the tracked form); item 5 syncs three copies of a list to the fuller text
      already in force in the worker and task prompts, a tightening whose failure
      (a worker stops and reports) is loud and whose parity a test now reds on.
