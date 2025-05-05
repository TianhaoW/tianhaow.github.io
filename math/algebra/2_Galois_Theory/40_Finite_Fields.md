---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Finite_Fields
---
## Finite Fields

**Theorem (Existence and Uniqueness of Finite Fields).**  
Every finite field has order $p^n$ for some prime $p$ and positive integer $n$.  
Conversely, for any such $p$ and $n$:

- There exists a finite field of order $p^n$.
- Any two finite fields of order $p^n$ are isomorphic. 
- Inside a fixed algebraic closure $\overline{\mathbb{F}_p}$, there is a **unique subfield** of order $p^n$.

> **Proof (Sketch).**  
> Let $\mathbb{F}$ be a finite field. Then $\mathbb{F}$ has positive characteristic $p$ for some prime $p$. The prime field $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ embeds into $\mathbb{F}$, so we can view $\mathbb{F}$ as an $\mathbb{F}_p$-vector space. Let $n = [\mathbb{F} : \mathbb{F}_p]$. Then:
>
> $$ |\mathbb{F}| = p^n $$
>
> **Existence:**  
> To construct a field of order $p^n$, fix an algebraic closure $\overline{\mathbb{F}_p}$ and define:
>
> $$ \mathbb{F}_{p^n} := \left\{ \alpha \in \overline{\mathbb{F}_p} : \alpha^{p^n} = \alpha \right\} $$
>
> This set forms a subfield with $p^n$ elements.
>
> **Uniqueness:**  
> Suppose $\mathbb{F}$ is a field with $|\mathbb{F}| = p^n$. Then:
>
> - $\mathbb{F}^\times$ is a cyclic group of order $p^n - 1$.
> - Every element satisfies $\alpha^{p^n} = \alpha$, so:
>
> $$ \mathbb{F} \subseteq \left\{ \alpha \in \overline{\mathbb{F}_p} : \alpha^{p^n} = \alpha \right\} = \mathbb{F}_{p^n} $$
>
> Since both have $p^n$ elements, equality holds. Thus, the subfield of $\overline{\mathbb{F}_p}$ defined above is the **unique** field of order $p^n$ inside it.

---

**Lemma.**  
$\mathbb{F}_{p^m}$ can be embedded into $\mathbb{F}\_{p^n}$ if and only if $m \mid n$.

> **Proof.**  
> Suppose $\mathbb{F}_{p^m} \subset \mathbb{F}\_{p^n}$. Then we have a tower of field extensions:
>
> $$ \mathbb{F}_p \subset \mathbb{F}_{p^m} \subset \mathbb{F}_{p^n} $$
>
> By the tower law:
>
> $$ [\mathbb{F}_{p^n} : \mathbb{F}_p] = [\mathbb{F}_{p^n} : \mathbb{F}_{p^m}] \cdot [\mathbb{F}_{p^m} : \mathbb{F}_p] $$
>
> Since $[\mathbb{F}\_{p^n} : \mathbb{F}_p] = n$ and $[\mathbb{F}\_{p^m} : \mathbb{F}\_p] = m$, this shows $m \mid n$.
>
> Conversely, assume $m \mid n$ and write $n = mk$. We want to show that $\mathbb{F}\_{p^m} \subset \mathbb{F}\_{p^n}$ as subfields of $\overline{\mathbb{F}_p}$.
>
> Recall that:
>
> $$ \mathbb{F}_{p^m} = \{ \alpha \in \overline{\mathbb{F}_p} : \alpha^{p^m} = \alpha \}, \quad \mathbb{F}_{p^n} = \{ \alpha \in \overline{\mathbb{F}_p} : \alpha^{p^n} = \alpha \} $$
>
> We can show that 
>
> $$x^{p^n}-x = x^{p^{mk}}-x = (x^{p^m}-x)(x^{p^{m(k-1)}}+x^{p^{m(k-2)}}+\cdots+1)$$
> 
> Therefore, $\alpha^{p^m} = \alpha$ implies $\alpha^{p^n} = \alpha$. This shows that $\mathbb{F}\_{p^m}\subset\mathbb{F}\_{p^n}$.

