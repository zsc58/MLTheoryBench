# Reference Proof

## Complete Proof

All expectations are for the experiment in the public setup. A latent index is uniform on the listed data matrices, including their multiplicities. We use column vectorization, which identifies the Frobenius norm with the Euclidean norm on R^{nm}.

### 1. Conditional laws and positive-time bounds

Fix a data matrix G. The operator matrices are finite and symmetric. The zero-overlap-degree convention is valid even if an overlap graph has isolated vertices. In particular, its quadratic form is the sum of x_j^2 over zero-degree indices and one half of the weighted squared differences over positive-degree indices, so this boundary case causes no singular operator definition.

Put d=nm, x=vec(X), g=vec(G), and mu=vec(bar M). Define

B_s(G)=alpha(s)(I_m tensor L_V(G)+L_E(G) tensor I_n)+beta(s)gamma I_d.

This matrix is continuous and bounded on [0,S]. Let Phi_G(s,r) solve partial_s Phi_G(s,r)=-B_s(G)Phi_G(s,r), with Phi_G(r,r)=I_d. Standard linear ODE existence gives a continuous invertible transition matrix. The variation-of-constants calculation gives

x_s=Phi_G(s,0)g+integral_0^s Phi_G(s,r)beta(r)gamma mu dr+sqrt(2tau)integral_0^s Phi_G(s,r)sqrt(beta(r))dw_r.

The stochastic integral has a deterministic integrand conditional on G. Consequently the conditional law is Gaussian with mean

m_s(G)=Phi_G(s,0)g+integral_0^s Phi_G(s,r)beta(r)gamma mu dr

and covariance

C_s(G)=2tau integral_0^s beta(r)Phi_G(s,r)Phi_G(s,r)^T dr.

For nonzero z and s>0,

z^T C_s(G)z=2tau integral_0^s beta(r)||Phi_G(s,r)^T z||^2 dr>0.

Here beta is strictly positive on (0,s] and Phi_G is invertible. Thus the conditional density p_s(·|G) is strictly positive and smooth in state. Its score is

r_{s|G}(X)=-mat(C_s(G)^{-1}(vec(X)-m_s(G))).

For each epsilon in (0,S), compactness and finiteness of the data list imply uniform bounds on all conditional means and covariances, and a uniform positive lower bound on covariance eigenvalues, for epsilon<=s<=S. The means and covariances are C1 in time. Hence the densities are C1 in time and smooth in state, their local derivatives are bounded uniformly on this interval, and their moments of every fixed order are uniformly finite. The conditional scores and conditional reverse targets are affine in state and satisfy uniform bounds K_epsilon(1+||X||_F).

At zero, Phi_G(s,0) tends to I, the deterministic forcing integral tends to zero, and tr C_s(G) tends to zero. Therefore E[||X_s-G||_F^2|G] tends to zero. Averaging the finite list gives E||X_s-G||_F^2 tending to zero.

### 2. Posterior and mixture-score identities

Write p_i(X)=p_s(X|G^i) at a fixed positive time. Every p_i is positive. Bayes' rule for the uniform latent index gives

pi_s(i|X)=p_i(X)/(sum_j p_j(X)).

This is valid with repeated matrices as well: the index, rather than the set of distinct matrices, is sampled uniformly. For any integrable component target h_i,

E[h_G(X_s)|X_s=X]=sum_i pi_s(i|X)h_i(X).

Differentiating the finite mixture gives

sum_i pi_s(i|X)r_{s|G^i}(X)
=(sum_i grad_X p_i(X))/(sum_j p_j(X))
=grad_X log p_hat_s(X).

No interchange with an infinite mixture or an unspecified expectation is involved.

Let b_s^G(X)=-alpha(s)A_G(X)-beta(s)gamma(X-bar M). The conditional target defined publicly is -b_s^G+2tau beta(s)r_{s|G}. Its posterior average is therefore

v_s(X)=alpha(s)E[A_G(X)|X_s=X]+beta(s)gamma(X-bar M)+2tau beta(s)grad_X log p_hat_s(X).

The OU term is unchanged by posterior averaging because bar M, gamma, and the schedule are common to all components. This defines a canonical continuous-in-time, smooth-in-state version at every positive time.

### 3. L2 minimization

Fix s>0 and put T=nu*_{s|G}(X_s). The affine conditional-target formula and the finite Gaussian experiment show E||T||_F^2<infinity. Let V=E[T|X_s]. Conditional Jensen gives E||V||_F^2<=E||T||_F^2, so the canonical field v_s belongs to the public minimization domain.

For any admissible state-only u,

J_s(u)=E||u(X_s)-V||_F^2+E||T-V||_F^2.

To derive this identity, expand u(X_s)-T=(u(X_s)-V)+(V-T). The cross term vanishes because u(X_s)-V is measurable with respect to X_s and E[V-T|X_s]=0. All terms are integrable by Cauchy-Schwarz.

