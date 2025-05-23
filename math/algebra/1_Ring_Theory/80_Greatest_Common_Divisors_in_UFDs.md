---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Ring_Theory/Greatest_Common_Divisors_in_UFDs
---
## Greatest Common Divisors in UFDs

**Motivating Remark.**  
In the ring of integers $\mathbb{Z}$, we can unambiguously choose the greatest common divisor of $a$ and $b$ to be a positive integer. 
However, in a general unique factorization domain, there is no canonical way to select a "positive" representative. 
Therefore, when we define a **gcd** in a UFD, it is only well-defined **up to associates**.

---

**Definition (p-valuation).**  
Let $D$ be a UFD and let $p$ be a prime element in $D$. For $a \in D \setminus \\{0\\}$, we define the **$p$-valuation** of $a$, denoted $v_p(a)$, as the largest non-negative integer $n$ such that $p^n \mid a$.

We also define $v_p(0) := \infty$.

---

**Lemma (Basic Properties of p-Valuation).**  
Let $D$ be a UFD and let $\mathcal{P}$ be a choice of representatives for the set of prime elements in $D$ up to associates (i.e., one prime per associate class. In $\mathbb{Z}$, we pick the positive primes). Then:

1. If $p \sim q$, then $v_p(a) = v_q(a)$ for all $a \in D$. So $v_{[p]}(a)$ is well-defined on associate classes.
2. Every nonzero $a \in D$ has a unique factorization:  

   $$ a = u \prod_{p \in \mathcal{P}} p^{v_p(a)}, \quad \text{where } u \in D^\times $$

3. If $a \sim b$, then $v_p(a) = v_p(b)$ for all $p$.
4. $a \mid b$ if and only if $v_p(a) \leq v_p(b)$ for all $p \in \mathcal{P}$.
5. $v_p(ab) = v_p(a) + v_p(b)$.
6. $v_p(a + b) \geq \min \{ v_p(a), v_p(b) \}$. If $v_p(a) \ne v_p(b)$, then equality holds.

---

**Definition (Greatest Common Divisor).**  
Let $D$ be a UFD and let $a_1, \ldots, a_m \in D \setminus \\{0\\}$. Define the **greatest common divisor** of $a_1, \ldots, a_m$ to be the associate class:

$$ \gcd(a_1, \ldots, a_m) := \left[ \prod_{p \in \mathcal{P}} p^{\min_i v_p(a_i)} \right] $$

This is well-defined up to associates. Any representative $d$ of this class satisfies:

1. If $\gcd(a_1,\ldots, a_m) = [d]$, then $d \mid a_i$ for all $i$, and  

    $$ \gcd\left(\frac{a_1}{d}, \ldots, \frac{a_m}{d} \right) = [1] $$

2. For any element $c \in D\setminus\\{0\\}$,  

   $$ \gcd(ca_1, \ldots, ca_m) = [c] \cdot \gcd(a_1, \ldots, a_m) $$