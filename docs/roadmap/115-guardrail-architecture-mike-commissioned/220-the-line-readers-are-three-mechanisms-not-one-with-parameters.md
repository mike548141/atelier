- [ ] 🎯 **The streaming line readers are three or four different mechanisms,
      not one mechanism with per-guard parameters — so `115/080`'s part 1 scope
      was wrong, and what to do with them is a decision.** Found 2026-09-20 by
      the worker that built part 1, which **declined to widen its own scope**
      and handed the dilemma back rather than picking a side. Correct call.

      ## What the item and the brief both assumed

      `115/080` describes the window/overlap constants and the
      finding-materialisation cap as travelling *with* `_walk_files` — one
      mechanism, per-guard parameters, 256 KiB for links and 4 MiB for
      credentials. The part 1 brief repeated it. **Inspecting the code
      falsifies it.**

      ## What is actually there — four shapes, not one

      1. **`secretscan` / `leakscan` / `conflictscan`** — a windowed-overlap
         reader (4 MiB window, 64 KiB overlap) bound to a `Tally` and a
         `MAX_MATERIALIZED_FINDINGS` cap of 50,000, with window-boundary
         dedup logic scoped to `Finding` excerpts. The overlap exists because
         a credential match can straddle a window cut at an arbitrary offset.
      2. **`linkscan`** — its own windowed-overlap reader (256 KiB / 4 KiB)
         that **also carries markdown fenced-code-block state** (`_FenceState`).
         That is guard-specific business logic riding inside the reader, not
         generic reading. It has **no** finding-materialisation cap.
      3. **`sizescan` / `datescan` / `wrapscan` / `spellscan` / `stampscan`** —
         a truncation-only reader, no overlap at all, because these guards'
         matches are anchored at line start. Its constants (1 MiB chunk,
         8 KiB max line) are **already literally identical across all five** —
         so this shape is not "per-guard different" in the slightest, and is
         arguably the safest single-source candidate of the four.
      4. **`licenscan`** — whole-file read to an 8 MiB cap, no line-splitting.
      *(`pathscan` has no line-content reader at all.)*

      ## Why this is a decision and not a build

      Folding these into the walk means one of two things, and both are bad
      without a ruling: **force one shape** onto guards with genuinely
      different needs — the exact mistake `115/080` warns against in its own
      text — or **build three-plus additional shared mechanisms**, which is a
      materially larger undertaking than "the file walk" and, in `linkscan`'s
      case, risks merging distinct guards' *intents*, which the item forbids
      outright and permanently.

      🔑 **The interesting asymmetry:** shape 3 is five guards already sharing
      identical constants by copy, which is the cheapest and safest
      consolidation on the board. Shape 1's overlap is load-bearing and shape
      2's fence state is not reading at all. So "consolidate the readers" is
      not one question — it is at least two, with very different risk.

      ## The ask

      Decide whether this becomes **part 1b** (a scoped follow-on now),
      **folds into part 2 or 3**, or is **deferred** pending
      `115/170`'s proportionality ruling. Ranked by risk if it helps:
      shape 3 alone is cheap and provable; shapes 1 and 4 are plausible;
      shape 2 should probably be left alone until `linkscan`'s fence state is
      separated from its reading, which is its own piece of work nobody has
      scoped.

      ## A correction to `115/080`'s own text, owed

      That item says the cap and window constants were copied "in four more"
      files alongside the walk's ten. Measured: the finding-materialisation
      cap exists in **three** files (`secretscan`, `leakscan`,
      `conflictscan`), not four, and the walk was in **eleven**, not ten.
      Both figures corrected there. This is the fleet-rollout failure mode
      recurring — a count stated from memory rather than swept
      (`010/030` carries the same warning about itself), and it is the third
      time this estate has recorded it.
