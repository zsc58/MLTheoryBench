# Reference Proof

## Contract and proof obligations

The experiment has a fixed iid law, fixed measurable group and prediction rule, a known reference value, and a fixed threshold. The selected scalar source statements assume iid sampling, positive group probability, and nondegenerate conditional variance. Finite conditional variance is made explicit, including the conditional second moment needed to define it. No moment assumption outside G, complementary-group probability bound, nuisance-estimation result, or uniformity over changing laws is used.

The upstream multivariate empirical-likelihood theorem has stronger assumptions, including boundedness of the metric. It is not invoked as a black box under the scalar task's weaker assumptions. Its multiplier proof is reconstructed below with a second-moment remainder bound.

The theorem-critical obligations are: (i) normalization and exceptional-sample definitions; (ii) constrained maximization; (iii) existence and identification of the boundary multiplier; (iv) its rate before expansion; (v) the quadratic likelihood expansion; (vi) the joint sign mechanism producing the mixture; and (vii) calibration and fixed-interior control. Every obligation is discharged below.

The standard independent probability results used are: the iid law of large numbers for an integrable random variable; the iid scalar central limit theorem for a centered variable with finite positive variance; Slutsky's theorem; and the continuous mapping theorem. Specifically, averages of integrable iid variables converge in probability to their expectations, and n^(-1/2) times a sum of centered iid variables of variance sigma^2 converges to N(0,sigma^2). Their hypotheses are verified at each use. The maximal-observation estimate is derived directly.

## 1. Likelihood normalization and exceptional samples

Put A={i:I_i=1}, k=N_G, and x_i=R_i-theta_P for i in A. On the probability simplex, the arithmetic-geometric mean inequality gives product_i p_i<=n^(-n), with equality only for uniform weights.

If k>0, uniform weights satisfy the moment constraint at e=hat_e. Thus L_n(hat_e)=sup_e L_n(e)=n^(-n). Equality at any other e would require uniform weights, whose sample moment is (k/n)(hat_e-e); consequently the unconstrained maximizing parameter is unique when k>0.

If k=0, every estimating variable is zero for every e. Therefore L_n(e)=n^(-n) for all e, ell_n(e)=0, and T_n(e0)=0. The public convention hat_e=0 makes every displayed object defined in this case. Also P(k=0)=(1-pi_G)^n tends to zero, including the case pi_G=1.

When k>0 and the group values x_i are not all equal, the positive-likelihood domain is the open interval (a,b), where a=min_{i in A} x_i and b=max_{i in A} x_i. Indeed, an interior candidate admits strictly positive weights with zero moment; outside that interval, including its endpoints, either feasibility fails or at least one weight must be zero, giving likelihood zero. If all group values equal a common value x, the likelihood is n^(-n) at e=x and zero elsewhere. These observations cover zero likelihoods and constant-group samples without assigning a meaning to infinity times zero.

## 2. Correct profile curvature and constrained maximization

Consider a nonconstant group sample and e in (a,b). Write U_i=U_i(e). The scalar equation

sum_i U_i/(1+lambda U_i)=0

has a unique root on the interval where every denominator is positive: its derivative with respect to lambda is -sum_i U_i^2/(1+lambda U_i)^2<0, and its limits at the two admissible endpoints have opposite infinite signs.

The Lagrange equations for the positive-weight maximizer are

1/p_i = rho + n lambda U_i.

Multiplying by p_i and summing shows rho=n. Hence

p_i(e)=1/[n(1+lambda(e)U_i(e))].

Conversely, the root gives positive weights satisfying the moment constraint and normalization, since

sum_i 1/(1+lambda U_i)=n-lambda sum_i U_i/(1+lambda U_i)=n.

The strict concavity of sum_i log p_i on positive weights verifies that these weights maximize the likelihood. This concavity is a property of the weight objective, not a claim that the raw profile likelihood is concave in e.

Let f(e)=log L_n(e). Crucially, U_i'(e)=-I_i. Implicit differentiation gives

lambda'(e) = - [sum_i I_i/(1+lambda U_i)^2] / [sum_i U_i^2/(1+lambda U_i)^2] < 0.

Differentiating the profile and using the multiplier equation yields

f'(e)=lambda sum_i I_i/(1+lambda U_i)=k lambda.

The last equality follows from sum_{i in A}1/(1+lambda U_i)=k. Therefore f''(e)=k lambda'(e)<0. At e=hat_e the root is lambda=0. Thus the profile likelihood increases up to hat_e and decreases afterward on its positive domain.

It follows, including candidates with zero likelihood, that for k>0

sup_{e<=e0} L_n(e) = n^(-n) if hat_e<=e0,

and

sup_{e<=e0} L_n(e) = L_n(e0) if hat_e>e0.

For a constant group sample the same formulas follow directly from the singleton positive-likelihood domain. For k=0 the constrained and unconstrained suprema are both n^(-n). Consequently the statistic has the following piecewise description:

T_n(e0)=0 if k=0 or hat_e<=e0;

T_n(e0)=ell_n(e0) if k>0 and hat_e>e0.

The second case may equal +infinity. This piecewise statement avoids the undefined product of an infinite likelihood ratio with a zero indicator. The finite-sample case descriptions and the unique continuous root on the nondegenerate domain also establish measurability of the statistics.

## 3. Boundary feasibility, multiplier rate, and quadratic expansion

Suppose epsilon*=e0 and put

U_i=U_i(e0), s_n=n^(-1)sum_i U_i, q_n=n^(-1)sum_i U_i^2, and d_n=max_i |U_i|.

By the conditional-mean definition,

E_P[U_i]=pi_G(E_P[R|G]-theta_P-e0)=0,

and

