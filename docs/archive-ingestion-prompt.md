# Archive Gap-Fill Ingestion Prompt
# For: hearthandcode-archive MCP agent

**Purpose:** Ingest content for curriculum domains that are missing or thin in the archive,
prior to running the PhD curriculum multi-agent workflow.

**Required:** Archive MCP server must be running (`just up` in hearthandcode-archive/knowledge-generation)

---

## Briefing for the archive ingestion agent

You are the knowledge curation agent for the hearthandcode-archive. Your job is to fill
coverage gaps identified during a curriculum gap analysis. The archive is a self-hosted
knowledge base managed via MCP tools. You have access to `kg_plan_search`,
`kg_fetch_with_fallback`, `kg_ingest`, `kg_bulk_ingest`, `kg_loop_state`, `kg_loop_report`,
`kg_status`, `kg_domain_summary`, `kg_list_domains`, and related tools.

### What you are filling

A 66-module PhD-level curriculum in Applied AI/ML has been designed. The archive's current
coverage was graded per domain. The following domains are **D or F grade** (< 20 good resources)
and need to be filled before the curriculum content generation workflow runs:

| Domain key (to use in ingest calls) | Curriculum modules | Target resources | Priority |
|---|---|---|---|
| `machine-learning` | M19–M20 (classical ML, stat learning theory) | 80–120 | HIGH |
| `deep-learning` | M21–M25 (neural nets, CNNs, transformers, optimization) | 80–120 | HIGH |
| `reinforcement-learning` | M27–M28 (RL fundamentals, deep RL) | 50–80 | HIGH |
| `llm-foundations` | M29–M31 (LLM architecture, fine-tuning, RLHF, GenAI) | 60–100 | HIGH |
| `ai-safety-alignment` | M41, M54 (safety, red-teaming, value alignment, virtue/vice) | 40–60 | HIGH |
| `aied` | M43–M51 (AI in education, ITS, adaptive learning, assessment) | 60–100 | HIGH |
| `affective-computing` | M52–M53 (emotion modeling, computational personality) | 30–50 | HIGH |
| `ai-ethics` | M55–M56 (ethics, governance, fairness, accountability) | 40–60 | MEDIUM |
| `causal-inference` | M39 (causality in ML, do-calculus, SCMs) | 30–50 | MEDIUM |
| `adversarial-ml` | M32 (adversarial examples, robustness, attacks) | 25–40 | MEDIUM |
| `multimodal-ai` | M36–M37 (vision, speech, multimodal models) | 30–50 | MEDIUM |
| `mlops` | M60 (ML engineering, deployment, monitoring, experiment design) | 30–50 | MEDIUM |
| `cognitive-science-learning` | M58 (Piaget, Vygotsky, Bloom, cognitive load theory) | 40–60 | MEDIUM |

### What "good" resources look like per domain

For each domain, prioritize in this order:
1. **Survey papers and review articles** — these are worth 3–5 single-topic papers in terms of
   curriculum value; an agent can learn a whole field from a good survey
2. **Seminal papers** — the canonical references that every researcher cites
3. **PhD-level course notes or textbooks** (open access: MIT OCW, Stanford course pages, arXiv books)
4. **arXiv papers** from top venues (NeurIPS, ICML, ICLR, EMNLP, ACL, EDM, L@S, AIED)
5. **Technical blog posts** from Anthropic, OpenAI, DeepMind, Google Brain, Meta AI
   (only if peer-reviewed papers don't cover the topic)

Avoid: news articles, marketing content, low-quality tutorials, duplicates of what's already
in the archive, paywalled content.

### Domain-specific seeding targets

**`machine-learning`**: Start with Bishop's PRML (open access version), Murphy's PML books,
ESL (Hastie, Tibshirani, Friedman), Shalev-Shwartz & Ben-David "Understanding ML" (open).
Then add papers on PAC learning, VC dimension, kernel methods, SVMs, random forests, XGBoost.

**`deep-learning`**: Goodfellow et al. "Deep Learning" book (deeplearningbook.org), LeCun,
Bengio, Hinton 2015 Nature paper, ResNet, LSTM, Attention is All You Need, BERT, GPT-1/2.
Stanford CS231n notes (open). Fast.ai course notes.

**`reinforcement-learning`**: Sutton & Barto "RL: An Introduction" (open access),
Silver et al. DQN (2015 Nature), PPO paper, TRPO, SAC, AlphaGo/Zero papers. 
OpenAI Spinning Up documentation.

**`llm-foundations`**: "Attention Is All You Need" (Vaswani 2017), GPT-3, PaLM, Llama papers,
RLHF (Christiano 2017, InstructGPT), Constitutional AI (Bai 2022, Anthropic),
"A Survey of Large Language Models" (Zhao et al.), Chinchilla, scaling laws papers.
Anthropic, OpenAI, DeepMind technical reports (all public).

**`ai-safety-alignment`**: Russell "Human Compatible" (chapter summaries/reviews),
Hadfield-Menell CIRL paper, Amodei "Concrete Problems in AI Safety" (arXiv),
Leike et al. AI safety gridworlds, Red-teaming LLMs papers (Perez 2022),
Constitutional AI (Bai 2022), "Alignment Forum" high-quality posts (LessWrong).
Virtue ethics in AI: Shannon Vallor "Technology and the Virtues" (philosophy, check open access).

**`aied`**: EDM conference proceedings (open access at educationaldatamining.org),
L@S conference papers, AIED conference papers. Vanlehn "The Relative Effectiveness of
Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems" (2011 review),
Corbett & Anderson BKT paper, Anderson et al. ACT-R tutors, Bloom "2-sigma problem" (1984).
Self-explanation effect (Chi et al.), desirable difficulties (Bjork), spaced repetition
(Ebbinghaus, modern: Pimsleur, Anki research papers).

**`affective-computing`**: Picard "Affective Computing" (MIT Press, check open access excerpts),
Russell "A Circumplex Model of Affect" (1980), Ekman facial action coding system papers,
D'Mello et al. affect and learning papers, Baker et al. "Towards Sensor-Free Affect Detection",
Grafsgaard et al. nonverbal behavior and learning. For personality: McCrae & Costa Big Five papers,
John & Srivastava "The Big Five Trait Taxonomy" (open access handbook chapter),
Mairesse et al. "Using Linguistic Cues for the Automatic Recognition of Personality".
For virtue/vice: Haidt "Moral Foundations Theory" papers (open access), 
"Character Strengths and Virtues" (Peterson & Seligman, check excerpt availability).

**`ai-ethics`**: Floridi et al. "AI4People" principles, EU AI Act (public document),
Gebru et al. "Datasheets for Datasets", Mitchell et al. "Model Cards",
Barocas & Moritz "Fairness and ML" (fairmlbook.org — open access full text),
Noble "Algorithms of Oppression" (check open access chapters), 
ACM FAccT conference papers, Zuboff "Surveillance Capitalism" (review articles).

**`causal-inference`**: Pearl "The Book of Why" (excerpts/reviews), Pearl "Causality" (2nd ed.
freely available older edition), Peters, Janzing, Schölkopf "Elements of Causal Inference"
(open access PDF), Hernán & Robins "Causal Inference: What If" (open access),
Schölkopf "Toward Causal Representation Learning" (2021 arXiv).

**`cognitive-science-learning`**: Bloom's taxonomy original paper + revised taxonomy (Anderson
& Krathwohl 2001), Vygotsky "Zone of Proximal Development" (excerpts/summaries in open journals),
Piaget cognitive development stages (review articles), Sweller "Cognitive Load Theory in
Instructional Design" (1994, 2010 reviews), Bransford "How People Learn" (open access 2nd ed.),
Ambrose "How Learning Works" (chapter summaries), Bjork desirable difficulties, 
Roediger "The Power of Testing Memory" (2006).

