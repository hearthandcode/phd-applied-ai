# Manual Workflow Guide

How to run any curriculum generation phase without Claude Code or the Workflow tool.
Use this when you have Cursor, OpenRouter, or Ollama but not Claude Code.

---

## When to use this

- You're on a machine without Claude Code installed
- You want to generate one module at a time (not all 18 at once)
- You're using a cheaper model via OpenRouter and want to control cost per module
- You want to test the prompts with Ollama or another local model

---

## Phase B: Generate one module (single-module manual mode)

**What Phase B produces for each module:**
- `foundations.md` — ground-floor primer: symbol reference card, axiom unpacking, subspace
  operational descriptions, concept dependency map, memorability hooks (NEW REQUIRED FILE, GENERIC)
- `theory.md` — doctoral-level theoretical content (2000–3000 words, GENERIC)
- `reading-list.md` — updated with archive docs + external sources (GENERIC)
- `project/README.md` — updated with concrete project deliverables (GENERIC)
- `project/hc-connection.md` — H&C-specific connection (project-specific, forks replace this)
- `resources.md` — updated with additional resources identified

> CONTENT SEPARATION RULE: theory.md, reading-list.md, and project/README.md must be
> generic and useful to any AI/ML researcher. H&C-specific content goes ONLY in
> project/hc-connection.md. This keeps the curriculum forkable.

### Step 1: Read the module spec

Open `curriculum/overview.md` and find the module. Note: module ID, phase, calibration target, archive coverage, par hours.

Open the existing `modules/MXX-slug/theory.md` — it has the front matter with all context.

### Step 2: Paste this prompt into any model (Claude, GPT-4o, Llama 3.3, etc.)

