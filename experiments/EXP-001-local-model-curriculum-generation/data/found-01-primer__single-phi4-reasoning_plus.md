<think>We have to output one section: "M01" for Linear Algebra for ML, topic ground-floor primer that warms up working memory before formal linear algebra theory. We need to follow some very strict instructions.

Let's check required structure and rules:

We must produce a complete markdown document with YAML front matter at the top, containing:
- module: M01
- title: "Linear Algebra for ML"
- artifact: foundations-primer
- section: "01 — Primer"
- calibration: "MIT 18.06 (Strang)"
- formalism_density: 0.4
- status: draft
- learner_id: L001

We must output a markdown document with content that is structured in various sections according to instructions.

The specific required elements:
1. YAML front matter as specified.
2. Conceptual Bridge First: before any formal definition, give an intuitive bridge in plain language (a second, denser bridge pass for the hardest part). THEN state the formal definition.
3. Start from comfort: anchor new ideas in things a programmer already knows (spreadsheets, arrays, loops).
4. Concrete Worked Example: include at least one fully worked numerical example with explicit steps.
5. Symbol discipline: every symbol is defined in sentence it appears; provide a symbol reference table if multiple new symbols are introduced.
6. ML Payoff: a section explaining why this matters for machine learning, with concrete examples.
7. TIERED MEMORY SUMMARY: a "CARRY (memorize, max 7) / RECONSTRUCT (re-derive) / LOOKUP (never memorize)" summary.
8. Computational Exercise: at least one small NumPy/SymPy exercise the learner can run.
9. Accuracy is non-negotiable: every definition, theorem, and derivation must be mathematically correct and verifiable against MIT 18.06 (Strang).
10. End with an "explain-out-loud check" prompt.

We need to cover these topics:
- Vectors as objects
- Vector spaces and closure,
- Basis & dimension
- Linear maps
- Matrices as the spreadsheet form of a map
- Rank-nullity theorem

The content should be structured in a warm-up style, starting from programmer's intuitions with spreadsheets, arrays, loops. We need to provide intuitive explanation then formal definition.

We have to produce a section that covers ground-floor primer: vectors, vector spaces, basis, dimension, linear maps, matrices and rank-nullity theorem.

Let's plan the markdown document content structure:

I'll start with YAML front matter as required:
```
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
```

Then I'll produce an explanation with headings:
- Introduction: A short description of the section.
- Then perhaps sub-sections for each topic.

I need to cover vectors, vector spaces, basis and dimension, linear maps, matrices as representation of maps, rank-nullity theorem. But maybe combine some topics.

We must follow "conceptual bridge first" rule: That means before formal definitions, provide an intuitive explanation in plain language. And a second denser explanation for the hardest part (maybe for the concept of basis and dimension).

I should produce concrete examples including at least one fully worked numerical example with explicit steps, e.g., demonstrating vector addition or matrix multiplication maybe.

We must use symbol discipline: every new symbol is explained when it appears; if multiple symbols appear in a page, produce a symbol reference table. We can produce a list of definitions for each symbol if there are many. But we might not have too many symbols? Possibly I'll mention some new symbols like "vectors", "span", "matrix".

We need to include computational exercise using numpy/sympy code snippet.

I should provide ML payoff: explanation why linear algebra matters in machine learning. We can talk about features, transformation and dimension reduction maybe. Provide a concrete example e.g. the role of matrices in neural networks.

We need a tiered memory summary with three parts:
- "CARRY (memorize, max 7) / RECONSTRUCT (re-derive) / LOOKUP (never memorize)" summary: so I'll produce a bullet list perhaps dividing into three groups. Actually I'll produce something like:

"CARRY": things to memorize with maximum of 7 items.

"RECONSTRUCT": things that the learner should be able to re-derive.
"LOOKUP": things which are always referenceable.

I must include an "explain-out-loud check" prompt at the end. This prompt asks: "explain out loud what you learned", etc.

I need to produce a code block for computational exercise using numpy/sympy code snippet so that the learner can run it in their environment.

