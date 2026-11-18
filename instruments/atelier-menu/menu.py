#!/usr/bin/env python3
"""atelier-menu -- print every /atelier: command the plugin ships, as a table.

Why (board 450/010 row 14): the principal pressed Enter on `/atelier` and on
`/atelier:` expecting the list of the plugin's commands. Claude Code's picker
shows that list only while the prefix is being typed, and a plugin's skills are
always `/<plugin>:<name>`, so no plugin skill can answer a bare `/atelier`. This
script is the body of a user-level skill named `atelier` (linked into
`~/.claude/skills/atelier` by `instruments/install`) that does.

The menu is read at run time from the plugin's own front matter -- every
`skills/*/SKILL.md` and `commands/*.md` -- never from a typed list, so a command
added to the plugin appears here with no edit.

  menu.py              the menu, as a Markdown table
  menu.py --root DIR   read the plugin at DIR (default: this file's repo)
  menu.py --selftest   prove it lists a fixture plugin and stays quiet on junk
"""
import argparse
import os
import re
import sys
import tempfile

PREFIX = "atelier"
FIRST_SENTENCE = re.compile(r"^(.+?[.!?])(\s|$)")


def front_matter(path):
    """Return the YAML front matter of a Markdown file as a flat dict.

    Only `key: value` lines are read; that is all the plugin's files use, and a
    full YAML parser would be a dependency for nothing."""
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    out = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def short(desc):
    """The description's lead clause, so the table stays one line a row: the
    text before the first spaced dash, else its first sentence."""
    desc = " ".join(desc.split()).split(" — ")[0]
    m = FIRST_SENTENCE.match(desc)
    return m.group(1) if m else desc


def entries(root):
    rows = []
    skills = os.path.join(root, "skills")
    if os.path.isdir(skills):
        for name in sorted(os.listdir(skills)):
            fm = front_matter(os.path.join(skills, name, "SKILL.md"))
            if fm:
                rows.append((fm.get("name") or name, short(fm.get("description", ""))))
    commands = os.path.join(root, "commands")
    if os.path.isdir(commands):
        for fn in sorted(os.listdir(commands)):
            if fn.endswith(".md"):
                fm = front_matter(os.path.join(commands, fn))
                rows.append((fn[:-3], short(fm.get("description", ""))))
    return sorted(rows)


def render(rows):
    if not rows:
        return "No /atelier: commands found -- is the plugin checkout where this skill points?\n"
    lines = ["| Command | What it does |", "|---|---|"]
    for name, desc in rows:
        lines.append(f"| `/{PREFIX}:{name}` | {desc.replace('|', '/')} |")
    lines.append("")
    lines.append(f"To run one, type `/{PREFIX}:` and pick from the list before pressing Enter.")
    return "\n".join(lines) + "\n"


def default_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def selftest():
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "skills", "alpha"))
        os.makedirs(os.path.join(d, "skills", "broken"))
        os.makedirs(os.path.join(d, "commands"))
        with open(os.path.join(d, "skills", "alpha", "SKILL.md"), "w") as f:
            f.write("---\nname: alpha\ndescription: Does A — in detail. Then more.\n---\nbody\n")
        with open(os.path.join(d, "skills", "broken", "SKILL.md"), "w") as f:
            f.write("no front matter\n")
        with open(os.path.join(d, "commands", "beta.md"), "w") as f:
            f.write('---\ndescription: "Does B | safely."\n---\n')
        rows = entries(d)
        assert rows == [("alpha", "Does A"), ("beta", "Does B | safely.")], rows
        out = render(rows)
        assert "`/atelier:alpha` | Does A |" in out, out
        assert "Does B / safely." in out, out
        assert "broken" not in out, out
        assert "No /atelier: commands" in render([])
    print("✓ atelier-menu selftest: lists a fixture plugin, skips a file with no front matter")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Print every /atelier: command as a table.")
    ap.add_argument("--root", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    sys.stdout.write(render(entries(a.root or default_root())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
