---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Galois_Group_of_Finite_Fields
comment: true
---
## Galois Group of Finite Fields

**Definition/Theorem (Frobenius Automorphism).**  
Let $\mathbb{F}_p$ be a finite field. We define the **Frobenius automorphism**:

$$ \sigma_p : \overline{\mathbb{F}_p} \to \overline{\mathbb{F}_p}, \quad \alpha \mapsto \alpha^p $$

Then $\sigma_p$ is a field automorphism of $\overline{\mathbb{F}_p}$. 

We also define its powers by: $\sigma_p^n(\alpha) = \alpha^{p^n}$, and denote this as $\sigma_{p^n}$. That is, $\sigma_{p^n} := \sigma_p^n$.

> **Proof.**  
> Since $\overline{\mathbb{F}_p}$ has characteristic $p$, the binomial expansion yields:
> 
> $$(\alpha + \beta)^p = \alpha^p + \beta^p $$
> 
> because all intermediate binomial coefficients $\binom{p}{k}$ are divisible by $p$ for $1 \leq k \leq p-1$.
> 
> Thus:
> 
> $$ \sigma_p(\alpha + \beta) = \alpha^p + \beta^p = \sigma_p(\alpha) + \sigma_p(\beta) $$
> 
> and:
> 
> $$ \sigma_p(\alpha \beta) = (\alpha \beta)^p = \alpha^p \beta^p = \sigma_p(\alpha) \sigma_p(\beta) $$
> 
> so $\sigma_p$ is a ring homomorphism.  
> 
> Since $\overline{\mathbb{F}_p}$ is a field, a nonzero element $\alpha$ satisfies $\alpha^p = 0$ only if $\alpha = 0$, so the map is injective. 
> Moreover, as $\overline{\mathbb{F}_p}$ is algebraically closed, the polynomial $x^p - \alpha$ has a root for all $\alpha\in\overline{\mathbb{F}_p}$, so the map is surjective.
> 
> Therefore, $\sigma_p$ is a field automorphism of $\overline{\mathbb{F}_p}$.

---

**Theorem. (Galois Group of Finite Field Extension)**  
Let $\mathbb{F}_{q^n}/\mathbb{F}_q$ be a finite field extension, where $q = p^r$ is a prime power. Then:

$$ \text{Gal}(\mathbb{F}_{q^n} / \mathbb{F}_q) = \langle \sigma_q \rangle \cong \mathbb{Z}/n\mathbb{Z} $$

> **Proof.**  
> As proved in [Separable Extensions](100_Separable_Extensions_and_Perfect_Fields.md), every finite field is perfect. Therefore, the extension $\mathbb{F}_{q^n}/\mathbb{F}_q$ is separable.
> Moreover, $\mathbb{F}\_{q^n}$ is the splitting field of the polynomial $x^{q^n} - x$ over $\mathbb{F}\_q$, 
> so the extension is normal. Hence, $\mathbb{F}\_{q^n}/\mathbb{F}_q$ is Galois.
> 
> Define the Frobenius automorphism $\sigma_q : \alpha \mapsto \alpha^q$. 
> Since this fixes all elements in $\mathbb{F}\_q$, and maps $\mathbb{F}\_{q^n}$ to itself, 
> it is an element of $\text{Gal}(\mathbb{F}\_{q^n}/\mathbb{F}\_q)$.
> 
> To compute the order of $\sigma_q$, note that:
> 
> - Since every element $\alpha$ in $\mathbb{F}\_{q^n}$ satisfies $\alpha^{q^n} = \alpha$, we have 
>     $\sigma_q^n = \text{id}$ on $\mathbb{F}_{q^n}$.
> - Suppose $\sigma\_q^k = \text{id}$ for some $0 < k < n$. 
>     Then for all $\alpha \in \mathbb{F}\_{q^n}$, 
>     $\alpha = \sigma\_q^k(\alpha) = \alpha^{q^k}$. 
>     Hence every element satisfies $\alpha^{q^k} = \alpha$, so $\alpha$ lies in $\mathbb{F}\_{q^k}$. This forces $\mathbb{F}_{q^n} \subset \mathbb{F}\_{q^k}$, which contradicts $k < n$.
> 
> Therefore, the **order** of $\sigma_q$ is exactly $n$.
> 
> Since $\text{Gal}(\mathbb{F}\_{q^n}/\mathbb{F}_q)$ has order $[\mathbb{F}\_{q^n} : \mathbb{F}\_q] = n$, and $\langle \sigma_q \rangle$ is a subgroup of order $n$, 
> it must be the whole Galois group, and we have
> 
> $$ \text{Gal}(\mathbb{F}_{q^n} / \mathbb{F}_q) = \langle \sigma_q \rangle \cong \mathbb{Z}/n\mathbb{Z}.$$