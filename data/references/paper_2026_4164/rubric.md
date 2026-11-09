# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly uses independent score learning and the i.i.d. sampling model to derive exchangeability of the null calibration scores and a null test score after the needed conditioning. Addresses why null validity also holds conditional on a fixed positive-probability test-membership configuration, or supplies an equally valid treatment of random null membership for the multiple-testing step.
- **3 points:** Establishes exact conditional uniformity of the randomized value given the null event and N_0. Handles arbitrary score ties, for example by conditioning on the unordered multiset and mixing uniform tie-block intervals with probabilities equal to their lengths. Merely asserting that an unrandomized rank is uniform despite ties is insufficient.
- **2 points:** Relates the deterministic and randomized values pointwise and correctly deduces the required null super-uniformity, with appropriate averaging over the conditioning information.
- **2 points:** Correctly applies BY under arbitrary dependence and BH under the stated full-vector PRDS condition. Verifies the hypotheses under the same probability law, handles the random null set by conditioning and averaging or a valid alternative, and obtains the task's FDR bounds.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its exact conditioning order.

The standard BY theorem and the standard PRDS-BH theorem may be invoked without proving them. Full credit for that invocation requires a correct statement of the relevant hypotheses and an explanation that they hold here. A bare procedure name without verifying applicability is insufficient. In particular, validity conditional only on one test index being null must not be silently treated as validity under every fixed null configuration without justification.

The PRDS hypothesis is imposed on the full p-value vector conditional on each positive-probability test-membership configuration. Do not require PRDS after additionally conditioning on the learned score, the calibration null count, or the calibration data. Conversely, dependence only within the null subvector is not the stated PRDS condition.

N_0=0 is permitted: then the deterministic value is one and the randomized value is U_j. If the population null probability is zero, the conditional null assertions are inapplicable and FDR is zero. Unsupported conditioning events require no asserted conditional distribution. A general argument that already covers these cases need not list them separately. Do not require a positive target probability, continuity of the score distribution, a minimum positive null calibration count, regional monotonicity, or any power-analysis assumptions.
