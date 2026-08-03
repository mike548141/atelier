"""Tests for tools/floor.py — the scanner registry, and the promises it makes.

floor.py exists because policy was vendored: 12 of 13 children ran a
scaffold-time scanner list and had never executed five of atelier's checks
(2026-07-25, ADR 0008). Centralising the list fixes that — and creates two new
ways to fail quietly, which is what these tests hold shut:

  1. A check could be absent because nobody noticed, rather than because someone
     decided. So the config may only express an opt-out in a form that STATES
     ITSELF: `advisory` (runs, reports, does not block) or `disabled` (with a
     reason). Anything ambiguous is rejected outright, never coerced.
  2. A check could be softened where softening is not legitimate. The boundary
     scanners (secretscan, leakscan) and integrity scanners (linkscan,
     reviewscan) have NO advisory form: a burned secret, a leaked personal fact
     and a botched harvest are not re-baselining problems. Only the prose-hygiene
     checks may re-baseline, because adopting them genuinely does demand a
     one-off cleanup pass.

The invocation contract (real scanners, real commits) is pinned separately by
test_precommit.py. These tests are the decision logic: what runs, in what state,
and what the config is allowed to mean.

Zero third-party deps, same as the rest of the suite.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import floor  # noqa: E402


def _cfg(payload: object) -> floor.Config:
    with tempfile.TemporaryDirectory() as td:
        p = Path(td)
        (p / floor.CONFIG_NAME).write_text(json.dumps(payload), encoding="utf-8")
        return floor.Config.load(p)


def _states(plane: str, cfg: floor.Config) -> dict[str, str]:
    return {s.name: state for s, state in floor.plan(plane, cfg)}


class RegistryTest(unittest.TestCase):
    """What the registry promises about the checks themselves."""

    def test_every_scanner_runs_on_both_planes(self):
        """A check that ran in CI but not the hook (or vice versa) would be a
        second, silent policy split — the bug this file exists to prevent."""
        for s in floor.SCANNERS:
            self.assertIsNotNone(s.hook, f"{s.name} has no hook form")
            self.assertIsNotNone(s.ci, f"{s.name} has no CI form")

    def test_every_registered_scanner_exists(self):
        """The registry may not name a scanner that isn't there — that would be
        a fail-closed block on every repo in the estate at once."""
        for s in floor.SCANNERS:
            self.assertTrue((TOOLS_DIR / f"{s.name}.py").is_file(),
                            f"{s.name}.py is registered but missing")

    def test_boundary_and_integrity_checks_cannot_be_softened(self):
        for name in ("secretscan", "leakscan", "linkscan", "reviewscan"):
            self.assertIsNone(floor.BY_NAME[name].advisory,
                              f"{name} must have no advisory form")

    def test_hygiene_checks_can_re_baseline(self):
        for name in ("sizescan", "datescan", "wrapscan", "spellscan"):
            self.assertIsNotNone(floor.BY_NAME[name].advisory,
                                 f"{name} needs an advisory form for adoption")

    def test_the_two_warn_only_checks_are_scoped_as_ruled(self):
        """`harvestscan` and `pointerscan` are in the registry on one condition:
        they never block. Both express that in the tool (findings exit 0), so
        the registry's job is to carry the SCOPE that made wiring defensible.

        For harvestscan that scope is the whole argument: unscoped it fired on
        one roadmap commit in four and was shelved on its author's own counsel;
        `--only-bulk-deletes` is what the principal overturned that verdict on
        (HV1, 2026-07-29). Losing the flag here would silently restore the 26.9%
        firing rate the shelving was about."""
        harvest = floor.BY_NAME["harvestscan"]
        for plane in (harvest.hook, harvest.ci, harvest.advisory):
            self.assertIn("--only-bulk-deletes", plane)
        # The hook reads the INDEX — what the commit is about to be. CI's
        # working tree IS HEAD, so it asks the same question of HEAD^.
        self.assertIn("--staged", harvest.hook)
        self.assertIn("HEAD^", harvest.ci)
        self.assertNotIn("--staged", harvest.ci)

    def test_the_pointer_guards_read_the_records_tree(self):
        pointer = floor.BY_NAME["pointerscan"]
        self.assertEqual(pointer.default_scope, "docs")
        self.assertIsNotNone(pointer.advisory)

    def test_ci_never_demands_the_machine_local_term_list(self):
        """--require-terms would demand a list CI cannot (and must not) hold:
        the person/estate terms are machine-local by design (SECRETS.md). CI's
        structural-only cover is the honest degradation — but only as long as
        nobody 'strengthens' it here, which would red every child at once.

        Narrowed from a both-planes ban (ADR 0008 cold pass, EP3). The ban is
        right for CI and was wrong for the hook: it read the two planes as one
        and so forbade the flag on the plane the design says carries the full
        cover. A developer machine can hold the list; a runner cannot."""
        self.assertNotIn("--require-terms", floor.BY_NAME["leakscan"].ci)

    def test_the_hook_plane_demands_the_term_list_it_claims_to_have(self):
        """The complement, and the reason the ban above had to be narrowed
        rather than deleted. "The full cover lives on the hook" was asserted in
        the registry, the workflow header and ADR 0008, and enforced nowhere —
        a clone with no term list got CI-grade cover from its pre-commit gate
        while every artefact said otherwise, and the floor still printed
        `✅ leakscan enforced`."""
        self.assertIn("--require-terms", floor.BY_NAME["leakscan"].hook)

    def test_a_plane_without_full_cover_does_not_render_as_a_plain_pass(self):
        """The measurement half of the same ruling: CI stays structural-only,
        so it must SAY so rather than render identically to a full-cover run."""
        self.assertEqual(floor.BY_NAME["leakscan"].full_cover_flag,
                         "--require-terms")

    def test_advisory_form_actually_softens(self):
        """An 'advisory' state that still blocked would be the worst outcome:
        a repo believes it has room to re-baseline and its commits keep failing."""
        root = Path("/repo")
        cfg = floor.Config()
        for name in ("datescan", "wrapscan", "spellscan"):
            soft = floor._render(floor.BY_NAME[name].advisory, root, cfg, name)
            self.assertIn("--warn", soft, f"{name} advisory must warn")
        # sizescan softens by dropping --check, not by adding a flag.
        soft = floor._render(floor.BY_NAME["sizescan"].advisory, root, cfg, "sizescan")
        self.assertNotIn("--check", soft)
        hard = floor._render(floor.BY_NAME["sizescan"].ci, root, cfg, "sizescan")
        self.assertIn("--check", hard)


class ConfigTest(unittest.TestCase):
    """What a child repo is allowed to declare — and what it may not."""

    def test_absent_config_enforces_everything(self):
        """A repo that has declared nothing has opted out of nothing. The old
        mechanism defaulted the other way: a scanner nobody had added simply
        never ran, and looked identical to one deliberately removed."""
        with tempfile.TemporaryDirectory() as td:
            cfg = floor.Config.load(Path(td))
        states = _states("ci", cfg)
        for s in floor.SCANNERS:
            if s.opt_in:
                continue
            self.assertEqual(states[s.name], "enforced", f"{s.name} must default on")

    def test_advisory_and_disabled_are_honoured(self):
        cfg = _cfg({"advisory": ["wrapscan"], "disabled": {"spellscan": "no prose"}})
        states = _states("ci", cfg)
        self.assertEqual(states["wrapscan"], "advisory")
        self.assertEqual(states["spellscan"], "disabled")
        self.assertEqual(states["secretscan"], "enforced",
                         "one opt-out must not weaken the others")

    def test_rejects_unknown_scanner(self):
        with self.assertRaises(floor.ConfigError):
            _cfg({"disabled": {"nosuchscan": "typo"}})

    def test_rejects_reasonless_disable(self):
        """The reason IS the mechanism — an opt-out without one is invisible
        again, which is the whole defect."""
        with self.assertRaises(floor.ConfigError):
            _cfg({"disabled": {"spellscan": "   "}})

    def test_rejects_disabled_as_a_bare_list(self):
        """A list would be the convenient shape, and it cannot carry a reason."""
        with self.assertRaises(floor.ConfigError):
            _cfg({"disabled": ["spellscan"]})

    def test_rejects_softening_a_boundary_check(self):
        with self.assertRaises(floor.ConfigError):
            _cfg({"advisory": ["secretscan"]})

    def test_rejects_contradictory_declaration(self):
        with self.assertRaises(floor.ConfigError):
            _cfg({"advisory": ["wrapscan"], "disabled": {"wrapscan": "both"}})

    def test_rejects_malformed_config(self):
        for payload in ([1, 2, 3], "nope"):
            with self.assertRaises(floor.ConfigError):
                _cfg(payload)

    def test_unreadable_config_raises_rather_than_defaulting(self):
        """Fail closed: a config we cannot parse must not silently become
        'enforce everything' OR 'enforce nothing' — either is a guess."""
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)
            (p / floor.CONFIG_NAME).write_text("{ not json", encoding="utf-8")
            with self.assertRaises(floor.ConfigError):
                floor.Config.load(p)

    def test_licenscan_is_opt_in(self):
        """A publish gate that hard-fails on a private pre-licence repo would
        block every child that hasn't settled a licence."""
        self.assertEqual(_states("ci", floor.Config())["licenscan"], "skipped")
        self.assertEqual(
            _states("ci", _cfg({"licence": "Apache-2.0"}))["licenscan"], "enforced")


