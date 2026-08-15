- [ ] **Where does the registry live? — the SCANNER half is answered and built
      (2026-07-26); the CHECKLIST half is still open.** Both layers, as proposed:
      an atelier-shared floor (fleet-wide, the current scanners) plus a
      repo-local append (a child's own conventions), same layering as doctrine —
      shared floor, local append, child may narrow-not-contradict.
      **Built:** `.atelier-floor.json` gains a `local` block, so a child declares
      and ships checks of its own; they run on both planes, block the same
      commit, fail closed when the script is missing, cannot take a fleet check's
      name, and show on `floorfleet`'s board. Forced by a real case from `ros`
      (2026-07-26): a tripwire whose blocklist names the estate's own tokens can
      never be a shared scanner, so without the seam the repo had to keep a
      bespoke hook — falling out of propagation, the exact ADR 0008 defect — or
      lose the check. REPO-STANDARD carries the layering statement.
      **Still open:** the *verifier/checklist* layer (V1–V7 and a child's own
      review catalogue) has no such seam, and gets one only once
      "Codify V1–V7 as the always-loaded reviewer checklist" (above) decides what
      a checklist entry even is. Do not read the scanner seam as covering it.
