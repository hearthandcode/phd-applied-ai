---
type: research-proposal
title: "Curriculum Structure Proposal — Technical Core + Extended-Mind Adjacent Tracks"
domain: research/learning
status: needs-review
created: 2026-07-01
updated: 2026-07-01
tags: [curriculum, redesign, extended-mind, cognitive-science, philosophy-of-mind, disability-studies, udl, neurodivergent, proposal]
graph_refs: [curriculum/overview.md, curriculum/phase-map.md, modules/M01-linear-algebra/theory.md, docs/redesign-2026-07/thesis-refocus-proposal.md, docs/redesign-2026-07/research-questions-proposal.md]
llm_accessible: true
generated_by: track-a-agent
verified: false
---

# Curriculum Structure Proposal

**Status: PROPOSAL — no module is created, moved, renumbered, or deleted by this document.**
It proposes a revised structure and shows how the existing 67 modules (and M01's generated
content) map into it.

---

## 1. Design principle

The refocused thesis (`thesis-refocus-proposal.md`) does **not** discard the technical
curriculum — it *reframes its purpose*. The CS/AI/ML stack is now **the domain in which the
extended-mind claim is tested**: a neurodivergent adult reaching doctoral competency in a
demanding technical field *via the scaffold* is the phenomenon. So:

- **KEEP** the full technical spine (math → CS → ML → advanced AI) as the domain being mastered.
- **ADD** adjacent tracks the new thesis makes central: cognitive science, neuroscience,
  philosophy of mind / consciousness, disability studies, HCI / human augmentation, learning
  sciences, and AI-ethics / transhumanism.
- **REFRAME** the pedagogy modules from generic instructional design toward **neurodivergent
  pedagogy and Universal Design for Learning (UDL)**.
- **DE-EMPHASIZE** gamification and virtue/vice modeling; recentre on **intrinsic motivation
  and reward-sensitivity-aware design** (per hub `learner-profile-variables.md`).

**Structural strategy: additive + retag, not renumber.** Renumbering M01–M67 would ripple
into every audit/scorecard/session reference. The proposal instead (a) keeps existing module
IDs, (b) regroups them into new *tracks*, (c) adds a small number of new modules with new IDs,
and (d) retags a handful. This keeps migration cost low.

---

## 2. Proposed track structure

Six tracks replace the old six phases as the organizing lens. Existing modules keep their IDs.

### Track I — Technical Core: the domain being mastered *(KEEP, unchanged)*
The evidence base for "doctoral competency was reached." No content change; purpose reframed.
- **Math foundations** — M01–M06
- **CS fundamentals** — M07–M18
- **ML foundations** — M19–M28
- **Advanced AI** — M29–M42

### Track II — Extended Mind & Philosophy of Mind *(NEW — the theoretical core)*
The thesis's home literature; currently absent as dedicated modules.
- **N01 — The Extended Mind & Active Externalism** (Clark & Chalmers; Clark; parity vs.
  complementarity; the coupling–constitution objection) — *nRQ1 core*
- **N02 — Philosophy of Mind & Consciousness** (functionalism, personal identity, extended
  self, phenomenology of agency/authorship) — *nRQ4 core*
- *(Absorbs and expands the "Extended Mind — hypothesis grounding" tag currently pinned to M58.)*

### Track III — Cognitive Science, Neuroscience & Neurodivergent Cognition *(EXPAND)*
- **M58 — Cognitive Science and Learning Theory** *(KEEP; reframe toward distributed/extended
  cognition, Hutchins, cognitive artifacts)*
- **N03 — Cognitive Neuroscience of Executive Function** (Barkley/Brown ADHD models;
  working memory; reward circuitry / dopamine; bipolar cognition) — *nRQ2 core (NEW)*
- **M61 — Neurodiversity, Mental Health, and AI-Mediated Learning** *(KEEP; now spine-adjacent,
  ties to Track IV)*
- **M52 — Affective Computing and Emotion Modeling** *(KEEP; supports affect-regulation
  mechanism in nRQ2)*