class ScopeAndFlagsTest(unittest.TestCase):
    """Where a check looks, and how it is tuned — the two things a repo may
    legitimately vary, and the line between them and *softening* a check."""

    def test_override_expands_to_every_subtree(self):
        cfg = _cfg({"scope": {"wrapscan": ["docs/method", "docs/build"]}})
        rendered = floor._render(floor.BY_NAME["wrapscan"].ci, Path("/repo"),
                                 cfg, "wrapscan")
        self.assertTrue(rendered[-1].endswith("docs/build"))
        self.assertTrue(rendered[-2].endswith("docs/method"))
        self.assertIn("--root", rendered)

    def test_override_does_not_leak_to_other_scanners(self):
        cfg = _cfg({"scope": {"wrapscan": ["docs/method", "docs/build"]}})
        rendered = floor._render(floor.BY_NAME["datescan"].ci, Path("/repo"),
                                 cfg, "datescan")
        self.assertEqual(len(rendered), len(floor.BY_NAME["datescan"].ci))

    def test_rejects_empty_override(self):
        """Narrowing a check to nothing is a silent hole, not a scope."""
        with self.assertRaises(floor.ConfigError):
            _cfg({"scope": {"wrapscan": []}})

    def test_networking_repo_case(self):
        """The worked case that forced this feature: a networking repo scans
        only its shareable subtree, with leakscan's IP/MAC rules off — those
        shapes are legitimate CONTENT there, not leaked estate data. It must be
        expressible in config, or the repo keeps a bespoke hook and falls out of
        propagation entirely, which is how this whole defect started."""
        cfg = _cfg({
            "scope": {"leakscan": ["tiki/"]},
            "flags": {"leakscan": ["--disable", "ipv4,ipv6,mac-address"]},
        })
        argv = floor._render(floor.BY_NAME["leakscan"].hook, Path("/repo"),
                             cfg, "leakscan")
        self.assertIn("--staged", argv)
        self.assertTrue(any(a.endswith("tiki") for a in argv), argv)
        self.assertEqual(argv[-2:], ["--disable", "ipv4,ipv6,mac-address"])

    def test_flags_cannot_soften_a_check(self):
        """The sharpest guard here. `--warn` through `flags` would be an
        advisory downgrade that bypasses every rule on `advisory` — including
        on a scanner that has no advisory form at all."""
        with self.assertRaises(floor.ConfigError):
            _cfg({"flags": {"secretscan": ["--warn"]}})

    def test_flags_cannot_change_a_checks_mode(self):
        for bad in (["--json"], ["--selftest"], ["--check"]):
            with self.assertRaises(floor.ConfigError):
                _cfg({"flags": {"sizescan": bad}})

    def test_staged_scope_is_repo_relative_never_absolute(self):
        """A fail-OPEN shape, pinned because it exits 0 and reads as a clean pass.

        secretscan/leakscan filter the staged diff by prefix against git's path
        list, which is always repo-relative. An absolute path matches NOTHING, so
        the boundary scanners silently approve every commit. The first draft of
        _render emitted absolute paths on both planes and did exactly that — only
        the planted-secret commit tests caught it.
        """
        cfg = _cfg({"scope": {"leakscan": ["tiki/"]}})
        argv = floor._render(floor.BY_NAME["leakscan"].hook, Path("/repo"),
                             cfg, "leakscan")
        self.assertIn("--staged", argv)
        positional = [a for a in argv if not a.startswith("-")
                      and a not in ("/repo",)]
        self.assertTrue(positional, "staged scope must still pass its subtree")
        for a in positional:
            self.assertFalse(a.startswith("/"),
                             f"staged path must be repo-relative, got {a!r}")

    def test_default_staged_scope_passes_no_positional(self):
        """Whole-repo staged cover means NO positional at all — not '.', which
        is an absolute-path-shaped miss in disguise (git never lists './x')."""
        argv = floor._render(floor.BY_NAME["secretscan"].hook, Path("/repo"),
                             floor.Config(), "secretscan")
        self.assertEqual(argv, ["--staged", "--root", "/repo"])

    def test_flags_stay_local_to_their_scanner(self):
        cfg = _cfg({"flags": {"leakscan": ["--disable", "ipv4"]}})
        argv = floor._render(floor.BY_NAME["secretscan"].hook, Path("/repo"),
                             cfg, "secretscan")
        self.assertNotIn("--disable", argv)


