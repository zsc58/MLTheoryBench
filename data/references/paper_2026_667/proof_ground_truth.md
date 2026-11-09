# Reference Proof

## Proof structure and obligations

We first verify that the specified normalized projections define the sliced cost on the full stated measure class. We then establish the positive-half-line quantile formula, including unequal or infinite total masses and the endpoint p=1. Finally, we integrate the scalar conditional-negative-definiteness inequality and apply the exponential criterion.

The specialized external optimal-plan result cited by the source is not assumed. Its needed role is replaced below by finite transport matrices, elementary uncrossing, and explicit approximation. The only external kernel facts used are the standard independent statements specified in the last section.

## 1. Projection measures, measurability, and moments

Write delta(b,d)=(d-b)/sqrt(2). In arclength coordinates the positive part of the projection of (b,d) is delta(b,d) when b<=t<=d, and is absent otherwise. Thus, for a nonnegative Borel function h on (0,infinity),

    integral h(r) dmu_t(r)
      = integral_Omega 1_{b<=t<=d} h(delta(b,d))/delta(b,d) dmu(b,d).

The normalized measure is Radon on Omega because delta is bounded below on every compact subset. For every a>0 and every t,

    mu_t([a,infinity))
      <= a^(-p-1) integral_Omega delta(x)^p dmu(x) < infinity.

Consequently mu_t is Radon on the positive half-line and has finite tails at every positive threshold. The displayed integral representation also establishes the required measurability in t for nonnegative Borel test functions.

Put M_mu(t)=integral r^p dmu_t(r), allowing infinity. Tonelli's theorem gives

    integral_R M_mu(t) dt
      = integral_Omega (d-b) delta(b,d)^(p-1) dmu(b,d)
      = sqrt(2) integral_Omega delta(x)^p dmu(x) < infinity.

Hence the projected p-moment is finite for almost every t, not necessarily for every t. For a finite collection of input measures, all projected moments are finite outside a common null set. No finite-total-mass assumption is used.

## 2. Reverse quantiles and the admissible coupling

Let eta be a nonnegative Radon measure on (0,infinity) with finite p-moment. Define, for r>0 and s>0,

    H_eta(r)=eta([r,infinity)),
    q_eta(s)=sup{r>0:H_eta(r)>=s},

with q_eta(s)=0 when the set is empty. The moment bound implies H_eta(r)<=r^(-p) integral x^p deta(x), so every positive tail is finite and H_eta(r) tends to zero as r tends to infinity. Thus q_eta(s) is finite for s>0.

The tail H_eta is left-continuous at positive r, by continuity of finite measures on decreasing tail sets. Monotonicity and this left-continuity imply

    q_eta(s)>=r  if and only if  s<=H_eta(r).

It follows that the restriction of (q_eta)#Lebesgue to (0,infinity) equals eta: the two measures agree on all positive upper tails, which determine a locally finite measure. In particular,

    integral_0^infinity q_eta(s)^p ds = integral_0^infinity x^p deta(x).

For eta and zeta of finite p-moment, define gamma_mon as the restriction of

    (q_eta,q_zeta)#Lebesgue on (0,infinity)

to E=[0,infinity)^2 minus {(0,0)}. This restriction is essential: the unrestricted pushforward can have infinite mass at (0,0), even when both input measures are finite or zero.

The positive marginals of gamma_mon are eta and zeta. Every compact subset of E has max(x,y)>=a for some a>0. Its gamma_mon mass is at most H_eta(a)+H_zeta(a), so gamma_mon is Radon on E and is admissible. Its cost is

    Q_p(eta,zeta)=integral_0^infinity |q_eta(s)-q_zeta(s)|^p ds.

Since the coordinates are nonnegative,

    |q_eta-q_zeta|^p <= q_eta^p+q_zeta^p,

and this cost is finite. Its positive upper-rectangle masses are

    gamma_mon([a,infinity) x [b,infinity))
      = min(H_eta(a),H_zeta(b)),  a,b>0.

We next prove that this coupling minimizes the cost.

## 3. Optimality for finite-support marginals

Suppose eta and zeta have finite support in (0,infinity), and let their total masses be m and n. If m+n=0, the conclusion is immediate. Otherwise set M=m+n and consider the equal-mass finite measures

    alpha=eta+n delta_0,
    beta=zeta+m delta_0.

Every admissible boundary-reservoir plan for eta and zeta is a finite matrix on their supports together with zero. If its interior-interior mass is c, its total mass off (0,0) is m+n-c. Adding c at (0,0) gives a coupling of alpha and beta. Conversely, deleting the (0,0) entry of any coupling of alpha and beta gives an admissible plan. This operation preserves the cost.

The set of finite matrices with these row and column sums is nonempty and compact. Therefore a cost-minimizing matrix exists.

For an exponent h>1, suppose two positive matrix entries occur at (x_1,y_1) and (x_2,y_2), where x_1<x_2 and y_1>y_2. Strict convexity gives

    |x_1-y_1|^h+|x_2-y_2|^h
      > |x_1-y_2|^h+|x_2-y_1|^h.

For completeness, the function x -> |x-y_1|^h-|x-y_2|^h is strictly decreasing when y_1>y_2, because the derivative of u -> |u|^h is strictly increasing. Evaluating it at x_1 and x_2 gives the inequality. Moving the smaller of the two positive entry masses from the crossing entries to the uncrossed entries preserves all margins and strictly decreases the cost. An optimal matrix therefore has monotone support.

