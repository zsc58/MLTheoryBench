# Reference Proof

## Contract and proof obligations

Use the public algorithm exactly as specified, including its inflated radius, pre-epoch covariance samples, epoch-local regression, and measurable completion on singular masks. Write alpha=delta/8 and L=log(16dT/delta). The obligations are: corrected-covariance concentration; projector and aligned-basis recovery; simultaneous observed-row conditioning; imputation; fixed-coordinate approximation and aggregated misspecification; an adapted, predictable self-normalized noise argument; optimism and potential summation; and burn-in/epoch accounting. All are established below.

The standard independent results used are the following. For independent mean-zero self-adjoint d-by-d matrices Q_l with ||Q_l||<=M and ||sum E Q_l^2||<=v, matrix Bernstein gives P(||sum Q_l||>=sqrt(2vu)+(2/3)Mu)<=2d exp(-u). For a rank-m positive semidefinite population matrix with smallest positive eigenvalue lambda_m, perturbation of norm E<=lambda_m/2 gives top-m projector error at most 2E/lambda_m. For independent positive semidefinite matrices bounded by rho I whose sum has expectation pI_m, matrix Chernoff gives P(lambda_min(sum)<=(1-a)p)<=m exp(-a^2 p/(2rho)), 0<a<1. Weyl's inequality bounds each ordered eigenvalue displacement by the operator norm of the perturbation.

For self-normalization, the precise filtration hypotheses matter. Let (F_s) be a filtration, let x_s be finite and F_{s-1}-measurable, and let nu_s be F_s-measurable with E[exp(a nu_s)|F_{s-1}]<=exp(a^2R^2/2) for every real a. For V_q=lambda I+sum_{s<=q}x_sx_s^T, lambda>0, with failure probability at most h, simultaneously over q,

||sum_{s<=q}x_s nu_s||_{V_q^{-1}} <= R sqrt(2 log(det(V_q)^{1/2}/(det(lambda I)^{1/2}h))).

Both noise adaptedness and feature predictability will be verified for the same filtration. We do not assume that unobserved original noises are measurable from past observed rewards, or that their conditional moment bounds persist upon enlargement by hidden variables. No concentration is asserted for the covariance of adaptively selected actions.

## 1. Corrected covariance and subspace recovery

For one masked action, Y_jj=p^{-1}S_j X_j^2 and Y_jk=p^{-2}S_jS_kX_jX_k for j!=k. Independence of the mask coordinates yields E[Y|X]=XX^T.

Expanding Y^2, its off-diagonal conditional expectation is p^{-1}X_jX_k||X||^2: the terms with intermediate index j or k use E[S_jS_k]=p^2, and the remaining terms use E[S_jS_kS_l]=p^3. Its diagonal conditional expectation is p^{-1}X_j^4+p^{-2}X_j^2(||X||^2-X_j^2). Consequently

E[Y^2|X]=(||X||^2/p)XX^T+(p^{-2}-p^{-1})diag(X_j^2(||X||^2-X_j^2)).

For Q=Y-Sigma, E Q=0, ||Q||<=3B_X^2/p^2, and

E Q^2=E Y^2-Sigma^2 <= E Y^2 <= (B_X^2/p)Sigma+(B_X^2/p^2)diag(Sigma)

in positive-semidefinite order. Since both ||Sigma|| and ||diag(Sigma)|| are at most bar(lambda), ||E Q^2||<=2B_X^2 bar(lambda)/p^2.

The qK offered samples through round q are independent, irrespective of arm choices. Apply matrix Bernstein with u=L and union bound over q=1,...,T. With failure probability at most alpha, simultaneously over these q,

||hat(Sigma)_{q+1}-Sigma|| <= E_q := 2B_X sqrt(bar(lambda)L/(p^2 qK))+2B_X^2L/(p^2 qK).

Here hat(Sigma)_{q+1} is the public estimator using q completed rounds, not q+1 rounds.

Set epsilon_q=C_a(kappa/p)sqrt(mL/(qK)), with C_a>=12 as in the algorithm. We show on this same event that both the projector distance and the optimally aligned basis distance are at most epsilon_q. If epsilon_q>=sqrt(2), this follows from projector distance at most one and aligned-basis distance at most sqrt(2). Otherwise,

qK>(C_a^2/2)B_X^2 bar(lambda)L/(lambda_m^2p^2).

