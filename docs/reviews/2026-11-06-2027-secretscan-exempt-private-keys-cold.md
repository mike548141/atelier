# Cold pass — secretscan still reads a file its .secretscanignore exempts, for real private keys

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (guard code is doctrine by
function).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACTS 1 AND 2 RUN — verdict and reconcile below: FAIL, 2 MAJOR · 4 MODERATE ·
6 minor · 4 note (XK1–XK16; XK13–XK16 formed at reconcile). Run 2026-11-06 UTC by a cold Fable
5.1 reviewer under orchestrator `850e2a78`, act 1 committed as `7c6b781` before the sibling was
opened. Brief written 2026-11-06 UTC by session `782f8a66`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1040-rule-4-cold-pass-queued-secretscan-reads-exempt-files-for-private-keys.md`.
**Why it earns a review:** `secretscan` is the credential boundary every adopting child floats on
at `floor.yml@main`, and this change alters what the guard reads inside its own exemptions, in
every child at once. Its green exit is read as "no real private key sits in an exempt file".
The worst failures are silent ones: a real key in an exempt file that the check does not see,
or a check that is slow, unbounded or noisy enough to be turned off.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session
  `722ac2e2`, 2026-11-06, and the Sonnet worker it dispatched, which wrote the code (per the
  queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `782f8a66` (`claude-opus-5-5`), a headless brief-writer
  started on 2026-11-06 by drain session `850e2a78` (Opus 5.5). Neither authored any of this
  delta, and neither was started or instructed by `722ac2e2`. **Off-tier for review,
  disclosed: the brief-writer forms no finding and writes no severity**, and stops after this
  brief, its sibling and the one for `160/1030`. It ran no review and used no Fable model.
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
  orchestrator). The reviewer of `160/1030` may not also review this pass in the same context.
- **The principal's approval**, 2026-11-06, as the queue pointer records it: asked whether the
  session he opens for `160/1030` should review this too, he picked **"Yes, both in that
  session"**, on the same terms as `160/1030`, whose approval is verbatim: *"If you can run it
  using the API credit and achieve parity of quality in the review as doing it locally then use
  the API. If you cant achieve parity then run it on fable locally now"*. The orchestrator's
  dispatch fixes the local route: this pass runs on the laptop through Claude Code, not through
  any API harness.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before
  writing):
  - its dispatch instructions; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md`
    whole; `docs/method/SECRETS.md` heading list and lines 111–135 and 188–262;
  - the house-form brief `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` and its
    sibling as they stood at commit `33ebcb6` (before that pass ran; other surfaces), and that
    commit's message;
  - board items `160/1030` and `160/1040` whole; **both intent records, `115/380` and
    `320/790`, whole, including the authors' landing accounts and a recorded probe result**;
    board item `160/950` whole, which carries the **summary of another pass's verdict** on the
    staged-diff reader that `secretscan --staged` uses (`115/360`);
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
posture — over-flag, because detection enables everything* (from line 188), including its
account of the advisory tier and of who decides a narrowing of coverage. The delta itself states
its purpose, its limits and its known gaps in `tools/README.md` § *What an exemption still
checks (115/380)*, in the `115/380` comment in `tools/secretscan.py`, in `.secretscanignore` and
in its `CHANGELOG.md` entry; those are the author's claims to test, not settled scope.

## What the work is

One commit on `main`, which closes `115/380`:

- **`0d8db9c`** — `secretscan: read an exempt file for a real private key, advisory (115/380)`.

Delta paths: `tools/secretscan.py`, `tools/test_secretscan.py`, `tools/README.md`,
`CHANGELOG.md` (the `115/380` entry), `.secretscanignore`. The commit also touches board
records; those are barred until phase 2 (below), so always pass `--path`. Read it body-free:

```
python3 tools/coldsweep.py --root . --commit 0d8db9c \
  --path tools/secretscan.py --path tools/test_secretscan.py \
  --path tools/README.md --path CHANGELOG.md --path .secretscanignore
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Review each delta path at HEAD too. The delta builds on `c5f6202` and `3d53b67`
(`320/790`: the DER helpers and the PEM bound it reuses), which are under their own pass
(`160/1030`); read them only as far as they bear on this delta. Confirm nothing has landed since
with
`git log --oneline 0d8db9c..HEAD -- tools/secretscan.py tools/test_secretscan.py tools/README.md CHANGELOG.md .secretscanignore`,
and read anything new the same way.

## The questions the queue pointer lists

As `160/1040` lists them, verbatim:

> the fragment-joining state machine in `exempt_key_hits` (what real shapes it misses, and
> whether any input makes it slow); whether the private-key outline test can match a non-key;
> the staged path reading added lines only.

They are a floor, never a fence. Name your own load-bearing assumptions first (lens 1).

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and
live behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in
scope.

**Non-goals:** the `320/790` entropy exemption in its own right (pass `160/1030`); the rules that
run on files no glob exempts, except where this delta changes what reaches them or how they are
reported.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   Ask whether this is the right problem, solved at the right altitude and with the right shape
   and response tier, against the posture above.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
   the text that makes it (docstrings, comments, `tools/README.md`, `CHANGELOG.md`,
   `.secretscanignore`, `--help`, the printed advisory block and summary line).
3. **Completeness / harvest.** Every surface that states what an exempt file is, how
   `secretscan`'s advisory tier works or how its rules are named and disabled (V3); one home
   (V4); no contradiction (V5); tests that would stay green on a broken check (mutate a scratch
   copy and re-run).
4. **Security & privacy** — mandatory, and the reason this pass exists. The check parses
   untrusted text and decodes it, so check it by hand for resource exhaustion (regular-expression
   backtracking included) and fail-open paths, and check the likely vectors against an open
   catalogue (OWASP ASVS, its cryptography and configuration chapters). **Fixtures are a
   privacy surface in this PUBLIC repo:** read every fixture this delta adds to
   `tools/test_secretscan.py` and judge whether any is real key material; locate by file and
   line, describe by class, quote none. Aim `/security-review` at the code diff only from a clean
   tree, as *House rules* says; weigh a clean pass over markdown as nothing.

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
  the rules of `findings` and `suppressed.files_by_ignore_glob`
- HEAD's check over every copy of `tools/test_secretscan.py` that `main` has held since the
  `320/790` work began (`c5f6202`, `3d53b67`, `0d8db9c`), by count of hits only (the loop below;
  quote the sha and path together, as `zsh` reads `$c:t` as a modifier)
- the exempt file, staged and whole, on a throwaway repo under your scratchpad (the commands
  below; no cd, `GIT_DIR` and `GIT_WORK_TREE` point git at the scratch repo): one exempt file
  holding a synthetic private key written as a Python test writes one; then the whole-tree scan,
  and the whole-tree scan with `--disable exempt-private-key`
- the adopting child repos, read-only and by count: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch
  file; extract the pre-delta tools with
  `git archive 815dce6 tools | tar -x -C <scratch>/pre1040` (`815dce6` is `0d8db9c`'s parent);
  then, for each child the report marks `wired` and not the parent, run both
  `python3 <scratch>/pre1040/tools/secretscan.py --root <child> --json <child>` and the same
  with this worktree's `tools/`, timing each, and compare exit codes, `counts.blocking`,
  `exempt-private-key` findings and run time. Count the children that carry a
  `.secretscanignore`. Report totals, never a child's name or path, and quote no excerpt

The test-file loop:

```
for c in c5f6202 3d53b67 0d8db9c; do
  git show "${c}:tools/test_secretscan.py" > <scratchpad>/tss-$c.py
  python3 -c 'import sys; sys.path.insert(0, "tools"); import secretscan as ss
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
print(sys.argv[2], len(list(ss.exempt_key_hits((i, t) for i, t in enumerate(lines, 1)))))' \
    <scratchpad>/tss-$c.py "$c"
