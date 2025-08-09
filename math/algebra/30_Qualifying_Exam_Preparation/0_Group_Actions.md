---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Group_Actions
comment: true
---
## Group Actions

### Key Definitions.
**Definition.**  
Let $G$ be a group and $X$ be a set. We say that $G$ **acts** on $X$ if there is
a map $\cdot: G\times X\to X$ such that

1. $e\cdot x = x$ for all $x\in X$.
2. $g_1\cdot(g_2\cdot x) = (g_1g_2)\cdot x$ for all $g_1,g_2\in G, x\in X$.

This induces a group homomorphism 

$$\rho: G\to S_X$$

where $\rho(g): X\to X$ is the left multiplication by $g$ map. 

**Definition.**  
Suppose that a group $G$ acts on a set $X$. Let $x\in X, g\in G$, we define
1. The **orbits** of $x$: $G\cdot x = \{g\cdot x: g\in G\}$
2. The **stablizer** of $x$: $G_x = \{g\in G: g\cdot x = x\}$
3. The **fixed points** of $g$: $X^g = \{x\in X: g\cdot x = x\}$
4. The **fixed points** of $G$: $X^G = \{x\in X: g\cdot x = x \;\;\forall\, g\in G\}$
5. The **set of orbits**: $G\backslash X = \{G\cdot x: x\in G\}$

**Definition.**  
Let $G$ be a group acting on a set $X$. We say that 
1. The action is **transitive** if there is only one orbit.
2. The action is **faithful** if $g\cdot x = x$ for all $x$ implies $g=e$. 
This is equivalent as saying that $\rho:G\to S_x$ is injective. In general, we also have $\ker \rho = \bigcap_{x\in X} G_x$.
and $G/\ker \rho$ acts faithfully on $X$. 

----
### Key Theorems.

**Theorem (Orbit-Stablizer Theorem).**  
Let $G$ be a group acting on a set $X$. Let $x\in X$. Then, $G_x$ is a subgroup of $G$, and there is a bijection 

$$G/G_x\to G\cdot x$$
$$gG_x\mapsto g\cdot x$$

**Theorem (Burnside's Lemma).**  
Let $G$ be a group acting on a set $X$. Then

$$|G\backslash X| = \frac{1}{|G|}\sum_{g\in X} |X^g|$$

> **Proof (Sketch).**  
> Let $S = \{(g,x): g\cdot x = x\}$. Consider two ways to count this set.

**Theorem (Class Equation).**  
Let $G$ be a group acting on a set $X$. Then

$$|X| = |X^G| + \sum_{G\cdot x\in G\backslash X, |G\cdot x|>1}[G: G_x]$$

---

### Key Examples
**Example 1.**  
Let $G$ be a group, then $G$ acts on $G$ via left multiplication. 
1. This action is transitive, and there is only one orbit. 
2. The stablizer of every element is trivial.
3. This action is also faithful, and we get an injection $\rho: G\hookrightarrow S_G$ (Cayley's Theorem).

**Example 2.**  
Let $G$ be a group, then $G$ acts on $G$ via conjugation.
1. The orbit of $x\in G$ is the **(conjugacy) class** of $x$: $Cl(x) = \{gxg^{-1}: g\in G\}$.
2. The stabilizer of $x\in G$ is the **centralizer** of $x$: $C_G(x) = \{g\in G: gx=xg\}$.
3. The fixed point of $g\in G$ is the centralizer of $g$.
4. The fixed points of $G$ is the **center** of $G$: $Z(G) = \{g\in G: gx=xg \;\;\forall, x\in G\}$.
5. Class Equation:
   $$|G| = |Z(G)| + \sum_{} [G: C_G(g)]$$
   where the sum go over all representative of the conjugacy classes, not in $Z(G)$.

**Example 3.**  
Let $G$ be a group and $H$ be a subgroup of $G$. Then, $G$ acts on $G/H$ via left translation.
1. The action is transitive, and there is only one orbit. 
2. The stabilizer of $xH$ is the subgroup $xHx^{-1}$.
3. The action may not be faithful. The kernel of $\rho: G\to S_{G/H}$ is 
the **normal core** of $H$: $Cor(H) = \bigcap_{x\in G}x H x^{-1}$. It is the largest subgroup of $H$, that is normal in $G$.

**Example 4.**  
Let $G$ be a group, and $X = \{H: H\leq G\}$ be the set of subgroups of $G$. Then, $G$ acts on $X$ via conjugation. 
1. The stablizer of $H\in X$ is the **normalizer** of $H$: $N_G(H) = \{g\in G: gHg^{-1}=H\}$. It is the largest subgroup of 
$G$ such that $H$ is a normal subgroup of this group.
2. The orbit of $H$ is the set of conjugates of $H: \{gHg^{-1}: g\in G\}$. The orbit stabilizer theorem tells 
that the number of conjugates of $H$ is given by $|G:N_G(H)|$.

--- 

### Exercises
1. Let $G$ be a finite p-group. Show that $Z(G)\neq \{e\}$. (Hint: Consider the class equation.)
2. Let $G$ be a finite group, and $H$ be a subgroup of $G$. Suppose that $[G: H] = p$ where $p$ is the smallest 
prime divisor of $|G|$. Show that $H$ is a normal subgroup of $G$. (Hint: Consider the example $3$ above. Show that $Cor(H) = H$)

