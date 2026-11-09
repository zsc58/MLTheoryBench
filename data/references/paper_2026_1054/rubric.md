# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identify the complementary population functional q=1-D as the integrated expected conditional-variance ratio. Use total variance to establish that its population ratios lie in [0,1], and obtain the n^{-1/2} fluctuation for their iid average. The conditional variance must be integrated over the population covariate, not evaluated at the held-out covariate.
- **3 points:** Establish conditional denominator concentration and exact leave-one-out variance bias; derive weighted ratio stability using finite inverse moments; and control the simultaneous bad-denominator event. A valid alternative may avoid the simultaneous event, but must rigorously handle small and zero empirical denominators. The zero-ratio convention is part of the task and does not license a positive-denominator assumption.
- **3 points:** Establish numerator fluctuation and bias. A replacement proof must account for old and new incoming edges, the relation between full and deleted graphs, and tie randomness where applicable. Derive the exact normalized conditional pairwise expansion and use the Holder assumptions to bound bias by centre-to-neighbour radius moments. Do not infer independence between numerators indexed by different evaluation points.
- **2 points:** Establish the required neighbour-radius moment bound through correctly conditioned occupancy counting or another complete argument; respect the admissible mass range and cover large admissible K. Combine the weighted estimates and probability bounds to obtain the stated O_P rate.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's particular decomposition, concentration inequality, or tie coupling.

The population definition contains E_X before integration over the response evaluation point. Replacing that quantity by Var_X(m_{1,y}(X)) changes q to D; replacing it by a conditional variance at X_i also changes the object and invalidates the ideal bounded-ratio argument.

On the relative good-denominator event the correct inequality is V_{n,i}≥V_Y(Y_i)/2. A bound on the probability of its complement is sufficient for O_P control; an expectation bound on ratios over the complement is not required.

Uniform tie breaking has independent observation-free randomization semantics. A private consistent-priority coupling is acceptable, but its sensitivity estimates must be derived. The full-sample indegree assumption implies a deleted-graph bound with an enlarged constant when priorities are coupled consistently. Constants in a replacement estimate need not equal the reference proof's constants.

The repaired local-mass hypothesis is uniform over every centre and includes the endpoint c_0r^d=1. It therefore permits direct radius truncation. A proof of the stronger radius bound C(K/n)^{β/d} earns full credit; reproducing an unnecessary logarithmic-tail calculation is not required. Do not accept an unconditional binomial law asserted after conditioning on a sample-maximum event without justification, or a mass lower bound larger than one.

All theorem-critical applications must be checked. Merely naming concentration, Efron-Stein, or nearest-neighbour geometry earns no credit for an unproved application. No paper-specific denominator or radius estimate is available to the solver as an assumed theorem. A complete derivation using standard inequalities is sufficient.