Let's start with the content.

Plan structure:

1. YAML front matter block as required.
2. Introduction: "Welcome to the Linear Algebra for ML - Foundations Primer." Use direct, warm tone.
3. Intuitive Bridge: For each concept I'll begin by explaining a concept from programmer perspective:
   e.g., Vectors: "Think of vectors like lists (or arrays) of numbers. They are used in spreadsheets as rows or columns."
4. Then provide formal definitions for vector and vector spaces.

Maybe structure sections:

I might create subsections with headers, but the document is a markdown file so I'll use # headings.

Section Outline:
Title: "Linear Algebra for ML - Foundations Primer"
Then introduction: "In this module we'll cover some of the fundamental concepts that underpin machine learning algorithms. You are likely already familiar with arrays and loops from programming; these ideas will be extended to mathematical objects such as vectors, vector spaces, linear maps, matrices, basis, dimension, and more."

I need to produce a bridging narrative.

Let's write content:

"Vectors as Objects"

Conceptual Bridge: "Imagine that you have an array in your program. In many programming languages, an array can hold multiple numbers. In mathematics, we treat these arrays of numbers as objects known as vectors."

Then formal definition: A vector is an element of a vector space. But let's check: Actually the formal definition: "A vector is typically defined as an ordered tuple (x_1, x_2, ..., x_n) where each entry is a real number." We might define them with some symbol if required.

But note rule #9: "every definition must be mathematically correct and verifiable against MIT 18.06 (Strang)". So I'll use definitions from Strang's textbook.
Definition of vector space: A set V of vectors, closed under addition and scalar multiplication, satisfying certain axioms. Possibly I'll include the formal definition.

Let me check standard definitions:
- A vector is usually an element of a vector space over some field F (often R).
- Vector Space: A set V with two operations: addition (+) and scalar multiplication (·), such that for all u, v in V and scalars c in F:
   (i) u + v ∈ V,
   (ii) commutativity, associativity, existence of additive identity and inverses, distributive properties etc.

I must include a worked example maybe with addition or scalar multiplication.

Then I'll cover basis & dimension: "Basis is a set of linearly independent vectors that spans the vector space. The number of elements in any basis is called the dimension." Introduce concept of span (closure under linear combinations) and linear independence (no redundancy). Provide an example using, say, two-dimensional vectors.

Then I'll cover linear maps: "A linear map is a function f from one vector space to another that preserves addition and scalar multiplication." Then formal definition: For all u, v in V, f(u + v) = f(u) + f(v), and for any scalar c, f(c * u) = c * f(u). We'll include an example.

Then I'll cover matrices as the spreadsheet representation of a linear map: "Think about representing your linear transformation by writing it down in a table (like rows and columns) which is essentially what a matrix is." Provide formal definition of a matrix, with indexing.

I need to mention rank-nullity theorem. The rank-nullity theorem states that for any linear map from vector space V to W, the dimension of V equals the dimension of the kernel plus the dimension of the image (rank). I'll include explanation and formula: "dim(V) = dim(ker f) + dim(im f)", where ker f is nullspace and im f is range.

I must produce a worked numerical example. Perhaps use a simple matrix representing a linear map, show how to compute its rank, or show the effect of applying the transformation on vectors.

We need a concrete worked numerical example: I can take a 2x2 matrix and show an explicit addition of two vectors, then check closure. Or I can take a vector space R^2 and define a basis.

Let me produce one fully worked numerical example: Possibly use a 3-dimensional example with matrix transformation, computing the result for some given vector, and demonstrating how to compute rank or nullity maybe.
Maybe simpler: Provide an example of finding the dimension (basis) of a subspace in R^2. E.g., "Let S be the set of all vectors of form (x, 0), then show that S is a subspace spanned by (1, 0)." But I need to include operations with matrices maybe.

Alternatively, produce one example for linear maps: Consider f(x,y) = x + y in R^2 -> R, which is not linear? Actually no, check linearity. Better: let f(x, y) = (x+y, 3x-2y). Then show it's linear and compute its matrix representation with explicit steps.

