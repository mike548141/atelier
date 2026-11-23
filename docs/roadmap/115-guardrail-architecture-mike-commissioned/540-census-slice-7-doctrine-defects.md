- [~] 🔎 **Defects the enforcement census found in slice 7.** Found
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
      *(claimed 2026-11-23 UTC, session 608d8123, wt: atelier-qr-608d-defects7; items 3–5 only)*
