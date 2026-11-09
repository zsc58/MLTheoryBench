# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (1 point):** Establishes the needed well-definedness: positivity of Q and its diagonal, existence and uniqueness of positive mtilde, and bounded positive deterministic normalization. A coordinatewise KKT derivation of Ahat=I-Q[diag(Q)]^(-1) is a valid structural step, but is not mandatory in an alternative proof that works directly with the matrix defined in the task.
- **Step 2 (2 points):** Justifies replacement of the random diagonal normalization under the actual finite-moment assumptions and shows its effect on the normalized resolvent trace is negligible. Either a valid uniform-diagonal argument with adequate quantitative estimates or the reference proof's averaged-diagonal and normalized-trace-norm argument is acceptable. Pointwise diagonal convergence followed by an unsupported union bound is not sufficient. Do not require operator-norm normalization convergence when a weaker sufficient estimate is proved.
- **Step 3 (4 points):** Establishes the dependent-resolvent deterministic equivalent and scalar closure with controlled errors, and proves existence and uniqueness of the specified chi. In the reference route this includes a correct block or lower-block inverse representation, correctly signed and scaled row-deleted identities, conditional quadratic-form variance, trace concentration, a tested expectation equation, and stability of the dimension-dependent approximate fixed point. Merely naming leave-one-out, concentration, or a specialized deterministic-equivalent method does not complete this step. The case Sigma=0 must be included or handled automatically by the stated scalar specification.
- **Step 4 (3 points):** Obtains exactly Gcal, proves the normalized-trace convergence in probability for every fixed upper-half-plane z, and justifies the probability-measure and subsequential spectral interpretation. Do not infer stability solely from uniqueness, or probability-measure convergence solely from a formal substitution into the scalar equation.

# Evaluator Notes

Accept a complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental linearization or notation. A standard independent theorem may be used when its relevant conclusion is stated and its hypotheses are verified; a paper-specific closure cannot be discharged merely by naming it.

The ordinary sample-covariance bilinear deterministic equivalent at fixed positive ridge is accepted background. Its pointwise conclusion alone does not supply a maximum-coordinate rate. Gaussian concentration cannot be imposed on the public finite-moment experiment, and the Gaussian-specific support lemma cannot silently strengthen the public assumptions.

A gap in fixed-point closure, branch uniqueness, approximate-fixed-point stability, or transfer of the random normalization is theorem-critical. Award downstream spectral credit only to the extent it is independently justified. No limiting spectral distribution of Sigma, covariance lower bound, Gaussian design, or restriction alpha>1 is required. The source-local inverse/sign/scaling mistakes are corrected in the reference proof and are not part of the solver's required conclusion.

All reference-proof obligations are closed; there is no unresolved private GT warning.
