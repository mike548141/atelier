# Cold review — REPO-STANDARD: CLI tools ship `--help` and a man page

**Scope:** the doctrine hunk of commit `125ada3` (2026-07-17) — the new
repo-craft convention in `build/REPO-STANDARD.md` (§ Repo-craft conventions):
the two-register split (`--help` a one-screen digest that points at the manual;
`man <tool>(1)` the plain-language full reference), the superset/digest
relationship, and the wiring (`man/` dir, installer publishes to `MANPATH`).
Review the whole of `build/REPO-STANDARD.md` at HEAD plus the delta. The worked
example in the same commit — `instruments/man/ccarchive.1`, the trimmed
`ccarchive --help`, `instruments/install` man-wiring — is code, tested and
driven, in scope for **consistency with the doctrine's claims** (does the
example actually exhibit the convention as written), not for a line-by-line
code review. Children inherit this convention; its blast radius is the fleet.

**Sequencing (REVIEW.md rules 1–2):** (1) read this brief **only above the
first `---` divider** (use a limited read); (2) review the doctrine at HEAD
plus the delta, naming and attacking the load-bearing assumptions yourself, and
**write your attack surface durably into the verdict section of this file
first**; (3) only then open the deferred section below the divider, and the
intent record `docs/sessions/2026-07-17-0946-ccarchive-man-cli-docs-standard.md`
(the author's account — reconcile, never anchor). Name any residual exposure
rather than denying it.

**Spawn provenance (rule 4):** this brief is written by a **non-author** — a
fresh session the principal opened and pointed at the queue ("do any review
work"); the author session (Opus, intent record above) neither started nor
instructed the taking session or this reviewer. The reviewer is a cold spawn of
the taking session. One disclosure: the ROADMAP `⏳` pointer the taking session
read carried two seed questions (reproduced in the deferred section) — a
refs-only pointer is the spec; the exposure is named, not denied. The verdict
must repeat this provenance.

**This is self-authored doctrine (by function):** all findings are the
principal's to decide (rule 3) — record counsel per finding, labelled as the
reviewer's counsel; apply nothing.

**Re-run live proofs in scope:** the commit claims `mandoc` lints the page
clean, the instrument suite green (67), and the floor green (247 tool tests ·
scan triad · sizescan · linkscan). Re-run what falls in scope.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict to this file below the second
`---` divider.

---

## Deferred — seeded questions (open only after your attack surface is committed)

Carried from the author's ROADMAP pointer:

- Q1. Is the digest/reference boundary drawn sharply enough to prevent drift
  between `--help` and the man page?
- Q2. Does the convention over-reach for repos with trivial one-flag tools —
  should it be sized to tool complexity like the rest of the standard?

---

## Verdict — cold review, 2026-07-17 (Fable 5, cold spawn of the taking session)

### Attack surface (written before opening the deferred section or the intent record)

Formed from `build/REPO-STANDARD.md` at HEAD, the `125ada3` delta (doctrine hunk
+ worked example + the commit's own ROADMAP/README/test hunks), and live probes.
The load-bearing assumptions I will attack:

- **A1 — scope predicate.** "A repo with command-line tools documents each in
  two registers" is unconditional. Does it bind atelier's own `tools/` scanners
  (seven CLIs, publicly offered to children, no man pages, no roadmap item)?
  Does it contradict the standard's own sizing principle ("apply what earns its
  place") and the sizing table's narrower row ("man page if it exposes a CLI",
  Package/library/CLI type only)?
- **A2 — the drift-guard claim.** "Detail in one place… can't drift" — but the
  options list is *necessarily* duplicated (`--help` flat list vs `OPTIONS`
  section), and the new tests assert length + pointer + three hard-coded flags,
  never the superset relation. Is the anti-drift claim mechanical or aspirational?
- **A3 — doctrine vs worked example, letter-for-letter.** Doctrine: "a one-line
  synopsis and the options as a flat list, *nothing more*… not where prose…
  belongs." Does the shipped `--help` (which ends with a three-line prose
  paragraph) actually exhibit that letter?
- **A4 — the wiring claim's portability.** "Symlink them onto `MANPATH`…
  auto-found because the bin dir is on `PATH`" — the install script's comment
  scopes this to macOS/BSD `man`; the doctrine generalises it fleet-wide without
  the scoping. Also: a set `MANPATH` env var can disable PATH-derivation.
- **A5 — proof durability.** "Lints clean under mandoc" is a local, moment-in-time
  claim: CI never runs mandoc; the roff test is a shallow regex. Can the page rot
  green?
- **A6 — collateral honesty.** The README now says the Node CLIs "each carry
  both" registers — measure it (`cctranscript --help` = 42 lines, `ccrepo` = 67,
  neither has a page). And the "fixed" installer bug: is the residue of the old
  bug (directory symlinks already leaked into `~/.local/bin`) actually gone from
  the live machine, and does the "idempotent, only touches symlinks it owns"
  installer ever clean up stale owned links?

