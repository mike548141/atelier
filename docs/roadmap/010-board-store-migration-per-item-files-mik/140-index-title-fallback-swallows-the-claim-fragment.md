- [x] 🔎 **`index_title`'s fallback swallows the claim fragment into the generated
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
      ✅ **FIXED 2026-08-23**, exactly as proposed — one line, plus the reason
      written into the docstring so the next hand does not restore the naive
      fallback. Three tests: the wrapped title no longer repeats the claim
      (fails against the unfixed tool), a closed `**…**` span is unaffected,
      and the claim still reaches the *index line* — stripping it from the
      title must not strip it from the line, since the claim is what tells
      another session the item is taken. `130` is untouched and still open.
