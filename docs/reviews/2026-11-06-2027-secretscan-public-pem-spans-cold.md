# Cold pass — secretscan exempts a public certificate's or public key's PEM body from the entropy rule

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (guard code is doctrine by
function).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 HAS RUN — verdict **PASS-WITH-FINDINGS** (0 MAJOR · 3 MODERATE · 2 minor ·
3 note), 2026-11-06 UTC, by a cold Fable 5.1 reviewer under orchestrator `850e2a78`; act 2 (the
reconcile against the sibling) is pending. Brief written 2026-11-06 UTC by session `782f8a66`, a
headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1030-rule-4-cold-pass-queued-secretscan-public-pem-block-spans.md`.
**Why it earns a review:** `secretscan` is the credential boundary every adopting child floats on
at `floor.yml@main`, so this change reached every child's next CI run the day it merged. It
opens a blind spot on purpose: lines it judges to be a public certificate's or public key's body
no longer reach the entropy rule. The worst failure is a silent one: private-key material, or
any other secret, passing a gate that reports clean because it sits in, or is shaped like, a
block the exemption covers.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session
  `722ac2e2`, 2026-11-06, and the Sonnet worker(s) it dispatched, which wrote the code (per the
  queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `782f8a66` (`claude-opus-5-5`), a headless brief-writer
  started on 2026-11-06 by drain session `850e2a78` (Opus 5.5). Neither authored any of this
  delta, and neither was started or instructed by `722ac2e2`. **Off-tier for review,
  disclosed: the brief-writer forms no finding and writes no severity**, and stops after this
  brief, its sibling and the one for `160/1040`. It ran no review and used no Fable model.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `850e2a78`:
  the two board-item paths, the run constraints below, and the statement that `850e2a78` wrote
  no delta and holds no view on either subject. It carried no framing of the work. The
  brief-writer had no contact with `722ac2e2` or its workers.
- **Who orchestrates:** drain session `850e2a78` (Opus 5.5), which runs the two passes one at a
  time. It is **not a reviewer**: under rule 4's off-tier conditions it holds the context
  partition (this brief's sibling stays with it until act 1 is committed), commits the records,
  **forms no finding and writes no severity**. That arrangement is disclosed here, and the
  reviewer repeats it in the verdict's provenance.
- **Who reviews:** a fresh Fable 5.1 subagent the orchestrator starts for this pass alone, with
  its own context. **Barred from reviewing:** session `722ac2e2` and everything it started (its
  Sonnet workers); session `782f8a66` (this brief-writer); session `850e2a78` (the
  orchestrator). The reviewer of `160/1040` may not also review this pass in the same context.
- **The principal's approval** (quoted in the queue pointer), 2026-11-06, verbatim: *"If you can
  run it using the API credit and achieve parity of quality in the review as doing it locally
  then use the API. If you cant achieve parity then run it on fable locally now"*. The
  orchestrator's dispatch fixes the local route: this pass runs on the laptop through Claude
  Code, not through any API harness.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before
  writing):
  - its dispatch instructions; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md`
    whole; `docs/method/SECRETS.md` heading list and lines 111–135 and 188–262;
  - the house-form brief `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` and its
    sibling as they stood at commit `33ebcb6` (before that pass ran; other surfaces), and that
    commit's message;
  - board items `160/1030` and `160/1040` whole; **both intent records, `320/790` and
    `115/380`, whole, including the authors' landing accounts**; board item `160/950` whole,
    which carries the **summary of another pass's verdict** on the staged-diff reader that
    `secretscan --staged` uses (`115/360`);
  - the three `secretscan` commits body-free through `tools/coldsweep.py --commit`, scoped to
    `tools/secretscan.py`, `tools/README.md`, `CHANGELOG.md` and `.secretscanignore`;
    `tools/test_secretscan.py` at HEAD lines 1877–2000, 2228–2275 and 2348–2362, and its
    class list; `--help` of `secretscan`, `coldsweep`, `floor`, `floorfleet`, `pointerscan` and
    `wrapscan`; commit subjects through `git log`; file names under `docs/reviews/` and
    `docs/roadmap/160-doctrine-review-owed/`;
  - the results of the re-run lines below, and count-only output of probes over the adopting
    child repos on the machine (held in the sibling, by count).

  It did **not** open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any other
  prior verdict, or any delta commit's message body. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the sibling.

## The acceptance test

No intent record for this delta carries a ruling of the principal's on its design. Judge it
against the posture the credential scan answers to: `docs/method/SECRETS.md` § *The boundary's
posture — over-flag, because detection enables everything* (from line 188), whose opening
states the principal's intent for the scans (2026-07-28) and whose third paragraph says who
decides a narrowing of coverage and where it is recorded. The delta itself states its purpose
and its limits in `tools/README.md` § *A public certificate's body (320/790)*, in the
`320/790` comment in `tools/secretscan.py` and in its `CHANGELOG.md` entry; those are the
author's claims to test, not settled scope.

