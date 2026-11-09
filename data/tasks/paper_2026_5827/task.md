# Problem

## Setup

Fix integers \(n,d\ge1\). Let \(X\sim\mathcal N(0,I_n)\), let \(\widetilde x=(x,1)\in\mathbb R^{n+1}\), and write \(\widetilde X=(X,1)\). Define
\[
\mathcal H_{\rm in}=L^2(P_X;\mathbb R),\qquad
\mathcal Y=\mathbb R^d,\qquad
\mathcal H=L^2(P_X;\mathcal Y),
\]
with their expectation inner products. Functions are identified up to equality almost everywhere. A state is a finite tuple \(\Phi=(f_1,\ldots,f_N)\in\mathcal H^N\), equipped with the product-Hilbert norm.

Let \(E\) be a nonnegative capacity on finite states. Suppose \(E((f))=\|f\|_{\mathcal H}\), and suppose there are a continuous strictly monotone function \(g:[0,\infty)\to\mathbb R\) and a function \(h\), defined on all finite sums of values of \(g\), such that
\[
E(f_1,\ldots,f_N)=h\!\left(\sum_{k=1}^N g(\|f_k\|_{\mathcal H})\right).
\]
Assume that replacing one coordinate \(f\) by \(M\) copies of \(f/M\) leaves capacity unchanged, for every integer \(M\ge1\). Set \(E(\varnothing)=0\).

A capacity cost \(J[\Phi]\) is defined on positive-capacity, capacity-nonincreasing \(C^1\) paths. It is additive under concatenation, vanishes on constant paths, is magnitude neutral in the sense that \(J[a\Phi]=J[\Phi]\) for \(a>0\), and has infinitesimal increment
\[
dJ=-\xi(\Phi(t))\,dE(\Phi(t)),\qquad \xi>0.
\]
The density is continuous on each fixed-active-support stratum, where the active support of a state is \(\{k:f_k\ne0\}\). Let \(c(\Phi)=\xi(\Phi)E(\Phi)\). Assume that \(c\) is unchanged along paths preserving active support and has a uniform lower bound \(c_{\min}>0\). The cost has an extinction barrier: with the positive initial state fixed, it diverges when terminal capacity tends to zero. Derivatives and path integrals involving capacity are understood almost everywhere, and all path densities are measurable.

For a discrete pruning or merging step, the rate is held at \(c(\Phi_a)\) throughout the continuous pre-deletion deformation. For a positive-capacity deformation \(\Phi(t)\), its geometric projection cost is defined separately by
\[
J_{\rm proj}[\Phi]
=\int_0^1\frac{c(\Phi_a)\|\dot\Phi(t)\|_{\mathcal H^N}}{E(\Phi(t))}\,dt.
\]
Such a geometric path need not have nonincreasing capacity.

Let \(\Psi:\mathbb R\to\mathbb R\) be nonzero and positively homogeneous of degree one: \(\Psi(az)=a\Psi(z)\) for \(a\ge0\). The realizable neurons are
\[
\mathcal N=\left\{x\mapsto w_{\rm out}\Psi(\widetilde w_{\rm in}^{\top}\widetilde x):
\widetilde w_{\rm in}\in\mathbb R^{n+1},\ w_{\rm out}\in\mathcal Y\right\}\subset\mathcal H.
\]
Define the scalar-activation kernel
\[
K(u,w)=\mathbb E\!\left[\Psi(u^\top\widetilde X)\Psi(w^\top\widetilde X)\right].
\]

In a pruning step, \(\widetilde\Phi_b\) is obtained by replacing one chosen coordinate of \(\Phi_a\) by zero, and \(\Phi_b\) is obtained by deleting that coordinate. In a merging step involving two distinct coordinates \(i,j\), choose a nonzero parent \(f_p\in\mathcal N\). Replace both child coordinates by \(f_p\) to obtain \(\widetilde\Phi_b\in\mathcal H^N\), and delete one of these two identical coordinates to obtain \(\Phi_b\in\mathcal H^{N-1}\). All other coordinates remain unchanged. In either case use the straight path
\[
\Phi(t)=(1-t)\Phi_a+t\widetilde\Phi_b,\qquad 0\le t\le1,
\]
and write \(J_{\rm proj}(\Phi_a,\Phi_b)\) for its geometric projection cost.

For a merge, put \(R=\sum_{k\notin\{i,j\}}\|f_k\|_{\mathcal H}\). An optimal merge parent means an attained minimizer, over nonzero \(p\in\mathcal N\), of
\[
\frac{\sqrt{\|f_i-p\|_{\mathcal H}^2+\|f_j-p\|_{\mathcal H}^2}}
{R+\|p\|_{\mathcal H}}.
\]
For prescribed magnitude \(s>0\), an optimal parent instead minimizes the same objective over \(p\in\mathcal N\) with \(\|p\|_{\mathcal H}=s\).

## Task

Prove the following integrated theorem.

First,
\[
E(\Phi)=\sum_k\|f_k\|_{\mathcal H},\qquad c(a\Phi)=c(\Phi)\quad(a>0),
\]
and every capacity-cost path obeys
\[
J[\Phi]=\int_0^1-c(\Phi(t))\frac{\dot E(\Phi(t))}{E(\Phi(t))}\,dt.
\]

For a straight pruning or merging path, let
\[
D=\|\Phi_a-\widetilde\Phi_b\|_{\mathcal H^N}.
\]
Whenever \(E(\Phi(t))\ge E(\Phi_b)>0\) for all \(t\in[0,1]\), show that
\[
J_{\rm proj}(\Phi_a,\Phi_b)\le\frac{c(\Phi_a)D}{E(\Phi_b)}.
\]

Moreover, for two nonzero realizable children, define
\[
\rho_{ij}=\frac{\langle f_i,f_j\rangle_{\mathcal H}}{\|f_i\|_{\mathcal H}\|f_j\|_{\mathcal H}}.
\]
Show that there is a threshold \(\rho^*(f_i,f_j)\in(0,1)\), independent of the unchanged coordinates, such that \(\rho_{ij}\ge\rho^*\) guarantees the preceding capacity condition along the whole straight merge path for every attained optimal merge parent.

Finally, write the children as
\[
f_k(x)=w_{\rm out}^k\Psi((\widetilde w_{\rm in}^k)^\top\widetilde x),\qquad k\in\{i,j\}.
\]
For any prescribed magnitude \(s>0\), prove that an optimal parent exists and can be written as
\[
\psi^*(x)=s\,\frac{\Psi((u^*)^\top\widetilde x)\,v^*}{\sqrt{K(u^*,u^*)}},
\]
where \(\|u^*\|=\|v^*\|=1\), and \(u^*\) attains the maximum of
\[
\frac{\left\|\sum_{k\in\{i,j\}}K(u,\widetilde w_{\rm in}^k)w_{\rm out}^k\right\|}
{\sqrt{K(u,u)}}
\]
over \(u\in\mathbb R^{n+1}\) with \(\|u\|=1\) and \(K(u,u)>0\). When the vector sum at \(u^*\) is nonzero, \(v^*\) is its normalization; if the maximum alignment is zero, any feasible unit \(u^*\) and any unit \(v^*\) are optimal.
