```yaml
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "01 — Primer"
calibration: "MIT 18.06 (Strang)"
formalism_density: 0.4
status: draft
learner_id: L001
```

# A Programmer's Primer to Linear Algebra

## Vectors as Objects, Not Just Arrows

### Conceptual Bridge (Intuitive)
Imagine you're working with lists of numbers in your code—maybe features of a dataset or activations in a neural network. These lists have structure and can be operated on in predictable ways. In linear algebra, these lists are called **vectors**, and they live in spaces where certain operations always "make sense." This intuition bridges to the formal definition.

### Formal Definition
A **vector** is an ordered list of numbers. For example, in 3D space, a vector might look like:
\[ \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \]
Each entry \( v_i \) is a scalar from a field (often real numbers).

---

## Vector Spaces: The Rules of the Game

### Conceptual Bridge
Think of your data as existing in some organized structure where adding two datasets or scaling one makes sense. This is the essence of a **vector space**.

### Formal Definition
A **vector space** over a field \( \mathbb{F} \) (like real numbers) is a set \( V \) with two operations:
1. **Addition**: For any \( \mathbf{u}, \mathbf{v} \in V \), their sum \( \mathbf{u} + \mathbf{v} \) is also in \( V \).
2. **Scalar Multiplication**: For any \( a \in \mathbb{F} \) and \( \mathbf{v} \in V \), the product \( a\mathbf{v} \) is in \( V \).

This "closure" ensures your data behaves nicely under these operations.

### Full Axioms of a Vector Space
For all vectors \( \mathbf{u}, \mathbf{v}, \mathbf{w} \in V \) and scalars \( a, b \in \mathbb{F} \):
- **Closure**:
  - Addition: \( \mathbf{u} + \mathbf{v} \in V \)
  - Scalar multiplication: \( a\mathbf{v} \in V \)
- **Associativity**: \( (\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w}) \)
- **Commutativity**: \( \mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} \)
- **Identity Element**: There exists a vector \( \mathbf{0} \in V \) such that \( \mathbf{v} + \mathbf{0} = \mathbf{v} \)
- **Inverse Elements**: For every \( \mathbf{v} \), there exists \( -\mathbf{v} \in V \) such that \( \mathbf{v} + (-\mathbf{v}) = \mathbf{0} \)
- **Distributivity**:
  - Scalar multiplication distributes over vector addition: \( a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v} \)
  - Distributive property of scalar multiplication over field addition: \( (a + b)\mathbf{v} = a\mathbf{v} + b\mathbf{v} \)
  - Compatibility with field multiplication: \( (ab)\mathbf{v} = a(b\mathbf{v}) \)

### Worked Example (Closure)
Consider the set of all 2D vectors:
\[ \mathbb{R}^2 = \left\{ \begin{bmatrix} x \\ y \end{bmatrix} \,|\, x, y \in \mathbb{R} \right\} \]
- **Addition**: 
  \[ \begin{bmatrix} a \\ b \end{bmatrix} + \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} a+c \\ b+d \end{bmatrix} \in \mathbb{R}^2 \]
- **Scalar Multiplication**:
  \[ 3 \cdot \begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} 3a \\ 3b \end{bmatrix} \in \mathbb{R}^2 \]

Both operations keep results in \( \mathbb{R}^2 \), so it's closed.

---

## Basis and Dimension: Building from Scratch

### Conceptual Bridge
Just as you might represent data with key features, a **basis** is a minimal set of vectors needed to span the space. Think of it like choosing columns that matter most in your dataset.

### Formal Definition
A **basis** for a vector space \( V \) is a minimal list of vectors:
1. They are **linearly independent**: No vector can be written as a combination of others.
2. They **span** \( V \): Any vector in \( V \) can be expressed as their linear combination.

The **dimension** of \( V \) is the number of vectors in any basis.

### Worked Example
For \( \mathbb{R}^3 \), a standard basis is:
\[ \mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{e}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \]
Any vector in \( \mathbb{R}^3 \) can be written as:
\[ a\mathbf{e}_1 + b\mathbf{e}_2 + c\mathbf{e}_3 = \begin{bmatrix} a \\ b \\ c \end{bmatrix} \]
Thus, \( \dim(\mathbb{R}^3) = 3 \).

---

## Linear Maps: Functions that Preserve Structure