```
You are generating doctoral-level content for an Applied AI PhD curriculum module.
This curriculum is designed for self-directed learners at the doctoral research level.
Content should be rigorous, specific, and assume mathematical maturity.

CONTENT SEPARATION RULE:
- theory.md, reading-list.md, and project/README.md must be GENERIC: useful to any
  AI/ML researcher regardless of their specific project or thesis.
- All project-specific and thesis-specific content goes ONLY in project/hc-connection.md.
  This keeps the curriculum forkable for other researchers.

MODULE METADATA:
- Module ID: M[XX]
- Title: [Module Title]
- Phase: [0-5]
- Par hours: [XX] (study time at a sustainable pace)
- Calibration target: [from theory.md front matter]
- Archive coverage: [from theory.md front matter]
- Language: [Python / Python + Haskell / etc.]
- Tags: [from theory.md front matter]

Generate the following for this module:

## theory.md content

Write doctoral-level theoretical content covering:
1. Core foundations and formal definitions
2. Mathematical framework (include equations where relevant, in LaTeX or plain notation)
3. Key algorithms or methods with pseudocode where applicable
4. Theoretical limits and open problems
5. Connection to adjacent modules in the curriculum

CONCEPTUAL BRIDGE RULE (required): Before every formal definition, theorem, or derivation,
write 2–4 sentences that build intuition using metaphor, imagery, or physical/spatial analogy.
Answer "what does this concept feel like to work with?" before stating what it formally is.
Pattern per subsection: intuition paragraph → formal definition → worked example → ML significance.
Use geometric and spatial language throughout (describe what transformations *do* to space).
Dense symbolic exposition without semantic grounding creates working memory overload —
especially for neurodivergent learners. Conceptual bridges are not optional decorations;
they are load-bearing scaffolding for comprehension.

CONCRETE WORKED EXAMPLE RULE (required): After every formal definition or theorem, include a
specific numerical example — a real matrix with actual numbers, a traceable dimensional
scenario, or a step-by-step calculation the reader can verify by hand or in a notebook.
Prefer ML-grounded scenarios: "a 512→64 weight matrix has null space of dimension at least 448,
meaning any two inputs differing only in those 448 directions are indistinguishable after the layer"
is the target level of specificity. Vague examples ("consider a large matrix") are not sufficient.
Pattern per subsection: intuition bridge → formal definition → worked example with numbers →
ML significance. The worked example makes the theorem real; it is not optional or decorative.

SYMBOL DEFINITION RULE (required): Every symbol appearing for the first time in theory.md
must be defined in plain English immediately after its first use. Format: "$x \in V$ (meaning:
x is an element of the set V)". Never assume ∈, ⊆, ℝⁿ, 𝒞, 𝒩, ∀, ∃, etc. are self-evident.

OPERATIONAL DESCRIPTION RULE (required): Every subspace definition must include three parts:
(a) formal set definition, (b) geometric description (what it looks like as a subspace in
low dimensions — a line, plane, hyperplane, or all of space), (c) operational reading (what
the matrix "does" that this subspace captures). In particular: 'b ∈ C(A)' must be explained
as "the machine can output b"; 'N(A) = {0}' as "no non-zero input is erased — different inputs
always give different outputs."

MEMORABILITY HOOK RULE (required): After every major theorem or definition, include one
"Memorability hook:" sentence — a single image or phrase that allows the reader to reconstruct
the definition from scratch. E.g., "Memorability hook: Rank-nullity says what a map uses and
what it destroys must sum to the input dimension. Nothing is created."

FOUNDATIONS.MD (required, separate file): Before writing theory.md, generate foundations.md
— a ground-floor primer that: anchors to what the learner already knows, defines every symbol
used in theory.md in a reference table, unpacks every algebraic structure axiom-by-axiom with
a "what breaks without this" column, gives triple descriptions (formal + geometric + operational)
for every subspace, shows a concept dependency map (which concepts build on which), provides
memorability hooks for each major idea, walks through 1–2 derivations step-by-step with
narration at each step, and explicitly connects each structure to where it appears in ML.
foundations.md is read BEFORE theory.md. It is GENERIC (no H&C refs). It is the accessible
entry point; theory.md is the rigorous reference.

Target length theory.md: 2,500–3,500 words. foundations.md: 1,500–2,500 words. Use ## subheadings.
Do not write survey-level content — write at the depth where a reader could implement
or critique a paper in this area.
DO NOT embed H&C, Hearth & Code, or thesis-specific references here.

## reading-list.md additions

List 5–8 seminal or foundational papers/books for this module.
Format:
- [Author(s) (Year). "Title." Venue/Publisher.] — one sentence on why this is essential reading.
Generic annotations only — no project-specific framing.

## project/README.md deliverable section

Describe a concrete project that demonstrates competency in this module.
Requirements:
- Uses [Language from metadata]
- Can be completed in [par_project_hours] hours
- Produces a runnable artifact (notebook, script, or CLI tool)
- GENERIC: any AI/ML researcher should be able to complete this, not just Scott
- Has a clear "done" state (not open-ended)

Format as: Goal, Deliverables (bulleted list), Evaluation criteria.

## project/hc-connection.md (CREATE THIS FILE)

This is the ONLY place for H&C-specific content. Write:
- How this module's content connects to the Hearth & Code adaptive learning platform
- Specific H&C applications (adaptive difficulty, competency modeling, learner profiling,
  gamification, neurodiversity support, AI tutoring, etc.)
- Which of these research questions this module most directly informs:
  RQ1: adaptive AI competency trajectory modeling
  RQ2: pedagogical frameworks for generative AI tutors
  RQ3: computational virtue/vice models for motivation
  RQ4: governance for AI assessment at scale
  RQ5: neurodiverse learner trajectory data
- 2–4 paragraphs, specific and actionable

LEARNER-CENTERED DESIGN RULES (apply to both foundations.md and theory.md):
- PRE-READING MAP: Every file opens with an ordered 8–12 item list of what the reader will
  encounter in that file, in order. Primes working memory. Not a table of contents — an active
  preview written as full phrases.
- MEMORY TIERS (required section in foundations.md): Sort all content into three explicit tiers:
  CARRY (5–7 items — the minimum conceptual hooks to internalize; write as phrases not formulas),
  RECONSTRUCT (5–10 items — can derive from first principles with time; key theorem skeletons,
  derivation logic), LOOK UP (8–12 items — exact formulas, API calls, proof details; reader
  should NOT memorize these, just know where to find them).
- CHECKPOINTS (3–5 inline per file): Mid-file pause markers that say "Checkpoint: if this is
  sitting right, you can say [X] without looking. If not, re-read [Y]." These are ADHD save
  points — complete ideas at which the reader can stop and return.
- MICRO-EXERCISES (5–10 in foundations.md, 2–3 in theory.md): Inline 5–15 min tasks immediately
  after the concept they test. Format: "> **Try this:** [task]. [Expected result/check]."
- "EXPLAIN OUT LOUD" PROMPTS (2–3 per foundations.md): Ask reader to explain the last concept
  without looking, as if to a friend. Activates recall over re-reading.
- SECTION RECAPS: Every ## section ends with 2–3 bullets "What we just established."
- CROSS-MODAL QUAD: Every major concept in foundations.md needs all four: METAPHOR (narrative/
  analogy), GEOMETRY (spatial description or ASCII diagram), SYMBOL (formal definition),
  EXERCISE (micro-task). Don't privilege any one modality as the "real" explanation.

Return output clearly labeled: ## foundations.md, ## theory.md, ## reading-list additions, ## project/README.md deliverable, ## project/hc-connection.md
```

