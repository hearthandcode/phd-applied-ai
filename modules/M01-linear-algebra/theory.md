---
type: module-theory
schema_version: "1.0"
module_id: M01
module_title: "Linear Algebra for ML"
phase: 0
created: 2026-06-13
updated: 2026-06-13
status: generated
learner_id: L001
calibration_target: "MIT 18.06 (Gilbert Strang)"
archive_coverage: partial
language: Python
tags:
  - linear-algebra
  - foundations
  - math
  - adaptive-engine
  - phase-0
---

# M01: Linear Algebra for ML

*Calibration target: MIT 18.06 (Gilbert Strang) — doctoral depth with ML emphasis*

---

## Overview and motivation

Linear algebra is the ambient language of modern machine learning. Every major architecture — from logistic regression to the transformer — is ultimately a structured composition of linear maps, learned by gradient methods operating on vector spaces. Before gradient descent can meaningfully navigate a loss surface, before attention can weight tokens, before PCA can compress a dataset, the underlying geometry must be understood with precision.

This module targets the depth of MIT 18.06 while foregrounding the specific structures that recur throughout the ML curriculum. The goal is not merely computational fluency but conceptual mastery: the ability to look at a neural network layer, a covariance matrix, or an attention score and immediately perceive its linear-algebraic skeleton. The adjacent modules — M02 (Multivariate Calculus and Optimization) and M03 (Probability Theory and Bayesian Inference) — build directly on the structures introduced here; eigendecomposition reappears as spectral analysis of covariance in M03, and the Jacobian studied in M02 is precisely a matrix of first-order partial derivatives applied to the weight maps defined here.

---

## Vector spaces and linear maps

### Abstract vector spaces

A vector space is a universe of objects that obeys two compatible rules: you can add any two objects together and stay in the universe, and you can scale any object by a number and still stay. Think of arrows in three-dimensional space — you can add two arrows tip-to-tail, and you can stretch or shrink any arrow. What makes the abstract definition powerful is that the exact same rules govern spaces of functions, spaces of matrices, and spaces of neural network parameters. "Arrow" intuition keeps working even when you can't draw a picture, because the rules are identical.

A **vector space** over a field $\mathbb{F}$ (typically $\mathbb{R}$ or $\mathbb{C}$) is a set $V$ equipped with operations of addition and scalar multiplication satisfying the eight standard axioms: closure, associativity, commutativity of addition, identity and inverse elements for addition, and distributivity of scalar multiplication over both field addition and vector addition.

The canonical example is $\mathbb{R}^n$, but the definition is intentionally general. The space of all continuous real-valued functions on $[0,1]$ is a vector space; so is the set of $m \times n$ real matrices; so is the set of polynomials of degree at most $d$. This generality matters because ML routinely operates in function spaces: the set of all neural networks with a given architecture, treated as a parameterized function class, has a vector-space-like structure that governs regularization and generalization.

A **subspace** $W \subseteq V$ is a subset closed under the inherited operations. The four fundamental subspaces of a matrix $A \in \mathbb{R}^{m \times n}$ — column space $\mathcal{C}(A)$, null space $\mathcal{N}(A)$, row space $\mathcal{C}(A^\top)$, and left null space $\mathcal{N}(A^\top)$ — organize the geometry of the linear system $Ax = b$ completely. A solution exists if and only if $b \in \mathcal{C}(A)$; the solution is unique if and only if $\mathcal{N}(A) = \{0\}$.

### Linear independence, basis, and dimension

Independence means no redundancy: a set of vectors is independent if none of them can be built by combining the others. A basis is the minimal independent set that still describes everything — the "alphabet" of the space. Dimension is the size of that alphabet. Intuitively: you need exactly $n$ truly different directions to locate any point in an $n$-dimensional space. Fewer and you can't reach everywhere. More and some directions are secretly duplicates disguised as new information.

A set $\{v_1, \ldots, v_k\} \subset V$ is **linearly independent** if $\sum_{i=1}^k c_i v_i = 0$ implies $c_i = 0$ for all $i$. A **basis** is a linearly independent spanning set. All bases of a finite-dimensional vector space have the same cardinality, defining the **dimension** $\dim(V)$.

In ML, dimension corresponds directly to the number of features in a dataset, the number of parameters in a model layer, or the number of latent dimensions in an embedding. Choosing the right dimension is never arbitrary — it is constrained by the rank of the data matrix, the intrinsic dimensionality of the underlying distribution, and the computational budget available for learning.

### The rank-nullity theorem

