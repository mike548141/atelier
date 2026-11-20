- [x] **A reason that opens with punctuation does not count as a reason.**
      `ALLOW_RX` ends `:[ \t]*(?P<reason>\w)`, so the first non-space character
      after the colon must be a word character. A marker written as
      `spellscan:allow: 'PKI Center' is a company name` — reason first word in
      quotes — parses as a **mention, not an exemption** (`parse_allow` returns
      `None`), and the line starts blocking. Found live in a child repo, on two
      markers that had been exempting correctly for weeks and stopped without
      anyone touching them; the child's next commit failed an enforced gate on
      lines it had not edited. Worked around there by reordering the reason to
      lead with a word; the class itself is unfixed and every child inherits it.
      🔎 **Two things make this worse than a cosmetic nit.** It is **silent** —
      a voided marker produces a *finding*, never "your marker did not parse",
      so the failure presents as a spelling error rather than a grammar
      rejection, and the obvious response is to reword the *prose*. And a quoted
      proper noun is the **single most likely** way to open a spellscan reason,
      because the reason nearly always names the term being allowed — so the
      false-negative concentrates exactly where the marker is most used.
      🤔 **Open question, the reason the fix is not obvious:** rule (c) of
      `method/GUARDS.md` wants a *stated* reason, and `\w` is a cheap proxy for
      "something was written". Widening to `\S` admits `-` or `.` as a reason.
      A narrower fix — accept an opening quote, or require *n* word characters
      anywhere in the remainder — keeps the intent and drops the false negative.
      ⚠️ **Check the sibling scanners before fixing one.** Ten loaders share this
      grammar and two of them (`datescan`, `pathscan`) already had their reason
      character class corrected once; whether the rest carry the same edge is
      unverified, and a one-scanner fix would leave the estate inconsistent.
