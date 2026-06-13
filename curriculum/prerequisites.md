---
type: curriculum-overview
schema_version: "1.0"
created: 2026-06-13
updated: 2026-06-13
---

# Module Prerequisites and Dependency Map

This document is the authoritative dependency reference for the PhD Applied AI curriculum.
It covers all 67 modules across 6 phases (Phase 0 through Phase 5).

---

## Prerequisites Table

| ID | Title | Phase | Prerequisites |
|----|-------|-------|---------------|
| M01 | Linear Algebra for ML | 0 | — |
| M02 | Multivariate Calculus and Optimization | 0 | — |
| M03 | Probability Theory and Bayesian Inference | 0 | — |
| M04 | Statistics and Statistical Learning | 0 | M03 |
| M05 | Information Theory | 0 | M03 |
| M06 | Graph Theory and Discrete Mathematics | 0 | — |
| M07 | Computability Theory and Formal Languages | 1 | M06 |
| M08 | Computational Complexity | 1 | M07 |
| M09 | Algorithm Design and Analysis | 1 | M06, M08 |
| M10 | Advanced Data Structures | 1 | M09 |
| M11 | Programming Language Theory | 1 | M07 |
| M12 | Type Theory and Dependent Types | 1 | M11 |
| M13 | Operating Systems and Systems Programming | 1 | M09 |
| M14 | Computer Networks and Distributed Systems | 1 | M13 |
| M15 | Database Systems and Theory | 1 | M09, M13 |
| M16 | Software Architecture Patterns | 1 | M15 |
| M17 | Software Engineering Methodology | 1 | M16 |
| M18 | Security Fundamentals | 1 | M14, M15 |
| M19 | Classical Machine Learning Algorithms | 2 | M01, M03, M04 |
| M20 | Statistical Learning Theory | 2 | M04, M19 |
| M21 | Neural Network Foundations | 2 | M01, M02, M19 |
| M22 | Convolutional and Recurrent Architectures | 2 | M21 |
| M23 | Attention Mechanisms and Transformer Architecture | 2 | M21, M22 |
| M24 | Optimization for Deep Learning | 2 | M02, M21 |
| M25 | Regularization, Generalization, and Overfitting | 2 | M20, M21 |
| M26 | Probabilistic Graphical Models | 2 | M03, M06, M19 |
| M27 | Reinforcement Learning Fundamentals | 2 | M03, M19 |
| M28 | Deep Reinforcement Learning | 2 | M21, M27 |
| M29 | LLM Architecture and Pretraining | 3 | M23, M24 |
| M30 | Fine-tuning, RLHF, and Alignment Techniques | 3 | M28, M29 |
| M31 | Generative Models: VAE, GAN, Diffusion | 3 | M21, M26 |
| M32 | Adversarial Machine Learning and Robustness | 3 | M21, M25 |
| M33 | Memory Systems and RAG Architecture | 3 | M29 |
| M34 | Multi-Agent Systems and Agentic AI | 3 | M29, M33 |
| M35 | AI Planning, Reasoning, and Symbolic AI | 3 | M07, M34 |
| M36 | Computer Vision and Multimodal AI | 3 | M22, M29 |
| M37 | Speech, Audio, and Multimodal Perception | 3 | M22, M29 |
| M38 | Knowledge Representation and Reasoning | 3 | M07, M35 |
| M39 | Causal Inference and Causality in ML | 3 | M03, M04, M19 |
| M40 | Interpretability and Explainability (XAI) | 3 | M21, M39 |
| M41 | AI Safety, Alignment, and Red-Teaming | 3 | M30, M40 |
| M42 | Frontier Research Methods and Practices | 3 | M29, M34, M41 |
| M43 | AI and Education (AIED) Foundations | 4 | M34, M47 |
| M44 | Intelligent Tutoring Systems | 4 | M43, M45 |
| M45 | Adaptive Learning Systems and BKT | 4 | M26, M43 |
| M46 | Curriculum Design Theory | 4 | M47, M58 |
| M47 | Instructional Design Methods | 4 | M58 |
| M48 | AI Literacy Frameworks | 4 | M43, M55 |
| M49 | AI Pedagogy and Teaching with AI | 4 | M43, M47, M48 |
| M50 | Gamification Theory and Game-Based Learning | 4 | M47, M58 |
| M51 | Educational Measurement and Assessment | 4 | M04, M45 |
| M52 | Affective Computing and Emotion Modeling | 4 | M26, M53, M58 |
| M53 | Computational Personality Modeling | 4 | M26, M58 |
| M54 | Value Alignment, Virtue, and Vice Modeling | 4 | M41, M52, M53, M55 |
| M55 | AI Ethics, Governance, and Policy | 4 | M40, M41 |
| M56 | Fairness, Accountability, and Transparency | 4 | M40, M55 |
| M57 | AI and Society: Policy, Economics, Labor | 4 | M55, M56 |
| M58 | Cognitive Science and Learning Theory | 4 | M03, M43 |
| M59 | HCI and Interface Design for AI-Native Learning | 4 | M50, M52, M58 |
| M60 | MLOps, AI Engineering, and Experiment Design | 4 | M19, M29, M39 |
| M61 | Neurodiversity, Mental Health, and AI-Mediated Learning | 4 | M44, M52, M58 |
| M62 | Research Methodology | 5 | M39, M42, M61 |
| M63 | Systematic Literature Review | 5 | M43, M44, M45, M62 |
| M64 | Thesis Proposal | 5 | M62, M63 |
| M65 | Original Research: H&C as Laboratory | 5 | M64 |
| M66 | Thesis Writing | 5 | M63, M64, M65 |
| M67 | PhD Defense: Preparation and Execution | 5 | M66 |

