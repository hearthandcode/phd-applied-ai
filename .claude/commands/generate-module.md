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

**theory.md body** (after the existing front matter):
- Doctoral-level exposition, 2,500–3,500 words
- ## subheadings for major sections
- Formal definitions with notation
- Mathematical derivations where applicable (use plain LaTeX: $E = mc^2$)
- Key theorems and proofs (or proof sketches)
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
