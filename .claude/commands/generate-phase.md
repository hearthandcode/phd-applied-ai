Launch full content generation for a curriculum phase. This is the manual-mode equivalent of running a Workflow script — generates all modules in a phase one at a time with full context.

Phase: $ARGUMENTS
(Format: "B" for Phase B (M01-M18), "C" for Phase C (M19-M42), etc.)

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
   c. Generate doctoral-level theory.md body content (see /generate-module for the full spec)
   d. Generate reading-list.md additions (5–8 sources)
   e. Generate project/README.md deliverable section
   f. Update the module's front matter: status: generated, updated: today
   g. Report: "M[XX] [title] — done. [X/Y] modules complete."
4. After all modules: update curriculum/overview.md status fields for this phase.
5. Log to AUDIT_LOG.md: Phase [X] generation complete, model used, date.

**Note:** For phases B–D (many modules), this is a long operation. If you want to generate one module at a time, use /generate-module M01 instead.

**Cost awareness:** Full phase generation requires large context. Prefer Claude 3.5 Sonnet (200k) or GPT-4o (128k via OpenRouter) over smaller models.
