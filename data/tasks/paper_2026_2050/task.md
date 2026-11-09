# Problem

## Setup

Let \(K\) and \(J\) be positive integers, let \(\lambda>0\), and let \(\mathcal X\subseteq\mathbb R^d\) be an input space equipped with its relative Borel sigma-algebra. Let \((X,Y,M)\), where \(M=(M_1,\ldots,M_J)\), have an arbitrary joint distribution on
\[
\mathcal X\times\{1,\ldots,K\}\times\{1,\ldots,K\}^J.
\]
Here \(M_j\) is expert \(j\)'s prediction, and define \(T_j=\mathbf1\{M_j=Y\}\).

A policy consists of measurable maps \(h:\mathcal X\to\{1,\ldots,K\}\) and \(r:\mathcal X\to\{0,1,\ldots,J\}\). Its class prediction and routing decision depend only on \(X\). Define its defer loss by
\[
L_\perp(h,r;X,Y,M)
=\mathbf1\{r(X)=0\}\mathbf1\{h(X)\ne Y\}
+\sum_{j=1}^J\mathbf1\{r(X)=j\}(1-T_j).
\]
Let \(\mathcal E_\perp(h,r)\) denote its expectation under the joint distribution, and let \(\mathcal E_\perp^*\) be its infimum over all such measurable policies.

Write
\[
\Delta^K=\left\{v\in[0,1]^K:\sum_{k=1}^K v_k=1\right\}.
\]
For measurable maps \(p:\mathcal X\to\Delta^K\) and \(u:\mathcal X\to[0,1]^J\), define
\[
\mathcal E_{\rm dec}(p,u)
=\mathbb E\left[-\log p_Y(X)
-\frac{\lambda}{J}\sum_{j=1}^J
\left(T_j\log u_j(X)+(1-T_j)\log(1-u_j(X))\right)\right].
\]
All logarithms are natural. Losses are interpreted in the extended-real sense: \(-\log0=+\infty\), and a term with zero coefficient is zero even when its logarithm is \(\log0\). Thus the Bernoulli loss is \(-\log u_j(X)\) when \(T_j=1\), and \(-\log(1-u_j(X))\) when \(T_j=0\). Let \(\mathcal E_{\rm dec}^*\) be the infimum of this risk over all such measurable \(p,u\).

Fix measurable tie-breaking for finite maxima. The plug-in policy \(f_{p,u}=(h_p,r_{p,u})\) uses a class \(h_p(x)\in\arg\max_k p_k(x)\) and routes according to
\[
r_{p,u}(x)=0\quad\text{if }\max_k p_k(x)\ge\max_j u_j(x),
\]
and otherwise selects an expert attaining \(\arg\max_j u_j(x)\).

## Task

Prove that, for every joint distribution and every measurable pair \(p,u\) specified above,
\[
\mathcal E_\perp(f_{p,u})-\mathcal E_\perp^*
\leq\max\left\{2\sqrt2,\sqrt{\frac{2J}{\lambda}}\right\}
\sqrt{\mathcal E_{\rm dec}(p,u)-\mathcal E_{\rm dec}^*}.
\]
In particular, for a fixed distribution and fixed \(K,J,\lambda\), show that any sequence of measurable estimates with decoupled-surrogate excess tending to zero has defer-risk excess tending to zero (Bayes consistency). Also show that when \(\lambda/J\) is fixed, the displayed calibration constant is independent of \(J\).