Every linear map may "collapse" some directions — squashing entire subspaces down to zero. The rank-nullity theorem is conservation arithmetic: what a map *uses* (its rank, the dimensions it actually produces outputs in) plus what it *destroys* (its nullity, the dimensions it collapses to zero) must exactly equal the total input dimension. Nothing is created; the rest is erased. A wide, flat weight matrix that maps 512 dimensions to 64 must destroy 448-dimensional worth of input — and the theorem tells you exactly where that information went.

**Theorem (Rank-Nullity).** For a linear map $T: V \to W$ between finite-dimensional spaces,
$$\dim(\ker T) + \dim(\text{im}\, T) = \dim(V).$$

*Proof sketch.* Let $\{u_1, \ldots, u_k\}$ be a basis for $\ker T$ and extend it to a basis $\{u_1, \ldots, u_k, v_1, \ldots, v_r\}$ of $V$. One shows that $\{T(v_1), \ldots, T(v_r)\}$ is a basis for $\text{im}\, T$ by (a) showing linear independence using the kernel basis and (b) showing span from the fact that any $w \in \text{im}\, T$ comes from some $x \in V$, which decomposes into kernel and complement parts. Hence $k + r = \dim(V)$. $\square$

**ML significance.** The rank-nullity theorem tells you exactly how much information a weight matrix destroys. A weight matrix $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$ with rank $r < d_{\text{in}}$ maps all inputs in a $(d_{\text{in}} - r)$-dimensional subspace to zero — those directions are permanently erased. This is the algebraic core of why low-rank approximations (LoRA, for instance) are a coherent compression strategy: they explicitly parameterize the map with a rank-$r$ structure, discarding directions the training signal does not need.

**Worked example.** Take a weight matrix $W \in \mathbb{R}^{64 \times 512}$ — the kind of projection layer that compresses a 512-dimensional token embedding into a 64-dimensional head representation. Since $W$ can produce at most 64 linearly independent output directions, $\text{rank}(W) \leq 64$. Rank-nullity immediately gives $\dim(\ker W) \geq 512 - 64 = 448$. Those 448 null-space directions are not approximated or weakened — they are annihilated to exactly zero. Any two inputs $x_1, x_2$ satisfying $x_1 - x_2 \in \ker(W)$ produce identical outputs: $Wx_1 = Wx_2$. The layer cannot distinguish them, no matter what comes after. This is not a flaw; controlled information destruction is the compression. Now consider LoRA fine-tuning with rank $r = 8$: parameterize the weight update as $\Delta W = BA$ where $B \in \mathbb{R}^{64 \times 8}$ and $A \in \mathbb{R}^{8 \times 512}$. Instead of updating $64 \times 512 = 32{,}768$ parameters, you train $8 \times (64 + 512) = 4{,}608$ — an 7× reduction. The rank-nullity structure makes this principled rather than heuristic: if the pretrained model already covers the important output directions, the fine-tuning signal plausibly lives in a much smaller subspace than the full parameter space.

---

## Inner products, norms, and geometry

### Inner product spaces

The inner product is a formal way to ask: "how much do these two directions agree?" Two vectors pointing the same way give a large positive answer. Two pointing opposite ways give a large negative one. Two pointing at right angles give exactly zero — they are invisible to each other, neither confirming nor contradicting the other's direction. This zero-agreement case, orthogonality, is one of the most structurally useful properties in all of linear algebra: orthogonal components of a problem can be solved completely independently, without interference.

An **inner product** on a real vector space $V$ is a map $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$ that is bilinear, symmetric, and positive definite. The canonical inner product on $\mathbb{R}^n$ is $\langle x, y \rangle = x^\top y = \sum_i x_i y_i$.

The induced **norm** is $\|x\| = \sqrt{\langle x, x \rangle}$, and the **angle** between nonzero vectors is $\cos\theta = \langle x, y \rangle / (\|x\| \|y\|)$. Vectors are **orthogonal** when $\langle x, y \rangle = 0$, i.e., $\theta = \pi/2$.

Two norms $\|\cdot\|_\alpha$ and $\|\cdot\|_\beta$ on a finite-dimensional space are always equivalent: there exist constants $c, C > 0$ such that $c\|x\|_\alpha \leq \|x\|_\beta \leq C\|x\|_\alpha$ for all $x$. This equivalence breaks in infinite dimensions, which is why the choice of norm in function-space regularization (RKHS, Sobolev spaces) carries real content.

