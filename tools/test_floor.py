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

    def test_leakscan_never_demands_the_machine_local_term_list(self):
        """--require-terms would demand a list CI cannot (and must not) hold:
        the person/estate terms are machine-local by design (SECRETS.md). CI's
        structural-only cover is the honest degradation — but only as long as
        nobody 'strengthens' it here, which would red every child at once."""
        for form in (floor.BY_NAME["leakscan"].hook, floor.BY_NAME["leakscan"].ci):
            self.assertNotIn("--require-terms", form)

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


class PathScopingTest(unittest.TestCase):
    """Record-subtree scoping — the part that lets the parent run its own floor."""

    def test_override_expands_to_every_subtree(self):
        cfg = _cfg({"paths": {"wrapscan": ["docs/method", "docs/build"]}})
        rendered = floor._render(floor.BY_NAME["wrapscan"].ci, Path("/repo"),
                                 cfg, "wrapscan")
        self.assertTrue(rendered[-1].endswith("docs/build"))
        self.assertTrue(rendered[-2].endswith("docs/method"))
        self.assertIn("--root", rendered)

    def test_override_does_not_leak_to_other_scanners(self):
        cfg = _cfg({"paths": {"wrapscan": ["docs/method", "docs/build"]}})
        rendered = floor._render(floor.BY_NAME["datescan"].ci, Path("/repo"),
                                 cfg, "datescan")
        self.assertEqual(len(rendered), len(floor.BY_NAME["datescan"].ci))

    def test_rejects_override_on_a_whole_tree_scanner(self):
        """Accepting it would read as 'linkscan is scoped' while linkscan kept
        reading everything — a false belief about cover, which is worse than
        no scoping at all."""
        with self.assertRaises(floor.ConfigError):
            _cfg({"paths": {"linkscan": ["docs"]}})

    def test_rejects_empty_override(self):
        with self.assertRaises(floor.ConfigError):
            _cfg({"paths": {"wrapscan": []}})


class InvocationTest(unittest.TestCase):
    """End-to-end behaviour of the tool as the hook and CI actually call it."""

    def _run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "floor.py"), *args],
            capture_output=True, text=True,
        )

    def test_selftest_passes(self):
        self.assertEqual(self._run("--selftest").returncode, 0)

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


if __name__ == "__main__":
    unittest.main()
