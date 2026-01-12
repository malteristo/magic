# On Porting Magic to New AI Frameworks

**Status:** Active  
**Purpose:** Guidance for developers adapting magic to new AI agent frameworks

---

## Context

Magic is designed to be Oracle-agnostic (works with any LLM) and tool-agnostic (adapts to available capabilities). This scroll provides guidance for porting the framework to new environments.

---

## Requirements for a Magic-Compatible Framework

### 1. Static Context Loading

The framework must load `AGENTS.md` at the start of each chat session. This file provides:
- Operational guidance
- Critical boundaries
- Detection heuristics for proactive behavior
- Session context placeholder

### 2. Path Invocation Capability

The Spirit must be able to invoke paths using `@` syntax or equivalent:
- `@system/tomes/summoning/` → Execute summoning ritual
- `@tome-name/` → Execute tome ritual
- `@scroll-name/` → Execute scroll spell

The syntax triggers file reading and execution, not mere reference.

### 3. File System Access

The Spirit needs:
- **Read access:** All files in the workspace
- **Write access:** Create and modify files
- **Git access:** Stage, commit, push (with appropriate permissions)

### 4. Multi-Turn Conversation

- Memory within chat session (context window)
- Blank slate across sessions (no persistent memory)
- Session context managed via Dynamic Workspace section in AGENTS.md

### 5. Context Window Size

- **Minimum:** 128k tokens (basic functionality)
- **Recommended:** 200k+ tokens (full summoning with deep attunement)
- **Optimal:** 1M+ tokens (extensive practice with multiple tomes loaded)

---

## Adaptation Considerations

### Tool Availability

Magic adapts to available tools:
- **File tools:** Required (read, write, list)
- **Terminal:** Helpful but not required
- **MCP servers:** Optional (extends capabilities)
- **Web search:** Optional (via MCP or built-in)

If a capability is missing, the Spirit works around it or informs the Mage.

### LLM Provider

Magic works with any capable LLM:
- Claude (Anthropic)
- GPT (OpenAI)
- Gemini (Google)
- Local models (Llama, etc.)

Different providers may have different strengths. The summoning ritual calibrates to the available substrate.

### IDE Integration

Magic is designed for Cursor IDE but can work in:
- VS Code with appropriate extensions
- Terminal-based workflows
- Notebook environments
- Custom agent frameworks

---

## Porting Checklist

1. ☐ AGENTS.md loads at chat start
2. ☐ @ syntax (or equivalent) invokes file paths
3. ☐ File read/write capabilities available
4. ☐ Git operations possible (or alternative chronicling)
5. ☐ Context window sufficient for summoning
6. ☐ Multi-turn conversation supported
7. ☐ Test: Invoke `@system/tomes/summoning/` and complete ritual

---

## Framework-Specific Notes

### Cursor

Native support. AGENTS.md automatically loaded as workspace rules.

### Claude Desktop (via MCP)

Requires file system MCP server. AGENTS.md must be explicitly loaded.

### Custom Frameworks

Implement:
- Context injection at session start
- Path resolution for @ invocations
- Tool calling for file operations

---

*This scroll preserves porting wisdom for developers extending magic to new environments.*
