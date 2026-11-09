# Problem

## Setup

There is an infinite reservoir of arms with independent values drawn from a common distribution F supported on [0,1]. An arm's value is not observed until that arm is inspected. Initially, no arm has been inspected.

The horizon T is a positive integer. At each round an adaptive policy takes exactly one action:

1. inspect one fresh arm, reveal its value X, and receive X as that round's payoff; or
2. exploit one previously revealed arm and receive its revealed value as that round's payoff.

Thus at most one fresh arm can be inspected per round, every inspection consumes one horizon round, and the first round must inspect a fresh arm. Decisions may depend on F, T, past actions and revealed values, and auxiliary randomization independent of the reservoir, but not on unrevealed values. Policies are measurable with respect to this information and may depend on the horizon.

For a policy pi, let Y_t be its payoff at round t and define

R_T(pi) = E[sum_{t=1}^T (1-Y_t)],

where the expectation includes the reservoir values and policy randomization. Write

p(y) = P(X >= 1-y).

Assume that for some alpha > 0, constants 0 < c_- <= c_+ < infinity, and y0 > 0,

c_- y^alpha <= p(y) <= c_+ y^alpha for all 0 < y <= y0.

Let L > 0 be the price scale. For 0 <= y <= 1, define the threshold-price correspondence

lambda(y) = L integral_0^y p(s) ds.

For a threshold y in (0,1], the reservation policy inspects fresh arms until one has value at least 1-y and then exploits that arm for every remaining round.

For a fixed override probability epsilon in (0,1], define the throttled reservation policy as follows. Its first round inspects a fresh arm, with this inspection included in both the horizon and regret. Until an arm of value at least 1-y has been revealed, at each subsequent round it uses a new Bernoulli(epsilon) coin: on success it inspects a fresh arm, and otherwise it exploits an arm with the largest value revealed so far. The coins are mutually independent and independent of all arm values. Once the threshold has been reached, the policy exploits the qualifying arm for every remaining round.

## Task

Fix a constant a > 0. All assertions below concern T tending to infinity, so the specified thresholds eventually belong to (0,min{1,y0}].

Prove that the reservation policy with

y_T = a T^(-1/(alpha+1))

satisfies

R_T = O(T^(alpha/(alpha+1))).

Prove also that there are constants c > 0 and T0, independent of the policy, such that every admissible adaptive policy satisfies

R_T(pi) >= c T^(alpha/(alpha+1)) for every integer T >= T0.

Moreover, prove

lambda(y_T) = Theta(L/T).

For the throttled reservation policy with fixed epsilon and threshold

y_(T,epsilon) = a (epsilon T)^(-1/(alpha+1)),

prove

R_T = O(epsilon^(-1/(alpha+1)) T^(alpha/(alpha+1)))

and

lambda(y_(T,epsilon)) = Theta(L/(epsilon T)).

In particular, the throttled policy has the same T^(alpha/(alpha+1)) regret order for each fixed epsilon, with an epsilon-dependent multiplicative constant.

The unthrottled comparison constants may depend on the fixed tail parameters and a; the lower-bound constants may depend on the fixed tail parameters but not on the policy. The throttled asymptotic assertions are for fixed epsilon. No comparison constant depends on T, and the constants in the price comparisons do not depend on L.
