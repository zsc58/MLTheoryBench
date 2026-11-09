# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Defines the Bellman residuals with the dummy initial transition and correctly establishes their conditional mean-zero and bounded properties from the Bellman equations, the shared MDP laws, and bounded remaining return.
- **4 points:** Uses prefix measurability to condition on all level-h prefixes so the learned weights are fixed; justifies conditional independence across trajectories; applies conditional weighted Hoeffding at every level; and obtains the simultaneous eta_h bounds with the stated probability and constants. The argument remains valid for signed weights and for zero reward range or zero weight vectors.
- **3 points:** Substitutes the Bellman identities into the estimator, telescopes the adjacent-level value terms including the initial and terminal boundaries, invokes realizability to bound every remaining discrepancy by ell_h, and concludes the displayed bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The standard Hoeffding inequality may be invoked without proving the background theorem, provided its relevant hypotheses and threshold application are justified. Merely naming a concentration inequality or telescoping without establishing the needed conditional structure or identities is insufficient.

A proof that treats data-dependent weights as fixed without a valid prefix-conditioning argument does not establish the theorem-critical concentration step. Conditioning on entire trajectories, including the outcomes being concentrated, is not a substitute. Independence across stages is neither assumed nor required.

The statement concerns every fixed admissible selection rule, with a probability guarantee for that rule. It does not require a single event holding simultaneously over all possible selection rules. No exact minimization, existence of an optimizer, least-second-moment selection, weight normalization, nonnegativity, unconditional weight-moment bound, density coverage, Bellman completeness, or class-uniform concentration argument is required.

Zero-denominator cases must be covered by the argument, but an appropriate concentration statement that already includes them suffices; do not demand a separate case split merely for presentation. If a matching loss is infinite, the conclusion is automatic in the extended-real sense. Do not require the solver to establish optimizer existence or uniform boundedness of the discriminator class, or to reproduce the reference proof's separate measurability discussion when using the stated objects correctly.
