# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly reduces exact recovery to MAP optimality, uses permutation symmetry, defines the likelihood score, and handles the zero-signal tie case rather than assuming all ties are null.
- **4 points:** Proves achievability above the threshold with justified uniform concentration and conditional moment bounds, the correct moved-edge count, a displacement split, and summable permutation-class estimates. For large displacement, uses the unnormalized sum of likelihood weights to rule out negative scores.
- **3 points:** Proves the converse through a diverging transposition first moment, including the Gaussian-tail prefactor, and an asymptotically matching second moment. The proof must distinguish disjoint and intersecting pairs and achieve the required relative precision under d=omega((log n)^2).
- **1 point:** Transfers MAP failure to impossibility for every estimator through Bayes optimality under the uniform prior.

# Evaluator Notes

Accept a complete valid alternative proof, including a direct treatment of signed correlations by sign changes. Do not require incidental presentation choices from the reference proof. Merely naming a concentration event does not prove the achievability estimates. If a converse count includes a high-probability-event indicator, its effect on the first moment must be quantified at the single-failure scale; counting failures without that indicator is also valid. An O(sqrt(log n/d)) uniform correlation error alone does not establish relative independence of disjoint transposition failures at the stated dimension scale.
