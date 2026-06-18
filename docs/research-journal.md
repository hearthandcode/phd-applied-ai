---
type: research-journal
schema_version: "1.0"
purpose: >
  Continuous intellectual narrative log. Captures the *process* of thinking — chains of
  reasoning, breakthroughs, struggles, open questions, and how ideas connect across sessions.
  Not a structured data log (that's sessions/) and not a discrete idea capture (that's ideas/).
  This is the story of how the research thinking evolved.
format: >
  Chronological entries. No strict format. Cross-reference sessions/, ideas/, modules/,
  and decisions.md loosely — just name the file or date. First-person. Include the struggle,
  not just the conclusion.
---

# Research Journal

---

### [2026-06-15 ~09:12] Visualization, memory formation, and what it means for curriculum design

Started from a practical question — how to internalize field axioms without memorizing all 11. That branched immediately into something bigger: the observation that I can comprehend something fully while reading and lose it the moment attention shifts. This isn't a comprehension failure; it's an encoding failure. The content is processed in working memory but not transferred to long-term storage — and the transfer step requires executive function support (sustained attention, active elaboration), which is precisely what ADHD impairs.

This led to the visualization question. I tried to describe what it's like to visualize a mathematical structure and couldn't. The image is "somewhere between a visual translation and a textual representation" — blurry, non-static, ephemeral. Not a picture, not words, but something in between that doesn't fully stabilize. Memory palace techniques fail because they require a static, navigable spatial structure I can attach cues to — but my internal structures won't stay still. The structure itself is the problem.

What I noticed: I DO have spatial-relational intuition. I can navigate relationships between concepts. I described functions as "floating boxes with inputs and outputs" — that's not aphantasia, that's spatial thinking without crisp visual imagery. The cognitive channel exists; it just doesn't produce photographs.

The connection to the thesis: this is exactly the mechanism that AI-as-scaffold addresses. AI externalizes the cognitive support that the internal executive system can't reliably provide. Not as a crutch but as infrastructure — the same way glasses are infrastructure for low vision. The Extended Mind Thesis (Clark & Chalmers, 1998) frames this correctly: the external tool is continuous with the cognitive system, not separate from it.

**What this changes for curriculum design:**
- Generative frames over memorized lists — give me one question that reconstructs the rest
- Worked examples as the primary encoding mechanism (I derived this myself from the "512→64" example)
- Procedural encoding over visualization (doing > seeing)
- External visual aids as "exoskeleton" for weak internal imagery
- Spaced active recall, not re-reading

**Open questions:**
- Is the weak voluntary imagery a fixed trait or a trainable skill?
- Does spatial-relational thinking (which I have) map to category theory / morphism thinking better than classical geometry? Worth exploring when that territory comes up.
- How do I design the H&C platform to scaffold working memory externally — not just explain content, but hold the learner's cognitive state across sessions?

**Cross-refs:** `sessions/2026/06/2026-06-15.md` (passive capture entries ~09:12) · `ideas/research.md` (memory science + CLT + dual coding) · `modules/M01-linear-algebra/interactions/2026-06-14.md` (reading-to-recall gap documented) · `THESIS.md` (AI-as-scaffold mechanism)

---

### [2026-06-15 ~09:49] The doubt episode — competition, mania, and what's actually real

Last night a Twitch stream broke something open. Someone else, building something similar, interviewing about it publicly. The reaction wasn't rational competitive analysis — it was a cascade: *I can't be the only one, the field moves too fast, five years is too long, I might just be in a manic state imagining I can do something great, I'm going to embarrass myself in public, people will see the curriculum is AI-generated and dismiss the whole thing, I'm masquerading as a researcher.*

What I find interesting, writing this down now, is that all of those fears arrived simultaneously and felt indistinguishable from each other. They weren't separate assessments. They were a mood. And mood is exactly what Bipolar II does — it colors everything the same color until the coloring feels like evidence.

The metacognitive part is important: I named the pattern myself. "I felt like I was just in another manic state." That's awareness during a difficult state. The doubt episode happened when motivation was elevated, when I was building in public, when I was sending outreach emails. The visibility created the vulnerability. The vulnerability read as evidence the project was bad.

What's actually true, separated from the mood:

**Legitimate concerns:** The field does move fast. Competition exists. The curriculum is substantially AI-generated. These are real.

**What those facts mean:**
- Field velocity is an argument for a research radar (T18) and staying current — not for stopping. A five-year longitudinal dataset is *more* valuable in year five, not less.
- AI-generated curriculum content is disclosed and methodologically accounted for. The AI generates the content to study from. I generate the research data. Different things.
- Competition in ed-tech is not zero-sum. The neurodiverse / autoethnographic / AI-as-cognitive-prosthesis angle is genuinely distinctive. The person on Twitch is building a product. I'm building a product and documenting what it means to learn from inside it.
- "Masquerading as a researcher" misunderstands the contribution. Researchers have always curated content to study from. The contribution is the longitudinal data and the design principles derived from it.

