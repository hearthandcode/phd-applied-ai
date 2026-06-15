# Pedagogical Foundations — Research Basis for Curriculum Design

Research literature supporting the learner-centered design rules in this curriculum.
Rules are codified in `docs/generate-module.md` and `docs/generate-phase.md`.

*Citations reflect author knowledge as of August 2025.*

---

## Cognitive Load Theory (Sweller, 1988; Paas, van Gog & Sweller, 2010)

Three types of load on working memory:
- **Intrinsic** — complexity inherent to the material (cannot be eliminated)
- **Extraneous** — load from poor presentation (reducible by design)
- **Germane** — load contributing to schema formation (should be optimized)

Dense symbolic exposition creates high extraneous load: symbol parsing, dependency tracking, and semantic grounding run simultaneously, compounding rather than adding linearly. Design responses:
- **Symbol reference card** — pre-builds semantic scaffolding before formal notation appears
- **Memory tier system (CARRY / RECONSTRUCT / LOOK UP)** — licenses external reference for low-priority items, freeing working memory for high-priority conceptual load
- **Conceptual bridge rule** — provides pre-built semantic scaffolding before formalism

---

## Dual-Coding Theory (Paivio, 1971)

Verbal/conceptual and visuospatial representations are processed in complementary cognitive channels. Providing both activates more of working memory productively rather than overloading it.

Design response: **Cross-modal quad** — every concept represented in all four modes:
1. Symbolic (formula / formal statement)
2. Geometric (ASCII diagram or spatial description)
3. Narrative metaphor (plain-language analogy)
4. Exercise (procedural / motor channel)

Each representation adds encoding pathways without competing with the others.

---

## Multimedia Learning Theory (Mayer, 2009)

Key principles relevant to text-only curriculum delivery:
- **Modality principle** — words + visuospatial content superior to words alone
- **Signaling principle** — organizational cues reduce extraneous load
- **Coherence principle** — remove material that doesn't serve the learning goal

Design responses:
- **Pre-reading map** — implements signaling (organizational cue at the top of every file)
- **Cross-modal quad** — implements modality principle in text form (describing geometry activates the visuospatial channel through language)

---

## Desirable Difficulties and Retrieval Practice (Bjork & Bjork, 1992; Roediger & Karpicke, 2006)

Certain learning difficulties improve long-term retention despite reducing short-term performance. Retrieval practice — attempting to recall without looking — is the most robust desirable difficulty in the literature.

Design responses:
- **"Explain it out loud" prompts** — implement retrieval practice (reconstruct from memory, not re-read)
- **RECONSTRUCT memory tier** — desirable difficulty by design: the learner can derive it, but must work for it
- **CARRY / RECONSTRUCT / LOOK UP distinction** — explicitly separates what to internalize vs. what to derive vs. what to externalize, making the encoding priorities visible to the learner

---

## Working Memory and Executive Function in ADHD (Willcutt et al., 2005; Martinussen et al., 2005; Barkley, 1997)

Working memory is a core deficit domain in ADHD, distinct from processing speed or general intelligence. Barkley's behavioral inhibition model: difficulty inhibiting irrelevant information actively increases working memory load. Time blindness — difficulty perceiving elapsed time — is a characteristic ADHD presentation.

Design responses:
- **Checkpoint system** — creates explicit save points, addressing time blindness and reducing anxiety about position within a long task
- **CARRY / LOOK UP distinction** — licenses external reference for low-priority items, effectively expanding functional working memory for the high-priority conceptual load
- **Computational exercises** — immediate feedback (strong ADHD-compatible reinforcer); removes motor-initiation demand of paper derivation; enables exploration (change a number, observe the change)

---

## Universal Design for Learning (CAST, 2018)

Three principles: multiple means of Representation, Action/Expression, and Engagement.

Design responses:
- **Cross-modal quad** — implements multiple means of Representation
- **Computational exercises** — implements Action/Expression (removes modality barrier for learners whose natural expression is through code rather than pen)
- **Checkpoint and self-assessment structure** — implements Engagement (learner decides when to stop; metacognitive scaffolding before the answer is given)

---

## Notes on application

These principles inform the generation spec rules and the learner-centered design rules in `docs/generate-module.md`. They are not cited inline in module content — they are the design-time rationale, not learning objectives for the curriculum itself (unless specifically relevant, e.g., in M57 or M58 on educational psychology and adaptive learning).

The learner profile schema (`curriculum/learner-profile-schema.json`) parameterizes these principles per learner: formalism density, example density, exercise format, and memory tier calibration can all be adjusted to serve different cognitive profiles.
