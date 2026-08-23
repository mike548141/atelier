- [ ] 🎯 **Decide whether this becomes a rule, and where it lives — then sweep
      the house for checks that discount their own primitive.** Two halves, and
      as with `330` the second is what earns the item.
  - [ ] **Where it lives.** It is not a safety floor — nothing catches fire the
        moment a check is weakened, and the floor is already long. It reads as a
        **how we build** rule, so `PRINCIPLES.md` or the conventions surface,
        stated tightly enough to be checkable by a reader:
        **use the full strength of the primitive you chose; never compare a
        truncation of it. Where a failure would be irreversible, verification is
        exact, and any residual that cannot be removed is printed in the output
        rather than reasoned about privately.**
  - [ ] **Then sweep for the pattern, which is broader than hashes.** It is any
        check that is weaker than it presents itself as being. Worth looking for:
    - [ ] a digest compared at reduced width — `cut -c1-N`, `[:8]`, `head -c`,
          short git SHAs used as identity rather than as display
    - [ ] a comparison that samples where it claims to cover — `head`, `| head -n`,
          a `find … | shuf`, "spot check" phrasing in a report
    - [ ] a report whose **verdict** is computed from an abbreviated value it also
          prints, which is the exact shape of the docker-heap defect
    - [ ] size-or-mtime equality standing in for content equality without saying
          so — the cheap check is often right and the claim must still match it
  - [ ] ⚠️ **Do not turn this into a scanner reflexively.** `grep -rn 'cut -c1-'`
        would fire on every legitimate abbreviation-for-display in the estate, and
        the house already carries a lesson about guards that produce more noise
        than signal. **Decide the rule first; decide whether it is mechanically
        checkable second, and separately.**
        🔎 If it *is* made mechanical, the discriminating question is not "is this
        truncated" but **"does a truncated value reach a comparison"** — which is
        a dataflow question, not a grep. That is probably beyond a line-based
        scanner and is a reason to leave it to review rather than to a tool.
  - [ ] 🔑 **Carry the provenance, because it is the strongest part of the case.**
        The docker-heap defect was found by the *owner* reading a report and
        asking why the hashes looked short. The agent had already shipped the
        fix and volunteered the flaw — and then undercut both by defending the
        window with a probability. **A rule written from that story lands better
        than one written from first principles**, and it also records the
        practice he explicitly asked to see continued: find the defect, say so,
        fix it, and re-run everything the defective version touched.
