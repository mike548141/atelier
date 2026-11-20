# 2026-07-16 · 1013 UTC · ccrepo — currency to a footnote, not a per-figure prefix

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 105+1 -->
- [2026-07-16 · 1013 UTC · ccrepo — currency to a footnote, not a per-figure prefix (Opus)](2026-07-16-1013-ccrepo-currency-footnote.md) — Mike: ccrepo stamped the currency on every dollar figure (`NZ$412.14`); move it to a footnote near the `Rate:` line. CONVENTIONS' declare-once rule made literal on the instrument that inspired its currency analogy two sessions back — the currency is now named exactly twice (column header `Cost (NZD)` + footnote) and never per figure. `SYMBOLS` collapses the disambiguating dollar prefixes (`NZ$`/`US$`/`A$`/`C$`) to a plain `$`; `£`/`€`/`¥` unchanged; unknown codes drop to no marker (`symbolFor` → `''`). New footnote `All amounts shown in <currency>.` prints **always** (so `--fx usd`, which has no `Rate:` line, gets it too), directly above the rate line. Verified: 34 instrument tests green (`symbolFor` test updated to the new contract), both render paths driven live (NZD `$412.14` + footnote above rate; USD footnote present, no rate line). No review owed — instrument display change, self-verifying (ceremony ∝ risk).


## What prompted it

Mike: ccrepo stamped the currency on every dollar figure (`NZ$412.14`); move
that to a footnote near the `Rate:` line instead.

## The change (`instruments/ccrepo`)

This is CONVENTIONS' declare-once rule made literal — the same currency analogy
that drafted the doctrine two sessions back ("NZD named once in the UX, not
prefixed to each `$`"), now applied to the instrument that inspired it.

- **`SYMBOLS` → bare markers.** The disambiguating prefixes (`NZ$`/`US$`/`A$`/
  `C$`) collapse to a plain `$` for the whole dollar family; `£`/`€`/`¥` are
  already unambiguous and unchanged; unknown codes drop their `CODE ` prefix to
  no marker at all. `symbolFor` returns `''` for unknowns.
- **Footnote added**, printed always (so `--fx usd` gets it too, where there is
  no `Rate:` line): `  All amounts shown in <currency>.` — sits directly above
  the `Rate:` line. The currency is now named exactly twice: the column header
  (`Cost (NZD)`) and this footnote, never on each figure.

## Verified

- 34 instrument tests green (`node --test instruments/*.test.js`). Updated the
  `symbolFor` test to the new contract (`NZD`/`USD` → `$`, unknown → `''`).
- Driven live both paths: default NZD render shows `$412.14` with the footnote
  above the rate line; `--fx usd` shows `All amounts shown in USD.` with no rate
  line, footnote still present.

## Owed

Nothing — an instrument display change, tested and driven, self-verifying. No
review gate (ceremony ∝ risk; this isn't doctrine text).
