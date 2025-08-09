---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Algebraic_Elements
comment: true
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

> **Proof (Sketch).**  
> It is clear that  
> 
> $$ \{ p(\alpha) : p(x) \in F[x] \} \subset F[\alpha] $$  
> 
> since $F[\alpha]$ contains $\alpha$, and is closed under addition and multiplication. Conversely, the set on the left is a subring of $E$ containing both $F$ and $\alpha$. Since $F[\alpha]$ is the smallest such ring, we must have:
> 
> $$ F[\alpha] \subset \{ p(\alpha) : p(x) \in F[x] \}. $$
> 
> The proof for $F(\alpha)$ is entirely analogous.

---

**Lemma.**  
Let $E/F$ be a field extension. Then:
1. $F[\alpha_1, \ldots, \alpha_n] \subset F(\alpha_1, \ldots, \alpha_n)$  
2. $(F(\alpha))(\beta) = F(\alpha, \beta)$  
3. The definition of $F[\alpha]$ also applies when $E$ and $F$ are (commutative) rings. In that case:

   $$ F[\alpha][\beta] = F[\alpha, \beta] $$

> **Proof (Sketch).**  
> 1. The field $F(\alpha_1, \ldots, \alpha_n)$ is also a ring containing both $F$ and the $\alpha_i$, so by minimality of $F[\alpha_1,\ldots, \alpha_n]$:
>
> $$ F[\alpha_1, \ldots, \alpha_n] \subset F(\alpha_1, \ldots, \alpha_n). $$
>
> 2. $F(\alpha)(\beta)$ is a field containing $F$, $\alpha$, and $\beta$, so it contains $F(\alpha, \beta)$. Conversely, $F(\alpha, \beta)$ contains both $F(\alpha)$ and $\beta$, so:
>
> $$ F(\alpha)(\beta) = F(\alpha, \beta). $$
>
> 3. The same reasoning as in (2) applies when $F$ and $E$ are rings.

---

**Definition.**  
Let $E/F$ be a field extension. An element $\alpha \in E$ is said to be **algebraic** over $F$ if it satisfies a nonzero polynomial $p(x) \in F[x]$. Otherwise, $\alpha$ is said to be **transcendental** over $F$.

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

We call $m_{\alpha, F}(x)$ the **minimal polynomial** of $\alpha$ over $F$. Moreover, if $p(x) \in F[x]$ is another irreducible polynomial such that $p(\alpha) = 0$, then:

$$ p(x) = c \cdot m_{\alpha, F}(x) $$

for some $c \in F^\times$.

> **Proof (Sketch).**  
> Consider the evaluation homomorphism:
>
> $$ \phi_\alpha : F[x] \to E $$
>
> The image of $\phi_\alpha$ is $F[\alpha]$. Since $\alpha$ is algebraic over $F$, the kernel of $\phi_\alpha$ is nontrivial. Because $F[x]$ is a principal ideal domain, there is a unique monic polynomial $m_{\alpha, F}(x)$ such that:
>
> $$ \ker(\phi_\alpha) = (m_{\alpha, F}(x)) $$
>
> By the First Isomorphism Theorem, we get:
>
> $$ F[x]/(m_{\alpha, F}(x)) \simeq F[\alpha] $$
>
> via $x + (m_{\alpha, F}(x)) \mapsto \alpha$.
>
> To see that $F[\alpha]$ is a field, it suffices to show that $m_{\alpha, F}(x)$ is irreducible. Suppose not. Then:
>
> $$ m_{\alpha, F}(x) = p(x) q(x) $$
>
> for nonconstant $p(x), q(x) \in F[x]$. Since $m_{\alpha, F}(\alpha) = 0$, either $p(\alpha) = 0$ or $q(\alpha) = 0$. Without loss of generality, assume $p(\alpha) = 0$. Then:
>
> $$ p(x) \in \ker(\phi_\alpha) = (m_{\alpha, F}(x)) $$
>
> so $p(x)$ divides $m_{\alpha, F}(x)$. But this contradicts the factorization $m_{\alpha, F}(x) = p(x) q(x)$ unless $q(x)$ is a constant polynomial. Therefore, $m_{\alpha, F}(x)$ must be irreducible.

---

**Corollary.**  
Let $E/F$ be a field extension and $\alpha_1, \ldots, \alpha_n \in E$. Then:

$$ F[\alpha_1, \ldots, \alpha_n] = F(\alpha_1, \ldots, \alpha_n) $$

if and only if each $\alpha_i$ is algebraic over $F$.

> **Proof.**  
> If each $\alpha_i$ is algebraic over $F$, then we can inductively show that $F[\alpha_1, \ldots, \alpha_n]$ is a field. Hence:
>
> $$ F[\alpha_1, \ldots, \alpha_n] = F(\alpha_1, \ldots, \alpha_n). $$
>
> Conversely, if $F[\alpha_1, \ldots, \alpha_n]$ is a field, then by [Zariski’s Lemma](https://en.m.wikipedia.org/wiki/Zariski%27s_lemma), it must be a finite extension of $F$. Hence, each $\alpha_i$ is algebraic over $F$.

---

**Lemma.**  
Let $F$ be a field, and let $p(x) \in F[x]$ be a non-constant polynomial. Then there exists a field extension $E/F$ in which $p(x)$ has a root.

> **Proof.**  
> Let $m(x)$ be an irreducible factor of $p(x)$ in $F[x]$. Consider the quotient ring:
>
> $$ E = F[x]/(m(x)) $$
>
> Since $m(x)$ is irreducible, this quotient is a field, and $E$ is a field extension of $F$. The element:
>
> $$ \alpha = x + (m(x)) \in E $$
>
> satisfies $m(\alpha) = 0$, and hence is also a root of $p(x)$.

{% include notification.html 
status="is-info is-light"
icon="false"
message="

**Remark.**  
The significance of this lemma is that **every non-constant polynomial in $F[x]$ has a root in some field extension of $F$**.  
Even if we don't know the explicit form of the root or the extension, we can still reason about roots confidently and rigorously.  
This allows us to speak about 'a root of $p(x)$' without worrying whether it lives in $F$ — it always exists *somewhere*.
" %}