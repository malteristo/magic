# On Development Sprints

*How the Turtle contributes to magic's evolution through structured research and proposal.*

---

## The Pattern

A development sprint gives the Turtle a frontier mind and a research brief, then steps back. The Turtle surveys territory — the repository, the workshop, the architecture — and returns with proposals. The dyad reviews. The Mage decides.

This is not delegation. The Turtle sees what Spirit cannot: the codebase from outside the summoning. No lore-weight, no philosophical framework, no partnership history. Just the files, a capable mind, and care for the garden.

---

## Sprint Anatomy

### The Brief

A sprint starts with a brief: what to look at, what questions to hold, what constraints apply. The brief sets scope without dictating conclusions.

**Sprint brief components:**
- **Territory** — which directories, files, or concepts to survey
- **Questions** — what the triad wants to understand
- **Constraints** — what's out of scope, what not to modify
- **Tools** — what the Turtle can access (workshop survey, file read, shell)

### The Research Phase

The Turtle reads, surveys, and pattern-matches. It works with whatever access the brief grants — sometimes blind to the private workshop (seeing only the public framework), sometimes sighted (seeing desk/, floor/, box/).

The difference matters. A blind sprint reveals what the framework looks like to an outsider. A sighted sprint reveals architectural gaps between private practice and public structure.

### The Proposal

The output is a structured proposal: findings, recommendations, open questions, implementation sketch. The Turtle does not implement — it proposes. The proposal travels to the triad for review.

### The Triad Review

Spirit reads both proposals (if blind + sighted pair) and synthesizes: what's already done, what's still valid, what's highest leverage. The Mage sanctions the work. Implementation happens through the dyad (Mage + Spirit in the IDE), not the Turtle.

---

## Sprint Types

**Blind sprint** — Turtle sees only the public repository. Tests discoverability, documentation completeness, newcomer experience. Good for finding what's missing from the outside.

**Sighted sprint** — Turtle sees the full workshop. Tests architectural coherence, identifies gaps between private practice and public structure. Good for finding what should be surfaced.

**Targeted sprint** — Turtle examines a specific subsystem or question. Narrow scope, deep investigation.

---

## The Infrastructure

Sprints run on the Mac Mini via a sprint shell script. The Turtle gets a dedicated identity (`sprint.md`) that frames its role as gardener-researcher, not practitioner. Workshop access comes through an HTTP API on the laptop (port 8420) serving health, survey, and file-read endpoints.

**Key architectural choice:** The sprint identity is separate from the Consul, Steward, and Witness identities. The sprint Turtle is a researcher, not a role-player. It doesn't need the nervous system, the bridge, or the care ritual. It needs file access and a frontier mind.

---

## What Sprints Produce

Sprints produce proposals, not implementations. This separation is load-bearing:

- The Turtle lacks summoning context — it sees structure but not meaning
- Implementation requires the dyad's depth — lore awareness, design intent, philosophical grounding
- The Mage's sovereignty over the framework is preserved
- The triad model (Mage + Spirit + Turtle) distributes cognition without distributing authority

---

## First Sprint: 2026-03-07

Two sprints ran back-to-back in a single session:

1. **Blind** — Surveyed the public repository. Found many gaps that were actually private-only features. Revealed that the public framework undersells what's built.

2. **Sighted** — Surveyed the full garden. Identified six proposals for bridging private practice to public structure. Surfaced the IDE/Application reframe as the central architectural insight.

The session demonstrated a complete development loop: write sprint infrastructure, run research, produce proposals, review as triad, decide next actions.

---

*Crystallized 2026-03-07. The gardener surveys; the Mage tends.*
