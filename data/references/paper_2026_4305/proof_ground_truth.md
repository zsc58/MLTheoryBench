# Reference Proof

## Obligations and proof structure

The proof must justify finite-depth differentiation and integrability, identify the h-weighted ambient gradient, establish conditional unbiasedness and a uniform one-sample moment bound, and close the constrained projected-SGD recurrence including its finite initial segment. An adapted-adjoint derivation is supplied in Steps 2–3 to retain the source chain; a solver may instead use the direct pathwise argument in Step 4. The adapted route and an innovation construction are not additional public conclusions.

Throughout, write `S=1+V_H(N)`, use the h-weighted inner product on the deterministic parameter space, and let `L` bound the relevant first derivatives in operator norm. All architecture parameters are fixed.

## Step 1: Gaussian structure, forward integrability, and first variation

Each noise coordinate is standard normal, so `E xi_n^2=1` and `E xi_n^4=3`. Conditional Jensen gives `0<=V_H(N)<=1`, hence `1<=S<=2`. Every polynomial in the absolute coordinates of the finite Gaussian vector has finite moments of every finite order, by Holder's inequality and the corresponding one-dimensional Gaussian moments. Independence between coordinates is not needed.

For completeness, the nondegeneracy needed for the private innovation construction follows directly from the covariance. Put `a=2H in (0,2)` and `I_a=int_0^infinity (1-cos t)t^{-1-a}dt`. This integral is finite and positive: near zero its integrand is of order `t^{1-a}`, and at infinity it is bounded by `2t^{-1-a}`. Substitution gives `|r|^a=I_a^{-1} int_0^infinity (1-cos(rt))t^{-1-a}dt`. Therefore the covariance at integer lag r equals `I_a^{-1} int_0^infinity cos(rt)(1-cos t)t^{-1-a}dt`. For a real vector z,

`z^T Sigma_N z=I_a^{-1} int_0^infinity (1-cos t)|sum_{j=0}^{N-1}z_j exp(ijt)|^2 t^{-1-a}dt`.

For nonzero z the trigonometric polynomial cannot vanish on an interval, and the weight is positive except on a discrete set. Thus this quadratic form is strictly positive. The finite covariance matrix consequently has a lower-triangular Cholesky factor beta with positive diagonal. The Gaussian vector `eta=beta^{-1}xi` has identity covariance and independent standard normal coordinates. Triangular invertibility gives `F_n=sigma(eta_0,...,eta_{n-1})=G_n`. In particular,

`xi_n=zeta_n+beta_n eta_n`,
`zeta_n=E[xi_n|F_n]=sum_{j<n}beta(n,j)eta_j`,
`beta_n=beta(n,n)>0`.

Here eta_n is independent of F_n, and `E zeta_n^2=1-beta_n^2<=V_H(N)`. No depth-uniform spectral estimate is required by the target.

For deterministic u, linear growth and bounded diffusion give the pathwise estimate

`|X_{n+1}| <= (1+h L')|X_n|+h L'(1+|u_n|)+sqrt(h)L'|xi_n|`.

Finite induction gives all finite moments of X. Bounded cost derivatives imply linear growth of the costs, so J is finite. For the private adapted derivation below, square-integrable adapted controls also give square-integrable states by the same finite recursion and bounded diffusion. More precisely, conditioning with the innovation decomposition and applying Young's inequality gives

`E|X_{n+1}|^2 <= (1+C h)E|X_n|^2+C h(1+E|u_n|^2)+C V_H(N)`.

Since `h<=T`, the constants can be chosen in terms of coefficient bounds and T. Iterating yields the source's finite-depth bound `max_n E|X_n|^2 <= C_T(1+|x_0|^2+h sum_n E|u_n|^2+N V_H(N))`.

Fix a deterministic direction v. The same variation argument also applies to an adapted direction whose components are essentially bounded. Define `Y_0=0`. Ordinary differentiation of the finite forward recursion gives

`Y_{n+1}=A_n Y_n+B_n Y_n xi_n+h b_{u,n}v_n+sqrt(h)sigma_{u,n}v_n xi_n`.

To justify convergence and exchange of derivative and expectation, choose a deterministic bound `v_max` on all components of v, and recursively set

`R_0=0`,
`R_{n+1}=(1+hL+sqrt(h)L|xi_n|)R_n+(hL+sqrt(h)L|xi_n|)v_max`.

The mean-value inequality shows that both the state difference quotients for `u+epsilon v` and their pathwise limit Y are bounded componentwise in norm by R. Each R_n is a polynomial in absolute Gaussian coordinates and has all finite moments. Pathwise differentiability and dominated convergence therefore give convergence of the difference quotients in every finite L^r. The loss difference quotients are dominated by

`L R_N+hL sum_n(R_n+v_max)`,

which is integrable. Consequently,

`DJ(u)v=E[<Phi_x(X_N),Y_N>+h sum_n(<ell_{x,n},Y_n>+<ell_{u,n},v_n>)]`.

