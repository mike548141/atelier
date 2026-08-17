- [x] 🎯 **RULED 2026-08-17 — "Build a guard."** The cold-sweep exclusion
      defect has now fired **three times**: a `grep` exclusion that assumes a
      `./` path prefix `grep` does not emit, leaking rule-2 barred material to
      a reviewer mid-pass. The rule was restated after each instance, and
      restatement has measurably not worked. Offered the cheap point-of-use fix
      (a tested command in the brief template) or leaving it to disclosure,
      Mike took the strongest option.
      - [x] Build it: the correct exclusion becomes the **default** and a bare
            tree-wide grep the exception. Scope, name and plane are the
            builder's design call; tests and catalogue entry are not optional.
      - [x] Grounding, not invention: the barred set is `REVIEW.md` rule 2's,
            and the three recorded instances are its test corpus.
      - [x] First-of-kind build — queue its own rule-4 `⏳` at landing.
