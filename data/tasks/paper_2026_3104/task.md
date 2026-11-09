# Problem

## Setup

Let \((M,g)\) be a compact, connected, \(m\)-dimensional Riemannian manifold without boundary, and let \(\nu=\operatorname{vol}/\operatorname{vol}(M)\) be normalized volume. Let \(k_t(x,y)\), \(t>0\), be the normalized heat kernel for the convention \(\partial_tu=\Delta u\). It is symmetric, strictly positive, normalized by \(\int_M k_t(x,y)\,d\nu(y)=1\), and satisfies
\[
k_{t+s}(x,y)=\int_M k_t(x,z)k_s(z,y)\,d\nu(z).
\]

Fix finitely many points \(x_1,\ldots,x_n\in M\) and weights \(w_i\ge0\) with \(\sum_iw_i=1\). For \(t>0\), define
\[
s_t(x,y)=\frac{k_{2t}(x,y)}{\sqrt{k_{2t}(x,x)k_{2t}(y,y)}},\qquad
 gESS_w(t)=\left[\sum_{i,j=1}^nw_iw_j s_t(x_i,x_j)\right]^{-1},
\]
and define the ordinary effective sample size by \(ESS(w)=(\sum_iw_i^2)^{-1}\).

## Task

Prove the following integrated theorem. For every \(t>0\),
\[
1\le gESS_w(t)\le ESS(w).
\]
The value of \(gESS_w(t)\) is unchanged if any collection of equal-location atoms is merged into one atom carrying the sum of their weights (equivalently, it is invariant under splitting a weight among duplicate labels). If the distinct support locations after merging are \(z_1,\ldots,z_r\) with total masses \(\alpha_a\), then
\[
\lim_{t\downarrow0}gESS_w(t)=\left(\sum_{a=1}^r\alpha_a^2\right)^{-1},
\]
which equals \(ESS(w)\) when the original locations are all distinct, and
\[
\lim_{t\to\infty}gESS_w(t)=1.
\]
