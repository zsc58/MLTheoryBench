# Problem

## Setup

For each integer \(n\ge2\), let \(z_{n,1},\ldots,z_{n,n}\in\mathbb R\) be deterministic scores and let \(z_n^*=\max_j z_{n,j}\). For a positive inverse temperature \(\beta\), define
\[
p_{n,j}(\beta)=\frac{e^{\beta z_{n,j}}}{\sum_{k=1}^n e^{\beta z_{n,k}}},
\quad
H_n(\beta)=-\sum_{j=1}^n p_{n,j}(\beta)\log p_{n,j}(\beta),
\]
and let \(D_n(\beta)\) be the largest softmax probability minus the second largest. Along a positive deterministic sequence \((\beta_n)\), say top-two collapse occurs when \(D_n(\beta_n)\to0\), and entropy collapse when \(H_n(\beta_n)\to0\). A positive deterministic sequence \(X_n\) is a top-two--entropy critical (TE) scale if, for every positive deterministic sequence \(\beta_n\), \(\beta_n/X_n\to0\) implies top-two collapse and \(\beta_n/X_n\to\infty\) implies entropy collapse.

Define gaps \(d_{n,j}=z_n^*-z_{n,j}\) and the cumulative gap count
\[
N_n(t)=\#\{j:d_{n,j}\le t\},\qquad t\ge0.
\]
Assume there is an integer \(n_0\ge2\) such that, for every \(n\ge n_0\),
\[
\Lambda_n:=\sup_{t>0}\frac{\log N_n(t)}{t}<\infty.
\]
For \(n\ge n_0\), let \(\Delta_n\) be the largest positive gap attaining this supremum, and set
\[
\alpha_n=\frac{\log N_n(\Delta_n)}{\log n}.
\]
(For finite \(\Lambda_n\), such a contact gap exists.) For \(2\le n<n_0\), choose arbitrary finite positive values for \(\Lambda_n,\Delta_n,\alpha_n\); their displayed definitions are imposed only for \(n\ge n_0\).

For a positive sequence \((x_n)\) and a real number \(\xi\), write \(x_n\asymp(\log n)^\xi\) when \(x_n/(\log n)^\xi\) is bounded above and below by positive constants for all sufficiently large \(n\). When this holds, call \(\xi\) a logarithmic growth exponent of \((x_n)\).

## Task

Prove the following integrated theorem. The sequence \((\Lambda_n)\) is a TE scale. Consequently, if \(\beta_n\asymp(\log n)^{\xi_\beta}\) with \(\xi_\beta\ge0\) and \(\Lambda_n\asymp(\log n)^{\xi_\Lambda}\), any positive deterministic schedule that avoids both top-two and entropy collapse satisfies \(\xi_\beta=\xi_\Lambda\). Moreover, whenever any two of \(\Lambda_n,\alpha_n,\Delta_n\) admit logarithmic growth exponents \(\xi_\Lambda,\xi_\alpha,\xi_\Delta\), so does the third and
\[
\xi_\Lambda=\xi_\alpha-\xi_\Delta+1.
\]
