# Cold review (rule 4) — stampscan (S4), first-of-kind scanner review

**Subject (refs only):** `tools/stampscan.py` + `tools/test_stampscan.py` at
HEAD; the stamp-marker convention added to `docs/method/PROPAGATION.md` and
`docs/build/templates/CLAUDE.md`; the build commit `2fe97f3` and the
subsequent unwiring commit `4f637b0` — the scanner is currently **built but
wired into no plane**, and both that state and the commit that produced it are
part of the subject. Establish the full delta with `git log --oneline --
tools/stampscan.py docs/method/PROPAGATION.md .github/workflows/ci.yml`.
This is the scanner's **first-of-kind review**: whether and under what
precondition it may be wired at all is the review's call to recommend — the
decision is the principal's.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer (which
carries the author's scrutiny list — deferred below) and SESSIONS index
one-liners, and a git-log grep incidentally surfaced the *subject line* of a
withdrawn earlier pass on this item (quarantined under
`docs/reviews/withdrawn/`, wrong tier, not accepted — its findings are dead
and are not reading for this redo). Nothing evaluative from any of those
sources appears above the divider.

**The reviewer's first acts:** establish what the scanner is, what invariant
it enforces, and why it is unwired from the code, tests, and the two commits
yourself; name the load-bearing assumptions and attack surface as your own;
run all four lenses at the widest scope (`docs/method/REVIEW.md`). The marker
convention written into PROPAGATION.md and the child template is doctrine text
on the same footing as the code. Re-run every claim the commits and CHANGELOG
make — test counts, the live template-pair comparison, and the stated reason
for `4f637b0` (reproduce the failure mode it describes before trusting it).
Probe with crafted inputs of your own design, including documents that merely
*describe* the marker syntax.

