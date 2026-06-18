---
module: M01
title: "Linear Algebra for ML"
artifact: theory-section
section: "01 — Vector Spaces and Linear Maps"
calibration: "MIT 18.06 (Strang), Lectures 1–10"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "foundations/01-primer.md"
---

# Section 1 — Vector Spaces and Linear Maps

## Opening — picking up the kindling

In the primer we lit a small fire: a **vector space** is a universe where you
can add and scale, and those two moves never throw you out of the universe. That
"never throw you out" property — *closure* — is the only magic word you need to
carry in. Everything in this section is a consequence of taking that one idea
seriously and asking the obvious follow-up questions: *How do I name points in
such a universe? What are the functions that respect its rules? And what is
conserved when I push the whole universe through one of those functions?*

We'll answer those three questions in order, and the answers are: **basis**,
**linear maps**, and the **rank–nullity theorem**. By the end you'll see that a
matrix — the spreadsheet you already know — is just a linear map in work clothes.

---

## 1. Abstract vector spaces

**Bridge.** You met `ℝⁿ` already: lists of `n` numbers, like `[0.3, −1.2, 5.0]`.
But here's the move that makes a mathematician (and an ML engineer) powerful:
the *list* was never the point. The point was the **rules** — add, scale, stay
in the box. Anything obeying those rules is a vector space, even if its
"vectors" are functions, or images, or 768-dimensional embeddings. We abstract
away the container and keep the behavior.

**Bridge, second pass.** Why bother abstracting? Because a theorem proved about
"any vector space" instantly applies to *all* of them — pixel images, weight
tensors, polynomial functions, audio signals. You prove once, you reap
everywhere. That's the leverage of abstraction (the good kind).

**Formal definition.** A *vector space* over `ℝ` is a set `V` with two operations
— addition `+ : V×V → V` and scalar multiplication `· : ℝ×V → V` — satisfying
eight axioms (commutativity/associativity of `+`, a zero `0`, negatives `−v`,
distributivity of scalars over vectors and vectors over scalars, and `1·v = v`).
Both operations land back *inside* `V` — that's closure, baked into the arrows.

**Operational intuition (what it DOES, not what it looks like):** A vector space
is a machine with two buttons. Button A takes two elements and fuses them into
one. Button S takes one element and a dial setting (a scalar) and stretches or
flips it. The axioms are just the promise that the buttons behave predictably —
press them in any order, you get consistent, in-the-box results. You operate the
machine; you don't need to *picture* it.

> ✋ **Checkpoint 1.** The set of all degree-≤2 polynomials `{a + bx + cx²}` is a
> vector space. Convince yourself: add two of them → still degree ≤ 2 ✅. Scale
> one by 7 → still degree ≤ 2 ✅. Closed. It behaves *exactly* like `ℝ³` with
> coordinates `(a,b,c)`. Same machine, different paint.

---

## 2. Linear independence, basis, dimension — the alphabet of the space

**Bridge.** If a vector space is a universe of points, we need a way to *name*
every point without writing them all down (there are infinitely many). The trick
is the same one the alphabet uses: pick a small set of fundamental pieces, and
build everything else by combining them. Those fundamental pieces are a
**basis**, and combining = add-and-scale (which is all we have anyway).

**Span — what you can reach.** The `span` of a set of vectors is *every* point you
can make by scaling them and adding the results. `span{[1,0],[0,1]}` is the whole
plane `ℝ²` — those two reach everywhere.

**Linear independence — no wasted letters.** A set is *linearly independent* if
no vector in it is reachable from the others — none is redundant. Formally:
`α₁v₁ + … + αₙvₙ = 0` forces *all* `αᵢ = 0`. Operationally: nobody in the set is
a leftover; remove any one and you lose reach.

**Basis.** A *basis* is a set that is **both** spanning (reaches everything)
**and** independent (nothing wasted). It's the Goldilocks set — just enough
directions to name every point, with no duplicates.

**Dimension.** Every basis of a given space has the *same* number of vectors.
That number is the **dimension**, `dim V`. It's the count of independent
directions — the number of dials you must set to specify one point.

> ✋ **Checkpoint 2.** In `ℝ³`, is `{[1,0,0],[0,1,0],[1,1,0]}` a basis? Say it
> out loud before reading on. → **No.** The third is `first + second` — wasted
> letter. They only span the `z=0` plane (a 2-D subspace). Independence fails.

