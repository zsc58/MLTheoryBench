# Reference Proof

## Contract and constants

The loss sequence is fixed independently of the coordinate samples. All expectations below are over those samples, except where an auxiliary randomization is explicitly introduced. The variance W_T is the deterministic supremum over X^T in the task, not the variance of only the generated centers. Constants denoted by C may depend on r,R,G,L, but not on d,T,W_T or lambda. Put K=(1-xi)X and epsilon=L delta/2. Write log_+(x)=max{0,log x} for x>0. In the strongly convex case, lambda<=L, by combining strong monotonicity of the gradient with L-smoothness on the nonempty interior of X.

We prove the following obligations explicitly: feasible queries and comparator transfer; estimator bias and moments; historical-coordinate probabilities; linear and convex variance conversions; the adaptive convex regret bound; and the strongly convex bound with the stated schedule. The sampling-gap bounds are also recorded with their boundary cases, although the final variance conversion does not need coupon-collector estimates.

## 1. Feasibility and comparator transfer

Since 0<delta<=r/2, we have 0<xi<=1/2. If w=(1-xi)x belongs to K, then

w±delta e_i=(1-xi)x+xi(±r e_i) belongs to X.

Thus all queries are feasible. All projections exist uniquely because K is nonempty, compact, and convex. The center, internal point, buffer, and current step size are determined by the history before the current coordinate sample.

Let x* minimize the cumulative loss over X, and put u=(1-xi)x*. This is a deterministic comparator in K. Lipschitzness gives

sum_t[ell_t(u)-ell_t(x*)]<=G xi R T.

Smoothness gives

[ell_t(w_t+delta e_i)+ell_t(w_t-delta e_i)]/2-ell_t(w_t)<=L delta^2/2.

Consequently, queried-loss regret is at most sum_t[ell_t(w_t)-ell_t(u)]+C. Indeed, delta<=1/(2d^2LTR) bounds both cumulative correction terms by constants with the permitted dependencies.

## 2. Estimator properties

Write q_t=nabla ell_t(w_t). For every coordinate define, privately for the analysis,

z_{t,i}=[ell_t(w_t+delta e_i)-ell_t(w_t-delta e_i)]/(2delta).

This vector is predictable, though the learner observes only its sampled entry. Integrating the directional derivative on the query segment gives

|z_{t,i}-q_{t,i}|<=epsilon,  |z_{t,i}|<=G.

The full historical buffer satisfies m_{t,i_t}=v_{a_t}. Therefore

g_t=m_t+d(v_t-m_{t,i_t})e_{i_t},

and

A_t:=||g_t-m_t||^2=d^2(v_t-v_{a_t})^2<=4d^2G^2.

Conditional on the pre-round history, uniform sampling cancels the buffer:

E[g_t|history]=z_t,

so

||E[g_t|history]-q_t||<=sqrt(d)epsilon.

Since ||w_t-u||<=2R, replacing gradients by estimators in expected comparator inner products costs at most

2RT sqrt(d)epsilon<=1/(2d^(3/2)).

This corrects the source's overly small Euclidean bias estimate. The cumulative cost remains a harmless constant.

For moments, ||q_t||<=G and the elementary square inequality imply

E[v_t^2]<=2G^2/d+2epsilon^2.

The historical-coordinate calculation below, applied to the predictable vector z_s with zero initialization, gives the same bound for E[v_{a_t}^2]. Hence

a_t^err:=E[A_t]<=8dG^2+8d^2epsilon^2<=C_0 d,

where C_0>0 depends only on the permitted fixed parameters.

Set q_0=0 solely as a notation for initialization. Expanding the difference between v_t-v_{a_t} and q_{t,i_t}-q_{a_t,i_t}, using an error at most 2epsilon and a gradient-coordinate difference at most 2G, gives

Vbar_T<=d^2 sum_t(q_{t,i_t}-q_{a_t,i_t})^2+C.

Here C is uniform in d,T because d^2T epsilon<=1/(4R), and d^2T epsilon^2 is bounded as well. No actual loss at time zero is introduced.

## 3. Historical-coordinate law and sampling gaps

For 1<=s<t and a specified coordinate i,

P(i_t=i,a_t=s)=d^(-2)(1-1/d)^(t-s-1).

This is a joint probability. Summing it over i gives P(a_t=s)=d^(-1)(1-1/d)^(t-s-1). The event consists of sampling i at s and t and avoiding it at intermediate rounds. It is independent of the history strictly before s. For s=0, the corresponding specified-coordinate probability is d^(-1)(1-1/d)^(t-1).

It follows that, for any predictable vector sequence h_s, zero initialization h_0=0, and deterministic vector c,

E[(h_{a_t,i_t}-c_{i_t})^2]
= sum_{s=1}^{t-1} d^(-2)(1-1/d)^(t-s-1) E||h_s-c||^2
  +d^(-1)(1-1/d)^(t-1)||c||^2.

