# Reference Proof

## Status and obligations

This proof establishes the repaired public statement. The theorem-critical obligations are: (1) drift under the actual link assumptions; (2) conditional increment tails; (3) scale-sensitive maximal concentration; (4) normalization control; (5) warm-start improvement; (6) regret and schedule conversion; (7) derivative-lower-bound burn-in; and (8) convex burn-in, including its integral comparison. Each is derived below. The specialized external self-normalized-concentration citation is not used as an unproved premise.

All constants may depend on the fixed link constants. We write c for a sufficiently small positive constant and C for a sufficiently large one, choosing C before c. Confidence parameters can first be replaced by min(delta,1/4). Integer durations are rounded up. These changes preserve the stated bounds and probabilities.

## 1. Drift, including nonsmooth monotone links

Condition on the pre-round history. Put q=<u,w>, r=rho, a=sqrt(1-r^2), and B=r sqrt(1-q^2). For |q|<1, write <u,Z>=sqrt(1-q^2)X, where X is a coordinate of a uniform point on S^{d-2}. Thus E[X]=0 and E[X^2]=1/(d-1). The update and conditional mean-zero noise give the exact identity

D:=E[q_{t+1/2}-q_t|F_t]=alpha r h'(a)sqrt(1-q^2) E[X h(aq+BX)].

If g(x)=h(aq+Bx) is absolutely continuous, integration by parts against the density c_d(1-x^2)^((d-4)/2), with c_d=1/Beta(1/2,(d-2)/2), yields

