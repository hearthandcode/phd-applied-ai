---
module: M01
formalism_density: 0.4
status: draft
learner_id: L001
title: "Attention Mechanisms as Linear Algebra"
calibration: "MIT 18.06 (Strang) — attention from first principles, ML emphasis"
---

# Section 7 — Attention Mechanisms as Linear Algebra

## 7.0 Bridge: attention is where linear algebra meets information retrieval

You already know two ideas in your hands. From programming: a dictionary lookup —
you have a **key** you're searching for, you compare it against stored keys, and
you pull back the matching **value**. From the last sections: the **dot product**
measures how aligned two vectors are (big when they point the same way, near zero
when perpendicular).

Attention is what you get when you make dictionary lookup *continuous* using dot
products. Instead of "find the one key that matches exactly and return its value,"
attention says "compare my query against *every* key, see how well each matches
(dot product), turn those match-scores into weights that sum to 1 (softmax), and
return a *blend* of all the values, weighted by how well their keys matched."

That's the whole mechanism. Soft, differentiable dictionary lookup. The headline
that powers transformers — GPT, BERT, every modern LLM — is, underneath the hype,
three linear maps and a weighted average. The eureka: **there is no magic here,
only matrix multiplication and a normalization.** Once you see that, attention
stops being a black box and becomes something you can read off the dimensions.

This section builds it from the linear algebra up, then has you write a single
attention head in pure NumPy — no PyTorch, no autograd, just the matrices.

---

## 7.1 Query, key, value as linear maps

### Conceptual bridge

Start with a sequence of tokens — say the words in a sentence — each already
turned into a vector (an embedding). Stack them as rows of a matrix $X$. If you
have $n$ tokens each of dimension $d_{\text{model}}$, then $X$ is
$n \times d_{\text{model}}$.

Now, the same token plays *three different roles* in attention, and we want a
learned way to extract each role. A linear map (a weight matrix) is exactly "a
learnable way to re-express vectors." So we make three of them — one per role.

### The definitions

$$Q = X W_Q, \qquad K = X W_K, \qquad V = X W_V$$

- $X$ — the input, $n \times d_{\text{model}}$ ($n$ tokens, each a row vector).
- $W_Q, W_K, W_V$ — learned weight matrices ($d_{\text{model}} \times d_k$ for
  $W_Q,W_K$; $d_{\text{model}} \times d_v$ for $W_V$). These are the *only*
  learned parameters in a head.
- $Q$ ("queries", $n\times d_k$) — each row asks: *"what am I looking for?"*
- $K$ ("keys", $n\times d_k$) — each row advertises: *"here's what I offer."*
- $V$ ("values", $n\times d_v$) — each row carries: *"here's the content I'll
  hand over if you attend to me."*

Each is just $X$ pushed through a linear map — the same projection idea from
Section 1, now learned by gradient descent. Query and key live in the same space
(dimension $d_k$) because we're about to compare them with a dot product, and you
can only dot vectors of equal length.

### Worked example (concrete shapes)

Picture a 3-token sentence with embedding dimension 4, projected down to $d_k=2$:

- $X$ is $3\times 4$. $W_Q,W_K$ are $4\times 2$, $W_V$ is $4\times 2$.
- $Q = XW_Q$ is $3\times 2$: three queries, each a 2-vector.
- $K = XW_K$ is $3\times 2$, $V = XW_V$ is $3\times 2$.

Token 1's query (row 1 of $Q$) will get compared against all three keys to decide
how much of each token's value it should absorb. Notice nothing here cares about
*word order* yet — that's why transformers bolt on positional encodings
separately. Attention itself is order-blind; it's a set operation dressed up with
position information.

> **Try this in Hermes:** "Quiz me on shapes: if $X$ is $10\times 512$ and
> $d_k=64$, what are the shapes of $W_Q$, $Q$, $K$, and $QK^\top$?"
> **Try this in Claude:** "Why do query and key share a dimension $d_k$ but value
> can have its own $d_v$? What breaks if I make $d_k \ne$ the key dimension?"

---

## 7.2 Attention scores: scaled dot products and softmax

