Append an entry to the research journal. Captures intellectual narrative — chains of reasoning, breakthroughs, struggles, open questions, and how ideas connect. Not for discrete ideas (use /study-idea) or behavioral observations (use session log). This is the story of how the thinking evolved.

Input: $ARGUMENTS (free text — the journal entry, or empty to be prompted)

PHD_ROOT: /home/cosmatrexis/devel/hearthandcode/open-source/phd-applied-ai

---

1. If $ARGUMENTS is empty: ask "What do you want to capture? Speak freely — I'll shape it into a journal entry."
2. If $ARGUMENTS has content: use it as the raw source material.
3. Determine a short title (5–8 words) summarizing the chain of thought.
4. Write the entry to `$PHD_ROOT/docs/research-journal.md` using this format:

```markdown
### [YYYY-MM-DD ~HH:MM] [Title]

[Narrative — first-person, free-form, no length limit. Include:
- What prompted the thinking
- How one idea led to the next
- What the breakthrough or sticking point was
- What it connects to or changes
- What remains open]

**Open questions:** (if any)
**Cross-refs:** [loose references to sessions/, ideas/, modules/, decisions.md, THESIS.md]

---
```

5. After writing, ask: "Want to route any of this to ideas/research.md or ideas/platform.md?"
6. Confirm: "Logged to docs/research-journal.md — [title]."
