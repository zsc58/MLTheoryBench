# Reference Proof

## Contract and proof obligations

The original filtration is the usual natural filtration of the driving Brownian motion. The observation is sampled from the Poisson kernel conditional on the full Brownian path, with rate given by its strong diffusion solution. It is not already included in the original filtration. The intensity is strictly positive throughout the full finite horizon. The parameter-differentiability assumptions used elsewhere for optimization are not needed for this fixed-coefficient result.

The obligations are: establish the conditional observation-density factorization; identify its Brownian covariation with the observation index held fixed; close the calculation at event times and after the observation horizon; apply the initial-enlargement decomposition with its hypotheses verified; identify the resulting Brownian motion and obtain the posterior SDE and conditional-law interpretation.

## Standard results used

1. For jointly measurable coefficients satisfying uniform state-Lipschitz and linear-growth bounds, an SDE with deterministic initial state has a unique strong solution. On a finite horizon its supremum has every finite polynomial moment. The moment estimate follows by applying the stochastic-integral maximal inequality and Gronwall's inequality to the SDE, first stopped and then passing to the limit. The same estimates, with initial value v, are bounded by a constant times 1+|v|^m for each finite moment order m.
2. In the usual natural Brownian filtration, every square-integrable martingale has a continuous version and a representation as its initial value plus an Itô integral. In particular, its predictable covariation with the Brownian motion is absolutely continuous in time, with density equal to its representing integrand.
3. Under the common conditional-density hypothesis for a standard Borel random element Y, the initial-enlargement decomposition for a continuous local martingale X is

   X_t - integral_0^t [1/p_{u-}(Y)] d<X,p(y)>_u evaluated at y=Y.

   This is a local martingale in the usual right-continuous enlargement. The bracket is formed in the original filtration for fixed y. We use the continuous, strictly positive density case, so no density-zero correction is needed.
4. A continuous local martingale starting at zero and having quadratic variation t is Brownian motion in its filtration.

The third result is the audited standard initial-enlargement result in theory_008 and theory_009. The other results are standard SDE and Brownian stochastic-calculus facts; the strong-solution result is also indexed by theory_011.

## 1. Conditional observation densities

Let eta_0 be the law of a unit-rate Poisson process on [0,S], regarded as a probability measure on the Borel space of finite ordered event sequences, including the empty sequence. For a fixed sequence y=(r_1,...,r_n), define

L_y = exp(S - integral_0^S V_u du) product_{i=1}^n V_{r_i}.

This is the conditional observation density given the full Brownian path. Indeed, the ratio of the inhomogeneous Poisson density exp(-integral_0^S V_u du) product_i V_{r_i} to the unit-rate density exp(-S) is precisely L_y. The empty product is one.

The assumed all-time positivity gives L_y>0 almost surely. Also

L_y <= exp(S) (sup_{0<=u<=S} V_u)^n

for n>=1, and L_empty<=exp(S). The polynomial moment estimate therefore gives L_y in L^2 for each fixed finite y. In particular, its expectation is finite and positive.

Hierarchical observation sampling and the tower property identify

p_t(y)=E[L_y | F_t]

as a conditional density of Y given F_t with respect to eta_0. These densities have jointly measurable versions. For each fixed y they are square-integrable martingales with continuous versions in the natural Brownian filtration. They are strictly positive throughout [0,T]: a nonnegative continuous martingale that reaches zero is thereafter zero, whereas p_S(y)=L_y>0. Thus p_t(y) and its left limits have no zero on this compact horizon, almost surely for fixed y. Fubini's theorem and the joint density L_y transfer the relevant fixed-index almost-sure statements to evaluation at the actual observation Y.

This also verifies the common-density hypothesis directly in the stated model. The initially enlarged filtration is taken with its usual augmentation as required by the enlargement theorem.

## 2. Markov factorization

For 0<=t<=S and fixed y, split the likelihood at t. Its past factor is F_t-measurable. The strong Markov diffusion has the time-inhomogeneous Markov property relative to the natural Brownian filtration, so

p_t(y)=A_t(y) beta_t(V_t;y),

where

