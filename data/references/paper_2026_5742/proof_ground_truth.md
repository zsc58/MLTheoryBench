# Reference Proof

## Proof Structure

First verify absolute continuity and finiteness of the two path laws from the finite-state jump likelihood formula. Next insert the data mass into the averaged negative path ELBO, identifying its excess over entropy with a KL divergence between two joint laws on the clean state and noisy path. Finally, factor both joint laws through the noisy path and its lower endpoint and apply the KL chain rule.

## Complete Proof

Let `J` and `M` denote the joint probability laws on `S x Omega` given by

`J(z,dw) = mu_0(z) N_z(dw)`

and

`M(z,dw) = d(z|w(t1)) R(dw)`.

We first check that the relevant Radon-Nikodym derivatives exist. Applying the finite-state jump-path likelihood formula to `P` and `R`, viewed in reverse time, gives

`KL(P || R) = KL(mu_t2 || nu_t2) + integral_[t1,t2] E_P[ sum_(y != Z_t) Phi(a_t(Z_t,y),b_t(Z_t,y)) ] dt`.

Indeed, the log likelihood ratio of a path is the log ratio of its endpoint masses, plus the sum over its jumps of `log(a/b)`, plus the integral of the difference of its holding rates. The jump compensator replaces the expected jump sum by the integral of `a log(a/b)`. Combining this with the holding-rate contribution `b-a` yields `Phi(a,b)`. The endpoint and rate-support assumptions imply `P << R`, and the assumed integral is finite. Thus `KL(P || R) < infinity`.

The Markov property of the noising process implies that, conditional on `Z_t1`, its trajectory after `t1` contains no further information about `Z_0`. Consequently the noising joint law has the alternative factorization

`J(z,dw) = mu_(0|t1)(z|w(t1)) P(dw)`.

By definition, the comparison joint law factors as

`M(z,dw) = d(z|w(t1)) R(dw)`.

The decoder-support assumption together with `P << R` therefore gives `J << M`. In particular, for `mu_0`-almost every `z`, `N_z << M_z`, so the negative path ELBO in the problem is well-defined and finite.

For such `z`, comparison of `J(z,dw)=mu_0(z)N_z(dw)` with `M(z,dw)=M_z(dw)` gives

`log(dJ/dM)(z,w) = log(mu_0(z)) + log(dN_z/dM_z)(w)`.

Taking expectation under `J` yields

`KL(J || M) = sum_z mu_0(z) log(mu_0(z)) + N`

`= N - H(mu_0)`.

This is the required conversion of the entropy-adjusted negative ELBO into a joint path-law divergence.

It remains to decompose that divergence. Using the two factorizations through the path marginal, the Radon-Nikodym derivative splits as

`dJ/dM (z,w) = (dP/dR)(w) * mu_(0|t1)(z|w(t1)) / d(z|w(t1))`

on the support of `J`. Taking its logarithm and expectation under `J` gives

`KL(J || M) = KL(P || R)`

`+ E_(w~P)[ KL(mu_(0|t1)(.|w(t1)) || d(.|w(t1))) ]`.

Under `P`, the lower endpoint `w(t1)` has law `mu_t1`. Hence

`KL(J || M) = KL(P || R) + E_(x~mu_t1)[KL(mu_(0|t1)(.|x) || d(.|x))]`.

Combining this identity with `KL(J || M)=N-H(mu_0)` proves the theorem.
