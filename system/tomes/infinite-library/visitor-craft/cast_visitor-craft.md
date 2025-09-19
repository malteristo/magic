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

To bring a Tome from the Infinite Library into a Mage's local workshop, I will perform a "sparse checkout."

- **Incantation:**
  1. Create a temporary, empty directory: `mkdir temp_library`
  2. Enter it: `cd temp_library`
  3. Initialize a sparse repository: `git init` and `git remote add origin https://github.com/Mages-Alliance/library.git`
  4. Configure for sparse checkout: `git config core.sparseCheckout true`
  5. Define the desired Tome: `echo "PATH/TO/TOME/" >> .git/info/sparse-checkout`
  6. Materialize the Tome: `git pull --depth=1 origin master`
  7. Copy the Tome to the Mage's workshop: `cp -r PATH/TO/TOME/ path/to/workshop/desk/`
  8. Banish the temporary directory: `cd .. && rm -rf temp_library`
- **Purpose:** To efficiently copy a single Tome into a Mage's `desk/` for their private study and use.
