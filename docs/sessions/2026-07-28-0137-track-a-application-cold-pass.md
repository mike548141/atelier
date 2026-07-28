# 2026-07-28 · 0137 UTC · Track A application cold pass taken (Fable)

**Seat:** Fable, worktree `atelier-review-0123-take`.
**Ask:** *"Please do any review work. There are parallel sessions so take
precautions"* — the rule-4 worked example: the principal opening a fresh
session and pointing it at the queue.

The one open reviewer-work item was the queued Track A application pass
(the other ⏳ markers all carry verdicts and await rulings, which are
Mike's). Claimed on `main` before any work per CONCURRENCY § Claiming
work, then taken in a worktree.

**Verdict: PASS-WITH-FINDINGS 1M/4m/4n** —
[brief + verdict](../reviews/2026-07-28-0123-track-a-application-cold.md).
All five ruled items (A1/A2/A3, LS1–LS5, A5b) verified faithfully
applied; every probe in the intent record's before/after table
reproduced live at HEAD; both suites (720 Python + 207 node) green with
and without a machine term list, re-run both ways.

**The MAJOR (TA1), proven live:** the new scope guard tests *existence*,
not *membership* — a declared `scope` path that resolves outside the
repo (`/etc`, `..`) still vacates a boundary check. A staged AWS
credential that blocks in the control run passes `✅ secretscan
enforced`, exit 0, when the repo declares `scope: {"secretscan":
["/etc"]}` — the staged-diff prefix filter matches nothing and an empty
match exits clean. The same commit series closes exactly this
lexical-vs-resolved gap for local `run` paths (LS3) but not for fleet
scope paths, and the guard's comment claims the class is shut. Findings
are queued for Mike's ruling (rule 3); the MAJOR keeps the cycle open,
so the application of these rulings earns a further cold pass.

Sequencing held: brief committed first, findings committed before the
intent record or either prior verdict was opened, reconcile written
after and marked as such. Unavoidable onramp exposure (the SESSIONS tail
entry) named in the brief, not denied.
