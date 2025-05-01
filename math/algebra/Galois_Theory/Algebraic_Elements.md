---
menubar: algebra
permalink: /math/algebra/Galois_Theory/Algebraic_Elements
---
## Algebraic Element
**Definition**  
Let $F$ be a field, and suppose $F\subset E$ for some field $E$. Then we say $E$ is a **field extension** over $F$, denoted as $E/F$. For $\alpha\in E$, we denote $F[\alpha]$ to be the smallest ring in $E$ containing $F$ and $\alpha$, and $F(\alpha)$ to be the smallest field in $E$ containing $F$ and $\alpha$. Similarly, we define $F(\alpha_1,\ldots, \alpha_n)$ to be the smallest field in $E$ containing both $F$ and $\alpha_i$.

**Lemma**
1. $F[\alpha_1,\ldots, \alpha_n]\subset F(\alpha_1,\ldots, \alpha_n)$
2.  $(F(\alpha))(\beta) = F(\alpha, \beta)$
3.  The definition for $F[\alpha]$ also works if $E, F$ are rings. Then we also have $F[\alpha][\beta] = F[\alpha, \beta]$

**Definition**

Let $E/F$ be a field extension. We say $\alpha\in E$ is **algebraic** over $F$ if $\alpha$ satisfies a non-constant polynomial $p(x)\in F[x]$. Else, we say that $\alpha$ is **transcendental** over $F$.

**Theorem (Characterization of algebraic elements)**
Let $E/F$ be a field extension, and $\alpha\in E$ be algebraic, then
1. There is a unique monic polynomial $m_{\alpha, F}(x)\in F[x]$ such that $\ker \phi_\alpha = (m_{\alpha, F}(x))$ where $\phi_\alpha: F[x]\mapsto E$ is the evaluation map at $\alpha$.
2. $m_{\alpha, F}(x)$ is irreducible
3. $F[\alpha]$ is a field, and $F[\alpha]\simeq F[x]/(m_{\alpha, F}(x))$
4. $F[\alpha] = \{\sum_0^{d-1} c_i\alpha^i:c_i\in F\}$  where $d = \deg m_{\alpha, F}(x)$

We call such $m_{\alpha, F}(x)$ as **minimal polynomial** of $\alpha$ over $F$. Note that if $p(x)\in F[x]$ is another irreducible polynomial such that $p(\alpha) = 0$, then we have $p(x)=cm_{\alpha, F}(x)$ for some $c\in F\setminus\{0\}$.

**Corollary**
Let $E/F$ be a field extension, and $\alpha_1,\ldots, \alpha_n\in E$. Then $F[\alpha_1,\ldots,\alpha_n] = F(\alpha_1,\ldots, \alpha_n)$ if and only if $\alpha_i$ are all algebraic over $F$ (The forward direction is non-trivial).
**Proof**
If $\alpha_i$ are all algebraic, then we can prove by induction that $F[\alpha_1,\ldots, \alpha_n]$ is a field, and hence $F[\alpha_1,\ldots, \alpha_n] = F(\alpha_1,\ldots, \alpha_n)$. Conversely, by [Zariski Lemma](https://en.m.wikipedia.org/wiki/Zariski%27s_lemma), if $F[\alpha_1,\ldots,\alpha_n]$ is a field, then it must be a finite extension over $F$, and hence every $\alpha_i$ is algebraic over $F$.