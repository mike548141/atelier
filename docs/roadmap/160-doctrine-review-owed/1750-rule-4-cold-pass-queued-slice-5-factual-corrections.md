- [x] **Rule-4 cold pass queued: the slice-5 census corrections, five
      doctrine statements and `signscan`'s coverage line (`115/510` items
      1, 3–6).** Doctrine text changed, one change restates the signing
      plane's status, and a guard's output changed shape, so it earns its
      own pass. The authoring session (608d8123, Opus 5.5, a
      principal-opened queue run, 2026-11-23 UTC, whose worker wrote the
      change) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine and code cold pass, per `method/REVIEW.md`
      rule 4.
      *Delta, scoped to paths:* `tools/signscan.py`,
      `tools/test_signscan.py`, `docs/method/TOOLBOX.md`,
      `docs/method/SIGNING.md`, `docs/method/README.md`,
      `docs/method/STORAGE.md`, `docs/method/session-open/README.md`: the
      four commits citing `115/510`, on `main`.
      *Intent record:*
      [`../115-guardrail-architecture-mike-commissioned/510-census-slice-5-doctrine-defects.md`](../115-guardrail-architecture-mike-commissioned/510-census-slice-5-doctrine-defects.md).
      *What to test hardest:* that each corrected statement is true
      against the tree and history it describes, the signing status
      above all; that `signscan`'s `--json` stays compatible for a child
      reading `signatures_verified`; that each new TOOLBOX row matches the
      instrument's own help.
      *Approval:* none yet; owed to the principal before the pass runs.
      💬 **Answered 2026-11-23 ~19:20 UTC (session 608d8123, AskUserQuestion), his pick:** *"Next drain (Recommended)"*:
      this pass and the other three of run 608d8123 (`160/1740`–`1770`)
      wait for his next weekly drain.
      **Dequeued 2026-11-27 ~01:55 UTC (board `460/040`; session 4ce066ba, `atelier-c1`,
      AskUserQuestion; an answer to options Claude wrote, not a ruling), not run.** His pick,
      verbatim: *"Drop 8, merge 6 (Recommended)"* (option text: *"31 reviews stay in Monday's
      drain. Takes back your earlier picks on 4 of them. Saves roughly 8 Fable passes of
      budget; the 6 merged ones still get reviewed, just together."*). Under the bar in
      `method/REVIEW.md` § *Whether work earns a review at all*, this is factual corrections
      that add or change no rule, and one output line on `signscan`, a reviewed tool its tests
      cover. This takes back his earlier pick on this pass, *"Next drain (Recommended)"*
      (2026-11-23 ~19:20 UTC, recorded above); the option text he chose on 2026-11-27 says so.
      review: not warranted — factual corrections and an output line its tests cover
