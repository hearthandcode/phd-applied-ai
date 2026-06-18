# Hermes Curriculum Verification Rubric — v1

**Synthesized from established open standards:**
- [LORI 1.5](https://edutechwiki.unige.ch/en/Learning_Object_Review_Instrument) — Nesbit, Belfer & Leacock (2004). *Learning Object Review Instrument.* 9 dimensions, empirically validated.
- [Achieve OER Rubrics](https://www.achieve.org/files/AchieveOERRubrics.pdf) — Achieve (2011). *Rubrics for Evaluating Open Education Resources.* 8 criteria, publicly funded, US standards-aligned.
- [OERTrust Framework](https://www.researchgate.net/publication/323882739_Quality_Assurance_for_Open_Educational_Resources_The_OERTrust_Framework) — Mayrberger, Zawacki-Richter & Müskens (2018). *Quality Assurance for OER.* Pedagogical + technical dimensions.

**Adapted for:** AI-generated, self-directed doctoral curriculum with cognitive profile parameterization (L001).

---

## Scoring

Each dimension: **0 (absent)** → **3 (meets standard)** → **5 (exemplary)**

A section must score ≥ 3 on ALL dimensions to pass verification. Any dimension scoring ≤ 2 generates an automatic FLAG requiring human review.

---

## Dimension 1: Content Quality (LORI §1 · Achieve §2)

*Veracity, accuracy, balanced presentation of ideas, appropriate level of detail.*

| Score | Criteria |
|-------|----------|
| 5 | All claims are correct and verifiable. Mathematical theorems are stated with precise conditions. No hallucinations. Level of detail matches doctoral depth (MIT 18.06 calibration). |
| 3 | Claims are generally correct. Minor imprecision in edge cases. Level of detail is appropriate but may occasionally oversimplify. |
| 1 | Factual errors present. Hallucinated citations. Detail level inappropriate for doctoral study. |

**Verification prompt for Haiku:**
> "Check every theorem, definition, and claim in this section against established mathematical/CS knowledge. Flag anything that is incorrect, imprecise, or hallucinated. Be especially strict on citation of named theorems."

---

## Dimension 2: Learning Goal Alignment (LORI §2 · Achieve §1)

*Alignment among learning goals, activities, assessments, and learner characteristics.*

| Score | Criteria |
|-------|----------|
| 5 | Every exercise, recap, and assessment directly supports stated learning goals. Goals are specific, measurable, and calibrated to the module's phase. |
| 3 | Most exercises align with goals. Some activities may be tangentially related. Goals are stated but could be more specific. |
| 1 | Poor alignment between goals and content. Exercises test different material than what was taught. |

**Verification prompt for Haiku:**
> "Does every exercise and activity in this section directly test material the section actually taught? Are the stated learning goals specific enough to measure mastery?"

---

## Dimension 3: Cognitive Load Calibration (LORI §3 · Adapted)

*Appropriate scaffolding for the learner's working memory profile (L001: high sensitivity). Formalism density target: 0.4.*

| Score | Criteria |
|-------|----------|
| 5 | Conceptual bridges precede every formal definition (≥1 bridge/definition). Formalism density is approximately 40% symbolic, 60% intuition. Python exercises are the primary assessment modality. |
| 3 | Some bridges present but not systematic. Formalism density may drift to 50-60%. |
| 1 | Dense symbolic exposition with minimal scaffolding. Paper-only exercises. No working memory accommodations. |

**Verification prompt for Haiku:**
> "Count the conceptual bridge paragraphs before formal definitions. Is there at least one bridge per definition? What percentage of the section is symbolic notation vs. prose intuition? Are exercises computational (Python)?"

---

## Dimension 4: Memory Tier Design (LORI §3 · Adapted)

*Seven CARRY items, ten RECONSTRUCT items, remainder as LOOKUP. Tiered retrieval practice.*

| Score | Criteria |
|-------|----------|
| 5 | Exactly 7 CARRY items (the most essential). 7-10 RECONSTRUCT items (derivable). LOOKUP items are clearly reference material. Tiers are pedagogically sound — learner truly needs to internalize CARRY items. |
| 3 | Tiers present but counts may be off (8-9 CARRY, unrelated RECONSTRUCT). Most tier assignments are reasonable. |
| 1 | No memory tiers. All content treated as equally important. No guidance on what to internalize vs. reference. |

**Verification prompt for Haiku:**
> "Are there exactly 7 CARRY items? Are these truly the 7 most essential concepts the learner must memorize forever? Do the RECONSTRUCT items make sense as derivable rather than memorized?"

---

## Dimension 5: Interaction Design & Motivation (LORI §4 · §6 · Achieve §3)

*Ability to motivate the learner. Explain-out-loud prompts, cross-modal questions, and interaction prompts for both Hermes and Claude. Ease of navigation.*

| Score | Criteria |
|-------|----------|
| 5 | Every section ends with "Try this in Hermes" AND "Try this in Claude" prompts. Explain-out-loud prompts appear mid-section. Navigation between sections is clear via the unified TOC. |
| 3 | Interaction prompts present but may be generic. Some sections missing prompts. Navigation is functional but could be clearer. |
| 1 | No interaction prompts. Passive reading only. No navigation guidance. |

**Verification prompt for Haiku:**
> "Does every section have both a 'Try this in Hermes' and 'Try this in Claude' interaction prompt? Are there explain-out-loud prompts mid-section? Can the learner navigate between sections easily?"

---

## Dimension 6: Assessment Quality (Achieve §4 · QM §3)

*Quality of assessment. Pretest/posttest alignment. Mastery-based progression indicators.*

| Score | Criteria |
|-------|----------|
| 5 | Section-level assessment items directly test CARRY and RECONSTRUCT items. Module-level pretest and posttest exist. Clear mastery thresholds. |
| 3 | Some assessment items present but may not align with CARRY/RECONSTRUCT tiers. Module-level assessment exists but lacks thresholds. |
| 1 | No assessment items. No way to verify learner mastery. |

**Verification prompt for Haiku:**
> "Does this section have a way for the learner to verify they've mastered the material? Do exercises match the CARRY and RECONSTRUCT items stated?"

---

## Dimension 7: Cross-Module Consistency (Achieve §1 · Extended)

*Definitions, notation, and theorems are consistent across sections and with adjacent modules. Forward references are accurate.*

| Score | Criteria |
|-------|----------|
| 5 | Notation is uniform across all 17 sections of M01. Forward references to M02-M23 are accurate and specific. No contradictory definitions. |
| 3 | Most notation is consistent. Minor inconsistencies across sections. Forward references are vague but not wrong. |
| 1 | Notation changes between sections. Forward references are inaccurate or hallucinated. |

**Verification prompt for Haiku:**
> "Check notation consistency across all sections. Does `A` mean the same thing in sections 1 and 6? Are forward references to M02 (Calculus) and M23 (Transformers) accurate?"

---

## Dimension 8: Code Correctness (Extended · Computational Requirement)

*All Python/NumPy code blocks compile and produce correct output. No synthetic results.*

| Score | Criteria |
|-------|----------|
| 5 | All code blocks are syntactically valid. Comments explain what each block demonstrates. Outputs are correct for the stated problem. |
| 3 | Most code blocks are correct. Minor issues (e.g., undefined variable, wrong import). Comments may be sparse. |
| 1 | Code has syntax errors. Outputs are hallucinated (no actual run). Code doesn't demonstrate what it claims. |

**Verification prompt for Haiku:**
> "Review every Python code block. Is the syntax valid? Would it run without errors? Does the code actually demonstrate the mathematical concept it claims to show?"

---

## Dimension 9: Accessibility (LORI §7 · Achieve §8 · QM §8)

*Support for the learner's specific accessibility needs. ADHD-friendly formatting (short sections, clear headings, concrete next actions).*

| Score | Criteria |
|-------|----------|
| 5 | Short sections (< 400 lines). Clear hierarchical headings. Every section ends with a concrete next action. No spatial-diagram dependencies (operational descriptions instead). |
| 3 | Moderate section lengths. Headings present but could be clearer. Some spatial language used. |
| 1 | Long, undifferentiated walls of text. Heavy spatial/visual dependency. No concrete closure. |

**Verification prompt for Haiku:**
> "Is this section short enough to be read in one sitting (< 400 lines)? Are headings clear and hierarchical? Does the section avoid relying on spatial diagrams? Does it end with a concrete next action?"

---

## Dimension 10: Open Research Framing (Achieve §7 · Extended)

*Open problems and research frontiers are correctly framed. Known unknowns are distinguished from settled science.*

| Score | Criteria |
|-------|----------|
| 5 | Open problems are clearly labeled as "active research" or "unsolved." Speculation is flagged as such. References to "current research" cite actual directions. |
| 3 | Most open problems are correctly framed. Occasional overconfidence about unsettled questions. |
| 1 | Open questions presented as settled science. Speculation presented as fact. Hallucinated "current research" directions. |

**Verification prompt for Haiku:**
> "Are any claims about 'open problems' or 'active research' actually settled science? Is speculation clearly flagged? Could a reader distinguish what's known from what's debated?"

---

## Automation

This rubric is applied by Haiku via Claude Code CLI:

```bash
claude -p "$(cat verification-prompt.txt)" --model haiku --output-format json --max-turns 30
```

The prompt embeds all 10 dimensions with the specific verification questions listed above. The output is a structured JSON report with per-section PASS/FLAG/FAIL and a confidence score (0.0-1.0) for each dimension.

---

## References

- Nesbit, J. C., Belfer, K., & Leacock, T. (2004). *Learning Object Review Instrument (LORI 1.5)*. E-Learning Research Group, Simon Fraser University.
- Achieve (2011). *Rubrics for Evaluating Open Education Resource (OER) Objects.* Washington, DC: Achieve.org.
- Mayrberger, K., Zawacki-Richter, O., & Müskens, W. (2018). *Quality Assurance for Open Educational Resources: The OERTrust Framework.* In: Handbook of Open, Distance and Digital Education. Springer.
- Quality Matters (2023). *Higher Education Rubric, Seventh Edition.* MarylandOnline. [Proprietary — referenced for architecture, not reproduced]