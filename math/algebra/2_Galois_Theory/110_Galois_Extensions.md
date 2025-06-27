---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Galois_Extensions
---
## Galois Extensions

**Definition.**  
A field extension $E/F$ is called a **Galois extension** if it is both normal and separable.
In this case, we denote the group $\operatorname{Aut}(E/F)$ by $\operatorname{Gal}(E/F)$ and call it the **Galois group** of the extension.

---

**Theorem (Characterization of Finite Galois Extensions).**  
Let $E/F$ be a finite field extension. The following are equivalent:

1. $E/F$ is a Galois extension.
2. $E$ is the splitting field of a separable polynomial $p(x) \in F[x]$.
3. $\|\operatorname{Aut}(E/F)\| = [E:F]$.
4. $F = E^{\operatorname{Aut}(E/F)} := \\{ e \in E : \sigma(e) = e \text{ for all } \sigma \in \operatorname{Aut}(E/F) \\}$.

> **Proof.**  
> $1 \Rightarrow 2$: Since $E/F$ is normal and finite, it is the splitting field of some polynomial $p(x) \in F[x]$ (see [Normal Extension](./80_Normal_Extensions.md)).
> As $E/F$ is also separable, each irreducible factor of $p(x)$ is a scalar multiple of some minimal polynomials of elements in $E$, and hence separable. Therefore, $p(x)$ is separable. 
> 
> $2 \Rightarrow 3$ and $3\Rightarrow 1$: This will be proved in the following theore,
> 
> We will prove the equivalence with (4) in separate theorems later.

---

**Theorem (Number of Automorphisms Characterizes Galois Extensions).**  
Let $E/F$ be a finite field extension, and let $\sigma : F \hookrightarrow E$ be an injective field homomorphism. Define:

- $\operatorname{Iso}\_\sigma(E, E) = \\{ \hat\sigma : E \to E \mid \hat\sigma\|\_F = \sigma \\}$
- $\operatorname{Embed}\_\sigma(F(\alpha), E) = \\{ \bar\sigma : F(\alpha) \hookrightarrow E \mid \bar\sigma\|\_F = \sigma \\}$

Then,  

$$|\operatorname{Iso}_\sigma(E, E)| \leq [E : F]$$  

with equality if and only if $E/F$ is a Galois extension.
Taking $\sigma = \operatorname{id}_F$ proves the equivalence of (1) and (3) in the previous theorem.

> **Proof.**  
> We proceed by strong induction on $[E : F]$. The base case $[E : F] = 1$ is trivial.
> Suppose $[E : F] > 1$, and choose $\alpha \in E \setminus F$.  
> 
> Every extension $\hat\sigma \in \operatorname{Iso}\_\sigma(E, E)$ restricts to $\bar\sigma = \hat\sigma\|\_{F(\alpha)} \in \operatorname{Embed}_\sigma(F(\alpha), E)$.
> By inductive hypothesis,
> 
> $$ |\operatorname{Iso}_\sigma(E, E)| = \sum_{\bar\sigma \in \operatorname{Embed}_\sigma(F(\alpha), E)} |\operatorname{Iso}_{\bar\sigma}(E, E)| = |\operatorname{Embed}_\sigma(F(\alpha), E)| \cdot [E : F(\alpha)]. $$
> 
> Each $\bar\sigma$ is determined by $\bar\sigma(\alpha)$, which must be a root of $\sigma(m_{\alpha, F}(x))$ in $E$.
> Therefore,
> 
> $$ |\operatorname{Embed}_\sigma(F(\alpha), E)| \leq \deg m_{\alpha, F}(x) = [F(\alpha) : F], $$
> 
> and hence,
> 
> $$ |\operatorname{Iso}_\sigma(E, E)| \leq [F(\alpha) : F] \cdot [E : F(\alpha)] = [E : F].$$
> 
> Equality holds if and only if $\sigma(m_{\alpha, F}(x))$ has all of its roots in $E$, and they are distinct. This is true for all $\alpha\in E$.
> Thus, we know that $E/F$ is normal and separable. If $E/F$ is the splitting field of a separable polynomial, the above equality will also hold 
> by the same argument. 

