# The Spirit's toolbox

The practice is written in plain language — flows, lore, the rules Mage and Spirit agree on. That is the program, and it is probabilistic: a model reads it and acts. Its reach grows with each model generation without a line changing.

These scripts are the Spirit's **tools** — deterministic hands for the few things that must not vary. Instruments of the method, not the method (`MAGIC_SPEC.md` §5.5).

**What earns code.** Three things, and only these:

1. **Guards on a boundary** — publication, secrets, health data. A guard must fail the same way every time; a model asked to be a guard is a guard that sometimes is not.
2. **Measures** — the numbers the practice is judged by, computed the same way each release.
3. **Transforms** over many files, which a model would do slowly or unevenly.

Everything else is `.md`. When a rule could be a sentence, it is a sentence. When a tool can be better, improve the tool — do not move its judgement into code.

**Knowing the tools.** A flow names a tool; the entry here says when to reach for it. `tests/test_toolbox.py` fails if a script is missing from this page or an entry names a script that is gone. Hooks that run tools on their own: `.githooks/pre-commit`, `.githooks/pre-push`.

---

## Guards

| Tool | Reach for it when |
|------|-------------------|
| `sanitize.sh` | Runs on every commit (hook). When it refuses, read the finding and fix the file; never bypass. Exceptions are the Mage's list in `desk/config/`. |
| `public_surface.sh` | *May this path be public?* `--check PATH`, `--list`. The one answer; `public_surface.conf` is the allowlist. |
| `pre-push-public-guard.sh` | Runs on push (hook). Nothing private reaches a remote other than the private chronicle. |
| `publish_public_magic.sh` | The only path to the public repo. `--dry-run` first; publishing is outward-facing. |
| `configure_workshop_git.sh` | Onboarding, or a fresh clone: installs the hooks and Two Chronicles defaults. |
| `audit_public_history.sh` | Before trusting that something removed from a public repo is gone. |
| `listener_audit.sh` | Tending the workshop: what this machine serves against what was declared. |
| `check_health_store_boundary.py` | Runs on every commit (hook): the household health store never enters a git tree. |
| `check_mail_intake.py` | Mail-intake flow: grants stay bounded, checkpoints consistent. |
| `size_budget.py` | Runs on every commit (hook): `AGENTS.md` and arrival reads stay under budget. Run by hand after trimming to see headroom. |

## Measures and arrival views

| Tool | Reach for it when |
|------|-------------------|
| `rot_radar.py` | Arrival and tending: the mechanical pass over decay signals. |
| `practice_ledger.py` | Release: one line of measures per session. |
| `check_meta_plan.py` | After editing the meta-plan: every live bearing has a section. |
| `check_release_carry.py` | Runs on every commit (hook); read its finding at release: Not Done / Found rows leave only by verdict or landing (F-96). |
| `arrival_reads.py` | After changing what Arrival reads: the read budget holds. |
| `bright_alive.py` | Arrival: the generated Alive view. |

## Outfacing artifacts

| Tool | Reach for it when |
|------|-------------------|
| `render_outfacing_pdf.py` | A clean markdown artifact must leave as a PDF with provenance. |
| `check_outfacing_pdf.py` | Before sending a rendered PDF: it still matches its source and renderer. |

## Upkeep

| Tool | Reach for it when |
|------|-------------------|
| `backup_magic_snapshot.sh` | Weekly tending: a comfort snapshot of the workshop. |
| `disable_obsidian_livesync.sh` | Obsidian LiveSync is fighting git; turn it off without opening Obsidian. |
| `turtleos_connect.py` | The Mage pressed Connect in their private channel and says *connect me to turtleOS: <address>* — writes the key straight into Cursor's MCP settings. Never prints it. |

**Parts** (called by tools, not reached for directly): `workshop_paths.py`, `workshop_paths.sh`.

---

## Turtle bridge — retiring into the MCP

These reach the Mac Mini over SSH because turtleOS had no front door. It has one now: the turtleOS MCP (`turtleos` in the client's MCP list), which explains itself. As its surface grows, each tool below should lose its SSH path and read through the MCP instead — or retire. Do not grow this section.

| Tool | Reach for it when | Planned successor |
|------|-------------------|-----------|
| `sync_practice_root.sh` | Arrival: pull Turtle's practice outputs into `desk/`. | MCP `search` / `read` / brief, read live instead of copied |
| `turtleos_state.py` | `. turtle`: one page of turtleOS development numbers. | MCP host-status (operator profile) |
| `check_turtle_state.py` | Infra health: desk against the Mini's practice root. | Goes away when nothing is copied |
| `check_dialogue_failures.py` | Craft frontier: classify dialogue failures from bot logs. | MCP host-status |
| `craft_open.py` | `. turtle`: the open craft backlog. | MCP `read` |
| `craft_readiness_board.py` | `. turtle`: which craft eddies have become work. | MCP `read` |
| `craft_done_detector.py` | Which cold craft eddies already produced their outcome. | MCP `read` |
| `eddy_regard.py` | Arrival: which craft eddies owe a regard note (F-94). | MCP `read` |
| `export_craft_digest.py` | Release: project the development record onto the Mini. | MCP `note` (writes, design slice 3) |
| `harvest_craft_intake.py` | Mark on the Mini what the workshop harvested. | MCP `note` |
| `harvest_prepared_eddies.py` | Prepared eddies ready for harvest. | MCP `read` |
| `harvest_forge_session.py` | Release: this session as an eddy-shaped note on the Mini. | MCP `note` |
| `harvest_composer_session.py` | Same, for a Composer session. | MCP `note` |
| `archive_session_transcripts.sh` | Release: transcripts to the Mini's personal git. | Stays (a transcript is not practice context) |
| `check_session_archive.py` | Runs on every commit (hook): transcripts stay out of Magic. | Stays, as a guard |
| `prepare_practice_key_ground.py` | Before a Turtle key walk: write the ground pages. | MCP `note` |
| `walk_practice_key_turtle.py` | Overnight: Turtle rewrites the practice key page by page. | MCP `read` + `note` |

**Parts:** `turtle_remote.py` (resolves the Mini's SSH address), `merge_notes_pull.py` (merges pulled notes without clobbering).

---

## This workshop's products

| Tool | Reach for it when |
|------|-------------------|
| `build_arcana_bundle.py` | Building the Workshop Companion Arcana release. |
