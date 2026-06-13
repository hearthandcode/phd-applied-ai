# Changelog

All significant changes to this curriculum are documented here.
Entries are dated and organized most-recent-first.
Format adapted from [Keep a Changelog](https://keepachangelog.com).

---

## 2026-06-13 — Fork-Friendliness, Tooling, Session Infrastructure

**Commits:** 53b37ce, c1e6000, 91012dd, 3f49ec5

### Added
- `FORK_GUIDE.md` — 10-step guide for adapting the curriculum to a different research focus
- `CHANGELOG.md` — this file
- 17 curriculum skill commands in `.claude/commands/`:
  `study-session`, `committee-session`, `committee-debrief`, `oral-exam`, `module-review`,
  `generate-module`, `generate-phase`, `blog-draft`, `post-draft`, `audit-entry`,
  `scorecard-update`, `week-review`, `rq-check`, `archive-search`, `phd-status`
- `AGENT.md` — tool-agnostic ecosystem context for any AI assistant (non-Claude-Code)
- `docs/manual-workflow.md` — copy-paste generation prompts for any AI model
- `docs/session-log-process.md` — documented process for collaborative session logging and verification
- `sessions/` directory with date-based session log structure (`sessions/YYYY/MM/YYYY-MM-DD.md`)
- `sessions/README.md` — session log format specification and YAML frontmatter schema
- `sessions/EXAMPLE-session-template.md` — annotated example session log (not a real session)
- `sessions/reviews/EXAMPLE-weekly-review.md` — weekly review template
- `sessions/2026/06/2026-06-13.md` — first real session log (meta-reflection, launch day)

### Changed
- `README.md` — expanded Fork section (references FORK_GUIDE.md); added Transparency,
  Processes, and License sections; updated progress table (Phase A complete)
- `docs/spec.md` — locked at v2.1; corrected module count (63→67) and range (M01–M66→M01–M67)
- `AUDIT_LOG.md` — redesigned schema v2.0: lightweight index table only; full session
  narratives now live in `sessions/`
- `LICENSE` — plain-language CLA summary added to CONTRIBUTING section
- `.claude/commands/generate-module.md` — CONTENT SEPARATION RULE added; `project/hc-connection.md`
  now a required generation output; theory.md must be generic
- `.claude/commands/generate-phase.md` — same content separation rule applied
- `docs/manual-workflow.md` — generation prompt updated to produce separate
  `project/hc-connection.md` alongside generic theory and project files

### Notes
- Git tag `v2.1-spec-locked` applied to `docs/spec.md`
- Option B fork-friendliness: H&C-specific content isolated to `project/hc-connection.md` per module

---

## 2026-06-13 — Phase A Complete (Scaffold Generation)

**Commit:** 277b1a0

### Added
- 67 module scaffold directories (M01–M67), each containing:
  - `theory.md` — YAML front matter: calibration target, tags, archive coverage, par hours, prerequisites
  - `rubric.md` — 4-level competency scale (1: exposure → 4: mastery)
  - `project/README.md` — project deliverable template
  - `reading-list.md` — seed sources (1–3 items)
  - `resources.md` — supplementary links template
  - `audit.md` — session log index for this module
  - `blog-post-seed.md` — Substack post outline template
- `SCORECARD.md` — par vs. actual hours tracker for all 67 modules, all phases
- `committee/` — five advisory personas:
  - `dr-chen.md` — ML Theory (Stanford), high Conscientiousness
  - `dr-kowalski.md` — Systems/Architecture (CMU), high Conscientiousness + low Agreeableness
  - `dr-williams.md` — Education/Pedagogy (MIT Media Lab), high Agreeableness + Openness
  - `dr-okonkwo.md` — AI Ethics (Oxford), high Openness + Conscientiousness
  - `dr-patel.md` — Applied AI (Industry), high Extraversion + low Neuroticism
  - Each advisor has `PERSONA.md` (complete AI system prompt) and `profile.md` (academic bio)
- `THESIS.md` — thesis title, 5 research questions, methodology sketch, abstract
- `curriculum/overview.md` — full module registry: phase, title, par hours, prerequisites, archive coverage
- `PERSONA.md` — learner profile template (populated at M61 after self-assessment data)
- `POSTS.md` — published Substack post index (empty at generation)
- `exams/`, `defense/`, `portfolio/`, `bibliography/` — structural scaffolds
- `architecture/workflows/phd-phase-a.js` — Claude Code Workflow script (in hearthandcode-hub)

---

## 2026-06-13 — License

**Commit:** 991e41e

### Added
- `LICENSE` — CC BY-NC-SA 4.0; commercial rights reserved to copyright holder;
  CLA clause for contributors; contact for commercial licensing

---

## 2026-06-12 — Repository Initialized

**Commit:** d91599d

### Added
- `README.md` — project overview, committee table, curriculum phase map
- `CLAUDE.md` — Claude Code session context and hub-first workflow notes
- `docs/spec.md` — master curriculum spec (draft, pre-lock)
- `docs/frontmatter-schema.md` — YAML front matter field definitions for theory.md files
- `docs/archive-ingestion-prompt.md` — prompt for seeding reading lists from archive

---

## Planned

### Next (Phase B)
- Generate doctoral-level theory content for M01–M18 (Math + CS Fundamentals)
- Create `project/hc-connection.md` for each module (H&C-specific applications)
- Update `curriculum/overview.md` status fields
- Log generation event in `AUDIT_LOG.md`

### Ongoing
- Session logs committed after each study session
- `SCORECARD.md` updated as modules are studied
- `AUDIT_LOG.md` index updated with session summaries
- `POSTS.md` updated as Substack posts publish
