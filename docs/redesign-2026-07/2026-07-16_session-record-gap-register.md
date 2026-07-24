---
type: research-record-register
schema_version: "1.0"
title: "Session Record Gap Register and Recovery Protocol"
domain: research/methodology
kind: register
status: draft
created: 2026-07-16
updated: 2026-07-16
reviewed_by: null
reviewed_at: null
review_notes: "Draft inventory. It records repository evidence only and never reconstructs unreported subjective experience."
revision: 1
hub_canonical:
  artifact_id: phd-research-evidence-framework-v1
  authority_class: hub-canonical-foundation
  projection_status: internal-only
  authority_pointer: "See the Hub PhD research-program source using this stable artifact ID; no private local path is disclosed here."
supersedes: null
superseded_by: null
related:
  - sessions/README.md
  - docs/session-log-process.md
  - AUDIT_LOG.md
  - SCORECARD.md
  - docs/redesign-2026-07/methodology-refinement-after-external-feedback.md
  - docs/redesign-2026-07/2026-07-16_knowledge-workbench-research-redesign-plan.md
graph_refs:
  - sessions/README.md
  - AUDIT_LOG.md
  - SCORECARD.md
  - docs/session-log-process.md
  - docs/redesign-2026-07/2026-07-16_knowledge-workbench-research-redesign-plan.md
tags:
  - session-logs
  - methodology
  - provenance
  - gap-recovery
  - audit-trail
  - research-record
llm_accessible: true
generated_by: "Virgil / orientation-and-redesign"
verified: false
---

# Session Record Gap Register and Recovery Protocol

## Recognition

- **Why this exists:** The session log is the declared source of truth for the longitudinal record, yet the repository has periods with no dated log and its master audit index remains empty. The gap itself is a finding about the capture process and should be made visible without fabricating experience.
- **Where it belongs:** `docs/redesign-2026-07/` until the research program and session schema are reviewed. It is a methodology-facing register, not a replacement for session files or the master audit index.
- **What Scott should recognize:** Missing capture is not a personal failure or an excuse for retrospective invention. It identifies where a future scaffold must make ordinary research activity easier to record, review, recover, and distinguish from subjective self-report.
- **Papertrail:** Repository inspection on 2026-07-16 of `sessions/2026/07/`, `sessions/README.md`, `docs/session-log-process.md`, `AUDIT_LOG.md`, and existing methodology proposals.
- **Verification state:** Draft. It makes no claim that work occurred on a date solely because no session file exists.

## Evidence snapshot

### July 2026 dated session records found

| Date | Record status from file inventory | Notes |
|---|---|---|
| 2026-07-01 to 2026-07-08 | One date-named session file per day | Status and verification must be inspected individually before analytical use. |
| 2026-07-09 | No date-named session file found | Absence of a record does not establish whether a research-relevant session occurred. |
| 2026-07-10 | One date-named session file found | Status and verification must be inspected individually before analytical use. |
| 2026-07-11 | No date-named session file found | Absence of a record does not establish whether a research-relevant session occurred. |
| 2026-07-12 to 2026-07-13 | One date-named session file per day | Status and verification must be inspected individually before analytical use. |
| 2026-07-14 | No date-named session file found | Absence of a record does not establish whether a research-relevant session occurred. |
| 2026-07-15 | One date-named session file found | Draft close-out record, pending subject review. |
| 2026-07-16 | One date-named orientation record created | Draft, pending subject review. |

### Index divergence

`AUDIT_LOG.md` declares the session file to be the source of truth but currently reports `total_sessions: 0`, `total_hours: 0.0`, and a no-sessions placeholder. It therefore cannot currently function as a reliable index of the existing session corpus.

`SCORECARD.md` separately contains one non-zero module entry while its all-module total remains zero. This may be a pre-existing aggregation inconsistency. It must be reconciled from source records rather than corrected by estimation.

## Register rules

1. **Preserve sealed history.** Never alter a verified or `locked: true` session to make the new research framing look consistent.
2. **No invented self-report.** A backfill may identify observable artifacts, Git history, task receipts, and a subject's later retrospective statement. It must not infer mood, cognitive load, agency, or phenomenology from activity alone.
3. **Separate record types.** Keep subject report, observable artifact activity, tool-generated interpretation, and later verification distinct.
4. **Mark reconstruction.** Any future backfill must include a clear marker such as `[backfilled: YYYY-MM-DD, source: <durable evidence>]` and must state what remains unreported.
5. **Do not use a draft as analytical data.** `verified: false` records remain review material, not final evidence.
6. **Repair indexes only from evidence.** Populate `AUDIT_LOG.md` and scorecard totals only after the underlying session or module audit records establish the relevant hours and outcomes.

## Recovery queue

| Priority | Scope | Safe action | Stop condition |
|---|---|---|---|
| 1 | 2026-07-15 and 2026-07-16 draft records | Scott reviews, corrects, accepts, or rejects them. | No seal occurs without Scott's explicit confirmation. |
| 2 | Existing July session corpus | Create a read-only inventory of date, status, `verified`, `locked`, session type, and record links. | Do not rewrite historical tags or narratives. |
| 3 | Missing July dates | Identify durable artifact evidence and ask the subject whether a retrospective entry is wanted. | Do not create a backfill without a disclosed source and review route. |
| 4 | Master index | Draft a reconciliation report that distinguishes study sessions, meta sessions, and admin sessions. | Do not invent hours or update totals from uncertain material. |
| 5 | Future capture | Propose a minimal, reviewable event-to-log workflow with a visible pending state. | No automated public-log writes or telemetry expansion without approved privacy and methodology design. |

## Open methodological questions

1. Which events merit a session record under the knowledge-workbench thesis: lived cognitive events, design decisions, artifact transformations, or all of these with separate record types?
2. Which information should enter a public record, a private local ledger, a review queue, or no record at all?
3. What is the minimum capture experience that produces provenance and returnability without turning documentation into correction load?
4. How should historical RQ5 tags map forward after a new research-question source is approved without rewriting locked data?

## Next action

Create a read-only July session inventory and a proposed new session-record schema only after the redesigned research question and method packet receive review.