## What the work is

Two commits on `main`, 2026-11-06, which close `320/790`:

- **`c5f6202`** — `secretscan: exempt a public certificate's body from the entropy rule
  (320/790)`.
- **`3d53b67`** — `secretscan: a forged certificate header around a private key's DER is not
  exempt (320/790)`.

Delta paths: `tools/secretscan.py`, `tools/test_secretscan.py`, `tools/README.md`,
`CHANGELOG.md` (the `320/790` entry). `3d53b67` also touches board records; those are barred
until phase 2 (below), so always pass `--path`. Read each commit body-free:

```
python3 tools/coldsweep.py --root . --commit <sha> \
  --path tools/secretscan.py --path tools/test_secretscan.py \
  --path tools/README.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Review each delta path at HEAD too. One later commit touches the same paths:
**`0d8db9c`** (`115/380`), which reuses this delta's DER helpers and PEM bound, and is under its
own pass (`160/1040`). Read it only as far as it bears on this delta's behaviour at HEAD.
Confirm nothing else has landed with
`git log --oneline 3d53b67..HEAD -- tools/secretscan.py tools/test_secretscan.py tools/README.md CHANGELOG.md`,
and read anything new the same way.

## The questions the queue pointer lists

As `160/1030` lists them, verbatim:

> can any input other than a public certificate or public key reach the exemption (the label
> match, the consecutive-line and base64 rules, the 2048-line bound, the nested SEQUENCE
> check); does the `--staged` path read the index copy only when it should, and fail closed
> when git cannot give it; is whole-block voiding right, or too strict for a real-world
> certificate file.

They are a floor, never a fence. Name your own load-bearing assumptions first (lens 1).

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and
live behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in
scope.

**Non-goals:** the existing per-line public-key carve-out (`PUBLIC_KEY_RX`) and the named and
assigned rules as they stood before `c5f6202`, except where this delta changes what reaches
them; the `115/380` check added by `0d8db9c` in its own right (pass `160/1040`).

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   Ask whether this is the right problem, solved at the right altitude and with the right shape,
   against the posture above.
2. **Correctness & quality.** Diff both commits; run the probes live. Record each overclaim
   against the text that makes it (docstrings, comments, `tools/README.md`, `CHANGELOG.md`,
   `--help`, the printed summary line).
3. **Completeness / harvest.** Every surface that states what `secretscan` exempts or how it
   counts suppressions (V3); one home (V4); no contradiction (V5); tests that would stay green on
   a broken exemption (mutate a scratch copy and re-run).
4. **Security & privacy** — mandatory, and the reason this pass exists. The exemption decodes
   untrusted input, so check it by hand for resource exhaustion and fail-open paths, and check the
   likely vectors against an open catalogue (OWASP ASVS, its cryptography and configuration
   chapters). **Fixtures are a privacy surface in this PUBLIC repo:** read the fixture byte
   strings this delta adds to `tools/test_secretscan.py` and judge whether any is real key or
   certificate material; locate by file and line, describe by class, quote none. Aim
   `/security-review` at the code diff only from a clean tree, as *House rules* says; weigh a
   clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-06 UTC, from the worktree
root at `b2851e9`, in the foreground; its results are held in the sibling. Read exit codes
explicitly. Check `uptime` first and run the heavy lines under `nice -n 10`.

- `python3 -m unittest discover -s tools -p test_secretscan.py`
- `python3 tools/secretscan.py --selftest`
- the full suite once: `nice -n 10 python3 -m unittest discover -s tools`
- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane ci --root .`, and
  `--plane hook`
- the tree: `python3 tools/secretscan.py --root . . --json` to a scratch file; read `counts`,
  the rules of `findings`, and `suppressed.by_public_key_line`
- the `--staged` path, on a throwaway repo under your scratchpad (the commands below; no cd,
  `GIT_DIR` and `GIT_WORK_TREE` point git at the scratch repo): a new certificate-shaped file
  staged whole, then committed, then re-keyed in place so the staged diff adds body lines only