**Worked example.** Consider three token embeddings simplified to 3 dimensions (after normalization to unit length):
$$v_{\text{cat}} = [0.90,\ 0.30,\ 0.10], \quad v_{\text{kitten}} = [0.80,\ 0.50,\ 0.10], \quad v_{\text{democracy}} = [0.10,\ 0.10,\ 0.90].$$
The standard inner products are:
$$\langle v_{\text{cat}}, v_{\text{kitten}} \rangle = (0.90)(0.80) + (0.30)(0.50) + (0.10)(0.10) = 0.72 + 0.15 + 0.01 = 0.88$$
$$\langle v_{\text{cat}}, v_{\text{democracy}} \rangle = (0.90)(0.10) + (0.30)(0.10) + (0.10)(0.90) = 0.09 + 0.03 + 0.09 = 0.21$$
The cat–kitten score is more than four times the cat–democracy score, reflecting semantic proximity. In a transformer's self-attention layer, these inner products are the raw logits before scaling: the scaled score $q_i \cdot k_j / \sqrt{d_k}$ for positions $i, j$ determines how strongly position $i$ attends to position $j$. Near-orthogonality ($\langle q, k \rangle \approx 0$) means near-inattention; alignment ($\langle q, k \rangle$ large) means strong attention.

### Projection and least squares

Projection is the mathematical equivalent of casting a shadow. Hold a point above a surface and drop a perpendicular: the spot where it lands is the projection — the closest point on the surface to where you started. Least squares asks: when a system has no exact solution (more constraints than free variables, as happens whenever you have more data points than model parameters), which approximate solution minimizes total error? The answer is always the projection of the target onto the reachable set. The residual — what you wanted minus what you could get — is always perpendicular to every reachable direction. That perpendicularity is not a coincidence; it is the optimality condition.

The **orthogonal projection** of $b \in \mathbb{R}^m$ onto $\mathcal{C}(A)$ is $\hat{b} = A(A^\top A)^{-1} A^\top b$ (when $A$ has full column rank). The vector $\hat{x} = (A^\top A)^{-1} A^\top b$ minimizes $\|Ax - b\|^2$ — this is ordinary least squares. The matrix $P = A(A^\top A)^{-1} A^\top$ is the **projection matrix** onto $\mathcal{C}(A)$; it satisfies $P^2 = P$ (idempotent) and $P^\top = P$ (symmetric).

Least squares is not just a statistical estimator; it is a geometric statement. The residual $b - \hat{b}$ is orthogonal to every column of $A$, which is encoded by the **normal equations** $A^\top(b - A\hat{x}) = 0$.

In neural networks, the final linear layer of a regression head is solving a least-squares problem in the feature space defined by the penultimate layer's outputs. This perspective — neural networks as learned feature extractors followed by a linear readout — is foundational for understanding fine-tuning, linear probing, and transfer learning.

**Worked example.** Fit a line $y = mx + b$ through three data points: $(1, 2)$, $(2, 4)$, $(3, 5)$. Three equations, two unknowns — the system is overdetermined and has no exact solution. Setting up $Ax = y$:
$$A = \begin{pmatrix} 1 & 1 \\ 2 & 1 \\ 3 & 1 \end{pmatrix}, \qquad y = \begin{pmatrix} 2 \\ 4 \\ 5 \end{pmatrix}.$$
The normal equations $A^\top A\, \hat{x} = A^\top y$ give:
$$A^\top A = \begin{pmatrix} 14 & 6 \\ 6 & 3 \end{pmatrix}, \qquad A^\top y = \begin{pmatrix} 25 \\ 11 \end{pmatrix}.$$
Solving: $\hat{m} = 1.5$, $\hat{b} \approx 0.33$. The fitted line $y = 1.5x + 0.33$ passes through none of the three points exactly, but minimizes total squared error across all three. The residual vector $e = y - A\hat{x} \approx (-0.17,\ 0.33,\ -0.17)^\top$ satisfies $A^\top e \approx 0$ to numerical precision — confirming the geometric optimality condition: the residual is orthogonal to every direction reachable by $A$, which means no linear adjustment to $\hat{x}$ can reduce the error further.

---

## Eigendecomposition

### Eigenvalues and eigenvectors

Most vectors, when a matrix acts on them, change both length and direction simultaneously — they get rotated and stretched at once. Eigenvectors are the exceptional directions where only the length changes, never the direction. Apply the matrix, and the vector still points exactly the same way — just longer or shorter by the eigenvalue factor. These "fixed directions" are the natural axes in which the matrix's behavior is simplest: instead of a complex rotation-and-stretch, you see only a list of scale factors. When you find all the eigenvectors, you have found the coordinate system in which the matrix is completely diagonal — all coupling between dimensions disappears.

