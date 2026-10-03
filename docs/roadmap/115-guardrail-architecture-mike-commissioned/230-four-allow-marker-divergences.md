- [ ] 🔎 **Single-sourcing the allow-marker grammar surfaced four
      divergences, and one of them widens an exemption** `[S][tools]`. Found
      2026-10-03 by `080` part 2, which preserved every one of them on
      purpose, because unifying is a behaviour change and needs a decision.
      Each is now one parameter in `tools/allowmarker.py`, so any fix is a
      one-place edit with a pinned test.
      1. 🚩 **A scope with no reason exempts more, not less.** For a scoped
         scanner, `datescan:allow:relative-time` with nothing after it
         backtracks to the *unscoped* form, reads `relative-time` as the
         reason, and returns scope `""`, which exempts every kind on the
         line. The same happens with `leakscan:allow:email,local-term` and
         `x:allow:a,b: why`. That contradicts the stated rule that a marker
         with no reason does not exempt. `test_allowmarker.py` pins the
         behaviour as **existing, not endorsed**.
      2. **Unscoped scanners accept scoped spellings.** `conflictscan` and
         `wrapscan` read `conflictscan:allow:anything: why` as a valid
         marker, because everything after the colon is "the reason".
      3. **Two separator rules.** `datescan` and `pathscan` each carry a
         scoped regex (`[ \t]*`) and an unscoped one (`\s*`). `stampscan`
         and `blockscan` use `\s*`. They differ only when the reason sits on
         the next line. The two `\s*` regexes are unused in code
         (`datescan`'s appears only in tests).
      4. **Docstring drift.** Several scanner docstrings still describe the
         bare-substring acceptance the 2026-08-05 tightening retired (e.g.
         `datescan`'s DSR8 comment).
      Item 1 is the one with consequence: a malformed marker silently
      widens. Closing it would void any live marker written in that shape,
      in atelier or a child, so a fix needs a count of such markers across
      the estate first. That is the 2026-08-09 lesson in reverse.
