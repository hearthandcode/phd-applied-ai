Generate a weekly progress report. Reads audit logs and SCORECARD.md to summarize actual progress, energy patterns, and next week's priorities.

Week ending: $ARGUMENTS
(Format: "2026-06-20" or leave empty for current week)

Instructions:
1. Read SCORECARD.md for overall hours and status.
2. Read audit.md for every module that has entries dated within the past 7 days.
3. Read AUDIT_LOG.md for any generation or publication events this week.
4. Read POSTS.md for any posts published this week.

**Generate a report with these sections:**

## Week ending [date]

**Hours logged this week:** [sum of session_hours from this week's audit entries]
**Modules touched:** [list]
**Competency advances:** [any module where competency level increased]
**Posts published:** [from POSTS.md]

**Energy pattern:**
- High-energy sessions: [count]
- Medium-energy sessions: [count]
- Low-energy sessions: [count]
- Days with no activity: [count]
[1–2 sentence observation about the pattern — no judgment, just what it shows]

**What happened this week:**
[3–5 bullet points summarizing actual work done, in plain language]

**What didn't happen (and why it's fine):**
[1–2 things planned that didn't happen, with a one-line reason — normalize incomplete weeks]

**Next week's one priority:**
[Single most important thing to do next week — not a list]

**Suggested MVP for Monday:**
[The smallest action that counts as showing up on Monday — completable in 10 minutes]

5. Offer to copy this report to a file: ops/schedule/week-[date].md in the hub.
6. Offer to post it as a Substack Note (edited for public audience).
