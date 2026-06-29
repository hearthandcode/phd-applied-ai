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

# Linear Algebra Primer

## Vectors as Objects

Before diving into formal definitions, let’s bridge intuition with programming concepts you already know. In your experience with spreadsheets and arrays, a vector is like a list of numbers. It has a specific order and length. Think of it as a one-dimensional array.

Formally, **a vector** is an object in space with a specific direction and magnitude. In linear algebra terms, we often represent vectors using lowercase boldface letters (e.g., **v**, **u**, **w**). Each vector exists within a **vector space**, which is the set of all possible vectors that can be formed by scaling and adding together other vectors in that space.

## Vector Spaces and Closure

In programming terms, imagine a list of lists, where each inner list follows specific rules. In linear algebra, a **vector space** is a set of vectors that satisfies two properties:
1. **Closure under addition**: Adding any two vectors in the space results in another vector in the same space.
2. **Closure under scalar multiplication**: Multiplying any vector by a scalar (a real number) results in another vector in the same space.

For example, consider 2D vectors like [x, y]. If you add any two such vectors or multiply them by a scalar, the result is still a 2D vector. This forms a vector space we call **R²**.

## Basis and Dimension

In programming, you often use basis sets (like orthogonal bases in machine learning). In linear algebra, a **basis** for a vector space is a minimal set of vectors that can be combined to create any vector in the space through addition and scalar multiplication.

Formally, the **standard basis** for R² is:
- **e₁** = [1, 0]
- **e₂** = [0, 1]

These vectors are orthogonal and span the entire space. The number of vectors in a basis is the **dimension** of the space. For R², dimensionality is 2.

## Linear Maps as Functions

Think of functions you write in code: they take inputs and produce outputs based on some rules. In linear algebra, a **linear map** (or linear transformation) is a function between vector spaces that preserves the operations of addition and scalar multiplication.

For example, consider the function f(x, y) = [y, x]. This swaps the components of vectors in R² and is a valid linear map.

## Matrices as Spreadsheets

You’re already familiar with matrices from working with arrays or spreadsheets. In linear algebra, a **matrix** is a rectangular array of numbers arranged in rows and columns. The size of a matrix is defined by its dimensions: m x n (m rows, n columns).

Matrices are crucial because they represent **linear maps** between vector spaces. For instance, a 2x2 matrix can represent a linear map from R² to R².

## Rank-Nullity Theorem

In programming terms, think of efficiency and optimization. In linear algebra, the **rank-nullity theorem** states that for any linear map:
- **Rank (column space)**: The dimension of the output space.
- **Nullity (kernel)**: The dimension of the set of inputs that map to zero.

These concepts are fundamental in understanding how linear maps operate and will be essential for optimizing machine learning models.

## Why This Matters for Machine Learning

### ML Payoff
1. **Feature Representation**: Vectors represent features in data, and matrices handle transformations like rotations (e.g., PCA).
2. **Linear Models**: Linear regression and neural networks rely on understanding linear maps and their properties.
3. **Dimensionality Reduction**: Techniques like PCA use basis vectors to reduce complexity while retaining information.

### Computational Example
```python
import numpy as np

# Create a vector in R²
v = np.array([2, 3])

# Create a matrix (linear map)
A = np.array([[1, 0], 
              [0, -1]])

# Apply the linear map to the vector
result = A @ v

print(result)  # Output: array([ 2, -3])
```

## Tiered Memory Summary

- **CARRY (memorize)**:
  - Definition of a vector.
  - Basis vectors and dimensionality.
- **RECONSTRUCT**:
  - Proof that matrices represent linear maps.
- **LOOKUP**:
  - Detailed properties of specific matrix operations.

## Computational Exercise

1. Create a NumPy array representing a vector in R³.
2. Define a matrix and apply it to your vector using matrix multiplication (`@`).
3. Observe the result and explain what happens.

## Explain-Out-Loud Check

Take a moment to explain out loud: "What’s the difference between a vector and a matrix?" If you stumbled on any part, review that section until it feels intuitive.

```