---

## Phase Gates

Each phase gate lists the modules that must be completed before any module in the next
phase can begin. These are derived from direct cross-phase prerequisite edges — if a
module in phase N requires a module from phase N-1 or earlier, that prior-phase module
is part of the gate.

### Gate into Phase 1 (from Phase 0)

| Required | Title |
|----------|-------|
| M06 | Graph Theory and Discrete Mathematics |

Phase 0 modules M01, M02, M03, M04, M05 have no direct dependents in Phase 1 and can
be completed concurrently with Phase 1 work, but they are required before Phase 2 begins.

### Gate into Phase 2 (from Phase 0)

All five of the following Phase 0 modules are direct prerequisites of Phase 2 modules:

| Required | Title |
|----------|-------|
| M01 | Linear Algebra for ML |
| M02 | Multivariate Calculus and Optimization |
| M03 | Probability Theory and Bayesian Inference |
| M04 | Statistics and Statistical Learning |
| M06 | Graph Theory and Discrete Mathematics |

Phase 1 modules are not direct prerequisites of any Phase 2 module and can be completed
in parallel with Phase 2, but they gate Phase 3 work.

### Gate into Phase 3 (from Phases 0–2)

| Required | From Phase | Title |
|----------|-----------|-------|
| M03 | 0 | Probability Theory and Bayesian Inference |
| M04 | 0 | Statistics and Statistical Learning |
| M07 | 1 | Computability Theory and Formal Languages |
| M19 | 2 | Classical Machine Learning Algorithms |
| M21 | 2 | Neural Network Foundations |
| M22 | 2 | Convolutional and Recurrent Architectures |
| M23 | 2 | Attention Mechanisms and Transformer Architecture |
| M24 | 2 | Optimization for Deep Learning |
| M25 | 2 | Regularization, Generalization, and Overfitting |
| M26 | 2 | Probabilistic Graphical Models |
| M28 | 2 | Deep Reinforcement Learning |

### Gate into Phase 4 (from Phases 0–3)

| Required | From Phase | Title |
|----------|-----------|-------|
| M03 | 0 | Probability Theory and Bayesian Inference |
| M04 | 0 | Statistics and Statistical Learning |
| M19 | 2 | Classical Machine Learning Algorithms |
| M26 | 2 | Probabilistic Graphical Models |
| M29 | 3 | LLM Architecture and Pretraining |
| M34 | 3 | Multi-Agent Systems and Agentic AI |
| M39 | 3 | Causal Inference and Causality in ML |
| M40 | 3 | Interpretability and Explainability (XAI) |
| M41 | 3 | AI Safety, Alignment, and Red-Teaming |

