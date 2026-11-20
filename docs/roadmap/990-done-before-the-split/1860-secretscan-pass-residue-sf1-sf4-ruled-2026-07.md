- [x] (2026-08-03: applied, built to E6c) **secretscan pass residue — SF1–SF4, RULED 2026-07-28 (Mike,
      plain-language walk-through with per-option impacts and a live
      six-shape probe).** The rule-4
      pass ran 2026-07-28 (Fable): **0 MAJOR / 1 minor / 3 notes, cycle
      CLOSED** ([verdict](../../reviews/2026-07-28-1220-secretscan-fragment-cold.md)).
      All four red legs reproduced old-vs-new; the FP fixes hold; the
      estate figures verified (the 26→4 delta is the ruled untrack).
      **SF1+SF2** (minor+note, ruled together as one low-charset-diversity
      family) — the new kebab exemption un-flags hyphenated passphrases
      (caught before, clean now; the snake twin was already exempt), and the
      pre-existing lowercase-hex gap is half its stated size (digit-leading
      hex already flags; letter-leading slips) → **TAKE BOTH WHOLE-SHAPE
      CARVE-OUTS**: in assigned-secret context, a full-match 32+ lowercase
      hex value and a 4+ hyphenated/underscored lowercase-word value are not
      identifier/slug-suppressed. Cry-wolf risk is git SHAs, which rarely sit
      assigned to credential-named keys. **Ruled on a live probe, recorded
      because it sharpens the case**: of six credential-shaped assignments,
      four passed clean — both passphrase spellings and both letter-leading
      hex values — while only the digit-leading hex and the mixed-class
      password flagged. **Also carried, and it corrects a record**: the
      triage's "entropy net catches ≥32 chars regardless of key name" aside
      is true only for mixed-class values, and was probed false for this
      family — two 32-character values in the probe did not flag.
      **SF3** (note) — the corpus re-scan question answered: sound
      regression floor, insufficient acceptance test → **BUILD THE CANARY
      SUITE**: a standing fixture set of credential *shapes* (env-var, hex,
      base64, passphrase, connection string) that must always flag, run
      beside the corpus re-scan on gate changes. It would have caught SF1.
      **SF4** (note) — resolved at reconcile, no action.
      **Work owed: SF1+SF2 carve-outs, SF3 canary suite, and the triage
      record's entropy aside corrected.**
      **Superseded in shape, not in substance (Mike, 2026-07-28):** the two
      named carve-outs are now a special case of the general rule ruled under
      **E6c** — in credential-key context, low character variety is not
      evidence of innocence. Build to E6c; this entry is the grounding for
      why, and the probe evidence above still stands.
