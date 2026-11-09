# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes marginal coverage by applying split-conformal validity at level `q/p` and multiplying by the independent non-null probability `p`. Also establishes the conditional statement under its additional premise by the analogous conditional calculation.
- **2 points:** Correctly computes `E|T_{p,q}(X)|=pG(q/p)` using the zero length of the singleton branch and identifies the base expected length as `G(q)`.
- **4 points:** Resolves the central parameter-selection argument: introduces an equivalent normalization such as `H(u)=G(u)/u`, derives `H'(q)=[qG'(q)-G(q)]/q^2<0`, and rigorously obtains some `u>q` with `H(u)<H(q)`, or proves the equivalent strict improvement directly as a function of p.
- **1 point:** Sets `p=q/u`, verifies `p in (q,1)`, and converts the normalized inequality into the required strict expected-length comparison for a deterministic parameter that also has the proved coverage guarantees. An equivalent direct parameter-selection argument earns the same credit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Merely asserting that the derivative condition permits a suitable parameter, without establishing the relevant strict length comparison, does not earn the central four points. If conditional coverage is omitted but marginal coverage is correct, award partial credit for the first step. Do not deduct for ignoring possible extra coverage from the singleton branch, since only a lower bound is needed.

The standard split-conformal coverage theorem may be invoked rather than reproved: its fitted-score exchangeability hypotheses and corrected quantile convention are explicit in the task. A rank proof is also acceptable. Such a proof must allow ties and the `+infinity` threshold when the corrected index is n+1. Do not require continuity of the response or scores.

The chosen parameter is deterministic relative to the probability experiment. A proof that chooses p from the realized calibration data and then invokes fixed-level coverage without further justification is not complete. Ordinary differentiability is needed only locally at q; do not require finite expected lengths at every coverage level or differentiation under an expectation.