### Step 3: Copy output into the module files

- Copy `## theory.md` content → paste into `modules/MXX-slug/theory.md` after the front matter
- Add reading list entries to `modules/MXX-slug/reading-list.md`
- Update `modules/MXX-slug/project/README.md` with the deliverable section
- CREATE `modules/MXX-slug/project/hc-connection.md` with the H&C connection content
- Update the front matter `status:` from `pending` to `generated`

### Step 4: Update audit

Add a row to `AUDIT_LOG.md`:
```
| [date] | [Module ID] | manual-generation | Generated via [model name] | — |
```

---

## Phase B: Full batch mode (if your model supports long context)

If using Claude (200k context) or GPT-4o (128k), you can generate all 18 Phase B modules in one prompt by:

1. Paste the full `curriculum/overview.md` (Phase 0 + Phase 1 sections)
2. Paste all 18 existing `theory.md` front matters
3. Use the same prompt above but add: "Generate content for all 18 modules listed above. Use the same format for each, labeled ## M01, ## M02, etc."

This produces a very long response. Copy each section to the appropriate file.

---

## Committee sessions (any model)

The committee advisors are in `committee/<name>/PERSONA.md`. Each file is a complete system prompt.

**To start a session:**
1. Open the relevant `PERSONA.md`
2. Set it as the system prompt in your chat interface
3. Begin the conversation as yourself (the student)

**Works with any model that supports system prompts:**
- OpenRouter: system prompt field in playground
- Ollama: `/system [paste PERSONA.md]` then start chatting
- Cursor: paste PERSONA.md as first message labeled "SYSTEM:"
- ChatGPT: paste as first message, ask it to adopt the role

**Example session opener (works with any advisor):**
```
[After setting PERSONA.md as system prompt]

I've just completed the theory section of M07: Computability Theory.
My current competency self-assessment is level 2 (can explain concepts, struggle with proofs).
I'd like to discuss the relationship between the halting problem and the expressiveness limits 
of modern LLMs. Can you push back on my current understanding?
```

---

## Oral exam (any model)

After completing a module, use this prompt for any model:

```
You are a doctoral committee member conducting an oral examination on [Module Title].
The student has studied this module for [X] hours and self-assessed at competency level [1-4].

Conduct a 20-minute oral examination. Ask 4–6 questions that probe:
1. Fundamental understanding of core concepts
2. Ability to derive or prove key results
3. Ability to apply concepts to novel problems
4. Awareness of limitations and open problems
5. Connection to adjacent areas

Be rigorous. Do not accept vague answers. Ask follow-up questions.
Start with a question now.
```

---

## Choosing a model for each task

| Task | Minimum model | Recommended |
|---|---|---|
| Theory Q&A | Llama 3.2 3B (Ollama) | Claude 3.5 Sonnet / GPT-4o |
| Full module generation | GPT-4o (128k) | Claude 3.5 Sonnet (200k) |
| Committee session | Llama 3.3 70B (Ollama) | Claude 3.5 Sonnet |
| Oral exam | Llama 3.3 70B (Ollama) | GPT-4o |
| Social post drafting | Any | Any |
| Blog post draft | Llama 3.3 70B | Claude 3.5 Sonnet |
