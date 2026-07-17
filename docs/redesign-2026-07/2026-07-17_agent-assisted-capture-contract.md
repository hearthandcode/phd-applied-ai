---
type: architecture-proposal
title: "Agent-Assisted Session Capture Contract: Pending, Reviewable, and Human-Governed"
domain: research/architecture
status: proposal
created: 2026-07-17
updated: 2026-07-17
tags: [agents, session-capture, provenance, human-review, privacy, architecture, proposal]
graph_refs:
  - docs/redesign-2026-07/2026-07-17_session-record-continuity-proposal.md
  - docs/redesign-2026-07/hermes-exocoreos-session-capture-roadmap.md
llm_accessible: true
generated_by: agent-assisted-capture-design
verified: false
extended:
  implementation_authority: none
  data_classification: review-gated-research-support
---

# Agent-Assisted Session Capture Contract

## Status and scope

**Source-only architecture proposal.** This contract does not authorize a plugin, profile, background process, telemetry field, storage schema, provider call, or public-log mutation. A future implementation must re-inspect current runtime documentation and source before choosing any hook or storage API.

## Purpose

Automatic support can reduce the friction that leaves a longitudinal record incomplete. It becomes methodologically weak if an agent turns its interpretation into self-report or silently publishes a draft.

This contract permits an agent to record that an observable capture opportunity occurred, offer an optional prompt, retain an explicitly pending response for review, and assemble a draft from supplied data. It does not let the agent decide research meaning, create self-report, write public session logs, or seal a record.

## Non-goals

- Clinical assessment, emotion classification, behavioral profiling, or mental-state inference.
- A default memory store or hidden future-prompt context source.
- A background pipeline that writes or edits session records.
- A runtime-specific API proposal or deployment plan.
- A replacement for an existing session-log source of truth or human review.

## State machine

```text
observed
  -> ignored | pending
pending
  -> deferred | dismissed | answered
answered
  -> draft-ready | dismissed
draft-ready
  -> accepted | amended | rejected | deferred
accepted
  -> linked-to-session-record
```

Every transition must be visible to the subject. A missing answer remains `pending`, `deferred`, or `dismissed`. It is never silently promoted to `answered` or `accepted`.

## Canonical capture-record shape

A later implementation may serialize this contract as YAML, JSON, SQLite, or another local format only after a separate review.

```yaml
schema_version: "0.1"
capture_id: null
created_at: null
source_session_ref: null
state: observed # observed | pending | deferred | dismissed | answered | draft-ready | accepted | amended | rejected
trigger:
  class: explicit-user-report # explicit-user-report | explicit-log-request | session-gap-check | observable-work-boundary
  observed_event_ref: null
  rationale: null
subject_report:
  provided: false
  answers: []
  consent_to_draft: false
agent_interpretation:
  present: false
  text: null
  status: prohibited-until-subject-report # prohibited-until-subject-report | proposed | rejected
linked_artifacts: []
privacy:
  visibility: local-review-only
  source_export_allowed: false
  retention_review_at: null
review:
  state: pending
  reviewed_by: null
  reviewed_at: null
  notes: null
provenance:
  creating_surface: null
  tool_or_agent_id: null
  schema_version: "0.1"
```

## Invariants

1. `subject_report.provided: false` requires `agent_interpretation.present: false`.
2. An agent may draft only from explicit subject answers plus observable artifact evidence, with the layers labeled separately.
3. `accepted` requires explicit human review. It does not set `verified: true` on a session record.
4. No capture record is public by default. `source_export_allowed` begins `false`.
5. Deletion, retention, and archive decisions are human-governed and auditable.
6. Capture state never becomes automatic memory, profile data, or model context.
7. Tool telemetry is an observed event only. It must not become a cognitive, diagnostic, or phenomenological field.

## Component responsibilities

| Component | Permitted responsibility | Forbidden responsibility |
|---|---|---|
| Trigger detector | Detect explicit requests, session gaps, named capture events, or observed artifact boundaries. | Infer attention, affect, diagnosis, comprehension, or consent. |
| Prompt renderer | Offer up to four dismissible questions and defer during active flow. | Require an answer, interrupt critical work, or coerce disclosure. |
| Local queue | Preserve state, source links, retention metadata, and review status. | Become a default knowledge-memory corpus or sync to a public repository. |
| Draft assembler | Produce a clearly labeled candidate from supplied answers and cited observable events. | Fabricate subject report, produce a sealed log, or hide uncertainty. |
| Export bridge | Create a review packet or explicit draft for human inspection. | Write a public log without human command and final text review. |
| Evaluator | Report queue health, unanswered rate, review latency, and capture failure modes. | Claim a clinical or cognitive outcome from the data. |

## Minimal interaction design

A future surface may support actions equivalent to:

```text
capture status
capture pending
capture answer <capture-id>
capture defer <capture-id>
capture dismiss <capture-id>
capture draft <capture-id>
capture review <capture-id>
```

These labels are examples, not an approved command surface. A renderer-free Markdown/YAML fixture and manual review workflow are valid first proofs.

## Privacy and provenance

- Store the smallest amount of data required for a pending decision.
- Preserve source references and timestamps, while avoiding raw transcript copies by default.
- Do not transmit a capture record to a provider, gateway, dashboard, or external repository without reviewed policy and explicit action.
- Separate a prompt issued from an answer supplied. A skipped prompt is a valid method outcome.
- Let a review packet cite a capture ID and structural status without disclosing content.
- Make deletion or retention auditable without retaining sensitive content longer than necessary.

## Testable first proof

A later local proof should validate only this narrow behavior:

1. Create one observable-event fixture.
2. Generate one pending capture with no subject report.
3. Confirm that no agent interpretation or session-log body is created.
4. Provide an explicit synthetic subject response in the fixture.
5. Assemble a draft that visibly separates subject report, observed event, and provisional interpretation.
6. Confirm that review is required before export and that no public-repository write occurs.
7. Delete or defer the fixture and verify that no hidden memory/context record remains.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Capture interrupts deep work. | Use explicit triggers, a defer action, and a visible but quiet pending marker. |
| The agent records only successes. | Include correction, distrust, interruption, and deferral as valid event classes. |
| Telemetry is mistaken for subjective data. | Enforce source separation and prohibit inference fields. |
| Pending state becomes hidden surveillance. | Keep it local, reviewable, minimal, non-default, and excluded from memory/context. |
| Public logs expose private data. | Require exact text review and separate publication policy before export. |
| Tool/runtime details become stale. | Re-inspect current surfaces before implementation. |

## Decision gates

1. Is a review queue acceptable as the default alternative to automatic public-log writing?
2. Is a plain local fixture sufficient before any runtime plugin is considered?
3. Which retention period and deletion route make deferred capture safe and practical?
4. Does a proposed adapter preserve agency and returnability better than a manual end-of-session prompt?
