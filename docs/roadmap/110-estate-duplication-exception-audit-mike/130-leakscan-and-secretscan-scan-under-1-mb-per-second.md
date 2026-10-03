- [ ] 🔎 **leakscan and secretscan scan at roughly 0.5–1 MB/s, so a 128 MB
      repo still takes minutes** `[M][tools]`. Measured 2026-10-03, after
      `110` stopped them walking untracked trees: leakscan took 231 s and
      secretscan 139 s over 128 MB of tracked text. Memory is flat (43–60
      MB), so this is time only. A profile from the same day puts leakscan's
      cost in `scan_lines` (the structural regex set) and `_shadow_spans`.
      **Candidate levers, not chosen:**
      - skip files git marks binary *before* reading them (G3 changes what
        happens to binaries, so sequence this with `020/150`);
      - a per-file size threshold with a declared, counted skip;
      - one combined alternation pass instead of many patterns per line;
      - a cheap literal pre-filter before the expensive patterns.
      Every lever must keep output byte-identical on atelier's tree and
      report anything it skipped.
      📏 **Re-measured 2026-10-03, after `140`:** leakscan 147 s, secretscan
      56 s on the same 128 MB. The quadratic reader was part of it, and the
      rest is regex. On a 50 MB file of short lines, leakscan takes 52 s and
      secretscan 22 s.
