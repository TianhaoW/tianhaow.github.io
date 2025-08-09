---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Miscellaneous/Zorn's_Lemma
comment: true
---
## Zorn's Lemma

**Definition (Partial Order and Partially Ordered Set).**  
Let $\mathcal{P}$ be a set equipped with a binary relation $\leq$. We say that $\leq$ is a **partial order** if it satisfies:
1. **Reflexivity:** $x \leq x$ for all $x \in \mathcal{P}$
2. **Antisymmetry:** If $x \leq y$ and $y \leq x$, then $x = y$
3. **Transitivity:** If $x \leq y$ and $y \leq z$, then $x \leq z$

A set $\mathcal{P}$ together with a partial order is called a **partially ordered set** (or **poset**).

A subset $\mathcal{C} \subset \mathcal{P}$ is called a **chain** if every pair of elements is comparable:  
for all $x, y \in \mathcal{C}$, either $x \leq y$ or $y \leq x$.

An element $m \in \mathcal{P}$ is called **maximal** if there is no element $n \in \mathcal{P}$ such that $m < n$.

---

**Zorn’s Lemma.**  
Let $\mathcal{P}$ be a partially ordered set in which **every chain** $\mathcal{C}\subset\mathcal{P}$ has an upper bound in $\mathcal{P}$. Then:

> $$\mathcal{P} \text{ contains at least one maximal element.}$$

Zorn’s Lemma is logically equivalent to the Axiom of Choice, and it is a powerful tool for constructing maximal objects.

---

**How to Use Zorn’s Lemma in Practice.**  
To apply Zorn’s Lemma, follow these steps:

1. Define a set $\mathcal{P}$ of “candidate” structures.
2. Introduce a partial order $\leq$ on $\mathcal{P}$.
3. Prove that every chain has an upper bound in $\mathcal{P}$.
4. Conclude that $\mathcal{P}$ has a **maximal element**.

---

{% include notification.html
status="is-info is-light"
icon="false"
message="
**Intuition: Why Zorn’s Lemma is Useful**

Zorn’s Lemma gives us a way to 'build' something maximal without having to explicitly describe it.  
It guarantees the existence of large mathematical objects (fields, ideals, bases) under mild closure properties.

For example:
- Every nonzero ring has a **maximal ideal**.
- Every vector space has a **basis**.
- Every field has an **algebraic closure**.

Zorn’s Lemma formalizes the idea:  
> “If I can always extend, then I can extend as far as possible.”
" %}

---

**Example: Existence of Maximal Ideals.**  
Let $R$ be a commutative ring with $1 \ne 0$. Then $R$ has a maximal ideal.

> **Proof Sketch.**  
> Let
>
> $$ \mathcal{I} := \{ I \subset R : I \text{ is an ideal and } I \ne R \} $$
>
> ordered by inclusion. Any chain $\mathcal{C} \subset \mathcal{I}$ has an upper bound:
>
> $$ I^* := \bigcup_{I \in \mathcal{C}} I $$
>
> which is also a proper ideal. So by Zorn’s Lemma, $\mathcal{I}$ has a maximal element — a maximal ideal.
