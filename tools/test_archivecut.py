"""Tests for archivecut — the frozen pre-split archives, cut into their stores.

Board `010/220`. Every fixture is synthetic. Covers the board cut (item files,
the section README, the byte-for-byte proof from disk, the index rebuilding
over it), the fallback to a whole-file move when the proof fails (a line
shaped like the cut's own link line, an archive with no `[x]` entries, a
reference-style link cut away from its definition), link re-pointing on both
sides of `](` and in reference definitions, anchors kept or dropped, a
same-page anchor inside an entry, `--plan` writing nothing, and (`010/270`)
the session log's retirement into `docs/sessions/`: index lines placed in the
files they link, new dated files for the rest, the README, the proof from
disk, the refusals that write nothing, and an archive cut by the earlier
route still verifying after the index goes. Stdlib only.
"""

import contextlib
import io
import re
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
import wrapscan  # noqa: E402

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


class SessionRetire(unittest.TestCase):
    """`010/270`: the one-file session log (the index, and a frozen archive
    where one is left) retires into `docs/sessions/`, files only."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_retires_index_and_archive_into_files_with_proof(self):
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE)
        second_before = r.read("docs/sessions/2026-01-03-01-second.md")
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("route: retired into the session folder", out)
        self.assertNotIn("FAIL", out)
        self.assertFalse((r.root / "docs/SESSIONS.md").exists())
        self.assertFalse((r.root / "docs/SESSIONS-ARCHIVE.md").exists())
        # an index line goes into the file it links, after its heading
        second = r.read("docs/sessions/2026-01-03-01-second.md")
        self.assertTrue(second.startswith(
            "# second\n\n" + archivecut.LOG_LABEL + "\n\n"
            "<!-- archivecut:log-entry docs/SESSIONS-ARCHIVE.md 8+2 -->\n"
            "- [2026-01-03 · second](2026-01-03-01-second.md) — already an\n"
            "  index line, kept as it stands.\n\n"), second)
        self.assertEqual(archivecut.without_entries(second), second_before)
        newest = r.read("docs/sessions/2026-02-01-0900-newest.md")
        self.assertIn("- [2026-02-01 · newest](2026-02-01-0900-newest.md)"
                      " — the tail.\n", newest)
        # an entry that links no session file gets a new file for its date;
        # it states no time, so its name carries a day counter
        made = r.read("docs/sessions/"
                      "2026-01-02-01-first-session-built-the-thing-see.md")
        self.assertIn("[`decisions/0001.md`](../decisions/0001.md)", made)
        self.assertTrue(made.startswith(archivecut.LOG_LABEL))
        self.assertTrue((r.root / "docs/sessions/"
                         "2026-01-04-01-third-session-more-work.md").is_file())
        # the preambles go to the README, fenced, word for word
        readme = r.read("docs/sessions/README.md")
        self.assertIn("Verbatim older entries rotated out of [`SESSIONS.md`]"
                      "(SESSIONS.md).", readme)
        self.assertLess(readme.index("`docs/SESSIONS-ARCHIVE.md`, retired"),
                        readme.index("`docs/SESSIONS.md`, retired"))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  docs/SESSIONS.md", out)
        self.assertIn("PASS  docs/SESSIONS-ARCHIVE.md", out)
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)

    def test_plan_writes_nothing(self):
        r = make_repo(self.tmp, done=None)
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  docs/SESSIONS.md: the README and the session files", out)
        self.assertEqual(git(r.root, "status", "--porcelain").stdout, "")

    def test_verify_catches_a_changed_entry(self):
        r = make_repo(self.tmp, done=None)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        r.commit()
        p = "docs/sessions/2026-02-01-0900-newest.md"
        r.write(p, r.read(p).replace("the tail.", "the tale."))
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("FAIL  docs/SESSIONS.md", out)

    def test_stated_time_names_the_new_file(self):
        r = make_repo(self.tmp, done=None, extra={"docs/SESSIONS.md": SESSIONS
                      + "- 2026-03-04 · 1415 UTC · a timed entry (no link)\n"
                      + "- **2026-03-05 · ~0730 UTC** (bold) — approximate\n"})
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertTrue((r.root / "docs/sessions/"
                         "2026-03-04-1415-a-timed-entry-no-link.md").is_file())
        self.assertTrue((r.root / "docs/sessions/"
                         "2026-03-05-0730-bold-approximate.md").is_file())

    def test_writes_nothing_when_an_entry_has_no_date(self):
        r = make_repo(self.tmp, done=None, extra={"docs/SESSIONS.md": SESSIONS
                      + "- **an undated entry**: no date anywhere.\n"})
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("FAIL  every entry that links no session file carries "
                      "a date", out)
        self.assertTrue((r.root / "docs/SESSIONS.md").is_file())
        self.assertFalse((r.root / "docs/sessions/README.md").exists())
        self.assertEqual(git(r.root, "status", "--porcelain").stdout, "")

    def test_writes_nothing_on_a_same_page_anchor_or_self_link(self):
        for extra in ("- 2026-03-04 · see [above](#top)\n",
                      "- 2026-03-04 · see [the log](SESSIONS.md)\n"):
            with self.subTest(extra=extra):
                tmp = tempfile.TemporaryDirectory()
                self.addCleanup(tmp.cleanup)
                r = make_repo(Path(tmp.name), done=None,
                              extra={"docs/SESSIONS.md": SESSIONS + extra})
                code, out = run(["--cut", "--root", str(r.root)])
                self.assertEqual(code, 1, out)
                self.assertIn("FAIL  every link in an entry still has a "
                              "target", out)
                self.assertTrue((r.root / "docs/SESSIONS.md").is_file())

    def test_an_existing_readme_is_kept_above_the_tools_part(self):
        r = make_repo(self.tmp, done=None, extra={
            "docs/sessions/README.md": "# mine\n\nThe index is "
                                       "[`../SESSIONS.md`](../SESSIONS.md).\n"})
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("docs/sessions/README.md already exists", out)
        readme = r.read("docs/sessions/README.md")
        self.assertTrue(readme.startswith("# mine\n\nThe index is "), readme)
        self.assertIn("\n\n" + archivecut.INTRO_MARK + "\n", readme)
        self.assertNotIn("# Session records", readme)
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)

    def test_entry_linking_its_file_on_a_later_line_is_placed_there(self):
        r = make_repo(self.tmp, done=None, extra={"docs/SESSIONS.md": SESSIONS
                      + "- 2026-02-01 — the same session, linked later:\n"
                        "  [detail](sessions/2026-02-01-0900-newest.md)\n"})
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        newest = r.read("docs/sessions/2026-02-01-0900-newest.md")
        self.assertIn("  [detail](2026-02-01-0900-newest.md)\n", newest)
        self.assertEqual(
            [p.name for p in (r.root / "docs/sessions").glob("2026-02-01-*")],
            ["2026-02-01-0900-newest.md"])

    def test_non_canonical_link_maps_back(self):
        r = make_repo(self.tmp, done=None, extra={"docs/SESSIONS.md": SESSIONS
                      + "- [2026-03-04 · x](../docs/ROADMAP.md) — and "
                        "[a tool](../tools/t.py)\n"})
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        names = [p.name for p in (r.root / "docs/sessions").glob("2026-03-04-*")]
        self.assertEqual(len(names), 1)
        text = r.read("docs/sessions/" + names[0])
        self.assertIn("(../../docs/ROADMAP.md)", text)
        self.assertIn("(../../tools/t.py)", text)
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)

    def test_no_final_newline_rebuilds(self):
        r = make_repo(self.tmp, done=None, extra={
            "docs/SESSIONS.md": SESSIONS + "- 2026-03-04 · last, no newline"})
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn(" nl=no ", r.read("docs/sessions/README.md"))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)

    def test_an_archive_cut_before_010_270_still_verifies(self):
        """The old route left an index block in `SESSIONS.md` and
        `-archived-` detail files; retiring the index places the block's
        lines in those files, and both logs still rebuild."""
        archive = ("# arch\n\nSee [`SESSIONS.md`](SESSIONS.md).\n\n"
                   "- **2026-01-02 (one)**: did a thing.\n")
        r = make_repo(self.tmp, done=None, sessions_archive=archive)
        pre = "2026-01-02-archived-000-arch.md"
        one = "2026-01-02-archived-001-2026-01-02-one.md"
        git(r.root, "rm", "-q", "docs/SESSIONS-ARCHIVE.md")
        r.write("docs/sessions/" + pre,
                "# arch\n\nSee [`SESSIONS.md`](../SESSIONS.md).\n\n")
        r.write("docs/sessions/" + one, "- **2026-01-02 (one)**: did a thing.\n")
        block = (archivecut.BEGIN + "\n"
                 f"- [2026-01-02 · arch](sessions/{pre}) — archived preamble,"
                 " verbatim in its file\n"
                 f"- [2026-01-02 · 2026-01-02 (one)](sessions/{one}) — archived"
                 " entry, verbatim in its file\n" + archivecut.END + "\n")
        index = r.read("docs/SESSIONS.md").replace(
            "Older entries: [`SESSIONS-ARCHIVE.md`](SESSIONS-ARCHIVE.md).\n\n", "")
        r.write("docs/SESSIONS.md",
                index.replace("- [2026-02-01", block + "- [2026-02-01"))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  docs/SESSIONS.md", out)
        self.assertIn("PASS  docs/SESSIONS-ARCHIVE.md: 2 detail files", out)


class PlaceEntries(unittest.TestCase):
    def test_insert_strip_round_trip(self):
        ent = [("docs/SESSIONS.md", 3, 1, "- [x](y.md) — z\n")]
        for original in (None, "", "# T\n", "# T\n\nbody\n", "no heading\n",
                         "# T no newline", "body without newline"):
            with self.subTest(original=original):
                text = archivecut.insert_entries(original, ent)
                got = archivecut.strip_entries(text)
                self.assertIsInstance(got, tuple)
                self.assertEqual(got[0], original)
                self.assertEqual(got[1], ent)

    def test_untouched_file_reads_as_not_present(self):
        self.assertIs(archivecut.strip_entries("# T\n\nbody\n"),
                      archivecut.NOT_PRESENT)

    def test_entry_date_time(self):
        f = archivecut.entry_date_time
        self.assertEqual(f("- [2026-07-20 · ~1945 UTC · x](y)"),
                         ("2026-07-20", "1945"))
        self.assertEqual(f("- **2026-11-09 · 1242 UTC** (x)"),
                         ("2026-11-09", "1242"))
        self.assertEqual(f("- [2026-07-18 · 13:50 · Opus"), ("2026-07-18", "1350"))
        self.assertEqual(f("- [2026-07-14 · cold review](x)"), ("2026-07-14", None))
        self.assertEqual(f("- 2026-07-10 · 1157→234 lines"), ("2026-07-10", None))
        self.assertEqual(f("- no date"), (None, None))


ROOT_DONE = """\
# demo ROADMAP — completed detail (archive)