### Track IV — Disability Studies & the Ethics of Cognitive Extension *(NEW + regroup)*
- **N04 — Disability Studies & the Neurodiversity Paradigm** (social vs. medical model;
  crip theory; assistive tech as environment-reshaping) — *nRQ4 core (NEW)*
- **N05 — Ethics of Cognitive Extension & Transhumanism** (dependence, deskilling, epistemic
  agency/offloading, autonomy for disabled users, enhancement vs. therapy) — *nRQ4 core (NEW)*
- **M55 — AI Ethics, Governance, and Policy** *(KEEP; narrowed toward agency/autonomy for the
  extended self rather than governance-at-scale)*
- **M56 — Fairness, Accountability, Transparency** *(KEEP as adjacent/elective)*
- **M57 — AI and Society** *(KEEP as adjacent/elective)*

### Track V — HCI, Human Augmentation & Learning Sciences *(EXPAND + reframe)*
- **M59 — HCI and Interface Design** *(KEEP; reframe toward cognitive-artifact / augmentation
  design, Engelbart lineage)* — *nRQ5 core*
- **N06 — Human Augmentation & Distributed Cognition** (Engelbart; intelligence augmentation;
  human-AI teaming as coupled system) — *nRQ5 core (NEW)*
- **Learning sciences / UDL cluster (reframed pedagogy):**
  - **M46 — Curriculum Design Theory** *(KEEP; reframe toward UDL)*
  - **M47 — Instructional Design** → **reframe to "Universal Design for Learning & Neurodivergent
    Pedagogy"** *(UDL principles, executive-function-aware design)*
  - **M49 — AI Pedagogy / Teaching with AI** *(KEEP; reframe: AI as co-cognitive partner, not tutor-over-student)*
  - **M43 AIED Foundations, M44 Intelligent Tutoring, M45 Adaptive Learning/BKT, M51 Educational
    Measurement** *(KEEP as applied-AIED adjacent; supply technique for nRQ5)*

### Track VI — Method, Motivation & Thesis *(KEEP + reframe motivation)*
- **Motivation cluster (de-emphasize gamification/virtue-vice):**
  - **N07 — Intrinsic Motivation & Reward-Sensitivity-Aware Design** (Self-Determination
    Theory: autonomy/competence/relatedness; flow; ADHD reward architecture) — *nRQ3 core (NEW)*
  - **M50 — Gamification** → **demote to elective**, folded under N07 as a cautionary/secondary topic
  - **M53 — Computational Personality Modeling** *(KEEP as elective input to nRQ3)*
  - **M54 — Value Alignment, Virtue & Vice Modeling** → **demote to elective** (was RQ-core; no longer)
- **Autoethnographic method & thesis (KEEP):**
  - **M62 Research Methodology** *(reframe: autoethnography + phenomenological method as the
    thesis-wide spine, not a chapter)*
  - **M63 Literature Review, M64 Proposal, M65 Original Research (living), M66 Thesis Writing,
    M67 Defense** *(KEEP)*
  - **M60 MLOps / Experiment Design** *(KEEP as elective)*

---

## 3. Where M01 fits (preserved)

**M01 — Linear Algebra for ML is kept exactly as generated** (theory TOC + foundations +
sections 01–11, calibrated to MIT 18.06, `formalism_density: 0.4`, learner-profile-tuned).

- **Track:** Track I → Math Foundations. Its ID, content, rubric, and audit history are unchanged.
- **New thesis role:** M01 is no longer "just prerequisite math." It becomes a **primary
  data point for nRQ2**: its generated structure (conceptual-bridge-before-formalism, worked
  examples, memory tiers, checkpoints) is a *worked example of the cognitive scaffold itself*.
  How M01 was generated — calibrated to this learner's working-memory-load sensitivity and
  formalism tolerance — is evidence of the scaffold externalizing working memory (nRQ2) and of
  reward-sensitivity-aware pacing (nRQ3).
- **No action required on M01.** It slots in as-is; only its *interpretation* in the thesis changes.

---

