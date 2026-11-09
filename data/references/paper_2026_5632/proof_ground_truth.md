# Reference Proof

## Theorem-critical obligations

The proof must establish: simultaneous validity of learned intervals; an atom-sensitive squared-radius budget; a randomized calibration guarantee with correct online information timing; a finite partition with a squared-mass budget; uniform deterministic-rounding control; and the claimed sample, success-probability, representation, and query bounds. All six obligations are proved below. In particular, the implemented rounding rule uses one independently sampled pair consisting of an online index and a uniform seed per cell. It is not asserted that the inverse CDF of an average distribution can be evaluated from one arbitrarily selected component.

## Standard background used

Only the following standard-independent results are used, in addition to elementary finite-dimensional algebra and probability.

1. For nonempty compact convex sets and a continuous payoff affine in each argument, the infimum-supremum equals the supremum-infimum, and the extrema are attained.
2. If independent variables Z_i have range lengths b_i, then P(|sum_i(Z_i-E Z_i)|>t) <= 2 exp(-2t^2/sum_i b_i^2). For a martingale difference sequence with |D_i|<=b_i, the corresponding bound is 2 exp(-t^2/(2 sum_i b_i^2)). One-sided versions follow as well.
3. If N is binomial with mean lambda, then P(N<lambda/2)<=exp(-lambda/8). For nonnegative Z, P(Z>a)<=E[Z]/a.
4. Exponential weights, initialized uniformly over H alternatives and updated by exp(eta z_t^r) for gains z_t^r in [-1,1], satisfies the pathwise regret bound

max_r sum_t z_t^r <= sum_t sum_r pi_t(r)z_t^r + log(H)/eta + eta T/2.

The last inequality follows by upper-bounding each log-partition increment using the bounded-variable exponential-moment inequality and lower-bounding the final partition function by the contribution of each individual alternative. It therefore applies to the adaptive gains below. Each application of these results has its hypotheses checked in the corresponding argument.

## 1. Parameters, notation, and learned intervals

Write m(x)=E[Y|X=x] for a measurable [0,1]-valued version of the conditional mean, and p_x=P_X({x}). These quantities are used only in the analysis and are not supplied to the learner. The atoms, those x with p_x>0, form an at most countable set with total mass at most one. Conditional means at atoms are unambiguously determined; a bounded version elsewhere suffices.

Fix a sufficiently small universal c>0, to be chosen after the error estimates, and put alpha=c epsilon and gamma=alpha/64. Take N_grid=ceil(1/gamma) and

V={i/N_grid: i=0,...,N_grid},  K=|V|,

so V contains both endpoints, is a gamma-net of [0,1], and K<=192/alpha. Set

L=K+log(|G|+1)+100,  J=b log(100L/alpha),

n0=ceil(C0 L J/alpha^2),  T=ceil(C0 L/alpha^2),  M=ceil(C0 L/alpha^2).

Here C0 and b are fixed universal constants. Choose them so that J>=1 and 2 n0 exp(-2J)<=0.01 uniformly in the stated regime. Such a choice exists: for fixed C0, log n0 is bounded by a universal constant plus log L+log J+2 log(1/alpha), whereas J is a sufficiently large fixed multiple of log(100L/alpha). The constants are fixed before choosing c. Integer ceilings affect subsequent estimates only by universal factors.

Split a predetermined number of iid observations into three disjoint blocks S0, S1, S2 of these sizes. They are independent. Only the contexts of S2 are used.

Let O0 be the finite set of contexts observed in S0. For x in O0, let N_x be its count and ybar_x its empirical label mean, and set

r_x=min{1,sqrt(J/N_x)},
I_x=[ybar_x-r_x,ybar_x+r_x] intersected with [0,1].

For x outside O0 set N_x=0, r_x=1, and I_x=[0,1]. Write I_x=[a_x,b_x] and define

A_x={v in V: dist(v,I_x)<=gamma}.

Each A_x is nonempty, and every u in I_x has an element of A_x within gamma.

Almost surely no non-atom occurs twice in S0. For each pair of sample indices, the probability that their contexts agree at a non-atom is

