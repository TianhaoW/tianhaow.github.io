---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Sylow's_Theorems
comment: true
---
## Sylow’s Theorems

### Key Definitions

**Definition.**  

1. A group $G$ is called a **$p$–group** if every element of $G$ has order $p^k$ for some non-negative integer $k$. A finite group $G$ is a $p$–group if and only if $\|G\| = p^n$ for some $n$.

2. Let $G$ be a finite group such that $p^n \mid \|G\|$ but $p^{n+1} \nmid \|G\|$. A **Sylow $p$–subgroup** of $G$ is a subgroup of order $p^n$. We denote the set of Sylow $p$–subgroups of $G$ by $\mathrm{Syl}_p(G)$.

---

### Key Theorems

**Theorem (Sylow’s First Theorem).**  
Let $G$ be a finite group with $p^n \mid |G|$. Then $G$ contains a subgroup of order $p^n$.
In fact, there exist subgroups

$$P_1 \trianglelefteq P_2 \trianglelefteq \cdots \trianglelefteq P_n \leq G$$

such that $\|P_i\| = p^i$ for each $i$.


**Theorem (Sylow’s Second Theorem).**  
Let $G$ be a finite group, $Q \leq G$ a $p$–group, and $P \in \mathrm{Syl}_p(G)$.
Then there exists $g\in G$ such that

$$gQg^{-1} \leq P.$$

As a corollary:

- $G$ acts transitively on $\mathrm{Syl}_p(G)$ by conjugation.
- For $P \in \mathrm{Syl}_p(G)$,  

  $$|\mathrm{Syl}_p(G)| = [G : N_G(P)].$$


**Theorem (Sylow’s Third Theorem).**  
Let $G$ be a finite group and $p$ a prime dividing $|G|$. Then

$$|\mathrm{Syl}_p(G)| \equiv 1 \pmod{p}$$

---

### Exercises

**Easy:**

1. Let $G$ be a group of order $pq$, where $p$ and $q$ are primes with $p < q$. Show that $G$ has a normal subgroup of order $q$.
2. Let $G$ be a group of order $p(p-1)$ where $p$ is prime. Show that $G$ has a subgroup of order $p$.
3. (**UCI 2025 June Algebra Qual**) Let $G$ be a finite group and $p$ a prime dividing $|G|$.
   Let $O_p(G)$ denote the intersection of all Sylow $p$–subgroups of $G$.
   Show that $O_p(G) \trianglelefteq G$ and that it contains every normal $p$–subgroup of $G$.


**Medium:**

1. (**UCI 2024 September Algebra Qual**)
   Let $G$ be a group of order $p^k (p+1)$ where $p$ is prime and $k \geq 2$. Show that $G$ is not simple.  
   *(Hint: Show that $s_p = |\mathrm{Syl}_p(G)|$ is either $1$ or $p+1$. In the latter case, pick $P \in \mathrm{Syl}_p(G)$ and consider the induced homomorphism*

   $$\rho: G \to S_{G/P} \cong S_{p+1}.$$ 

   *Analyze $\ker \rho$.)*  
   *(Hint: You can also use the Burnside's normal p-complement theorem to overkill this problem. )*
