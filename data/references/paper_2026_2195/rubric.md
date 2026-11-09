# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Lower-bound instance and admissibility (3 points).** Constructs hard objectives and fidelity families under a common admissible cost/selection mechanism. Verifies an attained optimizer, local smoothness, the near-optimal-cell count with the stated C restriction, and fidelity-class membership. An infinite branch alone does not establish an attained maximum on an arbitrary partition; a finite-prefix construction completed along an actual point is sufficient.
2. **Information limitation and regime inversion (2 points).** Establishes valid adaptive first-hit or equivalent indistinguishability arguments, accounts for an arbitrary output rather than only queried recommendations, and derives all five lower rates. Constants and budget thresholds must be independent of the policy. Lower bounds are existential over admissible cost/fidelity instances, not universal instancewise lower bounds.
3. **Adaptive algorithm analysis (3 points).** Accounts for paid child evaluations at all activated levels, initialization, every validation candidate, skipped operations, and the zero-internal-budget case. Establishes the depth/fidelity guarantee using same-fidelity raw rankings and existential increasing calibrations only in the analysis. Uses the candidate set of evaluated cells and a correct near-optimal-cell counting contradiction.
4. **Parameter choices and matching upper rates (2 points).** Verifies appropriate depth/fidelity choices and obtains all five displayed upper rates. Retains logarithms contributed by Lambert-W inversion. Addresses sufficiently large budgets and the remaining budget-feasibility cases; explicit low-budget regret formulas are welcome but not required by the public asymptotic target. Establishes adaptation to all unknown parameters.

# Evaluator Notes

Accept any complete valid alternative proof, including stronger upper bounds. Do not require the reference proof's incidental tree notation, exact constants, or use of Lambert W. Lower- and upper-bound exponential constants need not agree. The algorithm observes raw F_z values, not the numerical calibrated values. A proof may nevertheless apply an unknown increasing calibration to a same-fidelity comparison in its analysis.

The public bounds hold for all sufficiently large budgets with fixed class parameters. Do not require the displayed asymptotic rates at B=1 or with zero internal budget. Budget feasibility itself is required for every B>=1.

A missing regime, unproved central width/depth argument, failure to establish an attained optimizer, omission of essential evaluation costs, or reliance on an unsupported log-squared upper rate is a substantive gap. Do not award completion credit merely for citing the source's paper-specific lemmas. No unresolved reference-proof obligation is being treated as an accepted premise.
