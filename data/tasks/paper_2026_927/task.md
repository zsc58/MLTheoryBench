# Problem

## Setup

Let \(d,m,n,K\) be positive integers with \(K\leq m\), and write \([m]=\{1,\ldots,m\}\) and \([K]=\{1,\ldots,K\}\). Let \((Z,L)\), with \(Z\in\mathbb R^d\) and \(L\in[m]\), be a test feature-label pair. Let \((Z_i,L_i)_{i=1}^n\) be a calibration sample such that these \(n+1\) feature-label pairs are exchangeable.

Let \(B=\phi(Z)\), where \(\phi\) is a measurable map to a finite set \(\mathcal A\), and assume \(\Pr(B=u)>0\) for every \(u\in\mathcal A\). Fix a measurable score \(\rho:\mathbb R^d\times[m]\to\mathbb R\), a level \(\alpha\in(0,1)\), and a map \(c:[m]\to[K]\) whose clusters
\[
\mathcal L_j=\{\ell:c(\ell)=j\}
\]
are all nonempty.

For each cluster define
\[
I_j=\{i\in\{1,\ldots,n\}:c(L_i)=j\},\qquad n_j=|I_j|,
\]
and assume \(n_j\geq1\) almost surely. Arrange the calibration scores \(\{\rho(Z_i,L_i):i\in I_j\}\) in nondecreasing order as
\[
V_{j,(1)}\leq\cdots\leq V_{j,(n_j)}.
\]
Set \(k_j=\lceil(n_j+1)(1-\alpha)\rceil\) and define the split-conformal threshold by
\[
t_j=\begin{cases}
V_{j,(k_j)},&k_j\leq n_j,\\
+\infty,&k_j=n_j+1.
\end{cases}
\]
The same \(t_j\) is used for every sensitive group. Define
\[
S(z)=\{\ell\in[m]:\rho(z,\ell)\leq t_{c(\ell)}\}.
\]

All probabilities and expectations below are under the joint law of the calibration sample and test pair; in particular, calibration randomness is included in the expectations. For groups \(u,v\in\mathcal A\), define
\[
\Delta_{u,v}=\left|\mathbb E[|S(Z)|\mid B=u]-\mathbb E[|S(Z)|\mid B=v]\right|,
\]
\[
\mu_{j,u}=\mathbb E[|S(Z)|\mid c(L)=j,B=u],\qquad
r_{\ell,u}=\mathbb E[|S(Z)|\mid L=\ell,B=u],
\]
and
\[
\varepsilon_{j,u}=\max_{\ell\in\mathcal L_j}r_{\ell,u}-\min_{\ell\in\mathcal L_j}r_{\ell,u}.
\]
If a conditioning event has probability zero, define the corresponding conditional expectation as zero.

## Task

Prove that for every pair of sensitive groups \(u,v\in\mathcal A\),
\[
\Delta_{u,v}\leq
\max_{1\leq j\leq K}\varepsilon_{j,u}
+\left(\max_{1\leq j\leq K}\mu_{j,u}-\min_{1\leq j\leq K}\mu_{j,u}\right)
+\left|\sum_{\ell=1}^{m}\Pr(L=\ell\mid B=v)\bigl(r_{\ell,u}-r_{\ell,v}\bigr)\right|.
\]
