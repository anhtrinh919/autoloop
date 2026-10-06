# autoloop

A light build loop. `loop.md` holds what every skill shares. Read it in full before editing any skill.

Writing style for every file under `skills/` and `templates/`, and for `loop.md`:

- 15 words a sentence. Plain, common words.
- State a rule once, in the one file that owns it. A rule every skill shares lives in `loop.md`.
- A skill keeps this order: frontmatter, title and one line on what it reads and writes, Rules, Resume, Steps, Hand-off.
- A step gets a gate only when its output can be wrong in a way that matters.
- Keep every rule that must bend per project flexible. Never fix a build order or a surface.

`.githooks/pre-commit` bumps the plugin version on commits that touch other files. Leave the version alone.

Run `python3 scripts/check.py` before every commit.
