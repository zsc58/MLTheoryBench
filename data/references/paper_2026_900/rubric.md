# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the needed resolvent properties, characteristic-root ordering, and continuation equation. Justifies finiteness and growth using the positive discount and the geometric-Brownian moment exponent. Derives or adequately justifies regularity, the resolvent ODE, and monotonicity; correctly removes the increasing characteristic power when using the ODE construction.
- **4 points:** Establishes the stated boundary, coefficient, piecewise value, and optimal reflected control. Handles the capped inverse and coefficient endpoint; verifies matching at positive fuel, the gradient constraint, and the stopping-region HJB inequality. Gives a valid verification argument for all admissible cadlag controls, including jump increments and possible initial depletion, localization, discounted terminal decay, and zero fuel. Shows equality for the reflected policy. A mere reference to Ito-Meyer verification does not close these obligations.
- **2 points:** Proves that the classical boundary equation has exactly one finite positive solution and identifies it with an optimal lower hitting threshold for the defined classical stopping problem. Establishes the monotonicity and endpoint range facts needed for the inverse boundary equation. A correctly stated independent stopping verification result may be used if its hypotheses are checked.
- **2 points:** Establishes the regularized inverse equation and proves pointwise convergence for every fixed y in (0,1], including the cap endpoint y=1 and eventual membership of y in the inverse's domain. Continuity of a strictly increasing inverse is sufficient; no uniform convergence in y is requested.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its auxiliary notation. Because the formulas are supplied in the task, directly verifying them is as acceptable as deriving them first.

The central construction and verification are theorem-critical. In particular, do not award full verification credit for omitting all jump terms, assuming global smoothness at y=0, or asserting terminal decay without an applicable estimate. Conversely, do not require differentiability at y=0: the entropy term prevents it, and truncation or an equivalent endpoint argument is valid.

The source's printed sign directions are not grading requirements. The correct statements are 1+log y>=0 for y>=e^{-1} and <=0 for y<=e^{-1}; as a function of lambda, b_lambda(y) is respectively nondecreasing and nonincreasing on its domain. These comparisons are optional if the limit is proved directly.

The current reference proof closes all its critical obligations. Its classical-threshold verification does not depend on an unspecified specialized theorem, and no private proof gap is to be treated as a completed scoring step.
