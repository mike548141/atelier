- [ ] 🔎 **Hand-up from faves: leakscan's `nz-phone` matches digit runs
      inside hex digests** `[XS][tools]` — filed 2026-10-02 by faves session
      `faves-4f`, from a measured instance. Offered with options; the remedy
      is atelier's.

  **The instance.** A faves tool began writing a 64-hex `sha256` per
  evidence row into a committed JSON record. `leakscan` refused the commit:
  `nz-phone` matched 3 of 88 digests. The pattern's lookarounds are
  `(?<!\d)` and `(?!\d)`, so a run such as `…a0312345678b…` reads as a phone
  number because the neighbours are hex *letters*, not digits. Every
  re-fingerprint shifts which digests trip it.

  **What the child did, disclosed rather than silent.** It used the
  sanctioned hatch: one reasoned `.leakscanignore` glob for that file
  (`data/intake/menu-sources.json`), since JSON cannot carry a per-line
  marker. That drops all leakscan cover on the file, which is the cost the
  child would rather not carry.

  **The class.** Any committed hash, digest, UUID-ish or hex id beside a
  structural digit rule. The house's own SHA-2 programme (`330`) will put
  more digests into more trees, so this will recur.

  **Options (offered, not recommended):**
  1. Widen the lookarounds to refuse a neighbouring hex letter as well as a
     digit when the surrounding run is 16+ hex characters (a digest-context
     guard), keeping the rule's reach on prose.
  2. A per-rule allowance in the ignore file (`path  rule=nz-phone  #
     reason`), so a child can drop one rule on one file instead of all rules.
  3. Leave the rule; document file-level ignore as the answer for digest
     stores.
