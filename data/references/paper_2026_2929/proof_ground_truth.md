# Reference Proof

## Proof Structure

Establish the conditional weighted swap inequality directly for the implemented weights. Apply the TV-profile assumption. On the mean-concentration event, compare empirical and latent squared distances, derive a Jacobian bound for the peer-coordinate normalized exponential map, include the sentinel coordinate, and substitute the resulting weight error into the empirical-to-oracle decomposition.

## Complete Proof

Fix `t>=2` and `delta in (0,1)`. Put `n=N+1`, `F=F_{t-1}^+`, `a=bar alpha_t`, and `w_i=hat omega_i^(t)`. The running means, and hence the weights, are `F_{t-1}`-measurable. The level is `F`-measurable. Moreover, all weights are positive, their sum is one, and `w_i<=w_n` for every peer `i`: each unnormalized peer weight is at most the unnormalized target weight one. These properties follow from the implemented weight formula.

### 1. Conditional weighted swap bound

We first work with fixed weights, fixed `a`, and a deterministic finite score vector `z in R^n`. Let `f(z)` be the indicator that `z_n` exceeds the weighted threshold formed from `(z_1,...,z_{n-1},+infinity)` with weights `w`. Let `T_i` swap coordinates `i` and `n`, with `T_n` the identity.

Suppose `0<a<1`. By the finite-score quantile definition,

`f(z)=1{sum_{j<n} w_j 1{z_j<z_n} >= 1-a}`.

Indeed, the threshold is strictly below the target score exactly when enough cumulative weight is attained at scores strictly below it. This equivalence also handles ties and equality with the required cumulative weight.

For a peer `i`, the calibration mass strictly below the target score `z_i` after the swap is

`sum_{j!=i,n} w_j 1{z_j<z_i} + w_i 1{z_n<z_i}`.

Since `w_i<=w_n`, this is at most

`r_i(z)=sum_{j=1}^n w_j 1{z_j<z_i}`.

For `i=n`, the same domination holds with equality. Consequently,

`f(T_i z)<=1{r_i(z)>=1-a}`

for every `i`.

Let `B={i:r_i(z)>=1-a}`. If `B` is empty its total weight is zero. Otherwise choose an index in `B` having the smallest score, denoted `c`. The total weight strictly below `c` is at least `1-a`, and every member of `B` has score at least `c`. Thus `sum_{i in B}w_i<=a`. We have proved the pointwise inequality

`sum_{i=1}^n w_i f(T_i z)<=a`.

This argument uses strict lower-score masses and therefore requires no absence-of-ties assumption.

Now condition on `F`. On a full-probability set, the weights and level are fixed and the regular conditional law of the actual score vector is `P_t`. The swap law is the pushforward `P_{t,i}^{swap}` under `T_i`. Because `f` is a measurable indicator, the definition of total variation gives, for each peer `i`,

`E_{P_t}f <= E_{P_{t,i}^{swap}}f + d_TV(P_t,P_{t,i}^{swap}) = E_{P_t}[f(T_i Z)] + d_TV(P_t,P_{t,i}^{swap})`.

For `i=n`, use the identity with discrepancy zero. Multiplying these inequalities by `w_i`, summing, and using the pointwise inequality gives

`P(Y_{n,t} notin C_t(X_{n,t}) | F) <= a + sum_{i=1}^N w_i d_TV(P_t,P_{t,i}^{swap})`.

If `a=0`, positive sentinel mass makes the threshold `+infinity`, so the prediction set is `R` and miscoverage is zero. If `a=1`, the threshold is `-infinity` and miscoverage is at most one. Thus the displayed bound holds at both endpoints as well. This closes the specialized conformal obligation without relying on an unproved external theorem.

### 2. Profile discrepancy

Write `phi_k=phi(||mu_k-mu_n||_2)`. The TV-profile assumption and nonnegative weights imply, almost surely,

`P(Y_{n,t} notin C_t(X_{n,t}) | F) <= a + sum_{k=1}^N hat omega_k^(t) phi_k`.

### 3. Squared-distance approximation

Let

`E={max_{1<=j<=n}||hat mu_{j,t-1}-mu_j||_2<=epsilon_{t,delta}}`.

Its probability is at least `1-delta`. Write `epsilon=epsilon_{t,delta}`. On `E`, define vectors

`u_k=mu_k-mu_n`,

`e_k=(hat mu_{k,t-1}-mu_k)-(hat mu_{n,t-1}-mu_n)`.

Then `||u_k||_2<=D_mu`, `||e_k||_2<=2epsilon`, and the empirical difference vector is `u_k+e_k`. Define scalar squared distances

`A_k=||u_k+e_k||_2^2`, `B_k=||u_k||_2^2`.

The expansion and Cauchy-Schwarz inequality give

`|A_k-B_k|=|2<u_k,e_k>+||e_k||_2^2| <= 4D_mu epsilon+4epsilon^2`.

This holds uniformly over peers.

### 4. Normalized-exponential perturbation

Define the peer-coordinate map `G:R^N->R^N` by

`G(v)_k=exp(-v_k/(2h^2))/(1+sum_{j=1}^N exp(-v_j/(2h^2)))`.

Direct differentiation yields

`partial G(v)_k/partial v_l = -(1/(2h^2))G(v)_k 1{k=l} +(1/(2h^2))G(v)_k G(v)_l`.

Since the coordinates are nonnegative and sum to at most one, each Jacobian column satisfies

`sum_k |partial G(v)_k/partial v_l| <= (1/(2h^2))(G(v)_l+G(v)_l sum_k G(v)_k) <= 1/h^2`.

Hence its induced `l1` operator norm is at most `1/h^2`. Integrating the derivative along the line segment from `B` to `A` gives

`||G(A)-G(B)||_1 <= h^(-2)||A-B||_1 <= (N/h^2) max_k|A_k-B_k|`.

Define the full weight vectors by adjoining the coordinate `1-sum_k G(v)_k`. Its difference is at most the peer-coordinate `l1` difference. Therefore

`||hat omega_full-omega_full^circ||_1 <= (2N/h^2)max_k|A_k-B_k|`.

On `E`, substitution yields

`||hat omega_full-omega_full^circ||_1 <= (8N/h^2)(D_mu epsilon+epsilon^2)`.

Here `omega_full^circ` consists of the public oracle peer weights and their remaining target-coordinate mass.

### 5. Oracle decomposition and conclusion

Because `0<=phi_k<=phi_max`,

`sum_k hat omega_k^(t) phi_k = sum_k omega_k^circ phi_k + sum_k (hat omega_k^(t)-omega_k^circ)phi_k`

`<= sum_k omega_k^circ phi_k + phi_max sum_k |hat omega_k^(t)-omega_k^circ|`

`<= sum_k omega_k^circ phi_k + phi_max ||hat omega_full-omega_full^circ||_1`.

Combining the preceding bounds gives, almost surely on `E`,

`P(Y_{N+1,t} notin C_t(X_{N+1,t}) | F_{t-1}^+) <= bar alpha_t + sum_{k=1}^N omega_k^circ phi(||mu_k-mu_{N+1}||_2) + (8N phi_max/h^2)(D_mu epsilon_{t,delta}+epsilon_{t,delta}^2)`.

Intersecting `E` with the full-probability sets for the conditional bound and TV assumptions does not reduce its probability. The resulting event has probability at least `1-delta`, as required. No union over rounds or confidence levels is asserted. The argument also covers `epsilon=0`, `D_mu=0`, `phi_max=0`, and all clipped-level endpoints without division by any of these quantities.
