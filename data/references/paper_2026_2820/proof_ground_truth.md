# Reference Proof

## Contract and proof obligations

The two probability assertions are proved separately for each fixed confidence level. The confidence assertion must retain the exact noise normalization `sigma_ell/sqrt(alpha_ell lambda_0)`. The regret assertion uses a three-way failure-probability allocation. All constants below may depend on the fixed instance, regularization schedule, and confidence level, but not on the horizon or realized sample path.

The obligations are: (1) correct quotient-RKHS geometry and the factor-two estimator comparison; (2) predictable self-normalized concentration with its exact scaling; (3) reference-kernel variance and determinant comparison; (4) favorable-initialization accuracy and a quantitative count established without conditioning on a global confidence event; (5) repeated-observation variance decay, including degenerate cases; and (6) initialization tails, both variance sums, and cumulative regret. Each is closed below.

## 1. RKHS geometry and adaptive confidence

Let `S=span{phi(x):x in X}` inside `H_Theta`. Because `X` is finite, `S` is finite-dimensional and closed. The map `w -> [x -> <w,phi(x)>]` is an isometry from `S` to `H_G` equipped with its infimum-representation norm. Indeed, every representation has the same projection onto `S`, and that projection is the unique minimum-norm representative. The parameter reproducing property represents `g_theta` by `k_Theta(.,theta)`, so every model lies in `H_G`. Its minimum-norm representative is the projection of that section onto `S`, not necessarily the section itself. In what follows identify functions with these minimum-norm representatives.

Write
`L_t(h)=(lambda_t/2)||h-g_{t,0}||^2 + sum_{i<=t}ell(h(x_i),y_i)`
and
`H_t=lambda_t I+alpha_ell sum_{i<=t}phi(x_i) tensor phi(x_i)`.
The loss is defined on the line segment joining `f` and `g_t`, because its prediction domain is an interval. Its second-derivative lower bound gives
`L_t(g_t)>=L_t(f)+<grad L_t(f),g_t-f>+(1/2)||g_t-f||_{H_t}^2`.
Realizability and global minimization over the parametric class give `L_t(g_t)<=L_t(f)`. Consequently, with `d_t=g_t-f`,
`(1/2)||d_t||_{H_t}^2<=-<grad L_t(f),d_t><=||grad L_t(f)||_{H_t^{-1}}||d_t||_{H_t}`.
Division when the last norm is nonzero, and the trivial zero case otherwise, yield
`||g_t-f||_{H_t}<=2||grad L_t(f)||_{H_t^{-1}}`.
This is the direct strong-convexity version of the source's full-RKHS-minimizer comparison and does not require extending a restricted-domain loss to all real predictions.

Set `xi_i=ell'_{y_i}(f(x_i))`. Then
`grad L_t(f)=lambda_t(f-g_{t,0})+sum_{i<=t}xi_i phi(x_i)`.
Since `H_t>=lambda_t I`, the initialization contribution is at most `sqrt(lambda_t)||f-g_{t,0}||`.

The supplied standard self-normalized result says that, for predictable features `h_i` in a separable Hilbert space and adapted noise satisfying `E[exp(s xi_i)|F_{i-1}]<=exp(s^2 sigma_ell^2/2)`, a fixed positive-definite `V` gives, with probability at least `1-eta`, simultaneously for all times,
`||sum_{i<=t}xi_i h_i||_{(V+sum_{i<=t}h_i tensor h_i)^{-1}}^2 <= 2 sigma_ell^2 log(det(I+F_t^* V^{-1}F_t)^{1/2}/eta)`,
where the columns of the feature operator are `h_i`. Here the feature space `S` is finite-dimensional, `x_i` is selected before `y_i` and is `F_{i-1}`-measurable, and the required conditional moment inequality is precisely a task assumption. Apply the result with `h_i=sqrt(alpha_ell)phi(x_i)` and `V=lambda_0 I`. Since `lambda_t>=lambda_0`, on this single event,
`||sum_{i<=t}xi_i phi(x_i)||_{H_t^{-1}} <= sigma_ell sqrt((2/alpha_ell)log(det(I+(alpha_ell/lambda_0)K_t^G)^{1/2}/eta))`,
where `K_t^G=[k_G(x_i,x_j)]`.

Thus, defining
`beta_hat_t(eta)=sqrt(lambda_t)||f-g_{t,0}||+sigma_ell sqrt((2/alpha_ell)log(det(I+(alpha_ell/lambda_0)K_t^G)^{1/2}/eta))`,
reproducing-kernel Cauchy-Schwarz gives simultaneously for all `t>=1` and `x in X`
`|g_t(x)-f(x)|<=2 beta_hat_t(eta)||phi(x)||_{H_t^{-1}}`.
At time zero, `g_0=g_{0,0}`, and the same inequality follows directly from the evaluation bound with `H_0=lambda_0 I`. Empty Gram determinants are one.

