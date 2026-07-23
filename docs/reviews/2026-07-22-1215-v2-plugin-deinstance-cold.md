# Review brief — v2-plugin de-instance build + ADR (rule-4 cold pass)

- **Date/time:** 2026-07-22 1215 UTC
- **Reviewer:** fresh-context subagent (two-hop spawn — see provenance).
- **Subject:** the single commit `1516ae1` on branch `v2-plugin-deinstance`
  (checked out read-only at `/Users/mike/worktrees/atelier-v2-plugin-deinstance`):
  `skills/create-repo/SKILL.md` (new, relocated into the bundle),
  `skills/create-repo/instance.yaml.example`, `commands/worktree.md`,
  `commands/fleet-pins.md`, `skills/session-onramp/SKILL.md` wiring,
  `.claude-plugin/plugin.json` + `marketplace.json` (0.1.0→0.2.0),
  `CHANGELOG.md`, and
  `docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`
  — the queued pointer directs ADR + build reviewed **as one**.
- **Composition check in scope:** the delta was cut from `4da0340`
  (2026-07-21); `main` has moved ~130 commits since. Whether the delta still
  composes with current `main` (naming, cross-references, doctrine it cites)
  is part of the subject, not an aside.
- **Intent record:** the branch's `docs/SESSIONS.md` index entry and
  `docs/ROADMAP.md` delta — **deferred material**, not opened before the
  reviewer's findings are committed (REVIEW.md rules 1–2). No prior review of
  this delta exists.

## Spawn provenance (REVIEW.md rule 4)

The principal opened this orchestrating session and pointed it at the queue —
the worked example rule 4 names. The delta's authoring session (2026-07-21,
recorded in the commit) neither started nor instructed this session; this
taker authored none of the delta. QR1's chain-spawn caution checked on the
criterion itself: started-or-instructed, not authorship. **Exposure, named:**
the taker read the delta's commit message (an evaluative account) and the
1018 run's closing note on the stray worktree during its onramp. So the
review runs **two-hop** (the 2026-07-21 2208 precedent): this brief is
refs-only above the divider, and a **fresh-context subagent** is the
reviewer; its prompt carries refs only. The reviewer names its own attack
surface first; the deferred material and all session records stay closed to
it until its findings are durably committed.

## Status of the work

Self-authored doctrine (doctrine by function — the skill stamps behaviour
into other repos; the ADR forks ADR 0002 for plugin-only adopters).
**Findings are Mike's to decide** (REVIEW.md rule 3); nothing is applied by
this review; each finding carries plain-language what/why/likely-impact.

## Scope

Widest the work admits: the de-instancing design and its assumptions; the
ADR as doctrine; the skill wording future adopter sessions will obey; the
two commands as behaviour-stamping surfaces; consistency with sibling
doctrine at **current main** (PROPAGATION stamped-copy discipline, ADR 0002,
ECONOMICS, CONCURRENCY, REVIEW); manifest/version hygiene; the mechanical
floor re-run on the branch. No non-goals declared; nothing fenced off.

## Lenses

All four REVIEW.md lenses, both altitudes. Lens 4: the file class is
markdown/JSON config — if `/security-review` is definitionally empty here,
discharge on those grounds and weigh it as nothing; the manual lens-4 pass
still runs (an adopter-profile that stamps identity has real design-altitude
surface: what travels in a public bundle, what stays adopter-local).

---

## Deferred — reviewer opens only after its findings are committed