The proof is expansion over s and i followed by conditioning on the history before s. The formula remains valid for d=1 with the conventional value of a zeroth power. Applying it with h_s=z_s and c=0 proves the historical moment bound used above, since ||z_s||^2<=2G^2+2d epsilon^2 and the geometric weights sum to at most 1/d.

For completeness, define the sampling gaps as follows. For each t in {1,...,T} and i in {1,...,d}, let

tau^-_{t,i}=max({0} union {s in {1,...,t-1}: i_s=i}),

tau^+_{t,i}=min({T+1} union {s in {t,...,T}: i_s=i}),

rho_{t,i}=tau^+_{t,i}-tau^-_{t,i}.

Thus 0 is the backward sentinel when there is no previous occurrence, and T+1 is the forward sentinel when there is no occurrence at or after t. These are endpoint conventions, not additional algorithmic samples. Define the backward and forward durations by

B_{t,i}=t-tau^-_{t,i},  F_{t,i}=tau^+_{t,i}-t+1.

Then rho_{t,i}=B_{t,i}+F_{t,i}-1, with 1<=B_{t,i}<=t and 1<=F_{t,i}<=T-t+2.

To compare these durations with infinite searches, extend the independent uniform coordinate draws beyond both ends of the horizon, solely for analysis. Let U^-_{t,i} be the number of draws until coordinate i first appears in the backward list i_{t-1},i_{t-2},..., and let U^+_{t,i} be the corresponding number for the forward list i_t,i_{t+1},.... The extensions agree with every original draw in their respective lists. Hence, simultaneously for all i,

B_{t,i}=min{U^-_{t,i},t},

F_{t,i}=min{U^+_{t,i},T-t+2}.

A fixed-coordinate geometric waiting time U^-_{t,i} or U^+_{t,i} has mean d. For either infinite list, the maximum over i is its coupon-collection time. This has mean dH_d, where H_d=sum_{j=1}^d1/j<=1+log d: after k-1 distinct coordinates, the next new coordinate has success probability (d-k+1)/d, so the expected additional waiting time is d/(d-k+1), and summing these expectations gives dH_d.

The simultaneous domination and rho_{t,i}=B_{t,i}+F_{t,i}-1 now give

E[rho_{t,i}]<=2d-1,

E[max_i rho_{t,i}]<=E[max_i B_{t,i}]+E[max_i F_{t,i}]-1<=2dH_d-1.

These statements include d=1, when B_{t,1}=F_{t,1}=rho_{t,1}=1, and they include t=1 and t=T under the explicit sentinel definitions. No coupon-collector bound is needed in the next section.

## 4. Conversion to gradient variance

### Linear losses

Write q_t=b_t for t>=1, a deterministic vector, set b_0=0 for initialization, and let c=T^(-1)sum_t b_t. Central differences are exact. Since the gradients do not depend on their evaluation points, W_T=sum_t||b_t-c||^2. Uniform sampling gives

sum_t E[(b_{t,i_t}-c_{i_t})^2]=W_T/d.

Summing the historical identity and exchanging the finite sums gives

sum_t E[(b_{a_t,i_t}-c_{i_t})^2]<=W_T/d+||c||^2<=W_T/d+G^2.

Indeed, the weights associated with each positive historical index sum to at most 1/d, and the initialization weights sum to at most one. Thus

E[Vbar_T]<=4dW_T+2d^2G^2.

### Convex losses

For each realization let mu=T^(-1)sum_t q_t. Do not insert this random mean into the historical-coordinate expectation identity. Instead use a pathwise argument:

sum_t(q_{t,i_t}-q_{a_t,i_t})^2
<=2sum_t||q_t-mu||^2+2sum_t||q_{a_t}-mu||^2.

Each positive index s can occur as a_t at most once: its only possible successor is the next sample of the coordinate sampled at s. Also a_t=0 occurs at most d times. Consequently

sum_t||q_{a_t}-mu||^2<=sum_t||q_t-mu||^2+d||mu||^2.

Since ||mu||<=G and the realized centers belong to X, the definition of the supremum variance yields

Vbar_T<=4d^2W_T+2d^3G^2+C.

This is a deterministic inequality. In particular,

S:=sum_t E[A_t]<=C_1(d^2W_T+d^3).

## 5. Projection inequality and the linear/convex rates

We first derive the needed optimistic-gradient inequality rather than relying on an unspecified theorem. Let y in K, x=Pi_K(y-eta m), z=Pi_K(y-eta g), and u in K. Applying projection optimality to the two projections and expanding squared norms gives

<g,x-u><=[||u-y||^2-||u-z||^2-||x-y||^2-||x-z||^2]/(2eta)+<g-m,x-z>.

Young's inequality, followed by discarding a nonpositive term, gives

<g,x-u><=[||u-y||^2-||u-z||^2]/(2eta)+(eta/2)||g-m||^2.   (P)

This holds pathwise without stochastic assumptions.

Use y=hat w_t, x=w_t, z=hat w_{t+1}. The schedule eta_t=R/sqrt(d^2+Vbar_{t-1}) is positive, predictable, and nonincreasing. Summation by parts and diameter(K)<=2R bound the potential sum in (P) by 2R^2/eta_T. Convexity, the comparator transfer, and the bias estimate therefore reduce expected regret to these potentials and sum_t eta_t A_t/2, up to C.

