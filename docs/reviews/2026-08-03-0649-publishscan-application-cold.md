# Brief — publishscan application cold pass (rule 4)

- **Work under review:** the `publishscan` application delta — commit
  `c85285b` (`tools/publishscan.py`, `tools/test_publishscan.py`), which
  applied Mike's rulings PB1–PB4 from the 2026-08-02 publishscan cold pass.
- **Review shape:** application review (REVIEW.md § *Applying decisions to
  doctrine*). Sequence honoured: the edited code and tests are reviewed at
  HEAD and findings committed **before** the prior verdict
  (`2026-08-02-2313-publishscan-cold.md`) is opened; the verdict is then read
  to reconcile the application against the rulings. The residual exposure —
  the delta's commit message carries the author's one-paragraph account of
  PB1–PB4 — is named, not denied.
- **Spawn provenance (rule 4):** taken from the ROADMAP `⏳` queue by a
  session Mike spawned with a generic "do any work that requires Fable,
  including reviews" — the worked example in REVIEW.md rule 4. This session
  authored neither the scanner, the verdicts, nor the application; the
  application's author (the 2026-08-02 taker session) spawned nothing here.
  Reviewer tier: Fable.
- **Disclosed exposure:** the mandated session onramp (SESSIONS.md tail)
  included the author session's addendum summarising the application
  ("any-depth matching, enforced `# reason`, `--root` rebasing") before this
  taker could choose not to read it. Named here so the verdict is auditable;
  the detail below that summary was met cold.
- **Scope:** the full commitment — the code, the tests (reviewable on the
  same footing), the live behaviour (re-run, not read), and whether the
  application is faithful to rulings it implements (checked at reconcile).
  Non-goals: the scanner's original design (reviewed 2026-08-02; its cycle's
  findings are Mike's rulings, not re-litigated here) — but a ruling whose
  application *introduces* a new defect is in scope.
- **Lenses:** all four (approach/assumptions · correctness/quality ·
  completeness/harvest · security/privacy). Review deep, not fast.

---

# Verdict — PASS-WITH-FINDINGS · 0 MAJOR / 1 minor / 3 notes

**Provenance (restated per rule 4):** reviewed by a Fable session Mike spawned
generically ("do any work that requires Fable, including reviews"); the
reviewer authored neither the scanner, the 2026-08-02 verdict, nor the
application. Findings below were committed before the prior verdict was
opened; the reconcile section beneath them was written after.

**What was re-run, not read** (all reproduce at HEAD, worktree of `b3101c3`):
`test_publishscan.py` 18/18 OK · `--selftest` OK · live `--root .` clean over
387 tracked paths, exit 0 · the PB2 bare-glob leg red (exit 2, in-suite) · the
PB1 depth rows red in both the suite and the selftest red leg · PB4's dropped
rows confirmed redundant by the depth form. The delta's own claims all held.

**Lens 1 (approach).** The `glob OR */glob` depth form is the right minimal
fix — `fnmatch`'s `*` spanning `/` makes it complete without a `**` engine,
and the docstring states the mechanism honestly. The load-bearing assumption
("machine-local wherever it sits") holds for every pattern except one shape —
see PA2. Moving `load_ignores` inside the `try` (so `BadIgnoreFile` exits 2,
not a traceback) is correct fail-safe plumbing.

**Lens 4 (security/privacy).** `/security-review` discharged with grounds:
this is a landed-delta review — the only pending change in the tree is this
brief, and a pending-changes scanner run now would scan the brief itself (the
SL2 trap REVIEW.md names). Manual pass: subprocess calls are argv-form with
fixed args, no shell; no network; input surfaces are the repo tree and the
ignore file — PA3/PA4 below are the two findings that surface produced.

## Findings

**PA1 (minor) — the PB3 rebase notice corrupts `--json` output.**
`run()` prints the "--root is inside the repo" notice to **stdout**
unconditionally, before the JSON document. Reproduced: `--json --root <subdir>`
emits a prose line then JSON; `json.load(stdout)` raises. Latent on the live
floor — both registry planes pass `--root {root}` (the repo root), so the
notice never fires there — but any future consumer scripting `--json` against
a subtree hits it. Counsel: route the notice to stderr (where diagnostics
belong; also fixes the JSON plane in one move), and/or carry a `"rebased_to"`
key in the JSON. One-line fix, plus a test asserting `--json` stdout parses
under a subdir root.

**PA2 (note) — depth matching widens the `.env.example` false-positive class
from one directory to all of them.** `.env.*` has always matched
`.env.example` at the root; the depth form now reds `config/.env.example`
anywhere. Reproduced live. Templates of exactly this shape
(`.env.example`/`.env.sample`) are conventionally tracked **on purpose** —
they are the documented mitigation for not tracking `.env`. Not introduced by
this delta (the class predates it) and not a defect in the PB1 ruling —
recorded because the application multiplies the surface, and the first
adopter with a tracked `.env.example` meets the scanner's sharpest FP on day
one. Counsel: leave the pattern alone (a carve-out is a blind spot in a
security scanner, and `secretscan`'s SF1 history argues against exempting by
name-shape); the `# reason` hatch is the designed answer. If FP reports
accumulate, that is Track E's call to make with data, not this application's.

**PA3 (note) — a glob containing `#` silently misparses into a different
exemption.** `load_ignores` partitions at the first `#`, so
`foo#bar.md  # reason` yields glob `foo` — an exemption for a *different
path* than written, silently. Filenames with `#` are rare and the misparsed
glob usually matches nothing, but a silent rewrite of a security exemption is
the wrong failure direction. Counsel: fold into any future ignore-file touch
— reject globs containing `#` (config error, exit 2) rather than support
escaping; not worth its own commit.

**PA4 (note) — ignore-file strings print raw to the terminal.** The
`BadIgnoreFile` message embeds the offending glob verbatim into stderr; a
hostile child's ignore file could carry C0 escape sequences. This is exactly
the class C1F3 already ruled (STRIP C0 CONTROLS AT PARSE, on `floor.py`'s
config-authored strings) — recorded so publishscan's two config-authored
surfaces (glob text in errors, finding paths in output) are named in that
fix's scope rather than discovered after it closes. No separate work item.

*(Reconcile against the 2026-08-02 verdict follows in a separate commit —
the prior verdict stays unopened until the findings above are committed.)*
