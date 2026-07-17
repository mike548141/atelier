# 2026-07-17 · 0958 UTC · the three queued cold reviews taken (Fable)

## Trigger

Mike opened a fresh session: work in a worktree (a parallel session is live)
and "do any review work or fable only work". Three `⏳` items sat in
*Doctrine — review-owed*; this session is a valid rule-4 taker for all three —
the author sessions (all Opus: 2026-07-17-0946, 2026-07-17-0810,
2026-07-15-1327) neither started nor instructed it.

## What happened

1. **Worktree first** — `worktree-fable-review`; the primary checkout left to
   the parallel session.
2. **Claimed before working** (CONCURRENCY § Claiming work): all three `⏳`
   lines stamped `(claimed 2026-07-17-1000, wt: worktree-fable-review)` in one
   direct-to-`main` commit (`325011b`), pushed, then the worktree rebased onto
   it.
3. **Three briefs written by the taker** (rule 4: the author queues the
   pointer, the taker writes the brief), each with the author's ROADMAP seed
   questions in the deferred section below the divider, spawn provenance
   stated, rule-3 apply-nothing standing orders, and re-run-the-proofs scope.
   One disclosure carried into each brief: the `⏳` pointers themselves carried
   seed questions, where rule 4 specifies refs-only — named, not denied.
4. **Three cold reviewers spawned in parallel** (background agents, Fable;
   agents-for-breadth per CONCURRENCY). Each committed its own attack surface
   durably before opening the deferred section or the intent record, re-ran
   every recorded proof in scope, and appended its verdict to the brief file.

## Verdicts — all three PASS-WITH-FINDINGS, nothing applied

| Review | Result | Sharpest finding |
|---|---|---|
| REPO-STANDARD CLI-docs convention | 1 MAJOR · 4 MEDIUM · 2 LOW | F1: the scope predicate is unbounded — it binds atelier's own seven `tools/` scanners (no man pages, no exception stated); the parent ships a letter it doesn't meet |
| ADR 0006 addendum — ccarchive, the *preserve* verb | 0 MAJOR · 1 MEDIUM · 3 LOW | F1: "append-only" is delete-proof, not overwrite-proof — a corrupt newer-mtime source silently overwrites the only durable copy and the manifest blesses the damage |
| CONVENTIONS.md + UTC-at-rest ADR | 1 MAJOR · 0 MEDIUM · 4 LOW | F1: the ADR changed what `HHMM` means (UTC) but the six identifier-minting docs (incl. the child templates) still describe the old regime — stale in the delivering commit |

Verdicts, attack surfaces, provenance, and per-finding reviewer's counsel:
`reviews/2026-07-17-1000-cli-docs-standard-cold.md`,
`reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md`,
`reviews/2026-07-17-1000-conventions-utc-at-rest-cold.md`.

Every recorded proof re-ran green in all three reviews — 247 tool tests, 67
instrument tests, selftests, the full scan set (secretscan · leakscan
structural **and** local · licenscan · linkscan · sizescan), `mandoc` lint, a
fresh installer drive into throwaway XDG dirs, and the UTC dogfood claim
verified arithmetically *and* behaviourally. Positive results worth keeping:
the ccarchive public-repo boundary held as shipped (guard 1 verified at HEAD),
"preserve" was judged a genuine fourth verb, the §8 reconciliation holds, and
CONVENTIONS leaks nothing person-local (seeded Q3 cleared decisively).

## Owed

**All findings are Mike's to decide (rule 3 — self-authored doctrine):** three
🎯 ROADMAP items point at the verdicts (F1–F7, F1–F4, F1–F5). Nothing was
applied; reviewer's counsel is recorded per finding. Two passes carried a
MAJOR, so those cycles stay open until ruled and their applications pass;
the ccarchive pass (0 MAJOR) closes on Mike's ruling per the close rule.

## Claim release

Records landed on `main`; the three claims are released with this landing (the
`⏳` lines rewritten as 🎯 ruling-owed items). Worktree put away —
zero unique commits after the landing.

## Addendum — same session: Mike ruled all three batches; applied

Mike ruled in sequence, each after a plain-language what/why/impact (the
informed-principal rule): **CLI-docs F1–F7 "agreed"** · **ccarchive F1–F4
"agreed"** · **CONVENTIONS F1–F5 + F6 "make all the changes as you
counselled"** — F6 being his own finding, raised mid-review (the "ISO 8601"
row declares a standard the estate deliberately profiles; strict ISO wants
`T`, a zone-less stamp means local). All applied same session by the taking
session (authored none of the three doctrines nor any verdict); per-finding
detail stamped in each verdict file's § Decision.

Highlights of the application:

- **ccarchive** (F1–F4, all pinned; tests 27→35, instrument total 75): shrink
  guard (`--force` overrides), git-work-tree dest guard (`--allow-repo-dest`),
  layout-drift alarm (zero transcripts + non-empty archive ⇒ exit 1), strict
  `--verify` (unmanifested fails; `fromArchive` surfaced). Man page + README
  carry the exposures honestly. **Cycle CLOSED** (0 MAJOR, ruled, verified).
- **CLI-docs** (F1–F7): scope predicate drawn (installed-onto-a-machine ships
  both registers; in-place scripts owe `--help` only — why `tools/` carries no
  pages is now stated); superset drift test added; the `--help` letter matches
  its own exemplar; README tense fixed; installer gains a stale-owned-link
  cleanup pass (proven in throwaway XDG dirs; live residue `fixtures` +
  `browser-fetch` removed from `~/.local/bin`); MANPATH claim scoped; guarded
  mandoc step in CI. **Cycle open** — applied-batch ⏳ queued.
- **CONVENTIONS/UTC** (F1–F6): the six minting sites now say UTC (`date -u`,
  ADR pointer) — templates via the canonical block, drift test green, children
  inherit at next pin bump; label strength aligned; prose-date-is-UTC in the
  ADR addendum + RECORD; ingestion clause honestly marked instance-less;
  boundary sort inversion named; the Date & time row rewritten as the declared
  three-shape house profile. ADR changed by dated addendum only. **Cycle
  open** — applied-batch ⏳ queued.

Floor after applying: 247 tool tests · 75 instrument tests · mandoc ·
sizescan · linkscan · scan triad — all green.
