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
