## Hom Functor
**Definition/Lemma**
Let $M$ be an $R$-module, then we define $h^M$ as a functor 

$$
\begin{align}h^M: \text{Category of }R\text{-module} &\mapsto \text{Category of }R\text{-module} \\
N &\mapsto \operatorname{Hom}_R(M, N)
\end{align}
$$

Given $f\in\operatorname{Hom}_R(N_1, N_2)$, then $h^M(f)(\phi) = f\circ \phi$ for every $\phi\in h^M(N_1)$. 

This makes $h^M$ a covariant functor. 

**Lemma**
1. $\operatorname{Hom}_R(R, N)\simeq N$ via $\phi\mapsto \phi(1)$
2. $\operatorname{Hom}_R(\bigoplus M_i. N)\simeq \prod\operatorname{Hom}_R(M_i. N)$
3. $\operatorname{Hom}_R(M, \prod N_i)\simeq \prod\operatorname{Hom}_R(M, N_i)$

**Theorem**
$h^M$ is a left exact functor in the sense that given exact sequence of $R$-module 

$$
0\rightarrow A \xrightarrow{f_1}B\xrightarrow{f_2} C
$$

We get another exact sequence of $R$-module 

$$
0\rightarrow h^M(A) \xrightarrow{h^M(f_1)}h^M(B)\xrightarrow{h^M(f_2)} h^M(C)
$$

In other words, $h^M$ preserves kernel in the sense that $h^M(\ker(A\mapsto B)) = \ker (h^M(A)\mapsto h^M(B))$