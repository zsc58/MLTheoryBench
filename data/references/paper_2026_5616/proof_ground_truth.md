# Reference Proof

## Proof Structure and Obligations

The two assertions concern their respective sampling settings. The upper-bound observations have law D; the likelihood-increment observations have law p_theta0. The second assertion is a sharpness example, not a lower bound for every bounded Fisher-Lipschitz loss, and the proof does not apply the first assertion to the likelihood-increment loss.

The theorem-critical obligations are:

1. Establish finite, measurable suprema and justify empirical-process symmetrization.
2. Verify conditional subgaussian increments, the anchoring condition, and all hypotheses of the standard chaining/Gaussian-width comparison.
3. Control the absolute supremum and establish the stated bounded-differences constant.
4. Verify that the likelihood increments and risks are well defined, and derive their exact empirical fluctuation.
5. Verify the multivariate CLT hypotheses, justify convergence of expected norms, identify the Fisher width, and obtain the eventual relative lower bound.

All five obligations are closed below. The external results used are precisely the standard-independent empirical-process and bounded-differences results indexed by theory_017 and the multivariate CLT indexed by theory_020. The expectation-convergence step is additionally justified directly by truncation.

## Standard Comparison Used in the Upper Bound

We use the following standard consequence of the subgaussian generic-chaining upper bound and the Gaussian majorizing-measure comparison invoked in the source. Let S be a compact subset of Euclidean space containing 0. Suppose (V_s) is a centered, separable real process, V_0=0, and for every real lambda and all s,t in S,

E exp(lambda(V_s-V_t)) <= exp(lambda^2 a^2 ||s-t||_2^2/2).

Then

E sup_{s in S} V_s <= K a E_g sup_{s in S} <g,s>,

where K is universal. Indeed, the subgaussian chaining upper bound is K a times the chaining functional of the Euclidean metric, and the Gaussian majorizing-measure comparison bounds that functional by a universal constant times the displayed Gaussian supremum. These are the two standard-independent inequalities used together in theory_017. We verify the compactness, separability, centering, anchoring, and increment hypotheses explicitly in the application.

We also use standard symmetrization for a measurable separable class with an integrable envelope, and the bounded-differences inequality: if a measurable function F of independent observations changes by at most c_i when only observation i changes, then, for t>0,

P(F-EF >= t) <= exp(-2t^2 / sum_i c_i^2).

## Uniform Upper Bound

### Measurability and symmetrization

The Fisher-Lipschitz condition makes theta -> ell(theta;z) continuous on T for every z. It also gives

|R(theta)-R(theta')| <= L ||theta-theta'||_{G0},

so the population risk is continuous. Empirical risks and the Rademacher processes below are continuous as functions of theta. Since T is compact in a finite-dimensional space, it has a countable dense subset, and each relevant supremum equals the supremum over that subset. Consequently these suprema are measurable. Boundedness supplies an integrable envelope and gives

F := sup_{theta in T} |R(theta)-Rhat_n(theta)| <= B.

Let epsilon_1,...,epsilon_n be independent Rademacher signs, independent of the observations, and set

Y_theta = (1/n) sum_i epsilon_i ell(theta;Z_i).

Standard symmetrization therefore applies and yields

E F <= 2 E_{Z,epsilon} sup_{theta in T} |Y_theta|.

### Conditional increments and Gaussian-width comparison

Fix the observations. The process Y_theta is centered with respect to the signs, and Y_0=0 because ell(0;z)=0. For theta,theta' in T, put a_i=ell(theta;Z_i)-ell(theta';Z_i). Independence of the signs and the elementary Rademacher exponential bound give

