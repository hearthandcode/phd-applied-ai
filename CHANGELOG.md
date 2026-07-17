# Changelog

All significant changes to this curriculum are documented here.
Entries are dated and organized most-recent-first.
Format adapted from [Keep a Changelog](https://keepachangelog.com).

---

## 2026-07-17 — Governed Knowledge-Work Redesign Proposal

### Added
- `docs/redesign-2026-07/2026-07-17_research-program-direction-changelog.md` — a forward-looking proposal that reframes the program around governed AI-augmented knowledge work, provenance, review, recovery, and a cognitive workbench. It records explicit non-actions for thesis text, raw records, modules, and runtime configuration.
- `docs/redesign-2026-07/2026-07-17_curriculum-architecture-v2-83-modules.md` — a source-grounded candidate architecture preserving M01-M67 and proposing M68-M83. It sets seven flexible study windows, distinct tracks, cross-cutting lenses, and a module-generation gate.
- `docs/redesign-2026-07/2026-07-17_session-record-continuity-proposal.md` — a review-gated session-record method proposal that separates observable events, subject report, draft records, and derived analysis.
- `docs/redesign-2026-07/2026-07-17_agent-assisted-capture-contract.md` — an implementation-neutral pending-capture contract with explicit prohibition of inferred self-report, automatic public writes, automatic verification, and default memory injection.

### Notes
- These are proposals. They do not revise `THESIS.md`, `METHODOLOGY.md`, existing modules, session records, scorecards, audit rows, or runtime configuration.
- The curriculum count is a candidate architecture, not authorization to generate modules or treat its sequence windows as a valid prerequisite schedule. The existing Phase 4 prerequisite cycle remains a separate repair task.

---

## 2026-06-15 — Research Question Refinement (v3, finalized)

### Changed
- `THESIS.md` — research questions revised from Version C (5 broad academic questions
  spanning competency modeling, pedagogy comparison, virtue/vice frameworks, governance/ethics,
  and autoethnography) to Version B (5 tightly scoped questions anchored to the central
  hypothesis and answerable by one researcher studying their own learning trajectory).
  Version C questions requiring platform deployment data and IRB processes are documented
  as future research directions in THESIS.md §Research questions.
- `CLAUDE.md` — thesis research questions section updated to match THESIS.md v3
- `.claude/commands/rq-checkpoint.md` — RQ list updated (was Version A, oldest framing)
- `tools/hermes/profile/user-context-template.md` (hub) — RQ list updated to v3

### Rationale
Three generations of RQ framing existed across the repo (Version A in rq-checkpoint.md,
Version B in user-context.md, Version C in THESIS.md). The virtue/vice personality
calibration framework — the most novel contribution in Version C — is retained as the
theoretical mechanism underlying RQ2, not a standalone question. Governance/ethics at
scale is deferred: it requires a live platform, user data, and IRB review outside the
scope of this self-directed study.

### RQ numbering history (for session log interpretation)
Session log RQ tags from before 2026-06-15 use prior numbering schemes. Treat as
historical record. Do not retag existing entries.

---

## 2026-06-14 — M01 Content, Learner-Centered Design Rules, Session Log Restructure, New Skills

### Added
- `modules/M01-linear-algebra/foundations.md` — ground-floor primer created: axiom-by-axiom
  field and vector space tables (with "what breaks without it" column), triple description format
  (formal + geometric + operational) for all four fundamental subspaces, symbol reference card
  (28 symbols), 7 Python/NumPy micro-exercises, memory tiers (CARRY / RECONSTRUCT / LOOK UP),
  3 "explain it out loud" prompts, pre-reading map, cross-modal quad applied to every concept.
- `modules/M01-linear-algebra/theory.md` — 8 concrete worked examples added (one per major
  section): rank-nullity projection layer, attention dot products, overdetermined least squares,
  eigenvalue characteristic polynomial, PCA variance retention, SVD rank-1 approximation,
  Eckart-Young compression, near-singular condition number. Pattern: intuition → formal →
  worked example with specific numbers → ML significance.
- `.claude/commands/learn.md` — interactive learning session skill: presents concept, assigns
  micro-exercise, responds to answer, tracks engagement signals, advances checkpoints.
- `.claude/commands/learning-log.md` — learning interaction record skill: logs pedagogical
  data (questions asked, exercises, competency self-assessment) to `modules/MXX-*/interactions/`.
- `.claude/commands/study-idea.md` — mid-session idea capture: appends to `ideas/[domain].md`
  and returns immediately without breaking session flow.
- `ideas/` directory — four-domain ideas ledger (research, curriculum, platform, connections)
  with 5 entries from 2026-06-14 session.
- `docs/pedagogical-foundations.md` — research citations document: Cognitive Load Theory,
  Dual-Coding, Multimedia Learning, Desirable Difficulties, UDL, ADHD executive function
  literature supporting the learner-centered design rules.
- `docs/commands.md` — command reference: all 21 commands with descriptions, triggers,
  and when-to-use guidance.

### Changed
- `docs/generate-module.md`, `docs/generate-phase.md`, `docs/manual-workflow.md` — added
  CONCRETE WORKED EXAMPLE RULE: every abstract formal statement must be followed by a
  concrete numerical worked example with specific numbers. ALL EXERCISES MUST BE
  COMPUTATIONAL (Python/NumPy, no paper derivation). Added all 6 learner-centered design
  rules (PRE-READING MAP, MEMORY TIERS, CHECKPOINTS, MICRO-EXERCISES, EXPLAIN IT OUT LOUD,
  CROSS-MODAL QUAD).
- `docs/session-log-process.md` — restructured: added data routing table (what goes where),
  enforced 10-line maximum for passive capture entries, removed "clinical note" and "design
  implication" as entry sub-sections (fold into body or route to correct file).
- `sessions/2026/06/2026-06-14.md` — distilled to new format: verbose clinical entries
  trimmed to 10-line maximum, Pedagogical Principles and Design Correlation sections removed
  from session log (content routed to `docs/pedagogical-foundations.md` and hub respectively).
- `CLAUDE.md` — added "Suggest commands proactively" convention to session behavior rules.

---

## 2026-06-14 — Central Hypothesis Derived; THESIS.md Restructured

### Added
- `THESIS.md` — **Central hypothesis** section (new, above Abstract): augmented intelligence
  as bidirectional cognitive extension enabling previously inaccessible doctoral outcomes for
  neurodiverse learners. Derived through Socratic introspective dialogue on 2026-06-14.
  Grounded in Extended Mind Thesis (Clark & Chalmers, 1998).
- `THESIS.md` — **Key concepts and terms** section populated with four foundational
  definitions: augmented intelligence, conception-to-execution interface, task-initiation
  difficulty, neurodiverse learner profile. All derived from RQ5 research subject's lived
  experience and Socratic hypothesis derivation session.
- `sessions/2026/06/2026-06-14.md` — rolling entries capturing: researcher outreach
  victory (David Wiley email sent), legitimacy anxiety reflection, personal narrative
  (K-12 success → institutional collapse → late diagnosis → AI-mediated recovery),
  Extended Mind Thesis connection, working hypothesis formation, finalized hypothesis.

### Changed
- `THESIS.md` — Thesis contribution #3 revised to reflect the central hypothesis directly:
  augmented intelligence enables outcomes institutional structures failed to produce,
  specifically through resolving the task-initiation and conception-to-execution interface.
- `THESIS.md` — Abstract placeholder updated to note it should open by restating the
  central hypothesis.
- `THESIS.md` — Title flagged for review post-M63 to ensure alignment with hypothesis.
- `THESIS.md` — frontmatter updated: `updated: 2026-06-14`, added `augmented-intelligence`
  tag.

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
