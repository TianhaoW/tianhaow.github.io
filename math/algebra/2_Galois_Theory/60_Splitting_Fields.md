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