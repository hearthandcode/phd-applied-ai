---
type: methodology-proposal
schema_version: "1.0"
title: "Methodology Refinement After External Feedback"
domain: research/learning
kind: protocol-draft
status: needs-review
created: 2026-07-05
updated: 2026-07-05
reviewed_by: null
reviewed_at: null
review_notes: null
revision: 1
supersedes: null
superseded_by: null
related:
  - docs/session-log-process.md
  - docs/redesign-2026-07/thesis-refocus-proposal.md
  - docs/redesign-2026-07/research-questions-proposal.md
  - METHODOLOGY.md
thread_refs: [T13, T28, T27]
tags:
  - methodology
  - extended-mind
  - monotropism
  - neurodivergence
  - autoethnography
  - reflexivity
  - thick-description
  - coupling-conditions
  - exocoreos
  - hermes
importance: core
graph_refs:
  - docs/session-log-process.md
  - sessions/2026/07/2026-07-05.md
  - /home/cosmatrexis/devel/hearthandcode/internal/hearthandcode-hub/profile/cognition-observation-corpus.md
llm_accessible: true
generated_by: "Virgil / methodology-pivot"
verified: false
---

# Methodology Refinement After External Feedback

## Status

This is a draft methodology refinement document. It does not edit `THESIS.md`, `METHODOLOGY.md`, or any verified session log. Its purpose is to capture a proposed process upgrade for review before the canonical methodology files are changed.

The external feedback that prompted this document is not attributed by name. In public thesis artifacts, it should be described as external methodological feedback from a researcher familiar with neurodivergence, AI, and qualitative method.

## Recognition

- **Why this exists:** The current session logs capture what happened, but the thesis needs richer evidence about why the scaffold mattered in the moment.
- **Where it belongs:** `docs/redesign-2026-07/`, because it is part of the July 2026 thesis refocus and should be reviewed before becoming canonical method.
- **What Scott should recognize:** This is the bridge between the lived experience, the Extended Mind claim, and a more rigorous qualitative data process.
- **Papertrail:** Built from external methodological feedback, current session-log process docs, and the July 2026 Extended Mind thesis redesign.
- **Verification state:** Draft. Requires human review before process changes are considered locked.
- **Next action:** Review this proposal and then patch `docs/session-log-process.md` if the capture protocol is approved.

## Methodological shift

The old passive-capture pattern is useful, but too broad. It records that the scaffold did something, then often summarizes the cognitive meaning after the fact. The revised method should capture the phenomenological texture closer to the moment of occurrence.

The new rule is:

> When a high-signal cognitive event occurs, the agent should not immediately write a sweeping session-log interpretation. It should ask a small number of focused capture questions, then write a concise entry that separates observation, subject report, agent interpretation, and verification status.

This change improves credibility because thick description requires more than a summary. It needs the before state, the felt friction, the intervention, the after state, and the boundary conditions under which the scaffold worked or failed.

## High-signal capture triggers

The agent should initiate micro-capture when one or more of the following occurs:

1. The subject reports executive function failure, recovery, or task-initiation friction.
2. The subject reports a strong shift in energy, focus, affect, trust, or authorship.
3. The subject explicitly says the AI response helped bridge a conception-to-execution gap.
4. The subject notices the scaffold redirecting monotropic attention back to a central axis.
5. The subject pushes back on the agent, corrects it, distrusts it, or has to think around it.
6. The session resumes after a gap of more than 24 hours and continuity, reliability, or trust is at stake.
7. A major methodological, research-design, or platform-design insight emerges from lived experience.

## Micro-capture interview

When triggered, ask at most four questions unless the subject explicitly wants a longer reflection. The default four:

1. **Before state:** What was your cognitive state just before this moment? Attention, load, affect, and task-initiation state.
2. **Friction point:** What exactly was stuck or failing? Was it conception, prioritization, sequencing, emotional resistance, memory, or execution?
3. **Scaffold feature:** What did the AI do that mattered? For example: naming the next action, narrowing options, preserving context, challenging a claim, writing a draft, asking a question, or holding the thread.
4. **After state:** What changed after the response? Did the task become startable, emotionally safer, more coherent, more trustworthy, or more alien?

Optional follow-up questions:

