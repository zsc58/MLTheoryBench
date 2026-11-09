# Reference Proof

## Contract and Obligations

The objective is the expected allocation criterion explicitly defining R(B), not an assertion that the fitted, adaptively stopped estimator has exact finite-sample MSE A_q/n_{q,B}. The fixed-coefficient variance formula in the source does not establish that latter identity. The source policy uses residual sample variance with denominator s-1 and stops as soon as the remainder is below c_max; consequently every unit is feasible whenever indices are compared.

The proof obligations are: (1) concentration and denominator control for the fitted coefficient; (2) uniform residual-standard-deviation concentration, including the statement and hypotheses of the standard independent inequality; (3) a simultaneous two-sided event and its adaptive-time interpretation; (4) a quantitative last-selected-unit argument including initialization; (5) regret conversion uniformly over all admissible confidence levels; and (6) expectation and the stated specialization. All six obligations are closed below.

The radius in the public task is exactly the source radius after using the valid support intervals [-R_Y,R_Y] and [-R_Z,R_Z]. Thus the source range widths become 2R_Y and 2R_Z, while its absolute moment bounds become R_Y and R_Z. No confidence inequality is assumed as a public hypothesis.

Write T=T_max, S_c=sum_q c_q, ell=log(QT/delta), and

L=log(16QT(T+1)/delta).

For T>=1 and delta<1/2, ell>log 2 and ell<=L<=6ell. Indeed, L=ell+log(16(T+1)), 16(T+1)<=32T, and log(32T)<=5log(2T)<=5ell. Constants below depend only on the fixed problem parameters. Let A_+=(R_Y+R_Z)^2 and S_0=A_+ sum_q w_q, so A_q<=A_+ and sum_q w_q A_q<=S_0.

## step_001: Coefficient Concentration

For completeness, bounded-variable Hoeffding concentration follows from an elementary exponential-moment argument. If U has support of width d, the second derivative of log E exp(tU) is a variance under an exponentially tilted law and is at most d^2/4: subtracting the support midpoint bounds its second moment by d^2/4. Integrating twice gives E exp(t(U-EU))<=exp(t^2d^2/8). Independence, Markov's inequality and optimization in t imply

P(|s^{-1}sum_i U_i-EU|>d sqrt(log(2/epsilon)/(2s)))<=epsilon.

Fix q and s. Set eta=delta/(2QT) and g=sqrt(log(8/eta)/(2s))=g_s. Apply this bound to Y, Z, YZ and Z^2, whose support widths are bounded by 2R_Y, 2R_Z, 2R_YR_Z and R_Z^2 respectively, assigning failure probability eta/4 to each. With probability at least 1-eta, the four empirical mean errors are at most

2R_Y g, 2R_Z g, 2R_YR_Z g, R_Z^2 g.

Let a=Cov(Y,Z) and b=Var(Z). Expanding the products of sample means gives

|a_hat-a|<=Delta_a:=6R_YR_Z g+4R_YR_Z g^2,

|b_hat-b|<=Delta_b:=5R_Z^2 g+4R_Z^2 g^2.

For example, bar Y bar Z-EY EZ=(bar Y-EY)(bar Z-EZ)+EZ(bar Y-EY)+EY(bar Z-EZ); the analogous expansion for (bar Z)^2 gives the second inequality.

Since s>=K>=K_0 ell and log(16QT/delta)<=5ell, g^2<=5/(2K_0). Choose K_0 sufficiently large, depending only on the permitted bounds, that g<=1 and 9R_Z^2 g<=V_min/2. One sufficient choice is any integer K_0>=max{3,2592R_Z^4/V_min^2}. Thus Delta_b<=V_min/2 and b_hat>=V_min/2 on the event. In particular, the zero-denominator convention is inactive there.

Using b>=V_min, b_hat>=V_min/2 and |a|<=2R_YR_Z,

|a_hat/b_hat-a/b|<=2Delta_a/V_min+4R_YR_Z Delta_b/V_min^2=:Delta_lambda.

Projection onto [0,1] is 1-Lipschitz, so |lambda_tilde-lambda^*|<=Delta_lambda. This includes population coefficients at either endpoint. Since g<=1, Delta_lambda is also bounded by a constant times sqrt(L/s).

## step_002: Uniform Standard-Deviation Concentration

Define sigma_q(lambda)=sqrt(Var(Y_q-lambda Z_q)) and

S_{q,s}(lambda)=sqrt((s-1)^{-1}sum_{i=1}^s[(Y_{q,i}-lambda Z_{q,i})-(bar Y_{q,s}-lambda bar Z_{q,s})]^2).