class LocalSeamTest(unittest.TestCase):
    """The repo-local extension point: a child declaring a check of its OWN.

    The forcing case (`ros`, 2026-07-26) is a tripwire whose blocklist names the
    estate's own tokens — it can never be a shared scanner, so before this seam
    the repo's only options were a bespoke hook (falling out of propagation, the
    exact defect floor.py exists to end) or losing the check.

    Every test here is about the seam being an ADDITION. The moment it can
    replace, shadow or quietly weaken a fleet check, it has become a hole with a
    config key in front of it.
    """

    DECL = {"run": "tools/tripwire.py", "why": "estate tokens never enter a commit"}

    def test_local_check_runs_on_both_planes_by_default(self):
        cfg = _cfg({"local": {"tripwire": dict(self.DECL)}})
        for plane in ("hook", "ci"):
            self.assertEqual(_states(plane, cfg)["tripwire"], "enforced")

    def test_local_check_does_not_disturb_the_fleet_floor(self):
        cfg = _cfg({"local": {"tripwire": dict(self.DECL)}})
        states = _states("ci", cfg)
        self.assertEqual(len(states), len(floor.SCANNERS) + 1)
        for s in floor.SCANNERS:
            if not s.opt_in:
                self.assertEqual(states[s.name], "enforced", f"{s.name} must be untouched")

    def test_a_local_check_may_not_shadow_a_fleet_scanner(self):
        """The load-bearing guard. If `local` could take a registered name, a
        child could point `leakscan` at a script that exits 0 — and the board
        would go on printing 'leakscan enforced' beside it."""
        with self.assertRaises(floor.ConfigError):
            _cfg({"local": {"leakscan": {"run": "x.py", "why": "mine now"}}})

    def test_run_path_must_stay_inside_the_repo(self):
        """The seam runs the repo's own committed code. A path that climbs out
        of the tree is running something the repo does not hold, on a plane the
        repo's reviewers never see."""
        for bad in ("../../etc/evil.sh", "/usr/bin/env", "tools/../../x.py"):
            with self.assertRaises(floor.ConfigError):
                _cfg({"local": {"t": {"run": bad, "why": "w"}}})

    def test_unknown_keys_in_a_local_declaration_are_refused(self):
        """Local seam cold pass, LS4. Extras were read past in silence, which
        relaxed this file's own "a config cannot quietly mean less than it says"
        rule exactly where it IS enforced for scanner names. The failures are
        not cosmetic: a `planes` typo leaves the default in place, so a
        hook-only tripwire also runs on CI, and an `args` typo drops the
        arguments so the check runs against nothing."""
        for bad in ({"plane": ["hook"]}, {"arg": ["--x"]}, {"scopes": ["src"]},
                    {"nonsense": 1}):
            decl = {"run": "tools/t.py", "why": "w", **bad}
            with self.assertRaises(floor.ConfigError, msg=repr(bad)):
                _cfg({"local": {"t": decl}})

    def test_every_key_the_parser_reads_is_a_known_key(self):
        """The set and the parser must not drift apart: a key the parser reads
        but the set omits would be rejected as unknown the first time a child
        used it, which fails safely but confusingly."""
        self.assertEqual(floor.LOCAL_KEYS,
                         frozenset({"run", "why", "planes", "args", "scope"}))
        # And a fully-populated declaration still parses.
        cfg = _cfg({"local": {"t": {"run": "tools/t.py", "why": "w",
                                    "planes": ["hook"], "args": ["--x"],
                                    "scope": ["src"]}}})
        self.assertEqual(cfg.local[0].name, "t")

    def test_a_local_check_states_what_it_protects(self):
        for bad in ({"run": "x.py"}, {"run": "x.py", "why": "  "}, {"why": "w"}):
            with self.assertRaises(floor.ConfigError):
                _cfg({"local": {"t": bad}})

    def test_rejects_local_as_a_bare_list(self):
        with self.assertRaises(floor.ConfigError):
            _cfg({"local": [{"name": "t", "run": "x.py", "why": "w"}]})

    def test_planes_must_be_real_and_non_empty(self):
        for bad in (["prod"], [], ["hook", "staging"]):
            with self.assertRaises(floor.ConfigError):
                _cfg({"local": {"t": {**self.DECL, "planes": bad}}})

    def test_hook_only_check_still_lists_on_ci_as_skipped(self):
        """The machine-local-data case — leakscan's shape, in a child. A check
        absent from CI must SAY it was absent; silence there is indistinguishable
        from a check that ran and passed, which is the whole file's defect."""
        cfg = _cfg({"local": {"tripwire": {**self.DECL, "planes": ["hook"]}}})
        self.assertEqual(_states("hook", cfg)["tripwire"], "enforced")
        self.assertEqual(_states("ci", cfg)["tripwire"], "skipped")

    def test_local_check_can_be_softened_by_the_same_two_spellings(self):
        """One vocabulary. A reader of a board should not need to know whether a
        softened check was inherited or declared to know what happened to it."""
        soft = _cfg({"local": {"tripwire": dict(self.DECL)}, "advisory": ["tripwire"]})
        self.assertEqual(_states("hook", soft)["tripwire"], "advisory")
        off = _cfg({"local": {"tripwire": dict(self.DECL)},
                    "disabled": {"tripwire": "rewriting the blocklist"}})
        self.assertEqual(_states("hook", off)["tripwire"], "disabled")

    def test_disabling_a_local_check_still_needs_a_reason(self):
        with self.assertRaises(floor.ConfigError):
            _cfg({"local": {"tripwire": dict(self.DECL)}, "disabled": {"tripwire": " "}})

    def test_scope_and_args_belong_with_the_declaration(self):
        """One fact, one home. `scope`/`flags` bend a check the child did not
        write; a local check's own scope and arguments sit beside it, so nobody
        has to read two blocks to know what actually ran."""
        for block in ({"scope": {"t": ["src"]}}, {"flags": {"t": ["--quiet"]}}):
            with self.assertRaises(floor.ConfigError):
                _cfg({"local": {"t": dict(self.DECL)}, **block})

    def test_local_scope_narrows_the_check(self):
        cfg = _cfg({"local": {"t": {**self.DECL, "scope": ["src"]}}})
        self.assertEqual(floor.subtrees(Path("/repo"), cfg, "t"), ["src"])

    def test_rejects_empty_local_scope(self):
        with self.assertRaises(floor.ConfigError):
            _cfg({"local": {"t": {**self.DECL, "scope": []}}})

    def test_args_render_with_the_same_templates(self):
        cfg = _cfg({"local": {"t": {**self.DECL, "args": ["--root", "{root}", "{scope}"]}}})
        argv = floor._render(cfg.local[0].hook, Path("/repo"), cfg, "t")
        self.assertEqual(argv, ["--root", "/repo", "/repo"])


