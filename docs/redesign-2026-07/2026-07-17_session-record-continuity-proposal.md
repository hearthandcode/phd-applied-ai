---
type: methodology-proposal
title: "Session-Record Continuity: A Review-Gated Capture Proposal"
domain: research/methodology
status: proposal
created: 2026-07-17
updated: 2026-07-17
tags: [methodology, session-records, provenance, continuity, human-review, privacy, proposal]
graph_refs:
  - docs/session-log-process.md
  - sessions/README.md
  - docs/redesign-2026-07/2026-07-17_agent-assisted-capture-contract.md
llm_accessible: true
generated_by: methodology-redesign
verified: false
---

# Session-Record Continuity: A Review-Gated Capture Proposal

## Status and scope

**Proposal.** This document proposes a safer continuity process for future session records. It does not rewrite historical logs, create a backfill, alter aggregate indexes, collect telemetry, install an agent integration, or change public disclosure policy.

## Problem framing

An incomplete or stale record is a method signal. It may indicate that capture, review, or indexing is too fragile for the work being studied. It is not evidence of a person's unrecorded state, activity, or experience.

The proposed change is from automatic interpretive log writing toward a low-friction review queue that keeps observable events, subject report, agent interpretation, and human acceptance distinct.

## Four record planes

| Plane | What it contains | Authority | It must never become |
|---|---|---|---|
| Observable event receipt | Tool activity, explicit instruction, artifact change, session gap, or capture prompt. | Clearly labeled system or tool receipt. | A claim about mood, cognition, consent, or authorship. |
| Pending capture | An optional prompt, user-provided answer if any, and defer/skip state. | The subject controls the answer and whether it proceeds. | Silent memory injection or automatic publication. |
| Draft session record | A reviewable candidate that separates subject report, observed evidence, and provisional interpretation. | Draft only. | Sealed research data or a substitute for subject review. |
| Derived index or analysis | Audit indexes, scorecards, summaries, or later coding views derived from accepted records. | Derivative of source evidence. | A reconstruction that guesses missing hours or experience. |

## Proposed lifecycle

```text
observable event
  -> pending capture or explicit no-capture decision
  -> optional subject response
  -> reviewable draft session record
  -> accept, amend, reject, or defer
  -> only an accepted record may feed a derived index
```

A capture may be skipped without penalty. A blank answer is not consent, and an unreviewed draft is not analytical evidence.

## Appropriate capture triggers

A future assistant may create a **pending** capture, never a public log entry, only when there is an explicit basis such as:

1. a user reports task-initiation friction, interruption recovery, a notable cognitive-load shift, a trust change, or an authorship concern;
2. a user asks for continuity after a meaningful gap or reports whether continuity succeeded or failed;
3. a bounded research, methodology, or platform decision arises from stated lived experience;
4. a user corrects, rejects, or reclaims an AI output in a way relevant to agency or correction load; or
5. a user explicitly asks to log or backfill a session.

An agent must not infer these triggers from message length, typing latency, tool use, Git activity, or a model theory about the person.

## Optional prompt and interruption policy

When an interruption is appropriate, an optional prompt may ask:

1. What was your state just before this moment?
2. What exactly was stuck, changing, or at stake?
3. What did the AI or other scaffold do that mattered?
4. What changed afterwards, if anything?

During deep work, the system should defer the prompt and preserve only a visible, dismissible pending marker. It must not demand documentation or write an inferred account in the meantime.

## Closure and recovery

A draft may summarize durable artifacts, subject report actually provided, observed evidence, provisional interpretation, what remains unreported, review state, and one restart point.

At a later session, a recovery check can ask:

1. Was a draft left pending review?
2. Is there a durable source for a possible backfill?
3. Does the subject want to discuss the gap, defer it, or preserve it as a recorded absence?
4. Can the restart locate the thread, source artifact, and next action without recreating private experience from traces?

No backfill should be created without a disclosed durable source and the subject's review. Derived indexes should use only accepted source records and source-established values.

## Required source separation

| Layer | Required label | Permitted content |
|---|---|---|
| Subject report | `subject_report` | An answer actually provided, or a clearly quoted/paraphrased statement. |
| Observable interaction | `observed_event` | A source reference, tool receipt, prompt, artifact update, or documented gap. |
| Provisional interpretation | `agent_interpretation` | A proposed design hypothesis clearly labeled as provisional. |
| Human review | `review_state` | Pending, amended, accepted, rejected, or deferred. |

A tool record can never fill an empty `subject_report` field. A generated summary must preserve `not-recorded` rather than invent a plausible state.

## Privacy and publication boundary

- Pending capture state is not permanent memory and is not injected into later prompts by default.
- The minimum data necessary for a review decision should be retained.
- Raw transcript copies should not be collected by default.
- Any public-facing record requires review of the exact text, even where a disclosure policy exists.
- A public methods document may describe safeguards. It must not expose an unreviewed record inventory, prompts, third-party information, or sensitive data.

## Relationship to passive capture

Existing passive capture can be helpful for recall, but automatic interpretive writing can blur observation, inference, and subject report. This proposal does not invalidate earlier drafts. If adopted, a separate reviewed amendment should replace automatic public-log writing with a pending-capture workflow, source-separation schema, and small closure/recovery loop.

## Open decisions

1. Which types of work count as session-relevant under a knowledge-workbench program?
2. What is the lowest-friction review interaction that still makes acceptance and correction legible?
3. When should any controlled coupling codes be applied: entry, closure, or later analysis?
4. What retention and deletion rules should apply to deferred or rejected pending-capture records?