### Conceptual bridge

Now the lookup. Every query needs a match-score against every key. The dot product
is our alignment meter. Stack all queries against all keys at once and you get an
$n\times n$ table of scores: entry $(i,j)$ is "how much does token $i$'s query
align with token $j$'s key?" That single matrix multiply, $QK^\top$, computes
*all* pairwise comparisons in one shot — this is why attention is so
GPU-friendly.

Then two finishing moves: **scale** (divide by $\sqrt{d_k}$) and **normalize**
(softmax each row so the weights are positive and sum to 1).

### The definition

$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) V$$

Read it left to right:
- $QK^\top$ — the $n\times n$ score matrix; row $i$, column $j$ is the dot product
  of query $i$ with key $j$.
- $\frac{1}{\sqrt{d_k}}$ — the **scaling factor** (more in §7.3).
- $\text{softmax}(\cdot)$ — applied row-wise: turns each row of scores into a
  probability distribution (exponentiate, then divide by the row sum). Each row
  now sums to 1 — these are the **attention weights**.
- Multiply by $V$ — each output row is a weighted average of all value rows, using
  that row's attention weights. High weight on token $j$ → token $j$'s value
  dominates the output.

So output row $i$ = "the blend of values that token $i$ chose to pay attention
to." The score matrix is the *who-looks-at-whom*; multiplying by $V$ is the
*actually-fetch-the-content*.

### The role of dimension $d_k$ — why divide by $\sqrt{d_k}$

This is the detail people memorize without understanding, so let's grok it.
A dot product of two $d_k$-dimensional vectors is a sum of $d_k$ products. If the
entries are roughly independent with unit variance, that sum has variance about
$d_k$ — so its *standard deviation* grows like $\sqrt{d_k}$. As $d_k$ gets large
(64, 128, …), raw scores get large in magnitude.

Why does that hurt? Softmax of large-magnitude inputs **saturates**: it puts
almost all weight on the single biggest score and nearly zero everywhere else
(it becomes a hard argmax). Saturated softmax has near-zero gradient — learning
stalls. Dividing by $\sqrt{d_k}$ rescales the scores back to unit-ish variance,
keeping softmax in its soft, well-gradiented regime. **The $\sqrt{d_k}$ is a
variance-control trick, pure and simple** — a direct consequence of how dot-product
magnitude scales with dimension.

### Worked example (the saturation, numerically)

```python
import numpy as np

def softmax(z, axis=-1):
    z = z - z.max(axis=axis, keepdims=True)   # numerical stability
    e = np.exp(z)
    return e / e.sum(axis=axis, keepdims=True)

d_k = 64
q = np.random.randn(d_k)
k = np.random.randn(d_k)

raw    = q @ k
scaled = raw / np.sqrt(d_k)
print(f"raw score    ~ {raw:6.2f}   (std grows like sqrt(d_k) = {np.sqrt(d_k):.1f})")
print(f"scaled score ~ {scaled:6.2f}  (back near unit scale)")

# Saturation demo: a row of scores, with and without scaling
scores = np.array([8.0, 6.0, 5.5, 5.0])      # large -> nearly one-hot
print("unscaled softmax:", softmax(scores).round(3))
print("scaled   softmax:", softmax(scores / np.sqrt(d_k)).round(3))
# Unscaled is almost a hard argmax (tiny gradient); scaled stays soft.
```

> **Try this in Hermes:** "Make me derive why the dot product of two unit-variance
> $d_k$-vectors has std $\approx\sqrt{d_k}$. Then explain in one sentence why that
> motivates the scaling."
> **Try this in Claude:** "Show me what attention weights look like as I crank
> $d_k$ from 4 to 4096 *without* the scaling — at what point does softmax collapse
> to argmax?"

---

## 7.3 Multi-head attention: parallel projections

### Conceptual bridge

One attention head can only learn one notion of "relevance." But language needs
many at once — one head might track subject–verb agreement, another might track
which pronoun refers to which noun, another local phrasing. The fix is delightfully
simple: **run several heads in parallel, each with its own $W_Q, W_K, W_V$, then
concatenate their outputs and mix them with one more linear map.**