## 2. Kernel-to-predictive-variance reduction

Put `r=lambda_0/alpha_ell`. Operator inversion and Woodbury give
`||phi(x)||_{H_t^{-1}}^2 <= lambda_0^{-1} sigma_{G,t}^2(x)`,
where `sigma_{G,t}` is the posterior standard deviation for `k_G` with ridge `r`.

For any positive-semidefinite kernel `a`, its posterior variance equals
`min_{b in R^t} [a(x,x)-2 b^T a_t(x)+b^T A_t b+r||b||_2^2]`.
The kernel part is the quadratic form of the joint Gram matrix on `(x,x_1,...,x_t)` with coefficient vector `(1,-b)`. Therefore `k>=k_G` makes the expression for `k` at least that for `k_G` for every `b`; taking minima proves `sigma_{G,t}^2(x)<=sigma_t^2(x)`.

Also `K_t>=K_t^G`, so
`det(I+(alpha_ell/lambda_0)K_t^G)<=det(I+(alpha_ell/lambda_0)K_t)`.
For example, factor the larger positive-definite matrix relative to the smaller one; the resulting extra determinant has all eigenvalues at least one. Both determinants must be compared at `lambda_0`, not at different ridges.

Substituting these inequalities proves
`|g_t(x)-f(x)|<=2 beta_t(eta)sigma_t(x)`,
with exactly the public `beta_t`, including `1/sqrt(alpha_ell lambda_0)` in its noise term. This proves the confidence assertion for `eta=delta` when `0<delta<1`. The endpoint `delta=1` imposes only a probability-zero lower guarantee.

## 3. Favorable initialization forces the optimal decision

For the regret proof fix `0<delta<1` and let `eta=delta/3`. Use the induced-kernel concentration event from Section 1 at level `eta`. Let `m=|X|` and `M_G=max_x k_G(x,x)`.

If `|X|=1`, every decision is optimal and regret is identically zero. Hence suppose `|X|>1`, and define the positive gap
`Delta_star=f(x_star)-max_{x!=x_star}f(x)`.
The rank of `K_t^G` is at most `m`, and its trace is at most `t M_G`. Therefore its log determinant is at most `m log(1+(alpha_ell/lambda_0)t M_G)`.

Let `E_t={rho(theta_star,theta_{t,0})<=lambda_t^{-1/2}}`. On `E_t`, the initialization term in `beta_hat_t` is at most one, and `||phi(x)||_{H_t^{-1}}<=sqrt(M_G/lambda_t)`. On the concentration event this gives
`sup_x |g_t(x)-f(x)| <= 2 sqrt(M_G/lambda_t)[1+C sqrt(log(2+t)+log(1/eta))]`.
Because `lambda_t/log t` tends to infinity, there is a deterministic `n_0`, depending only on the fixed instance and `eta`, such that for every `t>=n_0` this bound is below `Delta_star/2`. Increase `n_0` so that `lambda_t^{-1/2}<alpha_0` as well. Thus, on the concentration event, `E_t` implies `x_{t+1}=x_star` for every `t>=n_0`.

This is a pathwise implication on an event. It is not an assertion that the unconditional conditional probability of an optimal visit has the small-ball lower bound.

## 4. Quantitative favorable-event counting

For `t>=n_0` set `B_t=1_{E_t}` and `p_t=c_star lambda_t^{-d_eff/2}`. Fresh initialization and the prior assumption imply `P(E_t|F_{t-1})>=p_t`; in particular `0<=p_t<=1`. Then
`E[exp(-B_t)|F_{t-1}]=1-(1-e^{-1})P(E_t|F_{t-1})<=exp(-(1-e^{-1})p_t)`.
Consequently
`Z_n=exp(-sum_{t=n_0}^n B_t+(1-e^{-1})sum_{t=n_0}^n p_t)`
is a nonnegative supermartingale, starting at one. Stopping at the first crossing of `1/eta` up to a finite horizon bounds the crossing probability by `eta`: the stopped expectation is at most one, and on a crossing the stopped value is at least `1/eta`. Taking increasing finite horizons yields the same bound for any crossing. Hence, on an event of probability at least `1-eta`, simultaneously for every `n`,
`sum_{t=n_0}^n B_t >= (1-e^{-1})sum_{t=n_0}^n p_t-log(1/eta)`.

