# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles interpolation on the scaled unisolvent design, the extrapolation functional, and the relevant infinity norms. Justifies the interpolation and design-stability facts needed by the chosen proof; in the reference route these include the Lagrange representation and scaling identity for the Lebesgue value. Repeating definitions already supplied in the task is not required.
- **3 points:** Proves the exact-data bound with the stated order h^n and all stated parameter dependencies. The reference route differentiates the SPD resolvent, applies the spectral bound and Taylor remainder, and propagates the residual through interpolation with the factor 1+lambda_ref. An alternative valid derivation, including a stronger estimate implying the target, earns the same credit.
- **3 points:** Proves the perturbation estimate for arbitrary prescribed nodal values, using the maximum coordinatewise sampled discrepancy and coefficient lambda_ref. The nodal Lagrange formula is one valid route; continuity of numerical data must not be imposed as an extra hypothesis.
- **2 points:** Combines the exact and perturbation estimates into the total accuracy-stability bound with all parameter dependencies and quantifiers correct.

# Evaluator Notes

Accept a complete valid alternative proof and allocate credit for equivalent mathematical accomplishments rather than requiring the reference proof's particular intermediate formulas or presentation. Failure to establish the exact-data inequality or the perturbation inequality, or a valid stronger statement implying it, is a theorem-critical gap. Omission of Taylor expansion, resolvent differentiation, or a separately named Lebesgue-operator argument is not itself a gap when another valid argument establishes the required bound.

The theorem uses the monomial space P_n. Do not accept an unsupported assertion that arbitrary polynomial spaces preserve unisolvency or extrapolation weights under dilation. A brief correct argument for the specified monomial space is sufficient.

The proof must cover the permitted cases n=1, b=0, a reference design containing zero, sigma_max=0, and h=1. A separate case split is unnecessary when the argument already applies. The case h=0 is not required. No direct-solver error model or claim about rounding in the interpolation computation is part of the task.
