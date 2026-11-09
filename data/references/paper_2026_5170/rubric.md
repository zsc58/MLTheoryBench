# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derive $\|L-\widetilde L\|_2\leq\varepsilon B_L$ from the Loewner spectral-sparsifier inequalities and symmetry.
- **2 points:** Prove the polynomial-filter perturbation bound $\|p_k(L)-p_k(\widetilde L)\|_2\leq C_k\varepsilon$ using the matrix-power telescoping identity or an equally valid argument, with finite coefficient-dependent constants. The argument must not assume that $L$ and $\widetilde L$ commute.
- **4 points:** Establish uniform forward bounds and correctly derive and solve the nonlinear layerwise recursion to obtain $\|Z-\widetilde Z\|_F=O(\varepsilon)$, with constants allowed to depend on the fixed dimensions and architecture, polynomial coefficients, activation Lipschitz constants and offsets, and $B_X,B_W,B_L$. Do not assume that the activations vanish at zero.
- **2 points:** Factor the Gram difference or use an equivalent valid argument and apply the embedding bounds to prove both operator- and Frobenius-norm $O(\varepsilon)$ estimates with admissible constants independent of $\varepsilon$.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A named method without the corresponding inequalities and recursion does not earn the associated points. The final score is capped below full credit when either norm bound or the nonlinear propagation step is absent.

The reference proof includes the source-internal induction establishing the matrix-power identity. A solver may invoke that elementary identity in its correct noncommutative form; reproducing the reference induction is not independently required for full credit.

Intermediate bounds and perturbation coefficients are allowed to be zero, including for constant filters, zero inputs, zero weights, or constant activations. An explicit final choice must meet the task's strict positivity requirement; any nonnegative valid bound can be enlarged, for example by adding one. A zero explicit final witness without this enlargement is a readily repairable constant-choice error, not a counterexample to the theorem. Do not require strictly positive inputs, nonzero embeddings, or division by perturbation or recursion coefficients.

The targets are absolute Gram-matrix bounds. Do not require relative-error, normalized-geometry, class-statistics, or training-dynamics claims.