I'll produce a worked example with vectors in R^2:
Example: Let v1 = (1, 2), v2 = (3,4). Compute sum v1+v2. And show scalar multiplication. But that may be too trivial.

Alternatively, produce an example for linear transformation on R^2 given by matrix A = [ [1,2], [3,4] ]. Then compute the image of vector v = (x, y). And then also discuss rank-nullity theorem: For a 2x2 matrix in general, if it is invertible then kernel dimension 0 and rank 2; if not then maybe compute null space.

Perhaps produce an example with a non-invertible matrix. For instance, let A = [ [1, 2], [2,4] ] which has rows that are multiples of each other so its rank is 1 and nullity is 1 because the dimension of domain R^2 equals rank + nullity.
Let's produce that example:

Worked numerical example: Consider the matrix M in R^(2x2) defined by:
M = [ [1, 2],
      [2,4] ]
Check closure properties. Then show that for any vector v = (a,b), Mv is computed as:
first component: a + 2b,
second component: 2a+4b.
Notice the second component equals 2*(first component). So every output lies on the line y = 2x, which shows the range of M has dimension 1. Then null space: Solve a+2b=0 => a = -2b so v = (-2b, b) for any scalar b. That gives one degree of freedom; thus nullity is 1.
Then check rank-nullity theorem: domain R^2 has dimension 2 equals rank (1) + nullity (1).

That worked example satisfies the requirement.

I must provide a computational exercise in NumPy or Sympy code snippet that allows computing something similar. For instance, define matrix A and compute its rank using numpy.linalg.matrix_rank() etc. Or use sympy to compute nullspace. I'll produce one small piece of code:
```
import numpy as np
A = np.array([[1,2],[2,4]])
print("Rank:", np.linalg.matrix_rank(A))
print("Nullity:", 2 - np.linalg.matrix_rank(A))
```
I can also produce a sympy snippet.

I must include ML payoff: "why linear algebra matters for machine learning" with concrete examples:
For instance: "Linear maps and matrices are used in deep learning as the building blocks of neural networks. The transformation applied to input features by weights in hidden layers is modeled as a matrix multiplication. Also, dimensionality reduction techniques such as PCA rely on eigenvector computations." I'll produce some details.

Symbol discipline: every symbol defined when appears.
I must produce a "symbol reference table" if multiple symbols are introduced. But how many symbols? Possibly we have vectors denoted by bold lowercase letters (v) but since we're in plain text, maybe I'll denote them as v = (x1, x2, ...) but I need to define each symbol on first occurrence. For example: "Let vector v be represented as (v1, v2,...)".
I can produce a table listing symbols and definitions if necessary:
Maybe after the section I'll include a block with a table of symbols used.

We have new symbols: Let V denote a set or vector space, maybe F denotes field; let v be a generic vector, etc. Possibly also use "dim" for dimension and "span". Possibly produce something like:
Symbol Table:
- R: the set of real numbers.
- F: the underlying field (typically R).
- v: a typical vector in V.
- +: vector addition
- scalar multiplication: c * v.

I must include explanation to check out-loud, at end "explain-out-loud check" prompt. Perhaps I'll say: "Now, explain out loud what you've learned about vectors and linear maps from this section."

I need to ensure that instructions are adhered exactly. I must produce a complete markdown document with YAML front matter.

I should include the computational exercise code snippet as a separate fenced block (like triple backticks) with language specifier.

We must produce text in direct, warm tone, and avoid unexplained symbols across page breaks. So every new symbol is explained in that sentence it appears.

Plan outline:

1. YAML Front Matter
2. Title: "Linear Algebra for ML - Foundations Primer" maybe with a header.
3. Introduction paragraph: "Welcome to your primer on linear algebra for machine learning." etc.

