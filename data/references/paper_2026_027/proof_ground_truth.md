# Reference Proof

## Proof Structure

The proof identifies the population and empirical rank, integrates the Gaussian likelihood over active and likelihood-flat coordinates, controls the stochastic evidence remainder directly, and compares the result with the ordinary `d/2` BIC penalty. It does not require an application of a general singular-learning expansion.

## Complete Proof

Let `mu=E[u_1]` and set

`Gamma=E[u_1u_1^T]=Sigma+mu mu^T`.

Because `Sigma` is positive definite, so is `Gamma`. Let `U_n` have rows `u_i^T` and define

`C_n=M^TU_n^TU_nM`.

Every product of two input coordinates is integrable by the finite second-moment assumption and Cauchy-Schwarz. The entrywise strong law therefore gives

`n^{-1}C_n -> H:=M^T Gamma M`

almost surely. Since `Gamma` is positive definite and `rank(M)=r`, `H` has rank `r` and is positive definite on `ker(M)^perp`. Eigenvalue continuity shows that the largest `r` eigenvalues of `C_n`, divided by `n`, converge to positive constants. Moreover, `rank(C_n)<=r` for every `n`, so the other `d-r` eigenvalues are exactly zero. In particular, the empirical rank is `r` eventually almost surely, although it can be smaller for early samples.

Choose matrices `T in R^{d x r}` and `N in R^{d x (d-r)}` whose columns form orthonormal bases for `ker(M)^perp` and `ker(M)`. Write

`beta=T gamma+N zeta`,

and put `gamma_0=T^T beta_0`. Since `MN=0`, the likelihood depends only on `gamma`. The isotropic Gaussian prior factorizes in these orthogonal coordinates, and integrating its `zeta` density gives one. When `r=d`, the flat coordinate space has dimension zero and this factor is still one.

The population conditional KL contrast is

`E[(u_1^T M(beta-beta_0))^2]/(2nu^2)=(beta-beta_0)^T H(beta-beta_0)/(2nu^2)`.

Thus it is exactly quadratic in the `r` active coordinates and zero in the flat coordinates. We establish its evidence exponent directly below.

Put `D_n=U_nMT`, `J_n=nu^{-2}D_n^TD_n`, and `s_n=nu^{-2}D_n^T eta`, where `eta=(eta_1,...,eta_n)^T`. For `h=gamma-gamma_0`,

`ell_n(gamma_0+h)-ell_n(gamma_0)=s_n^T h-(1/2)h^T J_n h`.

Here the likelihood in active coordinates is the same likelihood as in the original parameterization, and `ell_n(gamma_0)=ell_n(beta_0)`. Consequently,

`Z_n=exp(ell_n(beta_0)) integral exp(s_n^T h-(1/2)h^T J_n h) phi_{kappa,r}(gamma_0+h) dh`,

where `phi_{kappa,r}` is the normalized `N(0,kappa^2 I_r)` density.

Let

`K_n=J_n+kappa^{-2}I_r`,  `b_n=s_n-kappa^{-2}gamma_0`.

The matrix `K_n` is positive definite for every sample, including samples with deficient empirical rank. Completing the square gives the exact identity

`log Z_n-ell_n(beta_0)=-r log kappa-(1/2)log det(K_n)-||gamma_0||^2/(2kappa^2)+(1/2)b_n^T K_n^{-1}b_n`.

The Gram convergence implies

`J_n/n -> G:=nu^{-2}T^T H T`

almost surely, where `G` is positive definite. Therefore

`log det(K_n)-r log n -> log det(G)`

almost surely.

Conditionally on the inputs, `s_n` is centered Gaussian with covariance `J_n`. Since `0 <= J_n <= K_n`,

`E[s_n^T K_n^{-1}s_n | inputs]=tr(K_n^{-1}J_n)<=r`.

Also `K_n^{-1} <= kappa^2 I_r`. The quadratic-form inequality for a difference of two vectors gives

`0 <= b_n^T K_n^{-1}b_n <= 2s_n^T K_n^{-1}s_n+2kappa^{-4}gamma_0^T K_n^{-1}gamma_0`

`<=2s_n^T K_n^{-1}s_n+2kappa^{-2}||gamma_0||^2`.

Taking expectations and applying Markov's inequality proves

`b_n^T K_n^{-1}b_n=O_p(1)`.

Substitution into the exact identity yields

`log Z_n=ell_n(beta_0)-(r/2)log n+O_p(1)`.

Equivalently, `n^{r/2}Z_n exp(-ell_n(beta_0))` and its reciprocal are tight. In the expansion used to define the RLCT in the task, a different coefficient of `log n`, or a nonzero coefficient of `log log n`, would leave a diverging deterministic term rather than an `O_p(1)` remainder. Hence `lambda(r)=r/2` and there is no `log log n` term; the multiplicity is one.

It remains to compare the evidence with the maximized likelihood. Let `P_n` be the orthogonal projection onto the column space of `U_nM`. Least-squares fitted values exist for every sample and are unique even when the maximizing parameter is not. Because `U_nM beta_0` belongs to that column space, every maximum-likelihood estimator satisfies

`ell_n(hat beta_n)-ell_n(beta_0)=(2nu^2)^{-1}||P_n eta||^2`.

Conditionally on the inputs, `nu^{-2}||P_n eta||^2` has a chi-squared distribution with `rank(U_nM)<=r` degrees of freedom, with the zero-rank case interpreted as a point mass at zero. Its conditional expectation is at most `r`, so the likelihood improvement is `O_p(1)`. No convergence of an arbitrary parameter representative is needed.

Using the definition of `Q_n`,

`Q_n-log Z_n`

`=ell_n(hat beta_n)-ell_n(beta_0)-(d/2)log n+(r/2)log n+O_p(1)`

`=-((d-r)/2)log n+O_p(1)`.

For `r<d`, the score is below the log evidence by `(d-r)log(n)/2` up to a tight remainder, giving the claimed over-penalization. For `r=d`, the logarithmic discrepancy vanishes and the difference remains `O_p(1)`.
