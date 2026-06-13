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

## License and contributions

This curriculum is licensed under [CC BY-NC-SA 4.0](LICENSE). You can share and adapt it
freely for non-commercial purposes, as long as you give attribution and license your
adaptations under the same terms.

**The copyright holder (Scott Rallya) retains commercial rights** — including the right
to incorporate this curriculum into the Hearth & Code platform. Forks may not be used
commercially without written permission.

**Contributor License Agreement (plain language):** By submitting a pull request, you
grant Scott Rallya / Hearth & Code the right to include your contribution in commercial
products (such as the H&C platform), in addition to the standard CC BY-NC-SA 4.0 terms.
You keep your copyright; you just also grant commercial use rights to the repository owner.
This is a standard CLA structure for dual-licensed open-source projects. If you don't want
to grant commercial use rights, open an issue instead of a PR — contributions via issue
discussion are also welcome.

Full license terms in [LICENSE](LICENSE).

---

## Repo structure

```
phd-applied-ai/
├── CLAUDE.md           — context for Claude Code sessions
├── THESIS.md           — thesis statement, research questions, abstract
├── AUDIT_LOG.md        — master study session log
├── SCORECARD.md        — par vs. actual hours by module
├── POSTS.md            — index of published Substack posts
├── PERSONA.md          — learner profile (generated at M61)
├── docs/
│   ├── spec.md         — master curriculum spec
│   ├── frontmatter-schema.md
│   └── archive-ingestion-prompt.md
├── committee/          — 5 advisory personas with system prompts
├── curriculum/         — phase overviews and module registry
├── modules/            — M01–M67, one directory each
├── exams/              — qualifying exam artifacts
├── defense/            — defense transcript and committee feedback
├── portfolio/          — H&C-connected project index
└── bibliography/       — master.bib
```

---

*Built with [Hearth & Code](https://hearthandcode.dev) · [Substack](https://hearthandcode.substack.com) · [GitHub](https://github.com/hearthandcode)*
