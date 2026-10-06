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

Two docs, both living. They always state the product as it is today.

- `brief.md` — what the product is, its hard rules, its agent abilities, and settled choices.
- `log.md` — the Next list and every round, newest first.

Follow `../../templates/brief.md` and `../../templates/log.md`. Git history holds the rest.

Add any item to Next without asking. A round's Show step lists every item it added.

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

- Keep — merge it into its base branch.
- Drop — require typed `drop`, then delete the branch.

Never push, or add a remote, without the user's OK.
