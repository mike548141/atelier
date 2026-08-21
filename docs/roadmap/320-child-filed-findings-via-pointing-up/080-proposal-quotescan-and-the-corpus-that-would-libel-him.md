- [ ] 🎯 **PROPOSAL — `quotescan`: check quotations attributed to the principal
      against the transcript corpus** `[M][tools][docs]` — filed from `cbom`
      2026-08-19/21 via § *Pointing up* (its board `120/080`), on Mike's
      direction: *"Suggest it to atelier repo for doctrine + guards"*.
      **The gap it closes.** `RECORD.md` § *An approval is not the whole ruling*
      already rules that *"Capture is the approver's word, not the recorder's
      summary… because a paraphrase of an objection is an objection you have
      already started to answer."* Nothing checks it. `COMMUNICATION.md` supplies
      the test for whether that is acceptable, in its own words: *"a doc that
      claims write-time discipline is the only available one should first check
      whether the rule is machine-decidable."*
      **It is machine-decidable.** Read only quotations **explicitly attributed
      to the principal**, normalise whitespace and punctuation, match against the
      corpus. Verbatim ⇒ pass. Long-window match ⇒ pass **as
      paraphrase-at-source**, and label it — which is the distinction `RECORD.md`
      wants and no repo currently makes.
      **Its declaration (`GUARDS.md` fourth requirement): it forbids the act.**
      An untraceable quotation does not land. There is no cheap recovery: once it
      is in the record, later sessions build on it, and the principal ends up
      reading his own supposed words back and having to remember whether he said
      them.
      🛑 **The corpus is not an implementation detail — it IS the guard.** Built
      on the obvious corpus, this scanner **accuses the principal of fabricating
      his own instructions**. The filer's first pass flagged **51 quotations as
      unverifiable**, and the list included every one of the nineteen mid-turn
      commissions that define its repo's scope. Had it run as a blocking check,
      the indicated remedy would have been to **delete his real instructions from
      the record as fabrications** — with a floor check's authority behind it. So
      the three-channel rule (`320/070`) must land in the **same commit** as the
      scanner, never after it.
      **Two more implementation hazards, both measured by the filer, not
      theorised.** (1) A file a session *reads* lands in the transcript as a
      `tool_result`, so a naive corpus **self-verifies any quote already
      committed** — the corpus must be built from principal-authored channels
      only; the filer hit this and rebuilt. (2) A loose regex over every
      `*"…"*` returned **115 findings, nearly all false** — the repo quoting
      standards, its own report strings, its own prose. At that noise level it
      joins the ignored pile (`pathscan` 61, `plainscan` 1,390 in that child),
      which is the exact failure `GUARDS.md` names. Attribution-anchored
      matching only.
      **Offered with it:** the filer has a working extractor and a
      26-transcript corpus with known-good answers, offered as a test fixture.
      **Not verified here:** the 51-finding and 115-finding counts are the
      child's measurements of its own repo, recorded as reported. The corpus
      mechanism behind them **is** reproduced at the parent — see `320/070` and
      `210/100`.
