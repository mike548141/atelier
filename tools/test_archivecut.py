"""Tests for archivecut — the frozen pre-split archives, cut into their stores.

Board `010/220`. Every fixture is synthetic. Covers the board cut (item files,
the section README, the byte-for-byte proof from disk, the index rebuilding
over it), the fallback to a whole-file move when the proof fails (a line
shaped like the cut's own link line, an archive with no `[x]` entries, a
reference-style link cut away from its definition), link re-pointing on both
sides of `](` and in reference definitions, anchors kept or dropped, a
same-page anchor inside an entry, `--plan` writing nothing, and the session
archive's cut and fallback. Stdlib only.
"""

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import archivecut  # noqa: E402
import board  # noqa: E402
import linkscan  # noqa: E402

SECTION = Path("docs/roadmap/990-done-before-the-split")

DONE = """\
# demo ROADMAP — completed detail (archive)

The companion to [`ROADMAP.md`](ROADMAP.md). Entries kept verbatim; the
board lives in [`roadmap/`](roadmap/README.md) now.

## Doctrine — completed cycles
- [x] **First cycle closed** — see
  [`reviews/one.md`](reviews/one.md) and [`../tools/t.py`](../tools/t.py).
- [x] **Second cycle closed** — the [same page](#done-early) and
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md) itself.

  A second paragraph of the second entry.

Some prose that is not an entry, kept under its heading.
- A top-level bullet that is not an entry
  with a continuation line.

## Done early
- [x] **Third thing** — plain.
"""

SESSIONS_ARCHIVE = """\
# demo session log — archive

Verbatim older entries rotated out of [`SESSIONS.md`](SESSIONS.md).

- **2026-01-02 (first session)**: built the thing; see
  [`decisions/0001.md`](decisions/0001.md).

- [2026-01-03 · second](sessions/2026-01-03-01-second.md) — already an
  index line, kept as it stands.

- **2026-01-04 (third session)**: more work.
"""

SESSIONS = """\
# demo — session log (index)

Older entries: [`SESSIONS-ARCHIVE.md`](SESSIONS-ARCHIVE.md).

---

- [2026-02-01 · newest](sessions/2026-02-01-0900-newest.md) — the tail.
"""


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, check=False)


