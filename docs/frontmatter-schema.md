---
type: schema-reference
schema_version: "1.0"
created: 2026-06-12
updated: 2026-06-12
tags: [schema, frontmatter, data, anonymization, curriculum]
---

# PhD Curriculum — Front-Matter Schema Reference

All Markdown files in the `phd-applied-ai` public repo use YAML front matter for:
- Machine-readable data collection (research dataset)
- Curriculum navigation and status tracking
- Anonymized learner data (never personal names in data fields)
- Transparency and reproducibility

## Data policy (confirmed 2026-06-12)

**All data is public.** Energy levels, mood, focus quality, effort hours, personal
reflections — published as-is in the repo. This is a deliberate research design choice,
not accidental disclosure.

**Rationale (methodological):** RQ5 asks how a neurodiverse learner's personal
characteristics affect their AI-mediated learning trajectory. That question cannot be
answered with anonymized data — the personal specificity *is* the data. Sanitizing it
would undermine the contribution.

**`learner_id: L001`** is retained as a data science convention (for programmatic queries
and potential future cross-study comparison), not as anonymization. The repo is
attributed to Scott; the learner_id maps to him transparently.

**What is genuinely withheld:**
- Financial details (income, SSDI amounts, service costs) — personal privacy boundary
- Third-party personal information (no identifying details about other people)
- Medical records or treatment details beyond what Scott chooses to disclose in narrative

**The disclosure arc:**
- `audit.md` entries: structured data (energy, focus, hours) — recorded per session
- `blog posts`: narrative reflection — Scott's voice, Scott's choice per post
- `PERSONA.md` (generated from M61): the anchoring first-person disclosure document
  that contextualizes all data for readers of the repo

**Mental health and neurodivergence fields** (`energy_level`, `focus_quality`,
`cognitive_load`, `emotional_state`, `recall_difficulty`) are present as first-class
optional fields — not afterthoughts. Recording them is voluntary per session but
encouraged as primary research data for RQ5. Over 5+ years, even partial recording
produces a rich longitudinal dataset.

**SSDI note (for Scott only):** Blog post income from Medium Partner Program may affect
SSDI SGA thresholds — consult WIPA before enabling monetization. This is a separate
decision from data publication.

---

## Schema: `module-theory`

```yaml
---
type: module-theory
schema_version: "1.0"
module_id: M##
module_title: ""
phase: 0          # 0-5
calibration: ""   # e.g., "Stanford CS229 / MIT 6.867"
archive_coverage: A|B|C|D|F
languages: []     # e.g., [python, typescript]
h_and_c_connection: ""
prerequisites: [] # e.g., [M01, M03]
status: not-started|in-progress|complete
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

---

## Schema: `module-rubric`

```yaml
---
type: module-rubric
schema_version: "1.0"
module_id: M##
module_title: ""
phase: 0
par_hours: 0              # estimated hours at moderate pace
current_competency: 0     # 0-4 (see rubric levels)
target_competency: 3      # 3 for most modules; 4 for thesis-critical modules
last_assessed: null       # YYYY-MM-DD
assessor: self|dr-chen|dr-kowalski|dr-williams|dr-okonkwo|dr-patel
assessment_method: self-assessment|oral-exam|project-review|qualifying-exam
status: not-started|in-progress|passed|needs-revision
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

---

## Schema: `audit-entry` (study session log — anonymized data)