class LocalSeamInvocationTest(unittest.TestCase):
    """The seam as it actually executes — fail-closed, and the argv it builds."""

    def _repo(self, td: str, decl: dict, script: str | None = None,
              name: str = "tools/tripwire.py") -> Path:
        root = Path(td)
        (root / floor.CONFIG_NAME).write_text(
            json.dumps({"local": {"tripwire": decl}}), encoding="utf-8")
        if script is not None:
            p = root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(script, encoding="utf-8")
        return root

    def _floor(self, root: Path) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "floor.py"),
             "--plane", "ci", "--root", str(root), "--json"],
            capture_output=True, text=True,
        )

    def test_declared_but_missing_script_blocks(self):
        """Declaring a check you do not ship must not be a way to look guarded —
        the same fail-closed rule the registry applies to its own scanners."""
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.py", "why": "w"})
            r = self._floor(root)
            self.assertEqual(r.returncode, 1)
            self.assertIn("fail closed", r.stderr.lower())
            self.assertIn("tripwire", r.stderr)

    def test_a_child_authored_why_cannot_forge_an_actions_annotation(self):
        """Local seam cold pass, LS1. Actions parses its `::` log commands line
        by line, so a newline inside an interpolated value ends the command and
        lets what follows be read as a fresh one. Before the seam this channel
        carried only hardcoded registry strings; the seam feeds it
        child-authored text, and on a repo whose CI runs against pull requests
        that text can come from a contributor.

        GITHUB_ACTIONS is set explicitly rather than inherited: annotation mode
        is env-gated, so a test that merely runs the floor would pass on a
        laptop by never entering the branch it means to exercise.

        TWO guards now stand between that payload and the log, and the outer
        one moved. C1F3's parse-time strip (ruled 2026-07-28) drops C0
        controls from every config string, so the newline is GONE before `_wc`
        is reached — the payload arrives as inert text on one line rather than
        as an encoded `%0A`. `_wc` is kept and still pinned directly below: it
        guards the interpolation point itself, which is where a string from
        some future source that never passed through the config parser would
        arrive. The property under test is unchanged — no forged annotation
        reaches the log — but it is now met by removal rather than encoding,
        and that is stated here rather than left for the next reader to
        rediscover from a mysteriously absent `%0A`."""
        payload = ("legit\n::error::INJECTED spoofed annotation\n"
                   "::set-output name=x::pwn")
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.py", "why": payload},
                              "import sys; sys.exit(1)")
            r = subprocess.run(
                [sys.executable, str(TOOLS_DIR / "floor.py"),
                 "--plane", "ci", "--root", str(root)],
                capture_output=True, text=True,
                env={**os.environ, "GITHUB_ACTIONS": "true"},
            )
        # The load-bearing assertions, unchanged: Actions reads a `::` command
        # only at the START of a line, so a payload that cannot open a line
        # cannot forge one.
        self.assertNotIn("\n::error::INJECTED", r.stdout)
        self.assertNotIn("\n::set-output", r.stdout)
        # It survives as inert text on the real annotation's line — not
        # silently swallowed, which would hide a hostile `why` from the
        # operator who most needs to see it.
        self.assertIn("INJECTED spoofed annotation", r.stdout)
        self.assertNotIn("\x0a::", r.stdout.split("::error::tripwire failed")[1])
        # ...and the real annotation is still emitted, or the guard has simply
        # broken the feature it was protecting.
        self.assertIn("::error::tripwire failed", r.stdout)

    def test_the_interpolation_point_still_encodes_newlines_itself(self):
        """The inner guard, pinned on its own now that the parse-time strip
        means the end-to-end test above can no longer reach it. `_wc` is the
        mitigation at the point of interpolation, which is where a string that
        never came through `Config.load` would arrive — a registry `why`, a
        future field, a scanner name read from somewhere else."""
        self.assertEqual(floor._wc("legit\n::error::INJECTED"),
                         "legit%0A::error::INJECTED")

    def test_a_percent_in_a_why_is_encoded_before_the_newlines(self):
        """Order matters: encoding `%` after the newline escapes would
        re-encode the `%` in `%0A` and corrupt every annotation."""
        self.assertEqual(floor._wc("100%\nx"), "100%25%0Ax")

    def test_a_symlink_out_of_the_tree_does_not_execute(self):
        """Local seam cold pass, LS3. "`run` must resolve inside the repo" was
        enforced on the declared STRING only, so a committed symlink whose
        target sits outside the tree executed out-of-tree code — proved live.
        The lexical test above cannot see this: it never plants a symlink, so
        the suite overstated what the guard did."""
        with tempfile.TemporaryDirectory() as td, \
                tempfile.TemporaryDirectory() as outside:
            evil = Path(outside) / "EVIL.py"
            evil.write_text("open('" + str(Path(outside) / "ran") + "', 'w').close()",
                            encoding="utf-8")
            root = self._repo(td, {"run": "tools/tripwire.py", "why": "w"})
            link = root / "tools" / "tripwire.py"
            link.parent.mkdir(parents=True, exist_ok=True)
            link.symlink_to(evil)
            r = self._floor(root)
            self.assertEqual(r.returncode, 1)
            self.assertIn("resolves outside", r.stderr)
            self.assertFalse((Path(outside) / "ran").exists(),
                             "out-of-tree code must not have executed")

    def test_a_symlink_staying_inside_the_tree_still_runs(self):
        """The complement — the guard must not break the legitimate case of a
        repo symlinking its own committed script."""
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.py", "why": "w"},
                              "import sys; sys.exit(0)", name="tools/real.py")
            (root / "tools" / "tripwire.py").symlink_to(root / "tools" / "real.py")
            r = self._floor(root)
            self.assertEqual(r.returncode, 0, r.stderr)
            got = {x["name"]: x for x in json.loads(r.stdout)["results"]}["tripwire"]
            self.assertEqual(got["state"], "enforced")

    def test_an_unrunnable_script_blocks_cleanly_instead_of_crashing(self):
        """Local seam cold pass, LS2. The exec-bit guard had an unguarded
        sibling: an EXECUTABLE non-Python script with no valid shebang raised
        Errno 8 out of subprocess and took the whole floor down with a
        traceback — no summary, and any local check after it never ran. That is
        fail-closed by exit code but not by clean message, which is precisely
        what the exec-bit guard exists to avoid."""
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.sh", "why": "w"},
                              "this is not a script", name="tools/tripwire.sh")
            (root / "tools" / "tripwire.sh").chmod(0o755)
            r = self._floor(root)
            self.assertEqual(r.returncode, 1)
            self.assertNotIn("Traceback", r.stderr)
            self.assertIn("shebang", r.stderr)
            # The summary must survive: a floor that dies mid-list has reported
            # nothing about the checks that never got to run.
            self.assertIn("tripwire", r.stdout)

    def test_a_disabled_local_check_keeps_its_local_marking(self):
        """Local seam cold pass, LS5. Every other branch passes `local=`; the
        disabled one did not, so a --json consumer could not tell a disabled
        LOCAL check from a disabled fleet one, and the render dropped the
        `· local` tag that says whose decision it was."""
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.py", "why": "w"},
                              "import sys; sys.exit(0)")
            cfg = json.loads((root / floor.CONFIG_NAME).read_text())
            cfg["disabled"] = {"tripwire": "probe reason"}
            (root / floor.CONFIG_NAME).write_text(json.dumps(cfg), encoding="utf-8")
            r = self._floor(root)
            got = {x["name"]: x for x in json.loads(r.stdout)["results"]}["tripwire"]
            self.assertEqual((got["state"], got["local"]), ("disabled", True))

    def test_a_failing_local_check_blocks_the_floor(self):
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.py", "why": "w"},
                              "import sys; sys.exit(3)")
            r = self._floor(root)
            self.assertEqual(r.returncode, 1)
            got = {x["name"]: x for x in json.loads(r.stdout)["results"]}["tripwire"]
            self.assertEqual((got["state"], got["rc"], got["local"]),
                             ("enforced", 3, True))

    def test_an_advisory_local_check_reports_without_blocking(self):
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.py", "why": "w"},
                              "import sys; sys.exit(3)")
            cfg = json.loads((root / floor.CONFIG_NAME).read_text())
            cfg["advisory"] = ["tripwire"]
            (root / floor.CONFIG_NAME).write_text(json.dumps(cfg), encoding="utf-8")
            r = self._floor(root)
            self.assertEqual(r.returncode, 0, r.stderr)
            got = {x["name"]: x for x in json.loads(r.stdout)["results"]}["tripwire"]
            self.assertEqual(got["state"], "advisory")
            self.assertEqual(got["rc"], 3, "the check still ran and still failed")

    def test_a_non_python_check_needs_the_execute_bit(self):
        """Without this guard subprocess raises PermissionError and the whole
        floor dies with a traceback — which reads as broken tooling rather than
        the config error it is."""
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.sh", "why": "w"},
                              "#!/bin/sh\nexit 0\n", name="tools/tripwire.sh")
            r = self._floor(root)
            self.assertEqual(r.returncode, 1)
            self.assertIn("not executable", r.stderr)
            (root / "tools/tripwire.sh").chmod(0o755)
            self.assertEqual(self._floor(root).returncode, 0)

    def test_local_results_are_marked_in_json_and_render(self):
        """A consumer must be able to tell an inherited check from a declared
        one without a lookup table of atelier's registry."""
        with tempfile.TemporaryDirectory() as td:
            root = self._repo(td, {"run": "tools/tripwire.py", "why": "w"},
                              "import sys; sys.exit(0)")
            payload = json.loads(self._floor(root).stdout)["results"]
            got = {x["name"]: x for x in payload}
            self.assertTrue(got["tripwire"]["local"])
            self.assertFalse(got["secretscan"]["local"])
            self.assertIn("· local", floor.render(
                [floor.Result("tripwire", "enforced", 0, local=True)], "ci"))


