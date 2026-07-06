---
type: technical-roadmap
schema_version: "1.0"
title: "Hermes and ExocoreOS Session Capture Implementation Roadmap"
domain: research/tooling
kind: implementation-plan
status: draft
created: 2026-07-05
updated: 2026-07-05
reviewed_by: null
reviewed_at: null
review_notes: null
revision: 1
supersedes: null
superseded_by: null
related:
  - docs/redesign-2026-07/methodology-refinement-after-external-feedback.md
  - docs/session-log-process.md
  - /home/cosmatrexis/devel/hearthandcode/internal/hearthandcode-hub/05-mechanism-annex--forge/hermes/hermes-plugin-interface-discord-thread-draft.md
  - /home/cosmatrexis/devel/hearthandcode/open-source/hermes-agent/plugins/cognitive-telemetry/__init__.py
thread_refs: [T13, T27, T28]
tags:
  - hermes
  - exocoreos
  - session-capture
  - cognitive-telemetry
  - plugins
  - methodology
  - extended-mind
  - neurodivergence
importance: core
graph_refs:
  - docs/redesign-2026-07/methodology-refinement-after-external-feedback.md
  - /home/cosmatrexis/devel/hearthandcode/open-source/hermes-agent/AGENTS.md
  - /home/cosmatrexis/devel/hearthandcode/open-source/hermes-agent/hermes_cli/plugins.py
  - /home/cosmatrexis/devel/hearthandcode/open-source/hermes-agent/plugins/cognitive-telemetry/plugin.yaml
llm_accessible: true
generated_by: "Virgil / methodology-pivot + hermes-agent"
verified: false
---

# Hermes and ExocoreOS Session Capture Implementation Roadmap

## Status

This is a draft roadmap. It does not modify Hermes Agent, ExocoreOS, or the PhD methodology. It translates the methodology refinement into a possible implementation sequence that can be reviewed before code is written.

## Recognition

- **Why this exists:** The thesis needs a more accountable capture process for AI-mediated cognition, and Hermes already has hooks and a cognitive telemetry plugin that can support this direction.
- **Where it belongs:** The PhD repo holds this as methodology-facing design. Implementation work belongs in `~/devel/hearthandcode/open-source/hermes-agent` or the hub-local ExocoreOS project after review.
- **What Scott should recognize:** This roadmap separates human-authored research meaning from automated telemetry. The agent can observe and prompt, but it must not silently turn its interpretation into human self-report.
- **Papertrail:** Based on local inspection of Hermes plugin docs, `hermes_cli/plugins.py`, the bundled `cognitive-telemetry` plugin, and the existing Hermes plugin-interface Discord draft.
- **Verification state:** Draft. Claims about existing APIs should be rechecked against Hermes `main` before implementation.
- **Next action:** Decide whether to begin with a local ExocoreOS plugin or an upstream Hermes PR sequence.

## Current Hermes surface verified locally

Hermes already supports a rich plugin system. The relevant existing surface includes:

- Directory plugins with `plugin.yaml` and `register(ctx)`.
- Bundled, user, project, and pip plugin discovery.
- `ctx.register_tool()` for plugin-defined tools.
- `ctx.register_hook()` for lifecycle hooks.
- `ctx.register_command()` for in-session slash commands.
- `ctx.register_cli_command()` for CLI subcommands.
- `ctx.register_skill()` for bundled skills.
- `ctx.dispatch_tool()` for plugin commands that call Hermes tools.
- `ctx.llm.complete()` and `ctx.llm.complete_structured()` for host-owned LLM calls.
- `ctx.register_context_engine()` and `ctx.register_platform()` for specialized integrations.
- Hook names including `pre_tool_call`, `post_tool_call`, `pre_llm_call`, `post_llm_call`, `pre_gateway_dispatch`, `on_session_start`, `on_session_end`, `on_session_finalize`, approval lifecycle hooks, subagent hooks, and Kanban lifecycle hooks.

The bundled `cognitive-telemetry` plugin already records passive per-tool telemetry to JSONL and validates markdown frontmatter on writes. It is observational, fail-open, and tested. That makes it the best starting point.

