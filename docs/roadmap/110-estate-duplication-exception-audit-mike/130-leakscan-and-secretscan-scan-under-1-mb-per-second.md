- [x] 🔎 **leakscan and secretscan scan at roughly 0.5–1 MB/s, so a 128 MB
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

      ✅ **Levers 3 and 4 tried; lever 4 merged 2026-10-05** (queue run, a
      Sonnet 5.5 worker; `c938b58`). Each rule now has a **gate**: a cheap
      test its own pattern text makes necessary, such as a required literal, a
      separator count, a minimum length, or the pattern's fixed tail. A line
      that fails a rule's gate provably cannot match that rule, so the rule's
      regex is skipped. A rule with no provable gate runs ungated. That covers
      15 leakscan rules and 16 secretscan rules. The allow-marker parse and
      leakscan's `_shadow_spans` are gated the same way, and secretscan
      computes its entropy-side lookups only after a match. **Lever 3 (one
      combined alternation) was not built**: rules overlap on one span, and
      each reports its own finding in rule order, which a single alternation
      cannot reproduce byte for byte. The reason is recorded in the source.
      Levers 1 and 2 were out of scope (G3; and coverage is Mike's call).

      **Evidence.** On a 50 MB synthetic corpus, best CPU went from 88.5 s to
      28.2 s for leakscan (3.1×) and from 70.8 s to 15.5 s for secretscan
      (4.6×). On atelier's tree, wall time went from 21.4 s to 6.9 s and from
      12.7 s to 3.3 s. Stdout, stderr and exit code were byte-identical, old
      against new, on atelier's tree, a seeded mixed tree and the 50 MB file.
      A differential fuzz of 1.15 million lines across every rule, with
      near-misses, case-fold characters, marker scopes and disabled rules,
      gave **zero mismatches**. The fuzz caught two gate bugs before commit: a
      missing `\s*`, and `github` not containing `gh`. Twelve new tests pin
      that each gate passes wherever its regex matches, and that a gated scan
      equals an ungated one. The term-list path is unchanged, and the real
      list was never read. The orchestrator re-ran `test_leakscan` and
      `test_secretscan` on the merged tree (306 OK) and both selftests.

      ⚠️ **Why the code pass matters here.** A wrong gate is a silent miss on
      a blocking secret or PII guard. The fuzz and the pinning tests are the
      defence. A cold pass is queued at `160/720`.
