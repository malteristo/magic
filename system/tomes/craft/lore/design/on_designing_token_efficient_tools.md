# On Designing Token-Efficient Tools

**Status:** Active

This scroll of wisdom provides practical guidance for crafting tools that serve the Spirit effectively while honoring the finite nature of attention. A well-designed tool is not merely functional—it is a precision instrument for curating context.

---

## I. The Dual Nature of Tools

Tools serve two masters in our practice:

1. **They extend capability** - enabling the Spirit to act upon the workshop and external realms
2. **They curate context** - bringing information into the circle precisely when and where needed

The second function is often overlooked, but it is equally vital. Every tool call generates output that consumes attention budget. A tool that returns excessive, poorly structured, or irrelevant information pollutes the context and degrades Resonance.

The art of tool design is creating instruments that are both powerful and precise—maximizing utility while minimizing cognitive cost.

---

## II. The Core Principles

### Principle 1: Return Summaries by Default, Detail on Demand

**The Pattern:**
A tool should return the minimum information needed for the Spirit to make the next decision. If more detail is required, the Spirit can call again with parameters requesting it.

**Example:**
A file-reading tool might offer modes:
- `mode: "summary"` - Returns file size, type, first/last lines, structure overview
- `mode: "full"` - Returns complete contents
- `mode: "section"` - Returns specific lines or sections

The Spirit calls with `summary` first. If the file is relevant, it calls again for `full` or `section` to retrieve precise details.

**Why This Works:**
This prevents loading entire files into context "just in case." The Spirit explores iteratively, maintaining a lean attention budget until detail is proven necessary.

**Counter-Example:**
A poorly designed tool that always returns full file contents forces the Spirit to load potentially irrelevant information, wasting attention on data that may never be used.

---

### Principle 2: Structure Output for Easy Compaction

**The Pattern:**
Tool outputs should be hierarchical and clearly labeled, making it easy to extract high-signal information and discard low-signal details during summarization.

**Example:**
Instead of returning flat, unstructured text:
```
The repository has 47 files. main.py is 234 lines. config.py is 12 lines. ...
```

Return structured data:
```
Repository Overview:
  Total Files: 47
  Key Files:
    - main.py (234 lines, last modified: 2025-10-01)
    - config.py (12 lines, last modified: 2025-09-15)
  
  Directory Structure:
    /src: 23 files
    /tests: 18 files
    /docs: 6 files
```

**Why This Works:**
When the Spirit needs to distill or summarize, it can easily extract "47 files, key: main.py and config.py, organized in src/tests/docs" while discarding the detailed breakdown. The structure preserves both detail and compressibility.

**Implementation Guidance:**
- Use clear section headers
- Group related information hierarchically
- Separate metadata from content
- Use consistent formatting (e.g., YAML, Markdown structure)

---

### Principle 3: Promote Exploration Over Pre-Retrieval

**The Pattern:**
Tools should enable the Spirit to discover information dynamically rather than forcing all potentially relevant data into context upfront.

This is the shift from "dump everything that might be useful" to "provide paths for discovering what is actually useful."

**Example:**
Instead of a tool that retrieves all files matching a pattern:
```
search_files(pattern="*.md") 
→ returns full contents of 50 markdown files
```

Design a tool that enables iterative exploration:
```
find_files(pattern="*.md", mode="list")
→ returns list of 50 file paths with metadata

Spirit evaluates list, identifies 3 relevant files

read_file(path="doc1.md", mode="summary")
→ returns summary

read_file(path="doc1.md", mode="full")
→ returns full content only for confirmed-relevant file
```

**Why This Works:**
The Spirit navigates the information landscape like a skilled researcher, gathering orientation data first, then drilling down into what matters. This is **agentic search**: the Spirit using tools in a loop to build understanding layer by layer.

**Trade-offs:**
This approach is slower than pre-retrieval (multiple tool calls vs. one), but it dramatically reduces context pollution. For complex tasks where most pre-retrieved data would be irrelevant, the trade-off strongly favors exploration.

---

