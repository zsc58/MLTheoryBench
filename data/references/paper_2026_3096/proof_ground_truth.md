# Reference Proof

## Contract and Obligations

The true observation law is lambda=lambda_L and pi=pi_L, not an arbitrary marginal paired with the same posterior conditionals. Probability is under the joint sampling law of the outer data and independent inner prior samples. No restriction on M(N)/N, monotonicity of M(N), or full support of the prior is assumed.

The obligations are: (1) uniform normalizer and moment bounds; (2) the KL identity and its equality characterization; (3) log-normalizer continuity, including the density-ratio estimates supporting it; (4) separation on a properly defined compact extension; (5) admissible finite pointwise brackets and fixed-endpoint nested convergence; (6) uniform empirical convergence and measurable suprema; and (7) the approximate-argmin conclusion. All are derived below.

Write B=C_2^+, a=C_2^-, z=(x,y), and J_f=integral Z_f(y)dy. Constants below may depend on the prior exponential-moment data, the common growth and weighted smoothness bounds, and the dimensions, but not on f, N, M, or a bracket index.

## 1. Normalizers, Moments, and the Domain of the Estimates

The estimates in this section hold for every measurable nonnegative potential satisfying the same common quadratic bounds, not merely for members of F. This extension is important for bracket endpoints and closure elements. This larger collection is convex.

Take eta=C_1/2 and d=delta(eta)>0. The growth bounds imply

A exp(-B||y||^2) <= Z_f(y) <= D exp(-d||y||^2),

where A=exp(-B) E_mu exp(-B||X||^2)>0 and D=exp(a) E_mu exp(eta||X||^2)<infinity. Thus there are common constants 0<J_-<=J_f<=J_+<infinity. Also, since f>=0, Z_f<=1 and

|log Z_f(y)| <= -log A+B||y||^2.

Choose 0<kappa<min(C_1-eta,d). Using the joint density with respect to mu(dx)dy, rather than pi_f tensor mu, gives

E^{lambda_f} exp(kappa(||X||^2+||Y||^2))
<= exp(a) J_-^{-1} E_mu exp((eta+kappa)||X||^2) integral exp(-(d-kappa)||y||^2)dy
<= C.

Consequently every lambda_f, including lambda_L, has uniform polynomial moments of every fixed order. All population objectives and normalized-potential distances used below are finite. Each empirical normalizer is a strictly positive finite average and its logarithm is finite.

## 2. KL Identity and Identification

All posterior densities are strictly positive relative to mu. Direct substitution gives

log(dmu_L^y/dmu_f^y)=f-L+log Z_f-log Z_L.

The preceding bounds justify conditional and joint integration. Therefore

Phi(f)-Phi(L)=E^{pi_L} D_KL(mu_L^y || mu_f^y)>=0.

For completeness, nonnegativity and equality follow from -log t>=1-t with t=dmu_f^y/dmu_L^y: its mu_L^y expectation is at least zero, and equality holds precisely when t=1 almost everywhere. Thus the population excess is zero exactly when the posterior conditionals agree for pi_L-almost every y. By the displayed log-density identity this is exactly d_Phi(f,L)=0.

This statement concerns identification on the observation support, not pointwise uniqueness outside the prior support. It applies to every potential in the extended domain from Section 1.

Only the posterior conditionals and Phi are invariant under addition of a function h(y). The induced joint law is not: whenever the expressions are admissible, lambda_{f+h}=(J_f/J_{f+h})exp(-h(y))lambda_f. No joint-law invariance is used.

## 3. Density Ratios and Log-Normalizer Continuity

First, the bounds on Z_f and J_f, together with Z_g<=1, give

pi_g(y)/pi_f(y) <= C exp(B||y||^2).

For 1<r<1+kappa/B,

E^{pi_f}(pi_g/pi_f)^r
=E^{pi_g}(pi_g/pi_f)^{r-1}
<= C E^{pi_g}exp((r-1)B||Y||^2)
<= C_r.

The probability density must remain in this integral; replacing it by unweighted Lebesgue measure would give an invalid estimate.

Let R=dmu_f^y/dmu_g^y. Nonnegativity, the quadratic upper bound, Z_g<=1, and the lower bound on Z_f imply

R=exp(g-f)Z_g/Z_f <= C exp(B(||x||^2+2||y||^2)).

Set r=1+kappa/(2B), r'=r/(r-1), and q_0=1+kappa/(2Br'). For 1<q<q_0, change measures and apply Holder:

