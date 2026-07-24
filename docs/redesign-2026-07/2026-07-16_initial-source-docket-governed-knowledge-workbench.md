---
type: research-source-docket
schema_version: "1.0"
title: "Initial Source Docket: Governed AI-Augmented Knowledge Workbench"
domain: research/knowledge-work
kind: literature-brief
status: draft
created: 2026-07-16
updated: 2026-07-16
reviewed_by: null
reviewed_at: null
review_notes: "All anchors below were directly inspected through their linked source on 2026-07-16. This is a design-direction docket, not a completed systematic literature review."
revision: 1
hub_canonical:
  artifact_id: phd-initial-source-docket-v1
  authority_class: hub-canonical-foundation
  projection_status: review-required
  authority_pointer: "See the Hub PhD research-program source using this stable artifact ID; no private local path is disclosed here."
supersedes: null
superseded_by: null
related:
  - docs/redesign-2026-07/2026-07-16_knowledge-workbench-research-redesign-plan.md
  - docs/redesign-2026-07/thesis-refocus-proposal.md
  - docs/redesign-2026-07/methodology-refinement-after-external-feedback.md
  - docs/redesign-2026-07/literature-anchor-map-for-methodology-refinement.md
  - THESIS.md
  - METHODOLOGY.md
graph_refs:
  - docs/redesign-2026-07/2026-07-16_knowledge-workbench-research-redesign-plan.md
  - docs/redesign-2026-07/2026-07-16_curriculum-crosswalk-governed-knowledge-work.md
  - https://www.w3.org/TR/prov-dm/
  - https://doi.org/10.6028/NIST.AI.600-1
  - https://doi.org/10.2753/MIS0742-1222240302
  - https://doi.org/10.1145/1240624.1240704
  - https://www.w3.org/TR/skos-reference/
  - https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
  - https://arxiv.org/abs/2309.02427
thread_refs: [T13, T37, T38]
tags:
  - literature-review
  - design-science
  - research-through-design
  - provenance
  - knowledge-organization
  - knowledge-governance
  - fair-data
  - extended-cognition
  - ai-risk-management
importance: core
llm_accessible: true
generated_by: "Virgil / source-grounded-orientation"
verified: false
citation_audit_status: "direct-source-inspected anchors; expansion and full bibliography integration pending"
---

# Initial Source Docket: Governed AI-Augmented Knowledge Workbench

## Recognition

- **Why this exists:** The thesis needs a research center that can connect Applied AI, agentic engineering, knowledge organization, provenance, cognitive scaffolding, and human agency without making any one of those fields carry claims it cannot support.
- **Where it belongs:** The July redesign packet. It supplies directly inspected anchors for the next decision, not final thesis citations or a completed systematic review.
- **What Scott should recognize:** The strongest new contribution is not "an AI that organizes notes." It is the design and evaluation of a cognitive workbench where knowledge transformations remain inspectable, governed, recoverable, and compatible with human authorship.
- **Papertrail:** Each source URL below was directly inspected on 2026-07-16. The document distinguishes what the source supports from what still needs empirical study.
- **Verification state:** Draft. All proposed thesis language and evaluation design remain subject to review and later citation audit.

## Directly inspected anchors

