---
module: M01
title: "Linear Algebra for ML"
artifact: theory-section
section: "02 — Inner Products, Norms, and Geometry"
calibration: "MIT 18.06 (Strang), Lectures 14–17"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "theory/01-vector-spaces.md"
---

# Section 2 — Inner Products, Norms, and Geometry

## Pre-reading map — what we're about to build

In Section 1 we had two things: a **universe** (the vector space, where you can
add and scale) and a **map** (the linear function, which respects those moves).
That's a lot of power, but it's a *blind* power. We could move points around, but
we had no way to ask the two questions every geometer — and every ML engineer —
eventually needs:

- **"How far apart are these two points?"** (distance)
- **"Do these two directions agree, disagree, or ignore each other?"** (angle)

This section installs the single piece of machinery that answers both: the
**inner product**. From it, distance and angle fall out for free. The route:

```
inner product  ──gives──▶  norm (length)  ──gives──▶  distance
      │
      └──gives──▶  angle  ──special case──▶  orthogonality (perfect indifference)
                                                   │
                                                   └──enables──▶  projection
                                                                      │
                                                                      └──is──▶  least squares
```

Everything downhill of "inner product" is a consequence of that one definition.
Hold onto that — it's the through-line.

---

## 1. The inner product

**Bridge.** You already have an intuition for "these two things point the same
way." Two embedding vectors for *king* and *queen* feel like they should align;
*king* and *banana* should not. The inner product is the machine that turns that
fuzzy feeling into one number. Operationally: **an inner product is a function
that eats two vectors and spits out a single number telling you how much they
align** — big and positive when they point together, zero when they're
indifferent, negative when they oppose.

**Bridge, second pass.** Why a *number* and not a yes/no? Because alignment is a
dial, not a switch. Attention in a transformer doesn't ask "is this token
relevant — yes or no?"; it asks "*how* relevant, on a continuous scale?" That
continuous answer is an inner product. You are about to learn the literal
arithmetic behind attention scores.

**Definition.** An **inner product** on a real vector space `V` is a function
`⟨·,·⟩` (read "angle brackets") that takes two vectors `u, v ∈ V` and returns a
real number `⟨u, v⟩ ∈ ℝ`, satisfying three rules:

1. **Symmetry:** `⟨u, v⟩ = ⟨v, u⟩` — alignment doesn't care about order.
2. **Linearity in the first slot:** `⟨au + bw, v⟩ = a⟨u, v⟩ + b⟨w, v⟩` — it
   respects the add-and-scale moves from Section 1.
