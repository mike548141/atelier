# Cold pass — secretscan still reads a file its .secretscanignore exempts, for real private keys

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (guard code is doctrine by
function).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-11-06 UTC by session `782f8a66`, a
headless Opus 5.5 brief-writer; the pass waits for a cold Fable 5.1 reviewer under the
orchestrator named below.
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
this brief's sibling
`docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.deferred.md` (held by the
orchestrator), every delta commit's message body, and these records beyond their first line
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
