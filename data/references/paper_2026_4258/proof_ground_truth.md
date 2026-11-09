# Reference Proof

## Proof Structure and Obligations

The obligations are: (1) compute the conditional Dirichlet covariance with the correct normalization; (2) remove the simplex-centering term using empirical stationarity and propagate covariance through the symmetric inverse Hessian; (3) control the sample-dependent sandwich matrix to justify the asymptotic difference statement; (4) prove the curvature specialization using the additional empirical convergence premise; and (5) prove validation consistency and calibrated population coverage from uniform convergence and compactness. No Gaussian limit or approximation error for the weighted minimizer is asserted or needed.

## Conditional Covariance

Write D_n for the training data and condition on D_n. The matrices G, H, and H_F are then fixed. The standard symmetric Dirichlet moment formulas, valid for positive alpha, are

E[w_i | D_n] = 1/n,

Cov(w_i,w_k | D_n) = (n 1{i=k}-1)/(n^2(n alpha+1)).

Their hypotheses hold because the weights are drawn conditionally from Dirichlet(alpha,...,alpha). For n=1 the weight is identically one and the same covariance formula is zero. Thus, with j the all-ones vector and P=I-jj^T/n,

Var(tilde w | D_n) = n/(n alpha+1) P.

Empirical stationarity gives Gj=0, so GPG^T=GG^T=n H_F. Consequently,

Var(G tilde w/n | D_n)
 = n^{-2}G Var(tilde w | D_n)G^T
 = [n(n alpha+1)]^{-1}GPG^T
 = (n alpha+1)^{-1}H_F.

The Hessian H is symmetric, and its inverse is symmetric because H is invertible. Covariance propagation through -H^{-1} therefore gives the exact identity

Var(Delta vartheta_w | D_n)
 = (n alpha+1)^{-1}H^{-1}H_FH^{-1}.

## Asymptotic Scaling and Specialization

Let S_n=H^{-1}H_FH^{-1}. Since

||H_F|| <= n^{-1} sum_i ||g_i||^2 = O_p(1)

and ||H^{-1}||=O_p(1), we have ||S_n||=O_p(1). For each fixed alpha>0,

n Var(Delta vartheta_w | D_n) - alpha^{-1}S_n
 = -[alpha(n alpha+1)]^{-1}S_n.

The deterministic coefficient tends to zero, so the norm of this difference tends to zero in probability. This proves the requested statement for every fixed alpha in A. It does not require S_n to converge to a fixed matrix.

At alpha=1, Dirichlet(1,...,1) is the Bayesian-bootstrap weighting law. The preceding identity gives

||n Var(Delta vartheta_w | D_n)-S_n|| ->p 0.

If, in addition, ||H_F-H|| ->p 0 as stipulated in the likelihood specialization, then

S_n-H^{-1}=H^{-1}(H_F-H)H^{-1},

whose norm tends to zero in probability because ||H^{-1}||=O_p(1). Hence

||n Var(Delta vartheta_w | D_n)-H^{-1}|| ->p 0

at alpha=1. Correct specification alone is not used to prove empirical convergence. The population information identity explains this specialization in regular likelihood settings, but deriving empirical convergence from a sampling model is not an obligation of the stated task.

## Validation Consistency

In this part n is held fixed while m tends to infinity. The trained predictive construction, its population coverage C, and alpha_tau may depend on D_n. Set

T(alpha)=|C(alpha)-(1-tau)|,

T_hat_m(alpha)=|C_hat_m(alpha)-(1-tau)|,

U_m=sup_{alpha in A}|C_hat_m(alpha)-C(alpha)|.

The reverse triangle inequality gives

sup_{alpha in A}|T_hat_m(alpha)-T(alpha)| <= U_m ->p 0.

Since alpha_hat_m minimizes T_hat_m and T(alpha_tau)=0,

T(alpha_hat_m)
 <= T_hat_m(alpha_hat_m)+U_m
 <= T_hat_m(alpha_tau)+U_m
 <= 2U_m.

In particular,

|C(alpha_hat_m)-(1-tau)| ->p 0,

which already proves calibrated population coverage.

To prove selector consistency, fix epsilon>0 and consider

K_epsilon={alpha in A: |alpha-alpha_tau|>=epsilon}.

For each training realization satisfying the assumptions, K_epsilon is compact. If it is nonempty, continuity of T and uniqueness of its zero imply

delta_epsilon=min_{alpha in K_epsilon} T(alpha)>0.

If K_epsilon is empty, the event |alpha_hat_m-alpha_tau|>=epsilon is impossible; define delta_epsilon=1 in that case. This also covers a singleton A. Roots at endpoints require no modification.

Whenever |alpha_hat_m-alpha_tau|>=epsilon, the preceding bounds imply delta_epsilon<=2U_m. If the training data are fixed, delta_epsilon is a positive constant, immediately giving consistency. For random training data with fixed n, delta_epsilon is positive almost surely and its distribution does not change with m. For any eta>0,

Pr{|alpha_hat_m-alpha_tau|>=epsilon}
 <= Pr{delta_epsilon<=eta}+Pr{2U_m>=eta}.

First let m tend to infinity and then let eta decrease to zero. The right-hand side tends to zero. Therefore alpha_hat_m ->p alpha_tau. Continuity of C also transfers selector consistency to coverage when conditioning on a fixed trained construction; the direct bound T(alpha_hat_m)<=2U_m proves the requested coverage statement without any uniform continuity issue across random training realizations.

The empirical objective takes only finitely many values because C_hat_m is an average of m indicators. Thus its minimum over nonempty A is attained. Measurability of the chosen selector is stipulated in the task. All probability expressions and uniform errors are measurable under the stated measurability convention.
