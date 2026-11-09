# Reference Proof

## Proof Structure

Establish conditional bridge existence and uniqueness using the specified Hilbert spaces and singular system. Assemble conditional solutions measurably. Identify the bridge through the complete-case conditional equation, and separately prove the inverse-propensity weighted equivalence. Use the shared controlled reward law and augmented transition law to obtain the correct augmented Bellman kernels. Finally, derive target-support coverage from action-policy domination and perform backward induction.

## Complete Proof

### 1. Conditional solvability and uniqueness

Fix a stage and state-action pair, and abbreviate the conditional next-state and reward laws by \(\nu\) and \(\eta\). Put \(g(r)=r\) and
\[
T:L^2(\nu)\longrightarrow L^2(\eta),\qquad Th=E[h(S')\mid R,s,a].
\]
Conditional Jensen gives \(\|T\|\leq1\). For \(h\in L^2(\nu)\) and \(f\in L^2(\eta)\), conditioning the product \(h(S')f(R)\) in either order gives
\[
\langle Th,f\rangle_{L^2(\eta)}
=E[h(S')f(R)\mid s,a]
=\langle h,E[f(R)\mid S',s,a]\rangle_{L^2(\nu)}.
\]
Thus \(T^*f=E[f(R)\mid S',s,a]\). The two completeness assumptions imply \(\ker T^*=\{0\}\) and \(\ker T=\{0\}\), respectively.

The independent operator fact used here is the Picard criterion: for a compact operator \(T\), a vector \(g\) is in its range if and only if \(g\perp\ker T^*\) and \(\sum_j|\langle g,u_j\rangle|^2/\sigma_j^2<\infty\), where \(Tv_j=\sigma_j u_j\) and \(T^*u_j=\sigma_j v_j\). The solution orthogonal to \(\ker T\) is the convergent series
\[
h=\sum_j\frac{\langle g,u_j\rangle}{\sigma_j}v_j.
\]
Here compactness follows from the stated Hilbert--Schmidt hypothesis; \(g\in L^2(\eta)\) because rewards are bounded; orthogonality follows from \(\ker T^*=\{0\}\); and summability is assumed. Equivalently, convergence of the displayed series follows directly from summability, and applying the bounded operator \(T\) to its partial sums gives \(Th=g\), since the \(u_j\) span \((\ker T^*)^\perp\).

If \(Th_1=Th_2=g\), then \(h_1-h_2\in\ker T\), so \(h_1=h_2\) \(\nu\)-almost surely. This includes finite-rank cases, with finite sums.

### 2. Measurable assembly

The preceding argument produces conditional equivalence classes. The following routine construction gives a jointly measurable representative without postulating an existing bridge or an unconditional L2 bound.

For each stage use the measurable conditional kernels to define jointly measurable iterates, at every state-action pair,
\[
h_0=0,\qquad h_{n+1}=h_n+T^*(g-Th_n).
\]
For each fixed pair their singular coefficients are
\[
h_n=\sum_j\left[1-(1-\sigma_j^2)^n\right]
\frac{\langle g,u_j\rangle}{\sigma_j}v_j.
\]
Since \(0<\sigma_j\leq1\), dominated convergence for the summable squared coefficients gives \(h_n\to h\) in the conditional L2 norm.

To select measurable pointwise versions of these limits, write
\[
D_{p,q}(s,a)=\int|h_p(s,a,s')-h_q(s,a,s')|^2\,\nu_{t,s,a}(ds').
\]
These are measurable. Recursively choose \(N_k(s,a)>N_{k-1}(s,a)\) to be the least integer such that
\[
\sup_{p,q\geq N_k(s,a)}D_{p,q}(s,a)\leq 2^{-4k}.
\]
Conditional L2 convergence ensures this integer exists; countability makes the choice measurable. The successive selected iterates have conditional L1 distances at most \(2^{-2k}\). Their increments are therefore absolutely summable almost surely under each conditional next-state law. Define \(b_t(s,a,s')\) as their pointwise limit where it exists and as zero elsewhere. This is jointly measurable and represents the conditional L2 solution for each pair. Consequently
\[
\int b_t(s,a,s')\,P_t(ds'\mid r,s,a)=r
\]
for \(\eta_{t,s,a}\)-almost every \(r\). No integration of the conditional solution norms over state-action pairs was needed.

### 3. Observable and weighted moment equivalences

Fix a behavior-supported state-action pair. Positivity implies that the full conditional reward law \(\eta\) and its complete-case counterpart \(\eta^{\mathrm{obs}}\) are equivalent measures: their density ratio is
\[
\frac{d\eta^{\mathrm{obs}}}{d\eta}(r)
=\frac{e_t(s,a,r)}{P_\mu(O_t=1\mid s,a)}>0.
\]
The normalizing probability is strictly positive. Exclusion gives
\[
P_\mu(ds'\mid r,s,a,O_t=1)=P_\mu(ds'\mid r,s,a)
\]
for the equivalent almost-everywhere reward laws. Therefore a candidate bridge satisfies the full equation if and only if
\[
E_\mu[b_t(s,a,S_{t+1})-R_t\mid R_t,S_t=s,A_t=a,O_t=1]=0.
\]
This last equation uses only complete-case observations and their conditional next-state law.

For any candidate in the specified conditional L2 domain, put \(Z=b_t(s,a,S_{t+1})-R_t\). Exclusion and positivity imply, as a conditional kernel identity,
\[
E_\mu\left[\frac{O_t}{e_t(s,a,R_t)}Z\mid R_t,s,a\right]
=E_\mu[Z\mid R_t,s,a].
\]
The relevant integrability is not an unproved inverse-propensity second-moment assumption. Indeed,
\[
E_\mu\left[\frac{O_t}{e_t(s,a,R_t)}|Z|\mid s,a\right]
=E_\mu[|Z|\mid s,a]<\infty,
\]
because \(b_t(s,a,\cdot)\in L^2(\nu_{t,s,a})\) and rewards are bounded. The weighted residual is defined to be zero when \(O_t=0\). Thus the conditional weighted equation is equivalent to the full bridge equation, and hence to the complete-case equation. Neither a known propensity nor a uniform positive lower bound is needed.

The full next-state marginal \(\nu_{t,s,a}\) is observable because next states, including the terminal one, are always observed. It specifies the candidate L2 domain. The complete-case equation is also observable. Any two admissible solutions of that observable equation solve the full equation under the actual model and therefore coincide \(\nu_{t,s,a}\)-almost surely. More generally, two admissible full-data models with the same observation law have the same conditional next-state L2 domain and the same complete-case equation, so their bridges agree on behavior support. This proves observational identification of the bridge, not merely an identity involving an unknown propensity.

### 4. The augmented one-step reward and transition

Integrating the bridge equation with respect to the conditional reward law gives
\[
\int b_t(s,a,s')\,\nu_{t,s,a}(ds')
=\int r\,\eta_{t,s,a}(dr)=:m_t(s,a).
\]
This calculation is legitimate for each conditional kernel since the bridge is conditionally L2. It also shows \(|m_t(s,a)|\leq1\).

The controlled reward/next-state law depends on the decision history only through \((S_t,A_t)\). Consequently, on any supported augmented state-action pair,
\[
\bar r_t((s,o_-),a)
=E_\mu[b_t(s,a,S_{t+1})\mid S_t=s,O_{t-1}=o_-,A_t=a]
=m_t(s,a)
=E_\pi[R_t\mid S_t=s,O_{t-1}=o_-,A_t=a].
\]
The source's separate augmented transition restriction likewise makes the conditional law of \((S_{t+1},O_t)\) the same controlled law under behavior and target policies. This is an observed kernel. These conclusions use the explicit controlled-law assumptions, not an invalid application of the tower property that adds \(O_{t-1}\) to a conditioning set.

For comparison with the source's mixed imputation, exclusion also gives
\[
E_\mu[O_tR_t+(1-O_t)b_t\mid R_t,s,a]
=e_tR_t+(1-e_t)R_t=R_t.
\]
Hence the all-bridge reward mean in the task and the source's mixed-imputation reward mean coincide. This identity is supporting proof material, not an additional public assumption.

### 5. Coverage under the target policy

Fix an admissible target policy and its finite action-domination constants \(\kappa_t\). At each decision, \(\pi_t(da\mid s,o_-)\) is dominated by \(\mu_t(da\mid s)\) with density at most \(\kappa_t\). The initial law and controlled augmented transitions are shared. Multiplying the action densities along a history, or inducting on the history law, therefore shows that the target law through the action at stage \(t\) is dominated by the corresponding behavior law with density at most
\[
\prod_{j=1}^t\kappa_j<\infty.
\]
Marginalizing gives the same bound for the augmented state-action occupancy law. Thus behavior-null sets of augmented state-action pairs are target-null. This derived product bound must not be confused with the primitive per-action coefficient \(\kappa_t\).

### 6. Bellman induction and policy value

Define the true target conditional return functions using the shared controlled kernels. Their terminal value is zero. Suppose the task's recursively defined value function agrees with the true one at stage \(t+1\). Section 4 supplies the correct conditional reward mean and the correct augmented transition kernel, and Section 5 ensures that all kernels needed under the target policy are identified on the relevant support. Hence the displayed recursion computes the true conditional action value at stage \(t\). Integrating against \(\pi_t\) computes the true conditional state value. Backward induction establishes the asserted equalities for all stages, up to the relevant occupancy-null sets.

In particular, the recursive values are bounded in absolute value by \(H-t+1\), so their initial average is well-defined. Since the initial state law is observed and \(O_0=0\),
\[
E_\pi\left[\sum_{t=1}^H R_t\right]
=\int\widetilde V_1^\pi(s,0)\,\rho_1(ds).
\]
Every quantity on the right is determined by the behavior observation law and the specified target policy. This proves the requested identification for each admissible missingness-aware target policy.