class InvocationTest(unittest.TestCase):
    """End-to-end behaviour of the tool as the hook and CI actually call it."""

    def _run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "floor.py"), *args],
            capture_output=True, text=True,
        )

    def test_selftest_passes(self):
        self.assertEqual(self._run("--selftest").returncode, 0)

    def test_json_stdout_stays_pure_inside_actions(self):
        """--json promises stdout carries nothing but the JSON document. Inside
        Actions, floor.py also emits ::group::/::error:: workflow commands — and
        those went to stdout unconditionally, so any caller parsing --json from
        within a workflow got a JSONDecodeError on the first ::group:: line.

        This is the regression that made the whole floor red for ~13 hours from
        2026-07-25: the suite passed locally (no GITHUB_ACTIONS in the
        environment) and failed only in CI, where the var is always set. Pinning
        the var here means the contract is tested where it actually breaks,
        rather than only where it happens to hold."""
        env = {**os.environ, "GITHUB_ACTIONS": "true"}
        with tempfile.TemporaryDirectory() as td:
            r = subprocess.run(
                [sys.executable, str(TOOLS_DIR / "floor.py"),
                 "--plane", "ci", "--root", td, "--json"],
                capture_output=True, text=True, env=env,
            )
            self.assertEqual(r.returncode, 0, r.stderr)
            # The real assertion: parses at all. A ::group:: on stdout fails here.
            payload = json.loads(r.stdout)
            self.assertEqual(payload["plane"], "ci")
            self.assertNotIn("::group::", r.stdout)
            # ...and the markers are not lost, just relocated to stderr.
            self.assertIn("::group::", r.stderr)

    def test_unresolvable_scope_blocks_a_check_that_may_not_be_softened(self):
        """ADR 0008 cold pass, EP1. A one-character typo in a `scope` path used
        to turn secretscan or leakscan off and still exit 0 — the skip branch
        below, reached by a check that has no advisory form precisely because it
        may never be softened. Same call as an empty `local.*.scope` and as an
        absolute path in --staged mode. This is ONE member of that class; the
        two that resolve-but-outside are pinned by the three tests below
        (TA1)."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"secretscan": ["nosuchtree"]}}), encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td)
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("secretscan", r.stderr)
            self.assertIn("nosuchtree", r.stderr)
            # The remedy has to name both ways out, or it reads as "your repo is
            # broken" rather than "your config drifted".
            self.assertIn(floor.CONFIG_NAME, r.stderr)
            self.assertIn("scope.secretscan", r.stderr)

    def test_partial_scope_drift_blocks_too(self):
        """One of two declared paths going missing halves a boundary check's
        cover. The finding was written about a scope resolving to NOTHING; the
        class is any declared path that does not resolve."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"secretscan": ["docs", "gone"]}}), encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td)
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("gone", r.stderr)

    def test_scope_outside_the_repo_is_refused_at_parse(self):
        """Track A application cold pass, TA1 (MAJOR), ruled (a). A scope path
        that RESOLVES but not to this repo's tree used to pass the existence
        guard, render on the hook plane to a prefix matching nothing in the
        staged diff, and exit 0 — a boundary check vacated under a ✅. Refused
        at config load, so it blocks on BOTH planes and by message, never by
        the traceback an absolute path used to take on CI (TA2)."""
        for bad in ("/etc", "..", "../sibling"):
            for plane in ("hook", "ci"):
                with self.subTest(scope=bad, plane=plane):
                    with tempfile.TemporaryDirectory() as td:
                        (Path(td) / floor.CONFIG_NAME).write_text(
                            json.dumps({"scope": {"secretscan": [bad]}}),
                            encoding="utf-8")
                        r = self._run("--plane", plane, "--root", td)
                        self.assertEqual(r.returncode, 1, r.stdout)
                        self.assertIn("INSIDE the repo", r.stderr)
                        self.assertIn("scope.secretscan", r.stderr)
                        # Fail-closed by config error, not by crash: a traceback
                        # reads as broken tooling rather than a fixable config.
                        self.assertNotIn("Traceback", r.stderr)

    def test_scope_escaping_via_symlink_blocks_at_the_guard(self):
        """The member the lexical check cannot see: a relative, `..`-free path
        that exists and points out of the tree. Caught where a root exists to
        resolve against, and it must block rather than skip — this is a check
        with no advisory form reading a tree that is not the repo."""
        with tempfile.TemporaryDirectory() as td:
            outside = Path(td) / "outside"
            outside.mkdir()
            root = Path(td) / "repo"
            root.mkdir()
            (root / "logs").symlink_to(outside)
            (root / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"secretscan": ["logs"]}}), encoding="utf-8")
            r = self._run("--plane", "hook", "--root", str(root))
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("OUTSIDE this repo", r.stderr)

    def test_an_in_tree_scope_is_still_accepted(self):
        """The guard must not become "no scope override works". atelier and one
        child both declare in-tree scopes today; measured at ruling time, every
        live declaration in the estate passes this unchanged."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"secretscan": ["docs"]}}), encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td, "--json")
            self.assertEqual(r.returncode, 0, r.stderr)
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            self.assertEqual(results["secretscan"]["state"], "enforced")

    def test_local_scope_is_held_to_the_same_rule(self):
        """`local.*.scope` feeds the same `subtrees`/`_render` path as a fleet
        `scope`, so it carries the same hazard and the same check. `local.run`
        was already validated this way — the point of TA1 is that one spelling
        of "where does this check look" was guarded and the others were not."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "check.py").write_text("import sys; sys.exit(0)\n", encoding="utf-8")
            (Path(td) / floor.CONFIG_NAME).write_text(json.dumps({"local": {"t": {
                "run": "check.py", "why": "pins a repo-local invariant",
                "scope": ["../elsewhere"]}}}), encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td)
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("local.t.scope", r.stderr)
            self.assertIn("INSIDE the repo", r.stderr)

    def _cfg_run(self, td, cfg, plane="ci", *extra):
        (Path(td) / floor.CONFIG_NAME).write_text(json.dumps(cfg), encoding="utf-8")
        return self._run("--plane", plane, "--root", td, *extra)

    def test_advisory_needs_both_a_reason_and_a_review_date(self):
        """C1, ruled 2026-07-28: both hard-required. `disabled` — the harder,
        more visible opt-out — has always demanded a reason while `advisory`,
        the softer and more forgettable one, demanded nothing. Each half is
        refused separately, and the message says WHICH half is missing: a
        declaration that is nearly right is the one a writer will re-submit."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            r = self._cfg_run(td, {"advisory": {"wrapscan": {"why": "adopting"}}})
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("review-by", r.stderr)

            r = self._cfg_run(td, {"advisory": {"wrapscan": {"review-by": "2026-12-01"}}})
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("`why`", r.stderr)

            # A bare string reads like the full spelling and is not.
            r = self._cfg_run(td, {"advisory": {"wrapscan": "adopting the check"}})
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("review date", r.stderr)

    def test_review_by_must_be_a_real_iso_date(self):
        """The format is validated at parse so the ageing comparison downstream
        can be a plain string compare — and so a repo cannot declare
        '01/12/2026' and get an advisory that never expires."""
        with tempfile.TemporaryDirectory() as td:
            for bad in ("01/12/2026", "2026-13-01", "soon"):
                with self.subTest(date=bad):
                    r = self._cfg_run(td, {"advisory": {
                        "wrapscan": {"why": "x", "review-by": bad}}})
                    self.assertEqual(r.returncode, 1, r.stdout)

    def test_an_unknown_advisory_key_is_refused(self):
        """Same call as the local seam's key check (LS4): a key read past in
        silence is a declaration its writer believes is doing something."""
        with tempfile.TemporaryDirectory() as td:
            r = self._cfg_run(td, {"advisory": {"wrapscan": {
                "why": "x", "review-by": "2026-12-01", "until": "2027-01-01"}}})
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("'until'", r.stderr)

    def test_an_expired_advisory_reports_but_never_blocks(self):
        """The ruled shape of expiry (2026-07-28): the board goes red, nothing
        fails. A commit blocked by a date somebody set months earlier is how a
        forcing function becomes a --no-verify habit, so the pressure is
        visibility, not breakage."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            r = self._cfg_run(td, {"advisory": {"wrapscan": {
                "why": "adopting", "review-by": "2020-01-01"}}}, "ci", "--json")
            self.assertEqual(r.returncode, 0, r.stderr)
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            self.assertTrue(results["wrapscan"]["expired"])
            self.assertEqual(results["wrapscan"]["state"], "advisory")
            self.assertEqual(results["wrapscan"]["review_by"], "2020-01-01")

    def test_a_live_advisory_is_not_expired(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            r = self._cfg_run(td, {"advisory": {"wrapscan": {
                "why": "adopting", "review-by": "2999-01-01"}}}, "ci", "--json")
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            self.assertFalse(results["wrapscan"]["expired"])
            self.assertEqual(results["wrapscan"]["reason"], "adopting")

    def test_the_legacy_bare_list_still_parses_and_says_it_is_legacy(self):
        """The transition (ruled 2026-07-28). Children fetch atelier@main at CI
        run time, so a hard error on the old spelling would break every child's
        CI the afternoon this lands. The bare list parses, marks itself, and
        becomes an error in phase 2 — a transition, not a dialect."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            r = self._cfg_run(td, {"advisory": ["wrapscan"]}, "ci", "--json")
            self.assertEqual(r.returncode, 0, r.stderr)
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            self.assertTrue(results["wrapscan"]["legacy"])
            self.assertEqual(results["wrapscan"]["state"], "advisory")
            self.assertFalse(results["wrapscan"]["expired"])

    def test_narrowing_a_boundary_check_states_why(self):
        """A1 option (b), deferred out of the A1 ruling into C1 and ruled there
        (2026-07-28). A `scope` on a check that may never be softened is a cover
        decision, so it goes on the record like a disabled one."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            r = self._cfg_run(td, {"scope": {"leakscan": {"paths": ["docs"]}}})
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("needs a `why`", r.stderr)

            r = self._cfg_run(td, {"scope": {"leakscan": {
                "paths": ["docs"], "why": "only docs/ is shareable here"}}})
            self.assertEqual(r.returncode, 0, r.stderr)

    def test_a_softenable_scope_needs_no_reason(self):
        """The other side of A1(b), or the rule becomes ceremony: narrowing a
        prose check is an ordinary layout fact, not a cover decision."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            r = self._cfg_run(td, {"scope": {"wrapscan": {"paths": ["docs"]}}})
            self.assertEqual(r.returncode, 0, r.stderr)

    def test_a_legacy_scope_list_is_exempt_for_the_transition(self):
        """It cannot carry a `why` at all, so holding it to A1(b) would be the
        flag day the transition exists to avoid."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            r = self._cfg_run(td, {"scope": {"leakscan": ["docs"]}})
            self.assertEqual(r.returncode, 0, r.stderr)

    def test_partial_scope_drift_on_a_softenable_check_is_visible(self):
        """TA3. The blocking guard covers only checks with no advisory form, so
        a softenable check whose scope has half stopped resolving used to run on
        less and print nothing at all — cover shrank with no signal. It must
        still not block (the code-only-repo case), but it must say so, and the
        note must reach --json so the fleet board can carry it."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"wrapscan": ["docs", "gone"]}}), encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td, "--json")
            self.assertEqual(r.returncode, 0, r.stderr)
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            self.assertEqual(results["wrapscan"]["state"], "enforced")
            self.assertIn("1 of 2 scope paths missing", results["wrapscan"]["partial"])
            self.assertIn("gone", results["wrapscan"]["partial"])

    def test_a_fully_resolving_scope_carries_no_drift_note(self):
        """The other direction, or the note becomes wallpaper: a scope whose
        paths all resolve is full cover for that check and renders plain."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"wrapscan": ["docs"]}}), encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td, "--json")
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            self.assertEqual(results["wrapscan"]["partial"], "")

    def test_the_cover_note_states_the_invocation_not_a_cover_level(self):
        """TA4. The argv knows what cover was DEMANDED; only the scanner's own
        output knows what it got. On a machine holding a term list, a ci-plane
        leakscan reports 'structural + local' while this line used to assert
        'partial cover' — the delta's own test failed in mirror image. The line
        now states the invocation, which is true in both environments; the 🟡
        stays, because a real runner holds no list."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / floor.CONFIG_NAME).write_text("{}", encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td, "--json")
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            note = results["leakscan"]["partial"]
            self.assertIn("does not pass --require-terms", note)
            # The claim it must no longer make: that cover WAS partial.
            self.assertNotIn("partial cover", note)

    def test_a_softenable_check_still_skips_a_missing_tree(self):
        """The other half of the guard, and the reason it is not blanket: the
        skip exists so a code-only repo is not blocked by the prose checks. Only
        the no-advisory-form scanners lose it."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"wrapscan": ["nosuchtree"]}}), encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td, "--json")
            self.assertEqual(r.returncode, 0, r.stderr)
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            self.assertEqual(results["wrapscan"]["state"], "skipped")

    def test_missing_records_tree_skips_visibly(self):
        """A code-only repo has no dating discipline to check. It must not be
        BLOCKED (the scanners exit 2 on a missing path) and must not be silently
        green either — the skip has to say what it looked for."""
        with tempfile.TemporaryDirectory() as td:
            r = self._run("--plane", "ci", "--root", td, "--json")
            self.assertEqual(r.returncode, 0, r.stderr)
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
            for name in ("datescan", "wrapscan", "spellscan"):
                self.assertEqual(results[name]["state"], "skipped")
                self.assertIn("docs", results[name]["reason"])

    def test_unusable_config_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / floor.CONFIG_NAME).write_text("{ broken", encoding="utf-8")
            r = self._run("--plane", "hook", "--root", td)
            self.assertEqual(r.returncode, 1)
            self.assertIn(floor.CONFIG_NAME, r.stderr)

    def test_missing_scanner_blocks_and_names_itself(self):
        """The fail-closed contract, at the registry level."""
        with tempfile.TemporaryDirectory() as td:
            empty_tools = Path(td) / "tools"
            empty_tools.mkdir()
            r = self._run("--plane", "ci", "--root", td, "--tools", str(empty_tools))
            self.assertEqual(r.returncode, 1)
            self.assertIn("fail closed", r.stderr.lower())
            self.assertIn("secretscan", r.stderr)