- Intent record: `docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`
  §context (the ADR's normative text is subject; its narrative context is the
  author's account), the branch's `docs/SESSIONS.md` entry, and the branch's
  `docs/ROADMAP.md` delta.
- The author's commit message for `1516ae1`.
- No seeded questions: the taker defers none (it has read only the material
  named above and declines to relay it).

---

# Verdict — v2-plugin de-instance cold pass (rule 4)

*Appended verbatim by the taker from the fresh-context reviewer's output,
2026-07-22 1221 UTC. Nothing edited beyond this preamble.*

**PASS-WITH-FINDINGS — 2 MAJOR / 3 MEDIUM / 1 LOW / 2 notes.** The design is sound: externalising the seven instance facts into an adopter-owned profile is the right cut, the rejected alternatives are genuinely worse, and the new bundle surfaces carry zero leftover identity (verified by grep, not asserted). The two MAJORs are gaps *inside* the accepted design, both on the bundled-adopter path the delta exists to open — the reviewer's counsel is that both precede merge, but per REVIEW.md rule 3 every finding here is Mike's to decide; nothing is applied by this review.

**Spawn provenance (repeated from the brief):** the principal opened the orchestrating session and pointed it at the queue — rule 4's worked example. The delta's authoring session (2026-07-21) neither started nor instructed this review; the taker authored none of the delta. The taker's named exposure (the commit message, the 1018 run's closing note) made the review two-hop: this reviewer is a fresh-context subagent whose prompt carried refs only. The reviewer named its own attack surface first and committed all findings to its draft before opening any deferred material; the ADR's §Context, the branch's SESSIONS entry, its ROADMAP delta, and the commit message of `1516ae1` were opened only at the reconcile step.

## Findings (most severe first)

**VP1 · MAJOR — the bundled-mode doctrine block is unimplementable as specified.**
*What:* `PROPAGATION.md` and the template `CLAUDE.md` (untouched by the delta — zero mentions of plugin or bundled mode) define one canonical block whose drift check is `git -C "<atelier-path>" log --oneline <SHA>..HEAD`. The skill orders bundled mode to stamp the plugin version into `<SHA>` and to "record in the block that drift is tracked by plugin version" — while also ordering "the block's canonical text is atelier's PROPAGATION.md … don't paraphrase it". No canonical bundled-mode block text exists anywhere in the tree.
*Why it matters:* every bundled scaffold forces the acting model to improvise doctrine wording — the exact divergence-by-neglect PROPAGATION forbids — and the stamped drift command is unrunnable with a version pin. The ADR's own Consequences say "the drift-check the stamped block carries must branch on which"; the build implements that branch nowhere an adopter can copy.
*Likely impact:* plugin-only adopters' repos are born with hand-invented variant blocks that drift per scaffold, in the keystone file the whole propagation model rests on.

**VP2 · MAJOR — signing posture is an eighth instance fact, not externalised.**
*What:* the skill bakes `git config commit.gpgsign true` (SKILL.md line 95). The ADR enumerates exactly seven externalised facts; signing posture is not among them and not a deliberate exclusion (confirmed against §Context at reconcile).
*Why it matters:* signing is a machine property — the comment says so itself. A plugin-only adopter with no SSH/GPG signing configured hits a failed commit at the skill's *own* step 7, first run, with no branch or ask in the skill.
*Likely impact:* the primary new path the delta exists to enable breaks at first use; the plausible model recovery is silently flipping signing off, contradicting the baked intent. Mitigating honesty: the CHANGELOG flags the bundled-mode scaffold as unexercised — the admission sits exactly where this defect lives.

**VP3 · MEDIUM — README contradicts the bundle it ships.** "What you get" still omits `create-repo`, `/atelier:worktree`, `/atelier:fleet-pins`, and line 100 still reads "`create-repo` and the fleet tooling follow in a later version" — false at 0.2.0. Post-merge the bundle's public front door disagrees with its own manifest; an adopter's first read undersells and misstates the release.

**VP4 · MEDIUM — the template-readability guard misfires verbatim.** `ls "$SRC/docs/build/templates/"` lists 11 entries (6 files + 5 directories); the skill says "should list ~19 files; anything less, stop and say so". Run as written, the stop-rule trips on every invocation (the recursive file count is 20, reachable only via `find`/`ls -R`). Also an ungrounded numeric that rots as templates change — a structural check (named must-exist entries) would not.

**VP5 · MEDIUM — the delta does not compose cleanly with current main (131 commits of drift).** `git merge-tree` reports conflicts in four files. Three are records (CHANGELOG, ROADMAP, SESSIONS — routine rebase work). The content-bearing one is `skills/session-onramp/SKILL.md`: main added the `queue-run` skill to the exact paragraph the branch restructured, so a branch-side resolution silently drops queue-run from the onramp's companion-behaviours wiring. Everything else composes: ADR 0002 exists under the cited name, all doctrine files the skill references exist at main, and the manifests conflict-free (main still 0.1.0).

