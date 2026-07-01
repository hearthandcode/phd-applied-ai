---
type: research-proposal
title: "Research Questions Proposal — Extended-Mind-Aligned RQ Set + Migration Ripple"
domain: research/learning
status: needs-review
created: 2026-07-01
updated: 2026-07-01
tags: [research-questions, redesign, extended-mind, autoethnography, migration, proposal]
graph_refs: [THESIS.md, docs/redesign-2026-07/thesis-refocus-proposal.md, curriculum/phase-map.md, scripts/sync-layer.py, scripts/generate-glance.py, .claude/commands/rq-checkpoint.md, .claude/commands/learning-log.md]
llm_accessible: true
generated_by: track-a-agent
verified: false
---

# Research Questions Proposal

**Status: PROPOSAL — no RQ text is changed anywhere by this document.** It specifies a
revised RQ set, maps old→new, and makes the migration cost visible before anything is edited.

Terminology: new questions are labelled **nRQ1–nRQ5** here to avoid collision with the live
RQ1–RQ5 during review. On approval they would simply become RQ1–RQ5.

---

## 1. The revised RQ set

All five are **autoethnographic N=1** and scoped to **generative hypotheses, not
generalizable findings.** The subject is Scott (ADHD, bipolar II, possible autism;
cognition-as-identity). The applied artifact is the Hearth & Code platform.

**nRQ1 — Constitution (is it really an extended mind?)**
Does a persistent, trusted, individually-calibrated AI partner satisfy the Extended Mind
thesis's conditions (Clark & Chalmers' trust-and-glue criteria) well enough to count as a
*constituent* of the subject's cognitive system, rather than merely a tool it is coupled to?
What first-person (phenomenological) and behavioral evidence supports, or complicates, a
constitution reading against the coupling–constitution objection (Adams & Aizawa)?

**nRQ2 — Mechanism (how does the scaffold work?)**
Through what specific mechanisms does the AI scaffold externalize executive function — task
initiation, working memory, temporal/planning organization, affect regulation — and bridge
the conception-to-execution gap for this neurodivergent subject? Which mechanisms are load-
bearing for reaching doctoral-level competency in the CS/AI domain?

**nRQ3 — Configuration (what makes an effective cognitive prosthesis?)**
What configurations of the extended cognitive system — calibration to the subject's
cognitive profile, pacing, and **intrinsic-motivation- and reward-sensitivity-aware** design —
most reliably sustain the coupling and keep the subject engaged? (Explicitly reframes the old
gamification/virtue-vice mechanism toward intrinsic motivation and reward-sensitivity; see §4.)

**nRQ4 — Identity, agency, and ethics of cognitive extension**
Given that this subject's *cognition is inseparable from identity*, how does incorporating AI
into the cognitive system affect his sense of agency, authorship, and self — and what ethical
risks (dependence, deskilling, epistemic-agency erosion, autonomy for disabled users) attend
cognitive extension for neurodivergent adults?

**nRQ5 — Applied translation (from N=1 to designed artifact)**
What design principles for tools that function as cognitive scaffolding — instantiated in the
Hearth & Code platform — follow from this autoethnographic record, stated as generative
hypotheses for future (non-N=1) validation?

---

## 2. Old → New mapping

| Old RQ (live in THESIS.md) | Disposition | Maps to |
|---|---|---|
| **RQ1** — Does profile-calibrated AI scaffolding enable doctoral outcomes institutions failed to produce? | **Split + re-grounded** in Extended Mind theory | **nRQ1** (is the enabling *constitutive*?) + **nRQ2** (by what mechanism?) |
| **RQ2** — What scaffolding configurations (pedagogy, virtue/vice affect modeling, pacing) are most effective? | **Retained, reframed** — de-emphasize virtue/vice + gamification, emphasize intrinsic motivation / reward-sensitivity | **nRQ3** |
| **RQ3** — How should an adaptive platform implement these for *similar learner populations*? | **Downscoped** — drop the generalization ("similar populations") to generative design hypotheses | **nRQ5** |
| **RQ4** — What curriculum design principles emerge from longitudinal AI-mediated study? | **Absorbed** | **nRQ5** (design principles) + **nRQ3** (configuration) |
| **RQ5** — How do the learner's characteristics shape the AI-mediated trajectory (autoethnographic)? | **Promoted to the spine** — its method now governs all five | Runs through **all**, most directly **nRQ2** + **nRQ4** |
| *(none)* | **New, made central by Extended Mind framing** | **nRQ1** (constitution question) and the identity half of **nRQ4** are genuinely new |

**Net effect:** 5 → 5, but the center of gravity moves from *platform/pedagogy* (old RQ2–RQ4)
to *cognition/identity* (new nRQ1, nRQ2, nRQ4), with platform design surviving only as the
downstream applied question (nRQ5).

---

## 3. Migration ripple — everything that references the RQs

The RQ set is referenced in more places than `THESIS.md`. **Sessions are locked and must not
be edited** (see §3.1). Migration cost is moderate and mostly mechanical, except the two
Python dicts and the locked-session crosswalk.