## Cycles
- [x] **First cycle closed** — see [`docs/reviews/one.md`](docs/reviews/one.md).
- [x] **Second cycle closed** — and [`ROADMAP-DONE.md`](ROADMAP-DONE.md) itself.
"""


class FieldEdges(unittest.TestCase):
    """010/280, `archivecut` in the field: items 1 and 3, and the label line
    of item 2's 2026-11-20 form (item 4 is `board.py`'s, in test_board)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    # -- item 1: report the lines a re-pointed link pushed past the limit

    LONG = ("See [the archive](ROADMAP-DONE.md) for the work done earlier "
            "and for what it was for.\n")

    def test_a_line_the_repointing_lengthens_past_the_limit_is_reported(self):
        r = make_repo(self.tmp)
        self.assertLessEqual(len(self.LONG.rstrip("\n")), wrapscan.LINE_LIMIT)
        r.write("docs/notes.md", "# notes\n\n" + self.LONG)
        r.commit()
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertRegex(out, r"WRAP  1 line\(s\) a re-pointed link pushed past 85")
        self.assertRegex(out, r"docs/notes\.md:3 \(\d+ columns\)")
        # after the cut the file really is over, which is what was reported
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        found = wrapscan.scan_text("docs/notes.md", r.read("docs/notes.md"))
        self.assertEqual([3], [f.line for f in found])
        # the tool wrote the lengthened line as it was: prose is never re-wrapped
        self.assertIn("(roadmap/990-done-before-the-split/README.md) for the work",
                      r.read("docs/notes.md"))

    def test_a_short_line_and_a_line_already_over_are_not_reported(self):
        r = make_repo(self.tmp)
        already = ("This line was already over the house limit before any link "
                   "moved, with words [a](ROADMAP-DONE.md) after it.\n")
        r.write("docs/notes.md", "# notes\n\n" + already)
        r.commit()
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("WRAP", out)

    def test_an_exempt_file_is_not_reported(self):
        r = make_repo(self.tmp)
        r.write("docs/notes.md", "# notes\n\n" + self.LONG)
        r.write(".wrapscanignore", "docs/notes.md # fixture: exempt on purpose\n")
        r.commit()
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("WRAP", out)

    # -- item 1, residue: the session files the retirement places entries in

    @staticmethod
    def _padded_entry(width: int) -> str:
        """A log entry whose first line is `width` columns before its link is
        re-pointed one level down (which adds three: `../`). At 85 it fits the
        limit as written and is 88 once placed."""
        head = "- **2026-01-02 (first)**: see [adr](decisions/0001.md) and "
        # short words, not one long token: wrapscan lets a lone token through
        pad = ("ab " * 60)[:width - len(head)].rstrip() \
            .ljust(width - len(head), "b")
        line = head + pad
        assert len(line) == width
        return line + "\n"

    def test_a_placed_session_entry_lengthened_past_the_limit_is_reported(self):
        r = make_repo(self.tmp, done=None, extra={
            "docs/SESSIONS.md": SESSIONS + "\n" + self._padded_entry(85)})
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertRegex(out, r"WRAP  1 line\(s\) a re-pointed link pushed past 85")
        self.assertRegex(
            out, r"docs/sessions/2026-01-02-01-first-see[^:\s]*\.md:\d+ "
                 r"\(88 columns\)")
        # the line it names is the line wrapscan reads in the written file
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        made = next((r.root / "docs/sessions").glob("2026-01-02-01-*.md"))
        found = wrapscan.scan_text(made.name, made.read_text(encoding="utf-8"))
        self.assertEqual([88], [f.length for f in found])

    def test_session_entries_not_lengthened_or_exempt_are_not_reported(self):
        # 82 columns stays inside 85 after the three added; 90 was already over
        for width in (82, 90):
            with self.subTest(width=width):
                with tempfile.TemporaryDirectory() as d:
                    r = make_repo(Path(d), done=None, extra={
                        "docs/SESSIONS.md":
                            SESSIONS + "\n" + self._padded_entry(width)})
                    code, out = run(["--plan", "--root", str(r.root)])
                    self.assertEqual(code, 0, out)
                    self.assertNotIn("WRAP", out)
        with tempfile.TemporaryDirectory() as d:
            r = make_repo(Path(d), done=None, extra={
                "docs/SESSIONS.md": SESSIONS + "\n" + self._padded_entry(85),
                ".wrapscanignore": "docs/sessions/** # fixture: exempt\n"})
            code, out = run(["--plan", "--root", str(r.root)])
            self.assertEqual(code, 0, out)
            self.assertNotIn("WRAP", out)

    # -- item 3: the pre-split archive at the repo root

    def root_repo(self) -> Repo:
        r = make_repo(self.tmp, done=None)
        r.write("ROADMAP-DONE.md", ROOT_DONE)
        r.write("docs/notes.md", "# notes\n\nSee [old](../ROADMAP-DONE.md).\n")
        r.commit()
        return r

    def test_an_archive_at_the_repo_root_is_found_and_cut(self):
        r = self.root_repo()
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("board: ROADMAP-DONE.md — route: (a) cut into the store", out)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("FAIL", out)
        self.assertFalse((r.root / "ROADMAP-DONE.md").exists())
        items = sorted(p.name for p in (r.root / SECTION).glob("*.md")
                       if p.name != "README.md")
        self.assertEqual(2, len(items))
        self.assertIn("](../../reviews/one.md)", r.read(SECTION / items[0]))
        # a link to the archive from elsewhere in the tree follows it
        self.assertIn("(roadmap/990-done-before-the-split/README.md)",
                      r.read("docs/notes.md"))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  ROADMAP-DONE.md: 2 item files", out)
        board_main(["--rebuild", "--root", str(r.root)])
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)

    def test_the_docs_archive_wins_when_both_exist_and_the_root_one_is_left(self):
        r = make_repo(self.tmp)
        r.write("ROADMAP-DONE.md", ROOT_DONE)
        r.commit()
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("board: docs/ROADMAP-DONE.md — route: (a)", out)
        self.assertIn("reason: ROADMAP-DONE.md also exists and is left alone", out)
        self.assertTrue((r.root / "ROADMAP-DONE.md").is_file())
        self.assertFalse((r.root / "docs/ROADMAP-DONE.md").exists())

    def test_no_archive_anywhere_is_still_nothing_to_do(self):
        r = make_repo(self.tmp, done=None)
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("board: docs/ROADMAP-DONE.md — route: nothing to do", out)

    def test_a_root_archive_that_cannot_cut_moves_whole(self):
        r = make_repo(self.tmp, done=None)
        r.write("ROADMAP-DONE.md", "# done\n\n- a bullet, not a checkbox\n"
                "  see [`docs/reviews/one.md`](docs/reviews/one.md)\n")
        r.commit()
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("route: (b) moved whole", out)
        self.assertTrue((r.root / SECTION / "frozen/ROADMAP-DONE.md").is_file())
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  ROADMAP-DONE.md: route (b)", out)

    # -- item 2 (2026-11-20 form): the label line fits the limit

    def test_the_label_line_fits_the_house_limit(self):
        self.assertLessEqual(len(archivecut.LOG_LABEL), wrapscan.LINE_LIMIT)
        for old in archivecut.LEGACY_LOG_LABELS:
            self.assertGreater(len(old), wrapscan.LINE_LIMIT)

    def test_no_session_file_the_cut_writes_has_a_line_over_the_limit(self):
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        # The README's marker comments are held to the limit too (below).
        for p in sorted((r.root / "docs/sessions").glob("2*.md")):
            for f in wrapscan.scan_text(p.name, p.read_text(encoding="utf-8")):
                self.fail(f"{p.name}:{f.line} is {f.length} columns")

    def test_a_file_cut_under_the_old_label_still_reads_and_verifies(self):
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE)
        ent = [("docs/SESSIONS.md", 3, 1, "- [x](y.md) — z\n")]
        old = archivecut.LEGACY_LOG_LABELS[0]
        text = archivecut.insert_entries("# T\n\nbody\n", ent, old)
        got = archivecut.strip_entries(text)
        self.assertEqual(("# T\n\nbody\n", ent), got)
        # a whole cut, its label then rewritten to the shipped-first wording
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        for p in (r.root / "docs/sessions").glob("*.md"):
            t = p.read_text(encoding="utf-8")
            if archivecut.LOG_LABEL in t:
                p.write_text(t.replace(archivecut.LOG_LABEL, old), encoding="utf-8")
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("FAIL", out)

    # -- item 2 (2026-11-23 form): the README's marker comment fits the limit

    def test_the_retired_marker_comment_fits_the_house_limit(self):
        # Fails on the old `final-newline=` spelling: 92 columns for the
        # `-ARCHIVE` log with a short sha.
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        marks = [x for x in r.read("docs/sessions/README.md").splitlines()
                 if archivecut.RETIRED_RE.match(x)]
        self.assertGreaterEqual(len(marks), 1)
        for x in marks:
            self.assertLessEqual(len(x), wrapscan.LINE_LIMIT, x)
        worst = archivecut.RETIRED_MARK.format(
            src=archivecut.SESSIONS_SRC, lines=99999, nl="yes", sha="a" * 8)
        self.assertLessEqual(len(worst), wrapscan.LINE_LIMIT, worst)

    def test_a_readme_cut_under_the_old_marker_still_reads_and_verifies(self):
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        path = r.root / "docs/sessions/README.md"
        t = path.read_text(encoding="utf-8")
        old = re.sub(r" nl=(yes|no) ", r" final-newline=\1 ", t)
        self.assertNotEqual(old, t)
        path.write_text(old, encoding="utf-8")
        self.assertIsNotNone(archivecut.parse_readme(old))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("FAIL", out)


