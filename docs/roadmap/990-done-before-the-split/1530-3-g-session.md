- [x] **3. `-g session`.** A `DIMS` entry as predicted, not a grain change. Keys
  on the **full UUID** (a synthetic ordinal stays a display label, never a key)
  and prints an 8-character prefix in the human table only; `--json`/`--csv`
  carry the whole id, because a truncated id you cannot look up is worse than a
  wide one you can. The filter's private session getter is **gone**, so filtering
  and grouping can no longer disagree about what a session key is. `--top` was
  deliberately not added — it travels with ask 4. Answers "which session hit
  529k?", the one part of that question ccrepo previously couldn't.
