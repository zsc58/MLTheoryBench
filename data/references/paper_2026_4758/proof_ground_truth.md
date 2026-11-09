# Reference Proof

## Proof Structure

1. Construct the exact reverse masking path and derive its time, index, and token kernels.
2. Prove that every FHS event strictly decreases the number of masks, and identify the common time/index law.
3. Derive the event-time density and the distribution of the true visible context at each stage.
4. Compute path KL, identify it with integrated score entropy, and pass to the output.
5. Construct an equality example for every allowed alphabet, dimension, and error level.

## Complete Proof

Write α_t=e^{-t} and λ_t=α_t/(1-α_t) for t>0. For a masked state y, let M be its mask set, k=|M|, and c=y^{M^c}. Independence of the forward masking mechanisms from the clean data gives

q_t(y)=(1-α_t)^k α_t^{d-k} q_0(X^{M^c}=c).

If q_t(y)>0, i∈M, and a∈V, replacing the ith mask by a therefore gives

r_t(y,i,a)=q_t(y^{i←a})/q_t(y)=λ_t q_i(a|c).

This derivation uses no independence assumption on the coordinates of q_0.

### 1. Exact reverse path and its kernels

Draw X∼q_0 and independent random variables T_1,...,T_d with density e^{-t} on t>0, independently of X. Coordinate i retains X_i until forward time T_i and is masked thereafter. This realizes the specified forward process. Read this path in decreasing forward-time order: it starts all-masked above max_i T_i, reveals coordinate i at T_i, and ends at X below min_i T_i. The clocks are finite, positive, and distinct almost surely. This constructs the reverse path from infinity without a finite-horizon initialization approximation. Denote its law by Q.

The finite-state time-reversal identity says that, at a positive-time state y with q_t(y)>0, the reverse rate to z≠y is R_t(z,y)q_t(z)/q_t(y). Here the only possible reverse moves replace a mask by a visible token, and R_t(y^{i←a},y)=1. Thus the reverse rate to y^{i←a} is λ_t q_i(a|c). These rates are finite and continuous on compact subintervals of (0,infinity) on every accessible state, so the usual local hazard calculation applies there.

Summing over a∈V shows that each masked coordinate has exit rate λ_t. The total exit rate with k masks is kλ_t. Conditional on remaining in the current state, the probability of no jump while the clock decreases from t to s is

exp(-∫_s^t kλ_u du)=((1-e^{-s})/(1-e^{-t}))^k.

For completeness, this hazard formula follows from S(h+δ)=S(h)(1-kλ_{t-h}δ+o(δ)), hence S'(h)=-kλ_{t-h}S(h), S(0)=1. The denominator tends to 1 at t=infinity, agreeing with the explicit clock construction.

Dividing the rate λ_t of a specified masked coordinate by kλ_t gives uniform index selection. Dividing its token-specific rate by λ_t gives token law q_i(·|c). FHS uses the same conditional time and index kernels and replaces only this token law by μ_i(·|c,s), evaluated at the new event time s. Write P for its path law.

For every k≥1 and t∈(0,infinity], the displayed time CDF tends to 0 as s decreases to 0 and to 1 as s increases to t. It is continuous, so the next event lies strictly in (0,t) almost surely and is finite even at the first step. The sampled token belongs to V, not to the mask state. Consequently each event removes exactly one mask, no revealed coordinate is selected again, and FHS completes exactly d events almost surely.

### 2. Stage distributions under the exact path

Let S_k be the time of the event occurring when k coordinates remain masked, and let M_k be the mask set just before that event. Under Q, S_k is the kth smallest among T_1,...,T_d. The independence and identical continuous distributions of the clocks imply that their rank permutation is uniform and independent of their ordered values: for every strict ordering the product density is the same. The entire clock collection is also independent of X. It follows that M_k is a uniform k-subset, independent of X and S_k. Given M_k, the next index is uniform in M_k. The visible context is X^{M_k^c}.

The density of S_k is obtained by choosing the clock in an infinitesimal interval at s, the k-1 clocks below s, and the d-k clocks above s:

f_k(s)=d! / ((k-1)!(d-k)!) · (1-e^{-s})^{k-1} e^{-(d-k)s} e^{-s}
       =k binom(d,k) α_s^{d-k+1}(1-α_s)^{k-1},  s>0.

Equivalently, e^{-S_k} has Beta(d-k+1,k) distribution. This density calculation proves the needed order-statistic result directly; no specialized external result is assumed.

The independence of visible values and ordered times asserted here is under Q. It is not asserted for P: a time-dependent learned predictor can make generated token values depend on event times.

### 3. Path relative entropy

For i∈M define

D_i(c,s)=KL(q_i(·|c) || μ_i(·|c,s)).

The path is a finite sequence of event times, indices, and token values. Its probability kernels factor in that order. Q and P have common time and index factors; their token factors are respectively q_i and μ_i. The relative-entropy chain rule therefore gives

