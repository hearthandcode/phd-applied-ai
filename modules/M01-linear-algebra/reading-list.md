---
type: reading-list
schema_version: "1.0"
module_id: M01
module_title: "Linear Algebra for ML"
created: 2026-06-13
updated: 2026-06-14
status: active
---

# M01: Linear Algebra for ML — Reading List

**Access philosophy:** Tier 1 (Free & Open Access) is the required reading path. No learner
should be blocked by cost. Tier 2 resources require a library card but no purchase. Tier 3
texts are cited for academic completeness — every concept they cover is addressable from Tier 1.

---

## Tier 1 — Free and open access

*Start here. Complete a module with these resources alone.*

### Courses and lecture materials

**MIT 18.06SC Linear Algebra — Gilbert Strang (full OCW course)**
`ocw.mit.edu/18-06sc-linear-algebra-fall-2011/`
The gold standard. Full lecture videos, problem sets, and exams. Strang's geometric approach —
four fundamental subspaces, orthogonality, SVD — is the calibration target for this module's
theory and examples. Videos for the relevant sections map directly to theory.md §§1–8.

**MIT 18.065 Matrix Methods in Data Analysis, Signal Processing, and ML — Gilbert Strang**
`ocw.mit.edu/18-065-matrix-methods`
The explicit bridge from linear algebra to machine learning: SVD, low-rank approximations,
deep learning geometry. A direct complement to 18.06 for ML applications. Lectures 1–12 are
directly relevant to M01.

**3Blue1Brown — Essence of Linear Algebra (playlist)**
`youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab`
Sixteen short videos building geometric intuition for every core concept in this module.
Watch the full playlist before or alongside the formal theory — the visual models anchor the
symbols to spatial meaning.

### Textbooks (free from authors or open license)

**Axler, S. (2024). *Linear Algebra Done Right* (4th ed.)**
`linear.axler.net` — Free PDF from the author.
The rigorous abstract treatment: vector spaces defined without determinants, the spectral theorem
proved from first principles. Builds proof fluency and explains *why* results hold. Work through
this alongside 18.06; the two are complementary rather than redundant.

**Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning* — Chapter 2: Linear Algebra**
`deeplearningbook.org/contents/linear_algebra.html` — Free from the authors.
A concise treatment written specifically for ML practitioners. Covers scalars, vectors, matrices,
tensors, matrix operations, eigendecomposition, and SVD from a machine learning perspective.
Read this for the applied framing before the formal theory in 18.06.

**The Matrix Cookbook — Petersen & Pedersen (2012)**
`math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf` — Free PDF.
The reference card for matrix identities, derivatives, and decompositions. Not a textbook —
use it the way you use a symbol table. Pin it open while working through exercises.

### Key papers (arXiv — all free)

**Hu, E. J., et al. (2021). LoRA: Low-rank adaptation of large language models.**
`arxiv.org/abs/2106.09685`
Introduces Low-Rank Adaptation ($\Delta W = BA$ with $\text{rank}(BA) = r \ll d$). The
theoretical justification is the Eckart-Young low-rank approximation theorem from theory.md §7.
The most widely deployed application of SVD in production ML systems.

**Aghajanyan, A., Zettlemoyer, L., & Gupta, S. (2021). Intrinsic dimensionality explains the effectiveness of language model fine-tuning.**
`arxiv.org/abs/2012.13255`
Demonstrates that LLM fine-tuning constrains to a surprisingly low-dimensional subspace.
The analysis is a direct application of rank and SVD concepts; the empirical precursor to LoRA.

**Halko, N., Martinsson, P.-G., & Tropp, J. A. (2011). Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions.**
`arxiv.org/abs/0909.4061`
The foundational paper for randomized SVD — the algorithm used in practice when exact SVD is
too slow for large matrices. Connects to the open problems section of theory.md and is
essential background for M42.

---

## Tier 2 — Library accessible

*Available through most public library systems via Libby, hoopla, or university proxy.
No purchase required with a library card.*

**Strang, G. (2023). *Introduction to Linear Algebra* (6th ed.). Wellesley-Cambridge Press.**
The companion text to the 18.06 OCW course. Chapters 1–7 cover the core; Chapter 11 connects
to ML. Useful if you prefer structured text to video, but the OCW alone is sufficient.

**Strang, G. (2019). *Linear Algebra and Learning from Data*. Wellesley-Cambridge Press.**
Strang's explicit bridge from linear algebra to deep learning, statistics, and optimization.
Chapters on SVD, low-rank approximations, and neural network geometry are directly prerequisite
for Phases 2 and 3 of this curriculum.

---

## Tier 3 — Reference only (paywalled)

*Cited for academic completeness. No learner is expected to purchase these.
Access via university library or institutional subscription if available.*

**Horn, R. A., & Johnson, C. R. (2012). *Matrix Analysis* (2nd ed.). Cambridge University Press.**
Graduate-level reference for matrix theory. The chapters on eigenvalues, singular values, norms,
and positive semidefinite matrices are encyclopedic and proof-complete. Use when proof sketches
in theory.md need rigorous completion, or when matrix inequalities appear in later modules.

**Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
The definitive text on how linear algebra theory is actually computed in floating-point. The
chapters on QR, SVD algorithms, and condition numbers explain why `numpy.linalg.svd` differs
from a naive eigendecomposition — directly relevant to `verify_svd.py` in the M01 project.

---

## Archive documents

> **Note:** The following documents are in the `hearthandcode-archive` knowledge base, which
> is a **private repository** and not publicly accessible. These entries are included for the
> author's reference only. External learners should rely on Tier 1–2 resources above.

- **docs/open-library/type-theory/zoomnotes-for-linear-algebra.md** — ZoomNotes for Linear Algebra. Vector spaces, matrices, and related concepts.
- **docs/open-library/type-theory/es1803-s24-reading-topic-13-linear-algebra-vector-spaces-matrices-and-linearity.md** — ES.1803 S24: Linear Algebra: Vector Spaces, Matrices and Linearity. MIT differential equations course reading on linear algebra foundational topics relevant to ML.
- **docs/open-library/algorithms/algorithmic-aspects-of-machine-learning-textbook.md** — Algorithmic Aspects of Machine Learning, Textbook. Algorithmic and linear-algebraic underpinnings of ML including matrix methods.
- **docs/open-library/deep-learning/lecture-27-backpropagation-find-partial-derivatives-matrix-methods-in-data-analy.md** — Lecture 27: Backpropagation: Find Partial Derivatives | Matrix Methods in Data Analysis, Signal Processing, and Machine Learning. MIT 18.065 lecture connecting matrix methods to ML.
- **docs/open-library/computability/15-859n-spectral-graph-theory-and-numerical-linear-algebra-fall-2011.md** — 15-859N: Spectral Graph Theory and Numerical Linear Algebra, Fall 2011. CMU course bridging numerical linear algebra and spectral methods.
