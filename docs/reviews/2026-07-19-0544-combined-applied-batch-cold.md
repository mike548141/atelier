# Cold review — the applied batch of the combined cold pass (F1–F9 rulings)

**Date**: 2026-07-19 · 0544 UTC · **Status**: brief written, review pending

## Spawn provenance (REVIEW.md rule 4)

This review is spawned by a session Mike opened fresh with "Do any review
work" — a session the applied batch's author (the 0407 pass's taking session,
which applied Mike's F1–F9 rulings) neither started nor instructed. That
applier queued the `⏳` pointer and wrote no brief, per rule 4 and the
applying-decisions clause. This brief is written by the taking session
(Fable), which authored neither the three original deltas, nor the 0407
verdict, nor the applied batch under review. The cold reviewer is a
fresh-context agent spawned by the taker. Claim: `599b631` on `main`; work on
`main` (tree clean, no parallel session).

## Subject (refs only)

**One commit, `9d95644`, reviewed at HEAD** — the application of Mike's
2026-07-19 rulings on the 0407 combined cold pass's findings F1–F9 (F1–F8
fixed, F9 accepted). An application review's special sequencing binds — see
Ask. In-repo delta:

- `docs/method/REVIEW.md` — the F6 enforcement-claim qualification.
- `docs/method/PRINCIPLES.md` — the F8 re-key off the build grammar.
- `tools/sizescan.py` + `docs/build/templates/workflows/floor.yml` — the F5
  gate-class wording change.
- `skills/review-brief/SKILL.md` — the F3 re-key + stamped-copy header.
- `tools/test_templates.py` — the F7 test additions (records claim suite
  267→274 green).
- `CHANGELOG.md`,
  `docs/sessions/2026-07-19-0111-review-trigger-commitment-not-artefact.md`,
  `docs/decisions/2026-07-19-0100-review-trigger-is-commitment-not-artefact.md`
  — the F2/F4 dated correction addenda (originals left standing).
- Hunks in `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`,
  `docs/sessions/2026-07-19-0407-combined-cold-pass-taken.md`, and
  `docs/SESSIONS.md` — **deferred material**, see the divider rule in Ask.
- ROADMAP restructuring hunks (the queue's state after application).

Machine-local, in scope: `~/.claude/skills/create-repo/SKILL.md` — the F1
stamp-step fix (fill + prove `<atelier-path>` across the whole stamped tree),
recorded as live-proven red and green in a scratch child.

## Ask

Review deep, not fast, all three lenses (`method/REVIEW.md` § What a review
actually checks): approach & assumptions — name and attack the load-bearing
assumptions yourself, as your **first act**; correctness & quality — does each
applied fix do what its ruling asked, any overclaim, any silent scope-cut, any
new defect the new wording introduces; completeness/harvest — did any fix land
short, and what should the application have touched that it didn't. The
framing of this brief is itself attackable.

**Sequencing — the application-review rule (REVIEW.md § Applying decisions to
doctrine), binding.** This delta includes hunks in the prior verdict file, so
rule 2 cannot be fully honoured; the doctrine's stated sequence applies:

1. Commit your own attack surface to the verdict draft **first**.
2. Review the edited doctrine/tools/records at HEAD (everything in the in-repo
   list above **except** the three deferred files) and **commit your findings**.
3. Only then open the deferred material — the 0407 verdict file (its findings,
   rulings, and decision stamps), the applier's session log
   (`2026-07-19-0407-combined-cold-pass-taken.md`), and the `SESSIONS.md`
   index entry — to **reconcile**: check each ruling F1–F9 against what was
   actually applied, and whether the application drifted from, softened, or
   overshot the ruling. Never to anchor. The residual exposure (you will meet
   the rulings' framing at reconcile) is named, not denied.

**Re-run every recorded proof in scope** — a proof you have not re-run is not
a proof you can close on. Recorded proofs include: the tool suite green
(`cd tools && python3 -m unittest` — records claim 274), `sizescan --selftest`,
the four scans clean at HEAD (secretscan, leakscan, linkscan,
`sizescan --check`), the F7 tests actually biting (prove at least one banned
phrase and one pinned invariant fails red when violated — use a scratch copy,
never the live tree), and the F1 claim ("live-proven both ways in a scratch
child": the old two-file grep passes with the reviews README unfilled, the
widened grep catches it, clean after filling) — rebuild that proof yourself in
scratch from the skill's current text.

**Verdict**: append below this file's `---` divider. Stable IDs **G1…** (the
prior pass used F1–F9; don't collide), severity MAJOR / MEDIUM / LOW, per-lens
coverage, spawn provenance repeated, your attack-surface commit named, every
re-run proof listed with its result. Apply **nothing** (rule 3 —
self-authored doctrine): findings go to the principal; the taker will add
non-author counsel but the decisions are Mike's. Cycle close rule: the cycle
closes only when a pass returns no MAJOR, on the principal's ruling; a
no-MAJOR pass here makes the terminal application close without a further
queued pointer.

---

## Deferred — open only after your findings are committed (step 3 above)

- `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md` —
  the prior brief, verdict, taker's counsel, and Mike's decision stamps (the
  rulings you reconcile against).
- `docs/sessions/2026-07-19-0407-combined-cold-pass-taken.md` — the
  taker/applier's own account of the application.
- The `docs/SESSIONS.md` index entry for that session.
- Prior verdicts in `docs/reviews/` — rule 2: reconcile-step only.