| Anchor | What the source establishes | Thesis use | Boundary / caveat |
|---|---|---|---|
| Moreau, L. and Missier, P., eds. (2013). *PROV-DM: The PROV Data Model*. W3C Recommendation. https://www.w3.org/TR/prov-dm/ | A domain-agnostic provenance model with entities, activities, agents, derivations, bundles, and collections. It describes provenance as information about what produced, influenced, or delivered an entity. | Reference model for tracing a knowledge artifact from source through AI or human transformations, review actions, and later revisions. | It is a provenance interchange model, not a complete interaction model, knowledge-quality model, or privacy policy. |
| Lebo, T., Sahoo, S., and McGuinness, D., eds. (2013). *PROV-O: The PROV Ontology*. W3C Recommendation. https://www.w3.org/TR/prov-o/ | An OWL2 encoding of the PROV data model that can represent and exchange provenance across systems and be specialized for application domains. | A future interoperability target if Exocore needs to export provenance. | The workbench can adopt PROV-inspired concepts without requiring RDF or a graph database in its first implementation. |
| National Institute of Standards and Technology. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1. https://doi.org/10.6028/NIST.AI.600-1 | A cross-sectoral companion profile that treats governance, content provenance, pre-deployment testing, and incident disclosure as primary GAI considerations, and organizes suggested actions around govern, map, measure, and manage. | Risk and control frame for AI-mediated synthesis, including source attribution, review gates, policy boundaries, and recovery after failures. | Voluntary risk guidance, not a claim that a workbench is safe, fair, or trustworthy merely by naming those controls. |
| Peffers, K., Tuunanen, T., Rothenberger, M. A., and Chatterjee, S. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems. https://doi.org/10.2753/MIS0742-1222240302 | A six-step design science research method: problem identification and motivation, objectives, design and development, demonstration, evaluation, and communication. | Primary research-process spine for designing and evaluating a cognitive-workbench artifact. | DSRM provides a process model. It does not specify the correct human-subject method, privacy protocol, or quality rubric for this specific artifact. |
| Zimmerman, J., Forlizzi, J., and Evenson, S. (2007). *Research through Design as a Method for Interaction Design Research in HCI*. CHI. https://doi.org/10.1145/1240624.1240704 | Artifacts can be research contributions when they address under-constrained problems, produce design exemplars, and are evaluated through explicit lenses. | Supports Exocore as an inquiry-producing design artifact rather than product proof dressed as research. | Research through design does not itself demonstrate general usability or effectiveness for a broader population. |
| ANSI/NISO Z39.19-2005 (R2010). *Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies*. https://www.niso.org/publications/ansiniso-z3919-2005-r2010 | Guidelines for controlled vocabularies used to represent content objects in knowledge organization systems, including lists, synonym rings, taxonomies, and thesauri. | Supports a deliberate taxonomy and vocabulary layer for artifact types, status terms, relationships, and policy states. | A controlled vocabulary is a semantic governance mechanism. It does not by itself solve semantic ambiguity, retrieval quality, or generative-model reliability. |
| Miles, A. and Bechhofer, S., eds. (2009). *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation. https://www.w3.org/TR/skos-reference/ | A common data model for sharing and linking knowledge-organization systems. It represents concepts, labels, hierarchies, associative relations, concept schemes, collections, and mappings across schemes. | A reference for a portable terminology and concept-scheme layer that remains distinct from the workbench's provenance and review-policy layers. | SKOS represents concepts and relationships. It does not prescribe artifact authority, temporal validity, or human approval gates. |
| DCMI Usage Board. (2020). *DCMI Metadata Terms*. DCMI Recommendation. https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ | An authoritative, extensible vocabulary of resource-description properties, classes, and encoding schemes, including creator, source, provenance, access rights, license, relation, and type. | A reference for interoperable artifact metadata and an eventual export profile that does not bind the first Exocore implementation to RDF. | Resource description is not a complete provenance graph, governance model, or knowledge representation language. |
| Sumers, T. R., Yao, S., Narasimhan, K., and Griffiths, T. L. (2023). *Cognitive Architectures for Language Agents*. arXiv:2309.02427. https://arxiv.org/abs/2309.02427 | A conceptual framework for language agents organized around memory, a structured action space, and a decision-making loop. | A useful contrast for distinguishing agent-internal memory and action design from the human-owned, provenance-aware record layer proposed for Exocore. | Preprint and agent-centered. It neither establishes a human cognitive-workbench method nor provides provenance, review, or agency-preservation controls. |
| Wilkinson, M. D. et al. (2016). *The FAIR Guiding Principles for scientific data management and stewardship*. Scientific Data, 3, 160018. https://doi.org/10.1038/sdata.2016.18 | Findability, Accessibility, Interoperability, and Reusability guide stewardship of scholarly digital objects, including algorithms, tools, and workflows as well as data. | Helps define machine- and human-readable evidence, source metadata, reproducible transformations, and reuse boundaries. | FAIR is a stewardship framework, not an account of truth, human agency, or an interface design method. |
| Clark, A. and Chalmers, D. J. (1998). *The Extended Mind*. Analysis, 58(1), 7–19. https://consc.net/papers/extended.html | Proposes active externalism and evaluates when external processes can be part of a coupled cognitive process. | Theory for asking when a workbench supports cognitive activity rather than merely generating outputs. | It does not establish that generative AI is constitutively part of anyone's mind. The thesis must investigate degrees and failures of coupling rather than assume the answer. |
| Heersmink, R. (2015). *Dimensions of Integration in Embedded and Extended Cognitive Systems*. Phenomenology and the Cognitive Sciences. https://doi.org/10.1007/s11097-014-9355-1 | A multidimensional integration framework spanning information flow, reliability, durability, trust, procedural and informational transparency, individualization, and transformation. | Candidate analytic lens for availability, reliability, transparency, trust, recovery, and individual fit in AI-supported knowledge work. | The framework is conceptual. Any operational measure in this research must be explicitly designed, tested, and qualified. |

## Recommended thesis direction

### Recommended working title

> **Governed AI-Augmented Knowledge Work: Designing and Evaluating a Provenance-Aware Cognitive Workbench**

This foregrounds the research object and contribution. It keeps Exocore as the applied artifact without turning the thesis into product promotion, and keeps neurodivergent cognitive scaffolding as a consequential design and evaluation lens.

### Two viable alternatives

1. **Human-Governed Knowledge Synthesis with AI: A Design Study of a Local-First Cognitive Workbench**
   - Stronger emphasis on source work and human approval.
   - Slightly less explicit about provenance as a technical contribution.
2. **Provenance, Agency, and AI-Supported Knowledge Work: A Cognitive Workbench Research Program**
   - Stronger bridge to cognitive science and authorship.
   - More abstract and less obviously Applied AI/engineering.

### Recommended contribution claim, deliberately bounded