This inequality makes the linear term in E_q no larger than the square-root term, and gives E_q<=4B_X sqrt(bar(lambda)L/(p^2qK))<=4sqrt(2)lambda_m/C_a<lambda_m/2. The perturbation bound therefore yields projector distance at most (8/C_a)epsilon_q.

For completeness, if Uhat^T U=A cos(Theta)B^T and O=AB^T, direct expansion gives

(Uhat O-U)^T(Uhat O-U)=B[2I-2cos(Theta)]B^T.

Thus ||Uhat O-U||<=sqrt(2)||Uhat Uhat^T-UU^T||. Since 8sqrt(2)/C_a<=1, the aligned-basis bound follows as well. If m=d, the projector distance is zero and the bases can be aligned exactly, so no nonexistent (d+1)-st eigenvalue is needed.

The prescribed burn-in and C_b>=(32C_a)^2 ensure epsilon_{t_b}<=p/32. Every nonempty epoch uses q=tau_e-1>=t_b.

## 2. Simultaneous mask conditioning and imputation

Put rho=max_j||U_{j,:}||^2=mu^2m/d. For each offered mask,

U_Omega^T U_Omega=sum_j S_j u_j u_j^T,

where the independent summands lie between zero and rho I_m and their sum has expectation pI_m. Matrix Chernoff with a=1/4 gives failure probability at most m exp(-p/(32rho)) for the lower bound 3p/4. With C_mu sufficiently large, the public condition p>=C_mu rho log(8mTK/delta) and a union bound give this lower bound for all TK masks with failure probability at most alpha.

Intersect this event with the covariance event. The resulting event E_rep has failure probability at most 2alpha, hence at most delta/2. In particular, E_rep explicitly includes simultaneous positive definiteness of all true observed Gram matrices. This event is defined under the original probability law; it will not be used to condition the noise concentration argument.

Fix a post-burn-in mask. The true observed Gram is positive definite, so |Omega|>=m. Its eigenvalues are the top m eigenvalues of the restricted projector R_Omega P R_Omega^T. The analogous statement, allowing zero eigenvalues, holds for the estimated projector. Weyl's inequality and ||R_Omega||<=1 give

lambda_min(Uhat_{e,Omega}^T Uhat_{e,Omega}) >= 3p/4-epsilon_{tau_e-1} >= p/2.

In particular, the singular-matrix fallback is never used on E_rep.

Write epsilon_e=epsilon_{tau_e-1}. Right-orthogonal rotation of Uhat leaves the imputed vector unchanged. Analyze an aligned basis with ||Uhat-U||<=epsilon_e. Write X=Ua, so ||a||<=B_X, and let Ghat=Uhat_Omega^T Uhat_Omega. The normal equations imply

Ghat(ahat-a)=Uhat_Omega^T(U_Omega-Uhat_Omega)a.

Using ||Ghat^{-1}||<=2/p and ||Uhat_Omega||<=1 gives ||ahat-a||<=2B_X epsilon_e/p. Observed entries are copied exactly, while on missing coordinates

||U_{Omega^c}a-Uhat_{Omega^c}ahat|| <= B_X epsilon_e+||ahat-a||.

Uniformly over all epoch arms,

||X-Xhat|| <= (1+2/p)B_X epsilon_e.

## 3. Surrogate approximation and confidence

Fix an epoch and define vartheta_e*=Uhat_e^T theta*, with ||vartheta_e*||<=S. Its surrogate mean is z_{t,i}^T vartheta_e*=<Phat_e Xhat_{t,i},theta*>. Since PX=X,

X-Phat_e Xhat=(P-Phat_e)X+Phat_e(X-Xhat).

On E_rep this yields

|X_{t,i}^T theta*-z_{t,i}^T vartheta_e*| <= b_e,

where b_e=SB_X(2+2/p)epsilon_e. This b_e is the coefficient appearing in the public radius; the approximation inequality itself was not assumed in the task. Thus played rewards satisfy r_s=z_s^T vartheta_e*+xi_s+eta_s with |xi_s|<=b_e on E_rep.

For q=t-tau_e, let Z have columns z_{tau_e},...,z_{t-1}, and let xi be the vector of the corresponding errors. An SVD of Z shows that the eigenvalues of Z^T(lambda I+ZZ^T)^{-1}Z are sigma_j^2/(lambda+sigma_j^2) and zeros. Therefore this matrix lies between zero and I_q, and

||sum_{s=tau_e}^{t-1}z_s xi_s||_{V_{e,t}^{-1}}^2 <= ||xi||^2 <= b_e^2q.

