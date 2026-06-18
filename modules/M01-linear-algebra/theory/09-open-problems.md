---
module: M01
formalism_density: 0.4
status: draft
learner_id: L001
title: "Open Problems, Limitations, and Research Frontiers"
calibration: "MIT 18.06 (Strang) — frontiers of applied linear algebra, ML emphasis"
---

# Section 9 — Open Problems, Limitations, and Research Frontiers

## 9.0 Bridge: knowing where the map ends

You've spent eight sections building fluency with linear algebra — vector spaces,
eigenvalues, SVD, attention, weight matrices. That toolkit is astonishingly
powerful. But a doctoral education isn't just "learn the tools"; it's "learn
exactly where the tools stop working, and what people are doing about it." The
edge of the map is where research lives.

So this final section is a tour of the cracks. Where does the clean, linear story
break down? Three places, mainly: **nonlinearity** (the world isn't linear, and
linear algebra is, by name, linear), **scale** (linear algebra's nice algorithms
choke when matrices have billions of entries), and **geometry** (the flat,
Euclidean intuitions you've built quietly betray you in high dimensions and on
curved data). Each crack is a live research frontier. Walking them is how you
turn "I know linear algebra" into "I know what linear algebra can't yet do" —
which is the more valuable thing.

---

## 9.1 Where linear algebra hits its limits

### Nonlinearity

The whole edifice you built assumes linear maps: $f(ax + by) = af(x) + bf(y)$.
That assumption is what makes everything tractable — superposition, eigenvectors,
SVD, all of it leans on linearity. But almost nothing interesting is linear.
Perception isn't, language isn't, decision-making isn't. We saw in Section 8 that
networks get *all* their expressive power from the nonlinear kinks between linear
maps. So linear algebra is the *scaffolding* of deep learning, never the building.
The frontier: we can analyze a single linear layer beautifully, but the
*composition* with nonlinearities — what the network as a whole computes — remains
largely a theoretical mystery. "Why does this trained net generalize?" has no
clean linear-algebraic answer.

### Billions of parameters

Classical linear algebra was designed for matrices you could hold in memory and
factor exactly. A modern model has weight matrices with billions of entries. You
cannot compute the SVD of a $50000\times 50000$ matrix the textbook way, let
alone the full Hessian of a billion-parameter network (which would have $10^{18}$
entries). Exact methods don't just get slow — they become *physically
impossible*. Every classical algorithm needs a scalable approximate cousin.

### Non-Euclidean data

Your geometric intuitions — distances, angles, "nearby means similar" — assume a
flat Euclidean space. But lots of real data lives on *curved* spaces or *discrete*
structures: molecules are graphs, social networks are graphs, 3D shapes are
manifolds, hierarchies are trees that embed naturally in *hyperbolic* (negatively
curved) space, not flat space. Standard linear algebra, built for $\mathbb{R}^n$,
doesn't natively respect that structure. Forcing graph or manifold data into flat
vectors loses the very geometry that matters.

> **Try this in Hermes:** "Quiz me: give an example of data where Euclidean
> distance is actively misleading, and say what kind of space would fit better."
> **Try this in Claude:** "Explain why a composition of linear layers needs the
> nonlinearity to be more than a single linear map — and why that makes the whole
> network hard to analyze linearly."

---

## 9.2 The curse of dimensionality: why $\mathbb{R}^2$ intuition lies

### Conceptual bridge

You build geometric intuition by drawing pictures in 2D and 3D. The quiet tragedy
is that those pictures *mislead you* in the high-dimensional spaces where ML
actually lives — embeddings of dimension 768, 4096, or more. High-dimensional
space is just *weird*, and the weirdness has a name: the curse of dimensionality.

### Two concrete weirdnesses

**Everything is far from everything, and equally so.** In high dimensions, the
distances between random points concentrate — the nearest and farthest neighbors
become almost the same distance away. "Nearest neighbor" loses meaning. This
breaks the intuition behind k-NN, clustering, and any method that leans on "close
= similar."

**Random vectors are nearly orthogonal.** Pick two random vectors in $\mathbb{R}^d$.
In 2D their angle is uniformly random. In $\mathbb{R}^{4096}$ they are almost
*always* nearly perpendicular (dot product near zero). This is counterintuitive —
and it's secretly *good news* for ML: it means a high-dimensional space can hold a
vast number of nearly-orthogonal "concept directions," which is part of why
embeddings can pack so much meaning. The same fact, two faces: a curse for
distance-based methods, a blessing for representation capacity.

### Worked example — watch the intuition break

