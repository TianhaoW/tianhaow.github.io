---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Galois_Correspondence_Theorem
comment: true
---
## Galois Correspondence Theorem

**Theorem.**  
Let $E/F$ be a finite Galois extension. Then, there is a one-to-one correspondence between intermediate subfields of $E/F$ and subgroups of the Galois group $\text{Gal}(E/F)$:

$$\begin{aligned}
\{K : F \subset K \subset E \} 
&\longleftrightarrow 
\{H \leq \text{Gal}(E/F)\} \\
K &\xmapsto{\Psi} \text{Gal}(E/K) \\
E^H &\xleftarrow{\Phi} H
\end{aligned} $$

1. $\Psi$ is well-defined: for each intermediate field $K$, the extension $E/K$ is Galois. Moreover, $\Psi$ and $\Phi$ are inverse bijections.
2. This correspondence restricts to a bijection between **normal extensions** $K/F$ and **normal subgroups** $H \leq \text{Gal}(E/F)$.
3. If $K/F$ is a normal extension, then:

$$ \text{Gal}(K/F) \cong \text{Gal}(E/F) / \text{Gal}(E/K) $$

> **Proof.**  
> We pick $\alpha\in E$, and observe that $m_{\alpha, K}(x) \mid m_{\alpha, F}(x)$. Since $E/F$ is Galois, we know that $m_{\alpha, F}(x)$ has all its distinct roots in $E$, and so are $m_{\alpha, K}(x)$. Thus, $E/K$ is Galois, and $\Psi$ is well-defined. 
> 
> Since $E/K$ is Galois, we have $K = E^{\text{Gal}(E/K)}$ and $\text{Gal}(E/E^H) = H$, proving that $\Psi$ and $\Phi$ are inverse to each other.
> 
> Now, suppose $K/F$ is also Galois. Then we define a restriction map:
> 
> $$ r: \text{Gal}(E/F) \to \text{Gal}(K/F), \quad \sigma \mapsto \sigma|_K $$
> 
> This is well-defined because $K$ is normal over $F$. The map is surjective by the **Isomorphism Extension Theorem** (see [Isomorphism Extension](70_Isomorphism_Extension_Theorem.md)), which guarantees that every automorphism of $K$ extends to one of $E$.  
> 
> The kernel of $r$ is $\text{Gal}(E/K)$, so by the First Isomorphism Theorem:
> 
> $$ \text{Gal}(K/F) \cong \text{Gal}(E/F) / \text{Gal}(E/K) $$
> 
> Conversely, suppose $H \leq \text{Gal}(E/F)$ is a **normal subgroup**. Then for all $\sigma \in \text{Gal}(E/F)$ and $h \in H$, we have $\sigma h \sigma^{-1} \in H$.  
> 
> Let $\alpha \in E^H$ and $\sigma \in \text{Gal}(E/F)$. We want to show that $\sigma(\alpha) \in E^H$, i.e., $h(\sigma(\alpha)) = \sigma(\alpha)$ for all $h \in H$.  
> 
> Note that:
> 
> $$ h(\sigma(\alpha)) = (h\sigma)(\alpha) = (\sigma h')(\alpha) = \sigma(h'(\alpha)) = \sigma(\alpha) $$
> 
> where $h' = \sigma^{-1} h \sigma \in H$. This shows that $\sigma(\alpha) \in E^H$, and so $E^H$ is fixed under all automorphisms in $\text{Gal}(E/F)$, i.e., $E^H/F$ is normal.  
> 
> Since $E/E^H$ is separable as $E/F$ is separable, we know that $E^H/F$ is Galois.

---

**Corollary.**  
Let $E/F$ be a finite separable extension. Then $E/F$ has only finitely many intermediate subfields.

> **Proof.**  
> Let $\{\alpha_1, \ldots, \alpha_n\} \subset E$ be a basis over $F$, and let $p(x) = \prod_{i=1}^n m_{\alpha_i, F}(x)$. Since $E/F$ is separable, each $m_{\alpha_i, F}(x)$ is separable, so $p(x)$ is separable.
> 
> Let $L$ be the splitting field of $p(x)$ over $F$. Then $E \subset L$, and $L/F$ is a finite Galois extension. Hence, the number of intermediate fields of $L/F$ equals the number of subgroups of $\text{Gal}(L/F)$, which is finite.  
> 
> Since every intermediate field of $E/F$ is also one of the intermediate subfield of $L/F$, we know that $E/F$ has only finitely many intermediate subfields.

---

**Definition/Theorem (Simple Extensions).**  
Let $E/F$ be a finite field extension. If $E/F$ has finitely many intermediate subfields, then 
$E = F(\alpha)$ for some $\alpha \in E$.

In this case, we say that $\alpha$ is a **primitive element**, and $E/F$ is a **simple extension**.

> **Proof.**  
> Suppose $E = F(\alpha_1, \ldots, \alpha_n)$ is a finite extension. We prove the result by induction on $n$.  
> 
> The base case $n = 1$ is trivial. Suppose the result holds for $n-1$. Then consider $E = F(\alpha_1, \alpha_2)$.  
> 
> - If $F$ is a **finite field**, then so is $E$, and $E^\times$ is a finite cyclic group. Let $\alpha$ be a generator of $E^\times$, then $E = F(\alpha)$.
> 
> - If $F$ is **infinite**, consider subfields of the form $F(\alpha_1 + c\alpha_2)$ for varying $c \in F$. There are infinitely many such $c$, but only finitely many intermediate subfields by assumption. Hence, for some $c \neq d$, we have:
> 
> $$ F(\alpha_1 + c\alpha_2) = F(\alpha_1 + d\alpha_2) =: K $$
> 
> Then:
> 
> $$ (c - d)\alpha_2 = (\alpha_1 + c\alpha_2) - (\alpha_1 + d\alpha_2) \in K  \quad \Rightarrow \quad \alpha_2 \in K \text{ as } c-d\in F\subset K$$
> 
> and:
> 
> $$ \alpha_1 = (\alpha_1 + c\alpha_2) - c\alpha_2 \in K $$
> 
> So $\alpha_1, \alpha_2 \in K$, and hence $E = K = F(\alpha_1 + c\alpha_2)$ is simple.

---

**Corollary.**  
Any finite separable extension is a simple extension.