E_epsilon exp(lambda(Y_theta-Y_theta'))
= product_i cosh(lambda a_i/n)
<= exp(lambda^2 sum_i a_i^2/(2n^2))
<= exp(lambda^2 L^2 ||theta-theta'||_{G0}^2/(2n)).

Set S=G0^(1/2)T and V_s=Y_{G0^(-1/2)s}. Positive definiteness makes this change of variables well defined. The set S is compact and contains 0; V is centered, anchored at zero, and continuous, hence separable. Its increments satisfy the standard comparison with a=L/sqrt(n), because

||theta-theta'||_{G0} = ||G0^(1/2)theta-G0^(1/2)theta'||_2.

It follows that

E_epsilon sup_{theta in T} Y_theta <= K L w(S)/sqrt(n).

Directly from the width definitions, w(S)=w_G0(T). Moreover, 0 in T implies T is contained in T-T, so pointwise comparison of the defining suprema gives w_G0(T)<=w_G0(T-T). Hence

E_epsilon sup_{theta in T} Y_theta <= K L w_G0(T-T)/sqrt(n).

The process -Y has the same increment bound, is centered, and is also zero at the origin. Both sup Y and sup(-Y) are nonnegative, and therefore

sup_{theta in T} |Y_theta| <= sup_{theta in T} Y_theta + sup_{theta in T} (-Y_theta).

Applying the same comparison to -Y and then using symmetrization proves

E F <= C L w_G0(T-T)/sqrt(n).

The widths here are finite: the relevant sets are compact, G0 is a finite matrix, and the supremum of the Gaussian linear functional is bounded in absolute value by a finite radius times ||g||_2. The constant C is universal and absorbs only the universal comparison and symmetrization constants. No convexity or symmetry of T is needed. If T={0}, the anchored process and its gap are identically zero, so this case is included.

### Concentration

When only observation Z_i is replaced, each empirical risk changes by at most B/n, since its summands lie in [0,B]. The inequality between the difference of two suprema and the supremum of their pointwise differences then gives the same bound B/n for the change in F. Thus the bounded-differences hypotheses hold with c_i=B/n and sum_i c_i^2=B^2/n. Consequently

P(F-EF >= t) <= exp(-2nt^2/B^2).

Taking t=B sqrt(log(1/delta)/(2n)) and inserting the expectation bound proves the first assertion for every delta in (0,1).

## Exponential-Family Asymptotic Sharpness

### Well-defined risks and the exact fluctuation

Work now with the independent observations Y_i of law p_theta0. On the common support of a regular exponential family, the density representation gives

tilde ell(u;y) = A(theta_0+u)-A(theta_0)-u^T phi(y).

The log-partition values are finite for parameters in the specified domain. The second-moment assumption implies E||phi(Y)||_2<infinity, so this expression is integrable for every allowed u. The common null-set extension has no effect on either the population risk or, almost surely, any empirical risk. In particular, integrability of the two separate log densities is not required: it is their difference that defines the loss.

Define

mu = E_{p_theta0} phi(Y),

Delta_n = (1/n) sum_i phi(Y_i)-mu.

The deterministic log-partition difference cancels when subtracting empirical from population risk, leaving

tilde R(u)-Rhat_tilde_n(u) = u^T Delta_n.

Cauchy-Schwarz gives |u^T Delta_n|<=r||Delta_n||_2 when ||u||_2<=r. If Delta_n is nonzero, equality is attained at u=r Delta_n/||Delta_n||_2. If Delta_n=0, both sides vanish. Therefore

sup_{u in r B_2^d} |tilde R(u)-Rhat_tilde_n(u)| = r||Delta_n||_2.

This identity also establishes measurability and finiteness of the supremum and its expectation.

### Gaussian limit and convergence of expectations

Let xi_i=phi(Y_i)-mu and W_n=n^(-1/2) sum_i xi_i=sqrt(n)Delta_n. The xi_i are independent and identically distributed centered vectors with finite second moments and covariance G0. The multivariate CLT for such vectors, as indexed by theory_020, gives

W_n converges in distribution to W, where W has distribution N(0,G0).

Independence and zero means make the cross terms vanish, so

E||W_n||_2^2 = (1/n) sum_i E||xi_i||_2^2 = Tr(G0)

for every n. For M>0 this gives the explicit tail bound

E[||W_n||_2 1_{||W_n||_2>M}] <= Tr(G0)/M.

Thus the norms are uniformly integrable. To verify the expectation passage directly, the function x -> min(||x||_2,M) is bounded and continuous, so convergence in distribution gives convergence of its expectations. The displayed tail bound controls the truncation error uniformly in n. The Gaussian limit also has second moment Tr(G0), so its truncation error satisfies the same bound. Letting M tend to infinity proves

E||W_n||_2 -> E||W||_2 = E||G0^(1/2)g||_2,

where g is standard Gaussian in R^d.

### Width identification and eventual lower bound

For every g, symmetry of the positive-definite square root and the Euclidean-ball support formula give

sup_{||u||_2<=r} <g,G0^(1/2)u> = r||G0^(1/2)g||_2.

This is also valid when G0^(1/2)g=0. Taking expectations yields

w_G0(r B_2^d) = r E||G0^(1/2)g||_2.

Combining the exact fluctuation identity with expectation convergence therefore proves

sqrt(n) E[sup_{u in r B_2^d} |tilde R(u)-Rhat_tilde_n(u)|]
= r E||W_n||_2
-> w_G0(r B_2^d).

Write K0=w_G0(r B_2^d). It is finite. If K0=0, the requested eventual lower bound is immediate from nonnegativity. Otherwise, convergence with tolerance epsilon K0 gives a threshold N_epsilon such that, for all n>=N_epsilon, the scaled expectation is at least (1-epsilon)K0. Dividing by sqrt(n) gives the stated lower bound. The threshold is for the fixed model, dimension, base point, and radius; no uniform threshold over varying families or dimensions is asserted.

All theorem-critical obligations are closed. No source-specific unproved dependency or unresolved private proof gap remains.