**Operational subspace description:** A *subspace* is a vector space living
inside a bigger one — a sealed sub-sandbox. The `z=0` plane inside `ℝ³` is a
subspace: add or scale anything in it, you stay in it. Subspaces are where ML
"compression" happens — more on that below.

---

## 3. The rank–nullity theorem — conservation of information

**Bridge.** Here is the emotional center of the whole section. When you push a
vector space through a linear map, some directions survive and come out the other
side; other directions get *crushed flat to zero*. The theorem says: **nothing
vanishes by accident — every input dimension is accounted for, either as
survived-output or as crushed-to-zero.** It's a conservation law, like energy.

**The two buckets.**
- **Kernel** (`ker T`, the *null space*): the directions the map crushes to `0`.
  Its dimension is the **nullity**.
- **Image** (`Im T`, the *range*): the directions that survive as output. Its
  dimension is the **rank**.

**Rank–nullity theorem.** For a linear map `T : V → W` with `V` finite-dimensional:

```
        dim(V)        =        rank(T)        +        nullity(T)
   ┌──────────────┐      ┌──────────────┐         ┌──────────────┐
   │ input dims    │  =   │ survives (Im) │    +    │ crushed (ker) │
   └──────────────┘      └──────────────┘         └──────────────┘
```

**Operational reading:** count the dials going in. Each one either turns
something on the output side (counts toward rank) or does nothing because the map
ignores it (counts toward nullity). The books always balance. If you have a
`5 → 3` map and the rank is 3, then nullity is `5 − 3 = 2`: two input directions
are silently discarded. *That discarding is exactly what dimensionality reduction
and lossy compression are.*

