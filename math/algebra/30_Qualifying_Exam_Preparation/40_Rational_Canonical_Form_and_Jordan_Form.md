---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Rational_Canonical_Form_and_Jordan_Form
comment: true
---
## Rational Canonical Form and Jordan Form

### Key Definitions

**Definition / Lemma.**  
Let $k$ be a field and $A \in M_n(k)$. We may view $k^n$ as a $k[x]$–module by defining

$$f(x) \cdot v := f(A)\, v.$$

We denote this module by $V_A$. Then:

1. $V_A \cong V_B$ as $k[x]$–modules if and only if $A$ and $B$ are similar matrices.  
2. If $A \in M_n(k)$, $B \in M_m(k)$, and we define the block diagonal matrix
   
    $$A \oplus B = \begin{bmatrix} A & 0 \\ 0 & B \end{bmatrix},$$

    then $V_{A \oplus B} \cong V_A \oplus V_B$.

> **Proof (Sketch).**  
> A $k[x]$–module isomorphism $\theta : V_A \to V_B$ is also a $k$–linear isomorphism satisfying
> 
> $$\theta(x \cdot v) = x \cdot \theta(v), \quad \text{i.e. } \theta(Av) = B\theta(v).$$
> 
> Writing $\theta$ as a matrix $P \in \mathrm{GL}_n(k)$ gives $PA = BP$, hence $B = P A P^{-1}$.

---

**Definition / Lemma (Invariant Factors).**  
Let $A \in M_n(k)$, and let $V_A$ be the corresponding $k[x]$–module. Then $V_A$ decomposes as

$$V_A \cong k[x]/\langle f_1 \rangle \;\oplus \cdots \oplus\; k[x]/\langle f_m \rangle,$$

where $f_1, \ldots, f_m$ are unique monic non-constant polynomials with

$$f_1 \mid f_2 \mid \cdots \mid f_m.$$

- The $f_i$ are called the **invariant factors** of $A$.  
- The last one, $f_m$, is the **minimal polynomial** of $A$. It is the minimal in the sense that if $p(A) = 0$, then $f_m(x) \mid p(x)$.

> **Proof (Sketch).**  
> Consider the ideal
> 
> $$I = \{p(x) \in k[x] : p(A) = 0\}.$$
> 
> Since $k[x]$ is a PID, $I = \langle f(x) \rangle$ for some polynomial $f(x)$.  
> From the decomposition of $V_A$, one checks that $I = \langle f_m(x) \rangle$, hence $f_m$ is the minimal polynomial.

---

**Definition / Lemma (Companion Matrix).**  
Let $f(x) = x^n + c_{n-1}x^{n-1} + \cdots + c_0 \in k[x]$.
The **companion matrix** of $f$ is

$$
C(f) =
\begin{bmatrix}
0 & 0 & \cdots & 0 & -c_0 \\
1 & 0 & \cdots & 0 & -c_1 \\
0 & 1 & \cdots & 0 & -c_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & -c_{n-1}
\end{bmatrix}.
$$

Then $V_{C(f)} \cong k[x]/\langle f \rangle$.

> **Proof (Sketch).**  
> Recall that the $k[x]$–module structure on $k^n$ is uniquely determined once we know how $x$ acts.  
> For $V_A$, this action is defined by $x \cdot v = A v.$
> 
> To construct a matrix $C(f)$ such that $V_{C(f)} \cong k[x]/\langle f \rangle$, we want multiplication by $x$ on $k^n$ (i.e. the action of $C(f)$) to mimic the multiplication by $x$ map on $k[x]/\langle f \rangle$.
> In other words, $C(f)$ must be the matrix representation of the linear map
> 
> $$m_x : k[x]/\langle f \rangle \to k[x]/\langle f \rangle, \quad \bar g(x) \mapsto \overline{x g(x)}.$$
> 
> To compute this matrix, we pick the natural $k$–basis
> $\\{\bar{1}, \bar{x}, \bar{x}^2, \ldots, \bar{x}^{n-1}\\}$
> of $k[x]/\langle f \rangle$.
> Multiplication by $x$ sends these basis elements to
> $\\{\bar{x}, \ \bar{x}^2, \ \ldots, \ \bar{x}^{n-1}, \ \bar{x}^n\\}.$ where
> $\bar x^n \equiv -c_0 - c_1\bar x - \cdots - c_{n-1} \bar x^{n-1}.$ The matrix representation is exactly $C(f)$.
> 
> Therefore, multiplication by $x$ on $k[x]/\langle f \rangle$ has exactly the same matrix form as multiplication by $C(f)$ on $k^n$, and so $V_{C(f)} \cong k[x]/\langle f \rangle$
> as $k[x]$–modules.

