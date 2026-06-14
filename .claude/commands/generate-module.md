Generate full doctoral-level content for a single module. Use when Phase B workflow hasn't run yet or needs to be re-run for one module.

Module: $ARGUMENTS

> CONTENT SEPARATION RULE (fork-friendliness):
> theory.md must be completely generic — useful to any AI/ML learner, regardless of their
> project or thesis. Do NOT embed Hearth & Code, H&C, or thesis-specific references in
> theory.md or reading-list.md. Project-specific content belongs ONLY in project/hc-connection.md.

Instructions:
1. Read modules/$ARGUMENTS-*/theory.md (front matter has calibration target, archive coverage, tags, language).
2. Read curriculum/overview.md to understand the module's place in the sequence.
3. Read modules/$ARGUMENTS-*/reading-list.md and resources.md for any existing context.
4. If archive MCP tools are available, run: kg_search("<module title>") and kg_fts_search("<key concepts from tags>") to pull relevant archive documents.
5. Generate the following content:

**foundations.md** (CREATE this file — the ground-floor primer, read BEFORE theory.md):

This file exists for learners who need to build the module's concepts from scratch rather than
absorb them from a formal definition downward. It is the reference implementation of every
pedagogical rule listed below. Required sections:

LEARNER-CENTERED DESIGN RULES (apply universally — every module, every file):
These rules are designed for neurodivergent learners (ADHD, working memory constraints,
variable focus, multi-modal processing) but improve the material for all learner types.
They are not optional additions — they are part of the minimum quality bar.

  PRE-READING MAP: Every file begins with an ordered list (8–12 items) of exactly what
  the reader will encounter, in order. Not a table of contents — an active preview that
  primes working memory. E.g., "1. What a field is and its 11 arithmetic rules / 2. What
  a vector space is and why the rules matter / 3. Three non-standard vector spaces...".

  MEMORY TIERS (required in foundations.md, one dedicated section near the end):
  Explicitly sort all module content into three tiers:
  - CARRY (5–7 items only): The minimum the reader must internalize. Conceptual hooks,
    recognition patterns, when-to-use triggers. If you internalize nothing else, internalize
    these. Write them as short phrases — intuitions, not formulas.
  - RECONSTRUCT (5–10 items): Understand the structure, know the skeleton — can derive
    from first principles given time and a whiteboard. These include the key theorem proofs
    (sketch level), the logic of major derivations, and "why this formula has this shape."
  - LOOK UP (everything else): Formulas, API calls, proof details, implementation specifics.
    Have a reference handy and don't spend energy memorizing. List 8–12 specific items that
    belong here so the reader knows explicitly what NOT to memorize.

  CHECKPOINTS (3–5 per file, inline): Explicit pause markers mid-file — not chapter breaks,
  but short callouts saying: "Checkpoint: this is a complete idea. If it's sitting right,
  you can say [X] in your own words. If not, re-read [Y paragraph/section]." These are
  save points for cognitive load. The reader can stop at a checkpoint and return later.

  MICRO-EXERCISES (5–10 in foundations.md, 2–3 in theory.md): Embedded small tasks
  (5–15 min each) that verify understanding in the moment, not just one big project.
  ALL EXERCISES MUST BE COMPUTATIONAL: every exercise includes a Python code block
  (NumPy for numerical verification, SymPy for symbolic derivation). Paper-and-pencil
  is not assumed or required — the computer is the workspace. Format:
    > **Try this:** [conceptual question — what are we testing?]
    > ```python
    > import numpy as np  # or sympy
    > # [starter code — set up the problem, leave the key computation for the learner to complete or run]
    > # Expected output: [what they should see]
    > ```
  Distribute throughout, immediately after the concept they test. Do NOT cluster at the end.
  Computational exercises let the learner change numbers and observe what changes —
  this builds intuition faster than paper derivation and fits a code-first workflow.

  "EXPLAIN IT OUT LOUD" PROMPTS (2–3 per foundations.md): Explicit pauses asking the
  reader to explain the last concept without looking, as if talking to a friend. These
  activate recall rather than re-reading, which is more durable for memory formation.

  SECTION RECAPS (end of every ## section): 2–3 bullet "What we just established" before
  moving to the next section. Allows working memory to consolidate before new load.

  CROSS-MODAL QUAD: Every major concept in foundations.md must be represented in all four
  modes, not just one. Pattern:
  - METAPHOR: a narrative or everyday analogy (linguistic/verbal channel)
  - GEOMETRY: what it looks like spatially; use ASCII art when helpful (visual/spatial)
  - SYMBOL: the formal definition (symbolic/logical)
  - EXERCISE: a micro-task to do with it (kinesthetic/project-based)
  A learner who only processes well in one modality should still fully grasp the concept.
  Do not assume the symbolic representation is the "real" one and the others are decoration.

- **What you already know** (2–3 paragraphs): anchor to everyday intuition the learner already
  has. E.g., for linear algebra: "You already add numbers and scale them. Linear algebra is
  what happens when you do that to *anything* — arrows, functions, neural network weights."
- **Symbol reference card**: every symbol used in theory.md defined in plain English and
  pronunciation. Format: | Symbol | Pronunciation | Plain-English Meaning |
- **Algebraic structures from the inside out** (for any field, group, ring, or vector space
  introduced): (a) what kinds of objects live here, (b) what operations you can do, (c)
  AXIOM-BY-AXIOM TABLE with columns: Axiom Name | Formal statement | Plain English | Everyday
  analogy | What breaks without it. (d) 2–3 concrete examples of the structure, (e) 1–2
  non-examples (things that look like the structure but fail one axiom).
- **Subspace triple description** (for every subspace introduced): (a) formal set definition,
  (b) geometric picture (what it looks like as a line/plane/subspace in low dimensions),
  (c) operational reading ("what does the matrix DO that this subspace captures?"). In
  particular: "b ∈ C(A)" must be explained as "the machine can output b"; "N(A) = {0}" as
  "different inputs always give different outputs — no blind spots."
- **Concept dependency map**: a textual graph showing how the module's concepts build on each
  other, e.g. "Fields → Vector spaces → Subspaces → Linear independence → Dimension →
  Rank-nullity → Eigendecomposition → SVD". Each arrow means "you need this to define the next."
- **Memory tiers section** (CARRY / RECONSTRUCT / LOOK UP — see learner-centered rules above)
- **Memorability hooks**: for each major definition/theorem, one sentence that lets the
  reader reconstruct the concept from scratch. E.g., "Eigenvector hook: the directions a
  matrix can't rotate — only stretch."
- **Derivation walk** (for 1–2 key formulas): step-by-step derivation of a major result with
  one-line narration at each step explaining *why* this algebraic move is being made.
- **Connections to ML**: for each algebraic structure, 2–3 sentences on exactly where the
  learner will encounter this in ML. E.g., "Vector spaces: a neural network layer Wx+b
  lives in a vector space — W is a linear map, x is a vector, the operations follow all
  8 axioms you just saw."
- 5–10 micro-exercises, 2–3 checkpoints, 2–3 "explain it out loud" prompts (see above)
- GENERIC: no H&C-specific content here. Fork-friendly.

**theory.md body** (after the existing front matter):
- Doctoral-level exposition, 2,500–3,500 words
- ## subheadings for major sections
- CONCEPTUAL BRIDGE before every formal definition or theorem: 2–4 sentences using
  metaphor, imagery, or spatial/physical analogy that answers "what does this feel like
  to work with?" BEFORE the symbolic definition. Pattern: intuition → formal statement →
  worked example → ML significance. Dense symbol sequences without semantic grounding
  create cognitive load spikes — especially for neurodivergent learners. Not optional.
- Formal definitions with notation
- Mathematical derivations where applicable (use plain LaTeX: $E = mc^2$)
- Key theorems and proofs (or proof sketches)
- CONCRETE WORKED EXAMPLE after every formal definition or theorem: a small matrix with
  actual numbers, a specific dimensional scenario (e.g., "a 512→64 weight matrix destroys
  exactly 448 dimensions — meaning any two inputs differing only in those 448 directions
  are indistinguishable after the layer"), or a step-by-step traceable calculation.
  Examples must be specific enough to verify by hand or in a notebook. Prefer ML-grounded
  scenarios (weight matrices, embeddings, loss surfaces, attention scores) over pure
  mathematical abstractions. The example makes the theorem real — it is not decorative.
- Geometric and visual language throughout: describe what transformations *do* to space,
  not just what they *are* symbolically
- FIRST SYMBOL USE: every symbol appearing for the first time in theory.md must be
  defined in plain English immediately after its first use. Format: "$x \in V$ (meaning:
  x is an element of the set V)". Never assume symbols are self-evident.
- OPERATIONAL DESCRIPTIONS for all subspaces: every subspace definition must include the
  operational reading ("what does the matrix machine DO that this captures?") not just the
  set definition.
- DEPENDENCY CALLOUTS: every major definition must include a one-sentence explicit backward
  link ("This builds on: linear independence") and forward link ("We'll need this in: SVD").
- MEMORABILITY HOOKS: after each major theorem, one sentence — a single memorable image or
  phrase that reconstructs the theorem. E.g., "Rank-nullity hook: what a matrix uses and
  what it destroys must sum to its input dimension. Nothing is created."
- Limitations and open problems
- Connection to adjacent curriculum modules
- GENERIC: any AI/ML doctoral learner should find this useful — no H&C-specific content here

**project/README.md** (update the TBD sections):
- Concrete project deliverable using the module's language
- Clear "done" state
- 3–5 evaluation criteria
- GENERIC: the deliverable should be completable by any researcher, not just Scott

**project/hc-connection.md** (CREATE this file alongside project/README.md):
- How this module's content connects to the Hearth & Code adaptive learning platform
- Specific H&C applications (adaptive difficulty, competency modeling, learner profiling, etc.)
- Which research questions (RQ1–RQ5) this module most directly informs
- THIS is the only file in the module where H&C-specific content belongs
- Forks replace this file with their own project connection file

**reading-list.md** (add to existing):
- 5–8 seminal papers/books
- One sentence per item: why it matters for this module specifically
- GENERIC: no H&C-specific framing in annotations

6. Write each section to the correct file.
7. Update theory.md front matter: status: generated, updated: [today]
8. Log to AUDIT_LOG.md: generation event with model name if known.
9. Say: "M[XX] content generated. Run /module-review when you've read it."
