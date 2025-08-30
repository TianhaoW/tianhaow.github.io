---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Modules
comment: true
---
## Modules

### Key Definitions

**Definition.**  
Let $R$ be a commutative ring with unity. An abelian group $M$ is called a **(left) $R$–module** if there exists a scalar multiplication map

$$\cdot : R \times M \to M$$

satisfying:

1. $r \cdot (m_1 + m_2) = r \cdot m_1 + r \cdot m_2$  
2. $(r+s) \cdot m = r \cdot m + s \cdot m$  
3. $(rs) \cdot m = r \cdot (s \cdot m)$  
4. $1 \cdot m = m$  

An $R$–module structure on $M$ is equivalent to a unital ring homomorphism

$$R \to \operatorname{End}(M).$$

If $R = k$ is a field, then an $R$–module is precisely a **vector space over $k$**.

---

**Definition.**  
Let $\{M_i\}_{i \in I}$ be $R$–submodules of $M$. The **sum** of the $M_i$ is defined as

$$\sum_{i \in I} M_i = \left\{ \sum_{i \in I} m_i : m_i \in M_i \ \text{and finitely many } m_i \neq 0 \right\}.$$

We say the sum is an **(internal) direct sum** if

$$M_i \cap \sum_{j \in I, \ j \neq i} M_j = \{0\} \quad \text{for all } i \in I.$$

In this case, we write

$$\bigoplus_{i \in I} M_i.$$

The internal direct sum is isomorphic to the **external direct sum**

$$\bigoplus_{i \in I} M_i = \{ (m_i)_{i \in I} : m_i \in M_i, \ \text{finitely many } m_i \neq 0 \}.$$

Thus, we do not distinguish between internal and external direct sums in notation.

---

**Definition.**  
For a family of $R$–modules $\{M_i\}_{i \in I}$, the **direct product** is defined as

$$\prod_{i \in I} M_i = \{ (m_i)_{i \in I} : m_i \in M_i \}.$$

---

**Definition.**  
Let $M$ be an $R$–module and $X \subset M$. We say $X$ **generates** $M$ if

$$M = \sum_{x \in X} R x.$$

Equivalently, the natural $R$–linear map

$$\phi : R^{|X|} \to M, \qquad (c_x)_{x \in X} \mapsto \sum_{x \in X} c_x x$$

is surjective.

- $X$ **freely generates** $M$ if $M=\sum_{x \in X} R x$ is a direct sum. In this case, we say that $M$ is a **free** $R$-module and $M \cong \bigoplus_{x\in X}Rx\cong R^{|X|}$ as $R$–modules.
We call $X$ as a **basis** of $M$.
- $M$ is **finitely generated** if there exists a finite generating set $X$.

---

**Definition.**  
Let $M$ be an $R$–module. A subset $X \subset M$ is **linearly independent** if $\sum_{x \in X} R x$ is a direct sum.


The **rank** of $M$ is the cardinality of the largest linearly independent subset of $M$.