### Conceptual Bridge
Think of functions in your code that transform data—like applying filters to images. In linear algebra, a **linear map** is a function between vector spaces that preserves the operations of addition and scalar multiplication.

### Formal Definition
A **linear map** \( T: V \rightarrow W \) satisfies:
1. \( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \)
2. \( T(a\mathbf{v}) = aT(\mathbf{v}) \)

### Worked Example
Let \( V = \mathbb{R}^2 \) and \( W = \mathbb{R}^3 \). Define:
\[ T\left( \begin{bmatrix} x \\ y \end{bmatrix} \right) = \begin{bmatrix} x + y \\ 2x - y \\ x \end{bmatrix} \]
This is a linear map because it preserves addition and scalar multiplication.

---

## Matrices: Spreadsheets of Linear Maps

### Conceptual Bridge
Think of your code using NumPy arrays or Excel spreadsheets to transform data systematically. A **matrix** represents how a linear map transforms vectors.

### Formal Definition
A **matrix** \( A \) is a rectangular array of scalars:
\[ A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} \]
Each column represents where the basis vectors are mapped.

### Worked Example
Let \( A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \\ 5 & 6 \end{bmatrix} \). Then:
\[ A\mathbf{e}_1 = \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix}, \quad A\mathbf{e}_2 = \begin{bmatrix} 3 \\ 4 \\ 6 \end{bmatrix} \]
This matrix represents the linear map \( T \) defined earlier.

---

## Rank and Nullity: The Impact of Linear Maps

### Conceptual Bridge
Think of your code's efficiency—how much data is "lost" or "retained" after transformation. In linear algebra, **rank** measures how much information is preserved, while **nullity** measures what's lost (zerosed out).

### Formal Definition
The **rank-nullity theorem** states:
\[ \text{rank}(T) + \text{nullity}(T) = \dim(V) \]
- **rank**: Dimension of the image \( \text{Im}(T) \).
- **nullity**: Dimension of the kernel (solutions to \( T(\mathbf{v}) = 0 \)).

### Worked Example
For \( A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \\ 5 & 6 \end{bmatrix} \):
\[ \text{rank}(A) = 2 \quad (\text{full rank}) \]
\[ \text{nullity}(A) = 0 \quad (\text{no non-trivial solutions to } A\mathbf{x}=0) \]

---

## ML Payoff: Why This Matters

### Intuition for Machine Learning
- **Data Representation**: Vectors and matrices are the primary data structures in ML. For example, images can be represented as high-dimensional vectors.
- **Linear Transformations**: Neural networks use linear maps (matrices) to transform data through layers.
- **Dimensionality Reduction**: Basis concepts underpin techniques like PCA, where finding a "basis" reduces data complexity.

### Example: Linear Classifiers
A simple linear classifier in ML can be represented as:
\[ y = \mathbf{w}^T\mathbf{x} + b \]
Here, \( \mathbf{w} \) is a weight vector (basis), and \( \mathbf{x} \) is the input vector. The rank of this system determines if the decision boundary can separate classes.

---

## Tiered Memory Summary

### CARRY (Memorize)
- **Vectors**: Ordered lists of numbers.
- **Matrices**: 2D arrays representing linear maps.
- **Rank**: Measure of information retention.
- **Basis**: Minimal building blocks for vector spaces.

### RECONSTRUCT (Derive When Needed)
- Vector space closure properties.
- Linear map definitions from their action on basis vectors.
- Matrix multiplication as composition of transformations.

### LOOKUP (Never Memorize)
- Detailed proofs of linear independence and span.
- Non-square matrix rank definitions.

---

## Computational Exercise

Use NumPy to:
1. Create a 2x3 matrix \( A \).
2. Multiply it by the vector \( \mathbf{x} = [1, 2, 3]^T \).
3. Compute the rank of \( A \).

```python
import numpy as np

# 1. Create matrix A (2x3)
A = np.array([[1, 3, 5],
              [2, 4, 6]])

# 2. Vector x (3x1)
x = np.array([1, 2, 3])

# Multiply Ax
result = A @ x

# Compute rank of A
rank_A = np.linalg.matrix_rank(A)

print("Result of Ax:\n", result)
print("\nRank of A:", rank_A)
```

---

## Explain Out Loud Check

Write down:
- What’s the relationship between a matrix and a linear map?
- How does the concept of basis help in understanding machine learning models?

This exercise ensures you internalize the concepts rather than just computing.
```