def run(argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        code = archivecut.main(argv)
    return code, out.getvalue()


def board_main(argv):
    with contextlib.redirect_stdout(io.StringIO()), \
            contextlib.redirect_stderr(io.StringIO()):
        return board.main(argv)


def linkscan_ok(root: Path) -> tuple[bool, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        code = linkscan.main(["--root", str(root), str(root)])
    return code == 0, out.getvalue()


class Repo:
    def __init__(self, tmp: Path):
        self.root = tmp

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def read(self, rel):
        return (self.root / rel).read_text(encoding="utf-8")

    def commit(self):
        git(self.root, "add", "-A")
        r = git(self.root, "commit", "-q", "-m", "fixture")
        assert r.returncode == 0, r.stderr


def make_repo(tmp: Path, done: str | None = DONE,
              sessions_archive: str | None = None,
              extra: dict | None = None) -> Repo:
    git(tmp, "init", "-q")
    git(tmp, "config", "user.email", "t")
    git(tmp, "config", "user.name", "Fixture")
    git(tmp, "config", "commit.gpgsign", "false")
    r = Repo(tmp)
    r.write("docs/roadmap/README.md", "# board\n\nlegend\n")
    r.write("docs/roadmap/010-live/README.md", "# Live work\n")
    if done is not None:
        r.write("docs/roadmap/010-live/010-open-thing.md",
                "- [ ] **Open thing.** See [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)"
                "\n      and [the early ones](../../ROADMAP-DONE.md#done-early) and"
                "\n      [a gone one](../../ROADMAP-DONE.md#no-such-heading).\n")
    else:
        r.write("docs/roadmap/010-live/010-open-thing.md",
                "- [ ] **Open thing.**\n")
    r.write("docs/reviews/one.md", "# one\n")
    r.write("docs/decisions/0001.md", "# adr\n")
    r.write("docs/ROADMAP.md", "placeholder\n")
    r.write("tools/t.py", "x = 1\n")
    r.write("docs/sessions/2026-01-03-01-second.md", "# second\n")
    if done is not None:
        r.write("docs/sessions/2026-02-01-0900-newest.md",
                "# newest\n\nHarvested to [`docs/ROADMAP-DONE.md`](../ROADMAP-DONE.md)."
                "\n\n[archive]: ../ROADMAP-DONE.md\n")
    else:
        r.write("docs/sessions/2026-02-01-0900-newest.md", "# newest\n")
    r.write("docs/SESSIONS.md", SESSIONS if sessions_archive is not None
            else SESSIONS.replace(
                "Older entries: [`SESSIONS-ARCHIVE.md`](SESSIONS-ARCHIVE.md).\n\n",
                ""))
    if done is not None:
        r.write("docs/ROADMAP-DONE.md", done)
    if sessions_archive is not None:
        r.write("docs/SESSIONS-ARCHIVE.md", sessions_archive)
    for rel, text in (extra or {}).items():
        r.write(rel, text)
    r.commit()
    board_main(["--rebuild", "--root", str(tmp)])
    r.commit()
    return r


class BoardCut(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_plan_writes_nothing(self):
        r = make_repo(self.tmp)
        before = git(r.root, "status", "--porcelain").stdout
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("route: (a) cut into the store", out)
        self.assertEqual(git(r.root, "status", "--porcelain").stdout, before)
        self.assertFalse((r.root / SECTION).exists())

    def test_cut_writes_items_readme_and_proves_from_disk(self):
        r = make_repo(self.tmp)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("FAIL", out)
        self.assertFalse((r.root / "docs/ROADMAP-DONE.md").exists())
        items = sorted(p.name for p in (r.root / SECTION).glob("*.md")
                       if p.name != "README.md")
        self.assertEqual(len(items), 3)
        self.assertTrue(items[0].startswith("0010-first-cycle-closed"))
        for name in items:
            st = board.item_state(r.read(SECTION / name))
            self.assertEqual(st.marker, "[x]")
        readme = r.read(SECTION / "README.md")
        # preamble, headings and non-entry text verbatim, in order
        self.assertIn("# demo ROADMAP — completed detail (archive)", readme)
        self.assertLess(readme.index("## Doctrine — completed cycles"),
                        readme.index("## Done early"))
        self.assertIn("Some prose that is not an entry, kept under its heading.",
                      readme)
        self.assertIn("- A top-level bullet that is not an entry\n"
                      "  with a continuation line.\n", readme)
        self.assertIn(f"- ✅ [{items[0][:-3]}]({items[0]})", readme)
        # links re-pointed for the new depth, inside the cut text
        self.assertIn("](../../ROADMAP.md)", readme)
        self.assertIn("](../README.md)", readme)
        first = r.read(SECTION / items[0])
        self.assertIn("](../../reviews/one.md)", first)
        self.assertIn("](../../../tools/t.py)", first)
        second = r.read(SECTION / items[1])
        self.assertIn("[same page](./README.md#done-early)", second)
        self.assertIn("[`README.md`](README.md)", second)
        self.assertIn("  A second paragraph of the second entry.\n", second)
        # the proof from disk, against the deleted file's committed copy
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS", out)
        board_main(["--rebuild", "--root", str(r.root)])
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)
        self.assertEqual(board_main(["--check", "--root", str(r.root)]), 0)
        # the index lists only unfinished items (010/210), so the archive
        # section shows as one finished row; its items stay in their files
        self.assertIn("roadmap/990-done-before-the-split/README.md",
                      r.read("docs/ROADMAP.md"))
        self.assertTrue(any(p.name.startswith("0010-") for p in
                            (r.root / "docs/roadmap/990-done-before-the-split")
                            .iterdir()))

    def test_links_repointed_both_sides_and_anchors(self):
        r = make_repo(self.tmp)
        run(["--cut", "--root", str(r.root)])
        item = r.read("docs/roadmap/010-live/010-open-thing.md")
        self.assertIn("[`../990-done-before-the-split/README.md`]"
                      "(../990-done-before-the-split/README.md)", item)
        # an anchor the README carries is kept; one it does not is dropped
        self.assertIn("(../990-done-before-the-split/README.md#done-early)", item)
        self.assertIn("[a gone one](../990-done-before-the-split/README.md)", item)
        rec = r.read("docs/sessions/2026-02-01-0900-newest.md")
        self.assertIn("[`docs/roadmap/990-done-before-the-split/README.md`]"
                      "(../roadmap/990-done-before-the-split/README.md)", rec)
        self.assertIn("[archive]: ../roadmap/990-done-before-the-split/README.md",
                      rec)
        self.assertNotIn("ROADMAP-DONE.md)", rec)

    def test_verify_catches_a_changed_item(self):
        r = make_repo(self.tmp)
        run(["--cut", "--root", str(r.root)])
        name = sorted(p.name for p in (r.root / SECTION).glob("0010-*.md"))[0]
        r.write(SECTION / name, r.read(SECTION / name).replace("First", "Fist"))
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("FAIL", out)

    def assert_fallback(self, done: str, reason: str, extra=None):
        r = make_repo(self.tmp, done=done, extra=extra)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("route: (b) moved whole", out)
        self.assertIn(reason, out)
        frozen = r.root / SECTION / "frozen" / "ROADMAP-DONE.md"
        self.assertTrue(frozen.is_file())
        self.assertFalse((r.root / "docs/ROADMAP-DONE.md").exists())
        status = git(r.root, "status", "--porcelain").stdout
        # a rename in the index, so `git log --follow` keeps the history
        self.assertRegex(status, r"(?m)^R. docs/ROADMAP-DONE\.md -> "
                                 r"docs/roadmap/990-done-before-the-split/"
                                 r"frozen/ROADMAP-DONE\.md$")
        self.assertIn("frozen/ROADMAP-DONE.md", r.read(SECTION / "README.md"))
        board_main(["--rebuild", "--root", str(r.root)])
        self.assertEqual(board_main(["--check", "--root", str(r.root)]), 0)
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        return r

    def test_fallback_when_a_line_looks_like_the_cuts_link_line(self):
        self.assert_fallback(
            DONE + "- ✅ [0010-x](0010-x.md)\n",
            "FAIL  no source line is shaped like the cut's link line",
            extra={"docs/0010-x.md": "# x\n"})

    def test_fallback_when_there_are_no_entries(self):
        self.assert_fallback("# done\n\n- a bullet, not a checkbox\n"
                             "  see [`reviews/one.md`](reviews/one.md)\n",
                             "FAIL  0 `[x]` entries found")

    def test_fallback_when_a_reference_link_loses_its_definition(self):
        self.assert_fallback(
            DONE + "\n- [x] **Uses a label** — see [the review][rev].\n\n"
                   "[rev]: reviews/one.md\n",
            "FAIL  no reference-style link is cut away")

    def test_blocked_when_990_is_taken(self):
        r = make_repo(self.tmp)
        r.write("docs/roadmap/990-something-else/README.md", "# x\n")
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("section number 990 is already used", out)
        self.assertTrue((r.root / "docs/ROADMAP-DONE.md").exists())


class Primitives(unittest.TestCase):
    def test_split_lines_keeps_form_feed_inside_a_line(self):
        self.assertEqual(archivecut.split_lines("a\x0cb\nc"), ["a\x0cb\n", "c"])

    def test_segment_takes_blank_then_indented_into_the_entry(self):
        blocks = archivecut.segment("- [x] a\n  b\n\n  c\n\nd\n",
                                    archivecut.ENTRY_RE)
        self.assertEqual(blocks, [("entry", ["- [x] a\n", "  b\n", "\n", "  c\n"]),
                                  ("text", ["\n", "d\n"])])

    def test_fenced_link_is_not_rewritten(self):
        text = "```\n[x](ROADMAP-DONE.md)\n```\n[y](ROADMAP-DONE.md)\n"
        out, edits = archivecut.rewrite_links(
            text, lambda d: "NEW" if d == "ROADMAP-DONE.md" else None)
        self.assertEqual(out, "```\n[x](ROADMAP-DONE.md)\n```\n[y](NEW)\n")
        self.assertEqual(len(edits), 1)


class SessionCut(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_cut_detail_files_index_block_and_proof(self):
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("sessions: docs/SESSIONS-ARCHIVE.md — route: (a)", out)
        self.assertNotIn("FAIL", out)
        self.assertFalse((r.root / "docs/SESSIONS-ARCHIVE.md").exists())
        names = sorted(p.name for p in (r.root / "docs/sessions").glob("*archived*"))
        self.assertEqual(names, [
            "2026-01-02-archived-000-demo-session-log-archive.md",
            "2026-01-02-archived-001-2026-01-02-first-session.md",
            "2026-01-04-archived-002-2026-01-04-third-session.md"])
        first = r.read("docs/sessions/" + names[1])
        self.assertIn("](../decisions/0001.md)", first)
        index = r.read("docs/SESSIONS.md")
        # the block sits before the first existing entry, oldest first
        self.assertLess(index.index(archivecut.BEGIN),
                        index.index("2026-02-01 · newest"))
        self.assertIn("- [2026-01-03 · second](sessions/2026-01-03-01-second.md)"
                      " — already an\n  index line, kept as it stands.\n", index)
        self.assertIn("(sessions/" + names[2] + ") — archived entry", index)
        # the index's own link to the archive moved to the index itself
        self.assertIn("Older entries: [`SESSIONS.md`](SESSIONS.md).", index)
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  docs/SESSIONS-ARCHIVE.md", out)
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)

    def test_fallback_when_an_entry_has_no_date(self):
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE
                      + "\n- **an undated entry**: no date anywhere.\n")
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("route: (b) moved whole", out)
        self.assertTrue((r.root / "docs/sessions/SESSIONS-ARCHIVE.md").is_file())
        self.assertIn("(sessions/SESSIONS-ARCHIVE.md)", r.read("docs/SESSIONS.md"))
        moved = r.read("docs/sessions/SESSIONS-ARCHIVE.md")
        self.assertIn("](../decisions/0001.md)", moved)
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
