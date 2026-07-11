# 2026-07-11 · session 38 — ccrepo actuals, plugin go-live, docker-heap standardised (Opus)

Mike cleared three open items in one go: build ccrepo actuals-vs-estimate, merge
the plugin bundle (PR #3), standardise docker-heap. Plus a mid-turn steer: "we
should be thinking about how we sign all the code in the various repos."

## 1. ccrepo — Actual vs Est (the design-before-code strand closed)

Built the billing model whose config was designed last session, once Mike
confirmed the shape (USD Max-20x, all Claude families covered). A present
`~/.claude/ccrepo-billing.json` (machine-local, never in a repo) adds an **Actual**
column beside **Est (API)**: `covers[]` matches model families by prefix after
`claude-` is stripped, `perTokenModels` carves one back out; covered tokens cost
$0 marginal, the sunk plan fee is apportioned per repo by covered-token share
(fallback: total-token share if nothing covered ran in range), uncovered models
keep the API-rate figure. **Actual = plan share + uncovered spend**, so TOTAL
Actual = fee + all uncovered. Absent config ⇒ estimate-only with a **byte-identical
JSON contract** (covered/uncovered internals stripped, no `actual` key); malformed
⇒ ignored-with-warning, never fatal. Both columns convert together under `--fx`;
`--no-billing` forces estimate-only. Multi-month outlay + overage are stated
footnotes, out of scope v1. Proven live estate-wide (**Est US$2,305 vs Actual
US$200** — the whole plan fee) and `--by-model` children sum to their repo. 8 new
pure tests (`loadBilling`/`coversPredicate`/`actualFor`/covered-split fold); Node
26→34, Python 205, scanners clean. Grounded in EVIDENCE §14.

## 2. Plugin bundle (PR #3) merged — first deliberate widening spent

Mike authorised go-live. PR #3 was CONFLICTING (main had moved on with the
instruments work): resolved a **CHANGELOG append-conflict** in a worktree (kept
both 2026-07-11 blocks, plugin on top), re-ran the floor green on the merged head
(`6245986`: 34 Node + 205 Python + 4 scanners), confirmed CI green on the head SHA,
then **merged to `main` (`a0ef731`)** with branch delete. `main` now carries
`.claude-plugin/plugin.json` + `marketplace.json`, so
`/plugin marketplace add mike548141/atelier` → `/plugin install atelier@atelier`
resolves — **the doctrine now travels as behaviour**. The "next widening"
live-floor item is marked spent; the floor advances to the *next* deliberate
widening (announcement / v2 plugin / package), still Mike's call.

## 3. docker-heap standardised — and a scan finding handled honestly

Standardise-existing pass (`atelier@5db645e`). The interesting part was that the
scan hooks *surfaced findings* the private repo's own records already track.
(What they are, where, and their history deliberately stay in that private
repo — RECORD's "the record is public" rule.) The principal chose "externalise
now, you rotate," but tracing the linkage revealed the scope was bigger than it
first looked, plus a genuine **reconciliation smell** where a "fix" could sever
a running service's auth if applied blind. **Then the decisive find:** the repo
*already has* a considered ROADMAP item tracking exactly this, **with a decided
fix** — my first instinct would have fought the repo's own direction. So I
**deviated from "externalise now"** and left the stack configs entirely
untouched: the right fix is the owner's, needs him at the host for the
redeploy, and is already planned. Surfaced that reconciliation smell into the
repo's own (private) roadmap item.

Scaffolding delivered (no stack config touched): doctrine block + pin (`CLAUDE.md`),
house `README`, `docs/ARCHITECTURE.md` (estate map), moved `ROADMAP.md` → `docs/`,
`SESSIONS.md` + `CONTRIBUTING.md`, `.github/workflows/floor.yml`, fail-closed hook
(proven live to block a planted AKIA key). Two real defects fixed along the way:
`.gitignore` was **self-ignoring and untracked** (a fresh clone got *no* ignore
rules — `.claude/settings.local.json`/`.env`/OS-litter all unignored) — now tracked;
and `floor.yml` + the hook **scoped to disable `ipv4,ipv6,mac-address`** because a
container/network estate has ~60 legitimate network shapes that would drown the real
signal (the ros/tiki precedent). floor CI red by design on the known,
owner-tracked item; everything else clean. docker-heap is `current` in `tools/pins.py`.

## 4. Code-signing (Mike's mid-turn steer) — captured, recommended

Expanded the deferred A5 roadmap item into a **code-signing standard** split by
cost: (a) **commit/tag signing via SSH keys** — native to git (`gpg.format=ssh`),
zero-install, GitHub "Verified", verifiable in `floor.yml`; the house-ethos answer,
should become doctrine + a create-repo `commit.gpgsign` default. Blocked on Mike
registering a signing key (identity infra + a GitHub trust surface — his call).
(b) **release-artifact signing + SBOM** stays deferred (needs cosign/syft, breaks
zero-dep). Recommendation recorded: adopt SSH commit signing fleet-wide; I wire the
create-repo + doctrine side once he's named a key.

## Floor at close
atelier: 34 Node + 205 Python + 4 scanners clean; main at the session's doc commit.
docker-heap: floor red by design on the known, owner-tracked item; everything else clean.
