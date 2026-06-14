---
type: slash-command
name: generate-theory-chunked
title: Generate theory.md section by section (chunked, parallel-ready)
domain: phd
accepts_args: true
args_description: "Module ID — e.g. M02"
created: 2026-06-14
updated: 2026-06-14
status: active
---

Generate theory.md for a module by extracting the topic list first, then generating each
topic section as an independent task. This avoids the quality degradation and hallucination
risk of single-call monolithic generation.

Module: $ARGUMENTS

---

## Step 1 — Extract the topic list

Read the following and DO NOT generate content yet:
- `modules/$ARGUMENTS-*/theory.md` front matter (calibration target, tags, archive coverage)
- `curriculum/overview.md` (module's place in the sequence and dependencies)
- `modules/$ARGUMENTS-*/resources.md` (key concepts)

Produce a structured topic list in this format — one line per topic, printed to the conversation
so Scott can review and adjust before generation begins:

```
TOPIC LIST for M[XX]: [Module Title]
─────────────────────────────────────
01. [Topic title] — [2-sentence description of what this section covers, what formal result it builds toward]
02. ...
...
NN. Open problems and connections — [preview of what this module feeds into next]

Total sections: NN  |  Target words/section: 500–700  |  Total theory.md: ~XXXX words
```

Wait for Scott to confirm the topic list before proceeding to Step 2.
He may reorder, add, remove, or rename topics. The topic list is the design artifact — 
it represents the module's argument structure, not just its contents.

---

## Step 2 — Generate each topic section independently

For EACH topic in the confirmed list, generate exactly one section with this structure:

```markdown
## [N]. [Topic title]

**[Conceptual bridge — 2–4 sentences of intuition, metaphor, or spatial language]**
Answer "what does this feel like to work with?" BEFORE the symbolic definition.

### Definition / Theorem

[Formal statement with notation. Define every symbol at first use: "$x \in V$ (x is an
element of V)". Include a one-sentence backward link ("This builds on: [prior topic]") and
forward link ("We'll need this for: [later topic]").]

### Worked example

[Concrete numbers. A specific matrix with actual values, a traceable calculation, or a
real ML scenario with dimensions stated. Must be specific enough to verify in a notebook.
Prefer ML-grounded scenarios: weight matrices, embeddings, attention scores, LoRA ranks.]

### ML significance

[2–4 sentences connecting this result to a real ML system or paper. Name the paper or
system. E.g., "This is the mathematical basis for LoRA (Hu et al., 2021)..." ]

### Memorability hook

> [One sentence that lets a reader reconstruct the concept from scratch. A single image
> or phrase. E.g., "Rank-nullity hook: what a matrix uses and what it destroys must sum
> to its input dimension. Nothing is created."]

---
```

**Generation rules (apply to every section):**
- CONTENT SEPARATION: theory.md is generic — useful to any AI/ML doctoral learner.
  No H&C, Hearth & Code, or thesis-specific references. Project content goes ONLY in
  `project/hc-connection.md`.
- FIRST SYMBOL USE: every new symbol defined inline at first appearance.
- OPERATIONAL DESCRIPTIONS: every subspace or mapping gets an operational reading
  ("what does the matrix machine DO that this captures?").
- DEPENDENCY CALLOUTS: explicit backward + forward links as specified above.
- MICRO-EXERCISES (2–3 in theory.md total, embedded after the section they test):
  ALL COMPUTATIONAL — Python/NumPy starter code, expected output, observation prompt.
  Do NOT cluster at the end.
- SECTION RECAP at end of every ## section: 2–3 "What we just established" bullets.
- CHECKPOINTS (2–3 in theory.md total): explicit pause markers with a self-assessment
  prompt. These go between sections at natural cognitive break points.

Generate topics one at a time (or request permission to generate multiple). After each
section, note: "Section [N] done — [topic title]. Ready for [N+1]?" so Scott can review
incrementally.

---

## Step 3 — Consistency review (after all sections)

After all sections are generated, run a consistency pass:

Read all generated sections and check:
1. **Notation consistency**: same symbol used for same thing throughout? No redefinitions?
2. **Terminology uniformity**: same term used for same concept? No synonym drift?
3. **Cross-reference accuracy**: forward/backward links name the right sections?
4. **Worked example coherence**: do the examples use compatible setups? (e.g., if §3 uses
   a 3×2 matrix, does §5 build on the same setup or introduce a new one unnecessarily?)
5. **Spec compliance**: every section has all required elements (bridge, formal, example,
   hook, recap)?
6. **Word count balance**: any section under 350 or over 900 words?

Report issues as a numbered list. Fix only what's flagged — do not regenerate whole sections.

---

## Step 4 — Stitch

Assemble the final `theory.md` in topic order with:
- The existing front matter (updated: [today], status: generated)
- A DOCUMENT-LEVEL pre-reading map at the top (10–12 items, ordered active preview)
- All sections in sequence
- A final "Connections to adjacent modules" section (3–5 bullet forward links)

Write to `modules/$ARGUMENTS-*/theory.md`.

Update `theory.md` front matter: `status: generated`, `updated: [today]`.
Log to `AUDIT_LOG.md` if it exists.

Say: "M[XX] theory.md generated in [N] sections. Run /phd-review M[XX] when you've read it."
