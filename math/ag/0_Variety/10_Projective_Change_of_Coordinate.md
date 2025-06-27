---
hide_hero: true
menubar: math_menubar
permalink: /math/ag/Variety/Projective_Change_of_Coordinate
---
## Change of Coordinates and Projective Linear Group

### Affine Change of Coordinates

In affine space $\mathbb{A}^n(k)$, a **change of coordinates** is given by an **affine linear transformation**:

$$ \vec{x} \mapsto A \vec{x} + \vec{b} $$

where $A \in \mathrm{GL}_n(k)$ is an invertible $n \times n$ matrix and $\vec{b} \in k^n$ is a translation vector. Such transformations form the **affine group**:

$$ \mathrm{Aff}_n(k) = \mathrm{GL}_n(k) \ltimes k^n $$

This group acts on $\mathbb{A}^n(k)$ and preserves affine properties like collinearity and ratios of distances along lines.

---

### Projective Change of Coordinates

In projective space $\mathbb{P}^n(k)$, a change of coordinates corresponds to applying an invertible linear transformation of $k^{n+1}$:

$$ (x_0 : x_1 : \cdots : x_n) \mapsto (x_0', x_1', \ldots, x_n') = A(x_0, x_1, \ldots, x_n)^T $$

where $A \in \mathrm{GL}_{n+1}(k)$. However, since projective points are only defined up to scalar, two matrices $A$ and $\lambda A$ (for $\lambda \in k^\times$) induce the same projective transformation. Thus, the group of projective coordinate changes is:

$$ \mathrm{PGL}_{n+1}(k) = \mathrm{GL}_{n+1}(k) / k^\times $$

This is called the **projective general linear group**.

---

### Action on Projective Space

An element of $\mathrm{PGL}_{n+1}(k)$ acts on $\mathbb{P}^n(k)$ by:

$$ A \cdot (x_0 : x_1 : \cdots : x_n) = (x_0' : x_1' : \cdots : x_n') $$

where $(x_0', \ldots, x_n') = A (x_0, \ldots, x_n)^T$, and the result is interpreted modulo scalar. This action:

- Preserves incidence relations (e.g., whether points lie on a line),
- Maps lines to lines,
- Is transitive on triples of points in general position (when $n = 1$).

---

### Example: Projective Line $\mathbb{P}^1(k)$

When $n = 1$, $\mathrm{PGL}_2(\mathbb{C})$ acts on $\mathbb{P}^1(\mathbb{C}) = \mathbb{C}\cup\\{\infty\\}$ by **fractional linear transformations**:

$$ \begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \cdot (x : y) = (ax + by : cx + dy) $$

In affine coordinates $z = x/y$, this becomes the familiar **Möbius transformation**:

$$ z \mapsto \frac{az + b}{cz + d} $$

with $ad - bc \ne 0$.
