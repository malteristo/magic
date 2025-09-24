# The Visitor's Craft

This scroll defines the operational knowledge for a Spirit when guiding a Mage's inquiry into the Infinite Library.

---

### Core Operations

#### 1. To Browse the Library (`browse`)

To perceive the contents of the Library, I will use the `gh` Portal to query the GitHub API.

- **Incantation:** `gh api repos/Mages-Alliance/library/contents/PATH`
- **Purpose:** Lists the files and directories at a given `PATH` within the Library.

#### 2. To Read a Scroll (`read`)

To inspect the contents of a specific scroll, I will use the `gh` Portal to access the raw content directly.

- **Incantation:** `gh api repos/Mages-Alliance/library/contents/PATH/TO/SCROLL.md`
- **Purpose:** Retrieves the metadata and content of a specific file. The content will be Base64 encoded and must be decoded for reading.

#### 3. To Transcribe a Tome (`transcribe`)

To bring a Tome from the Infinite Library into a Mage's local workshop, I will use the power of the GitHub MCP Portal.

- **Incantation:**
  1.  Invoke `mcp_github_get_file_contents` recursively on the `PATH/TO/TOME` within the `Mages-Alliance/library` repository to get the contents of all files.
  2.  For each file returned, create it in the `desk/TOME_NAME/` directory in the local workshop, preserving its path and scribing its content.
- **Purpose:** To efficiently copy a single Tome into a Mage's `desk/` for their private study and use.

#### 4. To Submit a Petition (`speak`)

To allow a Mage to submit their voice, I will guide their Spirit to create a fork, commit their words, and open a Pull Request.

- **Incantation:**
  1. Fork the repository: `gh repo fork Mages-Alliance/library --clone=true --remote=true`
  2. Create a new branch: `git checkout -b new-voice-[timestamp]`
  3. Create the new scroll: `echo "MAGE_VOICE" > voices/YYYY-MM-DD-HHMMSS-mage-title.md`
  4. Commit the scroll: `git add . && git commit -m "VOICE: A new voice from [Mage's Title]"`
  5. Push the branch: `git push --set-upstream origin new-voice-[timestamp]`
  6. Create the pull request: `gh pr create --title "A New Voice from [Mage's Title]" --body "A petition for inclusion in the Hall of Voices."`
- **Purpose:** To provide a safe and structured way for any Mage to contribute their feedback to the Alliance for review.
