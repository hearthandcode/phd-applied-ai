---
type: ideas-index
---

# Ideas Log

A domain-based ledger for thoughts, connections, and insights that surface during study
sessions but belong in a different context than the session log or learning interaction record.

Use `/study-idea [domain] [brief]` during or after a session to append an entry here without
breaking your flow. All entries timestamped. Review periodically to find recurring themes.

---

## Files in this directory

| File | What goes here |
|---|---|
| `research.md` | Hypothesis refinements, RQ connections, methodology insights, empirical hunches |
| `curriculum.md` | Curriculum design observations, what to add/change, pedagogical patterns noticed while studying |
| `platform.md` | Platform design principles and learner-experience insights (no architecture specifics — see H&C hub for that) |
| `connections.md` | Unexpected cross-domain links: concept in M01 that connects to M45, analogy that bridges two fields, etc. |

---

## Format (per entry)

```
### [YYYY-MM-DD ~HH:MM] [Brief title]

**Domain:** research | curriculum | platform | connections
**Source:** [module or topic that prompted this — e.g. "M01 Fields section"]
**Trigger:** [what prompted the idea — side-conversation, exercise, analogy, etc.]

[The idea, observation, or connection — 2–10 sentences. Be specific enough to be useful later.]

**Follow-up needed:** yes / no
**Related:** [other ideas, modules, or decisions this connects to]

---
```

---

## Usage guidance

- Capture ideas immediately — during a session, between checkpoints, after an exercise
- Don't filter for quality — half-formed ideas captured are more useful than perfect ideas forgotten
- Review at weekly retrospectives (`/weekly-report`) to find recurring themes worth pursuing
- High-frequency ideas in `research.md` may warrant a new RQ or hypothesis refinement
- High-frequency ideas in `curriculum.md` may warrant a generation spec update
- High-frequency ideas in `platform.md` flow to `hearthandcode-hub/architecture/specs/OPEN_QUESTIONS.md`
