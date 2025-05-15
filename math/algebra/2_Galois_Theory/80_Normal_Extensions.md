---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Normal_Extensions
---

## Normal Extensions

**Definition/Theorem (Characterizations of Normal Extensions).**  
Let $F$ be a field, and let $E$ be an intermediate field such that $F \subset E \subset \overline{F}$, where $\overline{F}$ is an algebraic closure of $F$. Then the following statements are equivalent:

1. For every $\sigma \in \operatorname{Aut}(\overline{F}/F)$, we have $\sigma(E) = E$.
2. For every $\alpha \in E$, the minimal polynomial $m_{\alpha,F}(x)$ splits completely in $E$.
3. There exists a nonempty set of nonconstant polynomials $\mathcal{P} \subset F[x]$ such that $E$ is the splitting field of $\mathcal{P}$ over $F$.

If one of these conditions holds, we say that **$E/F$ is a normal extension**.

> **Proof.**  
> (1) ⟹ (2): Let $\alpha \in E$, and let $m_{\alpha,F}(x)$ be its minimal polynomial over $F$. If $\beta \in \overline{F}$ is any other root of $m_{\alpha,F}(x)$, then $\beta$ is a conjugate of $\alpha$ over $F$. By the Galois characterization of conjugates, there exists $\sigma \in \operatorname{Aut}(\overline{F}/F)$ such that $\sigma(\alpha) = \beta$. Since $\sigma(E) = E$ by assumption, we conclude that $\beta \in E$. Thus, all roots of $m_{\alpha,F}(x)$ lie in $E$, so it splits completely in $E$.
> 
> (2) ⟹ (3): Define $\mathcal{P} := \\{m_{\alpha,F}(x) : \alpha \in E\\}$. By assumption, each $m_{\alpha,F}(x)$ splits in $E$. Furthermore, any field extension of $F$ in which all elements of $\mathcal{P}$ split must contain $E$, so $E$ is the splitting field of $\mathcal{P}$ over $F$.
> 
> (3) ⟹ (1): This direction was proved previously in the [Splitting Fields](60_Splitting_Fields.md) section. If $E$ is a splitting field over $F$, then $\sigma(E) = E$ for all $\sigma \in \operatorname{Aut}(\overline{F}/F)$.

---

**Theorem (Characterization of Finite Normal Extensions).**  
Let $E/F$ be a field extension. Then $E/F$ is a finite normal extension if and only if $E$ is the splitting field of some polynomial $p(x) \in F[x]$.

> **Proof (Sketch).**  
> Suppose $E$ is the splitting field of some $p(x)$ over $F$. By the previous theorem, $E/F$ is normal. Write $E = F(\alpha_1, \ldots, \alpha_k)$, where $\alpha_i \in \overline{F}$ are the roots of $p(x)$. Since each $\alpha_i$ is algebraic, $E/F$ is finite by repeated applications of the tower law.
> 
> Suppose $E/F$ is finite and normal. Let $\\{e_1, \ldots, e_n\\}$ be an $F$-basis of $E$. Each $e_i$ is algebraic over $F$, so let $m_i(x) := m_{e_i,F}(x)$ be its minimal polynomial over $F$. Define:
> 
> $$ p(x) := \prod_{i=1}^n m_i(x).$$
> 
> Then we can show that $E$ is the splitting field of $p(x)$ over $F$.