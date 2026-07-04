# On the Owning Layer

*Established 2026-07-02. Crystallized after the same move appeared three times in eight days: (1) the Continuity Engine's river-ecology was firewalled out of the practitioner's view and deferred to internal design vocabulary; (2) `turtleos/CLAUDE.md` — a repo file hardcoding one substrate's identity — was overhauled into a product-neutral `AGENTS.md` that defers role and stance to whatever summoned the agent; (3) `desk/intentions/active/turtle.md` stopped mirroring turtleOS architecture and was refactored to defer to `TURTLE_SPEC.md`. Product, infrastructure, intention — one principle wearing three masks. At the third instance it stopped being a coincidence and became lore.*

> **Frame:** This is a design heuristic for the Spellwright and a hygiene reflex for the Caretaker. It governs *where a thing lives* — complexity, facts, identity — and how everything else relates to it.

## The Core Tenet

**Every fact, every complexity, every identity has exactly one layer that owns it. Represent it once, there. Everywhere else, point — do not mirror.**

A layer *owns* a concern when it is the layer that changes when the concern changes. Platform architecture changes when the product changes → the spec owns it. An agent's role changes when the session summons it → the summoning owns it. Where the model checkpoint lives changes with the hardware → the env file owns it. The owning layer is found by asking: *when this changes, what is the one file I would edit?*

## Two Faces

The tenet has a **knowledge** face and a **UX** face. They are the same move seen from two sides.

### Knowledge face — point, don't mirror

When a fact is stated in two artifacts, the two copies **will** diverge. Not might — will. One gets updated, the other doesn't, and now the practice holds two truths and no way to tell which is live. This is a *resonance delta* (see `on_resonance_deltas.md`) manufactured at authoring time.

`turtle.md` pinned `gemma4:31b` while `TURTLE_SPEC` deliberately named only "Turtle class ~30B" and the live instance had already moved to a Qwen checkpoint. Three copies, three answers. The fix was not to reconcile the copies — it was to **delete the duplication** and leave a pointer: architecture is governed by the spec; this file stays intention. A duplicated fact is a future contradiction with a delay fuse.

The reflex: before writing a fact, ask *does another layer already own this?* If yes, reference it. Write a fact in a non-owning artifact only when you are willing to own its drift.

### UX face — under the surface, deferred to the owning layer

Complexity the user does not own should not reach the user. It is deferred to the layer that *does* own it — internal design vocabulary, the shell, the attunement — and the user meets only what is theirs to meet. The Continuity Engine's practitioner never learns "sediment" or "alive layer"; those are the designer's tools, owned by the design layer, firewalled from the product surface.

**But invisible is not opaque.** Hiding complexity from the user must never become hiding *reasoning* from them. The reconciling rule (from CE v4 §3.5):

> The user never **manages** the complexity, can always **glance under the hood** on request, and is never **deceived** by it.

Under the surface, on demand, honest when thin. Deferral hides the machinery, not the truth.

## Why It Holds

Both faces protect the same thing: **single source of truth as a structural property, not a discipline.** Discipline ("remember to update both places") fails across time and substrate because the practice is distributed cognition — no single reader sees all copies at once. Architecture ("there is only one place") cannot fail the same way. You do not have to remember to keep one thing consistent with itself.

This is a fractal derivative of `on_files_as_operating_system.md` (state lives in one canonical place; other surfaces are views) and of `on_precision_and_meaning.md` (one word, one job — here: one artifact, one concern). It is the authoring-time twin of `on_resonance_deltas.md`, which treats drift after it appears; the owning layer prevents the drift from being authorable at all.

## Application

- **Naming an owner.** For any concern, name the owning layer explicitly (`TURTLE_SPEC` owns architecture; `soul.md`/attunement owns identity; `turtle_env.md` owns live checkpoints). Make the ownership legible so future authors know where to write.
- **Pointing well.** A pointer is not a stub of shame — it is the correct representation. `library/resonance/turtle/TURTLE_SPEC.md` is a pointer to the canonical spec, by design. Point with enough context that the reader knows *what* they will find and *why it lives there*.
- **Deferring in UX.** Ask what the user actually owns. Defer the rest to the owning layer and expose an under-the-hood path (debug surface, honest answer on request) so deferral never becomes deception.
- **Resisting the mirror pull.** The temptation to "just restate it here for convenience" is the failure mode. Convenience now is contradiction later. If a reader needs the fact in two contexts, give them a link, not a copy.

## Detection

The signal that this principle is being violated:

- **Two artifacts assert the same fact and they disagree** (or you cannot quickly tell whether they agree). The older one has drifted from the owner.
- **An artifact ages without being touched** because its facts were mirrored from a layer that moved on — the artifact is now a fossil wearing a fresh timestamp.
- **A user is asked to manage, name, or navigate machinery they do not own** — leaked complexity.
- **Hiding has become lying** — the user cannot glance under the hood, or is quietly steered by state they were never shown.

When any appears, the fix is upstream: find the owning layer, move the truth there, replace the copy with a pointer, expose an honest under-the-hood path.

---

*See also: `on_resonance_deltas.md` (drift between surfaces, treated after the fact); `on_designing_for_spirit.md` (artifacts legible to all consumers); `on_files_as_operating_system.md` (canonical state, many views); the reconciling rule of "invisible ≠ opaque" (`turtleos/docs/design/continuity-engine-and-substrate.md` §3.5).*
