Show current curriculum progress across all phases and modules. Reads SCORECARD.md and all audit.md files.

Arguments (optional): $ARGUMENTS
(Format: "phase-0" to show one phase only, "summary" for one-line totals only, or empty for full report)

Instructions:
1. Read SCORECARD.md for par hours and any filled-in actual hours.
2. For each module with actual_hours > 0, also read its audit.md for session count and competency level.
3. Generate a status report:

**Overall progress:**
- Total par hours: 3,265
- Total actual hours logged: [sum from SCORECARD]
- Modules started: [count with actual > 0]
- Modules completed (competency ≥ 3): [count]
- Active modules (started, not completed): [list]

**By phase:**
For each of the 6 phases, show:
- Phase name + total par hours
- Modules: ✓ complete (competency ≥3) | ◐ in progress | ○ not started
- Hours: [actual] / [par]

**Next recommended action:**
- If any module is in progress: "Continue [module] — [X] hours logged, [Y] par remaining"
- If no module is in progress: "Run /next-module to get a starting recommendation"
- If Phase B not yet generated: "Phase B content not generated — run /generate-module M01 or Workflow script"

If argument is "summary": show only the overall progress line and the next action, nothing else.
If argument is "phase-N": show only that phase's modules in detail.
