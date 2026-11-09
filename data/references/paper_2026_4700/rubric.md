# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the lower bound from a shattered improvement tree, including the stay and move cases. Explains why movement implies a nonminimal prediction and why an available edge forces a mistake. Establishes realizability by one fixed hypothesis for the completed finite transcript; deterministic simulation and replay, or an equivalent argument, is sufficient.
- **3 points:** Proves the trichotomy for nonempty finite-dimensional version spaces. Uses restriction monotonicity and failure of the three alternatives to select the required full-dimension restrictions, attaches their depth-\(D\) trees, and verifies that the resulting tree is shattered and has depth \(D+1\). Finite-depth attainment and any required truncation must be justified or correctly implicit in the argument. No bounded-degree assumption may be introduced.
- **3 points:** Analyzes the learner's applicable cases under strict-improvement best response. Shows that the selected point is the realized destination, or that the agent stays as appropriate, and that each mistaken label yields a restriction of strictly smaller dimension. Uses the observed final-feature/label pair only on mistakes and does not require pair feedback on correct rounds. Establishes that the finite-dimensional rule never needs its fallback.
- **2 points:** Preserves a nonempty version space containing the fixed target, counts at most \(\operatorname{IDim}(H)\) mistakes in the finite case, and combines both bounds for exact optimality. Correctly includes zero dimension and the one-label case, whether explicitly or through an argument that covers them. For infinite dimension, proves the absence of any finite uniform worst-case bound and explains why deterministic totalization is optimal.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A named method without the corresponding dimension-decrease derivation does not earn the central-step credit.

The maintained version space need only agree with revealed mistake pairs; the source learner does not update it on correct rounds. A proof must not rely on observing final-feature/label pairs on correct rounds. It may ignore information that is legitimately available.

The convention \(\operatorname{IDim}(\varnothing)=-1\) applies to empty restrictions, not to encountered realizable version spaces. At \(D=0\), nonemptiness rules out any further mistaken update. When \(k=1\), the first prediction condition cannot occur, all predictions are correct, and the dimension is zero; an equivalent argument covering this case is acceptable.

For the lower bound, a branch witness may depend on the learner and the desired finite number of mistakes. Do not require one hypothesis or one infinite play to witness all finite lower bounds simultaneously. Conversely, consistency of isolated rounds with potentially unrelated hypotheses is not enough unless the argument supplies a witness for the entire constructed finite branch.

Improvement trees may have infinitely many children but use finite-height witnesses. Do not require the entire tree to have finitely many nodes or impose a finite neighborhood bound. The empty-instance case is immediate from the definitions and need not receive a separate paragraph if the proof already covers it.

The finite trichotomy must not be asserted at infinite dimension. The fallback is part of a deterministic total prediction rule; its unrestricted worst-case value at infinite initial dimension follows from the lower bound, not from an invalid \(\infty+1>\infty\) argument.

Minor omissions that are genuinely routine should be evaluated under the 8-9 band rather than treated as failure of the whole proof. No proof obligation in this rubric is being credited merely by citation to an unresolved source dependency.
