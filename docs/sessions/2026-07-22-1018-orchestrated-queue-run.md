# 2026-07-22 · 1018 UTC · Orchestrated queue run — wave 1 (Fable orchestrator, Opus/Fable workers)

**Shape:** Mike opened this session and pointed it at the shared queue ("progress
any work you can without me"), Fable orchestrating from the primary checkout,
workers in worktrees — the queue-run pattern the ROADMAP ratified 2026-07-22,
run live while its doctrine build is still queued (that build is a wave-2 item
for this run). Per-item close throughout: each item merges, pushes, and records
before the next report, so a session-limit cut loses at most the in-flight item.

**Rule-4 standing:** this session authored none of the queued `⏳` delta
(`caa85fe`) and was spawned by the principal with a generic queue instruction —
the worked example REVIEW.md rule 4 names as an eligible taker. The review
worker's brief and verdict carry the provenance statement.

## Wave 1 — claimed 1018 (commit `9e7e031`)

| Item | Worker | Worktree | State |
| --- | --- | --- | --- |
| ECONOMICS.md rename + ref sweep (decided, execution-only) | Opus | atelier-econ-rename | in flight |
| SECRETS/ACCESS `⏳` cold review (rule 4) | Fable | atelier-secrets-review | in flight |
| Security canon gap map (records-only) | Opus | atelier-sec-gap-map | in flight |
| ccarchive `--restore` full + delta | Opus | atelier-ccarchive-restore | in flight |

Wave 2 (queued, unclaimed until started): queue-run doctrine + skill (ratified —
waits for the rename so it lands citing `ECONOMICS.md`), then candidates by
economics: anti-slop registry mining, ccarchive dataless-awareness / manifest
signing, ccrepo reconciliation drift, the two ccarchive/cctranscript open
questions.

## Observations at open

- 🚩 **Stray worktree `atelier-v2-plugin-deinstance`** (branch
  `v2-plugin-deinstance`, one commit ahead of main: "plugin: de-instance
  create-repo, add worktree + fleet-pins commands (v2)", based on `4da0340`,
  clean tree). No `[~]` claim on the v2 item, no session record mentions it —
  either a live parallel session that skipped the claim step, or an orphan
  from a cut. Left untouched per stay-in-your-lane; the v2 item is out of
  bounds for this run; disposition is Mike's (resume it, or salvage → tag →
  delete per CONCURRENCY put-away).

## Per-item closes

**1030 · Security canon gap map — landed.** Worker (Opus) delivered
`sessions/2026-07-22-1025-security-canon-gap-map.md` (`be737aa`, merged
`--no-ff`): every canon source consulted live, every "already held" claim
verified against the cited doc. A/B/E confirmed narrow, C confirmed-reframed
(zero-dep is the unnamed control; residual = mutable-tag CI actions), D
dismissed to the instance layer. Honesty catch worth naming: the ROADMAP's own
"already held" list overclaimed the anti-slop promotion rule (captured, not
doctrine) — corrected at close. Follow-up queued: doctrine edits for A/B/C/E,
first slice SHA-pinned actions + SECURITY.md. Floor scanners re-run green on
main post-merge (orchestrator's first run used a wrong flag and read exit 2 as
suspect — invocation corrected against the hook, then clean; named per the
check-exit-codes rule). Worktree put away.

**1035 · SECRETS/ACCESS `⏳` cold pass — landed, cycle closed.** Taker (Fable
worker) met the delta cold: brief + findings committed (`092db29`) before the
intent record or reconcile (`7b6c935`), provenance stated in brief and verdict.
**PASS-WITH-FINDINGS 0M/4m/4L/1n** — terminal, cycle closed. Citations
re-verified against live sources (NIST 800-63B rev 4 confirmed final
2025-07-31; OWASP store/rotation/audit-trail confirmed; one Appendix-A
rationale verified in substance only, named). Live-proven claims re-run clean
at HEAD. Reconcile overturned nothing; the reviewer noted SA1's gap originates
in the in-conversation ruling itself, so Mike's ruling sits at the ruling's
level, not the text's. 🎯 SA1–SA8 (+ a spelling nit) queued for Mike.
Worktree put away.

