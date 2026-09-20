# NightCode

A terminal (TUI) app built with [Bun](https://bun.sh), React and [OpenTUI](https://github.com/sst/opentui).

## Requirements

- [Bun](https://bun.sh) `>= 1.3.0`
- A terminal that supports TUI apps (run it in a real terminal, not a piped/CI shell)

## Setup

```bash
git clone https://github.com/elina4675/NightCode.git
cd NightCode
bun install
```

Copy the example configuration and fill in your own values (see [Configuration](#configuration)):

```bash
cp .env.example .env
```

## Run

From the repository root:

```bash
bun run dev
```

This starts `packages/cli/src/index.tsx` in watch mode, so the app restarts when you edit a file.

## Checks

Type-check the CLI package:

```bash
bun run --cwd packages/cli typecheck
```

## Configuration

Configuration is read from environment variables. `.env.example` lists every variable with a placeholder value and is safe to commit. Your real `.env` is git-ignored — never commit it or put real secrets in `.env.example`.

## Project structure

```
packages/cli/src/
├── index.tsx            # app entry point
└── components/
    ├── command-menu/    # slash-command menu (list, filtering, keyboard hook)
    ├── header.tsx
    ├── input-bar.tsx
    ├── status-bar.tsx
    └── border.tsx
```
