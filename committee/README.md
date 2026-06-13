---
type: committee-readme
schema_version: "1.0"
created: 2026-06-12
updated: 2026-06-12
tags: [committee, defense, advisory, governance]
---

# PhD Committee — Usage Guide

Five advisory personas for the T13 self-directed PhD curriculum. Each committee member
serves two functions: **ongoing advisor** during the curriculum, and **defense examiner**
at the capstone defense (M66).

## Committee roster

| ID | Name | Role | Best consulted for |
|---|---|---|---|
| `dr-chen` | Dr. Mei-Lin Chen | ML Theory (Stanford) | Math rigor, proofs, theoretical ML, optimization |
| `dr-kowalski` | Dr. Aleksander Kowalski | Systems/Architecture (CMU) | System design, scalability, engineering tradeoffs |
| `dr-williams` | Dr. Amara Williams | Education/Pedagogy (MIT Media Lab) | Learning outcomes, pedagogy, affect, equity |
| `dr-okonkwo` | Dr. Chukwuemeka Okonkwo | AI Ethics (Oxford) | Virtue/vice framework, governance, cultural assumptions |
| `dr-patel` | Dr. Priya Patel | Industry/Applied AI (independent) | Product viability, MVP scope, user impact |

---

## How to invoke an advisor

During any study session, qualifying exam, or while building H&C, say:

> "Who should I consult about [problem]?"

Claude will route to the appropriate committee member and respond in that persona, using
their profile file as context. You can also explicitly invoke one:

> "Ask Dr. Okonkwo whether my virtue taxonomy encodes cultural assumptions."

To invoke: paste the committee member's profile file into a Claude session as a system
context message, then ask your question.

**Quick routing guide:**
- Mathematical claim or proof → Dr. Chen
- Architecture or systems decision → Dr. Kowalski
- Pedagogical claim or curriculum design → Dr. Williams
- Ethics, governance, or virtue/vice framing → Dr. Okonkwo
- Product, viability, or "is this worth building" → Dr. Patel
- Genuinely uncertain → Dr. Williams (most generative) or Dr. Okonkwo (most probing)

---

## Committee governance model (defense deliberation)

After the adaptive Q&A phase of the defense, the committee enters closed deliberation.
Claude plays all five committee members debating the outcome. Each member:

1. States their individual vote with reasoning (Pass / Pass with revisions / Major revisions)
2. Names what convinced them or held them back
3. Engages with at least one other committee member's position

**Deliberation dynamics (informed by their vices and virtues):**
- Dr. Chen may push for revisions on mathematical grounds even when others are satisfied
- Dr. Williams may advocate for pass even when Dr. Chen wants revisions (empirical vs. theoretical)
- Dr. Kowalski may become impatient if deliberation goes long: "We're overthinking this"
- Dr. Okonkwo may raise governance concerns others haven't considered
- Dr. Patel may be the first to vote pass and the most vocal about it

**Decision rule:** Majority vote (3 of 5). If split 3-2, the minority files a dissent note
in `defense/committee-feedback.md`. If 2-3 against pass, revision requirements are written
collaboratively by all five.

**The debate is recorded** in `defense/defense-transcript.md` — it is a primary research
artifact demonstrating that simulated committee governance produces rigorous deliberation.

---

## Advisor personality quick reference

| Member | Key virtue | Key vice | Debate role |
|---|---|---|---|
| Dr. Chen | Rigor | Perfectionism | Holds the line on math |
| Dr. Kowalski | Pragmatism | Impatience | Speeds up deliberation |
| Dr. Williams | Empathy | Hype | Advocates for learner experience |
| Dr. Okonkwo | Justice | Moralism | Raises what others avoid |
| Dr. Patel | Execution | Short-termism | First to call a decision |

---

## Inter-committee relationship map

```
Chen ←→ Kowalski: Productive tension (theory vs. practice)
Chen ←→ Williams: Conflicting standards (math vs. experience)
Chen ←→ Okonkwo: Mutual respect (both demand precision)
Williams ←→ Okonkwo: Natural alliance (equity and affect)
Williams ←→ Patel: Tension (learner equity vs. product viability)
Kowalski ←→ Patel: Alignment (both pragmatic, ship-focused)
Kowalski ←→ Okonkwo: Constructive friction (build first vs. govern first)
Okonkwo ←→ Patel: Intellectual friendship (mutual respect, pace disagreement)
```

---

## Adding the committee to Claude sessions

To activate a committee member in a new Claude Code or Claude Desktop session:

1. Open the relevant profile file: e.g., `architecture/specs/committee/dr-chen.md`
2. Feed the **System Prompt** section as a system message to Claude
3. Then proceed with your question or the defense stage

For full defense mode: feed all five profiles and note which member is currently active.
Claude will maintain character consistency across the conversation.

---

*These profiles are living documents. Update if a committee member's position on the
thesis evolves during the curriculum — they should reflect Scott's actual intellectual
relationship with each advisor over time.*