class ScopeGuardHonestyTest(unittest.TestCase):
    """The guard's own comment must not claim a door it shut is still open.

    TAA1 (minor, ruled FIX 2026-07-28). One commit in the TA series shut both
    outside-the-repo members of the scope class; the series landed without
    updating the class-members comment a few lines below, which went on
    asserting both were "(open)" — the enforcement plane advertising two
    fail-opens that no longer existed. That is the record-drift class TA8
    fixes, running the opposite way, and it is the one claim no behaviour test
    can catch, which is why the assertion is made against the source text.

    The behaviour these three members describe is pinned by the three TA1
    tests in InvocationTest above; this pins that the prose beside them agrees.
    """

    def _guard_comment(self) -> str:
        src = (TOOLS_DIR / "floor.py").read_text(encoding="utf-8")
        self.assertIn("It is ONE member of that class", src)
        return src.split("It is ONE member of that class")[1].split(
            "if missing and")[0]

    def test_no_member_of_the_scope_class_is_labelled_open(self):
        comment = self._guard_comment()
        self.assertNotIn("(open", comment)
        self.assertNotIn("has neither half", comment)

    def test_the_ta1_pointer_survives_the_correction(self):
        """The ruling kept the pointer deliberately: a reader who meets this
        guard needs the finding that produced it, or the next correction has
        to be rediscovered from scratch."""
        self.assertIn("TA1", self._guard_comment())


