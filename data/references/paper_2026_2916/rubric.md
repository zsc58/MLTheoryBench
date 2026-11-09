# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Prove a simultaneous, center-uniform single-task bound under the conditional-on-design noise model, valid for arbitrary outlier parameters and all taskwise minimizers, yielding the independent-task safety rate. Verify the concentration hypotheses and handle singular task covariances on their prediction-relevant spaces.
- **3 points:** Derive the pooled inlier error by separating heterogeneity and noise. Distinguish the centroid error from the error relative to each task parameter. Under an explicit sufficient tuning inequality, establish a uniform invariant neighborhood where all inlier regularized objectives equal their losses and their sum equals the pooled quadratic.
- **2 points:** Establish the local pooled curvature and convex outlier Lipschitz perturbation bound. Verify the perturbation-radius condition using |S^c|/m<=epsilon and |S|>=(1-epsilon)m. Obtain the sqrt(B) factor for pooled-seminorm displacement and the B factor after taskwise conversion, and justify that every full minimizing center remains in the invariant region.
- **2 points:** Convert the center and task seminorm estimates into squared in-sample MSE. Give a valid case split for the explicit tuning condition, combine with safety to obtain the minimum term, account for the contamination term, and justify the final placement of z outside the minimum. Cover epsilon=0, zero-rank covariances, and the fact that infinite balancedness invokes safety only.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's normalization or presentation. Naming whitening, concentration, or a perturbation lemma without giving the relevant result and verifying its hypotheses earns no credit for the corresponding achievement. Equivalent objective normalizations and universal-constant changes are acceptable.

Do not impose an equality between epsilon and the realized outlier fraction. Do not require an upper-side tuning assumption; no such hypothesis appears in the public task or the source's linear transfer proposition. A favorable-tuning invariant-region claim must be conditional on a verified threshold, not asserted for arbitrary delta.

A proof using a minimum with z inside it may receive full credit if it explicitly implies the public bound, for example by min{A,zU}<=z min{A,U} for z>=1. A concentration result written with max{1,log(1/alpha)} or log(e/alpha) is acceptable. The public z=log(16m/kappa) dominates either form up to universal constants.

The estimator is defined by an attained finite-dimensional convex minimum. A solver need not separately reprove attainment if using the minimizer as defined, but must not assume uniqueness of Euclidean null-space representatives or a positive lower eigenvalue for any individual covariance. All scored proof obligations have been closed in the replacement reference proof; there is no unresolved GT dependency.
