# Reference Proof

## Proof Structure

Center the affine proxy at the specified regularized stationary point. The first-order condition and invertibility of the expected drift coefficient make the stationary mean equal to that point. Conditional centering of the minibatch sampling noise then gives the stationary covariance recursion and its expanded discrete Lyapunov identity. Compute the minibatch covariance directly for both sampling schemes, average its affine-gradient expansion over the stationary centered state, and use the first-order condition to obtain the exact score-moment, Hessian-covariance, and regularizer-correction formula. Substitution closes the covariance-tuning relation.

## Complete Proof

### step_001: Centering and stationary mean

Write `x_t=psi_t-theta_hat`, and let `mu_x=E[x_t]` in a stationary version of the chain. For `x in R^d`, set
`a_n(x)=g_n+J_n x`,
`g_S(x)=B^{-1}sum_{b=1}^B a_{I_{tb}}(x)`,
`g-bar=N^{-1}sum_n g_n`, and
`a-bar(x)=N^{-1}sum_n a_n(x)=g-bar+Jx`.

The first-order condition is `g-bar+Gamma theta_hat/N=0`. In either sampling scheme each sampled index has the uniform marginal distribution. Fresh sampling is independent of the pre-update state, so
`E[G_t(theta_hat+x)|x]=g-bar+Jx+Gamma(theta_hat+x)/N=H-hat x`.
Consequently stationarity and the zero mean of the Gaussian innovation give
`mu_x=(I_d-Lambda H-hat)mu_x`.
The assumed invertibility of `Lambda H-hat` implies `mu_x=0`. Thus `E[psi_t]=theta_hat` and `Sigma_psi=E[x_t x_t^T]`.

All quantities in these calculations are integrable: the stationary state has finite second moment and the finitely many vectors `g_n` and matrices `J_n` are fixed and finite. In particular, affine functions of the state have finite second moments.

### step_002: Conditional sampling noise

Define
`eta_t=g_S(x_{t-1})-a-bar(x_{t-1})`.
The deterministic regularizer cancels when the stochastic gradient is conditionally centered. Therefore
`E[eta_t|x_{t-1}]=0`
and
`E[eta_t eta_t^T|x_{t-1}]=C_psi(x_{t-1})`,
where `C_psi(x)=Cov_S(g_S(x)|x)`. Its stationary expectation is the public quantity `C-bar_psi`.

The centered update becomes
`x_t=(I_d-Lambda H-hat)x_{t-1}-Lambda eta_t+sqrt(2 beta^{-1}Lambda)xi_{t-1}`.
Conditional mean zero implies
`E[x_{t-1}eta_t^T]=E[x_{t-1}E[eta_t^T|x_{t-1}]]=0`.
The transpose cross moment is also zero. The fresh Gaussian vector is independent of the state and batch, so its cross moments with both other terms vanish. No independence between `eta_t` and the state is asserted or needed.

### step_003: Stationary covariance identity

Taking second moments in the centered update and using stationarity gives
`Sigma_psi=(I_d-Lambda H-hat)Sigma_psi(I_d-Lambda H-hat)^T+Lambda C-bar_psi Lambda+2 beta^{-1}Lambda`.
The Hessians, `H-hat`, and `Lambda` are symmetric. Expand the first term without interchanging matrix factors:
`(I_d-Lambda H-hat)Sigma_psi(I_d-H-hat Lambda)=Sigma_psi-Lambda H-hat Sigma_psi-Sigma_psi H-hat Lambda+Lambda H-hat Sigma_psi H-hat Lambda`.
Canceling `Sigma_psi` and rearranging proves
`Lambda H-hat Sigma_psi+Sigma_psi H-hat Lambda=Lambda(C-bar_psi+H-hat Sigma_psi H-hat)Lambda+2 beta^{-1}Lambda`.

### step_004: Conditional covariance in both sampling schemes

Fix `x`. Define `z_n=a_n(x)-a-bar(x)` and
`V(x)=N^{-1}sum_n z_n z_n^T=N^{-1}sum_n a_n(x)a_n(x)^T-a-bar(x)a-bar(x)^T`.
We have `sum_n z_n=0`.

