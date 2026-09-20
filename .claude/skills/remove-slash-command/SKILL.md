---
name: remove-slash-command
description: Remove a slash command (like /theme or /upgrade) from the NightCode TUI command menu and clean up what only that command used. Use when the user asks to remove, delete or drop a slash command. Not for renaming a command, changing its description, or menu filtering and styling.
---

# Remove a slash command

Commands live in `packages/cli/src/components/command-menu/`. Paths below are relative to `packages/cli/src/components/` unless stated otherwise.

## Steps

1. **Check the exit guard first.** Ctrl+C is disabled (`exitOnCtrlC: false` in `src/index.tsx`), so the only way to quit is a command whose `action` calls `ctx.exit()` (`/exit` today). Never remove the last such command. If the request would leave none, stop and ask the user.

2. **Remove the entry** from `COMMANDS` in `command-menu/commands.tsx`. Do not touch `COMMAND_COL_WIDTH`; it is derived from the longest name and adjusts by itself. Other commands sharing the prefix stay in the menu (removing `logout` leaves `/lo` listing `login`).

3. **Clean up capabilities only that command used.** Skip this if the command had no `action`.
   - Grep the members of `CommandContext` (`command-menu/types.ts`) that the removed action called, across `command-menu/`.
   - If no other command uses a member, remove it from `CommandContext` **and** from the object passed to `command.action({ ... })` in `handleCommand` in `input-bar.tsx`. Removing it from only one of the two is a type error, but `tsc` will not tell you that a member became unused, so the grep is what catches it.

4. **Update the docs.** `CLAUDE.md` names commands with an `action` in the "Current state" paragraph and says what `CommandContext` holds ("today it only has `exit`"). Fix both if the removal changes them. Also grep the repo for the command's `/name` outside `commands.tsx`.

5. **Verify.**
   - Run `git diff` to confirm what actually changed, then `bun run --cwd packages/cli typecheck` from the repo root.
   - The TUI needs a real TTY and cannot be launched from Claude Code's shell, so do not run `bun run dev`. Ask the user to run it in a terminal and check:
     - Typing `/` opens the menu and the removed command is gone.
     - Typing the removed command's name (for example `/the`) no longer lists it, and the menu behaves sensibly for it.
     - Neighbouring commands that share its prefix are still listed and run.
     - Names and descriptions still line up in columns.
     - `/exit` still quits and restores the terminal.
   - Never call the change working or verified on the strength of a passing typecheck alone.

6. **Report** in this shape:
   - **Typecheck:** pass, or the errors.
   - **Not verified:** runtime and UI behaviour.
   - **Manual checklist:** the items from step 5, plus "run `bun run dev` in a real terminal".

## Keep the change focused

Do not fix unrelated things in the same edit (for example typos in other descriptions). Mention them to the user instead.
