- [ ] 🎯 **B4 — the roadmap-deletion guard: BUILT, MEASURED, and deliberately
      NOT WIRED (2026-07-28).** `tools/harvestscan.py` exists, is tested (16
      tests) and runs clean on the live tree. It fingerprints *content* as the
      item required — never titles — and the measurement is why it stops short
      of the registry.
      **Replayed over all 390 commits touching `ROADMAP.md`**, each against its
      parent exactly as a hook would see it:

      | design | fires on | items |
      |---|---|---|
      | raw body, Jaccard ≥ 0.6 | 165 commits (42.3%) | 257 |
      | + bookkeeping stripped, containment | 120 (30.8%) | 179 |
      | + review pointers excluded | 105 (26.9%) | 158 |

      Every step fixed a **cause** — matching on claim stamps and cycle
      vocabulary that churn while the work does not; punishing an item for
      being absorbed into a larger one; counting refs-only `⏳` pointers whose
      disappearance *is* the mechanism working — and each bought less than the
      last. **One roadmap commit in four would still warn**, which is the rate
      the 2026-07-26 audit already showed gets a guard `allow`-markered into
      silence. Reviewer's counsel to itself is `stampscan`'s: **do not wire,
      not even advisory.**
      **The signal is real, which is why this is shelved and not binned.**
      Replayed against `dd7fcb74` — the commit that removed 185 lines on a
      heading-only comparison and lost a completed item — it reports 2 items,
      including work that genuinely vanished. The detector works; the
      discriminator does not.
      **What would make it wireable, none of it a threshold change:** scope to
      delete-only commits (a commit rewriting a section is both the noisy case
      and the one a human is already reading); compare against a branch's
      merge-base rather than the previous commit, so a multi-commit rewrite is
      judged once at its end state; or narrow to items carrying a decision
      marker, whose loss is what actually costs. **Tuning
      `SURVIVAL_SIMILARITY` is explicitly not on that list** — it would be
      fitting a constant to the corpus it is measured on. Mike's call whether
      to fund the next step or leave it as a hand-run tool before deliberate
      bulk deletions, which is the one moment the 2026-07-25 failure would have
      been caught.
