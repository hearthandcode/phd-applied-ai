---
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "01 — Primer"
calibration: "MIT 18.06 (Strang)"
formalism_density: 0.4
status: draft
learner_id: L001
---

# Primer — Lighting the Fire Before the Theory

> This file is not a summary. It is a **warm-up for working memory**. Read it
> *before* you open `theory/01-vector-spaces.md`. Its only job is to make sure
> that when the formal definitions arrive, your head already has a place to put
> them. Think of it as laying the kindling before you strike the match.

---

## 1. Pre-reading map — the order is the lesson

We are going to build one idea, brick by brick, and the order is deliberate.
Here's the route, and *why* each step comes where it does:

```
   [ vectors as objects ]            you already half-know this — start from comfort
            │
            ▼
   [ vector SPACE ]                  the "universe" those objects live in
            │
            ▼
   [ basis & dimension ]             the minimal alphabet that names everything
            │
            ▼
   [ linear maps ]                   functions that respect the universe's rules
            │
            ▼
   [ matrices ]                      the *spreadsheet* form of a linear map
            │
            ▼
   [ rank–nullity ]                  the conservation law tying it all together
```

Why this order? Because every later idea is **defined in terms of an earlier
one**. You cannot say "dimension" until you have "basis." You cannot say
"matrix" honestly until you have "linear map." We climb the ladder; we never
skip a rung. If a definition ever feels like it came from nowhere, scroll *up* —
the missing rung is always above.

**Dependency callout:** This primer assumes you can multiply a matrix by a
vector in NumPy and that you've *seen* the word "eigenvalue." That's it. No
unified framework required — we're building that framework right now.

---

## 2. Symbol reference card

Keep this open in a split pane. The single biggest source of "I'm lost" in
linear algebra is not hard ideas — it's forgetting what a squiggle means.
(Working-memory tax. We refuse to pay it.)

| Symbol | Read it as | Plain-English meaning |
|---|---|---|
| `V`, `W` | "vee", "double-u" | A vector space — a universe where add & scale work |
| `v`, `w` | bold lowercase | A single vector — one point/arrow/data-row in that universe |
| `ℝ` | "the reals" | Ordinary numbers (1.5, −7, π). Our scalars. |
| `ℝⁿ` | "R-n" | All lists of `n` real numbers — the most common vector space |
| `α`, `c` | "alpha", "cee" | A **scalar** — a plain number you scale a vector by |
| `dim V` | "dimension of V" | How many numbers you need to name any point in `V` |
| `T` | "tee" | A **linear map** — a structure-respecting function `V → W` |
| `A` | matrix `A` | The spreadsheet of numbers that *implements* a map `T` |
| `ker T` | "kernel of T" | Everything that `T` crushes to zero (the **null space**) |
| `Im T` | "image of T" | Everything `T` can actually produce (the **range**) |
| `rank A` | "rank" | Size of the image — how much survives the map |
| `∈` | "in" / "is a member of" | `v ∈ V` means "v lives in space V" |
| `span{…}` | "span of" | All points reachable by adding & scaling the listed vectors |

**Inline rule:** every time one of these appears in the theory file, it gets
re-defined *in the sentence*. You should never have to remember a symbol across
a page break.

---

## 3. What you already know (we start from comfort)

You are a programmer. You already own three intuitions that *are* linear algebra
wearing a disguise:

- **A matrix is a data table.** A spreadsheet. Rows are records, columns are
  features. You've held this in your hands a thousand times. ✅
- **Scaling a number stretches it.** `3 * x` makes `x` bigger. Multiplying a
  whole row of numbers by 3 is the *exact same move*, done in parallel. ✅
- **Adding coordinates combines positions.** `[1,2] + [3,0] = [4,2]`. You've
  done this in every game loop where two velocities combine. ✅

