---
module: M01
title: "Linear Algebra for ML"
artifact: theory-section
section: "10 — Connections to Adjacent Modules"
calibration: "MIT 18.06 (Strang) — synthesis / forward-links to M02–M23"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "theory/05-matrix-decompositions.md"
---

# Section 10 — Connections to Adjacent Modules

## Pre-reading map — why this section exists

You've built the whole machine: vector spaces, inner products, eigendecomposition,
SVD, the practical decompositions. This section does something different — it shows
that the machine you built is **the same machine** running under the hood of five
modules you haven't studied yet. Linear algebra isn't a prerequisite you finish and
file away; it's the *skeleton* every later module hangs flesh on. The goal here is
recognition: when you reach M02, M03, M04, M21, M23, you should feel a jolt of
"wait — I already know this part."

We'll walk five bridges, each: **the adjacent idea → the linear-algebra skeleton you
already own → one line of why it matters.**

---

## 1. Bridge to M02 (Calculus): derivatives are linear maps

**The adjacent idea.** Calculus is about how functions change. For a function of
many variables `f : ℝⁿ → ℝᵐ`, "the derivative" can't be a single slope — there are
`n` inputs and `m` outputs, so the rate of change is a whole *table* of partial
derivatives.

**The linear-algebra skeleton.** That table is the **Jacobian** `J` — an `m×n`
matrix (exactly the shape from the four-subspaces file). And here's the deep
unification: the derivative *is the best linear map approximating `f` near a point*.
Zoom in close enough to any smooth function and it looks linear; the Jacobian is that
linear map. For a scalar function `f : ℝⁿ → ℝ`, the Jacobian collapses to a single
row — the **gradient** `∇f`, the direction of steepest ascent. A gradient is a linear
functional: it eats a direction vector and returns a rate of change *via a dot
product* (`directional derivative = ∇f · direction` — the alignment meter from
foundations/06).

**Why it matters.** Gradient descent is "walk opposite the gradient." Every step is a
dot product and a scaled vector add — the primer's two operations. Calculus on many
variables *is* linear algebra applied locally.

---

## 2. Bridge to M03 (Probability): covariance is an eigenproblem

**The adjacent idea.** Probability describes spread and correlation. For a random
vector, the **covariance matrix** `Σ` records how each pair of coordinates varies
together — diagonal entries are variances, off-diagonal entries are correlations.

**The linear-algebra skeleton.** `Σ` is **symmetric positive semi-definite**, so by
the spectral theorem (eigendecomposition, theory/03) it has orthogonal eigenvectors
and non-negative eigenvalues: `Σ = QΛQᵀ`. The eigenvectors are the **principal axes**
of the data cloud; the eigenvalues are the **variance along each axis**. The
multivariate Gaussian density is `exp(−½ (x−μ)ᵀ Σ⁻¹ (x−μ))` — its exponent is a
**quadratic form**, the bowl-shaped surface eigendecomposition was built to analyze.
The eigenvectors of `Σ` orient the ellipsoidal contours; the eigenvalues set their
widths.

**Why it matters.** "Decorrelate the data" = rotate into `Σ`'s eigenbasis. The
Gaussian — the most important distribution in ML — is *geometrically* an eigen-shaped
ellipsoid. You already own the geometry.

---

## 3. Bridge to M04 (Statistics): regression is projection, PCA is SVD

**The adjacent idea.** Statistics fits models to data. Two pillars: linear
**regression** (fit a line/hyperplane) and **PCA** (find the dominant directions of
variation).

**The linear-algebra skeleton.** You already saw it in foundations/06:
**linear regression is projection onto the column space** `C(A)` of the design
matrix. The fitted values are `P b` with `P = A(AᵀA)⁻¹Aᵀ`; the residual is
perpendicular, living in `N(Aᵀ)`. And **PCA is just the SVD** (theory/04) of the
centered data matrix: the right singular vectors are the principal directions, the
singular values squared (over `n−1`) are the explained variances. Equivalently, PCA
is the eigendecomposition of the covariance `Σ` from bridge 2 — SVD and the
eigenproblem are two doors into the same room.

