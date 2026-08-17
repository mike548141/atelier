# 2026-08-17 · 0900 UTC · Mike's ruling round on the cold run — four rulings, all applied (Opus, wt: rulings-0817)

Continuation of the 0710 UTC cold run in the same session. That half ran two
rule-4 passes and wrote a third brief; this half is what Mike did with the
findings, and what the doctrine now says because of it.

**How the round opened, verbatim:** *"ask me any questions"*, then, when the
first was put to him, *"e.g. rulings etc"*. Four asks went up as a decision set
with per-option impacts. He ruled all four in one sitting.

## The four rulings, in his own selected wording

| Ask | Ruled | What it does |
|---|---|---|
| The off-tier orchestrator | **"Accept, and write the rule"** | AA/RG cycles stand closed; `REVIEW.md` rule 4 now says what the tier binds |
| AA7 — the derivation | **"Ratify, but not at the floor"** | apex keeps the wording, gains a floor exception; closes AA6 with it |
| RG4 — the homeless rule | **"RECORD.md + GUARDS.md"** | the rule and its class both get doctrine surfaces |
| The cold-sweep defect | **"Build a guard"** | `tools/coldsweep.py`, exclusion by default |

He was offered the cheap option on the last two — *COMMUNICATION.md only*, and
*leave it, keep disclosing* — and took neither. On the tier question he was
offered plain acceptance and instead required the rule be written, which is the
part that outlives this session.

## What the rulings changed

**The tier bar now names what it binds.** `REVIEW.md` rule 4: the named tier
binds *the judgement that forms findings*, not every hand a pass passes
through. A reviewer is on the tier without exception. An orchestrator holding
the context partition, releasing the deferred sibling and committing the
records may be off-tier, on two conditions that are not optional — it forms no
finding and writes no severity, and the arrangement is disclosed in the claim,
the pointer and the verdict, before the findings rather than after. Absent
either, the stop clause is unchanged. The session that raised the question by
departing is the grounding, named as such.

**The apex gained one exception, and only one.** The extracted-approval rule
keeps its *stands as the principal's word but is open to challenge* wording —
Mike ratified the derivation AA7 exposed. At the **always-confirm floor** the
order is now fixed: re-brief *before* the irreversible action, never challenge
after it. Elsewhere challenge and obedience can run in either order because the
work can be undone; at the floor it cannot. Still no licence to refuse. This
closes **AA6** as well: AA6 named the pause-versus-act divergence at exactly
this point and this decides it. Applied to the apex, `REVIEW.md` rule 3, the
`PROPAGATION.md` floor block and the byte-identical templates stamp
(`stampscan` `[identical]`, 61 lines).

**Two rules got homes, and the class got one too.** `RECORD.md` § *An approval
is not the whole ruling*: when a recommendation is approved with reservations,
the reservations go into the record beside the approval, and **each becomes a
check the build has to answer** — a reservation is not a caveat. `GUARDS.md`
§ *A rule with no home is not a rule* carries the class: a rule written only to
a record reaches exactly the readers who already knew it, because rule 2 bars a
cold reviewer from records and no onramp loads them. `COMMUNICATION.md` keeps
the grounded instance and points at both.

## The guard

`tools/coldsweep.py` — the tree search a cold reviewer runs, with rule 2's
barred paths excluded by default and the wide sweep behind `--include-barred`,
which prints a disclosure banner.

**The fix is at the defect's real location.** Three reviewers tried to honour
the bar and three exclusions silently did not apply, because a path was matched
as a text *prefix* against output whose prefix is a platform detail
(`grep -r <dir>` emits no `./`). coldsweep never compares paths as text: it
walks with `pathlib` and compares relative path **parts**. So `./docs/sessions`,
`docs/sessions`, `docs/sessions/` and `docs//sessions` bar the same files, and
`docs/sessions-archive/` is not swept up by any of them. Both directions are
pinned by tests — a bar that over-reaches produces a clean sweep of *nothing*,
which reads identically to a clean tree, and that failure would be worse than
the one it replaced.

Not a floor check and not in the registry: it gates no commit. Exercised live
on this tree — **289 barred files excluded**, which is the material that leaked
three times. 20 tests plus a selftest whose corpus is the three real instances
reduced to shapes.

## What the applications owe, and what they did not touch

Both landings queue their own rule-4 `⏳` (`160-…/230` for the doctrine batch,
`160-…/240` for the guard), and **both pointers are scoped to paths rather than
to the landing commit** — the `AA11` shape found this morning, applied to its
own successor rather than only filed. The guard's pointer also names the thing
its author cannot weigh: coldsweep makes the safe path easier but does not make
the unsafe path *fail*, so a reviewer reaching for `grep` from habit is still
unprotected. Whether that is the right altitude is a lens-1 question this build
deliberately did not decide.

**Not applied, because not ruled:** AA8–AA13 and RG1–RG3, RG5–RG9 stay in the
pile. AA9 in particular — the session-onramp skill carries neither the
authority-absolute sentence nor the informed-confirmation duty — was tempting
to fix while the surrounding surfaces were open, and was left alone. An
unruled finding is counsel, and applying counsel because it is convenient is
how a ruling round stops meaning anything.