- the adopting child repos, read-only and by count: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch
  file; extract the pre-delta tools with
  `git archive 0518906 tools | tar -x -C <scratch>/pre1030` (`0518906` is `c5f6202`'s parent);
  then, for each child the report marks `wired` and not the parent, run both
  `python3 <scratch>/pre1030/tools/secretscan.py --root <child> --json <child>` and the same
  with this worktree's `tools/`, and compare exit codes, `counts.blocking` and
  `suppressed.by_public_key_line`. Report totals, never a child's name or path

The `--staged` lines (fixtures built at run time by the test module's own helpers; the
certificate-shaped bytes are random DER, not a certificate):

```
SCR=<scratchpad>/pem-staged; rm -rf "$SCR"; git init -q "$SCR"
git -C "$SCR" config user.email probe; git -C "$SCR" config user.name probe
git -C "$SCR" config commit.gpgsign false
mk() { python3 -c 'import sys; sys.path.insert(0, "tools"); import test_secretscan as t
open(sys.argv[1], "w").write("\n".join(t.pem_lines(sys.argv[2],
    t.der_blob(476, seed=int(sys.argv[3])))) + "\n")' "$@"; }
mk "$SCR/cert.pem" CERTIFICATE 13; git -C "$SCR" add cert.pem
GIT_DIR="$SCR/.git" GIT_WORK_TREE="$SCR" \
  python3 tools/secretscan.py --staged --root "$SCR"; echo "new cert exit $?"
git -C "$SCR" commit -qm cert --no-verify
mk "$SCR/cert.pem" CERTIFICATE 1; git -C "$SCR" add cert.pem
GIT_DIR="$SCR/.git" GIT_WORK_TREE="$SCR" \
  python3 tools/secretscan.py --staged --root "$SCR"; echo "body-only exit $?"
```

Run them from the worktree root. Extend the scratch repo as your probes need (the fail-closed
case, other labels, forged blocks); never commit to anything but the scratch repo.

## House rules for this run

- **Local only.** The pass runs on the laptop, on Fable 5.1, through Claude Code. No live system
  is touched: no network service, no remote, no push, no `gh` call that writes. Probes run on
  scratch copies and synthetic fixtures under your scratchpad only.
- **Never print a secret.** Build any key or certificate shape at run time from the test
  module's helpers (`der_blob`, `pem_lines`, `synthetic_private_der`) or from random bytes. If
  you generate a real key or certificate with `openssl`, keep it under your scratchpad, never
  print its body, never quote it in the verdict, and delete it when you finish.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file.
  Other sessions may be live on this machine: touch nothing outside your worktree and
  scratchpad. Never open another `docs/reviews/` file before phase 2, including the `160/1040`
  brief, its sibling and its verdict.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to the orchestrator to commit). Read-only git is fine. Scratch repos,
  extracted trees, mutated copies and fixtures go under your session scratchpad and are deleted
  when you finish; never mutate the worktree's `tools/`.
- The child repos are read-only to you: no write, no git command that writes, no file copied out
  of them. Count only.
- One heavy process at a time; foreground, with a long timeout. Never run an installed tool by
  bare name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude
  read by hand — never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or
  a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo
  is PUBLIC: quote no secret, placeholder token, email address, key or certificate body, child
  repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1030-rule-4-cold-pass-queued-secretscan-public-pem-block-spans.md`,
this brief's sibling `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.deferred.md`
(held by the orchestrator), every delta commit's message body, and these records beyond their
first line (the title):

- `docs/roadmap/320-child-filed-findings-via-pointing-up/790-hand-up-secretscan-flags-every-body-line-of-a-public-certificate.md`
  (the intent record)
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/380-the-scanners-exempt-test-files-hold-a-promise-nothing-checks.md`
- `docs/roadmap/160-doctrine-review-owed/1040-rule-4-cold-pass-queued-secretscan-reads-exempt-files-for-private-keys.md`
  and the `160/1040` brief and sibling

The delta's own docstrings, comments, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1030-rule-4-cold-pass-queued-secretscan-public-pem-block-spans.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1040-rule-4-cold-pass-queued-secretscan-reads-exempt-files-for-private-keys.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/790-hand-up-secretscan-flags-every-body-line-of-a-public-certificate.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/380-the-scanners-exempt-test-files-hold-a-promise-nothing-checks.md \
  '<pattern>'