The standard independent result recorded as theory_014 is the following bounded sample-standard-deviation inequality: if U_1,...,U_s are iid, s>=2, U lies in an interval of width d, and S_s^2=(s-1)^{-1}sum_i(U_i-bar U)^2, then for 0<epsilon<1,

P(|S_s-sqrt(Var(U))|>d sqrt(2log(2/epsilon)/(s-1)))<=epsilon.

This is the precise statement used at source L000610-L000611. Its normalization is s-1, not s. For each fixed lambda, the residuals here are iid and lie in an interval of width at most 2(R_Y+R_Z), so every hypothesis is satisfied.

Apply this inequality to the T+1 grid values {0,1/T,...,1}, with failure probability eta/(T+1) at each value, where eta=delta/(2QT). A union bound gives the grid error bound

2(R_Y+R_Z) sqrt(2log(4QT(T+1)/delta)/(s-1))

with probability at least 1-eta.

The population standard deviation is Lipschitz in lambda with constant sqrt(Var(Z_q))<=R_Z. The sample standard deviation is a seminorm of the centered observation vector and is Lipschitz with constant S_{Z,s}<=R_Z sqrt(s/(s-1))<=sqrt(2)R_Z. These bounds follow by the triangle inequality and by bounding a variance with the squared distance to the midpoint of [-R_Z,R_Z]. Approximating any lambda by a grid point within 1/T therefore adds at most (1+sqrt(2))R_Z/T<=2sqrt(2)R_Z/T. Consequently, with probability at least 1-eta,

sup_{lambda in [0,1]} |S_{q,s}(lambda)-sigma_q(lambda)|

<=2(R_Y+R_Z) sqrt(2log(4QT(T+1)/delta)/(s-1))+2sqrt(2)R_Z/T.

The uniformity permits substitution of the sample-dependent lambda_tilde without conditioning on it.

## step_003: Simultaneous Event and Adaptivity

Intersect the two events for each fixed (q,s). By the population Lipschitz bound,

|sqrt(A_q)-sqrt(A_hat_{q,s})|

<=R_Z |lambda_q^*-lambda_tilde_{q,s}|+|sigma_q(lambda_tilde_{q,s})-S_{q,s}(lambda_tilde_{q,s})|

<=rho_{q,s}.

The failure probability for this pair is at most 2eta=delta/(QT). Union bounding over q and K<=s<=T yields an event E with P(E)>=1-delta on which the inequality holds for all such pairs. At an adaptive decision time, a unit's statistics are exactly its prefix statistics at s=n_{q,t}; hence the event covers every decision time without an optional-stopping assertion.

Both sides of the concentration inequality are needed. On E,

sqrt(A_q)<=sqrt(A_UCB_{q,s})<=sqrt(A_q)+2rho_{q,s}.

There is a fixed constant C_rho such that

rho_{q,s}<=C_rho sqrt(L/(s-1)),  K<=s<=T.

To verify this, the first logarithm in rho is at most L, the coefficient term is bounded by a constant times g_s because g_s<=1, and 1/T<=sqrt(L/(s-1)) since s<=T and L>=1.

## step_004: Oracle and Quantitative Allocation Control

Put d_q=sqrt(w_q A_q/c_q), beta_q=d_q/Lambda. Then sum_q c_q beta_q=1 and n_q^*=B beta_q. For every positive allocation n with sum_q c_q n_q<=B, Cauchy-Schwarz gives

Lambda^2<=(sum_q w_q A_q/n_q)(sum_q c_q n_q)<=B sum_q w_q A_q/n_q.

Equality holds at n_q^*. Thus the oracle objective is Lambda^2/B, and

w_q A_q/(n_q^*)^2=(Lambda^2/B^2)c_q.

There is a fixed positive lower bound for every beta_q, namely

beta_lower=min_q sqrt(w_q A_min/c_q)/(sum_j sqrt(w_j A_+ c_j))>0.

Also beta_q<=1/c_q. Let H=2C_rho/sqrt(A_min beta_lower).

We first establish allocation control when L<epsilon_0 B, where epsilon_0>0 is a sufficiently small fixed constant chosen below. Since K<=K_0 L+1, choose epsilon_0<=min{1,1/(4S_c K_0)} and B_0>=max{1,2c_min,4(S_c+c_max)}. Then

D=B-S_c K-c_max>=B/2>0.

The source stopping rule gives a remainder Rem=B-sum_q c_q n_{q,B} in [0,c_max), including when initialization itself exhausts the usable budget. In the present regime,

sum_q c_q(n_{q,B}-K)=B-S_c K-Rem>=D.

Because sum_q c_q beta_q=1, some unit a satisfies n_{a,B}-K>=beta_a D. In particular it was selected adaptively. At its last adaptive selection, its pre-selection count is n_{a,B}-1. Every unit is feasible at that time, so the selection rule and optimism imply, for every q,

