# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines the per-group cumulative coverage errors and derives the wealth/parameter identity, including the expression for total wealth. Justifies the nonnegativity needed to compare individual and total wealth and the positivity needed when taking logarithms.
- **3 points:** Applies a quantitatively correct finite-horizon Jeffreys-mixture comparison to the specified update and return domain. Derives the weighted comparator lower bound and obtains A_j^2/[2n_j alpha(1-alpha)+(2/3)|A_j|], or a sufficient alternative bound. The weighted Bernoulli argument must remain valid when either weighted outcome count vanishes.
- **2 points:** Proves the total-wealth upper bound by a valid exhaustive case analysis or equivalent argument, including zero scores and threshold equality, and uses the polynomial score-growth assumption to obtain B_T.
- **3 points:** Compares the bounds, obtains the logarithmic quantity U_T(k), validly solves or bounds the resulting quadratic for each cumulative group error, and divides by the positive group count to conclude the stated rate at every admissible horizon.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the particular case ordering, notation, or presentation used in the reference proof. Standard independent quantitative results, including the portfolio comparison and Bernoulli KL lower bound, may be invoked when their relevant statements are given and their hypotheses are checked; reproving them is not mandatory. A method name alone without the quantitative comparison and its valid application is insufficient for the portfolio lower-bound step.

The stream and return sequence may be adaptive: no independence assumption is available or needed. The predictor function is based on past data, but its evaluated prediction may use the current feature. Group memberships may be fractional or zero, individual asset returns may vanish, and one of the weighted outcome counts may be zero. Do not demand positive counts at earlier horizons or a positive limiting group frequency. Routine endpoint conventions or readily repaired omissions should be assessed according to their mathematical impact, rather than automatically treated as a failure of the entire proof.
