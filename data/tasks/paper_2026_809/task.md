# Problem

## Setup

Let \(\operatorname{sgn}(x)=1\) for \(x>0\), \(-1\) for \(x<0\), and \(0\) for \(x=0\). Fix \(\alpha>0\), \(\sigma\ge0\), and an initial state \(x_0\in\mathbb R\). Let \((\xi_n)_{n\ge1}\) be iid standard Gaussian random variables, and define
\[
X_{n+1}^{(\sigma)}=X_n^{(\sigma)}-\alpha\bigl(\operatorname{sgn}(X_n^{(\sigma)})+\sigma\xi_{n+1}\bigr),
\qquad X_0^{(\sigma)}=x_0.
\]
For \(\varepsilon>0\), define the hitting time
\[
T_{\varepsilon}^{(\sigma)}=\inf\{n\ge0:|X_n^{(\sigma)}|\le\varepsilon\},
\]
with \(\inf\varnothing=\infty\). Write \(U_n=X_n^{(0)}\) for the deterministic trajectory.

## Task

Prove the following integrated theorem.

1. For every \(\sigma>0\), \(\mathbb P(T_{\varepsilon}^{(\sigma)}<\infty)=1\). For \(\sigma=0\), if \((x_0+\alpha\mathbb Z)\cap[-\varepsilon,\varepsilon]=\varnothing\), then \(T_{\varepsilon}^{(0)}=\infty\).
2. Suppose there is a \(\Delta>0\) such that \(|U_n|\ge\varepsilon+\Delta\) for every \(n\ge0\). Then, for each fixed integer \(N\ge1\),
\[
\lim_{\sigma\downarrow0}\mathbb P(T_{\varepsilon}^{(\sigma)}>N)=1,
\qquad
\lim_{\sigma\to\infty}\mathbb P(T_{\varepsilon}^{(\sigma)}>N)=1.
\]