4. Section Vectors and Vector Spaces:
   - Intuitive Bridge: Explain arrays in programming, like lists or arrays that hold numbers. For example, a vector is simply an ordered list of numbers. In many languages, you'll use loops over array indices. 
   - Then formal definition: "A vector is an element of a set V over a field F (usually the real numbers R). The set V with operations addition and scalar multiplication satisfying these axioms forms a vector space."
   - List vector space axioms if needed.

5. Basis, Dimension:
   - Intuitive Bridge: Think about the minimum set of ingredients (like basis elements) that you can combine to make any recipe (vector) in your vector space.
   - Formal definition: "A subset B ⊆ V is a basis for V if every vector v ∈ V can be uniquely expressed as a linear combination of elements in B, and no proper subset of B has this property. The number of elements in the basis is called the dimension."
   - Provide example with R^2.

6. Linear Maps:
   - Intuitive Bridge: Think about functions that preserve structure. In programming, a function that transforms one array to another but preserves relationships between elements is like a linear map.
   - Formal definition: "A function f: V → W (with V and W vector spaces over the same field F) is called linear if for all vectors u,v ∈ V and scalars c in F, f(u+v)=f(u)+f(v), and f(c*u)=c*f(u)."
   - Provide example with a 2D transformation.

7. Matrices as Representations of Linear Maps:
   - Intuitive Bridge: In your spreadsheets, you arrange numbers into rows and columns; similarly, matrices represent linear maps in finite-dimensional spaces.
   - Formal definition: "A matrix A ∈ F^(m×n) is an array of m by n numbers arranged in rows and columns. The multiplication of a vector v ∈ R^n with the matrix A yields another vector in R^m."
   - Provide example using our worked numerical example with a non-invertible matrix.

8. Rank-Nullity Theorem:
   - Intuitive Bridge: In programming, you might think about what information is preserved and lost under a transformation; similarly, every linear map has an input dimension that splits into the parts that survive (the image) and those that vanish (kernel).
   - Formal statement: "For any linear map f: V → W, if we let ker(f) be its kernel (nullspace) and im(f) its image (range), then dim(V)=dim(ker(f)) + dim(im(f))."
   - Provide the worked numerical example with our matrix M = [ [1,2],[2,4] ].
   - Step by step explanation.

9. Symbol Reference Table:
   - We need a table that lists each symbol and its definition (if we have more than one). I'll produce a small table at the bottom of the document.
   - Which symbols? Possibly: R for real numbers, F for field, V vector space, f linear map, M matrix, dim dimension, etc.

10. ML Payoff:
    - Explain why these ideas matter in machine learning. For instance, matrices and vectors are used to represent data and perform transformations, e.g., in neural networks and PCA.
    - Provide concrete examples: "In a neural network, each layer applies a linear transformation followed by a non-linear activation; the weights are stored as matrices."

11. TIERED MEMORY SUMMARY:
   - Create a section with headings "CARRY (memorize, max 7)", "RECONSTRUCT (re-derive)", and "LOOKUP (never memorize)". Provide bullet points summarizing key takeaways.
   - For example: CARRY: The idea of vector spaces, the definition of linear maps, etc.

12. Computational Exercise:
    - Provide a small exercise using Python code snippet with NumPy or SymPy that allows one to compute matrix rank and nullity.
    - Possibly also produce instructions on how to run it.

13. "Explain-out-loud check" prompt at the end: "Now explain out loud what you learned about linear maps from this section."

I need to ensure that every symbol is defined when used, e.g., "R", "F", etc. I must not use any unexplained symbols across page breaks.

I must produce a final answer that is output as one markdown document in plain text with YAML front matter included, and then content inside the markdown file.

Let's produce final document accordingly.

I'll produce headings with # for each section maybe.
- YAML front matter: triple dash lines.

