"""Stdlib-only tests for flipcheck (no pytest, no network): `python3 -m unittest`.

`gh` is stubbed at `floorfleet._gh_run`, the one place flipcheck reaches it, so
every test drives the real parsing against a canned `CompletedProcess`."""

import json
import subprocess
import unittest
from pathlib import Path
from unittest import mock

import floorfleet
import flipcheck

TOOLS_DIR = Path(__file__).resolve().parent
SLUG = "o/r"


def ok(obj):
    return subprocess.CompletedProcess(["gh"], 0, json.dumps(obj), "")


def err(status, message):
    return subprocess.CompletedProcess(
        ["gh"], 1, json.dumps({"message": message}),
        f"gh: {message} (HTTP {status})\n")


PUBLIC = {
    "repos/o/r": ok({"has_wiki": False, "default_branch": "main",
                     "visibility": "public"}),
    "repos/o/r/actions/permissions": ok(
        {"enabled": True, "allowed_actions": "all",
         "sha_pinning_required": False}),
    "repos/o/r/actions/permissions/workflow": ok(
        {"default_workflow_permissions": "read",
         "can_approve_pull_request_reviews": False}),
    "repos/o/r/actions/permissions/fork-pr-contributor-approval": ok(
        {"approval_policy": "first_time_contributors"}),
    "repos/o/r/private-vulnerability-reporting": ok({"enabled": True}),
    "repos/o/r/rulesets": ok([{"enforcement": "active"},
                              {"enforcement": "disabled"}]),
    "repos/o/r/rules/branches/main": ok(
        [{"type": "deletion"}, {"type": "required_signatures"},
         {"type": "deletion"}]),
    "repos/o/r/branches/main/protection": err(404, "Branch not protected"),
}
UPGRADE = "Upgrade to GitHub Pro or make this repository public to enable this feature."
PRIVATE_FREE = dict(PUBLIC, **{
    "repos/o/r": ok({"has_wiki": True, "default_branch": "main",
                     "visibility": "private"}),
    "repos/o/r/actions/permissions/fork-pr-contributor-approval":
        err(404, "Not Found"),
    "repos/o/r/branches/main/protection": err(403, UPGRADE),
    "repos/o/r/rules/branches/main": err(403, UPGRADE),
    "repos/o/r/rulesets": err(403, UPGRADE),
})


class Gh:
    """A recording stand-in for `floorfleet._gh_run`, keyed by endpoint."""

    def __init__(self, table):
        self.table = table
        self.calls = []

    def __call__(self, args):
        self.calls.append(list(args))
        assert args[0] == "api" and len(args) == 2, args
        return self.table.get(args[1], err(404, "Not Found"))


def read(table, slug=SLUG):
    gh = Gh(table)
    with mock.patch.object(floorfleet, "_gh_run", gh):
        rep = flipcheck.read_repo(slug)
    return rep, gh


def by_key(rep):
    return {s["key"]: s for s in rep["settings"]}


class Reads(unittest.TestCase):
    def test_all_five_read_on_a_public_repo(self):
        rep, _ = read(PUBLIC)
        s = by_key(rep)
        self.assertEqual(rep["visibility"], "public")
        self.assertEqual(
            list(s), ["wiki", "actions_policy", "fork_pr_approval",
                      "private_vulnerability_reporting", "protection"])
        self.assertTrue(all(x["status"] == "read" for x in s.values()))
        self.assertIn("allowed_actions: all", s["actions_policy"]["value"])
        self.assertIn("can_approve_pull_request_reviews: false",
                      s["actions_policy"]["value"])
        self.assertIn("first_time_contributors",
                      s["fork_pr_approval"]["value"])
        self.assertIn("rulesets: 2 (1 active)", s["protection"]["value"])
        self.assertIn("rules on main: deletion, required_signatures",
                      s["protection"]["value"])
        self.assertIn("classic protection on main: none",
                      s["protection"]["value"])

    def test_house_values_only_where_ruled(self):
        s = by_key(read(PUBLIC)[0])
        self.assertIs(s["wiki"]["matches_house"], True)
        self.assertIs(s["private_vulnerability_reporting"]["matches_house"],
                      True)
        for k in ("actions_policy", "fork_pr_approval", "protection"):
            self.assertIsNone(s[k]["matches_house"])

    def test_a_wiki_that_is_on_differs(self):
        s = by_key(read(dict(PUBLIC, **{
            "repos/o/r": ok({"has_wiki": True, "default_branch": "main",
                             "visibility": "public"})}))[0])
        self.assertIs(s["wiki"]["matches_house"], False)
        self.assertIn("ON", s["wiki"]["value"])
        rep = read(dict(PUBLIC, **{
            "repos/o/r": ok({"has_wiki": True, "default_branch": "main",
                             "visibility": "public"})}))[0]
        self.assertIn("Wiki: off (a second git repo the floor never sees)"
                      " -> DIFFERS", flipcheck.render(dict(rep, read_at="x")))

    def test_pvr_off_differs(self):
        s = by_key(read(dict(PUBLIC, **{
            "repos/o/r/private-vulnerability-reporting":
                ok({"enabled": False})}))[0])
        self.assertIs(s["private_vulnerability_reporting"]["matches_house"],
                      False)


