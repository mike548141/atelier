"""Every /atelier: command is subject, space, action (board 450/020).

The principal, 2026-11-24, verbatim: "I think a space and for the default it
could have a menu or help screen a little like what /atelier does by itself.
We should make all the atelier command like this so its consistent". And:
"So something like /atelier:review by itself would be a help screen, not run
a command by default".

So the plugin ships one skill per subject (`skills/<subject>/SKILL.md`, a
router) and one file per action beside it (`skills/<subject>/<action>.md`,
front matter `action:`). These tests keep the router's table, the action
files and the router's description in step, keep the bare-subject menu wired,
and keep the retired hyphen names (his pick for them, "Nothing": no
forwarder, no signpost) out of the live surfaces.
"""
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MENU = ROOT / "instruments" / "atelier-menu" / "menu.py"

RETIRED = ("review-brief", "review-drain", "review-plan", "work-run", "work-plan",
           "queue-run", "queue-plan", "fleet-sweep", "fleet-pins", "install-hook",
           "create-repo", "session-onramp", "scan")

# Live surfaces: what a reader is told to run or where a thing lives now.
# Records (sessions, reviews, decisions, board items, census, changelog) keep
# the names they were written with.
LIVE = ["README.md", "CLAUDE.md", "skills", "instruments", "tools",
        "docs/build", "docs/method", ".claude-plugin"]
RECORDS = ("docs/method/census/",)


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    out = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"')
    return out


def subjects():
    return sorted(d for d in SKILLS.iterdir() if (d / "SKILL.md").is_file())


def action_files(d: Path):
    return {p.stem: p for p in sorted(d.glob("*.md"))
            if p.name != "SKILL.md" and front_matter(p).get("action")}


def unquoted(text: str) -> str:
    """The text with the principal's quoted words removed: an italic quote
    (*"..."*) keeps the names he used, verbatim, and is not a live use."""
    return re.sub(r'\*"[^"]*"\*', "", text, flags=re.S)


class SubjectSkills(unittest.TestCase):
    def test_the_six_subjects(self):
        self.assertEqual([d.name for d in subjects()],
                         ["fleet", "repo", "review", "session", "work", "worktree"])

    def test_no_commands_directory(self):
        self.assertFalse((ROOT / "commands").exists(),
                         "commands/ is retired: each command is a subject's action")

    def test_every_skill_dir_is_a_subject(self):
        for d in SKILLS.iterdir():
            if d.is_dir():
                self.assertTrue((d / "SKILL.md").is_file(), f"{d} has no router")
                self.assertTrue(action_files(d), f"{d.name} has no action files")

    def test_router_front_matter(self):
        for d in subjects():
            fm = front_matter(d / "SKILL.md")
            self.assertEqual(fm.get("name"), d.name)
            desc = fm.get("description", "")
            self.assertLessEqual(len(desc), 1024, f"{d.name}: description too long")
            self.assertIn("Pass the action as the first argument", desc)
            self.assertIn(f"bare /atelier:{d.name} shows this menu", desc)

    def test_description_carries_every_action(self):
        """One description does the work of several, so it must carry every
        action's word, or a request for that action never finds the skill."""
        for d in subjects():
            desc = front_matter(d / "SKILL.md")["description"]
            for a in action_files(d):
                self.assertRegex(desc, rf"\b{re.escape(a)}\b", f"{d.name}: {a}")

    def test_action_names_match_files(self):
        for d in subjects():
            for stem, p in action_files(d).items():
                self.assertEqual(front_matter(p)["action"], stem, str(p))
                self.assertTrue(front_matter(p).get("description"), str(p))
                self.assertNotIn("name", front_matter(p),
                                 f"{p}: an action file is not a skill; no name:")

    def test_router_table_matches_action_files(self):
        for d in subjects():
            body = (d / "SKILL.md").read_text(encoding="utf-8")
            rows = re.findall(r"^\| `([a-z]+)` \| \[`([a-z]+)\.md`\]", body, re.M)
            self.assertEqual(sorted(a for a, _ in rows), sorted(action_files(d)), d.name)
            for a, f in rows:
                self.assertEqual(a, f, d.name)
            self.assertEqual(front_matter(d / "SKILL.md")["argument-hint"],
                             " | ".join(a for a, _ in rows))

    def test_bare_subject_shows_its_menu(self):
        for d in subjects():
            body = (d / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(f"instruments/atelier-menu/menu.py\" {d.name}", body)
            self.assertIn("do\nnothing else", body)
            out = subprocess.run([sys.executable, str(MENU), "--root", str(ROOT), d.name],
                                 capture_output=True, text=True, timeout=30).stdout
            for a in action_files(d):
                self.assertIn(f"`/atelier:{d.name} {a}`", out)

    def test_retired_names_are_gone_from_live_surfaces(self):
        names = "|".join(re.escape(n) for n in RETIRED)
        # A user-level path (`~/.claude/skills/<name>`) is the adopter's own,
        # not the plugin's layout, so it is not a use of a retired name.
        rx = re.compile(rf"/atelier:(?:{names})\b|(?<!\.claude/)\b(?:skills|commands)/(?:{names})\b")
        files = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--", *LIVE],
                               capture_output=True, text=True).stdout.split()
        hits = []
        for f in files:
            if f.startswith(RECORDS) or f == "tools/test_subject_skills.py":
                continue
            p = ROOT / f
            if not p.is_file():
                continue
            try:
                text = unquoted(p.read_text(encoding="utf-8"))
            except UnicodeDecodeError:
                continue
            for n, line in enumerate(text.splitlines(), 1):
                if rx.search(line):
                    hits.append(f"{f}:{n}: {line.strip()[:100]}")
        self.assertEqual(hits, [], "retired command names in live files:\n" + "\n".join(hits))


if __name__ == "__main__":
    unittest.main()