Each head projects the tokens into its *own* smaller subspace ($d_k = d_{\text{model}}/h$
for $h$ heads), does the attention dance there, and reports back. It's
divide-the-representation-space-and-specialize. Geometrically: each head looks at
the tokens from a different low-dimensional angle.

### The definition

$$\text{head}_i = \text{Attention}(XW_Q^{(i)}, XW_K^{(i)}, XW_V^{(i)})$$
$$\text{MultiHead}(X) = \big[\text{head}_1 \,\|\, \text{head}_2 \,\|\, \cdots \,\|\, \text{head}_h\big]\, W_O$$

- $h$ — the number of heads.
- $W_Q^{(i)},W_K^{(i)},W_V^{(i)}$ — head $i$'s own projection matrices (each
  projects to dimension $d_k = d_{\text{model}}/h$, so total parameters stay
  comparable to one big head).
- $\|$ — horizontal concatenation of the head outputs into an $n\times d_{\text{model}}$
  matrix.
- $W_O$ — the **output projection** ($d_{\text{model}}\times d_{\text{model}}$),
  which mixes the heads' findings back together.

The keeping-parameter-count-fixed move ($d_k = d_{\text{model}}/h$) is why
multi-head is nearly free: 8 heads of dimension 64 cost about the same as 1 head
of dimension 512, but you get 8 specialized views instead of 1 muddled one.

> **Try this in Hermes:** "If $d_{\text{model}}=512$ and $h=8$, what is $d_k$ per
> head, and what's the shape of the concatenated output before $W_O$?"
> **Try this in Claude:** "Explain why concatenate-then-project ($W_O$) is needed —
> what would go wrong if we just summed the heads instead?"

---

## 7.4 Python: a single attention head from scratch (NumPy only)

This is the payoff — the whole mechanism, no framework, every shape annotated.
Read it as the literal restatement of §7.1–7.2.

```python
import numpy as np

def softmax(z, axis=-1):
    z = z - z.max(axis=axis, keepdims=True)   # stability: subtract row max
    e = np.exp(z)
    return e / e.sum(axis=axis, keepdims=True)

def attention_head(X, W_Q, W_K, W_V, mask=None):
    """One scaled-dot-product attention head, pure NumPy.
       X:   (n, d_model)   token embeddings (rows)
       W_*: (d_model, d_k) learned projections
       returns: (n, d_v) attended outputs, and the (n, n) attention weights."""
    Q = X @ W_Q                       # (n, d_k)  -- "what each token seeks"
    K = X @ W_K                       # (n, d_k)  -- "what each token offers"
    V = X @ W_V                       # (n, d_v)  -- "content each token carries"

    d_k = Q.shape[1]
    scores = (Q @ K.T) / np.sqrt(d_k) # (n, n)    -- scaled pairwise alignment

    if mask is not None:              # e.g. causal mask for GPT-style decoding
        scores = np.where(mask, scores, -1e9)

    weights = softmax(scores, axis=-1)# (n, n)    -- each row sums to 1
    output  = weights @ V             # (n, d_v)  -- weighted blend of values
    return output, weights

# --- run it on a tiny 3-token, d_model=4 example ---
np.random.seed(0)
n, d_model, d_k = 3, 4, 2
X   = np.random.randn(n, d_model)
W_Q = np.random.randn(d_model, d_k)
W_K = np.random.randn(d_model, d_k)
W_V = np.random.randn(d_model, d_k)

out, attn = attention_head(X, W_Q, W_K, W_V)
print("attention weights (each row sums to 1):")
print(attn.round(3), "\nrow sums:", attn.sum(axis=1).round(3))
print("\noutput (n x d_v):\n", out.round(3))

# Causal mask demo: token i may only attend to tokens <= i (GPT-style)
causal = np.tril(np.ones((n, n), dtype=bool))
out_c, attn_c = attention_head(X, W_Q, W_K, W_V, mask=causal)
print("\ncausal attention weights (upper triangle is zeroed):")
print(attn_c.round(3))
```