E[1{X_i is not an atom} P_X({X_i})]=0,

and there are finitely many pairs. Conditional on the sampled contexts, labels at a repeated atom are independent [0,1]-valued variables with mean m(x). Whenever r_x<1, Hoeffding's inequality gives coverage failure probability at most 2 exp(-2J). Whenever r_x=1, the clipped interval is all of [0,1] and coverage is automatic. There are at most n0 observed contexts, so the union bound gives an S0-measurable event E_cov of probability at least 0.99 on which m(x) belongs to I_x for every x. In particular, singleton non-atomic observations have N_x=1 and r_x=1; unobserved points also have the full interval. Thus no uncountable union bound is being used.

For the radius estimate, fix an atom of mass p and put lambda=n0 p. Its count N is binomial. If lambda<=2J, then

p^2 E[r(N)^2] <= p^2 <= (2J/n0)p.

If lambda>2J, then

E[r(N)^2] <= P(N<lambda/2)+2J/lambda <= exp(-lambda/8)+2J/lambda.

Since lambda exp(-lambda/8) is bounded and J>=1, multiplication by p^2 gives

E[p^2 r(N)^2] <= C (J/n0)p.

The nonnegative summands may be summed over the countable atom set. Consequently

E[sum_{x: p_x>0} p_x^2 r_x^2] <= C J/n0 <= C alpha^2/L.

Markov's inequality gives an event E_rad of probability at least 0.90 on which

sum_{x: p_x>0} p_x^2 r_x^2 <= C1 alpha^2/L.                 (1)

Here and below C1 and all other constants not explicitly parameter-dependent are universal. Coverage and the radius bound hold jointly with probability at least 0.89.

## 2. Randomized learning with the correct information timing

For a measurable randomized grid predictor q:X->Delta(V), define

B_P(q;g,v)=E[g(X)q_X(v)(v-Y)],
Cal_P(q;G)=max_g sum_v |B_P(q;g,v)|.

For r=(g,s), where s:V->{-1,+1}, define

R_r(q)=E[g(X)sum_v s(v)q_X(v)(v-Y)].

For deterministic f, R_r(f)=E[g(X)s(f(X))(f(X)-Y)]. All these expectations are over a fresh observation with the learned predictor held fixed. The elementary signed-sum identity gives

Cal_P(q;G)=max_r R_r(q),

and likewise for f. Let H=|G|2^K be the number of indexed signed tests. Then log H<=L.

Condition on any fixed S0 satisfying E_cov. The online algorithm starts with uniform exponential weights pi_1 over the H signed tests. Before the t-th observation, the previous observations determine pi_t and the entire predictive map q_t. For every possible query x, set

c_t(x,v)=sum_{r=(g,s)} pi_t(r)g(x)s(v),

and choose q_t(x) in Delta(A_x) to minimize

max_{u in I_x} sum_v q_t(x)(v)c_t(x,v)(v-u),

with fixed deterministic measurable tie-breaking. This defines a map from all contexts to distributions before X_t is observed; training need only evaluate that map at the realized X_t. In particular, no label from round t is used to choose q_t.

The coefficient magnitudes are at most one. For a fixed x and any u in I_x, choose v in A_x with |v-u|<=gamma. The payoff of this pure action is c_t(x,v)(v-u)<=gamma. The action simplex and the interval are nonempty, compact, and convex, and the payoff is continuous and affine in both variables. The stated minimax theorem therefore gives a distribution q with worst-case payoff at most gamma. For fixed q the payoff is affine in u, so its worst case is at a_x or b_x. The action is thus found by the finite endpoint linear program with nonnegative q summing to one, q zero outside A_x, and the two endpoint payoff constraints. A concrete polynomial and measurable selection rule is given in Section 6 below.

On observation (X_t,Y_t), define

z_t^r=g(X_t)sum_v s(v)q_t(X_t)(v)(v-Y_t),
W_t=sum_r pi_t(r)z_t^r,

and update pi_{t+1}(r) proportionally to pi_t(r)exp(eta z_t^r), where

eta=sqrt((log H+log 80)/T).