```yaml
---
type: audit-entry
schema_version: "1.0"
learner_id: L001           # anonymized — never use real name in data fields
module_id: M##
session_number: 0          # sequential within module
date: YYYY-MM-DD
duration_minutes: 0
topics_covered: []
resources_used: []         # titles or archive paths, not personal URLs
competency_before: 0       # 0-4, self-assessed at session start
competency_after: 0        # 0-4, self-assessed at session end
par_hours_accumulated: 0   # running total for this module
actual_hours_accumulated: 0

# Learner personal data (optional, voluntary)
energy_level: low|medium|high|null
focus_quality: low|medium|high|null      # ADHD-relevant
interruption_count: null                 # number of significant focus breaks
recall_difficulty: none|some|significant|null
cognitive_load: low|medium|high|null     # Sweller cognitive load
emotional_state: null                    # e.g., frustrated, curious, tired, anxious

# Session outcomes
blockers: []               # specific conceptual blockers
breakthroughs: []          # moments of clarity
connections_made: []       # links to other modules or H&C
questions_raised: []       # open questions to carry forward
next_session_goal: ""

# H&C connection
hc_impact: none|minor|significant        # did this session affect H&C decisions?
hc_note: ""

created: YYYY-MM-DD
tags: []
---
```

---

## Schema: `phase-scorecard`

```yaml
---
type: phase-scorecard
schema_version: "1.0"
learner_id: L001
phase: 0
phase_name: ""
modules_in_phase: []
total_par_hours: 0
total_actual_hours: 0
par_variance: 0             # actual - par (positive = over par)
average_competency: 0.0     # 0-4 scale
modules_passed: 0
modules_in_revision: 0
qualifying_exam_status: not-started|in-progress|passed|failed

# Aggregate personal data (averaged across phase)
average_energy_level: null
average_focus_quality: null

# Narrative (first-person, voluntary)
phase_reflection: ""        # Scott's prose reflection on the phase

completed: YYYY-MM-DD|null
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

---

## Schema: `defense-qa-entry`

```yaml
---
type: defense-qa-entry
schema_version: "1.0"
learner_id: L001
stage: opening|qa|deliberation|decision
committee_member: dr-chen|dr-kowalski|dr-williams|dr-okonkwo|dr-patel|all
question_number: 0
date: YYYY-MM-DD
question_text: ""
response_summary: ""        # brief summary of the response (not full text — see transcript)
response_quality: 0         # 1-5, scored by committee member in character
follow_up_count: 0
committee_member_virtue_displayed: []
committee_member_vice_displayed: []
verdict_tendency: pass|revisions|major-revisions
notes: ""
created: YYYY-MM-DD
tags: []
---
```

---

## Schema: `committee-feedback`

```yaml
---
type: committee-feedback
schema_version: "1.0"
committee_member: dr-chen|dr-kowalski|dr-williams|dr-okonkwo|dr-patel
stage: module-advisory|qualifying-exam|defense-deliberation|defense-decision
target: ""                  # module ID, exam ID, or "thesis"
date: YYYY-MM-DD
vote: pass|revisions|major-revisions|null
vote_confidence: low|medium|high

strengths: []
weaknesses: []
required_revisions: []      # specific, actionable
recommended_resources: []

# Committee member character notes (meta-transparency)
virtue_expressed: []        # which of their virtues shaped this feedback
vice_expressed: []          # which of their vices shaped this feedback
conflict_with: []           # other committee members they disagreed with

created: YYYY-MM-DD
tags: []
---
```

---

## Schema: `qualifying-exam`

```yaml
---
type: qualifying-exam
schema_version: "1.0"
learner_id: L001
phase: 0
exam_id: "phase-0-qualifying"
date: YYYY-MM-DD
modules_covered: []

# Written component
written_questions: []
written_completion_date: null

# Oral component (simulated)
oral_questions: []
oral_completion_date: null

# Capstone project
capstone_project_id: ""
capstone_status: not-started|complete

# Results
overall_result: pass|revisions|fail|null
committee_votes:
  dr-chen: pass|revisions|fail|null
  dr-kowalski: pass|revisions|fail|null
  dr-williams: pass|revisions|fail|null
  dr-okonkwo: pass|revisions|fail|null
  dr-patel: pass|revisions|fail|null
committee_notes: ""

created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

---

## Schema: `blog-seed`