## Design principle

The capture system must preserve four boundaries:

1. **Human report versus AI interpretation:** The subject's answer is data. The agent's interpretation is analysis.
2. **Telemetry versus memory:** Operational events do not automatically become memory or prompt context.
3. **Prompting versus coercion:** The agent may ask short capture questions, but it should not create logging fatigue or interrupt deep flow without reason.
4. **Scaffold versus author:** Automation can reduce friction, but the subject remains the source of meaning, verification, and final authorship.

## Proposed implementation sequence

### PR 1: Extend cognitive telemetry schema for session continuity

**Goal:** Add a stable, versioned telemetry event shape for session continuity and restart friction without changing core model tools.

**Likely location:** `plugins/cognitive-telemetry/` and tests under `tests/plugins/`.

**Existing base:** `plugins/cognitive-telemetry/__init__.py`, `cogtel.py`, and `tests/plugins/test_cognitive_telemetry_plugin.py`.

**Schema sketch:**

```json
{
  "telemetry_schema_version": "0.2",
  "event_type": "session_continuity",
  "session_id": "...",
  "profile": "default",
  "surface": "cli|tui|gateway|cron|kanban",
  "previous_session_id": "...",
  "session_gap_hours": 27.5,
  "context_rebuild_required": true,
  "continuity_status": "success|partial|failed|not_assessed",
  "notes": null
}
```

**Use cases:**

- Measure gaps longer than 24 hours.
- Track whether the agent can recover the right working thread.
- Support Extended Mind availability and reliability coding.

**Tests:**

- Unit test JSONL write/read roundtrip with the new event type.
- Unit test sanitized session id behavior.
- Unit test missing previous session handling.
- Integration-style test with temp `HERMES_HOME`.

### PR 2: Add methodology capture event records

**Goal:** Add a second event type for high-signal cognitive capture prompts and responses.

This should not require the plugin to decide research meaning on its own. It records that a capture prompt was issued and stores structured subject answers only when explicitly provided.

**Schema sketch:**

```json
{
  "telemetry_schema_version": "0.2",
  "event_type": "methodology_capture",
  "capture_id": "2026-07-05T20-46-00Z-abc123",
  "trigger": "executive_function_recovery|monotropic_containment|coupling_failure|session_gap|authorship_boundary",
  "questions": [
    "What was your cognitive state before this moment?",
    "What was stuck or failing?",
    "What did the AI do that mattered?",
    "What changed afterward?"
  ],
  "subject_answers": [],
  "ai_interpretation": null,
  "verification_status": "pending"
}
```

**Use cases:**

- Produce auditable prompt history for session-log entries.
- Distinguish what the subject said from what the AI inferred.
- Prevent success-biased passive capture.

**Tests:**

- Build entry shape with each trigger type.
- Verify no subject answer is fabricated when no response exists.
- Verify telemetry remains fail-open on bad input.
- Verify PII-sensitive fields can be omitted or null.

### PR 3: Add a local ExocoreOS capture plugin using existing hooks

**Goal:** Build the research-specific behavior as a local or separate plugin first, not as a core Hermes feature.

**Reason:** Hermes project guidance says to keep the core narrow and avoid speculative infrastructure. A local ExocoreOS plugin is a concrete consumer that can prove the pattern before upstreaming generic surfaces.

**Possible hooks:**

- `on_session_start` to detect gap and prompt a continuity check.
- `post_tool_call` to append telemetry for tool-mediated friction or recovery.
- `transform_llm_output` only if used carefully to add a short capture prompt at the end of a response.
- `pre_gateway_dispatch` for messaging-platform capture cues.

**Command surface:**

```text
/capture status
/capture pending
/capture answer <capture_id>
/capture write-log <capture_id>
/capture config
```

**Expected behavior:**

- The plugin can propose a capture prompt, but it should not write public session logs automatically.
- The subject can answer in chat or skip.
- A later command can produce a draft session-log entry with source separation.

**Tests:**

