# Problem

## Setup

Fix \(0<\delta<T<\infty\), \(0\le M<\infty\), and a probability law \(\mu_0\) supported on \([-M,M]\). Let
\[
X_t=X_0+\sqrt t\,G,\qquad X_0\sim\mu_0,\quad G\sim N(0,1),
\]
where \(X_0\) and \(G\) are independent. Let \(p_t\) be the density of \(X_t\) for \(t\in[\delta,T]\), and define
\[
D_t(x)=\mathbb E[X_0\mid X_t=x],\qquad s_t(x)=\partial_x\log p_t(x)=\frac{D_t(x)-x}{t},
\]
using the smooth version of the conditional mean determined by the positive Gaussian-convolution density.

Write \(L=T-\delta\). On a common probability space, let \(V\sim p_T\) be independent of a standard Brownian motion \((B_u)_{0\le u\le L}\). The reverse SDE driven by a field \(v_t\) is
\[
dZ^v_u=v_{T-u}(Z^v_u)\,du+dB_u,\qquad Z^v_0=V,\qquad 0\le u\le L.
\]
Denote the solutions driven by \(s\) and \(\widehat s\) by \(U\) and \(Z\), respectively.

For a descending grid \(T=t_K>\cdots>t_0=\delta\), put \(h_k=t_{k+1}-t_k\). The Euler chain driven by \(\widehat s\) starts from \(Y_K=V\) and uses
\[
\xi_k=\frac{B_{T-t_k}-B_{T-t_{k+1}}}{\sqrt{h_k}},\qquad
Y_k=Y_{k+1}+h_k\widehat s_{t_{k+1}}(Y_{k+1})+\sqrt{h_k}\,\xi_k.
\]
Within each grid these noises are independent standard Gaussians, independent of \(V\). All grids and the SDEs use the same \(V,B\).

## Task

Prove the following theorem. For every \(\varepsilon,\eta,\lambda,\alpha>0\), there exists a smooth score field \(\widehat s:[\delta,T]\times\mathbb R\to\mathbb R\) such that:

1. \(\sup_{t\in[\delta,T]}\mathbb E_{X\sim p_t}|\widehat s_t(X)-s_t(X)|^2\le\varepsilon\).
2. The learned reverse SDE has a unique nonexplosive strong solution, has moments of every positive integer order uniformly over \([0,L]\), and satisfies
\[
\operatorname{TV}\!\left(\mathcal L((Z_u)_{0\le u\le L}),\mathcal L((U_u)_{0\le u\le L})\right)\le\eta.
\]
3. For \(K=2^m\to\infty\), use the grids
\[
t_k^{(K)}=\delta\exp\!\left(\frac{k}{K}\log\frac{T}{\delta}\right),\qquad k=0,\ldots,K.
\]
Under the coupling in the setup, the Euler endpoints converge in probability to \(Z_L\), but for every \(q>0\),
\[
\mathbb E|Y_0^{(K)}|^q\longrightarrow\infty.
\]
Consequently the endpoint laws converge weakly to \(\mathcal L(Z_L)\), while for every \(p\ge1\) and every fixed \(\nu\in\mathcal P_p(\mathbb R)\),
\[
W_p\bigl(\mathcal L(Y_0^{(K)}),\nu\bigr)\longrightarrow\infty.
\]

Here path laws are measures on \(C([0,L],\mathbb R)\) with its Borel sigma-algebra, and \(\operatorname{TV}(P,Q)=\sup_A|P(A)-Q(A)|\). The set \(\mathcal P_p(\mathbb R)\) consists of probability laws with finite \(p\)-th moment. For probability laws \(P,Q\), use the possibly extended-valued definition
\[
W_p(P,Q)=\inf_{\pi\in\Pi(P,Q)}\left(\int|x-y|^p\,\pi(dx,dy)\right)^{1/p},
\]
where \(\Pi(P,Q)\) is the set of their couplings; on \(\mathcal P_p(\mathbb R)\) this is the usual \(p\)-Wasserstein distance.
