- [~] **A scanner's verdict has two states and needs three — "found,
      🔒 Claimed by session 9c5fa72c (`atelier-fa`, Opus 5.5), principal-opened by
      `/atelier:work run` (leakscan slice first).
      (claimed 2026-11-27-1050, wt: atelier-qr-9c5f-thirdstate)
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
