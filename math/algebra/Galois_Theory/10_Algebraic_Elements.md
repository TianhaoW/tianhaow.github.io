---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Algebraic_Elements
---
## Algebraic Elements

**Definition.**  
Let $F$ be a field, and suppose $F \subset E$ for some field $E$. We say $E$ is a **field extension** of $F$, denoted by $E/F$.

For an element $\alpha \in E$, we define:
- $F[\alpha]$ as the smallest **subring** of $E$ containing both $F$ and $\alpha$.
- $F(\alpha)$ as the smallest **subfield** of $E$ containing both $F$ and $\alpha$.

More generally, for $\alpha_1, \ldots, \alpha_n \in E$, we define $F(\alpha_1, \ldots, \alpha_n)$ as the smallest subfield of $E$ containing $F$ and all the $\alpha_i$.

---

**Lemma.**  
Let $E/F$ be a field extension. Then:
1. $F[\alpha_1, \ldots, \alpha_n] \subset F(\alpha_1, \ldots, \alpha_n)$
2. $(F(\alpha))(\beta) = F(\alpha, \beta)$
3. The definition of $F[\alpha]$ also applies when $E$ and $F$ are rings (not necessarily fields). In this case, we still have:  
   $$F[\alpha][\beta] = F[\alpha, \beta]$$

---

**Definition.**  
Let $E/F$ be a field extension. An element $\alpha \in E$ is said to be **algebraic** over $F$ if it satisfies a nonzero polynomial $p(x) \in F[x]$. Otherwise, $\alpha$ is called **transcendental** over $F$.

---

**Theorem (Characterization of Algebraic Elements).**  
Let $E/F$ be a field extension, and let $\alpha \in E$ be algebraic over $F$. Then:
1. There exists a unique **monic** polynomial $m_{\alpha, F}(x) \in F[x]$ such that  
   $$\ker(\phi_\alpha) = (m_{\alpha, F}(x)),$$  
   where $\phi_\alpha : F[x] \to E$ is the evaluation map $f(x) \mapsto f(\alpha)$.
2. $m_{\alpha, F}(x)$ is irreducible in $F[x]$.
3. $F[\alpha]$ is a field, and we have a canonical isomorphism  
   $$F[\alpha] \cong F[x]/(m_{\alpha, F}(x)).$$
4. The field $F[\alpha]$ has the form  
   $$F[\alpha] = \left\{ \sum_{i=0}^{d-1} c_i \alpha^i : c_i \in F \right\},$$  
   where $d = \deg m_{\alpha, F}(x)$.

The polynomial $m_{\alpha, F}(x)$ is called the **minimal polynomial** of $\alpha$ over $F$. Moreover, if $p(x) \in F[x]$ is another irreducible polynomial such that $p(\alpha) = 0$, then  
$$p(x) = c \cdot m_{\alpha, F}(x)$$  
for some $c \in F^\times$.

---

**Corollary.**  
Let $E/F$ be a field extension and let $\alpha_1, \ldots, \alpha_n \in E$. Then  
$$F[\alpha_1, \ldots, \alpha_n] = F(\alpha_1, \ldots, \alpha_n)$$  
if and only if each $\alpha_i$ is algebraic over $F$.

**Proof.**  
If each $\alpha_i$ is algebraic over $F$, we can inductively show that $F[\alpha_1, \ldots, \alpha_n]$ is a field. Hence it equals $F(\alpha_1, \ldots, \alpha_n)$.

Conversely, if $F[\alpha_1, \ldots, \alpha_n]$ is already a field, then by [Zariski's Lemma](https://en.m.wikipedia.org/wiki/Zariski%27s_lemma), the extension is finite, and each $\alpha_i$ must be algebraic over $F$.
