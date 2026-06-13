# Session Log Process

How session logs are created, described, verified, and stored in this curriculum.

---

## Purpose

Session logs serve two functions simultaneously:

1. **Curriculum tracking** — what was studied, for how long, at what competency level.
2. **RQ5 data collection** — longitudinal psychological and cognitive data on a neurodiverse
   learner navigating AI-mediated doctoral study. Energy, mood, focus, and cognitive load
   over 5+ years constitute the dataset for Research Question 5.

Because these logs are both a personal research record and a public longitudinal dataset,
accuracy and verification matter. A session log is only as useful as it is honest.

---

## Log types

| Type | When | Files |
|---|---|---|
| `study-session` | After any module study session | `sessions/YYYY/MM/YYYY-MM-DD.md` |
| `meta-reflection` | Non-study events with RQ5 relevance (launch days, decisions, significant psychological events) | `sessions/YYYY/MM/YYYY-MM-DD.md` |
| `weekly-review` | End of week | `sessions/reviews/YYYY-WXX.md` |
| `generation-event` | After AI content generation for a phase | `AUDIT_LOG.md` entry only |

---

## The collaborative logging process

This process is designed for sessions conducted with an AI assistant (Claude Code or any
model via AGENT.md prompts). It can also be used for solo logging without the interview step.

### Step 1 — Initiation

Start a session log by telling the AI assistant: *"Let's log today's session."*

The assistant will ask structured interview questions (see below). Answer in whatever form
comes naturally — bullet points, stream of consciousness, a paragraph. The raw answer is
not the log; it's the source material.

### Step 2 — Interview questions

The assistant asks:

**Logistics**
- What did you work on today? (Modules, tasks, or type of session)
- Approximately how many hours?
- Was this primarily study, generation, meta work, or mixed?

**Psychological state**
- How would you rate your energy today? (1–5 scale)
- How would you rate your focus quality? (1–5 scale)
- How would you describe your mood? (free response — one word or a phrase)
- Anything notable about cognitive load (high/low, why)?
- Any significant emotional events, stressors, or mental health observations relevant to the session?
- Medication notes (optional — record or skip)?

**Study content (for study sessions)**
- Which modules were active?
- What did you read, implement, or work through?
- What clicked? What didn't?
- Self-assessment against rubric.md: where do you think you are on competency 1–4?
- Any key insights worth preserving?
- Open questions the session raised?

**RQ5 (brief)**
- Anything this session reveals about how your ADHD/bipolar shapes your learning?
- Off days? Unusual cognitive states? Patterns you noticed?

### Step 3 — Clinical/research-level description generation

The assistant generates a session log using the YAML frontmatter schema (see
`sessions/README.md`) and a structured narrative body with sections:

- **Session summary** — 2–3 sentences, factual
- **Psychological state** — clinical description of self-reported emotional and cognitive state
- **Study content** (for study sessions) — what was covered and at what depth
- **Cognitive observations** — executive function, attention, meta-cognitive awareness
- **RQ5 relevance** — how this session contributes to the longitudinal dataset
- **Adaptive responses** — decisions made, coping strategies employed
- **Open items** — unresolved questions or next steps

