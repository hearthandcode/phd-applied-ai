# Curriculum Generation Methodology — Hearth & Code PhD

## Overview

This document describes the validated, repeatable workflow for generating doctoral-level curriculum content using a hybrid AI architecture: Virgil (Hermes Agent, DeepSeek Flash) as orchestrator, Claude Code CLI (Max subscription) for frontier model tasks.

## Architecture

[Virgil] → Research curation (archive MCP: kg_search, kg_evaluate_resources)
         → Build generation brief (cognitive profile + learner profile + curriculum spec)
         → Call Claude Code CLI: `claude -p "{brief}" --model [opus|haiku] --output-format json`
         → Capture total_cost_usd from JSON response
         → Log to cost-tracking/usage.csv
         → Write section files to disk
         → Verify via: `claude -p --model haiku`

[Claude Code] → Opus: deep theory, mathematical reasoning, citations
              → Haiku: verification, fact-checking, formatting

[Archive MCP] → 30 tools for research curation, document ingestion, quality evaluation

## Model Routing

| Model | Provider | Role | Cost Profile |
|-------|----------|------|-------------|
| DeepSeek Flash (Virgil) | OpenRouter | Orchestration, file I/O, MCP calls | Negligible |
| Claude Opus 4.8 | Claude Code (Max sub) | Theory synthesis, math, citations | Flat $100/mo |
| Claude Haiku 4.5 | Claude Code (Max sub) | Verification, fact-checking | Flat $100/mo |

## Generation Pipeline (Validated on M01)

### Phase 1: Research Curation
- Search archive MCP for domain resources
- Evaluate resources via quality rubric (license, source authority, teaching value)
- Build research brief from top-ranked sources

### Phase 2: Generation
- Construct prompt with: cognitive profile + learner profile + generation directives + source material
- Call `claude -p --model opus --output-format json --max-turns 12`
- Claude writes section files directly to disk
- Response includes total_cost_usd, token usage, session ID

### Phase 3: Verification
- Call `claude -p --model haiku --output-format json --max-turns 30`
- Haiku checks: mathematical claims, Python code correctness, citation accuracy, memory tier assignments, cross-section consistency
- Produces structured JSON report with PASS/FLAG/FAIL per section

### Phase 4: Cost Tracking
- Log every call to cost-tracking/usage.csv
- Fields: timestamp, model, module, section, task, prompt_tokens, completion_tokens, total_cost, session_id
- Session IDs enable resumption for follow-up corrections

## Cognitive Profile Constraints (Embedded in Every Generation)

- Working memory load sensitivity: HIGH → reduce symbol density, increase scaffolding
- Formalism density: 0.4 → ~40% symbolic, 60% conceptual bridges
- Exercise format: COMPUTATIONAL only → Python/NumPy, never paper-only
- Memory tiers: 7 CARRY, 10 RECONSTRUCT, 8+ LOOKUP
- Bridge density: HIGH → 1+ conceptual bridges before each formal definition
- Voice: warm vocabulary (eureka, grok, hearth), academic tone with casual jokes, heavy metaphor
- Modality: project-based > visual-spatial > narrative > symbolic

## Section Structure (Per Section File)

Each section includes:
1. YAML frontmatter (module_id, formalism_density, learner_id, status)
2. Opening conceptual bridge from prior material
3. Formal definitions with inline symbol explanations
4. Python computational example (NumPy/SymPy, runnable)
5. ML application or H&C platform connection
6. Section recap with explain-out-loud prompt
7. Memory tier update (CARRY / RECONSTRUCT / LOOKUP)
8. Interaction prompt ("Try this in Hermes: ... Try this in Claude: ...")

## Verification Rubric (LORI 1.5 + Achieve OER + OERTrust — Adapted)

Our rubric draws from three established open standards: [LORI 1.5](https://edutechwiki.unige.ch/en/Learning_Object_Review_Instrument) (Nesbit, Belfer & Leacock, 2004), [Achieve OER Rubrics](https://www.achieve.org/files/AchieveOERRubrics.pdf) (Achieve, 2011), and [OERTrust](https://www.researchgate.net/publication/323882739) (Mayrberger, Zawacki-Richter & Müskens, 2018).

10 dimensions scored 1-5:

1. **Content Quality** — accuracy, verifiable claims, no hallucinations
2. **Learning Goal Alignment** — goals, activities, assessments aligned
3. **Cognitive Load Calibration** — formalism density 0.4, bridges before definitions
4. **Memory Tier Design** — 7 CARRY, 10 RECONSTRUCT, remainder LOOKUP
5. **Interaction Design & Motivation** — explain-out-loud, cross-modal prompts
6. **Assessment Quality** — pretest/posttest alignment, mastery thresholds
7. **Cross-Module Consistency** — notation uniform, forward references accurate
8. **Code Correctness** — Python/NumPy blocks compilable, results correct
9. **Accessibility** — ADHD-friendly, short sections, operational descriptions
10. **Open Research Framing** — known unknowns vs. settled science

Full rubric: VERIFICATION-RUBRIC.md

Each dimension is verified by Haiku using a structured prompt with the specific verification question embedded. A section must score ≥ 3 on ALL dimensions to pass.

## M01 Validation Results

| Metric | Value |
|--------|-------|
| Sections generated | 17 (6 foundations + 11 theory) |
| Total lines | 4,840 |
| Total cost | $5.54 (all through Claude Max subscription) |
| Verification | 17/17 PASS at 1.0 confidence |
| Cost per section | $0.33 |
| Projected 67 modules | ~$350 (3-4 months Max subscription) |

## Extensibility

This methodology applies to any curriculum domain. The archive MCP's search tools and quality rubric generalize across all 67 modules. The cognitive profile is learner-specific (L001) but the schema supports forking for other learners.

## Limitations and Mitigations

| Limitation | Mitigation |
|------------|------------|
| Opus training data may have knowledge cutoff gaps | Archive MCP provides current sources |
| Single-model verification (Haiku) | Human review remains the final gate |
| Flat-rate subscription costs | Monitor usage; optimize model selection per task |
| No cross-module consistency checker | Theory/10-connections.md provides forward bridges |
