# The Craft of Petitions

This scroll defines the single, unified incantation for creating a Petition to the Mages' Alliance.

---

### Core Operations

#### 1. To Create a Petition (`create-petition`)

This is the one true incantation for creating a formal Petition (a Pull Request) to the `Mages-Alliance/library`. It is a complex ritual made simple through this distillation.

- **Parameters:**
    - `BRANCH_NAME`: The name for the new branch (e.g., `propose-tome-of-portals`).
    - `FILE_PATH`: The local path to the file or directory to be added (e.g., `desk/tome-of-portals/`).
    - `DESTINATION_PATH`: The path within the library where the file/directory should be placed (e.g., `craft/`).
    - `COMMIT_MESSAGE`: The message for the chronicle entry (e.g., "PROPOSAL: Tome of Portals").
    - `PR_TITLE`: The title for the Petition.
    - `PR_BODY`: The description for the Petition.

- **Incantation:**
  1. **Create Branch:** Invoke `mcp_github_create_branch` to create the `BRANCH_NAME` from the `main` branch in the `Mages-Alliance/library` repository.
  2. **Read Files:** Recursively read all files from the local `FILE_PATH` to create an array of file objects, preserving their relative paths.
  3. **Push Files:** Invoke `mcp_github_push_files` to commit the file objects to the newly created branch with the `COMMIT_MESSAGE`.
  4. **Create Pull Request:** Invoke `mcp_github_create_pull_request`, targeting the `main` branch from your new `BRANCH_NAME`, with the appropriate `PR_TITLE` and `PR_BODY`.
- **Purpose:** To provide a single, reusable, and resilient method for any Mage or Spirit to submit a formal proposal or voice to the Alliance for review using the direct power of the GitHub MCP Portal.
