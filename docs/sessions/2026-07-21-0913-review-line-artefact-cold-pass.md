# 2026-07-21 · 0913 UTC · the review-line artefact cold pass: PASS 0M/1M/5L, rulings to Mike (Fable)

Mike: "Please do any review work." One `⏳` sat in the queue — the review-line
artefact delta (`fa7a90f`: `tools/reviewscan.py` + templated `Review` field +
wiring + `REVIEW.md`'s per-surface enforcement re-statement). This session
qualified as a rule-4 taker (Mike-spawned, authored none of the delta), claimed
on `main` (`921cc1a`) before touching anything, and ran the full cycle in
wt: review-line-artefact-cold-pass — parallel sessions were live (Mike's
warning, and a REACH-rulings claim landed on `main` mid-pass).

**The cycle, in order:** taker-written brief committed cold (`baff8b6`) — seven
named assumptions, deferred material listed, spawn provenance stated; probes
and proofs run; findings committed (`ed478ee`) *before* any deferred material
was opened; reconcile appended (`d335a3a`) with one further finding from the
deferred material itself, flagged as post-commit discovery.

**Verdict: PASS — 0 MAJOR / 1 MEDIUM / 5 LOW**
(`docs/reviews/2026-07-21-0913-review-line-artefact-cold.md`). Every recorded
proof reproduced live: 293 tests OK (the 284→293 claim), selftest OK,
whole-tree scan green with the intent record as the one post-boundary record
(dogfood holds), red/green legs re-driven in scratch, boundary edges
(pre-boundary / retired-scheme / README / template / templates-tree) all
correctly skipped, pre-commit fail-closed. The build is sound: presence-only
is the right depth, the decisions-dir scope honours the 0820 rejection, the
filename-date boundary is the SIGN_BOUNDARY shape. Findings: **RS1 (MEDIUM)**
the §14 silent-success class on the natural hand-run — `reviewscan --root .
docs/decisions` (or a single record file) scans nothing and exits 0 green,
probed both legs; wired invocations unaffected. **RS2** fenced `review:`
false-greens; **RS3** empty `**Review**:` passes (a blank in the field's
clothes); **RS4** backdated-filename escape + all-caps `REVIEW:` reds, stated
residuals; **RS5** REPO-STANDARD:94's scanner enumeration stale by three
scanners (pre-existing, widened by this delta); **RS6** the 0820 addendum was
spliced mid-note, orphaning the prior note's closing sentence. Positive
compliance note: this cycle's queue pointer was the first to honour rule 4's
refs-only ceiling — the point-of-use fix worked on first exercise.

🎯 **Rulings owed (rule 3): RS1–RS6 are Mike's** — counsel per finding in the
verdict; nothing applied by this pass. No MAJOR ⇒ per the close rule, the
applying session closes the cycle without a further full ceremony.

**Session hygiene worth recording:** two mid-turn prompts arrived that Mike
then identified as pasted from a previous session, not from him — one pointing
at PR #13 (the v2 plugin de-instance) as a review subject, one reporting a
`worktree.py list` mislabel bug. Neither was acted on: PR #13 was inspected
only to title + file list (enough to establish a different strand; no ⏳
queues it), and the bug report was left unlogged as unverified. Both handed
back to Mike to re-issue if current.

## Addendum 2026-07-21 1110 UTC — accept-all applied, cycle closed (same session)

Mike: *"I accept your recommendations on all these."* Applied as a **terminal
application** (no-MAJOR pass ⇒ the counsel's author applies, no further
pointer — the REACH `87af9f9` shape): claim `8815f40` on `main` first
(push deferred by a machine-wide network outage at claim time, named
honestly), then wt: review-line-rs-apply, landed `c06c0a4`. RS1–RS6 all
[fixed] with every leg re-driven live — dir/file-direct red (exit 1, was
silent 0), fenced-only red, empty-value red, all-caps green — suite
**293→298**, selftest OK, floor scans clean. Decisions stamped in the
verdict's dated addendum; item harvested to ROADMAP-DONE; CHANGELOG closed.

Two operational notes for future sessions: (a) a scan run from the primary
checkout while a worktree lives under `.claude/worktrees/` walks into that
checkout's tree and double-counts its files — transient, benign, but it
explains a "2 records" count that puzzled this session for a minute;
(b) the outage also produced Mike's API error — same cause, not a repo
matter.
