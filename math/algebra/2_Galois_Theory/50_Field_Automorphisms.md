---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Field_Automorphisms
---
## Field Automorphisms

**Definition / Theorem.**  
Let $E/F$ be a field extension. We define:

1.  
   $$ \operatorname{Aut}(E) = \{ \sigma : E \to E \mid \sigma \text{ is a bijective field homomorphism} \} $$

2.  
   $$ \operatorname{Aut}(E/F) = \{ \sigma \in \operatorname{Aut}(E) \mid \sigma(a) = a \text{ for all } a \in F \} $$

Then $\operatorname{Aut}(E)$ is a group under composition, and $\operatorname{Aut}(E/F)$ is a subgroup of $\operatorname{Aut}(E)$.

---

**Definition.**  
Let $F$ be a field, and let $\alpha, \beta \in \overline{F}$. We say that $\alpha$ and $\beta$ are **conjugate over $F$** if they satisfy the same minimal polynomial over $F$. That is:

$$ m_{\alpha, F}(x) = m_{\beta, F}(x) $$

An algebraic element $\alpha$ over $F$ has exactly $\deg(\alpha, F)$ conjugates in $\overline{F}$ *counted with multiplicity*, corresponding to the roots of its minimal polynomial over $F$.

---

**Theorem.**  
Let $E/F$ be a field extension, and let $\sigma \in \operatorname{Aut}(E/F)$. If $\alpha \in E$ is algebraic over $F$ and satisfies a polynomial $p(x) \in F[x]$, then $\sigma(\alpha)$ is also a root of $p(x)$.

> **Proof.**  
> Write  
> 
> $$ p(x) = c_0 + c_1 x + \cdots + c_n x^n $$  
> 
> with $c_i \in F$, and suppose $p(\alpha) = 0$. Since $\sigma$ is a homomorphism and fixes each $c_i \in F$, we get
> 
> $$ \sigma(p(\alpha)) = \sigma(c_0 + c_1 \alpha + \cdots + c_n \alpha^n) = c_0 + c_1 \sigma(\alpha) + \cdots + c_n \sigma(\alpha)^n = p(\sigma(\alpha)). $$
> 
> Therefore, we have $p(\sigma(\alpha)) = \sigma(p(\alpha)) = \sigma(0) = 0$, and $\sigma(\alpha)$ is a root to $p(x)$.

---

**Corollary.**  
Let $E/F$ be a field extension, and let $\sigma \in \operatorname{Aut}(E/F)$. If $\alpha \in E$ is algebraic over $F$, then $\sigma(\alpha)$ is conjugate to $\alpha$ over $F$.

> **Proof.**  
> Let $m_{\alpha, F}(x)$ be the minimal polynomial of $\alpha$ over $F$. By the previous theorem, $\sigma(\alpha)$ is a root of this polynomial. Since $m_{\alpha, F}(x)$ is monic and irreducible, it must also be the minimal polynomial of $\sigma(\alpha)$. Hence, $\alpha$ and $\sigma(\alpha)$ are conjugate over $F$.

---

**Corollary.**  
Let $F$ be a field, and let $\alpha \in \overline{F}$ be an element of degree $d$ over $F$. Then:

$$ |\operatorname{Aut}(F(\alpha)/F)| \leq [F(\alpha):F] = d $$

> **Proof.**  
> Each $\sigma \in \operatorname{Aut}(F(\alpha)/F)$ is uniquely determined by the image of $\alpha$, and by the previous corollary, $\sigma(\alpha)$ must be a conjugate of $\alpha$ in $F(\alpha)$. Since $\alpha$ has at most  
> 
> $$ d = \deg(\alpha, F) $$
> 
> conjugates in $F(\alpha)$, there are at most $d$ such automorphisms.

---

**Lemma.**  
Let $F$ be a field, and let $\alpha, \beta \in \overline{F}$ be conjugate over $F$. Then there exists an isomorphism of fields:

$$ \sigma : F(\alpha) \to F(\beta) $$

such that $\sigma(\alpha) = \beta$ and $\sigma(a) = a$ for all $a \in F$.

> **Proof.**  
> Since $\alpha$ and $\beta$ satisfy the same minimal polynomial $p(x) \in F[x]$, we have:
> 
> $$ F(\alpha) \cong F[x]/(p(x)) \cong F(\beta) $$
> 
> where the isomorphisms send $\alpha \mapsto x + (p(x))$ and $x + (p(x)) \mapsto \beta$, respectively. 
> Composing these maps yields a field isomorphism $\sigma : F(\alpha) \to F(\beta)$ with $\sigma(\alpha) = \beta$ and $\sigma|\_F = \text{id}$.

---

**Theorem (Galois Characterization of Conjugates).**  
Let $F$ be a field, and let $\alpha, \beta \in \overline{F}$. Then $\alpha$ and $\beta$ are conjugate over $F$ if and only if there exists $\sigma \in \operatorname{Aut}(\overline{F}/F)$ such that:

$$ \sigma(\alpha) = \beta $$

> **Proof.**
> If such a $\sigma$ exists, then by the previous corollary, $\beta = \sigma(\alpha)$ is a conjugate of $\alpha$ over $F$.
>
> Conversely, suppose $\alpha$ and $\beta$ are conjugate over $F$. Then there exists an isomorphism:
> 
> $$ \sigma : F(\alpha) \to F(\beta) $$
> 
>  with $\sigma(\alpha) = \beta$ and $\sigma\|\_F = \text{id}$. By an extension theorem (to be proven later), such $\sigma$ can be extended to an automorphism:
> 
> $$ \overline{\sigma} \in \operatorname{Aut}(\overline{F}/F) $$
> 
> such that $\overline{\sigma}\|\_{F(\alpha)} = \sigma$. Therefore, $\overline{\sigma}\in \operatorname{Aut}(E/F)$ and $\overline{\sigma}(\alpha) = \beta$.