For a,b>0, a monotone plan cannot put positive mass in both [a,infinity) x [0,b) and [0,a) x [b,infinity). Its upper-rectangle mass is consequently min(H_eta(a),H_zeta(b)). These masses determine the interior-interior part of the plan; its prescribed positive marginals then determine both boundary-axis parts. Thus the optimal plan off (0,0) is gamma_mon. This proves the quantile formula for finite-support marginals for every h>1.

To obtain p=1, fix any admissible finite matrix gamma. For each epsilon>0, the preceding result gives

    integral |x-y|^(1+epsilon) dgamma_mon
      <= integral |x-y|^(1+epsilon) dgamma.

Both sides are finite sums over a fixed finite set. Passing epsilon down to zero proves the same inequality with exponent 1. This argument does not integrate an additive error against an unnormalized or infinite-mass measure.

## 4. Extension to arbitrary finite-p-moment marginals

Fix p>=1. For an integer k>=1 define the nondecreasing finite-range map

    T_k(r)=2^(-k) floor(2^k min(r,k)),  r>=0.

It satisfies T_k(0)=0, 0<=T_k(r)<=r, and T_k(r)->r for every finite r. Let eta_k and zeta_k be the restrictions of (T_k)#eta and (T_k)#zeta to (0,infinity). They have finite support and finite mass, because positive images require r>=2^(-k), where each original tail is finite.

The nonincreasing function T_k(q_eta(s)) has positive-half-line pushforward eta_k. Therefore it agrees almost everywhere with q_eta_k. One way to see uniqueness here is to compare the superlevel sets at all positive rational thresholds: for a nonincreasing function they are initial intervals whose lengths are fixed by its positive tails. Likewise q_zeta_k=T_k(q_zeta) almost everywhere. Dominated convergence gives

    Q_p(eta_k,zeta_k) -> Q_p(eta,zeta),

using q_eta^p+q_zeta^p as a dominating integrable function.

Now take any admissible plan gamma for eta and zeta on E. Push it forward by (T_k,T_k) and discard the (0,0) part, obtaining gamma_k. This is an admissible finite plan for eta_k and zeta_k. Indeed, its mass is bounded by

    eta([2^(-k),infinity))+zeta([2^(-k),infinity)),

and its positive marginals follow directly from those of gamma.

The finite-support result implies

    Q_p(eta_k,zeta_k)
      <= integral_E |T_k(x)-T_k(y)|^p dgamma(x,y).

For all x,y>=0,

    |T_k(x)-T_k(y)|^p <= x^p+y^p.

The integral of this upper bound against gamma is the sum of the finite p-moments of eta and zeta; boundary coordinates contribute zero. Dominated convergence therefore yields

    Q_p(eta,zeta) <= integral_E |x-y|^p dgamma(x,y).

Taking the infimum over gamma, and combining with the admissibility and cost of gamma_mon, proves

    F_p(eta,zeta)^p
      = integral_0^infinity |q_eta(s)-q_zeta(s)|^p ds

for every p>=1 and arbitrary finite-p-moment marginals, including unequal finite masses, infinite total masses, and zero measures. No infinite-mass optimal-plan existence theorem is needed.

## 5. The sliced quadratic form

For each input measure mu_i, let H_i(t,r)=mu_{i,t}([r,infinity)). The explicit projection formula shows that H_i(t,r) is measurable in t for every r>0. Its tails are finite for every t and tend to zero as r tends to infinity. Define q_i(t,s) by the reverse-tail formula. For fixed r>0,

    { (t,s):q_i(t,s)>=r }={ (t,s):s<=H_i(t,r) },

so q_i is jointly measurable, using positive rational thresholds.

Outside the common null set from Section 1, the one-dimensional formula applies to every pair of projected measures. The extended transport cost on the exceptional set does not affect Lebesgue integration. Moreover,

    integral_R integral_0^infinity |q_i(t,s)-q_j(t,s)|^p ds dt
      <= integral_R (M_mu_i(t)+M_mu_j(t)) dt < infinity.

Consequently D_p is finite on the entire stated M^p(Omega), and

    D_p(mu_i,mu_j)^p
      =2^(-p/2) integral_R integral_0^infinity
          |q_i(t,s)-q_j(t,s)|^p ds dt.

We use the standard independent scalar negative-type theorem invoked in the source: for 0<p<=2, any finite real numbers u_1,...,u_n and real a_1,...,a_n with sum_i a_i=0 satisfy

    sum_{i,j} a_i a_j |u_i-u_j|^p <= 0.

Its hypotheses hold here because 1<=p<=2 and all the quantile values are finite. Every pairwise integrand is integrable, so the finite signed sum may be interchanged with the integrals. Hence

    sum_{i,j} a_i a_j D_p(mu_i,mu_j)^p
      =2^(-p/2) integral_R integral_0^infinity
          sum_{i,j} a_i a_j |q_i(t,s)-q_j(t,s)|^p ds dt
      <=0.

This is the required conditional negative definiteness.

## 6. Exponentiation

The standard independent exponential criterion used here states: if f is a real-valued symmetric conditionally negative definite function on a set X, with f(x,x)=0, then exp(-lambda f(x,y)) is a positive-semidefinite kernel for every lambda>0.

The transport definition gives symmetry, and the quantile formula gives zero diagonal; Section 5 gives finiteness and conditional negative definiteness of f=D_p^p. Taking lambda=1/sigma^2>0 proves that

    K_sigma(mu,nu)=exp(-D_p(mu,nu)^p/sigma^2)

is positive semidefinite on all of M^p(Omega).

## Closure assessment

All theorem-critical obligations are proved above or supplied by the two explicitly stated standard independent kernel facts with their hypotheses verified. The specialized external transport citation is not used as a proof premise. There are no unresolved reference-proof obligations.
