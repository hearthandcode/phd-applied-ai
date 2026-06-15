---
type: ideas-log
domain: curriculum
---

# Curriculum Design Ideas Log

Observations about what works, what doesn't, what to add or change — noticed while studying,
running exercises, or reflecting on session structure. Feed these into generation spec updates
or module patches.

---

### [2026-06-14 ~19:55] Side-conversation capture during learning sessions — the "ideas in tangent" problem

**Domain:** curriculum
**Source:** M01 learning session setup
**Trigger:** Observation that engaging with material prompts side thoughts that don't belong in the session log or learning interaction record

Studying a concept frequently surfaces questions and ideas that are adjacent to the material rather than about it. A learner studying Fields might ask about the ethics of research methodology. A learner studying Vector Spaces might get an idea for a platform feature. These are valuable — they're signs of active engagement and cross-domain thinking — but they interrupt flow if not captured quickly and filed.

The ideas log (this system) is the solution. The design question: should the skill `/study-idea` be invocable mid-session without breaking conversation context? Answer: yes, it should append an entry and immediately return to the session without requiring a response.

**Follow-up needed:** no — system is built
**Related:** `/study-idea` skill, learning session design, engagement tracking

---

### [2026-06-14 ~20:19] Jupyter ↔ Claude bridge for learning sessions

**Domain:** curriculum
**Source:** M01 learning session — LaTeX rendering question
**Trigger:** Native LaTeX doesn't render in Claude Code CLI; Jupyter renders it natively

Design: IPython cell magic (`%%claude`) that sends cells to Claude via Anthropic SDK, renders responses as Markdown (LaTeX included), feeds code execution output back to Claude as tool results. Project context injected at notebook startup from CLAUDE.md + memory files — replicating Claude Code's project awareness inside Jupyter.

Result: a single interface with rendered math, live code execution, and maintained conversation context. Ideal learning session environment for math-heavy modules like M01–M06.

Build location: `tools/jupyter-bridge/` in hearthandcode-hub. Should ship alongside the curriculum so forkers can use it. Needs: `anthropic` SDK, IPython magics, `IPython.display.Markdown`. ~1–2 focused sessions to build.

**Follow-up needed:** yes — open a thread (T19?) for this build
**Related:** T18 (Research Radar MCP — similar SDK + tool pattern), M01 learning session workflow

---
