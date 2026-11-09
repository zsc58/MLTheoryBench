# Reference Proof

## Proof Structure

Verify split-conformal validity using the fitted-score exchangeability and corrected quantile convention. Apply independence of the Bernoulli randomization to establish marginal coverage and, under the additional premise, conditional coverage. Compute the randomized set's expected length. Finally normalize the base length curve by the coverage level and use the derivative condition to find a deterministic mixture parameter giving a strict length reduction.

## Complete Proof

### Base coverage

Let F denote the training data and all randomness used to fit the score. Conditional on F, the calibration observations and the test observation are exchangeable, and the same fitted score is applied to each. Their n+1 scores are therefore conditionally exchangeable.

Fix u in (0,1) and let k=ceil((n+1)u). If k=n+1, the threshold Q_u is +infinity, so B_u(X) contains every real response and its coverage is one. Otherwise Q_u is the k-th smallest calibration score. The standard exchangeable-rank argument gives

`P(Y in B_u(X) | F) >= k/(n+1) >= u`.

For completeness, introduce independent continuous tie breakers solely for this rank argument. Conditional on F, the test score's rank among the n+1 lexicographically ordered score–tie-breaker pairs is uniform. If that rank is at most k, at most k-1 calibration scores can be strictly smaller than the test score, so the test score is no larger than the k-th smallest calibration score. Thus ties can only increase the coverage bound. Averaging over F proves

`P(Y in B_u(X)) >= u`.

### Marginal and conditional mixture coverage

Fix any deterministic `p in (q,1)` and put `u_p=q/p`. Then `u_p in (q,1)`. By the base coverage result,

`P(Y in B_{u_p}(X)) >= u_p`.

The Bernoulli variable is independent of the entire base construction and the test pair. Consequently,

`P(Y in T_{p,q}(X)) >= P(Z=1, Y in B_{u_p}(X)) = p P(Y in B_{u_p}(X)) >= p u_p = q`.

The omitted event on the singleton branch can only increase coverage. Thus every admissible deterministic p preserves the target marginal coverage.

If the additional conditional premise holds, independence also gives, almost surely,

`P(Y in T_{p,q}(X) | X) >= P(Z=1, Y in B_{u_p}(X) | X) = p P(Y in B_{u_p}(X) | X) >= p u_p = q`.

This statement holds for each fixed p; it does not assert that an arbitrary data-dependent choice of p preserves coverage.

### Expected length

The singleton has Lebesgue length zero. Independence and the definition of G yield

`E|T_{p,q}(X)| = p E|B_{q/p}(X)| = p G(q/p)`.

This identity is valid for nonnegative extended expectations as well. The base set at target coverage q has expected length G(q).

### Strict improvement and parameter selection

Ordinary real differentiability at q supplies a neighborhood of q on which the following real-valued derivative calculation is valid. Define

`H(u)=G(u)/u`

on that neighborhood. Then

`H'(q) = (q G'(q)-G(q))/q^2 < 0`.

By the definition of the derivative, for all sufficiently small positive h the difference quotient

`[H(q+h)-H(q)]/h`

is negative. Choose such an h with q+h<1 and set u=q+h. Then q<u<1 and H(u)<H(q).

Choose the deterministic number p=q/u. Since q<u<1, we have q<p<1 and q/p=u. Therefore,

`E|T_{p,q}(X)| = pG(q/p) = (q/u)G(u) = qH(u) < qH(q) = G(q) = E|B_q(X)|`.

The parameter depends on q and the fixed average-length curve, not on a realized calibration sample or the test observation. For this same deterministic parameter, the marginal and, under its additional premise, conditional coverage statements already proved apply. This establishes the integrated claim.

## Obligation Closure

The exchangeable-rank argument closes the standard coverage dependency with its hypotheses and boundary convention verified. Both mixture coverage calculations, the expected-length identity, the local derivative implication, and the parameter-domain check are explicitly derived above. No paper-specific dependency remains unproved.