For a square matrix $A \in \mathbb{R}^{n \times n}$, a nonzero vector $v$ is an **eigenvector** with **eigenvalue** $\lambda$ if
$$Av = \lambda v.$$

Eigenvalues are the roots of the **characteristic polynomial** $\det(A - \lambda I) = 0$, a degree-$n$ polynomial in $\lambda$. By the fundamental theorem of algebra, $A$ has exactly $n$ eigenvalues in $\mathbb{C}$ (counted with multiplicity). For real symmetric matrices, all eigenvalues are real.

**Worked example.** Take the symmetric matrix
$$A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}.$$
The characteristic polynomial is $\det(A - \lambda I) = (3 - \lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = 0$, giving $\lambda_1 = 4$ and $\lambda_2 = 2$. For $\lambda_1 = 4$: solving $(A - 4I)v = 0$ gives $v_1 = [1,\ 1]^\top / \sqrt{2}$ (the diagonal direction). For $\lambda_2 = 2$: solving gives $v_2 = [1,\ -1]^\top / \sqrt{2}$ (the anti-diagonal). Verify directly: $A \cdot [1,1]^\top = [4,4]^\top = 4 \cdot [1,1]^\top$. The vector pointing diagonally gets stretched by 4. The anti-diagonal vector gets stretched by 2. In every other direction, $A$ simultaneously rotates and stretches — only these two eigendirections experience pure scaling with no rotation. If $A$ were an empirical covariance matrix, $v_1 = [1,1]^\top/\sqrt{2}$ would be the principal component — the direction of maximum variance — and the ratio $\lambda_1 / \lambda_2 = 2$ would indicate that data varies twice as strongly along the diagonal as along the anti-diagonal.

### The spectral theorem

The spectral theorem says something striking about symmetric matrices: they always have a set of perfectly perpendicular "natural directions" such that in those directions the matrix does nothing but scale. The matrix may look complicated in ordinary coordinates — entries everywhere, coupling every dimension to every other — but rotate to its eigenvectors and complexity collapses into a diagonal list of stretch factors. PCA exploits this directly: it finds the natural directions of a dataset's covariance matrix, the axes along which the data varies independently and most strongly.

**Theorem (Spectral Theorem for Symmetric Matrices).** If $A \in \mathbb{R}^{n \times n}$ is symmetric ($A = A^\top$), then $A$ has $n$ real eigenvalues $\lambda_1, \ldots, \lambda_n$ and a corresponding set of orthonormal eigenvectors $q_1, \ldots, q_n$ forming a basis for $\mathbb{R}^n$. Equivalently,
$$A = Q \Lambda Q^\top$$
where $Q = [q_1 | \cdots | q_n]$ is orthogonal ($Q^\top Q = I$) and $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_n)$.

*Proof sketch.* By the real spectral theorem (proved inductively): find one eigenvalue (guaranteed real by showing $\lambda = \bar\lambda$ using $q^\top A q \in \mathbb{R}$), take the orthogonal complement of the corresponding eigenspace, and use the symmetry of $A$ to show that the restriction to this complement is also symmetric. Repeat. $\square$

The spectral theorem gives a complete geometric picture: every symmetric matrix is a rotation (by $Q^\top$), axis-aligned scaling (by $\Lambda$), and inverse rotation (by $Q$). Symmetric matrices arise naturally as covariance matrices, Gram matrices ($A^\top A$ and $AA^\top$), the Hessian of a loss function, and the Laplacian of a graph.

**ML application: PCA.** Principal component analysis finds the directions of maximum variance in a dataset $X \in \mathbb{R}^{n \times d}$. The empirical covariance is $\Sigma = \frac{1}{n} X^\top X$ (assuming centered data). By the spectral theorem, $\Sigma = Q\Lambda Q^\top$. The principal components are the columns of $Q$, ordered by decreasing eigenvalue. Projecting onto the top-$k$ eigenvectors achieves the optimal rank-$k$ approximation to $\Sigma$ in the Frobenius norm sense — a fact that connects eigendecomposition to the next section.

**Worked example.** A centered 2D dataset has empirical covariance matrix
$$\Sigma = \begin{pmatrix} 4 & 2 \\ 2 & 2 \end{pmatrix}.$$
The characteristic polynomial $(4-\lambda)(2-\lambda) - 4 = \lambda^2 - 6\lambda + 4 = 0$ gives $\lambda_1 \approx 5.24$ and $\lambda_2 \approx 0.76$. PCA with $k=1$ retains $5.24 / (5.24 + 0.76) \approx 87\%$ of total variance, compressing each 2D point to a single coordinate — the projection onto the first eigenvector. The second eigenvector direction, accounting for only 13% of variance, is discarded. Scaling this up: in a typical 512-dimensional language model hidden-state space, the top 50 eigenvectors of the covariance matrix of activations across a dataset often capture 85–92% of total variance. The model's effective intrinsic dimensionality is far lower than 512 — which is why dimensionality-reduction probes of transformer representations work so well.

