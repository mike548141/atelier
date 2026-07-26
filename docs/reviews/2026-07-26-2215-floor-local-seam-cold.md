# Cold review (rule 4) — the repo-local floor seam

**Subject (refs only):** commits `f526dea` and `76f4acc` at HEAD (plus the
records-pointer commit `92bc0cb` that queued this review). Touched surfaces:
`tools/floor.py` (the `local` block, `_load_local`, the `is_local` path
through plan/run/render, `_interpreter`), `tools/floorfleet.py` (the `➕`
board line), `tools/test_floor.py`, `tools/test_floorfleet.py`,
`docs/build/REPO-STANDARD.md`, `docs/build/templates/CONTRIBUTING.md`,
`docs/build/templates/workflows/floor.yml`, `CHANGELOG.md`.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and the
SESSIONS index one-liner for this work before writing this stub. Nothing
evaluative from either appears above the divider.

**The reviewer's first acts:** establish what the seam is and why it exists
from the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). This extends a *security floor's* configuration
surface with repo-owned executable checks — what a malicious or careless child
config can now make the floor do is lens-4 territory at both altitudes,
checked against open catalogues, not recalled. Re-run every claim the two
commit messages and the CHANGELOG entry make — test counts, fail-closed legs,
visibility surfaces — and probe the seam with crafted configs of your own
design (colliding names, out-of-repo `run` paths, missing scripts, permission
edge cases, softening vocabulary).

