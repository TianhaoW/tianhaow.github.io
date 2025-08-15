---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Semi-direct_Product
comment: true
---
## Semi-Direct Product

### Key Definitions

**Definition.**  
Consider a **short exact sequence** of groups

$$1 \to N \xrightarrow{\phi_1} G \xrightarrow{\phi_2} G_2 \to 1.$$

We say that the short exact sequence **splits** if one of the following equivalent conditions holds:

1. There exists a homomorphism $\psi: G_2 \to G$ such that $\phi_2 \circ \psi = \mathrm{id}_{G_2}$.
2. There exists a subgroup $H \leq G$ such that:
   - $H \cap N = \{e\}$, and  
   - $HN = G$.  

   In this case, $H \cong G_2 \cong G/N$.


**Definition / Theorem.**  
Let $N$ and $H$ be groups, and let $f \in \operatorname{Hom}(H, \operatorname{Aut}(N))$.
The **semi-direct product** $H \ltimes_f N$ is a group with underlying set $H \times N$ and multiplication

$$(h_1, n_1) \cdot (h_2, n_2) = \big(h_1 h_2, \ f(h_2^{-1})(n_1) \, n_2\big).$$

---

### Key Theorems

**Theorem (Schur–Zassenhaus).**  
A short exact sequence

$$1 \to N \to G \to H \to 1$$

splits if $\gcd(\|N\|, \|H\|) = 1$.

**Theorem.**  
Let

$$1 \to N \to G \to H \to 1$$

be a splitting short exact sequence. Then there exists $f \in \operatorname{Hom}(H, \operatorname{Aut}(N))$ such that

$$G \cong H \ltimes_f N.$$

> **Remark.**  
> In the splitting case, we can replace $N$ and $H$ by isomorphic copies inside $G$ (viewing them as subgroups).  
> Every element $g \in G$ can be written uniquely as $h n$ with $h \in H$ and $n \in N$.  
> This gives a bijection $G \leftrightarrow H \times N$ via $h n \mapsto (h, n)$. Then, we use group structure on $G$ to 
> define a group structure on $H\times N$. 
> 
> The multiplication in $G$ satisfies
> 
> $$h_1 n_1 \, h_2 n_2 = h_1 h_2 \, (h_2^{-1} n_1 h_2) \, n_2.$$
> 
> Since $N \trianglelefteq G$, we have $h_2^{-1} n_1 h_2 \in N$.
> Defining $f: H \to \operatorname{Aut}(N)$ by $f(h) = c(h)$ (conjugation by $h$) yields the desired formula for the semi-direct product structure.


**Lemmas.**  
Let $H$ and $N$ be groups and $f \in \operatorname{Hom}(H, \operatorname{Aut}(N))$.

1. If $f$ is the trivial homomorphism (sending every $h \in H$ to $\mathrm{id}_N$), then $H \ltimes_f N \cong H \times N$ (the direct product).
2. If $f$ is non-trivial, then $H \ltimes_f N$ is non-abelian.

---

### Exercises

**Easy:**

1. (**UCI 2025 June Algebra Qual**) Give an example of a semi-direct product of two cyclic groups of odd order that is not abelian. *(See Medium problem 2.)*
2. (**UCI 2024 June Algebra Qual**) Prove that every group of order $15$ is cyclic. *(See Medium problem 1.)*
3. (**UCI 2024 June Algebra Qual**) Determine whether every group of order $21$ is cyclic. *(See Medium problem 2.)*

**Medium:**

1. Let $p < q$ be primes with $p \nmid (q-1)$. Show that every group of order $pq$ is cyclic.
2. Let $p < q$ be primes with $p \mid (q-1)$. Show that there exists a non-abelian group of order $pq$.
3. Let $G$ be a group of order $2p$ where $p$ is an odd prime. Show that $G$ is either cyclic or dihedral.