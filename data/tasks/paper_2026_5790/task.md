# Problem

## Setup

Let d be a positive integer and let Sigma be a real symmetric positive-definite d x d matrix. For each class c in {+,-}, let p_c be a measurable probability density on (0,infinity). Under class c, draw u with density p_c and independently draw g~N(0,Sigma), then set z=sqrt(u)g. Define the Mahalanobis energy q(z)=z^T Sigma^{-1}z.

For q>0 define

F_c(q)=integral_0^infinity u^(-d/2) exp(-q/(2u))p_c(u)du,

h(q)=log F_+(q)-log F_-(q).

The notation E_c[·|q] refers to the probability density on u>0 proportional to u^(-d/2)exp(-q/(2u))p_c(u). When the finite right limit lim_{epsilon down to 0}h(epsilon) exists, denote it by h(0). An integral from 0 involving posterior expectations is interpreted as the limit of integrals from epsilon>0 as epsilon decreases to zero.

The monotone-likelihood-ratio (MLR) assumption, when imposed, is

p_+(v)p_-(u)>=p_+(u)p_-(v) for almost every pair 0<u<v.

This is the nondecreasing likelihood-ratio condition, expressed so it also specifies the meaning when a density vanishes.

For aggregation, let K be a positive integer. Conditional on class c, let z_1,...,z_K be independent draws from the class model just specified, and put q_k=q(z_k).

In a specialization, let nu>0, let s_-=1 and s_+=r>1, and draw v independently of g with density

p_v(v)=[(nu/2)^(nu/2)/Gamma(nu/2)]v^(-nu/2-1)exp(-nu/(2v)), v>0,

where Gamma(a)=integral_0^infinity t^(a-1)exp(-t)dt for a>0. Set u=s_c^2v and z=s_c sqrt(v)g, so p_c in the definitions above is the density of this class-dependent u. The aggregation model again uses independent draws conditional on class.

A randomized test is a measurable function phi of the observed data with values in [0,1], giving its probability of declaring class +. Its false-positive and true-positive probabilities are E_-[phi] and E_+[phi]. The threshold ROC of a statistic is the set of these pairs for tests that declare + above a threshold, allowing randomization at equality and the constant tests.

## Task

Prove the following integrated theorem.

1. For every q>0,

   -2 d/dq log F_c(q)=E_c[u^(-1)|q],

   h'(q)=(1/2)(E_-[u^(-1)|q]-E_+[u^(-1)|q]).

   Whenever the finite endpoint h(0) exists,

   h(q)=h(0)+(1/2)integral_0^q(E_-[u^(-1)|t]-E_+[u^(-1)|t])dt.

   Under the MLR assumption, h is nondecreasing.

2. In the inverse-gamma scale specialization,

   h(q)=-d log r+((nu+d)/2)[log(1+q/nu)-log(1+q/(nu r^2))],

   h(0)=-d log r, lim_{q->infinity}h(q)=nu log r, and h is strictly increasing. Thus each one-location log-likelihood contribution is bounded in [-d log r,nu log r], although q has unbounded support under either class.

3. If h is strictly increasing, thresholding h(q) and thresholding q induce the same one-location threshold ROC. For K observations in the specified aggregation model, the Neyman-Pearson optimal statistic is sum_{k=1}^K h(q_k): for every alpha in [0,1], a threshold test based on this sum, with boundary randomization or a constant decision if needed, maximizes E_+[phi] among all measurable randomized tests of (z_1,...,z_K) satisfying E_-[phi]<=alpha. In the inverse-gamma scale specialization, its summands lie in the interval stated in part 2, while the raw energy sum has unbounded support.