---

**Definition / Theorem (Rational Canonical Form).**  
Let $A \in M_n(k)$ with invariant factors $f_1, \ldots, f_m$. Then

$$A \sim C(f_1) \oplus C(f_2) \oplus \cdots \oplus C(f_m).$$

This block diagonal form is called the **rational canonical form** of $A$.

> **Proof (Sketch).**  
> From the invariant factor decomposition,
> 
> $$V_A \cong \bigoplus_{i=1}^m k[x]/\langle f_i \rangle \cong \bigoplus_{i=1}^m V_{C(f_i)} \cong V_{C(f_1) \oplus \cdots \oplus C(f_m)},$$
>
> so $A$ is similar to the block diagonal matrix of companion matrices.

---

**Definition / Theorem (Characteristic Polynomial).**  
For $A \in M_n(k)$, the **characteristic polynomial** is

$$f_A(x) = \det(xI - A).$$

If $f_1, \ldots, f_m$ are the invariant factors of $A$, then:

1. $f_A(x) = \prod_{i=1}^m f_i(x)$.  
2. Every irreducible factor of $f_A(x)$ divides the minimal polynomial $f_m(x)$.  
3. (**Cayley–Hamilton Theorem**) $f_A(A) = 0$.

> **Proof (Sketch).**  
> First show that a companion matrix $C(f)$ has characteristic polynomial $f(x)$.   
> Then, we check that the characteristic polynomial of $A\oplus B$ is $f_A(x)f_B(x)$.
> 
> Part 2 and 3 are direct consequences of 1

---

**Definition / Theorem (Jordan Form).**  
Let $A \in M_n(k)$, and suppose the minimal polynomial splits completely over $k$:

$$f_m(x) = (x - \lambda_1)^{n_{m1}} \cdots (x - \lambda_k)^{n_{mk}}, \quad \lambda_i \in k \text{ distinct}.$$

Then the invariant factors have the form

$$f_i(x) = \prod_{j=1}^k (x - \lambda_j)^{n_{ij}}.$$

By the Chinese Remainder Theorem,

$$k[x]/\langle f_i \rangle \;\cong\; \bigoplus_{j=1}^k k[x]/\langle (x - \lambda_j)^{n_{ij}} \rangle.$$

Hence $V_A$ has the **primary decomposition**:

$$V_A \;\cong\; \bigoplus_{i=1}^m \bigoplus_{j=1}^k k[x]/\langle (x - \lambda_j)^{n_{ij}} \rangle.$$

We define the **Jordan block** of size $n$ for eigenvalue $\lambda$ as

$$
J_n(\lambda) =
\begin{bmatrix}
\lambda & 0 & \cdots & 0 \\
1 & \lambda & \cdots & 0 \\
 & \ddots & \ddots & 0\\
 & & 1 & \lambda
\end{bmatrix}.
$$

Then:

1. $V_{J_n(\lambda)} \cong k[x]/\langle (x - \lambda)^n \rangle$.  
2. $V_A \cong \bigoplus_{i=1}^m \bigoplus_{j=1}^k V_{J_{n_{ij}}(\lambda_j)}$.  
3. $A \sim \bigoplus_{i=1}^m \bigoplus_{j=1}^k J_{n_{ij}}(\lambda_j)$, called the **Jordan canonical form** of $A$. This form is unique up to reordering the blocks.

> **Proof (Sketch).**  
> Consider $k[x]/\langle (x - \lambda)^n \rangle$ with basis $\{1, (x-\lambda), (x-\lambda)^2, \ldots, (x-\lambda)^{n-1}\}$.
> Multiplication by $x$ has matrix representation $J_n(\lambda)$, giving the desired module isomorphism.

