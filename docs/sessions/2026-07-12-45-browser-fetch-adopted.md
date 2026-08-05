# 2026-07-12 · session 45 — browser-fetch adopted; the fetch ladder + credential boundary

The same conversation as session 41 (signing), continued: Mike's "carry on with
the browser fetch work" executed the adoption the ROADMAP had scoped, then the
wrap-up questions produced the fetch escalation ladder and a sharpened
credential boundary. Recorded separately from 41 — a distinct body of work.

## The adoption (first capability instrument)

`~/.claude/mcp-servers/browser-fetch` (a Python MCP server driving Chrome via
Playwright — no git, no README, a `.venv`, "Mike" throughout) became
`instruments/browser-fetch/`:

- **Pre-public scrub first**: every "Mike" → operator, the pre-SDK/machine
  history dropped, `127.0.0.1` marked `leakscan:allow`; floor scanners clean <!-- leakscan:allow:ipv4: loopback, in a frozen session record; the prose-mention exemption this line used to rely on stopped counting 2026-08-05 -->
  before the code ever entered the public repo.
- **Code in atelier, venv outside**: pinned `requirements.txt` (mcp,
  playwright) + `constraints.txt` (`cryptography<46`, Intel-macOS wheels), a
  reproducible `setup` that builds the venv under `~/.cache/atelier/…` (never
  committed, never in iCloud) and prints the `~/.claude.json` registration.
- **ADR 0006 addendum**: `instruments/` widens to admit **capability** tools —
  three verbs now: `tools/` enforce, instruments observe (ccrepo/cctranscript)
  or **extend reach** (browser-fetch). The prior sub-norms (zero-dep Node,
  read-only) were descriptive of the first two, not constitutive; zero-dep
  flexes for a capability tool whose value needs deps, paid honestly.
- **Proven end-to-end**: driven directly after setup (example.com → 200), then
  by a fresh parallel session against the re-registered server (httpbin UA
  `HeadlessChrome/149` — real Chrome). Old dir + config backup deleted after
  confirmation. Not CI-unit-tested (a browser in CI is disproportionate);
  scanners cover the source, live use verifies — the honest-scope stance.

## The fetch escalation ladder (Mike's shape, renumbered 1–6)

Documented in the browser-fetch README: 1 WebFetch/WebSearch · 2 curl ·
3 `browser_fetch` (a **completely standalone** disposable Chrome — own
process/session, nothing shared with the operator's browsing, can't be clicked
away) · 4 `browser_fetch_persistent` on a **dedicated profile** (real,
non-headless, still isolated) · 5 the same tool on the operator's **everyday
session** ("just another tab", deliberate exposure of the real profile) ·
6 ask the operator to paste. Start cheapest; step down only when blocked.
Mike rejected the interim 4a/4b sub-rungs — flat 1–6. Rungs 4/5 are one tool,
split by which profile the operator exposes on `:9222`. Chrome-only today;
Safari/Firefox engines + an explicit 4/5 split are ROADMAP.

## The credential boundary — a purpose-of-storage test

Mike's rule, sharpened across two turns: the agent may **ride a session the
operator already authenticated**; it may never use the browser's **saved
credentials** (or access them) without explicit permission. Then the crucial
generalisation *before* doctrine gets drafted: the line is **purpose of
storage**, not "agent never touches credentials" —

- **Provisioned stores** (keychain items the estate registry records, minted
  per-consumer tokens — the ros/tiki/shed pattern) exist *for* repo/tool/agent
  use: the intended path.
- **Personal convenience stores** (browser logins; the principal's password
  manager — Apple Passwords here, browsers hold almost nothing by his own
  practice) were saved to ease *his* browsing, are broader than any task needs,
  and are off-limits by default.
- **The principal grants across the line** — temporary or permanent, per
  credential, his explicit act, landing in the provisioned machinery.

Stated operationally in the browser-fetch README (browser-scoped, so it never
implicated shed/tiki); the generalised test is encoded in the ROADMAP
doctrine-elevation item so the future `method/` text (SECRETS/ACCESS family)
cannot be written to find the estate's intended credential use contrary to the
principle. Drafting deferred — Mike chose to close the session; next session's
candidate.

## Concurrency note

Two parallel sessions worked the same checkout during this one (sessions 42–44:
faves/ros floor adoption, COMMUNICATION.md + its cold review). Held off
committing while their tree was dirty; a post-landing survival audit confirmed
all of this session's commits and content intact (one grep false-alarm on the
signing pre-flight — case-sensitive search, content was fine). `local ==
origin`, history linear.
