---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Normal_Extensions
comment: true
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

---


{% include notification.html 
status="is-info is-light"
icon="false"
message="
**Remark.**  
A tower of normal extensions does not necessarily yield a normal extension. Consider the following chain:

$$
\mathbb{Q} \subset \mathbb{Q}(\sqrt{2}) \subset \mathbb{Q}(\sqrt[4]{2})
$$

Both intermediate extensions are normal:

- $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$ is normal because it is the splitting field of $x^2 - 2$ over $\mathbb{Q}$.
- $\mathbb{Q}(\sqrt[4]{2})/\mathbb{Q}(\sqrt{2})$ is normal because it is the splitting field of $x^2 - \sqrt{2}$ over $\mathbb{Q}(\sqrt{2})$

However, the composite extension $\mathbb{Q}(\sqrt[4]{2})/\mathbb{Q}$ is **not** normal, since the minimal polynomial $x^4 - 2$ does not split completely over $\mathbb{Q}(\sqrt[4]{2})$. 

"%}

---

**Definition/Theorem (Normal Closure).**  
Let $E/F$ be an algebraic extension, and fix an algebraic closure $\overline{F}$ of $F$ containing $E$.
The **normal closure** of $E/F$ is the smallest subfield of $\overline{F}$ containing $E$ that is normal over $F$.

More concretely, the normal closure of $E/F$ is the splitting field of the set $\{ m_{\alpha, F}(x) : \alpha \in E \}$ over $F$.  
If $E = F(\alpha_1, \ldots, \alpha_n)$, then the normal closure of $E/F$ is the splitting field of the polynomial $\prod_{i=1}^n m_{\alpha_i, F}(x)$
over $F$, which is the same as $F$ adjoinging all the conjugates of each $\alpha_i$.

> **Proof.**  
> Let $L$ be the splitting field of the set $\{ m_{\alpha, F}(x) : \alpha \in E \}$ over $F$. Then $L/F$ is normal by construction, and clearly $E \subset L$.  
> 
> Suppose $L'$ is another field extension of $F$ such that $E \subset L'$ and $L'/F$ is normal.
> Then for each $\alpha \in E$, its minimal polynomial $m_{\alpha, F}(x)$ splits in $L'$ by normality. 
> Hence, the splitting field $L$ of all such $m_{\alpha, F}(x)$ is contained in $L'$.  
> 
> Therefore, $L$ is the smallest subfield of $\overline{F}$ containing $E$ that is normal over $F$.

