# Reference Proof

## Proof Structure and Obligations

Fix n, y, c and delta as in the task. The proof must establish: (1) the almost-everywhere conditional product law of the labels; (2) the deterministic kernel-bias bound; (3) the conditional noise representation with the correct sub-Gaussian convention; (4) the needed fixed-weight concentration inequality, including its constants; (5) both kernel-mass regimes; and (6) the joint probability statement without evaluating an undefined estimator at zero kernel mass. All six obligations are derived below. No unrestricted stochastic-weight theorem is used as a black box.

## 1. Conditional Distribution of the Labels

For any label tuple (a_1,...,a_n) and Borel sets A_1,...,A_n, independence of the training pairs gives

P(Y_i in A_i, C_i=a_i for every i)
= product_{i=1}^n integral_{A_i} p_{a_i}(x) P_Y(dx).

This is also the integral, over the corresponding covariate rectangle under P_Y^n, of product_i p_{a_i}(x_i). Consequently a version of the conditional label law given Y_1,...,Y_n is

P(C_1=a_1,...,C_n=a_n | Y_1,...,Y_n)
= product_{i=1}^n p_{a_i}(Y_i)

for P_Y^n-almost every covariate vector. The label set is finite, so one exceptional null set suffices for all label tuples. Intersect this full-measure set with the sets on which the stipulated sub-Gaussian property holds at every observed covariate.

Fix a covariate vector in this full-measure set. The labels are conditionally independent, but their conditional distributions need not be identical. All subsequent probabilities and expectations until the final integration are under this conditional law.

## 2. Deterministic Bias

Write K_i=K_lambda(y,Y_i) and kappa=sum_i K_i. If kappa=0, the task makes no assertion about an estimator, so this covariate vector cannot produce a failure of the requested implication.

Suppose kappa>0. Define, privately for the proof,

theta_i=K_i/kappa,

bar p_c(y)=sum_i theta_i p_c(Y_i).

The weights are nonnegative and sum to one. Therefore

|p_c(y)-hat p_c(y)|
<= |p_c(y)-bar p_c(y)| + |bar p_c(y)-hat p_c(y)|.

By the triangle inequality and Lipschitz continuity,

|p_c(y)-bar p_c(y)|
<= sum_i theta_i |p_c(y)-p_c(Y_i)|
<= L sum_i theta_i ||y-Y_i||.

If theta_i>0, then K_i>0, and compact support implies ||y-Y_i||<=lambda. Terms with theta_i=0 contribute zero, regardless of their distances. Hence

|p_c(y)-bar p_c(y)| <= L lambda sum_i theta_i = L lambda.

This argument also covers L=0 and points exactly at distance lambda.

## 3. Conditional Noise and the Zero-Scale Case

Set epsilon_i=p_c(Y_i)-1_{C_i=c}. Under the conditional product law, these variables are independent, centered, and sigma-sub-Gaussian. In particular, the centering is at p_c(Y_i), not at p_c(y). Put

S=sum_i K_i epsilon_i,   V=sum_i K_i^2.

Then

bar p_c(y)-hat p_c(y)=S/kappa.

Because 0<=K_i<=1, we have V<=kappa. The kernel factors in S are not squared; squared factors occur only in V.

If sigma=0, the moment bounds at t=1 and t=-1 give E[cosh(epsilon_i)]<=1. Since cosh(u)>=1 with equality only at u=0, epsilon_i=0 almost surely. Thus S=0 almost surely, and the deterministic bias estimate already proves the result. Henceforth suppose sigma>0.

## 4. Complete Fixed-Weight Concentration Derivation

For every real t, conditional independence and the sub-Gaussian bounds imply

E[exp(t S/sigma)]
= product_i E[exp(t K_i epsilon_i/sigma)]
<= exp(t^2 V/2).

Thus E[exp(t S/sigma-t^2 V/2)]<=1 for every real t. Integrate this inequality against the standard Gaussian density exp(-t^2/2)/sqrt(2 pi). The integrand is nonnegative, so interchanging integration and expectation is valid. Completing the square in the scalar Gaussian integral gives

E[(1+V)^{-1/2} exp(S^2/[2 sigma^2(1+V)])] <= 1.

