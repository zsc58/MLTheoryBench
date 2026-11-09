# Reference Proof

## Proof Structure

Use equivariance to obtain one common target-row function that is invariant in the remaining rows. For general input dimension, approximate that function by a polynomial, average over remaining-row permutations, and represent its invariant coefficient polynomials through sums of row monomials. For scalar inputs, use an exact power-sum encoding and extend the resulting continuous outer map from its compact encoded domain. Finally verify equivariance by an explicit index calculation.

## Standard Background Used

Only the following independently standard results are used without deriving their full proofs.

1. **Real Stone-Weierstrass theorem.** On a compact Hausdorff space, a real subalgebra of continuous functions that contains the constants and separates points is uniformly dense in the continuous real functions. Restricted coordinate polynomials have these properties on every compact subset of a finite-dimensional Euclidean space.
2. **Bounded Tietze extension theorem.** A bounded continuous real function on a closed subset of a metric space has a continuous real-valued extension to the whole space. Below, the subset is compact and hence closed, and the function is continuous on that compact subset and hence bounded.

No external sum-representation theorem is assumed. Its relevant polynomial and power-sum mechanisms are established below.

## Complete Proof

If $K=\varnothing$, choose $q=r=1$, the unique maps with empty domains for $\phi$ and $\rho_1$, and a constant continuous $\rho_2$. All claims are vacuous except the uniform-error value, which is zero by the stated convention. Hence assume $K\ne\varnothing$.

Write $n=m-1$ and $d=k_1$, and define
\[
F(x,Y)=g_1(x,Y_1,\ldots,Y_n),\qquad (x,Y)\in K\times K^n.
\]
For every permutation $Q$ of the $n$ remaining rows, equivariance under the block permutation fixing the first row gives
\[
F(x,QY)=F(x,Y).
\]
Let $T_i$ exchange rows $1$ and $i$, with $T_1$ the identity, and let $Y^{(i)}$ be the list of rows after the first row of $T_iX$. Then equivariance gives
\[
g_i(X)=g_1(T_iX)=F(X_i,Y^{(i)}).
\]
The list $Y^{(i)}$ consists precisely of the rows other than $X_i$. Its ordering does not matter. This proves both remaining-row symmetry and the existence of a single common target-row function, rather than separately choosing coordinate maps.

### General Input Dimension: Uniform Approximation

The compact space $K\times K^n$ is a subset of $\mathbb R^{md}$. Coordinate polynomials restricted to it contain constants and separate points, so Stone-Weierstrass provides a real polynomial $p(x,Y)$ with
\[
\sup_{(x,Y)\in K\times K^n}|F(x,Y)-p(x,Y)|<\varepsilon/2.
\]
Average over the finite remaining-row permutation group:
\[
R(x,Y)=\frac1{n!}\sum_{\sigma\in S_n}p(x,\sigma Y).
\]
Because the domain is preserved by these permutations and $F$ is invariant in $Y$,
\[
\sup_{K\times K^n}|F-R|<\varepsilon/2.
\]
Expand the polynomial in target-row monomials:
\[
R(x,Y)=\sum_{\beta\in B}x^\beta a_\beta(Y),
\]
where $B$ is finite and each coefficient $a_\beta$ is an invariant polynomial in the $n$ remaining rows. If $R$ is zero, take $B=\{0\}$ and $a_0=0$.

We now prove the required sum representation for these invariant coefficient polynomials. For a multiindex $\alpha\in\mathbb N_0^d$, write
\[
p_\alpha(Y)=\sum_{j=1}^nY_j^\alpha.
\]
For a list of multiindices, define
\[
T_{\alpha_1,\ldots,\alpha_t}(Y)
=\sum_{\substack{j_1,\ldots,j_t\in\{1,\ldots,n\}\\\text{pairwise distinct}}}
\prod_{\ell=1}^tY_{j_\ell}^{\alpha_\ell},
\qquad T_{\varnothing}=1.
\]
For $t\ge1$, multiplication by $p_{\alpha_t}$ separates the last row index into a new index or a collision with one of the previous distinct indices. Consequently,
\[
T_{\alpha_1,\ldots,\alpha_t}
=T_{\alpha_1,\ldots,\alpha_{t-1}}p_{\alpha_t}
-\sum_{s=1}^{t-1}
T_{\alpha_1,\ldots,\alpha_{s-1},\alpha_s+\alpha_t,\alpha_{s+1},\ldots,\alpha_{t-1}}.
\]
The sum is empty for $t=1$. Induction on $t$ therefore expresses every such $T$ as a polynomial in finitely many $p_\alpha$.

For any row monomial $\prod_{\ell=1}^nY_\ell^{\alpha_\ell}$, its permutation average is $T_{\alpha_1,\ldots,\alpha_n}/n!$. This remains true with zero or repeated multiindices: both sides count permutations with their multiplicities. An invariant polynomial equals its own permutation average, so it is a finite linear combination of these averaged monomials. Thus every $a_\beta$ is a polynomial in finitely many $p_\alpha$.