E[Xg(X)]=(d-2)^(-1)E[(1-X^2)g'(X)].

Consequently the derivative form of the drift contains h'(aq+BX), not h(aq+BX). For an arbitrary bounded monotone g, integration by parts instead gives c_d/(d-2) times the integral of (1-x^2)^((d-2)/2) against dg. A singular part cannot simply be omitted from an equality.

The needed lower bounds require neither global absolute continuity nor this generalized identity. Symmetry gives

E[X h(aq+BX)]=E[X(h(aq+BX)-h(aq-BX))1{X>=0}].

Suppose aq>=0 and h has lower slope b on [aq,aq+B]. Monotonicity on the whole domain gives, for x>=0,

h(aq+Bx)-h(aq-Bx)>=h(aq+Bx)-h(aq)>=bBx.

It follows that

D>=alpha r^2 h'(a)(1-q^2)b/[2(d-1)].

Use b=c_0 under condition (A); use b=h'_-(aq) under convexity; and use b=gamma_1 when aq>=1-gamma_0. The convex left derivative is finite at every interior positive argument and is a supporting slope. The lower bound under (A) follows from the mean value theorem on the positive interval. The same symmetry identity always gives D>=0. At q=+/-1, the tangential projection of u is zero and the half-step correlation increment is zero, so these claims hold directly without division by zero.

## 2. Conditional tails

A spherical coordinate in dimension d-1 has Psi_2 norm at most C/sqrt(d-1)<=C'/sqrt(d). To verify this, represent G~N(0,I/(d-1)) as R U with independent radius and uniform direction, and E[R^2]=1. Conditional Jensen applied to exp(R^2<U,v>^2/s^2) bounds the spherical exponential moment by its Gaussian counterpart.

The link residual has absolute value at most two. Its product with <u,Z> therefore has Psi_2, and hence Psi_1, norm at most C sqrt((1-q^2)/d). The independent noise term is a product of subGaussian variables. The standard product bound follows also from 2|xy|<=x^2+y^2 and Cauchy-Schwarz applied to the exponential moments. Centering costs at most a universal factor. Thus, for

A_t=q_{t+1/2}-E[q_{t+1/2}|F_t],

we have the conditional bound

||A_t||_{Psi_1|F_t}<=K_t=C alpha_t rho_t h'(sqrt(1-rho_t^2))sqrt((1-q_t^2)/d).

All conditional hypotheses hold because the schedules are selected before the fresh direction and the reward noise is conditionally independent of that direction.

## 3. Scale-sensitive maximal concentration

Here is the precise concentration fact needed below, together with its derivation. Suppose centered adapted increments U_s have conditional Psi_1 norm at most k_s. Their conditional moments obey E[|U_s|^j|F_s]<=2j!k_s^j. Expanding the exponential and using conditional centering shows

log E[exp(lambda U_s)|F_s]<=C lambda^2 k_s^2

whenever |lambda|k_s<=c. The same statement holds for predictable weighted increments, with scales |w_s|k_s.

If these scales are at most a deterministic b and their squared sum up to a horizon is at most a deterministic v, then exp(lambda sum U_s-C lambda^2 sum k_s^2) is a nonnegative supermartingale initially equal to one for |lambda|<=c/b. Stop if an asserted scale or variance envelope would fail. Stopping this supermartingale at its first crossing of a level proves that its crossing probability is at most the reciprocal of that level: this follows first for bounded stopping times by iterated conditional expectation, and then by monotone convergence of the crossing events. Optimizing lambda and applying the argument to both signs gives

P(max_{n<=N}|sum_{s<n}U_s|>C[sqrt(v log(2/p))+b log(2/p)])<=p.

In particular, with k_s<=b, one may take v=Nb^2. Every subinterval sum is bounded by twice the maximum absolute prefix sum. Stopped increments permit use of a scale envelope that is valid only inside an induction region; no conditioning on a future good event is used.

For completeness, the self-normalized, time-uniform version follows by dividing the variance range into bins with upper endpoints 2^{j+1}v_0 and allocating probabilities proportional to p/(j+1)^2. Apply the preceding exponential crossing argument at each bin's upper endpoint and sum the probabilities. This produces a boundary of order sqrt((V vee v_0)[log(C/p)+2log(1+log(V/v_0 vee 1))]) plus b times the same logarithm. Equivalently, for psi(lambda)=lambda^2/(1-lambda/lambda_max), the linear term is lambda_max^-1 times that logarithm. Any dominating supermartingale must have initial expected mass at most one. Discounted sums are stopped before their weights exceed the asserted bound. This proves the needed concentration closure directly.

Crucially, the epoch calculations use the actual b and v. A bound containing sqrt(V vee 1) cannot be used without rescaling to claim a fluctuation much smaller than one.

## 4. Normalization

Write v_t=w_{t+1/2}-w_t. Orthogonality gives ||w_{t+1/2}||^2=1+||v_t||^2. Conditional subGaussian tails and boundedness of h imply, with failure probability at most p,

||v_t||^2<=C alpha_t^2 rho_t^2 h'(sqrt(1-rho_t^2))^2 log(2/p).

Since |q_{t+1/2}|/||w_{t+1/2}||<=1,

|q_{t+1}-q_{t+1/2}|<=sqrt(1+||v_t||^2)-1<=||v_t||^2/2.

If q_{t+1/2}>=0, normalization decreases it and

q_{t+1}>=q_{t+1/2}(1-||v_t||^2/2).

When q_t is of order l and the single-step change is a sufficiently small multiple of l, this sharper formula bounds normalization loss by C l alpha_t^2 log(2/p), for constant exploration and bounded outer derivative. Allocate a fixed small multiple of delta to each step's tail event. On an N-step epoch their union has probability at most a fixed multiple of N delta; this avoids inserting log N into every learning rate.

## 5. Warm-start epochs and pure exploration

Let e<=gamma_0/4 and q at the start of an epoch be at least 1-e. Let L=log(Cd/(e delta)), alpha=c e/(dL^2), and let s=rho^2 be either gamma_0 or e. Take N=ceil(Cd/(alpha s)). For s=gamma_0 this is order d/alpha; for s=e it is order d/(alpha e).

Stop the increment process before q falls below 1-2e. Within that region K_t<=C alpha sqrt(se/d). The maximal inequality gives a prefix fluctuation bounded by

C[alpha sqrt(Nse L/d)+alpha sqrt(se/d)L].

The normalization loss over the epoch is at most C N alpha^2 s L. Substituting N and alpha shows that, after choosing c small, every subinterval's combined fluctuation and normalization loss is at most e/4, and can be made smaller by any fixed constant factor. Since drift is nonnegative, an initial lower exit is impossible on this event. In particular q remains at least 1-5e/4.

Before q crosses 1-e/4, we have 1-q^2>=c'e. Moreover sqrt(1-s)q>=1-gamma_0: for s=gamma_0 use q>=1-2e>=1-gamma_0/2 and 1-gamma_0/2>=sqrt(1-gamma_0); for s=e use sqrt(1-e)(1-2e)>=1-3e. Section 1 therefore gives drift at least c' alpha s e/d. If no crossing occurred, summing this drift for N steps would improve correlation by an arbitrarily large fixed multiple of e when C is large, a contradiction. After the crossing, the same subinterval loss bound preserves q>=1-e/2 through the epoch end.

The maximal event and all normalization events can be budgeted to give failure probability at most N delta. Restarting at a deterministic epoch boundary is legitimate conditionally on its pre-round history.

For pure exploration use s=gamma_0 and e_j=(gamma_0/4)2^-j. The epoch lengths are O(d^2 L_j^2/e_j). Their geometric sum through the first target e_j<=epsilon is O-tilde(d^2/epsilon). The epochwise alpha_j=c e_j/(dL_j^2), expressed in cumulative time, is Theta-tilde(min(d/t,1/d)). The exploration is constant. Summing failure budgets gives at most delta times the final iterate index. If the requested accuracy is already met initially, no update is needed.

## 6. Regret and its schedule

Use the same epochs with s=e. Their lengths are O(d^2 L_j^2/e_j^2). Throughout an epoch q>=1-5e/4, so local derivative bounds give h(1)-h(q)<=C e. Thus the iterate-based regret of a complete epoch is O-tilde(d^2/e).

The stronger action geometry used in the source is also valid: <u,a_t>>=sqrt(1-e)q_t-sqrt(e)sqrt(1-q_t^2)>=1-4e. It is not necessary to replace the public iterate-based regret by action regret.

The epoch-time relation is e=Theta-tilde(min(d/sqrt(t),1)), giving alpha=Theta-tilde(min(1/sqrt(t),1/d)) and rho^2=Theta-tilde(min(d/sqrt(t),1)). Complete-epoch regret sums geometrically. If a horizon truncates an epoch, its additional regret is at most C e times the elapsed part. The current epoch's scale and the time spent in earlier epochs give O-tilde(d sqrt(T)); during the first epoch use min(T,C eT) and its length O-tilde(d^2). The failure probability through any fixed horizon T is at most delta T. This proves the stated regret quantity and quantifier order.

## 7. Burn-in under a positive derivative lower bound

Let L=log(Cd/delta), rho^2=gamma_0, alpha=c/(dL^2), and N=ceil(Cd/alpha). Stop before q becomes nonpositive or reaches H=1-gamma_0/8. Before reaching H, Section 1 gives drift at least a alpha/d, where a>0 depends only on the link constants. The per-step normalization bound is C alpha^2 L, at most half this drift for small c.

The full-epoch maximal noise bound, using K_t<=C alpha/sqrt(d), is

C[alpha sqrt(NL/d)+alpha L/sqrt(d)]<=C' sqrt(c)/(sqrt(d)),

and can be made at most 1/(4sqrt(d)). Hence q_n>=q_1-1/(4sqrt(d))+a alpha n/(2d) before the upper crossing. This excludes a lower exit and, for large C, forces the upper crossing by time N.

After that crossing, use nonnegative drift, the subinterval martingale bound, and total normalization loss C N alpha^2 L=C d alpha L. Both losses can be made smaller than gamma_0/16. The final correlation is therefore at least 1-gamma_0/4. The duration is O-tilde(d^2), with alpha=Theta-tilde(1/d), not Theta-tilde(1/d^2). The latter exponent is the source's locally corrected statement typo.

## 8. Convex burn-in

Let a=(1-gamma_0)^2, b_0=1-gamma_0/4, l_k=a sqrt(k/d), and b_k=b_0 sqrt(k/d). Write s_k=l_{k+1}-l_k. Uniformly for 1<=k<=d-1,

s_k is comparable to 1/(d l_k), and s_k/l_k<=sqrt(2)-1.

Let g_k=h'_-(l_k). Convexity and the local derivative upper bound imply 0<=g_k<=gamma_2. If the displayed integral is finite, g_k>0: otherwise the nondecreasing convex derivative would vanish on a positive-length interval between 1/(2sqrt(d)) and l_k, making the integral infinite.

Set L=log(Cd/delta), rho^2=gamma_0,

alpha_k=c g_k/(d l_k L^2),
N_k=ceil(C d s_k/(alpha_k g_k)).

These are deterministic known-link schedules. Rounding changes the following estimates by at most fixed factors, since the unrounded duration is bounded below by a sufficiently large constant.

The full-epoch martingale bound with K_t<=C alpha_k/sqrt(d) gives, simultaneously for all subintervals, an error at most

C_1[alpha_k sqrt(N_k L/d)+alpha_k L/sqrt(d)]<=C_2(sqrt(cC)+c)s_k.

Here one substitutes alpha_k and N_k and uses s_k comparable to 1/(d l_k). This is a spacing-scale estimate, not the incorrect uniform O(cC/d) estimate in the source.

On the normalization good event each one-step change in q is at most C alpha_k sqrt(L)+C alpha_k^2 L. Since alpha_k/l_k<=C c gamma_2/(kL^2), this is as small a fixed multiple of l_k as needed. On a segment with positive q=O(l_k), the half-step is also positive and O(l_k), and Section 4 bounds its total normalization loss over at most N_k steps by

C_3 l_k alpha_k^2 N_k L<=C_4 cC s_k/L.

Choose a fixed small zeta>0 depending only on gamma_0. It can be chosen so that sqrt(1-gamma_0)(b_k-zeta s_k)>=l_k for every k. Choose c sufficiently small that the preceding combined interval losses are less than zeta s_k/4.

Assume q at the epoch start is at least b_k, and put H_k=(1-gamma_0/8)sqrt((k+1)/d). First consider the path before it reaches H_k. If it starts below H_k, stop at a first exit below b_k-zeta s_k or at the upper crossing. In this band q=O(l_k), q remains positive, and sqrt(1-gamma_0)q>=l_k. Also 1-q^2 is bounded below by a positive link-dependent constant because q<H_k<=1-gamma_0/8. The convex drift lower bound is therefore at least a_1 alpha_k g_k/d. Summing drift, noise, and localized normalization excludes the lower exit and gives

q_n>=b_k+a_1 alpha_k g_k n/d-zeta s_k/2

until the upper crossing. If no upper crossing occurs by N_k, large C makes the endpoint at least b_{k+1}, because b_{k+1}-b_k=(b_0/a)s_k.

It remains to handle paths starting above H_k or reaching it during the epoch. The gap H_k-b_{k+1} is gamma_0 sqrt((k+1)/d)/8, a fixed multiple of l_k. Suppose a later iterate falls below b_{k+1}. Consider the last downward crossing of H_k before that fall. The one-step bound leaves the first iterate below H_k still above b_{k+1} by at least half this gap. Until the alleged fall, correlations on this segment lie between b_{k+1} and H_k, hence are positive and O(l_k). Drift is nonnegative, while the subinterval martingale bound and localized normalization loss total less than zeta s_k. Choose zeta small enough that this is less than half the gap, a contradiction. Thus the epoch endpoint is at least b_{k+1} in this case also. This argument also covers an initial correlation much larger than the epoch threshold; no upper-bound assumption on the initial correlation is introduced.

Allocate a small multiple of delta to the maximal event and to each individual normalization event. The epoch failure probability is at most N_k delta, without requiring logarithms of 1/g_k. Iteration for k=1,...,d-1 is valid since q_1>=1/sqrt(d)>=b_1 and ends at b_d=1-gamma_0/4.

Finally, the total duration is bounded by a constant times

d^2 L^2 sum_{k=1}^{d-1} l_k s_k/g_k^2.

For k>=2, monotonicity of the convex derivative gives

integral_{l_{k-1}}^{l_k} x/h'(x)^2 dx >=(l_k^2-l_{k-1}^2)/(2g_k^2)>=l_k s_k/g_k^2.

For k=1, use the interval [1/(2sqrt(d)),l_1]. Its squared-endpoint difference is a fixed positive multiple of 1/d because a>=0.81, so its integral dominates the first summand up to a universal factor. These intervals are disjoint and contained in the interval appearing in the public claim. This proves the stated integral complexity and, by summing epoch failure budgets, the probability at least 1-delta T. If the integral is infinite, the extended-real complexity expression supplies no finite-time conclusion; no division by a zero slope is performed.

All eight obligations are thereby closed.
