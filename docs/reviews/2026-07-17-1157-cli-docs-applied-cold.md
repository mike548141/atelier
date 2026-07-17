# Cold review — CLI-docs standard, the F1–F7 applied batch

**Scope:** the CLI-docs hunks of application commit `e6a295e` (2026-07-17) —
the rulings of the first cold pass applied to doctrine and instruments:
`build/REPO-STANDARD.md` (the CLI-docs convention hunks: scope predicate,
anti-drift wording, the `--help` letter), `instruments/README.md`,
`instruments/ccarchive` (the `--help` register), `instruments/ccarchive.test.js`
(the superset drift test), `instruments/install` (stale-owned-link cleanup
pass), `instruments/man/ccarchive.1`, and `.github/workflows/ci.yml` (guarded
mandoc step). Review the edited doctrine **at HEAD** plus those hunks. The core
question of an applied-batch pass: **does the new wording faithfully implement
the principal's rulings — no drift, no overreach, no silent miss — and is it
sound doctrine in its own right at HEAD?**

Out of scope: the ccarchive F1–F4 hunks interleaved in the same files — that
cycle is CLOSED (0 MAJOR, terminal application closes without a queued
pointer). They matter here only where they interact with CLI-docs claims
(e.g. new flags owing `--help`/man coverage under the superset relation).
Record hunks (`ROADMAP`, `SESSIONS`, session/review files) are context, not
target — but see sequencing: the review-file hunks stay closed until your
findings are committed.

