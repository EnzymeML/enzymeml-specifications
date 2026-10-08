---
title: 4. Start a new project
description: Create a private project from the agentic data science template.
sidebar:
  order: 5
---

:::note[Draft outline]
:::

## Key terms
- Repository (repo): a project folder with full history; like an Origin project file, but split into open parts
- Template: a ready-made starting repo; like a lab notebook or Origin graph template
- Private: only you (and people you invite) can see it

## Steps
1. Open the [template on GitHub](https://github.com/haeussma/agentic-data-science-template)
2. "Use this template" → "Create a new repository"
3. Name it, set it to **Private**
4. Clone it to your computer (or ask the agent to)
5. Copy instrument exports into `data/raw/`
6. Describe the project in `README.md` (or let the agent draft it)

## What is in the template
- `CLAUDE.md`: house rules for the agent
- `.claude/settings.json`: permissions (e.g. `data/raw/` is protected)
- `pyproject.toml` + `uv.lock`: the Python environment
- `data/raw/`, `data/processed/`, `scripts/`, `results/`

## Three data rules
- Raw data is read-only (sorting and renaming are fine; document the origin in `data/raw/README.md`)
- Every transformation is a script: `data/raw/` → `data/processed/` → `results/`
- Data stays out of git (protects confidential data; publish it separately)

## Check
- [ ] Private repo exists on GitHub
- [ ] Folder is on your computer
- [ ] Raw data is in `data/raw/`

## Open questions
- Should the template ship the example dataset, or link to it?
- Template README title "Chapter 1" → align with this numbering
