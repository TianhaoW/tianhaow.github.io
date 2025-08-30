---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Localization_of_Modules
comment: true
---

## Localization of Modules

### Key Definitions

**Definition.**  
Let $R$ be a commutative ring with unity, and let $S \subset R$ be a multiplicatively closed subset.
If $M$ is an $R$–module, the **localization** of $M$ with respect to $S$ is

$$S^{-1}M = \left\{ \frac{m}{s} : m \in M, \ s \in S \right\} / \sim,$$

where the equivalence relation is given by

$$\frac{m_1}{s_1} \sim \frac{m_2}{s_2} \quad \Longleftrightarrow \quad \exists\, s \in S \ \text{such that } \ s(s_1 m_2 - s_2 m_1) = 0.$$

$S^{-1}M$ is naturally both an $R$–module and an $S^{-1}R$–module.


If $\mathfrak{p}$ is a prime ideal of $R$, we define the localization of $M$ at $\mathfrak{p}$ by

$$M_{\mathfrak{p}} = S_{\mathfrak{p}}^{-1}M, \quad S_{\mathfrak{p}} = R \setminus \mathfrak{p}.$$


---

### Key Theorems

**Theorem (Localization is an exact functor).**  
The localization functor

$$S^{-1} : \text{Category of $R$–modules} \;\longrightarrow\; \text{Category of $S^{-1}R$–modules}$$

is exact. In other words, it preserves kernels and cokernels (more generally, all limits and colimits).

**Theorem (Localization as Tensor Product).**  
For any $R$–module $M$, there is a natural isomorphism

$$S^{-1}R \otimes_R M \;\cong\; S^{-1}M,$$

given by $\big(\tfrac{r}{s}, m\big) \mapsto \tfrac{rm}{s}$.

**Theorem.**  
For an $R$–module $M$, the following are equivalent:

1. $M = 0$.  
2. $M_{\mathfrak{p}} = 0$ for all prime ideals $\mathfrak{p}$ of $R$.  
3. $M_{\mathfrak{m}} = 0$ for all maximal ideals $\mathfrak{m}$ of $R$.

{% include notification.html 
status="is-info is-light"
icon="false"
message="

**Remark.**  
From a geometric perspective, modules correspond to quasi-coherent sheaves on the affine scheme $X = \operatorname{Spec}(R)$, which we may think of as collections of generalized functions on a geometric space.  

- Maximal ideals correspond to **closed points** of $X$.  
- Localizing $M$ at a maximal ideal $\mathfrak{m}$ gives the **germ of sections** near the point $\mathfrak{m}$.  

The theorem above can be interpreted as saying: if a function vanishes at every point (i.e., its germ is zero everywhere), then the function is identically zero globally.
" %}

  
**Corollary.**  
Let $f : M \to N$ be an $R$–module homomorphism. Then the following are equivalent
1. $f$ is injective/surjective.
2. $f_{\mathfrak{p}} : M_{\mathfrak{p}} \to N_{\mathfrak{p}}$ is injective/surjective for all prime ideals $\mathfrak{p}$ of $R$.
3. $f_{\mathfrak{m}} : M_{\mathfrak{m}} \to N_{\mathfrak{m}}$ is injective/surjective for all maximal ideals $\mathfrak{m}$ of $R$.

> **Proof (Sketch).**  
> Since localization is an exact functor, it preserves kernels. In particular,
> 
> $$(\ker f)_{\mathfrak{p}} = \ker(f_{\mathfrak{p}}) \quad \text{for all prime ideals } \mathfrak{p} \subset R.$$
> 
> Therefore, $\ker f = 0$ if and only if $\ker f\_\mathfrak{p} = (\ker f)\_\mathfrak{p} = 0$ for all prime ideals $\mathfrak{p}$ of $R$. This translates to 
> $f$ is injective if and only if $f\_\mathfrak{p}$ is injective for all prime ideals $\mathfrak{p}$ of $R$.
