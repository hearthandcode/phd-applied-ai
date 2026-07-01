---
type: changelog
title: "Thesis Changelog — Redline Record of Thesis & RQ Evolution"
domain: research/learning
status: needs-review
created: 2026-07-01
updated: 2026-07-01
tags: [thesis, changelog, redline, research-questions, provenance]
graph_refs: [THESIS.md, docs/redesign-2026-07/thesis-refocus-proposal.md, docs/redesign-2026-07/research-questions-proposal.md, docs/redesign-2026-07/curriculum-structure-proposal.md]
llm_accessible: true
generated_by: track-a-agent
verified: false
---

# Thesis Changelog

A dated redline history of how the thesis statement, research questions, and thesis-level
framing have evolved. This file exists so the evolution of the research design is itself part
of the public research record (a methodological commitment in `THESIS.md`: the design's
evolution is data, not embarrassment).

This is thesis-*framing* history. It complements — does not replace — the repo-wide
`CHANGELOG.md` (operational changes) and the `sessions/` logs (autoethnographic record).

---

## Convention

Each entry follows this format:

```
## YYYY-MM-DD — Short title
**Stage:** PROPOSAL | APPLIED
**Scope:** which artifact(s) the change touches (THESIS.md, RQ set, curriculum, …)
**Driver:** what prompted the change (1 line)

### Redline
> ~~struck old text~~ → **new text**

(one redline block per changed statement; quote the old text verbatim, strike it, and show
the replacement in bold)

### Rationale
Why the change is stronger / necessary (2–5 lines)

### Ripple
Files/scripts/commands affected + migration status
```

**Ordering:** newest entry at the top.

**Two-stage rule.** Entries are logged at **PROPOSAL** stage *before* any file is edited. The
redline is written here first; only after human approval is the change **applied** to the
target file, at which point the entry's `Stage:` is updated to **APPLIED** (with the applying
commit noted). This guarantees the redline is recorded even if the edit is later reverted, and
that no thesis-level text changes silently.

**Strike syntax.** GitHub-flavoured Markdown `~~text~~` renders as struck-through. Keep the
struck text an exact quote of what was in the file, so a reader can reconstruct the old state.

---

## 2026-07-01 — Refocus: AI as Cognitive Scaffolding (Extended Mind, implemented)

**Stage:** PROPOSAL *(nothing in `THESIS.md` has been edited; see the three proposal docs in
`docs/redesign-2026-07/`)*
**Scope:** `THESIS.md` (title, central hypothesis, RQ1–5, contributions, key terms),
`README.md`, `curriculum/phase-map.md`, and the RQ-referencing commands/scripts.
**Driver:** The working thesis had drifted into a platform/ed-tech systems framing while the
actual method was an N=1 autoethnography (old RQ5). Refocusing onto the Extended Mind thesis
gives the work a citable theoretical core, an argument with a real opposing side (the
coupling–constitution objection), and an honest scope (generative hypotheses, not
generalization). Full argument in `docs/redesign-2026-07/thesis-refocus-proposal.md`.

### Redline — Title
> ~~Adaptive AI-Native Learning Systems: Architecture, Pedagogy, and Ethics of a
> Next-Generation Educational Platform~~ → **The Extended Mind, Implemented: AI as Cognitive
> Scaffolding for Neurodivergent Adults — An Autoethnographic Study of Cognition, Identity,
> and the Conception-to-Execution Gap**

### Redline — Central hypothesis
> ~~Augmented intelligence — AI operating as a bidirectional cognitive extension, calibrated
> to a learner's individual personality and cognitive profile — enables learning outcomes that
> traditional institutional models of education failed to produce. For neurodiverse learners
> whose cognitive profiles create significant friction at the task-initiation and
> conception-to-execution interface, this augmentation does not merely improve outcomes: it
> enables doctoral-level engagement that was previously structurally inaccessible.~~ →
> **When an AI system is configured as a persistent, trusted, individually-calibrated
> cognitive partner, it functions as a literal implementation of the Extended Mind thesis
> (Clark & Chalmers, 1998): its representations and processes become genuine constituents of
> the subject's cognitive system rather than external aids to it. For a neurodivergent adult
> whose executive function is unevenly available and whose cognition is inseparable from
> identity, this extended cognitive system externalizes executive function, closes the
> conception-to-execution gap, and thereby makes doctoral-level intellectual work possible
> that unscaffolded cognition and conventional institutions did not produce. These claims are
> advanced as generative hypotheses from an N=1 autoethnography, not as generalizable findings.**

### Redline — Research questions (summary; full set in research-questions-proposal.md)
> ~~RQ1 AI scaffolding & doctoral outcomes · RQ2 Effective scaffolding configurations ·
> RQ3 Adaptive platform design · RQ4 Curriculum design principles · RQ5 Neurodiversity &
> AI-mediated learning (autoethnographic)~~ →
> **nRQ1 Constitution (is it a genuine extended mind?) · nRQ2 Mechanism (executive-function
> externalization, conception→execution) · nRQ3 Configuration (intrinsic-motivation- and
> reward-sensitivity-aware) · nRQ4 Identity, agency & ethics of cognitive extension ·
> nRQ5 Applied translation (design principles for the H&C platform).**

### Rationale
- Names the mechanism as a falsifiable philosophical claim (constitution vs. mere causation),
  not an unfalsifiable "augmentation helps."
- Aligns the thesis frame with its real method (autoethnography), removing the systems/qualitative
  mismatch and strengthening the existing conflict-of-interest commitments.
- Scopes claims honestly to N=1 generative hypotheses; moves generalization to future work.
- Elevates two genuinely new questions the old set lacked: the constitution question (nRQ1) and
  identity/agency under cognition-as-identity (nRQ4).
- Preserves M01 and the entire technical curriculum as the *domain of mastery* being evidenced.

### Ripple
See `research-questions-proposal.md` §3 for the full table. Key surfaces: `THESIS.md`,
`README.md`, `curriculum/phase-map.md` (map + inline module tags), `.claude/commands/rq-checkpoint.md`,
`.claude/commands/learning-log.md` (`rq5_tags` field), `docs/session-log-process.md`
(controlled vocabulary), `scripts/sync-layer.py` (`RESEARCH_QUESTIONS` + `RQ_MODULES` dicts),
`scripts/generate-glance.py`. **Locked `sessions/` logs are NOT edited** — a forward crosswalk
(research-questions-proposal.md §3.1) handles old→new tag continuity. A pre-existing
inconsistency was found: the scripts/phase-map already use different RQ titles than `THESIS.md`
(research-questions-proposal.md §3.3) — recommend a single canonical `research-questions.yaml`.

**Application status:** NOT applied. Awaiting Scott's decisions on: term retirement
("augmented intelligence"), title wording, strong-constitution vs. complementarity commitment,
RQ count, module numbering (`N`-prefix vs. `M68+`), and M50/M54 demote-vs-delete. On approval,
each target file gets its own redline entry here at APPLIED stage before being edited.
