# Reference Proof

## Contract and proof obligations

The task is conditional on the specified event E. In particular, its two local direction guards, pathwise curvature, score control, and direction bound are hypotheses. The task does not ask the solver to derive the probability of this entire adaptive-path event from the distributional assumptions alone.

The obligations are: establish candidate/error support containment; jointly prove cone and radius invariance without circularly applying local hypotheses after an exit; handle endpoint thresholding; derive and iterate the squared-error recursion without assuming unstated step-size restrictions; quantify Phase I contraction; and sum the harmonic-step recursion. All are closed below.

The externally cited additive-tolerance curvature result is not used. It would not imply the stronger pathwise curvature assumption in the task.

## 1. Support and provisional trajectories

Fix a sample point in E and a post-burn-in epoch j. Define the provisional trajectory by z_{tau_j}=beta_{tau_j} and z_{t+1}=z_t-eta_t d_t for t in T_j. Thus z_t=beta_t for tau_j<=t<tau_{j+1}, and z_{tau_{j+1}}=tilde beta_{tau_{j+1}} is the provisional endpoint. Let e_t=z_t-beta* for tau_j<=t<=tau_{j+1}.

Since supp(beta_{tau_j}) and S are contained in A_j, and every direction during the epoch is supported on A_j, induction gives supp(z_t) subseteq A_j and supp(e_t) subseteq A_j. Inside the epoch z_t=beta_t, including the input to its final update. Consequently, at every update,

<d_t,Delta_t>=<gbar_t(beta_t),Delta_t>.

This uses both active-support containment and true-support coverage. True-support coverage by itself would not suffice.

## 2. Joint cone and radius induction

Write

a_t=||e_{t,S^c}||_1, b_t=||e_{t,S}||_1, D_t=b_t+zeta, r_t=a_t/D_t.

Here D_t>0 because zeta>0. At the epoch start, r_{tau_j}<=c_small and ||e_{tau_j}||_2<=R_in<R.

Suppose all preceding provisional states through t are in the large cone and radius R. The local guards are therefore available for all preceding updates, including the update at t. Triangle and reverse-triangle inequalities give

a_{t+1}<=a_t+eta_t L_off D_t,

D_{t+1}>=D_t-eta_t L_on D_t=(1-eta_t L_on)D_t.

The latter denominator is positive since eta_t L_on<=1/2. Thus

r_{t+1}<= (r_t+eta_t L_off)/(1-eta_t L_on)
          = r_t+eta_t(L_off+L_on r_t)/(1-eta_t L_on)
          <=r_t+2eta_t(L_off+c_large L_on).

Summing only already justified updates yields

r_{t+1}<=c_small+2(L_off+c_large L_on) sum_{u=tau_j}^t eta_u<=c_large.

For the radius, at each already controlled state,

||d_u||_2<=||d_u||_1
 <=(L_off+L_on)(||e_{u,S}||_1+zeta)
 <=(L_off+L_on)(sqrt(s0)R+zeta).

Hence

||e_{t+1}||_2<=R_in+(L_off+L_on)(sqrt(s0)R+zeta) sum_{u=tau_j}^t eta_u<=R.

Both bounds follow at t+1 from bounds only through t. This simultaneous induction proves invariance through the provisional endpoint. Equality in either budget is harmless. The argument applies separately to every epoch, using the explicitly assumed small-cone/R_in condition at each epoch start; it does not infer that stronger reset condition from large-cone invariance.

## 3. Endpoint thresholding

Let v=z_{tau_{j+1}} and U=supp(H_s(v)). On E, S subseteq U. Since beta* vanishes on U^c,

||H_s(v)-beta*||_2^2=||(v-beta*)_U||_2^2<=||v-beta*||_2^2.

Moreover, H_s leaves every coordinate in S unchanged, while it can only delete off-support coordinates. Thus its on-support error l1 norm is unchanged and its off-support error l1 norm cannot increase. The thresholded endpoint also belongs to the large inflated cone and has error norm at most R.

For completeness, the familiar sufficient beta-min condition follows directly: if ||v-beta*||_2<beta_min/2, every true coordinate has magnitude greater than beta_min/2 and every null coordinate has magnitude less than beta_min/2. Therefore H_s retains S whenever s>=s0. This sufficient condition is not needed because support preservation is already assumed.