KL(Q||P)=Σ_{k=1}^d E_Q[D_{I_k}(X^{M_k^c},S_k)]
        =Σ_{k=1}^d (1/k) ∫_0^infinity f_k(s) E_{X,M_k}[Σ_{i∈M_k}D_i(X^{M_k^c},s)] ds.  (1)

Here X∼q_0 and M_k is an independent uniform k-subset. The factor 1/k is from uniform index selection; event-time averaging remains inside the integral.

This calculation is valid with extended-valued KL. One may obtain it directly by taking the logarithm of the finite product of token likelihood ratios and then conditioning successively on the histories. The negative parts have finite expectation: the true token log-probability has conditional entropy at most log|V|, while minus the learned token log-probability is nonnegative. A zero learned probability on a positive-mass true event gives infinite KL rather than an undefined cancellation. The finite-energy assumption, together with the identity below, ensures finite path KL and Q≪P.

### 4. Identification with score entropy

At a supported state y with mask set M, the earlier ratio calculation gives r_t(y,i,a)=λ_t q_i(a|y^{M^c}), whereas the task defines z_t(y,i,a)=λ_t μ_i(a|y^{M^c},t). By the boundary conventions for Φ and normalization of both token distributions,

Σ_{a∈V} Φ(r_t(y,i,a),z_t(y,i,a))
 =λ_t Σ_{a∈V}[μ_i(a|y^{M^c},t)-q_i(a|y^{M^c})
              +q_i(a|y^{M^c})log(q_i(a|y^{M^c})/μ_i(a|y^{M^c},t))]
 =λ_t D_i(y^{M^c},t).

The identity remains valid when a divergence is infinite. All resulting loss terms are nonnegative.

At deterministic time t, the mask count in the forward process has mass binom(d,k)(1-α_t)^k α_t^{d-k}; conditional on that count, the mask set is uniform and independent of X. Hence, using nonnegative integration,

E(μ)=Σ_{k=1}^d ∫_0^infinity binom(d,k) α_t^{d-k+1}(1-α_t)^{k-1}
             · E_{X,M_k}[Σ_{i∈M_k}D_i(X^{M_k^c},t)] dt.

The coefficient is f_k(t)/k, so comparison with (1) proves

KL(Q||P)=E(μ)≤ε.

For reference, the source's NELBO bridge can also be closed without an external citation. Define the full-time expected cross entropy

C(μ)=∫_0^infinity λ_t E_{X,Y_t}[Σ_{i:Y_t^i=m} -log μ_i(X_i|Y_t^{M(Y_t)^c},t)] dt.

The same calculation gives E(μ)=C(μ)-H_*, where

H_*=Σ_{k=1}^d (1/k) E_{X,M_k}[Σ_{i∈M_k}H(q_i(·|X^{M_k^c}))].

Indeed, binom(d,k)∫_0^1 a^{d-k}(1-a)^{k-1}da=1/k. This entropy correction is at most d log|V|, so no infinity-minus-infinity ambiguity is introduced. Zero loss means equality of the token kernels only almost everywhere in time and on supported contexts. This paragraph audits the attached NELBO support; it is not an additional public target.

Finally, relative entropy decreases under a measurable map: if F maps a path to its terminal state, then KL(F_#Q||F_#P)≤KL(Q||P). In this application the path space is a finite product of positive-time Borel spaces and finite token/index spaces, F is measurable, F_#Q=q_0 by the clock construction, and F_#P=P_FHS by definition. Thus

KL(q_0||P_FHS)≤E(μ)≤ε.

### 5. Equality construction

Fix the alphabet and dimension from the task, choose distinct a,b∈V, and let q_0=δ_{a^d}. For every masked coordinate, context, and t>0, define

μ_i(a|context,t)=e^{-ε/d},
μ_i(b|context,t)=1-e^{-ε/d},

with zero mass on other symbols. These are measurable normalized predictors. On every context seen under q_0, the true conditional is δ_a, and its token KL is ε/d. Since the expected number of masks at time t is d(1-e^{-t}), the identity derived in Section 4 gives

E(μ)=∫_0^infinity [e^{-t}/(1-e^{-t})]d(1-e^{-t})(ε/d)dt=ε.

At each of the d events, the conditional probability of assigning the correct token is e^{-ε/d}, regardless of time and history. Thus

P_FHS(a^d)=(e^{-ε/d})^d=e^{-ε},
KL(q_0||P_FHS)=-log P_FHS(a^d)=ε.

The construction also applies at ε=0 and d=1. Null contexts do not affect the loss or the true-path calculation, and the predictor has been specified on them so that FHS is defined everywhere.

## Closure and Source Repairs

All theorem-critical obligations are explicitly closed above. The only external probability facts used as general results are the finite-state reverse-generator identity and KL data processing, whose relevant statements and hypotheses are given in the proof. The event-time density, loss identity, and specialized NELBO bridge are derived rather than imported.

The private source record corrects the NELBO time horizon to infinity, qualifies the zero-loss characterization almost everywhere, and corrects the CTMC survival integration limits and short-interval conditional probability. These local corrections preserve the FHS theorem. No Euler boundary, Euler grid, or Euler discretization lemma is required.
