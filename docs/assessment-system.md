---
type: design-spec
title: M01 Assessment System and AI-Generated Content Verification Protocol
status: APPROVED
created: 2026-06-18
author: Scott Rallya + Claude (collaborative design session)
applies_to: All PhD curriculum modules, starting with M01-linear-algebra
decision: Approach B (three-layer) implemented; Approach C (knowledge graph) deferred to post-M18
---

# M01 Assessment System and AI-Generated Content Verification Protocol

**Status:** APPROVED — Design session 2026-06-18  
**Artifacts:** `modules/M01-linear-algebra/assessment/` · `modules/M01-linear-algebra/verification-log.md`  
**Next action:** Complete Layer 3 cascade pre-registration predictions in `assessment/layer1-items.md` and commit before beginning any M01 study session.

---

## Purpose

Two problems to solve:

1. **Quantifiable learning outcomes.** Without pre/post measurement, all competency claims are retrospective and unverifiable — invalid for longitudinal N=1 research.
2. **Auditable content quality.** A 67-module AI-generated curriculum accumulates errors. Without systematic verification, those errors propagate into research data.

This spec defines the architecture for both.

---

## Part 1: Three-Layer Assessment Structure (Approach B)

### Layer 1 — Standardized Recall (External sourced)

**Purpose:** Establish a pre-registered baseline that cannot be influenced by knowing what the assessment will ask.  
**Source:** External — MIT 18.06 problem sets, Strang "Introduction to Linear Algebra" exercises, standard textbook problems. Questions must be sourced, not AI-generated.  
**Format:** 8–12 items per module. Short-answer or exact-recall. Scored 0–3 per item.  
**Timing:** Pre-test before any study; post-test after module completion; optional mid-point.  
**Pre-registration requirement:** Layer 1 items finalized and committed to git before study begins. No modifications after study starts. The commit hash is the timestamp evidence.  
**File:** `modules/M01-linear-algebra/assessment/layer1-items.md`

### Layer 2 — Integration Probes (Custom, generative)

**Purpose:** Capture structural/spatial encoding — the understanding that survives when specific facts fade. Measures knowledge integration, not just acquisition.  
**Source:** Designed per module based on key conceptual transitions.  
**Format:** 4–6 open-ended items. Self-scored using a rubric or qualitative description. Evidence of prior knowledge restructuring is the target.  
**Key question types:**
- Spatial/relational explanation: "Draw or describe the relationship between X and Y"
- Cascade trace: "Why does concept X require concept Z? What breaks without Z?"
- Surprise capture: "What in this module most changed something you thought you already understood?"
- Novel application: "Generate an example of X that isn't in any material you studied"
- Meta-cognitive: "Which concept can you explain fluently vs. only reproduce mechanically?"

**Timing:** Post-test only (no meaningful pre-test for integration). Optional written reflection during study.  
**File:** `modules/M01-linear-algebra/assessment/layer1-items.md` (L2 section)

### Layer 3 — Cascade Pre-Registration

**Purpose:** Operationalize the spiral curriculum as a forward prediction problem. Generates quantitative data on conceptual dependency awareness.  
**Mechanism:** Before beginning study, predict which M01 concepts will reappear as prerequisites in M02 and M03. Write predictions. After those modules complete, score accuracy.  
**Why this works:** Predictions must precede outcomes — confirmation bias cannot reverse-engineer which concept "mattered most" after the fact. The prediction is itself a research instrument.  
**Format:** Free text predictions committed to git before study begins.  
**File:** `modules/M01-linear-algebra/assessment/layer1-items.md` (L3 section)

### Assessment Scoring Summary

| Layer | Type | Source | Pre-test | Post-test | Scored by |
|-------|------|---------|----------|-----------|-----------|
| L1: Recall | Standardized | External (Strang/18.06) | Yes | Yes | Rubric (objective) |
| L2: Integration | Custom | Internal (generative) | No | Yes | Qualitative self |
| L3: Cascade | Pre-registered | Internal (forward prediction) | Yes (predictions) | Deferred | Prediction accuracy post-M02/M03 |

---

## Part 2: Five-Type Claim Verification Protocol

### Taxonomy

| Type | Description | Verification method | Automatable |
|------|-------------|---------------------|-------------|
| Mathematical facts | Theorems, formulas, numerical results | First-principles derivation or CAS (SymPy, Wolfram) | ~70% |
| Code correctness | Code examples and implementations | Execute and test in local environment | ~95% |
| Pedagogical claims | "Research shows X improves learning" | Literature lookup + abstract scan | ~30% |
| Citations/references | Named papers, books, authors, dates | DOI lookup, publication existence check | ~80% |
| Metaphor accuracy | Analogies and informal explanations | Extension test: does the analogy hold beyond the stated case? | ~60% |

