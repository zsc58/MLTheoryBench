# Reference Proof

## Audit status

The public task and the complete proof have been checked against the source contract. The previously unresolved Gaussian noise-sensitivity/surface-area inequality, recorded as theory_010, is proved in step_004 below. That completion verifies the derivation supplied in the current downstream report; it is not attributed to the original paper, which states and cites the inequality without proving it. No additional assumption is imposed on the public task.

## Proof structure and obligation ledger

- **step_001 — Hermite background and smoothing:** Closed using the standard independent Gaussian Hermite basis theorem recorded in theory_007 and the generating-function calculation from theory_014, expanded below.
- **step_002 — Truncation estimate:** Closed by L2 contraction, the Hermite eigenvalues, and Parseval, as in theory_008.
- **step_003 — Boolean smoothing identity:** Closed by the correlated Gaussian coupling and the conditional-sign argument from theory_005 and theory_009.
- **step_004 — Surface-area control:** Closed by the explicitly verified Lipschitz-approximation and Gaussian-rotation argument below, using Rademacher's theorem as standard independent background with its hypotheses checked.
- **step_005 — Parameter balance and degenerate cases:** Closed, including zero, small positive, and infinite surface area.

## Definitions and standard independent background

All norms and expectations below use standard Gaussian probability measure unless otherwise specified. Put K={x:f(x)=1} and G=GSA(f). The public hypotheses give Borel measurability, gamma_n(partial K)=0, and existence of the defining surface-area limit. Since f is Boolean, f belongs to L2(gamma_n) and ||f||_2=1.

For independent X,Y distributed according to gamma_n and rho in [0,1], put Z_rho=rho X+sqrt(1-rho^2)Y. The pair (X,Z_rho) is jointly Gaussian, both marginals are standard Gaussian, and its cross-covariance is rho I_n. Define

GNS_delta(f)=P[f(X) != f(Z_{1-delta})],  0<=delta<=1.

The standard independent Hermite basis theorem states that the normalized probabilists' Hermite polynomials H_k, specified by

exp(tx-t^2/2)=sum_{k>=0} H_k(x)t^k/sqrt(k!),

have products H_alpha(x)=product_i H_{alpha_i}(x_i) forming an orthonormal basis of L2(gamma_n). Here alpha ranges over nonnegative integer multi-indices, |alpha|=sum_i alpha_i, and H_alpha has total degree |alpha|. Consequently, for every g in L2(gamma_n), its coefficients g_hat(alpha)=E[g(X)H_alpha(X)] satisfy

g=sum_alpha g_hat(alpha)H_alpha in L2,

||g||_2^2=sum_alpha g_hat(alpha)^2.

The finite sum Pi_{<=d}g=sum_{|alpha|<=d}g_hat(alpha)H_alpha is a polynomial of degree at most the nonnegative integer d, and these projections converge to g in L2 as d tends to infinity. This is the background supplied at source lines L000083-L000097; all its hypotheses hold for f.

If G=+infinity, choose a finite Hermite projection p with ||f-p||_2<=epsilon. Cauchy-Schwarz on the Gaussian probability space gives ||f-p||_1<=epsilon. The degree upper bound is vacuous because epsilon is positive and log(1/epsilon)>0. This case requires no surface-area inequality. Henceforth assume G is finite.

## step_001: Ornstein-Uhlenbeck smoothing and eigenvalues

For rho in [0,1], define

T_rho g(x)=E_Y[g(rho x+sqrt(1-rho^2)Y)].

Conditional Jensen and the fact that Z_rho has standard Gaussian distribution give

||T_rho g||_2^2 <= E_{X,Y}[|g(Z_rho)|^2]=||g||_2^2.

Thus T_rho is an L2 contraction. In one dimension, the Gaussian moment-generating function gives

E_Y[exp(t(rho x+sqrt(1-rho^2)Y)-t^2/2)]
=exp(rho xt-rho^2 t^2/2).

