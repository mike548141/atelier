# 2026-08-09 · 0715 UTC · A duplicate C5 cold pass, its reconciliation, and one increment for the ruling (Fable, main)

Mike opened this session on Fable with "please do any review work". The C5
cold-pass sub-item read **RUNNING** with no verdict appended and no closing
session entry after the briefing commit; the tree was clean and no worktrees
were live. This session judged the runner probably dead and took the pass.
That judgement was wrong: the legitimate pass was live in a parallel session
and landed its verdict (`ceb8824`) while this session's probes were mid-run.
CONCURRENCY already says a clean tree is not proof you are alone — the sharper
lesson worth carrying: **a RUNNING pointer with no verdict yet is evidence of
a live claim, not a stale one; absence of a close entry means assume live,
and do independent NEW work instead.**

## What this session did before discovering the collision

A full independent execution of the brief: all 13 re-run obligations, probed
with a scratch term list in the session scratchpad ($ATELIER_LEAKSCAN_TERMS;
the operator's list untouched, the term written into no repo file), plus the
doctrine cross-checks and both staged- and tree-plane empirical probes. On
discovering the landed verdict, REVIEW rule 2 was honoured in shape: this
session's findings were durably written outside the repo *before* the landed
verdict was opened, then reconciled.

## Reconciliation — two independent Fable passes on one brief

**Corroborated independently (same numbers from separate probes):** all 13
claims exact at the states the sweep measured (67/60/7 at `f83a6f7`; the
children's 58 at their pre-sweep commits); the same-day drift (74/62/12 and
58→60 at head, marker cost 118→122); the three `*` opt-outs clean at exit 0
with the bare term live (plus a positive control proving the probe fires);
path-before-terms on both planes — this pass also proved the staged plane
empirically (term staged behind a repo-wide glob → exit 0; glob removed →
exit 1); the ordinary-English census undercount including the archived-config
building instances the census missed; option 2's figures unreproducible for
want of a recorded shape set; the frozen-records convention grounded in
RECORD.md with the allow-marker edge unruled; the option-4 tension resolving
as two axes. Verdict grade would also have been PASS-WITH-FINDINGS.

**Found by the landed pass, missed by this one:** the composition MAJORs —
one of the six term-carrying children is public and only ~6 of the 58 lines
are the prescribed onramp act (C5R1); the 2026-08-06 deletion precedent
misdescribed against its own ADR (C5R2); the coined quotation that exists in
no child (C5R3); the unversioned home of option 1's scope grants (C5R5); the
line-0 path finding no marker can reach (C5R10). Two of these were
spot-verified by this session after reading (the path finding reproduces in
this session's own scan JSON; the pilot child's public visibility confirmed
via the forge API).

**The one increment the landed verdict lacks — flagged for the ruling
walk-through, standing Mike's to decide:** option 1's scope grammar declares
*where a term does not apply*, and a scope covering this repo's records paths
cannot distinguish the ~62 frozen lines from **future** record entries.
Future joins written into new session records would be counted in the tally,
not blocked at commit — on the surface the item itself calls where this
repo's real leaks have actually happened, in the same breath as it rejects
`.leakscanignore` there. Noisy subtraction makes that visible after the
fact; it does not prevent it. This also bounds the landed C5R11: of the
seven new same-day mentions, the five in live files would have been caught at
commit under option 1 — the two that landed in a new session record would
not, under a records-scoped grant as specced. The children's onramp scopes
are the opposite case (forward-open is the point there). One instrument, two
opposite forward semantics; the item prices neither. If option 1 is taken,
the records scope needs either a distinct grammar (frozen-at-grant, not
path-forever) or an explicit acceptance that records become
counted-not-blocked.

## Standing of this pass

Not a verdict. The item's cycle belongs to the landed pass; nothing was
appended to the brief file and no review record was written. This entry is
the session's honest account plus the reconciliation; the increment above is
put to Mike beside C5R1–C5R12, not merged into them. The duplicate spend is
the cost of the RUNNING misread, recorded so the next session prices it
correctly.