- Hook registration test.
- Capture prompt generation test.
- Pending capture persistence test using temp plugin storage.
- No-log-without-answer test.
- Redaction and no-third-party-name test fixtures.

### PR 4: Propose generic durable plugin state or artifacts surface

**Goal:** If the local plugin proves useful, propose a generic Hermes-hosted plugin state API so plugins do not invent unsafe path conventions.

This matches the existing Discord draft suggestion but gives it a concrete consumer.

**Suggested API shape:**

```python
state = ctx.storage.namespace("session-capture")
state.put_json("pending/{capture_id}.json", capture_record)
record = state.get_json("pending/{capture_id}.json")
state.list("pending/")
state.delete("pending/{capture_id}.json")
```

**Required properties:**

- Profile-scoped path under Hermes home.
- Schema version metadata.
- Locking or atomic writes.
- Export and backup compatibility.
- Retention metadata.
- Provenance fields: plugin id, profile, session id, task id, timestamp, schema version.

**Use cases beyond this thesis:**

- Research review queues.
- Support-ticket cursors.
- Migration manifests.
- Content draft ledgers.
- Ops incident notes.

**Tests:**

- Temp `HERMES_HOME` storage isolation.
- Atomic write behavior.
- Profile separation.
- JSON schema migration stub.
- No prompt injection of plugin state by default.

### PR 5: Add documentation, examples, and integration tests

**Goal:** Document the full pattern as a reusable plugin methodology, not as a private thesis hack.

**Docs to add:**

- Plugin author guide: session-capture example.
- Cognitive telemetry guide: event schema and privacy boundaries.
- Example plugin: capture prompt plus pending answer workflow.
- Testing guide: temp `HERMES_HOME`, no real credentials, no network.

**Integration tests:**

- Plugin loads and registers command.
- Hook creates pending capture record.
- Command renders draft log from provided answers.
- No capture writes to public PhD repo without explicit command.
- Config disables capture prompts.

## ExocoreOS application

ExocoreOS can use the capture stream as part of its path-map and validation layer.

Possible ExocoreOS responsibilities:

- Know where the PhD methodology docs live.
- Know where draft session logs can be written safely.
- Know that verified logs are protected.
- Route capture records into review packets rather than directly into public logs.
- Track coupling-condition evidence without flattening it into memory.
- Provide a dashboard view of pending captures, failures, and continuity checks.

Minimum ExocoreOS data model:

```yaml
capture_id: string
timestamp: string
source_session_id: string
thread_refs: [T13]
trigger: string
subject_report_path: null
ai_interpretation_path: null
linked_artifacts: []
coupling_conditions:
  availability: null
  accessibility: null
  endorsement: null
  prior_endorsement: null
  integration: null
  load_effect: null
verification_status: pending | reviewed | rejected | logged
```

## Thesis application

The implementation supports these research claims more rigorously:

- The scaffold is not just useful. It can be observed against coupling criteria.
- Failures are part of the dataset, not exceptions to hide.
- Monotropic containment can be tested as a recurrent pattern.
- Human endorsement and verification remain visible.
- The AI's role as instrument is documented rather than disguised.

## Risks

| Risk | Mitigation |
|---|---|
| Capture prompts interrupt monotropic flow. | Ask at most four questions, allow deferral, and track skipped captures. |
| Agent selects only success stories. | Trigger list includes failures, alienation, distrust, and load inversion. |
| Public logs expose private data. | Use redaction rules, third-party name ban, and human review. |
| Plugin state becomes hidden memory. | Keep telemetry separate from memory and do not inject it by default. |
| Upstream PR is rejected as too private. | Prove value locally first, then upstream only generic surfaces. |
| Core footprint grows. | Prefer plugin and docs over new model tools. |

## Decision points

1. Build local ExocoreOS plugin first, or open upstream Hermes issue/spec first?
2. Keep capture records in Hermes telemetry, ExocoreOS storage, or both?
3. Should the user answer capture questions inline, or should the plugin create a pending card for later review?
4. Should session-log drafting be a command, a cron summary, or a manual workflow?
5. Which event fields are safe enough for a public research pipeline?
