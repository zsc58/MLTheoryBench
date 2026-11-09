# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the graph-compatible correlation constraints and PSD inner-product nonnegativity to derive the inequality k - 2 alpha sum_edges X_e >= 0 for a valid PSD certificate with common edge value -alpha.
- **2 points:** Constructs and verifies the even-cycle certificate from alternating unit vectors, including the wrap-around edge, and obtains the bound 1/2.
- **4 points:** Constructs and verifies the odd-cycle planar certificate with theta = (k-1)pi/k, checks both ordinary and wrap-around edge inner products, and obtains 1/(2 cos(pi/k)).
- **2 points:** States the bounds for all cycle-compatible matrices and correctly concludes emptiness of the mean-threshold feasible set when t exceeds the corresponding parity-dependent ceiling.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