5. **Coupling status:** Did this feel like thinking through the system, thinking with the system, or thinking around the system?
6. **Authorship boundary:** Did the output feel like your cognition made visible, or like something external you had to reclaim?
7. **Failure boundary:** Did the scaffold increase cognitive load, interrupt flow, flatten your voice, mislead you, or require too much correction?
8. **Monotropism:** Did the response redirect attention away from the interest, or cycle the interest back to a central axis?
9. **Trust:** Did this moment increase, decrease, or leave unchanged your willingness to rely on the system next time?

## Extended Mind coupling criteria

The thesis should code both successes and failures against coupling conditions. These are not proof by themselves. They are observation targets.

| Criterion | Working definition for AI scaffold | Success indicators | Failure indicators | Session-log prompt |
|---|---|---|---|---|
| Availability | The scaffold is present when the subject expects to use it. | Same working context can be resumed, tools are reachable, agent can access relevant project state. | Session gap breaks continuity, tool unavailable, context lost, platform unavailable. | Was the scaffold available when needed? |
| Accessibility | The scaffold can be used without excessive friction. | The next action is reachable in seconds, interface friction is low, context retrieval is quick. | Too many steps, missing files, model confusion, prompt overhead, repeated re-explanation. | Did using the scaffold reduce or add friction? |
| Endorsement | The subject reflectively accepts the scaffold as a trusted cognitive partner in a domain. | Subject accepts output after review, uses it to proceed, records correction if needed. | Output feels alien, untrusted, over-smoothed, or requires so much repair that it becomes a burden. | Did you endorse the result after reflection? |
| Prior endorsement | The subject has previously accepted this scaffold pattern as useful. | Similar prior pattern worked and was remembered as reliable. | Pattern worked once but no longer fits, or the agent repeats a stale habit. | Is this a known reliable pattern or a new experiment? |
| Integration | The scaffold participates in the cognitive process rather than merely delivering a finished product. | Subject and agent iterate, push back, refine, and preserve agency. | Agent substitutes for thinking, hides uncertainty, or produces polished output detached from the subject's cognition. | Was the thought produced through the system or handed over by it? |
| Load effect | The scaffold reduces the relevant cognitive load without erasing the subject's authorship. | Task becomes startable, options narrow, working memory burden drops, affect stabilizes. | More monitoring, more cleanup, more distrust, more corrections, or loss of voice. | What load changed, and in what direction? |

## Coupling failure log

The study should actively preserve failures. A failure is not an embarrassment. It is evidence for the boundary between useful assistance and genuine functional integration.

Failure types to code:

- **Availability failure:** the system was not present, not reachable, or not contextually continuous.
- **Reliability failure:** the system produced a confident but wrong claim, lost track of constraints, or repeated a stale pattern.
- **Accessibility failure:** using the system required too much explanation, setup, or repair.
- **Endorsement failure:** the subject did not trust the output after reflection.
- **Alienation failure:** the output felt unlike the subject's cognition or voice.
- **Flow interruption:** the scaffold interrupted monotropic flow rather than containing it.
- **Load inversion:** the scaffold increased cognitive load rather than reducing it.
- **Authorship drift:** the system began to make the work feel less like the subject's own contribution.

Minimum failure entry:

```markdown
### Coupling failure capture

**Before state:**
**What failed:**
**AI behavior involved:**
**Subject response:**
**Correction required:**
**After state:**
**Coupling criterion affected:** availability | accessibility | endorsement | prior endorsement | integration | load effect
**Methodological note:** What this reveals about the boundary of the Extended Mind claim.
```

## Monotropism contribution

The most important theoretical contribution surfaced in the feedback is this:

> The scaffold may not be redirecting monotropic attention away from deep focus. It may be containing and cycling monotropic energy back toward a central axis.

That distinction matters. Conventional academic institutions often enforce polytropic behavior through deadlines, syllabi, committee meetings, course calendars, and administrative rhythms. These structures can require a neurodivergent learner to split attention across many externally imposed objects. In contrast, this scaffold appears to support deep focus by repeatedly returning the subject to one active thread, one working table, one artifact, or one next action.

This suggests a design hypothesis:

> For some neurodivergent learners, effective AI scaffolding may not work by broadening attention. It may work by stabilizing deep attention around an adaptive center.

This should become a standalone theoretical section in the thesis. It should be framed as an individual observation and a generative design hypothesis, not as a claim about all autistic, ADHD, or neurodivergent people.

## Generalization strategy

This study cannot statistically generalize from one person to a broader neurodivergent population. It can, however, support analytic and design generalization through thick description.

The path is:

