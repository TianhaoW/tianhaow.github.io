---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Group_Actions
comment: true
---
## Group Actions

### Key Definitions

**Definition.**  
Let $G$ be a group and $X$ be a set. We say that $G$ **acts** on $X$ if there is a map 
$\cdot: G\times X\to X$ such that:

1. $e\cdot x = x$ for all $x\in X$.
2. $g_1\cdot(g_2\cdot x) = (g_1g_2)\cdot x$ for all $g_1,g_2\in G$ and $x\in X$.

This action induces a group homomorphism

$$\rho: G\to S_X$$

where $\rho(g): X\to X$ is the map given by left multiplication by $g$.

**Definition.**  
Suppose a group $G$ acts on a set $X$. For $x\in X$ and $g\in G$, we define:

| **Orbit** of $x$:        | $G\cdot x = \\{g\cdot x: g\in G\\}$                     |
|--------------------------|---------------------------------------------------------|
| **Stabilizer** of $x$:   | $G_x = \\{g\in G: g\cdot x = x\\}$                      | 
| **Fixed points** of $g$: | $X^g = \\{x\in X: g\cdot x = x\\}$                      |
| **Fixed points** of $G$: | $X^G = \\{x\in X: g\cdot x = x \;\;\forall\, g\in G\\}$ |
| **Set of orbits**:       | $G\backslash X = \\{G\cdot x: x\in X\\}$                | 

**Definition.**  
Let $G$ act on $X$. We say:

1. The action is **transitive** if there is only one orbit.
2. The action is **faithful** if $g\cdot x = x$ for all $x$ implies $g=e$.  
   Equivalently, $\rho: G\to S_X$ is injective.

In general,  

$$\ker \rho = \bigcap_{x\in X} G_x,$$  

and $G/\ker \rho$ acts faithfully on $X$.

---

### Key Theorems

**Theorem (Orbit–Stabilizer Theorem).**  
Let $G$ act on $X$, and let $x\in X$. Then $G_x$ is a subgroup of $G$, and there is a bijection

$$G/G_x\ \longrightarrow\ G\cdot x,\qquad gG_x \mapsto g\cdot x.$$

**Theorem (Burnside's Lemma).**  
Let $G$ be a finite group acting on a finite set $X$. Then

$$|G\backslash X| = \frac{1}{|G|}\sum_{g\in G} |X^g|.$$

> **Proof (Sketch).**  
> Let $S = \\{(g,x)\in G\times X : g\cdot x = x\\}$. Count $|S|$ in two ways.

**Theorem (Class Equation).**  
Let $G$ act on $X$. Then

$$|X| = |X^G| + \sum_{\substack{G\cdot x\in G\backslash X \\ |G\cdot x|>1}} [G : G_x].$$

---

### Key Examples

**Example 1.**  
Let $G$ act on itself by left multiplication:

1. The action is transitive (one orbit).
2. The stabilizer of any element is trivial.
3. The action is faithful, giving an embedding $\rho: G\hookrightarrow S_G$ (Cayley’s Theorem).


**Example 2.**  
Let $G$ act on itself by conjugation:

1. The orbit of $x\in G$ is its **conjugacy class**:  

   $$\mathrm{Cl}(x) = \{gxg^{-1}: g\in G\}.$$

2. The stabilizer of $x$ is the **centralizer**: 

   $$C_G(x) = \{g\in G: gx = xg\}.$$

3. The fixed points of $g$ are exactly $C_G(g)$.
4. The fixed points of $G$ form the **center**:  

   $$Z(G) = \{g\in G: gx = xg \ \forall\, x\in G\}.$$

5. **Class Equation**:

   $$|G| = |Z(G)| + \sum [G : C_G(g)],$$

   where the sum runs over representatives of the conjugacy classes not contained in $Z(G)$.


**Example 3.**  
Let $G$ act on the left coset space $G/H$ by left multiplication:

1. The action is transitive (one orbit).
2. The stabilizer of $xH$ is $xHx^{-1}$.
3. The kernel of $\rho: G\to S_{G/H}$ is the **normal core**:  
   
   $$\mathrm{Cor}(H) = \bigcap_{x\in G} xHx^{-1},$$  

   the largest subgroup of $H$ that is normal in $G$.


**Example 4.**  
Let $X = \\{H \leq G\\}$ be the set of all subgroups of $G$. Let $G$ act on $X$ by conjugation:

1. The stabilizer of $H$ is the **normalizer**:  

   $$N_G(H) = \\{g\in G : gHg^{-1} = H\\},$$  

   which is the largest subgroup of $G$ in which $H$ is normal.
2. The orbit of $H$ is the set of conjugates $\\{gHg^{-1} : g\in G\\}$.
   By the Orbit–Stabilizer Theorem, the number of conjugates of $H$ is $[G : N_G(H)]$.

---

### Exercises

**Easy:**

1. Let $G$ be a finite $p$-group. Show that $Z(G) \neq \\{e\\}$.
   *(Hint: Use the class equation.)*
2. (**UCI 2023 Jan Algebra Qual**) Let $G$ be a group of order $p^2$. Show that $G$ is abelian. Classify all such groups up to isomorphism.
3. Let $G$ be a finite group, and $H\leq G$ with $[G : H] = p$ where $p$ is the smallest prime divisor of $|G|$. Show that $H \trianglelefteq G$.
   *(Hint: Apply Example 3 and show that $\mathrm{Cor}(H) = H$.)*
4. (**UCI 2024 June Algebra Qual**) Prove: If $H$ has finite index $n$ in $G$, then there exists a normal subgroup $K \trianglelefteq G$ with $K \leq H$ and $[G : K] \leq n!$. Do not assume $G$ is finite.

**Medium:**

1. Let $G$ be a group acting transitively on a finite set $X$ with $\|X\| > 1$. Show that there exists $g\in G$ with no fixed points (i.e., $X^g = \varnothing$).  
2. Let $G$ be a finite group, and $H\leq G$ be a proper subgroup. Show that $G\neq \bigcup\_{g\in G} gHg^{-1}$. *(Hint: Consider $G$ acting on $G/H$ via left translation. 
There is some $g\_0$ without any fixed point. Show that $g\_0\notin \bigcup_{g\in G}gHg^{-1}$)*