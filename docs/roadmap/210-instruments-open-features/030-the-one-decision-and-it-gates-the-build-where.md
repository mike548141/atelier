- [ ] 🎯 **The one decision, and it gates the build: where does the crypto come
      from?** Every option yields a confidential archive; what differs is what
      you owe. **A** shell out to `age` everywhere — simplest, standard format
      forever, but `age` must be installed on every *reading* machine and a full
      read gets ~27 s slower. **B** house format in `node:crypto` — nothing to
      install, fastest, but the archive is readable *only* by our code, a real
      durability risk for something built to outlive its tools. **C** implement
      the age format in both directions — no install, fast, standard, but we
      write the trickiest code in the estate twice over. **C′ (counselled)**
      write with the `age` binary, decrypt in-process — `age` needed only on the
      archiving machine, readers stay dependency-free and fast, the format stays
      standard, and **we author only the half where a bug fails loudly** (an
      encrypt bug can mint weak files you discover years later). `age` is
      already installed on this machine. Counsel, not a decision.
      Review **WARRANTED when this moves from design to build** (touches
      SECRETS.md + the instruments crypto surface); the design pass itself
      authored no doctrine, so nothing is queued yet.
