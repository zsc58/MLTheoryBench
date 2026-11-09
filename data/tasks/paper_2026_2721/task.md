# Problem

## Setup

Fix a sufficiently large horizon \(T\). In each round \(t=1,\ldots,T\), a policy observes \(K=\lceil4T^{1/3}\log T\rceil\) scalar contexts \(X_{t,1},\ldots,X_{t,K}\), drawn independently and uniformly from \([-1,1]\), and selects one arm. After selecting arm \(A_t\), it observes
\[
Y_t=f(X_{t,A_t})+\eta_t,
\]
where \(\eta_t\stackrel{\mathrm{iid}}\sim N(0,1)\), independent of all contexts and of the policy's internal randomness. The one-dimensional index parameter is fixed as \(\theta_*=1\). The unknown link \(f:[-1,1]\to[0,1]\) is continuously differentiable, satisfies \(\|f'\|_\infty\leq1\), and obeys the standing condition
\[
\mathbb E_{X\sim\mathrm{Unif}[-1,1]}[f'(X)]>0.
\]
No monotonicity is assumed. The same policy is used for all links: it may use the current and previously observed contexts, past selected rewards, and its internal randomness, but is not told \(f\). Define pseudo-regret
\[
R_T=\sum_{t=1}^T\left(\max_{1\leq a\leq K}f(X_{t,a})-f(X_{t,A_t})\right).
\]

## Task

Prove that there is a universal constant \(c>0\) such that, for every policy and all sufficiently large \(T\), there exists a valid one-dimensional non-monotone instance in the above class for which
\[
\mathbb E[R_T]\geq c\,T^{2/3}.
\]
The expectation is over contexts, Gaussian noise, and policy randomness.
