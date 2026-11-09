# Problem

## Setup

Let X be a finite nonempty set, let N>=1 be a fixed integer, and let f:X->R be an unknown deterministic function. Fix a known variance sigma^2>0 and put Sigma=sigma^2 I_N.

A deterministic adaptive procedure starts at a fixed x_1 in X. For n=1,...,N-1, it chooses x_{n+1} using only ((x_1,Y_1),...,(x_n,Y_n)). The observations are generated sequentially by

Y_i=f(x_i)+epsilon_i,  i=1,...,N,

where epsilon_1,...,epsilon_N are independent N(0,sigma^2) variables. The update rules, including their boundary decisions, are fixed before collecting the responses.

For each stage n and each fixed queried history (x_1,...,x_n), assume that the update rule is constant on each cell of a finite polyhedral partition of R^n in the response coordinates. A polyhedral cell here is specified by finitely many linear equalities and strict or weak linear inequalities; the partitions include their boundary assignments. Let tau(u) be the queried trajectory obtained by applying the procedure to a response vector u in R^N.

A target map eta:R^N->R^N is also given. It is constant on each cell of a finite polyhedral partition of R^N. Assume eta(Y) is nonzero almost surely. The cell descriptions and their output labels are available for the requested computation.

For a trajectory tau=(a_1,...,a_N), define

mu_tau=(f(a_1),...,f(a_N))^T.

The joint selection output and selected effect are

E(u)=(tau(u),eta(u)),

Delta_sel(Y)=eta(Y)^T mu_{tau(Y)}.

For a fixed nonzero vector w, define the residual map

Q_w(u)=(I_N-Sigma w w^T/(w^T Sigma w))u.

Write R(u)=Q_{eta(u)}(u) when eta(u) is nonzero, and set R(u)=0 otherwise.

For an observed response vector y with eta(y) nonzero, put

eta=eta(y),  tau=tau(y),  e=E(y),  t=eta^T y,

v=eta^T Sigma eta,  q=R(y),  Delta=eta^T mu_tau.

For z in R define

y(z)=q+(Sigma eta/v)z,

Z_{e,q}={z in R:E(y(z))=e}.

Let phi_v(r)=(2 pi v)^(-1/2) exp(-r^2/(2v)). Whenever its denominator is positive, define

p_sel(y) = [integral over Z_{e,q} intersect [t,infinity) of phi_v(u) du] / [integral over Z_{e,q} of phi_v(u) du].

Set p_sel(y)=1 if eta(y)=0 or if the displayed denominator is zero. Conditional distribution assertions below are understood as assertions about regular conditional laws, almost surely in the observed conditioning variables.

## Task

Prove that, for every y with eta(y) nonzero, Z_{e,q} is a finite union of intervals, allowing unbounded intervals and singletons, and is exactly computable from the stagewise and target-cell descriptions, including their boundary assignments.

Prove that the denominator defining p_sel(Y) is positive almost surely. Prove moreover that, conditional on E(Y)=e and R(Y)=q, the statistic eta^T Y has the N(Delta,v) distribution truncated to Z_{e,q}. Here Delta and v denote the mean and variance of the normal distribution before truncation.

Consequently, prove that for every alpha in (0,1), the test rejecting when p_sel(Y)<=alpha has conditional rejection probability at most alpha on every selected stratum with Delta<=0, almost surely in its residual. State the marginal selected-null guarantee precisely by proving, for every fixed f,

P_f(p_sel(Y)<=alpha, Delta_sel(Y)<=0)
 <= alpha P_f(Delta_sel(Y)<=0).

Thus, when the selected-null event has positive probability, rejection conditional on that event has probability at most alpha; in particular, P_f(p_sel(Y)<=alpha)<=alpha whenever Delta_sel(Y)<=0 almost surely.

Explain the exact finite-sum normal-CDF computation of p_sel.
