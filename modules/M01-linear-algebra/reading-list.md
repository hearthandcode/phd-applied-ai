---
type: reading-list
schema_version: "1.0"
module_id: M01
module_title: "Linear Algebra for ML"
created: 2026-06-13
updated: 2026-06-13
status: generated
---

# M01: Linear Algebra for ML — Reading List

---

## Archive documents (identified in Phase A)

- **docs/open-library/type-theory/zoomnotes-for-linear-algebra.md** — ZoomNotes for Linear Algebra. Direct linear algebra lecture notes covering vector spaces, matrices, and related concepts.
- **docs/open-library/type-theory/es1803-s24-reading-topic-13-linear-algebra-vector-spaces-matrices-and-linearity.md** — ES.1803 S24: Linear Algebra: Vector Spaces, Matrices and Linearity. MIT differential equations course reading on linear algebra foundational topics relevant to ML.
- **docs/open-library/algorithms/algorithmic-aspects-of-machine-learning-textbook.md** — Algorithmic Aspects of Machine Learning, Textbook. Textbook covering algorithmic and linear-algebraic underpinnings of ML including matrix methods.
- **docs/open-library/deep-learning/lecture-27-backpropagation-find-partial-derivatives-matrix-methods-in-data-analy.md** — Lecture 27: Backpropagation: Find Partial Derivatives | Matrix Methods in Data Analysis, Signal Processing, and Machine Learning. MIT 18.065 (Strang) lecture directly connecting matrix methods and linear algebra to ML.
- **docs/open-library/computability/15-859n-spectral-graph-theory-and-numerical-linear-algebra-fall-2011.md** — 15-859N: Spectral Graph Theory and Numerical Linear Algebra, Fall 2011. CMU course on numerical linear algebra and spectral methods, bridging linear algebra theory and computation.

---

## Primary texts

**Strang, G. (2016). *Introduction to Linear Algebra* (5th ed.). Wellesley-Cambridge Press.**
The calibration target for this module. Strang's geometric intuition — especially the four fundamental subspaces and the SVD chapters — is the clearest exposition of why linear algebra has the shape it does. Read Chapters 1–7 for the core, Chapter 11 for the ML connection. The accompanying MIT 18.06 lecture videos on OpenCourseWare make this effectively a free course.

**Strang, G. (2019). *Linear Algebra and Learning from Data*. Wellesley-Cambridge Press.**
Strang's explicit bridge from linear algebra to machine learning, covering deep learning, statistics, and optimization in the same geometric language as 18.06. Chapters on SVD, low-rank approximations, and the geometry of neural networks are directly prerequisite for Phases 2 and 3 of this curriculum.

**Axler, S. (2015). *Linear Algebra Done Right* (3rd ed.). Springer.**
The rigorous abstract treatment: vector spaces defined without determinants, the spectral theorem proved from first principles. Essential for building proof fluency and understanding why results hold, not just how to compute them. Work through this alongside Strang; the two books are complementary rather than redundant.

**Horn, R. A., & Johnson, C. R. (2012). *Matrix Analysis* (2nd ed.). Cambridge University Press.**
The graduate-level reference for matrix theory. The chapters on eigenvalues, singular values, norms, and positive semidefinite matrices are encyclopedic and proof-complete. Use as a reference when theory.md proof sketches need rigorous completion, and when results about Schur complements or matrix inequalities appear in M03 and M20.

**Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
The definitive text on how the theory of §§3–5 is actually computed in floating-point arithmetic. The chapters on QR factorization, SVD algorithms, and condition numbers explain why `numpy.linalg.svd` differs from a naive eigendecomposition approach — directly relevant to the project's verification task. Required reading before writing `verify_svd.py`.

---

## Key papers and articles

**Halko, N., Martinsson, P.-G., & Tropp, J. A. (2011). Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions. *SIAM Review*, 53(2), 217–288.**
The foundational paper for randomized SVD — the algorithm used in practice when exact SVD is too slow for large matrices. The probabilistic approximation error bounds connect directly to the open problems section of theory.md and are essential background for M42 (Frontier Research Methods).

**Aghajanyan, A., Zettlemoyer, L., & Gupta, S. (2021). Intrinsic dimensionality explains the effectiveness of language model fine-tuning. *arXiv:2012.13255*.**
Demonstrates empirically that the fine-tuning of large language models can be constrained to a surprisingly low-dimensional subspace of the parameter space — the intrinsic dimensionality — without significant loss of performance. The mathematical analysis is a direct application of the rank and SVD concepts in theory.md, and this paper is the empirical precursor to LoRA.

**Hu, E. J., et al. (2022). LoRA: Low-rank adaptation of large language models. *ICLR 2022*.**
Introduces Low-Rank Adaptation, which parameterizes weight updates as $\Delta W = BA$ with $\text{rank}(BA) = r \ll d$. The theoretical justification is precisely the Eckart-Young low-rank approximation theorem. This is the most widely deployed application of SVD in production ML systems as of 2026.
