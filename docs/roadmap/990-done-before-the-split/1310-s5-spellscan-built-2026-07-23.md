- [x] **S5 spellscan BUILT 2026-07-23** (`760260473`, 0618 run, Sonnet worker).
  `tools/spellscan.py` + 60 tests (suite 432 green) + `--selftest`. NZ-English
  wordlist over `docs/**`: generative `-ize/-ise` + `-yze/-yse` stem families
  (irregular-noun stems excluded so it never invents a word) + hand-listed
  irregulars. Exemptions: fenced/inline code, blockquotes, quote-flanked MENTION,
  URL/path tokens, an `ALLOWLIST_PHRASES` for bare-prose API terms,
  ALL-CAPS-as-identifier. **license/practice deliberately EXCLUDED** — US/NZ
  noun-verb homographs untaggable without POS. Honest baseline: **68 findings /
  32 files** (`artifact` ×53, `catalog` ×10…) — confirms "under-detected, not
  rare".
