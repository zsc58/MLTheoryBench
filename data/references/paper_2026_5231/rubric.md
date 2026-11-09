# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives the weight transform, with valid interchange or inversion arguments, and uses the fixed-drift first-passage law to prove conditional unbiasedness, unconditional unbiasedness, and uniqueness in the stated absolutely integrable smooth class. Justifies absolute integrability and handles zero drift without dividing by zero. The uniqueness argument must use the fixed-drift experiments, not only drifts in the population support.
- **2 points:** Correctly obtains the bounded-drift high-Laplace population expansion, including the nonzero one-scale lambda^(-1/2) bias and cancellation of its constant term in the two-scale expression. Does not assume the second weighted drift moment is positive or incorrectly demand a matching lower bound for the two-scale bias.
- **2 points:** Validly controls empirical transforms at both Laplace scales under sqrt(lambda_n)=o(log n), takes logarithms correctly, and proves consistency of both boundary estimators. Recognizes that the sample transforms are positive and the two-scale boundary estimate is positive, so the plug-in weight is defined. A direct second-moment or Chebyshev argument is sufficient; a triangular-array CLT is not required.
- **3 points:** Establishes continuity and a compact-uniform integrable envelope for the weight family, with justified control near zero and away from zero, then combines a uniform law or local-modulus argument with boundary consistency to prove same-sample plug-in consistency. Any specialized spectral or transformed-series identity needed for the argument must be derived or adequately justified rather than treated as a public assumption.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that merely asserts a specialized tail estimate, bias cancellation, or uniform-envelope argument without deriving or adequately justifying it does not earn the associated core-step credit.

The public weight is defined by its image-series ratio. The spectral representations in the reference proof are private supporting derivations, not additional public conclusions that must independently be reproduced if an alternative argument closes the same obligations.

Ordinary termwise Laplace integration of the spectral series for the numerator is invalid: the resulting summands do not tend to zero. A justified regularization or a justified transform of the image series is acceptable. With h_c(t)=c exp(-c^2/(2t))/(sqrt(2*pi)t^(3/2)), the correct inverse transform of sqrt(2s)exp(-c sqrt(2s)) is -partial_c h_c, not its negative.

Do not replace the universal integrability requirement on a competing weight by 'wherever its expectation exists'; that permits vacuous competitors. Zero drift supplies an integrability condition but its signed unbiasedness identity alone imposes no identification restriction.

The bias comparisons concern the stated population transforms, not expectations or mean-square errors of empirical estimators. Degenerate bounded drift laws, including D=0 almost surely, are allowed. Independence between the plug-in boundary estimate and the observations is neither assumed nor necessary.
