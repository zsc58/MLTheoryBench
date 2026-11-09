# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes that the specified conditional finite-moment domain is Borel and has full measure; proves its independence of the reference point, at least up to a null set; establishes finite continuous coercive conditional objectives with nonempty compact argmin sets; proves value measurability and validly obtains a Borel measurable minimizer selector on the whole manifold. A precise applicable selection or measurable optimization theorem with verified hypotheses is acceptable. Compact values alone do not establish the measurability needed for selection.
- **2 points:** Establishes finiteness of the integrated value, uses disintegration and pointwise minimality to prove the attained infimum identity, and correctly characterizes all minimizing Borel maps by conditional argmin membership. Handles exceptional conditional laws and potentially infinite competing losses without using undefined values or subtracting two infinities.
- **3 points:** Proves that zero integrated defect is equivalent to almost-sure zero conditional defect and derives that the conditional laws are Dirac measures for a Borel map, including the resulting map-induced representation.
- **2 points:** Proves the converse from a map-induced coupling, including identification of its conditional kernel and vanishing defect, thereby completing all four equivalences.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular compact-ball verification of weak measurability. A correctly stated standard selection theorem may be used without proving that theorem, provided its relevant hypotheses are established.

The source-variable selection domain is a Borel measurable space; it need not be Polish in its inherited topology. A merely universally measurable or completed-measure-measurable selector is not automatically the Borel map requested, but a valid Borel modification argument is acceptable.

Conditional objectives are defined publicly only on X_0. Integrating over X_0, or explicitly giving a suitable measurable extension before integrating over N, is acceptable. Exceptional sets do not justify an arbitrary non-Borel extension of a selector. The basepoint assertion follows from the two triangle-inequality moment comparisons and is scored within the first core step, not as an additional target with extra points.

The coupling need not be optimal. Curvature assumptions and uniqueness of general conditional minimizers are not required. Competing maps need not push mu to nu and need not be assumed to have finite loss. Do not require the second-moment conclusion for the selected pushforward, a tangential construction, a quantitative energy gap, or any other result outside the public task.
