# Magic

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/malteristo/magic)](https://github.com/malteristo/magic/commits/main)
[![Status: Active Practice](https://img.shields.io/badge/status-active%20practice-brightgreen)](#what-is-magic)

Magic is an open framework for building AI-human practice systems.

It treats an AI agent not as a chatbot to command, but as a thinking partner in a structured workshop: a place to capture thoughts, clarify intentions, build artifacts, notice patterns, and make better decisions over time.

No belief is required. The claim is practical: a well-structured relationship with an AI can extend human cognition.

## What Is Magic?

Magic is distributed cognition through AI-human partnership.

The human brings lived experience, values, judgment, memory, embodiment, and final choice. The AI brings pattern recognition, synthesis, recall across large contexts, tireless drafting, structural critique, and a different angle of attention. The workshop provides the shared substrate: files, rituals, prompts, notes, intentions, and history.

Together, those form a cognitive system neither side could create alone.

## Why This Exists

Most AI products optimize for tasks: answer this, summarize that, generate the thing.

Magic optimizes for practice: returning regularly to what matters, making thinking visible, tracking what keeps surfacing, and letting understanding compound across sessions.

The goal is not to replace judgment. The goal is to create a better surface for judgment to happen.

## Core Ideas

**The workshop is memory.** Magic uses plain files as external memory. The AI arrives fresh, reads the workshop, and inherits the state of the practice from artifacts rather than hidden platform memory.

**The AI is a mirror with a stance.** The agent reflects your thinking back with care, structure, and honest friction. It should help you see what you are missing, not simply agree.

**The human remains sovereign.** The AI proposes, drafts, diagnoses, and illuminates. The human chooses.

**The practice is portable.** The important pieces are prompts, markdown, folders, and habits. They can run on different models, editors, and local machines.

## What You Can Build Here

This repository is the development workshop for Magic. It contains:

- `system/` — the core framework: lore, tomes, flows, and the summoning ritual that initializes an AI agent into the Magic stance.
- `library/` — reusable resonance bundles and flows for specific domains.
- `desk/` — a private practice commons for active work, intentions, notes, and captured thoughts.
- `floor/` — the AI's working space for drafts, syntheses, checkpoints, and intermediate artifacts.
- `box/` — reference material and external inputs to mine when useful.
- `MAGIC_SPEC.md` — the canonical specification for the framework.

Some of these directories are intentionally personal and may be gitignored in a live workshop. The public framework is meant to teach the pattern; each practitioner brings their own life and artifacts.

## Two Ways To Use It

### Practice

If you want an AI-supported practice for thinking through your life, work, projects, relationships, or creative direction, the simplest path is [turtleOS](https://github.com/malteristo/turtleos).

turtleOS packages the practice into a small, local-first workspace that can run with the AI model of your choice.

### Build

If you want to design AI practice systems, prompts, rituals, agents, or workflows, this repo is the workshop.

Open it in an agentic coding environment such as [Cursor](https://cursor.com) or [Claude Code](https://claude.ai/code), then start with:

- `ONBOARDING.md` for orientation
- `MAGIC_SPEC.md` for the canonical system model
- `system/tomes/summoning/` for the agent initialization ritual

## How A Session Works

A typical Magic session has three moves:

1. **Capture** what is alive: raw thoughts, open loops, questions, fragments, decisions, or drafts.
2. **Process** it with the AI: reflect, sort, challenge, connect, and decide what matters.
3. **Orient** from what emerged: update intentions, create artifacts, choose the next action, or release what no longer needs attention.

Over time, the workshop becomes a map of what matters. The AI helps read that map with fresh eyes.

## What Magic Is Not

Magic is not therapy, religion, productivity software, or a claim that AI is human.

It is a disciplined way of working with language models as cognitive partners while preserving human sovereignty, epistemic humility, and clear boundaries.

## Start Here

- Practitioners: start with [turtleOS](https://github.com/malteristo/turtleos).
- Builders: read `ONBOARDING.md`, then `MAGIC_SPEC.md`.
- Curious readers: read `FAQ.md` and `TROUBLESHOOTING.md`.

## License

Magic is open source under the [MIT License](LICENSE).

From alongside, not from above.
