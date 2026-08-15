- [ ] 🎯 **A scanner's verdict has two states and needs three — "found,
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
