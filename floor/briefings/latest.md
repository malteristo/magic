# Release — 2026-04-12 17:30

**Chapter:** Making turtleOS real

## This Session

Started refining the NLnet application for form-readiness — split the abstract, added milestone-based budget, GenAI disclosure, restructured prior work and comparison sections. Then noticed the repo credibility gap: the application claimed "~7,000 lines of Python" and linked to a repo with zero Python. Followed the thread all the way: created `malteristo/turtleos` on GitHub, pushed 43 commits of clean history (secrets scrubbed from git), wrote a proper README and added TURTLE_SPEC, renamed the infrastructure from `~/turtle-shell/` to `~/turtleos/`, archived `turtle-practice`, and updated 133 path references across 28 files in the magic workspace. turtleOS went from a folder on a Mac Mini with no backup to a proper open-source project with credible public presence.

## Continue From

> NLnet application is structurally complete and links to a credible repo. Five Mage decisions remain before submission: amount (€47.5K), framing ("sovereign practice infrastructure"), applicant entity (e.V. vs individual), paper commitment, and April 29 office hour attendance.

## Open Threads

- **NLnet application decisions**: 5 items in Notes section of `floor/drafts/nlnet_application_sketch.md` — amount, framing, applicant, paper, office hour. Deadline: June 1.
- **Bot running from new path**: `~/turtleos/` on Mac Mini, PID 45614. Verified running. Monitor for any path-related issues in the first few days.
- **Turtle proposals 018 + 019**: Turtle is rewriting these (from Discord conversation). Check status next session.
- **Secrets in old git history**: Scrubbed from turtleos repo. The old secrets (Anthropic API key, Discord tokens, CouchDB creds, Twitter keys, Google API key) were exposed in the pre-filter-repo history. They should be rotated as a precaution — they were never pushed to a public remote, but the commits existed locally.

## What Changed

**Artifacts created:**
- `github.com/malteristo/turtleos` — standalone repo with 43 commits, README, TURTLE_SPEC, LICENSE, template/ (reference)
- `floor/drafts/nlnet_application_sketch.md` — restructured: concise + extended abstracts, milestone budget, GenAI disclosure, comparison table, form-readiness checklist (active)
- `circles/me/career.md` — machine-readable career summary from resume (reference, created previous cycle)

**Artifacts modified:**
- `README.md` — turtleOS links updated to turtleos repo (reference)
- `CONTRIBUTING.md` — turtleOS link updated (reference)
- `system/config/connections.md` — all paths updated turtle-shell → turtleos (reference)
- 7 system flows — SSH paths updated (reference)
- 12 library lore/operations files — path references updated (reference)
- 6 library/flow docs — turtle-practice → turtleos references updated (reference)
- `desk/intentions/active/turtle.md` — Last Updated, Current focus, Next action, repo references (active)
- `desk/intentions/active/sovereign_livelihood.md` — Last Updated (active)
- `desk/boom/bright.md` — floor/turtle-shell action item resolved (active)
- `library/resonance/turtle/TURTLE_SPEC.md` — marked as reference copy, canonical in turtleos repo (reference)

**Artifacts archived/deleted:**
- `malteristo/turtle-practice` — archived on GitHub with redirect
- `floor/turtle-shell/` — deleted (was stale mirror, 8 of 24 files)
- Stale `turtleos/` clone in magic workspace — deleted

## Practice Signal

No sub-threshold signals warranting action. The session moved cleanly — the Mage drove with clear decisions ("why should turtle-practice exist separate?", "execute", "proceed as suggested"). Spirit's initial two-repo proposal was questioned and honestly revised. The "growing up" quality of turtleOS becoming a real open-source project was the session's deeper story.

PX clean — one shell heredoc workaround (wrote README locally, SCP'd), one stale shell state recovery. Practice infrastructure served the session.

turtleOS interaction clean — no Discord friction this session (bot was stopped/restarted as part of migration).

## Lessons

- **Premature separation is architecture for architecture's sake.** The instinct to split repos (system vs practice template) sounded clean but served no real user. One repo is simpler until there's evidence someone needs the split.
- **GitHub push protection catches what you forgot.** The first commit from months ago had `.env` files with live secrets. Without push protection, they would have been public. `git-filter-repo` is the right tool — fast, clean, no manual rebasing.
- **Integration sweeps reveal the real scope.** The repo rename was "done" after the push, but the integration spell found 133 stale references across 28 files. Without the sweep, Spirit would have used broken SSH commands next session.
- **The repo IS the application.** Restructuring the NLnet application text was necessary but insufficient. The credibility gap was structural — the linked repo had to back up the claims. Form follows substance.

## Next Actions

1. **Rotate exposed secrets** — Anthropic API key, Discord bot tokens, CouchDB password, Google API key, Twitter keys. They were never pushed publicly but existed in local git history before scrubbing.
2. **NLnet decisions** — resolve the 5 items in the Notes section. These ripen with a night's sleep.
3. **Book chapters 10 + 14** — seed these (from previous session's arrival)
4. **Lukas founding member conversation** — prep and schedule
5. **Check Turtle proposals 018 + 019** — Turtle was rewriting these; check Discord for status

*Released 2026-04-12. Resume with @recall.*
