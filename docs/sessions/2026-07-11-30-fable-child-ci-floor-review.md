# 2026-07-11 · the child-CI-floor review: PASS-WITH-FINDINGS, the class finally closed (Fable)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 52+1 -->
- [2026-07-11 · the child-CI-floor review: PASS-WITH-FINDINGS, the class finally closed (Fable)](2026-07-11-30-fable-child-ci-floor-review.md) — the brief run cold, floor reproduced, numen logs re-read live, all nine assumptions probed. Headline: the d0870a4 masking fix closed the *instance*, not the class — secretscan+leakscan still hardcode-skipped `build`/`dist` (planted key in `docs/build/` scanned green, proven live), still phantom-succeeded on a nonexistent path (the L1 class), and the child ignore-file hatch was dead under exactly the floor.yml CWD (N1–N3, mirrored out from linkscan's reviewed patterns). floor.yml gains every-push triggers (a never-PR'd branch was scanned by nothing while the header claimed "every push"), a selftests step, and in-file FP-hatch docs (N4–N6). Six findings, all [fixed]+re-driven; suite 196→205. Floating `atelier@main` attacked and held (the fixes floating to every child bump-free is the argument); real-infra secret drive judged not owed (closed by composition). **Gate cleared**; follow-ups: numen re-copies floor.yml, atelier ci.yml shares the N4 trigger gap. Second review same session (related, no unreviewed dependency): the session-29 ceremony-calibration doctrine change (`cb37310`, merged as PR #2) — **PASS, no findings**; grounding probed not read (don't-stack genuinely un-codified pre-change; hygiene item 1's rationale was always pivot-cost), and this very session demonstrates both halves of the calibration.


The brief (`docs/reviews/2026-07-11-child-ci-floor.md`) run cold — a fresh
session that built none of it. Floor reproduced first (4 selftests, planted
`docs/build/` break flags exit 1, suite 196 OK, triad clean), both numen runs
re-read from the live GitHub logs (`29092514962` success, all three ✓;
`29092599385` failure, linkscan ✗ exit 1) — the record matched everywhere.
Then the nine assumptions attacked by probe, per the brief: damage it or
re-drive it, don't reason about it.

**The headline answered the brief's sharpest question against the work.**
"Does the fix close the class or just this instance?" — just the instance.
Three members of the same silent-success family were alive at review HEAD:

- **N1** — secretscan + leakscan still hardcode-skipped `build`/`dist`; a
  well-formed planted `AKIA…` key in `docs/build/` scanned **green**
  whole-tree. The layer d0870a4 unmasked for links was still masked for
  secrets and leaks — the two scanners whose false negative costs most.
- **N2** — both boundary scanners phantom-succeeded on a nonexistent path
  ("✓ clean", exit 0) — the exact L1 defect the linkscan review fixed in
  linkscan; licenscan already guarded.
- **N3** — the child's `.secretscanignore`/`.leakscanignore` hatch was **dead
  in exactly the floor.yml invocation**: unresolved `p.relative_to(root)`
  raised whenever CWD ≠ root and the fallback silently produced CWD-relative
  paths that no root-relative glob matches. The hook and ci.yml only worked
  because CWD == root there — correctness by coincidence.

Plus three in floor.yml itself: **N4** the header claimed "every push + PR"
while the trigger said `push: branches: [main]` — a never-PR'd feature branch
(already publication: the commit is on the remote) was scanned by *nothing*;
now every push triggers. **N5** no scanner selftests before the scans (ci.yml
runs them); added, with the empty-file residual stated honestly (an empty
`.py` passes `--selftest` exit 0 — bounded by atelier's own CI gating what
`main` serves). **N6** the false-positive hatches were undocumented where a
child would look — and pre-N3 the documented one didn't even work in CI; the
header now names both and that they travel with the repo.

All six [fixed] + re-driven same session: scanners mirror the reviewed
linkscan patterns (comment trail names this review), pinned by six new tests
across `test_secretscan.py`/`test_leakscan.py` + three new floor pins in
`test_templates.py` (suite **196→205** OK); planted key/IP in `docs/build/`
red both scanners; exact floor.yml commands re-driven on a scratch child from
the workspace CWD — secret in a child `build/` dir blocks, the ignore hatch
suppresses it, clean child passes 0/0/0.

**Judgement calls:** floating `atelier@main` attacked and **held** — the trust
root is identical (adopters point at their fork), what `main` serves is itself
gated, and this review is the argument: N1–N3 reach every child's next run
with zero per-child bumps; under a pin every child would still run the masked
scanners. Residual named (runtime-fetched code + private tree + egress;
accepted for a single-principal estate, re-opens with external committers).
The real-infra secret drive judged **not owed** — closed by composition (local
exact-command block + run 29092599385's scanner-agnostic exit-1-fails-job
mechanics); deliberately don't plant fake secrets in remote history.

**Follow-ups (not blockers):** numen re-copies floor.yml — the scanner fixes
float to it, the workflow-file fixes (N4–N6) don't; atelier's own ci.yml
trigger has the same N4 gap, take on next touch. **Gate cleared** — floor.yml
may roll to further children in its post-review form. CI watched green on
GitHub for the review commit (`29097784652`, 9s, 205 tests + triad ✓).

**Second review, same session (proportionate — related work, no unreviewed
dependency): the session-29 ceremony-calibration doctrine change (`cb37310`,
merged by Mike as PR #2) — PASS, no findings.** The light read its ROADMAP
item asked for, grounding probed not read: `don't-stack` is genuinely absent
from pre-change `docs/method/`, and hygiene item 1's original rationale was
always pivot-cost — the sharpening restores, not revises. The self-verifying
carve-out can't be over-read onto scanner-class changes (the
silent-failure-mode bullet catches them), and this session is the live proof
of both halves of the calibration: d0870a4 earned and *needed* its review,
the records-only edits around it earned none. Template hygiene line stays a
flagged follow-up (condensed, not contradictory).
