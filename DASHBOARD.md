---
type: curriculum-dashboard
schema_version: "1.0"
created: 2026-06-18
updated: 2026-06-18
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
