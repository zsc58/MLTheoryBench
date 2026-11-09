# Problem

## Setup

Let \(Z_1,\ldots,Z_n\), with \(Z_i=(X_i,Y_i)\), be independent observations from a distribution \(P\). Fix a partition of \(\{1,\ldots,n\}\) into \(K\ge 2\) nonempty folds \(I_1,\ldots,I_K\), and write \(n_k=|I_k|\) and \(k(i)=k\) when \(i\in I_k\).

A finite dictionary contains \(M\ge1\) learning configurations, some of which may use feature-prior information and some of which are prior-free. For each fold \(k\), let \(g_j^{(-k)}\) be configuration \(j\) trained using only the observations outside \(I_k\). Let \(\widetilde g_j\) denote the same configuration refitted on all \(n\) observations. Define
\[
 \Delta_M=\left\{w\in[0,1]^M:\sum_{j=1}^M w_j=1\right\},
 \quad
 g_w^{(-k)}=\sum_{j=1}^M w_jg_j^{(-k)},
 \quad
 \widetilde g_w=\sum_{j=1}^M w_j\widetilde g_j.
\]
For a loss \(\ell\), set
\[
 \widehat R_{\mathrm{CV}}(w)
 =\frac1n\sum_{i=1}^n
 \ell\bigl(g_w^{(-k(i))}(X_i),Y_i\bigr),
 \qquad
 \widehat w\in\operatorname*{argmin}_{w\in\Delta_M}
 \widehat R_{\mathrm{CV}}(w).
\]
For an independent test observation \((X,Y)\sim P\), define, conditionally on the fitted training data,
\[
 R_k(w)=\mathbb E\!\left[\ell(g_w^{(-k)}(X),Y)\right],
 \qquad
 R_{\mathrm{CF}}(w)=\sum_{k=1}^K\frac{n_k}{n}R_k(w),
\]
and
\[
 R_{\mathrm{ref}}(w)=\mathbb E\!\left[\ell(\widetilde g_w(X),Y)\right].
\]

Assume that, for every \(y\), the map \(u\mapsto\ell(u,y)\) is convex and \(L_\ell\)-Lipschitz, that \(\sup_y|\ell(0,y)|<\infty\), and that
\[
 |g_j^{(-k)}(x)|\le B
 \quad\text{for all }j,k,x.
\]
Also assume the realized cross-fitted and refitted risk functionals satisfy the uniform refit-gap bound
\[
 \Gamma_{\mathrm{ref}}
 :=\sup_{w\in\Delta_M}|R_{\mathrm{ref}}(w)-R_{\mathrm{CF}}(w)|
 \le \varepsilon_n.
\]
Let \(S_0\subseteq\{1,\ldots,M\}\) be the nonempty set of prior-free configurations and
\[
 \mathcal W_0=\{w\in\Delta_M:w_j=0\text{ for }j\notin S_0\}.
\]

## Task

Prove that there is a universal constant \(C>0\) such that, for every \(\delta\in(0,1)\), with probability at least \(1-\delta\), both
\[
 R_{\mathrm{CF}}(\widehat w)
 \le \inf_{w\in\Delta_M}R_{\mathrm{CF}}(w)
 +C L_\ell B\sqrt{\frac{K\log(MK/\delta)}{n}}
\]
and
\[
 R_{\mathrm{ref}}(\widehat w)
 \le \inf_{w\in\Delta_M}R_{\mathrm{ref}}(w)
 +C L_\ell B\sqrt{\frac{K\log(MK/\delta)}{n}}
 +2\varepsilon_n.
\]
Deduce on the same event that each inequality remains true when its infimum over \(\Delta_M\) is replaced by the corresponding infimum over \(\mathcal W_0\).
