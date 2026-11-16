- [x] **DONE 2026-11-17** (wt: qr-78ca-evidence) **Doctrine candidate — evidence hygiene: a scanner that greps for the
      name of a failure finds the sessions that discussed it.** The first cut of
      the incident scanner text-matched a refusal string and counted its own
      scanning session, inflating one class threefold. The general rule: when an
      agent analyses its own logs it is **inside its own corpus**, so a signal
      must key to a marker the harness sets, never to prose. Pairs with the
      item above; same `⏳` obligation. Second worked example the same session —
      a tool-use profile that grouped by parent directory filed every repo's
      subagent work into one bucket and reported a research-heavy repo as 2%
      research against a corrected 50.6%.
      - 🔀 Tidied 2026-11-16 (C0545, verified high; Mike approved 2026-11-16):
        not an ask of Mike. It is a doctrine candidate for an agent to write up
        (line 1); it asks him nothing. Nothing above was changed; the original
        text is as it was. To revert: delete this line (its commit is listed in
        `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      - 🔀 2026-11-16 (C0545): removed the 🎯 marker from this item's first line,
        because this ask is not Mike's (tidy line above). Original: that line
        began `- [ ] 🎯`. To revert: git revert this repo's marker commit (listed
        in `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      ✅ 2026-11-17 (wt: qr-78ca-evidence): `EVIDENCE.md` §21 (a scanner of one's own logs keys to markers), folded with `220/010` as one section. Rule-4 review owed at landing.
      🔒 CLAIMED 2026-11-16T11:02Z (claimed 2026-11-16-1102, wt: qr-78ca-evidence) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
