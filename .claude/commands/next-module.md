Recommend the best next module to study based on prerequisites, archive coverage, and current momentum.

Arguments (optional): $ARGUMENTS
(Format: "energy:high" / "energy:low" / "time:25min" / "interests:safety" — or leave empty)

Instructions:
1. Read SCORECARD.md to see which modules have been started and which are at 0 hours.
2. Read curriculum/prerequisites.md to understand the dependency graph.
3. Read all audit.md files for modules with actual_hours > 0 to understand momentum.
4. Parse any arguments: energy level, available time, interest area.

**Selection criteria (in order):**
1. Prerequisites must be met or waived (Phase 0 and 1 have no hard prerequisites among themselves)
2. If any module is in progress (actual_hours > 0, competency < 3), recommend continuing it first
3. Among not-started modules: prefer high archive_coverage (content exists to read)
4. If energy is "low": prefer modules with par ≤ 35 hours (shorter to complete)
5. If energy is "high": prefer foundational modules that unlock many others
6. If time is "25min": recommend a specific section within a module, not a new one

**Output:**
- Primary recommendation: one module with a brief reason
- Why now: what this module unlocks (which later modules depend on it)
- First step: the exact thing to do to start this session (not "open the file" — be specific, e.g. "Read the definitions section of theory.md and write down the 3 core concepts in your own words")
- Alternative: one other module if the primary doesn't feel right

**Starting modules (no prerequisites):**
M01, M02, M03, M04, M05, M06 (Phase 0 — any order)
M07, M08, M09, M10 (Phase 1 — any order, M07 recommended first for conceptual depth)
