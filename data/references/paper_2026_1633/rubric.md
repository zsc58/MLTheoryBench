# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes a uniform finite-sample upper comparison using a valid PAC-Bayes statement, a fixed sample-independent comparator, and objective optimality on the comparator-feasibility event. Controls sampling and feasibility failures and supplies a remainder tending to zero uniformly over experiments, with dependence on lambda and L* made explicit.
- **2 points:** Correctly minimizes and inverts the constrained transform in both lambda branches. Handles possible population risks above one half when lambda<=1, excludes the wrong inverse branch when lambda>1, and justifies inverse existence and the vanishing expected-risk remainder.
- **4 points:** Gives the matching lower bound on one fixed experiment with a normalized prior and comparator KL at most 10. Establishes the required growing-prefix empirical-error events, with the relevant specialized consequence proved rather than merely named. Compares arbitrary posteriors, not only two-point mixtures, and proves vanishing good mass or an equivalent limiting-risk conclusion. Handles L'=L*.
- **1 point:** Combines the bounds with the correct fixed-instance and supremum/limit quantifiers to obtain W_lambda(L*)=ell_lambda(L*).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, prior weights, or exact remainder constants. A clear explicit inverse modulus or fixed-parameter inverse sensitivity is acceptable together with the PAC-Bayes/KL and sampling terms.

A standard concentration result may be invoked when its relevant statement and hypotheses are supplied and verified. A citation to a specialized prior-work construction or binomial-minimum theorem alone does not complete the corresponding obligation.

Do not accept an m-dependent family of experiments as a proof of the fixed-instance lower bound. Growing finite prefixes of one fixed infinite experiment are valid. Do not accept an unsupported restriction of an optimizing posterior to two hypotheses, or treat arbitrarily small positive good mass as a fixed constant in an Omega(m) estimate. Convergence of the good mass to zero in probability suffices; eventual exact zero mass is neither required nor established by the reference proof.

Treat omission of the lower-instance mechanism, arbitrary-posterior comparison, either lambda branch, or the relevant transform domain as a theorem-critical gap. A missing comparator-feasibility tail is a local omission only when the rest of the argument explicitly uses a fixed comparator with L*<1/2 and can incorporate its exponentially small failure event without altering the proof.
