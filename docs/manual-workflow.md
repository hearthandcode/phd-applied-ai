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

Target length: 2,500–3,500 words. Use ## subheadings. Be specific and rigorous.
Include concrete examples. Do not write survey-level content — write at the depth
where a reader could implement or critique a paper in this area.
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

Return output clearly labeled: ## theory.md, ## reading-list additions, ## project/README.md deliverable, ## project/hc-connection.md
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