| # | Surface | Location | What references RQs | Migration action |
|---|---|---|---|---|
| 1 | Thesis body | `THESIS.md` | RQ1–5 definitions, methodology note, contribution list, key-concepts | Rewrite via CHANGELOG redline (human-approved) |
| 2 | README | `README.md` | "Five research questions" bullet list | Replace list |
| 3 | Phase map | `curriculum/phase-map.md` | "Research Questions Map" section **and** inline module tags: M54 *RQ3 core*, M55 *RQ4 core*, M58 *Extended Mind — hypothesis grounding*, M61 *RQ5 core* | Rewrite map + retag modules (see curriculum proposal) |
| 4 | RQ command | `.claude/commands/rq-checkpoint.md` | Hardcodes all five RQ texts verbatim | Replace RQ block |
| 5 | Learning-log command | `.claude/commands/learning-log.md` | **`rq5_tags:` frontmatter field** in the log template + an "RQ5 relevance" body section + controlled-vocabulary pointer | Rename/generalize `rq5_tags` → `rq_tags`; update section (see §3.2) |
| 6 | Session-log process | `docs/session-log-process.md` | Defines the `rq5_tags` **controlled vocabulary** | Update vocabulary to new RQ scheme |
| 7 | Sync script | `scripts/sync-layer.py` | `RESEARCH_QUESTIONS = {...}` and `RQ_MODULES = {...}` hardcoded dicts (lines ~48–56); drives RQ progress rollups | Edit both dicts; **note: these titles are already stale vs. THESIS.md — see §3.3** |
| 8 | Glance script | `scripts/generate-glance.py` | Iterates `["RQ1".."RQ5"]` and reads `rq['title']`/modules (line ~101) | No code change needed if keys stay RQ1–5; titles/modules come from data — verify |
| 9 | Session logs (data) | `sessions/**/*.md` frontmatter | Inline `tags: [rq2, rq4, rq5, ...]` on individual sessions | **DO NOT EDIT (locked).** Provide a forward crosswalk instead (§3.1) |
| 10 | Committee personas | `committee/dr-okonkwo.md`, `dr-williams.md`, `dr-chen.md` | Prose references to RQ focus areas | Light prose update when convenient |
| 11 | Idea log | `ideas/research.md` | RQ-tagged evidence fragments | Append note; no rewrite of history |
| 12 | Agent context | `AGENT.md`, `CLAUDE.md`, `docs/commands.md` | Summary mentions of the RQ set | Update summaries |

### 3.1 Locked sessions — forward crosswalk, not edits

Session logs 2026-06-24/26/28/29/30 are `verified: true, locked: true`; 2026-07-01 is pending
review. Historical logs carry old inline tags (`rq2`, `rq4`, `rq5`). **These stay as-is.**
Any RQ analytics that must span old and new logs should apply this crosswalk at read time:

| Old tag | Reads forward as |
|---|---|
| `rq1` | `nrq1` + `nrq2` (ambiguous — treat as "enablement/mechanism") |
| `rq2` | `nrq3` |
| `rq3` | `nrq5` |
| `rq4` | `nrq5` (+ `nrq4` where the entry was about ethics/governance) |
| `rq5` | spine; map to `nrq2`/`nrq4` by content, else keep as `nrq-spine` |

New sessions (2026-07-01 onward, once approved) use the new tags directly.

### 3.2 The `rq5_tags` field specifically
`learning-log.md` bakes a field literally named **`rq5_tags`** into every interaction-log
template, and `docs/session-log-process.md` holds its controlled vocabulary. Because RQ5 is
now the *spine* (not one question), the honest rename is **`rq_tags`** with the new
vocabulary — but this changes the schema of a per-session artifact. Recommend: keep accepting
`rq5_tags` as a deprecated alias for one migration window rather than a hard cutover.

### 3.3 Pre-existing inconsistency (found during this analysis — flag)
`scripts/sync-layer.py` and `curriculum/phase-map.md` already define the RQs with **different
titles than `THESIS.md`**:

| | RQ1 | RQ2 | RQ3 | RQ4 |
|---|---|---|---|---|
| `sync-layer.py` / phase-map | Adaptive Competency Modeling | Pedagogy & Generative AI | Personality, Virtue & Motivation | Ethics & Governance at Scale |
| `THESIS.md` (authoritative) | AI scaffolding → doctoral outcomes | Effective scaffolding configurations | Adaptive platform design | Curriculum design principles |

So the code's RQ model has been drifting from the thesis already. The migration is a chance to
make one canonical RQ source instead of three hand-maintained copies (recommend: a single
`curriculum/research-questions.yaml` that `THESIS.md`, the scripts, and the commands all read).

---

## 4. Note on virtue/vice and gamification (de-emphasis)

Old RQ2 named "virtue/vice calibration" as a core mechanism and old phase-map made M50
(Gamification) and M54 (Virtue & Vice) *RQ-core* modules. The new direction **de-emphasizes**
both:
- Gamification → reframed as **reward-sensitivity-aware, intrinsic-motivation-first** design
  (per the hub `learner-profile-variables.md`: frequent moderate-salience signals, visible
  artifacts, low-friction entry — *not* points/badges for their own sake).
- Virtue/vice personality modeling → retained only as a *possible* configuration input under
  nRQ3, not a headline mechanism.

**Decision for Scott:** demote M50/M54 to elective/adjacent, or drop them from RQ-core
entirely? (See curriculum proposal §5.)

---

## 5. Open decisions requiring Scott's judgment

1. Adopt nRQ1–nRQ5 as written, or fewer (e.g., merge nRQ1+nRQ2 into one constitution-and-
   mechanism question, yielding 4 RQs)?
2. `rq5_tags` → `rq_tags` hard rename vs. deprecated-alias window (§3.2)?
3. Build the single canonical `research-questions.yaml` source now, or keep hand-maintained
   copies (§3.3)?
4. Crosswalk analytics at read time (§3.1) — acceptable, or do you want a separate
   `sessions/rq-crosswalk.md` reference file committed?

**Next:** Decide §5.1 (RQ count) first — everything else (dicts, commands, crosswalk) follows
from the final RQ list. Nothing edits `THESIS.md` until that number is fixed.
