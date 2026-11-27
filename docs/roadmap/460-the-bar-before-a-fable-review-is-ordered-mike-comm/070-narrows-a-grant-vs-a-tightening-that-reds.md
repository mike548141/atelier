- [x] 🔎 **The bar decides a least-privilege change both ways: "it narrows a grant" owes
      🔒 Claimed by session 9c5fa72c (`atelier-fa`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-27-0915, wt: atelier-qr-9c5f-reviewbar)
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
      ✅ **Done 2026-11-27 (session 9c5fa72c, `atelier-fa`, an Opus worker).** `REVIEW.md`
      § *Whether work earns a review at all* gains *A narrowing is judged both ways it can be
      wrong*: the author names both failures, **too tight** (refuses what it should allow) and
      **not holding** (allows what it claims to stop, or a narrowed detection misses a true
      case); both loud is the never list's, either silent answers question 3. The item's
      reading is kept as the not-holding half, widened to the grant that stays wider than
      claimed, which `460/050` already calls a security hole. Question 3 points at it;
      `skills/review/brief.md`'s compressed copy and `CHANGELOG.md` follow. Grounded in
      `tools/test_leakscan.py`'s "both directions pinned" rule for a tightening. Under it
      `160/1760` keeps its pass: its test pins only the workflow-level block, and a job's own
      `permissions:` can widen it, so the not-holding way is silent.
      - Commitment: every session's verdict on whether a least-privilege change owes a pass.
      - Worst failure: the test calls a narrowing loud when one way it can be wrong is silent,
        so a grant that still holds more than it claims goes unreviewed.
      - Why the floor misses it: no test reads what doctrine means.
      **Review:** folds into `160/1880` (open, unbriefed, same section); its delta is widened
      to this commit.
