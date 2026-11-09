# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive the exact affine coefficient and velocity identities for the mixed ridge estimator from linearity in the response matrix, including the definitions of the pure-distilled and mixed fits. The ridge inverse is well defined for lambda>0 without a full-rank design assumption.
- **4 points:** Express the integrated student risk as the quadratic R - 2 xi (R - C) + xi^2 D, complete the square under D>0, and obtain the unique minimizer and exact risk reduction. The quadratic identity itself must not require D>0.
- **3 points:** Differentiate the ridge solution while holding the training data, feature map, and test law fixed; prove the teacher-to-pure-distillation direction identity; justify the risk derivative using the explicit moment assumptions; relate R - C to -(lambda/2)R'(lambda); and conclude the derivative formula, strict improvement when R' is nonzero, and the opposite-sign rule.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The score must reflect whether the affine ridge geometry, quadratic optimization, and derivative/sign mechanism are actually derived rather than merely named. Propagate a missing affine identity to later claims only when those claims are unsupported without it; independently valid quadratic or derivative arguments receive credit for what they establish.

The finite second moments make all displayed risks and cross terms finite. A finite moment-matrix expansion, a justified dominated differentiation argument, or an equivalent square-integrable argument is acceptable for the risk derivative. Scalar differentiability alone is not a justification for exchanging expectation and differentiation; a readily repairable omission of the justification belongs in the 8-9 range when the rest of the proof is complete.

No formula involving division by D and no uniqueness claim is required when D=0. A proof of the quadratic expansion that also covers D=0 suffices for that case; the additional degeneracy discussion in the reference proof is not a separate scoring requirement. Do not require any result about training-sample averages, generation error, ODEs, GCV, or time-dependent mixing.
