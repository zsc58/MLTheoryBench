# Problem

## Setup

Fix positive integers \(P,N\), integers \(K\ge2\) and \(M\ge2\), and a nonnegative integer degree \(D\). Let \(\mathcal X\subset\mathbb R^P\) be compact. Let \(\{(x_n,y_n)\}_{n=1}^N\) be an observed batch of independent, identically distributed copies of a predictor-response pair taking values in \(\mathcal X\times\{1,\ldots,M\}\). Define \(Q=P(D+1)\) and
\[
\phi(x)=\bigl(x_1^0,x_1^1,\ldots,x_1^D,\ldots,x_P^0,x_P^1,\ldots,x_P^D\bigr)^{\mathsf T}\in\mathbb R^Q,
\]
where each degree-zero coordinate is the constant \(1\).

For identifiability set the \(K\)-th gate coefficient and the \(M\)-th coefficient of every expert to zero. The free gate coefficients \(\alpha_1,\ldots,\alpha_{K-1}\) and expert coefficients \(\beta_{km}\), \(k\le K\), \(m<M\), are arbitrary finite vectors in \(\mathbb R^Q\). Their collection is denoted by \(\theta\); minimization over \(\theta\) is over these free real coefficients subject only to the zero-reference convention. Define
\[
 g_k(x)=\frac{\exp(\alpha_k^{\mathsf T}\phi(x))}{1+\sum_{j<K}\exp(\alpha_j^{\mathsf T}\phi(x))}\quad(k<K),\qquad
 g_K(x)=\frac1{1+\sum_{j<K}\exp(\alpha_j^{\mathsf T}\phi(x))},
\]
\[
 e_k(m\mid x)=\frac{\exp(\beta_{km}^{\mathsf T}\phi(x))}{1+\sum_{\ell<M}\exp(\beta_{k\ell}^{\mathsf T}\phi(x))}\quad(m<M),\qquad
 e_k(M\mid x)=\frac1{1+\sum_{\ell<M}\exp(\beta_{k\ell}^{\mathsf T}\phi(x))},
\]
and \(s_\theta(y\mid x)=\sum_{k=1}^K g_k(x)e_k(y\mid x)\). Let
\[
L(\theta)=\sum_{n=1}^N\log s_\theta(y_n\mid x_n).
\]

## Task

Starting from an arbitrary current parameter \(\theta^{(t)}\), construct an explicit batch quadratic MM surrogate for \(-L\), including the responsibility and gate/expert update formulas, and prove that your updates exactly minimize the surrogate you construct and satisfy
\[
L(\theta^{(t+1)})\ge L(\theta^{(t)})
\]
for every iteration and every realized batch. Your proof must state all curvature matrices and handle singular normal equations with a valid minimum-norm or ridge convention.
