# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly starts from the real-state Bellman expression and changes measure to the attacked-state transition law using the stated density ratio, with the ratio and transition laws in the correct direction.
- **4 points:** Performs the add-subtract algebra correctly and derives the exact action-level identity \(Q^\pi(x^0,a)=Q^\pi(x,a)+\Delta_{\mathrm{tr}}(x,a)+\Delta_{\mathrm{rw}}(x,a)\), including both correction integrals with their required factors.
- **2 points:** Averages the action-level identity first under the policy and then under the attacked posterior to obtain the exact posterior expectation for \(J(o)\).
- **1 point:** Correctly concludes that minimization over the stated likelihood ellipsoid preserves the exact decomposed objective.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, direct substitution of the correction definitions and cancellation can earn full credit without displaying the action-level identity separately.

The density ratio is defined up to null sets under the attacked-state transition law. Applying the stated absolute continuity and density-ratio convention is sufficient; a separate discussion of null sets is not mandatory unless the solution makes an invalid pointwise claim that affects its argument.

The assumptions justify the defining integrals and the joint expectation. It is sufficient to integrate the sum of the three policy-averaged terms under the posterior; do not demand separate posterior integrability of each summand.

The final claim is equality of optimization formulations, not existence of an optimizer. Equal infima and identical minimizers whenever attained are valid interpretations. Do not require continuity, compactness arguments, an explicit minimizing observation, or a filtering derivation.

The cases \(\gamma=0\), \(\rho=0\), and deterministic policies are included. No separate case split is needed if the proof applies to them.
