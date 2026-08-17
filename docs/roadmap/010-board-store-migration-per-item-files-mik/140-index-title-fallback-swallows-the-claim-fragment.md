- [ ] 🔎 **`index_title`'s fallback swallows the claim fragment into the generated
      title, so a claimed item whose bold title wraps renders `(claimed …)`
      twice** — reported by a child over the peer channel 2026-08-17,
      reproduced here against `tools/board.py` at HEAD. `TITLE_RE` wants a
      closed `**…**` span on the state line; many real item files wrap the
      bold title across lines, so the state line carries an opening `**` and no
      closing one, `index_title` falls back to the first 70 characters of
      `rest`, and `rest` begins with the claim. Live shape (title invented):
      `- [~] 🔥 (claimed …, wt: x) [(claimed …, wt: x) Some long title — the…](…)`.
      🎯 Cheapest fix, as the child proposed: strip `CLAIM_RE` in the fallback
      path of `index_title` (one line; `index_line` already surfaces the claim
      separately). Kills this outright; does nothing for `130`.
