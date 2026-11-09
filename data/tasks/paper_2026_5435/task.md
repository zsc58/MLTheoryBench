# Problem

## Setup

Fix a finite batch of prompts \(X=(x_1,\ldots,x_m)\) and a target index \(i\in\{1,\ldots,m\}\). Conditional on \(X\), let \(R_1,\ldots,R_m\) be independently sampled real-valued rewards with finite second moments. Write
\[
\mu_j=\mathbb E[R_j\mid X],
\qquad
\tau_j^2=\operatorname{Var}(R_j\mid X).
\]
Assume \(\tau_j^2>0\) for every \(j\ne i\), and assume
\[
Q_i:=\sum_{k\ne i}\frac{\mu_k^2}{\tau_k^2}>0.
\]

Consider leave-one-out linear estimators of the target value \(\mu_i\) of the form
\[
\widehat\mu_i=\sum_{j\ne i}a_{ij}R_j,
\]
where the coefficients may depend on the conditioned batch \(X\), but not on the sampled rewards.

## Task

Prove that, among all such estimators satisfying conditional unbiasedness
\[
\mathbb E[\widehat\mu_i\mid X]=\mu_i,
\]
the unique estimator minimizing the conditional mean-squared error
\[
\mathbb E\!\left[(\widehat\mu_i-\mu_i)^2\mid X\right]
\]
has coefficients
\[
a_{ij}^{\star}
=
\frac{\mu_i\mu_j/\tau_j^2}
{\displaystyle\sum_{k\ne i}\mu_k^2/\tau_k^2},
\qquad j\ne i.
\]
