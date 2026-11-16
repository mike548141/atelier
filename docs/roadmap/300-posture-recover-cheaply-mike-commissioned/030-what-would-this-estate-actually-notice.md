- [ ] **The census: what would this estate actually NOTICE, and what can it
      actually RESTORE?** `[L][ops]` — Mike ruled 2026-08-17 that this is looked
      at next. It is the posture's precondition, not an extension of it.
      **The question, in checkable terms.** For each class of failure the
      posture licenses us to stop fearing — a hostile device on the network, a
      leaked credential, a destroyed dataset, a lost service — two answers:
      **would we notice, and how**; and **can we restore, proven by having
      done it**. The split that matters is between *proven by exercise* and
      *assumed*, because those two read identically in every record we hold.
      **Why it cannot be answered here, and where it must be answered.** Estate
      facts — the inventory, the providers, the credentials, the backup and
      monitoring reality — live in the private estate-root repo, and atelier
      holds classes rather than instances. So the census runs **there**, in a
      session working that repo, and atelier receives only the generalised
      finding. Naming the instances here would be both a work-locality breach
      and, for a public tree, reconnaissance.
      🔑 **The asymmetry worth stating up front**, because it predicts the
      result: rotation-ease is provable by rotating, restore-confidence by
      restoring, and *"we would notice"* has no equivalent cheap proof — so it
      is the leg most likely to be assumed and the one the census exists to
      test. Expect the detection half to be weaker than the restore half.
      - 🔀 Tidied 2026-11-16 (C0547, verified high; Mike approved 2026-11-16):
        not an ask of Mike. That this is looked at next is already recorded at
        line 2; doing the census is agent work, and lines 10-14 say it runs in a
        session outside atelier, with only the generalised finding coming back
        here. Nothing above was changed; the original text is as it was. To
        revert: delete this line (its commit is listed in
        `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      - 🔀 2026-11-16 (C0547): removed the 🎯 marker from this item's first line,
        because this ask is not Mike's (tidy line above). Original: that line
        began `- [ ] 🎯`. To revert: git revert this repo's marker commit (listed
        in `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