> ✋ **Checkpoint 3.** A map `T : ℝ⁴ → ℝ⁴` has a 1-dimensional kernel. What's its
> rank? Say it. → `4 − 1 = 3`. One direction is crushed; three survive. The map
> is *not* invertible (something was lost — you can't un-crush a zero).

---

## 4. Linear maps and matrices — the bridge from abstract to computational

**Bridge.** We've been speaking of `T` as an abstract function. Time to cash it
out into numbers you can run. The key fact — and it's almost too convenient — is
that **once you fix a basis, every linear map becomes a matrix, and every matrix
is a linear map.** They're the same object in two outfits: `T` is the idea, `A`
is the implementation.

**Why a matrix captures the whole map.** A linear map respects add-and-scale, so
it is *completely determined by what it does to the basis vectors*. Tell me where
the basis goes, and by linearity I can compute where *everything* goes. So we
just record "where each basis vector lands" — and those landing spots, stacked as
columns, **are the matrix**. That's it. The columns of `A` are the images of the
basis vectors.

**Formal statement.** For `T : ℝⁿ → ℝᵐ`, there is a unique `m×n` matrix `A` with
`T(v) = A v` for all `v`. Composition of maps becomes matrix multiplication;
the kernel of `T` is the null space of `A`; the image of `T` is the column space
of `A`; `rank(T) = rank(A)`.

> ✋ **Checkpoint 4.** A neural-network linear layer is `f(x) = Wx + b`. Strip the
> `+b`. Is `x ↦ Wx` a linear map? → **Yes** — it respects add-and-scale, so it's
> exactly an `A`. The `+b` is a *shift* (affine, not linear), which is why we
> sometimes fold `b` in via a homogeneous coordinate. Good instinct to notice it.

---

## 5. Python computational example

Let's *see* basis, dimension, and rank with our hands. (Computational only —
that's how we work. Run this; predict each output before you do.)

```python
import numpy as np
from sympy import Matrix

# A matrix whose 3rd column is (col1 + col2): a deliberately "wasted" direction.
A = np.array([
    [1.0, 0.0, 1.0],
    [0.0, 1.0, 1.0],
    [0.0, 0.0, 0.0],
])

# RANK: how many independent directions survive the map (size of the image)?
print("rank(A)      =", np.linalg.matrix_rank(A))      # -> 2

# NULLITY via rank-nullity: dim(domain) - rank. Domain is R^3 (3 columns).
n_cols = A.shape[1]
rank   = np.linalg.matrix_rank(A)
print("nullity      =", n_cols - rank)                 # -> 1  (3 - 2)

# Confirm the kernel directly: SymPy gives a basis for the null space.
kernel = Matrix(A).nullspace()
print("kernel basis =", kernel)        # -> one vector ~ [1, 1, -1]: col1+col2-col3 = 0

# A basis for the COLUMN SPACE (the image) — which directions survived:
col_space = Matrix(A).columnspace()
print("image dim    =", len(col_space))                # -> 2
```

```
rank(A)      = 2
nullity      = 1
kernel basis = [Matrix([[1],[1],[-1]])]
image dim    = 2
```

**Read the output as the theorem:** `dim(domain) = 3 = rank(2) + nullity(1)`. ✅
The books balanced. The kernel vector `[1,1,−1]` is the algebraic proof that
"column 3 = column 1 + column 2" — the wasted letter from Checkpoint 2, now found
by code, not by eye.

> ✋ **Checkpoint 5.** Change `A`'s third column to `[2.0, 1.0, 0.0]` and re-run.
> Predict first: does rank go to 3? does the kernel collapse to just the zero
> vector? Run it and confront your prediction. (This is the whole skill: predict,
> run, reconcile.)

---

## 6. Applications to ML

The conservation law isn't a curiosity — it's the budget sheet of modern models.

- **Parameter spaces.** A model with `n` weights lives in `ℝⁿ`. Training walks a
  path through that space; the reachable behaviors are governed by which
  directions in parameter space actually *change the output* (rank) versus which
  are flat/redundant (kernel-like). Flat directions are why many different weight
  settings give identical loss.
- **LoRA compression.** Low-Rank Adaptation freezes a big weight matrix `W` and
  learns a *low-rank* update `ΔW = BA`, where `B` is `d×r` and `A` is `r×d` with
  `r ≪ d`. By rank–nullity, that update can only move the output within an
  `r`-dimensional image — you've *deliberately chosen a small rank* to slash the
  number of trainable parameters from `d²` to `2dr`. LoRA is rank–nullity used as
  an engineering knob. Eureka: the theorem is a compression dial.
- **Embedding dimensions.** Choosing `ℝ⁷⁶⁸` for embeddings is choosing a
  dimension — the number of independent semantic directions the model may use.
  Too few and distinct concepts get crushed together (forced into one kernel);
  too many and you waste capacity on directions nothing fills.

---

## 7. Section recap

We climbed the ladder rung by rung:

1. A **vector space** is the add-and-scale universe (closure is its soul).
2. A **basis** is the minimal alphabet; its size is the **dimension**.
3. A **linear map** is a function that respects add-and-scale, fully pinned down
   by where it sends the basis.
4. Fixing a basis turns every map into a **matrix** (columns = images of basis
   vectors) and back.
5. **Rank–nullity** is conservation of dimension: `dim(domain) = rank + nullity`.
   What doesn't survive as output was crushed into the kernel — and that crushing
   *is* compression (LoRA, dimensionality reduction, embedding bottlenecks).

> 🗣️ **Explain out loud (do this before moving on):** In your own words, with no
> notation, answer — *"When I push a 5-dimensional space through a linear map and
> 2 dimensions land in the kernel, what is the rank, and what does that mean for
> what the map can and cannot produce?"* If you can answer cleanly, you own this
> section.

---

## 8. Memory tier update (from THIS section)

### 🔥 CARRY (add to your campfire)
- Columns of a matrix = where the basis vectors land. (This unlocks everything.)
- `dim(domain) = rank + nullity` — and it's a *conservation* law, not a formula
  to memorize cold.
- Kernel = crushed-to-zero directions; Image = surviving directions.

### 🔧 RECONSTRUCT
- Why a map is determined by its action on a basis (rebuild from linearity).
- The dimension-counting argument behind rank–nullity.

### 📖 LOOKUP
- `np.linalg.matrix_rank`, `sympy.Matrix(...).nullspace()`, `.columnspace()`,
  `.rref()` — signatures and return shapes.

---

## 9. Interaction prompt

> **Try this in Hermes:** "Show me three different `4×4` matrices: one full rank,
> one with a 1-dimensional kernel, one with a 2-dimensional kernel. For each,
> verify rank + nullity = 4 in NumPy, and explain in one sentence what got
> crushed." Then predict each rank *before* running.

> **Try this in Claude:** "I think LoRA's rank `r` is just the rank of the update
> matrix `ΔW`. Push back on me — where does that intuition break, and how does
> rank–nullity bound what a rank-`r` adapter can and cannot change about the
> frozen layer's output?" Argue your side; make it defend the correction.
