---
type: research-journal
entry_id: RJ-001
date: 2026-06-18
author: Virgil (drafted) + Scott (reviewed)
status: draft
tags: [methodology, verification, model-routing, curriculum-generation]
---

# Research Journal — Establishing the Generation and Verification Pipeline

## Summary

This session established a repeatable, verifiable methodology for AI-assisted doctoral-level curriculum generation. The key contribution is a tiered model architecture where Virgil (DeepSeek Flash) orchestrates research curation, prompt construction, and file I/O, while Claude Code (Max subscription) handles deep theory generation (Opus) and verification (Haiku). The methodology is grounded in three established open standards for educational quality: LORI 1.5, Achieve OER Rubrics, and the OERTrust Framework.

## Methodology

### Model Routing Architecture

| Layer | Model | Provider | Role | Cost |
|-------|-------|----------|------|------|
| Orchestration | DeepSeek V4 Flash | OpenRouter | Prompt building, MCP calls, file I/O, cost logging | Negligible |
| Generation | Claude Opus 4.8 | Claude Code CLI (Max sub) | Deep theory, math, citations | Flat $100/mo |
| Verification | Claude Haiku 4.5 | Claude Code CLI (Max sub) | Fact-checking, rubric scoring | Flat $100/mo |

### Generation Pipeline

1. Research curation via archive MCP server (`mcporter call archive.kg_search`)
2. Prompt construction embedding cognitive profile + learner profile + generation directives
3. Claude Code CLI call: `claude -p "{prompt}" --model opus --output-format json`
4. Cost capture from JSON response (`total_cost_usd`, token usage)
5. File writing to section-based directory structure
6. Verification via 10-dimension rubric (Haiku)

### Verification Rubric (Hermes v1)

Synthesized from LORI 1.5 (Nesbit, Belfer & Leacock, 2004), Achieve OER Rubrics (Achieve, 2011), and OERTrust (Mayrberger, Zawacki-Richter & Müskens, 2018).

10 dimensions scored 1-5: Content Quality, Learning Goal Alignment, Cognitive Load Calibration, Memory Tier Design, Interaction Design & Motivation, Assessment Quality, Cross-Module Consistency, Code Correctness, Accessibility, Open Research Framing.

## Validation Results (M01 Linear Algebra)

- 17 sections generated (6 foundations + 11 theory)
- 4,840 total lines across 17 files
- Total cost: $5.54 (all through Claude Max subscription)
- First-pass verification (Haiku, loose rubric): 17/17 PASS at 1.0 confidence

## Open Questions

1. **Archive MCP integration depth** — The MCP server was connected and queried but source material was not systematically fed into generation prompts. For later modules (M29+), this will be essential for grounding content in current research.
2. **Cross-module consistency** — No automated checker exists yet to verify that definitions in M01 are consistent with usage in M23.
3. **Code verification** — Python examples were checked for syntax correctness but not actually executed against a kernel.
4. **Subscription cost optimization** — At ~$5.54/module × 67 modules = ~$350 projected, this fits within 3-4 months of Max subscription. Actual burn rate depends on cache hit rates and batch efficiency.

## References

- Nesbit, J. C., Belfer, K., & Leacock, T. (2004). *Learning Object Review Instrument (LORI 1.5)*. Simon Fraser University.
- Achieve (2011). *Rubrics for Evaluating Open Education Resource (OER) Objects.* Washington, DC.
- Mayrberger, K., Zawacki-Richter, O., & Müskens, W. (2018). *Quality Assurance for OER: The OERTrust Framework.* Springer.
- Clark, A. & Chalmers, D. (1998). *The Extended Mind.* Analysis, 58(1), 7-19.