---

## Singular value decomposition

### The SVD theorem

Every linear transformation — no matter how complex — can be decomposed into exactly three steps: first, rotate the input space into an aligned position; then, stretch or shrink along each axis (and possibly discard dimensions entirely); finally, rotate the output space into its final orientation. That is the SVD. The singular values are the stretch factors, listed largest to smallest. The first few carry most of the transformation's information; the last ones are near zero and can often be dropped without meaningful loss. Once you can see the singular value spectrum of a matrix, you can read off exactly how much of it you can safely discard — which is why SVD underlies image compression, recommendation systems, and low-rank approximations of neural network weight matrices alike.

**Theorem (SVD).** For any matrix $A \in \mathbb{R}^{m \times n}$ with rank $r$, there exist orthogonal matrices $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ and a matrix $\Sigma \in \mathbb{R}^{m \times n}$ with nonnegative diagonal entries $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots$ such that
$$A = U \Sigma V^\top.$$

The $\sigma_i$ are the **singular values** of $A$; the columns $u_i$ of $U$ are the **left singular vectors**; the columns $v_i$ of $V$ are the **right singular vectors**.

*Proof sketch.* Consider the symmetric positive semidefinite matrix $A^\top A \in \mathbb{R}^{n \times n}$. By the spectral theorem, $A^\top A = V \Lambda V^\top$ with $\lambda_i \geq 0$. Define $\sigma_i = \sqrt{\lambda_i}$ and $u_i = \frac{1}{\sigma_i} A v_i$ for $i \leq r$. One verifies that $\{u_1, \ldots, u_r\}$ are orthonormal and extends to a basis for $\mathbb{R}^m$. Writing out $U$, $\Sigma$, $V$ from these definitions gives $A = U\Sigma V^\top$. $\square$

The SVD is the most important matrix factorization in applied mathematics. It exists for every matrix, rectangular or square, and provides the complete geometry of the linear map: $V^\top$ rotates in the input space, $\Sigma$ stretches along the coordinate axes, and $U$ rotates in the output space.

**Worked example.** Take the matrix
$$A = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}.$$
Computing $A^\top A = \begin{pmatrix} 5 & 11 \\ 11 & 25 \end{pmatrix}$, the eigenvalues are approximately $29.73$ and $0.27$, giving singular values $\sigma_1 \approx 5.45$ and $\sigma_2 \approx 0.52$. The SVD says: first rotate the input plane (via $V^\top$, taking input directions into the aligned frame), then stretch axis 1 by $5.45$ and axis 2 by $0.52$ (via $\Sigma$), then rotate in the output plane (via $U$). The rank-1 approximation $A_1 = \sigma_1 u_1 v_1^\top$ has error $\|A - A_1\|_F = \sigma_2 \approx 0.52$, while $\|A\|_F = \sqrt{\sigma_1^2 + \sigma_2^2} \approx 5.47$. So the rank-1 approximation captures $\sigma_1^2 / (\sigma_1^2 + \sigma_2^2) \approx 99.1\%$ of the total Frobenius energy — this $2 \times 2$ matrix already has one overwhelmingly dominant singular mode.

### Low-rank approximation and the Eckart-Young theorem

**Theorem (Eckart-Young-Mirsky).** Let $A = \sum_{i=1}^r \sigma_i u_i v_i^\top$. The best rank-$k$ approximation to $A$ in both the Frobenius norm and the spectral norm is
$$A_k = \sum_{i=1}^k \sigma_i u_i v_i^\top = U_k \Sigma_k V_k^\top,$$
where $U_k, V_k$ are the leading $k$ singular vectors. The approximation error is
$$\|A - A_k\|_F^2 = \sum_{i=k+1}^r \sigma_i^2, \qquad \|A - A_k\|_2 = \sigma_{k+1}.$$

This theorem underpins image compression (treating the image as a matrix and discarding small singular values), latent semantic analysis in NLP, the mathematical justification for matrix factorization recommender systems, and the theoretical basis for LoRA in fine-tuning large language models.

