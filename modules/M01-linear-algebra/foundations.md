---
type: module-foundations
module_id: M01
module_title: "Linear Algebra for ML"
created: 2026-06-14
updated: 2026-06-14
purpose: >
  Ground-floor primer. Read this before theory.md. Builds the core concepts from everyday
  intuition upward: what fields and vector spaces are, what every axiom guarantees, what
  the four fundamental subspaces operationally mean, and how everything connects.
  No background in abstract algebra required.
---

# M01 Foundations: Linear Algebra from the Ground Up

*Read this before theory.md. It covers the same concepts but from scratch — starting with what
you already know, defining every symbol, and unpacking every axiom with intuition.*

---

## What you'll encounter in this file (pre-reading map)

Read this list before starting. It primes your working memory for what's coming so nothing
feels like it arrived without warning.

1. **What you already know** — anchoring to arithmetic rules you use every day
2. **Symbol reference card** — every symbol used in theory.md defined in plain English before you see it there
3. **Fields** — what the "number system" underlying everything is; 11 axioms with "what breaks without it"
4. **Vector spaces** — what the "universe of objects" is; 8 axioms unpacked; non-examples; neural networks as vectors
5. **The four fundamental subspaces** — column space (what A outputs), null space (what A erases), row space (what A uses), left null space (what A can't reach); all with geometric pictures and operational meanings
6. **Dot product and normalization** — the arithmetic before the abstraction; why normalization matters in ML
7. **How to derive the normal equations** — step-by-step with narration at each step
8. **Concept dependency map** — the full chain from fields → SVD → LoRA/PCA
9. **ML connections table** — where each structure appears in practice
10. **Memory tiers** — what to CARRY in your head, what to RECONSTRUCT from first principles, what to LOOK UP

You don't have to read this all at once. Checkpoints are marked throughout — each one is a
complete stopping point. Come back for the next section when you're ready.

---

## What you already know (the starting point)

You already do linear algebra every time you do basic arithmetic. When you compute
$3 + 4 = 7$, you're using addition on real numbers. When you compute $2 \times 5 = 10$,
you're using scalar multiplication. You know these operations follow rules: order doesn't
matter for addition ($3 + 4 = 4 + 3$), there's a number that changes nothing ($x + 0 = x$),
every number has a negative that cancels it ($3 + (-3) = 0$), and multiplication distributes
over addition ($2 \times (3 + 4) = 2 \times 3 + 2 \times 4$).

Linear algebra is what happens when you apply exactly those rules — the same ones, no more,
no less — to objects that aren't just single numbers. Arrows in space. Lists of numbers.
Matrices. Functions. Neural network weight tensors. The surprising and powerful fact is that
all of these "universes" follow the same arithmetic rules, so everything you learn about one
transfers to all the others.

When a neural network layer computes $h = Wx + b$ (weights times input plus bias), $W$ is a
matrix, $x$ is a vector, $h$ is a vector, and the computation lives in a vector space. When
PCA finds the "directions of greatest variance" in a dataset, it's decomposing a matrix into
its eigenvectors. When LoRA fine-tunes a language model with 7× fewer parameters, it's
exploiting the rank-nullity theorem. The language of linear algebra is not separate from ML
— it is the substrate all of ML is written on.

---

## Symbol reference card

Every symbol used in theory.md, defined before you encounter it there.

| Symbol | Pronunciation | Plain-English meaning |
|---|---|---|
| $\mathbb{R}$ | "R" (blackboard bold) | The set of all real numbers ($-\infty$ to $+\infty$, including fractions, irrationals, etc.) |
| $\mathbb{R}^n$ | "R n" | All lists of $n$ real numbers, e.g. $\mathbb{R}^3$ = all 3D coordinate triples $(x, y, z)$ |
| $\mathbb{R}^{m \times n}$ | "R m by n" | All $m$-row, $n$-column matrices of real numbers |
| $\mathbb{C}$ | "C" (blackboard bold) | The complex numbers: all numbers of form $a + bi$ where $i = \sqrt{-1}$ |
| $\mathbb{F}$ | "F" (blackboard bold) | An unspecified field — in this module, you can always read this as $\mathbb{R}$ |
| $x \in V$ | "x in V" / "x is an element of V" | $x$ belongs to the set $V$; $x$ is one of the objects in $V$ |
| $W \subseteq V$ | "W is a subset of V" | Every element of $W$ is also in $V$; $W$ is a "room inside" $V$ |
| $V \times V$ | "V cross V" | All pairs of elements from $V$; the domain of a binary operation |
| $\langle x, y \rangle$ | "inner product of x and y" | The degree to which $x$ and $y$ point in the same direction (a single number) |
| $\|x\|$ | "norm of x" / "length of x" | The length (magnitude) of vector $x$; computed as $\sqrt{\langle x, x \rangle}$ |
| $\mathcal{C}(A)$ | "column space of A" | All vectors the matrix $A$ can produce as outputs |
| $\mathcal{N}(A)$ | "null space of A" (also "kernel of A") | All inputs that $A$ maps to the zero vector |
| $\mathcal{C}(A^\top)$ | "row space of A" | All linear combinations of A's rows; orthogonal complement of the null space |
| $\mathcal{N}(A^\top)$ | "left null space of A" | All vectors orthogonal to every output of $A$; complement of column space |
| $\ker(T)$ | "kernel of T" | Same as null space: inputs that $T$ maps to zero |
| $\text{im}(T)$ | "image of T" | Same as column space: all possible outputs of $T$ |
| $\dim(V)$ | "dimension of V" | Number of vectors in a basis for $V$; the "size" of the space |
| $\{0\}$ | "the trivial set" / "zero set" | The set containing only the zero vector; written to say "nothing non-trivial maps to zero" |
| $\forall$ | "for all" | "For every single element..." |
| $\exists$ | "there exists" | "There is at least one..." |
| $\Rightarrow$ | "implies" | If the left side is true, the right side must be true |
| $\Leftrightarrow$ | "if and only if" | Both sides are equivalent; each implies the other |
| $A^\top$ | "A transpose" | The matrix $A$ with rows and columns swapped |
| $A^{-1}$ | "A inverse" | The matrix that "undoes" $A$: $A A^{-1} = I$ (if it exists) |
| $I$ | "the identity matrix" | Square matrix with 1s on the diagonal and 0s elsewhere; acts like multiplying by 1 |
| $\det(A)$ | "determinant of A" | A single number encoding how much $A$ scales volumes; zero means $A$ collapses some dimension |
| $\sigma_i$ | "sigma i" | The $i$-th singular value of a matrix; how much it stretches in its $i$-th natural direction |
| $\lambda$ | "lambda" | An eigenvalue; how much a matrix stretches along an eigenvector direction |
| $\kappa(A)$ | "kappa of A" | Condition number; ratio of largest to smallest singular value; how numerically "fragile" $A$ is |
| $\hat{x}$ | "x hat" | The least-squares solution (the best approximate answer when no exact solution exists) |
| $\nabla$ | "nabla" / "gradient" | Points in the direction of steepest increase of a function |

---

## What is a field? (The number system underlying everything)

When we say "a vector space over a field $\mathbb{F}$," the word *field* names the kind of
*scalars* we're allowed to use — the numbers we scale vectors by. A field is just a set of
objects where you can add, subtract, multiply, and divide (everything except dividing by zero),
and the familiar arithmetic rules hold.

**Examples of fields:**
- $\mathbb{R}$: the real numbers. You can compute $\sqrt{2} + \pi$, divide $3$ by $7$, etc. This is the field used throughout ML.
- $\mathbb{C}$: the complex numbers. Adds $i = \sqrt{-1}$. Some eigenvalue proofs require this.
- $\mathbb{Q}$: the rational numbers (fractions). Also a field.
- $\mathbb{F}_2 = \{0, 1\}$ with addition and multiplication mod 2. A field with only two elements! Used in coding theory.

**Non-example:** The integers $\mathbb{Z}$ are NOT a field — you can't always divide. $1 \div 2$ gives $0.5$, which is not an integer.

Throughout this curriculum, whenever you see "over a field $\mathbb{F}$," read it as "over the real numbers $\mathbb{R}$." The abstraction is there so proofs work for any field, but you'll almost never need $\mathbb{C}$ or $\mathbb{F}_2$ in ML practice.

### Field axioms (what the rules guarantee)

For a set $\mathbb{F}$ with addition $(+)$ and multiplication $(\cdot)$:

| Axiom | Formal statement | Plain English | Everyday analogy | What breaks without it |
|---|---|---|---|---|
| Closure under $+$ | $a, b \in \mathbb{F} \Rightarrow a+b \in \mathbb{F}$ | Adding two elements stays inside the set | Adding two real numbers gives a real number | You could "escape" — add two elements and get something your algebra can't handle |
| Closure under $\cdot$ | $a, b \in \mathbb{F} \Rightarrow a \cdot b \in \mathbb{F}$ | Multiplying two elements stays inside | Two reals multiplied give a real | Same — multiplication could produce objects your framework doesn't recognize |
| Commutativity of $+$ | $a + b = b + a$ | Order of addition doesn't matter | $3 + 4 = 4 + 3$ | Reordering terms in an equation could change the answer |
| Associativity of $+$ | $(a+b)+c = a+(b+c)$ | Grouping doesn't matter | $(1+2)+3 = 1+(2+3)$ | Parentheses would change results; can't regroup algebraic expressions |
| Additive identity (0) | $\exists\, 0 : a + 0 = a$ | There's an element that adds nothing | The number 0 | No "do nothing" baseline; the zero vector loses meaning |
| Additive inverse | $\forall a\ \exists(-a): a+(-a)=0$ | Every element can be cancelled | $3 + (-3) = 0$ | Can't subtract; can't cancel terms; can't solve $x + 3 = 0$ |
| Commutativity of $\cdot$ | $a \cdot b = b \cdot a$ | Multiplication order doesn't matter | $3 \times 4 = 4 \times 3$ | Would make algebra asymmetric (note: matrix multiplication is NOT commutative — matrices are not a field) |
| Associativity of $\cdot$ | $(a\cdot b)\cdot c = a\cdot(b\cdot c)$ | Grouping of products doesn't matter | $(2\times3)\times4 = 2\times(3\times4)$ | Can't rearrange products freely |
| Multiplicative identity (1) | $\exists\, 1 : a \cdot 1 = a$ | There's an element that scales nothing | The number 1 | No baseline for scaling; the identity matrix has no meaning |
| Multiplicative inverse | $\forall a \ne 0\ \exists a^{-1}: a \cdot a^{-1} = 1$ | Every non-zero element has a reciprocal | $3 \times \frac{1}{3} = 1$ | Can't divide; can't solve $3x = 7$; equations like $Ax = b$ may have no unique solution |
| Distributivity | $a \cdot (b+c) = a\cdot b + a\cdot c$ | Multiplication distributes over addition | $2(3+4) = 2\cdot3 + 2\cdot4$ | Can't factor; the algebra of rearrangement collapses |

**Memorability hook:** A field is a number system where you can always add, subtract, multiply, and divide (except by zero), and the results make algebraic sense. Real numbers are the canonical field.

> **Try this (micro-exercise 1):** Is the set of all *even* integers a field? Check the multiplicative inverse axiom: does every non-zero even integer have a multiplicative inverse that is also an even integer? Use Python to explore:
> ```python
> from fractions import Fraction
> # Try to find the multiplicative inverse of 2 within even integers
> a = 2
> inverse = Fraction(1, a)  # the mathematical inverse of 2 is 1/2
> print(f"Inverse of {a} is {inverse}")
> print(f"Is {inverse} an even integer? {inverse.denominator == 1 and int(inverse) % 2 == 0}")
> # What does this tell you about the even integers as a field?
> ```
> Expected: `Inverse of 2 is 1/2`, `Is 1/2 an even integer? False`. The multiplicative inverse axiom fails — the inverse of 2 lands outside the even integers.

---

> **Checkpoint 1** — Fields
> 
> *This is a complete idea. Good stopping point.*
> 
> If it's sitting right, you can answer without looking: "What's the difference between ℝ and ℤ in terms of field axioms?" and "What does the distributivity axiom protect?"
> 
> If it's not clear: re-read the "What breaks without it" column in the field axioms table, focusing on the additive inverse and multiplicative inverse rows.

---

## What is a vector space? (The universe we work in)

A **vector space** over $\mathbb{R}$ is any collection of objects — call them *vectors* — where you can:
1. **Add** any two vectors to get another vector
2. **Scale** any vector by a real number to get another vector

...and those two operations obey the eight axioms below, which are exactly the rules ordinary arithmetic follows. The objects themselves don't have to be arrows or coordinate lists — the definition works for *anything* that follows the rules.

### The eight vector space axioms, unpacked

Let $V$ be a vector space with vectors $u, v, w \in V$ (meaning: $u$, $v$, and $w$ are elements of $V$) and scalars $c, d \in \mathbb{R}$:

| Axiom | Formal statement | Plain English | What breaks without it |
|---|---|---|---|
| Closure under $+$ | $u + v \in V$ | Adding two vectors stays inside the space | You could combine vectors and land "outside" — the space isn't self-contained |
| Closure under $\cdot$ | $c \cdot v \in V$ | Scaling a vector stays inside | Scaling could produce objects your space can't represent |
| Commutativity of $+$ | $u + v = v + u$ | Order of adding vectors doesn't matter | Two paths to the same sum could give different results |
| Associativity of $+$ | $(u+v)+w = u+(v+w)$ | Grouping of vector addition doesn't matter | Can't reorder or regroup sums in equations |
| Additive identity | $\exists\, \mathbf{0}: v + \mathbf{0} = v$ | There's a zero vector that changes nothing | No baseline; gradient descent can't start from "nothing" |
| Additive inverse | $\exists\, (-v): v + (-v) = \mathbf{0}$ | Every vector has a negative that cancels it | Can't subtract vectors; can't define differences in parameter space |
| Multiplicative identity | $1 \cdot v = v$ | Scaling by 1 changes nothing | The "don't scale" operation has no representation |
| Distributivity (two forms) | $c(u+v) = cu + cv$ and $(c+d)v = cv + dv$ | Scaling distributes over both vector sums and scalar sums | Can't factor expressions involving vectors and scalars |

**Worked example in $\mathbb{R}^2$:** Take $u = (3, 5)$, $v = (1, 2)$, $c = 2$:
- Closure under $+$: $(3,5) + (1,2) = (4,7) \in \mathbb{R}^2$ ✓
- Closure under $\cdot$: $2 \cdot (3,5) = (6,10) \in \mathbb{R}^2$ ✓
- Zero vector: $(3,5) + (0,0) = (3,5)$ ✓
- Additive inverse: $(3,5) + (-3,-5) = (0,0)$ ✓
- Distributivity: $2 \cdot ((3,5) + (1,2)) = 2 \cdot (4,7) = (8,14) = (6,10) + (2,4)$ ✓

**Non-examples (things that look like vector spaces but aren't):**

- *Vectors with positive entries only* ($\{(x,y) : x > 0, y > 0\}$): fails closure under additive inverse — $(1,1)$ is in the set but $(-1,-1)$ is not, yet $(1,1) + (-1,-1) = (0,0)$ requires both.
- *Vectors on the unit circle* ($\{v : \|v\| = 1\}$): fails closure under addition — $(1,0) + (1,0) = (2,0)$, which doesn't have unit length.

### Non-standard vector spaces (the objects don't have to be coordinate lists)

**Matrices as vectors:** The set of all $2 \times 2$ real matrices forms a vector space, with addition defined as elementwise addition and scalar multiplication as elementwise scaling. Dimension: 4 (a basis is $\{E_{11}, E_{12}, E_{21}, E_{22}\}$ where each $E_{ij}$ has a 1 in position $(i,j)$ and zeros elsewhere).

**Functions as vectors:** The set of all continuous functions on $[0,1]$ is a vector space, with $(f+g)(x) = f(x) + g(x)$ and $(cf)(x) = c \cdot f(x)$. This is infinite-dimensional — no finite basis can span it.

**Neural network weights as vectors:** Every neural network with a fixed architecture (fixed number and size of layers) can be represented by its weight vector — concatenate all weight matrices and bias vectors into one long list. The set of all such weight vectors is $\mathbb{R}^P$ where $P$ is the total parameter count. This is a vector space: you can add two networks' weights elementwise, scale all weights by a constant, and the 8 axioms hold. This is why phrases like "gradient descent moves through parameter space along the gradient direction" make precise geometric sense — you're literally moving in a vector space.

**Memorability hook:** A vector space is any universe where you can add objects and scale them by numbers, and those operations behave exactly like ordinary arithmetic. The objects can be arrows, matrices, functions, or neural network weights — the rules are the same.

> **Try this (micro-exercise 2):** Verify that vectors with positive entries do NOT form a vector space.
> ```python
> import numpy as np
> v = np.array([1.0, 2.0])
> scaled = -1 * v
> print(f"v = {v}")
> print(f"-1 * v = {scaled}")
> print(f"All entries positive? {np.all(scaled > 0)}")
> # Which of the 8 axioms fails? (Hint: additive inverse requires v + (-v) = 0.
> # But -v has negative entries, so it's not in the "positive entries" set.)
> ```
> Expected: `-1 * v = [-1. -2.]`, `All entries positive? False`. The additive inverse axiom fails.

> **Try this (micro-exercise 3):** Count the dimension of a small neural network's parameter space.
> ```python
> # 2-layer network: W1 is (3x2), W2 is (1x3)
> W1_shape = (3, 2)
> W2_shape = (1, 3)
> total_params = W1_shape[0] * W1_shape[1] + W2_shape[0] * W2_shape[1]
> print(f"W1 has {W1_shape[0] * W1_shape[1]} parameters")
> print(f"W2 has {W2_shape[0] * W2_shape[1]} parameters")
> print(f"Total parameter space dimension: {total_params}")
> # Now try a larger network: what's the parameter count for a single transformer
> # attention layer with d_model=512, 8 heads?
> d_model = 512; n_heads = 8; d_k = d_model // n_heads
> attn_params = 4 * d_model * d_model  # Q, K, V, O projections
> print(f"Single attention layer parameters: {attn_params:,}")
> ```
> Expected: `Total parameter space dimension: 9`. For the attention layer: `1,048,576` (1M parameters) — each gradient step moves in this 1M-dimensional vector space.

> **Explain it out loud (prompt 1):** Before reading on — explain in your own words, as if to someone who just walked in: *"What is a vector space, and how is it different from just a set of vectors?"* The key distinction is in the operations and the axioms they follow. If you can say this without looking, you understand vector spaces.

---

> **Checkpoint 2** — Vector spaces
> 
> *This is a complete idea. Good stopping point.*
> 
> If it's sitting right, you can say: "A vector space is a set of objects plus addition and scaling operations that follow 8 rules. The same 8 rules govern ℝⁿ, matrices, functions, and neural network weight spaces."
> 
> If it's not clear: re-read the table of 8 axioms focusing on the "What breaks without it" column. Then re-read the neural network weight space example — this is the most concretely relevant one.

---

## The four fundamental subspaces (what a matrix actually does)

A matrix $A \in \mathbb{R}^{m \times n}$ is a **linear map**: it takes any vector in $\mathbb{R}^n$ (n-dimensional input space) and produces a vector in $\mathbb{R}^m$ (m-dimensional output space). Think of $A$ as a machine:

```
n-dimensional input world ──[A]──► m-dimensional output world
```

The four fundamental subspaces answer four questions about this machine. Each one is both
a *subset* of one of the spaces and a *structure* that captures something the machine does.

---

### 1. Column space $\mathcal{C}(A) \subseteq \mathbb{R}^m$ — "What can the machine output?"

**Formal:** $\mathcal{C}(A) = \{Ax : x \in \mathbb{R}^n\}$ — all possible outputs of $A$.

**Why "column space":** $Ax$ is a linear combination of A's columns: $Ax = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n$ where $a_i$ is the $i$-th column of $A$ and $x_i$ is the $i$-th entry of $x$. So the column space is the set of all weighted combinations of A's columns — hence the name.

**Geometric picture:** If $A \in \mathbb{R}^{3 \times 4}$ has rank 2, then no matter what 4D input you feed in, the output $Ax$ always lands on a specific 2D plane through the origin in 3D output space. The machine only "paints" that plane — it can never produce a vector outside it.

**Operational reading (THE key intuition):** "$b \in \mathcal{C}(A)$" means **"the machine can produce $b$."** The equation $Ax = b$ has a solution if and only if $b$ is in the column space — because a solution $x$ is an input that produces exactly $b$. If $b$ is outside the column space, no input ever produces $b$ exactly, and we can only minimize the distance to $b$ (least squares).

**Geometric picture (ASCII):**
```
Output world ℝ²
│
│        ← C(A): the line y = 2x (everything A can produce)
│       /
│      /   ← b=(3,5) is NOT on this line → no solution to Ax=(3,5)
│     /
│    / ← b=(2,4) IS on this line → Ax=(2,4) has a solution
│   /
│  /
│ /
└─────────────────────────────────
```

**Worked example:** Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$. The two columns are $(1,2)$ and $(2,4)$. Notice $(2,4) = 2 \cdot (1,2)$ — they point in the same direction. So all linear combinations of the columns lie on the same line: $\mathcal{C}(A) = \{c \cdot (1,2) : c \in \mathbb{R}\}$, a 1D subspace (a line) inside $\mathbb{R}^2$.

Can we solve $Ax = (3,5)$? We need $(3,5)$ to be on the line $\{c \cdot (1,2)\}$. Since $(3,5) \ne c \cdot (1,2)$ for any $c$, the answer is no. The machine cannot output $(3,5)$.

Can we solve $Ax = (2,4)$? Yes: $(2,4) = 2 \cdot (1,2)$ — it's on the line. One solution is $x = (1, 0)$ (use only the first column once), another is $x = (0, \frac{1}{2})$ (use half the second column), and infinitely many others. This brings us to the null space.

> **Try this (micro-exercise 4):** Explore column space and null space for two different matrices.
> ```python
> import numpy as np
> 
> # Matrix 1: identity (full rank)
> I = np.eye(2)
> # Matrix 2: rank-deficient (columns are linearly dependent)
> A = np.array([[1, 2], [2, 4]], dtype=float)
> 
> print("Identity matrix rank:", np.linalg.matrix_rank(I))
> print("Rank-deficient matrix rank:", np.linalg.matrix_rank(A))
> 
> # Null space: vectors x where Ax = 0
> # Use SVD to find it: null space = right singular vectors for zero singular values
> U, s, Vt = np.linalg.svd(A)
> print(f"\nSingular values of A: {np.round(s, 4)}")
> print(f"(Near-zero singular values indicate null space directions)")
> null_vector = Vt[-1]  # last row of Vt when rank < n
> print(f"Null space direction: {np.round(null_vector, 4)}")
> print(f"Verify: A @ null_vector = {np.round(A @ null_vector, 10)}")
> ```
> Expected: rank 2 vs rank 1; singular values ~[4.47, 0.0]; null vector ~[-0.894, 0.447]; `A @ null_vector ≈ [0, 0]`. What this shows: for the identity, everything maps to something nonzero (trivial null space). For the rank-deficient matrix, there's a whole direction that gets erased.

---

### 2. Null space $\mathcal{N}(A) \subseteq \mathbb{R}^n$ — "What does the machine erase?"

**Formal:** $\mathcal{N}(A) = \{x \in \mathbb{R}^n : Ax = \mathbf{0}\}$ — all inputs that $A$ maps to the zero vector.

**Geometric picture:** If $\mathcal{N}(A)$ is 2-dimensional, there's a 2D plane of inputs that all produce zero output. The machine is "blind" to any input in this plane.

**Operational reading:** "$\mathcal{N}(A) = \{0\}$" means **"different inputs always give different outputs — no blind spots."** If only the zero vector maps to zero, then for any nonzero input, the output is nonzero. Consequently: if $Ax_1 = Ax_2$, then $A(x_1 - x_2) = 0$, so $x_1 - x_2 = 0$, so $x_1 = x_2$. The machine is injective — knowing the output uniquely determines the input (within what the machine can reach). This is the uniqueness condition for $Ax = b$.

**Worked example (continued):** For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the null space is $\{x : Ax = 0\}$. Writing this out: $x_1 + 2x_2 = 0$ and $2x_1 + 4x_2 = 0$ (same equation). The solution is $x_1 = -2x_2$, so $\mathcal{N}(A) = \{c \cdot (-2, 1) : c \in \mathbb{R}\}$ — a 1D line in input space ($\mathbb{R}^2$).

This confirms: $A$ can't tell the difference between $x$ and $x + c(-2,1)$ for any $c$, because they differ by a null-space vector, and $A \cdot c(-2,1) = 0$. This is why the solution to $Ax = (2,4)$ was not unique — infinitely many inputs produce the same output.

**Rank-nullity check:** $\dim(\mathcal{C}(A)) + \dim(\mathcal{N}(A)) = 1 + 1 = 2 = n$. ✓

---

### 3. Row space $\mathcal{C}(A^\top) \subseteq \mathbb{R}^n$ — "What part of the input matters?"

**Formal:** $\mathcal{C}(A^\top)$ is the column space of $A^\top$ — equivalently, all linear combinations of A's rows. Since A's rows are $n$-dimensional, this lives in input space $\mathbb{R}^n$.

**Geometric picture:** The row space and null space together partition the input space into two orthogonal halves: $\mathbb{R}^n = \mathcal{C}(A^\top) \oplus \mathcal{N}(A)$ (meaning: any input vector splits into a row-space part and a null-space part, and these two parts are perpendicular).

**Operational reading:** The row space is **"the part of the input that $A$ actually uses."** If you split any input $x = x_r + x_n$ where $x_r$ is in the row space and $x_n$ is in the null space, then $Ax = Ax_r + Ax_n = Ax_r + 0 = Ax_r$. The null-space component is invisible to $A$. Only the row-space component contributes to the output.

---

### 4. Left null space $\mathcal{N}(A^\top) \subseteq \mathbb{R}^m$ — "What part of output space is unreachable?"

**Formal:** $\mathcal{N}(A^\top) = \{y \in \mathbb{R}^m : A^\top y = \mathbf{0}\}$ — equivalently, $y^\top A = 0$.

**Geometric picture:** The column space and left null space together partition the output space: $\mathbb{R}^m = \mathcal{C}(A) \oplus \mathcal{N}(A^\top)$. Every vector in output space splits into a part the machine can reach (column space) and a part the machine can never reach (left null space).

**Operational reading:** **"The residual in least squares always lives here."** When you run least squares on $Ax \approx b$, the best approximation $A\hat{x}$ is the projection of $b$ onto the column space. The residual $e = b - A\hat{x}$ is the part of $b$ outside the column space — and it always lands in $\mathcal{N}(A^\top)$. You can verify: $A^\top e = A^\top(b - A\hat{x}) = A^\top b - A^\top A \hat{x} = 0$ (by the normal equations).

---

### The four subspaces together — summary table

| Subspace | Lives in | Answers | Dimension |
|---|---|---|---|
| Column space $\mathcal{C}(A)$ | Output world $\mathbb{R}^m$ | What can the machine output? | $r$ (= rank of $A$) |
| Null space $\mathcal{N}(A)$ | Input world $\mathbb{R}^n$ | What does the machine erase? | $n - r$ |
| Row space $\mathcal{C}(A^\top)$ | Input world $\mathbb{R}^n$ | What part of the input matters? | $r$ |
| Left null space $\mathcal{N}(A^\top)$ | Output world $\mathbb{R}^m$ | What output is unreachable? | $m - r$ |

Rank-nullity in one sentence: the dimensions in each world sum to the world's size.
- Input world: $r + (n-r) = n$ ✓
- Output world: $r + (m-r) = m$ ✓

**Memorability hook:** Column space = what A can output. Null space = what A erases. Their dimensions always sum to the input dimension. The solution to $Ax = b$ exists iff $b$ is reachable; it's unique iff nothing is erased.

> **Explain it out loud (prompt 2):** Without looking — explain to a friend: *"What does it mean for a system Ax = b to have (a) no solution, (b) exactly one solution, (c) infinitely many solutions?"* Each case corresponds to a relationship between b and the column space, and between the null space and {0}. The answer should mention column space and null space.

---

> **Checkpoint 3** — The four fundamental subspaces
> 
> *This is a major complete idea. Definitely a good stopping point.*
> 
> If it's sitting right, you can say: "The column space is what A can output. The null space is what A erases. $Ax = b$ has a solution iff $b$ is in the column space; it's unique iff the null space is trivial. Rank-nullity says rank + nullity = n."
> 
> If it's not clear: re-read the "Operational reading" paragraph for the column space and null space. Then re-trace the worked example for $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ — why are there infinitely many solutions to $Ax = (2,4)$?

---

## Concept dependency map

How the ideas in M01 build on each other, from first principles to ML applications:

```
ℝ (real numbers, a field)
    │
    ▼
Vector spaces (universes obeying the 8 axioms)
    │
    ├──► Subspaces (rooms inside the universe)
    │        │
    │        └──► The four fundamental subspaces of A
    │
    ├──► Linear combinations (weighted sums of vectors)
    │        │
    │        └──► Linear independence (no redundant directions)
    │                 │
    │                 └──► Basis (minimum spanning set)
    │                          │
    │                          └──► Dimension (size of the basis)
    │
    └──► Rank-nullity theorem (dimension accounting across all four subspaces)
              │
              ├──► Least squares (project b onto column space)
              │
              ├──► Inner products & orthogonality (angle between vectors)
              │        │
              │        └──► Gram-Schmidt / QR (make a basis orthogonal)
              │
              └──► Eigendecomposition (natural axes of symmetric matrices)
                        │
                        ├──► Spectral theorem (symmetric = diagonalizable)
                        │        │
                        │        └──► PCA (principal components = eigenvectors of covariance)
                        │
                        └──► SVD (generalizes eigendecomposition to any matrix)
                                 │
                                 ├──► Low-rank approximation (LoRA, image compression)
                                 ├──► Condition number (numerical stability)
                                 └──► Pseudoinverse (least-norm least-squares solution)
```

---

## Dot product and normalization from first principles

Before the abstract inner product definition in theory.md, here's what it means mechanically.

**The dot product** of two vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ is:
$$u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3$$
Multiply corresponding entries, then add. That's it.

**What does it measure?** The dot product measures how much $u$ and $v$ "agree" directionally:
- Same direction: large positive. $u = (1,0,0)$, $v = (2,0,0)$: $u \cdot v = 2$. Both point right.
- Opposite directions: large negative. $u = (1,0,0)$, $v = (-1,0,0)$: $u \cdot v = -1$. One goes left, one right.
- Perpendicular: exactly zero. $u = (1,0,0)$, $v = (0,1,0)$: $u \cdot v = 0$. Horizontal and vertical — no overlap.

The formula connecting dot product to angle: $u \cdot v = \|u\| \|v\| \cos\theta$, where $\theta$ is the angle between them. Rearranging: $\cos\theta = (u \cdot v) / (\|u\| \|v\|)$.

**Normalization:** To make a vector have length 1 (a unit vector), divide it by its length:
$$\hat{u} = \frac{u}{\|u\|} = \frac{u}{\sqrt{u_1^2 + u_2^2 + u_3^2}}$$

**Worked example:** $u = (3, 4, 0)$. Length: $\|u\| = \sqrt{9 + 16 + 0} = 5$. Normalized: $\hat{u} = (0.6, 0.8, 0)$.

Check: $\|\hat{u}\| = \sqrt{0.36 + 0.64 + 0} = \sqrt{1} = 1$ ✓

**Why normalization matters in ML:** Word embeddings are often normalized to unit length before computing similarity — because we care about the *direction* of meaning, not the magnitude. Normalizing makes $\cos\theta = u \cdot v$ exactly (since $\|u\| = \|v\| = 1$), so the dot product directly gives the cosine similarity.

> **Try this (micro-exercise 5):** Compute dot products and angles between vectors — like an attention mechanism does.
> ```python
> import numpy as np
> 
> u = np.array([1, 2, 3], dtype=float)
> v = np.array([4, 0, 1], dtype=float)
> 
> dot = np.dot(u, v)
> norm_u = np.linalg.norm(u)
> norm_v = np.linalg.norm(v)
> cos_theta = dot / (norm_u * norm_v)
> angle_degrees = np.degrees(np.arccos(np.clip(cos_theta, -1, 1)))
> 
> print(f"u · v = {dot}")
> print(f"‖u‖ = {norm_u:.4f}, ‖v‖ = {norm_v:.4f}")
> print(f"cos θ = {cos_theta:.4f}")
> print(f"angle = {angle_degrees:.1f}°")
> print(f"Direction: {'acute (same side)' if dot > 0 else 'obtuse (opposite sides)'}")
> ```
> Expected: `u · v = 7`, `cos θ ≈ 0.454`, `angle ≈ 63°`. They point in roughly the same direction. Now change `v` to `(-4, 0, -1)` and observe what happens to the dot product and angle.

> **Try this (micro-exercise 6):** Normalize a vector and verify unit length — then see how this affects dot product interpretation.
> ```python
> import numpy as np
> 
> u = np.array([3.0, 4.0])
> u_hat = u / np.linalg.norm(u)  # normalize
> print(f"Original: {u}, norm = {np.linalg.norm(u)}")
> print(f"Normalized: {u_hat}, norm = {np.linalg.norm(u_hat):.6f}")
> 
> # Simulate word embedding cosine similarity
> # When both vectors are normalized, dot product = cosine similarity directly
> cat  = np.array([0.90, 0.30, 0.10])
> kitten = np.array([0.80, 0.50, 0.10])
> democracy = np.array([0.10, 0.10, 0.90])
> # (already unit-ish; let's normalize properly)
> for name, vec in [("cat", cat), ("kitten", kitten), ("democracy", democracy)]:
>     vec[:] = vec / np.linalg.norm(vec)
> print(f"\ncat · kitten  = {np.dot(cat, kitten):.4f}")
> print(f"cat · democracy = {np.dot(cat, democracy):.4f}")
> print(f"Ratio: {np.dot(cat, kitten) / np.dot(cat, democracy):.1f}x more similar")
> ```
> Expected: normalized `u` has norm `1.0`; `cat · kitten ≈ 0.88`, `cat · democracy ≈ 0.20`; `~4.4x` more similar. This is exactly what the attention mechanism computes (scaled by $\sqrt{d_k}$).

---

## How to derive the normal equations (step-by-step)

This is one of the most important derivations in applied linear algebra. We want to find $\hat{x}$ that minimizes $\|Ax - b\|^2$.

**Step 1:** Write the squared error as a function of $x$:
$$f(x) = \|Ax - b\|^2 = (Ax - b)^\top (Ax - b)$$
*Why:* $\|v\|^2 = v^\top v$ for any vector $v$.

**Step 2:** Expand using the transpose distributive rule $(Ax - b)^\top = x^\top A^\top - b^\top$:
$$f(x) = x^\top A^\top A x - x^\top A^\top b - b^\top A x + b^\top b$$
*Why:* Multiplying out $(p - q)^\top(p - q) = p^\top p - p^\top q - q^\top p + q^\top q$.

**Step 3:** Note that $x^\top A^\top b = b^\top A x$ (both are scalar; a scalar equals its own transpose):
$$f(x) = x^\top A^\top A x - 2 b^\top A x + b^\top b$$

**Step 4:** Take the gradient with respect to $x$ and set it to zero (a minimum has zero gradient):
$$\nabla_x f = 2 A^\top A x - 2 A^\top b = 0$$
*Why:* For a scalar function $x^\top M x$, the gradient is $2Mx$ when $M$ is symmetric. And $b^\top b$ has zero gradient (no $x$).

**Step 5:** Rearrange:
$$A^\top A \hat{x} = A^\top b$$

These are the **normal equations**. If $A$ has full column rank (no null space), $A^\top A$ is invertible and $\hat{x} = (A^\top A)^{-1} A^\top b$.

**What does each step mean?**
- Step 1: frame least-squares as minimizing a smooth function
- Step 2–3: expand into a standard quadratic form
- Step 4: set derivative to zero (optimality condition)
- Step 5: the result — $\hat{x}$ is the unique minimizer, and it satisfies a linear system

**Memorability hook:** Normal equations come from "set the gradient to zero." What's the gradient of squared error? $2A^\top(Ax - b)$. Set to zero: $A^\top A \hat{x} = A^\top b$.

> **Try this (micro-exercise 7):** Solve a least-squares regression problem computationally, then verify the normal equations by hand and see the residual orthogonality in action.
> ```python
> import numpy as np
> 
> # Three data points: (1,2), (2,4), (3,5) — fit line y = mx + b
> A = np.array([[1, 1],
>               [2, 1],
>               [3, 1]], dtype=float)
> y = np.array([2, 4, 5], dtype=float)
> 
> # Method 1: normal equations directly
> ATA = A.T @ A
> ATy = A.T @ y
> print(f"A^T A =\n{ATA}")
> print(f"A^T y = {ATy}")
> x_hat = np.linalg.solve(ATA, ATy)
> print(f"\nSolution (normal equations): m={x_hat[0]:.4f}, b={x_hat[1]:.4f}")
> 
> # Method 2: NumPy's least squares solver (uses SVD internally — more numerically stable)
> x_lstsq, residuals, rank, sv = np.linalg.lstsq(A, y, rcond=None)
> print(f"Solution (lstsq): m={x_lstsq[0]:.4f}, b={x_lstsq[1]:.4f}")
> 
> # Verify: residual is orthogonal to columns of A
> e = y - A @ x_hat
> print(f"\nResidual e = {np.round(e, 4)}")
> print(f"A^T e = {np.round(A.T @ e, 10)}  ← should be ≈ [0, 0]")
> ```
> Expected: `A^T A = [[14, 6], [6, 3]]`, `A^T y = [25, 11]`, `m=1.5, b=0.3333`. The key result: `A^T e ≈ [0, 0]` — the residual is orthogonal to both columns of A, confirming the geometric optimality condition.

> **Explain it out loud (prompt 3):** Without looking — tell a friend: *"Why does least squares always have a solution, even when Ax = b has no exact solution? What geometric object is $\hat{x}$ finding?"* The answer should mention projection, column space, and the normal equations.

---

> **Checkpoint 4** — Dot product, normalization, and normal equations
> 
> *Complete section. Good stopping point.*
> 
> If it's sitting right, you can say: "The dot product measures directional agreement — positive means same direction, zero means perpendicular, negative means opposite. The normal equations $A^\top A \hat{x} = A^\top b$ find the best approximate solution by projecting $b$ onto the column space of $A$."
> 
> If it's not clear: re-read the derivation walk for normal equations, focusing on Step 4 — why "set the gradient to zero" gives you the optimality condition.

---

## Connections to ML — where you'll see each structure

| Structure | Where it appears in ML |
|---|---|
| Vector spaces | Parameter space of any neural network; embedding spaces; feature spaces; gradient vectors live here |
| Column space | The set of outputs a layer can produce; determines whether $Ax = b$ has an exact solution |
| Null space | Redundant input directions; the basis for understanding LoRA (fine-tuning updates live in a small subspace) |
| Inner product / dot product | Attention logits ($QK^\top$); cosine similarity in embedding search; kernel functions |
| Orthogonality | Independent gradient components; decorrelated features; QR factorization in optimization |
| Eigenvalues / eigenvectors | PCA directions; Hessian curvature; RNN stability analysis; graph Laplacian spectrum |
| SVD | Image compression; latent semantic analysis; matrix factorization recommenders; understanding LoRA mathematically |
| Condition number | Numerical stability of training; ill-conditioned Hessians cause gradient oscillation; motivation for preconditioning and adaptive optimizers |
| Least squares | Regression heads; linear probing; any "fit a linear function to data" setup |
| Rank | How many "effective dimensions" a weight matrix uses; full rank = no information destroyed; low rank = compression |

---

## Memory tiers — what to carry, what to reconstruct, what to look up

This is the single most important section for managing cognitive load. Most people try to memorize everything, which is impossible and creates overload. Here's what you actually need.

---

### CARRY — internalize these (5–7 items only)

These are conceptual hooks. If you internalize nothing else from M01, internalize these. Write them on a sticky note if it helps. They are *not* formulas — they are ideas.

1. **Column space = what A can output. Null space = what A erases.** Every question about $Ax = b$ reduces to these two.
2. **Rank + nullity = input dimension.** Conservation law. Nothing is created; what's not output is erased.
3. **Eigenvectors: the directions a matrix can't rotate, only stretch.** Find those directions; find the eigenvalues.
4. **SVD: every matrix = rotate input → stretch → rotate output.** Singular values are the stretch factors.
5. **Dot product near zero = nearly perpendicular = unrelated. Large positive = strongly aligned. Negative = opposite.** This is what attention scores are computing.
6. **High condition number = fragile system.** Small input perturbation → large output change. Numerically dangerous.
7. **Least squares is always projection.** When there's no exact solution, $\hat{x}$ projects $b$ onto the column space.

---

### RECONSTRUCT — understand and can re-derive with time

These you should be able to sketch out from first principles given a whiteboard and 10–20 minutes. You don't need them memorized, but you need to understand the *structure* of each.

1. The 8 vector space axioms — not memorized, but you know the pattern: closure, identity, inverse, distributivity
2. Why $Ax = b$ has a solution iff $b \in \mathcal{C}(A)$ — from the definition of matrix-vector multiplication
3. Why uniqueness requires $\mathcal{N}(A) = \{0\}$ — from the fact that null-space vectors add "free" solution components
4. The normal equations derivation — set gradient of $\|Ax - b\|^2$ to zero → $A^\top A \hat{x} = A^\top b$
5. Why symmetric matrices have real eigenvalues — the key step is showing $q^\top Aq \in \mathbb{R}$ for real $q$
6. The rank-nullity proof sketch — extend a basis for the kernel to a full basis; the non-kernel part maps injectively to the image
7. Why SVD exists — $A^\top A$ is always symmetric positive semidefinite, so it has a real eigendecomposition; take square roots
8. Why large condition number means numerical instability — ratio of largest to smallest singular value; tiny perturbation in the smallest direction gets amplified by the ratio

---

### LOOK UP — keep a reference handy (do not memorize these)

Everything below lives in theory.md, in your notes, or in numpy documentation. Looking it up when you need it is exactly the right behavior — spending energy memorizing it is exactly the wrong behavior.

- Exact pseudoinverse formula: $A^+ = V\Sigma^+ U^\top$
- Exact projection matrix formula: $P = A(A^\top A)^{-1} A^\top$
- Exact Gram-Schmidt recurrence: $q_j = (a_j - \sum_{i<j} \langle a_j, q_i\rangle q_i) / \|\cdot\|$
- The characteristic polynomial derivation for $n \times n$ matrices
- Full proof of the Eckart-Young theorem
- Matrix exponential series definition: $e^{tA} = \sum_{k=0}^\infty t^k A^k / k!$
- Exact condition number formula: $\kappa(A) = \sigma_1 / \sigma_r$
- NumPy API: `np.linalg.svd`, `np.linalg.eig`, `np.linalg.lstsq`, `np.linalg.solve`, `np.linalg.cond`
- The specific axiom numbering (there are 8 vector space axioms, but you don't need to know which is "Axiom 4")
- Proof details of the spectral theorem (the inductive step)
- The exact LU decomposition algorithm with pivoting

---

> **Checkpoint 5 — Final**
> 
> *You've covered the full foundations of M01. This is the end of this file.*
> 
> Before moving to theory.md: can you answer these three questions without looking?
> 
> 1. "What does it mean for $Ax = b$ to have infinitely many solutions — in terms of the null space?"
> 2. "What are the three things the SVD decomposes every matrix into?"
> 3. "Name one thing from the LOOK UP list and explain why you don't need to memorize it."
> 
> If you can answer all three, you're ready for theory.md. If not, find the section that covers the question you couldn't answer and re-read just that section.