---

**Lemma (Artin's Lemma).**  
Let $E$ be a field, and let $G \subset \operatorname{Aut}(E)$ be a finite subgroup. Define the **fixed field** of $G$ by  

$$E^G := \{ e \in E : \sigma(e) = e \text{ for all } \sigma \in G \}.$$

Then $E^G$ is a subfield of $E$, and  

$$[E : E^G] \leq |G|.$$

> **Proof.**  
> It is straightforward to verify that $E^G$ is a subfield of $E$.
> 
> Suppose $|G| = n$ with $G = \\{ \sigma_1, \ldots, \sigma_n \\}$, where $\sigma_1 = \operatorname{id}$.
> We will show that any $n+1$ elements $e_1, \ldots, e_{n+1} \in E$ are linearly dependent over $E^G$.
> 
> Let $V \subset E^{n+1}$ be the kernel of the $n \times (n+1)$ matrix:
> 
> $$
    \begin{bmatrix}
    \sigma_1(e_1) & \cdots & \sigma_1(e_{n+1}) \\
    \vdots & \ddots & \vdots \\
    \sigma_n(e_1) & \cdots & \sigma_n(e_{n+1})
    \end{bmatrix}.
    $$
> 
> Since this matrix has more columns than rows, the kernel $V$ has dimension at least 1.  
> 
> Let $v = (c_1,\ldots, c_{n+1}) \in V$ be a nonzero vector of minimal weight (number of nonzero entries), and scale $v$ so one coordinate is 1.
> Then, for any $\sigma \in G$, we have $\sigma(v) \in V$, so $\sigma(v) - v \in V$. We will show that $v\in (E^G)^{n+1}$. Then, the first row of the matrix multiplication by $v$
> yields a non-trivial linear relation among $e_1,\ldots, e_{n+1}$ over $E^G$.
> 
> If $v \notin (E^G)^{n+1}$, then $\sigma(v) \ne v$ for some $\sigma\in G$, and $\sigma(v) - v$ is a nonzero vector of smaller weight—contradicting minimality.
> Thus, $v \in (E^G)^{n+1}$, and $e_1, \ldots, e_{n+1}$ are linearly dependent over $E^G$.

---

**Theorem (Galois Extension from Automorphism Group).**  
Let $E$ be a field, and $G \subset \operatorname{Aut}(E)$ be a finite group of automorphisms.
Then, if $F = E^G$ is the fixed field of $G$, the extension $E/F$ is Galois and  

$$\operatorname{Gal}(E/F) = G.$$

> **Proof.**  
> By Artin's Lemma, $[E : F] \leq |G|$, and $G \subset \operatorname{Aut}(E/F)$.
> Thus,
> 
> $$ |G| \leq |\operatorname{Aut}(E/F)| \leq [E : F] \leq |G|, $$
> 
> so all inequalities are equalities. Hence, $\|\operatorname{Aut}(E/F)\| = [E:F]$, which implies $E/F$ is Galois.
> Moreover, since $\|G\| = \|\operatorname{Aut}(E/F)\|$ and $G \subset \operatorname{Aut}(E/F)$, we conclude that $\operatorname{Gal}(E/F) = G$.

---

**Corollary (Fix Field Characterizes Galois Extension).**  
Let $E/F$ be a finite extension. Then $E/F$ is Galois if and only if  

$$F = E^{\operatorname{Aut}(E/F)}.$$

> **Proof.**  
> If $E/F$ is Galois, then $\operatorname{Aut}(E/F)$ has size $[E : F]$. Since $F\subset  E^{\operatorname{Aut}(E/F)}$, we have 
> 
> $$|\operatorname{Aut}(E/F)| = [E: F]\geq [E:E^{\text{Aut}(E/F)}] = |\operatorname{Aut}(E/F)|,$$
> 
> and hence must be $F = E^{\text{Aut}(E/F)}$.  
> 
> The converse direction is proved in the above theorem with $G = \operatorname{Aut}(E/F)$.

