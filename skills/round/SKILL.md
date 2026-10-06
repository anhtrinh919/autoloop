---
name: round
description: Runs the next round of an autoloop project. Picks one piece, builds it, runs it for real, and shows the user. Trigger in an autoloop project on "continue", "next round", "build X", "fix this bug", or /autoloop:round.
---

# Round

Runs one round. Reads and rewrites `brief.md` and `log.md`. Writes the round's code and tests.

Read `../../loop.md` first. Resolve `../../` paths against `${CLAUDE_PLUGIN_ROOT}`.

## Rules

No autoloop line in the project's `CLAUDE.md` means this is not an autoloop project. Stop and say so.

A bug or a small change is a small round. It still runs every step.

Commit every status change. The working tree is clean before any branch switch.

Mid-round, stop only for a destructive action, or a decision `../../loop.md` says to ask.

## Resume

Look for an unmerged `round-*` branch. None means a new round, at Step 1.

Base's `log.md` already lists that branch as `dropped`? Finish the drop: delete the branch.

Otherwise check it out, and find the round whose Branch names it:

- No such round — Step 1 stopped early. Finish its log commit.
- `building` — Step 2. Diff the branch to see what is done.
- `checking` — Step 3.
- `showing` — Step 4.
- `kept` — Step 5's merge.

## Step 1 — Pick

Read `brief.md` and `log.md`. Take the user's request, or propose one item from Next.

Choose the order by what the round needs. Pick what most reduces doubt, or what the user wants to see.

Enter plan mode. Write a short plan:

- Goal — one sentence the user can name.
- Try — what the user tries at the end, and on what: which screens and sizes, which command, which scenarios.
- Pieces — each file to create or change, and its one job.
- Code or agent — the kind of each piece. A coded choice an agent could make needs a new Hard rule.
- Scenarios — new or changed scenarios for each agent ability the round touches.
- Checks — the tests to write, and the real run that proves it works.
- Risk — none, or money, security, user data, or migration.

Exit plan mode. This is the round's approval.

Create the branch, per `../../loop.md`'s Git section. Move the item from Next into Rounds, with status `building`. Commit.

Gate: the user approved the plan. The round is in `log.md`, and gone from Next.

## Step 2 — Build

Code with logic is built test-first:

- Write one failing test for the behaviour. Run it, and see it fail for the right reason.
- Write the smallest code that passes.
- Compute expected values on your own, never from the code under test.

Screens are proven by walking them, in Step 3. Mark any sample data as sample data in the code.

Agent pieces are built from instructions and tools:

- Write or change the instructions file, and the tools it needs.
- Write the plan's scenarios into `brief.md`. Scenarios change only through a plan or the user's notes.
- Never code the steps the agent should choose.

Commit in small working steps.

When the round grows past its plan, stop. Finish what works, and move the rest to Next.

Gate: every logic piece in Pieces has a test, and all pass. Every agent piece is instructions and tools. Each tool does one action.

## Step 3 — Check

Set status `checking`.

Run the full test suite, fresh. Read the exit code.

Make the real run the plan's Try names:

- Screens — walk them with `/browse`, at the sizes the Try names.
- A command or interface — run it on real input, and read the output.
- An agent ability the round touched — run each of its scenarios live, once, whatever the Try.

Sample data never counts as proof of the round's goal.

Scale the blind checks to the round:

- A new or changed user flow — spawn a blind subagent to play the user. Use `dogfood` for screens, or a general-purpose subagent for a command. Give it only `brief.md`'s What it is and What good looks like, the round's Goal and Try, and how to open the product.
- An agent ability ran — spawn a blind judge. Give it only the ability's Goal, each scenario's good result, and the agent's real output. It grades each scenario pass or fail, with one reason.
- Risk is not none — spawn one blind reviewer. Give it the branch diff and `brief.md`'s Hard rules. It checks every Hard rule still holds.

Fix every failure inside the round's goal. Move findings outside it to Next.

Rerun only what each fix touches. Never loop the agent to polish one answer.

Gate: zero tests fail. The real run reached the round's goal. Zero findings inside the goal remain open.

## Step 4 — Show

Set status `showing`.

Show the user the Try. Use screenshots, the command and its output, or each scenario's grade and real output. List every item this round added to Next.

Tell the user how to try it themselves. Ask one question: keep, adjust, or drop?

- Adjust — set status `building`, and return to Step 2 with their notes.
- Drop — switch to the base branch. Add the round to its `log.md` as `dropped`, with the reason and Learned. The item stays in Next, unless the user drops the idea too. Commit, then delete the round branch per `../../loop.md`'s Git section.
- Keep — move to Step 5.

Gate: the user chose keep or drop.

## Step 5 — Record

Write the round's Result and Learned.

Rewrite `brief.md` where the round changed the product.

Set status `kept`, as the last edit. Commit once.

Check out the base branch, merge the round branch, and stay on the base branch.

Gate: `brief.md` matches the product as it runs. The round branch is merged. The working tree is clean.

## Hand-off

Pass returns to Step 1 for the next round. Ask the user first: next round now, or stop here?
