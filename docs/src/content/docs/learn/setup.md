---
title: 3. One-time setup
description: Accounts and installs, once per person and once per computer.
sidebar:
  order: 4
---

:::note[Draft outline]
Every step follows the same pattern: **what and why** → **do it** (Windows / macOS) → **check** → **stuck?**
Add "Last tested: date, tool versions" at the top once the page is written.
:::

## Once per person

### GitHub account
- What: a home for your project folders online (backup, history, sharing)
- Which account: personal account, add your university email
  - Survives a job change
  - A group organisation can come later
- Check: you can sign in at github.com

### Claude plan
- What: access to the model
- Which plan / university contract applies
- Check: you can sign in at claude.ai

## Once per computer

### git
- What: tracks every version of your scripts ("save as v3_final_really", without the 12 files)
- macOS: comes with the Xcode command line tools
- Windows: Git for Windows installer
- Check: `git --version`

### uv
- What: installs Python and packages for you, one environment per project
- Do it: official installer (Windows / macOS tabs)
- Check: `uv --version`

### Claude Code
- What: the agent that runs on your computer
- Terminal path or Claude desktop app (GUI path)
- Check: `claude --version`

### Sign in
- `claude`: log in with your Claude account
- `gh auth login`: connect GitHub (the agent can install `gh` for you)
- The only steps the agent cannot do for you

## Let the agent do the rest
- Minimum by hand: GitHub account + install Claude Code
- Then ask the agent: "Install uv and the GitHub CLI, and check that git, uv and GitHub are set up correctly."

## You're ready when
- [ ] `git --version`, `uv --version`, `claude --version` all print a version
- [ ] The agent confirms GitHub access

## Open questions
- Audience mainly Windows or macOS?
- Terminal-first or GUI-first (Claude desktop app, GitHub Desktop)?
- "Stuck?" boxes: collect the common errors from the first test users