## 4. New modules summary (all additive, new IDs — N01–N07)

| ID | Title | Track | Primary RQ | Status |
|---|---|---|---|---|
| N01 | The Extended Mind & Active Externalism | II | nRQ1 | proposed |
| N02 | Philosophy of Mind & Consciousness | II | nRQ4 | proposed |
| N03 | Cognitive Neuroscience of Executive Function | III | nRQ2 | proposed |
| N04 | Disability Studies & the Neurodiversity Paradigm | IV | nRQ4 | proposed |
| N05 | Ethics of Cognitive Extension & Transhumanism | IV | nRQ4 | proposed |
| N06 | Human Augmentation & Distributed Cognition | V | nRQ5 | proposed |
| N07 | Intrinsic Motivation & Reward-Sensitivity-Aware Design | VI | nRQ3 | proposed |

*(Using an `N` prefix keeps new modules from colliding with the M-series numbering and makes
the "new for the refocus" set obvious. Alternative: append as M68–M74. Scott's call — §6.)*

---

## 5. Reframes and demotions summary

| Module | Old status | Proposed |
|---|---|---|
| M47 Instructional Design | pedagogy | **Reframe → UDL & Neurodivergent Pedagogy** |
| M46 Curriculum Design | generic | Reframe toward UDL |
| M49 AI Pedagogy | tutor model | Reframe → AI as co-cognitive partner |
| M58 Cognitive Science | RQ5-adjacent | Reframe → distributed/extended cognition; feeds Track II/III |
| M59 HCI | interface design | Reframe → cognitive-artifact / augmentation design |
| M55 AI Ethics | RQ4 core (governance-at-scale) | Narrow → agency/autonomy of the extended self |
| M50 Gamification | RQ-core (via phase-map) | **Demote → elective** under N07 |
| M54 Virtue & Vice Modeling | RQ3 core | **Demote → elective** |
| M52 Affective Computing | RQ5-adjacent | Keep; supports nRQ2 affect regulation |

Modules M02–M45/M48/M51/M53/M56/M57/M60 and all of M62–M67: **kept, unchanged**, roles noted above.

---

## 6. Open decisions requiring Scott's judgment

1. **New-module numbering:** `N01–N07` (clear "new") vs. `M68–M74` (continues the series)?
	1. Is there a way to determine the impact of changing module names? For example, M01 stays (M for math), but use track prefixes for the other modules and group them into discrete chunks? Or should we keep just the series as it is, M68-M74, and go from there?

2. **How many new modules to actually generate vs. hold as scaffolded stubs.** Recommend
   generating **N01 (Extended Mind)** and **N03 (Cognitive Neuroscience of EF)**
	1. Lets not generate anything, but lets keep track of the order modules should be generated. I'd like to try and delegate that task to Hermes to generate the modules.
3. **Demote or delete M50/M54?** Proposal demotes (keeps content, removes RQ-core status).
   Deleting would ripple into SCORECARD/overview totals.
	1. Demote
4. **Track vs. phase vocabulary:** replace "Phase 0–5" with "Track I–VI" everywhere, or keep
   phases as the *sequencing* mechanism and add tracks as a cross-cutting *tag*? (Recommend the
   latter — less ripple, phases still drive prerequisites.)
	1. Keep phases as sequencing, and tracks as cross-cutting tag.
5. **Reading-list depth:** the new Track II/IV modules are humanities-heavy; confirm the
   `reading_level: doctoral` calibration and archive-coverage expectations for non-CS material.
	1. Yes, please. We should strive for a doctoral reading level, but remember, I'd like to develop that skill with the help of AI. If I had to read a dense paper on my own, I'd struggle to stay engaged. I need a framing for dense and complex topics that keeps sustained engagement with it. But we should adjust archive-coverage expectations and look to fill in as many of the missing gaps and expand our existing domains further.

**Next:** Decide §6.1 (numbering) and §6.2 (which new modules to generate first); then a
follow-up session can scaffold N01 and N03 using `/phd-generate` — no existing module is touched.