This argument works for every deterministic ambient direction, even when u lies on the boundary of U_det, because the coefficient maps and J are defined on the full ambient parameter space.

## Step 2: Private adapted backward recursion

For an adapted trajectory define `p_N=Phi_x(X_N)` and, recursively,

`bar p_n=E[p_{n+1}|F_n]`,
`q_n=E[p_{n+1}eta_n|F_n]`,
`p_n=A_n^*bar p_n+B_n^*(zeta_n bar p_n+beta_n q_n)+h Lambda_n`.

The terminal variable is bounded. If p_{n+1} has all finite moments, conditional Jensen and Holder give, for every m>=2,

`E|bar p_n|^m<=E|p_{n+1}|^m`,
`E|q_n|^m<=E[|p_{n+1}|^m|eta_n|^m] <= (E|p_{n+1}|^{2m})^{1/2}(E|eta_n|^{2m})^{1/2}`.

Similarly, `E|zeta_n bar p_n|^m` is finite by Holder, since zeta_n is Gaussian. The matrices A_n,B_n and vector Lambda_n are bounded. Backward induction therefore gives a unique adapted recursion with all finite moments. Collecting finitely many second moments gives the fixed-architecture bound on `max_n E|p_n|^2+h sum_n E|q_n|^2`. This directly proves the needed backward well-posedness; no specialized external backward-equation result is invoked.

By the innovation decomposition and the definitions of the conditional expectations,

`E[p_{n+1}xi_n|F_n]=zeta_n bar p_n+beta_n q_n`.

## Step 3: Private adapted cancellation

All coefficients at time n and Y_n are F_n-measurable. The conditional-product identity gives

`E<p_{n+1},A_nY_n+B_nY_n xi_n>=E<p_n-h Lambda_n,Y_n>`.

Using the remaining terms in the linearized recursion,

`E[<p_{n+1},Y_{n+1}>-<p_n,Y_n>]`
`= -h E<Lambda_n,Y_n>+h E<b_{u,n}^*bar p_n,v_n>`
`  +sqrt(h)E<sigma_{u,n}^*(zeta_n bar p_n+beta_n q_n),v_n>`.

Every product is integrable by the moment bounds already proved. Summing over n, using Y_0=0 and p_N=Phi_x(X_N), and substituting the first-variation formula cancels the state-variation terms. The result is

`DJ(u)v=h sum_n E< b_{u,n}^*bar p_n+ell_{u,n}+h^{-1/2}sigma_{u,n}^*(zeta_n bar p_n+beta_n q_n),v_n>`.

This is the derivative representation underlying the source's adapted optimality system. At an adapted local minimizer it combines with the feasible-direction variational inequality; localized bounded perturbations produce its pointwise constrained condition. This optimality system remains private and is not a separate requirement of the public task.

## Step 4: Pathwise reverse sweep and unbiasedness

Fix a noise realization and use the public reverse recursion. Pairing it with the linearized forward recursion gives the deterministic identity

`<hat p_{n+1},Y_{n+1}>-<hat p_n,Y_n>`
`= -h<Lambda_n,Y_n>+h<b_{u,n}^*hat p_{n+1},v_n>`
`  +sqrt(h)<sigma_{u,n}^*hat p_{n+1}xi_n,v_n>`.

Telescoping and including the direct running-cost derivative yield

`D L(u;xi)v=h sum_n<hat g_n(u;xi),v_n>`.

The reverse variables themselves are bounded uniformly in u by the backward scalar recursion

`P_N=L`,
`P_n=(1+hL+sqrt(h)L|xi_n|)P_{n+1}+hL`.

These finite polynomials have all finite moments. Thus the displayed identity is integrable, consistently with the differentiation argument in Step 1. Taking expectations gives

`DJ(u)v=<E hat g(u),v>_h`.

Because this holds for every deterministic ambient direction v, and the gradient of J uses the h-weighted ambient inner product,

`E hat g(u)=nabla J(u)`.

All trajectory maps are measurable, since they are finite compositions of continuous coefficient maps. At iteration k, let A_k be the sigma-field generated by all previously sampled trajectories. Then u^k is A_k-measurable and the new trajectory is independent of A_k. Applying the preceding identity with the iterate fixed gives

`E[hat g^k|A_k]=nabla J(u^k)`.

Conditioning further on u^k gives the version stated in the task. Within-trajectory independence is neither asserted nor used.

## Step 5: Explicit sample moment and variance bounds

Let `L_sigma=sup_{n,x,u}||sigma_u(n,x,u)||<=L`. For the drift and running-cost part of one component, the assumed second moment gives

`E|b_{u,n}^*hat p_{n+1}+ell_{u,n}|^2 <= 2L^2(M_2+1)S`.

For its diffusion-control part, Holder's inequality, the fourth-moment assumption, and `E|xi_n|^4=3` give

`E|h^{-1/2}sigma_{u,n}^*hat p_{n+1}xi_n|^2`
`<= h^{-1}L_sigma^2(E|hat p_{n+1}|^4)^{1/2}(E|xi_n|^4)^{1/2}`
`<= h^{-1}L_sigma^2 sqrt(3M_4)S`.