**Re-run obligations:** `python3 -m unittest tools.test_stampscan` · run the
scanner over the live tree and over probes you construct ·
`python3 tools/floor.py --plane ci` · `python3 -m unittest discover -s tools` ·
`node --test instruments/*.test.js`. Lens 4: `/security-review` reaches only
pending diffs — on a landed delta discharge it in one explicit line with
grounds; the manual code-altitude pass (input handling, exit-code contract,
what a crafted document can make the floor do) is in scope regardless.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/` (quarantined). Do not grep git
history for review commits. Open the deferred section below — and the intent
record it names — only after your findings are durably written to this file;
then append the reconcile, named as such.

Findings carry stable IDs (**ST1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL**, severity counts, and an
explicit wiring recommendation with its precondition(s). The scanner and its
marker convention encode policy (doctrine by function): REVIEW.md rules 3–4
govern — findings are the principal's to decide; nothing is applied in this
pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* [`sessions/2026-07-22-1036-invariant-candidates.md`](../sessions/2026-07-22-1036-invariant-candidates.md) § S4.

*The author's scrutiny list from the queue pointer (a floor, never a fence):*
**(0) the wiring blocker, found in-run:** the marker parser recognises stamp
markers anywhere it scans — including prose and code spans that only
*document* the syntax — and treats a stray/unpaired marker as a hard config
error (exit 2) that `--warn` does NOT suppress, so even advisory wiring lets
ordinary docs about stampscan block the floor (a ROADMAP pointer describing
the markers reddened the floor mid-run; the CI step was reverted). Stated
precondition to wire: strip fenced/inline code before marker-hunting, as every
sibling scanner does. **(1)** the marker convention borders on a doctrine act —
`narrow=<reason>` declares a legitimate narrowing vs a silent drop
(mechanically identical subsequences) and needs explicit ratification.
**(2)** the stamp-end marker is appended inline to the `---` divider rather
than its own line — a placement compromise forced by a collision with
pre-existing `test_templates.py` slice logic (a cleaner fix teaches
`template_block()` to strip markers).

---

## Reviewer's attack surface (named first, before any probe was run)

Reviewer: cold rule-4 pass, Fable tier, worktree `atelier-review-2210-take` at
HEAD `9aef298`. Established independently from `tools/stampscan.py`,
`tools/test_stampscan.py`, the diffs of `2fe97f3` / `831ca05` / `4f637b0`
(restricted to non-quarantined paths), the current `.github/workflows/ci.yml`,
`tools/floor.py`, and `docs/method/PROPAGATION.md` +
`docs/build/templates/CLAUDE.md`. Load-bearing assumptions I intend to attack:

- **AS-A — "legitimately narrowed" = "declared `narrow=`".** The scanner trusts
  the mere presence of any non-empty token. Probe: does an empty stamped block
  with `narrow=x` (0 of N canonical lines kept) pass as clean/noted? Is
  "declared" a sufficient mechanical reading of the rule's word "legitimately",
  and is that reading a doctrine act that has been recorded as one?
- **AS-B — context-blind marker recognition.** `stamp:begin` matches at
  line-start only, but `stamp:end` is a bare `.search()` — any line merely
  containing the literal end token, in prose, a fence, or an inline-code span,
  reads as a stray end ⇒ malformed ⇒ exit 2, which `--warn` never suppresses.
  Reproduce the unwiring commit's stated failure mode with crafted documents
  that merely *describe* the syntax; test whether the stated wiring
  precondition (strip fenced/inline code before marker-hunting) is actually
  sufficient, and name its residual (a raw HTML-comment mention in bare prose).
- **AS-C — the test_templates placement compromise.** `---<!-- stamp:end -->`
  exists to avoid disturbing an unrelated frozen test's verbatim slice; the
  search-based end regex is the widened attack surface that placement bought.
  Is the coupling honest, and is the widening worth it?
- **AS-D — unconfined `source=` resolution.** `root / source` accepts `../`
  traversal and (via pathlib semantics) absolute paths — a crafted stamped doc
  can point the scanner at any file on the machine, and a drift hint prints one
  canonical line (`_first_offending_line`), an info-leak lever on a CI plane.
- **AS-E — propagation blast radius.** create-repo copies the template
  CLAUDE.md verbatim (markers included) into every scaffolded child, where
  `source=docs/method/PROPAGATION.md` cannot resolve ⇒ exit 2 in any child that
  ever runs stampscan. Registry wiring (`tools/floor.py`, ADR 0008 — enforcement
  propagates by call) would therefore red the estate at once, not just atelier.
- **AS-F — missing house furniture.** No `.stampscanignore` at root (every
  sibling's ignore file carries the `.claude/worktrees/` nested-worktree
  exemption; stampscan has none), no `tools/README.md` section, no `floor.py`
  registry entry, no CHANGELOG entry for the S4 build (S1/S5 got one), and no
  doctrine prose anywhere describing the stamp convention — only invisible
  markers landed in PROPAGATION.md and the template, for a mechanism the wiring
  commit itself called "borders on a doctrine act".
- **AS-G — stated-residual verification.** Fence-stripping is a first/last-line
  convention (single-line region edge, spaced info-string edge), the greedy
  two-pointer subsequence has a duplicate-line caveat, first region wins on a
  name collision — verify each header statement is true rather than assumed,
  and that the one live pair crosses none of them.
- **AS-H — claims audit.** 46/46 stampscan tests; 52/52-line live-pair
  identity (apex edits `572dddd`/`31b2ed0` postdate the markers — did both
  sides of the pair move in lockstep?); 548-test discover then / current count
  now; the byte-identity claim; the floor, instrument suite, and every re-run
  obligation in the brief.

---

## Verdict — cold rule-4 pass (Fable), 2026-07-26, HEAD `9aef298`

### What was re-run, with results

- `python3 -m unittest tools.test_stampscan` — **46/46 pass** (commit claim
  "46/46" verified exactly).
- `python3 tools/stampscan.py --selftest` — exit 0, all cases pass.
- `python3 tools/stampscan.py --warn --root . docs` (live tree) — **exit 2,
  5 config errors**: 4 from the quarantined withdrawn pass under
  `docs/reviews/withdrawn/` (10 literal marker tokens at HEAD, counted via
  `git show | grep -c` without opening the file) and 1 from this brief's own
  attack-surface section, whose inline-code quotation of the end marker
  tripped a stray-end the moment it was written — a live, unplanned
  demonstration of the failure mode under review. The one live pair
  (`docs/build/templates/CLAUDE.md:18` ↔ PROPAGATION.md region `floor`)
  reports **identical, 52 lines** — the "52/52" commit claim verified, and
  the apex edits that postdate the markers (`572dddd`, `31b2ed0`) kept both
  sides in lockstep.
- `python3 tools/floor.py --plane ci --root .` — exit 0, all nine registered
  scanners enforced and clean (one pre-existing sizescan size-advisory on
  ROADMAP, non-gating). stampscan is absent from the registry, from
  `.githooks/pre-commit`, and present in `ci.yml` only as an explanatory
  comment — the unwired state is exactly as `4f637b0` describes.
- `python3 -m unittest discover -s tools -p 'test_*.py'` — **694/694 pass**
  (548 at build time; suite has grown since — consistent).
- `node --test instruments/*.test.js` — **207/207 pass**.
- Failure-mode reproduction with crafted probes (scratchpad, outside the
  repo): a fenced example documenting the full marker pair → exit 2
  (missing-source); an inline-code mention of the end marker alone → exit 2
  (stray end); a raw begin marker at line start in prose → exit 2
  (unterminated); a mid-sentence begin mention → clean (begin is anchored at
  line start). `4f637b0`'s stated reason is accurate as written.
- Disposition probes: empty-payload stamp with `narrow=` → exit 0, reported
  "legitimate narrow — 0 of 3 canonical lines kept"; one-of-three with
  `narrow=x` → exit 0; `../` traversal and absolute-path `source=` both
  resolve outside `--root` and scan; a reordered child echoes one canonical
  line from the out-of-root file in the drift hint; duplicate-line greedy
  subsequence returns correct answers on adversarial inputs; two same-name
  regions → first wins, as stated; allow-marker bare-mention and
  empty-reason correctly do not exempt (DSR8 contract holds).

### Lens 4 mechanical floor

`/security-review` reaches only pending diffs; this is a landed delta
(`2fe97f3..4f637b0` on main) with nothing in-scope the scanner can be aimed
at — the only pending content in this worktree is this brief itself, which
REVIEW.md's SL2 caution bars from being scanned pre-reconcile. Discharged on
those grounds; the manual code-altitude pass (input handling, path
resolution, output echo, exit-code contract) ran in full and produced ST4.

### Findings

**ST1 — MAJOR (lens 2/1). Context-blind marker recognition reds any scan
that contains documentation of the syntax, and the `4f637b0` neutralisation
has already regressed at HEAD.**
Claim: the unwiring reason is real, reproduced, and *recurrent* — instance
neutralisation cannot hold the line.
Evidence: `tools/stampscan.py:207` (end marker matched by bare `.search()`
anywhere on any line) and `tools/stampscan.py:196-199` (begin anchored at
line start); probes P1a/P1b/P1d above all exit 2, and `--warn` never
suppresses exit 2 by design (`tools/stampscan.py:617-618`). At HEAD the
quarantined file `docs/reviews/withdrawn/2026-07-26-0647-stampscan-s4-cold.md`
carries 10 literal marker tokens (4 config errors), so the live tree already
exits 2 again three days after `4f637b0` "neutralised the two prose
mentions" — and this brief added a fifth within minutes of being written.
Counsel: the stated wiring precondition (strip fenced *and inline-code*
spans before marker-hunting, retaining stripped lines in payloads) fixes
both proven classes (P1a, P1b) and incidentally narrows ST4's input surface.
Pair it with a shipped `.stampscanignore` carrying the house net
(`docs/reviews/`, `.claude/worktrees/`) — review stores quote probe material
raw by nature, so the parser fix alone is not sufficient for this repo. The
remaining residual (a raw line-start HTML-comment marker in bare prose, P1d) is
defensible if named: rendered Markdown hides raw HTML comments, so genuine
documentation uses code spans.

**ST2 — MAJOR (lens 1). `narrow=` accepts narrowing to nothing: the entire
floor can be silently vacated with one token.**
Claim: the "declared = legitimate" reading has an unstated boundary case
that defeats the scanner's purpose.
Evidence: probe P2 — an empty stamped block with `narrow=we-dropped-everything`
exits 0, reported "legitimate narrow — 0 of 3 canonical lines kept";
`tools/stampscan.py:405-411` (any ordered subset, including the empty one,
passes with any non-empty `narrow` token; `_is_ordered_subsequence` at
line 340 is vacuously true for an empty child). The stated residual
(`tools/stampscan.py:118-122`) owns shallow trust in the *reason*, but
contemplates narrowing, not vacating — the floor block exists so doctrine
"binds even if atelier is never read", and a one-token declaration that
deletes all of it while reporting clean is a policy hole, not a residual.
Counsel: treat an empty (0-of-N) payload as drift regardless of `narrow=`;
consider whether a floor-class region should also carry a minimum-keep or
per-line rather than per-block narrowing. The wider question — is *presence
of a token* enough to make a drop "legitimate"? — is a doctrine call that
belongs to the principal, and should be recorded as one when ruled.

**ST3 — MAJOR (lens 3). The template now ships stamp markers that cannot
resolve in any scaffolded child, and nothing in create-repo knows they
exist.**
Claim: the propagation blast radius of wiring is unstated and currently
unsafe.
Evidence: `docs/build/templates/CLAUDE.md:18` pins
`source=docs/method/PROPAGATION.md` — a path that exists only in atelier;
`skills/create-repo/SKILL.md` copies the template and stamps placeholders
(steps at lines 39 and 124) with no mention of the stamp markers (no
`stamp:begin` match anywhere under `skills/`). A future child scaffolded
from this template that ever runs stampscan exits 2 (missing-source) — and
registry wiring (`tools/floor.py`, ADR 0008: enforcement propagates by
call) would make every child run it. Existing children predate the markers,
so they no-op — the exposure is every *future* scaffold plus any retrofit.
Counsel: before any `floor.py` registry entry, decide the child-side
resolution story — rewrite `source=` at scaffold time to the pinned
atelier path, or give stampscan a two-mode resolver (the reviews-template
re-stamp precedent in the CHANGELOG solved this same shape) — and teach
create-repo the markers are load-bearing scaffold content.

**ST4 — MINOR (lens 4). `source=` resolution is unconfined: traversal and
absolute paths escape `--root`, and the drift hint echoes canonical
content.**
Claim: a crafted stamped document can make the scanner read any file on the
machine and print one line of any file that carries matching region markers.
Evidence: probes P3/P3b/P3c — `source=../outside/…` and an absolute path
both scan successfully from outside `--root` (`tools/stampscan.py:479`,
`root / block.source` with no containment check; pathlib silently discards
`root` for an absolute right-hand side), and the reordered-child probe
printed `canonical='TOP-SECRET-LINE-ONE'` from the out-of-root file
(`tools/stampscan.py:373-385`). Exploitability is low today — the target
must carry region markers, and CI runs trusted commits — but the scanner is
estate-shipped, public, and will someday scan PR-authored docs.
Counsel: after resolving, require the source path to sit inside `--root`
(`resolve().relative_to(root)`) and fail as a config error otherwise —
matching the fail-safe posture the tool already takes everywhere else.

**ST5 — MINOR (lens 3/2). The convention that "borders on a doctrine act"
has zero words of doctrine, records, or roster.**
Claim: the mechanism's entire specification lives in a tool docstring and a
commit message.
Evidence: `docs/method/PROPAGATION.md` gained only the invisible region
markers (lines 98/153) — no prose names the stamp convention, `narrow=`, or
the declared-narrowing rule; `tools/README.md` has no stampscan section
(every wired sibling has one); CHANGELOG has no S4/S2 build entry (S1/S5
got a full one, "two more anti-slop scanners"); there is no
`.stampscanignore` (every sibling ships its ignore file with the
nested-worktree exemption). The wiring commit itself called the convention
"borders on a doctrine act" — it is currently a doctrine act recorded
nowhere on the doctrine surface.
Counsel: land the PROPAGATION.md paragraph (what a stamp is, what
`narrow=` means, who may declare it), the `tools/README.md` section, the
CHANGELOG entry, and the ignore file as part of the wiring act, not after
it.

**ST6 — NIT (lens 2). Small honesty and edge wrinkles, none load-bearing.**
Claim/evidence: (a) the duplicate-line caveat in STATED RESIDUAL
(`tools/stampscan.py:130-134`) overstates — a greedy two-pointer test is
exact for subsequence *membership*, and adversarial duplicate probes (P6)
return correct answers; an overstated residual errs safe but is still a
wrong claim. (b) Fence-stripping edges (P5): a region containing only a
fence line yields an empty canonical; an opener with a spaced info string
is not stripped; a single-backtick line is accepted as a closer — all
inside the header's named "looks like a fence delimiter" class, none
crossed by the live pair. (c) `render_human`
(`tools/stampscan.py:539-540`) joins note kinds without de-duplication
("identical, identical, …" for multiple clean stamps). Counsel: fix (a)'s
wording and (c) whenever the file is next open; (b) needs nothing until a
second live pair exercises it.

### What held

The exit-code contract (0/1/2; `--warn` never downgrades a config error) —
tests, selftest, live run and probes all agree. The disposition matrix
(identical / declared-narrow / silent-drop / reword-drift) behaves exactly
as documented, including narrow-does-not-excuse-rewording. The allow-marker
DSR8 contract (word boundary + non-empty reason) holds. The one live pair
is genuinely identical at 52 lines and survived two subsequent apex edits
in lockstep — the mechanism demonstrably works on production content. The
begin marker's line-start anchor keeps mid-sentence prose mentions safe.
Malformed stamps fail safe in all three shapes. First-region-wins and the
first/last-line fence convention behave exactly as the header states. Every
numeric claim in `2fe97f3`/`831ca05` re-ran true (46/46; 52/52; suite counts
consistent with growth). `4f637b0`'s stated reason reproduced precisely as
written — an honest commit.

### Verdict

**PASS-WITH-FINDINGS** — 3 MAJOR (ST1, ST2, ST3) · 2 MINOR (ST4, ST5) ·
1 NIT (ST6). The scanner's engine, tests, and honesty discipline are sound;
the unwired state is correct today and the unwiring commit's account is
accurate. The blockers are the wiring seam, not the core.

### Wiring recommendation

**Do not wire yet — not even advisory.** A config error survives `--warn`,
so any wiring today reds the floor on the quarantined review file alone
(proven live above). Recommend, in order:

1. **Advisory wiring in atelier's own `ci.yml` (hand step, like pathscan)**
   only after: (a) the parser strips fenced and inline-code spans before
   marker recognition (ST1); (b) a `.stampscanignore` ships with
   `docs/reviews/` and `.claude/worktrees/` (ST1); (c) the narrow-to-nothing
   hole is closed or the principal explicitly accepts it as a named
   residual (ST2 — a doctrine call, the principal's to make).
2. **Registry (`floor.py`) wiring — which reaches every child — only after**
   the child-side `source=` resolution story is decided and create-repo
   handles the markers (ST3), plus the doctrine/records furniture of ST5
   lands in the same act.
3. **Any blocking flip** remains a separate, later principal ruling after an
   advisory soak, per the house rollout discipline (wrapscan/datescan
   precedent).

Findings are counsel; nothing was applied in this pass. Decisions are the
principal's.

---

## Reconciliation — after opening the deferred section and the intent record

Read post-findings: the deferred scrutiny list above, and
`docs/sessions/2026-07-22-1036-invariant-candidates.md` § S4 (plus its V3
cross-reference). The withdrawn-directory ban was honoured throughout — the
quarantined file was never opened; only marker *counts* were taken via
`git show | grep -c`.

**Withdrawn: none.** All six findings stand as written.

**Confirmed independently (scrutiny item 0 ↔ ST1):** the wiring blocker was
reproduced from the code and probes before the deferred section was read, on
the same three vectors the author names — and **sharpened**: the
neutralisation approach has already regressed at HEAD (the quarantined
review file re-reds the live tree today, and this brief itself added
another instance while being written), so the parser precondition needs the
`.stampscanignore` companion; the surviving residual (raw line-start
markers in bare prose) is named rather than left implicit.

**Confirmed and sharpened (scrutiny item 1 ↔ ST2, ST5):** the author flags
`narrow=` as needing ratification; the pass adds the concrete boundary case
that makes ratification urgent — narrowing to *nothing* passes clean
(probe P2, "0 of 3 canonical lines kept", exit 0) — and ST5 documents that
the convention currently has zero words on the doctrine surface to ratify.

**Sharpened (scrutiny item 2 → ST7, new):** the author names the
`---` + end-marker placement as a compromise with a cleaner fix (teach
`template_block()` in `tools/test_templates.py` to strip marker lines).
The pass adds the causal chain that raises its priority: the placement is
*why* the end marker is matched by bare `.search()`
(`tools/stampscan.py:200-207`, the comment says so explicitly), and that
search-anywhere match is the widest single contributor to ST1's stray-end
class (probe P1b trips on an inline-code *mention*). Taking the cleaner fix
would let the end marker anchor to the line again, shrinking ST1's attack
surface at the parser rather than only filtering around it. **ST7 — MINOR:**
counsel the `template_block()` fix as part of the ST1 remediation, not as
deferred polish.

**Sharpened from the intent record (ST3):** the S4 seam reads "hash/compare
the stamped block against the **pinned** parent text". The built scanner
compares against the live file at `--root` — pin-blind. Inside atelier
(template ↔ PROPAGATION in one tree) that is equivalent; for a child pinned
at `atelier@<SHA>` it is not — the canonical text at the child's pin may
lawfully differ from atelier@main. ST3's precondition therefore gains a
requirement the intent record itself supplies: the child-side resolution
story must be **pin-aware**, not merely path-aware. Wiring recommendation
unchanged in shape; precondition 2 now explicitly includes pin-aware
resolution.

**Grounding check:** the docstring's three grounding findings
(`create-repo C3`, `method-layer P1`, `foundation Q2`) match the intent
record's occurrence list exactly — the scanner's stated grounding is
faithful to its source.

**Final count after reconciliation: PASS-WITH-FINDINGS — 3 MAJOR (ST1, ST2,
ST3) · 3 MINOR (ST4, ST5, ST7) · 1 NIT (ST6).**