E^{lambda_g}R^q
=E^{pi_g}E^{mu_f^y}R^{q-1}
=E^{lambda_f}[(pi_g/pi_f)R^{q-1}]
<= (E^{pi_f}(pi_g/pi_f)^r)^{1/r}(E^{lambda_f}R^{r'(q-1)})^{1/r'}
<= C_q.

The last factor is bounded because 2Br'(q-1)<kappa and Section 1 supplies the required exponential moment. This establishes the formerly omitted dependency explicitly.

Fix q strictly between 1 and q_0 and put p_0=q/(q-1). For k_t=g+t(f-g), the extended domain is convex. For fixed y, differentiation under the prior integral is justified by |f-g|exp(-k_t)<=B(1+||x||^2+||y||^2). The correct derivative is

d/dt log Z_{k_t}(y)=-E^{mu_{k_t}^y}(f-g).

The triangle inequality, change of measure, and Holder therefore yield

E^{pi_h}|log Z_f-log Z_g|
<= integral_0^1 E^{lambda_h}[|f-g| dmu_{k_t}^y/dmu_h^y]dt
<= C||f-g||_{L^{p_0}(lambda_h)}.

The same bound holds with any p>=p_0, since the underlying measure is a probability measure. In particular

d_Phi(f,g)<= (1+C)||f-g||_{L^{p_0}(lambda_L)}.

Independently, the definition immediately gives |Phi(f)-Phi(g)|<=d_Phi(f,g).

## 4. Compact Extension and Separation

The weighted smoothness bound implies a uniform bound for f and its first derivatives on every compact ball: writing q_f=f/(1+||z||^2), one has partial_k f=(1+||z||^2)partial_k q_f+2z_k q_f. Thus F is locally uniformly bounded and equicontinuous.

Here is the compactness completion needed by the source argument. On each ball, uniform equicontinuity and boundedness permit extraction of a uniformly convergent subsequence, by choosing successively finer finite grids and then using equicontinuity between grid points. A diagonal extraction over integer-radius balls gives convergence uniformly on every compact set. Let K be the closure of F in this topology. The same bounds apply to K, so the argument also applies to every sequence in K. The locally uniform topology is metrizable; hence K is compact. Its elements are continuous and retain nonnegativity and every common quadratic bound. They need not be C^1 or belong to F, and neither property is required.

If f_j converges locally uniformly to f in K, the quadratic bound and the moments of lambda_L give L^p(lambda_L) convergence for every finite p by dominated convergence. Section 3 then gives d_Phi(f_j,f)->0 and Phi(f_j)->Phi(f). Thus both functions needed for separation are continuous on K. The KL identity and equality characterization from Section 2 apply throughout K.

For epsilon>0, let K_epsilon={f in K:d_Phi(f,L)>=epsilon}. It is compact. If empty, the required infimum over F is infinity. Otherwise Phi attains a minimum on it, at some f_0. Since d_Phi(f_0,L)>=epsilon>0, Section 2 gives Phi(f_0)>Phi(L). Hence

c_epsilon:=inf_{f in F:d_Phi(f,L)>epsilon}[Phi(f)-Phi(L)]>0

whenever this set is nonempty.

## 5. Finite Pointwise Brackets

The following elementary construction proves the finite bracketing needed here and verifies endpoint admissibility. It avoids needing any specialized entropy theorem as an unclosed obligation.

Define a_0(z)=inf_{f in F}f(z) and b_0(z)=sup_{f in F}f(z). The common local Lipschitz bounds show that these finite functions are locally Lipschitz, hence measurable. They retain nonnegativity and all the common lower and upper potential bounds.

Fix p=p_0 and a desired bracket width w>0. Choose R large so that B||(1+||z||^2)1_{||z||>R}||_{L^p(lambda_L)}<w/2, and h>0 so that 2h<w/2. Uniform boundedness and equicontinuity on the radius-R ball give a finite sup-norm h-net with representatives f_1,...,f_K in F. This follows, for example, by discretizing values on a sufficiently fine finite spatial grid; functions with the same discretized grid values are uniformly close by equicontinuity.

Inside that ball set

ell_k=max(a_0,f_k-h),qquad u_k=min(b_0,f_k+h),

and outside it set ell_k=a_0 and u_k=b_0. These are measurable, ordered pointwise, and satisfy all common potential bounds. For each f in F some k gives ell_k<=f<=u_k everywhere. Moreover their width is at most 2h inside the ball and B(1+||z||^2) outside, so ||u_k-ell_k||_{L^p(lambda_L)}<w.

An L^p bracket is a pair of ordered functions with L^p width at most the specified tolerance. Unlike an abstract almost-everywhere bracket, this construction verifies ordering also for inner prior evaluations. All endpoints and their convex interpolations belong to the extended domain of Sections 1-3.

## 6. Fixed-Endpoint Nested Convergence

Let v be any fixed admissible endpoint or class member. Conditional on Y=y, the iid bounded positive variables exp(-v(X_j,y)) have mean Z_v(y)>0. The inner law of large numbers and continuity of the logarithm give log Z_v^M(Y)->log Z_v(Y) in probability, or almost surely under an infinite-array coupling.

Since v>=0, Jensen gives

0>=log Z_v^M(Y)>=-B(1+||Y||^2+M^{-1}sum_j||X_j||^2).

The fourth moments of Y and X, and Jensen applied to the average of ||X_j||^2, imply a uniformly bounded second moment for log Z_v^M(Y). The same holds for log Z_v(Y) by Section 1. Thus the log error is uniformly integrable and

E|log Z_v^M(Y)-log Z_v(Y)|->0.

For M=M(N), the expected absolute average of the N row errors is at most this single-row expectation. Markov's inequality makes the average inner error vanish in probability. The remaining outer average of log Z_v(Y_i) converges by the law of large numbers. Therefore Lambda_N(v)->Lambda(v). Also Psi_N(v)->Psi(v), where Psi(v)=E^{lambda_L}v and Psi_N(v)=N^{-1}sum_i v(X_i,Y_i).

These statements require only M(N)->infinity. They do not assume a rate or monotonicity.

## 7. Uniform Empirical Convergence and Measurability

For a bracket ell<=f<=u, monotonicity gives Psi_N(ell)<=Psi_N(f)<=Psi_N(u) and Lambda_N(u)<=Lambda_N(f)<=Lambda_N(ell), with the same order for population quantities. Sandwich the two components separately. Their absolute deviations are bounded by the maximum of their two endpoint deviations plus the corresponding population bracket width.

For the finite brackets of Section 5,

Psi(u_k)-Psi(ell_k)<=w,

Lambda(ell_k)-Lambda(u_k)<=Cw,

where the second inequality follows from Section 3. Section 6 makes all endpoint deviations vanish simultaneously in probability, because there are finitely many endpoints. Consequently, for every t>0,

P(sup_{f in F}|Phi_N(f)-Phi(f)|>(1+C)w+t)->0.

Letting w decrease to zero proves U_N:=sup_{f in F}|Phi_N(f)-Phi(f)|->0 in probability.

The suprema are measurable. The compact metrizable space K is separable, and F has a countable dense subset in the locally uniform topology. For each realized finite sample, Phi_N is continuous in that topology, since it consists of finitely many evaluations and logarithms of positive finite sums. Phi is continuous by Section 4. Thus U_N is the supremum over a countable dense subset of measurable random variables. The estimator's stated measurability likewise makes its distance event measurable.

## 8. Approximate Argmin

For the measurable approximate minimizer,

Phi(f_N^*)-Phi(L)
<=[Phi(f_N^*)-Phi_N(f_N^*)]+[Phi_N(L)-Phi(L)]+r_N
<=2U_N+r_N
<=2U_N+|r_N|.

If the set at distance greater than epsilon is empty, its event is impossible. Otherwise, on {d_Phi(f_N^*,L)>epsilon}, Section 4 implies Phi(f_N^*)-Phi(L)>=c_epsilon>0. Therefore

P(d_Phi(f_N^*,L)>epsilon)<=P(2U_N+|r_N|>=c_epsilon)->0.

This proves the frozen target for every epsilon>0. It also explicitly verifies the hypotheses and conclusion of the standard approximate M-estimator consistency result rather than relying on its name alone.

## Source-Repair Record

The source's previously recorded epsilon quantifier and sampling-probability corrections remain in force. Its inner summation starts at j=1. Additional local repairs concern the square-integrability display, joint reference measure, marginal-ratio integration measure, interpolation derivative sign and absolute-value inequality, endpoint admissibility, compact closure domain, and representative dependence of lambda_f. They are recorded in the corrected material records and provenance. All proof obligations are closed; no GT quality warning is needed.