With replacement, the sampled centered vectors are independent, mean zero, and have second moment `V(x)`. Expanding the outer product of their average gives
`C_psi(x)=B^{-2}sum_{b=1}^B E[z_{I_{tb}}z_{I_{tb}}^T]=V(x)/B`;
all terms with distinct draw positions vanish by independence and centering.

Without replacement, each diagonal term still has expectation `V(x)`. For two distinct draw positions, the ordered pair of indices is uniform over distinct population indices, and hence
`E[z_{I_{tb}}z_{I_{tc}}^T]=[N(N-1)]^{-1}sum_{n!=m}z_n z_m^T=-V(x)/(N-1)`.
Here the last equality follows from
`sum_{n!=m}z_n z_m^T=(sum_n z_n)(sum_m z_m)^T-sum_n z_n z_n^T=-N V(x)`.
It follows that
`C_psi(x)=B^{-2}[B V(x)-B(B-1)V(x)/(N-1)]=(N-B)V(x)/[B(N-1)]`.
This calculation also covers `B=1`; there are then no distinct-position terms. At `B=N`, without-replacement sampling has covariance zero, as the displayed coefficient states.

### step_005: Stationary averaging and closure

Using `E[x]=0` and `E[xx^T]=Sigma_psi`, expand the affine outer products to obtain
`E[a_n(x)a_n(x)^T]=g_n g_n^T+J_n Sigma_psi J_n^T`
and
`E[a-bar(x)a-bar(x)^T]=g-bar g-bar^T+J Sigma_psi J^T`.
The terms linear in `x` vanish because its mean is zero. Therefore
`E[V(x)]=mathcal I+N^{-1}sum_n J_n Sigma_psi J_n^T-g-bar g-bar^T-J Sigma_psi J^T`.
The first-order condition gives `g-bar=-Gamma theta_hat/N`, so
`g-bar g-bar^T=Gamma theta_hat theta_hat^T Gamma^T/N^2`.

Consequently, if
`Q(Sigma)=mathcal I-Gamma theta_hat theta_hat^T Gamma^T/N^2+N^{-1}sum_n J_n Sigma J_n^T-J Sigma J^T`,
then
`C-bar_psi=c_B Q(Sigma_psi)`,
where `c_B=1/B` with replacement and `c_B=(N-B)/[B(N-1)]` without replacement. These are exactly the two requested noise formulas. Substituting them into the covariance identity gives the closed relation
`Lambda H-hat Sigma_psi+Sigma_psi H-hat Lambda=Lambda[c_B Q(Sigma_psi)+H-hat Sigma_psi H-hat]Lambda+2 beta^{-1}Lambda`.

When `beta=infinity`, the Gaussian coefficient and its covariance contribution are zero; every preceding equality remains valid directly, without a limiting argument. The proof does not require invertibility of `Sigma_psi`, uniqueness of the stationary distribution, or commutation of any matrices. Existence and finite second moment of the stationary law are hypotheses, not conclusions. The closed relation is a necessary identity for that law; no additional solvability or uniqueness assertion is made.

## Source Audit Notes

The ambient parameter domain, sampling conventions, and noise normalization come from L000049-L000061. The positive-definite Gaussian regularizer is specified in L000125. L000326 confirms that convexity is not required for this covariance/noise chain.

The repaired stationary-mean hypothesis already recorded under theory_015 is retained. Invertibility of `Lambda H-hat` is used explicitly; it is not inferred from positive definiteness of `Gamma` alone for potentially nonconvex losses.

For theory_006, the expectation in the sampling-noise centering is interpreted conditionally on the pre-update state, consistent with L000869-L000870 and L000968-L000969. The intermediate `J-Gamma/N` in L000818 is corrected to `J+Gamma/N`, as required by L000815 and the immediately following lines of L000818.

For theory_007, the previously recorded statement corrections are retained. Additionally, the covariance bracket in L000829 must subtract the outer product of the mean observation-loss gradient, not the regularized objective gradient while leaving the first term unregularized. Thus the subtracted vector is `N^{-1}sum_n grad tilde ell_n(psi)=grad tilde L(psi)-Gamma psi/N`. The affine expansion in L000833 is understood with the Taylor gradients and with the sum covering both `g_n` and `J_n x`. L000836-L000842 uniquely confirm this correction and the final matrix formula. All repairs are local; no specialized external theorem is needed.
