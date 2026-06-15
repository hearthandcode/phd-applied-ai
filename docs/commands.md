# Commands Reference — phd-applied-ai

All slash commands available in Claude Code sessions started from this repo.
Invoke with `/command-name [arguments]` in the chat prompt.

> Tip: type `/` in the Claude Code prompt to see all available commands with descriptions.

---

## When to use what — trigger guide

| Situation | Suggested command |
|---|---|
| Starting to study a module | `/learn M01` or `/study-session` |
| At end of a learning session | `/learning-log M01` then `/audit-entry M01` |
| A side thought surfaces mid-session | `/study-idea [domain] [title] — [idea]` |
| Want to check understanding on theory content | `/theory-qa M01` |
| Want to be challenged with questions | `/oral-exam M01` |
| Need a committee member's perspective | `/committee-session dr-chen [topic]` |
| After a committee discussion | `/committee-debrief` |
| Checking thesis alignment | `/thesis-checkpoint` or `/rq-checkpoint RQ5` |
| Generating a new module | `/generate-module M02` |
| Generating a full phase | `/generate-phase 0` |
| Generating one theory section at a time | `/generate-theory-chunked M01 fields` |
| Finding the next module to tackle | `/next-module` |
| Checking phase progress | `/phase-status 0` |
| Drafting a Substack post from module content | `/blog-draft M01` |
| Drafting a social post | `/social-post "key insight"` |
| End-of-week review | `/weekly-report` |
| Module reading list management | `/reading-list M01` |

---

## Command directory

### Learning and study

**`/learn [MODULE] [energy:level] [checkpoint:N]`**
Interactive teaching session using foundations.md. Presents concept, assigns micro-exercise, responds to answer, tracks engagement per checkpoint. Use instead of reading foundations.md passively.
- `energy:low` — shorter explanations, more exercises, more frequent stops
- `energy:high` — deeper coverage, edge cases, connects to theory.md
- `checkpoint:N` — resume from a specific checkpoint

**`/study-session`**
Structured study session initiation (Socratic dialogue mode). Best when you want to explore ideas or review material you've already read. Contrast with `/learn` which teaches actively.

**`/theory-qa [MODULE]`**
Q&A mode on theory.md content. Ask questions; the assistant grounds answers in the theory file. Good for targeted questions without starting a full teaching session.

**`/oral-exam [MODULE]`**
Simulated oral exam on a module. Asks progressively harder questions; evaluates responses against the rubric. Use to test your own understanding before marking a module complete.

**`/module-review [MODULE]`**
Structured review of a completed module: gaps, connections to other modules, preparation for the committee.

---

### Logging and data capture

**`/learning-log [MODULE]`**
Records a learning interaction: what sections were covered, engagement per concept (click/partial/confused/skipped), exercises attempted, questions asked, self-assessed competency. Writes to `modules/MXX-*/interactions/YYYY-MM-DD.md`. Run after every `/learn` session.

**`/study-idea [domain] [title] — [idea]`**
Mid-session idea capture. Appends to `ideas/[domain].md` and returns immediately. Does not break session flow. Domain: `research`, `curriculum`, `platform`, or `connections`.
- Example: `/study-idea curriculum visual encoding — every concept needs a spatial metaphor before the formula`

**`/audit-entry [MODULE]`**
Logs hours studied and updates `SCORECARD.md`. Run at the end of any study block.

---

### Curriculum generation

**`/generate-module [MODULE_ID]`**
Full module generation: theory.md, rubric.md, reading-list.md, blog-post-seed.md, audit.md stub. Follows all generation spec rules (concrete examples, computational exercises, learner-centered design rules).

**`/generate-phase [PHASE_NUMBER]`**
Generates all modules for a phase in sequence. High context usage — monitor quality per module.

**`/generate-theory-chunked [MODULE] [SECTION]`**
Generates one section of theory.md at a time. Use when full-module generation produces degraded quality. Preferred for M01+ since full-length theory.md generation is long.

**`/next-module`**
Identifies the next module to study based on SCORECARD.md and prerequisite map. Accounts for concurrent phase structure (Phase 0 runs parallel to Phase 1).

**`/phase-status [PHASE_NUMBER]`**
Status of all modules in a phase: generated, in-progress, complete, blocked.

**`/reading-list [MODULE]`**
Manage reading list for a module: add/remove sources, check access tier (Free & Open Access / Library Accessible / Reference Only), confirm all required reading is freely available.

---

### Committee

**`/committee-session [MEMBER_ID] [TOPIC]`**
Invoke a committee member as an advisor. Member IDs: `dr-chen`, `dr-kowalski`, `dr-williams`, `dr-okonkwo`, `dr-patel`. Topic can be a module, an RQ, or an architectural question.

**`/committee-debrief`**
Structured debrief after a committee session: what was challenged, what held up, what to revise.

**`/oral-exam [MODULE]`**
Committee-style oral examination on a completed module. Mapped to dr-chen by default; specify a member for their angle. Records in `modules/MXX-*/audit.md`.

---

### Thesis and research

**`/thesis-checkpoint`**
Full thesis status: hypothesis statement, RQ alignment, methodology, completion estimate, what's still undefined. Good for beginning-of-sprint orientation.

**`/rq-checkpoint [RQ_NUMBER]`**
Focus on one research question: evidence collected so far, open gaps, next steps. Run after a study block that touched an RQ.

---

### Publishing and portfolio

**`/blog-draft [MODULE]`**
Draft a Substack post from module content. Uses the module's `blog-post-seed.md` as the scaffold. Scott writes the final post; this generates the structure and key points.

**`/social-post [TOPIC]`**
Draft a social post (LinkedIn, Bluesky, Mastodon) from a topic or key insight. Calibrated to Scott's voice via `profile/voice-guide.md` in the hub.

**`/weekly-report`**
End-of-week progress report: hours logged, modules advanced, key insights, next-week plan. References SCORECARD.md and recent audit entries.

---

## For forkers

If you have forked this repo for your own self-directed curriculum:
- Update `curriculum/learner-profile-schema.json` — commands use it to calibrate energy and formalism density
- Update `PERSONA.md` (generated during M61) — committee members adapt their tone to your profile
- The `ideas/` directory and `sessions/` directory are yours; the format is documented in `docs/session-log-process.md`
- All commands work with relative paths from the repo root; no hub or ecosystem dependency