done
```

The exempt-file lines (the key is random bytes in a private key's outline, built at run time by
the test module's own helpers; nothing real is written):

```
SCR=<scratchpad>/exempt-staged; rm -rf "$SCR"; git init -q "$SCR"
printf '# synthetic fixtures for this probe\nfixtures.py\n' > "$SCR/.secretscanignore"
python3 -c 'import sys; sys.path.insert(0, "tools"); import test_secretscan as t
open(sys.argv[1], "w").write("\n".join(t.py_fragments(t.synthetic_private_der("RSA_PKCS8")))
    + "\n")' "$SCR/fixtures.py"
git -C "$SCR" add .secretscanignore fixtures.py
GIT_DIR="$SCR/.git" GIT_WORK_TREE="$SCR" \
  python3 tools/secretscan.py --staged --root "$SCR" --json; echo "staged exit $?"
python3 tools/secretscan.py --root "$SCR" --json "$SCR"; echo "tree exit $?"
python3 tools/secretscan.py --root "$SCR" --disable exempt-private-key "$SCR"
echo "disabled exit $?"
```

Run them from the worktree root. Extend the scratch repo as your probes need (other key forms,
other wrappings, partial stagings, hostile inputs); never commit to anything but the scratch
repo.

## House rules for this run

- **Local only.** The pass runs on the laptop, on Fable 5.1, through Claude Code. No live system
  is touched: no network service, no remote, no push, no `gh` call that writes. Probes run on
  scratch copies and synthetic fixtures under your scratchpad only.
- **Never print a secret.** Build any key shape at run time from the test module's helpers
  (`synthetic_private_der`, `py_fragments`, `pem_lines`, `der_blob`) or from random bytes. If you
  generate a real key with `openssl` or `ssh-keygen` to test a real shape, keep it under your
  scratchpad, never print its body, never quote it in the verdict, and delete it when you
  finish. Quote no finding's excerpt beyond its form and length, and none of a fixture's bytes.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file.
  Other sessions may be live on this machine: touch nothing outside your worktree and
  scratchpad. Never open another `docs/reviews/` file before phase 2, including the `160/1030`
  brief, its sibling and its verdict.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to the orchestrator to commit). Read-only git is fine. Scratch repos,
  extracted trees, mutated copies and fixtures go under your session scratchpad and are deleted
  when you finish; never mutate the worktree's `tools/`.
- The child repos are read-only to you: no write, no git command that writes, no file copied out
  of them. Count only. Where the check reports a hit in a child, record the count and the form
  (`PKCS#8`, `SEC1`, …) only, never the path or the excerpt.
- One heavy process at a time; foreground, with a long timeout. Never run an installed tool by
  bare name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude
  read by hand — never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or
  a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo
  is PUBLIC: quote no secret, placeholder token, email address, key body, child repo name or
  path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1040-rule-4-cold-pass-queued-secretscan-reads-exempt-files-for-private-keys.md`,
this brief's sibling (now folded at the end of this file; held by the orchestrator until
act 1 was committed), every delta commit's message body, and these records beyond their first line
(the title):

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/380-the-scanners-exempt-test-files-hold-a-promise-nothing-checks.md`
  (the intent record)
- `docs/roadmap/320-child-filed-findings-via-pointing-up/790-hand-up-secretscan-flags-every-body-line-of-a-public-certificate.md`
- `docs/roadmap/160-doctrine-review-owed/1030-rule-4-cold-pass-queued-secretscan-public-pem-block-spans.md`
  and the `160/1030` brief and sibling

The delta's own docstrings, comments, `tools/README.md`, `.secretscanignore` and `CHANGELOG.md`
entries carry the author's account of why; they are the delta, and reading the delta is never
barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1040-rule-4-cold-pass-queued-secretscan-reads-exempt-files-for-private-keys.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1030-rule-4-cold-pass-queued-secretscan-public-pem-block-spans.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/380-the-scanners-exempt-test-files-hold-a-promise-nothing-checks.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/790-hand-up-secretscan-flags-every-body-line-of-a-public-certificate.md \
  '<pattern>'
```

For the reconcile surfaces, the pattern is `'115/380|exempt-private-key|secretscanignore'`.
`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
questions, your own assumptions and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, the orchestrator, what you read,
the UTC day you ran on), per-lens answers, the standing checklist V1–V7 each answered or
discharged with grounds, each load-bearing assumption you named damaged or confirmed with its
probe, an answer to each of the pointer's three questions, a per-commit ledger (`0d8db9c`: read
body-free yes/no, findings by id), findings with stable IDs (prefix `XK`: `XK1`, `XK2`, …) and
severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
with counts, a re-run ledger (commands and results, children by count only) and a follow-up
checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling is opened. The
orchestrator commits it and only then hands over the sibling. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The code is a guard and the guard is doctrine by function, so every finding is the principal's
to decide (rule 3): record all, apply nothing. Counsel per finding is welcome, labelled as
counsel and kept beneath it.

---

## Verdict — act 1 (cold pass, run 2026-11-06 UTC)

### Provenance, repeated

- **Reviewer:** a Fable 5.1 subagent (`claude-fable-5-1`), started for this pass alone by drain
  session `850e2a78` (Opus 5.5), with its own fresh context. Tier checked at selection. The
  pass ran locally, on the laptop through Claude Code, not through any API harness. The
  principal approved it on 2026-11-06 ("Yes, both in that session", on the `160/1030` terms the
  brief quotes).
- **Orchestrator:** `850e2a78` holds the context partition (this brief's `.deferred.md` sibling
  was removed from the review worktree and is handed over only after act 1 is committed),
  commits the records, **forms no finding and writes no severity**. It wrote neither the delta
  nor the brief; it started the headless brief-writer `782f8a66` with pointers only.
- **Barred, and honoured:** the reviewer was neither started nor instructed by `722ac2e2` (the
  author) or anything it started, nor by `782f8a66`. It is not the reviewer of `160/1030`, which
  ran earlier the same day in a separate context. No contact with any of them.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-1040-2115/atelier`, a fresh
  checkout of origin/main at `ec24318`, read-only to the reviewer except for this file. Nothing
  landed on the delta paths after `0d8db9c` (`git log 0d8db9c..HEAD -- <paths>`: empty).
- **What was read:** this brief; `docs/method/REVIEW.md` whole; `docs/method/SECRETS.md` from
  line 100; the delta body-free through `coldsweep --commit 0d8db9c --path …` (subject, stat,
  diff; the message body was not read) and each delta path at HEAD; the supporting HEAD code the
  delta leans on (`_der_element`, the 020/370 line reader, the PEM bounds, `Finding`, `_record`,
  the `--staged` path, `_render_advisory`, `--help`); the test module's helpers; the touched-path
  list of `0d8db9c` by name only (`git diff-tree --name-only`); board item `115/050` whole (not
  barred, surfaced by the sweep); the first line of `320/140`; `docs/build/templates/workflows/
  floor.yml` lines 50–70 and `commands/scan.md` lines 30–40. The tree was swept with `coldsweep`
  and the brief's four `--also-exclude` paths; no `--include-barred`. Not opened: `docs/
  SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any other `docs/reviews/` file, the
  four barred board items beyond their titles, any commit message body, the sibling.
