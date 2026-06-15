Capture an idea, insight, or tangent thought that surfaced during a study session. Appends immediately to the appropriate domain log and returns — designed to be called mid-session without breaking flow.

Input: $ARGUMENTS
Format: "[domain] [brief title] — [the idea]"
  domain: research | curriculum | platform | connections
  Example: "research hypothesis refinement — the self-fulfilling curriculum loop problem"
  Example: "platform help system — 'read more' is never the right first response"
  Example: "connections M01 fields and M45 BKT — both are about guaranteeing invariants under operations"

If domain is omitted, ask once. If the idea is very brief, expand it into 2–4 sentences before writing.

---

Instructions:

1. Parse domain (first word if it matches one of the four domains; otherwise ask).
2. Parse title and idea text from the remainder of $ARGUMENTS.
3. Determine source: ask "What module or topic prompted this?" if not obvious from context. One word answer is fine — you can infer. Skip if the source is clear from the session context.
4. Write an entry to `ideas/[domain].md` using this format:

```
### [YYYY-MM-DD ~HH:MM] [Title]

**Domain:** [domain]
**Source:** [module, topic, or "side conversation"]
**Trigger:** [what prompted it — one sentence]

[The idea — 2–6 sentences. Specific enough to be useful when read 6 months from now without context.]

**Follow-up needed:** yes / no
**Related:** [other modules, ideas, or decisions — or "none" if none obvious]

---
```

5. Confirm with one line: "Logged to ideas/[domain].md — back to [current topic]."
   Do NOT produce a summary, ask follow-up questions, or elaborate. Return to the session immediately.

---

For non-Claude-Code use: paste the relevant ideas/[domain].md content and append your entry manually using the format above.