```python
import numpy as np

def neighbor_ratio(d, n=1000):
    """In dimension d, how much farther is the farthest point than the nearest?
       Ratio -> 1 means 'nearest' and 'farthest' become meaningless."""
    pts = np.random.randn(n, d)
    q = np.random.randn(d)
    dists = np.linalg.norm(pts - q, axis=1)
    return dists.max() / dists.min()

for d in [2, 10, 100, 1000, 4096]:
    print(f"dim {d:>5}: farthest/nearest distance ratio = {neighbor_ratio(d):.3f}")
# Ratio collapses toward 1 as d grows -> 'nearest neighbor' stops being special.

# Near-orthogonality: average |cos angle| between random vectors shrinks with d
for d in [2, 10, 100, 4096]:
    a = np.random.randn(2000, d)
    a /= np.linalg.norm(a, axis=1, keepdims=True)
    cosines = np.abs(a[:1000] @ a[1000:].T).ravel()
    print(f"dim {d:>5}: mean |cos angle| between random vectors = {cosines.mean():.4f}")
# -> tiny in high d: random vectors are almost always nearly perpendicular.
```

Run it and *feel* the ratio collapse toward 1. That collapsing number is your 2D
intuition dying. Internalizing this is what stops you from trusting a pretty 2D
picture when you're really working in $\mathbb{R}^{4096}$.

> **Try this in Hermes:** "Make me predict the neighbor ratio for d=10000 before I
> run it, then explain why distance concentration happens."
> **Try this in Claude:** "Explain how near-orthogonality of random high-dim
> vectors enables superposition / feature packing in LLM embeddings."

---

## 9.3 Computational bottlenecks and approximation

### The $O(n^3)$ wall

Naive matrix multiplication of two $n\times n$ matrices costs $O(n^3)$ operations —
triple-nested loops. SVD, eigendecomposition, and solving linear systems are all
$O(n^3)$ too. That cubic scaling is fine for $n=1000$ but catastrophic for
$n=100000$: a $100\times$ bigger matrix costs $100^3 = 10^6\times$ more compute.
This wall is *the* reason large-scale ML can't just use textbook linear algebra.

There's a theoretical rabbit hole here too: Strassen's algorithm does
multiplication in about $O(n^{2.807})$, and the current record is roughly
$O(n^{2.37})$ — but whether you can get to $O(n^2)$ (the obvious lower bound,
since you must at least read the output) is a famous **open problem**. The
exponent of matrix multiplication is one of the genuinely unsolved questions in
the field.

### The escape: randomized and approximate methods

If exact is impossible, get a *good enough* answer fast — usually by *random
projection*. The key insight (Johnson–Lindenstrauss): you can squash
high-dimensional data into far fewer dimensions with a random matrix while
approximately preserving all pairwise distances. **Randomized SVD** uses this to
find the top-$k$ singular triplets of a giant matrix in roughly $O(n^2 k)$ instead
of $O(n^3)$ — sketch the matrix down with a random projection, do the expensive
work in the small sketched space, lift the answer back. When you only need the top
few components (which, per Section 8, is usually all that matters), this is a
massive win for a tiny approximation error.

### Worked example — naive vs. randomized SVD timing

```python
import numpy as np
import time

def randomized_svd(A, k, p=10):
    """Top-k SVD via random projection (Halko-Martinsson-Tropp, simplified).
       Sketch A onto a random k+p dim subspace, solve there, lift back."""
    n = A.shape[1]
    Omega = np.random.randn(n, k + p)     # random projection matrix
    Y = A @ Omega                          # sketch: capture A's dominant range
    Q, _ = np.linalg.qr(Y)                 # orthonormal basis of the sketch
    B = Q.T @ A                            # small: (k+p) x n
    Ub, S, Vt = np.linalg.svd(B, full_matrices=False)
    U = Q @ Ub
    return U[:, :k], S[:k], Vt[:k]

# A large, near-low-rank matrix (top-k is what we actually want)
np.random.seed(0)
n, k = 2000, 20
A = np.random.randn(n, k) @ np.random.randn(k, n) + 0.01 * np.random.randn(n, n)

t0 = time.perf_counter()
U_full, S_full, _ = np.linalg.svd(A, full_matrices=False)   # O(n^3)
t_full = time.perf_counter() - t0

t0 = time.perf_counter()
U_r, S_r, _ = randomized_svd(A, k)                          # ~O(n^2 k)
t_rand = time.perf_counter() - t0

print(f"full SVD       : {t_full*1000:8.1f} ms")
print(f"randomized SVD : {t_rand*1000:8.1f} ms   (speedup {t_full/t_rand:.1f}x)")
print(f"top-{k} singular value relative error: "
      f"{np.linalg.norm(S_full[:k]-S_r)/np.linalg.norm(S_full[:k]):.2e}")
# Big speedup, tiny error -- because we only ever needed the top-k components.
```

