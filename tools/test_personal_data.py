"""Tests for docs/PERSONAL-DATA.md — the one list of personal data atelier holds.

Board `160/630` (cold pass PI1/PI2). atelier's hard constraint used to claim each
personal-data exception was "declared where it appears"; the cold pass measured
the account name on 27 lines with no declaration, and the claim was false. The
claim is now "listed in one place", and this is the test that keeps it true:

  * the list is CLOSED — a new entry must change this file's expected set too,
    so adding one is a visible act and not a quiet edit (in a public repo only
    the principal grants one, REPO-STANDARD § Personal data);
  * every tracked file that holds a listed string is a place its entry names;
  * every place an entry names still holds the string (no stale entries);
  * a personal-data allow-marker stands only in a file some entry names.

It reads the register and the tree; it holds no personal string itself.
"""

import fnmatch
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "docs" / "PERSONAL-DATA.md"

# The closed set. Adding an entry means changing these two lines on purpose.
EXPECTED_IDS = ["PD1", "PD2", "PD3", "PD4", "PD5"]
UNPINNED_IDS = {"PD4", "PD5"}  # a given name / a commit header: no file to pin

# Rules (and the term list) whose allow-marker is an excuse for personal data,
# as opposed to a credential or a network shape. Scoped markers only: the
# unscoped form exempts every structural rule and is counted separately.
PERSONAL_SCOPES = {
    "local-term", "email", "pii-key-context", "nz-phone", "nz-address",
    "nz-bank-account", "nz-ird", "payment-card", "iban", "coordinates",
    "diagnosis-key",
}
# The scanner's own sources and tests demonstrate the marker mechanism with
# invented fixtures; they hold no real person's data.
MECHANISM_PREFIXES = ("tools/", "instruments/")

MARKER_RX = re.compile(r"leakscan:allow:([a-z0-9,-]+):")


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True,
                         capture_output=True).stdout
    return [p for p in out.decode("utf-8").split("\0") if p]


def read_text(rel: str) -> str | None:
    try:
        data = (ROOT / rel).read_bytes()
    except OSError:
        return None  # a tracked path removed in the working tree
    if b"\0" in data:
        return None  # binary: not text this test can read
    return data.decode("utf-8", errors="replace")


def glob_rx(pattern: str) -> re.Pattern:
    """`*` stays inside a path segment, `**` crosses them."""
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out, i = out + ".*", i + 2
        elif pattern[i] == "*":
            out, i = out + "[^/]*", i + 1
        else:
            out, i = out + re.escape(pattern[i]), i + 1
    return re.compile(out + r"\Z")


def parse_register() -> list[dict]:
    """Entries from `## PDn — title` sections and their `- **Field:**` bullets."""
    entries, cur, field = [], None, None
    for line in REGISTER.read_text().splitlines():
        m = re.match(r"## (PD\d+) ", line)
        if m:
            cur = {"id": m.group(1), "fields": {}}
            entries.append(cur)
            field = None
            continue
        if cur is None:
            continue
        m = re.match(r"- \*\*([^*:]+):\*\*(.*)", line)
        if m:
            field = m.group(1)
            cur["fields"][field] = m.group(2)
        elif field and line.startswith("  "):
            cur["fields"][field] += " " + line.strip()
        else:
            field = None
    return entries


def ticks(text: str) -> list[str]:
    text = re.sub(r"<!--.*?-->", "", text)
    return re.findall(r"`([^`]+)`", text)


class RegisterShapeTest(unittest.TestCase):
    def setUp(self):
        self.entries = parse_register()

    def test_list_is_closed(self):
        self.assertEqual([e["id"] for e in self.entries], EXPECTED_IDS,
                         "docs/PERSONAL-DATA.md changed its set of entries — "
                         "in a public repo only the principal grants one; "
                         "update this test only on his grant, in his words")

    def test_every_entry_says_why_and_how_granted_and_where(self):
        for e in self.entries:
            for key in ("Data", "Why held", "Granted by", "May stand in"):
                self.assertTrue(e["fields"].get(key, "").strip(),
                                f"{e['id']} has no '{key}' field")

    def test_unpinned_entries_are_exactly_the_declared_ones(self):
        unpinned = {e["id"] for e in self.entries
                    if not self.pinned_strings(e)}
        self.assertEqual(unpinned, UNPINNED_IDS)

    @staticmethod
    def pinned_strings(entry) -> list[str]:
        data = entry["fields"].get("Data", "")
        if "not pinned" in data:
            return []
        return ticks(data)


class RegisterMatchesTreeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = parse_register()
        cls.files = tracked_files()
        cls.text = {f: read_text(f) for f in cls.files}

    def holders(self, strings):
        return sorted(f for f, t in self.text.items()
                      if t and any(s in t for s in strings))

    def test_every_holder_of_a_listed_string_is_a_named_place(self):
        for e in self.entries:
            strings = RegisterShapeTest.pinned_strings(e)
            if not strings:
                continue
            rxs = [glob_rx(g) for g in ticks(e["fields"]["May stand in"])]
            stray = [f for f in self.holders(strings)
                     if not any(rx.match(f) for rx in rxs)]
            self.assertEqual(stray, [],
                             f"{e['id']}: listed data stands in files its entry "
                             "does not name — remove it, or ask the principal "
                             "for a grant and list the place")

    def test_every_named_place_still_holds_the_string(self):
        for e in self.entries:
            strings = RegisterShapeTest.pinned_strings(e)
            if not strings:
                continue
            held = self.holders(strings)
            for g in ticks(e["fields"]["May stand in"]):
                rx = glob_rx(g)
                self.assertTrue(any(rx.match(f) for f in held),
                                f"{e['id']}: '{g}' names a place where the data "
                                "no longer stands — drop it from the entry")

    def test_named_places_exist(self):
        for e in self.entries:
            for g in ticks(e["fields"].get("May stand in", "")):
                if "/" not in g and "*" not in g and not g.startswith("."):
                    continue  # prose token, e.g. a file type
                rx = glob_rx(g)
                self.assertTrue(any(rx.match(f) for f in self.files),
                                f"{e['id']}: '{g}' matches no tracked file")

    def test_personal_data_markers_stand_only_in_named_places(self):
        named = [glob_rx(g) for e in self.entries
                 for g in ticks(e["fields"].get("May stand in", ""))]
        stray = []
        for f, t in self.text.items():
            if not t or f.startswith(MECHANISM_PREFIXES):
                continue
            for line in t.splitlines():
                for m in MARKER_RX.finditer(line):
                    scopes = set(m.group(1).split(","))
                    if scopes & PERSONAL_SCOPES and not any(
                            rx.match(f) for rx in named):
                        stray.append(f)
        self.assertEqual(sorted(set(stray)), [],
                         "a personal-data allow-marker stands in a file no "
                         "docs/PERSONAL-DATA.md entry names — a marker is not "
                         "a grant; only the principal grants an exception")

    def test_personal_scopes_are_real_leakscan_rules(self):
        import leakscan as mod
        names = {p.name for p in mod.STRUCTURAL + mod.WITHDRAWN} | {"local-term"}
        self.assertEqual(PERSONAL_SCOPES - names, set(),
                         "PERSONAL_SCOPES names a rule leakscan does not have")


class ClaimWordingTest(unittest.TestCase):
    """The false claim is gone, and each surface points at the one list."""

    def read(self, rel):
        return (ROOT / rel).read_text()

    def test_no_surface_claims_declared_where_it_appears(self):
        for rel in ("CLAUDE.md", "docs/build/REPO-STANDARD.md",
                    "docs/build/templates/CLAUDE.md",
                    "docs/build/templates/CONTRIBUTING.md"):
            text = re.sub(r"\s+", " ", self.read(rel))
            for stale in ("declared where it appears",
                          "each exception is a declared allowance"):
                self.assertFalse(stale in text, f"{rel} still says: {stale}")

    def test_own_constraint_points_at_the_list(self):
        text = re.sub(r"\s+", " ", self.read("CLAUDE.md"))
        self.assertTrue("docs/PERSONAL-DATA.md" in text, "no pointer")
        self.assertTrue("closed" in text, "does not say the list is closed")

    def test_standard_says_who_grants_in_a_public_repo(self):
        text = re.sub(r"\s+", " ", self.read("docs/build/REPO-STANDARD.md"))
        self.assertTrue("In a public repo only the principal grants" in text,
                        "REPO-STANDARD does not say who grants")
        self.assertTrue("in his own words" in text, "no 'in his own words'")


if __name__ == "__main__":
    unittest.main()
