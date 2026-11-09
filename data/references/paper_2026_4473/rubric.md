# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct core step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important obligations remain open.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Random transition estimate.** Establishes a high-probability norm lower bound for a fixed zero-sum vector independent of the current random transition matrix. Correctly handles sampling without replacement, conditional moments, and lower-tail concentration. Iterates by conditional independence and allocates failure probability over the required levels and pairs. A simultaneous lower singular-value bound on the whole zero-sum subspace is neither supplied nor required.
- **2 points — Conditional-label signal.** Uses the uniform root, doubly stochastic first-token transitions, uniform production probability, and unique parent to obtain the correct conditional-label vectors and simultaneous separation. Handles the empty product at level one and verifies the stated level-independent K_rho. Does not assume the separation that the random construction is supposed to prove.
- **4 points — Uniform single-layer learning and recursion.** Establishes feature control for all reachable representations, including a justified bounded region and correct bandwidth/error allocation; uses fresh stage samples and conditional counts; controls empirical label-feature cross-moment fluctuations rather than factoring empirical conditional expectations; proves ridge leakage, convergence with a valid step size, positive normalization, and uniform normalized accuracy. Shows that these conclusions restore token clusters and that the chosen accuracy schedule closes through all levels without a super-geometric statistical cost.
- **2 points — Resources and final recovery.** Sums actual stage sample counts to obtain the stated K_rho^(-2)m^L bound with only the allowed polynomial factors. Verifies polynomial feature width and iteration bounds, combines failure probabilities, and uses a strictly sub-1/2 final coordinate error and the one-hot root label to prove exact argmax recovery for a fresh example.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's particular constants, choice of ridge strength, safe gradient step size, or presentation.

The following are theorem-critical unless replaced by a valid alternative argument: the uniform root law; the first-patch conditioning convention; the permitted input-label-only information; conditional independence justified after fixing previously trained layers; fresh stage sampling; sufficient nonempty conditional counts; uniform control beyond the training points; an empirical cross-moment error bound; nonzero normalization; a valid depth recursion; and a strict final classification margin.

Population conditional independence does not imply exact factorization of empirical conditional moments. A proof using that identity without controlling its residual has not completed the regression step. Increasing the sample size by additional polynomial factors is allowed, but changing the inverse-square accuracy dependence in a way that destroys the claimed total sample bound is not.

Merely naming the source's random-matrix, single-layer, or chaining lemma does not complete a core step. Likewise, a named specialized method is not a substitute for the needed statement and verified hypotheses. Standard independent tools may be used when their relevant conclusions and applicability are clear. The public task does not provide the private proof's representation invariant, transition identities, error schedule, or intermediate estimates as assumptions.
