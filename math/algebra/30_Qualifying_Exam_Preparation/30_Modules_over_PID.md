---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Qualifying_Exam_Preparation/Modules_over_PID
comment: true
---

## Modules over a PID

### Key Theorems

**Theorem (Submodules of Free Modules over a PID).**  
Let $D$ be PID, and let $M \subseteq D^n$ be a submodule. Then:

1. $M$ is a free $D$–module.  
2. There exist elements $x_1, \ldots, x_n \in D^n$ and nonzero elements $a_1, \ldots, a_m \in D$ such that:
   1. $a_1 \mid a_2 \mid \cdots \mid a_m$ (divisibility chain).  
   2. $D^n = \bigoplus_{i=1}^n D x_i$ (i.e., $\{x_1, \ldots, x_n\}$ is a basis of $D^n$).  
   3. $M = \bigoplus_{i=1}^m D (a_i x_i)$.


**Corollary (Structure Theorem for Finitely Generated Modules over a PID).**  
Let $D$ be a PID, and let $M$ be a finitely generated $D$–module. Then there exist nonzero elements $d_1, \ldots, d_m \in D$ with

$$d_1 \mid d_2 \mid \cdots \mid d_m$$

such that

$$M \;\cong\; D^r \;\oplus\; \bigoplus_{i=1}^m D / \langle d_i \rangle.$$

Here:

1. $r = \operatorname{rank}(M)$ is uniquely determined.  
2. The ideals $\langle d_i \rangle$ are uniquely determined (up to multiplication by units).  
3. The minimal number of generators of $M$ is $r + m$.  
4. The torsion submodule of $M$ is

    $$\operatorname{Tor}(M) \;=\; \{m\in M: \exists \,d\in D \text{ s.t }dm = 0\} \;=\;  \bigoplus_{i=1}^m D / \langle d_i \rangle.$$

---

### Remarks

- This decomposition splits $M$ into a **free part** ($D^r$) and a **torsion part** (finite direct sum of cyclic modules).  
- For $D = \mathbb{Z}$, the theorem is the **Fundamental Theorem of Finitely Generated Abelian Groups**.  
- The elements $d_1 \mid d_2 \mid \cdots \mid d_m$ are called the **invariant factors** of $M$.  
