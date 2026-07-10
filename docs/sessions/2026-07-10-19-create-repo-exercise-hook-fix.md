# 2026-07-10 · create-repo exercised end-to-end; scan-hook fail-open defect fixed (Opus)

The first of session 18's two owed items: **exercise `create-repo` on a real
scaffold**. Session 18 dry-ran only the mechanical core in scratch (seed +
renames + placeholder fills + drift-check). This session did the parts the
dry-run skipped — a real `git init`, the hook install, and a first commit — on a
real local git repo. That's where the defect was hiding: the honest-instrument
rule (§14) says a tool's "it works" is a claim until it's driven, and this one
wasn't true.

## The defect the dry-run couldn't see

`create-repo` step 6 tells the scaffolder to wire the safety scans as a
pre-commit hook and "point at atelier's `tools/leakscan.py` + `secretscan.py`".
But `tools/pre-commit.sample` — the thing step 6 says to copy — hardcoded
`$repo_root/tools/` and guarded each scanner with `if [ -f … ]`. A child repo
**has no scanners of its own**; they live only in atelier (the templates ship no
copy — one source, by design). So in a scaffolded repo both guards were false,
both scans were skipped **silently**, and the hook exited 0. Proven the blunt
way: a first commit carrying a real `AKIA…`-shaped key went straight into
history with a green hook.

This is the repo's own headline failure mode one layer down: a repo that
inherits the *hook* but not the *scanning* has inherited the costume, not the
doctrine. And it is a textbook §14 silent-success defect — the gate reported
"ok" while doing nothing.

## The fix — resolve up, fail closed

Two coupled changes:

- **`tools/pre-commit.sample`** (the atelier-tracked artifact): resolve the
  scanners' home as `ATELIER_TOOLS` env → `git config hooks.atelierTools` →
  `$repo_root/tools` fallback (so atelier's own hook is unchanged), then **fail
  closed** — a `run_scan` helper that *blocks the commit with an explanation*
  when a scanner it is asked to run is missing. A gate whose whole job is to
  stop bad commits must never wave one through because its tool wasn't found.
  Opting a repo out of a scanner is now an explicit deleted line, not a silent
  skip.
- **`create-repo` step 6** (machine-local skill): stop implying "copy the sample
  and it just works". Install the hook *and* **bake the path** —
  `git config hooks.atelierTools "$PP/atelier/tools"` — plus a prove-it-once
  instruction (stage a fake secret, confirm the block).

## Verification (driven, not read)

Re-exercised on a fresh local scaffold with the fixed hook:

- **Fail-closed:** hook installed, no config, no env → commit **blocked** (exit
  1, 0 commits), with the pointer message.
- **Blocks a real secret:** `hooks.atelierTools` set, `AKIA…` key staged →
  **blocked** (0 commits in history).
- **Passes clean:** secret removed → commit succeeds (exit 0).
- **atelier unaffected:** atelier's own hook path (no config → `$repo_root/tools`
  fallback) still blocks a staged `AKIA…` secret.
- Suite **137 OK**; the three scanner `--selftest`s pass. (I touched only a
  shell sample + the machine-local skill, so the Python suite was expected
  unchanged — confirmed, not assumed.)

*Note on a false start:* my first "planted secret" was AWS's published
documentation example secret (`wJalr…EXAMPLEKEY`), which secretscan **correctly
ignores** as a known dummy — so the first re-run looked like a miss but was the
scanner behaving. Switched to the access-key-*ID* shape (`AKIA…`, a structural
match) to prove teeth honestly.

## Surfaced, not fixed

The CI templates (`workflows/ci-*.yml`) run **no scanner** — so a scaffolded
repo's *only* scan gate is the machine-local hook, and the "pair it with CI"
line in both the sample and step 6 is currently unbacked. Wiring scanners into
CI hits the same "child has no scanners" wall, harder (no local atelier path):
it needs the scanner-distribution decision — vendor into each repo / fetch
atelier in CI / publish the scanners — which is the already-*deferred*
supply-chain item. Recorded in ROADMAP + CHANGELOG; not half-built here.

## Close

The `create-repo` rewire's real-scaffold exercise is done and it paid for
itself — the delivery mechanism shipped a security gate that protected nothing,
now fixed and proven. **Still owed on the rewire:** the single outward `gh repo
create --push` step (skipped deliberately — no throwaway GitHub repo spun up
just to test), a Fable sweep of the whole rewire, and the CI-scan-wiring call
above. ros pin unchanged (`f72031c` — no `method/` change).
