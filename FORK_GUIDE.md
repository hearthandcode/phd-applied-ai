---
type: guide
audience: fork
---

# Fork Guide: Adapt This Curriculum for Your Research

This curriculum is designed to be genuinely forkable. Phases 0–3 (42 of 67 modules)
cover universal doctoral-level content: math, CS theory, ML, and advanced AI. These
modules work for any research focus. Scott's thesis is tied to
[Hearth & Code](https://hearthandcode.dev), but that connection lives in isolated
`project/hc-connection.md` files — not in the theory or rubrics.

---

## What's generic vs. what's personal

| Content | Status | Fork action |
|---|---|---|
| Phase 0–1 (M01–M18): Math + CS theory | Generic | Keep as-is |
| Phase 2–3 (M19–M42): ML + Advanced AI | Generic | Keep; theory.md is generic by design |
| Phase 4 (M43–M61): Specialized Research | Mixed | Replace domain modules with yours |
| Phase 5 (M62–M67): Thesis | Personal | Replace entirely |
| `theory.md` files | Generic | Keep; add to, don't embed your project here |
| `project/README.md` files | Generic | Keep; the deliverables are universal |
| `project/hc-connection.md` files | H&C-specific | **Replace with your project connection** |
| `THESIS.md` | H&C-specific | **Replace with your thesis** |
| `committee/` personas | Generic archetypes | Keep, or replace with domain specialists |
| `sessions/` | Personal data | Clear before sharing publicly |
| `AUDIT_LOG.md` | Personal data | Clear before sharing publicly |
| `SCORECARD.md` | Personal data | Reset actual hours to 0 or `—` |

---

## Step 1: Fork on GitHub

Click **Fork** on `github.com/hearthandcode/phd-applied-ai`. Clone your fork.

```bash
git clone git@github.com:YOUR_USERNAME/phd-applied-ai.git
cd phd-applied-ai
```

---

## Step 2: Update THESIS.md

Replace the thesis statement, research questions, and abstract with your own. You don't
need a complete thesis to start — a working hypothesis is enough.

The thesis shapes what you write in `project/hc-connection.md` for each module, but it
doesn't affect theory.md, rubrics, or the reading lists.

---

## Step 3: Decide on the committee

The five advisors (Chen, Kowalski, Williams, Okonkwo, Patel) are generic academic
archetypes calibrated to the OCEAN personality model. They work for any AI/ML research focus.

**Keep them if:** your research is in AI/ML, learning systems, ethics, or systems engineering.
The PERSONA.md files are self-contained system prompts — paste them into any AI model.

**Replace them if:** your research is in a different domain. Copy one `PERSONA.md` as a
template. Update the name, institution, specialization, OCEAN scores, virtues, and vices.
The format is designed for this.

---

## Step 4: Clear personal data

Replace these files before making your fork public:

```bash
# Clear session logs (keep the example)
rm -rf sessions/2026/
# Optionally keep sessions/EXAMPLE-session-template.md as reference

# Reset SCORECARD actual hours
# Edit SCORECARD.md: set all "Actual" columns to 0 or "—"

# Reset AUDIT_LOG.md
# Keep the schema header and index columns; delete the entry rows
```

---

## Step 5: Review the module list

**Phases 0–3 (M01–M42): Keep.** Universal for any AI/ML researcher. Linear algebra,
probability, computability, algorithms, classical ML, neural networks, LLMs, safety,
RAG, multi-agent systems — these are the foundation regardless of your thesis.

**Phase 4 (M43–M61): Customize.** Scott's domain is AIED, pedagogy, neurodiversity,
gamification. Replace the modules that don't fit your research with your own specialized
topics. To add a module:
1. Copy any existing module directory as a template
2. Update `theory.md` front matter: module ID, title, tags, par hours, phase
3. Add it to `curriculum/overview.md`
4. Add a row to `SCORECARD.md`

**Phase 5 (M62–M67): Replace.** These are tied to Scott's thesis. Use the structure
(methodology, literature review, proposal, draft, revision, defense) but replace the
content with your own research arc.

---

## Step 6: Understand the per-module file structure

```
modules/MXX-slug/
├── theory.md           — GENERIC: doctoral content, usable by anyone
├── rubric.md           — competency levels (generic, keep as-is)
├── reading-list.md     — papers/books (generic, extend freely)
├── resources.md        — supplementary links
├── audit.md            — YOUR study sessions (empty, start logging)
├── blog-post-seed.md   — for your writing
└── project/
    ├── README.md       — generic project deliverable (keep)
    └── hc-connection.md — H&C-specific (REPLACE with yours)
```

The key fork action per module: **replace `project/hc-connection.md`** with a file
explaining how the module connects to your own research project.

---

## Step 7: Generate Phase B content

Run Phase B content generation (Phase A scaffold is already complete):

```bash
# Claude Code
/generate-phase B

# Or one module at a time:
/generate-module M01
```

The generation prompts produce generic theory.md content and separate
`project/hc-connection.md` files for project-specific connections.

See `docs/manual-workflow.md` for model-agnostic instructions using any AI tool.

---

## Step 8: Write your project/hc-connection.md files

After generation, each module has an `hc-connection.md` with Scott's H&C context.
Replace with your own:

```markdown
# [Module Title] — [Your Project] Connection

## How this module connects to [Your Project Name]

[2–4 paragraphs explaining the connection]

## Specific applications

- [Application 1]
- [Application 2]

## Research questions this module informs

- RQ[X]: [Your relevant research question]
```

You can do this as you study each module rather than all at once.

---

## Step 9: Start studying

Nothing else needs configuration before you start. Open any `theory.md` and read.

The committee, rubrics, skills, and session log format all work out of the box.
Use `.claude/commands/` skills (Claude Code) or `AGENT.md` prompts (any AI tool).

The par score system applies to your fork too: par is aspirational hours, not a deadline.
Over par means you went deep. Under par means you moved fast. Neither is wrong.

---

## Step 10: License your fork

This curriculum is CC BY-NC-SA 4.0. Your fork must also be CC BY-NC-SA 4.0 (ShareAlike
requirement). You may not apply a more restrictive license.

**Attribution required in your fork's README:**
> Based on phd-applied-ai by Scott Rallya / Hearth & Code
> (github.com/hearthandcode/phd-applied-ai), CC BY-NC-SA 4.0

If you submit improvements back upstream via PR, see the LICENSE file for contribution terms.

---

## Questions

Open an issue at `github.com/hearthandcode/phd-applied-ai/issues` or reach out at
[hearthandcode.dev](https://hearthandcode.dev).
