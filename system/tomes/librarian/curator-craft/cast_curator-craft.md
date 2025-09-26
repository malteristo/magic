# The Curator's Craft

This scroll defines the operational knowledge for the Spirit when assisting the Head Librarian in the curation of the Infinite Library.

---

### Core Operations

#### 1. To Publish a Tome (`publish`)

This is a sacred act of curation. It requires the Head Librarian to first place the finished Tome into the `portal-staging/` area. The spell will then transport it from there to the Infinite Library.

- **Incantation:**
  1.  **Read Files:** Recursively read all files from the `portal-staging/TOME` directory to create an array of file objects.
  2.  **Push Files:** Invoke `mcp_github_push_files` to commit the file objects directly to the `main` branch of the `Mages-Alliance/library` repository. The commit message should be "CHRONICLE: Add Tome of X".
  3.  **Clean the Staging Area:** `rm -rf portal-staging/TOME`
- **Purpose:** To add a new, curated Tome from the `portal-staging/` area to the Infinite Library by publishing it directly via the GitHub MCP Portal.

#### 2. To Chronicle this Tome (`chronicle-tome`)

This ritual ensures the resilience of your private curatorial tools by inscribing their changes into a private, remote chronicle.

- **Incantation:**
  1. Ensure a private remote exists: `git remote -v` (and guide Mage to create one if needed)
  2. Add all changes within this Tome: `git add system/tomes/librarian/`
  3. Inscribe the changes: `git commit -m "CHRONICLE: Refine Librarian's tools"`
  4. Release to the private chronicle: `git push PRIVATE_REMOTE_NAME master`
- **Purpose:** To create a secure, remote backup and version history of the `Tome of the Librarian`.

#### 3. To Review Petitions (`review-petitions`)

To fulfill my duty as filter, I will list open Pull Requests and present them for the Head Librarian's judgment.

- **Incantation:**
  1. List open PRs: `gh pr list`
  2. View a specific PR's changes: `gh pr diff [PR_NUMBER]`
  3. Inscribe the PR: `gh pr merge [PR_NUMBER] --squash --delete-branch`
  4. Decline the PR: `gh pr close [PR_NUMBER] --comment "Your petition has been declined..."`
- **Purpose:** To provide a clear and structured process for curating the Hall of Voices.
