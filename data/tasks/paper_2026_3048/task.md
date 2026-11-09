# Problem

## Setup

Fix \(n\ge1\). Let \(r_{1:n}=(r_1,\ldots,r_n)\in\mathbb R^n\) be residuals and let \(\bar r_n=n^{-1}\sum_{i=1}^n r_i\). For a candidate residual \(r_{n+1}\), define its centered-residual deviation from the training mean as \(|r_{n+1}-\bar r_n|\).

Define the posterior-predictive nonconformity score
\[
S(r_{n+1},r_{1:n})=-p(r_{n+1}\mid r_{1:n}),
\]
where \(p\) is the posterior-predictive density under
\[
R_i\mid\theta\stackrel{\mathrm{iid}}\sim N(\theta,\sigma^2),\qquad
\theta\mid w\sim N(0,\gamma w),\qquad
w\sim g(w)\,dw,
\]
with fixed \(\sigma,\gamma>0\). Assume that \(g\) is a density on \((0,\infty)\) and
\[
g(w)\sim Cw^{-\delta}\qquad(w\to\infty),
\]
for constants \(C>0\) and \(\delta>1\).

For the plug-in-variance statement, let \(n\ge2\), let \(r_{1:n}^{(m)}\in\mathbb R^n\), and define
\[
\widehat v_m^2=\frac1n\sum_{i=1}^n\left(r_i^{(m)}-\bar r_n^{(m)}\right)^2.
\]
Assume \(\widehat v_m^2\to v^2\in(0,\infty)\). For a candidate with deviation \(\Delta\), use the observation variance obtained from the augmented \(n+1\) residuals,
\[
\frac1n\sum_{i=1}^{n+1}\left(r_i^{(m)}-\bar r_{n+1}^{(m)}\right)^2,
\qquad r_{n+1}^{(m)}=\bar r_n^{(m)}+\Delta.
\]

## Task

Prove the following integrated asymptotic robustness theorem. For every sequence \(r_{1:n}^{(m)}\) with \(|\bar r_n^{(m)}|\to\infty\):

1. With the fixed variance \(\sigma^2\), for every fixed \(\Delta\in\mathbb R\),
\[
S(\bar r_n^{(m)}+\Delta,r_{1:n}^{(m)})\to h_n(|\Delta|),
\]
where
\[
h_n(u)=-[2\pi\sigma^2(1+1/n)]^{-1/2}
\exp\{-u^2/[2\sigma^2(1+1/n)]\},
\]
and \(h_n\) is strictly increasing on \([0,\infty)\). Thus the limiting score ordering is the ordering by centered-residual deviation.

2. Under the plug-in construction above, for every fixed \(\Delta\in\mathbb R\),
\[
S(\bar r_n^{(m)}+\Delta,r_{1:n}^{(m)})\to h_{n,v}(|\Delta|),
\]
where
\[
h_{n,v}(u)=-[2\pi(1+1/n)(v^2+u^2/(n+1))]^{-1/2}
\exp\{-u^2/[2(1+1/n)(v^2+u^2/(n+1))]\},
\]
and \(h_{n,v}\) is strictly increasing on \([0,\infty)\). Hence the plug-in score has the same limiting centered-residual ordering.