For q=0 both sides are zero.

### Adapted noise localization

The selected feature is measurable before the current reward, but that alone is insufficient to apply self-normalization to eta_s: past observed rewards need not reveal past noises when ideal selected actions remain unidentified. We construct a process satisfying all the filtration hypotheses without changing the algorithm or the public assumptions.

Fix the environment throughout the argument. The matrices U and the vector theta* are deterministic constants. Unknown constants can occur as coefficients in a measurable function without being supplied to the learner.

For the selected arm at round s, write Omega_s=Omega_{s,I_s} and define

J_s=1{U_{Omega_s}^T U_{Omega_s} is invertible}.

This is H_s-measurable because the selected index and its mask are available before the reward. Define the proof-only vector

X_s^o=U(U_{Omega_s}^T U_{Omega_s})^{-1}U_{Omega_s}^T X_{s,I_s,Omega_s}

when J_s=1, and X_s^o=0 otherwise. This is a measurable function of the selected observed coordinates and mask, with the fixed U as a coefficient. On J_s=1, writing X_{s,I_s}=Ua shows X_s^o=X_{s,I_s} exactly.

Set

eta_s^o=J_s(r_s-(X_s^o)^T theta*).

This variable is measurable with respect to A_s:=sigma(H_s,r_s). It equals J_s eta_s on every sample path, up to the almost-sure action-support condition. In particular, it is zero when J_s=0, without needing to recover the missing ideal action. Since J_s is H_s-measurable, for every real a,

E[exp(a eta_s^o)|H_s]

=1-J_s+J_s E[exp(a eta_s)|H_s]

<=1-J_s+J_s exp(a^2R^2/2)

<=exp(a^2R^2/2).

Histories satisfy A_s subset H_{s+1} for s<T. Define H_{T+1}=A_T and F_{s-1}=H_s for s=1,...,T+1. These sigma-fields form a filtration. The feature z_s is F_{s-1}-measurable, eta_s^o is F_s-measurable, and the displayed conditional moment bound is with respect to F_{s-1}. All earlier localized noise increments are therefore measurable in the required histories. No hidden original noises or ideal actions have been adjoined to the filtration.

Apply the stated self-normalized theorem within epoch e to x_s=z_s and nu_s=eta_s^o, using the original design matrices V_{e,t}. The completed public algorithm supplies finite features on every sample path. We obtain an event N_e with P(N_e^c)<=delta_e such that, simultaneously throughout the epoch,

||sum_{s=tau_e}^{t-1}z_s eta_s^o||_{V_{e,t}^{-1}}

<=R sqrt(2log(det(V_{e,t})^{1/2}/(det(lambda I)^{1/2}delta_e))).

This is an unconditional probability statement. On E_rep every true observed Gram is positive definite, hence J_s=1 and eta_s^o=eta_s at all epoch rounds. Thus on E_rep intersect N_e the same bound applies to the original noise sum. No additional failure probability is spent on localization, and the actual regression is not modified.

### Ridge confidence

On E_rep intersect N_e, ridge regression gives

V_{e,t}(hat(vartheta)_{e,t}-vartheta_e*)=-lambda vartheta_e*+sum_{s=tau_e}^{t-1}z_s xi_s+sum_{s=tau_e}^{t-1}z_s eta_s.

The inverse-design norm of the first term is at most sqrt(lambda)S; the other two terms have just been bounded. Hence

||hat(vartheta)_{e,t}-vartheta_e*||_{V_{e,t}} <= sqrt(lambda)S+R sqrt(2log(det(V_{e,t})^{1/2}/(det(lambda I)^{1/2}delta_e)))+b_e sqrt(t-tau_e)=beta_{e,t}.

If R=0, the conditional moment assumption forces eta_t=0 almost surely, and the same conclusion holds with zero noise term.

## 4. Optimism and within-epoch potential

On E_rep, ||z_{t,i}||<=B_e:=B_X[1+(1+2/p)epsilon_e]. Since epsilon_e<=p/32 and p<=1, B_e<=2B_X and lambda=4B_X^2>=B_e^2.

Let ell_t=||z_t||_{V_{e,t}^{-1}}. Then ell_t^2<=1. The rank-one update and determinant lemma imply

log(det(V_{e,t+1})/det(V_{e,t}))=log(1+ell_t^2)>=ell_t^2/2.

