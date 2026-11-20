- [x] **Should cctranscript and ccarchive be one?** — analysed 2026-07-22
  (wave-3 queue run, same record): **keep separate** counselled. Measured
  shared code is ~10 lines; merging would couple ccarchive's schema-immunity
  (the property guarding the sole durable copy) to cctranscript's
  schema-fragile parser, and blur ADR 0006's observe vs preserve verbs.
  Counter-case captured (natural pipeline pair → argues for a
  `--source <archive>` flag on the reader, not a merge); middle path (shared
  lib) only if shared code crosses ~40–50 lines. Mike's call whether to
  accept the recommendation; no work owed until then.
