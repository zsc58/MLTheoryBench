# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes boundedness and continuity of the recursively defined values and one-step objectives, and nonemptiness and compactness of the worst-case sets using the compact ambiguity sets and continuous objectives.
- **4 points:** Proves the envelope result for possibly nonunique worst-case laws. This includes uniform expansion over feasible laws, comparison with original and perturbed minimizers, identification of limiting perturbed minimizers as original optimizers, and the right-minimum/left-maximum formulas with correct inequality signs.
- **3 points:** Rigorously differentiates the policy integral, justifying domination from the bounded score and bounded one-step quotients. Closes the backward induction from the zero terminal derivative, using value-quotient equicontinuity to establish continuous uniform downstream sensitivities after proving pointwise convergence.
- **1 point:** Derives the stated one-sided derivative of J by integrating against the fixed, parameter-independent initial law.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The Bellman recursion is supplied as the definition of the public values. A solver need not separately prove equality with a trajectory-law infimum or construct measurable minimizing kernels to earn full credit. Such arguments are valid supporting material but are not additional scoring requirements.

Apply every directional conclusion separately on the relevant feasible side. A boundary direction feasible only for positive increments does not require or define the negative-increment derivative.

Equicontinuity by itself does not prove existence of a derivative. A correct induction first proves pointwise existence and then obtains continuity and uniform convergence. Do not require equicontinuity or continuity of the derivatives of G in the state-action variables; boundedness and measurability suffice for the policy integral.

A bare appeal to Danskin without a relevant statement and verification of its uniformity or moving-optimizer hypotheses leaves a theorem-critical gap. A correctly stated applicable envelope theorem with those hypotheses verified is acceptable, as is the explicit compactness argument.

Do not impose uniqueness, differentiability of worst-case selectors, dual-quotient stability, or a vector-valued gradient. Do not accept a smooth likelihood-ratio formula as a substitute for the requested general one-sided objective derivative unless the solver also establishes the actual requested claim under the stated assumptions.