This calculation does not assume that hat p_{n+1} and xi_n are independent. Combining the two parts by `|a+b|^2<=2|a|^2+2|b|^2`, multiplying by h, and summing gives

`E||hat g(u)||_h^2 <= Q:=S(kappa_0+kappa_1/h)`,

where one may take

`kappa_0=4T L^2(M_2+1)`,
`kappa_1=2T L_sigma^2 sqrt(3M_4)`.

These bounds are uniform over feasible deterministic u. By unbiasedness,

`E||hat g(u)-nabla J(u)||_h^2=E||hat g(u)||_h^2-||nabla J(u)||_h^2<=Q`.

They consequently also hold conditionally at an SGD iterate. If the diffusion is control independent, `L_sigma=0`, so `kappa_1=0`. This is a private specialization, not an additional public target or hypothesis.

## Step 6: Constrained projected-SGD convergence

Existence and uniqueness of the minimizer do not require an interior feasible set. Integrating the strong-monotonicity inequality along the feasible segment from 0 to u gives

`J(u)>=J(0)+<nabla J(0),u>_h+(mu/2)||u||_h^2`.

Thus J is coercive on U_det. The set is nonempty and closed in a finite-dimensional space, so continuity and compactness of bounded sublevel sets give a minimizer; strong convexity gives uniqueness. At that minimizer,

`<nabla J(u*),u-u*>_h>=0` for every `u in U_det`.

Together with strong monotonicity, this implies

`<nabla J(u),u-u*>_h>=mu||u-u*||_h^2`.

In particular, no assertion that `nabla J(u*)=0` is needed.

Set `e_k=u^k-u*` and `a_k=E||e_k||_h^2`. Projection non-expansiveness and `Pi_{U_det}(u*)=u*` give

`||e_{k+1}||_h^2 <= ||e_k||_h^2-2alpha_k<hat g^k,e_k>_h+alpha_k^2||hat g^k||_h^2`.

All a_k are finite. Indeed, the elementary inequality `||e_k-alpha_k hat g^k||^2<=2||e_k||^2+2alpha_k^2||hat g^k||^2` and Step 5 give `a_{k+1}<=2a_k+2alpha_k^2 Q`, starting from the fixed finite a_0.

For the source's smoothness-based recurrence, note that

`||nabla J(u)||_h^2<=2L_J^2||u-u*||_h^2+2||nabla J(u*)||_h^2`.

Jensen's inequality and Step 5 give `||nabla J(u*)||_h^2<=Q`. The conditional variance identity therefore yields the convenient bound

`E[||hat g^k||_h^2|A_k]<=4L_J^2||e_k||_h^2+3Q`.

Conditional unbiasedness, the constrained inequality above, and total expectation now give

`a_{k+1}<=(1-2mu alpha_k+4L_J^2 alpha_k^2)a_k+3Q alpha_k^2`.

Put `c=mu alpha_0>1`. Choose an integer k0 such that `k0+1>=c` and `k0+1>=4L_J^2 alpha_0/mu`. For k>=k0,

`a_{k+1}<=(1-c/(k+1))a_k+D/(k+1)^2`,
`D=3alpha_0^2 Q`.

The coefficient is now nonnegative. Choose `A>=max{(k0+1)a_{k0},D/(c-1)}`. If `a_k<=A/(k+1)`, then

`a_{k+1}<=A/(k+1)-(cA-D)/(k+1)^2`
`<=A/(k+1)-A/(k+1)^2`
`=Ak/(k+1)^2<=A/(k+2)`.

This proves the tail estimate by induction.

To track the finite initial segment and the two displayed rate terms explicitly, the earlier elementary bound gives, for j<=k0,

`a_j<=2^j a_0+2Q sum_{i=0}^{j-1}2^{j-1-i}alpha_i^2`,

with an empty sum equal to zero. Let

`F_0=max_{0<=j<=k0}(j+1)2^j`,
`F_1=max_{0<=j<=k0} 2(j+1)sum_{i=0}^{j-1}2^{j-1-i}alpha_i^2+3alpha_0^2/(c-1)`.

Then `A=F_0 a_0+F_1 Q` covers every initial index and satisfies both requirements of the tail induction. Since S>=1,

`A<=S(C_0+C_1/h)`,
`C_0=F_0 a_0+F_1 kappa_0`,
`C_1=F_1 kappa_1`.

Thus, for every K>=1,

`E||u^K-u*||_h^2<=S(C_0+C_1/h)/(K+1)<=C_0(1+V_H(N))/K+C_1(1+V_H(N))/(Kh)`.

The constants may be enlarged to be strictly positive. They depend only on fixed problem and assumption constants, the stepsize parameter, and the initial error, not on K. Architecture dependence through the assumed moments is permitted. The proof also covers a singleton or lower-dimensional feasible set, N=1, H=1/2, and V_H(N)=0.

All theorem-critical obligations are closed; no unproved specialized external dependency remains.
