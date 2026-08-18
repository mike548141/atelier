# 2026-08-18 · 0746 UTC · Pointing up — the child-to-parent route, and the block defect that made it necessary

**Tier:** Opus 5 (1M). **Worktree:** `pointing-up-doctrine-0818`.
**Commission:** Mike, opening the session by quoting a private child's session
back at me — *"The other session homed it as BS2 in CLAUDE.md, the onramp every
future session reads, with the upstream debt to atelier marked 🎯 as one rule
with four symptoms, not four rules."* — and ruling on it: *"That does not seem
like a good precedent. Lets build whatever fills that need properly in the
doctrine and once thats ready (incl reviews etc) revert the changes cbom has
made to claude.md."* He later refined the last clause to *"queue it in cbom repo
so that a cbom session can revert"*.

## What I set out to do, and what changed under me

The brief read as: the child had a real upstream debt, no route to discharge it,
and improvised. Build the route.

Half of that was right. **The route genuinely did not exist** —
`PROPAGATION.md` § *The layer-override rule* said children point up and the
parent never points down for truth; § *Who is a child* said a child may add and
never repeat. Neither said *where* a child files a rule the house owns.
Meanwhile `GUARDS.md` § *A rule with no home is not a rule* told the session to
name a surface a future session reads it on, or queue the homing — and the only
loaded surface a child session can reach is its own onramp. Both rules followed;
wrong outcome. That is a missing rule, not a session's misjudgement, and it is
why the fix landed here rather than as a correction to that child.

**The other half was wrong, and finding it changed the work.** I went to check
what `CONCURRENCY.md` was owed before writing it up, and both authored rules
were already there — BS1 verbatim at § *Claiming work* (lines 249–254), BS2's
substance at § *The trigger* (lines 78–86). **Nothing was owed upstream at
all.**

## The cause, which is the finding worth keeping

The child did not read the parent. It read **its own floor block's compression
of the parent** — *"stage explicit paths, and read the staged hunk headers
before every commit"* — and reasoned, correctly given that text, that the rule
only covers what you staged and therefore could not catch a path a peer left in
the index. The parent's actual rule runs `git diff --cached -U0 | grep '^@@'`
over the **whole index**, and covers precisely that case.

So: a stamped copy read as the source does not merely misinform. **It
manufactures phantom debt, and the debt looks like diligence.** That is one rung
below the drift hazard § *One statement, stamped copies* already names, and it
is what § *Pointing up* now opens with — check the parent's actual file, never
your own block.

**Two block defects, both estate-wide.** The phrase above is lossy in the one
place precision mattered, *and* the bullet points at `CONCURRENCY.md` § *The
channel* where the rule lives in § *The trigger* — so a session that did follow
the pointer landed in the wrong section and found nothing. Swept, not estimated:
**ten children** carry both (`ros`, `rpi`, `faves`, `shed`, `cbom`, `kainga`,
`tuhura`, `docker-heap`, `derry-hill`, `stewart-drive`), plus the scaffold
template. `shed` is least exposed — its variant names the actual command — and
still mis-pointed.

## What landed

- `PROPAGATION.md` § *Pointing up — when a child earns a house rule*: the
  check-the-parent-first rule, the whose-rule-is-it test, the four-step route,
  the close at pin bump, and the instance written out with its four defects.
- The canonical block's concurrency bullet reworded and repointed, in
  `PROPAGATION.md` and in `docs/build/templates/CLAUDE.md`.
- `CONCURRENCY.md` § *The trigger*: the whole-index clause, the stale-entry
  cause (an index outlives the ref that fed it), and a bearing for the instance.
- `GUARDS.md`: the cross-repo pointer on "queue the homing".
- Board section `310`, five items, and this record.

## Mike's ruling, and how it was taken

Asked one substantive question, twice — the first popup came back *"I don't
understand"*, which was fair: it was written in the vocabulary of the problem
rather than the vocabulary of the decision. Re-asked after a plain-language
walk-through in session, with the impacts of each option stated first.

**Ruled:** where a child checks the parent properly and the rule genuinely *is*
new, it may keep **one repo-shaped line**, marked pending-upstream and naming
the parent item — in preference to holding nothing. The reason he ruled on:
forbidding the local write without removing the exposure that causes it leaves
the child knowingly unprotected between learning and landing, and that exposure
is what produced this instance.

