---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Ring_Theory/Irreducible,_Prime_and_Associate
---
## Irreducibles, Primes and Associates

**Definition.**  
Let $D$ be an integral domain.
1. Let $a,b\in D$. We say that $a\mid b$ if there is $c\in D$ such that $b=ac$.

2. An element $a \in D$ is called **irreducible** if $a \ne 0$, $a \notin D^\times$, and 

   $$a = xy \implies x \in D^\times \quad \text{or} \quad y \in D^\times$$

3. An element $a \in D$ is called **prime** if $a \ne 0$, $a \notin D^\times$, and 

   $$a \mid xy \implies a \mid x \quad \text{or} \quad a \mid y$$

4. Two elements $a, b \in D$ are called **associates** if there exists a unit $u \in D^\times$ such that $a = ub$.  
   This defines an equivalence relation $\sim$, and we write the equivalence class of $a$ as:

   $$ [a] := \{ au : u \in D^\times \} $$

---

**Lemma.**  
Let $D$ be an integral domain.

1. Let $a,b\in D$. Then, $a\mid b$ if and only if $\langle a\rangle \supset\langle b\rangle$ (**To Divide Is To Contain**)
2. $a \in D$ is irreducible if and only if the principal ideal $\langle a \rangle$ is maximal among proper principal ideals of $D$.
3. $a \in D$ is prime if and only if $a \ne 0$ and $\langle a \rangle$ is a prime ideal.
4. $a,b\in D$ are associates if and only if $\langle a \rangle = \langle b \rangle$.

---

**Lemma (Prime implies Irreducible).**  
Let $D$ be an integral domain. Then:

$$a \in D \text{ is prime} \quad \Longrightarrow \quad a \text{ is irreducible}$$

> **Proof.**  
> Suppose $a$ is prime, so $a \ne 0$ and $a \notin D^\times$. Let $a = bc$ for some $b, c \in D$.  
> Since $a \mid bc$, by the definition of prime, either $a \mid b$ or $a \mid c$.  
> Without loss of generality, assume $a \mid b$. Then $b = a c'$ for some $c' \in D$, so:
>
> $$ a = bc = (a c') c = a (c' c)$$
>
> Since $D$ is an integral domain, we can cancel $a \ne 0$ to get $1 = c' c$.  
> Hence $c \in D^\times$, so $a$ is irreducible.

---

**Proposition (Primes and Irreducibles in a PID).**  
Let $D$ be a principal ideal domain (PID), and $a\in D$. Then:

$$ a \in D \text{ is irreducible} \quad \Longleftrightarrow \quad a \text{ is prime} $$

> **Proof.**  
> Suppose $a$ is irreducible. Then $a \ne 0$, $a \notin D^\times$, and $\langle a \rangle$ is maximal among proper principal ideals.  
> In a PID, every ideal is principal. Therefore, $\langle a \rangle$ is a maximal ideal, which implies it is also a prime ideal.  
> Since $a \ne 0$, we conclude that $a$ is prime.

{% include notification.html 
status="is-info is-light"
icon="false"
message="
**Remark.**  
The implication “irreducible implies prime” holds in any PID, but in fact the PID assumption can be weakened.  
What is truly needed is that elements factor uniquely into irreducibles—i.e., the domain is a **unique factorization domain** (UFD).
We will talk about this in the next section.
"%}

--- 

**Definition (Unique Factorization Domain).**  
An integral domain $D$ is called a **unique factorization domain (UFD)** if $\forall a\in D$ with 
$a\neq 0$, $a\notin D^\times$, 
1. (Existence) There are irreducibles $p_i\in D$ such that $a = p_1\cdots p_n$
2. (Uniqueness) If $a = p_1\cdots p_n = q_1\cdots q_m$ are two factorizations into irreducibles, then: 
   - $m=n$
   - After possible reordering, $p_i$ is a conjugate to $q_i$ for all $i$. 