Run it and *stare at the weight matrix*. Each row is a probability distribution —
that row's token deciding how to split its attention across the sequence. The
causal version zeros out the future (upper triangle), which is the one extra line
that turns this into the attention inside GPT. You just built the core of a
transformer in ~15 lines.

> **Try this in Hermes:** "Have me extend this to multi-head: loop over $h$ heads,
> concatenate, apply $W_O$. Check my shapes at each step."
> **Try this in Claude:** "I built a single head in NumPy. Help me verify it
> matches `torch.nn.functional.scaled_dot_product_attention` on the same inputs."

---

## 7.5 Connections to ML — the attention family tree

The single head you wrote is the atom; here's the molecule it builds:

- **Self-attention (BERT, GPT).** $Q$, $K$, $V$ all come from the *same* sequence
  $X$ — tokens attend to each other. BERT does it *bidirectionally* (no mask,
  every token sees every other) for understanding; GPT does it *causally* (the
  triangular mask you coded) so each token only sees the past, enabling
  left-to-right generation. The *only* difference between "understanding" and
  "generation" attention is that mask.

- **Cross-attention (encoder–decoder, e.g. translation, T5).** $Q$ comes from one
  sequence (the decoder's current state) while $K, V$ come from *another* (the
  encoder's output). This is how a translation decoder "looks back at" the source
  sentence — the query asks the source what's relevant right now. Same equation,
  different sources for $Q$ vs. $K,V$.

- **Why this scales.** Everything is matmul + softmax — exactly what GPUs/TPUs
  devour. The cost is the $n\times n$ score matrix: $O(n^2)$ in sequence length,
  which is *the* bottleneck behind long-context research (FlashAttention, linear
  attention, sparse attention all attack this $n^2$). You can see the wall right
  there in the `Q @ K.T` line.

The conceptual win for your thesis: attention is **content-addressable memory done
with linear algebra**. That same "soft retrieval by alignment" pattern is exactly
how a RAG tutor in H&C fetches relevant knowledge for a learner's query —
attention is the in-network version of the retrieval you'll build into the
platform.

---

## 7.6 Section recap

**Explain out loud (no notes):**
1. "Attention is soft dictionary lookup because…" — name what plays the role of
   query, key, value.
2. "The formula is $\text{softmax}(QK^\top/\sqrt{d_k})V$, and each piece does…"
   — narrate the four steps.
3. "We divide by $\sqrt{d_k}$ because…" — connect dot-product variance to softmax
   saturation.
4. "Multi-head helps because…" and "the difference between BERT and GPT attention
   is…"

If the $\sqrt{d_k}$ explanation wobbles, that's the deepest idea in the section —
reread §7.2.

### Memory tiers for THIS section

**CARRY (memorize):**
- $Q=XW_Q,\; K=XW_K,\; V=XW_V$ (three roles, three linear maps)
- $\text{Attention}(Q,K,V) = \text{softmax}\!\big(\frac{QK^\top}{\sqrt{d_k}}\big)V$
- "Attention = soft, differentiable dictionary lookup via dot products"
- Self-attention: $Q,K,V$ from same sequence; cross-attention: $Q$ separate

**RECONSTRUCT (re-derive):**
- Why $\sqrt{d_k}$: dot-product std $\sim\sqrt{d_k}$ → softmax saturation
- Multi-head shapes: $d_k = d_{\text{model}}/h$, concat then $W_O$
- The causal mask as the one change from BERT-style to GPT-style
- The NumPy head, line by line

**LOOKUP (know it exists):**
- Positional encoding schemes (sinusoidal, RoPE, ALiBi)
- $O(n^2)$ fixes (FlashAttention, linear/sparse attention)
- LayerNorm/residual placement around the attention block

> **Closing interaction prompt —**
> **Try this in Hermes:** "Give me a 4-token toy sentence; have me hand-trace one
> attention head's weight matrix and explain which token attends to which and why."
> **Try this in Claude:** "Relate the attention head I wrote to how an H&C RAG
> tutor retrieves relevant concepts for a learner query — what's the analogue of
> $Q$, $K$, and $V$ there?"
