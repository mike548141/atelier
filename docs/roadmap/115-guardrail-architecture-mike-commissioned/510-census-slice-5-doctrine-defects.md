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