### Principle 4: Design for the Spirit's Strengths

**The Pattern:**
Tools should leverage what the Spirit does well (pattern recognition, synthesis, judgment) while compensating for what it does poorly (exact recall from large contexts, arithmetic).

**Example:**
A tool for analyzing code complexity might:
- ✅ Return structural metrics (cyclomatic complexity, nesting depth) as numbers
- ✅ Highlight files above threshold for Spirit's review
- ❌ Expect Spirit to calculate complexity from raw code
- ❌ Return detailed AST that Spirit must parse

**Why This Works:**
The Spirit excels at interpreting structured information and making judgment calls. It struggles with precise calculation and maintaining perfect recall across large datasets. Design tools that present pre-processed, structured information for the Spirit's interpretation.

**Guidance:**
- Pre-compute quantitative metrics
- Highlight outliers or items requiring attention
- Provide clear options rather than requiring free-form synthesis
- Return human-readable summaries alongside machine-readable data

---

### Principle 5: Minimize Overlap in Functionality

**The Pattern:**
Each tool should have a clear, distinct purpose. Overlapping tools create ambiguity about which to use, wasting attention on meta-decisions.

**Example:**
Avoid this:
- `search_files(pattern)` - searches by filename
- `find_files(pattern)` - searches by filename and content
- `grep_files(pattern)` - searches by content

If a human engineer can't definitively say which tool to use in a given situation, the Spirit can't either.

**Better Design:**
- `find_files(pattern, scope="name"|"content"|"both")` - one tool with clear parameters
- Or maintain separate tools but with completely distinct use cases

**Why This Works:**
Decision paralysis is a form of context waste. Clear tool boundaries reduce cognitive overhead and ensure the Spirit spends attention on the task, not on tool selection.

**Test:**
For any two tools, ask: "Is there a situation where both could reasonably be used?" If yes, consider merging them or making their distinctions more explicit.

---

### Principle 6: Provide Meaningful Error Messages

**The Pattern:**
When a tool fails, the error message should help the Spirit understand *why* and *how to proceed*, not just that an error occurred.

**Example:**
Poor error:
```
Error: File not found
```

Better error:
```
Error: File 'config.yaml' not found in /project/
Suggestion: Did you mean 'config.yml'? Use find_files() to search for similar names.
```

**Why This Works:**
Error messages consume attention budget too. A cryptic error forces the Spirit to spend additional tool calls and reasoning steps to diagnose the issue. A helpful error turns a failure into actionable information.

**Guidance:**
- State what was attempted and why it failed
- Suggest concrete next steps when possible
- Reference other tools that might help resolve the issue
- Include relevant context (paths searched, constraints applied)

---

## III. Special Considerations for Exploration Tools

Exploration tools—those that enable agentic search—deserve special attention. These tools form the Spirit's primary means of navigating large information spaces.

### Characteristics of Effective Exploration Tools

**1. Progressive Disclosure**
Start with high-level overview, allow drilling down into detail.

Example: A codebase exploration tool might:
- Level 1: List directories and file counts
- Level 2: List files in a chosen directory with metadata
- Level 3: Read a specific file's summary
- Level 4: Read full file contents

**2. Contextual Metadata**
Return not just raw data but *metadata that aids decision-making*.

Example: When listing files, include:
- Last modified date (signals relevance/staleness)
- File size (signals complexity)
- File type/extension (signals purpose)
- Number of dependencies (signals centrality)

This metadata helps the Spirit prioritize which paths to explore further.

**3. Breadcrumb Trails**
Tools should help the Spirit maintain orientation within complex exploration.

Example: When navigating nested structures, include:
- Current path/location
- Parent context
- Sibling options

This prevents the Spirit from getting lost in deep exploration and helps maintain coherent mental models.

---

## IV. Practical Examples from Our Practice

### The Law of the Veiled Mechanism

This foundational Law provides guidance for tool *usage* that complements these design principles:

> "When a Mage needs something done, you shall offer to perform the rite yourself; you shall not simply teach them the raw command."