- **Harness exposure, disclosed:** the harness loaded user-level and repo instruction files and
  a memory index, which hold private context this verdict does not carry. One fleet probe
  printed a JSON field holding the children's local-check descriptions into the session
  transcript; none of it is carried into this record.
- **Scratch:** everything under `…/scratchpad/rev1040/` (a scratch git repo, real keys made
  with `openssl` and `ssh-keygen` and never printed, mutated copies of `tools/`, the pre-delta
  `tools/` from `815dce6`). Deleted at the end of act 1, probe scripts included.

### The acceptance test, applied

The posture (`SECRETS.md` § *The boundary's posture*) is: find every private key, over-flag
where uncertain, never narrow coverage at tool altitude, and keep the blocking set from
shrinking. The delta's own claims (README § *What an exemption still checks*, the `115/380`
comment, `.secretscanignore`, `CHANGELOG.md`) were tested one by one. Two hold in full (every
other rule stays skipped for the file; the blocking set and the summary line are unchanged).
Two do not: the one-line PEM forms the README lists as read are not read for any DER-form key
(XK1), and "BOUNDED" is true of memory and false of time (XK2).

### Lens 1 — approach and the load-bearing assumptions, named first

| # | Assumption | Result | Probe |
|---|---|---|---|
| A1 | A private key is the one fixture class a shape test can tell from a fictional one, so one narrow check is the right width | Confirmed as a fact; the records disagree about it (XK5) | `115/050` whole; `private_key_outline` read |
| A2 | Judging on decoded bytes keeps false positives out | Confirmed for every non-key shape tried | tests; certificate, SPKI, DigestInfo, version-2, 4-INTEGER, random bodies all rejected; tree 0 hits; the fleet's 6 hits are unclassified (XK12) |
| A3 | The PEM shapes a test or a config writes — raw, fragments, one-line — are all read | **Damaged**: the `\n`-escaped one-line form is missed for every DER key (XK1) | 7 real keys × 20 wrappings |
| A4 | The bare-run path covers what the PEM path covers, minus the header | **Damaged** for OPENSSH (XK3); ENCRYPTED is stated | 5 OPENSSH keys × 6 bare shapes |
| A5 | The check is bounded | Memory yes; **time no** (XK2) | doubling-ratio timings against the engine |
| A6 | Advisory is the right tier for a fleet rollout | A decision, not a fact; the principal's (XK4) | `SECRETS.md` lines 226–240; roadmap titles |
| A7 | "Exempt" is decided in one place for both modes | Confirmed: `_classify_files` for the tree, `_ignored` for `--staged`, both `allowmarker.ignored` | code; `files_by_glob` 3 on this tree, 1 on scratch |
| A8 | A non-exempt file's behaviour is unchanged | Confirmed | `iter_files` is a filter over `_classify_files` with identical yields; the same key un-exempted blocks on `private-key-header`; full suite (ledger) |
| A9 | `--staged` reads added lines only and never the blob | Confirmed | `reads_no_blob` test; scratch repo: staged hit at line 2, exit 0 |

