# Reference Proof

## Source Contract and Scope

The selected result is the independent, common-prior, revealed-value reservoir model in L000132-L000143 and L000318-L000337. Every round plays either one fresh arm, revealing and receiving its value, or a previously revealed arm. No free initial observations are available. Decisions precede revelation of a fresh value and use only the stated history and independent policy randomization.

For the constant-override extension, L000014, L000021, and L000071 provide the ordinary history-conditional mixture semantics; L000331-L000336 use the resulting inspection waiting time. The first inspection is compulsory under the two-action model when the history is empty. Charging that inspection does not invalidate the source's waiting-time upper bound. The remaining rounds use independent override coins, exploit the best revealed arm between inspections, and stop inspecting after success.

The finite-action normalization in the general algorithm is not applied to an infinite collection of equally weighted arms: here an inspection draws one independent fresh value from F. Neither a Pandora optimality theorem nor the separate noisy-bandit and information-budget results are needed. The default annealed schedule is not the constant-epsilon procedure; L000143 and L000151 explicitly distinguish those regimes.

## Theorem-Critical Obligations

1. Establish a positive mean inspection gap and justify fresh-draw expectations under adaptive inspection decisions.
2. Bound the horizon-truncated reservation policy and evaluate its threshold choice.
3. Establish the converse uniformly over all admissible, possibly horizon-dependent policies.
4. Verify the threshold-price calibration, including distributions with atoms.
5. Bound calendar-round regret for the explicitly defined throttled policy, including its initial inspection.

All five obligations are derived below without an unresolved external dependency.

## step_001: Positive Mean Inspection Gap

Let mu = E[1-X]. Choose

delta = min{y0, 1, (2c_+)^(-1/alpha)}.

Then delta > 0, the tail assumption applies at delta, and p(delta) <= 1/2. Consequently,

mu >= delta P(X < 1-delta) = delta(1-p(delta)) >= delta/2 > 0.

All round gaps lie in [0,1], so every expectation used below is finite. Conditional on the history and the decision to inspect, the inspected value has law F: the decision is taken before revelation, and the unrevealed arm values and auxiliary policy randomization are independent. This remains true when the number and timing of inspections depend on previous values.

## step_002: Unthrottled Upper Bound

Fix 0 < y <= min{1,y0}. Consider the reservation policy continued hypothetically beyond T with this same threshold, and let K be the inspection number of its first success. Independent fresh values give

P(K > n) = (1-p(y))^n for integers n >= 0.

Therefore

E[K] = sum_{n>=0} P(K>n) = 1/p(y).

Up to and including success, each round incurs gap at most 1. Every subsequent round incurs gap at most y. If there is no success by T, all T rounds are included in the initial search period. Hence, pathwise, total regret is at most min{K,T}+Ty, and

R_T(y) <= E[min{K,T}] + Ty <= 1/p(y)+Ty <= c_-^(-1)y^(-alpha)+Ty.

Set kappa = 1/(alpha+1) and q = alpha/(alpha+1). For y_T = a T^(-kappa), eventually y_T <= min{1,y0}, and

R_T(y_T) <= (c_-^(-1)a^(-alpha)+a) T^q.

This proves the asserted upper bound without assuming that success occurs within the horizon.

## step_003: Policy-Uniform Lower Bound

Fix any admissible policy and horizon T. Let I_t indicate that round t inspects a fresh arm, and let N_T = sum_{t=1}^T I_t. Include the policy randomization determining the current action in the pre-revelation information. Then I_t is measurable with respect to that information, and an inspected value still has law F. Thus

E[I_t(1-Y_t)] = mu E[I_t].

Summing over the finite horizon, and using nonnegative regret on exploitation rounds, gives

R_T(pi) >= mu E[N_T].

For a fixed 0 < y <= min{1,y0}, let

S_T(y) = sum_{t=1}^T I_t 1{Y_t >= 1-y}

count successful fresh inspections. The same conditioning argument gives

E[S_T(y)] = p(y) E[N_T].

These identities use pre-revelation conditioning, not independence between N_T and the observed values.

If E[N_T] >= 1/(4p(y)), then

R_T(pi) >= mu/(4p(y)) >= mu/(4c_+) y^(-alpha).