**1032 · ECONOMICS.md rename — landed.** Worker (Opus) executed the decided
rename (`b639513`, merged `--no-ff`): `git mv` on canonical + child-template
copies, 24 refs across 16 live files, history untouched. Worker judgement
call, endorsed at merge: the child-template copy renamed too (in the sweep's
stated scope; `create-repo` globs the dir, so scaffolds pick it up
transparently). Proofs: linkscan clean before/after + in-hook, 323 tool tests
green incl. template block-sync, re-proven post-merge by the orchestrator.
Cross-repo recon (read-only): nothing dangles — children resolve against
pins; per-child atelier-pointing refs update at next pin bump; ros keeps its
own counterpart's name (its own 2026-07-22 record anticipated this). ⚠️ ros
tree observed with one modified inventory YAML (unrelated file) — possible
live ros session; nothing touched there. Worker also caught and corrected a
staging hazard mid-flight (git add aborting on renamed pathspecs left content
edits unstaged while renames staged) — verified the index before committing.
Worktree put away.

**1042 · ccarchive restore (full + delta) — landed.** Worker (Opus) built the
inverse of `--audit` (`9ca1425`, merged `--no-ff`): one engine, two shapes
(`--restore`, `--restore --delta` off the audit's mutated/pruned/renamed
buckets), content-first safety (grown = byte-prefix ⇒ never a target; newer
diverged live refuses unless a loud `--force`; zip-slip containment; additive
only — the renamed bucket re-materialises the old path and never deletes the
live rename). Suite 46→63/109 green — re-run by the orchestrator post-merge
(first orchestrator invocation ran `node --test` on the whole dir and
false-failed; corrected to the test files). Live fixture run exercised
refuse/force/grown paths with matching exit codes. Wave 2 launched in
parallel: queue-run doctrine + skill, anti-slop corpus mining, ccrepo drift
(claims `77f1037`). Worktree put away.

**1105 · Queue-run doctrine + skill — landed; rule-4 `⏳` queued.** Worker
(Opus) built the ratified pattern (`343def8` + `8111e9f`, merged `--no-ff`):
CONCURRENCY capstone section (96 lines) + ECONOMICS tier-split subsection
(22 lines) — section-not-file settled on actual size as ratified — and the
plugin-bundled `queue-run` skill (auto-discovered like review-brief; no
manifest change, verified against how review-brief travels). The stale
interruption-resilience pointer to "(ROADMAP)" rewired to the new section.
Orchestrator read the full doctrine diff and skill before merging; linkscan
clean, 323 tool tests green post-merge (worker ran the suite via `unittest`
— pytest absent on system python; identical TestCase suite). Self-authored
doctrine: the worker drafted the `⏳` pointer, the orchestrator queued it —
neither this run nor its workers may take that review (rule 4; stated on the
queue line). The meta-note worth keeping: the run built its own doctrine
while running the pattern, so the intent record doubles as the delta's
second live bearing.

**1052 · ccrepo reconciliation drift — landed.** Worker (Opus) traced the
whole sonnet-5 residual to one defect class (`75bba4c`, merged `--no-ff`):
last-wins dedup kept trailing partial/zeroed usage lines the logs re-emit,
silently dropping tokens; richest-record-wins recovers them and matches
ccusage exactly on a frozen matched-session set — per-model drift 0.00%
across the board, only in-flight variance left. `server_tool_use` measured
all-zero live → per-call pricing not built and the v1 hypothesis retracted
in the design doc (honesty: measured-false, not quietly dropped). Bonus
catch: per-model reconcile was comparing unmatched session sets, smearing
window-edge sessions into phantom per-model deltas — now scoped to matched.
Suite 92→94 (111 instruments-wide, re-proven post-merge). Worker isolated
the moving-target artefact (this very session writing logs during
measurement) before attributing drift — the discriminating-evidence
discipline holding in the small. Worktree put away.

**1115 · Anti-slop invariant candidates — landed.** Worker (Opus) + five
parallel miners read the whole review corpus (330 findings, 47 review files,
plus the sessions/ROADMAP-DONE disposition sweep — near-total double-homing
confirmed, reviews kept primary) and applied the >2 promotion rule with cited
IDs (`84fb112`, merged `--no-ff`): 5 scanner candidates (S1–S5) + 7
verifier/checklist candidates (V1–V7), below-threshold classes named rather
than rounded up. Sharpest results: the wrap class shipped three consecutive
cycles (SL7→AC1→IR3) — the clearest scanner case; "artifact" appears 15+
times in method/ against the NZ-English rule (caught twice — the
eye-skips-what-a-scanner-catches premise in one word); and
fail-open/detector-edge (~23) kept recurring *after* the selftest floor
existed — flagged ⚠️ as "harden tools/ tests", not "solved". The worker
survived one mid-flight API drop (resumed from transcript; nothing lost —
its worktree was verified clean before resume). 🎯 S1–S5/V1–V7 rulings
queued for Mike. Worktree put away.
