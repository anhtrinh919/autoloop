---
name: round
description: Runs the next round of an autoloop project. Picks one piece, builds it, runs it for real, and shows the user. Trigger in an autoloop project on "continue", "next round", "build X", "fix this bug", or /autoloop:round.
---

# Round

Runs one round. Reads and rewrites `brief.md`, `log.md`, and `bug.md`. Writes the round's code and tests.

Read `../../loop.md` first. Resolve `../../` paths against `${CLAUDE_PLUGIN_ROOT}`.

## Rules

No autoloop line in the project's `CLAUDE.md` means this is not an autoloop project. Stop and say so.

A bug or a small change is a small round. It still runs every step.

Commit every status change. The working tree is clean before any branch switch.

Mid-round, stop only for a destructive action, or a decision `../../loop.md` says to ask.

Sort each bug found mid-round into the first case that fits:

1. The round caused it — fix it now.
2. It is small, in code the round touches — fix it now, with a test. Add it to the round's Bugs line.
3. A Next feature touches its area — add it to `bug.md`, folded into that feature.
4. Anything else — add it to `bug.md`, for a bug round.

Small means one fix and one test. It adds no screen, and no choice for the user.

## Resume

Look for an unmerged `round-*` branch. None means a new round, at Step 1.

Base's `log.md` already lists that branch as `dropped`? Finish the drop: delete the branch.

Otherwise check it out, and find the round whose Branch names it:

- No such round — Step 1 stopped early. Finish its log commit.
- `building` — Step 2. Diff the branch to see what is done.
- `checking` — Step 3.
- `showing` — Step 4.
- `kept` — Step 5's merge, push, and deploy.

## Step 1 — Pick

Read `brief.md`, `log.md`, and `bug.md`.

`bug.md` holds at most 9 items. At 10 or more, this round is a bug round. Offer no other pick. A round the user named runs after it.

For that bug round, tidy `bug.md` first:

- Merge repeats.
- Find bugs that later rounds already fixed.
- Check each target still names a feature in Next.
- Show both lists. Ask which bugs to drop. Drop nothing without the user's yes.

Commit a new `bug.md` and the tidy on the base branch, before the round's branch exists.

Otherwise, a user who named the round has picked it. Or show Next and `bug.md` with your recommended pick. Wait for the user's choice before planning.

A pick is one of:

- One feature. It takes every bug that folds into it. Name each one.
- A bug round: every item in `bug.md`, whatever its target. Its goal is an empty `bug.md`.

A bug round fixes bugs by impact times visibility, highest first. Impact is how much a bug hurts the user. Visibility is how often the user meets it. A bug it cannot fix goes back to `bug.md`, with the reason.

Recommend by what the round needs. Pick what most reduces doubt, or what the user wants to see.

Ask every open question in chat first, per `../../loop.md`'s Asking section. Wait for the answers.

The plan holds no questions. It states each answer as a settled choice. A question found while planning goes to chat, before the plan is shown.

Enter plan mode. Write a short plan:

- Goal — one sentence the user can name.
- Try — what the user tries at the end, and on what: which screens and sizes, which command, which scenarios. Use the user's own screen sizes. Cover each bug the round takes.
- Pieces — each file to create or change, and its one job.
- Code or agent — the kind of each piece. A coded choice an agent could make needs a new Hard rule.
- Scenarios — new or changed scenarios for each agent ability the round touches.
- Checks — the tests to write, and the real run that proves it works.
- Risk — none, or money, security, user data, or migration.

Exit plan mode. This is the round's approval.

Create the branch, per `../../loop.md`'s Git section. Add the round to Rounds, with status `building`. Remove its feature from Next. Move its bugs from `bug.md` to its Bugs line. Commit.

Gate: the user picked the round and approved the plan. The round is in `log.md`. Its items are gone from Next and `bug.md`.

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

When the round grows past its plan, stop. Finish what works. Move the rest to Next or `bug.md`.

Gate: every logic piece in Pieces has a test, and all pass. Every agent piece is instructions and tools. Each tool does one action.

## Step 3 — Check

Set status `checking`.

Run the full test suite, fresh. Read the exit code.

Make the real run the plan's Try names:

- Screens — walk them with `/browse`, or a real terminal for a terminal app, at the sizes the Try names.
- A command or interface — run it on real input, and read the output.
- An agent ability the round touched — run each of its scenarios live, once, whatever the Try.

Sample data never counts as proof of the round's goal.

Look at every screen yourself, in screenshots:

- Take them as the user sees them: the user's own window size, theme, and real data.
- Open each screenshot. Screen text or a passing check never counts as a look.
- Judge it as the user. Note what the eye meets first, and what is empty, cut, or unclear.
- Fix what fails that look, as any other failure.

Scale the blind checks to the round:

- A new or changed user flow — spawn a blind subagent to play the user. Use `dogfood` for screens, or a general-purpose subagent for a command. Give it only `brief.md`'s What it is and What good looks like, the round's Goal and Try, and how to open the product.
- An agent ability ran — spawn a blind judge. Give it only the ability's Goal, each scenario's good result, and the agent's real output. It grades each scenario pass or fail, with one reason.
- Risk is not none — spawn one blind reviewer. Give it the branch diff and `brief.md`'s Hard rules. It checks every Hard rule still holds.

Fix every failure inside the round's goal. Sort every other bug per Rules. Move other findings to Next.

Rerun only what each fix touches. Never loop the agent to polish one answer.

Gate: zero tests fail. The real run reached the round's goal. You looked at every screen's screenshots. Zero findings inside the goal remain open. Every bug Rules says to fix now is fixed.

## Step 4 — Show

Write the round's Built line: 3 to 5 short points of what the user can see.

Rewrite its Try line as the user's own steps. Split the points in both with `;`.

Set status `showing`, in the same commit.

Show the user the Try. Use screenshots for every screen, the command and its output, or each scenario's grade and real output. List every bug this round fixed off-plan, and every item it added to Next or `bug.md`.

Tell the user how to try it themselves. Ask one question: keep, adjust, or drop?

- Adjust — set status `building`, and return to Step 2 with their notes. Write the notes on the round's own `Adjust:` line, never into Try; Try stays the user's steps.
- Drop — switch to the base branch. Add the round to its `log.md` as `dropped`, with the reason and Learned. Its feature goes back to Next, and its bugs to `bug.md`, unless the user drops them too. So does each feature the user asked for during the round. Commit, then delete the round branch per `../../loop.md`'s Git section.
- Keep — move to Step 5.

Gate: the user chose keep or drop.

## Step 5 — Record

Write the round's Result and Learned.

Rewrite `brief.md` where the round changed the product.

Set status `kept`, as the last edit. Commit once.

Check out the base branch, merge the round branch, and stay on the base branch.

Push and deploy, per `../../loop.md`'s Git section. Open the live product, and see the round's change there.

A push or deploy fails? Fix it, or tell the user. Never call a round shipped before it is live.

Tell the user it shipped, with the live link. Name any part How to ship marks none.

Gate: `brief.md` matches the product as it runs. The round branch is merged, then pushed and deployed per How to ship. The live product shows the change. The working tree is clean.

## Hand-off

Pass returns to Step 1 for the next round. Ask the user first: next round now, or stop here?
