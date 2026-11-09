# Problem

## Setup

Let \(H\) be a finite-dimensional Euclidean space, let \(\mathcal Z\subset\mathbb R^n\) be a latent parameter space, and let \(\mathcal A=\{1,\ldots,q\}\) be a finite output alphabet, where \(n\ge1\) and \(q\ge2\). Write
\[
\Delta^{q-1}=\left\{u\in\mathbb R^q:u_j\ge0\text{ for all }j,\ \sum_{j=1}^q u_j=1\right\}.
\]

Fix a law for a latent variable \(Z\in\mathcal Z\). For every \(z\in\mathcal Z\), the model specifies a conditional law \(P_z\) for observations \(X_1,X_2,\ldots\in\mathcal A\). Under \(P_z\), these observations form a time-homogeneous Markov chain with transition probabilities \(Q_z(a,j)\). Expectations \(\mathbb E_z\) use this specified conditional law, and \(\mathbb E\) uses the joint law obtained by first drawing \(Z\) and then the observations under \(P_Z\).

For each integer \(t\ge1\), let \(h_t\in H\) be a hidden state that is a function of the observed prefix \((X_1,\ldots,X_t)\). Let
\[
\mu_t(z,a)=\mathbb E_z[h_t\mid X_t=a]
\]
be specified finite, measurable versions of the conditional means. At zero-probability conditioning events, any versions used in this setup are fixed as part of the model. Assume
\[
\mathbb E\|h_t-\mu_t(Z,X_t)\|^2\longrightarrow0.
\]

Let \(U\subseteq\mathcal Z\) contain an interior point \(z_0\) in \(\mathbb R^n\), and fix an anchor \(a_\star\in\mathcal A\). For \(z\in U\), set
\[
m_t(z)=\mu_t(z,a_\star),
\]
and assume that the finite limit
\[
m(z)=\lim_{t\to\infty}m_t(z)\in H
\]
exists for every fixed \(z\in U\).

Fix \(K\ge2\) vectors \(v_1,\ldots,v_K\in H\) in the centered gauge \(\sum_{i=1}^K v_i=0\). Fix \(b\in H\), and define
\[
V=\operatorname{span}\{v_2-v_1,\ldots,v_K-v_1\},\qquad S=b+V,\qquad k_\star=\dim V\ge1.
\]

Define the target prediction map by
\[
g(z)=\bigl(Q_z(a_\star,j)\bigr)_{j=1}^q\in\Delta^{q-1},\qquad z\in\mathcal Z.
\]
Suppose \(g\) is \(C^1\) on a neighborhood of \(z_0\). Define
\[
d_0=\operatorname{rank}Dg(z_0),\qquad E=(\ker Dg(z_0))^\perp,
\]
and let \(s_0>0\) be the smallest nonzero singular value of \(Dg(z_0)\). Assume \(d_0>0\).

Fix \(r_0>0\) such that \(B(z_0,r_0)\subseteq\mathcal Z\), where \(B\) denotes a Euclidean open ball. Suppose there are finite constants \(M\ge0\), \(L>0\), and \(\delta\ge0\), and a decoder \(D:H\to\Delta^{q-1}\), such that for all \(z,z'\in U\):
\[
\|m(z)-m(z')\|\le M,
\]
\[
\|D(m(z))-D(m(z'))\|_2\le L\|m(z)-m(z')\|,
\]
and
\[
\|D(m(z))-g(z)\|_2\le\delta.
\]
Define
\[
\operatorname{dist}(x,S)=\inf_{y\in S}\|x-y\|,\qquad
\varepsilon=\sup_{z\in U}\operatorname{dist}(m(z),S).
\]

## Task

Prove that there exists \(r_{\rm loc}\in(0,r_0]\) such that, with \(c=s_0/2\), for every \(0<\rho<r_{\rm loc}\) satisfying \(c\rho>2\delta\),
\[
\varepsilon\ge\frac12\left[
\left(\frac{c\rho-2\delta}{L}\right)^2-
\left(\frac{2M}{(r_{\rm loc}/\rho)^{d_0/k_\star}-1}\right)^2
\right]_+^{1/2},
\]
where \([x]_+=\max\{x,0\}\).