Each z_t^r and W_t lies in [-1,1]. Conditional on the past and X_t, the label mean is m(X_t), which belongs to I_{X_t}. The minimax inequality therefore gives E[W_t | past,X_t]<=gamma, and hence E[W_t | past]<=gamma. Applying the martingale bound to W_t-E[W_t | past], whose magnitude is at most two, and then applying the pathwise exponential-weights regret inequality yields, except on an event of probability at most 0.025,

max_r (1/T)sum_t z_t^r <= gamma+C sqrt((log H+log 80)/T).    (2)

Define q_X(v)=T^{-1}sum_t q_t(X)(v). For each signed test let

D_t^r=R_r(q_t)-z_t^r.

Conditional on the previous observations and S0, q_t is fixed and observation t is fresh from P. Thus E[D_t^r | past,S0]=0 and |D_t^r|<=2. Also, pathwise,

R_r(q)-(1/T)sum_t z_t^r=(1/T)sum_t D_t^r.

Azuma-Hoeffding and a union bound over the H tests give, with failure probability at most 0.025,

max_r |R_r(q)-(1/T)sum_t z_t^r|
 <= sqrt(8 log(80H)/T).

Combining with (2) and the signed identity gives, with conditional probability at least 0.95 over S1,

Cal_P(q;G)<=A1 alpha,                                      (3)

for a universal A1. Every q_t(x), and therefore q_x, is supported on A_x. Independence of S1 means that this same conditional guarantee holds after additionally conditioning on S2 and any event determined by S0,S2.

## 3. The complete finite partition

Order contexts lexicographically. Let w_1<...<w_r be the distinct ordered contexts in S2; here r>=1 because M>=1. Put U0=X outside O0. Form the following cells, discarding empty sets:

- each observed singleton {x}, x in O0;
- U0 intersected with {x:x<w_1};
- U0 intersected with each cutpoint singleton {w_j};
- U0 intersected with each open gap {x:w_j<x<w_{j+1}};
- U0 intersected with {x:w_r<x}.

These measurable disjoint cells partition X. Denote their family by Pi and the subfamily contained in U0 by Pi_unobs. There are at most n0+2M+1 cells. The singleton cutpoint cells and both tails are included even when the distribution has atoms or all partition observations agree.

For independent A,B,W_1,...,W_M from P_X, consider the event that A differs from B and no W_i lies in their closed lexicographic interval. Conditional on the multiset of all M+2 observations, an isolated ordered pair of sample labels must have adjacent distinct context values, each of multiplicity one. There are at most 2(M+1) such ordered pairs out of (M+2)(M+1). Exchangeability therefore bounds the event probability by 2/(M+2).

For fixed S0, the sum of squared unobserved cell masses is the P_X x P_X mass of pairs in the same unobserved cell. Its diagonal contribution is sum_{x in U0: p_x>0} p_x^2. Two distinct points in the same cell cannot have a partition observation in their closed interval, precisely because cutpoints are singleton cells. Averaging over S2, and using that restriction of P_X to U0 is dominated by P_X, gives

E_{S2}[sum_{C in Pi_unobs} P_X(C)^2 | S0]
 <= sum_{x in U0: p_x>0}p_x^2+2/(M+2).

An atom of mass p is unobserved in S0 with probability (1-p)^n0. Since p(1-p)^n0<=1/(n0+1),

E_{S0,S2}[sum_{C in Pi_unobs}P_X(C)^2]
 <= 1/(n0+1)+2/(M+2)
 <= C alpha^2/L.

Markov's inequality gives an event E_part of probability at least 0.95 on which

sum_{C in Pi_unobs}P_X(C)^2<=C2 alpha^2/L.                  (4)

No independence between E_part and the S0 events is required. A union bound gives probability at least 0.84, and in particular at least 0.80, for E_cov intersect E_rad intersect E_part.

## 4. Implemented cell-wise rounding

