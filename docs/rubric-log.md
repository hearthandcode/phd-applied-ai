# Hermes Evaluation Rubric Log

Session-level scoring data for the Hermes vs. Claude Code transition study.
Rubric spec: `hearthandcode-hub/architecture/specs/hermes-evaluation-rubric.md`

Score 1–5 per dimension. N/A if the dimension doesn't apply to this session.
Score immediately after the session — don't wait, don't average.

---

## Dimension reference (quick lookup)

| # | Dimension | When scored |
|---|---|---|
| 1 | Session Initiation Friction | Every session |
| 2 | Context Continuity | Every session |
| 3 | PhD Tutoring Depth | PhD sessions |
| 4 | Voice Fidelity | Content tasks |
| 5 | Workflow Orchestration Accuracy | Hub management |
| 6 | ADHD-Adaptive Behavior | Every session |
| 7 | Ambient Output Quality | Weekly review (Hermes only) |
| 8 | Curriculum Adaptation Quality | Amendment review (Phase 2.5+) |
| 9 | Research Integrity Enforcement | Every session |
| 10 | User Model Depth | Monthly |
| 11 | Cost Efficiency | Monthly |
| 12 | Tool & Integration Reliability | Weekly |

---

## Score entries

### 2026-06-15 — Hub/Architecture/Content — Claude Code (Baseline 1)

**Session focus:** Hub management, Hermes migration spec, evaluation rubric, social publishing (T21, T20)
**Energy level:** [fill in]

| Dim | Name | Score | Notes |
|---|---|---|---|
| 1 | Session Initiation Friction | 3/5 | Continuation from previous compacted session — cold-start from summary, had to re-establish context mid-task |
| 2 | Context Continuity | 4/5 | Excellent within-session; summary was accurate; minor friction re-fetching docs already gathered in prior session |
| 3 | PhD Tutoring Depth | N/A | No module study today |
| 4 | Voice Fidelity | 4/5 | SOUL.md and user-context template written in-voice; skills reflect voice conventions; slight hedging in places |
| 5 | Workflow Orchestration Accuracy | 4/5 | T21+T22 created, kanban+KANBAN+threads all updated, next-ID counter incremented; no observed divergences |
| 6 | ADHD-Adaptive Behavior | 4/5 | Held T21 focus through multiple product pivots; queued questions and resolved after; minor: could have named the park earlier |
| 7 | Ambient Output Quality | N/A | Claude Code has no ambient mode |
| 8 | Curriculum Adaptation Quality | N/A | Phase 0 |
| 9 | Research Integrity Enforcement | 5/5 | Rubric-log created with boundary caveats; all skills enforce research data boundary in their steps; no violations |
| 10 | User Model Depth | 4/5 | ADHD conventions, dual-state, voice correctly applied throughout; small gaps in predicting product idea scope |
| 11 | Cost Efficiency | N/A | Score monthly |
| 12 | Tool Reliability | 5/5 | 20+ Write operations, WebFetch, TaskCreate/Update — all clean, no phantom calls |

**Composite (scored dims: 1,2,4,5,6,9,10,12):** 4.1 / 5
**Flags:** None
**Notes:** First baseline entry. Session was a continuation from compacted context — the 3 on Dim 1 reflects that specific pattern (summary cold-start), not typical performance. Hermes with persistent memory (Honcho) should score higher on Dim 1 once the user model builds. Strong baseline: 4.1/5 is the target for Hermes to meet or exceed.

---

## Monthly aggregates

*(Start recording when Phase 1 is live — two tools running in parallel)*

---

## How to score quickly (3-minute post-session habit)

1. Open this file immediately after closing the session
2. Copy the session template above, fill in the date and tool
3. Score each applicable dimension in one word or phrase — don't overthink
4. Composite = average of scored dims (exclude N/A)
5. Flag any 1 immediately — don't leave it in the table without a note
6. Save

Honest, fast scoring beats perfect delayed scoring every time.
