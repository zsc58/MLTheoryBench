# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Ellipsoidal projection/lifting and decision preservation (3 points).** Derive the canonical lift, verify uniqueness and feasibility for projected coordinates, and use set-valued global sufficiency to preserve the selected decision and its SPO loss for every true cost. Map each C-valued fixed-intercept predictor to the compressed class, use the reverse class inclusion, and prove equality of risk infima without assuming attainment. Handle an empty sufficient span.
2. **Intrinsic-dimension generalization (2 points).** Embed scores b c0+L_U Bz in a fixed-feature multiclass linear class of dimension d_star p+1. State a valid Natarajan-dimension result and the finite-label SPO inequality, verify their hypotheses, and obtain the exact requested bound, including K and both deviation terms. A correct alternative proof of that inequality is equally acceptable. Do not award completion for the previous unsupported label-independent inequality or an arbitrary-intercept parameter count.
3. **OLS representation control (2 points).** Use the iid centered regression model, bounded contexts, population covariance, and conditional subgaussian noise. Establish the empirical Gram-matrix lower bound with failure probability at most delta_mu/2. Bound normalized noise, union over responses, and derive the Frobenius and uniform prediction radius with constant 4sqrt(2), using the stated sample-size condition.
4. **Compression-to-decision transfer (3 points).** Establish cumulative certification, independent relevant queries, reconstruction, and deletion stability. Justify |T|<=d_star under the closed ellipsoid; an unexplained invocation of an open-prior necessity characterization does not suffice. Conditional on the regression sample, apply a correctly stated stable-compression theorem to the iid fresh pseudo-costs. Use C-valuedness, pointwise sufficiency, regression accuracy, the mean margin, and almost-sure uniqueness of the lifted optimum to bound the specifically defined candidate's disagreement. Convert that bound to learned-class excess risk by conditional expectation, candidate membership, Bayes optimality, and comparison of infima. Combine regression and discovery confidence events correctly.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Standard independent learning and concentration results may be invoked when the relevant mathematical statement is supplied and its hypotheses are checked; a named specialized method alone is insufficient.

Treat omission of projection/lifting, the correct compressed complexity and generalization step, conditional pseudo-cost sampling, or the margin-transfer argument as theorem-critical gaps. Pointwise sufficiency only supplies a common optimizer; it does not by itself equate tie-broken decisions at a nonunique lifted optimum.

The disagreement target concerns tilde_mu, not every population risk minimizer. Excess-risk optimality does not imply the same disagreement bound. The unconditional learned-class claim is about its risk infimum; a minimizer inherits it when attained. Do not require an unsupported existence proof for a minimizer.

Check boundary cases proportionately: empty query spans, vacuous facet tests for a singleton polytope, and r=0. For r=0, exact regression and a limit eta down to zero close the transfer argument. Minor omitted routine cases can be scored at 8-9 when the central proof is complete. No theorem-critical reference-proof obligation is left unresolved.
