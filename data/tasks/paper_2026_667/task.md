# Problem

## Setup

Fix \(1\le p\le2\) and \(\sigma>0\). Let
\[
\Omega=\{(b,d)\in\mathbb R^2:b<d\},\qquad
\delta(x)=\operatorname{dist}(x,\partial\Omega),
\]
where distance is Euclidean. Let \(\mathcal M^p(\Omega)\) consist of the nonnegative Radon measures \(\mu\) on \(\Omega\) satisfying
\[
\int_\Omega\delta(x)^p\,d\mu(x)<\infty.
\]
Persistence diagrams are the point-measure subclass; total mass need not be finite.

For either \(U=\Omega\) or \(U=(0,\infty)\), put
\[
E_U=(\overline U\times\overline U)\setminus(\partial U\times\partial U).
\]
For nonnegative Radon measures \(\eta,\zeta\) on \(U\), define
\[
F_p(\eta,\zeta)
=\left(\inf_\gamma\int_{E_U}\|x-y\|_2^p\,d\gamma(x,y)\right)^{1/p},
\]
where \(\gamma\) ranges over nonnegative Radon measures on \(E_U\) such that, for all Borel \(A,B\subset U\),
\[
\gamma\bigl((A\times\overline U)\cap E_U\bigr)=\eta(A),\qquad
\gamma\bigl((\overline U\times B)\cap E_U\bigr)=\zeta(B).
\]
Thus mass may be sent to or received from the boundary. Radon finiteness is required on compact subsets of \(E_U\), not across the removed boundary-boundary set. For \(U=(0,\infty)\), the norm in the cost is absolute value and \(\partial U=\{0\}\). The infimum is interpreted as an extended nonnegative value, with \(\inf\varnothing=+\infty\).

For \(t\in\mathbb R\), define the ray
\[
G_t=\left\{(t,t)+\frac r{\sqrt2}(-1,1):r\ge0\right\}
\]
and the map \(\pi_t:\Omega\to G_t\) by
\[
\pi_t(b,d)=
\begin{cases}
(t,t)+\dfrac{d-b}{2}(-1,1),&b\le t\le d,\\
(t,t),&\text{otherwise}.
\end{cases}
\]
Identify \(G_t\setminus\{(t,t)\}\) with \((0,\infty)\) using its arclength coordinate \(r\).

For \(\mu\in\mathcal M^p(\Omega)\), set
\[
d\widetilde\mu(x)=\delta(x)^{-1}\,d\mu(x),\qquad
\mu_t=(\pi_t\#\widetilde\mu)|_{G_t\setminus\{(t,t)\}},
\]
where \(\#\) denotes pushforward. In particular, all mass at the ray's base point is discarded. Define
\[
D_p(\mu,\nu)=2^{-1/2}
\left(\int_{\mathbb R}F_p(\mu_t,\nu_t)^p\,dt\right)^{1/p},
\]
where the integral is a Lebesgue integral of an extended nonnegative function.

## Task

Prove that \(D_p^p\) is a finite-valued conditionally negative definite function on \(\mathcal M^p(\Omega)\): for every finite collection \(\mu_1,\ldots,\mu_n\in\mathcal M^p(\Omega)\) and real coefficients \(a_1,\ldots,a_n\) with \(\sum_i a_i=0\),
\[
\sum_{i,j=1}^n a_i a_j D_p(\mu_i,\mu_j)^p\le0.
\]
Consequently, prove that
\[
K_\sigma(\mu,\nu)=\exp\!\left(-\frac{D_p(\mu,\nu)^p}{\sigma^2}\right)
\]
is a positive-semidefinite kernel on \(\mathcal M^p(\Omega)\).
