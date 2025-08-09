---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Isomorphism_Extension_Theorem
comment: true
---
## Isomorphism Extension Theorem

**Theorem (Isomorphism Extension Theorem).**  
Let $\sigma : F \to F'$ be a field isomorphism. Then there exists an isomorphism

$$ \overline{\sigma} : \overline{F} \to \overline{F'} $$

such that $\overline{\sigma}\|\_F = \sigma$. In other words, every isomorphism between base fields extends to an 
isomorphism between their algebraic closures.

We will prove this theorem at the end of this page. First, we explore several important consequences.

---

**Corollary (Uniqueness of Algebraic Closures).**  
Let $F$ be a field, and let $\overline{F}$ and $\overline{F}'$ be two algebraic closures of $F$. Then there exists an isomorphism

$$ \overline{\sigma} : \overline{F} \to \overline{F}' $$

such that $\overline{\sigma}(a) = a$ for all $a \in F$.

> **Proof.**  
> Apply the isomorphism extension theorem to the identity map $\mathrm{id} : F \to F$.

---

**Corollary (Uniqueness of Splitting Fields).**  
Let $F$ be a field, and let $\mathcal{P} \subset F[x] \setminus F$ be a set of non-constant polynomials. Suppose $E$ and $E'$ are two splitting fields of $\mathcal{P}$ over $F$. Then there exists an isomorphism

$$ \tilde{\sigma} : E \to E' $$

such that $\tilde{\sigma}(a) = a$ for all $a \in F$.

> **Proof (Sketch).**  
> We prove the result for the case where $\mathcal{P}$ is finite. The general case is similar.
>
> Suppose $p(x) = \prod_{f \in \mathcal{P}} f(x) \in F[x]$ is the product of all polynomials in $\mathcal{P}$, so that $E$ and $E'$ are both splitting fields of $p(x)$ over $F$.
>
> Let $\overline{E}$ and $\overline{E'}$ be algebraic closures of $E$ and $E'$ respectively. Since $E$ and $E'$ are algebraic extensions of $F$, both $\overline{E}$ and $\overline{E'}$ are also algebraic closures of $F$.
>
> Let $\alpha_1, \ldots, \alpha_k \in \overline{E}$ be the roots of $p(x)$, so that $E = F(\alpha_1, \ldots, \alpha_k)$. Similarly, let $\alpha_1', \ldots, \alpha_k' \in \overline{E'}$ be the roots of $p(x)$ in $\overline{E'}$, so $E' = F(\alpha_1', \ldots, \alpha_k')$.
>
> By the isomorphism extension theorem, there exists an isomorphism
>
> $$ \overline{\sigma} : \overline{E} \to \overline{E'} $$
>
> such that $\overline{\sigma}\|\_F = \mathrm{id}$. Since $p(x) \in F[x]$, each $\alpha_i$ is mapped to another root 
> of $p(x)$, so $\overline{\sigma}(\alpha_i) \in E'$. Hence, $\overline{\sigma}(E) \subset E'$. By symmetry and invertibility, we must have equality: $\overline{\sigma}(E) = E'$.
>
> The restriction $\tilde{\sigma} := \overline{\sigma}\|\_E$ is the desired isomorphism.

{% include notification.html 
status="is-info is-light"
icon="false"
message="
**Remark.**  
If we fix an algebraic closure $\overline{F}$, then the splitting field of a polynomial $p(x) \in F[x] \setminus F$ is uniquely given by

$$ F(\alpha_1, \ldots, \alpha_k) \subset \overline{F} $$

where $\alpha_i$ are the roots of $p(x)$ in $\overline{F}$. The theorem above shows that even without a fixed $\overline{F}$, the splitting field is still **unique up to isomorphism**.
"%}

---

**Corollary (Uniqueness of Finite Fields).**  
Let $E$ and $E'$ be finite fields of order $p^n$ for some prime $p$ and integer $n$. Then:

$$
E \simeq E'
$$

as fields.

> **Proof (Sketch).**  
> Both $E$ and $E'$ are splitting fields of the polynomial $x^{p^n} - x \in \mathbb{F}_p[x]$ over the base field 
> $\mathbb{F}_p$. By the uniqueness of splitting fields up to isomorphism, we conclude that $E \simeq E'$.

{% include notification.html 
status="is-info is-light"
icon="false"
message="
**Remark.**  
If we fix an algebraic closure $\overline{\mathbb{F}_p}$, then there is a unique subfield of order $p^n$ inside it. This corollary shows that **without reference to a fixed closure**, finite fields of a given order are still unique **up to isomorphism**.
"%}

---

**Corollary (Galois Characterization of Conjugates).**  
Let $F$ be a field, and let $\alpha, \alpha' \in \overline{F}$ be conjugate over $F$. Then there exists an automorphism

$$ \sigma \in \operatorname{Aut}(\overline{F}/F) $$

such that $\sigma(\alpha) = \alpha'$.

> **Proof.**  
> Since $\alpha$ and $\alpha'$ are conjugate over $F$, they share the same irreducible minimal polynomial $p(x) \in F[x]$. Then we have canonical isomorphisms:
>
> $$ F(\alpha) \cong F[x]/(p(x)) \cong F(\alpha') $$
>
> with the map $\sigma : F(\alpha) \to F(\alpha')$ defined by sending $\alpha \mapsto \alpha'$ and fixing $F$.
>
> Since $\overline{F}$ is an algebraic closure of both $F(\alpha)$ and $F(\alpha')$, the isomorphism extension theorem guarantees that $\sigma$ extends to an automorphism:
>
> $$ \overline{\sigma} \in \operatorname{Aut}(\overline{F}/F) $$
>
> such that $\overline{\sigma}(\alpha) = \alpha'$.

---

Now, we prove the isomorphism extension theorem. We formulate the proof using the following two lemmas.

**Lemma (Extension into Algebraically Closed Field).**  
Let $F$ be a field and $\overline{F}$ its algebraic closure. Let $\Omega$ be an algebraically closed field, and suppose $\sigma : F \hookrightarrow \Omega$ is an injective field homomorphism. Then there exists an embedding

$$
\tilde{\sigma} : \overline{F} \hookrightarrow \Omega
$$

such that $\tilde{\sigma}\|\_F = \sigma$.

> **Proof.**  
> Define the set:
>
> $$ \Sigma = \{ (K, \theta) : F \subseteq K \subseteq \overline{F},\ \theta : K \hookrightarrow \Omega,\ \theta|_F= \sigma \} $$
>
> We partially order $\Sigma$ by declaring:
>
> $$ (K_1, \theta_1) \leq (K_2, \theta_2) \quad \text{if} \quad K_1 \subseteq K_2 \quad \text{and} \quad \theta_2|_{K_1} = \theta_1. $$
>
> It is straightforward to check that $(\Sigma, \leq)$ is a partially ordered set. Let $\mathcal{C}$ be a chain in $\Sigma$. Define:
>
> $$ K = \bigcup_{(K_i, \theta_i) \in \mathcal{C}} K_i, \quad \text{and} \quad \theta : K \to \Omega \quad \text{by} \quad \theta|_{K_i} = \theta_i. $$
>
> Since the $\theta_i$ agree on overlaps, $\theta$ is well-defined. Also, $K$ is a field, as the union of a chain of nested subfields. Therefore, $(K, \theta)$ is an upper bound of $\mathcal{C}$.
>
> By Zorn's Lemma, there exists a maximal element $(K, \theta)$ in $\Sigma$.
>
> We claim $K = \overline{F}$. If not, let $\alpha \in \overline{F} \setminus K$, and let $p(x) \in K[x]$ be the minimal polynomial of $\alpha$ over $K$. Since $\Omega$ is algebraically closed, the polynomial $\theta(p(x))$ has a root $\beta \in \Omega$.
>
> Then, $\theta$ extends to an embedding $\tilde{\theta} : K(\alpha) \to \Omega$ by mapping $\alpha \mapsto \beta$. This defines a proper extension $(K(\alpha), \tilde{\theta}) \in \Sigma$, contradicting the maximality of $(K, \theta)$. Therefore, $K = \overline{F}$, and the extended embedding $\tilde{\sigma} := \theta$ is the desired one.

---

**Lemma.**  
Let $\overline{F}$ and $\overline{F}'$ be algebraic closures of fields $F$ and $F'$, respectively. Suppose

$$ \sigma : \overline{F} \hookrightarrow \overline{F}' $$

is an injective field homomorphism such that $\sigma(F) = F'$. Then $\sigma$ is an isomorphism — that is, $\sigma$ is also surjective.

> **Proof.**  
> Suppose for contradiction that $\alpha' \in \overline{F}' \setminus \sigma(\overline{F})$. Let $K' := \sigma(\overline{F})$.
>
> Since $\sigma : \overline{F} \to K'$ is an isomorphism, we can define its inverse:
>
> $$ \tau := \sigma^{-1} : K' \to \overline{F}.$$
>
> Let $p'(x)$ be the minimal polynomial of $\alpha'$ over $K'$, and define:
>
> $$ p(x) := \tau(p'(x)) \in \overline{F}[x].$$
>
> This $p(x)$ is irreducible in $\overline{F}[x]$ (as $p'(x)$ was irreducible over $K'$), so $K'(\alpha') \cong \overline{F}[x]/(p(x)) \cong \overline{F}(\alpha)$ for some root 
> $\alpha\in\overline{F}$ of $p(x)$. Therefore, $\tau$ extends to an isomorphism
>
> $$ \tilde{\tau} : K'(\alpha') \to \overline{F}(\alpha) \subseteq \overline{F}.$$
>
> Composing this injection with $\sigma: \overline{F}\to K'$ gives an injection $K'(\alpha')\hookrightarrow K'$
> which is identity on $K'$. However, this is impossible as 
> $\alpha' \notin K'$. Thus, $\sigma$ must be surjective.


To prove the **Isomorphism Extension Theorem**, let $\sigma : F \to F'$ be an isomorphism. Using the first lemma, we extend $\sigma$ to an embedding

$$ \tilde{\sigma} : \overline{F} \hookrightarrow \overline{F}' $$

such that $\tilde{\sigma}\|\_F = \sigma$. By the second lemma, since $\tilde{\sigma}(F) = F'$, the extension $\tilde
{\sigma}$ is in fact **surjective**. Therefore, $\tilde{\sigma}$ is an isomorphism from $\overline{F}$ to $\overline{F}'$ that extends $\sigma$.
