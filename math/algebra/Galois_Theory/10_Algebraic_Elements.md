---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Algebraic_Elements
---
## Algebraic Elements

**Definition.**  
Let $F$ be a field, and suppose $F \subset E$ for some field $E$. We say that $E$ is a **field extension** of $F$, denoted $E/F$.

For an element $\alpha \in E$, we define:
- $F[\alpha]$ as the smallest **subring** of $E$ containing both $F$ and $\alpha$.
- $F(\alpha)$ as the smallest **subfield** of $E$ containing both $F$ and $\alpha$.

More generally, for $\alpha_1, \ldots, \alpha_n \in E$, we define $F(\alpha_1, \ldots, \alpha_n)$ to be the smallest subfield of $E$ containing $F$ and all the $\alpha_i$.

---

**Lemma (Explicit Description of $F[\alpha]$ and $F(\alpha)$).**  
Let $E/F$ be a field extension and $\alpha \in E$.

- The image of the evaluation map $\phi_\alpha : F[x] \to E$ is exactly $F[\alpha]$. That is:

  $$ F[\alpha] = \{ p(\alpha) : p(x) \in F[x] \} = \left\{ \sum_{i=0}^k c_i \alpha^i : c_i \in F,\ k \in \mathbb{Z}_{\geq 0} \right\} $$

- Similarly, $F(\alpha)$ is the image of the evaluation map $\phi_\alpha : F(x) \to E$, and:

  $$ F(\alpha) = \left\{ \frac{p(\alpha)}{q(\alpha)} : p(x), q(x) \in F[x],\ q(\alpha) \ne 0 \right\} $$

---

**Lemma.**  
Let $E/F$ be a field extension. Then:
1. $F[\alpha_1, \ldots, \alpha_n] \subset F(\alpha_1, \ldots, \alpha_n)$  
2. $(F(\alpha))(\beta) = F(\alpha, \beta)$  
3. The definition of $F[\alpha]$ also applies when $E$ and $F$ are (commutative) rings. In that case:

   $$ F[\alpha][\beta] = F[\alpha, \beta] $$

---

**Definition.**  
Let $E/F$ be a field extension. An element $\alpha \in E$ is said to be **algebraic** over $F$ if it satisfies a nonzero polynomial $p(x) \in F[x]$. Otherwise, we say that $\alpha$ is **transcendental** over $F$.

---

**Theorem (Characterization of Algebraic Elements).**  
Let $E/F$ be a field extension, and let $\alpha \in E$ be algebraic over $F$. Then:

1. There exists a unique **monic** polynomial $m_{\alpha, F}(x) \in F[x]$ such that:

   $$ \ker(\phi_\alpha) = (m_{\alpha, F}(x)) $$

   where $\phi_\alpha : F[x] \to E$ is the evaluation map $f(x) \mapsto f(\alpha)$.

2. $m_{\alpha, F}(x)$ is irreducible in $F[x]$.

3. $F[\alpha]$ is a field, and there is an isomorphism:

   $$ F[\alpha] \simeq F[x]/(m_{\alpha, F}(x)) $$

4. The field $F[\alpha]$ has the form:

   $$ F[\alpha] = \left\{ \sum_{i=0}^{d-1} c_i \alpha^i : c_i \in F \right\} $$

   where $d = \deg m_{\alpha, F}(x)$.

We call $m_{\alpha, F}(x)$ the **minimal polynomial** of $\alpha$ over $F$. Moreover, if $p(x) \in F[x]$ is any other irreducible polynomial such that $p(\alpha) = 0$, then:

$$ p(x) = c \cdot m_{\alpha, F}(x) $$

for some $c \in F^\times$.

---

**Corollary.**  
Let $E/F$ be a field extension and $\alpha_1, \ldots, \alpha_n \in E$. Then:

$$ F[\alpha_1, \ldots, \alpha_n] = F(\alpha_1, \ldots, \alpha_n) $$

if and only if each $\alpha_i$ is algebraic over $F$.

> **Proof.**  
> If each $\alpha_i$ is algebraic over $F$, then we can inductively show that $F[\alpha_1, \ldots, \alpha_n]$ is a field. Hence it must equal $F(\alpha_1, \ldots, \alpha_n)$.  
>
> Conversely, if $F[\alpha_1, \ldots, \alpha_n]$ is already a field, then by [Zariski's Lemma](https://en.m.wikipedia.org/wiki/Zariski%27s_lemma), it is a finitely generated $F$-algebra that is also a field. Therefore, each $\alpha_i$ must be algebraic over $F$.