The second term is independent of u. Thus v_s minimizes J_s, and equality with its minimum holds exactly when u(X_s)=V almost surely. This proves uniqueness modulo p_hat_s-null sets and the requested conditional-expectation and marginal-score expressions.

### 4. Averaged forward density equation

Each conditional Gaussian density satisfies

partial_s p_s(X|G^i)=-div_X(b_s^{G^i}(X)p_s(X|G^i))+tau beta(s)Delta_X p_s(X|G^i).

This can be obtained from the conditional SDE or directly from its Gaussian mean and covariance equations. Finite averaging and the posterior formula yield

partial_s p_hat_s=-div_X(b_bar_s p_hat_s)+tau beta(s)Delta_X p_hat_s,

where b_bar_s(X)=sum_i pi_s(i|X)b_s^{G^i}(X).

This calculation establishes a one-time marginal equation. It does not assert that the original process obtained by retaining a sampled G has a Markovian path law after the latent index is integrated out.

### 5. Audited standard background and its hypotheses

The standard-independent diffusion facts used here are the following localized statements. On a compact time interval, continuous coefficients with a drift locally Lipschitz in state and uniformly at most linearly growing, and continuous state-independent uniformly positive scalar diffusion covariance, give a nonexplosive SDE unique in law. The associated Fokker-Planck equation is unique among weakly continuous probability-measure solutions with uniformly finite second moments and a specified initial law. For such a diffusion with positive C1-in-time, smooth-in-state densities and finite drift energy and Fisher information on the interval, the additive-noise time-reversal formula gives reverse drift -b_s+a(s)grad log p_s, where a(s)I is the diffusion covariance. These are the standard representing-diffusion, density-equation uniqueness, and localized reversal facts used in the source's exactness argument, not paper-specific dependencies.

Here all these checks are available on [epsilon,S]. Posterior weights are ratios of positive smooth densities, so b_bar is continuous and locally Lipschitz in state. Since it is a convex combination of finitely many uniformly bounded affine drifts, ||b_bar_s(X)||_F<=K_epsilon(1+||X||_F). The diffusion covariance is a(s)I=2tau beta(s)I, continuous and uniformly positive on this interval. The mixture densities have uniformly finite moments by Step 1.

The mixture-score identity and conditional Jensen give

integral ||grad log p_hat_s||_F^2 p_hat_s dX
<=N^{-1}sum_i tr(C_s(G^i)^{-1}),

uniformly bounded for epsilon<=s<=S. Drift energy is bounded by the linear-growth estimate and the second moments. Thus reversal can be applied to the representing diffusion on this interval. The representing diffusion exists with initial law p_hat_epsilon, and Step 4 plus density-equation uniqueness identifies its one-time laws with p_hat_s.

The reverse drift v_s=-b_bar_s+2tau beta(s)grad log p_hat_s is itself a convex combination of the affine conditional targets. Consequently it is continuous, smooth and locally Lipschitz in state, and uniformly linearly growing on [epsilon,S]. These checks also permit a direct reverse-Fokker-Planck proof, given next.

### 6. Exact reverse marginals

Fix epsilon in (0,S), and let q_t(X)=p_hat_{S-t}(X) for 0<=t<=S-epsilon. Step 4 gives

partial_t q_t=div_X(b_bar_{S-t}q_t)-tau beta(S-t)Delta_X q_t.

Because v_s=-b_bar_s+2tau beta(s)grad log p_hat_s,

-div_X(v_{S-t}q_t)+tau beta(S-t)Delta_X q_t
=div_X(b_bar_{S-t}q_t)-tau beta(S-t)Delta_X q_t.

Thus q solves exactly the forward density equation for the reverse SDE, with initial law q_0=p_hat_S. It is a weakly continuous probability family with uniformly finite second moments. The reverse coefficients satisfy every hypothesis of the standard uniqueness statement in Step 5. Therefore the exact reverse SDE marginals are q_t. Equivalently, the localized time-reversal theorem applied to the representing forward diffusion gives the same conclusion. Neither argument identifies its path law with that of the original latent-conditioned mixture.

The reverse SDE in the public task uses this canonical v_s and has the specified initial law. Uniqueness in law identifies its restriction to [0,S-epsilon] with this solution. Since epsilon is arbitrary, Law(Y_t)=p_hat_{S-t} for every 0<=t<S.

### 7. Empirical-law endpoint

Step 1 gives X_s tending to G in mean square, hence in probability and distribution, as s decreases to zero. The law of G is N^{-1}sum_i delta_{G^i}. Consequently p_hat_s converges weakly to that empirical measure. Combining this with Step 6 proves the requested weak convergence of Law(Y_t) as t increases to S. No score, density, or reverse drift is evaluated at the atomic endpoint.

All theorem-critical obligations are closed. The source-local repairs concern only the distinction between a marginal representation and an original path law, and the verification of standard positive-time uniqueness and reversal hypotheses.