Choose $D$ at least the total degree of every remaining-row monomial occurring in the coefficient polynomials. All multiindices introduced by the recurrence have degree at most $D$. Set
\[
A=\{\alpha\in\mathbb N_0^d:|\alpha|\le D\},\qquad
q=|A|,\qquad \phi(y)=(y^\alpha)_{\alpha\in A}.
\]
There are polynomials $B_\beta:\mathbb R^q\to\mathbb R$ such that
\[
a_\beta(Y)=B_\beta\!\left(\sum_{j=1}^n\phi(Y_j)\right).
\]
Take $r=|B|$ and define
\[
\rho_2(z)=(B_\beta(z))_{\beta\in B},\qquad
\rho_1(x,u)=\sum_{\beta\in B}x^\beta u_\beta.
\]
These maps have exactly the required domains and are continuous; in particular, the outer maps are defined on their full stated latent-space domains. Their composition equals $R(x,Y)$.

Using the same maps for every coordinate gives
\[
\widetilde g_i(X)=R(X_i,Y^{(i)}),
\]
and hence
\[
\sup_{X\in K^m}\|g(X)-\widetilde g(X)\|_\infty
\le \sup_{(x,Y)\in K\times K^n}|F(x,Y)-R(x,Y)|
<\varepsilon/2<\varepsilon.
\]
All dimensions and maps are chosen after $g$ and $\varepsilon$ are fixed and work simultaneously for every input and every coordinate.

### Scalar Input: Exact Representation

Now let $d=1$. Set $q=r=n$,
\[
\phi(t)=(t,t^2,\ldots,t^n),\qquad \rho_2(z)=z.
\]
Let
\[
S=\{(y_1,\ldots,y_n)\in K^n:y_1\le\cdots\le y_n\},
\qquad E(y)=\sum_{j=1}^n\phi(y_j).
\]
The set $S$ is compact. We verify that $E$ is injective on it. If $p_a=\sum_jy_j^a$ and $e_\ell$ denotes the elementary symmetric polynomial of degree $\ell$, with $e_0=1$, then
\[
\ell e_\ell=\sum_{a=1}^\ell(-1)^{a-1}e_{\ell-a}p_a,
\qquad 1\le\ell\le n.
\]
These identities follow by differentiating the formal polynomial $\prod_j(1+y_jt)=\sum_\ell e_\ell t^\ell$ and comparing coefficients after using the formal expansion of $\sum_j y_j/(1+y_jt)$. Thus the first $n$ power sums recursively determine $e_1,\ldots,e_n$. They determine the polynomial
\[
\prod_{j=1}^n(u-y_j)=u^n-e_1u^{n-1}+\cdots+(-1)^ne_n,
\]
and therefore its root multiset, including multiplicities. Sorting determines a unique tuple. This proves injectivity, also when rows coincide or $n=1$.

Put $C=E(S)$. The continuous bijection $E:S\to C$ has a continuous inverse: a closed subset of compact $S$ has compact image, which is closed in the Hausdorff space $C$. Define
\[
H(x,z)=F(x,E^{-1}(z)),\qquad (x,z)\in K\times C.
\]
This is continuous. Every tuple in $K^n$ has a sorted representative with the same encoding, so remaining-row symmetry yields
\[
F(x,Y)=H\!\left(x,\sum_{j=1}^n\phi(Y_j)\right).
\]
The subset $K\times C$ is compact and hence closed in the metric space $K\times\mathbb R^n$, and $H$ is bounded there. The bounded Tietze extension theorem therefore gives a continuous
\[
\rho_1:K\times\mathbb R^n\to\mathbb R
\]
whose restriction is $H$. Together with the chosen $\phi$ and identity $\rho_2$, this represents all $g_i$ exactly. The uniform error is consequently zero.

### Equivariance of the Constructed Vector

Use the explicit convention $(PX)_i=X_{\pi(i)}$ for the row permutation induced by $P$. Then
\[
\begin{aligned}
\widetilde g_i(PX)
&=\rho_1\!\left(X_{\pi(i)},\rho_2\!\left(\sum_{j\ne i}\phi(X_{\pi(j)})\right)\right)\\
&=\rho_1\!\left(X_{\pi(i)},\rho_2\!\left(\sum_{\ell\ne\pi(i)}\phi(X_\ell)\right)\right)\\
&=\widetilde g_{\pi(i)}(X)=(P\widetilde g(X))_i.
\end{aligned}
\]
Thus the assembled vector is permutation preserving in both constructions.

## Source-Contract Clarification

The source writes the target function on an ambient Euclidean array space and evaluates it on a compact row domain. Using its compact restriction in the public task does not enlarge the substantive class: a continuous equivariant map on closed compact $K^m$ can be extended coordinatewise to the ambient Euclidean space by bounded Tietze extension and then averaged as
\[
G(Z)=\frac1{m!}\sum_P P^{-1}H(PZ).
\]
This agrees with $g$ on $K^m$, and the substitution $R=PQ$ gives $G(QZ)=QG(Z)$. No additional Gaussian-process or sampling hypothesis is needed for the representation theorem.