class ReportedNoteTest(unittest.TestCase):
    """One line, every note that is true of it.

    Two findings from two cold passes, one shape: a report field that held one
    note at a time. `Result.partial` chose the cover note OR the scope-drift
    note (TAA2), and the human line chose an advisory's reason OR whatever
    `partial` held (C1F1). Both drop the SHRINK and keep the excuse, which is
    the wrong half to lose — a softened check whose cover is quietly shrinking
    is the case the board is least able to see. Ruled JOIN THE NOTES,
    2026-07-28, and implemented as one design.
    """

    def _run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "floor.py"), *args],
            capture_output=True, text=True,
        )

    def test_a_cover_note_and_a_drift_note_are_both_reported(self):
        """TAA2. Unreachable through a config today — the only scanner with a
        `full_cover_flag` has no advisory form, so a missing scope path blocks
        at the guard before this code is reached. That is precisely why it is
        pinned: the invariant holding it shut is a registry fact nobody has
        promised to keep, and a future softenable scanner with a cover flag
        would silently re-open a shrink hole inside the fix built to close one.
        A note that joins cannot decay; a comment saying "mind this" can."""
        import dataclasses
        from unittest import mock

        covered = dataclasses.replace(floor.BY_NAME["wrapscan"],
                                      full_cover_flag="--require-terms")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "docs").mkdir()
            (root / "docs" / "a.md").write_text("fine\n", encoding="utf-8")
            cfg = floor.Config(scope={"wrapscan": ("docs", "gone")})
            with mock.patch.object(floor, "SCANNERS", (covered,)), \
                    mock.patch.object(floor, "BY_NAME", {"wrapscan": covered}):
                results = floor.run("ci", root, TOOLS_DIR, cfg, ci=False)
        self.assertEqual(len(results), 1)
        note = results[0].partial
        # Both, not either: the cover note used to win and the drift note
        # vanished with it.
        self.assertIn("--require-terms", note)
        self.assertIn("1 of 2 scope paths missing", note)
        self.assertIn("gone", note)

    def test_a_drift_note_alone_still_reads_as_one_note(self):
        """The other direction, or joining becomes punctuation nobody trusts:
        one true note renders exactly as it did before, with no separator."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(
                json.dumps({"scope": {"wrapscan": ["docs", "gone"]}}),
                encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td, "--json")
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
        note = results["wrapscan"]["partial"]
        self.assertTrue(note.startswith("1 of 2 scope paths missing"), note)
        self.assertNotIn(";", note)

    def test_an_advisory_reason_does_not_displace_the_drift_note(self):
        """C1F1. C1 populates `reason` for every advisory result, so from the
        day it landed a softened check with a half-missing scope rendered
        `🟡 … (clearing backlog) [review by …]` — the visible cause was the
        advisory and the actual mark was the drift's, which survived only in
        --json."""
        line = floor.render([floor.Result(
            "wrapscan", "advisory", 0, reason="clearing backlog",
            partial="1 of 2 scope paths missing (gone) — ran on the rest",
            review_by="2999-01-01")], "hook")
        self.assertIn("clearing backlog", line)
        self.assertIn("1 of 2 scope paths missing", line)
        self.assertIn("[review by 2999-01-01]", line)

    def test_a_line_with_neither_note_stays_bare(self):
        line = floor.render(
            [floor.Result("secretscan", "enforced", 0)], "hook")
        self.assertNotIn("(", line.split("\n")[1])

    def test_an_expired_advisory_shows_how_long_it_has_stood(self):
        """C1F2, ruled ADD THE COUNT TO THE FLOOR LINE (2026-07-28). The
        commit and the intent record both claimed the count rendered "on the
        floor and on the board"; `_days_over` lived only in floorfleet and the
        floor line said `— PASSED]` with no count. "Expired" reads the same on
        day one and day two hundred, and it is day two hundred that means the
        declaration was abandoned — so the count goes where the commit is
        being made, not only on a board someone has to go and look at."""
        line = floor.render([floor.Result(
            "wrapscan", "advisory", 0, reason="adopting",
            review_by="2020-01-01", expired=True,
            days_over=floor._days_over("2020-01-01", "2020-03-01"))], "hook")
        self.assertIn("[review by 2020-01-01 — PASSED, 60 days over]", line)
        self.assertIn("🔴", line)

    def test_the_count_reads_the_same_as_the_fleet_board(self):
        """One declaration, one age. Two spellings of the same fact across the
        floor and the board would read as two different facts, so the wording
        is pinned against floorfleet's rather than merely intended to match."""
        sys.path.insert(0, str(TOOLS_DIR))
        import floorfleet  # noqa: E402
        for review_by, today in (("2020-01-01", "2020-01-01"),
                                 ("2020-01-01", "2020-01-02"),
                                 ("2020-01-01", "2021-06-15"),
                                 ("not-a-date", "2020-01-01")):
            with self.subTest(review_by=review_by, today=today):
                self.assertEqual(floor._days_over(review_by, today),
                                 floorfleet._days_over(review_by, today))

    def test_a_live_advisory_carries_no_count(self):
        line = floor.render([floor.Result(
            "wrapscan", "advisory", 0, reason="adopting",
            review_by="2999-01-01")], "hook")
        self.assertIn("[review by 2999-01-01]", line)
        self.assertNotIn("PASSED", line)

    def test_the_count_reaches_json_as_a_stable_field(self):
        """Always present, empty when there is nothing to say — a --json
        consumer compares two runs field for field."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(json.dumps(
                {"advisory": {"wrapscan": {"why": "adopting",
                                           "review-by": "2020-01-01"},
                              "spellscan": {"why": "adopting",
                                            "review-by": "2999-01-01"}}}),
                encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td, "--json")
            self.assertEqual(r.returncode, 0, r.stderr)
            results = {x["name"]: x for x in json.loads(r.stdout)["results"]}
        self.assertIn("days over", results["wrapscan"]["days_over"])
        self.assertEqual(results["spellscan"]["days_over"], "")
        self.assertEqual(results["secretscan"]["days_over"], "")

    def test_the_expired_line_is_rendered_end_to_end(self):
        """The render path as the hook actually drives it — the human line
        goes to stderr, and an expired advisory still exits 0."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(json.dumps(
                {"advisory": {"wrapscan": {"why": "adopting",
                                           "review-by": "2020-01-01"}}}),
                encoding="utf-8")
            r = self._run("--plane", "ci", "--root", td)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("PASSED,", r.stderr)
            self.assertIn("days over]", r.stderr)