**Re-run obligations:** `python3 tools/floor.py --plane ci` ·
`python3 tools/floor.py --selftest` · `python3 -m unittest tools.test_floor
tools.test_floorfleet` · `python3 -m unittest discover -s tools` ·
`node --test instruments/*.test.js` · your own probe configs in a scratch
repo. `/security-review` reaches only pending diffs — on a landed delta
discharge it in one explicit line with grounds; the manual pass above stands
regardless.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/` (quarantined). Do not grep git
history for review commits; confine git archaeology to the delta commits
named above. Open the deferred section below — and the intent record it
names — only after your findings are durably written to this file; then
append the reconcile, named as such.

Findings carry stable IDs (**LS1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts. The
seam edits `REPO-STANDARD.md` and adds a surface every child may declare
against — self-authored doctrine by function: REVIEW.md rules 3–4 govern —
findings are the principal's to decide; nothing is applied in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* [`sessions/2026-07-26-1120-floor-local-seam.md`](../sessions/2026-07-26-1120-floor-local-seam.md)

---

## Reviewer's attack surface (named before any re-run or probe)

Reviewer: cold rule-4 pass, Fable, worktree at HEAD `9aef298`. The seam as I
establish it from `f526dea` + `76f4acc` alone: `.atelier-floor.json` gains a
`local` block; `_load_local` parses each entry into a `Scanner` with `run`
(repo-relative script) and inline `scope_paths`; `plan`/`run`/`render`/`--json`
carry an `is_local`/`local` marking; `floorfleet` prints a `➕ name local — why`
board line from config text alone. This turns a subtract-only config file into
a **config-directed execution surface**: whoever writes the child's config now
names code that runs at hook time and in CI.

Load-bearing assumptions I will attack, as my own:

1. **Trust boundary of the config author.** The claim "it is the child's own
   code ... which is code both already run" must hold on BOTH planes. CI: any
   PR already executes repo code, no escalation. Hook: under the preferred
   `core.hooksPath .githooks` install the tracked shim already gives repo
   content commit-time execution; under the legacy per-clone copy it did NOT —
   the config now moves that boundary. Fork-PR and cloned-repo cases probed.
2. **Containment of `run`.** The check is lexical (`PurePosixPath`: absolute,
   `..`). I will probe what "inside the repo" misses: committed symlinks whose
   target is outside the tree, `run` naming a directory, `.`/empty/whitespace
   paths, Windows-style absolutes, `run` naming the config file itself.
3. **Add-only.** Collision with `BY_NAME` at load. Probes: exact collision,
   opt-in scanner names, empty-string name, whitespace/near-miss names
   (`"leakscan "`), names that collide only visually on the board, and a local
   name colliding with a future fleet scanner (behaviour on registry growth).
4. **Fail-closed legs.** Missing script; non-`.py` without execute bit; and the
   adjacent leg the guard implies but may not cover: an executable non-`.py`
   file with no shebang (ENOEXEC — traceback vs clean block). Also: missing
   script under `advisory`; declared `scope` pointing at absent trees.
5. **Visibility claims.** `--list`, `--json`, render tag, board `➕` — and the
   states where the marking might drop (disabled local check; skipped legs).
   Board resilience against malformed `local` blocks (list-shaped, non-dict
   entries, huge/newline-laden `why`).
6. **Softening vocabulary.** Advisory-downgrades-result semantics; disabled
   needs a reason; both-spellings conflict; hook-only + softened combos;
   whether `local` names can reach `scope`/`flags` by any spelling.
7. **Output-channel injection.** `name`/`why` are attacker-chosen JSON strings
   that reach GitHub workflow-command lines (`::error::{name} … {why}`) and the
   board render; newlines in JSON strings are legal. Probe what a crafted
   `why` can inject into the Actions log stream.
8. **Silent-config drift.** Unknown keys in a declaration (`plane`, `arg`,
   `scopes` typos) — does the file's "a config cannot quietly mean less than
   it says" rule hold inside `local`? Non-string/odd-typed `run`, `args` as a
   dict, duplicate JSON keys.

Lens 4 is checked against the injection/untrusted-input classes of the OWASP
Top 10 (A03 injection — argv and log-stream; A08 software/data integrity —
config-directed execution, symlinked targets; A05 misconfiguration — silent
typo acceptance), not recalled from memory.

---

## Verdict — cold rule-4 pass (Fable, HEAD `9aef298`)

**PASS-WITH-FINDINGS.** Counts: 0 critical · 0 high · 3 medium (LS1 LS2 LS3)
· 2 low (LS4 LS5) · 1 minor folded into LS1. The seam is well-built and its
central add-only / fail-closed invariants hold under attack; the findings are
edges the design's own stated goals reach but the code does not quite close.

### What I re-ran, with results
- `floor.py --plane ci` → **green**, all 9 scanners enforced, rc 0.
- `floor.py --selftest` → **ok (9 scanners, 0 failures)**.
- `unittest tools.test_floor tools.test_floorfleet` → **72 OK**.
- `unittest discover -s tools` → **694 OK** — matches the commit's "694 tests
  OK (+21)" exactly.
- `node --test instruments/*.test.js` → **207 pass, 0 fail**.
- `/security-review`: landed delta, no pending diff — discharged here in one
  line; the manual lens-4 pass below stands in its place (probes P1–P7 in a
  scratch repo, run directly against `floor.py` at HEAD).
- Commit/CHANGELOG claim audit — all re-verified true: add-only collision
  (exact + opt-in names hard-error), lexical containment (`..`/absolute/empty
  rejected), fail-closed missing script (blocks even under `advisory`),
  advisory downgrades result not invocation (rc preserved), hook-only lists on
  CI as skipped, both softening spellings, `scope`/`flags` refused for local
  names, floorfleet renders a malformed `local` block without crashing.

### Findings (counsel — the principal decides; nothing applied)

**LS1 — MEDIUM (lens 4, A03 injection).** A child-authored `why` (and `name`)
is emitted verbatim into the GitHub Actions log-command stream.
*Evidence:* `tools/floor.py:764` — `print(f"::error::{scanner.name} failed —
{scanner.why}", file=child_stdout)`; real CI runs without `--json`, so
`child_stdout` is stdout = the Actions log. Probe P5: a `why` of
`"legit\n::error::INJECTED spoofed annotation\n::set-output name=x::pwn"`
produced a second, spoofed `::error::INJECTED spoofed annotation` line in the
log stream. Before the seam this channel carried only hardcoded registry
strings; the seam feeds it attacker-authored config text, and on a repo whose
CI runs on PRs that may edit `.atelier-floor.json`, a contributor's `why`
reaches the base repo's annotations. *Recurrence-prevention (class):* encode
`%0A`/`%0D`/`%25` (or strip newlines) when interpolating `name`/`why` into any
`::` workflow-command line — a GitHub-recommended mitigation for the whole
workflow-command-injection class. *Minor, folded:* the exact-string collision
guard is evaded by a whitespace/near-miss name (`"leakscan "`, probe P7) which
renders near-indistinguishably from the fleet `leakscan` on `--list`/board —
confusion only, not weakening, since both still run (it cannot shadow).

**LS2 — MEDIUM (lens 2/4).** The execute-bit guard has an unguarded sibling: an
*executable* non-`.py` `run` script with no valid shebang crashes the whole
floor with an uncaught `OSError: [Errno 8] Exec format error` traceback —
the exact failure mode the guard was written to prevent for `PermissionError`.
*Evidence:* `tools/floor.py:721` guards only `not os.access(path, os.X_OK)`;
`tools/floor.py:762` `subprocess.run(argv, …)` is not wrapped for `OSError`.
Probe P3: `tools/tripwire.sh` (exec bit set, body `this is not a script`) →
traceback, no floor summary, exit 1. Fail-closed by exit code, but the commit's
own goal ("rather than taking the floor down with a … traceback … a crash reads
as broken tooling, not as the config error it actually is") is not met, and a
second local check after it never runs. *Recurrence-prevention (class):* wrap
the invocation in `try/except OSError` and emit the same clean BLOCK message the
exec-bit leg does.

**LS3 — MEDIUM (lens 2/4, A08 integrity; defence-in-depth).** "`run` must
resolve inside the repo" is enforced on the path STRING only; a committed
symlink at the `run` path whose target is outside the tree executes out-of-tree
code. *Evidence:* `tools/floor.py:353-359` checks `PurePosixPath.is_absolute()`
and `".." in parts` on the declared string; `:689` runs `root / scanner.run`
with no realpath containment check. Probe P2b: `tools/tripwire.py` → symlink to
an out-of-tree `EVIL.py` executed it ("PWNED: out-of-tree code executed by the
floor", tripwire ✅). Marginal privilege is bounded (config author usually owns
the repo, and CI runs repo code anyway), but the stated invariant is not
enforced, and its test `test_run_path_must_stay_inside_the_repo`
(`tools/test_floor.py`) exercises only lexical strings — it never plants a
symlink, so the suite overstates what the guard does. *Recurrence-prevention
(class):* resolve the realpath and assert it is within `root` before executing;
add a symlink-escape test.

**LS4 — LOW (lens 1/2).** Unknown keys inside a `local.<name>` declaration are
silently ignored, and wrong-typed `args`/`scope` silently coerce — relaxing the
file's own "a config cannot quietly mean less than it says" invariant that IS
enforced for top-level scanner names (`validate()`, `tools/floor.py:498`).
*Evidence:* `_load_local` (`tools/floor.py:322-395`) reads only known keys and
never rejects extras. Probe P6: `{"plane":["hook"], "arg":["--x"],
"scopes":["src"], "nonsense":1}` accepted silently — a `planes` typo runs the
check on BOTH planes (the default) instead of hook-only, and an `args` typo
silently drops the intended arguments, so a check meant to scan a target runs
with none. A hook-only tripwire whose blocklist is repo-local could thereby run
on CI unintentionally. *Recurrence-prevention:* reject unknown keys in a local
declaration, the same fail-closed shape used for unknown scanner names.

**LS5 — LOW (lens 2).** A *disabled* local check loses its `local` marking in
`--json` (`"local": false`) and in the render (no `· local` tag).
*Evidence:* `tools/floor.py:679` — the disabled branch builds
`Result(scanner.name, state, 0, cfg.disabled[scanner.name])` without
`local=scanner.is_local` (every other branch passes it). Probe P1: a disabled
local `tripwire` reports `local: False` in `--json` and renders untagged, while
`--list` and the floorfleet board correctly show it as local. Contradicts the
commit's "local checks are in `--json`, in the render" for the disabled state —
a `--json` consumer cannot tell a disabled local check from a disabled fleet
one. *Recurrence-prevention:* pass `local=scanner.is_local` on the disabled
Result, matching the other four branches.

### What held (positive)
The load-bearing guards all survived probing: add-only collision (exact + opt-in
names), lexical containment (`..`/absolute/whitespace/empty), fail-closed on a
missing script even when declared `advisory` (probe: state hard-set to enforced,
blocks), advisory downgrades the result while preserving the check's rc,
hook-only lists on CI as skipped, one softening vocabulary, `scope`/`flags`
refused for local names, and floorfleet reporting DECLARED-not-working without
dying on a malformed block. The design is sound; LS1–LS5 are edges, not holes in
the central invariant.

---

## Reconciliation (after reading the deferred section + intent record)

Intent record: `sessions/2026-07-26-1120-floor-local-seam.md`. It sets out the
ask ("Create a repo-local extension point"), the `ros` forcing case, the three
properties (ADDS / fails CLOSED / VISIBLE), and an "Honest limits" section. I
reconciled each finding against it; **none withdrawn, none added, two
sharpened**. The record does not blunt any finding — each lands in a seam the
record's own account leaves open.

- **LS1 (injection) — STANDS, sharpened.** The record's trust model reasons
  about the *script* ("a repo that can commit a script can already run it in its
  own CI"); it never reasons about the `why`/`name` config *strings* reaching
  the Actions workflow-command channel. That surface is unnamed in the record, so
  the finding is not anticipated — it is a genuine gap, not a known limit.
- **LS2 (ENOEXEC) — STANDS, sharpened by the record.** The record explicitly
  names the exec-bit guard's purpose: a non-`.py` check that would raise
  `PermissionError` and "take the whole floor down with a traceback ... reads as
  broken tooling rather than as the config error it is." The ENOEXEC sibling is
  the identical class the author set out to eliminate, implemented for one errno
  and not the other — the record strengthens the finding rather than excusing it.
- **LS3 (symlink escape) — STANDS; severity confirmed, not blunted.** The
  record's "Honest limits" asserts `run` "is contained to the repo and never
  shell-interpreted" — the exact containment my probe defeats via a committed
  symlink. The record's adjacent point (a repo that can commit code can already
  run it in its own CI) is why I rated this Medium/defence-in-depth rather than
  High, so the record confirms my severity calibration; the containment *claim*
  itself is still overstated.
- **LS4 (silent unknown keys) — STANDS.** Unaddressed by the record; no bearing.
- **LS5 (disabled drops `local` marking) — STANDS.** Directly contradicts the
  record's VISIBLE claim ("`--json` (a `local` field)") for the disabled state:
  the field is present but reports `false`.

Out-of-scope, correctly untouched: the record's "What was NOT built" (the
verifier/checklist V1–V7 layer) is explicitly deferred and I did not stray into
it; the AWA2 pointer-timing note is a self-flagged process nuance the author
already owns. Verdict unchanged: **PASS-WITH-FINDINGS** — 3 medium, 2 low.