---

**Lemma (Irreducible Polynomials over Finite Field).**  
Let $f(x) \in \mathbb{F}_p[x]$ be irreducible of degree $d$. Then:

1.  
   $$ f(x) \mid x^{p^d} - x $$
2.  
   $$ f(x) \mid x^{p^n} - x \quad \text{if and only if} \quad d \mid n $$

> **Proof.**  
> Let $\alpha$ be a root of $f(x)$ in some algebraic closure $\overline{\mathbb{F}_p}$. Since $f(x)$ is irreducible over $\mathbb{F}_p$ and has degree $d$, 
> $f(x)$ is a scalar multiple of the minimal polynomial of $\alpha$ over $\mathbb{F}_p$, 
> and the field $\mathbb{F}_p(\alpha)$ is a degree $d$ extension of $\mathbb{F}_p$.
>
> Hence:
>
> $$ \mathbb{F}_p(\alpha) = \mathbb{F}_{p^d} \quad \implies \quad \alpha^{p^d} = \alpha $$
>
> So $\alpha$ is a root of $x^{p^d} - x$. By the property of the minimal polynomial, we have $f(x)$ divides $x^{p^d} - x$.
>
> Now for the second part:
>
> If $f(x) \mid x^{p^n} - x$, then $\alpha \in \mathbb{F}\_{p^n}$. We have a tower of extension $\mathbb{F}\_p\subset\mathbb{F}\_p(\alpha)\subset\mathbb{F}\_{p^n}$, so $d = [\mathbb{F}\_p(\alpha) : \mathbb{F}\_p] \mid n$.
> 
> If $d \mid n$, then $\mathbb{F}\_{p^d} \subset \mathbb{F}\_{p^n}$ by the previous lemma. Thus, we have $\alpha\in\mathbb{F}\_{p^n}$ with $\alpha$ satisfying $x^{p^n}-x$. Since $f(x)$ is a scalar 
> multiple of the minimal polynomial of $\alpha$, we have $f(x)\mid x^{p^n}-x$ by the property of the minimal polynomial.

---

**Theorem (Counting Monic Irreducible Polynomials over Finite Fields).**  
Let $\mathcal{P}_d$ be the set of monic irreducible polynomials of degree $d$ in $\mathbb{F}_p[x]$. Then:

$$
\prod_{d \mid n} \prod_{f \in \mathcal{P}_d} f(x) = x^{p^n} - x
$$

As a consequence:

$$
p^n = \sum_{d \mid n} d \cdot |\mathcal{P}_d|.
$$

Applying **Möbius inversion**, we get:

$$
|\mathcal{P}_n| = \frac{1}{n} \sum_{d \mid n} \mu(n/d) p^d.
$$

where $\mu$ is the **Möbius function**

> **Proof.**  
> The polynomial $x^{p^n} - x$ splits completely over $\mathbb{F}_{p^n}$ as 
>
> $$ x^{p^n} - x = \prod_{\alpha \in \mathbb{F}_{p^n}} (x - \alpha) $$
>
> and is square-free. Hence it factors into distinct irreducible polynomials over $\mathbb{F}_p$.
>
> Let $f(x) \in \mathbb{F}_p[x]$ be an irreducible factor of $x^{p^n} - x$. Then the previous lemma implies that $\deg f(x) \mid n$.
>
> Conversely, by the previous lemma, every monic irreducible polynomial $f(x)$ of degree $d$ with $d \mid n$ divides $x^{p^n} - x$. Hence:
>
> $$ x^{p^n} - x = \prod_{d \mid n} \prod_{f \in \mathcal{P}_d} f(x) $$
>
> where each irreducible factor $f(x)$ appears exactly once. Taking degrees on both sides:
>
> $$ \deg(x^{p^n} - x) = p^n = \sum_{d \mid n} d \cdot |\mathcal{P}_d| $$
>
> Applying Möbius inversion to this identity yields the formula:
>
> $$ |\mathcal{P}_n| = \frac{1}{n} \sum_{d \mid n} \mu(n/d) p^d $$