Right problem, right altitude: yes. `115/050` had already named the class and said a scanner
cannot know a fixture is fictional; the delta answers the one sub-class where bytes *can* say
(a key's DER outline is not a thing a fictional fixture has by accident), and leaves the rest
honestly unread. That is the right narrow shape. The response tier is the open design question
(XK4), and the open item is left contradicting the build (XK5).

### Lens 2 — correctness and quality

**XK1 — MAJOR — The one-line PEM path is defeated by the `+` strip in `_ESCAPES_RX`, so the
`\n`-escaped one-line form is missed for every DER-form key.** `_ESCAPES_RX` is
`\\[nrt]|[\s"'+\\]`: it removes `+`, a base64 alphabet character, from the body before decode
(it is there for `"…" + "…"` concatenation on one line). A real body without a `+` is a
5 % event at EC size and a 10⁻¹¹ event at RSA size, so path (a) fails on essentially every real
one-line key. Path (b) masks that only when the body has no `\n` escapes between its lines, is
at least 100 decoded bytes, and is a DER outline. The masked case is the one the delta's test
uses; the unmasked case is the commoner one: `json.dumps(pem)` — a GCP service-account
`private_key`, a Kubernetes `stringData` value, a Terraform or Ansible variable, a Python
`repr`, a `.env` value — writes `\n` every 64 characters.
Probe, real keys from `openssl`/`ssh-keygen`: the `\n`-escaped one-line form (S4) and a
GCP-shaped JSON holding it — 0 hits for 7/7 DER-form keys (PKCS#8 RSA and EC, PKCS#1 RSA ×2,
SEC1, DSA, ENCRYPTED PKCS#8); 4/4 OPENSSH keys hit only because the magic prefix decodes
before the first `+` corrupts the stream. On the real CLI, the GCP-shaped fixture in an exempt
file: `--staged` 0 advisory, whole tree 0 advisory; the same file un-exempted blocks on
`private-key-header`. Under-floor keys in one-line form: 17/17 synthetic Ed25519 PKCS#8 bodies
with a `+` missed. ENCRYPTED PRIVATE KEY misses in every one-line form, since (b) cannot
rescue it. With `+` removed from the class on a scratch copy: 11/11 S4, 11/11 GCP-JSON, 17/17
Ed25519 hit; the delta's test module stays green (mutation M9). The claim it damages: README
table, "a body of pure base64 on consecutive lines (raw, or quoted fragments)" and the
one-line regex's own comment; the test `test_a_quoted_pem_in_python_is_a_hit_in_both_spellings`
stays green with path (a) dead (mutation M1), so it pins nothing about (a).
Security marks: severity MAJOR; class CWE-184/185 (an incomplete handling of the input
alphabet). Recurrence step: fixtures derived from real tool output (`openssl`, `ssh-keygen`,
`json.dumps`) beside the hand-built ones, and no transformation of a base64 body before decode
without a test whose body carries every alphabet class.
*Counsel:* strip the inter-literal operator, not the character: replace `+` in the class with a
pre-pass on `["']\s*\+\s*["']`; add the `json.dumps(pem)` shape, an under-floor key and an
ENCRYPTED block in one-line form to `ExemptPem`.

**XK2 — MAJOR — Time is not bounded, though the `115/380` comment says BOUNDED.** Memory is
bounded as claimed; run time has two super-linear paths, both reachable from any exempt file in
any child, on the hook and in CI, with `--disable` as the only hatch.
(i) `_PEM_PRIV_ONELINE_RX` (`-----BEGIN (…)-----(.*?)-----END \1-----`) is run on any line
containing `PRIVATE KEY-----` with no length bound; a lazy `.*?` with a backreference retries
from every BEGIN on the line, so cost is quadratic in BEGIN markers: 0.014 s at 250 markers,
×4.0 per doubling, 0.89 s at 2 000 (54 KB). The line reader's window is 4 MiB, so one window of
markers extrapolates to about 90 minutes; the existing engine (`scan_lines`) takes 3 ms on the
same line.
(ii) `_FRAG_RX` and `_TAIL_AFTER_RX` end in `\s*([+,)\\]*)\s*(?:\#.*)?$` — two adjacent `\s*`
with an optional empty group between — which is quadratic in whitespace to reject. The 4 096
bound makes that 0.36 s (`"A` + spaces + `!`) and 0.71 s (16 letters + spaces + `!`) **per
line**, against 0.2 ms in the engine: ×1 800–3 500. A 40 MB exempt fixture of padded lines costs
hours. Plain code and plain base64 lines cost the same as the engine (0.1–0.2 ms).
The brief's acceptance test names "a check that is slow, unbounded or noisy enough to be turned
off" as a worst failure; the child's remedy for a hung hook is `--disable exempt-private-key`,
which blinds the rule for the whole repo. Likelihood is low (a hostile or generated fixture),
impact is a hung gate, fix is a few lines.
Security marks: severity MAJOR; class CWE-1333 / CWE-400. Recurrence step: every regex that
runs on untrusted lines gets a doubling-ratio timing in the test module (the 6 MB test counts
hits; it should also bound time).
*Counsel:* gate the one-line search on a bound of its own (16 KiB holds an RSA-16384 one-liner)
or make it linear (`str.find("-----END ")`, then match the slice before it); collapse the
trailer to one `\s*` — `\s*(?:([+,)\\]+)\s*)?(?:\#.*)?$` rejects linearly; assert a time budget
on the three hostile shapes above.

**XK3 — MODERATE — A bare OPENSSH body is not read, and the gap is not stated.** Path (b)
accepts only a DER outline; an `openssh-key-v1\0` body is `b3BlbnNzaC1rZXktdjEA` in base64, a
fixed prefix. 5/5 OPENSSH keys (ed25519 plain and passphrase-wrapped, ecdsa, rsa) missed in
every bare shape: fragments, dict value with comma, 76-column raw, first fragment on the
assignment line. `ssh-keygen`'s default output on every current platform is this format, so it
is the commonest private key a test would carry. The README's known-gaps list (five entries)
and the comment's (three) do not name it: an overclaim by omission (V1).
*Counsel:* in `_bare_run_hit`, `raw.startswith(OPENSSH_MAGIC)` → form `OPENSSH`; a test per
OPENSSH shape; and the gap list in one place (see XK7).

**XK6 — minor — Traditional encrypted blocks (`Proc-Type: 4,ENCRYPTED` + `DEK-Info`) are real
key material and miss in all 14 shapes for both such keys.** Stated as a non-hit by design
(README table and gap list), on the ground that the body is ciphertext with no outline. The
header pair under a `… PRIVATE KEY` label with a base64 body of key size is as structural a
signal as the OPENSSH magic, and a fictional fixture would have to fake the `DEK-Info` IV
format to trip it. Against the over-flag posture the exclusion errs quiet; a passphrase does
soften the exposure. PKCS#12 (version 3) also misses, unstated; it is normally binary, so low
value.
*Counsel:* either read it as `<PEM … block, traditional-encrypted, N bytes>` or record the
exclusion as the principal's decision (XK4's same question).

**XK11 — note — Two variants of the stated "judged from its first character" gap.** A first
fragment under `EXEMPT_FRAG_MIN` (16) does not open a run, so the join starts at the second
fragment and the key is judged from the wrong byte (S24: 0/11); and a key split across two
literals on one line (`"MIIE…" + "…"`) is judged per run. Both rare; the stated gap covers the
principle, not these instances.

### Lens 3 — completeness and harvest

**XK5 — MODERATE — Open item `115/050` says the opposite and is untouched.** `115/050`
(open, 2026-08-15, under the commissioned `115` track) names this exact class — a real
credential in an exempt fixture file — and says the fictional fact "lives in the author's head
… the answer is not a cleverer scanner", listing three candidate shapes (a declared
fictional-source marker, a commit-time prompt when an exempt file grows, or stating the gap in
the ignore files' reasons). The delta builds a cleverer scanner for the one slice bytes can
judge — a sound partial answer — but `0d8db9c` does not touch `115/050` (path list by name),
reconcile with it, or narrow it to the residual it leaves (a real token or password in an exempt
fixture is still invisible; only a key has a shape). Two open records now disagree (V5).
*Counsel:* amend `115/050` to record `115/380` as the shape-detectable slice and keep the
residual open with its candidate shapes, or close it with grounds; the principal's call, since
the track is his.

**XK7 — minor — Mirror sites missed (V3/V4).** `--help` for `--disable` and README lines
723–724 enumerate the rule names without `exempt-private-key`, while README § `115/380` says
`--disable exempt-private-key` works (it does: `1 rule(s) disabled`, 0 advisory, the file not
read). The known-gaps list exists twice and already differs (the comment: three gaps; the
README: five) — one home, stamped.

**XK8 — minor — Tests that stay green on a broken check.** Fifteen single-point mutations of
a scratch copy of `tools/secretscan.py` against the delta's test module (two
`StagedAbsolutePathTest` failures occur on the unmutated copy too — an artefact of running
outside a git checkout — and are excluded). Caught: path (a) dead, path (b) dead, staged path
dead, dedup removed, escape-lead drop removed, any version byte accepted, hits under
`RESPONSE_BLOCK`, the main-path call removed, the floor raised to 2 000 bytes. **Not caught:**
`_is_encrypted_pkcs8` always true (M4), the OPENSSH magic test always true (M5), the PKCS#8 OID
check dropped (M12), the `EXEMPT_LINE_MAX` guard removed (M7), the rule's advisory explanation
removed (M8). So the README's "a placeholder body … cannot trip it" is untested for the
ENCRYPTED and OPENSSH labels, and no cost bound has a test. With XK1's note on the one-line
test, that is six claims with no test behind them.
*Counsel:* negative tests for the ENCRYPTED and OPENSSH labels with random bodies; a time
budget on the hostile lines; a test that the advisory block names the rule's remedy.

**XK9 — minor — No hatch for a true false positive but `--disable`.** `_exempt_findings`
records straight through `_record`, bypassing the allow-marker (probe: `secretscan:allow:` on
the line, hit stands, 0 suppressed by marker). A fixture that must be a literal DER-outline
blob — a parser test vector, or the test module's own `synthetic_private_der` output if ever
written down — can only be silenced by `--disable exempt-private-key` for the whole repo. The
advisory block rightly omits the marker advice; the trade-off is stated nowhere.
*Counsel:* honour `secretscan:allow:exempt-private-key: <reason>` on the line (the marker
already demands a reason), or say in the README that the rule has no hatch by design and why.

**XK10 — note.** `Finding.kind` gains a fourth value, `"exempt"`, while the dataclass comment
enumerates three; nothing consumes `kind` (`report.py`, `floor.py`), so harmless. The comment,
README and CHANGELOG say the 2026-11-06 keys were "committed" in the fragment shape; the three
copies of the test file `main` has held since `320/790` began each read 0 hits under HEAD's
check, so the shape claim cannot be verified from `main`'s history (consistent with a human
catch before landing). V1 note, not a defect.

### Lens 4 — security and privacy