A_t(y)=exp(S - integral_0^t V_u du) product_{r_i<=t} V_{r_i}.

This follows by conditioning the remaining exponential/product functional on V_t. The conditional expectation in beta is under the prior started at time t in state V_t, not under the posterior.

For fixed y, A(y) has finite variation: it is a continuous finite-variation exponential between the finitely many deterministic event times and has only finitely many jumps. It therefore has zero quadratic covariation with W. This statement is not an assertion about an adapted process obtained by inserting Y before computing the bracket.

For t>=S, L_y is already F_S-measurable, hence

p_t(y)=L_y.

Consequently its covariation with W has no contribution after S.

## 3. Covariation with the observation index fixed

Fix y. On every open interval between its event times, the stated regularity of beta permits Itô's formula for beta_t(V_t;y). Localize to compact subsets of positive states and to compact time subintervals when necessary. Its Brownian differential coefficient is

c(V_t,t) partial_v beta_t(V_t;y).

The product formula with A(y) therefore identifies the Brownian coefficient of p(y), on these intervals, as

A_t(y)c(V_t,t) partial_v beta_t(V_t;y).

There is no missing term at the event times. The process p(y), independently identified as a Brownian-filtration square-integrable martingale, has a continuous Itô-integral representation. Uniqueness of its representing integrand identifies that integrand with the preceding expression on each open interval. Their complement in [0,S] is finite and has Lebesgue measure zero. Thus the identification holds dt times probability almost everywhere on the whole observation interval. This also supplies the local integrability needed when approaching its endpoints; no global smoothness of beta across an event time is asserted.

It follows that, for fixed y,

d<W,p(y)>_t = 1_{t<S} A_t(y)c(V_t,t) partial_v beta_t(V_t;y) dt.

Dividing by the positive continuous density, outside the finite event-time set, gives

[1/p_t(y)]d<W,p(y)>_t = 1_{t<S} c(V_t,t) h(V_t,t,S,y)dt.

Values at t=S or at individual event times do not affect this dt identity. The task defines beta_S=1 and extends h by zero after S, so the same identity can be written with the requested indicator 1_{t<=S}.

The joint measurability of the likelihood and its specified derivatives permits the fixed-index identity to be evaluated at y=Y in the enlargement formula. We never treat p(Y) as an F-martingale.

## 4. Enlarged Brownian motion and the SDE

Apply the initial-enlargement decomposition to W. Its hypotheses hold because the event-sequence space is standard Borel, p is a common conditional-density family, and the densities in the preceding calculation are continuous and strictly positive. It yields the G-local martingale

W-tilde_t = W_t - integral_0^{t wedge S} c(V_u,u)h(V_u,u,S,Y)du.

The theorem supplies local finite variation of the compensator. It is continuous, and therefore [W-tilde]_t=[W]_t=t. Since W-tilde_0=0, Lévy's characterization makes W-tilde a G-Brownian motion under the joint law.

Substitute

dW_t=dW-tilde_t+1_{t<=S}c(V_t,t)h(V_t,t,S,Y)dt

into the prior SDE. This gives

dV_t=[a(V_t,t)+1_{t<=S}c(V_t,t)^2h(V_t,t,S,Y)]dt+c(V_t,t)dW-tilde_t.

The substitution is legitimate on the full horizon: the enlargement theorem supplies the finite-variation integral for the Brownian correction, while continuity of V and linear growth make c(V_t,t) bounded along each path on the finite interval. The original diffusion stochastic integral is defined by the same semimartingale integral after enlargement. The initial state remains v_0.

Finally, sigma(Y) is contained in G_0. Brownian increments of W-tilde are consequently independent of Y as well as of the enlarged past. Disintegrating the increment identities on the standard Borel path spaces, first at rational times and then using continuity, shows that for the law of Y-almost every y the same representation holds under the conditional law given Y=y, with a Brownian driving process in the induced conditional filtration. This is precisely the claimed posterior representation. No assertion is needed for exceptional null observations.

All obligations listed above are closed. The empty observation requires no separate argument beyond the empty-product convention, and the proof does not require c to be nonzero.