**Why it matters.** Two of the most-used tools in applied statistics are not new
techniques — they're foundations/06's projection and theory/04's SVD wearing
statistical clothing.

---

## 4. Bridge to M21 (Neural Networks): backprop is the chain rule on linear maps

**The adjacent idea.** A neural network is a stack of layers; training adjusts
weights by **backpropagation** — propagating error gradients backward through the
stack.

**The linear-algebra skeleton.** Each layer's core is a linear map `z = Wx + b`
(theory/01) followed by a nonlinearity. Its local derivative is a Jacobian (bridge 1).
Backprop is the **chain rule** — and the chain rule for compositions of maps is
**matrix multiplication of Jacobians**, applied right-to-left. The "backward pass" is
literally a sequence of matrix-vector products with **transposed** weight matrices
`Wᵀ` (the transpose from the four-subspaces file — sending gradients back through the
map). Forward pass: `W`. Backward pass: `Wᵀ`. Same matrix, two directions — exactly
the input-side/output-side duality of Section 05.

**Why it matters.** "Backprop" sounds like deep-learning sorcery; it's the chain rule
expressed as chained Jacobian transposes. The hard part is bookkeeping, not new math.

---

## 5. Bridge to M23 (Transformers): the architecture is linear algebra + softmax

**The adjacent idea.** Transformers power modern LLMs. The headline mechanism is
**attention** — every token "attends to" every other token.

**The linear-algebra skeleton.** Attention is `softmax(QKᵀ / √d) V`. Strip the
softmax and it's *all* linear algebra you own:
- `Q, K, V` are the input embeddings hit by three learned **linear maps** (`Wx`).
- `QKᵀ` is a matrix of **dot products** (foundations/06) — every query·key alignment,
  the alignment meter computing token-to-token relevance.
- Dividing by `√d` is normalization; **softmax** is the only nonlinear step, turning
  alignments into weights that sum to 1.
- Multiplying by `V` is a **weighted linear combination** (theory/01) of value
  vectors — the one fundamental operation from foundations/03.

The feed-forward blocks are linear maps; the residual stream is vector addition; layer
norm is rescaling. **Remove softmax and a transformer is pure linear algebra.**

**Why it matters.** The most important architecture of the decade is, mathematically,
dot products + linear combinations + one softmax. You built the 90% that's linear.

---

## 6. Python: the shared skeleton across modules

Let's make the unity literal — one script touching all five bridges, showing the same
operations (matmul, transpose, dot product, eigen/SVD) reappear everywhere.

```python
import numpy as np
rng = np.random.default_rng(0)

# --- M02: gradient as the linear map giving directional derivatives ---
# f(x) = ½ xᵀAx → ∇f = Ax. Directional derivative = ∇f · direction (a dot product).
A = np.array([[3., 1.], [1., 2.]])
x = np.array([1., -1.])
grad = A @ x
direction = np.array([1., 0.])
print("M02  directional deriv = ∇f·dir:", grad @ direction)      # dot product

# --- M03/M04: covariance eigendecomposition == PCA via SVD ---
X = rng.normal(size=(200, 2)) @ np.array([[2., 0.], [1., 0.5]])  # correlated data
Xc = X - X.mean(0)
Sigma = np.cov(Xc.T)
eigvals, eigvecs = np.linalg.eigh(Sigma)                          # spectral theorem
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)                 # PCA via SVD
print("M03/M04  eigvals of Σ:", np.round(np.sort(eigvals)[::-1], 3))
print("         S²/(n-1)    :", np.round(np.sort(S**2 / (len(Xc)-1))[::-1], 3),
      " ← same numbers: PCA = SVD = eigen(Σ)")

# --- M21: backprop = chain rule = transposed-Jacobian matmul ---
W1 = rng.normal(size=(4, 2)); W2 = rng.normal(size=(1, 4))
h = W1 @ x                                   # forward through layer 1 (linear map W)
out = W2 @ h                                 # forward through layer 2
grad_h = W2.T @ np.array([1.0])              # backward: gradient flows through Wᵀ
grad_x = W1.T @ grad_h                       # ...and again — transpose sends it back
print("M21  backward pass uses Wᵀ, shape grad_x:", grad_x.shape)

# --- M23: attention = dot products + softmax + linear combination ---
def softmax(z): e = np.exp(z - z.max(-1, keepdims=True)); return e / e.sum(-1, keepdims=True)
Q = rng.normal(size=(3, 8)); K = rng.normal(size=(3, 8)); V = rng.normal(size=(3, 8))
scores = Q @ K.T / np.sqrt(8)                # dot-product alignment meter
attn = softmax(scores) @ V                   # weighted linear combination of values
print("M23  attention output shape:", attn.shape, "— dot products + softmax + lin. comb.")
```

