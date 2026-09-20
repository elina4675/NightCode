---
name: add-slash-command
description: Add a new slash command (like /clear or /help) to the NightCode TUI command menu, or give an existing placeholder command real behaviour. Use when the user asks to add, register or implement a slash command. Not for menu styling, filtering logic or keyboard handling.
---

# Add a slash command

Commands live in `packages/cli/src/components/command-menu/`. Paths below are relative to `packages/cli/src/components/` unless stated otherwise.

## Steps

1. **Add an entry to `COMMANDS`** in `command-menu/commands.tsx`. The `Command` type (`command-menu/types.ts`) has:
   - `name`: no leading slash. The menu matches it by case-insensitive **prefix**, so a new name that shares a prefix with existing ones will appear next to them (`/lo` already lists `login` and `logout`).
   - `description`: shown in the menu.
   - `value`: `"/" + name`. `CommandMenu` uses it as the React `key`, so it must be unique.
   - `action?`: optional, see step 2.

   Array order is menu order. Do not touch `COMMAND_COL_WIDTH`; it is derived from the longest name.

2. **Choose the behaviour.**
   - No `action`: selecting the command inserts `value + " "` into the textarea so the user can type arguments. This is what every placeholder command does today.
   - With `action(ctx)`: runs immediately, after the textarea has been cleared. `/exit` is the reference example.

3. **If the action needs something `CommandContext` does not offer** (today only `exit`):
   - Add the member to `CommandContext` in `command-menu/types.ts`.
   - Supply it in the object passed to `command.action({ ... })` inside `handleCommand` in `input-bar.tsx`. Forgetting this is a type error at that call site.
   - `handleCommand` and `handleCommandExecute` are `useCallback(..., [])`, so anything the new capability closes over from props or state is frozen at first render. Read changing values through a ref (the `onSubmitRef` pattern in `input-bar.tsx`) instead of closing over them.

4. **Verify.**
   - Run `git diff` to confirm what actually changed, then `bun run --cwd packages/cli typecheck` from the repo root.
   - The TUI needs a real TTY and cannot be launched from Claude Code's shell, so do not run `bun run dev`. Ask the user to run it in a terminal and check: typing `/` lists the new command, a prefix of its name narrows the menu to it, and Enter runs it (an `action` command does its job, a placeholder inserts `/name ` into the input).
   - Never call the change working or verified on the strength of a passing typecheck alone. Report what was not verified.

## Keep the change focused

Do not fix unrelated things in the same edit (for example typos in existing descriptions). Mention them to the user instead.
