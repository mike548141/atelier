# Findings filed from a child via § *Pointing up* (2026-08-18)

**The route's first exercise, hours after it landed.** A private child's session
sent three findings over the cross-session channel rather than writing them into
its own onramp. It checked the parent's actual files first, stopped at the
finding instead of writing into atelier's tree, and stated all three as class
only — no repo name, no hosts, no client, no child filenames. That is
`PROPAGATION.md` § *Pointing up* working as written, and it is worth recording
as a worked example rather than only as three tickets.

**Kept together deliberately.** These could be split across the scanner and
guard sections by subject. They are not, because the fact that a *child* filed
them is load-bearing evidence about the route, and splitting them would bury it.

**Verified here, not taken on trust** — which the filing session explicitly
asked for: *"I would rather you reproduced it at your HEAD than took my word for
it."* That verification then **had to be done twice, because the first pass was
wrong**, and the exchange is the most useful thing in this section.

First pass: a throwaway `src/<pkg>/` repo run against `tools/pathscan.py` at
HEAD. It reproduced all three classes and produced two confident corrections to
the child's account — one widening Class B, one narrowing Class C. **The child
falsified both from its own tree within the hour.** Class B's widening rested on
an **invalid control**: the probe repo had no sibling at the path the reference
named, so a correct relative path to the parent had nothing to resolve to, and
the red was the probe's artefact. Class C's narrowing proposed backticks as the
discriminator; the child's two real hits are both backticked, and re-probing
showed the actual discriminator is *which wildcard character* — `*` handled,
`{` not — with a trailing slash stripped rather than exempting.

Both corrections are **left visible in item `010`** rather than edited out. The
invalid control is the third recorded instance of that specific mistake, and a
board that quietly absorbs its own wrong turns cannot show a pattern three
instances deep.

**Net effect on priority:** Class A is the whole story at 33 of 45. Class B
drops — the scanner is not punishing children for following doctrine, it is
punishing prose shorthand.

**A fourth item arrived as a question, not a finding.** `040` records a
mechanism the child raised *after* reading the section that would have answered
it — it checked `PROPAGATION.md` § *Enforcement propagates too* first, found the
argument already made, and declined to file the finding it had been about to
write. The narrow residue survives that check and is filed here; the declining
is worth as much as the filing.

**Two of the three original items are proposals, not defects**, and are filed as
such.
Item `020` would change the fourth requirement in `GUARDS.md`, which was Mike's
own ruling of 2026-08-17 — so it is his to change, and this session deliberately
did not write it into doctrine. Item `030` is a testing rule with unusually
clean evidence and no owner in `docs/method/` yet.

**What this section does not claim.** The child's count of 45 findings is *its*
measurement in *its* repo, and is recorded as reported rather than reproduced —
this session verified the three mechanisms, not the tally. The distinction
matters because the fix priority in `010` rests on the mechanism, while the
alarm-fatigue argument rests on the tally.