Differentiating at t=0 and using the Hermite generating function yields T_rho H_k=rho^k H_k. Differentiation under the Gaussian expectation is justified because, on each bounded interval of t, each derivative is dominated by a polynomial in |Y| times exp(a|Y|) for a finite constant a, which is Gaussian-integrable. Independence across coordinates then yields

T_rho H_alpha=rho^{|alpha|}H_alpha.

For rho=0, the eigenvalue for the constant polynomial is 1 and all positive-degree eigenvalues are 0. Applying the contraction to finite Hermite projections and passing to their L2 limits proves

T_rho f=sum_alpha rho^{|alpha|} f_hat(alpha)H_alpha in L2.

## step_002: Truncation error

For a nonnegative integer d, set p=Pi_{<=d}(T_rho f). Parseval gives

||T_rho f-p||_2^2
=sum_{|alpha|>d} rho^{2|alpha|}f_hat(alpha)^2
<=rho^{2(d+1)}sum_alpha f_hat(alpha)^2
=rho^{2(d+1)}.

Therefore p has degree at most d and

||T_rho f-p||_1<=||T_rho f-p||_2<=rho^{d+1}.

The estimate also holds at rho=0, where T_0 f is constant and the tail is zero.

## step_003: Smoothing error

For fixed X, the random variable f(X)-f(Z_rho) is nonnegative when f(X)=1 and nonpositive when f(X)=-1. Hence the absolute value commutes with the conditional expectation in this instance, giving

||f-T_rho f||_1
=E_{X,Y}[|f(X)-f(Z_rho)|]
=2P[f(X) != f(Z_rho)]
=2GNS_{1-rho}(f).

Together with step_002 and the triangle inequality, this proves

||f-p||_1<=2GNS_{1-rho}(f)+rho^{d+1}.

## step_004: Surface-area inequality

We prove the inequality stated in the source as theory_010:

GNS_{1-rho}(f)<=sqrt(pi)*sqrt(1-rho)*G,  0<=rho<=1.  (B)

If K is empty, f is constant and the assertion is immediate. If rho=1, the coupled Gaussian points coincide and both sides are zero. Otherwise let K be nonempty, let 0<=rho<1, and put theta=arccos(rho), so 0<theta<=pi/2.

For r>0 define

h_r(x)=max{0,1-dist(x,K)/r}.

The distance to a nonempty set is 1-Lipschitz: the triangle inequality gives dist(x,K)<=||x-z||+dist(z,K), and reversing x,z gives the opposite bound. Therefore h_r is globally 1/r-Lipschitz and takes values in [0,1].

We use the following standard independent result, also stated in the downstream derivation: Rademacher's theorem says that a Lipschitz real-valued function on R^n is differentiable Lebesgue-almost everywhere. Its hypothesis holds for h_r. Gaussian measure is absolutely continuous with respect to Lebesgue measure, so h_r is also differentiable Gaussian-almost everywhere, with ||grad h_r||<=1/r. Take a measurable representative of this gradient, setting it to zero on the exceptional null set.

On the interior of K, h_r is identically one locally and its gradient is zero. Outside K^{(r)}, h_r is identically zero locally. Since K outside its interior is contained in partial K, whose Gaussian measure is zero, this proves

E||grad h_r(X)||<=gamma_n(K^{(r)}\K)/r.  (1)

For independent standard Gaussian vectors X,Y define, for 0<=t<=theta,

W_t=cos(t)X+sin(t)Y,

V_t=-sin(t)X+cos(t)Y.

For each fixed t this is an orthogonal transformation of the pair (X,Y). Consequently W_t and V_t are independent standard Gaussian vectors, and dW_t/dt=V_t.

For every fixed pair X,Y the path W_t is continuously differentiable and Lipschitz on [0,theta], with speed at most ||X||+||Y||. Thus h_r(W_t) is Lipschitz, hence absolutely continuous, on this interval. Let N_r be a measurable Gaussian-null set containing the nondifferentiability points of h_r. Since W_t has standard Gaussian distribution for every t, Tonelli gives

