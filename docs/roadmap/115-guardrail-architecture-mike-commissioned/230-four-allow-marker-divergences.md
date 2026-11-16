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
      **2026-11-16, queue run 78ca (partly done; item stays open).** A
      read-only census came first: old reader against new on every tracked
      line carrying a scoped marker word in atelier and every sibling repo
      (2,965 lines) showed the item-1 fix changes none of them; items 2 and 3
      have no markers of their shape anywhere either. Done: **item 1** (a
      scope with no reason, `m:allow:kind` or `m:allow:a,b` with nothing
      after it, now exempts nothing at once and gets the "present but
      unparseable" note; the test pin moved from "existing, not endorsed" to
      endorsed); **item 4** (datescan and pathscan docstrings, the
      `allowmarker.py` separator note, and the README table now lists
      attribscan, namescan and quotescan). **Item 3** needed no change: the
      unused `\s*` regexes in datescan and pathscan were already gone, and the
      `\s*` that remains is the documented next-line reason of the five
      multi-line scanners. Still open, each a design choice: **item 2**
      (refuse a scoped spelling on conflictscan and wrapscan, or keep reading
      it as the reason; zero markers of that shape in the estate, so either is
      free); a reasoned marker whose scope names no kind still exempts every
      kind in licenscan, sizescan, pointerscan, pathscan and reviewscan
      (`allowmarker.covers`, the same class); and a glued scope then a space
      and words with no colon (`m:allow:kind why`) still reads as unscoped and
      exempts every kind on its line. That last shape is live: 5 markers in 1
      sibling repo (plus one atelier test fixture), so narrowing it would turn
      that repo red on its next CI run and needs a ruling and a migration first.
      🔒 CLAIMED 2026-11-16T11:22Z (claimed 2026-11-16-1122, wt: qr-78ca-allow) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