**Worked example.** A $1000 \times 1000$ grayscale image has a full SVD with 1000 singular values. The cumulative energy $\sum_{i=1}^k \sigma_i^2 / \sum_{i=1}^{1000} \sigma_i^2$ typically reaches 90–95% at $k \approx 50$ for natural images — visual content concentrates in a few dozen orthogonal modes. Storing the rank-50 approximation $A_{50} = U_{50} \Sigma_{50} V_{50}^\top$ requires $50 \times (1000 + 1000 + 1) = 100{,}050$ numbers instead of $10^6$, a $10\times$ compression with near-photographic quality. The discarded 950 singular values account for at most 5–10% of energy and are primarily high-frequency noise components that a human observer cannot distinguish. This concentration of "signal" in the leading singular values is not accidental — natural images have smooth spatial structure that the leading singular vectors naturally capture.

### SVD and the pseudoinverse

When $A$ is not square or not full rank, the ordinary inverse does not exist. The **Moore-Penrose pseudoinverse** is
$$A^+ = V \Sigma^+ U^\top,$$
where $\Sigma^+$ replaces each nonzero diagonal entry $\sigma_i$ with $1/\sigma_i$. The pseudoinverse delivers the minimum-norm least-squares solution: $\hat{x} = A^+ b$ minimizes $\|Ax - b\|$ and, among all minimizers, has the smallest $\|x\|$.

---

## Orthogonality and matrix decompositions

### Gram-Schmidt and QR

Orthogonalization is the process of taking a set of vectors that lean into each other and rotating them apart until every pair is perfectly perpendicular. Gram-Schmidt does this one vector at a time: take the next vector, subtract off everything that overlaps with the directions you've already cleaned up, then normalize. The result covers the same subspace as before but now every axis is at a right angle to every other. This geometric cleanliness translates directly into numerical stability — orthogonal bases are as well-conditioned as a basis can be.

Given a linearly independent set $\{a_1, \ldots, a_k\}$, the **Gram-Schmidt process** produces an orthonormal set $\{q_1, \ldots, q_k\}$ spanning the same subspace by iteratively subtracting projections:
$$q_j = \frac{a_j - \sum_{i<j} \langle a_j, q_i \rangle q_i}{\left\|a_j - \sum_{i<j} \langle a_j, q_i \rangle q_i\right\|}.$$

Applied to the columns of $A$, this yields the **QR decomposition** $A = QR$ where $Q$ has orthonormal columns and $R$ is upper triangular. QR is numerically more stable than forming the normal equations $A^\top A$ and is the basis for most practical least-squares solvers and eigenvalue algorithms (the QR algorithm for computing eigenvalues runs $O(n^3)$ iterations of QR factorization).

### LU decomposition and Gaussian elimination

For square systems $Ax = b$, Gaussian elimination produces the **LU decomposition** $A = PLU$ where $P$ is a permutation matrix (row pivoting), $L$ is unit lower triangular, and $U$ is upper triangular. Solving $Ax = b$ reduces to two triangular solves, each $O(n^2)$, after an $O(n^3)$ factorization. LU is the workhorse for dense linear system solvers and appears in many numerical linear algebra routines invoked internally by ML frameworks.

### Cholesky decomposition

For symmetric positive definite (SPD) matrices, the more efficient **Cholesky decomposition** $A = LL^\top$ (where $L$ is lower triangular with positive diagonal) halves the operations of LU. Gaussian processes, Kalman filters, and Laplace approximations in Bayesian inference all exploit Cholesky factorization for $O(n^3)$ inference and sampling.

---

## Spectral analysis and matrix functions

### The matrix exponential and differential equations

The familiar scalar equation $\dot{x} = ax$ (where $a$ is a number) has solution $x(t) = e^{at} x(0)$: the system grows or decays exponentially at rate $a$. When many variables are coupled together, the same idea generalizes: the system $\dot{x} = Ax$ (where $A$ is a matrix) has solution $x(t) = e^{tA} x(0)$. The eigenvalues of $A$ completely determine long-run behavior — positive real parts cause growth, negative parts cause decay, imaginary parts cause oscillation. For a recurrent neural network, the recurrent weight matrix plays the role of $A$, and eigenvalues larger than 1 in magnitude cause the exploding gradients that make RNNs notoriously hard to train on long sequences.

The **matrix exponential** is defined by $e^{tA} = \sum_{k=0}^\infty \frac{t^k A^k}{k!}$. For a diagonalizable matrix $A = Q\Lambda Q^{-1}$, this simplifies to $e^{tA} = Q e^{t\Lambda} Q^{-1}$, where $e^{t\Lambda} = \text{diag}(e^{t\lambda_1}, \ldots, e^{t\lambda_n})$. The system of ODEs $\dot{x} = Ax$ has solution $x(t) = e^{tA} x(0)$.