## 4. One-step and epoch error bounds

Set E_t=||Delta_t||_2^2 and C=C_sc+G^2. Expand a provisional update and use Section 1:

||Delta_t-eta_t d_t||_2^2
=E_t-2eta_t<gbar_t(beta_t),Delta_t>+eta_t^2||d_t||_2^2.

Split the gradient into its difference from gbar_t(beta*) and the truth score. The two assumed inequalities and ||d_t||_2<=G imply

||Delta_t-eta_t d_t||_2^2
 <=(1-3mu eta_t/2)E_t+C eta_t^2
 <=(1-mu eta_t)E_t+C eta_t^2.

Endpoint thresholding does not increase squared error, so

E_{t+1}<=(1-mu eta_t)E_t+C eta_t^2

holds for every post-burn-in update. No assumption mu eta_t<=1 has been imposed. To iterate safely, use E_t>=0 and 1-mu eta_t<=exp(-mu eta_t) before making recursive substitutions:

E_{t+1}<=exp(-mu eta_t)E_t+C eta_t^2.

These exponential coefficients are positive and at most one. Therefore

E_{tau_{j+1}}
 <=exp(-mu B_j)E_{tau_j}
   +C sum_{u in T_j} eta_u^2 exp(-mu sum_{v in T_j,v>u}eta_v)
 <=exp(-mu B_j)E_{tau_j}+C sum_{u in T_j}eta_u^2.

This proves the epoch bound, including for an epoch containing large steps allowed by the stated budgets.

If B_j>=B_min>0, put a=exp(-mu B_min)<1. Taking square roots and using sqrt(x+y)<=sqrt(x)+sqrt(y) gives

||Delta_{tau_{j+1}}||_2<=sqrt(a)||Delta_{tau_j}||_2+sqrt(C)(sum_{t in T_j}eta_t^2)^{1/2}.

This is geometric contraction up to the specified stochastic tolerance. If q is fixed with a<q<1 and C sum_{t in T_j}eta_t^2<=(q-a)E_{tau_j}, then E_{tau_{j+1}}<=q E_{tau_j}. Repetition gives geometric squared-error decay with factor q and norm decay with factor sqrt(q). A lower bound on epoch mass alone does not justify dropping the remainder.

## 5. Harmonic-step phase

Let t0=T0+1, n_t=t+b2, a=mu/c_eff>=1, and D=C/c_eff^2. The non-exponential one-step inequality gives

E_{t+1}<=(1-a/n_t)E_t+D/n_t^2.

Multiply by n_t+1>0. Since E_t>=0 and

(n_t+1)(1-a/n_t)=n_t+1-a-a/n_t<=n_t,

we obtain, using n_t>=2,

n_{t+1}E_{t+1}<=n_t E_t+2D/n_t.

This comparison does not require 1-a/n_t to be nonnegative. Summation from t0 to t-1 yields

n_t E_t<=n_{t0}E_{t0}+2D sum_{u=t0}^{t-1}1/(u+b2)
         <=n_{t0}R^2+2D(1+log n_t).

Because log n_t>=log 2, one admissible constant is

C'=(n_{t0}R^2+2D)/log 2+2D.

Thus E_t<=C' log(t+b2)/(t+b2) throughout Phase II, and taking square roots gives the corresponding norm rate. The initial case t=t0 is included. Constants do not depend on t; their dependence on the fixed local parameters and the phase-start time is explicit.

## 6. Audited upstream statistical material

This section records the source-local repairs, not additional obligations of the conditional public task.

The standard concentration fact used here is the following: if independent centered real variables Z_i satisfy ||Z_i||_{psi2}<=B, then for an absolute c>0,

Pr(|W^{-1}sum_{i=1}^W Z_i|>u)<=2 exp(-cWu^2/B^2).

This is the independent centered sub-Gaussian average inequality used in the source. Each application below verifies independence, centering, and a uniform psi2 envelope. No independence across different windows is needed.

At beta*, each score summand Z_ik=X_ik(tau-1{epsilon_i<=0}) is centered by the conditional quantile assumption and has absolute value at most |X_ik|. Independent observations give independence across i, and ||Z_ik||_{psi2}<=K. The tail bound therefore gives probability at most 2 exp(-cWu^2/K^2) for a fixed coordinate and window. A union bound over p coordinates and at most T windows gives