- **Design altitude.** The check adds a read of files the repo chose not to read, inside a
  guard every child floats on. What it exposes: nothing new (an excerpt is the label, the form
  and the decoded length; the JSON and human outputs were both checked). What it trusts: the
  exempt file's text, which is untrusted input to three regexes and a base64 decoder — the
  threat enumeration the delta's comment half-does ("Cost: … quadratic to reject … 4096") and
  then under-bounds (XK2). Over-collection: none. Fail-open paths: `_scan_exempt_file` swallows
  `OSError` as `_scan_file` does; decode errors return None (a miss, not a crash); `_der_element`
  bounds-checks every length; `_der_children` always advances. No crash path found.
- **Code altitude, by hand.** Regular-expression backtracking: XK2 (two vectors, measured).
  Alphabet handling before decode: XK1. Output redaction: the key is never printed (test and
  probe). The one switch, `--disable`, prints itself in the summary (`1 rule(s) disabled`), so
  a narrowed run is visible. Catalogue cross-check, from memory and offline (local-only rule):
  CWE-1333 and CWE-400 for XK2, CWE-184/185 for XK1; OWASP ASVS V5 (input validation) is the
  chapter that bears; the cryptography chapter (V6) has no control that reaches a scanner that
  recognises key shapes without parsing keys; the configuration chapter's concern — a switch
  that narrows a guard — is met by the printed `disabled:` line.
- **`/security-review`: discharged by grounds, not run.** It reads this session's pending diff,
  which is this brief and the *deleted sibling*: running it here would feed the sibling's
  deletion diff into the reviewer before act 1, the SL2 shape `REVIEW.md` warns of. A scratch
  clone carrying the code diff was not built for it because the hand read above and the probes
  cover the code altitude it would reach, and its markdown exclusions would make most of the
  delta's surface a definitionally empty pass.
- **Fixtures as a privacy surface (this repo is public).** Every key shape the delta's tests
  use is built at run time: `synthetic_private_der` (random bytes in a DER outline),
  `encrypted_pkcs8` (random), the OPENSSH magic plus random bytes. The literal strings added are
  the documented AWS example key id (allow-marked), a counting-pattern placeholder IV in a
  `DEK-Info` line, `FAKEFAKE…`, and the public certificate and public key bodies `320/790`
  already carried. None is real key material. HEAD's check over the three `main` copies of the
  test file (`c5f6202`, `3d53b67`, `0d8db9c`): 0, 0, 0 hits. The repo's three exempt files at
  HEAD: 0 hits. Confirmed clean.

**XK4 — MODERATE — The response tier is a posture decision taken at tool altitude, and the
doctrine now describes the advisory tier wrongly.** `SECRETS.md` lines 226–240 define the
tier: "high-confidence hits block exactly as they do today … while context-free entropy hits
report and exit clean". A decoded private-key outline is the highest-confidence hit the scanner
makes, and the delta places it in the advisory tier for rollout caution ("children float at
`main`"; "a later item may make it blocking once the estate reads clean" — no such item exists:
roadmap titles swept). The reasoning is sound as a rollout step; it is recorded in a code
comment and a README paragraph, which the same section says is "how a gap becomes invisible";
and it is the principal's to make (rule 3; the section's own "the call of whoever owns the
risk"). The fleet measurement in this pass is the data the decision needs, and it says the
flip condition is not met today (XK12).
*Counsel:* put it to the principal with the fleet count: advisory for one fleet cycle with a
queued flip item and a trigger, or blocking now; record the answer in the roadmap and amend
`SECRETS.md`'s account of what the advisory tier holds. XK1–XK3 should land before any flip.

**XK12 — MODERATE — The estate does not read clean, and the rollout plan has no step for
that.** HEAD's check over the 21 wired children (read-only, counts only): 6
`exempt-private-key` hits, all in one child, all `<PEM PRIVATE KEY block, 1217 bytes decoded>`
— the decoded size of an RSA-2048 PKCS#8 key, six times over (one key repeated, or six). The
excerpt cannot say whether they are real or synthetic, which is the point: the README's flip
condition, "once the estate reads clean", is not met; the hits are advisory, so nothing stops;
and their only consumer today is a CI log line (EI1: an advisory finding nobody reads is cover,
not coverage). Nothing in the delta names who triages a fleet hit or when.
*Counsel:* the orchestrator reports the count and form to the principal at commit time; the
child's owner triages (real: remove and rotate; synthetic: build at run time, or XK9's hatch);
the flip item (XK4) carries "fleet reads 0" as its trigger.

### The pointer's three questions

1. **The fragment-joining state machine: what real shapes it misses, and whether any input makes
   it slow.** Misses: the `\n`-escaped one-line form for every DER key (XK1, the commonest
   serialised form); a bare OPENSSH body (XK3); a first fragment under 16 characters, and a key
   split across two literals on one line (XK11); and, as stated, a comma-separated list,
   base64url, PGP, a run not starting at a fragment. Hits, verified with real keys: raw PEM,
   quoted-header fragments, triple-quoted, YAML block scalar, CRLF, JS template literal,
   `+`-concatenated lines, backslash-continued lines, bytes literals, bare fragments, a dict
   value with a trailing comma, 76-column raw base64, the first fragment on the assignment
   line. Slow: yes, two inputs (XK2), one of them a plain whitespace-padded line.
