# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derive the contraction of G(x)=x-(mu/L^2)F(x), establish the fixed-point relation, rewrite the stochastic recursion with the time-dependent rescaled stepsize and correctly rescaled noise, and introduce a valid averaged-noise/auxiliary-iterate decomposition with its perturbation and error-transfer bounds.
- **3 points:** In the independent finite-p-moment regime, establish the weighted-noise p-moment estimate, verify the hypotheses of any independent-sum inequality used, derive a quantitatively valid auxiliary recursion, and solve it to obtain the (k+K0)^{-(p-1)} rate for the original iterate. Deterministic weights and the factor zeta^p in rescaled noise moments must be handled correctly. A valid alternative argument establishing the same uniform bound receives equivalent credit.
- **3 points:** In the weakly stationary long-range-dependent regime, correctly expand the weighted-noise second moment, use the scalar covariance envelope to control all lagged cross terms, derive and solve a valid squared auxiliary recursion, and obtain the (k+K0)^(-delta) rate for the original iterate. If rescaling is used, the covariance is multiplied by zeta^2. No independence, martingale-difference property, mixing, Gaussianity, or matrix covariance decay may be assumed without justification from the stated model.
- **2 points:** Give and justify explicit finite thresholds and prefactors with the public dependency hierarchy; verify the product/convolution conditions or an equivalent recurrence argument; control initial/transient terms; and establish both conclusions for every k>=0, including mu=L and any endpoint stepsize allowed by the chosen thresholds.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its exact numerical constants, or its precise sufficient thresholds. The two noise regimes may be proved in either order. Allocate the core-step credit by equivalent mathematical accomplishments when another proof architecture is used.

A standard independent-sum moment inequality may be invoked when its relevant quantitative statement is given and independence, centering, moment finiteness, and the Euclidean-vector setting are verified. Merely naming a paper-specific auxiliary result, a weighted-sum estimate, or a contraction method does not close its mathematical obligation. A recurrence solution must include sufficient parameter conditions and a derivation or a correctly stated standard result with verified hypotheses.

The threshold on beta must not depend on beta or K0. The offset threshold may depend on beta but not on K0. Prefactors may depend on the fixed admissible K0 and the initial error; do not demand uniformity over all K0 with one prefactor. Constants must be uniform in time and in the admissible operators, dimensions, and noise laws with the same public parameter values.

Treat failure to control the weighted-noise term, failure to close either auxiliary recursion, circular threshold choices, or use of an unjustified noise assumption as a theorem-critical gap. A proof that establishes only an asymptotic order without justifying the all-k bound and required dependencies is incomplete. Conversely, an eventual estimate together with rigorously controlled finite transients can establish an all-k result.

The infinite second moment and covariance nonsummability restrictions remain part of the respective models, but a valid upper-bound proof need not use them: proving the same bound for a larger noise class is acceptable. Do not require the solver to reproduce source-local errors or discuss their repair. In particular, accept the correct time indices, rescaled moments and covariances, the rho=1 case, and separate handling of k=0.
