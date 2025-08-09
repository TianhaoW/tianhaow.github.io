---
hide_hero: true
menubar: math_menubar
permalink: /math/algebra/Galois_Theory/Separable_Polynomials
comment: true
---
## Separable Polynomials

**Definition.**  
A polynomial $p(x) \in F[x] \setminus F$ is called **separable** if all of its irreducible factors over $F$ have distinct roots in $\overline{F}$.

---

**Theorem (Invariance of GCD across field extensions).**  
Let $E/F$ be a field extension, and let $f(x), g(x) \in F[x]$. Then, the greatest common divisor of $f(x)$ and $g(x)$ is the same in $F[x]$ and in $E[x]$, up to associates.

> **Proof.**  
> Let $d(x) \in F[x]$ be a representative of $\gcd(f(x), g(x))$ in $F[x]$ up to associates. Then:
> 
> $$\gcd_{F[x]}\left(\frac{f(x)}{d(x)}, \frac{g(x)}{d(x)}\right) = 1.$$
> 
> Since $F[x]$ is a PID, we can find $a(x), b(x) \in F[x]$ (See [Bezout's identity](../1_Ring_Theory/80_Greatest_Common_Divisors_in_UFDs.md)) such that
> 
> $$a(x)\frac{f(x)}{d(x)} + b(x)\frac{g(x)}{d(x)} = 1.$$
> 
> This same identity holds in $E[x]$, so:
> 
> $$\gcd_{E[x]}\left(\frac{f(x)}{d(x)}, \frac{g(x)}{d(x)}\right) = 1,$$
> 
> and therefore
> 
> $$\gcd_{E[x]}(f(x), g(x)) = d(x) = \gcd_{F[x]}(f(x), g(x)).$$

This result shows that we may compute $\gcd$ of polynomials over the base field $F$ without ambiguity, even when working inside an extension.

---

**Theorem (Irreducible polynomial separability criterion).**  
Let $F$ be a field, and let $p(x) \in F[x]$ be an irreducible polynomial. Then $p(x)$ is separable if and only if $\gcd(p(x), p'(x)) = [1]$, where $p'(x)$ is the formal derivative of $p(x)$.

> **Proof.**  
> Suppose $\alpha \in \overline{F}$ is a root of $p(x)$. We write
> 
> $$p(x) = (x - \alpha)^v q(x),$$
> 
> where $v \ge 1$ and $(x - \alpha) \nmid q(x)$. Then, using the product rule,
> 
> $$p'(x) = v(x - \alpha)^{v - 1} q(x) + (x - \alpha)^v q'(x).$$
> 
> If $\alpha$ is a repeated root, then $v \ge 2$, and thus $(x - \alpha) \mid p'(x)$. So $(x - \alpha)$ divides both $p(x)$ and $p'(x)$, meaning that $\gcd(p(x), p'(x))$ is not a unit in $F[x]$.
> 
> Conversely, suppose $\gcd(p(x), p'(x))$ is not a unit. Then, there exists some $\alpha \in \overline{F}$ such that $(x - \alpha)$ divides both $p(x)$ and $p'(x)$. Write
> 
> $$p(x) = (x - \alpha) q(x),$$
> 
> so that
> 
> $$p'(x) = q(x) + (x - \alpha) q'(x).$$
> 
> Since $(x - \alpha) \mid p'(x)$, substituting $x = \alpha$ yields
> 
> $$0 = p'(\alpha) = q(\alpha).$$
> 
> Thus, $(x - \alpha) \mid q(x)$, and we conclude that
> 
> $$p(x) = (x-\alpha)q(x) = (x - \alpha)^2 r(x)$$
> 
> for some $r(x) \in F[x]$. Therefore, $p(x)$ has a repeated root, and is not separable.

---

**Corollary.**  
Let $F$ be a field of characteristic zero. Then every irreducible polynomial $f(x) \in F[x] \setminus F$ is separable.

> Since $f(x)$ is irreducible, any common factor of $f(x)$ and its formal derivative $f'(x)$ must be either a unit or a scalar multiple of $f(x)$. 
> 
> Suppose the contrary that $f$ is not separable, then we have $\gcd(f, f') \neq 1$, so $f \mid f'$. Since $\deg f' < \deg f$, the only possibility is that 
> $f' = 0$. However, since $F$ has characterstic 0, and $f$ is a non-constant polynomial, this is impossible. 

---

**Corollary.**  
Let $F$ be a field of characteristic $p > 0$, and let $f(x) \in F[x] \setminus F$ be an irreducible polynomial.
Then there exists an irreducible and separable polynomial $g(x) \in F[x]$ and an integer $k \ge 0$ such that 

$$f(x) = g\left(x^{p^k}\right).$$

> **Proof.**  
> If $f(x)$ is separable, the result holds with $k = 0$ and $g(x) = f(x)$.
> 
> Otherwise, suppose $f(x)$ is not separable. Then, as shown in the earlier theorem, we must have $f'(x) = 0$.  
> Writing
> 
> $$f(x) = \sum_{i = 0}^n a_i x^i,\quad f'(x) = \sum_{i = 1}^n i a_i x^{i-1},$$
> 
> we see that $f'(x) = 0$ if and only if $i a_i = 0$ for all $i$, which implies $a_i = 0$ unless $p \mid i$.
> Therefore, all non-zero monomials in $f(x)$ have degrees divisible by $p$, and we can write
> 
> $$f(x) = g_1(x^p)$$
> 
> for some $g_1(x) \in F[x]$.
> 
> Since $f(x)$ is irreducible, $g_1(x)$ must also be irreducible: otherwise, if $g_1(x) = h_1(x) h_2(x)$, then $f(x) = h_1(x^p) h_2(x^p)$
> would be a factorization of $f(x)$ in $F[x]$, contradicting its irreducibility.
> 
> Now, $\deg g_1 < \deg f$, so by strong induction on the degree of $f$, we can write
> 
> $$g_1(x) = g(x^{p^k})$$
> 
> for some irreducible and separable $g(x) \in F[x]$ and some $k \ge 0$. Then,
> 
> $$f(x) = g_1(x^p) = g\left(x^{p^{k+1}}\right).$$
> 
> This completes the proof.


