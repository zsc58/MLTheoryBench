# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly explain the restricted native-space order \(\widetilde s=s-(d-m)/2\) and the role of intrinsic fill distance in reconstruction. Distinguish the assumed H^1 reconstruction from an interpolation-based guarantee. A quantitative interpolation result must be stated with its applicable hypotheses and Sobolev-order range; the source's cited H^1 rate applies when \(\widetilde s>1\) and its spectral hypothesis holds. A precise qualitative explanation with these scope limitations is sufficient; reproducing an external interpolation proof is not required.
- **3 points:** Apply the restricted-kernel expansion and derive the triangle-inequality decomposition into reconstruction and section-training errors, using linearity of T rather than assuming linearity of the learned operator.
- **2 points:** Bound the reconstruction contribution by the H^1 operator norm of T times \(\varepsilon\).
- **2 points:** Bound the section contribution by \(\delta\sum_i|\alpha_i|\), combine the contributions, and give valid constant dependencies for the fixed expansion.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference notation or presentation. The public all-centers guarantee supplies the inequalities at the chosen nodes; using only those instances in the proof is correct.

Do not require the solver to derive the explicitly assumed reconstruction accuracy. Do not require a global strengthening to \(\widetilde s>1\), translation invariance, or a spectral decay condition. Those conditions may be introduced conditionally when explaining a particular interpolation theorem, but not silently imposed on the main extension bound. Conversely, claiming that the cited H^1 interpolation rate follows throughout the public smoothness range is incorrect. The given expansion need not be an interpolant.

Omission of the requested manifold/fill-distance discussion leaves that component incomplete, but does not invalidate a correct extension-error estimate. Award the algebraic components independently. An unsupported stronger assumption used to prove the main bound is a substantial gap; an explicit conditional discussion of interpolation is not.

Constants may depend on the chosen expansion. There is no assumed uniform bound on coefficient l1 norms across expansions or tolerances, and no automatic convergence claim should be inferred as both tolerances decrease while expansions change. Non-strict estimates cover zero coefficients, the zero function, and the zero target operator. Do not penalize omission of a separate zero-case discussion when the proof's inequalities already cover it.
