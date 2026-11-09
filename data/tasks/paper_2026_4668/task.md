# Problem

## Setup

Let \(\mathcal Z\) and \(\mathcal W\) be measurable data and hypothesis-parameter spaces. Let \(\mathcal T\) be a measurable space of transformations of \(\mathcal Z\), with jointly measurable evaluation \((g,z)\mapsto gz\). Let \(D\) be a probability distribution on \(\mathcal Z\), let \(D_G\) be a probability distribution on \(\mathcal T\), and let \(\ell:\mathcal W\times\mathcal Z\to[0,\infty)\) be measurable. Fix integers \(m,n\ge1\) and a constant \(R>0\).

Draw \(S=(Z_1,\ldots,Z_m)\sim D^m\). Independently draw \(E=(G_1,\ldots,G_n)\sim D_G^n\). Given \((S,E)\), a randomized learner outputs \(W\sim P_{W\mid S,E}\), where \(P_{W\mid S,E}\) is a measurable probability kernel. The same sampled transformations \(G_1,\ldots,G_n\) are used for all training examples.

For an integrable real random variable \(X\), write
\[
\psi_X(\lambda)=\log\mathbb E\exp(\lambda(X-\mathbb EX)).
\]
We call \(X\) \(R\)-sub-Gaussian when \(\psi_X(\lambda)\le\lambda^2R^2/2\) for every \(\lambda\in\mathbb R\). Assume:

1. For every fixed \(w\in\mathcal W\), \(\ell(w,Z')\) is \(R\)-sub-Gaussian when \(Z'\sim Q:=D_G\circ D\), where \(D_G\circ D\) is the law of \(GZ\) for independent \(G\sim D_G\) and \(Z\sim D\).
2. For every fixed \(w\in\mathcal W\) and \(z\in\mathcal Z\), \(\ell(w,Gz)\) is \(R\)-sub-Gaussian for \(G\sim D_G\).

Define
\[
L_D(w)=\mathbb E_{Z\sim D}\ell(w,Z),\qquad
L_{S,E}(w)=\frac1{mn}\sum_{i=1}^m\sum_{j=1}^n\ell(w,G_jZ_i),
\]
\[
\ell_G(w,z)=\mathbb E_{G\sim D_G}\ell(w,Gz),\qquad
L_Q(w)=\mathbb E_{Z'\sim Q}\ell(w,Z')=\mathbb E_{Z\sim D}\ell_G(w,Z).
\]
Let \(H=L_D(W)-L_{S,E}(W)\). Assume that \(\mathbb E H^+<\infty\) or \(\mathbb E H^-<\infty\), where \(x^+=\max\{x,0\}\) and \(x^-=\max\{-x,0\}\). Thus the signed expectation
\[
\operatorname{gen}(D,P_{W\mid S,E})=\mathbb E_{S,E,W}H
\]
is defined, possibly as an extended real number.

All logarithms are natural. For probability measures \(\mu,\nu\) on the same measurable space, use
\[
D_{\rm KL}(\mu\Vert\nu)=
\begin{cases}
\displaystyle\int\log\!\left(\frac{d\mu}{d\nu}\right)\,d\mu,&\mu\ll\nu,\\
+\infty,&\text{otherwise}.
\end{cases}
\]
For random variables \(U,V\), let
\[
I(U;V)=D_{\rm KL}(P_{U,V}\Vert P_U\otimes P_V).
\]
The loss subscripts below are labels and do not change the underlying joint law. In particular,
\[
I_{\ell_G}(Z_i;W)=D_{\rm KL}(P_{Z_i,W}\Vert D\otimes P_W).
\]
For each \(i,j\), define
\[
I_{\ell}^{z}(G_j;W)
=D_{\rm KL}\!\left(P_{G_j,W\mid Z_i=z}\,\middle\Vert\,D_G\otimes P_{W\mid Z_i=z}\right).
\]
Here the conditioning is only on \(Z_i=z\); the other training examples and the remaining augmentation variables are marginalized. Assume that these conditional laws admit measurable probability-kernel versions and that the displayed conditional relative entropy is a measurable function of \(z\). Versions differing on \(D\)-null sets are identified. The notation \(I_{\ell}^{Z_i}(G_j;W)\) denotes this function evaluated at the random example \(Z_i\).

## Task

Prove the following integrated theorem, with the inequality interpreted in the extended nonnegative real numbers:
\[
\left|\operatorname{gen}(D,P_{W\mid S,E})\right|
\le R\left[\sqrt{2D_{\rm KL}(D\Vert D_G\circ D)}
+\frac1m\sum_{i=1}^m\sqrt{2I_{\ell_G}(Z_i;W)}
+\frac1{mn}\mathbb E_S\sum_{i=1}^m\sum_{j=1}^n\sqrt{2I_{\ell}^{Z_i}(G_j;W)}\right].
\]