ROOT_SESSIONS = """\
# demo session log (kept at the repo root)

Older entries: [`SESSIONS-ARCHIVE.md`](SESSIONS-ARCHIVE.md).

---

- [2026-02-01 · newest](docs/sessions/2026-02-01-0900-newest.md) — the tail;
  see [`docs/decisions/0001.md`](docs/decisions/0001.md).
"""

ROOT_ARCHIVE = """\
# demo session log — archive

Verbatim older entries rotated out of [`SESSIONS.md`](SESSIONS.md).

- **2026-01-02 (first session)**: built the thing; see
  [`README.md`](README.md) and [`tools/t.py`](tools/t.py).

- [2026-01-03 · second](docs/sessions/2026-01-03-01-second.md) — already an
  index line, kept as it stands.
"""


class RootSessionLogs(unittest.TestCase):
    """010/280, the last residue of item 3: a session log kept at the repo
    root (SESSIONS.md, SESSIONS-ARCHIVE.md) is found as the board archive is.
    `docs/` wins per log when both exist, and the other is named and left."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def root_repo(self, archive=True, index=True, docs_index=False) -> Repo:
        r = make_repo(self.tmp, done=None)
        if not docs_index:
            git(r.root, "rm", "-q", "--", "docs/SESSIONS.md")
        r.write("README.md", "# demo\n")
        if index:
            r.write("SESSIONS.md", ROOT_SESSIONS)
        if archive:
            r.write("SESSIONS-ARCHIVE.md", ROOT_ARCHIVE)
        r.write("docs/notes.md", "# notes\n\nSee [log](../SESSIONS.md) and "
                "[older](../SESSIONS-ARCHIVE.md).\n")
        r.commit()
        return r

    def test_a_root_log_is_found_retired_and_verifies_byte_for_byte(self):
        r = self.root_repo()
        code, out = run(["--plan", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("sessions: SESSIONS-ARCHIVE.md + SESSIONS.md — route: "
                      "retired into the session folder", out)
        self.assertEqual(git(r.root, "status", "--porcelain").stdout, "")
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("FAIL", out)
        self.assertFalse((r.root / "SESSIONS.md").exists())
        self.assertFalse((r.root / "SESSIONS-ARCHIVE.md").exists())
        # a placed entry: links re-pointed for the folder, from the root
        newest = r.read("docs/sessions/2026-02-01-0900-newest.md")
        self.assertIn("<!-- archivecut:log-entry SESSIONS.md 7+2 -->", newest)
        self.assertIn("- [2026-02-01 · newest](2026-02-01-0900-newest.md)"
                      " — the tail;\n  see [`docs/decisions/0001.md`]"
                      "(../../docs/decisions/0001.md).\n", newest)
        # an entry linking no session file gets a new dated file
        made = list((r.root / "docs/sessions").glob("2026-01-02-*.md"))
        self.assertEqual(1, len(made))
        body = made[0].read_text(encoding="utf-8")
        self.assertIn("[`README.md`](../../README.md)", body)
        self.assertIn("[`tools/t.py`](../../tools/t.py)", body)
        second = r.read("docs/sessions/2026-01-03-01-second.md")
        self.assertIn("(2026-01-03-01-second.md) — already an", second)
        readme = r.read("docs/sessions/README.md")
        self.assertIn("`SESSIONS-ARCHIVE.md`, retired", readme)
        self.assertIn("`SESSIONS.md`, retired", readme)
        # links to the retired logs elsewhere in the tree follow them
        notes = r.read("docs/notes.md")
        self.assertIn("(sessions/README.md)", notes)
        self.assertNotIn("SESSIONS", notes.replace("sessions/README.md", ""))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  SESSIONS.md: the README and", out)
        self.assertIn("PASS  SESSIONS-ARCHIVE.md: the README and", out)
        self.assertNotIn("FAIL", out)
        ok, lout = linkscan_ok(r.root)
        self.assertTrue(ok, lout)

    def test_verify_catches_a_changed_root_entry(self):
        r = self.root_repo()
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        r.commit()
        p = "docs/sessions/2026-02-01-0900-newest.md"
        r.write(p, r.read(p).replace("the tail;", "the tale;"))
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("FAIL  SESSIONS.md", out)

    def test_verify_catches_a_link_changed_in_a_root_entry(self):
        r = self.root_repo()
        run(["--cut", "--root", str(r.root)])
        r.commit()
        made = next((r.root / "docs/sessions").glob("2026-01-02-*.md"))
        made.write_text(made.read_text(encoding="utf-8").replace(
            "(../../README.md)", "(../../tools/t.py)"), encoding="utf-8")
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("FAIL  SESSIONS-ARCHIVE.md", out)

    def test_docs_only_is_unchanged(self):
        r = make_repo(self.tmp, done=None, sessions_archive=SESSIONS_ARCHIVE)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("sessions: docs/SESSIONS-ARCHIVE.md + docs/SESSIONS.md "
                      "— route: retired", out)
        self.assertNotIn("left alone", out)
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  docs/SESSIONS.md", out)
        self.assertIn("PASS  docs/SESSIONS-ARCHIVE.md", out)

    def test_the_docs_log_wins_when_both_exist_and_the_root_one_is_left(self):
        r = self.root_repo(archive=False, docs_index=True)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("sessions: docs/SESSIONS.md — route: retired", out)
        self.assertIn("reason: SESSIONS.md also exists and is left alone; "
                      "retiring docs/SESSIONS.md", out)
        self.assertFalse((r.root / "docs/SESSIONS.md").exists())
        self.assertEqual(ROOT_SESSIONS, r.read("SESSIONS.md"))
        self.assertEqual("", git(r.root, "status", "--porcelain", "--",
                                 "SESSIONS.md").stdout)
        # the docs copy was retired: its entry is placed, the root one's is not
        self.assertIn("- [2026-02-01 · newest](2026-02-01-0900-newest.md)",
                      r.read("docs/sessions/2026-02-01-0900-newest.md"))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  docs/SESSIONS.md", out)
        self.assertNotIn("FAIL", out)

    def test_each_log_is_found_where_it_sits_when_they_sit_apart(self):
        # the archive at the root, the index in docs/
        r = self.root_repo(index=False, docs_index=True)
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("sessions: SESSIONS-ARCHIVE.md + docs/SESSIONS.md — "
                      "route: retired", out)
        self.assertNotIn("FAIL", out)
        readme = r.read("docs/sessions/README.md")
        self.assertLess(readme.index("`SESSIONS-ARCHIVE.md`, retired"),
                        readme.index("`docs/SESSIONS.md`, retired"))
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertIn("PASS  SESSIONS-ARCHIVE.md", out)
        self.assertIn("PASS  docs/SESSIONS.md", out)

    def test_an_entry_linking_the_root_log_itself_writes_nothing(self):
        r = self.root_repo(archive=False)
        r.write("SESSIONS.md", ROOT_SESSIONS + "\n- **2026-02-02 (x)**: see "
                "[the log](SESSIONS.md).\n")
        r.commit()
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("a link to the log itself", out)
        self.assertTrue((r.root / "SESSIONS.md").is_file())
        self.assertFalse((r.root / "docs/sessions/README.md").exists())

    def test_awkward_root_links_still_prove_and_verify(self):
        r = self.root_repo(archive=False)
        r.write("SESSIONS.md", ROOT_SESSIONS + "\n- **2026-02-02 (x)**: see "
                "[a](docs/sessions/../../README.md) and [b](docs/sessions/).\n")
        r.commit()
        code, out = run(["--cut", "--root", str(r.root)])
        self.assertEqual(code, 0, out)
        self.assertNotIn("FAIL", out)
        r.commit()
        code, out = run(["--verify", "--root", str(r.root)])
        self.assertEqual(code, 0, out)

    def test_the_link_maps_are_inverse_for_both_homes(self):
        for base in ("docs", ""):
            folder = "sessions" if base else "docs/sessions"
            for dest in (f"{folder}/x.md", f"{folder}/x.md#a", "a.md",
                         "a/b.md#c", "../up.md", f"{folder}/", f"{folder}/..",
                         f"{folder}/a/b.md", f"{folder}/../a.md"):
                errors: list[str] = []
                fwd = archivecut._entry_forward(dest, errors, base)
                self.assertEqual([], errors)
                self.assertEqual(dest, archivecut._entry_back(fwd, base),
                                 (base, dest))
        self.assertEqual(
            "x.md", archivecut._entry_forward("docs/sessions/x.md", [], ""))
        self.assertEqual("../../a.md", archivecut._entry_forward("a.md", [], ""))


if __name__ == "__main__":
    unittest.main()