Fix all three data blocks, with E_cov holding, and the resulting supported predictor q=T^{-1}sum_t q_t. Independently across cells, and independently of the data, draw pairs (tau_C,U_C), with tau_C uniform on {1,...,T}, U_C uniform on (0,1), and the two components independent. On x in C, define f(x) by inverse-CDF sampling from q_{tau_C}(x) at U_C using the fixed ordering of V. Once these pairs and the data are fixed, f is a deterministic function.

For every fixed x, averaging over its cell's pair gives

P(f(x)=v | data)=(1/T)sum_t q_t(x)(v)=q_x(v).

Furthermore f(x) belongs to A_x, and different cells depend on independent pairs. These facts do not assert that the pair-based sampler and the inverse CDF of q_x produce identical functions of a shared scalar seed. They establish exactly the properties required for the following concentration proof. Using seeds in (0,1) avoids a zero-endpoint support convention; this has the same continuous uniform distribution for all probability calculations.

For v in A_x, let clip_x(v) be its projection onto I_x. Then |v-clip_x(v)|<=gamma. For a signed test r=(g,s), put a_r(x,v)=g(x)s(v). Its magnitude is at most one. Since f and q are functions of the context once training is fixed, replacing Y by m(X) does not change their population residuals.

For each cell define the centered clipped contribution

Z_{r,C}=integral_C [a_r(x,f(x))(clip_x(f(x))-m(x))
 -sum_v q_x(v)a_r(x,v)(clip_x(v)-m(x))] dP_X(x).

The pointwise marginal identity and boundedness imply E_seed Z_{r,C}=0. For fixed r these variables are independent across cells. On an observed singleton {x}, coverage puts both clip_x(v) and m(x) in an interval of length at most 2r_x. The clipped payoff is therefore in [-2r_x,2r_x], and Z_{r,{x}} has range length at most 4p_x r_x. This range is zero for a zero-mass observed singleton. On an unobserved cell, I_x=[0,1], so the clipped payoff is in [-1,1] and the range length is at most 2P_X(C).

Define

V_Pi=sum_{x in O0: p_x>0}p_x^2 r_x^2
     +sum_{C in Pi_unobs}P_X(C)^2.

The sum of squared range lengths is at most 16 V_Pi. Thus Hoeffding's inequality and a union bound over the H signed tests give, with probability at least 0.99,

max_r |sum_C Z_{r,C}| <= sqrt(8 V_Pi log(200H)).

If V_Pi=0, all the centered contributions have zero range and zero mean, so the same conclusion holds directly without division by zero.

It remains to restore the grid discrepancy. For every realized choice of seeds,

|integral [a_r(x,f(x))(f(x)-clip_x(f(x)))
 -sum_v q_x(v)a_r(x,v)(v-clip_x(v))] dP_X(x)| <= 2gamma.

This is a deterministic upper bound on a possibly random quantity, not an assertion that the discrepancy is nonrandom. Consequently, with probability at least 0.99 over the pairs,

max_r |R_r(f)-R_r(q)|
 <= sqrt(8 V_Pi log(200H))+2gamma.                          (5)

On E_rad and E_part, (1) dominates the observed-atom sum and (4) controls the other sum, so V_Pi<=C alpha^2/L. Since log(200H)<=C L and gamma=alpha/64, (5) is at most A2 alpha for a universal A2. Applying the signed identity yields

Cal_P(f;G)<=Cal_P(q;G)+A2 alpha.                           (6)

## 5. Success probability and sample rate

With probability at least 0.80, S0,S2 satisfy all three required events. Conditional on every such choice, independence of S1 gives (3) with probability at least 0.95. Conditional on any resulting data and online states, (6) holds with probability at least 0.99 over the independent cell pairs. Thus the total success probability is at least

0.80 x 0.95 x 0.99 > 2/3.

Choose the universal c>0 small enough that c<1 and (A1+A2)c<=1. Then alpha=c epsilon is in the required interval and (3),(6) imply Cal_P(f;G)<=epsilon.

The constants used to construct the algorithm are universal. Since

K=O(1/epsilon),
L=O(1/epsilon+log(|G|+1)),
J=O(log((1/epsilon+log(|G|+2))/epsilon)),

integer rounding can be absorbed into a universal constant and

