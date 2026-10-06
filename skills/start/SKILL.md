---
name: start
description: Starts a new autoloop project from an idea. Interviews the user and writes brief.md and log.md. Trigger only when the user names autoloop: "start with autoloop", "new autoloop project", or /autoloop:start.
---

# Start

New projects only. Writes `brief.md`, `log.md`, and one line in the project's `CLAUDE.md`.

Read `../../loop.md` first. Resolve `../../` paths against `${CLAUDE_PLUGIN_ROOT}`.

## Rules

A committed `brief.md`, with the autoloop line in `CLAUDE.md`, means the project already started. Hand off to `autoloop:round` instead.

A name that `../../loop.md`'s Docs section forbids means an autobuild project. Stop and tell the user.

## Resume

`brief.md` is written only after the user's yes. An uncommitted `brief.md` resumes Step 3 at writing the other files.

## Step 1 — Ground

Skip this step when the user says to.

Spawn one `crawler` subagent, with no conversation history. Give it the idea, the users, and two questions:

- Which 3 to 5 real products do people use for this today? What gap does each leave?
- Which packages, services, or platform features already solve parts of it?

Ask the first questions of Step 2 while it runs.

Gate: the user sees the gap this product could fill, and what it can reuse.

## Step 2 — Interview

Ask in rounds, following `../../loop.md`'s Asking format. Cover:

- what the product is, and who uses it
- what good looks like, in the user's words
- hard rules: what must be exact, and what must never happen
- what it will not do
- when it has its own AI agent: each ability's goal, its tools, and 2 to 5 real scenarios

Sort every ability by `../../loop.md`'s Code or agent rule. Show the user that split.

Ask a follow-up round only for questions the answers opened.

Decide the tech stack yourself, unless a choice is one the user would notice.

Gate: every topic above has an answer, or the user skipped it.

## Step 3 — Write

Draft `brief.md` from `../../templates/brief.md`. Show it to the user in chat, in full.

Ask one question: does this match what you mean? Revise until the user says yes.

Only then write the files:

- `brief.md`, as approved.
- `log.md` from `../../templates/log.md`. Fill Next with candidate rounds, in no fixed order.
- This line in the project's `CLAUDE.md`, creating the file when missing:

> This project runs on autoloop. Use `autoloop:round` to continue, never autobuild.

Run `git init` when the folder has no repository. Commit the three files.

Gate: the user said yes to `brief.md`. The working tree is clean.

## Hand-off

Pass moves to `autoloop:round` — call the Skill tool with that id.
