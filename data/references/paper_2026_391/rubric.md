# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies the likelihood normalization and sample-disparity maximizer and justifies the one-sided constrained maximization. A valid argument may use concavity of the profiled log likelihood on its positive domain or another correct optimization argument. Raw-likelihood concavity is false and must not be required. If using differentiation, retain subgroup indicators; the derivative of log L is N_G lambda. Account for exceptional samples directly or work on an explicitly justified event of probability tending to one.
- **3 points:** Establishes the scalar empirical-likelihood quadratic expansion at the boundary. This includes positivity/feasibility with probability tending to one, a valid multiplier representation, a noncircular multiplier-rate argument before Taylor expansion, empirical second-moment consistency, and control of both multiplier and logarithm remainders under the stated conditional second moment. A valid alternative derivation is acceptable. Do not assume an unstated third moment, global metric moment, or boundedness condition.
- **3 points:** Combines the expansion with the estimator's sign using the same normalized sample moment, thereby deriving the positive-part Gaussian-square limit and the half-point-mass/half-chi-square distribution. Merely naming a chi-bar-square law or proving only an unconstrained chi-square limit does not discharge this step.
- **2 points:** Uses continuity at the positive mixture critical value to obtain limiting rejection probability alpha at the boundary, and proves vanishing rejection probability for each fixed strict-interior null through estimator consistency or an equivalent argument. States the resulting Type I guarantee pointwise in the data-generating law.

# Evaluator Notes

Accept a complete valid alternative proof; do not require incidental presentation choices or optional curvature calculations. A scalar empirical-likelihood theorem may replace explicit expansion only if its relevant statement is supplied and its hypotheses actually cover this task; invoking a stronger theorem without verifying its assumptions is insufficient.

The task allows pi_G=1 and imposes no moment condition on R outside G. Finite conditional variance is nonzero. The reference value and threshold are fixed, and no plug-in reference estimator is part of the experiment. The conventions for N_G=0 and log zero are explicit. An asymptotic proof may discard exceptional events after proving their probabilities tend to zero. Avoid treating infinity times zero as an ordinary product; a piecewise expression or a high-probability finite-valued reduction is valid.

The target is not uniform asymptotic size over arbitrary sequences of laws. Fixed-law limits do not justify interchanging a supremum over laws with a limit. No additional uniformity or local-power theorem is required.

A minor algebraic or notation error may be repaired locally. Unresolved feasibility, circular multiplier-rate reasoning, uncontrolled expansion remainders, loss of the joint sign information, or unsupported calibration are theorem-critical gaps. The reference proof contains no unresolved GT obligation.