**VP6 · LOW — the instance schema is stated twice and already divergent.** Inline in SKILL.md step 1 and in `instance.yaml.example` ("your-gh-account" vs "your-account", differing comments), and nothing in the skill references the example file. The N-copies pattern the ADR's own Rejected section forbids, in miniature.

**VP7 · note (downgraded from LOW at reconcile) — the superseded baked-identity skill is still live.** `~/.claude/skills/create-repo` still carries Mike's identity; post-merge two create-repo skills coexist. The ROADMAP delta explicitly tracks its retirement as owed-after-merge, Mike's call — so this survives only as confirmation, not as a gap.

**VP8 · note — malformed markup, SKILL.md line 82:** `(e.g. *"stamp `git_identity`"`)` — stray backtick/asterisk, unclosed emphasis.

## Mechanical floor (branch worktree, read-only; invocations lifted from the branch's ci.yml)

| Check | Exit |
|---|---|
| leak/secret/licen/link/sign/size scan `--selftest` | all 0 |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 0 |
| `node --test instruments/*.test.js` (fail 0) | 0 |
| `secretscan --root . .` · `leakscan --root . .` | 0 · 0 |
| `licenscan --expect Apache-2.0 .` · `linkscan --root . .` | 0 · 0 |
| `sizescan --check --root . .` | 0 |
| `worktree.py --selftest` · `pins.py --selftest` (record's claim, re-run verbatim) | 0 · 0 |
| Composition extra: current **main's** `reviewscan.py --root . .` over the branch tree | 0 |

`/security-review` discharged with grounds: landed-delta review with no pending diff to aim it at, and the subject's file class (markdown/JSON/YAML example) is barred by the scanner's exclusions — a pass would be definitionally empty and is weighed as nothing. The manual lens-4 pass ran at design altitude instead: the profile collects identity only, no tokens (remote auth stays in the `gh` CLI), lives outside every repo, and the hook's trust note is present — clean apart from VP2.

## Reconcile (deferred material opened only after findings were committed)

Opened: ADR §Context, the branch SESSIONS entry, the branch ROADMAP delta, the commit message of `1516ae1`.

- **VP7 downgraded LOW → note** — retirement of the global skill is explicitly tracked in the ROADMAP delta and repeated in SESSIONS and the commit message. Recorded here as a change, not silently rewritten.
- **VP2 sharpened, stands** — §Context enumerates the seven facts precisely; signing posture is absent, confirming a miss rather than a deliberate exclusion.
- **VP1, VP3, VP4, VP5, VP6, VP8 stand unchanged** — nothing in the deferred material addresses them.
- **Claims re-run:** "Floor green (4 scanners + 2 tool selftests)" reproduces at branch HEAD (all exits 0, tool selftests run verbatim); the "two placeholder-email leakscan hits allow-marked" account matches the two `leakscan:allow` comments observed in the delta.
- Nothing overturned; nothing added beyond the VP7 downgrade.

---

## Decisions (Mike, 2026-07-23 — per-finding walk-through)

- **VP1–VP6, VP8 — [fixed] as counselled**, ruled individually after a
  per-finding what/why/impact walk-through. Applied as one commit
  (`ff8a07f`, worker-built on the branch rebased to current main —
  ~155 commits absorbed, the session-onramp resolution keeping both the
  queue-run wiring and the branch's restructure, grep-proven), merged
  `0de6f52` on Mike's merge-on-green ruling. Bundle 0.1.0→0.2.0 shipped.
- **VP7 — confirmed as counselled**: the superseded baked-identity global
  skill was retired the same day post-merge (archived machine-locally,
  outside this repo).
- **The application is itself self-authored** (built by the orchestrating
  session's instructed worker) ⇒ its rule-4 cold pass is **queued on the
  ROADMAP**; this session may not spawn it. Old→new SHA mapping for the
  record: the reviewed delta `1516ae1` was rebased to `2271a44`; the
  application sits atop it as `ff8a07f`; the superseded remote branch was
  deleted after merge (its content is fully carried by the merge).
