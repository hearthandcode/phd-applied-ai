---
type: dashboard
title: PhD Module Tracker
---

# PhD Curriculum — Module Tracker

> Vault path: `phd/modules/` — queries `rubric.md` in each module directory.
> Assumes Obsidian vault with symlink: `phd/ → phd-applied-ai/`
> To log hours: open the module's `audit.md` and add a session entry. Update `actual_hours` and `competency_level` in `rubric.md` frontmatter.

---

## Progress Summary

```dataviewjs
const rubrics = dv.pages('"phd/modules"').where(p => p.type === "module-rubric")

const total = rubrics.length
const complete = rubrics.where(p => p.status === "complete").length
const inProgress = rubrics.where(p => p.status === "in-progress").length
const pending = rubrics.where(p => p.status === "pending").length
const totalPar = rubrics.array().reduce((s, p) => s + (p.par_hours ?? 0), 0)
const totalActual = rubrics.array().reduce((s, p) => s + (p.actual_hours ?? 0), 0)
const pctDone = total > 0 ? Math.round((complete / total) * 100) : 0
const avgCompetency = total > 0
  ? (rubrics.array().reduce((s, p) => s + (p.competency_level ?? 0), 0) / total).toFixed(2)
  : 0

dv.paragraph(`**Modules:** ${total} total · ✅ ${complete} complete · 🔵 ${inProgress} in progress · ⬜ ${pending} pending · ${pctDone}% done`)
dv.paragraph(`**Hours:** ${totalActual} actual / ${totalPar} par · **Avg competency:** ${avgCompetency} / 4`)
```

---

## Phase 0 — Mathematical Foundations

```dataviewjs
const mods = dv.pages('"phd/modules"')
  .where(p => p.type === "module-rubric" && p.phase === 0)
  .sort(p => p.module_id, "asc")

const parSum = mods.array().reduce((s, p) => s + (p.par_hours ?? 0), 0)
const actualSum = mods.array().reduce((s, p) => s + (p.actual_hours ?? 0), 0)
dv.paragraph(`${mods.length} modules · ${parSum} par hrs · ${actualSum} actual hrs`)

dv.table(
  ["ID", "Title", "Par Hrs", "Actual", "Competency", "Status"],
  mods.map(p => [p.module_id, p.file.link, p.par_hours ?? "—", p.actual_hours ?? 0, `${p.competency_level ?? 0}/4`, p.status])
)
```

## Phase 1 — CS Fundamentals

```dataviewjs
const mods = dv.pages('"phd/modules"')
  .where(p => p.type === "module-rubric" && p.phase === 1)
  .sort(p => p.module_id, "asc")

const parSum = mods.array().reduce((s, p) => s + (p.par_hours ?? 0), 0)
const actualSum = mods.array().reduce((s, p) => s + (p.actual_hours ?? 0), 0)
dv.paragraph(`${mods.length} modules · ${parSum} par hrs · ${actualSum} actual hrs`)

dv.table(
  ["ID", "Title", "Par Hrs", "Actual", "Competency", "Status"],
  mods.map(p => [p.module_id, p.file.link, p.par_hours ?? "—", p.actual_hours ?? 0, `${p.competency_level ?? 0}/4`, p.status])
)
```

## Phase 2 — ML Foundations

```dataviewjs
const mods = dv.pages('"phd/modules"')
  .where(p => p.type === "module-rubric" && p.phase === 2)
  .sort(p => p.module_id, "asc")

const parSum = mods.array().reduce((s, p) => s + (p.par_hours ?? 0), 0)
const actualSum = mods.array().reduce((s, p) => s + (p.actual_hours ?? 0), 0)
dv.paragraph(`${mods.length} modules · ${parSum} par hrs · ${actualSum} actual hrs`)

dv.table(
  ["ID", "Title", "Par Hrs", "Actual", "Competency", "Status"],
  mods.map(p => [p.module_id, p.file.link, p.par_hours ?? "—", p.actual_hours ?? 0, `${p.competency_level ?? 0}/4`, p.status])
)
```

## Phase 3 — Advanced AI

```dataviewjs
const mods = dv.pages('"phd/modules"')
  .where(p => p.type === "module-rubric" && p.phase === 3)
  .sort(p => p.module_id, "asc")

const parSum = mods.array().reduce((s, p) => s + (p.par_hours ?? 0), 0)
const actualSum = mods.array().reduce((s, p) => s + (p.actual_hours ?? 0), 0)
dv.paragraph(`${mods.length} modules · ${parSum} par hrs · ${actualSum} actual hrs`)

dv.table(
  ["ID", "Title", "Par Hrs", "Actual", "Competency", "Status"],
  mods.map(p => [p.module_id, p.file.link, p.par_hours ?? "—", p.actual_hours ?? 0, `${p.competency_level ?? 0}/4`, p.status])
)
```

## Phase 4 — Specialized Research

```dataviewjs
const mods = dv.pages('"phd/modules"')
  .where(p => p.type === "module-rubric" && p.phase === 4)
  .sort(p => p.module_id, "asc")

const parSum = mods.array().reduce((s, p) => s + (p.par_hours ?? 0), 0)
const actualSum = mods.array().reduce((s, p) => s + (p.actual_hours ?? 0), 0)
dv.paragraph(`${mods.length} modules · ${parSum} par hrs · ${actualSum} actual hrs`)

dv.table(
  ["ID", "Title", "Par Hrs", "Actual", "Competency", "Status"],
  mods.map(p => [p.module_id, p.file.link, p.par_hours ?? "—", p.actual_hours ?? 0, `${p.competency_level ?? 0}/4`, p.status])
)
```

## Phase 5 — Thesis & Defense

```dataviewjs
const mods = dv.pages('"phd/modules"')
  .where(p => p.type === "module-rubric" && p.phase === 5)
  .sort(p => p.module_id, "asc")

const parSum = mods.array().reduce((s, p) => s + (p.par_hours ?? 0), 0)
const actualSum = mods.array().reduce((s, p) => s + (p.actual_hours ?? 0), 0)
dv.paragraph(`${mods.length} modules · ${parSum} par hrs · ${actualSum} actual hrs`)

dv.table(
  ["ID", "Title", "Par Hrs", "Actual", "Competency", "Status"],
  mods.map(p => [p.module_id, p.file.link, p.par_hours ?? "—", p.actual_hours ?? 0, `${p.competency_level ?? 0}/4`, p.status])
)
```

---

## How to log a study session

1. Open `modules/M##-name/audit.md`
2. Add a session block at the bottom:

```markdown
## Session N — YYYY-MM-DD
- **Duration:** X hrs
- **Topics covered:** ...
- **Competency reached:** [0-4]
- **Energy level:** [high / medium / low]
- **Focus quality:** [deep / moderate / scattered]
- **Blockers/questions:** ...
- **H&C connections:** ...
```

3. Update `rubric.md` frontmatter: increment `actual_hours`, update `competency_level` and `status`
4. Dataview picks up the change automatically on next render
