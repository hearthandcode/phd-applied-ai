# Spec: Self-Directed Doctoral Curriculum in Applied AI & Machine Learning

**Status:** Draft v2 — spec updated with Scott's answers; ready to proceed to Phase A
**Thread:** T13
**Owner:** Scott + Claude
**Public repo target:** `github.com/hearthandcode/phd-applied-ai` (or similar)
**Last updated:** 2026-06-12 (v2 — Scott's Q&A resolved)

---

## 1. Overview and rationale

This spec defines a self-directed, AI-assisted doctoral-equivalent curriculum in Applied AI and
Machine Learning, with a thesis focused on the design and implementation of Hearth & Code — a
gamified, adaptive, AI-native educational platform.

The goal is to produce a public repository that documents:
- A rigorous, peer-equivalent course of study spanning ~5–6 years
- A thesis representing an original research contribution
- A simulated PhD defense with transcript and committee feedback
- Mastery rubrics and audit logs proving competency at each stage
- A companion Substack/blog series: each module produces a public reflection post connecting
  theory to H&C, Scott's own understanding, and how others can replicate the approach

The public framing: **"What it looks like to receive a PhD-equivalent education using AI as
a collaborator, tutor, and committee."** This is itself a contribution to the field of AI
literacy and self-directed learning — and it doubles as a portfolio centerpiece for H&C.

The blog series is not optional decoration — it is a core artifact. It:
1. Forces synthesis and genuine comprehension (you can't fake a readable post)
2. Builds the H&C public audience in parallel with the curriculum
3. Demonstrates mastery in a format employers, investors, and peers can actually read
4. Creates a timestamped public audit trail that adds credibility to the "equivalent PhD" claim

### Why this matters for Hearth & Code

H&C's mission is to deliver university-equivalent education at a fraction of the cost. Scott
doing this himself — and documenting every step — is the most authentic possible proof of
concept. The curriculum, rubrics, and archive integration are all prototypes of what H&C will
offer at scale.

---

## 2. Archive coverage assessment

Based on the hearthandcode-archive inventory (47k+ docs, 35k+ files):

| Domain | Archive strength | Coverage grade |
|---|---|---|
| CS theory (computability, complexity, PLT, type theory) | 1,200+ docs | **A** |
| Algorithms and data structures | 320+ docs | **A** |
| Systems programming | 42+ docs | **B** |
| Programming language fundamentals | 17k+ docs (Rust-heavy) | **A** |
| Pedagogy and gamification | 3,300+ docs | **A** |
| Software architecture | 420+ docs (system-design-101) | **B** |
| ML/DL foundations | ~270 docs | **C+** |
| LLM architecture and training | ~35 docs | **C** |
| Memory, RAG, knowledge graphs | ~44 docs | **C+** |
| Multi-agent systems | ~30 docs | **C** |
| AI ethics and governance | ~8 docs | **D** |
| Reinforcement learning | ~15 docs (embedded in ML) | **D** |
| AI safety and alignment | ~2 docs | **D** |
| Affective computing / emotion modeling | ~0 docs | **F** |
| AI and education (AIED) research | ~0 docs | **F** |
| Causal inference | ~5 docs | **D** |
| Frontier AI research methods | ~10 docs | **D** |

**Conclusion:** The archive covers Phase 0–1 (math, CS fundamentals) and Phase 4 (pedagogy) very
well. Phases 2–3 (ML/AI depth) and specialized research areas need substantial supplementation
via web research and LLM-generated content during the workflow execution.

The multi-agent workflow strategy: query the archive first for each module, then use web search
and LLM knowledge to fill gaps. This ensures archive content is always primary where available.

---

## 3. Thesis direction

**Working title:**
> *Adaptive AI-Native Learning Systems: Architecture, Pedagogy, and Ethics of a Next-Generation
> Educational Platform*

**Research questions:**
1. How can adaptive AI systems model individual learner competency trajectories in real time,
   and what instructional design principles govern their effectiveness?
2. What pedagogical frameworks are most effective when mediated by generative AI tutors, and
   how do they compare to traditional human-mediated instruction?
3. Can computational models of personality, affect, and values (virtue/vice frameworks) improve
   motivation and learning outcomes in AI-native educational environments?
4. What governance, ethics, and fairness constraints are necessary for AI systems that assess
   and adapt to individual learners at scale?
5. How do a learner's personal characteristics — ADHD, bipolar disorder, cyclical energy,
   variable recall, and task-initiation difficulty — shape their trajectory through AI-mediated
   doctoral-level study? What patterns emerge across 5+ years of granular self-report data,
   and what design principles for AI adaptive systems follow from those patterns?

**RQ5 is the autoethnographic thread.** Scott is simultaneously researcher and primary
research subject. This is a legitimate qualitative/mixed-methods design:
- **Method:** Longitudinal autoethnography with structured self-report (audit logs)
- **Dataset:** 5+ years of session-level data (energy, focus, mood, hours, competency)
- **Scope of claims:** Generative hypotheses for future research, not generalizable theory
  from N=1. Appropriate framing: "This is what happened for this learner; here is what
  it suggests for system design."
- **Contribution type:** Rich qualitative dataset (rare in AIED), first-person account of
  AI as accommodation tool for neurodiverse adult learner, design principles for adaptive
  systems that respond to cognitive/affective state fluctuation
- **Data policy (confirmed):** Fully public. No anonymization beyond `learner_id: L001`
  as a data science convention. Energy levels, mood, effort, focus quality, personal
  reflections — all published as-is. Scott's voluntary disclosure is the core of the
  contribution; sanitizing it would undermine the research.

**Why this is frontier territory:**
Almost no AIED research has longitudinal data on neurodiverse learners — studies typically
run 6–12 weeks on neurotypical university students in lab settings. A 5+ year, session-
granular dataset from an adult learner with ADHD and bipolar disorder, using AI as a primary
educational tool, would be among the richest datasets of its kind in the field. The closest
analogues are in assistive technology research and special education — not AIED. This crosses
both fields in a way that has not been done before.

**Connection to H&C:** This research question directly informs how H&C's adaptive engine
should behave for neurodiverse learners. If session energy correlates with learning efficiency,
the system should detect low-energy states and offer different content (retrieval practice
vs. new material) rather than pushing forward uniformly. If focus quality predicts completion
rates, the interface should adapt session length and pacing. This is the practical output.

**On virtue/vice modeling being frontier territory (Scott was right to flag this):**
The components exist in scattered form — Anthropic's Constitutional AI models values and
principles; affective computing (Picard, MIT Media Lab) recognizes and simulates emotions;
virtue ethics applied to AI exists in philosophical literature (Shannon Vallor, Luciano Floridi,
Mark Coeckelbergh); value alignment (Stuart Russell, Hadfield-Menell) addresses aligning AI to
human values. BUT: computationally modeling *virtue and vice as learner traits* in an
AI-native educational context — and using those models to personalize motivation and instruction
— is a genuine gap in the AIED literature. The synthesis is novel. This is where the thesis
makes a distinct, original contribution. The framing "what if an AI tutor could recognize when
a student is avoiding challenge (sloth), overcomplicating things (pride), or rushing to the
answer (impatience), and adapt its scaffolding accordingly?" does not yet exist as a formal
research program. It maps onto character-based AI in game design and onto moral foundations
theory in educational psychology — but the combination, applied to adaptive learning, is
genuinely new territory.

**Thesis contribution:**
A theoretical framework + working implementation (H&C) demonstrating:
1. That AI-assisted adaptive learning can achieve outcomes comparable to elite university instruction
2. That virtue/vice-aware learner modeling is a tractable and useful extension of current
   affect- and motivation-aware ITS architectures
3. That self-directed AI-assisted doctoral study, rigorously documented, constitutes a valid
   and reproducible model for PhD-equivalent education

**Why this works as a thesis:**
- Grounded in real implementation (H&C is the research laboratory)
- Crosses multiple disciplines (AI, ML, education, ethics, HCI, moral psychology)
- Produces both theory and artifact
- The curriculum itself is a meta-contribution: proving the thesis by example
- Confirmed direction by Scott: focuses on effective adaptive curricula, governance at scale,
  novel virtue/vice considerations, and pedagogical principles for AI-first education

---

## 4. Curriculum structure

### Timeline overview

| Phase | Name | Duration | Months | Focus |
|---|---|---|---|---|
| Phase 0 | Mathematical Foundations | 6–12 mo | 1–12 (concurrent) | Linear algebra, calculus, probability, optimization |
| Phase 1 | CS Fundamentals | 12–18 mo | 1–18 | Theory, algorithms, systems, architecture |
| Phase 2 | ML Foundations | 12–18 mo | 6–24 | Classical ML, neural nets, deep learning |
| Phase 3 | Advanced AI | 18–24 mo | 18–48 | LLMs, GenAI, RL, RAG, multi-agent, safety |
| Phase 4 | Specialized Research | 18–24 mo | 24–60 | AIED, pedagogy, affective computing, ethics |
| Phase 5 | Thesis & Defense | 12–24 mo | 36–72 | Research, writing, defense |

Phases overlap intentionally — this is a self-paced curriculum, not a sequential lockstep.
Phase 0 math runs concurrently with Phase 1. Phase 4 begins as Phase 3 plateaus.

**Pace design — the Par/Scorecard system:**
Each module has a "Par" — an estimated effort in hours at a sustainable, moderate pace.
Par is aspirational, not prescriptive. It exists to give a frame of reference, not create guilt.

- **Under par**: You moved fast (high energy, familiar territory, or prior knowledge)
- **At par**: Steady and thorough
- **Over par**: You went deep, hit a hard topic, or had a low-energy stretch — all valid

Every `audit.md` records actual hours per session. A `SCORECARD.md` per phase aggregates:
- Par hours (target) vs. actual hours (reality)
- Competency level reached per module
- Energy notes (were you high-capacity or low-capacity during this module?)

The scorecard is public in the repo — it's honest data about what self-directed doctoral study
actually looks like, warts and all. That honesty is itself part of the thesis contribution.
This is also directly useful prototype data for H&C's adaptive pacing system.

---

## 5. Module registry (63 modules)

### Phase 0 — Mathematical Foundations

| ID | Module | Archive coverage | Supplement needed |
|---|---|---|---|
| M01 | Linear Algebra for ML | Partial (type theory adjacent) | Yes — geometry, eigendecomposition |
| M02 | Multivariate Calculus and Optimization | Low | Yes — gradient descent theory |
| M03 | Probability Theory and Bayesian Inference | Low | Yes — measure theory, conjugate priors |
| M04 | Statistics and Statistical Learning | Moderate | Yes — hypothesis testing, MLE |
| M05 | Information Theory | Low | Yes — entropy, mutual information, KL divergence |
| M06 | Graph Theory and Discrete Mathematics | Moderate (computability adjacency) | Partial |

### Phase 1 — CS Fundamentals

| ID | Module | Archive coverage | Supplement needed |
|---|---|---|---|
| M07 | Computability Theory and Formal Languages | **Strong** (351 docs) | Minimal |
| M08 | Computational Complexity | **Strong** (computability folder) | Minimal |
| M09 | Algorithm Design and Analysis | **Strong** (222 docs) | Minimal |
| M10 | Advanced Data Structures | **Strong** | Minimal |
| M11 | Programming Language Theory | **Strong** (200 docs) | Minimal |
| M12 | Type Theory and Dependent Types | **Strong** (HoTT, 101 docs) | Minimal |
| M13 | Operating Systems and Systems Programming | Moderate (42 docs) | Partial |
| M14 | Computer Networks and Distributed Systems | Low | Yes |
| M15 | Database Systems and Theory | Moderate | Partial |
| M16 | Software Architecture Patterns | **Strong** (system-design-101) | Minimal |
| M17 | Software Engineering Methodology | Moderate | Partial |
| M18 | Security Fundamentals | Low | Yes |

### Phase 2 — ML Foundations

| ID | Module | Archive coverage | Supplement needed |
|---|---|---|---|
| M19 | Classical Machine Learning Algorithms | Moderate (77 docs) | Partial |
| M20 | Statistical Learning Theory | Low | Yes — PAC learning, VC dimension |
| M21 | Neural Network Foundations | Moderate | Partial |
| M22 | Convolutional and Recurrent Architectures | Low | Yes |
| M23 | Attention Mechanisms and Transformer Architecture | Moderate (35 LLM docs) | Partial |
| M24 | Optimization for Deep Learning | Low | Yes — Adam, learning rate schedules |
| M25 | Regularization, Generalization, and Overfitting | Low | Yes |
| M26 | Probabilistic Graphical Models | Low | Yes — Bayesian networks, HMMs |
| M27 | Reinforcement Learning Fundamentals | Low (15 docs) | Yes |
| M28 | Deep Reinforcement Learning | Low | Yes — PPO, DQN, policy gradients |

### Phase 3 — Advanced AI

| ID | Module | Archive coverage | Supplement needed |
|---|---|---|---|
| M29 | LLM Architecture and Pretraining | Moderate (35 docs) | Partial |
| M30 | Fine-tuning, RLHF, and Alignment Techniques | Low | Yes |
| M31 | Generative Models: VAE, GAN, Diffusion | Low | Yes |
| M32 | Adversarial Machine Learning and Robustness | Low | Yes |
| M33 | Memory Systems and RAG Architecture | Moderate (44 docs) | Partial |
| M34 | Multi-Agent Systems and Agentic AI | Moderate (30 docs) | Partial |
| M35 | AI Planning, Reasoning, and Symbolic AI | Low | Yes |
| M36 | Computer Vision and Multimodal AI | Low | Yes |
| M37 | Speech, Audio, and Multimodal Perception | Low | Yes |
| M38 | Knowledge Representation and Reasoning | Moderate | Partial |
| M39 | Causal Inference and Causality in ML | Low (5 docs) | Yes |
| M40 | Interpretability and Explainability (XAI) | Low | Yes |
| M41 | AI Safety, Alignment, and Red-Teaming | Very low (2 docs) | Yes |
| M42 | Frontier Research Methods and Practices | Low | Yes |

### Phase 4 — Specialized Research Areas

| ID | Module | Archive coverage | Supplement needed |
|---|---|---|---|
| M43 | AI and Education (AIED) Foundations | Very low | Yes |
| M44 | Intelligent Tutoring Systems | Very low | Yes |
| M45 | Adaptive Learning Systems and BKT | Moderate (adaptive-learning-research.md) | Partial |
| M46 | Curriculum Design Theory | Low (2 docs) | Yes |
| M47 | Instructional Design Methods | Low | Yes |
| M48 | AI Literacy Frameworks | Low (profile/ai-pillars.md) | Yes |
| M49 | AI Pedagogy and Teaching with AI | Low | Yes |
| M50 | Gamification Theory and Game-Based Learning | **Strong** (2,305 docs) | Minimal |
| M51 | Educational Measurement and Assessment | Low | Yes |
| M52 | Affective Computing and Emotion Modeling | None (0 docs) | Full generation |
| M53 | Computational Personality Modeling | None | Full generation |
| M54 | Value Alignment, Virtue, and Vice Modeling | Very low | Yes |
| M55 | AI Ethics, Governance, and Policy | Very low (8 docs) | Yes |
| M56 | Fairness, Accountability, and Transparency | Very low | Yes |
| M57 | AI and Society: Policy, Economics, Labor | Very low | Yes |
| M58 | Cognitive Science and Learning Theory | Low (pedagogy archive adjacent) | Yes — Piaget, Vygotsky, Bloom, cognitive load |
| M59 | HCI and Interface Design for AI-Native Learning | Low | Yes — UX for adaptive systems, learning UI patterns |
| M60 | MLOps, AI Engineering, and Experiment Design | Low | Yes — deployment, monitoring, A/B testing for ML |

*M58 note:* Cognitive science is foundational for H&C's instructional design decisions;
it explains *why* scaffolding, spaced repetition, and desirable difficulty work at a
neuroscience/psychology level — not just that they work.

*M59 note:* H&C needs good interface design. This module bridges ML capability and
learner-facing UX, with specific focus on AI tutoring interfaces and skill trees.

*M60 note:* MLOps is the practical infrastructure that makes an AI-native platform
deployable at scale. Covering it here rounds out the applied engineering side.

| M61 | Neurodiversity, Mental Health, and AI-Mediated Learning | None (0 docs) | Full generation + web research |

*M61 note:* This module is the theoretical and empirical home of RQ5. It covers:
- Neurodivergence in educational contexts (ADHD, autism, bipolar, dyslexia, learning disabilities)
- Cognitive load theory applied to variable-attention learners
- Mental health and self-directed learning (motivation, initiation, persistence)
- AI as assistive/adaptive technology for neurodiverse learners (literature review)
- Autoethnographic research methodology in education
- Longitudinal study design for self-report educational data
- The specific intersection: AI tutoring systems that respond to cognitive/affective state fluctuation
- Ethical considerations in researching one's own neurodivergence publicly

The module also produces **Scott's PERSONA.md** — the first-person disclosure document that
anchors the autoethnographic methodology and lives in the public repo root.

**Archive coverage:** Near zero. This will require full web research generation targeting:
ERIC (disability + education), assistive technology journals, ADHD and learning research,
autoethnography methods literature, special education + AI intersection.

### Phase 5 — Thesis and Defense

| ID | Module | Description |
|---|---|---|
| M62 | Research Methodology | Qualitative, quantitative, and mixed methods; autoethnographic design; experimental design |
| M63 | Systematic Literature Review | Survey of AIED, adaptive learning, neurodiversity + AI, and AI pedagogy |
| M64 | Thesis Proposal | Formal proposal document with committee review simulation |
| M65 | Original Research: H&C as Laboratory | Living research log tied to actual H&C development |
| M66 | Thesis Writing | Full dissertation document |
| M67 | PhD Defense: Preparation and Execution | Hybrid written/interview defense with transcript and feedback |

---

## 6. Module anatomy

Every module (M01–M66) produces the following artifacts:

### 6.1 `theory.md` — Doctoral-level theory digest
- Written at the level of a top-tier course reader (MIT OCW, Stanford CS229 equivalent)
- Sections: Overview, Core Concepts, Mathematical Formulation (where applicable),
  Historical Context, Current State of Research, Open Problems
- Length: 3,000–8,000 words
- Citations: real papers with author/year; archive docs cited by path where used

### 6.2 `project/` — Implementation project
**Language stack (confirmed):**
- **Python**: All ML/AI projects (PyTorch, scikit-learn, numpy, FastAPI, Jupyter)
- **TypeScript**: H&C integrations, agentic workflows, front-end components
- **Rust**: Systems modules (M13, M14), performance-critical ML inference, any module where
  systems-level control matters
- **C++**: Computer architecture (M14 adjacent), low-level ML framework internals exploration
- **C#**: Game/UI-adjacent modules (M59 — HCI, gamification UX prototypes)
- Language choice per module is specified in the project README

Each project includes:
- `README.md`: Problem statement, learning objectives, language rationale, deliverables
- `implementation/`: Working code
- `writeup.md`: Technical writeup connecting implementation to theory
- `portfolio-entry.md`: Public-facing description (employment/portfolio lens)
- `hc-connection.md`: Explicit note on how this connects to H&C architecture or design

At least one project per module must connect to H&C implementation.

### 6.3 `rubric.md` — Mastery rubric and par score
Four-level competency scale per module:

| Level | Name | Description |
|---|---|---|
| 0 | Unaware | Cannot explain the concept |
| 1 | Aware | Can explain at a high level; cannot apply |
| 2 | Competent | Can apply with guidance; explains trade-offs |
| 3 | Proficient | Applies independently; critiques approaches |
| 4 | Mastery | Extends, innovates, teaches; aware of open problems |

**Par score block** (included in every rubric):
```
Par: XX hours at moderate pace (10-15 hrs/week)
Suggested split: XX hrs theory / XX hrs project / XX hrs review
My actual: [fill in when complete]
Competency reached: [0-4]
Energy level during study: [high / medium / low / mixed]
```

Each rubric also includes: 5–10 evaluative questions, a practical assessment task,
expected artifacts at each level, and a self-assessment checklist.

### 6.4 `audit.md` — Study log
Dated entries recording:
- Sessions completed (date, duration, topics covered)
- Competency level reached (0–4 per rubric dimension)
- Blockers and open questions
- Connections to H&C implementation
- Par vs. actual hours running total
- Next session plan

### 6.5 `reading-list.md` — Annotated bibliography
- 5–15 sources per module (papers, books, courses, videos)
- Annotated with: what it covers, why it's relevant, difficulty rating
- Archive sources cited first where coverage exists; external sources fill gaps

### 6.6 `blog-post-seed.md` — Substack/blog post outline (generated)
Generated by the workflow as a seed/scaffold — **not the final post**. Scott writes the
actual post. The seed includes:
- Suggested title and subtitle
- 3-5 hook angles (personal, technical, H&C-building)
- Outline with main points
- Pull quotes or key concepts to highlight
- Suggested "H&C lesson" section: how this topic influences the platform design
- Suggested "how you can apply this" section for general readers

The final blog post lives on Substack; a copy or link is tracked in `POSTS.md` in the repo root.
Blog posts are optional per module but strongly encouraged — they are the most visible mastery
artifact.

---

## 7. Evaluation and mastery framework

### 7.1 Within-module evaluation
Each module uses its `rubric.md` for self-assessment, with Claude acting as evaluator:
- **Oral exam simulation**: Claude poses doctoral-level questions; Scott responds; Claude
  scores against rubric dimensions and provides written feedback
- **Implementation review**: Claude reviews project code and writeup against rubric
- **Pass threshold**: Level 3 (Proficient) required to advance; Level 4 for thesis-relevant modules

### 7.2 Phase-level evaluation (qualifying exams)
At the end of each Phase, a simulated qualifying examination:
- Written component: 3–5 essay questions drawing across phase modules
- Oral component: 60-minute simulated exam with Claude as committee
- Practical component: capstone project integrating phase concepts
- Output: `exams/phase-X-qualifying/` with questions, responses, and committee feedback

### 7.3 Thesis evaluation (defense)
See Section 9 (PhD Defense structure).

### 7.4 Calibration to top-tier standards
Module theory and rubrics are explicitly calibrated to public syllabi from:
- MIT 6.867 (Machine Learning), 6.S898 (Deep Learning), 6.004 (Computation Structures)
- Stanford CS229 (ML), CS224N (NLP), CS285 (Deep RL)
- CMU 10-701 (PhD ML), 11-785 (Deep Learning)
- Oxford ML course
- Berkeley CS285, STAT 241 (Statistical Learning Theory)

Calibration notes are included in each `theory.md` to document which course the module
content is equivalent to.

---

## 8. Public repo structure

The output is a standalone public repo, separate from hearthandcode-hub:

```
phd-applied-ai/
├── README.md                    # The pitch; curriculum overview; how to use
├── THESIS.md                    # Thesis statement, research questions, abstract
├── AUDIT_LOG.md                 # Master chronological study log (all sessions)
├── SCORECARD.md                 # Par vs. actual hours by module and phase
├── POSTS.md                     # Index of all published Substack posts with links
├── DEFENSE.md                   # PhD defense transcript and committee feedback
├── curriculum/
│   ├── overview.md              # Full module registry with status and links
│   ├── phase-0-math/
│   ├── phase-1-cs/
│   ├── phase-2-ml/
│   ├── phase-3-advanced-ai/
│   ├── phase-4-specialized/
│   └── phase-5-thesis/
├── modules/
│   ├── M01-linear-algebra/
│   │   ├── theory.md
│   │   ├── rubric.md
│   │   ├── audit.md
│   │   ├── reading-list.md
│   │   ├── blog-post-seed.md
│   │   └── project/
│   └── ... (M02–M65)
├── exams/
│   ├── phase-0-qualifying/
│   ├── phase-1-qualifying/
│   └── ...
├── defense/
│   ├── prospectus.md
│   ├── proposal.md
│   ├── qualifying-brief.md
│   ├── defense-transcript.md    # Full written transcript of the defense
│   └── committee-feedback.md
├── portfolio/
│   └── index.md                 # Map to H&C-connected projects
└── bibliography/
    └── master.bib               # BibTeX format; all citations
```

**Branding note:** The README positions this as:
1. A genuine, rigorous course of doctoral-level study
2. A proof of concept for what H&C will enable at scale
3. A public demonstration of AI-assisted education methodology
4. A portfolio artifact for Scott (researcher, builder, educator)
5. A companion to the H&C Substack — linking theory to building in public

---

## 9. PhD defense structure

The defense is the capstone event. It uses a **hybrid written/interview format** that Scott
identified as more authentic to his working style and potentially interesting as a research
artifact in itself. ("How does a simulated doctoral defense via LLM compare to traditional
formats?" is a valid research note for the thesis.)

### 9.1 Pre-defense milestones (written by Scott)
1. **Prospectus** (`defense/prospectus.md`): Written at ~Month 12. 5–10 pages stating the
   thesis question, motivation, preliminary literature review, and research plan.
2. **Proposal** (`defense/proposal.md`): Written at ~Month 30. 20–40 pages. Full literature
   review, methodology, preliminary results, and timeline to completion.
3. **Qualifying brief** (`defense/qualifying-brief.md`): Synthesizes all five qualifying exams
   into a committee-facing brief demonstrating breadth of mastery.

### 9.2 Defense format (hybrid written + adaptive interview)

**Stage 1 — Opening statement (written, ~1 hr window)**
Scott writes a 1,500–2,500 word thesis defense statement in a Markdown file:
`defense/opening-statement.md`
This summarizes the thesis, contributions, and key findings. Written at Scott's own pace.
Submitted when ready. Claude reads and begins Stage 2.

**Stage 2 — Adaptive committee Q&A (interview-style, chunked)**
Claude plays 5 committee members one at a time. Each exchange is:
1. Claude presents 1–2 questions from that committee member's perspective
2. Scott responds in the conversation (conversational length, not essay-length)
3. Claude follows up based on the response (direction adapts to Scott's answers)
4. Repeat for 2–4 rounds per committee member before moving to the next

Committee members:
- **Member 1 — Dr. Chen** (ML Theory, Stanford-caliber): Challenges mathematical rigor and proofs
- **Member 2 — Dr. Kowalski** (Systems/Architecture, CMU-caliber): Challenges implementation and engineering decisions
- **Member 3 — Dr. Williams** (Education/Pedagogy, MIT Media Lab-caliber): Challenges pedagogical claims and AIED theory
- **Member 4 — Dr. Okonkwo** (AI Ethics, Oxford-caliber): Challenges governance, fairness, and virtue/vice framing
- **Member 5 — Dr. Patel** (Industry/Product, applied lens): Challenges market viability and real-world deployment

The adaptive Q&A is the research-interesting part: the committee's follow-up questions depend
on Scott's responses, creating a more authentic dialogue than a scripted exam. Claude tracks
which claims were defended well, which need more support, and surfaces that in the feedback.

**Stage 3 — Closed deliberation (Claude writes)**
After all five committee rounds, Claude writes `defense/committee-feedback.md`:
- Per-member assessment of Scott's responses (strengths and weaknesses)
- Cross-cutting observations (what themes emerged across committee?)
- Recommendation with justification

**Stage 4 — Decision and record**
Decision written to `defense/defense-transcript.md` with full log of all Q&A.
Options: **Pass** / **Pass with revisions** / **Major revisions required**

### 9.3 Post-defense revisions
If revisions required:
- Specific revision requests documented in `defense/committee-feedback.md`
- Scott makes revisions to thesis document
- Re-submission session and approval recorded in transcript

---

## 10. Multi-agent workflow design

The curriculum content is generated via a phased multi-agent workflow using the Workflow tool.
Content generation happens in 5 execution phases spread across multiple sessions:

### Workflow Phase A — Architecture and Templates (~200k tokens)
*Agents:* 5–8
*Goal:* Finalize module registry, generate template files, validate archive mappings
```
- 1 architecture agent: validate module list, prerequisites graph, timeline
- 6 template agents: generate all blank module templates (theory.md, rubric.md, etc.)
- 1 archive-mapping agent: for each module, query archive MCP for relevant docs list
```
*Output:* All 63 module directories with empty scaffolding + archive content lists

### Workflow Phase B — Phase 0 & 1 Modules (~1.5M tokens)
*Agents:* ~60 (3 per module × 20 modules)
*Goal:* Generate full content for mathematical foundations and CS fundamentals
```
- Per module: theory agent + project agent + rubric agent running in pipeline
- Archive queries precede each theory agent
- Phase 0 math modules include LaTeX-style formulas in markdown
```
*Output:* 19 complete modules (M01–M18, plus M07/M08 fast-tracked from strong archive)

### Workflow Phase C — Phase 2 & 3 Modules (~2.5M tokens)
*Agents:* ~84 (3 per module × 28 modules)
*Goal:* Generate ML foundations and advanced AI modules
```
- Heavy web research supplementation for RL, safety, causality
- Each theory agent explicitly cites calibration target (CS229, CS285, etc.)
- Adversarial verification agents for factual claims in frontier modules
```
*Output:* 28 complete modules (M19–M42)

### Workflow Phase D — Phase 4 Modules (~1.8M tokens)
*Agents:* ~60 (4 per module × 15 modules — extra for specialized research)
*Goal:* Specialized research areas including AIED, affective computing, ethics
```
- Full web search for affective computing, virtue modeling (no archive coverage)
- H&C-connection agents: for each module, write explicit H&C integration note
- Ethics modules use adversarial verification (high sensitivity to fabrication)
```
*Output:* 15 complete modules (M43–M57)

### Workflow Phase E — Thesis & Defense Infrastructure (~500k tokens)
*Agents:* ~20
*Goal:* Generate thesis framework, qualifying exam templates, defense structure
```
- Thesis outline agent (THESIS.md, DEFENSE.md skeleton)
- 5 qualifying exam agents (one per phase)
- Defense committee persona agents (one per committee member profile)
- Master AUDIT_LOG.md and README.md generation
```
*Output:* All Phase 5 scaffolding; full repo README; defense setup

### Prompt template pattern — theory agent
Each module theory agent receives this context block:
```
You are generating doctoral-level course content for a self-directed PhD curriculum in
Applied AI/ML. This module is: [MODULE NAME] ([M##]).

Context:
- Phase: [0–5], curriculum calibration target: [e.g., "MIT 6.867 / Stanford CS229"]
- Archive documents available: [list from archive MCP query, or "none — full generation"]
- Prerequisite modules: [M## list]
- H&C connection: [e.g., "adaptive pacing engine", "gamification layer", "virtue/vice learner model"]
- Language for project: [Python / TypeScript / Rust / C++ / C#] with rationale

Generate theory.md with:
1. Overview (500w): What is this, why does it matter, where does it fit in the curriculum?
2. Core Concepts (2,000–3,000w): Precise definitions, mathematical formulation where applicable
3. Historical Context (500w): How the field developed, key turning points
4. Current State of Research (1,000w): What's settled, what's active, what's contested
5. Open Problems (500w): ≥2 genuine open questions the field hasn't solved
6. Archive Source Integration: Cite any archive docs used by path
7. Calibration note: Which specific course/syllabus this module is equivalent to

Length: 4,500–7,500 words total. Write at the level of a top-tier PhD course reader.
Include at least 8 real citations (author, year, venue). Do not fabricate citations.
```

### Prompt template pattern — blog seed agent
```
You are generating a blog post seed for the Hearth & Code Substack. The author (Scott)
has just completed studying: [MODULE NAME] ([M##]).

Scott's background: RPI CS grad, returning to industry, building H&C (gamified AI-native
ed-tech platform), writing in public about AI, learning, and building.

The blog post seed is NOT the final post — it is a scaffold Scott will write from.
Generate blog-post-seed.md with:
1. Three possible title + subtitle combinations (range from technical to accessible)
2. Opening hook (2–3 sentences that would stop a reader scrolling)
3. Main outline (5–7 sections with 1-sentence descriptions)
4. "H&C Lesson" section outline: how this module's content influenced H&C's design
5. "How you can apply this" section outline: what a general reader can take away
6. Pull quotes: 3 memorable formulations of key concepts from this module
7. Suggested Substack tags and cross-links to prior posts

Tone: intellectually honest, personal, builder-focused. Not a lecture — a field report
from someone actively learning and building. Voice: direct, curious, occasionally irreverent.
```

---

## 11. Token budget and phasing

### Per-execution estimates (Claude Max, claude-sonnet-4-6)

| Workflow Phase | Agents | Est. tokens | Sessions |
|---|---|---|---|
| Phase A: Architecture + templates | ~8 | ~200k | 1 |
| Phase B: Math + CS fundamentals (M01–M18) | ~72 (4/module) | ~1.8M | 2–3 |
| Phase C: ML + Advanced AI (M19–M42) | ~96 (4/module) | ~2.8M | 3–5 |
| Phase D: Specialized research (M43–M61) | ~76 (4/module) | ~2.3M | 3–4 |
| Phase E: Thesis + defense infra (M62–M67) | ~25 | ~600k | 1–2 |
| **Total** | **~277 agents** | **~7.7M tokens** | **~11–15 sessions** |

*Module count: 67 total (M01–M67). Phase 4 now ends at M61; Phase 5 is M62–M67.*
*M61 (Neurodiversity, Mental Health, and AI-Mediated Learning) added as the anchor module for RQ5.*

### Claude Max ($100/mo) feasibility

Claude Max provides substantially higher usage limits than Pro. The workflow runs on
claude-sonnet-4-6 (the session model). Realistic constraints:
- **Per-session cap:** Approximately 1–2M tokens per individual workflow execution before
  rate limiting or session exhaustion; varies by time of day and server load
- **Monthly capacity:** At $100/mo, the full 6.5M token corpus is achievable over 2–3 months
  of regular sessions (2–3 per week)
- **Cost:** Zero additional cost beyond the Claude Max subscription — no API billing
- **Practical strategy:** Run one workflow phase per session; pause between phases to review
  and spot-check output quality before continuing

### Quality vs. speed trade-off
- **High quality (recommended):** Run each workflow phase, review a sample of outputs, adjust
  prompts, re-run if needed. Adds 1–2 review sessions per phase. Total: ~4 months.
- **Speed-first:** Run all phases with minimal review. Total: ~6–8 weeks of active sessions.
  Risk: lower content quality requiring manual correction later.

**Recommendation:** High quality. The curriculum is a long-term asset; getting it right is
more important than getting it fast. Phase A outputs should be reviewed by Scott before Phase B.

---

## 12. Immediate next actions

**Pre-execution (before any workflow runs):**
1. **Archive gap-fill ingestion** — Run the hearthandcode-archive ingestion agent with the
   gap-fill prompt (see `architecture/specs/phd-curriculum-archive-ingestion-prompt.md`) to
   ingest content for D/F-grade domains before the workflow needs them
2. **Create public GitHub repo** `phd-applied-ai` under `hearthandcode` GitHub org
   (GitHub, not Forgejo — portfolio visibility requires GitHub)
3. Confirm spec is locked — no structural changes after Phase A starts

**Execution sequence:**
4. **Run Workflow Phase A** — architecture + scaffolding (~200k tokens, ~1 session)
5. **Scott reviews Phase A** — validate module list, par scores, template structure
6. **Run Workflow Phase B** — Math + CS fundamentals (~1.8M tokens, 2–3 sessions)
7. **Begin studying M07** in parallel — archive coverage is excellent, immediately startable
8. Continue Phases C → D → E, one per session block, with review gates between each

The curriculum is ready to study from the moment Phase B completes. Phases C–E generate
in the background while Scott works through Phase 0–1 modules in his actual study.

---

## 13. Confirmed decisions

All questions resolved in Scott's review (2026-06-12):

| # | Question | Decision |
|---|---|---|
| 1 | Thesis direction | Confirmed: adaptive curricula + governance + virtue/vice (confirmed frontier) + AI-first pedagogy |
| 2 | Repo location | GitHub public under `hearthandcode` org |
| 3 | Blog/post artifacts | Yes — each module produces a blog-post-seed.md; Scott writes the final Substack post |
| 4 | Language stack | Python + TypeScript primary; Rust, C++, C# for appropriate modules |
| 5 | Defense format | Hybrid: written opening statement + adaptive interview-style Q&A with Claude |
| 6 | Pace system | Par/Scorecard: estimated hours per module as aspirational target; actual tracked in audit.md |
| 7 | Phase A timing | Not yet — archive gap-fill ingestion first, then Phase A |

**One remaining open question:**
- Should the `SCORECARD.md` and `AUDIT_LOG.md` include energy/capacity notes publicly, or
  keep those in a private Obsidian/notes layer? (Public is more authentic to the thesis
  contribution; private is more comfortable. No urgency — decide before first module is done.)

---

---

## 14. Supporting specs and artifacts (generated this session)

| Artifact | Location | Status |
|---|---|---|
| Archive gap-fill ingestion prompt | `architecture/specs/phd-curriculum-archive-ingestion-prompt.md` | Ready |
| Committee member: Dr. Chen | `architecture/specs/committee/dr-chen.md` | Ready |
| Committee member: Dr. Kowalski | `architecture/specs/committee/dr-kowalski.md` | Ready |
| Committee member: Dr. Williams | `architecture/specs/committee/dr-williams.md` | Ready |
| Committee member: Dr. Okonkwo | `architecture/specs/committee/dr-okonkwo.md` | Ready |
| Committee member: Dr. Patel | `architecture/specs/committee/dr-patel.md` | Ready |
| Committee README (governance + advisory routing) | `architecture/specs/committee/README.md` | Ready |
| Front-matter schema (all artifact types) | `architecture/specs/phd-frontmatter-schema.md` | Ready |
| Launch blog post | `content/newsletter/posts/03-phd-curriculum-launch/substack.md` | Draft — Scott to review |

---

*Spec status: APPROVED v2, extended. All confirmed decisions are locked. Ready for archive*
*ingestion, then Workflow Phase A.*
*See `architecture/specs/phd-curriculum-archive-ingestion-prompt.md` for the ingestion spec.*
