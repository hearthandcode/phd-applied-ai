---
type: curriculum-architecture
title: "Curriculum Architecture v2: 83-Module Applied AI Program for Governed Knowledge Work"
domain: research/learning
status: proposal
created: 2026-07-17
updated: 2026-07-17
tags: [curriculum, applied-ai, knowledge-organization, provenance, governance, synthesis, agents, accessibility, proposal]
graph_refs:
  - curriculum/overview.md
  - curriculum/prerequisites.md
  - docs/redesign-2026-07/2026-07-17_research-program-direction-changelog.md
llm_accessible: true
generated_by: curriculum-redesign
verified: false
extended:
  legacy_module_count: 67
  proposed_additive_module_count: 16
  candidate_total_module_count: 83
  target_duration_years: 7
  target_modules_per_year: "11-12"
---

# Curriculum Architecture v2: 83-Module Applied AI Program for Governed Knowledge Work

## Status and scope

**Proposal.** M01-M67 remain unchanged. M68-M83 are candidate metadata only. This document creates no module folder, content, prerequisite edge, scorecard row, par-hour estimate, or research finding.

## Design rules

1. Preserve M01-M67 as stable curriculum and audit infrastructure.
2. Use cross-cutting tracks and sequence windows rather than a renumbering campaign.
3. Require a reviewed source bank, objectives, assessment shape, artifact boundary, and public/private handling before a proposed module is scaffolded.
4. Keep database theory, RAG, formal knowledge representation, provenance, governance, synthesis, and knowledge lifecycle work distinct even where they interact.
5. Treat agency and accessibility as technical design requirements, not optional human-factors afterthoughts.
6. Do not use clinical inference as personalization. Accessible design and explicit self-report do not authorize hidden diagnosis or profiling.

## Candidate count and seven-year cadence

The candidate total is **83 modules**: 67 preserved modules plus 16 proposed additions. This averages 11.86 modules per year across seven years, represented as six twelve-module windows and one eleven-module thesis window before accounting for overlap, electives, revision loops, or real-world pacing.

| Year window | Candidate set | Count | Purpose |
|---|---|---:|---|
| Year 1 | M01-M12 | 12 | Mathematical, discrete, computational, and programming-language foundations. |
| Year 2 | M13-M24 | 12 | Systems, architecture, security, ML foundations, and deep-learning preparation. |
| Year 3 | M25-M36 | 12 | Generalization, probabilistic reasoning, RL, LLMs, RAG, agents, planning, and multimodality. |
| Year 4 | M37-M42, M55-M57, M68-M70 | 12 | Knowledge representation, causality, interpretability, safety, research practice, governance, and provenance. |
| Year 5 | M43-M49, M51, M58, M71-M73 | 12 | Learning as application, cognitive foundations, evidence synthesis, semantic engineering, and knowledge lifecycle design. |
| Year 6 | M50, M52-M54, M59-M61, M74-M78 | 12 | Bounded adjacent human/application work plus agentic engineering and cognitive-workbench interaction. |
| Year 7 | M62-M67, M79-M83 | 11 | Method, evaluation, thesis work, and human-theory/ethics/accessibility study. |

This is a sequence-window view, not a guarantee that every prerequisite is valid. The current prerequisite map has a Phase 4 cycle involving M43, M47, and M58. Resolve that existing cycle before a sequence governs study order.

## Cross-cutting tracks

| Track | Question it serves | Anchors |
|---|---|---|
| Applied AI and computational foundations | Can the researcher reason about and build AI systems rigorously? | M01-M42, M60 |
| Knowledge representation, organization, and retrieval | How are concepts, artifacts, and sources represented and found? | M15, M33, M38, M68, M72, M73 |
| Governed synthesis, provenance, and integrity | Can transformations, authority, review, and uncertainty remain visible? | M17-M18, M41, M55-M57, M69-M71, M77 |
| Agentic systems and human oversight | How can agents act, adapt, coordinate, and remain controllable? | M29, M34-M35, M41, M60, M74-M77 |
| Cognitive workbench, agency, and accessibility | Does the artifact reduce burden while preserving authorship and returnability? | M52, M58-M59, M61, M78, M80-M83 |
| Learning and developmental knowledge work | What can learning, literacy, and instructional design contribute as an application domain? | M43-M51 |
| Research and reflexive evaluation | Which methods and artifacts justify bounded claims? | M42, M62-M67, M71, M79 |

