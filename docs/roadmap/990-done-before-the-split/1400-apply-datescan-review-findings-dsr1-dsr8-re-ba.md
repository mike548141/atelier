- [x] **Apply datescan review findings DSR1–DSR8 + re-baseline** — DONE
      2026-07-23 (queue run 0707, Sonnet worker, merged `b7b292c`→ merge commit).
      All eight applied; baseline **60→0** (5 genuine hits fixed: ISO rewrite
      where re-derivable, `datescan:allow` with honest reasons where not). Three
      extra real bugs caught mid-work (whole-line ISO cue leak, `YYYY-MM-DD-HHMM`
      false-fire, empty `-->` reason). 58 datescan + 489 tools-suite green; DSR3
      `today`-narrowing silent-miss trade declared in-header. Orchestrator (Opus)
      verified before merge.
