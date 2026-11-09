# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Oracle characterization and concentration.** Correctly reduces the oracle allocation to a minimum cost-variance source for each coordinate, derives or otherwise establishes the required oracle comparison, and obtains a simultaneous inflated-standard-deviation sandwich. Handles the infinite-norm endpoint if it is not covered directly by the argument. The empirical variance statistic must have the correct normalization, and the concentration hypotheses must be satisfied.
- **4 points: Stable empirical allocation comparison.** Controls both the true-variance contribution and the bounded-increment contribution under the empirical allocation. The reference route proves `a<=sqrt(Gamma_p)+C_1 eta+1_{p<2}C_2 eta^r` and `b<=3[Gamma_p eta^(-2)+C_1^2+1_{p<2}C_2^2 eta^(2r-2)]`, with `r=2p/(p+2)` and the infinite-p convention. A different sufficient comparison earns full credit. Merely asserting closeness to the oracle does not close this obligation. The argument must be valid for the stated positive-variance instances, without adding a uniform variance lower bound, a source-selection gap, or an extra public assumption.
- **2 points: Conditional estimation bound and budget.** Conditions on the first-stage information so that selected sources and counts are fixed, applies valid concentration to fresh second-stage observations, and aggregates in `l_p`. Establishes well-defined positive integer counts and total cost at most `T`. Accounts correctly for the reserved observations or establishes an equivalent bound for the actual specified allocation. Combines the failure probabilities to obtain at least `1-delta`.
- **2 points: Parameter substitution and uniformity.** Preserves the stated leading coefficient, obtains the correct powers of `T`, `M`, and the confidence logarithm in both regimes, and controls exploration and rounding losses. The hidden constants must have the allowed dependencies and be independent of both `T` and `delta`. Saying only that additional terms decay faster for fixed `delta` is not a complete uniform comparison. No unproved restriction such as `eta<1` may be imposed; a valid case split or a uniform estimate is acceptable.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's intermediate constants, its particular `eta^r` term, its inverse-square inflation bound, or its presentation order. In particular, an alternative argument that exploits the fixed positive instance variances may avoid the quasi-norm calculation; this is acceptable if its constants have precisely the dependencies permitted by the task and it proves both requested regimes. The estimator itself must not be given the unknown variances.

The oracle calculation need not be presented separately if it is established inside another valid comparison. The standard empirical-standard-deviation concentration theorem may be invoked with a correct relevant statement and verified hypotheses; it need not be reproved. Ordinary bounded-variable concentration and Minkowski may likewise be used correctly.

A flawed intermediate inequality does not erase independently established later credit, but it cannot serve as an unproved premise. Do not require or reward the source's incorrect dropped numerical factor in the variance-mismatch simplification. Merely citing the final source theorem does not supply the requested proof.

The theorem-critical obligations are a sufficient empirical-allocation comparison, valid conditional sampling and concentration, feasible integer implementation, and the final bounds with their stated uniformity. No specific proof route is mandatory.