**Also ruled:** the `cbom` revert is **queued in `cbom`**, after this cycle's
review, for a `cbom` session to take. He was offered the faster route — this
session editing that repo directly as a recorded exception — and declined it.

## What I am not claiming

- **The route is unwatched.** Nothing enumerates what the estate owes the
  house; `floorfleet.py` and `pins.py` only run downward. § *Pointing up* says
  this of itself rather than implying a closed loop, and `310/020` funds the
  instrument. This is rung 1 by its own ladder's test.
- **The ten children are unfixed.** Each clears at its own next pin bump, in its
  own session. `310/030` closes on a sweep showing zero, not on ten commits
  having happened.
- **The `cbom` finding is not yet filed** — deliberately, per the sequencing
  above. `310/040` carries what it must say so the taker is not re-deriving it.
- **Doctrine is self-authored here**, so the rule-4 `⏳` at `310/050` is queued
  in this landing commit and this session neither takes nor spawns it.

## Postscript — the route was exercised the same day, from the outside

Hours after the merge, a private child's session sent three findings over the
cross-session channel instead of writing them into its own onramp. It had read
§ *Pointing up*, checked the parent's actual files first, stopped at the
finding, and stated all three as class only — no repo name, no hosts, no
client, no child filenames. It also flagged that it had sent identically to two
atelier sessions and asked us to coordinate; a follow-up corrected that the
other had closed, which my own `ListAgents` independently confirmed.

**I reproduced its lead finding rather than filing it on trust**, which it
explicitly asked for: *"I would rather you reproduced it at your HEAD than took
my word for it."* A throwaway repo laid out `src/mypkg/sub/module.py` with a
`docs/` tree, run against `tools/pathscan.py` at HEAD.

**And then I got two of the three classes wrong, and the child corrected me
inside the hour.** This is the part worth keeping.

My first pass produced two confident corrections to the child's account. Both
were wrong, and the errors were not the same kind:

- **Class B — I claimed the correct relative form `../atelier/docs/method/…`
  reds, and called it the sharp end: a child accruing a finding for obeying the
  doctrine.** False. **The control was invalid** — my probe repo had no sibling
  at the path the reference named, so the token had nothing to resolve to and
  the red was my probe's artefact. The child falsified it from its own tree,
  where five references in exactly that form appear in none of its 45. Re-probed
  with the sibling present: it resolves. **Third recorded instance of using a
  control I had not checked was comparable.**
- **Class C — I proposed backticks as the discriminator.** False. Both of the
  child's real hits are backticked. Re-probing showed the actual discriminator
  is *which wildcard character*: `*` and `?` are excluded by the existing
  lookbehind, `{` brace expansion is not, and a trailing slash is **stripped**
  rather than exempting the token (`docs/client/` → `docs/client`).
- **Class A survived both passes** as the child stated it — 33 of 45, the whole
  story. Plus a discrepancy found while reproducing: the failure message names
  three resolution anchors where the module docstring advertises four.

I had also asked the child to check its pin, on the theory that version skew
explained the Class C gap. There is no pin: its hook execs the scanners from
this checkout, so it was running **my exact code**. The skew hypothesis was
mine and it was lazy — it would have explained away a real defect.

Controls behaved throughout (present path clean, absent path flagged), so this
is three resolution gaps and not a failed scanner.

**Filed as board section `320`, four items**, kept together rather than split
by subject because the fact that a *child* filed them is evidence about the
route and splitting would bury it. The two doctrine proposals went up **as
proposals**: `020` would change the fourth requirement Mike ruled on
2026-08-17, so it is his to change and I did not write it into `GUARDS.md`.
`040` is a mechanism the child raised as a question after reading the section
that would have answered it — it checked `PROPAGATION.md` § *Enforcement
propagates too*, found the argument already made, and declined to file the
finding it had been about to write. Only the narrow residue is filed.

**Both of my wrong turns are left visible in `010` rather than edited out.** A
board that quietly absorbs its own corrections cannot show a pattern three
instances deep, and the invalid-control mistake is now three deep.

**Not claimed:** the child's headline number — 45 findings, 0 real — is its
measurement in its repo, recorded as reported and **not** reproduced here. I
verified the three mechanisms, not the tally. The fix priority rests on the
mechanism; the alarm-fatigue argument rests on the tally, and only one of those
is verified.