Otherwise E[S_T(y)] < 1/4. Since 1{S_T(y)>=1} <= S_T(y), the probability that any inspected arm reaches the threshold is less than 1/4. With probability greater than 3/4, every inspected arm has value below 1-y. Every action on that event either inspects such an arm or exploits an arm previously inspected, so every round has gap at least y. There is no initially available revealed arm outside this accounting. It follows that

R_T(pi) >= (3/4)Ty.

Combining the cases,

R_T(pi) >= min{mu/(4c_+) y^(-alpha), (3/4)Ty}.

Choose y = T^(-kappa). For all sufficiently large T, this threshold is in the required range, and mu >= delta/2 yields

R_T(pi) >= min{delta/(8c_+), 3/4} T^q.

The constant and the required horizon cutoff depend only on the fixed tail parameters, not on the policy. The argument therefore covers every admissible policy separately at every sufficiently large horizon, including policies chosen as a function of T.

## step_004: Price Calibration

For 0 <= y <= 1 and any fixed x in [0,1],

integral_0^y 1{x >= 1-s} ds = (x-(1-y))^+.

The value of the indicator at its single boundary point does not affect the integral. Integrating this nonnegative identity with respect to F gives the source's correspondence between the tail integral and expected improvement; no continuity of F is required.

For 0 < y <= min{1,y0}, integrating the assumed tail inequalities gives

L c_- y^(alpha+1)/(alpha+1) <= lambda(y) <= L c_+ y^(alpha+1)/(alpha+1).

At y_T = a T^(-kappa), this becomes

[c_- a^(alpha+1)/(alpha+1)] L/T <= lambda(y_T) <= [c_+ a^(alpha+1)/(alpha+1)] L/T.

Thus lambda(y_T) = Theta(L/T), with comparison constants independent of L and T.

## step_005: Constant-Override Calendar-Time Bound

Fix epsilon in (0,1] and 0 < y <= min{1,y0}, and write p = p(y) > 0. Continue the throttled policy hypothetically beyond T to define its first successful inspection time tau.

The first round is an inspection. It succeeds with probability p. Conditional on its failure and on no later success yet, each subsequent round succeeds with probability epsilon p: its override coin is independent of the history and values, and, when it requests an inspection, the new value independently succeeds with probability p. If W denotes the number of subsequent rounds needed for success after a failed first inspection, repeated conditioning gives

P(W > n | first inspection fails) = (1-epsilon p)^n,

and therefore

E[W | first inspection fails] = 1/(epsilon p).

Consequently,

E[tau] = 1 + (1-p)/(epsilon p) <= 1/(epsilon p),

where the last inequality uses epsilon <= 1. This accounts for the initial inspection rather than assigning a free initial arm or allowing an undefined exploitation action.

Every round through tau, including intervening exploitation rounds, has gap at most 1. After tau, the selected arm has gap at most y and is exploited forever. Hence

R_T(y) <= E[min{tau,T}] + Ty <= 1/(epsilon p(y)) + Ty <= 1/(epsilon c_- y^alpha) + Ty.

For y_(T,epsilon) = a(epsilon T)^(-kappa), once this threshold is in the tail range,

R_T <= (c_-^(-1)a^(-alpha)+a) epsilon^(-kappa) T^q.

In particular, the displayed multiplicative coefficient can be chosen independently of epsilon, although the sufficiently-large-horizon condition depends on fixed epsilon. This is a calendar-time calculation; it does not follow merely by substituting epsilon T for T in a cumulative-regret formula.

Applying the bounds in step_004 to the same threshold gives

[c_- a^(alpha+1)/(alpha+1)] L/(epsilon T) <= lambda(y_(T,epsilon)) <= [c_+ a^(alpha+1)/(alpha+1)] L/(epsilon T).

The throttled policy is an admissible policy in the original sequential action model, so step_003 also applies to it. Its regret is consequently Theta(T^q) for every fixed epsilon. No matching dependence on epsilon in the lower-bound constant is asserted or required.

## Closure

The proof covers arbitrary atoms in F, horizons with no discovery, the initially empty revealed set, epsilon = 1, and every fixed epsilon > 0. The hypothesis alpha > 0 excludes a positive atom at the upper endpoint and supplies a strictly positive inspection gap through step_001. All asymptotic claims are restricted to sufficiently large horizons for their thresholds to enter the assumed tail range. There are no unresolved theorem-critical proof obligations.
