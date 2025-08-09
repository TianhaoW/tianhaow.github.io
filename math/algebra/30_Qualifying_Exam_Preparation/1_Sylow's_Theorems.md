---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Sylow's_Theorems
comment: true
---

## Sylow's Theorems

### Key Definitions.
**Definition.**  
1. We say that a group $G$ is a **$p$-group** if every element in $G$ has order $p^k$ for some non-negative integer $k$.
A finite group $G$ is a $p$-group if and only if $|G| = p^n$ for some $n$.
2. Let $G$ be a finite group such that $p^n\mid |G|$ yet $p^{n+1}\nmid |G|$. Then, a **sylow p-subgroup** of $G$ is a subgroup of order $p^n$.
We also denote the set of sylow $p$-subgroups of $G$ as $\text{Syl}_p(G)$.

---

### Key Theorems.

**Theorem (Sylow's First Theorem).**  
Let $G$ be a finite group such that $p^n\mid |G|$. Then, we can find 

$$P_1\triangleleft P_2\triangleleft\cdots\triangleleft P_n\leq G$$

such that $|P_i| = p^i$

**Theorem (Sylow's Second Theorem).**  
Let $G$ be a finite group, and $Q\leq G$ be a $p$-group, and $P\leq G$ be a sylow $p$-group. 
Then, there is $g\in G$ such that $gQg^{-1}\leq P$.

As a corollary, The action of $G$ on $\text{Syl}_p(G)$ via conjugation is transitive. Also, we have 

$$|\text{Syl}_p(G)| = [G: N_G(P)]$$

**Theorem (Sylow's Third Theorem).**  
Let $G$ be a finite group. Then, 

$$|\text{Syl}_p(G)|\equiv 1 \mod p$$

--- 

### Exercises
**Easy Level:**
1. Let $G$ be a group of order $pq$ where $p,q$ are prime numbers with $p < q$. Show that $G$ has a normal subgroup of order $q$.
2. Let $G$ be a group of order $p(p-1)$ where $p$ is prime. Show that $G$ has a subgroup of order $p$.

**Medium:**
1. (UCI 2024 Sep Algebra Qual) Let $G$ be a group of order $p^k(p+1)$ where $p$ is prime and $k\geq 2$. Show that $G$ is not simple.
   (Hint: Show that the number of sylow $p$-subgroups is either 1 or $p+1$. In the latter case, pick a Sylow $p$-group $P$, and consider the induced map 
    $\rho: G\to S_{G/P}\cong S_{p+1}$. What can we say about the kernel?)