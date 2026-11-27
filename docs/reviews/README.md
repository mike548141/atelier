# Reviews

Peer-review briefs and their verdicts, one file each. Atelier's own work earns
a review by the same test it gives its children: *what will come to rest on
this once it is trusted?* The trigger, the calibration, the lifecycle and the
independence rules are in
[`docs/method/REVIEW.md`](../method/REVIEW.md), and that file is the only
source for them. This README is a map of the folder, not a second copy of the
doctrine. What a child repo's reviews README carries is the stamped pointer
at
[`docs/build/templates/docs/reviews/README.md`](../build/templates/docs/reviews/README.md);
atelier's own differs because the doctrine sits next door.

## What is here

- **`<YYYY-MM-DD>-<HHMM>-<slug>.md`**: one brief, with its verdict below it
  once a pass has run (the *brief on top, verdict below* lifecycle is in
  `REVIEW.md`). The time is the start time in UTC, from `date -u`. The oldest
  files (July 2026) carry a date and a slug only; they keep their names.
- **`<brief>.deferred.md`**: a brief's deferred material, kept in its own file
  so reading the brief does not consume it (`REVIEW.md` rule 1). The reviewer
  opens it only after its own findings are written. It is folded into the brief
  below the verdict and deleted when the pass closes, so a file left here
  belongs to a pass still open.
- **`withdrawn/`**: passes that happened and were not accepted, kept apart
  from the accepted ones. Its own [README](withdrawn/README.md) says how.
- **`drafts/`**: a reviewer's draft that was kept; not a brief and not a verdict.

Each brief carries a `**Board:**` line (its board item's file, or
`none — <grounds>`) and a `**Status:**` line with an ISO date above its first
heading; `reviewscan` warns on a new file without them.

## Reading the folder

A cold reviewer is barred from prior verdicts until its own findings are
committed (`REVIEW.md` rule 2), and `tools/coldsweep.py` is the way to sweep the
tree without reading one by accident. Everyone else may read any file here.
This README is not a brief, and `reviewscan` treats it as one that is not.
