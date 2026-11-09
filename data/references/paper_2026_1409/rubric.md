# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines the CFN/DGN layer dynamics and proves that every hidden-state box \([-2,2]^{n_h^{(l)}}\), hence their product, is forward invariant under the bounded inputs.
- **3 points:** Derives the layerwise incremental inequality from the sigmoid/tanh Lipschitz bounds, explicitly includes recurrent-gate sensitivities, and obtains the stated \(\rho^{(l)}<1\) condition and valid comparison functions.
- **3 points:** Propagates the layer inequalities through depth using a lower-triangular nonnegative comparison matrix, proves Schur stability, and derives the KL decay and input-gain bounds for the deep CFN.
- **2 points:** Specializes to zero recurrent gate matrices, observes \(\rho^{(l)}=\bar\sigma_f^{(l)}<1\), and concludes unconditional delta-ISS of the deep DGN.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof must establish the contraction and depth-composition arguments; merely naming ISS, contraction, or a comparison theorem earns no credit for those steps. Deduct for treating the layer condition or DGN conclusion as assumptions.