**Live proofs re-run (this worktree, 2026-07-17):**

- `mandoc -T lint instruments/man/ccarchive.1` → clean, exit 0 ✅
- `node --test instruments/*.test.js` → 67 pass / 0 fail ✅
- `python3 -m unittest discover -s tools` → Ran 247 tests, OK ✅
- `secretscan` · `leakscan` (structural **+ local** — term list present on this
  machine, so fuller than CI's structural-only) · `licenscan --expect Apache-2.0`
  · `linkscan` · `sizescan --check` → all clean, exit 0 ✅

**Exposure disclosure (named, not denied):** I read the brief only above the
first divider, and located the second divider by line number (a 3-line tail-peek
showed the final seed-question line). But the commit's own ROADMAP hunk — squarely
in-scope delta — reproduces both seed questions, so I met them while reviewing
the delta, after forming attack lines A1–A5 but before this durable write. A2's
drift question and A1's sizing question overlap the seeds; they were also
independently derivable from the doctrine text, which is presumably why the
author queued them. The intent record remains unopened at this point.

### Spawn provenance (repeated per rule 4)

This brief was written by a **non-author** — a fresh session the principal
opened and pointed at the queue ("do any review work"); the author session
(Opus, intent record above) neither started nor instructed the taking session
or this reviewer. The reviewer is a cold spawn of the taking session. The one
brief-level disclosure carries: the ROADMAP `⏳` pointer the taking session read
carried two seed questions, reproduced in the deferred section — plus my own
exposure disclosure above (the same seeds arrived via the in-scope ROADMAP
delta hunk before my durable write).

### Reconciliation with the deferred seeds and the intent record

Opened after the attack surface above was committed. Seed Q1 ≡ my A2, seed
Q2 ≡ my A1 — both were already on my surface; the findings below answer them.
The intent record reconciles with the delta with two frictions I hold to:
it describes the trimmed `--help` as ending with "one line pointing at
`man ccarchive`" (it ends with a three-line prose paragraph — see F3), and it
is silent on `tools/` (see F1) and on the residue of the fixed install bug on
already-installed machines (see F5). Its "Verified" claims all re-proved true
here, including a fresh drive of `install` into throwaway XDG dirs: three CLIs
plus `ccarchive.1` published, **no** directory leaked into bin.

### Findings

**F1 — MAJOR — the scope predicate is unbounded, and atelier itself doesn't
meet it.** The bullet opens "A repo with command-line tools documents each in
two registers" — unconditional, no sizing hatch. Read as written it binds
atelier's own `tools/` layer: seven stdlib-Python CLI scanners, publicly
offered to children as adoptable tooling, none with a man page, and — unlike
`cctranscript`/`ccrepo`, whose gap is honestly roadmapped — with **no roadmap
item and no stated exception anywhere**. This contradicts the standard's own
spine twice: the sizing principle ("apply what earns its place"; "sizing is a
judgement, not a menu") and the sizing table, whose narrower pre-existing row
scopes the man-page expectation to the Package/library/CLI repo type. Doctrine
that binds children to a letter the parent silently doesn't meet is the exact
failure mode the apex names. This also answers seed Q2: yes, as written it
over-reaches.
*Reviewer's counsel:* draw the predicate — e.g. "a CLI a repo *installs onto
an operator's machine* ships both registers; repo-internal scripts run in
place (hooks, CI) owe a good `--help` only" — and either point the bullet at
the sizing table or fold the boundary into it. Then either roadmap `tools/`
pages or (better, under the drawn boundary) state why the scanners fall
outside. The principal decides which.

**F2 — MEDIUM — the anti-drift claim is aspirational, not mechanical.** The
doctrine claims the split "can't drift" because detail lives in one place —
but the one thing *necessarily present in both registers* is the options list
(`--help`'s flat list vs the page's `OPTIONS`), and nothing guards that
duplication: the new tests assert length ≤22, the manual pointer, and three
hard-coded flag strings. A flag added to the script and `--help` but not the
page (or vice versa) passes the whole suite green. Today the superset relation
holds (I checked every `--help` fact against the page — all covered, including
`CCARCHIVE_DEST`), but it holds by care, not by mechanism, while the doctrine's
words promise mechanism. This answers seed Q1: the register boundary is drawn
sharply; the *drift guard* is not.
*Reviewer's counsel:* one cheap test closes it — extract every `--\w[\w-]*`
token from `--help` output and assert each appears in `man/<tool>.1`; state in
the doctrine that the superset relation should be test-enforced where tests
exist. Alternatively soften "can't drift" to "is kept from drifting by…" —
but the test is cheaper than the hedge.

**F3 — MEDIUM — the worked example doesn't exhibit the doctrine's letter.**
Doctrine: `--help` is "a one-line synopsis and the options as a flat list,
**nothing more**", and "*not* where prose… belong[s]". The shipped `--help`
ends with a three-line prose paragraph ("Mirrors every ~/.claude/projects/…")
before the manual pointer — useful prose, but prose the letter forbids; the
intent record compounds it by describing the ending as "one line pointing at
`man ccarchive`". Children copying the cited worked example inherit something
the doctrine's text disallows. Either the letter is too strict or the example
is out of spec — they can't both stand.
*Reviewer's counsel:* the example's shape is the better norm — amend the
doctrine to permit "a one-breath closing line saying what the tool does and
where the manual is", which is also what the 40→18 trim actually produced.
Tightening the example to the current letter is the worse trade.

**F4 — MEDIUM — instruments/README overclaims in the present tense.** "The
Node CLIs each carry both a concise `-h`/`--help` digest and a fuller
`man <tool>` page" — false for two of three at HEAD (`cctranscript --help` is
42 lines, `ccrepo` 67; neither has a page). The very next sentence corrects it
("`ccarchive` is the worked example; `cctranscript` and `ccrepo` follow"), so
no reader is durably misled — but a claim stronger than its evidence, in the
exemplar repo, in the same commit that writes "grounded, not invented" into
the standard, is worth a finding.
*Reviewer's counsel:* one-word-class fix — "The Node CLIs are converging on
both registers…" or "carry a concise `--help`; `ccarchive` also ships the
first man page".

**F5 — MEDIUM — the fixed install bug left live residue, and the installer
can't clean it.** The fix is real and proven forward (fresh XDG-dir drive:
no directory leaks). But `~/.local/bin` on this machine **still contains**
the leaked `fixtures` and `browser-fetch` directory symlinks (dated before the
fix), and the installer — framed as "idempotent… only touches symlinks it
owns" — has no pass that removes stale owned links, so re-running it never
repairs the damage its earlier self did. "Fixed a latent bug" is true of the
code and silently untrue of the installed estate.
*Reviewer's counsel:* add a cleanup pass — for each symlink in `$DEST`
pointing back into `$BIN_DIR`, remove it unless it matches a currently
installable tool (the ownership test is already the script's own definition);
same for `man1`. Until then, a one-line note in the intent record or ROADMAP
that polluted machines need a manual `rm`.

**F6 — LOW — the MANPATH wiring claim is stated more universally than its own
implementation comments claim.** The doctrine asserts pages in
`~/.local/share/man/man1` are "auto-found because the bin dir is on `PATH`"
as a flat fact; the install script's comment correctly scopes the PATH→man
auto-mapping to "macOS/BSD `man`". man-db (mainstream Linux) does derive
manpaths from PATH too, but an operator with a non-empty `MANPATH` env var
(no leading/trailing colon) *replaces* derivation and loses the pages — a
real, common gotcha for a convention with fleet blast radius. Strictly the
pages are never "on `MANPATH`" at all; they're found by derivation.
*Reviewer's counsel:* one clause — "auto-found on macOS/BSD and man-db Linux
via PATH-derived manpath; a hard-set `MANPATH` overrides this" — or have
`install` end with a `man -w <tool>` check that warns when the page isn't
findable, mirroring the existing PATH warning.

**F7 — LOW — "lints clean under mandoc" is a moment-in-time claim with no
gate.** True (re-proved: `mandoc -T lint` exits 0, silent), but CI never runs
mandoc and the shipped roff test is a shallow regex (`.TH` + six `.SH` names),
so the page can rot while everything stays green — the standard's own
phantom-success vocabulary applies.
*Reviewer's counsel:* a guarded CI step (`command -v mandoc && mandoc -T lint
instruments/man/*.1 || echo "mandoc unavailable — lint is local-only"`) keeps
the gate honest without adding a hard dependency; or extend the honest-CI
comment to name roff lint as a documented local step.

### Live proofs — summary of re-runs (all this worktree, this session)

| Proof | Claimed | Re-run result |
|---|---|---|
| `mandoc -T lint man/ccarchive.1` | clean | ✅ clean, exit 0 |
| Instrument suite | 67 green | ✅ 67 pass / 0 fail |
| Tool test suite | 247 green | ✅ Ran 247, OK |
| secretscan / leakscan / licenscan | clean | ✅ all clean (leakscan structural **+ local**) |
| linkscan / sizescan `--check` | clean | ✅ both clean |
| `install` (throwaway XDG dirs) | no dir leaks | ✅ 3 CLIs + 1 page, no leaks |

### Verdict

**PASS-WITH-FINDINGS** — 1 MAJOR (F1), 4 MEDIUM (F2–F5), 2 LOW (F6–F7).

The doctrine's substance is sound, wanted (Mike's ask, verbatim in the intent
record), grounded in a real, tested, re-driven worked example, and every
recorded proof re-ran green. The findings are boundary and letter problems,
not direction problems: the scope predicate needs drawing before children
inherit an obligation the parent itself doesn't meet (F1), the anti-drift
promise needs the one cheap test that would make it true (F2), and the
doctrine and its own exemplar need to agree on what `--help` may contain (F3).
All findings are the principal's to decide; counsel is recorded per finding
and nothing has been applied.