```yaml
---
type: blog-seed
schema_version: "1.0"
module_id: M##
module_title: ""
generated_by: "workflow-phase-X"
generated_date: YYYY-MM-DD

# Suggested titles (Claude-generated, Scott chooses/adapts)
title_options: []

# Content scaffold
hook_options: []
outline: []
hc_lesson_angle: ""
general_reader_angle: ""
pull_quotes: []
suggested_tags: []
cross_links: []

# Publication tracking (filled by Scott)
status: seed|drafted|published
final_title: ""
published_date: null
substack_url: ""
medium_url: ""
linkedin_url: ""

created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

---

## Schema: `learner-profile` (PERSONA.md — first-person, fully public)

This is the anchor document for RQ5. It is authored directly by Scott in first person.
It is not a template to be filled in — it is a living document that grows over the life
of the curriculum. Generated as the primary artifact of M61.

```yaml
---
type: learner-profile
schema_version: "1.0"
learner_id: L001
authored_by: Scott       # fully attributed, fully public
created: YYYY-MM-DD
updated: YYYY-MM-DD

# ---------------------------------------------------------------
# This document is a primary research artifact for RQ5:
# "How do a learner's personal characteristics shape their
# trajectory through AI-mediated doctoral-level study?"
# It is fully public. All fields below represent Scott's
# voluntary, first-person self-disclosure.
# ---------------------------------------------------------------

# Neurodivergence and health (Scott's self-reported profile)
conditions:
  adhd: true
  bipolar_ii: true
  # add others as comfortable; remove any that don't apply

# Learning characteristic profile (self-assessed baseline)
# These are starting points — update as the curriculum progresses
attention_profile: variable          # consistent|variable|low
recall_profile: variable             # strong|variable|weak
energy_profile: cyclical             # consistent|variable|cyclical
executive_function: low-medium       # strong|medium|low-medium|low
task_initiation: difficult           # easy|medium|difficult
commitment_consistency: low-medium   # high|medium|low-medium|low
hyperfocus_capable: true             # can lock in deeply under right conditions
rejection_sensitivity: moderate      # RSD — affects feedback reception

# Session-level patterns observed (updated over time)
high_energy_indicators: []           # fill as patterns emerge
low_energy_indicators: []
optimal_session_conditions: []
failure_mode_patterns: []            # what tends to derail sessions

# What AI as a teaching tool does differently for this learner
ai_advantages_observed: []           # fill as curriculum progresses
ai_limitations_observed: []
adaptations_that_work: []
adaptations_that_don_t: []

# Preferred learning conditions (baseline)
session_length_preferred_min: 45
session_length_preferred_max: 90
environment_preference: quiet
modality_preference: [reading, doing]
motivation_type: intrinsic-and-social

# Research methodology note
research_design: autoethnography
methodology_justification: >
  Autoethnography uses the researcher's own lived experience as primary data.
  It is a recognized qualitative method in education research (Chang, 2008;
  Ellis, Adams & Bochner, 2011), AIED (Buckingham Shum & Ferguson, 2012),
  and disability studies. N=1 studies cannot support generalizable claims,
  but can generate hypotheses, document phenomena, and produce design principles
  grounded in lived experience. Claims in this thesis derived from this dataset
  are framed as generative hypotheses for future research, not as universal findings.
scope_of_claims: generative-hypotheses-only
future_research_directions: []      # fill as patterns emerge

tags: [learner-profile, autoethnography, rq5, neurodivergence, mental-health, public]
---

# Scott — Learner Profile and PERSONA

*[This section is written by Scott in first person. It is the human document
behind the structured YAML above. It will be written as part of M61.]*
```

---

## Schema: `portfolio-entry`

```yaml
---
type: portfolio-entry
schema_version: "1.0"
module_id: M##
project_title: ""
project_description: ""
skills_demonstrated: []
languages_used: []
h_and_c_connection: ""
status: in-progress|complete|demo-ready
demo_url: ""
repo_path: ""            # path within phd-applied-ai repo
employment_relevance: "" # how this would appear in a job/investor conversation
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

---

*This schema is the source of truth for all phd-applied-ai repo artifacts.*
*Update schema_version when breaking changes are made. Maintain backwards compatibility.*
*The learner-profile schema is the most sensitive — treat it with care.*
