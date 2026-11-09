# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

The following allocation describes the reference route. Award equivalent credit for valid alternative arguments as specified below; these are not mandatory intermediate formulas for every proof.

- **3 points:** Correctly applies the chain rule to the diagonal product parameterization, derives the layer-square conservation law, and uses balanced positive initialization to obtain equality of corresponding layer coordinates.
- **3 points:** Derives the induced effective-weight dynamics \(\dot w_i=-Lw_i^{2-2/L}\partial_i\ell\) from the layer gradient flow.
- **2 points:** Establishes \(w^T\nabla\ell(w)=0\) on the Rayleigh-quotient domain, either from the explicit quotient-gradient calculation or a valid degree-zero homogeneity argument with hypotheses checked.
- **2 points:** Differentiates \(\sum_i w_i^{2/L}\), obtains \(-2w^T\nabla\ell\), and concludes the exact time-invariant quasi-norm, including the initial-value identity.

# Alternative-Route Credit

A proof may bypass the effective-weight dynamics entirely. For the direct layer-square route, award the first 3 points for establishing preservation of balance from the layer gradient flow; award the next 3 points for identifying \(\sum_i w_i^{2/L}=\sum_i(u_i^{(k)})^2\) for a fixed layer and deriving its time derivative as \(-2\sum_iw_i\partial_i\ell\); award 2 points for a valid orthogonality argument and the final 2 points for concluding conservation and the initial-value identity. This route earns full credit without any equation for \(\dot w_i\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or intermediate identities that the chosen proof route does not need. The trajectory must be handled on its stated positive admissible interval, globally for \(t\ge0\) under the setup. An unjustified effective-flow formula is a major gap when the proof relies on it, but omission of that formula is not a gap in an otherwise complete proof. Likewise, orthogonality or an equivalent cancellation must be justified wherever the argument requires it. Global existence, positivity, and denominator admissibility are assumptions of the task, not additional conclusions the solver must establish.
