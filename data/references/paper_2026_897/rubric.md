# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes almost-sure consistency from a correct conditional squared-distance inequality and obtains root-n tightness. The inequality must retain or validly absorb the summable multiplicative growth term. A localization proof must use stopped-event moments and separately control the exit probability; it must not infer an unconditional bound on k E||theta_k-theta*||^2 from a localized estimate.
- **2 points:** Constructs the singular linear diffusion, verifies its SDE and generator, proves the zero-in-probability boundary condition, and establishes the uniqueness needed for identifying its law. Distinguishes fixed-driver pathwise uniqueness from uniqueness in law and handles positive-semidefinite, possibly singular or zero, Gamma.
- **3 points:** Derives the correctly scaled conditional drift and covariance and proves adequate large-jump control. Covariance convergence must be justified from the finite convex-loss structure and local square-integrable envelope, or by another valid derivation under the stated assumptions. The envelope alone does not assert continuity. A correct argument establishes almost-sure differentiability of the sample loss at theta*, convergence of its subgradients there, and dominated convergence. Jump control must give a vanishing tail bound, not merely an O(1/n) probability estimate; local Lindeberg is sufficient.
- **3 points:** Establishes positive-time interval tightness and limit identification with an applicable diffusion-approximation or alternative theorem, checking compact containment or an equivalent localization argument and handling polygonal interpolation. Extracts compatible limits, derives their zero boundary using root-n tightness, and concludes full-sequence compact-open convergence. The boundary argument must account for both interpolation endpoints and use an appropriate weak-convergence inequality. Uniqueness away from zero does not by itself determine the entrance law.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. Do not require the reference proof's notation, ordering, diagonal construction, or named standard theorems. Standard independent results may be invoked when their relevant hypotheses and conclusions are clear and applicable. A specialized convex M-estimation citation alone does not replace the needed covariance-continuity argument unless its relevant result and verified hypotheses are supplied.

Do not require global strong convexity, continuity of every stochastic gradient, an additional covariance-continuity assumption, moments above order two, invertibility of Gamma, or a global root-n second-moment bound. Do not award a completed proof for simply adding any of these assumptions. Almost-sure vanishing of the limiting process at zero is stronger than the task requires and is not necessary for full credit.

The separate Gaussian-supremum estimates in attached source records are not targets or required proof steps for this task. All theorem-critical obligations in the replacement reference proof are closed.
