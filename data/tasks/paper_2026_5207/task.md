# Problem

## Setup

Let \(\tau>0\), let \(d\ge2\) be an integer, and set
\[
k(x,y)=\exp\!\left(-\frac{\|x-y\|^2}{\tau}\right).
\]
For a nonnegative Borel measure \(\mu\), write
\[
(k*\mu)(x)=\int k(x,y)\,d\mu(y).
\]
For Borel probability measures \(p,q\) on \(\mathbb R^d\), define
\[
p_\tau(x)=\int k(x,y)\,dp(y),\qquad
q_\tau(x)=\int k(x,y)\,dq(y).
\]
Define the affinities
\[
A^+(x,y)=\frac{k(x,y)}{\sqrt{q_\tau(y)p_\tau(x)}},
\qquad
A^-(x,y)=\frac{k(x,y)}{\sqrt{q_\tau(x)q_\tau(y)}},
\]
their row integrals
\[
s^+(x)=\int A^+(x,y)\,dp(y),\qquad
s^-(x)=\int A^-(x,y)\,dq(y),
\]
and the cross-weights
\[
W^+(x,y)=s^-(x)A^+(x,y),\qquad
W^-(x,y)=s^+(x)A^-(x,y).
\]
The Gaussian proxy velocity is
\[
V(x)=\int W^+(x,y)y\,dp(y)-\int W^-(x,y)y\,dq(y).
\]

Also set
\[
d\widetilde p(y)=q_\tau(y)^{-1/2}dp(y),\qquad
d\widetilde q(y)=q_\tau(y)^{-1/2}dq(y),
\]
\[
Z(x)=s^+(x)s^-(x),
\qquad
\Phi(x)=\frac{\tau}{2}\left[\log (k*\widetilde p)(x)-\log (k*\widetilde q)(x)\right].
\]
A \(C^2\) scalar-potential representation of \(V\) means an identity
\[
V=\nabla U\quad\text{on all of }\mathbb R^d
\]
for some \(U\in C^2(\mathbb R^d;\mathbb R)\). Such a representation is a necessary spatial condition for a smooth pointwise Wasserstein-gradient-flow velocity.

## Task

Prove the following integrated claim.

If \(V\) admits a \(C^2\) scalar-potential representation, then for every \(x\in\mathbb R^d\) and every \(i,j\in\{1,\ldots,d\}\),
\[
\partial_i Z(x)\,\partial_j\Phi(x)=\partial_j Z(x)\,\partial_i\Phi(x).
\]
Moreover, in \(d=2\), let \(p=\delta_{(1,0)}\) and \(q=\delta_{(-1,0)}\). Show that this condition fails at \(x=(0,1)\). Consequently, this velocity admits no such scalar-potential representation and cannot be a smooth pointwise Wasserstein-gradient-flow velocity.