The eigenvalues of the weight matrix in a recurrent neural network (RNN) play exactly this role: eigenvalues $|\lambda_i| > 1$ cause exponentially exploding activations over time, while $|\lambda_i| < 1$ cause vanishing. The exploding/vanishing gradient problem in RNNs is directly a spectral stability problem for the matrix $A = W_{\text{rec}}$.

### Condition number and numerical stability

The condition number measures how fragile a matrix is — how much a small perturbation in the input can amplify into a large change in the output. Imagine two ramps: a gentle slope and a nearly vertical cliff. A tiny horizontal step produces a tiny altitude change on the gentle slope but an enormous change near the cliff. A poorly conditioned matrix is the cliff: small input errors become large output errors. In optimization, a loss surface with very different curvatures in different directions (steep in one direction, nearly flat in another) has a large condition number on its Hessian, and gradient descent struggles because any step size that makes progress in the steep direction is too large for the flat one — and vice versa.

The **condition number** of a matrix $A$ is $\kappa(A) = \|A\| \cdot \|A^{-1}\| = \sigma_1 / \sigma_r$ (the ratio of the largest to smallest singular value). A large condition number means that small perturbations in $b$ can cause large changes in the solution $x$ of $Ax = b$. Numerical solvers lose approximately $\log_{10}(\kappa(A))$ digits of precision.

In training, large condition numbers for the Hessian of the loss surface correspond to ill-conditioned optimization landscapes: one direction has a very steep curvature and another is nearly flat. Second-order methods (Newton's method, natural gradient descent) attempt to precondition the gradient by multiplying by $H^{-1}$, normalizing these curvature scales. This is the linear-algebraic mechanism behind adaptive optimizers such as Adam.

**Worked example.** Consider the nearly-singular system
$$A = \begin{pmatrix} 1.000 & 1.000 \\ 1.000 & 1.001 \end{pmatrix}, \qquad b_1 = \begin{pmatrix} 2.000 \\ 2.000 \end{pmatrix}.$$
Solving $Ax = b_1$ gives $x_1 \approx (2, 0)^\top$. Now perturb $b$ by 0.05% in the second component: $b_2 = (2.000, 2.001)^\top$. Solving $Ax = b_2$ gives $x_2 \approx (1, 1)^\top$ — the solution weight has shifted entirely from the first variable to an equal split. A 0.05% input change produced a 100% change in the solution. The condition number here is $\kappa(A) = \sigma_1 / \sigma_2 \approx 2001$: relative errors in $x$ can be up to $\kappa$ times the relative errors in $b$. In a neural network, an ill-conditioned Hessian means one curvature direction is $2000\times$ steeper than another. Any gradient-descent step large enough to make progress along the flat direction overshoots catastrophically along the steep one — exactly the instability that adaptive optimizers like Adam correct by maintaining per-parameter learning rates proportional to gradient history.

---

## Attention mechanisms: linear algebra in action

The transformer's scaled dot-product attention is a direct application of multiple linear-algebraic constructs:
$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) V$$

Here $Q \in \mathbb{R}^{n \times d_k}$, $K \in \mathbb{R}^{n \times d_k}$, and $V \in \mathbb{R}^{n \times d_v}$ are linear projections of the input sequence. The matrix product $QK^\top / \sqrt{d_k}$ computes pairwise inner products between query and key vectors — exactly the inner product geometry of §2 — normalized by $\sqrt{d_k}$ to counteract the variance growth that pushes softmax into saturation regions. The resulting attention weight matrix is then used to take a weighted combination of value vectors, which is a matrix-vector product.

Multi-head attention applies this construction $h$ times with different learned projections $W_i^Q, W_i^K, W_i^V$, each projecting into a lower-dimensional subspace of dimension $d_k = d_{\text{model}} / h$. The outputs are concatenated and projected back: $\text{MultiHead} = [h_1; \ldots; h_h] W^O$. The full computation is a sequence of rectangular matrix multiplications, and its complexity scales as $O(n^2 d)$ in sequence length — a fact that motivates approximations based on low-rank decompositions of the attention matrix.

---

## Neural network weight matrices: structure and geometry

A feedforward network layer computes $h = \sigma(Wx + b)$ where $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$. The singular values of $W$ control the Lipschitz constant of the linear part: $\|Wx\| \leq \sigma_1(W) \|x\|$, so $\sigma_1(W)$ (the spectral norm) bounds how much the layer can amplify inputs.

