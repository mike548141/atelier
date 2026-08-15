# spellscan's reason class silently voided live allow-markers — CLOSED 2026-08-09

Fixed at the class in `8276a54` (14 regex sites across 12 scanners, re-enumerated
at HEAD before this close), and harvested the same day →
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *spellscan's reason class silently voided
live allow-markers*. Both of the item's open threads — whether to widen to `\S`,
and the check-the-siblings precondition — were closed by the shape of the fix
rather than deferred. The class-level residue it *did* leave open (a marker that
parses as nothing is indistinguishable from no marker) lives on as § *Estate
duplication + exception audit*'s **Make a voided allowance visible** item below.