**`mlops`**: "Machine Learning Engineering" (Burkov, free online), Sculley et al. "Hidden
Technical Debt in Machine Learning Systems" (Google, 2015 NeurIPS — very important),
Breck et al. "The ML Test Score" (Google), "Responsible AI Practices" (Google AI),
Martin Fowler "Continuous Delivery for ML" blog posts, Huyen "Designing ML Systems" excerpts.

### How to execute

Use the archive's loop/iteration pattern:

**Step 1 — Baseline check**
```
kg_list_domains()           # See what domains currently exist
kg_domain_summary(domain)   # For each gap domain, check what's there already
kg_loop_state()             # Check current loop state — don't duplicate work
```

**Step 2 — For each HIGH-priority domain (run these first, in parallel if possible):**
```
kg_plan_search(
  topic="[domain topic and subtopics]",
  domain="[domain key]",
  target_count=[target from table above],
  search_strategy="survey_first"   # prioritize surveys and seminal papers
)
```
This generates a search plan. Execute the plan by:
1. Running the searches via `kg_fetch_with_fallback` for each planned query
2. Queuing found URLs via `kg_bulk_ingest(urls=[...], domain="[domain key]")`
3. Monitoring with `kg_status()` until the queue drains

**Step 3 — Loop until coverage thresholds are met**
After each ingestion pass:
```
kg_loop_report(domain="[domain key]")  # Check coverage %
kg_loop_state()                        # Update loop state with progress
```
Repeat Step 2 for a domain if coverage is still below target.
Termination condition: all HIGH-priority domains have ≥ 60 resources ingested;
all MEDIUM-priority domains have ≥ 25 resources ingested.

**Step 4 — Quality check**
After ingestion:
```
kg_evaluate_resources(domain="[domain key]", top_n=20)
```
For any domain where the top-20 resources score poorly, flag them for manual review.

**Step 5 — Generate domain summaries**
```
kg_domain_summary(domain="[domain key]")    # for each filled domain
kg_research_report(topic="[thesis RQ]")    # optional: generate a pre-workflow research brief
```

### Looping protocol

- Run passes in this order: HIGH-priority domains first, MEDIUM second
- Between each full-domain pass, check `kg_budget_status()` — do not exceed daily provider limits
- If a domain is not filling well (< 10 results per search), try alternative query terms:
  - `machine-learning` → try "statistical learning theory", "supervised learning survey"
  - `aied` → try "intelligent tutoring systems", "educational data mining", "learning analytics"
  - `affective-computing` → try "emotion recognition machine learning", "affect-aware tutoring"
- Pause with `kg_pause()` if rate-limited; resume with `kg_resume()` after cooldown
- Log each domain's final resource count and average quality score to loop state

### Completion report

When all domains have hit their targets (or you've exhausted provider capacity for the day),
generate a completion report:
```
kg_loop_report()            # full coverage report across all domains
kg_diff(since="[start date of this session]")   # what was added
```
Return the report to the orchestrating session so the curriculum workflow can proceed.

---

*This prompt is used to brief the archive MCP agent. Feed it as the prompt in a Claude Code
session running against the hearthandcode-archive MCP server. The archive server must be
running (`just up`) before starting.*
