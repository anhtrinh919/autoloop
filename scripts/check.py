#!/usr/bin/env python3
"""Fails when a skill names a missing file, or a hand-off points at no skill."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skills = {p.parent.name: p.read_text() for p in (root / "skills").glob("*/SKILL.md")}
assert set(skills) == {"start", "round"}, f"unexpected skills: {sorted(skills)}"

for name, text in skills.items():
    assert f"name: {name}\n" in text, f"{name}: frontmatter name is wrong"
    assert "${CLAUDE_PLUGIN_ROOT}" in text, f"{name}: does not name the plugin root"
    for rel in re.findall(r"`(\.\./\.\./[^`]+)`", text):
        assert (root / "skills" / name / rel).resolve().exists(), f"{name}: missing {rel}"
    for target in re.findall(r"`autoloop:(\w+)`", text):
        assert target in skills, f"{name}: hands off to unknown autoloop:{target}"

for rel in re.findall(r"`(\.\./\.\./[^`]+)`", (root / "loop.md").read_text()):
    assert (root / "skills/x" / rel).resolve().exists(), f"loop.md: missing {rel}"

hook = json.loads((root / "hooks/hooks.json").read_text())
assert hook["hooks"]["SessionStart"][0]["matcher"] == "compact"
assert (root / "hooks/resume-after-compact.sh").stat().st_mode & 0o111, "hook script not executable"
print("ok")
