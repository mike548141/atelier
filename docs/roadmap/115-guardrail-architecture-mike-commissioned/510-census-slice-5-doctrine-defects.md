- [ ] 🔎 **Defects the enforcement census found in slice 5.** Found
      2026-11-23 UTC by `020/220` slice 5
      (`docs/method/census/2026-11-23-1651-reach-secrets-signing-storage-toolbox-session-open.md`);
      reported, not fixed in passing. The signing finding is `115/520`.
      1. **`SIGNING.md` contradicts itself on status.** Its header says
         steps 4 and 5 are still pending; its ladder marks both done; and
         `docs/method/README.md` calls the plane dormant. Two of three are
         stale. It also speaks of landed steps in the future tense.
      2. **`SIGNING.md`'s "boundary" means two commits**: the first signed
         commit and its parent. `ci.yml` uses the parent.
      3. **`signscan`'s coverage line overstates.** It prints "N
         signature(s) verified" counting signatures it checked, including
         the ones that failed (2604 "verified" against 29 bad on
         2026-11-23).
      4. **`TOOLBOX.md` is incomplete**: 8 of 13 entries under
         `instruments/` are not in its table (`ccopen` and `cclive` among
         them).
      5. **The session-open README says the say-so check "is not built"**;
         `tools/quotescan.py` is that check (landed 2026-11-17).
      6. **`docs/method/README.md` still describes `STORAGE.md` as "iCloud
         backup"**, and `STORAGE.md`'s heading counts four jobs against a
         table of three.
      7. **"Posture" means two things**: `SECRETS.md` and the floor
         registry use the word differently.
      ✅ **Items 1, 3, 4, 5, 6 fixed 2026-11-23** (queue run 608d8123, a
      Sonnet worker, read by the run before landing). 1: the evidence
      settled it (the 2026-07-12 record of steps 4–5, both floor workflows
      carrying the warn-first steps, `signscan` green over the range), so
      `SIGNING.md`'s header and the method README now say all five steps
      are live and warn-first, the flip not made; three future-tense
      phrases fixed. 3: the coverage line reads `N signature(s) checked (G
      good · B bad)`; `--json` keeps `signatures_verified` and adds
      `signatures_checked`, `_good`, `_bad`. 4: TOOLBOX gains eight rows
      (`cclive`, `ccopen`, `ccapple`, `ccfleet`, `ccstatusline`, `ccpdf`,
      `atelier-menu`, `browser-fetch`). 5: the session-open README names
      `quotescan` as the say-so check (added 2026-11-10). 6: the method
      README says Time Machine; `STORAGE.md`'s heading says three jobs.
      Cold pass queued as `160/1750`. **Still open:** item 2 (which commit
      "boundary" names) and item 7 ("posture" in two senses), both naming
      choices.
