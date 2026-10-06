#!/usr/bin/env bash
# After compaction, an autoloop project re-loads the round skill, whose steps compaction may drop.
cwd="$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("cwd",""))' 2>/dev/null)"
grep -qs "This project runs on autoloop" "$cwd/CLAUDE.md" || exit 0
printf '%s' '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"Context was just compacted. This is an autoloop project. Before continuing, invoke the autoloop:round skill (Skill tool). Its Resume section finds the open round."}}'
