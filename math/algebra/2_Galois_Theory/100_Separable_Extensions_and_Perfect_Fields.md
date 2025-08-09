---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Separable_Extensions_and_Perfect_Fields
comment: true
---
## Separable Extensions and Perfect Fields

**Definition.**  
1. Let $F$ be a field and $\alpha \in \overline{F}$. We say that $\alpha$ is **separable over $F$** if its minimal polynomial $m_{\alpha, F}(x)$ is separable.  
2. Let $E/F$ be an algebraic extension. We say that $E/F$ is a **separable extension** if every $\alpha \in E$ is separable over $F$.

---

**Theorem (Towers of separable extensions).**  
Let $F \subset E \subset K$ be a tower of algebraic extensions. Then $K/F$ is separable if and only if both $E/F$ and $K/E$ are separable.

> **Proof.**  
> Suppose $K/F$ is separable. Then every $\alpha \in E \subset K$ is separable over $F$, so $E/F$ is separable.
> For any $\alpha \in K$, the minimal polynomial $m_{\alpha, E}(x)$ divides $m_{\alpha, F}(x)$ in $E[x]$.
> Since $m_{\alpha, F}(x)$ is separable by assumption, so is $m_{\alpha, E}(x)$. Thus, $K/E$ is separable.  
> 
> The converse direction will be proven after we define the separable closure.

---

**Definition/Lemma (Perfect fields).**  
A field $F$ is called **perfect** if it satisfies any (and hence all) of the following equivalent conditions:
1. The algebraic closure $\overline{F}/F$ is a separable extension.
2. Every algebraic extension $E/F$ is separable.
3. Every polynomial $p(x) \in F[x]$ is separable.

> **Proof.**  
> $1 \Rightarrow 2$: Follows directly from the tower theorem above.  
> $2 \Rightarrow 3$: Let $p(x) \in F[x]$ be a polynomial, and let $p_i(x)$ be an irreducible factor of $p(x)$.
> Let $\alpha \in \overline{F}$ be a root of $p_i(x)$. Then $F(\alpha)/F$ is algebraic and hence separable.
> So $m_{\alpha, F}(x)$ is separable, and since $p_i(x)$ is irreducible, $p_i(x)$ is a scalar multiple of $m_{\alpha, F}(x)$ and thus also separable.
> Therefore, all irreducible factors of $p(x)$ are separable, so $p(x)$ is separable.  
> $3 \Rightarrow 1$: Let $\alpha \in \overline{F}$. Then $m_{\alpha, F}(x)$ is separable by assumption, so $\alpha$ is separable over $F$. 
> Hence, $\overline{F}/F$ is separable.

---

**Theorem (Characterization of perfect fields).**  
A field $F$ is perfect if and only if one of the following holds:
1. $\operatorname{char} F = 0$;
2. $\operatorname{char} F = p > 0$ and $F^p = F$, where $F^p := \{ a^p : a \in F \}$.

> **Proof.**  
> In characteristic zero, all polynomials are separable (see [Separable Polynomials](./90_Separable_Polynomials.md)), so $F$ is perfect.  
> 
> Suppose $\operatorname{char} F = p > 0$ and $F^p = F$. Then every $a \in F$ is a $p$-th power: $a = b^p$.
> By induction, for all $k \geq 0$, we have $a = c^{p^k}$ for some $c \in F$.
> 
> Let $f(x) \in F[x]$ be irreducible. By an earlier corollary, there exists an irreducible separable $g(x) \in F[x]$ and $k \geq 0$ such that  
> 
> $$f(x) = g\left(x^{p^k}\right).$$  
> 
> Since $F^p = F$, each coefficient $c_i$ of $f(x)$ satisfies $c_i = d_i^{p^k}$ for some $d_i \in F$, and we have:  
> 
> $$\begin{align*}
    f(x) &= c_0 + c_1 x^{p^k} + \cdots + c_n x^{n p^k} \\
    &= (d_0 + d_1 x + \cdots + d_n x^n)^{p^k}
    \end{align*}$$