E[integral_0^theta 1_{N_r}(W_t) dt]=0.

For almost every pair X,Y, therefore, W_t avoids N_r for almost every t. At those times the ordinary chain rule gives

d h_r(W_t)/dt=grad h_r(W_t) dot V_t.

The fundamental theorem for absolutely continuous functions and the triangle inequality yield, almost surely,

|h_r(W_theta)-h_r(W_0)|
<=integral_0^theta |grad h_r(W_t) dot V_t| dt.

Taking expectations and using Tonelli is legitimate because the integrand is nonnegative and is bounded by ||V_t||/r, which has finite integrated expectation. Conditional on W_t, the inner product grad h_r(W_t) dot V_t is a centered real Gaussian with standard deviation ||grad h_r(W_t)||. For a standard real Gaussian Z, direct integration of its density gives E|Z|=sqrt(2/pi). Hence

E|h_r(W_theta)-h_r(W_0)|
<=theta*sqrt(2/pi)*E||grad h_r(X)||
<=theta*sqrt(2/pi)*gamma_n(K^{(r)}\K)/r.  (2)

As r decreases to zero, h_r(x) converges to 1_{closure(K)}(x). Since closure(K)\K is contained in partial K, this equals 1_K(x) Gaussian-almost everywhere. Both endpoints W_0 and W_theta have standard Gaussian marginals, so bounded convergence identifies the limit of the left side of (2) as

E|1_K(W_theta)-1_K(W_0)|
=P[f(W_theta) != f(W_0)]
=GNS_{1-rho}(f).

Here W_0=X and W_theta=rho X+sqrt(1-rho^2)Y. The assumed surface-area limit identifies the limit of the right side of (2). Thus

GNS_{1-rho}(f)<=theta*sqrt(2/pi)*G.

Finally, concavity of sine on [0,pi/2] gives sin(u)>=2u/pi there. Applying this with u=theta/2 yields

theta*sqrt(2/pi)
<=sqrt(2*pi)*sin(theta/2)
=sqrt(pi)*sqrt(1-cos(theta))
=sqrt(pi)*sqrt(1-rho).

This proves (B), including G=0, under exactly the public finite-surface-area hypotheses.

## step_005: Parameter balance and conclusion

Assume first that G=0. Applying (B) at rho=0 and using step_003 gives

||f-T_0 f||_1=2GNS_1(f)=0.

Thus f equals its Gaussian mean almost everywhere, and the constant polynomial T_0 f proves the claim with degree zero.

Now assume 0<G<+infinity. Combining (B) with the approximation estimate gives

||f-p||_1<=2sqrt(pi)*sqrt(1-rho)*G+rho^{d+1}.

Choose

delta=min{1,epsilon^2/(16*pi*G^2)},  rho=1-delta.

If delta=1, choose d=0 and p=T_0 f. Then the tail is zero and 2sqrt(pi)*G<=epsilon/2, so the error is at most epsilon/2. The degree is at most zero and therefore satisfies the required bound, regardless of how small G is.

If delta<1, put

A=log(2/epsilon)/delta,

d=ceil(A)-1.

Since epsilon<=1/2 and delta<1, A>1, so d is a nonnegative integer. The inequality log(1-delta)<=-delta gives

rho^{d+1}<=exp(-delta(d+1))<=epsilon/2.

The smoothing term equals epsilon/2. Consequently ||f-p||_1<=epsilon. Moreover, ceil(A)-1<=A, and log(2/epsilon)<=2log(1/epsilon) for epsilon<=1/2. Therefore

d<=16*pi*G^2*log(2/epsilon)/epsilon^2
<=32*pi*G^2*log(1/epsilon)/epsilon^2.

Thus C=32*pi suffices for every finite G. The infinite-surface-area case was proved independently above. This completes the proof.
