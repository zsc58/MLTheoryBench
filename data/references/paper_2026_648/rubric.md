# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Represents the wedge error as independent centered symmetric summands, including diagonal wedges; proves unbiasedness and the incoherence consequences; derives a summand bound of order μ1μ2r²||A||²/(pmn) and variance bound of order μ1μ2r²||A||⁴/(pmn); and obtains the operator concentration rate by Bernstein.
- **1 point:** Uses the population gap and concentration to prove the stated operator-norm subspace estimate with a Frobenius Procrustes minimizer. Handles r=n directly or otherwise avoids invoking an undefined eigenvalue. A valid Frobenius estimate that implies the requested operator bound is acceptable, but an operator estimate and a Frobenius estimate with an extra √r are not interchangeable.
- **3 points:** Proves the claimed κ² row-wise rate by a genuine argument controlling dependence. For the reference route, retain AA^T in the centered leave-one-out matrix, verify conditional Bernstein estimates for incident wedges, compare the full and leave-one-out bases, and explicitly close the row-wise inequality. The projected eigenvector equation and the second-order parallel alignment term provide one valid closure. Merely naming leave-one-out or asserting an unsupported absorption inequality does not earn these points. A κ^4 rate does not prove the requested κ² rate.
- **2 points:** Establishes projector delocalization and controls independent denoising noise conditional on the wedge samples. Derives summand and variance bounds, applies Bernstein with the appropriate dimension logarithm, converts operator to Frobenius norm using rank at most r, and absorbs the linear term using the stated lower bound on q. Tracks the explicit 2^k dependence rather than hiding an arbitrary constant raised to k.
- **2 points:** Uses a correct multilinear telescoping or equivalent contraction argument to bound projection bias, exploits tensor symmetry appropriately, combines bias and noise, and gives the stated final Frobenius rate on the same event as both subspace bounds with probability at least 1−cn^−a.

# Evaluator Notes

Accept a complete valid alternative proof; do not require the reference proof's incidental presentation choices. All theorem-critical obligations in the repaired reference proof are closed.

A missing dependence argument or unsupported row-wise closure is theorem-critical. Propagate such a failure to any recovery step that relies on the unproved projector bound, but award independently correct concentration, operator perturbation, bias, or conditional denoising calculations.

Do not accept the source's invalid fixed-matrix variance substitution ||F||_{2,∞}≈||F||_F/√n without additional justification. A sufficient valid estimate bounds incident-row variance by a constant times μ1μ2r²||A||⁴||F||_{2,∞}²/(pmn).

For Procrustes alignment, the operator projector distance equals the largest principal-angle sine, not its square. The aligned basis error is first order in this sine, whereas the polar-factor and parallel-component errors are second order. Frobenius identities have different normalization factors.

Conditional projected-noise failure is at most n^{−a(k−1)}. After substituting a high-probability wedge-projector bound, include the wedge failure probability as well. A row-wise union bound requires a suitably increased confidence parameter; using a+O(1) is harmless for a≥2.

The full-rank case r=n has Q=I and exact aligned subspace recovery. The endpoints p=1 and q=1 are permitted. Infeasible lower sampling bounds make the theorem's implication vacuous. Do not add CP-factor assumptions, assume bounded κ, replace ordered entry sampling by symmetry-orbit sampling, or otherwise narrow the public contract.
