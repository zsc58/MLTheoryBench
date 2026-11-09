# Reference Proof

## Proof Structure and Obligations

1. Identify the class density and normalized posterior from the Gaussian scale-mixture model.
2. Establish positive-energy finiteness and dominated differentiation, then derive posterior precision and h'.
3. Transfer MLR order through the normalized posterior tilt and prove the expectation inequality.
4. Integrate h' with the correct endpoint constant and improper-integral convention.
5. Evaluate the inverse-gamma specialization with the class scale included.
6. Establish strict increase, finite evidence bounds, and unbounded energy support.
7. Identify the one-location threshold ROC under a strictly increasing transformation.
8. Apply the Neyman-Pearson lemma to the conditionally independent product experiment.

## Complete Proof

### 1. Mixture density and posterior

Conditional on u, the density of z in class c is

(2pi)^(-d/2)|Sigma|^(-1/2) u^(-d/2) exp(-q(z)/(2u)).

Integrating against p_c(u) gives

f_c(z)=(2pi)^(-d/2)|Sigma|^(-1/2) F_c(q(z)).

Consequently, for z with q(z)>0, the likelihood ratio is exp(h(q(z))). Every conditional Gaussian law is absolutely continuous and assigns probability zero to z=0, so the same holds for either mixture. Thus q>0 almost surely under both classes, and a statistic defined for q>0 suffices for all testing claims.

Bayes' formula gives the normalized posterior density

pi_c(u|q)=u^(-d/2) exp(-q/(2u)) p_c(u)/F_c(q).

The conditional density given z depends on z only through q(z), so this also gives a version of the conditional density given q.

### 2. Finiteness, differentiation, and posterior precision

For every epsilon>0 and every exponent b>0, the function u^(-b) exp(-epsilon/(2u)) is bounded on (0,infinity): it tends to zero at both endpoints. For q>=epsilon, the kernels defining F_c(q) and its first derivative are therefore bounded by constants times p_c(u), with b=d/2 and b=d/2+1 respectively. Those dominating functions are integrable because p_c is a probability density. The kernel is positive wherever p_c is positive, so 0<F_c(q)<infinity for q>0.

The standard dominated differentiation result says that a parameterized integral can be differentiated when its derivative is locally dominated by an integrable function; dominated convergence also gives continuity of the resulting derivative. The bounds just verified establish all these hypotheses on compact positive-energy intervals. Hence

F_c'(q)=-(1/2) integral_0^infinity u^(-d/2-1) exp(-q/(2u)) p_c(u)du.

The numerator defining the posterior precision is finite by the same bound. Dividing by the positive denominator F_c(q) proves

-2 (log F_c)'(q)=E_c[u^(-1)|q].

Subtracting the class identities yields

h'(q)=(1/2)(E_-[u^(-1)|q]-E_+[u^(-1)|q]).

In particular h is continuously differentiable on (0,infinity).

### 3. MLR and monotonicity

Write w_q(u)=u^(-d/2)exp(-q/(2u)). For almost every 0<u<v, the posterior cross-product difference is

pi_+(v|q)pi_-(u|q)-pi_+(u|q)pi_-(v|q)

= [w_q(u)w_q(v)/(F_+(q)F_-(q))] [p_+(v)p_-(u)-p_+(u)p_-(v)].

Thus the assumed MLR inequality passes to the posteriors. Where density ratios are defined, the exact identity is

pi_+(u|q)/pi_-(u|q)=[F_-(q)/F_+(q)] p_+(u)/p_-(u).

The normalizing factor must not be omitted, but it is positive and independent of u.

The standard MLR implication used here is that MLR-ordered probability laws have ordered expectations of increasing integrable functions, with the order reversed for decreasing integrable functions. Its relevant conclusion can also be proved directly in this case. Put a(u)=u^(-1). By the finiteness established above and Fubini's theorem,

E_-[a(u)|q]-E_+[a(u)|q]

= integral_{0<u<v<infinity} (a(u)-a(v)) [pi_-(u|q)pi_+(v|q)-pi_+(u|q)pi_-(v|q)]du dv.

This follows by expanding the difference of expectations as a double integral and combining the regions u<v and v<u. Both displayed factors are nonnegative. The expectation difference is therefore nonnegative, so h'(q)>=0. This proves that h is nondecreasing on (0,infinity), and also on its extension to zero whenever a finite endpoint exists.

### 4. Endpoint integration

For 0<epsilon<q, the fundamental theorem of calculus gives

