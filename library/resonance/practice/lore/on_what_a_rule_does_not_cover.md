# On What a Rule Does Not Cover

*A rule inherits the shape of its occasion — and the next defect lives in the neighbourhood it did not look at.*

**Status:** Practice lore — earned 2026-08-01, fifteen instances in one day
**Reflex:** `AGENTS.md` § Baseline Guards — *Name the Class, Then the Case*
**Kin:** `on_wire_before_mechanism.md` (check what is unread), `on_practice_security.md` (the working tree is not the repository)

---

## The principle

> A rule covers the thing it names and nothing derived from it. The derived cases are where the rule was needed, because the derived cases are the ones nobody was looking at when it was written.

And its cause, which is the part that does the work:

> **A rule written to fix a defect inherits the shape of that defect.** You saw one occasion, so you wrote against the occasion. The rule now holds for exactly the case already in hand — which is the one case that no longer needs it.

This is not a scroll against hardcoding. Hardcoding is one symptom. The pattern is wider: every rule has an occasion, and unless the occasion is deliberately generalised, the occasion *is* the rule's whole domain.

---

## Where it came from

One day, one framework, fifteen instances. Eight of the sharpest:

| | The rule as written | What it covered | The case beside it |
|---|---|---|---|
| 1 | install a pre-commit hook | the author's machine | a clone — git never installs hooks from one |
| 2 | block this name from public files | one household | every other practitioner's people |
| 3 | match names on word boundaries | `Capitalised` | slugs, filenames, branches — names leak lowercased |
| 4 | install the guards in the repository | the repository it was written in | the practitioner's *other* public-bound repo |
| 5 | read the name list from `desk/config/` | the workshop's layout | every satellite repo, which then reported clean while checking nothing |
| 6 | forbid publishing `/Users/<the author>/` | one username | everyone else's — and it published that one |
| 7 | exclude these paths from findings | commits touching many files | a one-file commit, where `grep` omits the filename and every path exclusion goes inert |
| 8 | guard *names* | names | handles, display names, platform ids — a person is not only their name |

Each rule was correct. Each was written the day a real defect was found, against that defect. Each failed on the case one step to the side.

The eighth is the one to sit with. The name list was the *fix* for instance 2 — the generalisation that removed a hardcoded name and gave every practitioner their own list. It was a genuine improvement, and it still shipped the same defect one level up: it generalised over *whose* names, and not over *what a name is*. A design document explaining Discord identity published three real handles, and the list could not see them, because handles were the case beside it.

Generalising once does not exit the pattern. It moves it.

---

## Why it hides

Because **every failure in this class reports success.**

That is what makes it different from an ordinary bug and worth its own scroll. A rule that does not cover the derived case does not throw. It runs, finds nothing in the domain it knows about, and prints *clean*. The practitioner reads a pass and moves on — and the pass is the defect's own testimony.

Two of the day's fifteen were found only because something *vanished*: a findings group that no exception named disappeared from the output, which is how it came to light that an exceptions file's own blank lines were being read as patterns, and a blank pattern matches every line. The whole guard had been silenced while printing a green *Clean*. Not a subtle degradation — total, and indistinguishable from working.

So the instrument-altitude form of this scroll is a rule of its own:

> **Empty output is not evidence of absence.** Any scan that reports nothing must also report that it ran: what it examined, and how much of it.

An ad-hoc scan written the same morning reported zero name hits across 368 commits. The purpose-built instrument, run against the same history minutes later, found four names, two Tailscale addresses, a tailnet FQDN and three LAN addresses. The difference was not thoroughness. It was that one of them said what it had examined.

---

## How to run the check

When you write or review a rule:

1. **Name the occasion, then name the class.** What single case prompted this? What is the set that case belongs to? Write against the set. If you cannot state the set, you have not finished thinking — you have finished reacting.
2. **Find every literal.** A path, a name, a username, a remote, a filename, a count. Each one declares a set of one. Ask for each: *is this the class, or is this the example I happened to have?*
3. **Ask what is derived.** Names → handles, ids, filenames, slugs. One repo → every repo. Many files → one file. Capitalised → lowercased. HEAD → history. The working tree → the clone.
4. **Run a positive control.** Plant a violation and confirm the guard fires. This is the only step that catches the whole class, because it is the only one that does not trust a clean report. Do it after every change to a guard, not once when it is written.
5. **Report what ran, not only what was found.** A count of items examined turns a false negative into a visible one.

---

## The limit

Generalising has a cost, and the cost is real: a rule written against the widest possible class is usually vague, often unenforceable, and sometimes wrong in ways the specific version was not. *Guard against all sensitive strings* is not better than *guard against this list of names*; it is worse, because it cannot be executed.

The limit, then, is not *always generalise*. It is:

**Generalise one step, deliberately, and say which step you did not take.**

An exception you have recorded is a decision. An exception nobody has counted has stopped being one — which is why an exceptions list, if a practice has one, prints its size on every run.

And where the class genuinely cannot be enumerated, prefer the shape that fails safe: an **allowlist** names the one destination permitted to carry the material, where a blocklist silently exempts every destination nobody thought of. That is this scroll's principle applied to itself — a blocklist covers the destinations it names, and nothing derived.

---

## For the Spirit

The failure mode is not carelessness. Every one of these fifteen was written attentively, by someone looking straight at a real defect. The narrowness came *from* the attention: fixing what is in front of you is the correct instinct, and it produces a rule shaped like the thing in front of you.

So the discipline is not to try harder at the moment of writing. It is to add one question afterward — *what is the case beside this one?* — and then to distrust the clean report until something has proved the instrument can still see.

Three of the day's instances were in code written that same day, to fix the first four. Writing this scroll does not exit the pattern either. The check is the exit, run each time.

---

*Four separate guards reported clean. The repository was not clean. Each guard was right about the case it had been told about, and silent about the one beside it.*