3. **Positive-definiteness:** `⟨v, v⟩ > 0` for every `v ≠ 0`. A nonzero vector
   always has positive alignment *with itself*. (This is the rule that secretly
   defines length, as we'll see.)

`u, v` — two vectors in the space. `a, b` — scalars (plain numbers). `w` — a
third vector, present only to show linearity.

**The one you'll use 99% of the time** is the **dot product** on `ℝⁿ`:

```
⟨u, v⟩  =  u₁v₁ + u₂v₂ + ... + uₙvₙ  =  Σᵢ uᵢ vᵢ
```

Multiply componentwise, then sum. That's it. In NumPy it's `u @ v`. The whole
edifice of geometry below is built on this one humble line.

```python
import numpy as np

king   = np.array([0.9, 0.1, 0.8])   # toy 3-D "embeddings"
queen  = np.array([0.8, 0.2, 0.9])
banana = np.array([-0.5, 0.9, -0.3])

print("king · queen :", king @ queen)    # large positive — they align
print("king · banana:", king @ banana)   # negative — they oppose
```

The dot product just *measured a relationship* with a single number. No diagram,
no protractor — pure arithmetic.

---

## 2. Norm, distance, orthogonality

**Bridge.** Once you can measure alignment, the *length* of a vector is just its
alignment with itself. A vector that strongly agrees with itself is long; the
zero vector agrees with nothing, not even itself, and has length zero. So length
isn't a new idea — it's the inner product looking in a mirror.

**Norm (length).** The **norm** of `v`, written `‖v‖` ("norm of v"), is

```
‖v‖  =  √⟨v, v⟩  =  √(v₁² + v₂² + ... + vₙ²)
```

This is the Pythagorean theorem wearing a lab coat. In ML this exact quantity is
the **L2 norm** — the thing weight decay shrinks, the thing gradient clipping
caps.

**Distance.** The distance between two points is the length of the arrow from one
to the other:

```
dist(u, v)  =  ‖u − v‖
```

Subtract to get the connecting arrow, then take its length. This is the
Euclidean distance you'd use in k-nearest-neighbors.

**Angle.** Rearranging the geometric identity `⟨u, v⟩ = ‖u‖‖v‖cos θ` gives the
angle between two vectors:

```
cos θ  =  ⟨u, v⟩ / (‖u‖ ‖v‖)
```

`θ` ("theta") — the angle between the two vectors. The right-hand side is exactly
**cosine similarity**, the workhorse of every embedding search you've ever run.
It strips out length and keeps only *direction*: are these two things pointing the
same way, regardless of how "loud" each one is?

**Orthogonality.** When `⟨u, v⟩ = 0`, we say `u` and `v` are **orthogonal**
(perpendicular). `cos θ = 0`, so `θ = 90°`. Operationally: **orthogonal vectors
are perfectly indifferent to each other** — knowing your position along one tells
you nothing about your position along the other. This is the geometric heart of
"independent features," and it's why we love orthogonal bases: they're
coordinate systems with zero cross-talk.

```
   v
   ▲
   │              orthogonal: the shadow of u onto v is a single point.
   │              u contributes NOTHING in the v direction.
   └────────▶ u
```

```python
u = np.array([3.0, 0.0])
v = np.array([0.0, 4.0])

norm_u = np.linalg.norm(u)                 # 3.0
dist   = np.linalg.norm(u - v)             # 5.0  (3-4-5 triangle!)
cos    = (u @ v) / (norm_u * np.linalg.norm(v))

print("‖u‖       :", norm_u)
print("dist(u,v) :", dist)
print("cos θ     :", cos, "→ orthogonal" if np.isclose(cos, 0) else "")
```

---

## 3. Cauchy–Schwarz — the inequality that keeps cosine honest

**Bridge.** We just wrote `cos θ = ⟨u, v⟩ / (‖u‖‖v‖)` and breezily called it
cosine similarity. But a cosine *must* live between `−1` and `+1`. Who guaranteed
that the fraction on the right never blows past 1? If it could, "cosine
similarity" would be a lie. The guarantee has a name.

**Cauchy–Schwarz inequality.** For any two vectors,

```
|⟨u, v⟩|  ≤  ‖u‖ ‖v‖
```

In words: **the alignment of two vectors can never exceed the product of their
lengths.** Equality happens *only* when the vectors are parallel (one is a scalar
multiple of the other). The intuition: alignment is maximized when the vectors
point exactly the same way; tilt one even slightly and some of its "agreement"
leaks off into a perpendicular direction, and the dot product drops.

Divide both sides by `‖u‖‖v‖` and you get `|cos θ| ≤ 1` — cosine similarity is
*forced* to behave. That's not a convention; it's a theorem. It's also the
backbone of nearly every error bound in ML: whenever you see a proof bound a dot
product by a product of norms, that's Cauchy–Schwarz doing the heavy lifting.

```python
rng = np.random.default_rng(0)
for _ in range(3):
    u, v = rng.normal(size=5), rng.normal(size=5)
    lhs = abs(u @ v)
    rhs = np.linalg.norm(u) * np.linalg.norm(v)
    print(f"|u·v| = {lhs:6.3f}  ≤  ‖u‖‖v‖ = {rhs:6.3f}   {'✓' if lhs <= rhs + 1e-9 else '✗'}")
```

It never fails. It *can't* — that's the whole point of proving things.

---

## 4. Projection — casting a shadow onto a subspace

**Bridge.** Here's a question that sounds abstract but is the secret engine of
regression: *"I have a target vector `b`, and a subspace I'm allowed to live in
(say, all the vectors my model can actually produce). `b` is probably not in that
subspace. What's the closest point in the subspace to `b`?"* The answer is the
**projection** of `b` onto the subspace — the shadow `b` casts when light shines
straight down onto the subspace's "floor."

**Projection onto a single vector.** The shadow of `b` onto the direction `a` is

```
proj_a(b)  =  ( ⟨a, b⟩ / ⟨a, a⟩ ) · a
```

Read it operationally: `⟨a, b⟩ / ⟨a, a⟩` is *how many copies of `a`* you need;
multiply by `a` to actually lay them down. The leftover, `b − proj_a(b)`, is
**orthogonal** to `a` — it's the part of `b` that `a` simply cannot explain.

```
        b
        ╱│
       ╱ │  ← residual  (b − proj),  orthogonal to a
      ╱  │
     ╱   ▼
    ●━━━━━━━━━━▶ a
    proj_a(b)
   (the shadow)
```

**Projection onto a subspace.** When the subspace is the **column space** of a
matrix `A` (all vectors you can build as `Ax`), the projection of `b` is

```
proj(b)  =  A (AᵀA)⁻¹ Aᵀ b
```

`Aᵀ` — `A` transpose (rows and columns swapped). `(AᵀA)⁻¹` — the inverse of the
small square matrix `AᵀA`. The matrix `P = A(AᵀA)⁻¹Aᵀ` is the **projection
matrix**: hand it any `b` and it returns the closest point in `A`'s column space.
Don't memorize the formula yet — memorize the *story*: drop a perpendicular from
`b` to the subspace, land on the closest point.

```python
A = np.array([[1.0, 0.0],
              [0.0, 1.0],
              [1.0, 1.0]])          # column space = a 2-D plane inside ℝ³
b = np.array([2.0, 3.0, 0.0])       # a target NOT on that plane

P = A @ np.linalg.inv(A.T @ A) @ A.T
proj = P @ b

residual = b - proj
print("projection of b :", proj)
print("residual         :", residual)
print("residual ⟂ plane?:", np.allclose(A.T @ residual, 0))  # True
```

That `True` is the punchline: the leftover is orthogonal to everything in the
subspace. The shadow is the *closest* point precisely because what's left over
points straight "up," away from the floor.

---

## 5. Least squares IS projection

**Bridge.** Now the cross-domain payoff. Linear regression asks: "find weights
`x` so that `Ax` is as close as possible to the targets `b`." But we *just* found
the closest point in `A`'s column space to `b` — that's the projection! So
least-squares regression isn't a separate technique; **it's projection wearing a
data-science costume.**

We want `Ax ≈ b`. Since `b` usually isn't reachable, we settle for making `Ax`
equal to the *projection* of `b`. The residual `b − Ax` must be orthogonal to
every column of `A`, which means `Aᵀ(b − Ax) = 0`. Rearrange:

```
AᵀA x  =  Aᵀ b          ← the NORMAL EQUATIONS
```

"Normal" here means "perpendicular" — the equations literally encode *the
residual is normal (orthogonal) to the column space.* Solve for `x` and you've
done least-squares regression, derived from nothing but the geometry of shadows.

```python
# Fit a line y = m·t + c to noisy data — least squares from scratch.
t = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([1.1, 2.9, 5.2, 6.8, 9.1])      # ≈ 2t + 1 with noise

A = np.column_stack([t, np.ones_like(t)])     # columns: [t, 1]

# Normal equations: solve AᵀA x = Aᵀy
x_normal = np.linalg.solve(A.T @ A, A.T @ y)
# NumPy's purpose-built solver (more numerically stable — see Section 5)
x_lstsq, *_ = np.linalg.lstsq(A, y, rcond=None)

print("slope, intercept (normal eqs):", x_normal)
print("slope, intercept (lstsq)     :", x_lstsq)
```

Both recover roughly `[2, 1]`. You just built regression out of inner products.
(One caution we'll cash out in Section 5: forming `AᵀA` squares the conditioning
and can be numerically nasty — that's why `lstsq` and QR exist. File that away.)

---

## 6. Where this lives in ML

- **Attention scores.** A transformer computes `score(qᵢ, kⱼ) = ⟨qᵢ, kⱼ⟩ / √d` —
  a scaled inner product between a *query* and a *key*. Every attention weight you
  have ever seen is Section 2.1 with a normalization constant. The softmax that
  follows just turns those alignment numbers into a probability distribution.
- **Cosine similarity** for embeddings (semantic search, RAG retrieval,
  deduplication) is `⟨u,v⟩/(‖u‖‖v‖)` verbatim — direction-only alignment, kept in
  `[−1, 1]` by Cauchy–Schwarz.
- **Least squares / projection** underlies linear regression, the closed-form
  solution layer of many models, and the "project onto the feasible set" step in
  constrained optimization.
- **Orthogonality** is why we prize orthogonal weight initializations and
  orthogonal bases (Section 4's SVD): zero cross-talk between directions keeps
  gradients well-behaved.

---

## Section recap

- An **inner product** `⟨u,v⟩` is a function returning one number that measures
  how much two vectors align (dot product: multiply componentwise, sum).
- **Norm** `‖v‖ = √⟨v,v⟩` is length; **distance** is `‖u−v‖`; **angle** comes from
  `cos θ = ⟨u,v⟩/(‖u‖‖v‖)` — exactly cosine similarity.
- **Orthogonal** (`⟨u,v⟩=0`) means perfectly indifferent / perpendicular.
- **Cauchy–Schwarz** (`|⟨u,v⟩| ≤ ‖u‖‖v‖`) is what forces cosine into `[−1,1]`.
- **Projection** finds the closest point in a subspace by dropping a
  perpendicular; the projection matrix is `P = A(AᵀA)⁻¹Aᵀ`.
- **Least squares** is projection in disguise; its **normal equations** are
  `AᵀA x = Aᵀb`, encoding "the residual is orthogonal to the column space."

**Explain out loud:** Without looking, say *why* least-squares regression and
"casting a shadow onto a subspace" are the same operation. If you can narrate the
residual being perpendicular to the column space, you own this section.

---

## Memory tier update — Section 2

**CARRY (memorize — these are reflexes):**
- Dot product = componentwise multiply then sum (`u @ v`).
- `‖v‖ = √⟨v,v⟩`; orthogonal ⇔ `⟨u,v⟩ = 0`.
- `cos θ = ⟨u,v⟩/(‖u‖‖v‖)` is cosine similarity.

**RECONSTRUCT (re-derive when needed, don't memorize):**
- Single-vector projection `(⟨a,b⟩/⟨a,a⟩)·a` — rebuild from "how many copies of a."
- The normal equations `AᵀA x = Aᵀb` — rebuild from "residual ⟂ column space."

**LOOKUP (know it exists, fetch the formula):**
- The full projection matrix `A(AᵀA)⁻¹Aᵀ`.
- Exact attention scaling constant (`1/√d`).

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Pull two embeddings for words you expect to be related
(*doctor*/*nurse*) and two you expect to be unrelated (*doctor*/*asphalt*).
Compute cosine similarity for both pairs by hand with `u @ v / (‖u‖‖v‖)`. Does
the geometry match your intuition? Where does it surprise you?

**Try this in Claude:** Ask Claude to walk you through how scaled dot-product
attention turns query/key inner products into attention weights, then have it
point to the exact line in a transformer implementation where the dot product
happens. Connect that line back to Section 2.1 — convince yourself they're the
same arithmetic.

**Reflection prompt:** You're a strong programmer — you've written `sum(a*b for
a,b in zip(u,v))` a hundred times without calling it geometry. How does it feel
to learn that this throwaway loop is *the* measurement underneath attention and
semantic search? Jot a sentence for the research journal about a moment where a
"boring" piece of code turned out to be load-bearing.