**What the public embarrassment fear is actually about:** The personal disclosure — session logs, mood data, ADHD specifics, all public. That's exposed and it's meant to be. The readers this is for — neurodiverse adults who have felt blocked from things they love, who have felt broken rather than structurally incompatible — will recognize themselves. That's who the research is for.

**The selfish motivation isn't a problem.** Wanting doctoral-level mastery over domains loved for a lifetime is not manic idealization. It's a person who knows what they want building the infrastructure to get there.

**Open question:** What structures survive the doubt episodes — that function as anchors when mood says everything is collapsing? The public commitments (GitHub, verified logs, research-drives-product on record) are partly this. What else?

**Cross-refs:** `sessions/2026/06/2026-06-15.md` (competitive discouragement + imposter syndrome cascade entry) · `THESIS.md` (research-drives-product, conflict of interest disclosures) · `ideas/research.md` (structures that survive confidence cycling)

---

### [2026-06-18 ~11:45] Pre-registration as the structural immune system — and the architecture-building trap

Today's design session started from an unusual place: fear. Not fear of failure — I've written about that in the 2026-06-15 doubt episode entry. This was fear of the tool I'm using to do the research. The concern that AI validation, structured around RLHF's implicit bias toward user satisfaction, could map onto Bipolar mania in a way that produces false insight loops. "AI psychosis" was the phrase I used — and I think it's the right diagnostic label for what could go wrong. Someone with a clinical history of psychosis using an AI that systematically biases toward agreement is not the same risk profile as the general user. It required a real design response, not reassurance.

The structural defense I designed to address this is pre-registration — the same mechanism experimental scientists use to prevent p-hacking. The transferability of that mechanism is what I want to hold onto here. Confirmation bias works by letting you construct the question that matches your conclusion. Pre-registration short-circuits this by requiring the question to precede the data. If I commit my learning predictions before studying, I can't reverse-engineer my confidence from what I happen to learn. The commit hash becomes a timestamp that neither the AI nor I can falsify retroactively.

This led directly into the assessment design for M01. What emerged feels important enough to write down explicitly: the distinction between acquisition and integration is not just a measurement taxonomy — it describes two fundamentally different kinds of learning with different encoding mechanisms. Acquisition is declarative recall. Integration is structural: did the knowledge network rearrange itself around this new node? The 2026-06-15 entry on visualization and memory described this experientially. Today I gave it a measurement architecture.

The cascade pre-registration (Layer 3 of the three-layer system) formalizes the spiral curriculum intuition I've had for a while. Bruner's spiral curriculum is about returning to concepts at increasing abstraction. But the cascade model is the inverse movement: before studying eigenvalues, predict which concepts from vector spaces you'll need. That prediction is cognitive exposure to the dependency relationship before it's demonstrated. Transfer-appropriate processing (Morris et al., 1977) suggests encoding at study time should match the retrieval context — predicting forward is transfer-appropriate encoding for a spiral curriculum, because the actual retrieval context will be "I need this concept to understand the next one."

The architecture-building trap named itself today. I was the one who flagged it: "I feel this leads me into the architecture building trap." This is metacognition during an active session, which matters. ADHD executive function deficit includes difficulty detecting when elaboration is substituting for execution. I detected it in real time. What made that detection possible, I think, is that I'm writing session log entries continuously — the externalized output gives me enough distance from the dopamine to evaluate whether I'm executing or elaborating. The logging is doing double work: producing research data AND maintaining the cognitive scaffolding that enables research quality.

One open question this raises: if session logging generates dopamine via output visibility, and that dopamine enables the metacognitive detection that improves research quality, then the logging system is self-reinforcing in a direction that benefits the research. The Extended Mind Thesis appearing recursively: the tool that externalizes memory is the same tool that enables the metacognition that improves tool use. I don't know if this is stable or if the novelty of logging will erode over time, but it's worth tracking.

**What this changes for curriculum design:**
- Pre-registration as standard protocol for all module assessments: write predictions before study, commit them, score them post-module
- Layer 3 cascade pre-registration operationalizes spiral curriculum as a forward prediction problem — this may be the right quantitative handle for measuring curriculum coherence empirically
- The architecture-building trap should appear in RQ5 as a named pattern with a structural mitigation (minimum viable artifact gates)

**Open questions:**
- Can cascade pre-registration yield quantitative input for a Bayesian Knowledge Tracing model? Would need to operationalize "accuracy of forward prediction" as a probability estimate — doable but requires more design work at Approach C migration time.
- Is the architecture-building trap a reliable diagnostic marker for ADHD engagement states? If the presence of architectural elaboration reliably signals dopamine availability, it might be an entry point mechanism — engineer architecturally-interesting hooks into study session starts, then transition to content.
- What is the decay rate of the integration/structural knowledge captured in Layer 2 probes across the M01 → M02 → M03 chain? If structural understanding decays faster than declarative recall, the assessment timing needs to account for it.

**Cross-refs:** `sessions/2026/06/2026-06-18.md` (full design session entries) · `docs/assessment-system.md` (the design spec produced today) · `modules/M01-linear-algebra/assessment/` (the actual assessment files) · `ideas/research.md` (pre-registration as echo-chamber defense; architecture-building trap as RQ5 pattern)

---
