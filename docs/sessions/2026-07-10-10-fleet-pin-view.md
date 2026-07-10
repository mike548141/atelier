**2026-07-10 (Opus) — the fleet pin view: `tools/pins.py`.** Built the last open
method-review [backlog] finding (P2), the mechanism-tier companion to
PROPAGATION's per-child drift check. **The gap it closes:** the drift check is
pull-based — a child only learns it's behind when a session opens *in it*. There
was no way to stand in atelier and ask "across the whole fleet, who is stale?".
`pins.py` is that roll-up: it resolves the atelier repo it lives in, reads every
discovered child's `CLAUDE.md` pin (`atelier@<SHA>`), and classifies each against
HEAD — `current` / `behind N` / `ahead` / `diverged` / `unknown` / `no-pin` —
with `--log` to print the exact commits a stale child would inspect.
**Discovery** walks one level under atelier's parent dir for git repos carrying a
pin (atelier itself excluded); an unreadable root degrades to a warning, never a
crash. `--child`/`--root` override it; `--json` for a dashboard, `--check` for a
CI gate.

**Deliberately read-only** — the design decision that matters. Bumping a pin
stays a per-repo human-in-the-loop act (PROPAGATION §5: read the delta, judge it
bears on the repo, then move the pin). So the tool widens *observability*
(per-child → fleet) and touches *enforcement* not at all; PROPAGATION's honest
caveat is updated to say exactly that, which is the "acknowledge the gap in
PROPAGATION" half of the ROADMAP item.

**Proven:** pure-logic classification table + pin parse unit-tested; the git
ancestry maths (incl. the ahead/diverged/unknown cases the live two-child fleet
can't show) driven end-to-end over throwaway repos — 12 stdlib tests, full tools
suite 86→98 green. Live on the real fleet it reports **faves 9 behind, ros
current** (exit 1), which is a real finding: faves still owes the P1 trust-surface
floor wording — the tool surfaces it instead of leaving it a ROADMAP memo. One
false positive fixed along the way: leakscan reads the tool's own
`atelier@<sha>..HEAD` pin syntax as an email (the `@`), allow-marked with a
reason on both sites.

**Housekeeping:** ros's pin (`7f5abd0`) was current *before* this commit; the
commit advances atelier HEAD, so ros/faves next-session drift checks will show
the delta and bump deliberately — not touched from here (that's the discipline
the tool exists to respect). Follow-on Opus work still open: MODEL-ECONOMICS
general shape, A6/A7 into method/, and the build/ layer (create-repo extraction +
rewire-to-inherit).

**Model note:** Opus build, plan-included pool — stated at session start;
squarely a mechanism build, no billing flag needed.
