- [ ] 🔎 **The bar decides a least-privilege change both ways: "it narrows a grant" owes
      a pass, "a tightening that reds on misuse" never does** `[S][doctrine]`. Found
      2026-11-27 by the `460/040` dequeue round (session 4ce066ba), judging `160/1760`.
      `REVIEW.md` § *Whether work earns a review at all* lists, under question 3, "it
      narrows a grant" as an answer that earns a pass; its never-a-pass-of-its-own list
      names "a tightening that reds on misuse" to an already-reviewed tool. Cutting a CI
      token's permissions is both: it narrows a grant, and if it is too tight the job
      reds loudly. So two sessions applying the same text can reach opposite verdicts.
      **Owed:** say which wins. One reading that fits both lists: a narrowing whose
      failure is loud (a job reds) is the never-list's; a narrowing whose failure is
      silent (something still passes but no longer checks what it did) is question 3's.
      The text is doctrine, so the change takes its own review line under the bar.
      **Not fixed in passing:** filed under `CLAUDE.md`'s rule that a doctrine defect is
      reported, not quietly patched.
