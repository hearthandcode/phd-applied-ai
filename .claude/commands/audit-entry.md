Log a study session to a module's audit.md file.

Input: $ARGUMENTS
(Format: "M07 2.5 1" = module M07, 2.5 hours, competency level 1
 Or: "M07 2.5" = module M07, 2.5 hours, competency unchanged
 Or: "M07" = prompt me for details)

Instructions:
1. Parse module ID, hours studied, and competency level from $ARGUMENTS.
2. If any field is missing, ask for it (one question per missing field).
3. Read modules/$ARGUMENTS-*/audit.md to see the current format and last entry.
4. Construct a new audit entry in the file's existing format:
   - date: today's date
   - session_hours: [hours]
   - cumulative_hours: [sum of all previous hours + this session]
   - competency_level: [0–4 or "unchanged"]
   - session_notes: [ask: "One sentence — what was the most important thing from this session?"]
   - energy_level: [ask: "Energy level: high / medium / low"]
5. Write the entry to modules/MXX-*/audit.md.
6. Update SCORECARD.md: set actual_hours for this module to the new cumulative total.
7. Confirm: "Logged [X] hours for M[XX]. Cumulative: [Y] hours. Par: [Z] hours."
8. If cumulative hours ≥ 80% of par, say: "You're close to par. Consider /module-review to assess completion."

This skill can also log committee sessions and oral exams — just note in session_notes.