```

For the reconcile surfaces, the pattern is `'320/790|public-key line|PUBLIC_KEY_RX'`.
`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
questions, your own assumptions and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, the orchestrator, what you read,
the UTC day you ran on), per-lens answers, the standing checklist V1–V7 each answered or
discharged with grounds, each load-bearing assumption you named damaged or confirmed with its
probe, an answer to each of the pointer's three questions, a per-commit ledger (`c5f6202`,
`3d53b67`: read body-free yes/no, findings by id), findings with stable IDs (prefix `PM`: `PM1`,
`PM2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger (commands and results, children by
count only) and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the
sibling is opened. The orchestrator commits it and only then hands over the sibling. Edit no
other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The code is a guard and the guard is doctrine by function, so every finding is the principal's
to decide (rule 3): record all, apply nothing. Counsel per finding is welcome, labelled as
counsel and kept beneath it.

---

## Verdict — act 1 (2026-11-06 UTC)

### Provenance (V7)

- **Reviewer:** a Fable 5.1 subagent (`claude-fable-5-1`) started for this pass alone, with its
  own context, on 2026-11-06 UTC; the tier was checked at selection. It ran locally, on the
  laptop through Claude Code, not through any API harness, per the principal's approval of
  2026-11-06 quoted in *Spawn provenance* above.
- **Orchestrator:** drain session `850e2a78` (Opus 5.5). It holds the context partition (this
  brief's `.deferred.md` sibling was removed from the review worktree and is handed over only
  after act 1 is committed), commits the records, and forms no finding and writes no severity.
  It wrote neither the delta nor this brief; it started the headless brief-writer `782f8a66`
  with pointers only.
- **Barred, and not involved:** session `722ac2e2` and everything it started (the author and
  its Sonnet workers); the brief-writer `782f8a66`. Neither started nor instructed this
  reviewer.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1030-2041/atelier`, a fresh checkout
  of origin/main at `a7e9167`, read-only to this reviewer except for this file. No git command
  that writes was run in it; the orchestrator commits.
- **What was read:** this brief whole; `docs/method/REVIEW.md` lines 245–462; `docs/method/
  SECRETS.md` lines 186–262; the two delta commits and `0d8db9c` body-free through
  `coldsweep --commit`, scoped to the four delta paths; `tools/secretscan.py` at HEAD (the
  module docstring, `Tally`, lines 395–570, 1006–1140, 1238–1340, 1684–1745, 1870–1915);
  `tools/report.py` lines 170–230; `tools/test_secretscan.py` lines 365–380 and 752–792 plus
  the delta's own additions; `tools/README.md` lines 575–640 and the `320/790` section;
  `.secretscanignore`; `CHANGELOG.md`'s two 2026-11-06 entries; `--help` of `secretscan`,
  `coldsweep` and `floorfleet`; `docs/decisions/` file names. Sweeps ran through `coldsweep`
  with the four `--also-exclude` paths the brief lists; `--include-barred` was not used.
- **Not opened:** `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any other file
  under `docs/reviews/`, the sibling, the four barred board items beyond their titles, and
  every delta commit's message body. Exposure, disclosed: the tree scan's JSON lists the
  paths of its 28 advisory findings, three of which are file names under `docs/reviews/`
  (names only, none opened); the fleet report's JSON carries child names and paths, which
  the comparison script read and never printed; the harness loaded user-level and repo
  instruction files and a memory index, which hold context this verdict does not carry.
- **`/security-review`:** discharged by grounds. It reads the session's pending diff, which
  here is this brief and a deleted sibling, not the delta; the shell's working directory
  resets per command, so a scratch clone carrying the diff could not be made the session's
  tree without dirtying this worktree. The code-altitude read was done by hand (lens 4).

### Load-bearing assumptions, named first (lens 1)

| # | Assumption the delta rests on | Probe | Result |
|---|---|---|---|
| A1 | A certificate's body lines were **blocking** findings before, so a child had no quiet route | pre-delta tools (`git archive 0518906`) on a real openssl certificate | **confirmed**: 9 × `high-entropy`/block, exit 1; HEAD: 0, exit 0 |
| A2 | No allow-marker can cover a block, so the block must be recognised in code | marker grammar in `tools/README.md` (per line, or a per-file glob; `--disable` is run-wide) | **confirmed**; no ranged or rule-scoped glob exists, so the shape chosen is the one the grammar leaves |
| A3 | The DER shape (outer SEQUENCE whose first element is a SEQUENCE) separates every private-key form from a certificate or public key | synthetic `EncryptedPrivateKeyInfo`; a real openssl `ENCRYPTED PRIVATE KEY` relabelled; a DER-framed random secret | **damaged** — PM2 |
| A4 | The index copy is what the commit holds, and its line numbers are the diff's post-image numbers | the brief's two `--staged` lines; `report.staged_blob` reads `git cat-file blob :0:<path>` and inherits `GIT_INDEX_FILE` | **confirmed**: body-only diff of 10 lines with no BEGIN → exit 0, 10 by public-key line |
| A5 | Memory stays bounded as 020/370 promised (the comment: "about 150 KiB per open block") | a block of 2,000 body lines each indented by 200,000 spaces | **damaged** — PM3 |
| A6 | A narrowing of the blocking set may be settled at tool altitude | `SECRETS.md` § posture, third paragraph; the E3 comment cites a ruling, the 320/790 comment cites none; the brief: no ruling on this design | **damaged** — PM1 |
| A7 | Only the entropy rule is suppressed; named and assigned rules still run on body lines | tests (AWS id, `password=` inside a block); a real encrypted key under its own header still fires `private-key-header` at HEAD | **confirmed** |

**Right problem, right altitude, right shape?** The problem is real (A1) and the per-line
carve-out could not reach it (A2), so recognising the block is the right shape, and holding
the lines until END and voiding the whole block on any defect is the right posture. The
altitude is the defect: the delta is a deliberate blind spot in a guard whose doctrine says
over-flag when uncertain and that narrowing is the principal's decision, recorded on the
roadmap or in an ADR, "never let the code comment be the record" (`SECRETS.md` lines 217–223).
This delta's record is a code comment, a README section and a CHANGELOG entry. See PM1.

### Lens 2 — correctness and quality

Both commits diffed body-free and re-driven live. The code does what its comments say in
every case I could build except two: one standard private-key form passes the shape check
(PM2), and the held-block memory bound is not what the comment states (PM3). The streaming
reader preserves order, so `_scan_file`'s overlong-window dedupe and the per-line allow-marker
logic are unchanged; a block that is voided releases its lines as ordinary lines and re-reads
the voiding line, so a certificate after an unterminated one stands alone (test and probe).
`_der_element` accepts a non-minimal long-form length (BER, not DER); harmless for a shape
heuristic and noted only. Overclaims, each against the text that makes it:

- "which **no private-key DER form** has: PKCS#8, PKCS#1 and SEC1 all open with an `INTEGER`
  version" (`tools/README.md` table, last row; `CHANGELOG.md` 320/790 entry; the 320/790
  comment and the `_is_der_sequence` docstring in `tools/secretscan.py`) — PM2.
- "the buffer for it held at 2048 x 76 characters, about 150 KiB, per open block" (the
  320/790 comment, `tools/secretscan.py`) — PM3.
- "the hook's hot path is unchanged for every other file" (`staged_pem_lines` docstring) and
  "a file with no long base64 line among its added lines never reads a blob" (README,
  CHANGELOG) — the second is exact, the first is wider than it: PM7.
- "the largest certificate in current use (an SLH-DSA-256f signature …)" (README, comment):
  SLH-DSA certificates are standardised, not in current use. The bound itself is sound and
  the test pins both sides of it. Wording only; no finding.

### Lens 3 — completeness and harvest

- **Mirror sites (V3):** `tools/README.md` and `CHANGELOG.md` carry the change. No doctrine
  file, child template or skill enumerates `secretscan`'s carve-outs (coldsweep over
  `320/790|public-key line|PUBLIC_KEY_RX|by_public_key_line|public_key_spans` and over the
  certificate wording: hits only in the delta files, `tools/test_report.py`'s summary-line
  fixture and roadmap `020`'s README on the 2026-08-09 counting). Two sites inside the delta's
  own files were not swept: the README's running carve-out sentence (PM6) and the
  `BlockingSetNeverShrinks` docstring (PM1).
- **Tests that would stay green on a broken exemption.** Twelve mutants of a scratch copy of
  `tools/` (inside a `git init`-ed directory, with an unmutated control that ran green), each
  against `test_secretscan.py`: eight go red on exactly the test written for them. Four stay
  green: the fail-closed blob path (`except STAGED_DIFF_FAILURES` replaced by "treat as no
  exemption"), the empty-block guard (`bool(held)`), an indefinite DER length (`0x80`), and
  BEGIN matched by `search` instead of `fullmatch`. See PM4. The first of those is the
  pointer's own question and the docstring's own promise.
- **Harvest.** `0d8db9c` (115/380, under `160/1040`) reuses `_der_element`, the PEM bound and
  the line regex unchanged; it adds callers only. Its README row for `ENCRYPTED PRIVATE KEY`
  describes the very outline PM2 is about, so the fact was in the tree the same day and the
  claim here was not reconciled to it (V5).

### Lens 4 — security and privacy

- **Catalogue check (OWASP ASVS 4.0.3).** V1.6/V6.4 (secrets and keys never in source: the
  exemption must not cover a private key) — PM2 is the gap. V7.1 (no sensitive data in
  output): holds; the report prints a redacted fingerprint only, and `git_diff_failed` prints
  git's stderr, which names a path, never content. "Fail securely" (CWE-636): holds for the
  blob read (exit 2 on a raised `CalledProcessError`, and again when git dies after a partial
  stream — probe E1/E2) and for EOF inside an open block; untested (PM4). CWE-400 resource
  exhaustion: PM3. CWE-1333 ReDoS: both regexes are linear (`[A-Za-z0-9+/]+={0,2}` under
  `fullmatch`; a fixed alternation for BEGIN). Injection: the subprocess runs a fixed argv
  with no shell, and the path is passed as `:0:<path>`, so a path starting with `-` cannot be
  read as an option. The decode is bounded: at most 2048 × 76 characters of base64, so at
  most ~114 KiB of DER, read for two headers, no recursion.
- **Threat model, stated by me because the delta does not state it:** the shape check
  defends against an *accident* (a mislabel, an editor gluing a key under a certificate's
  header), not an *adversary*. A committer who frames a secret as `SEQUENCE { SEQUENCE {},
  bytes }` under a forged header is exempt (probe A2) — and could equally add a
  `.secretscanignore` line. The README calls it "a heuristic on shape"; it should say whom
  the heuristic is for. Counsel, folded under PM2.
- **Fixtures as a privacy surface (this repo is public).** `tools/test_secretscan.py` lines
  1912–1936, `REAL_PEM_BODIES`: a real self-signed X.509 certificate (EC with explicit P-256
  parameters, a synthetic `example.test` subject, one month's validity from 2026-11-06) and
  its SubjectPublicKeyInfo, which carries the same EC point — public material by class, and
  the private half is not in the file. Corroborated: the tree scan's `exempt-private-key`
  advisory (115/380) over that exempt file reports 0. Every other fixture is random bytes in
  a DER outline (`der_blob`, `synthetic_private_der`, with public algorithm OIDs), and the
  private-key labels are assembled from parts. No real key material; nothing to quote.

### The pointer's three questions

1. **Can any input other than a public certificate or public key reach the exemption?** Yes,
   one that matters: a PKCS#8 `EncryptedPrivateKeyInfo` under a `CERTIFICATE` or `PUBLIC KEY`
   header (PM2). The label match (exact `fullmatch` after `strip`; `X CERTIFICATE`,
   `CERTIFICATE REQUEST`, `RSA PUBLIC KEY` all tested), the consecutive-line and base64 rules
   (mutants M1, M6, M8 red; thirteen delimiter shapes probed) and the 2048-line bound (M5
   red) hold. A CSR under a forged header is also exempt; that is public material, noted
   only. The nested-SEQUENCE check is the one condition that is weaker than its claim.
2. **Does `--staged` read the index copy only when it should, and fail closed?** It reads
   `:0:<path>` only when an added line is a body-shaped line of 32+ characters (the no-read
   case is pinned by a test and mutant M11 goes red), inherits `GIT_INDEX_FILE`, and exits 2
   when git cannot give the blob, including after a partial stream (probe E1/E2). It reads
   slightly more often than the docstring says (PM7), and nothing pins the exit 2 (PM4).
3. **Is whole-block voiding right, or too strict for a real-world certificate file?** Right,
   for a PEM file: 64- and 76-column wrapping, CRLF, indentation, YAML block scalars and
   fenced Markdown are all exempt, and a chain is judged certificate by certificate. It is
   too strict only for shapes that were flagged before this delta too and are not PEM files:
   a certificate in a Go or Python multi-line string literal with the quote glued to the
   BEGIN or END line, an END line with a trailing comment, a blank line inside (PM5). The
   README's "not covered" list does not name the first of these, which is the common way a
   CA certificate lives in source.

### Standing checklist V1–V7

- **V1** — three claims stronger than their evidence: PM2, PM3, PM7.
- **V2** — every recorded proof re-run (ledger below); all reproduce. The "fails closed"
  claim was re-driven by probe, not read.
- **V3** — swept with coldsweep; two unswept sites inside the delta's own files: PM6, and the
  test docstring cited under PM1.
- **V4** — the certificate-body carve-out has one home (the README section), but the
  README's older running list of carve-outs still reads as a complete list: PM6.
- **V5** — the delta contradicts three "the blocking set never shrinks" statements (PM1) and
  the next commit's README row on the encrypted PKCS#8 outline (PM2).
- **V6** — lens 4 above; `/security-review` discharged by grounds, hand read done.
- **V7** — provenance stated in the brief and again above.

### Findings

Every finding is the principal's to decide (rule 3): recorded, nothing applied. Counsel is
labelled and kept beneath each.

**PM1 — MODERATE — a narrowing of the blocking set, decided at tool altitude.** Before the
delta a bare certificate file exited 1 with one blocking `high-entropy` finding per body line
(A1); at HEAD it exits 0. Three surfaces state the opposite invariant: `tools/secretscan.py`
module docstring ("**The blocking set never shrinks.** Every input that exited non-zero before
this tier existed still exits non-zero, with the same finding"), `tools/README.md` line 588
("The blocking set never shrinks"), and `tools/test_secretscan.py` lines 756–766, whose
docstring calls E3 "the ONE ruled subtraction (2026-08-04, Mike)" — a sentence that already
omitted the 320/290 URL carve-out and now omits this one. `SECRETS.md` lines 217–223 make a
narrowing the principal's decision, recorded on the roadmap or in an ADR, never in a code
comment; the E3 comment cites its ruling, the 320/790 comment cites none, and this brief
records that no intent record carries a ruling on this design. The change reached every
adopting child at `floor.yml@main` the day it merged. The `BlockingSetNeverShrinks` canaries
cannot see an input-level shrink, so the test that pins the invariant did not move.
*Counsel:* the principal ratifies or reverses. If ratified: record the ruling in `320/790`;
rewrite the three sentences to what is true — the blocking set never shrinks **per rule**,
and the ruled per-input subtractions are E3, 320/290 and 320/790 — in one home with the
other two stamped; and add a certificate-body canary to the test class in the decided
direction so the next carve-out has to touch it.

**PM2 — MODERATE, security — a PKCS#8 encrypted private key passes the shape check.**
`EncryptedPrivateKeyInfo` (RFC 5208 § 6) is `SEQUENCE { encryptionAlgorithm
AlgorithmIdentifier, encryptedData OCTET STRING }`: its first element is a SEQUENCE, so
`_is_der_sequence` accepts it. Probed three ways: a synthetic outline (nested check: True;
under `CERTIFICATE` or `PUBLIC KEY`: 0 findings at HEAD, 6 blocking pre-delta); a real
openssl `ENCRYPTED PRIVATE KEY` (PBES2) relabelled `CERTIFICATE`: 0 findings at HEAD, 8
blocking pre-delta, while under its own header it still blocks and the plaintext PKCS#8 key
relabelled still blocks (the delta's own test case). The claim "no private-key DER form has
it: PKCS#8, PKCS#1 and SEC1 all open with an `INTEGER` version" is false for PKCS#8's second
form, and `0d8db9c`'s README row for `ENCRYPTED PRIVATE KEY` names that outline the same
day. The exposure needs the mislabel or glue the delta itself gives as its reason for the
nested check, and the material is passphrase-protected; the posture is over-flag. A confirmed
security finding carries a recurrence-prevention step and, for tooling this repo ships, the
private-disclosure route in `SECURITY.md` (`REVIEW.md` lines 315–324) — see the follow-ups.
*Counsel:* check the element **sequence** each label actually has, and bind the label to it:
`CERTIFICATE` is `[SEQUENCE, SEQUENCE, BIT STRING]`, `PUBLIC KEY` is `[SEQUENCE, BIT
STRING]`, and `EncryptedPrivateKeyInfo` is `[SEQUENCE, OCTET STRING]`; `0d8db9c` already has
element-walking helpers. Add the encrypted outline to `synthetic_private_der` and to
`test_private_key_shaped_bodies_under_a_public_header_are_flagged`. Say in the README whom the
heuristic defends against (accident, not an adversary; probe A2).

**PM3 — MODERATE — the held block's memory bound is not the one stated.** `pem_exempt_stream`
holds each body line's whole `item`, including the unstripped `text`, and judges it on
`text.strip()`; `_iter_numbered_lines` bounds a line only at `LINE_WINDOW_BYTES` (4 MiB). So a
block of 2,048 body lines each padded with leading whitespace is held at up to 2048 × 4 MiB,
about 8 GiB, not "about 150 KiB". Measured (`ru_maxrss`, fresh interpreter per case, under
`nice`): a 381 MiB file of 2,000 body lines each indented by 200,000 spaces peaks HEAD's
`_scan_file` at 412 MiB; the pre-delta tools at 25 MiB. On the `--staged` path
`staged_pem_lines` iterates the blob with `for raw in stream`, which holds a line whole with
no window at all. This is the 020/370 class (a measured 9 GB incident) in a guard that runs
on every push of every child; it needs a crafted file, so the exploit cost is high and the
fix is small. *Counsel:* hold `(lineno, stripped)` rather than the item, or refuse to hold a
line whose raw length exceeds a few times `PEM_MAX_LINE`; cap the blob line the same way;
restate the comment with the real bound and pin it with a test that measures.

**PM4 — minor — four conditions no test pins.** Mutants that stay green: (a) the blob
failure treated as "no exemption" instead of exit 2 — the pointer's question and the
docstring's promise ("the caller exits 2 rather than treat that as clean"), live-proven by
probe but unpinned; (b) `bool(held)` dropped — `test_empty_block_is_not_a_block` asserts
nothing observable, since an empty block has no line to exempt or flag either way; (c)
`_der_element` accepting the indefinite length `0x80`; (d) `_PEM_BEGIN_RX` by `search`
rather than `fullmatch`. (a) is the one that matters. *Counsel:* a test that monkeypatches
`report.staged_blob` to raise a `STAGED_DIFF_FAILURES` member and asserts exit 2; replace
(b) with a test that can fail, or drop it; a one-byte case each for (c) and (d).

**PM5 — minor — real shapes the README's "not covered" list does not name.** Probed at HEAD:
a certificate in a Go backtick or Python triple-quoted literal with the quote glued to the
BEGIN or END line (9 blocking findings each), an END line with a trailing comment (9), a
blank line inside (9), one unwrapped body line (7), line-quoted fragments (9). All flagged
before the delta too, so no regression, and all fail closed. The README names other labels
and "a certificate escaped inside a one-line string"; the glued multi-line literal is the
common way a CA certificate lives in source and is not named. *Counsel:* name it as not
covered, or decide to widen (a quote or backtick prefix on BEGIN and suffix on END) — a
widening, so the principal's call.

**PM6 — note — the README's running carve-out sentence not updated (V4).** `tools/README.md`
lines 598–601 list what the entropy net skips (public-key material, fingerprints, URL path)
and read as complete; the block body is described fifteen lines later. One sentence.

**PM7 — note — the hot-path claim is wider than the code.** `staged_pem_lines` reads the
blob for any file whose added lines include a 32+ character line of `[A-Za-z0-9+/]` — a hex
digest qualifies — not only for certificate files. Cost is one `git cat-file`, fail-closed.
The docstring's "unchanged for every other file" should say "for a file with no such line",
which is what the README and CHANGELOG already say.

**PM8 — note — a widened meaning under an unchanged name.** `by public-key line` now counts
body spans too, so a reader comparing a pre- and post-delta summary line sees the number
climb with nothing on the line saying why. Decided and documented; noted so the next reader
of a jump knows where to look.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `c5f6202` | yes (`coldsweep --commit`, four paths) | PM1, PM3, PM4 (a, b, d), PM5, PM6, PM7, PM8 |
| `3d53b67` | yes (same) | PM2 (the nested check and its claim), PM4 (c) |
| `0d8db9c` | yes (same; later commit on the same paths, read for its bearing only) | none of its own here; cited under PM2 (V5) |

### Re-run ledger (all from the worktree root, 2026-11-06 UTC, `uptime` load 1.9–3.4)

| Command | Result |
|---|---|
| `python3 -m unittest discover -s tools -p test_secretscan.py` (nice) | 239 tests, OK, exit 0 |
| `python3 tools/secretscan.py --selftest` | `selftest OK`, exit 0 |
| `nice -n 10 python3 -m unittest discover -s tools` | exit 0 (the count line was cut by my own `tail`; the exit is the record) |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | exit 0; `secretscan` enforced, 🟡 28 advisory; `leakscan` enforced, 🟡 3 advisory; every other guard clean |
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | exit 0, all guards clean |
| `python3 tools/secretscan.py --root . . --json` | exit 0; `counts` blocking 0, advisory 28 (all `low-variety-entropy`); `suppressed.by_public_key_line` 3; `files_by_ignore_glob` 3 |
| the brief's `--staged` lines on a scratch repo | new certificate staged whole: exit 0, 10 by public-key line; re-keyed in place (10 added body lines, 0 BEGIN in the diff): exit 0, 10 by public-key line |
| `--staged` fail-closed (probe, `report.staged_blob` raising) | exit 2 on `CalledProcessError`; exit 2 when git dies after a partial stream |
| `python3 tools/floorfleet.py --root <clones dir> --json` | exit 0; 23 repos: 22 wired (one of them the parent), 1 absent |
| pre-delta (`git archive 0518906 tools`) vs HEAD `secretscan --root <child> --json <child>`, per wired child, by count | 21 children compared; exit codes identical (18 × 0, 3 × 1 on both); `counts.blocking` identical (11,023 in total on both); `suppressed.by_public_key_line` identical (111,985 on both); 20 identical in every field, 1 differs in the advisory count only (the `115/380` rule, which the pre-delta tools lack). So the body exemption fires on **no line** anywhere in the fleet today: no child has a certificate block in a scanned file |
| twelve mutants vs `test_secretscan.py` (scratch copy, `git init`-ed, control green) | 8 red on their own test; 4 green (PM4) |
| memory probe, `_scan_file` peak RSS | PM3: 17/25/412 MiB (HEAD) vs 17/20/25 MiB (pre) for 0 / 2,000 / 200,000 spaces of indentation |
| shape probes (DER forms, thirteen delimiter shapes) | PM2, PM5; a real openssl certificate: 0 findings at HEAD, 9 blocking pre-delta |

Scratch (probe scripts, the scratch repo, the pre-delta tree, mutant copies, the one real
encrypted key) lived under the session scratchpad `rev1030/`; the key was deleted by the probe
that made it, and the rest is deleted at the end of act 1 except the scripts act 2 may re-run.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (PM1, PM2, PM3) · 2 minor (PM4, PM5) · 3 note
(PM6, PM7, PM8).** The block is recognised carefully and voided on every defect I could build
but one; that one is a standard private-key form, and the three MODERATE findings are each a
claim the delta makes that its own probes would have falsified. No MAJOR: the work is the
right shape at the wrong altitude, and the cycle can close on the principal's rulings.

### Follow-up checklist

- [ ] 🎯 PM1 — ratify or reverse the carve-out; if ratified, record the ruling in `320/790`
      and reconcile the three "never shrinks" sentences (one home, two stamps).
- [ ] 🎯 PM2 — decide the fix (counsel: per-label element sequence) and its recurrence step;
      the `SECURITY.md` route is the principal's call, since the affected fleet is his own
      and the exposure needs a mislabelled, passphrase-protected key.
- [ ] ⏳ For the orchestrator, before committing act 1: PM2 is a confirmed security finding
      in a public repo; the commit publishes it. My counsel is that it is proportionate to
      publish (no secret, no child named, exploit needs the mislabel), but the call is not
      mine.
- [ ] 🎯 PM3 — hold stripped lines (or cap the raw line) on both paths; restate the bound.
- [ ] PM4 — pin the exit-2 path; mend or drop the vacuous test.
- [ ] 🎯 PM5 — name the glued-literal shape as not covered, or widen (a widening is his).
- [ ] PM6, PM7 — one sentence each.
- [ ] 🤔 For the principal: should a `PUBLIC KEY` label accept a certificate's shape and vice
      versa? Today either shape passes under either label; binding them is part of PM2's
      counsel.
- [ ] Act 2: reconcile against the sibling and the author's account; the orchestrator folds
      the sibling in.
