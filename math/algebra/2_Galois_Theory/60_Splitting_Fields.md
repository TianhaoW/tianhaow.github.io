---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Splitting_Fields
---

## Splitting Fields

**Definition.**  
Let $F$ be a field, and let $p(x) \in F[x] \setminus F$ be a non-constant polynomial. A **splitting field** of $p(x)$ over $F$ is a minimal field extension $E/F$ such that $p(x)$ splits completely in $E$. That is, there exist $\alpha_i \in E$ such that

$$ p(x) = \prod_{i=1}^k (x - \alpha_i) $$

More generally, if $\mathcal{P} \subset F[x] \setminus F$ is a set of non-constant polynomials, then a splitting field of $\mathcal{P}$ over $F$ is a minimal field extension $E/F$ such that every polynomial in $\mathcal{P}$ splits completely in $E$.

---

**Theorem (Existence and Uniqueness of Splitting Fields).**  
Let $F$ be a field and let $p(x) \in F[x] \setminus F$ be a non-constant polynomial. If we fix an algebraic closure $\overline{F}$ of $F$, then there exists a **unique** splitting field of $p(x)$ over $F$ inside $\overline{F}$.

Later, we will also prove (using the isomorphism extension theorem) that the splitting field is unique **up to isomorphism**, even without reference to a fixed $\overline{F}$.

> **Proof.**  
> Let $\alpha_1, \ldots, \alpha_k \in \overline{F}$ be the roots of $p(x)$. We claim that
>
> $$ F(\alpha_1, \ldots, \alpha_k) $$
>
> is the splitting field of $p(x)$ over $F$.
>
> First, since all the roots $\alpha_i$ lie in $F(\alpha_1, \ldots, \alpha_k)$, the polynomial $p(x)$ splits completely in this field.
>
> Now suppose $E$ is another field extension of $F$ in which $p(x)$ splits completely. Then all the roots $\alpha_i$ lie in $E$, so the field $F(\alpha_1, \ldots, \alpha_k)$ is contained in $E$. Therefore, $F(\alpha_1, \ldots, \alpha_k)$ is the **minimal** such field — i.e., a splitting field.
>
> Uniqueness inside $\overline{F}$ follows similarly: if $E' \subset \overline{F}$ is another splitting field of $p(x)$, then it must contain all roots $\alpha_i$, and hence also contain $F(\alpha_1, \ldots, \alpha_k)$. Conversely, since $E'$ is minimal, it must equal $F(\alpha_1, \ldots, \alpha_k)$.

---

{% include notification.html 
status="is-info is-light"
icon="false"
message="

**Remark (Splitting field of a set of polynomials).**  
Let

$$ \mathcal{P} = \{ p_1(x), \ldots, p_n(x) \} \subset F[x] \setminus F $$

be a **finite set** of non-constant polynomials. Then the splitting field of $\mathcal{P}$ over $F$ is the same as the 
splitting field of the single polynomial 
$p(x) = \prod_{i=1}^n p_i(x)$, since all the roots of the $p_i$ are also roots of $p$, and vice versa.

If $\mathcal{P}$ is an **infinite** set of non-constant polynomials, we proceed as follows. Choose an increasing chain 
of finite subsets

$$ \mathcal{P}_1 \subset \mathcal{P}_2 \subset \cdots \subset \mathcal{P} \;\;\;\;\;\;\;\;\;\;\;\;\bigcup_{i \in I} \mathcal{P}_i = \mathcal{P} $$

Let $E_i \subset \overline{F}$ be the splitting field of $\mathcal{P}_i$ over $F$. By the previous theorem, each $E_i$ exists and is uniquely determined inside $\overline{F}$. Moreover, we have an increasing chain of subfields:

$$ E_1 \subset E_2 \subset \cdots $$

We define:

$$ E = \bigcup_{i \in I} E_i $$

Then $E$ is a field extension of $F$ in which every $p(x) \in \mathcal{P}$ splits completely, and it is minimal with 
respect to this property. Therefore, $E$ is the unique splitting field of $\mathcal{P}$ over $F$ inside $\overline{F}$.

"%}

---

**Theorem.**  
Let $E$ be the splitting field of a set of polynomials $\mathcal{P} \subset F[x]$ over a field $F$, inside a fixed algebraic closure $\overline{F}$. Then for every $\sigma \in \operatorname{Aut}(\overline{F}/F)$, we have:

$$
\sigma(E) = E
$$

That is, the splitting field $E$ is stable under the action of all automorphisms of $\overline{F}$ fixing $F$.

> **Proof.**  
> First suppose $\mathcal{P}$ is a finite set of polynomials. Then, by a previous remark, $E$ is also the splitting field of a single polynomial 
> $p(x) = \prod_{f \in \mathcal{P}} f(x)$, and we can write
>
> $$ E = F(\alpha_1, \ldots, \alpha_k) $$
>
> where the $\alpha_i \in \overline{F}$ are all roots of $p(x)$. Let $\sigma \in \operatorname{Aut}(\overline{F}/F)$. Since $\sigma$ fixes $F$ pointwise and $p(x) \in F[x]$, we have:
>
> $$ p(\sigma(\alpha_i)) = \sigma(p(\alpha_i)) = \sigma(0) = 0 $$
>
> so $\sigma(\alpha_i)$ is also a root of $p(x)$ and hence belongs to $\{ \alpha_1, \ldots, \alpha_k \} \subset E$. Therefore,
>
> $$ \sigma(E) = \sigma(F(\alpha_1, \ldots, \alpha_k)) = F(\sigma(\alpha_1), \ldots, \sigma(\alpha_k)) \subset E $$
>
> and since $\sigma$ is invertible, we must have equality: $\sigma(E) = E$.
>
> Now suppose $\mathcal{P}$ is an infinite set. Then, by a previous remark, we may write
>
> $$ E = \bigcup_{i \in I} E_i $$
>
> where each $E_i$ is the splitting field of a finite subset $\mathcal{P}_i \subset \mathcal{P}$. 
> By the finite case, we know that $\sigma(E_i) = E_i$ for all $i$. Now for any $e \in E$, there exists some $i$ such that $e \in E_i$, and hence $\sigma(e) \in E_i \subset E$. Therefore, $\sigma(E) \subset E$. Applying the same argument to $\sigma^{-1}$ gives the reverse inclusion, so $\sigma(E) = E$.
 