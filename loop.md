# loop.md

Every skill reads this first. It holds what every skill shares.

## The loop

A project is a run of rounds. Each round makes one piece real:

1. Pick — choose the piece, and what the user will try at the end.
2. Build — write it.
3. Check — run it for real.
4. Show — the user tries it, then keeps, adjusts, or drops it.
5. Record — update the docs, and merge the round.

The loop shape is fixed. Everything inside it bends to the round.

## Fixed and flexible

Fixed in every round:

- One goal the user can name.
- One thing the user tries at the end, chosen before building starts.
- Tests for every piece of code with logic.
- A real run before the user sees it.

A real run uses real input, through the product's real entry point. Test output alone is not one.

Flexible, decided per round:

- Build order. Screens, backend, tests, or agent — whichever the round needs first.
- What the user tries: screens, a command, test output, or a live agent run.
- How much checking the round needs, by its risk.

Never write a fixed order or a fixed surface into a project's docs.

## Code or agent

This section applies only when the product has its own AI agent.

Sort every ability into one of two kinds:

- Code — must give the same result every time. Storage, login, money, safety, the agent's tools.
- Agent — needs judgment. Reading, choosing, planning, asking, answering.

A tool does one action. It never runs a fixed chain of steps, or prompts a model to decide.

Code gives the agent hands, not a script.

- An agent ability is built from instructions and tools, never from coded steps.
- Before coding a choice, ask: could the agent make it, given a tool? Then write instructions.
- Code makes a choice only when a Hard rule in `brief.md` demands it.
- Only the user adds or changes a Hard rule. Ask each one as its own numbered question.
- A failed scenario is fixed in the instructions or tools first.
- Sample output shown in a screen is data only. Making it real never means coding its steps.

Each agent ability has scenarios in `brief.md`. A scenario is a real input, and what a good result looks like.

A live agent run uses the real model. A mocked or scripted model never counts. A missing key or account means ask the user.

## Docs

Three docs, all living. They always state the product as it is today.

- `brief.md` — what the product is, its hard rules, its agent abilities, and settled choices.
- `log.md` — the Next list of features in build order, and every round, newest first.
- `bug.md` — open bugs and small changes.

Follow `../../templates/brief.md`, `../../templates/log.md`, and `../../templates/bug.md`. Git history holds the rest.

Each Next item is a feature, and its own round. Split a big one when it is picked.

Write each Next item as two sentences:

- First — what it is, in 4 to 6 words.
- Second — a description or note. It can run longer.

Next is the build order. Its top item is the next round.

Number each Next item with the round it would be. That is the newest round's number, plus its place. Example: `- 38. The Windows app window. …`

Keep the numbers true after every change to Next or Rounds. Next items have no numbers? Add them.

The user names an item by its number. Read that number in `log.md`.

The user settles the order in chat? Rewrite Next and its numbers at once. Commit.

`bug.md` has two sections:

- Folded — bugs grouped under a feature in Next's top 5. That feature's round takes them.
- Loose — bugs with no such feature. They wait for a bug round.

Fold a bug when a top-5 feature touches its area. Otherwise it is loose.

Next's top 5 changes? Move the bugs of a feature that left it to Loose. Fold any Loose bug that fits a feature that joined it.

No `bug.md`, or no two sections? Create it from the template first. Move every bug or small change out of Next into it. Sort each one into Folded or Loose.

Before adding an item, look for it in Next and `bug.md`. Found it? Add the new note to it.

Add any item to Next or `bug.md` without asking. A round's Show step lists every item it added.

Resolve every `../../` path from the skill's `SKILL.md`, against `${CLAUDE_PLUGIN_ROOT}`.

Never create `prd.md`, `state.json`, `.build-state.json`, `spec/`, or `specs/` at the project root. Autobuild's tools claim those names.

Do not invent product limitations. Write a limit only when the user stated it or research proved it.

## Asking

Ask only decisions the user would notice. Decide plumbing yourself.

Number each question, with your recommended answer:

> ❓ **Q1** — **<title>**: <question>
>
> ➡️ <recommended answer>

End with one line: reply `ok` to accept every recommendation, or answer by number.

## Subagents

The main session builds. Spawn a subagent only for parallel work, research, or a blind check.

- Research and blind checks: Sonnet.
- A blind check on a round whose Risk is not none: Opus.

A blind subagent has no conversation history. It sees only what its check needs.

A named agent may be missing, such as `crawler` or `dogfood`. Use a general-purpose subagent with the same brief.

## Git

Each round runs on its own branch: `round-<n>-<slug>`.

- Keep — merge it into its base branch, push, and deploy. Keep is the user's OK for all three.
- Drop — require typed `drop`, then delete the branch.

Push and deploy follow `brief.md`'s How to ship. It is missing or empty? Ask the user once, then fill it.

Never push outside a keep, or add a remote, without the user's OK.