Pr(max_{W<=t<=T}||gbar_t(beta*)||_infinity>u)
 <=2pT exp(-cWu^2/K^2).

Taking u=(K/sqrt(c))sqrt(log(2pT/delta)/W) makes this at most delta. Overlap between windows does not invalidate this union bound. For a single fixed window, the corresponding bound uses log(2p/delta).

The factor 2 inside the logarithm cannot be suppressed uniformly over the entire stated parameter domain. Indeed, if p=T=W=1, X_1 is Rademacher, epsilon_1 is independent Uniform[-1,1], and tau=1/2, then ||gbar_1(beta*)||_infinity=1/2 almost surely. For any fixed A, A K sqrt(log(1/delta)) is less than 1/2 when delta is sufficiently close to one. Thus the uncorrected bound fails even though its promised success probability 1-delta is positive.

For either coordinatewise gradient lemma, fix deterministic beta and Delta. Define

V_ik=X_ik(1{epsilon_i<=X_i^T Delta}-1{epsilon_i<=0}).

The density upper bound must be the global constant M1. It implies

|E V_ik|<=M1 E|X_ik X_i^T Delta|
 <=M1 sqrt(E X_ik^2) sqrt(E(X_i^T Delta)^2)
 <=C M1 K^2||Delta||_2.

For the ordinary cone, ||Delta||_2<=||Delta||_1<=(1+c)||Delta_S||_1. Also |V_ik|<=|X_ik|, so V_ik-E V_ik are independent centered sub-Gaussian variables with parameter at most CK. Allocate failure probability delta/2 to their coordinatewise average bound and delta/2 to the fixed-window truth-score bound. Both thresholds can be taken of order K sqrt(log(4p/delta)/W). Because

log(4p/delta)<=2log(2p/delta),

their sum is bounded by C0 sqrt(log(2p/delta)/W), with C0 proportional to K. Combining this with the mean estimate proves, pointwise in deterministic beta, both coordinatewise bounds with this corrected stochastic term. This avoids the source's invalid removal of observation-dependent density weights from signed covariance sums and its uncontrolled full off-support Gram blocks.

The on-support lemma requires this confidence normalization throughout p>=1: at beta=beta* the preceding p=1 example applies directly. Its source window condition W>=C log(p/delta) does not eliminate the example, since W=1 satisfies it when delta is sufficiently close to one.

The off-support lemma's original log(p/delta) form can still be retained. If p=1, S is nonempty and S^c is empty, so the off-support norm is zero. If p>=2, then

log(4p/delta)<=3log(p/delta),

so all confidence prefactors can be absorbed into a fixed multiplicative constant in that lemma. No counterexample to its off-support statement is supplied by the p=1 case.

For an inflated cone the elementary mean comparison instead uses ||Delta||_1<=(1+c)||Delta_S||_1+c zeta; the additive term cannot simply be omitted. More importantly, none of these pointwise concentration arguments establishes simultaneous control over beta selected from the same overlapping windows. The reference proof makes no such claim.

Conditional on coordinatewise controls already holding with a common stochastic allowance sigma_W, candidate restriction gives

||d_{S^c}||_1<=(s+m)(rho||Delta_S||_1+sigma_W),

||d_S||_1<=s0(L_g||Delta_S||_1+sigma_W).

For zeta>=sigma_W this yields the guards with L_off=(s+m)max{rho,1} and L_on=s0 max{L_g,1}. When invoking the corrected fixed-beta concentration bounds, one may use sigma_W=C0 sqrt(log(2p/delta)/W), with the appropriate confidence allocation included in C0.

The public task uses the local guards themselves because they are expressly part of the source theorem's conditional local-event contract. Their probability is stipulated, not inferred from this pointwise calculation. In particular, this proof does not assert that the public zeta=C_zeta sqrt(log(pT/delta)/W) universally dominates the corrected concentration allowance for a parameter-uniform C_zeta when pT=1 and delta approaches one. No such assertion is needed in Sections 1–5, which use only zeta>0 and the explicitly assumed guards.
