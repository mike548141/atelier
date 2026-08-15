# The guardrail commission, answered properly the second time (2026-08-15, 1408 UTC)

**Session:** Opus, worktree `guardrail-scope-correction-0816`.
**Shape:** Mike rejected the first pass's scope and framing, both in one
message. This is the correction, run as a second four-agent fan-out and landed
as nine more items in the same board section.

## What was wrong, in Mike's words

Two errors, and he named them separately.

> You seem to have scoped your work to focus on a variant of the example. It was
> only an example, not the entire scope

The commission was *what guardrails can and should we build in atelier to ensure
the best outcomes from atelier itself and the child repos*. The first pass
studied the scanner fleet and answered the illustration.

> even then you seem to have interpreted my question of multiple narrowly scoped
> guards versus a wider purpose based guard like providence scan. You have taken
> that as multiple narrow vs a single wide guard.

The axis is what a guard is *organised around* — a detectable feature, or the
purpose the feature proxies for. Not breadth. A purpose-based guard can be
narrow.

Both errors are recorded in the section README rather than quietly fixed,
because the first pass's items are still on the board and a later reader needs
to know which frame each was written in.

## What the second pass found

**On the axis.** The correction I offered Mike mid-session was itself half
wrong, and I said so when the evidence landed. I claimed a purpose-based guard
cannot drift because the purpose *is* the rule. `stampscan` falsifies it: the
most purpose-shaped guard in the tree enforces the inverse of the doctrine it
cites, and has since it shipped. What survives is that feature-based guards do
not erode over time — they are born aimed off.

The real defect is that the organising principle is undeclared. Every registry
entry carries a `why` that is printed and never compared to anything, and *the
estate demands a reason for weakening a guard and no reason for building one*.
The one recorded case of a guard being tested against its purpose found what
eight rule-level findings had missed, in a section that labelled itself
mandatory and is mandated nowhere — one of 109 review files.

**On the commission as asked.** Scanners are one guardrail class of eleven.
Twenty-one mechanisms act after an act; five act before it; one of those five is
mechanical. The class that could sit between a decision and the act is the
harness plane, and it is empty here and reaches no child. That is why the
directive-doctrine aim has no carrier — not a wording problem, an empty plane.

The consequence: `00-APEX.md` has no blocking gate on any rule, and the
always-confirm floor has none either, including the line forbidding an agent
from widening its own authority.

**On the children.** Enforcement propagation works — 18 of 18 floors wired, by
call. Everything else does not. 16 of 17 pins stale, nine about five weeks back.
Eight children missing three of seven floor concerns, unchanged a week after the
audit. Only 4 of 17 stamp their copy, so the drift-checker is blind to 13. About
56 lines of doctrine reach a child at session start against roughly 5,620 in
`method/`. The plugin carrying the skills is not installed on this machine.

And the enumerator built to stop this decaying has decayed the same way: **the
scheduled estate conformance job has failed 19 times out of 19 and never once
been green.** Verified directly against the run history, not inferred.

**On cost.** Roughly 95 of 126 open board items are guard, policy, enforcement
or review work. The floor produces 4,598 findings and blocks on none of them. No
guard has ever cleared the trained-away bar to become blocking after
measurement — three refusals, no case naming a rate that passed.

## What landed

Nine items, `100`–`170`, plus a rewritten section README and framing notes on
two first-pass items. Two of the nine are decisions that are Mike's: declare and
test a guard's purpose, and the proportionality question about the layer's share
of the programme.

## Method note, and its limits

Ten agents across the two passes. Several spawned their own sweeps, which is
where the deepest material came from — the rule-by-rule enforcement map, the
child incident sweep, and the external formal results. One agent reported before
its own incident sweep returned and said so; its list is likely incomplete
rather than wrong.

The child incident sweep names private repos beside their postures. **None of
that is reproduced here or in the board items** — every child finding above is
written by class. The existing name-and-posture instances already live on this
board and are queued in their own section; this session added none.

## Concurrency

A parallel session ran cold review passes in its own worktree throughout, dirty
the whole time. No git write touched the shared checkout; explicit-path staging;
worktree taken before the first edit. The shell's working directory reset itself
once mid-session during a cross-repo verification, which is the recorded hazard,
and the affected command was re-run from an absolute path.