n=n0+T+M
 <= C ((1/epsilon+log(|G|+1)) log((1/epsilon+log(|G|+2))/epsilon))/epsilon^2.

This includes singleton or zero-valued group families and purely atomic, atomless, and mixed distributions. If |G|<=epsilon^{-kappa} for fixed kappa>=0, the displayed formula is tilde-O(epsilon^{-3}); constants may depend on kappa. The case kappa=0 simply restricts the nonempty family to cardinality one.

## 6. Representation, computation, and measurability

Define the cumulative quantities before round t by

S_{g,v}^{t-1}=sum_{s<t}g(X_s)q_s(X_s)(v)(v-Y_s).

The direct exponential weight of (g,sigma) is proportional to exp(eta sum_v sigma(v)S_{g,v}^{t-1}). Summing over all signs factorizes:

sum_sigma exp(eta sum_v sigma(v)S_{g,v}^{t-1})
 =product_v 2 cosh(eta S_{g,v}^{t-1}).

The group marginal pi_t(g) is obtained by normalizing these products, and the conditional sign mean is tanh(eta S_{g,v}^{t-1}). Therefore

c_t(x,v)=sum_g pi_t(g)g(x)tanh(eta S_{g,v}^{t-1}).

Every coefficient is computable from |G|K stored numbers and the supplied group evaluations, without enumerating sign patterns. The hyperbolic functions here are expressible by arithmetic and exp. Denominators are positive. Updates add g(X_t)q_t(X_t)(v)(v-Y_t) to each cumulative quantity.

For completeness, the endpoint optimization itself admits an elementary polynomial implementation in the specified real-operation model. Associate each allowed action v with the point

(c_t(x,v)(v-a_x), c_t(x,v)(v-b_x)) in R^2.

A distribution over actions produces a point in their convex hull, and its objective is the maximum of the two coordinates. A minimum can be represented on a segment joining at most two action points: if the convex hull is two-dimensional an interior point cannot minimize, because moving slightly in direction (-1,-1) improves both coordinates; every boundary edge joins action vertices. For a one-dimensional hull use its two endpoints, and for a singleton use its only point. On a segment, the objective is the maximum of two affine functions of the mixing weight. Its minimum is attained at a segment endpoint or where the two coordinates agree. Enumerate all action pairs, their endpoints, and such intersections when they lie in [0,1]. A fixed ordered choice of a minimizing candidate supplies a supported optimal q_t(x). There are polynomially many candidates, all computable by arithmetic and comparisons; zero denominators are handled by retaining the endpoints. This also supplies deterministic measurable tie-breaking and covers singleton allowed sets and equal interval endpoints.

During training, sort and group S0 contexts to build an observed-context table containing intervals and counts. Sort the distinct S2 contexts and store the gap and cutpoint cells, together with the observed singleton cells. Store all T online states and one pair (tau_C,U_C) for each cell. This uses O(T|G|K) online-state entries plus polynomially many interval, context, and seed entries. Only q_t(X_t) must be computed at round t. Training time is polynomial in n0,T,M,|G|,K,d in the stated computational model.

For a query x, first search the observed-context table, in O(d log(n0+1)) coordinate operations. If x is not observed, search the sorted S2 contexts to identify its gap, tail, or cutpoint cell in O(d log(M+1)) operations. Retrieve that cell's stored tau_C and U_C and the state indexed by tau_C. Evaluate the group functions, reconstruct only q_{tau_C}(x), and apply its inverse-CDF sampler at U_C. This is exactly the rounding rule analyzed in Section 4. It does not reconstruct the T-component average. The total query cost is polynomial in |G|,K,d,log(n+1), hence in |G|,d,1/epsilon,log(n+1).

Finally, the tables, equality tests, and lexicographic comparisons define measurable sets on the trace Borel context space. The group functions are measurable. The finite-candidate action selection uses measurable arithmetic and comparisons on its stated domains; all exceptional equalities have fixed choices. Thus each q_t and the final f are measurable, as are their joint constructions from the sample and seeds. Every query has a fixed value after training, including at zero-mass contexts. No conditional-mean or distribution oracle is used. This completes all theorem-critical obligations.
