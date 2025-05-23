---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Ring_Theory/Factorization_in_Noetherian_Domains
---
## Factorization in Noetherian Domains

**Definition/Theorem (Noetherian Rings).**  
A commutative ring $R$ is said to be **Noetherian** if it satisfies one of the following equivalent conditions:

1. (**Ascending Chain Condition**) Every ascending chain of ideals  
   
   $$ I_1 \subseteq I_2 \subseteq I_3 \subseteq \cdots $$
   
   stabilizes. That is, there exists $n_0 \in \mathbb{Z}^+$ such that $I_n = I_{n_0}$ for all $n \geq n_0$.

2. (**Finitely Generated Ideals**) Every ideal of $R$ is finitely generated.

> **Proof.**  
> $1\implies 2$: Let $I \subset R$ be an ideal. Suppose $I$ is not finitely generated. Then, we can construct a strictly increasing chain:
> 
> $$ \langle a_1 \rangle \subsetneq \langle a_1, a_2 \rangle \subsetneq \langle a_1, a_2, a_3 \rangle \subsetneq \cdots $$
> 
> where each $a_i \in I$ is chosen so that $a_i \notin \langle a_1, \dots, a_{i-1} \rangle$. Such $a_i$ exists 
> since $I$ is not finitely generated, and thus $\langle a_1, \dots, a_{i-1} \rangle\subsetneq I$. However, this contradicts the ascending chain condition.
> 
> $2\implies 1$: Let $I_1 \subseteq I_2 \subseteq \cdots$ be an ascending chain of ideals. Then, the union  
> 
> $$ I = \bigcup_{n=1}^{\infty} I_n $$
> 
> is also an ideal. Since $R$ is Noetherian, $I$ is finitely generated: $I = \langle a_1, \dots, a_k \rangle$. Then all $a_i$ lie in some $I_{n_0}$, hence $I = I_{n_0}$, and the chain stabilizes at $I_{n_0}$.

---

**Theorem (Existence of Factorizations in Noetherian Integral Domains).**  
Let $D$ be a Noetherian integral domain. Then every nonzero, non-unit element $a \in D$ can be written as a product of irreducible elements.

> **Proof.**  
> Let
> 
> $$ \mathcal{G} = \left\{ \langle a \rangle : a \in D \setminus (\{0\} \cup D^\times),\ a \text{ is not a product of irreducibles} \right\} $$
> 
> Suppose for the contrary that $\mathcal{G} \ne \emptyset$. Since $D$ is Noetherian, every chain in $\mathcal{G}$ has an upper bound, and by [Zorn’s Lemma](../20_Miscellaneous/Zorn's_Lemma.md), $\mathcal{G}$ has a maximal element $\langle m \rangle$.
> 
> If $m$ is irreducible, then $m$ is trivially a product of irreducibles—contradiction.  
> If $m$ is reducible, write $m = ab$ with $a, b \notin D^\times$. Then $\langle a \rangle, \langle b \rangle \supsetneq \langle m \rangle$, and by maximality, both $a$ and $b$ are products of irreducibles. Hence $m = ab$ is also a product of irreducibles—contradiction.  
> 
> Thus, $\mathcal{G} = \emptyset$ and the theorem holds.

---

**Theorem (Irreducible Is Prime $\Leftrightarrow$ Uniqueness of Factorization).**  
Let $D$ be an integral domain in which every nonzero, non-unit element can be written as a product of irreducibles. Then:

$$ D \text{ is a UFD} \iff \text{every irreducible in } D \text{ is prime} $$

> **Proof.**  
> Suppose $D$ is a UFD and let $p \in D$ be irreducible. If $p \mid ab$, then write $ab = pc$ for some $c \in D$. Factor $a$, $b$, and $c$ into irreducibles:
> 
> $$ a = q_1 \cdots q_m,\quad b = r_1 \cdots r_k,\quad c = s_1 \cdots s_l $$
> 
> then:
> 
> $$ ab = q_1 \cdots q_m r_1 \cdots r_k = p s_1 \cdots s_l $$
> 
> By uniqueness of factorization, $p$ is associate to one of the $q_i$ or $r_j$, hence divides $a$ or $b$.
> 
> Conversely, we suppose that every irreducible is prime. To show uniqueness of factorization, we consider:
> 
> $$ p_1 \cdots p_n = q_1 \cdots q_m $$
> 
> where $p_i, q_j$ are irreducibles. Since $p_1$ is prime, it divides one of the $q_j$.
> By possible reordering, we suppose that $p_1 \mid q_1$. Then, we have $q_1 = p_1u_1$ for some $u_1\in D$. Since $q_1$ is irreducible, 
> and $p_1$ is not a unit, we know that $u_1$ is a unit, and thus $p_1\sim q_1$.
> 
> Then, we cancel $p_1$ on both sides, and proceed by induction on $n$. 


**Corollary.**  
Let $D$ be a Noetherian integral domain. Then $D$ is a **UFD** if and only if every irreducible element in $D$ is also prime.

**Corollary.**  
Every **Principal Ideal Domain (PID)** is a UFD.

---

{% include notification.html 
status="is-info is-light"
icon="false"
message="
**Remark.**  
The implication \"irreducible ⇒ prime\" is essential for uniqueness. This condition holds in any UFD and in all PIDs. However, in general integral domains, irreducibles need not be prime, and factorization may fail to be unique.
"%}