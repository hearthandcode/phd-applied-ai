---
type: experiments-index
schema_version: "1.0"
created: 2026-06-29
updated: 2026-06-29
tags: [experiments, methodology, research]
---

# Experiments

This directory holds **formal experiments** conducted as part of the Hearth & Code PhD research.
Experiments are systematic investigations with a stated hypothesis, a documented methodology, raw
data, analysis, and findings tied back to the research questions (RQ1–RQ5, see `THESIS.md`).

Experiments differ from session logs (which capture the *researcher's* experience, RQ5) and from
modules (which are the *curriculum* artifacts). An experiment tests a **methodological or systems
question** about how the curriculum/platform should be built — feeding RQ2 (scaffolding
configurations), RQ3 (platform design), and RQ4 (curriculum design principles).

## Structure

```
experiments/
  README.md                         # this index
  EXP-NNN-short-slug/
    experiment.md                   # hypothesis, methodology, procedure, results, findings, implications
    data/                           # raw outputs / measurements (reproducible inputs)
    analysis/                       # graded comparisons, gap analyses
    artifacts/                      # scripts, prompts, configs used to run it
```

## Experiment registry

| ID | Title | Status | RQs | Date |
|---|---|---|---|---|
| [EXP-001](EXP-001-local-model-curriculum-generation/experiment.md) | Local-Model Curriculum Generation: quality, verification & generation-strategy comparison | in-progress | RQ2, RQ3, RQ4 | 2026-06-29 |

## Conventions

- Each experiment has a stable `exp_id` (EXP-NNN); IDs are permanent and not reused.
- `experiment.md` carries machine-readable frontmatter (`type: experiment`, `status`, `rq_refs`).
- Raw data goes in `data/` so results are reproducible; analysis/interpretation goes in `analysis/`.
- Findings must distinguish **deterministic** results (e.g. executed code) from **model-judged** ones.
- Every experiment ends with an **implications for the research** section linking findings to RQs and,
  where relevant, to `METHODOLOGY.md` (the curriculum generation methodology this research maintains).
