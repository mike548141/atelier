- [ ] **ccarchive: encryption at rest — BUILD not started; one decision open (🎯 Mike)**
  The **design pass is done** (2026-07-26, `d913698`/`7701a62`) →
  [`instruments/ccarchive.encryption.design.md`](../../../instruments/ccarchive.encryption.design.md),
  completed detail in [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md). Direction, shape,
  key management, granularity, migration and DONE conditions are all settled
  there. Two roadmap premises were **corrected by measurement**: the zero-dep
  tension doesn't exist for the Node instruments (`node:crypto` has AEAD +
  X25519; the `openssl` fallback has no AEAD modes at all), and the overhead is
  the *process boundary*, not key access — so encrypted-by-default is
  comfortably realistic.
  - [ ] ⏳ **Sequenced 2026-10-05: build after the `⏳ 160/670` review of the
        hardening.** Put to Mike as options, and he answered *"After the
        independent review (Recommended)"*. The crypto source is C′
        (`210/030`). His charter, `210/240`, gives the reason it comes next:
        anything can end up in a transcript. Note for the builder: the
        design predates the hardening, so `_versions/`, `_anomalies/`,
        `_untrusted/`, the intent journal and atomic rename are new surfaces
        it must cover.
