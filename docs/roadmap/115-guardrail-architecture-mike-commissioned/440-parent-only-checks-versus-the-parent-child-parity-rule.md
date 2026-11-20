- [x] 🔎 **`PROPAGATION.md` calls a parent enforcing what its children do not
      a defect, while atelier's CI deliberately runs checks only atelier can
      run.** Found 2026-11-16 UTC by the `020/220` census, slice 2. `stampscan`,
      `blockscan` and the signature checks run on atelier and on no child, by
      design: they check what only the parent holds. The rule's text does not
      carve that class out, so read literally it calls the design a defect.
      **Owed:** say in the rule which checks are parent-only by nature and
      why, so the rule and the practice agree. Not fixed in passing.
      🔒 CLAIMED 2026-11-20T08:25Z (claimed 2026-11-20-0825, wt: atelier-qr-08cd-docfix) by queue-run
      session 08cd3b95 (Opus 5.5, principal-opened). Scope: the parent-only checks named in PROPAGATION.md.
      ✅ **DONE 2026-11-20 UTC** (queue run 08cd, a Sonnet worker): `PROPAGATION.md`
      § *Enforcement propagates too* gains *What the parent runs alone, and
      which of it is legitimate*. Read against `.github/workflows/ci.yml` and
      `floor.yml`, the item's premise was half right. `blockscan` is parent-only
      by nature (its map names files only atelier holds). `stampscan` is
      parent-only for now, a real instance of the defect one level up, held open
      by `ST3`, and the text says so rather than excusing it. The signature
      checks are not parent-only: children run them through `floor.yml`, and
      only the trust root differs. The section ends on a test, *does what it
      checks exist anywhere but the parent?* Doctrine change, so its cold pass
      is owed.