The document:
```
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

# Linear Algebra for Machine Learning - Foundations Primer

Welcome, fellow programmer! This section is designed to warm up your working memory with the fundamental ideas of linear algebra that are crucial for machine learning. Think of it like setting up a spreadsheet where each cell holds a number; we'll now see how these numbers come together to form powerful mathematical structures.

## Vectors as Objects

Before diving into formal definitions, picture an array in your programming language—say a list or tuple of numbers. In linear algebra, such arrays are called vectors. They are the building blocks that you’ll use to represent data points, coefficients, and more.

Now, here’s the formal definition:
- A vector is defined as an element of a set V over a field F (typically the real numbers ℝ). Formally, we denote vectors with symbols like v, where v can be represented as an ordered tuple of numbers. For example, in ℝ², a typical vector v might look like v = (v₁, v₂).

## Vector Spaces and Closure

Imagine you have a collection of arrays that behave nicely under operations such as addition and scalar multiplication (multiplying each element by a number). That’s what we call a vector space.

The formal definition is:
- A vector space V over a field F (commonly the set ℝ of real numbers) is a set equipped with two operations:
  1. Vector addition: For any u, v ∈ V, their sum u + v is also in V.
  2. Scalar multiplication: For any scalar c ∈ F and any vector v ∈ V, the product c * v (each component of v multiplied by c) is in V.

These operations must satisfy a list of axioms (associativity, commutativity of addition, distributive properties, existence of an additive identity 0, etc.)—all ensuring that our intuitive notion of "array arithmetic" holds true mathematically.

## Basis and Dimension

Intuitive Bridge:
Think of a basis as the minimal set of “ingredient vectors” you need to mix together (via linear combinations) to create any vector in your space. It’s like having a recipe where each ingredient can be scaled and combined uniquely to make every dish possible.

Formal Definition:
- A subset B ⊆ V is called a basis for V if:
  1. Every vector v ∈ V can be written as a linear combination of the vectors in B.
  2. The representation of any vector as such a linear combination is unique.
The number of elements in the basis, denoted by dim(V), is called the dimension of the vector space.

For example, in ℝ², one common basis is {(1, 0), (0, 1)} because every vector (x, y) can be uniquely written as x*(1,0) + y*(0,1).

## Linear Maps

Intuitive Bridge:
Recall functions in your code that transform arrays: they might take an array of inputs and produce another array while preserving certain relationships. In linear algebra, a function between vector spaces that respects addition and scalar multiplication is called a linear map.

Formal Definition:
- A function f: V → W (where V and W are vector spaces over the same field F) is said to be linear if for all vectors u, v ∈ V and any scalar c ∈ F, it satisfies:
  1. f(u + v) = f(u) + f(v)
  2. f(c * u) = c * f(u)

For instance, consider the function f(x, y) = (x + y, 3x - 2y), which maps ℝ² to ℝ². It is linear because it satisfies both properties above.

## Matrices as the Spreadsheet Form of a Map

Intuitive Bridge:
Think about how you arrange numbers in rows and columns in a spreadsheet—this is exactly what matrices do. A matrix represents a linear map in finite-dimensional vector spaces, essentially serving as a recipe that transforms one array into another via multiplication.

Formal Definition:
- An m×n matrix over a field F (typically ℝ) is an ordered arrangement of m rows and n columns:
  
  For example, let M be a 2×2 matrix given by
  
  M = [ [a₁₁, a₁₂],
        [a₂₁, a₂₂] ]
  
  where each aᵢⱼ ∈ F. When you multiply this matrix with an n-dimensional vector v (v = (v₁, v₂) for ℝ²), the result is another m-dimensional vector given by:
  
  M * v = (a₁₁*v₁ + a₁₂*v₂, a₂₁*v₁ + a₂₂*v₂).

## Rank-Nullity Theorem

Intuitive Bridge:
When you apply a transformation to your data, some parts may vanish entirely while others change in predictable ways. In linear algebra, we quantify this by splitting the input space into two complementary pieces: the kernel (where data gets “lost”) and the image (what remains).

Formal Statement:
For any linear map f: V → W,
  
  dim(V) = dim(ker(f)) + dim(im(f))
  
where
- ker(f) is the kernel (or nullspace): the set of all vectors v in V such that f(v) = 0.
- im(f) is the image (or range): the set of all vectors w in W for which there exists a v ∈ V with f(v) = w.

### Concrete Worked Example

Consider the matrix A defined by:
  
  A = [ [1, 2],
        [2, 4] ]
  
Let’s examine how A acts on an arbitrary vector v ∈ ℝ². Let v = (a, b). Then
  
  A * v = (a + 2b, 2a + 4b).

Notice that the second component is exactly twice the first:
  
  2a + 4b = 2*(a + 2b).
  
This tells us every output lies on the line y = 2x in ℝ². Hence, the image of A (or its range) is one-dimensional.

Next, find the kernel (nullspace). We solve for v such that:
  
  a + 2b = 0.
  
Solving this gives:
  
  a = -2b.
  
Thus, any vector in ker(A) has the form (-2t, t) for some scalar t. This is a one-dimensional subspace.

By the Rank-Nullity Theorem,
  
  dim(ℝ²) = rank(A) + nullity(A)
  2 = 1 + 1.
  
This confirms our computations.

## ML Payoff

In machine learning, these linear algebra concepts are everywhere! For example:

- Neural networks rely on layers that apply linear transformations (via matrices) to their inputs. Each layer’s weights form a matrix that transforms data before applying non-linear activation functions.
- Dimensionality reduction techniques like Principal Component Analysis (PCA) depend on decomposing data into orthogonal components—a process steeped in linear algebra.
- Data preprocessing and feature extraction often involve operations such as vector normalization and transformations, which are based on the properties of vector spaces.

## TIERED MEMORY SUMMARY

Let’s break down what you should remember:

### CARRY (memorize, max 7 key ideas)
1. Vectors are ordered collections of numbers.
2. A vector space is a set closed under addition and scalar multiplication.
3. A basis is a minimal set of vectors that uniquely span the entire space.
4. The dimension of a vector space is the number of elements in any basis.
5. A linear map preserves both vector addition and scalar multiplication.
6. Matrices are finite representations of linear maps (like spreadsheets).
7. The Rank-Nullity Theorem states: dim(V) = dim(ker(f)) + dim(im(f)).

### RECONSTRUCT (re-derive)
• Derive the matrix-vector product rule for a given 2×2 matrix.
• Show that every vector in ℝ² can be uniquely expressed as a combination of basis vectors.

### LOOKUP (never memorize; always refer to a trusted source)
• The precise axioms of vector spaces.
• Detailed properties and proofs of the Rank-Nullity Theorem.
• Definitions and examples of more advanced linear maps and transformations.

## Symbol Reference Table

| Symbol | Meaning                                                     |
|--------|-------------------------------------------------------------|
| ℝ      | The set of real numbers (our typical field).               |
| F      | An arbitrary field (usually ℝ in our context).             |
| V      | A vector space over the field F.                            |
| v, u   | Typical vectors in a vector space V.                       |
| +      | Vector addition operation.                                  |
| · or * | Scalar multiplication and matrix-vector multiplication.    |
| dim(V) | The dimension of vector space V (number of basis elements). |
| ker(f) | Kernel (nullspace) of a linear map f.                      |
| im(f)  | Image (range) of a linear map f.                            |

## Computational Exercise

Try the following exercise in Python using NumPy to compute the rank and nullity of a matrix:

```python
import numpy as np

# Define a 2x2 matrix A, corresponding to our worked example.
A = np.array([[1, 2],
              [2, 4]])

# Compute the rank of A
rank_A = np.linalg.matrix_rank(A)
print("Rank of A:", rank_A)

# Since we are working in ℝ², the nullity is given by:
nullity_A = 2 - rank_A
print("Nullity of A:", nullity_A)
```

Run this code to verify that for our matrix A, rank is 1 and nullity is also 1.

## Explain-Out-Loud Check

Now, take a moment and explain out loud what you have learned about vectors and linear maps in this section. How do these concepts relate to familiar programming constructs such as arrays, loops, and functions? Reflect on how understanding these ideas helps build the foundation for machine learning algorithms.