### Gate into Phase 5 (from Phases 3–4)

| Required | From Phase | Title |
|----------|-----------|-------|
| M39 | 3 | Causal Inference and Causality in ML |
| M42 | 3 | Frontier Research Methods and Practices |
| M43 | 4 | AI and Education (AIED) Foundations |
| M44 | 4 | Intelligent Tutoring Systems |
| M45 | 4 | Adaptive Learning Systems and BKT |
| M61 | 4 | Neurodiversity, Mental Health, and AI-Mediated Learning |

---

## Critical Path

The critical path is the longest chain of sequential dependencies from Phase 0 through
Phase 5. It contains **12 modules** and represents the minimum-duration spine of the
curriculum — no amount of parallel study can compress below this chain.

```
M03 → M04 → M19 → M21 → M22 → M23 → M29 → M30 → M41 → M55 → M56 → M57
```

| Step | ID | Title | Phase |
|------|----|-------|-------|
| 1 | M03 | Probability Theory and Bayesian Inference | 0 |
| 2 | M04 | Statistics and Statistical Learning | 0 |
| 3 | M19 | Classical Machine Learning Algorithms | 2 |
| 4 | M21 | Neural Network Foundations | 2 |
| 5 | M22 | Convolutional and Recurrent Architectures | 2 |
| 6 | M23 | Attention Mechanisms and Transformer Architecture | 2 |
| 7 | M29 | LLM Architecture and Pretraining | 3 |
| 8 | M30 | Fine-tuning, RLHF, and Alignment Techniques | 3 |
| 9 | M41 | AI Safety, Alignment, and Red-Teaming | 3 |
| 10 | M55 | AI Ethics, Governance, and Policy | 4 |
| 11 | M56 | Fairness, Accountability, and Transparency | 4 |
| 12 | M57 | AI and Society: Policy, Economics, Labor | 4 |

Note: M40 (Interpretability and Explainability) is an unlisted co-prerequisite of M41
alongside M30, and M28 (Deep Reinforcement Learning) is a co-prerequisite of M30
alongside M29. Both must be completed before M41 even though they are not on the
backbone chain shown above.

There is also a competing 12-step path through the thesis track:

```
M03 → M04 → M19 → M21 → M27 → M28 → M30 → M41 → M55 → ... → M61 → M62 → M67
```

The full thesis spine (M62 → M63 → M64 → M65 → M66 → M67) adds 6 more sequential
steps after the Phase 3–4 work and represents the true end-to-end completion path.

---

## Parallel Study Paths

The sections below describe which module groups are independent of each other within
each phase and can be studied concurrently.

### Phase 0 — Foundation Mathematics (4 independent tracks)

All Phase 0 modules can be started on day one. There are four independent threads:

| Track | Modules | Notes |
|-------|---------|-------|
| **Probability track** | M03, M04, M05 | M04 and M05 both require M03; study M03 first, then M04 and M05 in parallel |
| **Linear Algebra** | M01 | No dependencies; start any time |
| **Calculus** | M02 | No dependencies; start any time |
| **Discrete Math** | M06 | No dependencies; start any time |

M01, M02, M03, and M06 can all be opened simultaneously on day one.

### Phase 1 — Computer Science Foundations (1 connected component, multiple parallel branches)

All Phase 1 modules trace back to M07, so the entire phase forms one connected graph.
Within that graph, several branches diverge after M09 and can be studied in parallel:

- **Theory chain**: M07 → M08 → M09 (serial; no parallelism)
- **After M09, three parallel branches open**:
  - **Structures branch**: M09 → M10 (Advanced Data Structures)
  - **Systems branch**: M09 → M13 → M14, M15; M15 → M16 → M17; M14 + M15 → M18
  - **PL theory branch**: M07 → M11 → M12 (can start M11 as soon as M07 is done, in parallel with M08)

M10, M12, and M18 are the three terminal (leaf) modules of Phase 1 — they have no
Phase 1 dependents and can be completed in any order once their prerequisites are met.

### Phase 2 — Core ML and Deep Learning (diverging branches from a single root)

