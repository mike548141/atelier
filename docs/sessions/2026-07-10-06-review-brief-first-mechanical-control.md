**2026-07-10 — review brief, then the first mechanical control (Opus, "keep
going until economics say stop").** Session-start drift check fired as designed:
`957fa08` surfaced past the `dde4170` pin — inspected, found session-log-only (no
`method/` change), bumped ros's pin `dde4170→957fa08` deliberately. Then two
deliverables. **(1) The owed review is briefed:** `docs/reviews/2026-07-10-
method-layer.md` scopes the Fable review of the whole `method/` layer (PROPAGATION,
EVIDENCE, REVIEW, RECORD, PRINCIPLES) against the three lenses, with a load-bearing
assumption to attack per doc — sharpest being REVIEW.md's "a *more capable* model
reviews" vs the actual Opus-builds/Fable-reviews split (Fable is the cheaper review
tier, not uniformly more capable; the real value may be independence + fresh
context). ROADMAP grew a "review gate" section so the brief blocks further
extraction. Applies REVIEW.md's own lifecycle to the layer that codified it.
**Running the review is Fable's job, not this Opus session's** — so, staying on the
independent side of that gate, built **(2) the mechanical leak-scan** — atelier's
first executable tool (`tools/leakscan.py` + README, `pre-commit.sample`, term-list
template, unittest). Two layers, split so the scanner leaks nothing: shareable
STRUCTURAL shape-patterns that always run, + a machine-local LITERAL term list
(`~/.claude/leakscan-terms.txt`, never in a repo); absent ⇒ structural-only with a
loud warning (graceful degradation + legibility). Fail-safe exit codes, `--staged`
hot path, `--json`, `.leakscanignore` + `leakscan:allow` escape hatches; zero-dep
stdlib. **It bit on first run** — caught real leaks in its own draft fixtures (a
real address, real coordinates, a family name), now fictionalised: the tool earning
its keep against its own author is the honest proof. ROADMAP safety item ticked;
README/CHANGELOG in lockstep; pyc litter caught + gitignored (amend). **Economics
call: a clean stopping point.** The remaining queue is gated — most extraction
waits on the method/ review (Fable), secret-scan needs a tool install (floor/
confirm), and the ros PRINCIPLES trim depends on the review trusting the spine.
**Next session:** (1) run the briefed Fable review; (2) seed the real
`~/.claude/leakscan-terms.txt` so the scan runs full-cover (turns the control from
partial to real); (3) wire the hook + CI per shareable repo; then the gated
extraction once the review clears.

*Continued (same session):* Mike chose "seed, then wire hooks". **Term list
SEEDED** at `~/.claude/leakscan-terms.txt` (estate specifics from `~/.claude/
CLAUDE.md`; full names, not bare "Mike" which doctrine uses deliberately). Full-
cover validation: atelier **clean**; a scan of ros `tiki/` returned 738 raw hits
but exposed a design truth — structural IP/MAC rules are pure noise on a
networking codebase (722 of them). Added **`--disable <rules>`** (skip named
structural rules, local terms always run) + **positional-path filtering in
`--staged`** (scope to a subtree). With network shapes off, tiki/ narrowed to 16,
all verified fictional/intended — the lone real residue being the OSS author name
in `tiki/pyproject.toml` (allow-marked as intentional attribution; Mike's call
whether to use a handle). This **live-validated the earlier tiki scrub**. Hooks
**installed + proven**: atelier whole-repo; ros `tiki/`-scoped (a real term in
`tiki/` blocks; the same term in the private `docs/` passes). Hooks are local
(`.git/hooks`, uncommitted); tool + docs committed. **Still owed:** CI wiring;
term-list portability to Mike's other devices. **Flagged for Mike:** the
`pyproject.toml` author-identity decision.