2. **Can the private-key outline test match a non-key?** No realistic one found. Certificate,
   SubjectPublicKeyInfo, DigestInfo, a version-2 record, four INTEGERs, random bytes: all
   rejected (the delta's tests, re-run, and a read of `private_key_outline`). The way in is a
   SEQUENCE whose first child is INTEGER 0 or 1 followed by one of the three child shapes
   filling it exactly — which is what a private key is. Random bytes in that outline (the test
   module's own helper) would match, by design, which is why the tests build them at run time
   and the hatch question (XK9) matters. Two label-only looseness points, both on the over-flag
   side: the PKCS#8 branch accepts any OID (present, untested — XK8), and a DSA key reports as
   `PKCS#1` (name only).
3. **The staged path reading added lines only.** Confirmed: no blob read (test and probe), a key
   added whole is reported at its real line (fragment shape at line 2 of the scratch file,
   exit 0, 1 advisory), `--disable` honoured, the exempt classification shared with the tree
   path. A key whose header line pre-exists is missed, as stated, and CI re-prints it. XK1
   applies equally: the GCP-shaped JSON staged into an exempt file reports nothing.

### Standing checklist V1–V7

- **V1** — claims stronger than evidence: XK1 (README table and one-line test), XK2 ("BOUNDED"),
  XK3 (gap list), XK10 ("committed" shape).
- **V2** — every recorded proof re-run: see the ledger; all reproduce. "On this repo's tree it
  finds nothing" holds (0 `exempt-private-key`, 28 `low-variety-entropy`, 3 files by glob).
- **V3** — swept to every mirror: XK7 (`--help`, README line 724, two gap lists); `SECRETS.md`
  (XK4). `.secretscanignore`'s comment, `CHANGELOG.md`, the floor template comment and
  `commands/scan.md` are consistent (a glob still silences a false positive, since the rule
  judges bytes).
- **V4** — one home: the exempt decision has one (`_classify_files`) — good; the gap list has
  two (XK7).
- **V5** — contradictions: `SECRETS.md` vs the tool on what "advisory" holds (XK4); `115/050`
  vs the delta (XK5); the README's one-line claim vs behaviour (XK1).
- **V6** — security and privacy: lens 4 above; `/security-review` discharged by grounds.
- **V7** — provenance: in the brief and repeated above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `0d8db9c` | yes (`coldsweep --commit`, five `--path`s; board paths left to act 2) | XK1–XK11; XK12 is the fleet's, not the commit's |

### Re-run ledger

All from the worktree root, foreground, exit codes read; heavy lines under `nice -n 10`;
`uptime` load 4.05 at start, 1.9–3.7 during.

| Line | Result |
|---|---|
| `python3 -m unittest discover -s tools -p test_secretscan.py` | 239 tests OK, exit 0 |
| `python3 tools/secretscan.py --selftest` | `selftest OK`, exit 0 |
| full suite `nice -n 10 python3 -m unittest discover -s tools` | `python3` (3.14): 2 358 tests OK, exit 0, 564 s. A first run under `/usr/bin/python3` (3.9) errored 20 tests at import (`contextlib.chdir`, `write_text(newline=)`, runtime `X \| None`): the interpreter, not the delta |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | exit 0; every check green except `pathscan` 1 finding, warn-only and pre-existing (a missing `tools/exception.py` path in a 2026-10-03 ADR), outside this delta; `secretscan advisory: 28` (the tree's `low-variety-entropy` hits) |
| `… --plane hook` | exit 0; every check green; `secretscan advisory: 0` (nothing staged) |
| tree `secretscan --root . . --json` | exit 0; counts blocking 0, advisory 28; rules `low-variety-entropy` only; `files_by_ignore_glob` 3; no rule disabled |
| test-file loop (`c5f6202`, `3d53b67`, `0d8db9c`), HEAD's check | 2211 / 2324 / 2699 lines; 0 / 0 / 0 hits |
| scratch repo, exempt `fixtures.py` with a synthetic RSA PKCS#8 in `py_fragments` | `--staged`: exit 0, advisory 1 at line 2, `<base64 run, 1216 bytes decoded, PKCS#8 outline>`, 1 file by glob; tree: same; `--disable exempt-private-key`: exit 0, 0 advisory, `1 rule(s) disabled`; human output shows the 🟡 block with the rule's remedy and no marker advice |
| scratch repo, the same file as a GCP-shaped JSON holding a real RSA key | `--staged` 0 advisory; tree 0 advisory (XK1); un-exempted: blocking 1, `private-key-header` |
| real-key shape matrix (7 PEM-form keys, 5 OPENSSH keys, 1 PKCS#12; 20 wrappings) | `shapes.txt`, summarised under XK1, XK3, XK6, XK11 |
| timing probe | `_PEM_PRIV_ONELINE_RX`: 0.014 / 0.056 / 0.224 / 0.894 s at 250 / 500 / 1 000 / 2 000 markers; exempt path vs engine on 1 000 markers 0.225 s vs 0.003 s; per 4 KiB line: frag-spaces 363 ms vs 0.2 ms, tail-spaces 709 ms vs 0.2 ms, plain code 0.2 vs 0.1 ms, base64 0.1 vs 0.6 ms |
| mutation runner (15 mutations) | `mutations.txt`, summarised under XK8 |
| children: `floorfleet --root <parent of the main checkout> --json`; per wired child, pre-delta (`815dce6`) tools vs this worktree's, `--json`, timed | 23 rows, 1 parent, 21 wired, 1 absent; 11 children carry a `.secretscanignore`; 1 135 files skipped by glob across the fleet; exit code and `counts.blocking` identical pre vs HEAD on 21/21; total scan time pre 135.2 s, HEAD 112.9 s (pre ran first, cold cache), largest per-child HEAD/pre ratio 1.16, so the exempt read costs nothing measurable on real trees; **`exempt-private-key` hits: 6, in one child, all `<PEM PRIVATE KEY block, 1217 bytes decoded>`** (XK12) |

### Overall

**FAIL — 2 MAJOR, 4 MODERATE, 4 minor, 2 note (XK1–XK12).** What that means: the delta's own
coverage claim does not hold for the commonest serialised PEM form, and the check adds an
unbounded-time path to a fleet-wide guard. Both are a few lines to fix, the check is worth
keeping landed as advisory while they land (it reads the shapes it was built for, the tree and
the fleet are clean, and nothing that blocked before blocks less), and the flip to blocking
should wait for them. Every finding is the principal's to decide (rule 3): nothing applied.

### Follow-up checklist

- [ ] XK1: stop stripping `+`; add the `json.dumps(pem)`, under-floor and ENCRYPTED one-line
      shapes to the tests. Re-run this pass's shape matrix on the fix.
- [ ] XK2: bound or linearise the one-line regex; one `\s*` in the trailer; a time budget test.
- [ ] XK3: OPENSSH prefix in `_bare_run_hit`, or state the gap.
- [ ] XK4: 🎯 the principal — advisory with a queued flip item and a trigger, or blocking now;
      record it; amend `SECRETS.md`'s account of the advisory tier.
- [ ] XK5: 🎯 the principal — amend or close `115/050` against `115/380`.
- [ ] XK6: traditional encrypted blocks — read them, or record the exclusion as his decision.
- [ ] XK7: `--help`, README line 724; one gap list.
- [ ] XK8: the five unpinned claims get tests.
- [ ] XK9: a hatch, or the README says there is none and why.
- [ ] XK10, XK11: record only.
- [ ] 🚩 XK12: six PEM-form hits in one child's exempt file, 1 217 bytes each — the
      orchestrator reports it to the principal with the count and form; the child's owner
      triages before any flip to blocking.
- [ ] Questions for the principal that did not need an answer to run this pass: none beyond
      XK4 and XK5.

### Reconcile (act 2, 2026-11-06 UTC)

Opened only after act 1 was committed unrevised (`7c6b781`): the held sibling, the queue pointer
`160/1040`, the intent record `115/380` whole, and `0d8db9c`'s message body. Not opened: the
sibling's list of prior records on nearby surfaces (five earlier verdicts, `GUARDS.md` and the
rest), and the `160/1030` brief, verdict and folded sibling, which belong to another reviewer.
The sibling is folded in by the orchestrator, not here. Act-1 text above is unrevised. One
reconcile probe printed path fragments from two children's scope lists into the session
transcript; none is carried here.

**Against the author's account** (`115/380`'s DONE paragraph and the commit body):

- The near miss: four real throwaway keys on a branch, amended to synthetic DER before the
  push, nothing on `main`. Consistent with the loop (0 / 0 / 0). XK10's note on the word
  "committed" stands as wording only; the record is accurate, and the README's public sentence
  names no person and no repo.
- "Probed before landing over every child with a `.secretscanignore` (13)": two independent
  runs count 11 of 21 wired children (the brief-writer's and this pass's). The 13 does not
  reproduce — XK13 below.
- "The rule's only hits are in one child that tracks dead TLS keys as recorded debt (true
  positives, reported, not blocking)": this answers XK12's triage question — the six
  1 217-byte PKCS#8 hits are known, recorded, dead keys. XK12 stands, re-aimed: the flip
  condition "once the estate reads clean" has no path to clean while recorded debt sits in an
  exempt file and the rule has no hatch (XK9); the two findings are one decision. Severity
  unchanged.
- "Taken by the finding run, advisory first": confirms XK4 — the tier was the author's choice,
  recorded in the item as "to judge" and judged by the same run; no ruling of the principal's
  on the design or the tier (the sibling found none either). Unchanged.
- "Patterns that must skip a long blank or base64 run are matched anchored, never searched (a
  search was quadratic on a 6 MB line)": the author found and fixed one quadratic, the tail
  search. XK2's two are different — the double `\s*` inside those anchored patterns, and the
  one-line regex, which is still searched. Unchanged.
