- [ ] **A scanner's verdict has two states and needs three — "found,
      and all properly accepted" reads as "found nothing".** (Mike,
      2026-08-09, stating the model the guards are meant to follow: find
      everything · report them all · subtract the ones that are
      well-reasoned and fully recorded · then give an honest final verdict.)
      The first three steps are built and good — `GUARDS.md` § *Fail noisy,
      then subtract*, leakscan's find-first-subtract-second order, and the
      2026-08-06 tally work. **The fourth is not.**
      [`render_human`](../../../tools/leakscan.py) branches on `not findings`
      alone, so it prints `✓ leakscan clean` in two materially different
      situations: nothing was found, and things were found but every one
      was forgiven. Measured this session, and it is not a corner case —
      atelier's own live run subtracts **35 findings by allow-marker plus
      7 files by glob** and still headlines `clean`; a permanently-private
      repo scanned with `*` prints `✓ leakscan clean (structural + local)`
      with **99 files never opened**. The `suppressed:` line underneath
      carries the numbers honestly; the *verdict word above it* does not,
      and the verdict is what a tired session and a CI log actually read.
      **Fix shape:** a third headline for the all-accepted state (the
      floor board's own `✅ enforced` / `advisory` / `👁️ warn-only` split,
      applied one level down at the scanner's own verdict). **Exit codes do
      not move** — 0 for both clean and all-accepted, 1 for live findings —
      so no CI behaviour changes and the blast radius is text plus one
      JSON field. **Keep `clean` in `--json` and add beside it** rather
      than redefining it; consumers read that key today.
      Same class as G3: it touches every scanner and every adopting tree,
      so it lands on its own rather than riding a C5 build. Whether the
      third state also belongs in the sibling scanners is the same
      question, one item.
      **No decision owed: build it (2026-11-24, session b95c0d98).** Put to
      him as a yes/no in the first oldest-asks round; he answered, verbatim,
      *"Your question does not follow doctrine rules for asking questions"*.
      Re-read against `COMMUNICATION.md` § *Asking for a ruling*: the first
      rule is to establish there is a decision, and there was none. His own
      model, stated on this item 2026-08-09 (*find everything · report them
      all · subtract … · then give an honest final verdict*), already settles
      it: a headline that says "clean" over excused findings is not an honest
      verdict. So this is work owed, the fix shape above, not an ask; the 🎯
      comes off. Today's measure: atelier's leakscan run subtracts 98
      findings by allow-marker and 7 files by glob and still prints `clean`.
      **Leakscan slice built (2026-11-27-1052, session 9c5fa72c worker).** Three
      verdicts, two exit codes. `report.verdict(blocking, accepted)` and
      `report.accepted_head(name, detail)` are the shared home; leakscan's
      `render_human` prints `✓ leakscan all accepted — nothing live; excused, not
      absent: <n> by allow-marker, <m> file(s) by .leakscanignore, …` when nothing
      blocks and `Tally.accepted_total` (markers + ignored files + manifest
      binaries) is above zero, and the old `✓ leakscan clean` only when nothing was
      excused. `--json` gains `"verdict"` (`clean` | `accepted` | `blocked`) and
      `"accepted"` (the count) beside `clean`, which keeps its meaning. Rules turned
      off (advisory) and coverage gaps (untracked, pruned) do not make a run
      accepted: they already have their own lines. Exit codes untouched. Tests:
      `test_leakscan.ThreeStateVerdict` plus the Tally render cases, and
      `test_report.test_the_three_state_verdict`; documented in `tools/README.md`
      § *Three verdicts, two exit codes*. No other scanner's output changed.
      Review: not warranted — an output-shape change to an already-reviewed tool
      its tests cover; a live finding classifies `blocked` before `accepted` is
      considered (pinned), the findings list and exit code run on the old path, and
      the worst case is a wrong headline word over a tally line that already
      carries the counts, which a test reds on.
      **Remains (not built):** the other scanners adopt `report.verdict` and
      `accepted_head`, one at a time, each its own small change. Recommended order,
      by how many suppressions each carries in practice and how many children run
      it: `secretscan` (same marker-and-glob shape, the credential gate, so the
      most to hide), `pathscan`, `datescan`, `linkscan`, `spellscan`, `sizescan`,
      `licenscan`, then the rest that print a `suppressed:` line (`conflictscan`,
      `wrapscan`, `indexscan`, `pointerscan`, `publishscan`, `reviewscan`,
      `stampscan`, `blockscan`). Also owed: leakscan's `--messages` JSON still has
      only `clean` (it excuses nothing: markers do not apply to commit messages, so
      it can only be clean or findings); and `GUARDS.md` § *Fail noisy, then
      subtract* should state the three-state verdict once a second scanner has
      adopted it, so the doctrine describes what two guards do, not one. Item stays
      `[~]` until the siblings are done.
      *Claim released 2026-11-27 at the close of session 9c5fa72c (`atelier-fa`): the
      leakscan slice is landed (`365d1782`); the other scanners' adoption, in the order
      recorded above, is open for any session.*