Writing V_end=lambda I+sum_{t in epoch}z_tz_t^T and Gamma_e=log(det(V_end)/det(lambda I)), we obtain

sum ell_t^2<=2Gamma_e,  sum ell_t<=sqrt(2n_e Gamma_e).

The arithmetic-geometric mean inequality applied to the positive eigenvalues of V_end gives

Gamma_e<=m log(1+n_e B_e^2/(m lambda))<=G_T:=m log(1+T/m).

On the confidence event, every surrogate mean lies between its fitted mean plus or minus beta_{e,t} times its width. Maximization of the public index therefore bounds the best surrogate mean minus the selected surrogate mean by 2beta_{e,t}ell_t. Each true mean differs from its surrogate by at most b_e, so true instantaneous regret is at most 2beta_{e,t}ell_t+2b_e.

Set H_e=2log(1/delta_e). The non-misspecification portion of beta_{e,t} is at most sqrt(lambda)S+R sqrt(Gamma_e+H_e). Also,

sum_{t in epoch}sqrt(t-tau_e)ell_t <= sqrt(n_e(n_e-1)/2) sqrt(2Gamma_e) <= n_e sqrt(Gamma_e).

Summing the instantaneous bound yields

R_e <= 2sqrt(2)S sqrt(lambda Gamma_e n_e)+2sqrt(2)R sqrt(Gamma_e(Gamma_e+H_e)n_e)+2b_e n_e(sqrt(Gamma_e)+1).

Every post-burn-in epoch has tau_e>=2, hence tau_e-1>=tau_e/2. Define

A_rep=4sqrt(2)C_a SB_X(kappa/p^2)sqrt(mL/K).

Since 2+2/p<=4/p, b_e<=A_rep/sqrt(tau_e). Consequently

R_e <= 2sqrt(2)S sqrt(lambda G_T n_e)+2sqrt(2)R sqrt(G_T(G_T+H_e)n_e)+2A_rep(sqrt(G_T)+1)n_e/sqrt(tau_e).

## 5. Probability, doubling, and burn-in

If there are N>0 nonempty epochs, delta_e=delta/(2N), so sum_e P(N_e^c)<=delta/2. These N_e are the localized-noise events constructed above. Thus

P(E_rep intersect all N_e)>=1-P(E_rep^c)-sum_e P(N_e^c)>=1-delta.

This is an unconditional union bound; it needs no independence between the events. On the intersection, localization coincides with the original noises and all the original confidence and regret inequalities hold. Put H=2log(2N/delta). Since tau_e=2^e(t_b+1), n_e<=tau_e, and the last nonempty start is at most T,

sum_e sqrt(n_e)<=sum_e sqrt(tau_e)<=sqrt(T)/(1-2^{-1/2})<=4sqrt(T),

and sum_e n_e/sqrt(tau_e)<=4sqrt(T). Therefore the total post-burn-in regret is at most

8sqrt(2)S sqrt(lambda G_T T)+8sqrt(2)R sqrt(G_T(G_T+H)T)+8A_rep(sqrt(G_T)+1)sqrt(T).

Each actual burn-in round costs at most 2SB_X. Retain the ceiling explicitly:

2SB_X min(t_b,T)<=2SB_X+2C_b SB_X kappa^2m L/(p^4K).

The additive 2SB_X is at most 2(R+SB_X)m sqrt(T), since m,T>=1. Furthermore N=O(1+log T), G_T<=m log(1+T), and L=log(16dT/delta). Substitution of lambda and A_rep consequently gives

R_T=tilde O_delta(SB_X kappa^2m/(p^4K)+(R+SB_X)m sqrt(T)+SB_X kappa m sqrt(T)/(p^2 sqrt(K))),

with only universal constants and logarithmic factors in d,T,K,1/delta hidden.

If t_b>=T, every round is burn-in and R_T<=2SB_X T<=2SB_X t_b. The same ceiling-aware bound proves the target deterministically, without defining an epoch confidence level. If S=0, all regret is zero. K=1 likewise gives zero regret. All denominators used above are positive in their stated domains.

## Repairs retained and completed

The prior empty-epoch convention and the correction of the basis-alignment SVD typo remain in force. The global-event conditional confidence assertion is replaced by separate noise events and intersection, and the burn-in ceiling is retained before absorption into an existing term. The noise-event construction now explicitly verifies adaptedness through localization to invertible true observed Grams. This is a proof-only construction; it changes neither the learner's information nor its actions. There are no unresolved proof obligations.
