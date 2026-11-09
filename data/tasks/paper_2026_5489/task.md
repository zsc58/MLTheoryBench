# Problem

## Setup

Let \(d,n,L\) be integers with \(d\ge3\), \(n\ge1\), and \(L\ge1\). Let \(X\in\mathbb R^{d\times n}\) be random with unit-norm columns. Assume that its law is invariant under left multiplication by every orthogonal matrix in \(O(d)\), and that
\[
\mathbb E\big[\lambda_d(XX^{\mathsf T})^{-1}\big]<\infty,
\]
where \(\lambda_d\) denotes the smallest eigenvalue and the reciprocal of zero is interpreted as \(+\infty\). Almost surely, let the largest eigenvalue of \(XX^{\mathsf T}\) have multiplicity \(r(X)\in\{1,\ldots,d-1\}\); this multiplicity may depend on \(X\). Let \(V(X)\) be its eigenspace and \(P_X\) the orthogonal projector onto \(V(X)\).

Let \(a\in\mathbb S^{d-1}\) be independent of \(X\) and uniform on the unit sphere. All expectations below are over this fixed joint law.

Embed the data and query as
\[
E^{(0)}=E_0(X,a)=\operatorname{diag}(X,a)\in\mathbb R^{2d\times(n+1)}.
\]
For matrices \(W,V\in\mathbb R^{2d\times2d}\), partitioned into \(d\times d\) blocks, define
\[
\operatorname{TF}(E;W,V)=\operatorname{LN}\!\left(E+VEE^{\mathsf T}WE\right),
\]
where \(\operatorname{LN}\) divides each nonzero token column by its Euclidean norm. Using the same parameters in every loop, set
\[
E^{(\ell+1)}=\operatorname{TF}(E^{(\ell)};W,V),\qquad 0\le\ell<L,
\]
and define the prediction by extraction of the lower query block:
\[
u_L(X,a;W,V)=E^{(L)}_{d+1:2d,n+1}\in\mathbb R^d.
\]
The model is evaluated where all its normalizations are defined. Its prediction is not separately normalized after extracting this block.

Train by population gradient descent on
\[
\mathcal L(W,V)=\mathbb E\,\bigl\|(I-P_X)u_L(X,a;W,V)\bigr\|^2,
\]
using simultaneous updates
\[
W^{(t+1)}=W^{(t)}-\eta\nabla_W\mathcal L(W^{(t)},V^{(t)}),\qquad
V^{(t+1)}=V^{(t)}-\eta\nabla_V\mathcal L(W^{(t)},V^{(t)}).
\]
The gradients are taken with respect to all matrix entries, with the Frobenius inner product. Initialize
\[
W^{(0)}=0,\qquad V_{21}^{(0)}=I_d,
\]
with every other block of \(V^{(0)}\) zero. Fix \(0<\eta\le d/(2Ln)\).

For \(\rho\ge0\), define
\[
R_L(\rho)=\mathbb E\,\left\|(I-P_X)\frac{(I+\rho XX^{\mathsf T})^La}{\|(I+\rho XX^{\mathsf T})^La\|}\right\|^2,
\]
\[
R_L(\infty)=\mathbb E\,\left\|(I-P_X)\frac{(XX^{\mathsf T})^La}{\|(XX^{\mathsf T})^La\|}\right\|^2.
\]
Write
\[
\Upsilon_1=\lim_{\rho\to\infty}-\rho^2R_L'(\rho),
\]
with existence of the derivatives and of this finite, strictly positive limit included among the conclusions to prove. At \(\rho=0\), \(R_L'(0)\) denotes the right derivative.

## Task

Prove that the population gradients and every gradient-descent iterate are well defined, that \(0<\Upsilon_1<\infty\), and that every iterate remains on the sparse manifold
\[
W_{12}^{(t)}=w_tI_d,\qquad V_{21}^{(t)}=v_tI_d,
\]
with all other blocks zero. Here \(w_0=0\) and \(v_0=1\). Writing \(\rho_t=w_tv_t\), prove the exact recursions
\[
w_{t+1}=w_t-\frac{\eta v_t}{d}R_L'(\rho_t),\qquad
v_{t+1}=v_t-\frac{\eta w_t}{d}R_L'(\rho_t).
\]
Moreover, prove
\[
\rho_t\to\infty,\qquad \frac{w_t}{v_t}\to1,
\]
\[
\rho_t\sim\left(\frac{4\eta\Upsilon_1}{d}t\right)^{1/2},\qquad
w_t,v_t=\Theta\!\left(\left(\frac{\eta\Upsilon_1t}{d}\right)^{1/4}\right),
\]
and
\[
R_L(\infty)>0,\qquad
\mathcal L(W^{(t)},V^{(t)})-R_L(\infty)
=O\!\left(\sqrt{\frac{d\Upsilon_1}{\eta t}}\right)
=O(t^{-1/2}).
\]
These asymptotics concern \(t\to\infty\) for fixed dimensions, loop count, learning rate, and data law; \(\Upsilon_1\) is determined by \(L\) and that law.

Finally, for every fixed matrix \(X\in\mathbb R^{d\times n}\) with unit-norm columns and positive definite \(XX^{\mathsf T}\), and every fixed \(a\in\mathbb S^{d-1}\), prove that the learned prediction converges to
\[
\frac{(XX^{\mathsf T})^La}{\|(XX^{\mathsf T})^La\|},
\]
the normalized \(L\)-step power-method iterate.
