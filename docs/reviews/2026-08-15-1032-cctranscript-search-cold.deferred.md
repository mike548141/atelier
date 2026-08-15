# Deferred — the `cctranscript --search` cold pass

*Sibling of `2026-08-15-1032-cctranscript-search-cold.md`. Open only after the
reviewer's own findings are durably written (REVIEW.md rule 1). Fold in below
the verdict and delete this file when the verdict lands.*

## References withheld from the brief

- **Intent record:** `docs/roadmap/210-instruments-open-features/README.md`
  (the *cctranscript learns to search* narrative and the follow-up items
  `050-…`, `080-…`, `090-…` it spawned), and `docs/ROADMAP-DONE.md`
  § *cctranscript learns to search*. The design document itself is in-delta
  and was not withheld.
- **The queue pointer:**
  `docs/roadmap/160-doctrine-review-owed/010-rule-4-review-queued-tier-fable-pass-type-code.md`.
- **Prior verdicts on the instruments** — reconcile only, never anchor:
  `docs/reviews/2026-07-11-instruments-test-floor-code-review.md` and
  `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md`. The
  design pass of 2026-07-27 has no verdict file of its own — check whether it
  was reviewed at all before being built to.

## The brief-writer's seeded questions

Written by a non-author cold session from the delta alone. A floor, never a
fence — the reviewer's own findings come first.

1. **The banner is the builder marking its own homework.** Six departures are
   declared in the design's status banner. A cold read of the design followed
   by a cold read of the code is the only way to find a seventh. Two places to
   look first: the design's DONE conditions that the banner does *not*
   mention, and any flag in `--help` that the design never named.
2. **The false-negative class in `--regex`.** The banner says the raw-line
   prefilter's escaping gap is "real and documented in NOTES rather than
   papered over" for regex mode. Is a documented false negative acceptable in
   a *search* tool whose whole value is recall, and does the manual page make
   it visible where a user would look, or only in a notes section?
3. **The wall-clock guard replaced by a structural one.** DONE condition 13
   became a `meta.sessionsParsed` assertion. Does the new test pin the
   property the 1.5× condition protected, or a property that is easier to
   pass? Reproduce the 1.22–1.32× and 3.7× figures if a store admits it.
4. **Excerpts as an exfiltration path.** The tool prints tool-input excerpts
   whole (the banner says searching one field is "the quiet wrongness §5
   warns against"). Whole tool inputs can carry secrets and personal data. Is
   there any redaction, truncation, or warning — and should there be, given
   the house's own rule that a scanner output pasted into a public record is
   a leak class it has recorded before?
5. **Shared-vocabulary claims.** The README table says `--since`/`--until`,
   `--top` and `--materialise` are shared vocabulary across the instruments.
   Check each flag's semantics in each instrument that claims it — same name,
   same meaning, same edge behaviour?
6. **The subagent gap.** A follow-up item records that subagent logs sit
   outside every `cctranscript` view. For a search tool that is a recall gap
   the user cannot see. Does `--search` say so in its output or manual page?