## Cross-cutting lenses, not extra modules

- **Executive function and cognitive accessibility** cross-cut M58, M59, M61, and M78. They are accessible-design and explicit-self-report concerns, not diagnostic or population-efficacy claims.
- **Motivation and self-regulation** cross-cut M50, M52, M58, and M62. M50 remains bounded elective/critique material, not a central causal theory or a reason to infer a person's state.

## Preserved M01-M67 inventory and role

### Technical core

| IDs | Modules |
|---|---|
| M01-M06 | Linear Algebra for ML; Multivariate Calculus and Optimization; Probability Theory and Bayesian Inference; Statistics and Statistical Learning; Information Theory; Graph Theory and Discrete Mathematics. |
| M07-M12 | Computability Theory and Formal Languages; Computational Complexity; Algorithm Design and Analysis; Advanced Data Structures; Programming Language Theory; Type Theory and Dependent Types. |
| M13-M18 | Operating Systems and Systems Programming; Computer Networks and Distributed Systems; Database Systems and Theory; Software Architecture Patterns; Software Engineering Methodology; Security Fundamentals. |
| M19-M28 | Classical Machine Learning Algorithms; Statistical Learning Theory; Neural Network Foundations; Convolutional and Recurrent Architectures; Attention Mechanisms and Transformer Architecture; Optimization for Deep Learning; Regularization, Generalization, and Overfitting; Probabilistic Graphical Models; Reinforcement Learning Fundamentals; Deep Reinforcement Learning. |
| M29-M42 | LLM Architecture and Pretraining; Fine-tuning, RLHF, and Alignment Techniques; Generative Models: VAE, GAN, Diffusion; Adversarial Machine Learning and Robustness; Memory Systems and RAG Architecture; Multi-Agent Systems and Agentic AI; AI Planning, Reasoning, and Symbolic AI; Computer Vision and Multimodal AI; Speech, Audio, and Multimodal Perception; Knowledge Representation and Reasoning; Causal Inference and Causality in ML; Interpretability and Explainability (XAI); AI Safety, Alignment, and Red-Teaming; Frontier Research Methods and Practices. |

### Specialization and application pathway

| IDs | Modules | Proposed role |
|---|---|---|
| M43-M49 | AI and Education (AIED) Foundations; Intelligent Tutoring Systems; Adaptive Learning Systems and BKT; Curriculum Design Theory; Instructional Design Methods; AI Literacy Frameworks; AI Pedagogy and Teaching with AI | Application pathway. |
| M50 | Gamification Theory and Game-Based Learning | Elective or case-study input. |
| M51 | Educational Measurement and Assessment | Application-method input. |
| M52 | Affective Computing and Emotion Modeling | Bounded adjacent interaction research. |
| M53 | Computational Personality Modeling | Elective/critique. |
| M54 | Value Alignment, Virtue, and Vice Modeling | Elective/critique. |
| M55-M57 | AI Ethics, Governance, and Policy; Fairness, Accountability, and Transparency; AI and Society: Policy, Economics, Labor | Promoted policy and social context. |
| M58-M61 | Cognitive Science and Learning Theory; HCI and Interface Design for AI-Native Learning; MLOps, AI Engineering, and Experiment Design; Neurodiversity, Mental Health, and AI-Mediated Learning | Promoted human-agency, interaction, implementation, and accessibility anchors. |
| M62-M67 | Research Methodology; Systematic Literature Review; Thesis Proposal; Original Research: H&C as Laboratory; Thesis Writing; PhD Defense: Preparation and Execution. | Core research and thesis route. |

## Proposed additive modules M68-M83