Run it and the thesis of this section is on screen: the eigenvalues of the covariance
and the SVD singular-values-squared print the **same numbers** (M03 = M04), the
backward pass is `Wᵀ` matmuls (M21), and attention is a dot-product matrix fed through
softmax into a linear combination (M23). One skeleton, five modules.

---

## Section recap

- **M02 (Calculus):** Jacobian = matrix of partials = the best linear map
  approximating `f`; gradient = a linear functional read via dot product.
- **M03 (Probability):** covariance `Σ = QΛQᵀ`; the Gaussian's exponent is a quadratic
  form — an eigen-shaped ellipsoid.
- **M04 (Statistics):** regression = projection onto `C(A)`; PCA = SVD of centered
  data = eigendecomposition of `Σ`.
- **M21 (Neural nets):** backprop = chain rule = right-to-left products of (transposed)
  Jacobians; forward uses `W`, backward uses `Wᵀ`.
- **M23 (Transformers):** attention = dot products (`QKᵀ`) + softmax + linear
  combination (`·V`). Remove softmax → pure linear algebra.

**Explain out loud:** Pick *one* bridge and narrate it end to end without notes —
e.g. *"A transformer's attention is ___ then ___ then ___, and the only nonlinear
piece is ___."* If you can do one cleanly, you can do all five.

---

## Memory tier update — Section 10

**🔥 CARRY (memorize):**
- Gradient/Jacobian = linear approximation (M02); covariance eigendecomp = PCA = SVD
  (M03/M04); backprop = transposed-Jacobian chain (M21); attention = dot-products +
  softmax + linear combination (M23).

**🔧 RECONSTRUCT (re-derive when needed):**
- Why regression residuals are orthogonal to `C(A)` (projection, foundations/06).
- Why forward uses `W` and backward uses `Wᵀ` (chain rule on linear maps).

**📖 LOOKUP (reference, never memorize):**
- Exact attention scaling/masking details, multi-head bookkeeping.
- PCA-vs-SVD sign/ordering conventions across libraries.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Take the script above and verify the M03/M04 claim hard —
assert that `sorted(eigvals)` and `sorted(S**2/(n-1))` agree to numerical tolerance.
Then build a 2-layer net by hand and confirm your manual `Wᵀ` backward pass matches a
finite-difference gradient.

**Try this in Claude:** *"Trace the linear algebra through a transformer's forward
pass."* Ask Claude to annotate each step of `softmax(QKᵀ/√d)V` with the M01 concept it
uses (linear map, dot product, normalization, linear combination), and to point out
the *single* place the math leaves linear algebra (softmax). See if its trace matches
yours.

**Reflection prompt:** You just saw five "advanced" topics reduce to operations you
already own. Journal one line on which bridge surprised you most — and what it tells
you about how much of "advanced ML" is really linear algebra in a costume.