h(q)-h(epsilon)=(1/2) integral_epsilon^q (E_-[u^(-1)|t]-E_+[u^(-1)|t])dt.

If h(epsilon) has a finite limit h(0) as epsilon decreases to zero, the right side has a finite limit as well. This is precisely the prescribed improper integral, and proves the claimed identity with the additive constant h(0). No posterior precision at zero is required. If both F_c(0) are finite, monotone convergence gives F_c(epsilon)->F_c(0)>0, so the endpoint agrees with log F_+(0)-log F_-(0).

### 5. Inverse-gamma specialization

Let a=nu/2 and let v have density a^a v^(-a-1)exp(-a/v)/Gamma(a). In a class with scale s, the effective mixer is u=s^2v. Its density is p_s(u)=s^(-2)p_v(u/s^2). This is the p_c appearing in the general definition of F_c, rather than the common density of v itself.

Changing variables in that definition gives

F_s(q)=s^(-d) integral_0^infinity v^(-d/2)exp(-q/(2s^2v))p_v(v)dv.

The standard Gamma integral is integral_0^infinity t^(b-1)exp(-B t)dt=Gamma(b)B^(-b) for b>0 and B>0. After t=1/v, its hypotheses hold with b=a+d/2>0 and B=a+q/(2s^2)>0, including at q=0. It follows that

F_s(q)=s^(-d) [a^a Gamma(a+d/2)/Gamma(a)] [a+q/(2s^2)]^(-(a+d/2))

=C s^(-d)(1+q/(nu s^2))^(-(nu+d)/2),

where C=Gamma((nu+d)/2)/[Gamma(nu/2)(nu/2)^(d/2)] is independent of s and q. Taking the log ratio for s_+=r and s_-=1 gives

h(q)=-d log r+((nu+d)/2)[log(1+q/nu)-log(1+q/(nu r^2))].

For completeness, the effective mixer ratio is p_+(u)/p_-(u)=r^nu exp(-nu(r^2-1)/(2u)), which is increasing in u. Thus the specialization is also compatible with the general MLR hypothesis; the direct strict-increase argument below does not need to appeal to it.

### 6. Evidence bounds and energy support

The formula gives h(0)=-d log r and

h'(q)=((nu+d)/2)[1/(nu+q)-1/(nu r^2+q)]>0

for q>=0, since nu>0 and r>1. The logarithmic difference tends to log(r^2) as q tends to infinity. Therefore

lim_{q->infinity}h(q)=-d log r+(nu+d)log r=nu log r.

Thus every finite q>=0 gives -d log r<=h(q)<nu log r, which implies the requested closed-interval bounds. The upper endpoint is a limit, not an attained value at finite q.

For each fixed positive mixer value, the nonsingular Gaussian has positive probability outside every Mahalanobis ball. Integrating this strictly positive conditional probability over the mixer proves P_c(q>M)>0 for every finite M>=0 under either class. Consequently, for K>=1 the nonnegative energy sum is unbounded in support as well, since it is at least q_1. No finite variance or finite mean energy is needed.

### 7. One-location ROC

Suppose h is strictly increasing. It is continuous on (0,infinity) by Step 2. For each positive energy threshold t, the events {q>t} and {h(q)>h(t)} agree. Conversely, a threshold lying inside the image of h corresponds to a unique energy threshold; thresholds outside that image give constant decisions, up to null events. Boundary randomizations are preserved by the same correspondence. Hence the two families of threshold tests have the same pairs of false-positive and true-positive probabilities, including the constant endpoints. This proves equality of the threshold ROCs.

### 8. Independent aggregation and optimality

Conditional on a class, the observations are independent draws from its specified distribution. Their joint density is therefore the product of the one-location densities. The joint likelihood ratio and log-likelihood ratio are

L(z_1,...,z_K)=product_{k=1}^K exp(h(q_k)),

log L(z_1,...,z_K)=sum_{k=1}^K h(q_k).

The Neyman-Pearson lemma for two specified probability laws with densities states that, for each size alpha, rejecting when their likelihood ratio exceeds a suitable threshold, with boundary randomization if needed, is most powerful among all measurable randomized tests of size at most alpha. Here the product densities supply the required dominated experiment, and L is finite and positive almost surely under either class. The lemma therefore applies to the displayed sum. Sizes zero and one are supplied by the constant tests.

In the specialization, summing the per-location bounds gives

-Kd log r<=sum_{k=1}^K h(q_k)<=K nu log r,

while Step 6 proves that sum_{k=1}^K q_k has unbounded support. All requested conclusions follow, and no theorem-critical obligation remains unresolved.
