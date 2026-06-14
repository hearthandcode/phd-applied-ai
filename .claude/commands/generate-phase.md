Launch full content generation for a curriculum phase. This is the manual-mode equivalent of running a Workflow script — generates all modules in a phase one at a time with full context.

Phase: $ARGUMENTS
(Format: "B" for Phase B (M01-M18), "C" for Phase C (M19-M42), etc.)

> CONTENT SEPARATION RULE (fork-friendliness):
> theory.md must be completely generic — useful to any AI/ML learner, regardless of their
> project or thesis. Do NOT embed Hearth & Code, H&C, or thesis-specific references in
> theory.md or reading-list.md. Project-specific content belongs ONLY in project/hc-connection.md.
> For every module: CREATE project/hc-connection.md as a separate file alongside project/README.md.

Phase map:
- A: Scaffold only (already complete — run Workflow script phd-phase-a.js instead)
- B: M01–M18 (Math + CS Fundamentals, ~1.8M tokens)
- C: M19–M42 (ML + Advanced AI, ~2.8M tokens)
- D: M43–M61 (Specialized Research, ~2.3M tokens)
- E: M62–M67 (Thesis + Defense, ~600k tokens)

Instructions:
1. Parse the phase letter from $ARGUMENTS.
2. Read curriculum/overview.md to get the module list for this phase.
3. For each module in the phase, in sequence:
   a. Read the module's existing theory.md (front matter gives calibration target, tags, archive_coverage)
   b. If archive MCP tools are available: run kg_search("<module title>") to pull archive docs
   c. Generate foundations.md (ground-floor primer, new required file — see /generate-module for full
      spec). Required sections: "What you already know" anchor, symbol reference card, axiom-by-axiom
      table with "what breaks without this" column for every algebraic structure, subspace triple
      descriptions (formal + geometric + operational), concept dependency map, memorability hooks,
      derivation walk for 1–2 key results, ML connections for each structure. GENERIC — no H&C refs.
   d. Generate generic theory.md body content (see /generate-module for the full spec — no H&C refs).
      Include CONCEPTUAL BRIDGES: 2–4 sentence intuition/metaphor paragraph before every formal
      definition or theorem. Answer "what does this feel like?" before "here is the formal statement."
      Use geometric and spatial language. Dense formalism without semantic grounding loses learners,
      especially neurodivergent readers. Bridges are required, not optional.
      Include CONCRETE WORKED EXAMPLES after every formal definition or theorem: a specific
      numerical case (actual matrix dimensions, real numbers, traceable calculation) that makes the
      theorem tangible. Prefer ML-grounded scenarios: weight matrices, embedding dimensions,
      attention scores, singular value spectra, loss-surface curvature. Pattern per subsection:
      intuition bridge → formal definition → worked example with numbers → ML significance.
      Examples must be specific enough to verify by hand — "a 512→64 weight matrix destroys exactly
      448 dimensions" rather than "a weight matrix discards some information." Not decorative; load-bearing.
   d. Generate reading-list.md additions (5–8 sources, generic annotations)
   e. Generate project/README.md deliverable section (generic, any researcher can complete it)
   f. CREATE project/hc-connection.md — H&C-specific application of this module's content,
      including which RQs it informs and specific platform use cases
   g. Update the module's front matter: status: generated, updated: today
   h. Report: "M[XX] [title] — done. [X/Y] modules complete."
4. After all modules: update curriculum/overview.md status fields for this phase.
5. Log to AUDIT_LOG.md: Phase [X] generation complete, model used, date.

**Note:** For phases B–D (many modules), this is a long operation. If you want to generate one module at a time, use /generate-module M01 instead.

**Cost awareness:** Full phase generation requires large context. Prefer Claude 3.5 Sonnet (200k) or GPT-4o (128k via OpenRouter) over smaller models.
