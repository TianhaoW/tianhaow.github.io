---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Field_Extensions
---
## Field Extensions

**Definition.**  
Let $E/F$ be a field extension. Then $E$ is naturally a vector space over $F$. We define the **degree** of $E$ over $F$ by:

$$ [E : F] = \dim_F E $$

where $\dim_F E$ denotes the dimension of $E$ as an $F$-vector space. We say that $E/F$ is a **finite extension** if $ [E : F] < \infty $.

---

**Definition / Lemma.**  
Let $E/F$ be a field extension, and let $\alpha \in E$ be algebraic over $F$ with minimal polynomial $m_{\alpha, F}(x)$ of degree $d$. We define the **degree** of $\alpha$ over $F$ as $d$. Moreover:
1.  
   $$ F(\alpha) = \left\{ c_0 + c_1 \alpha + \cdots + c_{d-1} \alpha^{d-1} : c_i \in F \right\} $$
2.  
   $$ [F(\alpha) : F] = d $$

> **Proof (Sketch).**  
> Since $\alpha$ is algebraic over $F$, we have $F(\alpha) = F[\alpha] = \{ p(\alpha) : p(x) \in F[x] \}$. In particular:
>
> $$ F(\alpha) \supset \left\{ c_0 + c_1 \alpha + \cdots + c_{d-1} \alpha^{d-1} : c_i \in F \right\} $$
>
> For the reverse inclusion, we use the fact that $\alpha^d$ can be written as a linear combination of lower powers using the minimal polynomial. Inductively, every $\alpha^k$ for $k \geq d$ lies in the $F$-span of $\{1, \alpha, \ldots, \alpha^{d-1}\}$.
>
> To prove the second part, we observe that $\{1, \alpha, \ldots, \alpha^{d-1}\}$ is linearly independent and spans $F(\alpha)$, so it forms an $F$-basis of $F(\alpha)$.

---

**Lemma (Tower Law).**  
Let $F \subset E \subset L$ be fields such that both $E/F$ and $L/E$ are finite extensions. Then $L/F$ is also a finite extension, and:

$$ [L : F] = [L : E] \cdot [E : F] $$

> **Proof (Sketch).**  
> Let $\{e_1, \ldots, e_n\}$ be an $F$-basis of $E$, and let $\{l_1, \ldots, l_m\}$ be an $E$-basis of $L$. Then the set:
>
> $$ \{ e_i l_j : 1 \leq i \leq n,\ 1 \leq j \leq m \} $$
>
> spans $L$ over $F$ and is linearly independent. Hence it forms an $F$-basis of $L$.

---

**Definition.**  
A field extension $E/F$ is called **algebraic** if every element $\alpha \in E$ is algebraic over $F$.

---

**Lemma (Finite Extensions are Algebraic).**  
If $E/F$ is a finite extension, then it is algebraic.

> **Proof (Sketch).**  
> Let $\alpha \in E$, and consider the set $\{1, \alpha, \alpha^2, \ldots\}$. Since $E$ has finite dimension over $F$, this set must be linearly dependent. Then, a nontrivial linear relation of those $\alpha^i$ gives a polynomial in $F[x]$ with $\alpha$ as a root.

---

**Theorem (Transitivity of Algebraic Extensions).**  
Let $F \subset E \subset L$ be field extensions. 
1. Then $L/F$ is algebraic if and only if both $E/F$ and $L/E$ are algebraic.

> **Proof (Sketch).**  
> Suppose both $E/F$ and $L/E$ are algebraic. Pick $\alpha \in L$. Since $L/E$ is algebraic, $\alpha$ satisfies a polynomial:
>
> $$ p(x) = \sum_{i=0}^n e_i x^i,\quad e_i \in E,\quad p(\alpha) = 0 $$
>
> Since $E/F$ is algebraic, each $e_i$ is algebraic over $F$. Then the field $F(e_0, \ldots, e_n)$ is a finite extension of $F$, and $\alpha$ is algebraic over it.
>
> Therefore:
>
> $$ [F(e_0, \ldots, e_n, \alpha) : F] < \infty $$
>
> and $\alpha$ is algebraic over $F$.
>
> Conversely, if $L/F$ is algebraic, then in particular every element of $E \subset L$ is algebraic over $F$, so $E/F$ is algebraic. Also, for $\alpha \in L$, if it satisfies a polynomial in $F[x] \subset E[x]$, then $\alpha$ is algebraic over $E$ as well. So $L/E$ is algebraic.
