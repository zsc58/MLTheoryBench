# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (3 points):** Establish the strict-local bias lower bound. For fixed i and u, use strictness to show the same G_i(u) is used for all compatible global states, apply the triangle inequality to two such states, take suprema, and derive E_i(u) >= Delta_i(u)/2.
- **Step 2 (4 points):** Use overlapping-read compatibility and unique ownership to derive the coordinatewise lifted-operator identity and hence the vector equation (1/m) sum_i tilde T_i(x) = (1-1/m)x + (1/m)bar F(x).
- **Step 3 (3 points):** Correctly deduce that fixed points of the averaged lifted operator are exactly fixed points of bar F by algebraic cancellation, including both directions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the strict-bias argument or the overlapping-read averaging identity as theorem-critical gaps; merely naming locality, averaging, or triangle inequality earns no credit for the corresponding step.