### Verification Workflow per Module

1. **Claim extraction pass** — read module content, flag claims by type, log to `verification-log.md`
2. **Automated pass** — run code; look up citations via DOI; run CAS for key formulas
3. **Manual pass** — pedagogical claims (~2–4 per module), hard math proofs, metaphor extension tests
4. **Disposition** — each claim marked: VERIFIED / FLAGGED / CORRECTED / EXCLUDED

### Automation Infrastructure

- Code correctness: run in local Python / Julia environment; write test assertions
- Citations: DOI lookup via CrossRef API (free, curl-accessible); confirm abstract matches claimed content
- Mathematical facts: SymPy for routine algebra; manual for theorems requiring proof
- Metaphor accuracy: write the extension case and check if the analogy still holds; fail if it breaks unexpectedly

### Feasibility Analysis

| Parameter | Value |
|-----------|-------|
| Module count | 67 |
| Estimated manual minutes per module | 26–33 min |
| Total manual hours | ~30–40 hrs |
| Concurrent with study? | Yes — ~15 min per study session |

Total manual verification burden across all 67 modules is approximately 30–40 hours. This is not a gate before studying — it runs in parallel. The bottleneck category is pedagogical claims (~30% automatable); all other types are majority-automatable.

**Five-year timeline viability:** Confirmed achievable. Verification is not a bottleneck given automation leverage.

---

## Part 3: Decision Record — Approach B over Approach C

### Approach C (Knowledge Graph Architecture) — Deferred to post-M18

**What it is:** Build a graph database encoding the conceptual dependency network of the entire curriculum. Each module is a subgraph; edges encode "concept A is prerequisite for concept B." Assessment generates graph traversal data; knowledge state is a colored subgraph with probabilistic node weights (Bayesian Knowledge Tracing).

**Why it's better eventually:**
- Quantitative graph-theoretic measures of knowledge completeness
- Bayesian Knowledge Tracing integration
- Enables knowledge space theory validation (requires ~3+ completed modules for calibration)
- Dramatically richer longitudinal data for the PhD research contribution

**Why it's deferred:**
- Requires graph DB setup, schema design, and custom tooling before any studying begins
- Creates an architecture-building trap: infrastructure work generates engagement sufficient to delay study indefinitely
- Knowledge space theory only yields meaningful signal after M03 at earliest
- Approach B can migrate to Approach C: Layer 3 cascade pre-registrations are the forward edge predictions that seed a knowledge graph

### Migration Path from B to C

| Milestone | Action |
|-----------|--------|
| Through M01–M03 | Continue with Approach B; bank all L3 predictions |
| After M03 | Extract L3 cascade predictions as preliminary edge list; sketch graph schema |
| After M06 | Evaluate: does L3 data show patterns worth quantifying rigorously? |
| If yes (after M06) | Build graph schema; backfill M01–M06 data; switch to graph-native assessment from M07 |
| If no | Continue Approach B; revisit after M12 |

**Decision criteria for migration:** If L3 cascade accuracy data by M06 shows structure predictable enough to model, invest in the graph. If patterns are weak or noisy, continue Approach B.

---

## Part 4: AI-Generated Content Risk Architecture

### The AI Psychosis Risk

RLHF-trained models have structural bias toward user satisfaction. For a learner with Bipolar history (including psychosis), this bias can amplify into false insight loops: the AI validates learner output, which registers as external confirmation, which reinforces potentially distorted self-assessment. This is a research integrity issue with a clinical risk component, not just an epistemic concern.

### Structural Defenses

1. **Pre-registration (primary defense):** Assessment questions and cascade predictions committed to git before study begins. Cannot be reverse-engineered post-hoc.
2. **External sourcing for L1:** Recall items sourced from published textbooks, not AI-generated. Independence from the AI content pipeline is guaranteed.
3. **Adversarial prompting:** Periodic sessions where the model is explicitly instructed to find flaws, not validate. Schedule at module completion, not reactively.
4. **Verifiable cross-checks:** Code runs or doesn't. Citations exist or don't. Mathematical derivations check out or they don't. These categories resist sycophancy structurally.
5. **Disclosure in THESIS.md:** Conflict of interest (AI generates curriculum content, AI assists research analysis) is documented. Methodological limitations stated explicitly.

### Unresolved Risk

Pedagogical claims (~30% automatable) remain the highest-risk category for echo-chamber effects. "Research shows X improves learning" is easy to fabricate plausibly and hard to verify quickly. Mitigation: treat all pedagogical claims as provisional until literature-verified; use `verification-log.md` to track their explicit status throughout the research period.