Indeed, for any real a and V>=0,

integral_R exp(t a-(1+V)t^2/2) dt/sqrt(2 pi)
= (1+V)^{-1/2} exp(a^2/[2(1+V)]).

Here V is deterministic under the conditional law. For a nonnegative random variable Z, Markov's inequality states P(Z>r)<=E[Z]/r for r>0. Apply it to

Z=(1+V)^{-1/2} exp(S^2/[2 sigma^2(1+V)])

with r=delta^{-1}. With conditional probability at least 1-delta,

|S| <= sigma sqrt(2(1+V) log(delta^{-1} sqrt(1+V))).

This proves exactly the concentration instance required for the classifier. Neither identically distributed conditional noises nor unrestricted random-weight concentration is needed.

## 5. Both Kernel-Mass Regimes

For 0<delta<1, both 1+v and log(delta^{-1} sqrt(1+v)) are positive and nondecreasing for v>=0. Using V<=kappa, the preceding event therefore implies

|S|/kappa
<= [sigma/kappa] sqrt(2(1+kappa) log(delta^{-1} sqrt(1+kappa))).

If kappa>1, then 1+kappa<=2 kappa, and consequently

|S|/kappa
<= [2 sigma/kappa] sqrt(kappa log(delta^{-1} sqrt(1+kappa)))
= 2 sigma alpha_n(y,delta)/kappa.

If 0<kappa<=1, then 1+kappa<=2 and

log(delta^{-1} sqrt(1+kappa)) <= log(sqrt(2)/delta).

Therefore

|S|/kappa
<= [2 sigma/kappa] sqrt(log(sqrt(2)/delta))
= 2 sigma alpha_n(y,delta)/kappa.

The endpoint kappa=1 is included in the second case; the two formulas agree there. No positive lower bound on kappa is needed.

## 6. Joint Probability and Conclusion

Let F be the event that kappa_n(y)>0 and the required error inequality fails, with the estimator and bound evaluated only on that positive-mass domain. For almost every covariate vector with positive mass, the deterministic bias estimate and the conditional concentration event show

P(F | Y_1,...,Y_n) <= delta.

For covariate vectors with zero mass, F is empty. Thus

P(F)
= E[P(F | Y_1,...,Y_n)]
<= delta P(kappa_n(y)>0)
<= delta.

Taking E=F complement proves the public claim. Measurability follows from the measurable kernel, the chosen conditional probabilities, and the measurable arithmetic operations on the positive-mass domain. The proof is for each fixed n, y, c and delta; it does not assert one event simultaneous over all of them. The almost-everywhere conditional guarantee established by this proof is sufficient for, and stronger than, the requested joint guarantee; the two forms are not equivalent in general.

## Source Normalization and Application Audit

The source's exponential-moment convention at L000451 uses sigma^2/2. Its assertion at L000463 that every centered Bernoulli noise admits sigma<=1/4 is therefore incorrect. The correct universal variance proxy is 1/4, corresponding to scale sigma=1/2.

This fact needs no external binary-noise theorem. For 0<q<1 and B distributed as Bernoulli(q), define h(t)=log E[exp(t(q-B))]. Direct differentiation shows h(0)=h'(0)=0 and h''(t)=r_t(1-r_t)<=1/4, where r_t is the probability of B=1 under exponential tilting. For t>=0, integrate h'' from 0 to t twice; for t<0, write h(t)=integral_t^0 (u-t)h''(u) du. In both cases h(t)<=t^2/8. For q=0 or q=1 the centered variable is identically zero. Thus sigma=1/2 is universally valid. At q=1/2, E exp(t(q-B))=cosh(t/2)=1+t^2/8+O(t^4), which forces sigma^2>=1/4 by comparison near zero. The public theorem permits any actual common scale and does not hardcode either number.

The quoted process inequality at L000450-L000453 lacks a relation between weights and noise and is false for arbitrary contemporaneously noise-dependent weights. No predictability or independence assumption is silently inserted into that external statement. Instead, Sections 1 and 4 explicitly prove the instance needed under the classifier's existing i.i.d. contract. This also resolves the source's inaccurate suggestion that conditional residuals must be identically distributed. All theorem-critical obligations of the frozen task are closed.