w_q A_q/(c_q n_{q,B}^2)<=I^*_{q,t}<=I^{UCB}_{q,t}<=I^{UCB}_{a,t}.

Since K>=2, both n_{a,B}-1 and n_{a,B}-2 are at least beta_a D. Taking square roots, applying the upper UCB bound, and using d_a=Lambda beta_a gives

d_q/n_{q,B}<=Lambda/D+2C_rho Lambda sqrt(L)/(sqrt(A_a beta_a)D^{3/2})

<=Lambda/D(1+H sqrt(L/D)).

Therefore

n_{q,B}>=beta_q D/(1+H sqrt(L/D))

>=B beta_q-beta_q(S_c K+c_max+H sqrt(BL)),

where the last step uses 1/(1+x)>=1-x and D<=B. Define G=S_c K+c_max+H sqrt(BL) and Delta_q=beta_q G. Budget feasibility then gives the upper deviation:

c_q(n_{q,B}-n_q^*)<=sum_{j!=q}c_j Delta_j.

Thus

|n_{q,B}-n_q^*|<=max{beta_q,(1-c_q beta_q)/c_q}G<=G/c_min.

This explicitly retains the initialization cost S_c K; it is not an O(1) term. Since L<=B, L>=1 and B>=1,

G<=(S_c K_0+S_c+c_max+H)sqrt(BL).

Set D_g=(S_c K_0+S_c+c_max+H)/c_min and decrease epsilon_0, if needed, so that epsilon_0<=beta_lower^2/(4D_g^2). It follows throughout this regime that

|n_{q,B}-n_q^*|<=D_g sqrt(BL)<=beta_lower B/2,

and hence n_{q,B}>=B beta_q/2. All constants and thresholds are independent of delta.

## step_005: Regret Conversion for Every Feasible Confidence Level

In the regime L<epsilon_0 B, apply Taylor's theorem to f_q(x)=w_q A_q/x between n_q^* and n_{q,B}:

f_q(n_{q,B})-f_q(n_q^*)=-w_q A_q(n_{q,B}-n_q^*)/(n_q^*)^2+w_q A_q(n_{q,B}-n_q^*)^2/xi_q^3.

Here xi_q>=B beta_q/2>=B beta_lower/2. The summed first-order term is exactly

(Lambda^2/B^2)(B-sum_q c_q n_{q,B})=(Lambda^2/B^2)Rem.

It is nonnegative, not nonpositive, and is at most Lambda^2 c_max/B^2. The quadratic term is at most

8S_0 D_g^2 L/(beta_lower^3 B^2).

Since Lambda is bounded above by a fixed constant and L>=1, the objective gap on E is at most a fixed constant times L/B^2.

It remains to handle L>=epsilon_0 B. One cannot infer a sublinear count gap uniformly in this regime. Instead, initialization alone gives a deterministic bound. From L<=6ell,

K>=K_0 ell>=K_0 L/6.

Therefore, without using E or assuming an adaptive selection occurred,

sum_q w_q A_q/n_{q,B}-Lambda^2/B<=sum_q w_q A_q/K

<=6S_0/(K_0 L)<=6S_0 L/(K_0 epsilon_0^2 B^2).

This includes budgets that leave no adaptive phase and confidence levels exponentially small in B, whenever initialization remains feasible. Combining the two regimes, on E the objective gap is bounded by C_* L/B^2 for a fixed C_* and all B>=B_0 under the stated feasibility condition.

## step_006: Expectation and Specialization

On E^c, all terminal counts are still at least K. Since the oracle objective is nonnegative, the objective gap is at most V_max=sum_q w_q A_q/K. Taking expectations yields

R(B)<=C_* L/B^2+delta V_max<=6C_* log(QT/delta)/B^2+delta V_max.

This is the stated inequality, for example with C_1=6C_* and C_2=1. The choices of K_0,C_1,C_2,B_0 depend only on the permitted fixed parameters, not on delta or B.

For delta=B^-2 and sufficiently large B, T=Theta(B), ell=Theta(log B), and K=Theta(log B). Thus S_c K<=B eventually, so initialization is feasible. The first term is O(log B/B^2), while delta V_max=O(1/(B^2 log B)). This proves the requested consequence.

## Completion Check

The argument covers Q=1, clipped coefficients at 0 or 1, zero empirical denominators outside E, nonintegral budgets and heterogeneous costs, and initialization-only runs. No additional assumption such as log(1/delta)=o(B) is imposed. The only external theorem used as a black box is the explicitly stated standard independent bounded sample-standard-deviation inequality, with all of its hypotheses checked. There is no unresolved private proof obligation.