E_P[U_i^2]=pi_G Var_P(R|G)=sigma_G^2 in (0,infinity).

The U_i are iid measurable functions of the observations. Therefore the scalar central limit theorem gives sqrt(n)s_n converging in distribution to N(0,sigma_G^2), and the law of large numbers applied to U_i^2 gives q_n converging in probability to sigma_G^2.

For every eta>0, the union bound and integrability of U_1^2 give

P(d_n>eta sqrt(n)) <= n P(|U_1|>eta sqrt(n))

<= eta^(-2) E[U_1^2 1{|U_1|>eta sqrt(n)}] -> 0.

Thus d_n=o_P(sqrt(n)); no third or 2+delta moment is needed.

Since U_1 has mean zero and positive variance, p_+=P(U_1>0)>0 and p_-=P(U_1<0)>0. Let E_n be the event that the sample contains both a positive and a negative U_i. Then

P(E_n^c) <= (1-p_+)^n+(1-p_-)^n -> 0.

On E_n, zero is strictly inside the scalar convex hull. The unique admissible multiplier exists, the likelihood at e0 is positive, and the representation in Section 2 applies.

Before Taylor expansion, rearrange the multiplier equation exactly:

s_n=lambda a_n,

where a_n=n^(-1)sum_i U_i^2/(1+lambda U_i)>0.

Since a_n>=q_n/(1+|lambda|d_n),

|lambda|(q_n-|s_n|d_n)<=|s_n|.

We have s_n=O_P(n^(-1/2)), d_n=o_P(sqrt(n)), and q_n converging to a positive constant. Hence q_n-|s_n|d_n is bounded away from zero with probability tending to one. It follows that

lambda=O_P(n^(-1/2)), and |lambda|d_n=o_P(1).

This establishes the small-denominator condition before it is used.

Expanding the multiplier equation by an exact algebraic identity gives

0=s_n-lambda q_n+r_n,

where r_n=lambda^2 n^(-1)sum_i U_i^3/(1+lambda U_i).

Whenever |lambda|d_n<1,

|r_n| <= lambda^2 d_n q_n/(1-|lambda|d_n)=o_P(n^(-1/2)).

Thus

lambda=s_n/q_n+o_P(n^(-1/2)).

For the logarithm expansion, on an event of probability tending to one the total absolute remainder is bounded by a fixed multiple of

sum_i |lambda U_i|^3 <= (|lambda|d_n) n lambda^2 q_n=o_P(1).

Consequently, on E_n,

ell_n(e0)=2 sum_i log(1+lambda U_i)

=2n lambda s_n-n lambda^2 q_n+o_P(1)

=n s_n^2/q_n-n q_n(lambda-s_n/q_n)^2+o_P(1)

=n s_n^2/q_n+o_P(1).

Formally, one may define an auxiliary finite-valued likelihood ratio equal to ell_n(e0) on E_n and zero on E_n^c. The expansion applies to this auxiliary variable; changing a variable on E_n^c changes any rejection probability by at most P(E_n^c)=o(1). Thus samples with an infinite original likelihood ratio do not create an omitted asymptotic case.

## 4. The boundary mixture

On E_n, k>0 and the exact sample identity is

s_n=(k/n)(hat_e-e0).

Define Z_n=sqrt(n)s_n/sqrt(q_n) when q_n>0, and Z_n=0 when q_n=0. By the central limit theorem, consistency of q_n, and Slutsky's theorem, Z_n converges in distribution to Z~N(0,1).

Let an auxiliary statistic equal T_n(e0) on E_n and zero on E_n^c. The piecewise optimizer formula, sign identity, and expansion give

auxiliary statistic = (max{Z_n,0})^2+o_P(1).

The function z maps to (max{z,0})^2 is continuous. The continuous mapping theorem therefore gives convergence to (max{Z,0})^2. The original statistic agrees with the auxiliary statistic with probability tending to one, so it has the same limit.

The limit is zero with probability 1/2. For t>0,

P((max{Z,0})^2>t)=P(Z>sqrt(t))=(1/2)P(chi-square_1>t).

Thus its distribution is precisely 0.5 delta_0+0.5 chi-square_1.

## 5. Calibration and fixed-interior nulls

For alpha in (0,1/2), c_alpha>0 and the mixture distribution is continuous at c_alpha. Equivalently, c_alpha is the upper 2alpha quantile of chi-square_1. Boundary convergence therefore yields

P(T_n(e0)>c_alpha) -> P(W>c_alpha)=alpha.

Now fix a law P satisfying the assumptions with epsilon*<e0. The conditional second moment implies E|I_i R_i|<infinity. The iid laws of large numbers give

n^(-1)sum_i I_i R_i -> pi_G E[R|G], and N_G/n -> pi_G>0

in probability. The estimator therefore converges in probability to epsilon*, regardless of its prescribed value when N_G=0.

The statistic is zero on empty-group samples and whenever the estimator belongs to the null region. Hence

P(T_n(e0)>c_alpha) <= P(hat_e>e0) -> 0.

For each fixed admissible null law, the limiting rejection probability is alpha at the boundary and zero at a strict interior point. This proves the stated pointwise asymptotic control. It does not interchange a supremum over laws with the limit, and no uniform-over-laws assertion is made.

## Source repair and closure notes

The corrected profile result concerns log L, not raw L, retains the subgroup indicators, and handles empty and constant group samples. The raw likelihood maximum is n^(-n). The scalar expansion explicitly establishes the convex-hull event, multiplier existence, multiplier rate, and second-moment remainder control instead of merely invoking the stronger multivariate theorem. The source's finite-family covariance argument is locally corrected in its material record. All required obligations are closed; there is no unresolved specialized dependency or private GT gap.