- "(OpenSSH: openssh-key-v1)" is claimed for the PEM form only: consistent with XK3. Unchanged.
- The brief-writer's held results agree with this pass's on every line: suite 2 358 OK; tree
  28 / 0 / 3; loop 0 / 0 / 0; scratch staging at line 2, 1 216 bytes, control 0; fleet 21 wired,
  11 with an ignore file, 6 hits in one child; its 74 → 78 s on the largest child matches the
  ≤ 1.16 ratio here.

**Against the sibling's eleven seeded questions** (a floor, read after the findings):

1. *Tier.* XK4: the author's decision, recorded in the item, not where `SECRETS.md` says a
   narrowing goes; no flip item exists.
2. *Who reads it.* Formed at reconcile, XK14 below: on this repo's board a real key would be
   29 on a count of 28 noise; the human and CI-log block names the rule per finding, the board
   carries the number only.
3. *Off switch.* XK7 for `--help`. A child can pass `--disable` through the floor's flags:
   3 of 21 wired children carry `--disable` flags today, none to `secretscan`; none narrows
   `secretscan`'s scope. A child that turned the rule off would be visible: the summary line
   prints `disabled: <rule>`, and `floorfleet`'s rows carry a `disabled` field.
4. *Shapes.* The act-1 matrix answers each: a JSON string with `\n` escapes — missed, silent
   (XK1, MAJOR); a bare OpenSSH body — missed, silent (XK3); `Proc-Type` — stated, and not
   principled against `ENCRYPTED PRIVATE KEY` as the question suspects: both are real key
   material, one judged on outline and the other excluded (XK6); a PuTTY `.ppk` — by its format
   (an SSH wire blob under `Private-Lines:`, not DER) not read, not probed, silent; a JWK `d` —
   stated (base64url); PKCS#12 — probed, missed, silent; a DER key file — probed at reconcile,
   never read (XK15); comma-separated literals — stated; `+` concatenation one literal per
   line — caught; one-line `"…" + "…"` — caught for DER forms by path (b); a first fragment
   sharing a line with other text — caught, unless under 16 characters (XK11).
5. *Outline false positives.* None realistic found. DSA and DH parameters, an ECDSA signature
   and a PKCS#1 public key each open with a large INTEGER, not a one-byte 0 or 1; a crypto
   library's ASN.1 fixture in this shape is a key fixture. The advisory block's "decodes as a
   real private key" is stronger than the outline test; a wording point under XK8's counsel.
6. *Cost.* XK2: two super-linear inputs. On the children's real exempt files: within noise.
7. *State-machine edges.* Probed at reconcile with synthetic keys: two PEM blocks in one file —
   2 hits (lines 1, 7); a PEM block then its own body as a literal — 2 (lines 1, 8), correct,
   two occurrences; two fragment sets — 2 (lines 2, 7); two keys glued as one fragment run with
   no separator — 1, the first, by design (judged from the first byte; one hit is enough). A
   padded `=` cannot sit mid-value in one base64 string, and the 150 KiB cap is far above any
   key. No defect.
8. *Staged plane.* The stated gap confirmed (act 1, question 3). "The CI run reads the whole
   file" holds for the fleet today: no wired child narrows `secretscan`'s CI scope (0 of 21).
   CI does not block on it either, which is XK4's point.
9. *Record dates.* Formed at reconcile, XK16 below.
10. *Public record of the near miss.* Accurate against history and the intent record; the one
    looseness is "committed" (XK10); acceptable content for a public README.
11. *Exempt binary files.* Formed at reconcile, XK15 below.

**Findings formed at reconcile, marked as such:**

- **XK13 — note — The intent record's child count does not reproduce.** `115/380` says 13
  children carry a `.secretscanignore`; two independent fleet runs count 11 of 21 wired. The
  difference is probably discovery (all git repos under the parent against wired children), but
  the record states the number without its method. V1.
- **XK14 — minor — On the floor board a real key is +1 on a count of noise.** `floor.py` reads
  the `secretscan advisory:` total only; per-rule counts do not reach the board, so a child's
  board cannot tell an `exempt-private-key` hit from a git SHA. The CI log's 🟡 block can, but
  the board is what gets looked at. This is EI1's "cover, not coverage" at the board altitude,
  and one more reason XK4's decision matters.
  *Counsel:* print the rule breakdown beside the total (the summary line already breaks
  allow-markers down by rule), and let the board carry it.
- **XK15 — note — An exempt binary key file is never read, and the README does not say so.**
  A `.der` private key in an exempt path is binary to the 020/370 reader (`_looks_binary` on
  the first chunk), so the check yields nothing (probe: 0 hits). By design of the reader, but
  the gap list should name it.
- **XK16 — minor — The CHANGELOG heading carries a local date.** `### Added (2026-11-07 …)`
  for a commit authored 2026-11-07T01:17+13:00, which is 2026-11-06T12:17Z. `CONVENTIONS.md`
  keeps UTC at rest; the `320/790` entry beside it says 2026-11-06.

**Overall, restated: FAIL — 2 MAJOR, 4 MODERATE, 6 minor, 4 note (XK1–XK16).** Nothing in the
sibling or the author's account moves an act-1 severity. The act-1 counsel stands: fix XK1–XK3
before any flip to blocking; XK4, XK5, XK12 and XK9 are one decision of the principal's about
the tier, the hatch and the recorded debt; the rest are record and test fixes.

Follow-ups added at reconcile:

- [ ] XK13: `115/380` states its child-count method, or takes 11.
- [ ] XK14: per-rule advisory counts to the board.
- [ ] XK15: the gap list names binary key files.
- [ ] XK16: the CHANGELOG heading in UTC.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-06)

*Released to the reviewer only after its act-1 findings were committed (`7c6b781`); folded here
verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (drain session `850e2a78`, Claude Opus 5.5) formed no finding and wrote no
severity.*

### Sibling to the secretscan exempt-private-keys cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** The orchestrator, drain session `850e2a78`, holds it and hands it over on receipt
of the committed act 1. Written 2026-11-06 UTC by the brief-writer, session `782f8a66` (Opus
5.5), named in the brief's provenance; it forms no finding and assigns no severity. Fold this
file in below the reconcile and delete it at phase 2.

#### Intent record and author's account

- `115/380` (`docs/roadmap/115-guardrail-architecture-mike-commissioned/`) — read in full by the
  brief-writer. Found 2026-11-06 by queue run `722ac2e2` at its own landing of `320/790`: the
  worker's fix had added four real throwaway private keys (EC and RSA PKCS#8, SEC1, PKCS#1) to
  `tools/test_secretscan.py`; every check passed and only the orchestrator's read caught them
  before the push; the branch was amended to synthetic DER and the record says nothing reached
  `main`. Its "possible shape, to judge" is the landed design. It says the finding run took the
  work itself, advisory first, because the change alters what a guard reads inside its own
  exemptions and children float at `main`.