The language is descriptive rather than evaluative. Clinical vocabulary is used where
appropriate (e.g., "elevated cognitive load," "anxiety presentation," "executive function
engagement"). First-person voice is maintained (this is autoethnographic research).

### Step 3b — Public disclosure check (REQUIRED before generation)

**Session logs are committed to a public GitHub repository and are permanently public record.**

Before the assistant generates the clinical description, it will flag any content from
the interview that may not be appropriate for public disclosure and ask whether to include,
omit, or rephrase it. Categories to watch for:

- Financial information (income, benefits, debts, specific monetary amounts)
- Legal or benefits status (disability benefits, legal proceedings, government programs)
- Medical specifics beyond general diagnosis disclosure (medications by name, dosages,
  treatment details you haven't publicly disclosed elsewhere)
- Identifying information about third parties (names, relationships, situations involving
  other people who haven't consented to being in a public record)
- Anything said in the interview heat-of-moment that on reflection you wouldn't want
  searchable and permanent

The assistant will prompt: *"Before I write this up, I want to flag [X] — is that something
you want included in the public log, omitted entirely, or noted in a private way (e.g.,
'a financial concern was noted but not detailed')?*"

When in doubt, omit or generalize. The research value of a session log comes from
psychological and cognitive data, not from financial or legal specifics.

### Step 4 — Review and edit

Read the generated log. Edit anything that is:
- Inaccurate (wrong facts, mischaracterized feelings)
- Overstated or understated
- Missing something important
- Worded in a way that doesn't represent your experience

You do not need to preserve the AI's framing. This is your record. Edit freely.

### Step 5 — Verification and sign-off

Add your verification to the log's sign-off block (see template below) and set
`verified: true` in the YAML frontmatter.

The verification declares that:
- You have read the log
- You made any necessary corrections
- The log accurately represents your experience and state on the logged date

### Step 6 — Commit

```bash
git add sessions/YYYY/MM/YYYY-MM-DD.md
git commit -m "study(session): YYYY-MM-DD session log — [brief description]"
git push
```

---

## Verification block template

Include this section at the end of every session log body:

```markdown
---

## Verification

I have read this session log, made any necessary corrections, and confirm that it
accurately represents my psychological state, cognitive experience, and activities
on the above date to the best of my recollection. I consent to its inclusion in
the RQ5 longitudinal research dataset as part of this curriculum.

| Field | Value |
|---|---|
| **Verified by** | Scott Rallya |
| **Initials** | SR |
| **Date reviewed** | YYYY-MM-DD |
| **Edits made** | Yes / No / Minor |
| **Status** | Verified |
```

---

## YAML frontmatter fields

See `sessions/README.md` for the full schema. Key fields for RQ5:

| Field | Type | Notes |
|---|---|---|
| `energy_level` | 1–5 | See scale anchors in `sessions/README.md` |
| `focus_quality` | 1–5 | See scale anchors in `sessions/README.md` |
| `mood` | string | Free description, consistent vocabulary preferred |
| `cognitive_load` | low/medium/high/critical | See scale anchors in `sessions/README.md` |
| `interruption_count` | int | External interruptions during session |
| `recall_difficulty` | low/medium/high/n-a | See scale anchors in `sessions/README.md` |
| `medication_notes` | string or null | Optional; omit if not for public record |
| `rq5_tags` | list | Tags for RQ5 analysis (see controlled vocabulary below) |
| `verified` | bool | Must be `true` before log counts as research data |
| `verified_by` | string | Full name |
| `verified_date` | YYYY-MM-DD | Date of sign-off |

Scale anchor definitions are in `sessions/README.md` — use that file as the canonical
reference. Do not redefine scales inline in individual logs.

### RQ5 tag vocabulary (use consistently)

```
project-initiation       — session involving starting something new
public-exposure          — first or significant public-facing action
anxiety                  — notable anxiety presentation
executive-function       — notable executive function engagement or difficulty
hyperfocus               — extended high-engagement session
low-energy-productive    — produced meaningful work despite low energy
off-day                  — session with minimal output (data, not failure)
confidence-calibration   — uncertainty about own judgment or work quality
meta-cognition           — awareness of own cognitive/emotional processes
medication-effect        — notable effect (positive or negative) of medication timing
interruption-recovery    — returned to session after significant interruption
```

---

## Solo logging (without AI interview)

If you're logging without an AI assistant:

1. Open a new file at `sessions/YYYY/MM/YYYY-MM-DD.md`
2. Copy the frontmatter from `sessions/EXAMPLE-session-template.md`
3. Fill in the fields as honestly as you can
4. Write a brief narrative — even 3 sentences counts
5. Add the verification block and sign off
6. Commit

An imperfect log committed is more valuable than a perfect log that isn't written.

---

## On accuracy and honesty

The longitudinal value of this dataset depends entirely on the accuracy of each entry.
Some guidance:

- **Log the bad days.** Off days are data. A log that says "low energy, did nothing, felt stuck" is
  exactly as valuable as a high-output session log. It's what RQ5 needs.
- **Don't reconstruct.** Log as close to the session as possible. Memory degrades within hours,
  especially under ADHD conditions. An imprecise same-day log beats a polished next-week log.
- **Verification is not editing for image.** The verification step is for accuracy, not
  for making yourself look good. If the session was bad, verify it accurately.
- **Medication notes are optional but valuable.** If you're comfortable including them,
  they may be the most analytically useful field in the dataset.
