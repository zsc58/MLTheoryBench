# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(3 points)** Derives the componentwise one-block Wasserstein inequality from fixed-center Fisher-smoothness, the fixed-point identity, and the transportation-information inequality, with R_ij=L_ij/lambda_i. The application of TI is justified because the smoothness bound makes the update's relative Fisher information finite and therefore ensures absolute continuity with respect to the fixed-point marginal.
2. **(2 points)** Establishes invariance of the prescribed sub-eigenvector-scaled product ball, explaining why each update remains in the domain of the assumptions. This must hold pathwise for random scan and at every intermediate state of a sequential sweep. Do not require delta to be an eigenvector or require irreducibility.
3. **(2 points)** Proves the parallel recurrence and the conditional uniform random-scan recurrence. Iterates them to obtain e_k<=R^k e_0 and E e_k<=A^k e_0, and establishes rho(A)=(M-1+rho(R))/M<1 or another valid argument sufficient for the claimed spectral-rate bound.
4. **(2 points)** Performs the within-sweep induction, obtains (I_M-R_L)e_{k+1}<=R_U e_k, and uses the nonnegative inverse of I_M-R_L to obtain G. Proves rho(G)<1 by the applicable Stein-Rosenberg implication or a valid direct argument. An argument using delta-G delta=(I_M-R_L)^(-1)(delta-R delta)>0 and a weighted norm is fully acceptable.
5. **(1 point)** Converts the matrix recurrences into exponential bounds for every rate strictly above the relevant spectral radius. For random scan, controls E||e_k||, not merely ||E e_k||; nonnegativity and the l1 norm give this directly. Handles arbitrary fixed norms by norm comparison and interprets the spectral rate as a limsup upper bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or invocation of a named matrix theorem when the needed implication is proved directly. Award partial credit for any correctly established schedule recurrence; do not award full credit if the sequential induction, invariant-region argument, or random-scan expectation is absent or merely asserted.

Only smoothness relative to the fixed-point input is assumed. A proof must not introduce pairwise smoothness between arbitrary points of U as an additional hypothesis. The positive vector delta is provided; proving its existence is not a separate scoring requirement. It is not generally valid to replace R delta<=q delta by R delta=rho(R)delta.

The asymptotic spectral rates are upper bounds, not necessarily exact trajectory rates. Do not demand a bound with base exactly equal to the spectral radius; polynomial factors can occur for nontrivial Jordan blocks. Reducible matrices, zero spectral radius, and zero initial error are included. Routine omitted norm-comparison details may warrant only a minor deduction, but using Jensen's inequality in the wrong direction to infer expected-norm convergence is not a valid argument.
