# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

## Reference-proof status

The recovery omission identified in revision 2 has been closed. The reference now proves a uniform Gaussian lower measurement bound on the relevant nuclear/Frobenius cone, using Gaussian moments, explicitly stated standard empirical-process inequalities, and an independently derived signed-covariance norm estimate. It then applies the deterministic feasibility and cone reductions to the exact known-cap estimator. No specialized recovery citation is treated as sufficient by itself.

This is one valid proof route, not an extra assumption or a mandatory solver method. In particular, feasibility, trace minimality, and the cone restriction alone still do not establish recovery. Poorly informative designs may occur and must be excluded probabilistically.

## Core Steps

1. **Recovery and probability event — 2 points.** Derive the rescaled measurements, use the stated known-cap PSD trace program, and justify an error bound of the form \(\|\widehat A-A\|_*\le K_d\bar\eta/\gamma^2\) on an appropriate high-probability design event at the stated rank-aware sample size. A coefficient-one bound is not required. A correct specialized theorem may be used if its relevant statement and application are justified; merely naming recovery theory does not close the step. The proof must control every selected minimizer and the admissible feedback vectors on the relevant design event. The known-cap program must not be confused with a program constrained by the realized noise norm. Control any additional probe-energy event needed for conditional-on-design regret.

2. **Phase costs, replay, and comparator — 2 points.** Establish or validly invoke the optimal causal comparator characterization. Bound exploration costs in the correct probability/expectation mode. Account for the replay, actual first exploitation switching cost, and suffix initial-state contribution. Do not apply a positive-definite whole-space contraction bound to the kernel of a singular matrix.

3. **Rank-sensitive exploitation control — 4 points.** Derive a valid quadratic-cost or regret identity with its boundary terms and conditioning. Obtain singular-regime control of order \(\varepsilon^2n^2+\sqrt\varepsilon n+\varepsilon n\) and full-rank control of order \(\varepsilon n\), with appropriate initial-state contributions, or establish alternative bounds sufficient for the same final rates. The reference uses estimated high/low spectral blocks; a complete valid alternative is equally acceptable. An unsupported bound on complete eigenbases from the positive-to-zero spectral gap is not valid, including after correcting the Frobenius/nuclear norm inequality. Handle the learned estimate's dependence on the exploration history and use only the stated covariance assumption.

4. **Balancing, parameter domain, and both rates — 2 points.** Substitute the prescribed \(m\) and \(\gamma\), retain recovery constants and the factor \(\sqrt{\bar\eta}\), and obtain both rates with the declared parameter dependencies. If the proof uses a perturbative error threshold, cover the bounded complementary remaining-horizon range without adding a public small-noise assumption or changing gamma. Combine probability events correctly, with universal exploration and exponent constants.

## Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. Do not require the reference's notation, decomposition labels, ordering, cutoff function, or recovery proof technique. In particular, a valid proof need not explicitly compare eigenbases. Omission of a rank regime, the conditional probability/expectation interpretation, a necessary boundary contribution, or a theorem-critical recovery or exploitation justification is a substantive gap. Do not require literal coefficients from the unrepaired source calculations. A positive-probability bad-design example is not a counterexample to a high-probability theorem unless its probability and consequences contradict the actual quantified guarantee.