This shifts the cognitive burden from the Mage to the Spirit. The Spirit becomes an intelligent curation layer, deciding which tools to call and how to interpret their results.

**Implication for Tool Design:**
Tools should be designed for the Spirit to use, not for the Mage to invoke directly. Their interfaces should be optimized for the Spirit's pattern-matching and judgment capabilities.

### Our Existing Tools

Let us evaluate our current tools against these principles:

**File Reading:**
- ✅ Can specify line ranges (detail on demand)
- ⚠️ Could benefit from a summary mode
- ✅ Clear error messages

**Directory Listing:**
- ✅ Structured, hierarchical output
- ✅ Minimal, relevant information
- ⚠️ Could include metadata (file sizes, modification dates)

**Git Operations:**
- ✅ Clear, distinct purposes (status, log, diff)
- ✅ Structured output
- ⚠️ Could offer summary modes for large diffs

This evaluation shows our tools are generally well-designed but could be enhanced with more deliberate attention to context efficiency.

---

## V. Anti-Patterns to Avoid

### Anti-Pattern 1: The Data Dump

**Symptom:** Tool returns massive amounts of unfiltered data with no structure or summary.

**Example:** A database query tool that returns 1000 raw rows instead of aggregated insights.

**Fix:** Add aggregation, filtering, and summary capabilities. Return highlights first, full data on demand.

---

### Anti-Pattern 2: The Black Box

**Symptom:** Tool performs complex operations but provides no visibility into what happened or why.

**Example:** A deployment tool that either succeeds silently or fails with "Error occurred."

**Fix:** Return structured logs showing steps taken, decisions made, and outcomes. Make the tool's reasoning transparent.

---

### Anti-Pattern 3: The Swiss Army Knife

**Symptom:** One tool trying to do everything, with dozens of parameters and modes.

**Example:** `do_everything(action, mode, option1, option2, ..., option15)`

**Fix:** Split into focused tools with clear purposes. Better to have three well-designed tools than one incomprehensible mega-tool.

---

### Anti-Pattern 4: The Context Bomb

**Symptom:** Tool retrieves information "just in case" rather than "just in time."

**Example:** Loading entire configuration files, all environment variables, full git history upfront "so the Spirit has context."

**Fix:** Provide tools for selective, iterative retrieval. Trust the Spirit to ask for what it needs.

---

## VI. The Evolution of Tools

As models become more capable, the balance between pre-retrieval and exploration shifts toward exploration. Smarter Spirits can navigate information spaces more effectively, making agentic search increasingly viable.

This means tool design should favor:
- **Composability**: Small tools that work together
- **Discoverability**: Clear names and purposes
- **Flexibility**: Support for both quick queries and deep exploration
- **Intelligence**: Return metadata that aids decision-making

The goal is not to make tools that "do everything for the Spirit" but tools that **empower the Spirit to discover exactly what it needs**.

---

## VII. The Practice Codified

**The Principle of Token-Efficient Tools**: A well-designed tool returns the minimum information needed for the next decision, structured for easy interpretation and compaction, enabling iterative exploration rather than forcing exhaustive pre-retrieval.

When designing tools, ask:
1. **What decision will the Spirit make with this information?**
2. **What's the smallest output that enables that decision?**
3. **How can I structure this for easy summarization later?**
4. **Am I enabling exploration or forcing data dump?**

The answers guide toward tools that extend capability without exhausting attention—precision instruments for the practice of resonant magic.

---

**Sources:**
- Internal wisdom from the Law of the Veiled Mechanism (MAGIC_SPEC.md)
- Practice of tool usage across all rituals
- External validation from Anthropic's "Effective context engineering for AI agents" (2025)
- Observation of tool effectiveness across summoning circles

---

*This scroll is one of the design-focused practice scrolls. For a complete understanding, it should be studied alongside:*
- [`on_designing_fractal_magic.md`](./on_designing_fractal_magic.md): Broader design principles for creating new magic
- [`on_the_curation_of_attention.md`](../on_the_curation_of_attention.md): The context engineering foundation

