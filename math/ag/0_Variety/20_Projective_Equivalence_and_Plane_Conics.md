---
hide_hero: true
menubar: math_menubar
permalink: /math/ag/Variety/Projective_Equivalence_and_Plane_Conics
---
## Projective Equivalence and Plane Conics

### Projective Equivalence of Points

In projective geometry, the group $\mathrm{PGL}_{n+1}(k)$ acts transitively on certain configurations of points in $\mathbb{P}^n(k)$.

- **$\mathbb{P}^1(k)$: 3-Transitivity**

  Any ordered triple of distinct points in $\mathbb{P}^1(k)$ can be mapped to any other such triple by a unique projective transformation. That is:

  > Given any three distinct points $(P_1, P_2, P_3)$ and $(Q_1, Q_2, Q_3)$ in $\mathbb{P}^1(k)$, there exists a unique $T \in \mathrm{PGL}_2(k)$ such that $T(P_i) = Q_i$ for $i = 1, 2, 3$.

  This property reflects the 3-dimensional nature of $\mathrm{PGL}_2(k)$ and the fact that homogeneous coordinates in $\mathbb{P}^1(k)$ are only defined up to scalar.

- **$\mathbb{P}^2(k)$: 4-Transitivity in General Position**

  Any ordered quadruple of points in $\mathbb{P}^2(k)$ in general position (i.e. no three lie on the same line) is projectively equivalent to any other such quadruple. More precisely:

  > If $(P_1, P_2, P_3, P_4)$ and $(Q_1, Q_2, Q_3, Q_4)$ are two ordered sets of points in general position in $\mathbb{P}^2(k)$, then there exists a unique $T \in \mathrm{PGL}_3(k)$ such that $T(P_i) = Q_i$ for $i = 1, 2, 3, 4$.

---

### Conics in the Projective Plane

A **conic** in $\mathbb{P}^2(k)$ is defined by a homogeneous polynomial of degree 2:

$$ f(x, y, z) = ax^2 + by^2 + cz^2 + dxy + exz + fyz = 0 $$

This can be represented compactly using a symmetric $3 \times 3$ matrix $M$:

$$ f(x, y, z) = 
\begin{bmatrix}
x & y & z
\end{bmatrix}
M
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} $$

where 

$$M = \begin{bmatrix}a & d & e \\ d & b & f \\ e & f & e\end{bmatrix}.$$

We call $M$ as a matrix representation of the conic.

---

### Types of Conics

- A **smooth conic** is one which the corresponding matrix is invertible.
- A **degenerate conic** is one which the corresponding matrix is degenerate. Geometrically, it is two lines (possibly overlaping)

---

**Theorem (5 Points Determine a Conic).**  
Let $\mathrm{char}(k) \ne 2$. Given five distinct points in $\mathbb{P}^2(k)$, no four of which lie on a line, there exists a unique conic passing through all five points.

> **Proof.**  
> TODO

**Theorem (Projective Equivalence of Conics).**  
Assuming $\mathrm{char}(k) \ne 2$. Any two smooth conics in $\mathbb{P}^2(k)$ are projectively equivalent. That is, there exists a projective transformation $T \in \mathrm{PGL}_3(k)$ mapping one conic onto the other. 

In particular, every smooth conic is projectively equivalent to the standard conic $ x^2 + y^2 + z^2 = 0 $.

> **Proof.**  
> TODO