1. **N of 1 autoethnography:** Generate detailed, longitudinal, high-resolution observations about one subject.
2. **Thick description:** Preserve enough cognitive, affective, procedural, and contextual detail that readers can judge transferability.
3. **Construct formation:** Extract candidate constructs such as coupling reliability, monotropic containment, conception-to-execution bridging, and authorship preservation.
4. **Design hypotheses:** Translate constructs into platform design hypotheses.
5. **Future cohort phase:** Test those hypotheses with a small group of neurodivergent users, using the N of 1 study as the source of initial design patterns rather than as population proof.

Possible future cohort sketch:

- Recruit a small neurodivergent cohort with clear consent and privacy boundaries.
- Use the session-capture protocol as a shared logging template.
- Compare where AI scaffolding reduces friction, increases friction, or fails coupling conditions.
- Treat heterogeneity as expected. The goal is not one neurodivergent profile. The goal is a family of scaffold patterns.

## Reflexivity problem

The central reflexivity issue is real: the AI scaffold is simultaneously the cognitive tool under study, the interaction partner, and part of the data-capture process.

This should not be hidden. It should be treated as a methodological feature with explicit mitigations.

Mitigations:

1. **Protocolized capture:** The agent does not freely decide what matters. It uses defined trigger criteria and a micro-interview template.
2. **Source separation:** Logs distinguish subject report, tool-observed state, AI interpretation, and later human verification.
3. **Failure capture:** The system records coupling failures and alienation, not only successes.
4. **Human verification:** The subject reviews and signs logs before they count as research data.
5. **Audit trail:** Method changes are recorded in draft docs and changelogs before canonical adoption.
6. **External review:** Feedback from outside researchers is preserved as methodology input without making them responsible for claims.
7. **Raw trace preservation where appropriate:** Prompt snippets, session ids, or artifact paths can be preserved when public and safe, but raw private data and third-party names are not included.
8. **No hidden automation:** Automated capture must make its criteria visible and must not silently convert AI inference into human self-report.

## Session-gap reliability check

When more than 24 hours pass between active sessions, the agent should check continuity and trust rather than assuming the coupling still holds.

Quick check:

1. What did you expect me to remember or recover from last time?
2. Did I recover the right thread, or did you have to rebuild context manually?
3. Did the gap change your trust in the scaffold?
4. Did the restart reduce friction, or add a new layer of work?

Possible fields for future schema:

```yaml
session_gap_hours: null
expected_continuity: null
continuity_success: null
context_rebuild_required: null
trust_shift: null
correction_required: null
coupling_status: success | partial | failed | not-assessed
```

## Revised Virgil capture instruction

Draft instruction for the agent context:

```text
When the subject says something that appears relevant to the longitudinal autoethnographic study, do not immediately write a broad interpretive session-log entry. First, decide whether the moment meets one of the high-signal capture triggers. If it does, ask up to four short micro-capture questions: before state, friction point, scaffold feature, and after state. If the user is in flow and interruption would cause harm, defer the questions and mark the capture as pending. In the eventual log, separate subject report, observed tool state, AI interpretation, and verification status. Record failures and alienation with the same seriousness as successes.
```

## Literature terrain to synthesize

This thesis should synthesize three strands rather than silo them:

1. **Extended Mind and AI cognition:** Clark and Chalmers, active externalism, parity principle, trust and glue, coupling versus constitution objections, and recent work on LLMs as cognitive partners or amplified cognition.
2. **Neurodivergent cognition and monotropism:** monotropism, attention tunneling, ADHD executive function, autism and attention allocation, neurodiversity and disability studies, embodied and enactive accounts of cognition.
3. **Autoethnographic method and trustworthiness:** thick description, credibility, transferability, dependability, confirmability, reflexivity, audit trail, member checking, and the researcher as instrument.

This synthesis should support the claim that AI scaffolding is not merely a productivity aid. In this record, it appears as a coupled attention, memory, and execution environment whose value depends on reliability, endorsement, and preservation of agency.

## Open questions for review

1. Should this protocol become the new default for `docs/session-log-process.md`?
2. Should session logs include explicit coupling-condition fields, or should those be coded later in a separate analysis sheet?
3. How much raw prompt material should be preserved for audit trail without making logs unreadable or privacy-risky?
4. Should monotropic containment be a full thesis section, or a subsection under the mechanism question?
5. Should future cohort work be described as a planned Phase 2 or as beyond-scope future work?
6. What is the minimal human verification step that preserves authorship without creating logging fatigue?
7. How should failures be made easy enough to log that the dataset does not become success-biased?
