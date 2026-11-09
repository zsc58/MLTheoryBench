# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Gaussian posterior decomposition and component formulas (2 points).** Derive the conditional Gaussian mean and covariance and show that posterior component likelihood ratios are prior-weight ratios times \(\exp[-(q_j-q_{j_0})]\). Posterior inference conditions on the known realized \(A\); the Bayesian component label is not the fixed true label in the data-generating experiment.
2. **Random-inpainting score-gap concentration (3 points).** Use sampling-without-replacement concentration for observed mean separation and conditional Gaussian concentration for the noise cross-term, with a union bound, to obtain the stated probability and gap \(\bar\delta=\Delta/[8(\sigma^2+\tau^2)]\). Full credit requires the displayed probability guarantee with denominator \(512(\sigma^2+\tau^2)\), or a valid stronger guarantee that implies it. A valid weaker guarantee alone receives only partial credit unless additional reasoning establishes the requested bound. Standard concentration inequalities may be invoked with their relevant hypotheses checked; they need not be reproved. Bounds must remain valid for zero projected separation and for \(m=n\).
3. **Posterior selection and exponential nonbest mass (3 points).** Combine the positive gap with bounded prior-weight ratios to prove \(\Pr(J\ne j_0\mid y)\le CM e^{-m\bar\delta}\) (or an equivalent sharper bound), for every observation and realized operator satisfying the stated gap and minimizer conditions.
4. **Total-variation collapse (2 points).** Express the posterior as the selected Gaussian component plus the residual mixture and transfer the nonbest mass bound to total variation, using the task's normalization \(\|P-Q\|_{\mathrm{TV}}=\sup_B|P(B)-Q(B)|\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The probability guarantee is over the random coordinate set and the independent Gaussian noises. The posterior conclusions condition on both the known realized operator and the observation and hold deterministically whenever the gap condition holds. No independence among competitor failure events is needed for a union bound. A nonpositive stated probability lower bound is valid but uninformative, not a missing parameter assumption. Do not require extra restrictions on \(M\), \(\Delta\), or the noise levels beyond the public assumptions. Do not award full credit for proving only a weaker probability or gap statement.