> This research designs and evaluates a local-first cognitive-workbench approach in which AI-assisted knowledge transformations can remain connected to sources, responsible agents, review states, uncertainty, and recovery paths. It investigates how those mechanisms can support knowledge work while preserving human authorship and agency.

The claim does **not** say the artifact improves all knowledge work, proves an AI is an extended mind, or establishes efficacy for neurodivergent people as a population.

## Method recommendation: retain N=1, but change its job

**Recommendation:** preserve the N=1 autoethnographic record, but do not make it the single method responsible for every thesis claim.

| Method strand | What it should answer | Evidence it can legitimately produce | What it cannot establish alone |
|---|---|---|---|
| Design science research | What problem is being addressed, what artifact is proposed, how is it demonstrated and evaluated? | Traceable artifact decisions, demonstrations, evaluation plans, and design principles. | Broad adoption, population effects, or causal user outcomes. |
| Research through design | What becomes knowable by designing and reflecting through an interaction artifact? | Design exemplars, tensions, alternatives, and transferable questions. | General usability or a representative user result. |
| Longitudinal N=1 case and autoethnography | How does one researcher experience continuity, authorship, cognitive load, agency, and failure while using the workbench? | Thick description, reflexive evidence, failure cases, and generative hypotheses. | General efficacy, prevalence, or claims about all neurodivergent users. |
| Trace-based artifact analysis | Did sources, transformations, reviews, and recoveries remain legible in the artifact record? | Provenance coverage, review-path evidence, reproducible transformations, and correction records. | Subjective experience unless paired with participant report. |
| Future consent-governed external evaluation | Which patterns hold, fail, or vary for additional users and contexts? | Comparative or broader evidence, once ethics and recruitment are in place. | A substitute for the first-person account of the originating researcher. |

The N=1 record is therefore still valuable. It becomes the place where agency, authorship, cognitive load, and returnability are observed in depth. It is no longer asked to prove the entire workbench architecture or make population claims.

## Candidate research questions for the next redline

1. **Knowledge-work breakdowns:** What recurring problems arise in AI-assisted capture, organization, retrieval, comparison, and synthesis of heterogeneous evidence?
2. **Governance and provenance mechanisms:** Which artifact-level mechanisms make sources, transformations, responsible agents, review states, uncertainty, and recovery paths inspectable without creating prohibitive correction load?
3. **Cognitive-workbench use:** In a longitudinal single-case record, how do these mechanisms affect the researcher's context recovery, task startability, cognitive load, agency, and authorship? Which failure modes recur?
4. **Design principles and evaluation:** What reusable, bounded design principles and evaluation criteria follow from the workbench's iterative design, traceable use, and documented failures?

## Candidate evaluation model

These are proposed measures, not validated outcome claims.

| Dimension | Example observable | Why it matters |
|---|---|---|
| Provenance completeness | A sampled synthesized claim can be traced to its source entities, transformations, and responsible human or tool agents. | Tests whether synthesis remains inspectable. |
| Governance-path integrity | A sampled artifact's review, authority, verification, and policy states are explicit and no automated promotion bypassed the stated gate. | Tests whether governance is operational rather than rhetorical. |
| Recovery and continuity | A bounded restart task can locate the active thread, governing artifact, next action, and relevant sources with documented reconstruction effort. | Tests returnability after interruption. |
| Knowledge-work quality | A predeclared rubric assesses source relevance, claim qualification, uncertainty treatment, and correction handling for a bounded task class. | Avoids treating fluent output as a proxy for sound synthesis. |
| Agency and correction load | Subject report plus trace evidence distinguishes endorsed assistance from alienation, excessive repair, or authorship drift. | Treats human partnership and failure as first-class evidence. |

## Immediate curriculum implication

Do not delete the technical or learning spine. Keep phases as sequencing. Add cross-cutting track metadata and later module extensions for:

- knowledge representation and organization;
- evidence synthesis, argumentation, and sensemaking;
- provenance, metadata, governance, and reproducibility;
- agentic knowledge-work orchestration and verification;
- cognitive-workbench interaction, recovery, and accessibility.

The first curriculum change should be a data model and crosswalk, not a new batch of generated module prose.

## Citation and research gaps still open

1. The knowledge-management, personal knowledge management, and information-sensemaking literature needs a dedicated reviewed source bank.
2. Autoethnography, single-case, and action-research methodological anchors need a full citation audit before a canonical method chapter is changed.
3. AI-supported knowledge-work evaluation research needs a review that distinguishes retrieval, summarization, argumentation, and long-horizon work.
4. The provenance model needs a privacy and local-first threat analysis before it becomes an implementation specification.
5. No source in this docket proves a neurodivergent benefit. That remains a research question requiring ethically appropriate evidence.

## Next action

Use this docket to review the new research center, candidate questions, and method split. If Scott approves the direction, create a canonical, versioned research-program data source and a forward crosswalk before redlining `THESIS.md`, `README.md`, `AGENT.md`, `CLAUDE.md`, curriculum maps, or scripts.
