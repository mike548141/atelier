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