Hold onto these. The entire abstract theory is just these three moves —
**scale, add, and "keep the rules consistent"** — promoted to adults. When the
formalism gets dense, your escape hatch is always: *"this is just scaling and
adding a spreadsheet."*

---

## 4. What is a vector space?

**Bridge (read this first, slowly).** Imagine a sandbox with exactly two legal
operations: you may **add** any two things in it, and you may **scale** anything
in it by a number. And here's the catch that makes it a *space* and not just a
pile of stuff: doing those operations can never throw you *out* of the sandbox.
Add two things in the box → result is still in the box. Scale something → still
in the box. The space is **closed** under its own operations. That closure is
the whole personality of the thing.

**Bridge, second pass (for the dense part).** "Closed" sounds bureaucratic but
it's the load-bearing wall. It's what lets you reason about *infinitely many*
points by only checking the rules, never the points. You verify the sandbox is
sealed once, and then every combination you'll ever build is guaranteed legal.

**Formal definition.** A *vector space* `V` over the reals `ℝ` is a set equipped
with addition (`v + w`) and scalar multiplication (`α · v`) such that addition
is commutative and associative, there's a zero vector `0`, every `v` has a
negative `−v`, and scaling distributes over both kinds of addition
(`α(v+w) = αv + αw` and `(α+β)v = αv + βv`), with `1·v = v`. Eight axioms — but
they all encode one idea: *add and scale, and never leave the box.*

**The intuition, one line to carry:**
> A vector space is a universe where **addition and scaling always make sense**
> and never kick you out.

---

## 5. Why this matters for ML (the payoff)

This is not abstract decoration. In machine learning you are *living inside*
vector spaces whether you name them or not:

- **Parameter spaces are vector spaces.** Every weight configuration of a
  neural network is one point in a giant `ℝⁿ`. Training is a *walk* through that
  space. Gradient descent only works because adding a gradient step keeps you in
  the space.
- **Embeddings live in vector spaces.** A word, a face, a molecule → a point in
  `ℝ⁷⁶⁸` (or wherever). "King − man + woman ≈ queen" is *literally* the add-and-
  scale rules from Section 4 doing semantic work.
- **Every neural-network layer defines one.** A linear layer `Wx + b` is a
  linear map (Section 5 of the theory) plus a shift. The whole forward pass is a
  relay race of maps between vector spaces.

When you understand the space, you understand the *shape of what's possible* for
a model — before you train a single epoch.

---

## 6. Memory tier summary (for this module)

Your working memory is precious. We tier everything. **Do not try to memorize
the LOOKUP tier — that's a feature, not laziness.**

### 🔥 CARRY — memorize these (max 7; these are the campfire you never let die)
1. Vector space = a universe where add & scale never kick you out (closure).
2. Basis = the minimal set of directions that names every point.
3. Dimension = how many numbers you need (= size of a basis).
4. Linear map = a function that respects add & scale: `T(αv+βw)=αT(v)+βT(w)`.
5. Matrix = the spreadsheet form of a linear map.
6. Kernel = what gets crushed to zero; Image = what can be produced.
7. **Rank–nullity:** `dim(domain) = rank + nullity`. Nothing is lost, only sorted.

### 🔧 RECONSTRUCT — re-derive when needed (don't memorize, *rebuild*)
- The 8 vector-space axioms (rebuild from "add & scale, stay in the box").
- Why a basis must be both spanning *and* independent.
- The proof sketch of rank–nullity (count the dimensions on each side).

### 📖 LOOKUP — keep a reference open, never memorize
- Exact axiom list and their formal names.
- NumPy/SymPy function signatures (`np.linalg.matrix_rank`, `Matrix.rref`, …).
- Specific embedding dimensionalities of named models.

---

**Explain-out-loud check before you proceed:** Without scrolling up, say aloud —
*"A vector space is ___, and the reason it matters for ML is ___."* If both
blanks come easily, the kindling is lit. Open `theory/01-vector-spaces.md`.