class NotAvailable(unittest.TestCase):
    def test_private_free_plan_says_not_available_with_the_reason(self):
        rep, _ = read(PRIVATE_FREE)
        s = by_key(rep)
        fork = s["fork_pr_approval"]
        self.assertEqual(fork["status"], "not available")
        self.assertIsNone(fork["parts"][0]["value"])
        self.assertIn("Not Found (HTTP 404)", fork["parts"][0]["reason"])
        prot = s["protection"]
        self.assertEqual(prot["status"], "not available")
        self.assertIn("HTTP 403", prot["value"])
        self.assertIn("Upgrade to GitHub Pro", prot["value"])
        # The settings that CAN be read are still read.
        self.assertEqual(s["wiki"]["status"], "read")
        self.assertIs(s["wiki"]["matches_house"], False)

    def test_an_unreadable_part_is_partial_never_set(self):
        rep, _ = read(dict(PUBLIC, **{
            "repos/o/r/branches/main/protection": err(403, UPGRADE)}))
        prot = by_key(rep)["protection"]
        self.assertEqual(prot["status"], "partial")
        self.assertIn("rulesets: 2 (1 active)", prot["value"])
        self.assertIn("classic protection on main: not available",
                      prot["value"])
        self.assertNotIn("classic protection on main: none", prot["value"])

    def test_branch_not_protected_is_an_answer_but_a_403_is_not(self):
        none, _ = read(PUBLIC)
        self.assertIn("classic protection on main: none",
                      by_key(none)["protection"]["value"])
        refused, _ = read(dict(PUBLIC, **{
            "repos/o/r/branches/main/protection": err(404, "Not Found")}))
        self.assertIn("classic protection on main: not available",
                      by_key(refused)["protection"]["value"])

    def test_an_unreadable_repo_is_all_not_available_and_does_not_raise(self):
        rep, _ = read({})
        self.assertIsNone(rep["visibility"])
        for s in rep["settings"]:
            self.assertEqual(s["status"], "not available", s["key"])
            self.assertIsNone(s["matches_house"])
        prot = by_key(rep)["protection"]["value"]
        self.assertIn("default branch unknown", prot)

    def test_a_missing_gh_is_not_available_not_a_traceback(self):
        with mock.patch.object(floorfleet, "_gh_run", return_value=None):
            rep = flipcheck.read_repo(SLUG)
        for s in rep["settings"]:
            self.assertEqual(s["status"], "not available")
            self.assertIn("gh could not be run", s["value"])

    def test_a_field_absent_from_a_good_response_is_not_a_value(self):
        rep, _ = read(dict(PUBLIC, **{
            "repos/o/r/private-vulnerability-reporting": ok({})}))
        pvr = by_key(rep)["private_vulnerability_reporting"]
        self.assertEqual(pvr["status"], "not available")
        self.assertIsNone(pvr["matches_house"])


class ReadOnly(unittest.TestCase):
    def test_every_call_is_a_bare_get(self):
        for table in (PUBLIC, PRIVATE_FREE, {}):
            _, gh = read(table)
            self.assertTrue(gh.calls)
            for args in gh.calls:
                self.assertEqual(len(args), 2)
                self.assertEqual(args[0], "api")
                self.assertTrue(args[1].startswith("repos/o/r"))
                self.assertFalse(args[1].startswith("-"))

    def test_the_one_gh_call_site_is_a_bare_api_get(self):
        text = (TOOLS_DIR / "flipcheck.py").read_text()
        self.assertEqual(text.count("_gh_run("), 1)
        self.assertIn('floorfleet._gh_run(["api", path])', text)
        self.assertNotRegex(text, r'"(PATCH|PUT|POST|DELETE)"')


class Cli(unittest.TestCase):
    def _main(self, argv, table):
        import io
        import contextlib
        out, errs = io.StringIO(), io.StringIO()
        with mock.patch.object(floorfleet, "_gh_run", Gh(table)), \
                contextlib.redirect_stdout(out), \
                contextlib.redirect_stderr(errs):
            code = flipcheck.main(argv)
        return code, out.getvalue(), errs.getvalue()

    def test_table_names_every_setting_and_exits_zero_on_unreadables(self):
        code, out, _ = self._main([SLUG], PRIVATE_FREE)
        self.assertEqual(code, 0)
        for label in ("Wiki", "Actions policy", "Fork-PR approval",
                      "Private vulnerability reporting",
                      "Rulesets / branch protection"):
            self.assertIn(label, out)
        self.assertIn("not available (Not Found (HTTP 404))", out)
        self.assertIn("House values:", out)

    def test_json_shape(self):
        code, out, _ = self._main(["--json", SLUG, "o/r2"], PUBLIC)
        self.assertEqual(code, 0)
        doc = json.loads(out)
        self.assertIs(doc["read_only"], True)
        self.assertEqual([r["repo"] for r in doc["repos"]], [SLUG, "o/r2"])
        self.assertRegex(doc["repos"][0]["read_at"],
                         r"^\d{4}-\d\d-\d\dT\d\d:\d\dZ$")
        self.assertEqual(len(doc["repos"][0]["settings"]), 5)

    def test_a_bad_slug_is_exit_2_and_reads_nothing(self):
        for bad in ("nonsense", "a/b/c", "--x", "o/r;rm"):
            gh = Gh(PUBLIC)
            import io
            import contextlib
            with mock.patch.object(floorfleet, "_gh_run", gh), \
                    contextlib.redirect_stderr(io.StringIO()):
                try:
                    code = flipcheck.main([bad])
                except SystemExit as e:  # argparse rejects a leading --
                    code = e.code
            self.assertEqual(code, 2, bad)
            self.assertEqual(gh.calls, [], bad)


if __name__ == "__main__":
    unittest.main()
