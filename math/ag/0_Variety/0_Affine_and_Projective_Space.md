---
hide_hero: true
menubar: math_menubar
permalink: /math/ag/Variety/Affine_and_Projective_Space
---
## Affine and Projective Space

**Definition (Affine Space).**  
Let $k$ be a field. The **affine $n$-space** over $k$, denoted $\mathbb{A}^n(k)$, is defined as:

$$\mathbb{A}^n(k) = \{ (x_1, x_2, \ldots, x_n) \mid x_i \in k \}$$

A **polynomial** $f \in k[x_1, \ldots, x_n]$ defines a **vanishing set** (or **affine algebraic set**):

$$V_a(f) = \{ (x_1, \ldots, x_n) \in \mathbb{A}^n(k) \mid f(x_1, \ldots, x_n) = 0 \}$$

---

**Definition (Projective Space).**  
The **projective space** $\mathbb{P}^n(k)$ is the set of lines through the origin in $k^{n+1}$. That is,

$$\mathbb{P}^n(k) = \left( k^{n+1} \setminus \{0\} \right) \big/ \sim$$

where two nonzero vectors $(x_0, \ldots, x_n) \sim (\lambda x_0, \ldots, \lambda x_n)$ for $\lambda \in k^\times$ are considered equivalent. A point in projective space is written in **homogeneous coordinates**:

$$(x_0 : x_1 : \cdots : x_n)$$

---

### Affine Charts and Hyperplanes at Infinity

Projective space $\mathbb{P}^n(k)$ can be covered by **affine charts**, each corresponding to setting one of the coordinates $x_i \ne 0$. For example, the chart $\\{x_0 \ne 0\\}$ identifies projective points with affine points via:

$$(x_0 : x_1 : \ldots : x_n) \mapsto \left( \frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0} \right)$$

This yields an isomorphism:

$$\mathbb{A}^n(k) \cong \{ x_0 \ne 0 \} \subset \mathbb{P}^n(k)$$

The **hyperplane at infinity** $H$ is defined by $H = \\{x_0 = 0\\}$. It "completes" affine space by adding points "at infinity," making the geometry more symmetric.

We observe that $H \simeq \mathbb{P}^{n-1}(k)$, and the full projective space decomposes as:

$$\mathbb{P}^n(k) = \mathbb{A}^n(k) \cup H$$

---

**Examples.**

1. Points in $\mathbb{P}^1(k)$ have coordinates $(x : y)$, not both zero, modulo scaling.  
   - **Affine chart** $\\{y \neq 0\\}$: we may use the representative $(x : 1)$, corresponding to $x \in \mathbb{A}^1(k)$
   - **Point at infinity**: $\infty = (1 : 0)$

    Thus, we have $\mathbb{P}^1(k) = \mathbb{A}^1(k) \cup \\{ \infty \\}$

2. Points in $\mathbb{P}^2(k)$ are given by $(x : y : z)$, not all zero, modulo scaling.  
   - **Affine chart** $\\{z \neq 0\\}$: write $(x/z, y/z, 1)$, giving coordinates in $\mathbb{A}^2(k)$
   - **Line at infinity**: $\\{(x:y:0)\in\mathbb{P}^2(k)\\}\simeq\mathbb{P}^1(k)$

    So we view: $\mathbb{P}^2(k) = \mathbb{A}^2(k) \cup \mathbb{P}^1(k)$

---

### Homogeneous Polynomials and Homogenization

**Definition (Homogeneous Polynomial).**  
A **homogeneous polynomial** $f(x_0, \ldots, x_n)$ of degree $d$ is a polynomial in which every monomial term has total degree $d$. It satisfies the scaling relation:

$$f(\lambda x_0, \ldots, \lambda x_n) = \lambda^d f(x_0, \ldots, x_n)$$

Such a polynomial defines a **projective vanishing set**:

$$V_p(f) = \{ (x_0 : \cdots : x_n) \in \mathbb{P}^n(k) \mid f(x_0, \ldots, x_n) = 0 \}$$

This is well-defined: if $f$ is homogeneous and $f(\vec{x}) = 0$, then $f(\lambda \vec{x}) = \lambda^d f(\vec{x}) = 0$, so the vanishing condition depends only on the class $(x_0 : \cdots : x_n)$.

**Definition (Homogenization).**  
Given a (non-homogeneous) polynomial $f(x_1, \ldots, x_n)$ of total degree $d$, its **homogenization** is defined as:

$$f^h(x_0, x_1, \ldots, x_n) = x_0^d \cdot f\left( \frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0} \right)$$

This yields a homogeneous polynomial of degree $d$ in the variables $x_0, \ldots, x_n$.

Setting $x_0 = 1$ recovers the original polynomial $f(x_1, \ldots, x_n)$ — this process is called **dehomogenization**. In terms of vanishing sets, we have:

$$V_p(f^h) \cap \mathbb{A}^n(k) = V_a(f)$$

---

### Lines in $\mathbb{P}^2(k)$

A **line** in $\mathbb{P}^2(k)$ is defined by a degree-1 homogeneous polynomial:

$$ax + by + cz = 0$$

- If at least one of $a$ or $b$ is nonzero, the line intersects the affine plane $\mathbb{A}^2(k)$ (in the chart $z \ne 0$) at the affine line $ax + by + c = 0$, and extends to a point at infinity.
- If $a = b = 0$, then the equation reduces to $cz = 0$, which defines the **line at infinity**, and does not intersect the affine chart $\{z \ne 0\}$.

Any two distinct lines in $\mathbb{P}^2(k)$ intersect at exactly one point. Non-parallel lines intersect in the affine chart, while parallel lines intersect at a point on the line at infinity.
