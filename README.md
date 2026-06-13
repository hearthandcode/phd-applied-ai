# phd-applied-ai

**A self-directed, AI-assisted doctoral curriculum in Applied AI and Machine Learning.**

Fully documented in public: 67 modules, a working thesis, five advisory personas, qualifying
exams, and a simulated PhD defense. Study logs, mastery rubrics, and personal audit data
published as-is — including energy levels, focus quality, and the realities of learning while
managing ADHD and bipolar disorder.

The thesis is tied to [Hearth & Code](https://hearthandcode.dev) — a gamified, AI-native
educational platform. This curriculum is simultaneously the course of study and the proof
of concept.

---

## The thesis

**Adaptive AI-Native Learning Systems: Architecture, Pedagogy, and Ethics of a
Next-Generation Educational Platform**

Five research questions:
1. How can adaptive AI systems model learner competency trajectories in real time?
2. What pedagogical frameworks work best when mediated by generative AI tutors?
3. Can computational virtue/vice models improve motivation and learning outcomes?
4. What governance structures are needed for AI that assesses individual learners at scale?
5. How does a neurodiverse learner's personal characteristics shape their trajectory through
   AI-mediated study — and what design principles follow from five years of that data?

---

## Curriculum structure

| Phase | Modules | Focus |
|---|---|---|
| 0 — Mathematical Foundations | M01–M06 | Linear algebra, probability, optimization, information theory |
| 1 — CS Fundamentals | M07–M18 | Computability, algorithms, PLT, type theory, systems, architecture |
| 2 — ML Foundations | M19–M28 | Classical ML, neural networks, deep learning, reinforcement learning |
| 3 — Advanced AI | M29–M42 | LLMs, generative models, adversarial ML, RAG, multi-agent, safety |
| 4 — Specialized Research | M43–M61 | AIED, pedagogy, affective computing, virtue/vice modeling, ethics, gamification, neurodiversity |
| 5 — Thesis & Defense | M62–M67 | Research methodology, literature review, proposal, dissertation, defense |

Each module produces: a doctoral-level theory digest, a working code project, a mastery
rubric with a "par score," a dated study log, an annotated reading list, and a blog post
seed that becomes a [Substack post](https://hearthandcode.substack.com).

---

## The committee

Five advisory personas — each with a full academic profile, OCEAN personality model, specific
virtues and vices, and a Claude system prompt. Available for advisory consultation throughout
the curriculum and as examiners at the final defense.

| Name | Role | Virtue | Vice |
|---|---|---|---|
| Dr. Mei-Lin Chen | ML Theory (Stanford) | Intellectual rigor | Perfectionism |
| Dr. Aleksander Kowalski | Systems/Architecture (CMU) | Pragmatism | Impatience with theory |
| Dr. Amara Williams | Education/Pedagogy (MIT Media Lab) | Empathy for learners | Hype susceptibility |
| Dr. Chukwuemeka Okonkwo | AI Ethics (Oxford) | Justice | Moralism |
| Dr. Priya Patel | Industry/Applied AI | Execution focus | Short-termism |

See `committee/` for full profiles and system prompts.

---

## Progress tracking

| Artifact | Status |
|---|---|
| Spec and design decisions | Complete (`docs/spec.md`, locked v2.1) |
| Committee profiles | Complete (`committee/`) |
| Curriculum module scaffolding | Complete — 67 modules scaffolded (Phase A, commit 277b1a0) |
| Module content (Phase 0–1) | Pending — Phase B generation next |
| Studying begun | Not yet |
| Blog posts published | 0 |

This repo grows over 5–6 years. Check `AUDIT_LOG.md` for the full session history and
`SCORECARD.md` for par vs. actual hours across all modules.

---

## How to use this repo

**Follow the curriculum:** Every module in `modules/` is self-contained — theory, project,
rubric, and reading list. You don't need to follow it in order, though the modules have
prerequisites noted.

**Fork and adapt:** Phases 0–3 (42 modules) are completely generic — math, CS theory,
ML, and advanced AI applicable to any research focus. The thesis-specific connections
are isolated in `project/hc-connection.md` files so they don't pollute the theory.
See **[FORK_GUIDE.md](FORK_GUIDE.md)** for a step-by-step guide to adapting this
curriculum for your own research.

**Contribute:** If you complete a module and have better project ideas, more accurate theory,
or improved rubric questions — open a PR. See the license section below for contribution terms.

**Follow along:** Module completions are announced on
[Hearth & Code Substack](https://hearthandcode.substack.com). Each post is a reflection on
what was studied, how it changes what I'm building, and what it's actually like to do this.

---

## Transparency

**What this project is.** This is Scott Rallya's personal doctoral research record,
published in full as an open curriculum. It is simultaneously a self-directed study
program, a longitudinal research data collection effort (RQ5), and a proof-of-concept
for the Hearth & Code platform. Following along, studying from it, and forking it are
explicitly encouraged — but the primary audience is the researcher and subject (Scott).

**How AI is used.** AI tools (primarily Claude, via Claude Code) generate initial module
content (theory.md, reading lists, project specs), conduct committee advisory sessions,
and generate clinical descriptions of session logs from self-report interview data. All
AI-generated session log narratives are reviewed, edited where necessary, and personally
verified by Scott before being considered part of the research record. All AI-generated
module content is study material, not a citation source — the reading lists point to real
papers that get read and evaluated independently.

**What contributing means in practice.** By submitting a pull request, you grant Scott
Rallya / Hearth & Code the right to include your contribution in commercial products,
in addition to the standard CC BY-NC-SA 4.0 terms. This means your contribution could
become part of the Hearth & Code platform. This is a standard Contributor License
Agreement (CLA) structure. It is intentional and disclosed upfront because it matters.
If you are not comfortable granting commercial use rights, open an issue instead — that
is a fully welcome form of contribution that does not involve the CLA.

**Session logs and personal data.** Session logs contain self-reported psychological
data (mood, energy, focus, cognitive load, medication notes) and are part of the RQ5
longitudinal dataset. They are personally verified by Scott before being committed. The
process for creating and verifying them is documented in
[docs/session-log-process.md](docs/session-log-process.md).

---

## License

This curriculum is licensed under [CC BY-NC-SA 4.0](LICENSE). You can share and adapt
it freely for non-commercial purposes with attribution, under the same license terms.

The copyright holder (Scott Rallya) retains commercial rights, including the right to
incorporate this curriculum into the Hearth & Code platform. Full terms in [LICENSE](LICENSE).

---

## Processes

**Session logging** — Conducted collaboratively with an AI assistant (or solo). The
process: describe your session → AI generates clinical/research description → you review
and edit → you verify and sign off → commit. Full process:
[docs/session-log-process.md](docs/session-log-process.md).

**Module content generation** — AI generates from module front matter context and archive
search. Human reviews before studying from it. Process: [docs/manual-workflow.md](docs/manual-workflow.md).

**Changes** — All significant changes logged in [CHANGELOG.md](CHANGELOG.md).

**Spec changes** — `docs/spec.md` is locked at v2.1. Changes require a
`workspace/decisions.md` entry in hearthandcode-hub before implementation.

---

## Repo structure

```
phd-applied-ai/
├── CLAUDE.md               — context for Claude Code sessions
├── AGENT.md                — tool-agnostic context for any AI assistant
├── CHANGELOG.md            — history of significant changes
├── FORK_GUIDE.md           — how to adapt this curriculum for your research
├── THESIS.md               — thesis statement, research questions, abstract
├── AUDIT_LOG.md            — master session index (lightweight; full logs in sessions/)
├── SCORECARD.md            — par vs. actual hours by module
├── POSTS.md                — index of published Substack posts
├── PERSONA.md              — learner profile (populated at M61)
├── docs/
│   ├── spec.md             — master curriculum spec (locked v2.1)
│   ├── frontmatter-schema.md
│   ├── session-log-process.md  — process for collaborative session logging + verification
│   ├── manual-workflow.md  — copy-paste generation prompts for any AI model
│   └── archive-ingestion-prompt.md
├── sessions/               — date-based session logs (YYYY/MM/YYYY-MM-DD.md)
│   ├── README.md           — session log format and YAML schema
│   └── reviews/            — weekly review logs
├── committee/              — 5 advisory personas with system prompts
├── curriculum/             — phase overviews and module registry
├── modules/                — M01–M67, one directory each
├── exams/                  — qualifying exam artifacts
├── defense/                — defense transcript and committee feedback
├── portfolio/              — H&C-connected project index
└── bibliography/           — master.bib
```

---

*Built with [Hearth & Code](https://hearthandcode.dev) · [Substack](https://hearthandcode.substack.com) · [GitHub](https://github.com/hearthandcode)*
