---
type: curriculum-dashboard
schema_version: "1.0"
created: 2026-06-18
updated: 2026-07-04
learner_id: L001
tags: [dashboard, curriculum, obsidian-dataview]
---

# Hearth & Code PhD — Curriculum Dashboard

> *"Every fire starts with a single spark. These are the 67."*
> — Virgil

## Usage

This dashboard uses [Obsidian Dataview](https://blacksmithgu.github.io/obsidian-dataview/) to track module progression. 
You need the Dataview plugin installed and JavaScript queries enabled.

To update: when you complete a section, update the `status` field in that section's frontmatter.

---

## Thesis refocus status: 2026-07-04

The active redesign thread shifts this repo from an education-platform thesis toward:

> **AI as a cognitive platform / cognitive prosthesis for neurodivergent adults, grounded in Extended Mind, documented through N=1 autoethnography.**

The Hearth & Code platform remains the applied artifact. It is no longer the primary object of study. The primary object is the coupled human-AI cognitive system: task initiation, working memory, affect regulation, authorship, identity, continuity, and the conception-to-execution gap.

### Read first

| Doc | Why it matters | Status |
|---|---|---|
| `docs/redesign-2026-07/thesis-refocus-proposal.md` | Main thesis pivot: Extended Mind, cognitive scaffolding, platform as artifact | needs review |
| `docs/redesign-2026-07/research-questions-proposal.md` | Proposed nRQ1 to nRQ5 and migration ripple | needs review |
| `docs/redesign-2026-07/curriculum-structure-proposal.md` | Keeps the technical spine, adds cognitive science, philosophy, and disability studies tracks | needs review |

### Current repo state found 2026-07-04

- Branch is current with `origin/main`.
- The three redesign proposal files above have local modifications with Scott's answers to open questions.
- New July session logs exist locally and are untracked: `sessions/2026/07/2026-07-02.md`, `2026-07-03.md`, `2026-07-04.md`.

### Next concrete action

Decide whether nRQ1 and nRQ2 stay separate or merge, then create a canonical `curriculum/research-questions.yaml` and a forward `docs/redesign-2026-07/rq-crosswalk.md` before editing `THESIS.md`.

Do not edit `THESIS.md` until Scott explicitly approves the redline.

---

## Overall Progress

```dataviewjs
const modules = dv.pages('"modules"')
  .where(p => p.type === 'module-theory' || p.module_id)
  .sort(p => p.module_id)

const total = modules.length
const reviewed = modules.where(p => p.status === 'reviewed').length
const generated = modules.where(p => p.status === 'generated' || p.status === 'draft').length
const planned = modules.where(p => p.status === 'planned' || !p.status).length

dv.span(`${reviewed} reviewed / ${generated} generated / ${planned} planned (of ${total} total)`)

if (total > 0) {
  dv.span(`\n`)
  dv.span(`![progress](https://progress-bar.dev/${Math.round(reviewed/total*100)}?title=Complete&width=500&color=e8923c)`)
}
```

---

## Module Table

```dataviewjs
const modules = dv.pages('"modules"')
  .where(p => p.type === 'module-theory' || p.module_id)
  .sort(p => p.module_id)

for (const m of modules) {
  const sections = dv.pages('"' + m.file.folder + '/theory"')
  const sectionCount = sections.length
  const sectionDone = sections.where(p => p.status === 'reviewed' || p.status === 'complete').length
  dv.header(3, `[[${m.file.path}|${m.module_id || m.file.name}: ${m.module_title || m.title}]]`)
  dv.paragraph(`Phase ${m.phase || '?'} · ${m.status || 'planned'} · Theory: ${sectionDone}/${sectionCount} · Last: ${m.updated || '—'}`)
}
```

---

## Next Module

```dataviewjs
const modules = dv.pages('"modules"')
  .where(p => p.type === 'module-theory')
  .sort(p => p.module_id)

const next = modules.find(p => p.status !== 'reviewed' && p.status !== 'complete')
if (next) {
  dv.paragraph(`**Next:** [[${next.file.path}|${next.module_id}: ${next.module_title || next.title}]]`)
} else {
  dv.paragraph('All modules reviewed!')
}
```

---

## Study Prompts

Click any prompt to copy and paste into Hermes or Claude.

**Quick Review**
> "I just finished [module]. Quiz me on the key concepts before I move to the next module."

**Deep Dive**
> "Explain [concept] at a doctoral level, connecting it to the H&C platform architecture."

**Debug My Understanding**
> "I think [my understanding]. Push back on me — where does my intuition break?"

---

*Last updated: 2026-06-18*