> 
> Since $f(x)$ is irreducible, we must have $p^k = 1$, so $f(x) = g(x)$ is separable. Hence, $F$ is perfect.  
> 
> Conversely, if $F^p \ne F$, then there exists $a \in F \setminus F^p$. Let $\alpha \in \overline{F}$ satisfy $\alpha^p = a$.
> Then $m_{\alpha, F}(x) \mid x^p - a = (x - \alpha)^p$, and since $\alpha \notin F$, we have $\deg m_{\alpha, F}(x) > 1$,
> so $m_{\alpha, F}(x)$ has repeated roots. Hence, $\alpha$ is not separable over $F$, and $F$ is not perfect.

---

**Corollary (Finite fields are perfect).**  
Every finite field is perfect.

> **Proof.**  
> The Frobenius map $\sigma_p : \mathbb{F}_q \to \mathbb{F}_q$ given by $x \mapsto x^p$ is bijective (since the field is finite). 
> Therefore, $\mathbb{F}_q^p = \mathbb{F}_q$, and $\mathbb{F}_q$ is perfect by the theorem above.

---

**Definition/Lemma (Separable closure).**  
Let $E/F$ be an algebraic extension. The **separable closure** of $F$ in $E$ is defined as  

$$S = \{ \alpha \in E : \alpha \text{ is separable over } F \}.$$

Then $S$ is a subfield of $E$, and $S/F$ is a separable extension.

Given a fixed algebraic closure $\overline{F}$, we define the **separable closure of $F$** as  

$$F^{\text{sep}} = \{ \alpha \in \overline{F} : \alpha \text{ is separable over } F \}.$$

Then $F^{\text{sep}}/F$ is separable, and the separable closure of $F$ in $E$ is $F^{\text{sep}} \cap E$.

> **Proof.**  
> Let $\alpha, \beta \in E$ be separable over $F$. Then their minimal polynomials $m_{\alpha, F}(x)$ and $m_{\beta, F}(x)$ are separable.
> The splitting field of their product is a Galois extension (We will prove this later in the characterization of finite Galois extension), 
> hence normal and separable. Therefore, $\alpha \pm \beta$, $\alpha \beta^{\pm 1}$ are also separable over $F$.
> Thus, $S$ is a subfield of $E$.

---

**Lemma.**  
Let $F$ be a field of characteristic $p > 0$, and let $E/F$ be an algebraic extension. For any $\alpha \in E$, there exists $k \ge 0$ such that $\alpha^{p^k}$ is separable over $F$.

> **Proof.**  
> Let $m_{\alpha, F}(x)$ be the minimal polynomial of $\alpha$. By [Separable Polynomials](./90_Separable_Polynomials.md), there exists an irreducible separable $g(x) \in F[x]$ and $k \ge 0$ such that  
> 
> $$m_{\alpha, F}(x) = g(x^{p^k}).$$  
> 
> Then $g(x)$ is the minimal polynomial of $\alpha^{p^k}$, which is separable. Thus, $\alpha^{p^k}$ is separable over $F$.

---

Now, we complete the proof of the tower theorem:

**Theorem (Tower of separable extensions, part 2).**  
Let $F \subset E \subset K$ be a tower of algebraic extensions, with $E/F$ and $K/E$ both separable. Then $K/F$ is separable.

> **Proof.**  
> If $\operatorname{char} F = 0$, then all algebraic extensions are separable, and there's nothing to prove.
> Assume $\operatorname{char} F = p > 0$. Let $S$ be the separable closure of $F$ in $K$. Since $E/F$ is separable, $E \subset S$.
> 
> Let $\alpha \in K$. By the lemma above, there exists $k \ge 0$ such that $\alpha^{p^k} \in S$. Assume $k$ is minimal with this property.
> Then,
> 
> $$m_{\alpha, S}(x) \mid x^{p^k} - \alpha^{p^k} = (x - \alpha)^{p^k}.$$
> 
> Since $k$ is minimal, $m_{\alpha, S}(x) = (x - \alpha)^{p^k}$.  
> 
> But $E \subset S$, so $m_{\alpha, S}(x) \mid m_{\alpha, E}(x)$. Since $K/E$ is separable, $m_{\alpha, E}(x)$ must be separable.
> This forces $p^k = 1$, or else $m_{\alpha, E}(x)$ will have repeated roots. Therefore, we have $\alpha \in S$. We conclude that every $\alpha \in K$ is separable over $F$, and $K/F$ is separable.