The randomized version returns the top components dramatically faster with
negligible error. This is not a toy — it's how SVD-based methods (PCA, recommender
factorization, LoRA initialization) actually run at scale.

> **Try this in Hermes:** "Walk me through the randomized SVD steps and why
> sketching to k+p dimensions preserves the top-k structure."
> **Try this in Claude:** "Explain the Johnson–Lindenstrauss lemma and why random
> projection preserves distances — what does the 'distortion' bound depend on?"

---

## 9.4 Open research directions

The cracks of §9.1 each spawned a thriving frontier:

- **Tensor methods for multi-modal data.** A matrix is a 2D array; a *tensor* is
  the n-dimensional generalization (think: a stack of matrices, or a (users ×
  items × time × context) array). Multi-modal data (vision + text + audio) and
  higher-order interactions don't flatten cleanly into matrices. Tensor
  decompositions (CP, Tucker, tensor-train) generalize SVD to these higher-order
  arrays — but they're harder: even computing tensor rank is NP-hard, and there's
  no clean Eckart–Young best-approximation guarantee. Active research: scalable,
  stable tensor factorization for fusing modalities.

- **Randomized linear algebra for scaling.** §9.3 was a first taste. The broader
  program ("RandNLA") asks: what's the *least* computation needed for a good-enough
  answer to every classical problem — least squares, low-rank approximation,
  leverage-score sampling? This is foundational to making trillion-parameter
  models tractable.

- **Geometric deep learning on manifolds and graphs.** This is the response to the
  non-Euclidean crack of §9.1. Instead of forcing data into flat $\mathbb{R}^n$,
  build operations that respect the data's native geometry: graph neural networks
  (for graphs), equivariant networks (that respect symmetries like rotation), and
  hyperbolic embeddings (for hierarchies/trees, which fit negatively-curved space
  far better than flat space). The unifying idea — "design the architecture around
  the data's symmetry group" — is one of the most active areas in modern ML, and
  it's where linear algebra blends into differential geometry and group theory.

The honest doctoral framing: linear algebra is the *necessary* foundation, but the
research frontier is everywhere it's *insufficient* — nonlinearity, scale, and
curvature. Knowing precisely where each begins is the difference between using the
tools and extending them.

---

## 9.5 Section recap

**Explain out loud (no notes):**
1. "Linear algebra hits three main limits, namely…" — name nonlinearity, scale,
   geometry, and one example of each.
2. "High-dimensional space is weird because…" — give the two facts (distance
   concentration, near-orthogonality) and which is a curse vs. a blessing.
3. "Exact SVD is $O(n^3)$, so at scale we…" — explain randomized SVD in one
   breath (sketch, solve small, lift back).
4. "Three live research frontiers are…" — tensors, randomized NLA, geometric deep
   learning, each tied to which limit it addresses.

If the high-dimensional weirdness still feels abstract, *rerun the §9.2 code* —
seeing the numbers move is the fastest way to retire your 2D intuition.

### Memory tiers for THIS section

**CARRY (memorize):**
- Linear algebra's three limits: nonlinearity, scale, non-Euclidean geometry
- Matrix multiply / SVD / eig are all $O(n^3)$ — the scaling wall
- High-dim facts: distances concentrate; random vectors are nearly orthogonal
- "Randomized methods trade a tiny error for a huge speedup, when you only need
  the top-$k$"

**RECONSTRUCT (re-derive):**
- Why $O(n^3)$ scaling makes a $100\times$ bigger matrix $10^6\times$ costlier
- Randomized SVD pipeline: random projection → QR → small SVD → lift
- The matching of frontier ↔ limit (tensors↔multi-modal, RandNLA↔scale,
  geometric DL↔curvature)

**LOOKUP (know it exists):**
- Johnson–Lindenstrauss distortion bounds; the matrix-multiply exponent record
- Tensor decomposition variants (CP, Tucker, tensor-train) and their costs
- Nyström method, leverage-score sampling, specific GNN/equivariant architectures

> **Closing interaction prompt —**
> **Try this in Hermes:** "Pick one frontier — tensors, randomized NLA, or
> geometric deep learning — and quiz me on which linear-algebra limit it addresses
> and how."
> **Try this in Claude:** "Explain the Nyström method for kernel approximation —
> how does it use a small subset of columns to approximate a giant kernel matrix,
> and how does that connect to the randomized-projection idea from §9.3?"