class ControlCharacterTest(unittest.TestCase):
    """A child's config is text an operator READS.

    Every `why`, every disabled reason, every local check's description prints
    straight to a terminal from the floor and from the fleet board, and a
    hostile or careless child could put ANSI escapes in any of them — enough
    to clear the screen, or repaint a red result green. C1F3 (ruled STRIP C0
    CONTROLS AT PARSE, 2026-07-28) closes it at the parse seam so the whole
    class goes at once, including the `disabled` reasons that predate C1.
    """

    def test_a_why_cannot_carry_an_escape_sequence(self):
        cfg = _cfg({"advisory": {"wrapscan": {
            "why": "clearing\x1b[2J\x1b[H backlog", "review-by": "2999-01-01"}}})
        self.assertEqual(cfg.advisory["wrapscan"].why, "clearing[2J[H backlog")

    def test_a_disabled_reason_cannot_either(self):
        """The pre-existing half of the class: `disabled` reasons have printed
        raw since long before C1 added two more fields to the same surface."""
        cfg = _cfg({"disabled": {"spellscan": "no prose\x07\x1b]0;owned\x07"}})
        self.assertNotIn("\x1b", cfg.disabled["spellscan"])
        self.assertNotIn("\x07", cfg.disabled["spellscan"])

    def test_a_scope_why_and_a_local_why_cannot_either(self):
        """Strip at the seam, not per field — the point of the ruling. These
        two were never named in the finding and are covered anyway."""
        cfg = _cfg({"scope": {"leakscan": {"paths": ["docs"],
                                           "why": "only docs\x1b[31m here"}},
                    "local": {"t": {"run": "check.py",
                                    "why": "pins a thing\x08\x08\x08"}}})
        self.assertNotIn("\x1b", cfg.scope["leakscan"].why)
        self.assertNotIn("\x08", cfg.local[0].why)

    def test_keys_are_stripped_as_well_as_values(self):
        """A scanner NAME is echoed in the unknown-scanner error, so it is the
        same surface. Stripped, it no longer matches a real scanner and the
        config fails closed by message — which is the safe direction."""
        with self.assertRaises(floor.ConfigError) as caught:
            _cfg({"disabled": {"spell\x1b[2Kscan": "why"}})
        self.assertNotIn("\x1b", str(caught.exception))

    def test_a_control_free_config_is_untouched(self):
        """The other direction: stripping must not quietly rewrite an honest
        declaration."""
        cfg = _cfg({"advisory": {"wrapscan": {
            "why": "adopting the check; 60 findings to clear",
            "review-by": "2999-01-01"}}})
        self.assertEqual(cfg.advisory["wrapscan"].why,
                         "adopting the check; 60 findings to clear")

    def test_the_rendered_line_carries_no_control_characters(self):
        """End to end, which is the claim that actually matters: what reaches
        the terminal is clean."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "docs").mkdir()
            (Path(td) / floor.CONFIG_NAME).write_text(json.dumps(
                {"disabled": {"spellscan": "no prose\x1b[2J\x1b[H"}}),
                encoding="utf-8")
            r = subprocess.run(
                [sys.executable, str(TOOLS_DIR / "floor.py"),
                 "--plane", "ci", "--root", td],
                capture_output=True, text=True)
        self.assertIn("spellscan", r.stderr)
        self.assertNotIn("\x1b", r.stderr)


if __name__ == "__main__":
    unittest.main()
