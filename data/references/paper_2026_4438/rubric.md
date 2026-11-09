# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Constructs two positive finite empirical normalized spectral laws with identical observations at every node in \(\mathcal T\) and unequal logarithmic moments. This must actually preserve empirical realizability, mass, mean, and all required moments, while establishing a nonzero logarithmic discrepancy.
- **3 points:** Constructs and analyzes a sequence of admissible normalized empirical spectral laws, correctly showing convergence of every observed \(K(t_j)\) and divergence of \(K'(0)\) to \(-\infty\). A two-point sequence is sufficient but is not required.
- **3 points:** Correctly applies continuity of an arbitrary estimator at the limiting observation vector and concludes divergence of absolute error and hence unbounded worst-case error; also establishes the equal-observation, unequal-target non-identifiability assertion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its specific number of atoms, its local-solvability argument, or its two-point saturation construction.

The empirical-law requirement is substantive: each law must be uniform over a finite list, allowing repeated values. Equivalently, its distinct atoms have positive rational weights. Arbitrary real weights are not sufficient without a valid exact realization argument. Merely approximating weights by rational numbers does not preserve exact moment matching and therefore does not complete the first part.

A construction that asserts moment matching without proving simultaneous mass, mean, and empirical-realizability constraints, or that does not establish a differing logarithmic moment, cannot receive full first-step credit. A null vector for a location Jacobian alone establishes only first-order matching; a local perturbation proof must justify exact matching, as the reference proof does by local solvability.

Continuity must be used at the limiting observation vector, which belongs to the estimator's stipulated domain \(\mathbb R^m\), even if it is not realized by an admissible positive law. A merely informal conditioning argument does not establish the final conclusion.

The task includes the redundant observation node 1 and, under the ordinary meaning of a finite set, the empty node set. A proof that already works for these cases need not discuss them separately. No prescribed common dimension is required by the task; the reference proof happens to give the equal-observation pair in a common finite dimension.
