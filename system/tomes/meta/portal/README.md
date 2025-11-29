# Charm of Portal Management

A charm for systematic portal lifecycle management—creating, monitoring, maintaining, and archiving shared practice spaces.

## Purpose

Portals are shared git repositories enabling distributed cognition across Mages. This charm handles their complete lifecycle: creation (repo + structure + collaboration), health monitoring (activity, sync, synthesis rhythm), maintenance (rotation, updates), and archival (graceful closure).

The charm removes portal management cognitive burden, allowing the Spirit to handle infrastructure while the Mage focuses on practice.

**Invocation:** `@meta/portal`

---

## Operational Guidance

### For the Spirit

When this charm is invoked:

1. **Determine intent** - Create new portal? Check status? Sync existing? Archive?
2. **Execute systematically** - Use GitHub API (Rube MCP) for repo management
3. **Update registry** - Maintain `portals/portals.yaml` with current state
4. **Handle STP artifacts** - Manage `.spirit/` coordination layer
5. **Report status** - Clear communication about portal health and actions taken

This charm makes portal management a Spirit duty, not a Mage burden.

### Portal Operations

**Create Portal:**
- Gather: Partner info, portal name, type (partnership/quest/research)
- GitHub: Create private repo, invite collaborators
- Local: Initialize structure per STP/1.0, commit, push
- Registry: Add entry, commit to magic repo

**Check Status:**
- Activity: Parse presence timestamps, detect inactive Mages
- Sync: Check git status (commits ahead/behind)
- Synthesis: Verify rhythm being maintained per protocol
- Health: Report overall portal vitality

**Sync Portal:**
- Pull changes from remote
- Review: New artifacts, intents, syntheses
- Alert: Contributions needing response or synthesis due
- Update: Own presence timestamp

**Rotate Synthesis:**
- Check schedule in protocol.yaml
- Update current_caretaker if rotation due
- Notify: Create intent for new caretaker
- Commit changes

**Pause/Resume:**
- Update presence: Set status (away/active)
- Update registry: Reflect current state
- Notify: Commit with clear message for partners

**Archive Portal:**
- Verify: Confirm archive intent
- Update registry: status → archived
- Optional: Final synthesis, closing ceremony
- Preserve: Portal remains accessible but marked complete

---

## Integration with Workflow

**Natural flow for portal creation:**
1. Mage: "I want to start partnership practice with [Name]"
2. Spirit: Invokes `@meta/portal create`
3. Spirit: Creates repo, structure, invites collaborator
4. Spirit: Reports portal ready, provides next steps
5. Mage: Begins practice

**Natural flow for portal health:**
1. Spirit: Periodic check during summoning (if portals exist)
2. Spirit: Detects synthesis due or inactive presence
3. Spirit: Offers portal status check or sync
4. Mage: Approves or defers

**Portal operations are infrastructure work** - Spirit's domain with Mage's oversight.