- Its `DONE 2026-11-06` paragraph is the author's landing account and carries a **live-proven
  claim** to re-run (V2): a probe over every child with a `.secretscanignore`, with a count of
  such children, blocking results unchanged, run times within noise, and the rule's only hits
  in one child, described there as true positives held as recorded debt.
- No principal ruling on the design was found in either record. The principal's pick quoted in
  the pointer approves running the pass, not the design or the advisory tier.
- No commit message body was read.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-11-06 UTC, from the worktree root at `b2851e9`, in the
foreground unless stated:

- `test_secretscan.py`: 239 tests, OK, exit 0 (about 10 s). `secretscan --selftest`: exit 0.
- Full suite under `nice -n 10`: 2358 tests, OK, exit 0 (536.5 s, load average 2.5 to 4.8).
- `floor.py --plane ci --root .`: exit 0. `--plane hook`: exit 0, with nothing staged. Both ran
  with this brief's four files untracked and the two pointer lines unstaged in the tree.
- The tree: exit 0; 0 blocking; 28 advisory, all `low-variety-entropy`; 0
  `exempt-private-key`; `files_by_ignore_glob` 3.
- The test-file loop: 0 hits in `tools/test_secretscan.py` at each of `c5f6202`, `3d53b67` and
  `0d8db9c`.
- The exempt file, scratch repo: staged, exit 0, 1 advisory finding, `exempt-private-key` at
  line 2, excerpt naming a base64 run of 1216 decoded bytes in a PKCS#8 outline,
  `files_by_ignore_glob` 1; whole tree, the same finding, exit 0; with `--disable
  exempt-private-key`, 0 advisory, exit 0. Control, the pre-delta tool from `815dce6` on the same
  staging: 0 advisory, exit 0. A first attempt with a glob carrying no stated reason exited 2
  on every plane (existing behaviour, not this delta's), so the recipe states a reason.
- Children, read-only, count only: `floorfleet` found 23 rows, 22 `wired` and 1 `absent`; 21
  wired children other than the parent, **11 of them carrying a `.secretscanignore`**. Pre-delta
  tool (`815dce6`) against HEAD: exit codes and `counts.blocking` identical in all 21.
  `exempt-private-key` hits in exactly **one** child: 6, all `PEM PRIVATE KEY` blocks, across 3
  files; that child's advisory count goes from 2 to 8. Run time: the largest child 74.0 s
  before and 78.0 s at HEAD (one run each, under load); every other child within 0.1 s. The
  intent record states a different count of children with a `.secretscanignore`; reconcile the
  two.

#### Prior records on nearby surfaces (named by filename, not opened, not exhaustive)

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/050-a-real-credential-in-an-exempt-fixture-file-is.md`
  — by its file name, an earlier instance of the same class; surfaced by the brief's reconcile
  sweep. Not opened.
- `docs/reviews/2026-07-28-1204-c1-advisory-cold.md`,
  `2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md`,
  `2026-10-17-1010-advisory-count-per-scanner-cold.md` — the advisory tier and its count line,
  which this delta adds a second rule to.
- `docs/reviews/2026-07-28-1220-secretscan-fragment-cold.md` — by its name, earlier work on
  fragments in `secretscan`.
- `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md` and its top-up — the
  `--staged` reader (`115/360`); the brief-writer read only `160/950`'s summary of it.
- `docs/method/GUARDS.md`, `commands/scan.md`, `docs/build/templates/workflows/floor.yml`,
  `tools/publishscan.py`: hits of the reconcile sweep, not read.

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **Tier.** `SECRETS.md`'s posture is over-flag, and a working private key in a public repo is
   the clearest leak there is. The check is advisory, so the exit code does not move. Whose
   decision was advisory, is it recorded where the doctrine says narrowing decisions go, and is
   there a board item for the flip to blocking that the README and comment promise ("a later
   item may")?
2. **Who reads it.** The floor board carries the `secretscan advisory:` count. On atelier's own
   tree that count is 28 low-variety findings. Does a real key in an exempt file show as 29 on
   the board, indistinguishable from noise, and is that "an advisory finding nobody reads is
   cover, not coverage" (EI1)?
3. **Off switch.** `--help` lists the rules `--disable` takes and does not name
   `exempt-private-key`. Can a child disable it through the floor's `flags`, and would
   `floorfleet` or the summary line show that it did?
4. **Shapes missed.** Traditional encrypted PEM (`Proc-Type: 4,ENCRYPTED`) is stated as not a
   hit, while `ENCRYPTED PRIVATE KEY` is checked; is the difference principled? A bare OpenSSH
   body (no PEM lines), a PuTTY `.ppk`, a JWK with a `d` member (base64url), a PKCS#12 or DER
   key file the reader treats as binary, a key in a JSON string with `\n` escapes, a key split
   over comma-separated literals or `+` concatenation, a key whose first fragment shares a line
   with other text: which are caught, which are stated gaps, and which are silent gaps?
5. **Outline false positives.** `private_key_outline` matches PKCS#1 as a `SEQUENCE` of an
   `INTEGER` 0 or 1 then five or more `INTEGER`s and optional trailing `SEQUENCE`s. What else has
   that shape (DSA or DH parameters, some signature formats, an ASN.1 test vector in a crypto
   library's fixtures)? Does the advisory text ("holds text that decodes as a real private
   key") overclaim when the test is an outline, not a parse?
6. **Cost.** `_FRAG_RX` and `_TAIL_AFTER_RX` carry `\s*` and optional groups; `_LONG_FRAG_RX`
   and `_RUN_RX` run `finditer` over every line of up to 4096 characters, and the reader windows
   longer lines. Is there an input that makes any of them super-linear, and what does the check
   cost on the largest exempt file in the children (the brief's probe times it)?
7. **State machine edges.** `covered` remembers one PEM block; `flush` drops a run whose start
   line falls in it. Two keys in one file, a PEM block followed by its own body as a quoted
   literal, a padded `=` mid-run, an `acc_len` cap flush in the middle of a 4096-bit key: does
   each report once, twice, or never?
8. **Staged plane.** Only added lines are read. A key added across two commits, or a commit
   that adds the key lines to an existing exempt file whose earlier half was committed earlier,
   is missed at the hook; the README says CI "prints anything the hook missed", but CI does not
   block on it either. Is "the CI run reads the whole file" a claim the floor's CI plane makes
   good for every child (scope, `flags`)?
9. **Record dates.** The changelog heading is dated 2026-11-07; the commit landed 2026-11-06
   UTC (2026-11-07 in the committer's zone). `CONVENTIONS.md` keeps UTC at rest.
10. **Public record of a near miss.** The README, comment and changelog say a worker put four
    working private keys in the test file. Is that statement accurate against history (the
    brief's test-file loop), and is it the right content for a public tool README?
11. **Exempt binary files.** `.secretscanignore` can name a binary file; does the exempt check
    read it, skip it as binary, or fail?

#### Facts held back from the brief

- The intent record's child-probe claim (above) is what the brief's children line re-runs; the
  brief does not state the claim or its numbers.
- `115/050` exists (above); the brief does not name it.