**Spectral normalization**, used in generative adversarial networks to stabilize training, constrains $\sigma_1(W) \leq 1$ by dividing $W$ by its estimated spectral norm at each step. This is computed efficiently via power iteration, an algorithm that approximates the top singular vector without a full SVD.

The **effective rank** of a weight matrix at convergence often differs from its nominal rank. Empirical studies (e.g., Aghajanyan et al., 2021) find that large pre-trained language models have intrinsically low-rank adaptation structure: fine-tuning directions live in a low-dimensional subspace of the full parameter space. This is the empirical motivation for LoRA, which parameterizes the weight update as $\Delta W = BA$ where $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times d}$, $r \ll d$.

---

## Limitations, open problems, and research frontiers

### Non-commutative and non-Euclidean geometry

Standard linear algebra assumes commutativity of the underlying field and a Euclidean metric. Machine learning increasingly operates in settings where these fail:

- **Matrix Lie groups**: rotation matrices form a group under multiplication, and the correct way to average or interpolate rotations uses the Riemannian geometry of $SO(n)$, not Euclidean averaging in $\mathbb{R}^{n^2}$.
- **Hyperbolic space**: hierarchical data (taxonomies, parse trees) embeds more naturally in hyperbolic than Euclidean space; the Poincaré disk model is not a vector space in the usual sense.
- **Tensor networks**: quantum computing and some neural network architectures use tensors (multilinear maps) whose decomposition theory generalizes but does not reduce to the matrix SVD.

### Randomized linear algebra

Exact SVD is $O(\min(m,n)^2 \cdot \max(m,n))$, which is prohibitive for matrices with millions of rows. **Randomized SVD** (Halko, Martinsson, Tropp, 2011) computes an approximate rank-$k$ decomposition in $O(mn \log k + (m+n) k^2)$ time by first projecting onto a random subspace. This is used in practice for PCA on large datasets and increasingly in model compression pipelines. The theoretical guarantees — probabilistic bounds on the approximation error — require tools from high-dimensional probability (M03).

### The expressivity-rank tradeoff

A central open question is: for a neural network of fixed depth and width, what is the relationship between the ranks of its weight matrices and the class of functions it can represent? Known results (e.g., for linear networks) show that training dynamics tend to discover implicitly low-rank solutions even when no explicit rank constraint is imposed. Whether this implicit regularization is a fundamental property of gradient descent or an artifact of specific initialization schemes remains an active research area.

---

## Connections to adjacent modules

**M02 — Multivariate Calculus and Optimization:** The Jacobian of a vector-valued function $f: \mathbb{R}^n \to \mathbb{R}^m$ is a matrix $J \in \mathbb{R}^{m \times n}$; backpropagation is precisely chain-rule composition of Jacobians. The Hessian $H = \nabla^2 \mathcal{L}$ is a symmetric matrix whose eigenstructure determines the local geometry of the loss surface.

**M03 — Probability Theory and Bayesian Inference:** Multivariate Gaussian distributions are parameterized by a covariance matrix $\Sigma$, which must be symmetric positive semidefinite. The spectral decomposition of $\Sigma$ gives the principal axes of the Gaussian; its Cholesky factorization enables sampling ($x = \mu + Lz$, $z \sim \mathcal{N}(0,I)$). Bayesian linear regression requires inverting or factorizing $\Sigma$ at every update — making numerical linear algebra a computational bottleneck in probabilistic ML.

**M04 — Statistics and Statistical Learning:** The hat matrix $H = X(X^\top X)^{-1} X^\top$ in linear regression is a projection matrix in the sense of §2. Ridge regression ($\hat\beta = (X^\top X + \lambda I)^{-1} X^\top y$) is equivalent to adding $\lambda$ to every singular value before inversion — a regularization that also improves the condition number of the system.

---

## Summary

Linear algebra provides the mathematical substrate for virtually every ML operation. The key results to internalize at doctoral depth are:

1. The four fundamental subspaces and the rank-nullity theorem — they determine what a linear map can and cannot represent.
2. The spectral theorem for symmetric matrices — the foundation of PCA, covariance analysis, and graph-based methods.
3. The SVD — the most general matrix factorization, connecting least squares, dimensionality reduction, and low-rank approximation.
4. The condition number — the quantitative measure of numerical stability and optimization landscape difficulty.
5. The geometric interpretation of each factorization as rotation + scaling + rotation — a lens that unifies apparently disparate ML techniques.

Mastery means being able to derive these results, apply them to new architectures, and recognize when a numerical or learning difficulty has a linear-algebraic explanation.