The adaptive sum can be checked directly. Put B=4d^2G^2. Since 0<=A_t<=B,

sum_t A_t/sqrt(d^2+Vbar_{t-1})
<=sqrt(1+4G^2) sum_t A_t/sqrt(d^2+Vbar_t)
<=2sqrt(1+4G^2)(sqrt(d^2+Vbar_T)-d).

The second inequality follows by rationalizing the difference of consecutive square roots. Thus Jensen's inequality gives

E[Reg_T]<=C sqrt(d^2+E[Vbar_T])+C.

Substitution of the linear bound proves O(sqrt(dW_T)+d). Substitution of the convex bound proves O(d sqrt(W_T+d)). The positive d^2 term makes the schedule and these estimates valid even when all prediction errors vanish.

## 6. Strongly convex losses

This section verifies the exact eta_t=1/(lambda t) schedule and the small-variance baseline.

### A valid curvature-sensitive projection calculation

Nonexpansivity gives ||x-z||<=eta||g-m||. Subtract (lambda/2)||x-u||^2 from (P), with eta=1/(lambda t), and regroup the potentials. The remaining difference of squared distances is bounded by

(lambda/2)(||u-z||^2-||u-x||^2)
<=2lambda R||z-x||
<=2R||g-m||/t
<=||g-m||^2/(2lambda t)+2lambda R^2/t.

Therefore

<g,x-u>-(lambda/2)||x-u||^2
<= (lambda t/2)||u-y||^2-(lambda(t+1)/2)||u-z||^2
   +||g-m||^2/(lambda t)+2lambda R^2/t.   (SC)

This establishes the required step-size normalization directly. Strong convexity bounds ell_t(w_t)-ell_t(u) by the expression on the left with g replaced by q_t; the expected replacement cost was already bounded.

### A lower bound inherent in the supremum variance

For T>=2, choose auxiliary independent signs, each uniform on {-1,+1}, and evaluation points x_t=±r e_1 according to those signs. This randomization is only a device to lower-bound a deterministic supremum. Strong monotonicity implies

||nabla ell_t(r e_1)-nabla ell_t(-r e_1)||>=2lambda r.

Thus the variance of each auxiliary gradient is at least lambda^2r^2. For independent vectors Y_t, with bar Y=T^(-1)sum_t Y_t, direct expansion gives

E sum_t||Y_t-bar Y||^2
= sum_t||E Y_t-T^(-1)sum_s E Y_s||^2
  +(1-1/T)sum_t E||Y_t-E Y_t||^2.

Apply this identity to Y_t=nabla ell_t(x_t), taking expectation over the auxiliary signs. Every auxiliary point sequence is admissible in the defining supremum, so

W_T>=(T-1)lambda^2r^2.   (W)

This is a derived fact, not an added hypothesis.

### Prefix and tail

Let H=ceil(d/lambda). If T<=H, Lipschitzness and diameter(X)<=2R give Reg_T<=2GRT<=C d/lambda, using lambda<=L. This includes T=1.

Suppose T>H. Charge the first H rounds directly, at cost at most C d/lambda. Apply (SC) from H+1 through T. Its potentials telescope, leaving at most 2lambda(H+1)R^2<=C d/lambda. Together with comparator and bias corrections this gives

E[Reg_T]<=C d/lambda+(1/lambda)sum_{t>H} a_t^err/t
                   +2lambda R^2 sum_{t>H}1/t.

We have 0<=a_t^err<=M:=C_0d and total sum at most S<=C_1(d^2W_T+d^3). An elementary harmonic estimate gives

sum_{t>H} a_t^err/t<=M[1+log(2+S/(MH))].

For example, take N=H+ceil(S/M), bound the part with H<t<=min{N,T} by M sum_{t=H+1}^N1/t, and bound the remainder by S/N<=M; zero S is immediate. Since H>=d/lambda,

S/(MH)<=C lambda(W_T+d).

Moreover T>H and (W) imply W_T>=lambda^2r^2H>=lambda d r^2. Together with lambda<=L, this proves

lambda(W_T+d)<=C W_T.

The weighted prediction-error contribution is consequently at most C(d/lambda)log(2+dW_T).

Finally, (W) yields T<=1+W_T/(lambda^2r^2). For 0<lambda<=L,

lambda^2 log T
<=lambda^2 log(1+W_T/r^2)+2lambda^2 log_+(1/lambda)
<=C[1+log(1+W_T)].

The last bound uses boundedness of lambda and of lambda^2 log(1/lambda) on (0,1]. Hence the remaining term 2lambda R^2 sum_{t>H}1/t is also at most C(d/lambda)log(2+dW_T).

Combining the estimates proves

E[Reg_T]=O((d/lambda)log(2+dW_T)).

The quantities 1+log(1+z) and log(2+z) are comparable for z>=0. Every expectation, adaptive step, initialization contribution, and boundary case has now been accounted for. No specialized or unverified proof dependency remains.
