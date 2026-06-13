---
type: hc-connection
schema_version: "1.0"
module_id: M01
module_title: "Linear Algebra for ML"
created: 2026-06-13
updated: 2026-06-13
---

# M01: Linear Algebra for ML — Hearth & Code Connection

This file maps the linear-algebraic concepts from M01 to specific design problems in the Hearth & Code (H&C) adaptive learning platform. It is the only file in this module where H&C-specific content belongs.

---

## Why linear algebra is load-bearing for H&C

H&C is, at its mathematical core, a system that represents learner state as a vector, evolves that vector as evidence accumulates, and uses the geometry of a high-dimensional knowledge space to make instructional decisions. Every significant component of the platform — the knowledge graph, the competency model, the content embedding layer, the item difficulty model — depends on linear-algebraic structure. M01 is therefore not background math; it is direct prerequisite for designing and reasoning about the platform's most critical subsystems.

---

## Specific H&C applications

### 1. Learner state as a vector in competency space

The H&C adaptive engine models each learner's current competency as a vector $\theta_t \in \mathbb{R}^K$ where $K$ is the number of knowledge components (KCs) in the curriculum. Each coordinate $\theta_{t,k}$ represents estimated mastery of KC $k$ at time $t$.

This representation is only coherent if the underlying space has the structure of a vector space — which requires the notion of dimension, basis (the choice of KCs), and linear independence (that the KCs are genuinely distinct skills, not redundant). The rank-nullity theorem from M01 tells us that if our KC decomposition is linearly dependent, the effective dimensionality of the learner-state space is lower than $K$, and we are wasting representational capacity. Designing a KC taxonomy that is approximately linearly independent is therefore a concrete engineering criterion, not an abstract mathematical nicety.

**RQ1 connection:** Adaptive competency modeling (RQ1) requires a precise answer to the question "what space does $\theta_t$ live in?" The linear-algebraic foundations from M01 are what make that question answerable with formalism.

### 2. Concept embeddings and the knowledge graph

H&C's knowledge graph maps concepts, learning objectives, prerequisites, and resources into a shared embedding space. Embedding-based methods (e.g., node2vec, knowledge graph embeddings, or the output layer of a transformer trained on curriculum text) produce concept vectors $c_i \in \mathbb{R}^d$.

The inner product $\langle c_i, c_j \rangle$ measures semantic similarity — a direct application of the inner product geometry from M01 §2. More practically:

- **Prerequisite detection:** If concept $j$ is a prerequisite of concept $i$, the vector $c_j$ should be "closer" to $c_i$ along some direction than random. Identifying these directions requires PCA or SVD over the concept co-occurrence matrix.
- **Clustering similar concepts:** Low-rank approximation of the concept-concept similarity matrix (via SVD) compresses the knowledge graph into a smaller set of latent topic axes, enabling the engine to group related concepts without manual ontology engineering.
- **Gap detection:** The column space of the concept matrix determines which directions in embedding space are actually covered by the curriculum. The null space identifies "conceptual gaps" — directions that have no current content.

### 3. Item difficulty modeling via matrix factorization

A central data structure in H&C is the learner-item response matrix $R \in \mathbb{R}^{N \times M}$ where $R_{ij}$ is learner $i$'s score on item $j$ (or missing if not yet attempted). This matrix is sparse and incomplete. Item Response Theory (IRT) can be expressed as a structured matrix factorization: $R \approx f(\Theta \cdot B^\top)$ where $\Theta \in \mathbb{R}^{N \times K}$ is the learner ability matrix, $B \in \mathbb{R}^{M \times K}$ is the item parameter matrix, and $f$ is a link function (e.g., logistic).

The SVD (and its probabilistic variant, probabilistic matrix factorization) is the natural starting point for initializing $\Theta$ and $B$ from observed data. The Eckart-Young theorem (M01 §4.2) tells us the optimal rank-$K$ initialization: it minimizes reconstruction error on observed entries before the link function is applied.

The image compression project in `README.md` is a deliberate analogue: an image is a matrix, pixels are "response entries," and finding the knee in the singular value spectrum corresponds exactly to choosing the right number of latent dimensions $K$ for the learner model. Building intuition about this tradeoff on images — where the ground truth is visually legible — transfers directly to the less visually interpretable setting of learner-item matrices.

### 4. Learner trajectory as a sequence in latent space

Over time, a learner's competency vector $\theta_t$ traces a trajectory. If we stack $T$ observations into a matrix $\Theta_{\text{traj}} \in \mathbb{R}^{T \times K}$, the SVD of this trajectory matrix reveals:
- The dominant "modes" of learning (the left singular vectors $u_i$ are basis patterns of how competency evolves over time)
- The principal directions of growth across skills (the right singular vectors $v_i$ are the skill-bundle combinations that change together)

This decomposition is the foundation for trajectory-based learner modeling and for identifying when a learner is "stuck" in a low-dimensional subspace (i.e., the effective rank of $\Theta_{\text{traj}}$ is low) — a potential signal for the engine to diversify content.

**RQ5 connection:** The autoethnographic research (RQ5) will produce a longitudinal $\theta_t$ trajectory for a single neurodiverse learner. Analyzing the structure of that trajectory using SVD-based methods is one concrete analytical technique. The condition number of the trajectory matrix, for instance, may correlate with energy cycles and cognitive variability documented in the audit log.

---

## Research question mapping

| RQ | How M01 contributes |
|---|---|
| **RQ1** — Adaptive competency modeling | KC space dimensionality, learner state vectors, matrix factorization for IRT initialization |
| **RQ2** — Pedagogy and generative AI | Less direct; reappears in M23 (attention mechanisms) and M33 (RAG retrieval using cosine similarity in embedding space) |
| **RQ3** — Virtue, vice, and learner motivation | Indirect; motivational state could be encoded as an additional component of $\theta_t$, but this is more M52/M53 territory |
| **RQ4** — Governance and ethics at scale | Fairness auditing of learner models often uses matrix decomposition to detect bias directions in embedding space |
| **RQ5** — Neurodiversity and AI-mediated learning | SVD of the longitudinal competency trajectory as an analytical tool for the autoethnographic dataset |

---

## Design principle emerging from M01

> **Principle:** Choose the dimensionality of every H&C latent space empirically, by examining the singular value spectrum of real data matrices, not by architectural intuition alone. The knee in the spectrum is an observable quantity that constrains the design.

This principle applies to KC taxonomy size, knowledge graph embedding dimension, and item difficulty model rank. It is testable: if the singular values decay slowly (no clear knee), the latent structure is not well-captured by the chosen factorization, and either the data is noisy or the representation is wrong.