**Sequencing (REVIEW.md rules 1–2, application-review form):** (1) read this
brief **only above the first `---` divider** (use a limited read); (2) review
the doctrine at HEAD and the scoped delta, naming and attacking the
load-bearing assumptions yourself, and **write your attack surface and findings
durably into the verdict section of this file first**; (3) only then open the
deferred section below the divider, the prior verdict + `§ Decision` in
`reviews/2026-07-17-1000-cli-docs-standard-cold.md`, and the intent record
`sessions/2026-07-17-0958-three-queued-cold-reviews-taken.md` — reconcile,
never anchor: check the application implements each ruling as decided. An
application review cannot fully honour rule 2 (the delta carries the prior
verdict's decision stamps); that residual exposure is named, not denied — keep
those hunks unopened until your findings are committed.

**Spawn provenance (rule 4, tested against the delta's author — the applier):**
this brief is written by a **non-author** taking session that Mike (the
principal) opened fresh and pointed at the queue ("do any review work queued");
the applier session (Fable, intent record above) neither started nor instructed
the taking session or this reviewer. The reviewer is a cold spawn of the taking
session, which authored neither the doctrine, the prior verdict, nor the
applied delta. Disclosure: the taking session read the intent record and the
prior verdict file in full to scope this brief; above-the-divider text is kept
to scope and refs. The verdict must repeat this provenance.

**This is self-authored doctrine (by function):** all findings are the
principal's to decide (rule 3) — record counsel per finding, labelled as the
reviewer's counsel; apply nothing.

**Re-run live proofs in scope:** the application claims 247 tool tests · 75
instrument tests · mandoc lint clean · sizescan · linkscan · scan triad all
green; the superset drift test present and green; the installer cleanup pass
proven in throwaway XDG dirs (stale owned links removed, real tools kept) and
the live `~/.local/bin` residue (`fixtures`, `browser-fetch`) gone. Re-run
what falls in scope, including a fresh installer drive into throwaway XDG dirs
with a planted stale owned link.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict to this file below the second
`---` divider.

---

## Deferred — refs (open only after your attack surface and findings are committed)

No seed questions were queued this time (the `⏳` pointer was refs-only, per
spec). Refs for the reconcile step:

- Prior verdict + rulings: `docs/reviews/2026-07-17-1000-cli-docs-standard-cold.md`
  (findings F1–F7, reviewer's counsel, and `§ Decision` — Mike ruled all seven
  [fixed] as counselled).
- Intent record: `docs/sessions/2026-07-17-0958-three-queued-cold-reviews-taken.md`
  (the taker/applier's account, including its application highlights — the
  author's claims to test, not settled scope).

---

## Verdict — cold reviewer, 2026-07-17 (UTC)

**Provenance (rule 4, repeated per the brief):** this reviewer is a cold spawn
of the taking session — a session Mike opened fresh and pointed at the queue —
which authored neither the doctrine, the prior verdict, nor the applied delta;
the applier session neither started nor instructed the taking session or this
reviewer. The taking session read the intent record and prior verdict to scope
the brief; this reviewer had read **only the brief above its first divider**
when the attack surface and findings below were formed and written.

**Sequencing disclosures:** (a) read brief lines 1–65 (stopping at the deferred
heading), then `grep -n '^---$'` for divider line numbers and lines 76–77 (a
blank and the final divider) to find the append point — no deferred content, no
prior verdict, no intent record opened before this section was written.
(b) The brief says append with the Edit tool; Edit needs a unique anchor and
`---` appears twice, so this section was appended by shell redirection instead
— same durable write, different tool. (c) The e6a295e commit message (read via
`git show`, needed to identify the CLI-docs hunks) itself summarises all three
batches; that summary is applier-authored framing and was treated as claims to
verify, not ground truth.

### Attack surface (named before any deferred material was opened)

1. **Scope predicate** — is "installed onto an operator's machine" a real
   boundary, or a rationalisation of the current gap (no pages on `tools/`)?
   Attacked by checking `tools/` `--help` quality, instruments' own conformance
   at HEAD, and whether the two page-less installed CLIs are honestly tracked.
2. **The `--help` letter vs its own exemplar** — does ccarchive's help at HEAD
   satisfy the reworded letter (one-line synopsis, flat options, one-breath
   closing)?
3. **Superset relation** — actually pinned mechanically? Test soundness: roff
   `\-` normalisation, flag-extraction regex, substring matching, flag count.
4. **Installer cleanup** — can the ownership test delete something it doesn't
   own (foreign links, real files) or miss stales (directory links from the
   historical bug, `*.md`-named links, relative targets)? Idempotence of the
   re-run. Driven fresh in throwaway XDG dirs, not taken on trust.
5. **MANPATH claim** — the doctrine now asserts PATH-derived manpath with
   hard-set `MANPATH` as the gotcha; tested empirically, not accepted.
6. **CI mandoc guard** — honest gate or ceremony? What does the step actually
   do on ubuntu-latest?
7. **Interaction boundary with the closed ccarchive cycle** — every new flag
   and every new non-zero exit path owes coverage in both registers under the
   superset relation; checked exhaustively against the man page.
8. **Proof-floor claims** — all re-runnable at HEAD, re-run rather than read.

### Findings

- **F1 (MEDIUM) — man page `EXIT STATUS` is stale against HEAD behaviour; the
  layout-drift alarm is absent from the page entirely.** An ordinary run now
  exits 1 on a refused shrink, on a repo dest, and on the empty-source alarm;
  `EXIT STATUS` still reads "0 on success … `--verify` exits 1 … (any mismatch
  or missing file)" — naming none of the three run-mode failures and omitting
  `UNMANIFESTED` from the verify causes. Worse, the empty-source/layout-drift
  alarm appears nowhere in the man page (README only): an operator whose
  scheduled run starts failing consults the full reference and finds no mention
  of that exit. Under the standard's own superset doctrine the page must carry
  what the tool does. *Counsel:* enumerate the non-zero exits in `EXIT STATUS`
  and give the layout-drift alarm a sentence in `DESCRIPTION` or `INTEGRITY`.
- **F2 (MEDIUM) — the CI mandoc step never lints in CI.** ubuntu-latest ships
  no mandoc, so as merged the step's only CI behaviour is echoing
  "unavailable". The in-line comment keeps it honest, but the gate is phantom
  in the one place it is wired, and the cheap real alternative —
  `apt-get install -y mandoc`, seconds, free Actions minutes on a public repo —
  is neither taken nor named as rejected. *Counsel:* install mandoc in the step
  (or record in the comment why not); until then roff lint is enforced only by
  unhooked local discipline.
- **F3 (LOW) — installer cleanup asymmetry.** The man-link cleanup pass sits
  inside `if [ -d "$BIN_DIR/man" ]`, so retiring the whole `man/` dir would
  strand stale owned man links forever, while the bin pass runs
  unconditionally. (Also: ownership only recognises absolute targets — a
  relative owned link is never cleaned; conservative, worth a comment at most.)
  *Counsel:* hoist the man cleanup out of the guard to mirror the bin pass.
- **F4 (LOW) — the letter still slightly under-describes its exemplar.** The
  reworded letter allows "at most a one-breath closing line"; the exemplar
  ships a two-sentence, three-line closing block. Small residual gap — the next
  tool's author must guess whether two sentences pass. *Counsel:* "a closing
  line or two" in the letter, or trim the exemplar's closing to one sentence.
- **F5 (LOW) — README wording vs trigger.** README says the zero-transcript
  alarm fires "against a non-empty archive"; the code keys on a non-empty
  *manifest*. Divergent only when the manifest is lost and the source moves in
  the same window. *Counsel:* say "non-empty manifest", or leave; a note only.

### Attacked and held

- **Installer cleanup proven fresh** in throwaway XDG dirs: planted stale owned
  link, stale owned *directory* link (the historical bug shape), and owned
  `.md`-named link all removed; foreign bin link, real file, and foreign man
  link untouched; stale owned man link removed; all three tools plus
  `ccarchive.1` linked; second run idempotent. Live `~/.local/bin` holds
  exactly the three tool links (no `fixtures`/`browser-fetch` residue);
  `man1/` holds `ccarchive.1` only.
- **Superset drift test** sound and green: `\-`→`-` normalisation correct, all
  11 flags captured including the sub-flags of `--install-schedule`; substring
  matching is a theoretical false-pass only.
- **MANPATH doctrine claim verified empirically**: PATH-derived lookup finds
  the page; hard-set `MANPATH` loses it; colon-suffixed `MANPATH` merges and
  still finds it. The doctrine's "hard-set … overrides" is accurate as worded.
- **Scope predicate grounded, not rationalised**: `tools/` scanners carry
  argparse-quality `--help`; the two page-less installed CLIs are named
  honestly (README "converging", ROADMAP rollout item) rather than papered
  over.
- **New flags fully covered**: `--force` and `--allow-repo-dest` present in
  both registers; `--help` is 20 lines — one screen.

### Proofs re-run (all green)

247 tool tests (`unittest discover`, OK) · 75 instrument tests (`node --test`,
0 fail — includes the superset drift test and the four contract tests for the
new guards) · `mandoc -T lint` clean · secretscan, leakscan (structural+local),
licenscan (Apache-2.0), linkscan, sizescan `--check` all clean **on a clean
export of HEAD**. Disclosure: on the *working tree* secretscan reports 29
findings, all inside untracked `.claude/worktrees/fable-review/` — a leftover
review worktree's copies of the scanners' own test fixtures. Machine-local
residue, not HEAD content, not a delta finding; flagged for hygiene (the
stale worktree also defeats any full-tree local scan until removed).

### Reconciliation (deferred section, prior verdict + § Decision, intent record — opened after the findings above were committed)

The deferred section was refs-only as specced — no seed questions to fold in.
Ruling-by-ruling, prior verdict `2026-07-17-1000-cli-docs-standard-cold.md`
against the applied delta:

| Ruling | Applied as decided? |
|---|---|
| F1 scope predicate | ✅ Drawn exactly as counselled (installed-onto-a-machine ships both; in-place scripts owe `--help` only; `tools/` exclusion stated; tied to the sizing table's row — the row exists, line 38, and the tie-in is coherent) |
| F2 superset test | ✅ Test present and green (flag-extraction regex equivalent to the counselled one; all 11 flags pinned); doctrine sentence added ("where the repo has tests, pin the superset relation mechanically") |
| F3 `--help` letter | ✅ Amended verbatim to the counselled phrase ("one-breath closing line…") |
| F4 README tense | ✅ "are converging on" — overclaim gone |
| F5 installer cleanup | ✅ Both passes present (bin + man1), ownership test as counselled; re-proven here in fresh throwaway XDG dirs incl. the historical dir-link shape; live residue confirmed gone |
| F6 MANPATH scoping | ✅ Applied nearly verbatim; verified empirically here (derived found / hard-set lost / colon-suffixed merged) |
| F7 guarded mandoc step | ✅ The step is character-for-character the ruled counsel's shape |

**No drift, no overreach, no silent miss** across F1–F7. The CLI-docs hunks
contain nothing beyond the rulings; the interleaved ccarchive/CONVENTIONS
hunks stayed in their own batches.

**How my findings land after reconciling** (no severities changed post-hoc;
framing sharpened):

- **My F1 (MEDIUM) stands, sharpened.** The ccarchive § Decision claims "man
  page + README name the exposures honestly" — the page carries the shrink
  guard, repo-dest guard, `UNMANIFESTED` and `fromArchive`, but the
  layout-drift alarm lives in the README only and `EXIT STATUS` predates all
  four new non-zero exits. Under the superset doctrine this batch itself wrote,
  the page owes them. (The ccarchive cycle is closed; this attaches through the
  CLI-docs interaction rule the brief names, so it is this cycle's to carry.)
- **My F2 (MEDIUM) stands, reframed: not drift — counsel against the ruled
  form.** The step is exactly what was ruled (F7, LOW, "no hard dependency").
  My finding is a soundness-at-HEAD challenge to that ruled form: on
  ubuntu-latest the step will never lint, and `apt-get install -y mandoc`
  (seconds, free public-repo minutes) is not a "hard dependency" in the sense
  the counsel guarded against. Mike may reasonably treat this as
  already-decided; the counsel is recorded because the cheap stronger form was
  never named as rejected.
- **My F3 (LOW) stands** — a completeness residue of the ruled F5 fix, not
  drift (the counselled cleanup said "same for man1" without the guard nuance).
- **My F4 (LOW) stands, reframed: the residual gap is in the ruled wording
  itself** ("one-breath closing *line*" vs the exemplar's two-sentence block)
  — the application is verbatim-faithful; the ruling's phrase carries the slack.
- **My F5 (LOW) stands** — README trigger wording vs code ("non-empty archive"
  vs non-empty manifest), a note only.

Intent-record frictions: none material. Its application highlights all
re-proved true here (instrument suite 67→75 consistent with the +8 new tests;
floor claims all green; residue removal confirmed live). One soft overclaim
already carried into my F1: "man page + README carry the exposures honestly"
is true of the README, partial for the page.

### Verdict

**PASS-WITH-FINDINGS** — 0 MAJOR · 2 MEDIUM (F1, F2) · 3 LOW (F3–F5).

The application is **faithful**: every one of the seven rulings is implemented
as decided, several verbatim, with nothing smuggled in beside them — and every
proof the application claims re-ran green here, including a fresh adversarial
installer drive and empirical verification of the MANPATH doctrine. The
findings are residue, not drift: the man page's `EXIT STATUS` fell behind the
behaviour the sibling batch added (F1, the one finding with an operator-facing
cost), and the rest are counsel on the ruled forms' remaining slack. As sound
doctrine at HEAD, the CLI-docs convention now says what it means, meets its own
letter in the exemplar repo, and is mechanically pinned where it promised to
be. All findings are the principal's to decide (rule 3); counsel is recorded
per finding; nothing has been applied.

Per the close rule: 0 MAJOR at an applied-batch pass — reviewer's counsel is
that this closes the CLI-docs cycle on Mike's ruling of F1–F5.

---

## Decision — 2026-07-17, ruled by Mike (principal)

Mike ruled **F1–F5 all [fixed] as counselled** ("agreed — apply as
counselled", 2026-07-17). Applied the same day by the taking session (authored
neither the doctrine nor this verdict; the reviewer was its cold spawn). What
was applied:

- **F1** — `man/ccarchive.1` `EXIT STATUS` now enumerates the three ordinary-run
  non-zero exits (shrink refusal, repo dest, layout-drift alarm) and names
  `UNMANIFESTED` among the verify causes; the layout-drift alarm gets its own
  paragraph in `INTEGRITY`.
- **F2** — the CI step now installs mandoc (`apt-get`, seconds, free
  public-repo minutes) and lints for real; the comment records why the guarded
  form was retired. Ruled knowingly against the earlier F7 form.
- **F3** — the man-link cleanup pass hoisted out of the `if [ -d man ]` guard
  (unconditional, mirroring the bin pass); proven live in throwaway XDG dirs
  with `man/` retired and a planted stale owned link (removed; real page kept).
- **F4** — the letter now reads "at most a closing line or two".
- **F5** — README says "non-empty manifest", matching the code's trigger.

Verified after applying: mandoc lint clean · 75 instrument tests · 247 tool
tests · sizescan · linkscan all green; installer driven fresh (normal and
retired-`man/` cases).

**0 MAJOR at the pass ⇒ CYCLE CLOSED** (close rule): this terminal
application queues no further pointer.