| ID | Candidate title | Distinct scope and boundary |
|---|---|---|
| M68 | Knowledge Organization, Metadata, and Information Architecture | Faceted classification, controlled vocabularies, metadata profiles, information architecture, and findability. It is not database-query optimization or formal reasoning alone. |
| M69 | Data Provenance, Lineage, and Reproducibility | Entities, activities, agents, derivations, receipts, reproducible transformations, and lineage queries. It does not equate documented lineage with source quality. |
| M70 | Knowledge Governance, Records, and Research Integrity | Authority, lifecycle, review, verification, retention, privacy/rights gates, policy-as-data, and correction paths. It is not a compliance checklist or a safety claim. |
| M71 | Evidence Synthesis, Argumentation, and Sensemaking | Claim-evidence mapping, uncertainty, contradiction handling, comparative reasoning, argument mapping, and synthesis artifacts. It differs from systematic-review procedure by focusing on ongoing knowledge work. |
| M72 | Knowledge Engineering, Ontology Design, and Semantic Interoperability | Conceptual models, ontologies, controlled relations, schema evolution, semantic mappings, and interoperability boundaries. It does not duplicate formal knowledge representation. |
| M73 | Knowledge Lifecycle, Curation, and Retrieval Evaluation | Capture, curation, maintenance, retention, review debt, collaborative knowledge management, and retrieval-quality evaluation. It differs from RAG runtime architecture. |
| M74 | Agentic Engineering and Tool-Using Systems | Agent runtime architecture, state, tool contracts, permission boundaries, retries, handoffs, sandboxing, and observability. It does not repeat LLM internals or planning algorithms. |
| M75 | Adaptive and Self-Improving Agent Systems | Bounded adaptation, memory update, evaluators, feedback loops, rollback, and anti-drift controls. It explicitly rejects unbounded autonomous self-modification. |
| M76 | Multi-Agent Orchestration and Collective Intelligence | Role separation, task graphs, coordination, communication, delegation, resource budgets, conflict handling, escalation, and termination. It goes beyond basic multi-agent taxonomy. |
| M77 | Agent Evaluation, Verification, and Governance | Task rubrics, adversarial testing, approval paths, provenance, incident handling, safety cases, and trajectory/tool evidence. It is not a static leaderboard module. |
| M78 | Cognitive Workbench Interaction, Accessibility, and Continuity | External memory, interruption recovery, context recovery, agency-preserving interaction, accessible modality, and local-first ergonomics. It does not infer cognition from telemetry. |
| M79 | Evaluation of AI-Augmented Knowledge Work | Design-science evaluation, trace-based artifact analysis, recovery measures, source-quality rubrics, correction load, and bounded comparative designs. |
| M80 | Extended and Distributed Cognition | Extended, distributed, embedded, and socially situated cognition; coupling criteria; reliability and failure conditions. It is a contested theoretical lens, not evidence that AI is literally part of a mind. |
| M81 | Philosophy of Mind, Agency, and Authorship | Agency, intentionality, responsibility, authorship, epistemic dependence, and human-AI collaboration. It does not settle legal or moral responsibility. |
| M82 | Ethics of Cognitive Extension, Cognitive Liberty, and Human Rights | Autonomy, identity, cognitive liberty, intervention, privacy, justice, and argument maps for AI-mediated cognitive support. It offers no clinical or policy advice. |
| M83 | Disability Studies, Neurodiversity, and Assistive Technology Ethics | Disability models, neurodiversity paradigms, assistive technology, participatory design, consent, and accessibility evaluation. It is distinct from M61's applied AI-mediated-learning role and makes no population claim. |

## Orientation sources and limits

- [W3C PROV](https://www.w3.org/TR/prov-overview/) and [PROV-DM](https://www.w3.org/TR/prov-dm/) inform provenance vocabulary, not truth or privacy guarantees.
- [W3C SKOS](https://www.w3.org/TR/skos-reference/) and [FAIR principles](https://www.go-fair.org/fair-principles/) inform controlled vocabularies and stewardship, not automatic authority decisions.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) and [AgentBench](https://arxiv.org/abs/2308.03688) motivate risk-aware agent evaluation, not safety certification.
- Agent surveys by [Xi et al.](https://arxiv.org/abs/2309.07864) and [Cheng et al.](https://arxiv.org/abs/2401.03428) map agent components and multi-agent patterns. They are not deployment prescriptions.
- [SEP: Externalism About the Mind](https://plato.stanford.edu/entries/content-externalism/), [Collective Intentionality](https://plato.stanford.edu/entries/collective-intentionality/), [Disability](https://plato.stanford.edu/entries/disability/), [Neuroethics](https://plato.stanford.edu/entries/neuroethics/), and [W3C WAI](https://www.w3.org/WAI/fundamentals/accessibility-intro/) motivate conceptual distinctions and accessibility obligations. They do not settle metaphysics, speak for communities, or establish efficacy.

## Required next step before module generation

Each approved module needs a reviewed, rights-safe source bank; learning objectives; computational or inspectable exercises; assessment expectations; prerequisite/sequence state; artifact types; privacy boundary; and a clear non-claim. No proposed module should be generated from this architecture alone.
