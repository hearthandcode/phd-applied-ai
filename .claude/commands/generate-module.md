Generate full doctoral-level content for a single module. Use when Phase B workflow hasn't run yet or needs to be re-run for one module.

Module: $ARGUMENTS

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
- Connection to the H&C platform adaptive learning use case
- Connection to adjacent curriculum modules

**project/README.md** (update the TBD sections):
- Concrete project deliverable using the module's language
- Clear "done" state
- 3–5 evaluation criteria
- Connection to H&C platform where possible

**reading-list.md** (add to existing):
- 5–8 seminal papers/books
- One sentence per item: why it matters for this module specifically

6. Write each section to the correct file.
7. Update theory.md front matter: status: generated, updated: [today]
8. Log to AUDIT_LOG.md: generation event with model name if known.
9. Say: "M[XX] content generated. Run /module-review when you've read it."