Intersect this event with the concentration event, without changing the conditional law used in its proof. The pathwise implication from Section 3 now gives
`N_T^star=sum_{i<=T}1_{x_i=x_star} >= sum_{t=n_0}^{T-1}B_t`.
Divergence of `sum lambda_t^{-d_eff/2}` absorbs the fixed initial segment and additive constant. The one-index shift is harmless because the individual terms are bounded while their sum diverges. Thus, with deterministic constants and a deterministic sufficiently large threshold on this intersection,
`N_T^star=Omega(sum_{t=1}^T lambda_t^{-d_eff/2})`.
For `lambda_t asymp (log t)^q`, let `a=q d_eff/2`. In particular the last half of the sum already gives a constant multiple of `T/(log T)^a`, so
`N_T^star=Omega(T/(log T)^a)`.

## 5. Optimal-point posterior variance

Let `A=k(x_star,x_star)>=0` and `r=lambda_0/alpha_ell>0`. Restricting the posterior calculation to the `N_T^star` observations at `x_star` can only increase variance; this also follows by restricting the coefficient vectors in the variance minimization formula. Their Gram matrix is `A 11^T`. The rank-one inverse formula yields
`sigma_T^2(x_star)<=A r/(r+A N_T^star)`.
If `A=0`, the bound and the variance are zero. Otherwise, for positive counts it is at most `r/N_T^star`. The formula is also defined at count zero. Combining with Section 4 gives both
`sigma_T^2(x_star)=O((sum_{t<=T}lambda_t^{-d_eff/2})^{-1})`
and, for the logarithmic schedule,
`sigma_T^2(x_star)=O((log T)^a/T)`.
For a singleton domain all observations are at `x_star`, and the same variance conclusions follow directly: the small-ball-rate sum is at most a fixed multiple of `T`.

It follows, including the finitely many initial terms, that
`sum_{t=1}^T sigma_{t-1}^2(x_star)=O((log(2+T))^{a+1})`.
This follows by bounding the sum of `(log t)^a/t` by its corresponding integral plus finitely many terms.

## 6. Initialization tails, played-point variances, and regret

For `t>=0`, define
`b_t=psi_0(log(pi^2(t+1)^2/(6 eta)))`.
The arguments are positive. The prior tail assumption gives probability at most `6 eta/(pi^2(t+1)^2)` that the initialization distance exceeds `b_t`. Summing proves an event of probability at least `1-eta` on which every initialization distance is at most `b_t`, including at time zero.

Let `M=max_x k(x,x)`. The Gram matrix has rank at most `m` and trace at most `tM`, so
`log det(I+K_t/r)<=m log(1+tM/r)`.
On the tail event, `psi_0(s)=O(s^zeta)` and the logarithmic schedule imply a deterministic nondecreasing envelope for the radii satisfying
`max_{0<=t<T} beta_t(eta)=O((log(2+T))^{zeta+q/2})`.
The noise contribution is `O(sqrt(log(2+T)))` and is absorbed because `q>1` and `zeta>0`.

For played-point variances write `v_t=sigma_{t-1}^2(x_t)`. A block determinant calculation, valid for each realized point sequence, gives
`log det(I+K_T/r)=sum_{t=1}^T log(1+v_t/r)`.
If `M=0`, all variances vanish. Otherwise `0<=v_t<=M`, and concavity of the logarithm gives
`log(1+v_t/r)>=(v_t/M)log(1+M/r)`.
Hence
`sum_{t=1}^T v_t <= [M/log(1+M/r)]log det(I+K_T/r)=O(m log(2+T))`.
This explicitly derives the information-gain inequality and verifies that adaptivity introduces no extra condition.

Since `x_t` maximizes `g_{t-1}`, the confidence event gives
`r_t<=2 beta_{t-1}(eta)[sigma_{t-1}(x_star)+sigma_{t-1}(x_t)]`.
On the intersection of concentration, counting, and tail events, whose probability is at least `1-3 eta=1-delta`, Cauchy-Schwarz therefore yields
`R_T <= 2 max_{t<T}beta_t(eta) sqrt(2T[sum_{t<=T}sigma_{t-1}^2(x_star)+sum_{t<=T}sigma_{t-1}^2(x_t)])`.
Using the two variance sums gives
`R_T=O(sqrt(T)(log(2+T))^{zeta+q/2+1/2+q d_eff/4})`.
Finally `q>1` implies `q/2+1/2<=q`, so this proves the requested
`R_T=O(sqrt(T)(log T)^{zeta+q(1+d_eff/4)})`.
The proof supplies deterministic constants and thresholds on the asserted event, uniformly for all sufficiently large integer horizons. The endpoint `delta=1` is vacuous, or follows by using any smaller confidence level. There are no unresolved private proof obligations.