M19 is the sole entry point for Phase 2. Once M19 is complete, four branches open:

| Branch | Chain | Notes |
|--------|-------|-------|
| **Statistical theory** | M19 → M20 → M25 | M25 also requires M21 |
| **Deep learning spine** | M19 → M21 → M22 → M23; M21 → M24 | M23 also requires M22; M24 is parallel to M22 after M21 |
| **PGM** | M19 → M26 | Fully independent after M19 |
| **RL** | M19 → M27 → M28 | M28 also requires M21 |

M20 and M21 can both start immediately after M19 and are independent of each other.
M26 and M27 can also both start after M19 independently of the M21 chain.
M24 and M22 are independent siblings after M21.
M28 converges the neural (M21) and RL (M27) branches.
M25 converges the statistical (M20) and neural (M21) branches.

### Phase 3 — Advanced AI (3 independent clusters, several parallel branches)

Phase 3 has three independent entry points:

| Entry group | Modules | Prerequisite from prior phase |
|-------------|---------|-------------------------------|
| **LLM/Agent cluster** | M29, M31, M32, M33, M34, M35, M36, M37, M38, M39, M40, M41, M42 | M23+M24 gate M29; M21+M26 gate M31; M21+M25 gate M32; M03+M04+M19 gate M39 |
| **Generative models** | M31 | M21, M26 — fully independent of the LLM cluster within Phase 3 |
| **Robustness** | M32 | M21, M25 — fully independent of the LLM cluster within Phase 3 |

Within the main LLM/Agent cluster, parallel branches exist:

- M29 → M33 → M34 → M35 → M38 (agent/reasoning chain)
- M29 → M30; M39 → M40; both → M41 (alignment spine — M30 and M40 are parallel prereqs of M41)
- M29 → M36 and M29 → M37 (multimodal branches, fully parallel with each other)
- M39 → M40 can start as soon as M39 is done, independently of M29/M30

M31 and M32 have no intra-phase dependencies on any other Phase 3 module and can run
in parallel with the entire LLM cluster from Phase 3 day one.

### Phase 4 — Applied AI, Education, and Ethics (2 independent clusters)

Phase 4 splits into two fully independent clusters:

**Cluster A — Education, Cognition, and Ethics (18 modules)**

This cluster has two concurrent entry points once Phase 3 gates are met:

- **Ethics track** (entry: M55): M55 → M56 → M57; M55 → M54 (via M52, M53)
- **EdTech track** (entry: M43 via M34+M47; M47 requires M58; M58 requires M03+M43):
  Note — M43 and M58 are mutually dependent via M43 → M58 → M47 → M43, which
  is resolved because M43's cross-phase prereq (M34) and M58's cross-phase prereq
  (M03) both arrive from prior phases. Within Phase 4, M55 has no intra-phase
  prerequisites and is the practical entry point alongside M60.

Branches within Cluster A that can be pursued in parallel once M43 and M58 unblock:

| Branch | Chain |
|--------|-------|
| **Tutoring systems** | M43 → M45 → M44 → M61; M45 → M51 |
| **Instructional design** | M58 → M47 → M46, M50; M50 → M59 |
| **Personality/affective** | M26+M58 → M53 → M52 → M59, M61 |
| **Ethics/policy** | M55 → M56 → M57; M55+M52+M53 → M54 |
| **Literacy/pedagogy** | M43+M55 → M48 → M49 |

**Cluster B — Engineering (1 module)**

| Module | Entry condition |
|--------|----------------|
| M60 — MLOps, AI Engineering, and Experiment Design | M19, M29, M39 (all from prior phases) |

M60 is fully independent of every other Phase 4 module and can be completed any time
Phase 3 prerequisites are satisfied.

### Phase 5 — Research and Thesis (1 sequential chain)

Phase 5 is nearly linear once the gate modules are complete. M62 is the sole entry
point; all subsequent modules form a single sequential chain:

```
M62 → M63 → M64 → M65 → M66 → M67
```

M63 requires M43, M44, M45 in addition to M62, so the earliest Phase 5 work (M62
and completion of the M43–M45 cluster) can proceed in parallel before M63 opens.
After M63 is complete the chain is fully serial through to PhD defense.
