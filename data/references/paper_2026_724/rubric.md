# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Sobolev generator and ReLU representation (2 points).** Select a near-minimizing H^s velocity generating Φ and establish action-controlled flow regularity. Supply an integrable normalized width-one ReLU representation with the required divergence identity and measurable dependence. Verify the domain on which the representation is valid and track any dependence of its cost on an action-dependent spatial domain. A specialized embedding citation without the relevant statement, verified hypotheses, and the quantitative properties actually used does not close this obligation. The reference proof derives the needed representation by a Fourier/Taylor identity; another justified representation is acceptable.

2. **Independent time sampling and flow approximation (3 points).** Specify cost-weighted interval laws and output-weight rescaling, including zero-cost intervals, to obtain a piecewise-constant width-one field. Prove conditional centering and variance bounds, control the within-interval remainders, and derive a terminal L² map-error rate of order m^{-1/2} with constants compatible with the public action-dependent bound. A remainder depending on the current sample cannot be treated as measurable with respect to preceding samples. An argument using a local representation must justify every evaluation, rather than assuming sampled-path containment. Naming sampling or Gronwall without closing these estimates earns little credit.

3. **Coupled log-Jacobian estimate (3 points).** Justify the almost-everywhere Jacobian calculation for ReLU flows. Use activation-sign invariance on each constant-control interval, or another valid mechanism, to obtain the exact sampled log-Jacobian increment. Establish the centered divergence fluctuation and control the drift and exact-flow remainder using the map error. Close an m^{-1/2} log-Jacobian estimate with the required quantitative constants. The reference proof uses martingale orthogonality and Minkowski's inequality; an equivalent valid energy recursion is acceptable.

4. **Deterministic realization, TV transfer, and rate (2 points).** Select one realization satisfying both errors, justify the inverse-displacement and composition log-determinant estimates, and establish global TV control for the compactly supported Lipschitz density. Account for mass outside the original support; the full change-of-variables integral does not generally reduce to that support. Choose the number of intervals, track action-dependent constants, and handle rounding and zero action to obtain the stated switch bound and both ε inequalities.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's particular representation, auxiliary domain, interval threshold, or use of a stronger TV estimate. Correctly stated and applicable standard independent results may be used. Neither a named specialized method nor the source's unproved sampled-path assertion is a substitute for the quantitative obligations actually needed.

The source uses the full variation norm, not half that norm; a proof using the other convention is acceptable if the factor of two is accounted for. ReLU terminal maps are generally bi-Lipschitz and piecewise affine, not C¹ everywhere, so almost-everywhere derivatives and a justified change-of-variables formula suffice.

A local algebraic inequality error or an omitted elementary endpoint case is readily repairable. Missing the Jacobian mechanism, unjustified spatial evaluations, loss of the required action dependence, or failure to justify global TV transfer is theorem-critical. The reference proof contains no unresolved obligation; do not award a completed rubric step merely because an invalid source inference is repeated.
